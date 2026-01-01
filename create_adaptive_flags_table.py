#!/usr/bin/env python3
"""
CREATE ADAPTIVE QUESTION FLAGS TABLE
=====================================
Creates the adaptive_question_flags table for storing
flagged issues with adaptive quiz questions.
"""

import sqlite3

DB_PATH = 'instance/mathquiz.db'

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if table already exists
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='adaptive_question_flags'
    """)
    
    if cursor.fetchone():
        print("✅ Table 'adaptive_question_flags' already exists")
        conn.close()
        return
    
    # Create the table
    cursor.execute("""
        CREATE TABLE adaptive_question_flags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            topic VARCHAR(50) NOT NULL,
            user_id INTEGER REFERENCES users(id),
            guest_identifier VARCHAR(100),
            flag_type VARCHAR(50) NOT NULL,
            description TEXT NOT NULL,
            question_text TEXT,
            status VARCHAR(20) DEFAULT 'pending',
            admin_notes TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            resolved_at DATETIME,
            resolved_by INTEGER REFERENCES users(id)
        )
    """)
    
    # Create index for faster lookups
    cursor.execute("""
        CREATE INDEX idx_adaptive_flags_status 
        ON adaptive_question_flags(status)
    """)
    
    cursor.execute("""
        CREATE INDEX idx_adaptive_flags_question 
        ON adaptive_question_flags(question_id)
    """)
    
    conn.commit()
    conn.close()
    
    print("✅ Created 'adaptive_question_flags' table")
    print("   - Indexed by status and question_id")


def show_stats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Count flags
    cursor.execute("SELECT COUNT(*) FROM adaptive_question_flags")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM adaptive_question_flags WHERE status='pending'")
    pending = cursor.fetchone()[0]
    
    print(f"\n📊 Adaptive Question Flags: {total} total, {pending} pending")
    
    conn.close()


if __name__ == '__main__':
    print("="*50)
    print("ADAPTIVE QUESTION FLAGS - TABLE SETUP")
    print("="*50)
    create_table()
    show_stats()
