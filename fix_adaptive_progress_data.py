#!/usr/bin/env python3
"""
AgentMath - Fix Adaptive Progress Data

This script cleans up the corrupted adaptive_progress records where:
- user_id = 38 (shared guest account)
- guest_code = None

These records were created due to a bug where session['is_guest'] was not
being set in repeat_guest_login(), causing all guest progress to be saved
to the shared guest@agentmath.app user instead of individual guest codes.

Since we cannot determine which guest each record belonged to, these
records must be deleted. Users will need to start fresh.

Run this AFTER uploading the fixed app.py
"""

import sqlite3

DB_PATH = 'instance/mathquiz.db'

def main():
    print("=" * 60)
    print("AgentMath - Adaptive Progress Data Cleanup")
    print("=" * 60)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Show current state
    cursor.execute("""
        SELECT COUNT(*) FROM adaptive_progress 
        WHERE user_id = 38 AND guest_code IS NULL
    """)
    bad_records = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM adaptive_progress")
    total_records = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT COUNT(*) FROM adaptive_progress 
        WHERE guest_code IS NOT NULL
    """)
    good_records = cursor.fetchone()[0]
    
    print(f"\nCurrent state:")
    print(f"  Total records: {total_records}")
    print(f"  Corrupted (user_id=38, no guest_code): {bad_records}")
    print(f"  Valid (has guest_code): {good_records}")
    
    if bad_records == 0:
        print("\n✓ No corrupted records found. Nothing to clean up!")
        conn.close()
        return
    
    print(f"\nThis will DELETE {bad_records} corrupted records.")
    print("These records were shared by all guests due to the bug.")
    print("After deletion, guests will start fresh at Level 1 for each topic.")
    
    response = input("\nProceed with cleanup? (yes/no): ")
    
    if response.lower() == 'yes':
        cursor.execute("""
            DELETE FROM adaptive_progress 
            WHERE user_id = 38 AND guest_code IS NULL
        """)
        deleted = cursor.rowcount
        conn.commit()
        print(f"\n✓ Deleted {deleted} corrupted records.")
        
        # Verify
        cursor.execute("SELECT COUNT(*) FROM adaptive_progress")
        remaining = cursor.fetchone()[0]
        print(f"  Remaining records: {remaining}")
    else:
        print("\nCleanup cancelled.")
    
    conn.close()
    print("\nDone!")

if __name__ == "__main__":
    main()
