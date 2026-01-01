#!/usr/bin/env python3
"""
LINK WHO AM I IMAGES TO ADAPTIVE QUIZ TOPICS
=============================================
Links existing mathematician images to the adaptive quiz topics
so they appear during adaptive quiz sessions.

The Who Am I system uses:
- who_am_i_images: Main table with image details and difficulty
- who_am_i_image_topics: Junction table linking images to topics

This script:
1. Shows current image/topic configuration
2. Links all active images to adaptive topics
3. Creates 'adaptive' difficulty copies or updates existing
"""

import sqlite3

DB_PATH = 'instance/mathquiz.db'

# Adaptive quiz topics
ADAPTIVE_TOPICS = ['fractions', 'percentages', 'probability', 'sets']


def show_current_config():
    """Show current Who Am I configuration"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("="*60)
    print("CURRENT WHO AM I CONFIGURATION")
    print("="*60)
    
    # Count images
    cursor.execute("SELECT COUNT(*) FROM who_am_i_images WHERE active = 1")
    total_active = cursor.fetchone()[0]
    print(f"\nTotal active images: {total_active}")
    
    # Show by difficulty
    cursor.execute("""
        SELECT difficulty, COUNT(*) 
        FROM who_am_i_images 
        WHERE active = 1 
        GROUP BY difficulty
    """)
    print("\nBy difficulty:")
    for diff, count in cursor.fetchall():
        print(f"  {diff}: {count}")
    
    # Show topics in junction table
    cursor.execute("""
        SELECT t.topic, COUNT(DISTINCT t.image_id)
        FROM who_am_i_image_topics t
        JOIN who_am_i_images i ON t.image_id = i.id
        WHERE i.active = 1
        GROUP BY t.topic
    """)
    print("\nTopics with images:")
    for topic, count in cursor.fetchall():
        print(f"  {topic}: {count} images")
    
    # Check adaptive topics
    print("\nAdaptive topic coverage:")
    for topic in ADAPTIVE_TOPICS:
        cursor.execute("""
            SELECT COUNT(DISTINCT t.image_id)
            FROM who_am_i_image_topics t
            JOIN who_am_i_images i ON t.image_id = i.id
            WHERE t.topic = ? AND i.active = 1
        """, (topic,))
        count = cursor.fetchone()[0]
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {topic}: {count} images")
    
    conn.close()
    return total_active


def link_images_to_adaptive_topics():
    """Link all active images to adaptive quiz topics"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("LINKING IMAGES TO ADAPTIVE TOPICS")
    print("="*60)
    
    # Get all active image IDs
    cursor.execute("SELECT id, answer FROM who_am_i_images WHERE active = 1")
    images = cursor.fetchall()
    
    if not images:
        print("❌ No active images found!")
        conn.close()
        return
    
    print(f"\nFound {len(images)} active images to link")
    
    # Link each image to all adaptive topics
    linked_count = 0
    for image_id, answer in images:
        for topic in ADAPTIVE_TOPICS:
            try:
                cursor.execute("""
                    INSERT OR IGNORE INTO who_am_i_image_topics (image_id, topic)
                    VALUES (?, ?)
                """, (image_id, topic))
                if cursor.rowcount > 0:
                    linked_count += 1
            except Exception as e:
                print(f"  Error linking image {image_id} to {topic}: {e}")
    
    conn.commit()
    print(f"\n✅ Created {linked_count} new topic links")
    
    # Now we need to handle the difficulty issue
    # The query looks for i.difficulty = 'adaptive'
    # We need to either:
    # Option A: Update some images to have difficulty = 'adaptive'
    # Option B: Modify the API query to not filter by difficulty for adaptive
    
    # Let's check what difficulties exist
    cursor.execute("SELECT DISTINCT difficulty FROM who_am_i_images WHERE active = 1")
    difficulties = [row[0] for row in cursor.fetchall()]
    print(f"\nExisting difficulties: {difficulties}")
    
    if 'adaptive' not in difficulties:
        print("\n⚠️  No images have difficulty='adaptive'")
        print("   The adaptive quiz looks for images with difficulty='adaptive'")
        print("\n   Options:")
        print("   1. Run with --set-adaptive to set all images to 'adaptive' difficulty")
        print("   2. Modify the API to accept any difficulty for adaptive quizzes")
    
    conn.close()


