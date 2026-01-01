#!/usr/bin/env python3
"""
Fix Exponent Formatting Script
Finds and fixes cases where exponents > 9 are incorrectly formatted
e.g., x²3 should be x²³, x¹0 should be x¹⁰

Can be run on:
1. SQLite database directly (on PythonAnywhere)
2. SQL file before import

Usage on PythonAnywhere:
    python3 fix_exponents.py --database /home/bbsisk/mathapp/instance/mathquiz.db

Usage on SQL file:
    python3 fix_exponents.py --sqlfile lc_hl_functions_complete.sql
"""

import re
import argparse
import sqlite3

# Mapping for superscript characters
SUPERSCRIPT_MAP = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '-': '⁻', '+': '⁺'
}

REVERSE_SUPERSCRIPT_MAP = {v: k for k, v in SUPERSCRIPT_MAP.items()}

# Pattern to find: superscript digit(s) followed by regular digit(s)
# This catches cases like ²3, ³45, ¹0, etc.
SUPERSCRIPT_CHARS = ''.join(SUPERSCRIPT_MAP.values())
BROKEN_EXPONENT_PATTERN = re.compile(f'([{SUPERSCRIPT_CHARS}]+)([0-9]+)')

def fix_broken_exponent(match):
    """Convert the regular digits following superscripts to superscripts too"""
    existing_super = match.group(1)
    regular_digits = match.group(2)
    
    # Convert regular digits to superscript
    fixed_digits = ''.join(SUPERSCRIPT_MAP.get(d, d) for d in regular_digits)
    
    return existing_super + fixed_digits

def fix_text(text):
    """Fix all broken exponents in a text string"""
    if not text:
        return text, 0
    
    # Count matches before fixing
    matches = BROKEN_EXPONENT_PATTERN.findall(text)
    count = len(matches)
    
    # Apply fix
    fixed_text = BROKEN_EXPONENT_PATTERN.sub(fix_broken_exponent, text)
    
    return fixed_text, count

def scan_and_report(text, context=""):
    """Scan text and report any broken exponents found"""
    matches = BROKEN_EXPONENT_PATTERN.findall(text)
    issues = []
    for match in matches:
        original = match[0] + match[1]
        fixed = match[0] + ''.join(SUPERSCRIPT_MAP.get(d, d) for d in match[1])
        issues.append({
            'original': original,
            'fixed': fixed,
            'context': context
        })
    return issues

def fix_database(db_path, dry_run=True):
    """Scan and optionally fix the database"""
    print(f"{'[DRY RUN] ' if dry_run else ''}Processing database: {db_path}")
    print("=" * 60)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all questions
    cursor.execute("""
        SELECT id, question_text, option_a, option_b, option_c, option_d, explanation, topic
        FROM questions_adaptive
    """)
    
    rows = cursor.fetchall()
    total_issues = 0
    questions_affected = 0
    updates = []
    
    for row in rows:
        q_id, q_text, opt_a, opt_b, opt_c, opt_d, expl, topic = row
        
        row_issues = 0
        fixed_q_text, c1 = fix_text(q_text)
        fixed_opt_a, c2 = fix_text(opt_a)
        fixed_opt_b, c3 = fix_text(opt_b)
        fixed_opt_c, c4 = fix_text(opt_c)
        fixed_opt_d, c5 = fix_text(opt_d)
        fixed_expl, c6 = fix_text(expl)
        
        row_issues = c1 + c2 + c3 + c4 + c5 + c6
        
        if row_issues > 0:
            questions_affected += 1
            total_issues += row_issues
            
            print(f"\nQuestion ID {q_id} (topic: {topic}) - {row_issues} issue(s):")
            
            if c1 > 0:
                print(f"  Question: '{q_text[:80]}...' -> '{fixed_q_text[:80]}...'")
            if c2 > 0:
                print(f"  Option A: '{opt_a}' -> '{fixed_opt_a}'")
            if c3 > 0:
                print(f"  Option B: '{opt_b}' -> '{fixed_opt_b}'")
            if c4 > 0:
                print(f"  Option C: '{opt_c}' -> '{fixed_opt_c}'")
            if c5 > 0:
                print(f"  Option D: '{opt_d}' -> '{fixed_opt_d}'")
            if c6 > 0:
                print(f"  Explanation: '{expl[:60]}...' -> '{fixed_expl[:60]}...'")
            
            updates.append((fixed_q_text, fixed_opt_a, fixed_opt_b, fixed_opt_c, fixed_opt_d, fixed_expl, q_id))
    
    print("\n" + "=" * 60)
    print(f"Summary: {total_issues} issues found in {questions_affected} questions")
    
    if not dry_run and updates:
        print(f"\nApplying {len(updates)} updates...")
        cursor.executemany("""
            UPDATE questions_adaptive 
            SET question_text = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, explanation = ?
            WHERE id = ?
        """, updates)
        conn.commit()
        print("Updates applied successfully!")
    elif updates:
        print("\nRun with --apply to fix these issues")
    
    conn.close()
    return total_issues

