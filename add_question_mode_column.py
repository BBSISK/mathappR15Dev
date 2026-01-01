"""
Database Migration: Add 'mode' column to questions_adaptive table
This allows questions to be tagged as 'practice' or 'jc_exam'
Run once on PythonAnywhere: python add_question_mode_column.py
"""

import sqlite3
import os

# Database path - adjust if needed
DB_PATH = 'instance/mathquiz.db'

def add_mode_column():
    """Add mode column to questions_adaptive table"""
    
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Check if column already exists
        cursor.execute("PRAGMA table_info(questions_adaptive)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'mode' in columns:
            print("✅ 'mode' column already exists in questions_adaptive")
        else:
            # Add the mode column with default value 'practice'
            cursor.execute("""
                ALTER TABLE questions_adaptive 
                ADD COLUMN mode VARCHAR(20) DEFAULT 'practice'
            """)
            print("✅ Added 'mode' column to questions_adaptive")
        
        # Update any NULL values to 'practice'
        cursor.execute("""
            UPDATE questions_adaptive 
            SET mode = 'practice' 
            WHERE mode IS NULL
        """)
        updated = cursor.rowcount
        if updated > 0:
            print(f"✅ Updated {updated} existing questions to mode='practice'")
        
        conn.commit()
        
        # Verify
        cursor.execute("""
            SELECT mode, COUNT(*) 
            FROM questions_adaptive 
            GROUP BY mode
        """)
        results = cursor.fetchall()
        print("\n📊 Questions by mode:")
        for mode, count in results:
            print(f"   {mode or 'NULL'}: {count}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    print("=" * 50)
    print("Adding 'mode' column to questions_adaptive")
    print("=" * 50)
    add_mode_column()
    print("\n✅ Migration complete!")