def set_images_to_adaptive_difficulty():
    """Set all active images to 'adaptive' difficulty"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("SETTING IMAGES TO ADAPTIVE DIFFICULTY")
    print("="*60)
    
    # First, let's see what we have
    cursor.execute("""
        SELECT id, answer, difficulty 
        FROM who_am_i_images 
        WHERE active = 1
    """)
    images = cursor.fetchall()
    
    print(f"\nFound {len(images)} active images")
    
    # Update all to 'adaptive' difficulty
    cursor.execute("""
        UPDATE who_am_i_images 
        SET difficulty = 'adaptive'
        WHERE active = 1
    """)
    updated = cursor.rowcount
    
    conn.commit()
    conn.close()
    
    print(f"✅ Updated {updated} images to difficulty='adaptive'")


def create_adaptive_copies():
    """Create copies of images with 'adaptive' difficulty (preserves originals)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("CREATING ADAPTIVE COPIES OF IMAGES")
    print("="*60)
    
    # Get all active non-adaptive images
    cursor.execute("""
        SELECT id, topic, image_filename, answer, hint 
        FROM who_am_i_images 
        WHERE active = 1 AND difficulty != 'adaptive'
    """)
    images = cursor.fetchall()
    
    if not images:
        print("No images to copy (all may already be adaptive)")
        conn.close()
        return
    
    print(f"\nCreating adaptive copies for {len(images)} images...")
    
    created = 0
    for orig_id, topic, filename, answer, hint in images:
        # Check if adaptive version already exists
        cursor.execute("""
            SELECT id FROM who_am_i_images 
            WHERE image_filename = ? AND difficulty = 'adaptive'
        """, (filename,))
        
        if cursor.fetchone():
            continue  # Already has adaptive version
        
        # Create adaptive copy
        cursor.execute("""
            INSERT INTO who_am_i_images (topic, difficulty, image_filename, answer, hint, active)
            VALUES (?, 'adaptive', ?, ?, ?, 1)
        """, (topic, filename, answer, hint))
        
        new_id = cursor.lastrowid
        
        # Link to all adaptive topics
        for adaptive_topic in ADAPTIVE_TOPICS:
            cursor.execute("""
                INSERT OR IGNORE INTO who_am_i_image_topics (image_id, topic)
                VALUES (?, ?)
            """, (new_id, adaptive_topic))
        
        created += 1
    
    conn.commit()
    conn.close()
    
    print(f"✅ Created {created} adaptive copies")


def verify_setup():
    """Verify the setup is correct"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("VERIFICATION")
    print("="*60)
    
    # Check adaptive images exist
    cursor.execute("""
        SELECT COUNT(*) FROM who_am_i_images 
        WHERE active = 1 AND difficulty = 'adaptive'
    """)
    adaptive_count = cursor.fetchone()[0]
    
    print(f"\nAdaptive difficulty images: {adaptive_count}")
    
    # Check each topic
    print("\nImages available per adaptive topic:")
    all_good = True
    for topic in ADAPTIVE_TOPICS:
        cursor.execute("""
            SELECT COUNT(DISTINCT i.id)
            FROM who_am_i_images i
            JOIN who_am_i_image_topics t ON i.id = t.image_id
            WHERE t.topic = ? AND i.difficulty = 'adaptive' AND i.active = 1
        """, (topic,))
        count = cursor.fetchone()[0]
        status = "✅" if count > 0 else "❌"
        if count == 0:
            all_good = False
        print(f"  {status} {topic}: {count} images")
    
    conn.close()
    
    if all_good:
        print("\n✅ Setup complete! Who Am I should work for all adaptive topics.")
    else:
        print("\n⚠️  Some topics still have no images. Run with --copy or --set-adaptive")
    
    return all_good


def main():
    import sys
    
    print("="*60)
    print("WHO AM I - ADAPTIVE QUIZ LINKER")
    print("="*60)
    
    if '--help' in sys.argv:
        print("""
Usage: python link_whoami_adaptive.py [options]

Options:
  (no args)      Show current configuration
  --link         Link existing images to adaptive topics
  --set-adaptive Change all active images to 'adaptive' difficulty
  --copy         Create copies with 'adaptive' difficulty (preserves originals)
  --full         Do everything: link + set-adaptive
  --verify       Check if setup is correct

Recommended for quick setup:
  python link_whoami_adaptive.py --full
""")
        return
    
    # Show current state
    total = show_current_config()
    
    if total == 0:
        print("\n❌ No Who Am I images found in database!")
        return
    
    if '--link' in sys.argv or '--full' in sys.argv:
        link_images_to_adaptive_topics()
    
    if '--set-adaptive' in sys.argv or '--full' in sys.argv:
        set_images_to_adaptive_difficulty()
    
    if '--copy' in sys.argv:
        create_adaptive_copies()
    
    if '--verify' in sys.argv or '--full' in sys.argv or '--link' in sys.argv:
        verify_setup()
    
    if len(sys.argv) == 1:
        print("\n" + "-"*60)
        print("To link images to adaptive quiz, run:")
        print("  python link_whoami_adaptive.py --full")
        print("-"*60)


if __name__ == '__main__':
    main()