def fix_sql_file(input_path, output_path=None):
    """Fix a SQL file and write the corrected version"""
    if output_path is None:
        output_path = input_path.replace('.sql', '_fixed.sql')
    
    print(f"Processing SQL file: {input_path}")
    print(f"Output file: {output_path}")
    print("=" * 60)
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all issues first for reporting
    issues = BROKEN_EXPONENT_PATTERN.findall(content)
    
    if issues:
        print(f"\nFound {len(issues)} broken exponent pattern(s):")
        unique_issues = set()
        for match in issues:
            original = match[0] + match[1]
            fixed = match[0] + ''.join(SUPERSCRIPT_MAP.get(d, d) for d in match[1])
            if (original, fixed) not in unique_issues:
                unique_issues.add((original, fixed))
                print(f"  '{original}' -> '{fixed}'")
        
        # Apply fixes
        fixed_content = BROKEN_EXPONENT_PATTERN.sub(fix_broken_exponent, content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"\nFixed file written to: {output_path}")
    else:
        print("\nNo broken exponent patterns found!")
        # Still write output file (copy)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return len(issues)

def main():
    parser = argparse.ArgumentParser(description='Fix broken exponent formatting in AgentMath questions')
    parser.add_argument('--database', '-d', help='Path to SQLite database')
    parser.add_argument('--sqlfile', '-s', help='Path to SQL file to fix')
    parser.add_argument('--output', '-o', help='Output path for fixed SQL file')
    parser.add_argument('--apply', action='store_true', help='Apply fixes to database (otherwise dry run)')
    parser.add_argument('--topic', '-t', help='Only check specific topic (for database)')
    
    args = parser.parse_args()
    
    if args.database:
        fix_database(args.database, dry_run=not args.apply)
    elif args.sqlfile:
        fix_sql_file(args.sqlfile, args.output)
    else:
        # Demo mode - show what the script does
        print("Exponent Fix Script - Demo Mode")
        print("=" * 60)
        print("\nThis script fixes broken exponent formatting where multi-digit")
        print("exponents are partially converted to superscript.")
        print("\nExamples of issues this fixes:")
        
        test_cases = [
            "x²3 should be x²³",
            "Calculate 2¹0",
            "The value x³45 is incorrect",
            "f(x) = x⁻12 + 5",
            "Simplify a²b³4",
        ]
        
        for test in test_cases:
            fixed, count = fix_text(test)
            if count > 0:
                print(f"  '{test}' -> '{fixed}'")
        
        print("\nUsage:")
        print("  For SQL file:  python3 fix_exponents.py --sqlfile input.sql")
        print("  For database:  python3 fix_exponents.py --database /path/to/db.db --apply")

if __name__ == '__main__':
    main()
