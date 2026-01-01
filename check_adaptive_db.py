#!/usr/bin/env python3
"""
Diagnostic Script: Check Adaptive Questions Database
=====================================================
Run this to diagnose issues with the adaptive quiz questions.
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
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            print(f"✅ Found database at: {path}")
            return path
    
    print("❌ Database not found!")
    print("Checked paths:")
    for path in POSSIBLE_PATHS:
        print(f"  - {path}")
    exit(1)

def diagnose():
    db_path = find_db()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("\n" + "=" * 60)
    print("ADAPTIVE QUESTIONS DIAGNOSTIC")
    print("=" * 60)
    
    # 1. Check if table exists
    print("\n1. Checking if questions_adaptive table exists...")
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='questions_adaptive'
    """)
    if cursor.fetchone():
        print("   ✅ Table exists")
    else:
        print("   ❌ Table does NOT exist!")
        print("\n   Run the migration script first:")
        print("   python3 migrate_levels_11_12.py")
        conn.close()
        return
    
    # 2. Check table schema
    print("\n2. Table schema:")
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = cursor.fetchall()
    for col in columns:
        print(f"   - {col[1]} ({col[2]})")
    
    # 3. Count total questions
    print("\n3. Total question count:")
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive")
    total = cursor.fetchone()[0]
    print(f"   Total: {total} questions")
    
    if total == 0:
        print("\n   ⚠️ No questions in database!")
        print("   Run a question generator first:")
        print("   python3 generate_fractions_skill_based.py")
        conn.close()
        return
    
    # 4. Count by topic
    print("\n4. Questions by topic:")
    cursor.execute("""
        SELECT topic, COUNT(*) 
        FROM questions_adaptive 
        GROUP BY topic
    """)
    for row in cursor.fetchall():
        print(f"   - {row[0]}: {row[1]} questions")
    
    # 5. Count by level for fractions
    print("\n5. Fractions questions by level:")
    cursor.execute("""
        SELECT difficulty_level, difficulty_band, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions'
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    """)
    results = cursor.fetchall()
    
    if not results:
        print("   ⚠️ No fractions questions found!")
    else:
        for row in results:
            print(f"   Level {row[0]:2d} ({row[1]:15s}): {row[2]:3d} questions")
    
    # 6. Sample question from level 1
    print("\n6. Sample question from Level 1:")
    cursor.execute("""
        SELECT id, question_text, option_a, option_b, option_c, option_d, correct_answer
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND difficulty_level = 1
        LIMIT 1
    """)
    sample = cursor.fetchone()
    
    if sample:
        print(f"   ID: {sample[0]}")
        print(f"   Question: {sample[1][:60]}...")
        print(f"   Option A: {sample[2]}")
        print(f"   Option B: {sample[3]}")
        print(f"   Option C: {sample[4]}")
        print(f"   Option D: {sample[5]}")
        print(f"   Correct: {sample[6]}")
    else:
        print("   ⚠️ No Level 1 fractions questions!")
    
    # 7. Check for NULL values
    print("\n7. Checking for NULL/empty values:")
    cursor.execute("""
        SELECT COUNT(*) FROM questions_adaptive 
        WHERE topic = 'fractions' 
        AND (question_text IS NULL OR question_text = '' 
             OR option_a IS NULL OR option_a = '')
    """)
    null_count = cursor.fetchone()[0]
    if null_count > 0:
        print(f"   ⚠️ Found {null_count} questions with NULL/empty fields!")
    else:
        print("   ✅ All questions have valid data")
    
    # 8. Check is_active
    print("\n8. Active vs inactive questions:")
    cursor.execute("""
        SELECT is_active, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions'
        GROUP BY is_active
    """)
    for row in cursor.fetchall():
        status = "Active" if row[0] == 1 else "Inactive"
        print(f"   {status}: {row[1]} questions")
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("DIAGNOSTIC COMPLETE")
    print("=" * 60)

if __name__ == '__main__':
    diagnose()
