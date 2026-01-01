#!/usr/bin/env python3
"""
Database Migration: Add Levels 11-12 Support
============================================
- Creates questions_adaptive table if it doesn't exist (with 1-12 support)
- Or updates existing table to support Levels 11-12
- Level 11: Application (real-life word problems)
- Level 12: Linked Topics (cross-topic integration)

Run: python3 migrate_levels_11_12.py
"""

import sqlite3
import os

# Check multiple possible database locations
POSSIBLE_PATHS = [
    'mathapp.db',
    'instance/mathquiz.db',
    'mathquiz.db',
]

def find_db():
    """Find the database file"""
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            print(f"Found database at: {path}")
            return path
    
    print("ERROR: Database not found!")
    print("Checked paths:")
    for path in POSSIBLE_PATHS:
        print(f"  - {path}")
    print("\nMake sure you're running from your mathappR12 directory")
    exit(1)

def get_db():
    db_path = find_db()
    return sqlite3.connect(db_path)


def table_exists(cursor, table_name):
    """Check if a table exists"""
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name=?
    """, (table_name,))
    return cursor.fetchone() is not None


def create_questions_adaptive_table(cursor):
    """Create the questions_adaptive table with Level 1-12 support"""
    print("\n   Creating questions_adaptive table (with Level 1-12 support)...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions_adaptive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            
            -- Core question data
            topic VARCHAR(50) NOT NULL,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer INTEGER NOT NULL,
            explanation TEXT NOT NULL DEFAULT '',
            
            -- Enhanced difficulty system (1-12 scale)
            difficulty_level INTEGER NOT NULL CHECK(difficulty_level BETWEEN 1 AND 12),
            difficulty_band VARCHAR(20) NOT NULL DEFAULT 'beginner',
            
            -- Complexity metadata (JSON)
            complexity_factors TEXT,
            
            -- Learning metadata
            estimated_time_seconds INTEGER DEFAULT 30,
            hint_text TEXT,
            hint_penalty INTEGER DEFAULT 50,
            
            -- Question type classification
            question_type VARCHAR(50),
            
            -- Tracking
            times_shown INTEGER DEFAULT 0,
            times_correct INTEGER DEFAULT 0,
            avg_response_time REAL,
            
            -- Metadata
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1,
            
            -- Visual content
            image_svg TEXT,
            
            -- Level 12: Linked topics (comma-separated topic IDs)
            linked_topics TEXT DEFAULT NULL,
            
            -- Prevent exact duplicates
            UNIQUE(topic, difficulty_level, question_text)
        )
    """)
    
    # Create indexes
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_questions_adaptive_topic 
        ON questions_adaptive(topic, difficulty_level, is_active)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_questions_adaptive_band 
        ON questions_adaptive(topic, difficulty_band, is_active)
    """)
    
    print("   ✓ questions_adaptive table created with Level 1-12 support")


def migrate():
    conn = get_db()
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Migration: Adding Levels 11-12 Support")
    print("=" * 60)
    
    # Step 1: Check if table exists
    print("\n1. Checking if questions_adaptive table exists...")
    
    if not table_exists(cursor, 'questions_adaptive'):
        print("   Table does not exist - creating it now...")
        create_questions_adaptive_table(cursor)
        conn.commit()
        
        print("\n" + "=" * 60)
        print("Table Created Successfully!")
        print("=" * 60)
        print("""
The questions_adaptive table has been created with Level 1-12 support.

Next steps:
1. Run your question generator script to populate questions
   python3 generate_adaptive_questions.py

2. The table supports:
   - Levels 1-10: Standard progression
   - Level 11: Application (real-life word problems)
   - Level 12: Linked Topics (cross-topic integration)
