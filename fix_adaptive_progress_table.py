#!/usr/bin/env python3
"""
AgentMath Adaptive Progress Table Diagnostic & Fix Script
Run this on PythonAnywhere to diagnose and fix the adaptive_progress table.

Usage:
    python fix_adaptive_progress_table.py          # Diagnose only
    python fix_adaptive_progress_table.py --fix    # Diagnose and fix issues
"""

import sqlite3
import os
import sys
from datetime import datetime

# Configuration - adjust path if needed
DB_PATH = '/home/bbsisk/mathappR12/instance/mathquiz.db'

def connect_db():
    """Connect to the database"""
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at: {DB_PATH}")
        print("   Try running from /home/barryod1/mathmaster/")
        sys.exit(1)
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def diagnose_table(conn):
    """Diagnose the adaptive_progress table"""
    cursor = conn.cursor()
    issues = []
    
    print("=" * 60)
    print("ADAPTIVE PROGRESS TABLE DIAGNOSTIC")
    print("=" * 60)
    
    # 1. Check if table exists
    print("\n📋 1. Checking if table exists...")
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='adaptive_progress'
    """)
    if not cursor.fetchone():
        print("   ❌ Table 'adaptive_progress' does NOT exist!")
        issues.append("TABLE_MISSING")
        return issues
    print("   ✅ Table exists")
    
    # 2. Check table structure
    print("\n📋 2. Table Structure:")
    cursor.execute("PRAGMA table_info(adaptive_progress)")
    columns = cursor.fetchall()
    column_names = [col['name'] for col in columns]
    
    print("   Columns found:")
    for col in columns:
        print(f"      - {col['name']} ({col['type']}) {'NOT NULL' if col['notnull'] else 'nullable'}")
    
    # Check for required columns
    required_columns = ['user_id', 'topic', 'current_level', 'current_points']
    for req in required_columns:
        if req not in column_names:
            print(f"   ❌ Missing required column: {req}")
            issues.append(f"MISSING_COLUMN_{req.upper()}")
    
    if 'topic' not in column_names:
        print("   ⚠️  CRITICAL: 'topic' column is missing - this causes cross-topic level bleeding!")
        issues.append("NO_TOPIC_COLUMN")
    
    # 3. Check indexes and constraints
    print("\n📋 3. Indexes and Constraints:")
    cursor.execute("SELECT sql FROM sqlite_master WHERE name='adaptive_progress'")
    create_sql = cursor.fetchone()
    if create_sql:
        sql = create_sql[0]
        print(f"   CREATE statement:\n   {sql[:200]}...")
        
        if 'UNIQUE(user_id, topic)' in sql or 'UNIQUE (user_id, topic)' in sql:
            print("   ✅ Has UNIQUE(user_id, topic) constraint")
        elif 'UNIQUE(user_id)' in sql or 'UNIQUE (user_id)' in sql:
            print("   ❌ Has UNIQUE(user_id) only - missing topic in constraint!")
            issues.append("WRONG_UNIQUE_CONSTRAINT")
        else:
            print("   ⚠️  No unique constraint found on user_id")
            issues.append("NO_UNIQUE_CONSTRAINT")
    
    # 4. Check existing data
    print("\n📋 4. Existing Data Analysis:")
    
    # Total records
    cursor.execute("SELECT COUNT(*) as count FROM adaptive_progress")
    total = cursor.fetchone()['count']
    print(f"   Total records: {total}")
    
    if total > 0:
        # Records by topic
        cursor.execute("""
            SELECT topic, COUNT(*) as count, 
                   MIN(current_level) as min_level, 
                   MAX(current_level) as max_level
            FROM adaptive_progress 
            GROUP BY topic
        """)
        print("\n   Records by topic:")
        for row in cursor.fetchall():
            topic = row['topic'] if row['topic'] else '(NULL/empty)'
            print(f"      - {topic}: {row['count']} records (levels {row['min_level']}-{row['max_level']})")
        
        # Check for NULL or empty topics
        cursor.execute("""
            SELECT COUNT(*) as count FROM adaptive_progress 
            WHERE topic IS NULL OR topic = ''
        """)
        null_topics = cursor.fetchone()['count']
        if null_topics > 0:
            print(f"\n   ⚠️  Found {null_topics} records with NULL/empty topic!")
            issues.append("NULL_TOPICS")
        
        # Check for duplicate user+topic combinations (shouldn't happen with proper constraint)
        cursor.execute("""
            SELECT user_id, topic, COUNT(*) as count 
            FROM adaptive_progress 
            WHERE user_id IS NOT NULL
            GROUP BY user_id, topic 
            HAVING COUNT(*) > 1
        """)
        duplicates = cursor.fetchall()
        if duplicates:
            print(f"\n   ❌ Found {len(duplicates)} duplicate user+topic combinations!")
            for dup in duplicates[:5]:
                print(f"      - user_id={dup['user_id']}, topic={dup['topic']}: {dup['count']} records")
            issues.append("DUPLICATE_RECORDS")
        
        # Show sample data
        print("\n   Sample records (first 10):")
        cursor.execute("""
            SELECT id, user_id, guest_code, topic, current_level, current_points 
            FROM adaptive_progress 
            LIMIT 10
        """)
        for row in cursor.fetchall():
            user = row['user_id'] if row['user_id'] else f"guest:{row['guest_code']}"
            topic = row['topic'] if row['topic'] else '(none)'
            print(f"      ID {row['id']}: user={user}, topic={topic}, level={row['current_level']}, points={row['current_points']}")
    
    # 5. Summary
    print("\n" + "=" * 60)
    print("DIAGNOSIS SUMMARY")
    print("=" * 60)
    
    if not issues:
        print("✅ No issues found! Table structure looks correct.")
        print("\n   If you're still seeing wrong levels, the issue may be:")
        print("   - Browser caching old JavaScript")
        print("   - Need to clear browser cache and reload")
    else:
        print(f"❌ Found {len(issues)} issue(s):")
        for issue in issues:
            print(f"   - {issue}")
        print("\n   Run with --fix flag to attempt automatic repair:")
        print(f"   python {sys.argv[0]} --fix")
    
    return issues

def fix_table(conn, issues):
    """Fix the adaptive_progress table"""
    cursor = conn.cursor()
    
    print("\n" + "=" * 60)
    print("APPLYING FIXES")
    print("=" * 60)
    
    if "TABLE_MISSING" in issues:
        print("\n🔧 Creating adaptive_progress table...")
        cursor.execute("""
            CREATE TABLE adaptive_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                guest_code TEXT,
                topic TEXT NOT NULL DEFAULT 'fractions',
                current_level INTEGER DEFAULT 1,
                current_points INTEGER DEFAULT 0,
                total_questions INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, topic),
                UNIQUE(guest_code, topic)
            )
        """)
        conn.commit()
        print("   ✅ Table created successfully!")
        return
    
    # Backup first
    print("\n🔧 Creating backup table...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_table = f"adaptive_progress_backup_{timestamp}"
    
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {backup_table}")
        cursor.execute(f"CREATE TABLE {backup_table} AS SELECT * FROM adaptive_progress")
        cursor.execute(f"SELECT COUNT(*) as count FROM {backup_table}")
        backup_count = cursor.fetchone()['count']
        print(f"   ✅ Backup created: {backup_table} ({backup_count} records)")
    except Exception as e:
        print(f"   ❌ Backup failed: {e}")
        print("   Aborting fix for safety.")
        return
    
    # Fix NULL topics
    if "NULL_TOPICS" in issues:
        print("\n🔧 Fixing NULL/empty topics (setting to 'fractions')...")
        cursor.execute("""
            UPDATE adaptive_progress 
            SET topic = 'fractions' 
            WHERE topic IS NULL OR topic = ''
        """)
        print(f"   ✅ Updated {cursor.rowcount} records")
    
    # Fix duplicate records
    if "DUPLICATE_RECORDS" in issues:
        print("\n🔧 Removing duplicate records (keeping highest level)...")
        cursor.execute("""
            DELETE FROM adaptive_progress 
            WHERE id NOT IN (
                SELECT MAX(id) 
                FROM adaptive_progress 
                GROUP BY COALESCE(user_id, ''), COALESCE(guest_code, ''), topic
            )
        """)
        print(f"   ✅ Removed {cursor.rowcount} duplicate records")
    
    # Recreate table with proper constraints if needed
    if "WRONG_UNIQUE_CONSTRAINT" in issues or "NO_UNIQUE_CONSTRAINT" in issues or "NO_TOPIC_COLUMN" in issues:
        print("\n🔧 Recreating table with proper structure...")
        
        # Save data
        cursor.execute("""
            SELECT user_id, guest_code, topic, current_level, current_points, 
                   total_questions, correct_answers, updated_at
            FROM adaptive_progress
        """)
        data = cursor.fetchall()
        
        # Drop and recreate
        cursor.execute("DROP TABLE adaptive_progress")
        cursor.execute("""
            CREATE TABLE adaptive_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                guest_code TEXT,
                topic TEXT NOT NULL DEFAULT 'fractions',
                current_level INTEGER DEFAULT 1,
                current_points INTEGER DEFAULT 0,
                total_questions INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, topic),
                UNIQUE(guest_code, topic)
            )
        """)
        
        # Restore data (handling duplicates by keeping the one with highest level)
        restored = 0
        skipped = 0
        seen = set()
        
        for row in data:
            user_id = row[0]
            guest_code = row[1]
            topic = row[2] if row[2] else 'fractions'
            
            # Create unique key
            key = (user_id, guest_code, topic)
            if key in seen:
                skipped += 1
                continue
            seen.add(key)
            
            try:
                cursor.execute("""
                    INSERT INTO adaptive_progress 
                    (user_id, guest_code, topic, current_level, current_points, 
                     total_questions, correct_answers, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (user_id, guest_code, topic, row[3], row[4], row[5] or 0, row[6] or 0, row[7]))
                restored += 1
            except sqlite3.IntegrityError:
                skipped += 1
        
        print(f"   ✅ Table recreated with proper constraints")
        print(f"   ✅ Restored {restored} records, skipped {skipped} duplicates")
    
    conn.commit()
    
    # Verify fix
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    
    cursor.execute("SELECT COUNT(*) as count FROM adaptive_progress")
    final_count = cursor.fetchone()['count']
    print(f"   Records in table: {final_count}")
    
    cursor.execute("""
        SELECT topic, COUNT(*) as count 
        FROM adaptive_progress 
        GROUP BY topic
    """)
    print("   By topic:")
    for row in cursor.fetchall():
        print(f"      - {row['topic']}: {row['count']} records")
    
    print("\n✅ Fix complete!")
    print(f"   Backup saved as: {backup_table}")
    print("\n   Next steps:")
    print("   1. Upload the new student_app.html (Revision 2.41)")
    print("   2. Clear browser cache (Ctrl+Shift+R)")
    print("   3. Test Percentages adaptive quiz - should start at Level 1")

def main():
    fix_mode = '--fix' in sys.argv
    
    print("\n" + "=" * 60)
    print("AgentMath Adaptive Progress Table Tool")
    print(f"Mode: {'FIX' if fix_mode else 'DIAGNOSE ONLY'}")
    print(f"Database: {DB_PATH}")
    print("=" * 60)
    
    conn = connect_db()
    
    try:
        issues = diagnose_table(conn)
        
        if fix_mode and issues:
            confirm = input("\n⚠️  Proceed with fixes? (yes/no): ")
            if confirm.lower() == 'yes':
                fix_table(conn, issues)
            else:
                print("   Fix cancelled.")
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()
