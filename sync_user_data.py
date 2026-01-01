"""
Database Sync Script - AgentMath (v2)
Syncs user data from LIVE database to DEVELOPMENT database

Usage:
    cd /home/bbsisk/mathappR14
    python sync_user_data.py --dry-run    # Preview changes without applying
    python sync_user_data.py              # Actually sync the data
"""

import sqlite3
import os
import sys
import shutil
from datetime import datetime

# Database paths
LIVE_DB = '/home/bbsisk/mathapp/instance/mathquiz.db'
DEV_DB = '/home/bbsisk/mathappR14/instance/mathquiz.db'

def get_connection(db_path):
    """Get database connection"""
    if not os.path.exists(db_path):
        print(f"❌ Database not found: {db_path}")
        sys.exit(1)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def backup_database(db_path):
    """Create a backup before making changes"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f"{db_path}.backup_{timestamp}"
    shutil.copy2(db_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def get_table_columns(conn, table_name):
    """Get column names for a table"""
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    return [row[1] for row in cursor.fetchall()]

def table_exists(conn, table_name):
    """Check if table exists"""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None

def show_table_structure(conn, table_name):
    """Show structure of a table"""
    if not table_exists(conn, table_name):
        return None
    columns = get_table_columns(conn, table_name)
    return columns

def show_summary(live_conn, dev_conn):
    """Show database comparison summary"""
    print("\n" + "="*60)
    print("DATABASE COMPARISON SUMMARY")
    print("="*60)
    
    live_cursor = live_conn.cursor()
    dev_cursor = dev_conn.cursor()
    
    # Users
    if table_exists(live_conn, 'users'):
        live_cursor.execute("SELECT COUNT(*) FROM users")
        live_users = live_cursor.fetchone()[0]
        dev_cursor.execute("SELECT COUNT(*) FROM users")
        dev_users = dev_cursor.fetchone()[0]
        print(f"Users:          Live: {live_users:>6}  |  Dev: {dev_users:>6}  |  Diff: {live_users - dev_users:>+6}")
    
    # Guests
    if table_exists(live_conn, 'guest_sessions'):
        live_cursor.execute("SELECT COUNT(*) FROM guest_sessions")
        live_guests = live_cursor.fetchone()[0]
        dev_cursor.execute("SELECT COUNT(*) FROM guest_sessions")
        dev_guests = dev_cursor.fetchone()[0]
        print(f"Guest Sessions: Live: {live_guests:>6}  |  Dev: {dev_guests:>6}  |  Diff: {live_guests - dev_guests:>+6}")
    
    # Points - check user_points table instead
    if table_exists(live_conn, 'user_points'):
        live_cursor.execute("SELECT COUNT(*), COALESCE(SUM(points), 0) FROM user_points")
        live_row = live_cursor.fetchone()
        dev_cursor.execute("SELECT COUNT(*), COALESCE(SUM(points), 0) FROM user_points")
        dev_row = dev_cursor.fetchone()
        print(f"Points Records: Live: {live_row[0]:>6}  |  Dev: {dev_row[0]:>6}  |  Diff: {live_row[0] - dev_row[0]:>+6}")
        print(f"Total Points:   Live: {live_row[1]:>6}  |  Dev: {dev_row[1]:>6}  |  Diff: {live_row[1] - dev_row[1]:>+6}")
    
    # Quiz attempts
    if table_exists(live_conn, 'quiz_attempts'):
        live_cursor.execute("SELECT COUNT(*) FROM quiz_attempts")
        live_attempts = live_cursor.fetchone()[0]
        dev_cursor.execute("SELECT COUNT(*) FROM quiz_attempts")
        dev_attempts = dev_cursor.fetchone()[0]
        print(f"Quiz Attempts:  Live: {live_attempts:>6}  |  Dev: {dev_attempts:>6}  |  Diff: {live_attempts - dev_attempts:>+6}")
    
    # Badges
    if table_exists(live_conn, 'user_badges'):
        live_cursor.execute("SELECT COUNT(*) FROM user_badges")
        live_badges = live_cursor.fetchone()[0]
        dev_cursor.execute("SELECT COUNT(*) FROM user_badges")
        dev_badges = dev_cursor.fetchone()[0]
        print(f"User Badges:    Live: {live_badges:>6}  |  Dev: {dev_badges:>6}  |  Diff: {live_badges - dev_badges:>+6}")

def sync_table(live_conn, dev_conn, table_name, key_columns, dry_run=True):
    """
    Sync a table from live to dev
    key_columns: list of columns that uniquely identify a record
    """
    if not table_exists(live_conn, table_name):
        print(f"  ⚠️ {table_name}: Not in live DB - skipping")
        return 0
    if not table_exists(dev_conn, table_name):
        print(f"  ⚠️ {table_name}: Not in dev DB - skipping")
        return 0
    
    live_cursor = live_conn.cursor()
    dev_cursor = dev_conn.cursor()
    
    # Get common columns
    live_cols = set(get_table_columns(live_conn, table_name))
    dev_cols = set(get_table_columns(dev_conn, table_name))
    common_cols = list(live_cols & dev_cols)
    
    if not common_cols:
        print(f"  ⚠️ {table_name}: No common columns - skipping")
        return 0
    
    # Check key columns exist
    for kc in key_columns:
        if kc not in common_cols:
            print(f"  ⚠️ {table_name}: Key column '{kc}' not found - skipping")
            return 0
    
    columns_str = ', '.join(common_cols)
    placeholders = ', '.join(['?' for _ in common_cols])
    
    # Get counts
    live_cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    live_count = live_cursor.fetchone()[0]
    dev_cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    dev_count = dev_cursor.fetchone()[0]
    
    # Get all records from live
    live_cursor.execute(f"SELECT {columns_str} FROM {table_name}")
    live_records = live_cursor.fetchall()
    
    # Build index of dev records by key
    key_indices = [common_cols.index(kc) for kc in key_columns]
    
    dev_cursor.execute(f"SELECT {columns_str} FROM {table_name}")
    dev_keys = set()
    for row in dev_cursor.fetchall():
        key = tuple(row[i] for i in key_indices)
        dev_keys.add(key)
    
    # Find records to insert
    to_insert = []
    for record in live_records:
        key = tuple(record[i] for i in key_indices)
        if key not in dev_keys:
            to_insert.append(record)
    
    if not to_insert:
        print(f"  ✓ {table_name}: In sync (Live: {live_count}, Dev: {dev_count})")
        return 0
    
    print(f"  📥 {table_name}: {len(to_insert)} new records to sync (Live: {live_count}, Dev: {dev_count})")
    
    if not dry_run:
        inserted = 0
        for record in to_insert:
            try:
                dev_cursor.execute(f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})", record)
                inserted += 1
            except sqlite3.IntegrityError as e:
                pass  # Skip duplicates
        dev_conn.commit()
        print(f"      ✅ Inserted {inserted} records")
        return inserted
    
    return len(to_insert)

def sync_users(live_conn, dev_conn, dry_run=True):
    """Sync users table"""
    print("\n" + "="*60)
    print("SYNCING USERS")
    print("="*60)
    
    # Try different key columns
    if 'id' in get_table_columns(live_conn, 'users'):
        return sync_table(live_conn, dev_conn, 'users', ['id'], dry_run)
    elif 'username' in get_table_columns(live_conn, 'users'):
        return sync_table(live_conn, dev_conn, 'users', ['username'], dry_run)
    else:
        print("  ⚠️ Could not determine user key column")
        return 0

def sync_guests(live_conn, dev_conn, dry_run=True):
    """Sync guest sessions"""
    print("\n" + "="*60)
    print("SYNCING GUEST SESSIONS")
    print("="*60)
    return sync_table(live_conn, dev_conn, 'guest_sessions', ['guest_code'], dry_run)

def sync_user_data_tables(live_conn, dev_conn, dry_run=True):
    """Sync user-related data tables"""
    print("\n" + "="*60)
    print("SYNCING USER DATA TABLES")
    print("="*60)
    
    # Tables and their key columns
    tables = [
        ('user_points', ['id']),
        ('user_badges', ['id']),
        ('guest_badges', ['id']),
        ('topic_progress', ['id']),
        ('topic_mastery', ['id']),
        ('quiz_attempts', ['id']),
        ('guest_quiz_attempts', ['id']),
        ('user_adaptive_progress', ['id']),
        ('topic_progressions_adaptive', ['id']),
        ('weekly_challenge_progress', ['id']),
        ('class_enrollments', ['id']),
        ('feedback', ['id']),
    ]
    
    total = 0
    for table_name, keys in tables:
        total += sync_table(live_conn, dev_conn, table_name, keys, dry_run)
    
    return total

def show_users_columns(conn):
    """Show what columns exist in users table"""
    print("\n" + "="*60)
    print("USERS TABLE STRUCTURE")
    print("="*60)
    columns = get_table_columns(conn, 'users')
    print(f"Columns: {', '.join(columns)}")

def main():
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    show_cols = '--show-columns' in sys.argv
    
    print("="*60)
    print("AgentMath Database Sync Tool v2")
    print("="*60)
    print(f"Live DB: {LIVE_DB}")
    print(f"Dev DB:  {DEV_DB}")
    print(f"Mode:    {'DRY RUN (preview only)' if dry_run else '⚠️  LIVE - Will modify dev database!'}")
    print("="*60)
    
    # Check databases exist
    if not os.path.exists(LIVE_DB):
        print(f"❌ Live database not found: {LIVE_DB}")
        sys.exit(1)
    
    if not os.path.exists(DEV_DB):
        print(f"❌ Dev database not found: {DEV_DB}")
        sys.exit(1)
    
    # Connect to databases
    live_conn = get_connection(LIVE_DB)
    dev_conn = get_connection(DEV_DB)
    
    try:
        # Show columns if requested
        if show_cols:
            show_users_columns(live_conn)
            return
        
        # Show initial summary
        show_summary(live_conn, dev_conn)
        
        # Backup dev database before making changes
        if not dry_run:
            print("\n📦 Creating backup of dev database...")
            backup_database(DEV_DB)
        
        # Sync tables
        sync_users(live_conn, dev_conn, dry_run)
        sync_guests(live_conn, dev_conn, dry_run)
        sync_user_data_tables(live_conn, dev_conn, dry_run)
        
        # Final summary
        if not dry_run:
            print("\n" + "="*60)
            print("SYNC COMPLETE - Updated Summary")
            print("="*60)
            show_summary(live_conn, dev_conn)
        else:
            print("\n" + "="*60)
            print("DRY RUN COMPLETE")
            print("="*60)
            print("\nTo apply these changes, run:")
            print("  python sync_user_data.py")
        
    finally:
        live_conn.close()
        dev_conn.close()

if __name__ == '__main__':
    main()