""")
        conn.close()
        return
    
    print("   ✓ Table exists")
    
    # Step 2: Check current schema
    print("\n2. Checking current schema...")
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    print(f"   Current columns: {list(columns.keys())}")
    
    # Step 3: Add linked_topics column if not exists
    if 'linked_topics' not in columns:
        print("\n3. Adding 'linked_topics' column...")
        cursor.execute("""
            ALTER TABLE questions_adaptive 
            ADD COLUMN linked_topics TEXT DEFAULT NULL
        """)
        print("   ✓ linked_topics column added")
    else:
        print("\n3. 'linked_topics' column already exists ✓")
    
    # Step 4: Check if we need to update the CHECK constraint for levels > 10
    print("\n4. Checking difficulty_level constraint...")
    
    # Test if we can insert level 11
    try:
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, question_text, option_a, option_b, option_c, option_d, 
             correct_answer, explanation, difficulty_level, difficulty_band, is_active)
            VALUES ('_test_', '_test_', 'A', 'B', 'C', 'D', 0, '', 11, 'application', 0)
        """)
        # If successful, delete the test row
        cursor.execute("DELETE FROM questions_adaptive WHERE topic = '_test_'")
        print("   ✓ Levels 11-12 already supported")
    except sqlite3.IntegrityError as e:
        if "CHECK constraint" in str(e):
            print("   ⚠ CHECK constraint blocking levels > 10")
            print("   Rebuilding table to support levels 1-12...")
            
            # Get current data
            cursor.execute("SELECT COUNT(*) FROM questions_adaptive")
            row_count = cursor.fetchone()[0]
            print(f"   Found {row_count} existing questions to migrate")
            
            # Create new table without the restrictive CHECK constraint
            cursor.execute("""
                CREATE TABLE questions_adaptive_new (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    topic VARCHAR(50) NOT NULL,
                    question_text TEXT NOT NULL,
                    option_a TEXT NOT NULL,
                    option_b TEXT NOT NULL,
                    option_c TEXT NOT NULL,
                    option_d TEXT NOT NULL,
                    correct_answer INTEGER NOT NULL,
                    explanation TEXT NOT NULL DEFAULT '',
                    difficulty_level INTEGER NOT NULL CHECK(difficulty_level BETWEEN 1 AND 12),
                    difficulty_band VARCHAR(20) NOT NULL DEFAULT 'beginner',
                    complexity_factors TEXT,
                    estimated_time_seconds INTEGER DEFAULT 30,
                    hint_text TEXT,
                    hint_penalty INTEGER DEFAULT 50,
                    question_type VARCHAR(50),
                    times_shown INTEGER DEFAULT 0,
                    times_correct INTEGER DEFAULT 0,
                    avg_response_time REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT 1,
                    image_svg TEXT,
                    linked_topics TEXT DEFAULT NULL,
                    UNIQUE(topic, difficulty_level, question_text)
                )
            """)
            
            # Copy data - handle both schemas (with and without linked_topics)
            if 'linked_topics' in columns:
                cursor.execute("""
                    INSERT INTO questions_adaptive_new 
                    SELECT * FROM questions_adaptive
                """)
            else:
                # Build column list from existing columns
                existing_cols = list(columns.keys())
                col_list = ', '.join(existing_cols)
                cursor.execute(f"""
                    INSERT INTO questions_adaptive_new ({col_list}, linked_topics)
                    SELECT {col_list}, NULL FROM questions_adaptive
                """)
            
            # Get count
            cursor.execute("SELECT COUNT(*) FROM questions_adaptive_new")
            count = cursor.fetchone()[0]
            print(f"   Copied {count} questions to new table")
            
            # Drop old table and rename new
            cursor.execute("DROP TABLE questions_adaptive")
            cursor.execute("ALTER TABLE questions_adaptive_new RENAME TO questions_adaptive")
            
            # Recreate indexes
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_questions_adaptive_topic 
                ON questions_adaptive(topic, difficulty_level, is_active)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_questions_adaptive_band 
                ON questions_adaptive(topic, difficulty_band, is_active)
            """)
            
            print("   ✓ Table rebuilt with levels 1-12 support")
        else:
            raise e
    
    conn.commit()
    
    # Step 5: Verify the migration
    print("\n5. Verifying migration...")
    
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = [row[1] for row in cursor.fetchall()]
    
    required = ['linked_topics', 'difficulty_level', 'difficulty_band']
    for col in required:
        if col in columns:
            print(f"   ✓ {col} column present")
        else:
            print(f"   ✗ {col} column MISSING!")
    
    # Test level 11 insert
    try:
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, question_text, option_a, option_b, option_c, option_d, 
             correct_answer, explanation, difficulty_level, difficulty_band, is_active)
            VALUES ('_test_', '_test_11_', 'A', 'B', 'C', 'D', 0, '', 11, 'application', 0)
        """)
        cursor.execute("DELETE FROM questions_adaptive WHERE topic = '_test_'")
        print("   ✓ Level 11 insert test passed")
    except Exception as e:
        print(f"   ✗ Level 11 insert failed: {e}")
    
    # Test level 12 with linked_topics
    try:
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, question_text, option_a, option_b, option_c, option_d, 
             correct_answer, explanation, difficulty_level, difficulty_band, 
             linked_topics, is_active)
            VALUES ('_test_', '_test_12_', 'A', 'B', 'C', 'D', 0, '', 12, 'linked', 
                    'percentages,decimals', 0)
        """)
        cursor.execute("DELETE FROM questions_adaptive WHERE topic = '_test_'")
        print("   ✓ Level 12 with linked_topics test passed")
    except Exception as e:
        print(f"   ✗ Level 12 insert failed: {e}")
    
    conn.commit()
    conn.close()
    
    # Step 6: Summary
    print("\n" + "=" * 60)
    print("Migration Complete!")
    print("=" * 60)
    print("""
New Difficulty Levels:
  Level 1-3:   beginner
  Level 4-6:   intermediate  
  Level 7-9:   advanced
  Level 10:    mastery
  Level 11:    application    (NEW - real-life word problems)
  Level 12:    linked         (NEW - cross-topic integration)

New Column:
  linked_topics  TEXT    Comma-separated list of linked topic IDs
                         e.g., 'percentages,decimals' for a fractions question
                         
Usage in generators:
  {
      'level': 12,
      'band': 'linked',
      'linked_topics': 'percentages,probability'
  }
""")

if __name__ == '__main__':
    migrate()
