#!/usr/bin/env python3
"""
FIX SETS QUESTIONS - Convert to Irish Notation
==============================================
Changes:
  n(A) → #(A)
  A - B → A\B
  A only (A - B) → A\B (A without B)
  B only (B - A) → B\A (B without A)
"""

import sqlite3

DB_PATH = 'instance/mathquiz.db'

def fix_notation():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check how many sets questions exist
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE topic='sets'")
    count = cursor.fetchone()[0]
    
    if count == 0:
        print("No existing 'sets' questions found.")
        print("Run generate_sets_questions.py to create new questions with correct notation.")
        conn.close()
        return
    
    print(f"Found {count} existing 'sets' questions")
    print("\nApplying Irish notation fixes...")
    
    # Replacements to make in question_text
    question_replacements = [
        ('n(A)', '#(A)'),
        ('n(B)', '#(B)'),
        ('n(C)', '#(C)'),
        ('n(P)', '#(P)'),
        ('n(Q)', '#(Q)'),
        ('n(X)', '#(X)'),
        ('n(Y)', '#(Y)'),
        ('n(M)', '#(M)'),
        ('n(N)', '#(N)'),
        ('n(U)', '#(U)'),
        ("n(A')", "#(A')"),
        ('A - B', 'A\\B'),
        ('B - A', 'B\\A'),
        ('A only (A - B)', 'A\\B (A without B)'),
        ('B only (B - A)', 'B\\A (B without A)'),
        ('A minus B', 'A without B'),
    ]
    
    # Replacements for options
    option_replacements = [
        ('A only (A - B)', 'A\\B (A without B)'),
        ('B only (B - A)', 'B\\A (B without A)'),
        ('A - B', 'A\\B'),
        ('B - A', 'B\\A'),
        ('A minus B', 'A\\B'),
    ]
    
    total_updated = 0
    
    # Fix question_text
    for old, new in question_replacements:
        cursor.execute("""
            UPDATE questions_adaptive 
            SET question_text = REPLACE(question_text, ?, ?)
            WHERE topic = 'sets' AND question_text LIKE ?
        """, (old, new, f'%{old}%'))
        if cursor.rowcount > 0:
            print(f"  Fixed {cursor.rowcount} questions: '{old}' → '{new}'")
            total_updated += cursor.rowcount
    
    # Fix options (A, B, C, D)
    for option_col in ['option_a', 'option_b', 'option_c', 'option_d']:
        for old, new in option_replacements:
            cursor.execute(f"""
                UPDATE questions_adaptive 
                SET {option_col} = REPLACE({option_col}, ?, ?)
                WHERE topic = 'sets' AND {option_col} LIKE ?
            """, (old, new, f'%{old}%'))
            if cursor.rowcount > 0:
                print(f"  Fixed {cursor.rowcount} in {option_col}: '{old}' → '{new}'")
                total_updated += cursor.rowcount
    
    conn.commit()
    
    # Verify the changes
    print("\n" + "="*50)
    print("VERIFICATION")
    print("="*50)
    
    # Check for any remaining old notation
    cursor.execute("""
        SELECT COUNT(*) FROM questions_adaptive 
        WHERE topic='sets' AND (
            question_text LIKE '%n(A)%' OR
            question_text LIKE '%n(B)%' OR
            question_text LIKE '% - B)%' OR
            question_text LIKE '%A only%'
        )
    """)
    remaining = cursor.fetchone()[0]
    
    if remaining == 0:
        print("✅ All questions now use Irish notation!")
    else:
        print(f"⚠️  {remaining} questions may still have old notation")
        cursor.execute("""
            SELECT question_text FROM questions_adaptive 
            WHERE topic='sets' AND (
                question_text LIKE '%n(A)%' OR
                question_text LIKE '%n(B)%'
            ) LIMIT 3
        """)
        for row in cursor.fetchall():
            print(f"   - {row[0][:80]}...")
    
    # Show sample of fixed questions
    print("\n📋 Sample questions with Irish notation:")
    cursor.execute("""
        SELECT question_text FROM questions_adaptive 
        WHERE topic='sets' AND question_text LIKE '%#(%'
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(f"   ✓ {row[0][:70]}...")
    
    conn.close()
    print(f"\n✅ Total updates made: {total_updated}")


def delete_and_regenerate():
    """Alternative: Delete all sets questions so they can be regenerated fresh"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE topic='sets'")
    count = cursor.fetchone()[0]
    
    if count > 0:
        confirm = input(f"\n⚠️  This will DELETE all {count} existing 'sets' questions. Continue? (yes/no): ")
        if confirm.lower() == 'yes':
            cursor.execute("DELETE FROM questions_adaptive WHERE topic='sets'")
            conn.commit()
            print(f"🗑️  Deleted {count} questions")
            print("\nNow run: python generate_sets_questions.py")
        else:
            print("Cancelled.")
    else:
        print("No sets questions to delete.")
    
    conn.close()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--delete':
        delete_and_regenerate()
    else:
        print("="*50)
        print("SETS NOTATION FIXER - Irish Junior Cycle")
        print("="*50)
        print("\nThis will update existing questions to use:")
        print("  • #(A) instead of n(A)")
        print("  • A\\B instead of A - B")
        print()
        fix_notation()
        print("\n" + "="*50)
        print("To delete and regenerate fresh instead, run:")
        print("  python fix_sets_notation.py --delete")
        print("="*50)
