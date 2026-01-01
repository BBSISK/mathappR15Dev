#!/usr/bin/env python3
"""
ADAPTIVE QUIZ DATABASE SETUP
=============================
Creates the tables needed for the adaptive quiz system:
1. questions_adaptive - Questions with difficulty levels 1-10 and SVG support
2. adaptive_progress - Tracks user progress per topic

Run this script once to set up the tables:
    python setup_adaptive_tables.py

"""

import sqlite3
import os

DB_PATH = 'instance/mathquiz.db'


def setup_tables():
    """Create the adaptive quiz tables if they don't exist."""
    
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        print("   Make sure you're running this from the mathapp-main directory")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Create questions_adaptive table
    print("\n📊 Setting up questions_adaptive table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions_adaptive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            explanation TEXT,
            difficulty_level INTEGER NOT NULL DEFAULT 5,
            difficulty_band TEXT NOT NULL DEFAULT 'intermediate',
            question_type TEXT DEFAULT 'text',
            image_svg TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Check if image_svg column exists, add if not
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = [row[1] for row in cursor.fetchall()]
    if 'image_svg' not in columns:
        cursor.execute("ALTER TABLE questions_adaptive ADD COLUMN image_svg TEXT")
        print("   ✓ Added image_svg column")
    
    # Create indexes for faster queries
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_adaptive_topic_level 
        ON questions_adaptive(topic, difficulty_level)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_adaptive_topic_band 
        ON questions_adaptive(topic, difficulty_band)
    """)
    print("   ✓ questions_adaptive table ready")
    
    # 2. Create adaptive_progress table
    print("\n📈 Setting up adaptive_progress table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS adaptive_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            topic TEXT NOT NULL,
            current_level INTEGER DEFAULT 1,
            current_points INTEGER DEFAULT 0,
            total_questions INTEGER DEFAULT 0,
            correct_answers INTEGER DEFAULT 0,
            highest_level_reached INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, topic),
            UNIQUE(guest_code, topic)
        )
    """)
    
    # Create indexes
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_progress_user 
        ON adaptive_progress(user_id, topic)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_progress_guest 
        ON adaptive_progress(guest_code, topic)
    """)
    print("   ✓ adaptive_progress table ready")
    
    conn.commit()
    
    # 3. Show current question counts
    print("\n📋 Current adaptive questions:")
    cursor.execute("""
        SELECT topic, difficulty_band, COUNT(*) as count
        FROM questions_adaptive
        WHERE is_active = 1
        GROUP BY topic, difficulty_band
        ORDER BY topic, difficulty_band
    """)
    rows = cursor.fetchall()
    
    if rows:
        current_topic = None
        for topic, band, count in rows:
            if topic != current_topic:
                print(f"\n   {topic}:")
                current_topic = topic
            print(f"      {band}: {count} questions")
    else:
        print("   No questions yet. Run the question generators to add questions.")
    
    conn.close()
    
    print("\n✅ Adaptive quiz tables set up successfully!")
    print("\nNext steps:")
    print("1. Run question_generator_visual.py to add visual questions")
    print("2. Run question_generator_templates.py to add text questions")
    print("3. Deploy app.py and student_app.html")
    
    return True


def show_stats():
    """Show statistics about adaptive questions."""
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n" + "="*50)
    print("ADAPTIVE QUESTIONS STATISTICS")
    print("="*50)
    
    # Overall counts
    cursor.execute("""
        SELECT COUNT(*) as total,
               SUM(CASE WHEN image_svg IS NOT NULL THEN 1 ELSE 0 END) as visual,
               SUM(CASE WHEN image_svg IS NULL THEN 1 ELSE 0 END) as text_only
        FROM questions_adaptive
        WHERE is_active = 1
    """)
    total, visual, text_only = cursor.fetchone()
    
    print(f"\nTotal questions: {total}")
    if total > 0:
        visual_pct = (visual / total) * 100
        print(f"  Visual: {visual} ({visual_pct:.1f}%)")
        print(f"  Text:   {text_only} ({100-visual_pct:.1f}%)")
        
        if visual_pct < 75:
            print(f"\n⚠️  Target is 75% visual - need {int(total * 0.75) - visual} more visual questions")
        else:
            print(f"\n✅ Visual target met!")
    
    # By topic
    print("\n--- By Topic ---")
    cursor.execute("""
        SELECT topic,
               COUNT(*) as total,
               SUM(CASE WHEN image_svg IS NOT NULL THEN 1 ELSE 0 END) as visual
        FROM questions_adaptive
        WHERE is_active = 1
        GROUP BY topic
        ORDER BY topic
    """)
    for topic, total, visual in cursor.fetchall():
        pct = (visual / total * 100) if total > 0 else 0
        status = "✅" if pct >= 75 else "⚠️"
        print(f"  {topic}: {total} total, {visual} visual ({pct:.0f}%) {status}")
    
    # By level
    print("\n--- By Level ---")
    cursor.execute("""
        SELECT difficulty_level, COUNT(*) as count
        FROM questions_adaptive
        WHERE is_active = 1
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    """)
    for level, count in cursor.fetchall():
        bar = "█" * min(count // 2, 20)
        print(f"  Level {level:2d}: {bar} {count}")
    
    conn.close()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'stats':
        show_stats()
    else:
        setup_tables()
        show_stats()
