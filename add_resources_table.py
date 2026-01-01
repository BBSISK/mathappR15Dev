#!/usr/bin/env python3
"""
Database migration: Add additional_resources table for external learning links
Run this script once to add the resources functionality
"""

import sqlite3
import os

def run_migration():
    db_path = 'instance/mathquiz.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at {db_path}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if table already exists
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='additional_resources'
        """)
        
        if cursor.fetchone():
            print("ℹ️  Table 'additional_resources' already exists")
        else:
            # Create the additional_resources table
            cursor.execute("""
                CREATE TABLE additional_resources (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    button_text VARCHAR(100) NOT NULL,
                    link_url VARCHAR(500) NOT NULL,
                    popup_text TEXT,
                    image_filename VARCHAR(255),
                    display_order INTEGER DEFAULT 0,
                    is_active INTEGER DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    created_by INTEGER,
                    FOREIGN KEY (created_by) REFERENCES users(id)
                )
            """)
            print("✅ Created 'additional_resources' table")
        
        # Insert default Corbett Maths resource
        cursor.execute("""
            SELECT id FROM additional_resources WHERE button_text = 'Corbett Maths'
        """)
        
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO additional_resources 
                (button_text, link_url, popup_text, image_filename, display_order, is_active)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                'Corbett Maths',
                'https://corbettmaths.com/contents/',
                'Worksheets for all topics which are very useful in building proficiency in Junior Cycle Topics',
                'corbett_maths_preview.png',
                1,
                1
            ))
            print("✅ Added default 'Corbett Maths' resource")
        else:
            print("ℹ️  'Corbett Maths' resource already exists")
        
        conn.commit()
        print("\n✅ Migration completed successfully!")
        
        # Show current resources
        cursor.execute("SELECT id, button_text, link_url, is_active FROM additional_resources ORDER BY display_order")
        resources = cursor.fetchall()
        
        if resources:
            print("\n📚 Current Resources:")
            for r in resources:
                status = "✓ Active" if r[3] else "✗ Inactive"
                print(f"   {r[0]}. {r[1]} - {r[2][:50]}... [{status}]")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

if __name__ == '__main__':
    print("=" * 50)
    print("Additional Resources Table Migration")
    print("=" * 50)
    run_migration()
