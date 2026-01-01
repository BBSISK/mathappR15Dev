"""
Maths Passport v2 - Database Migration Script
Run this script to set up the new weekly planner tables.

Usage:
    cd /home/bbsisk/mathappR15Dev
    source venv/bin/activate
    python passport_migration.py
"""

import sqlite3
import json
from datetime import datetime

DATABASE_PATH = 'instance/mathquiz.db'

def run_migration():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    print("🚀 Maths Passport v2 - Database Migration")
    print("=" * 50)
    
    # =========================================================
    # TABLE 1: passport_setup - Core passport configuration
    # =========================================================
    print("\n📋 Creating passport_setup table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_setup (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            curriculum TEXT NOT NULL,
            exam_date DATE,
            study_hours_per_week REAL DEFAULT 3.5,
            setup_completed_at DATETIME,
            last_plan_generated_at DATETIME,
            last_daily_review_at DATETIME,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id),
            UNIQUE(guest_code)
        )
    """)
    print("   ✓ passport_setup created")
    
    # =========================================================
    # TABLE 2: passport_self_assessment - Granular topic ratings
    # =========================================================
    print("\n📋 Creating passport_topic_assessment table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_topic_assessment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            topic TEXT NOT NULL,
            strand TEXT,
            confidence INTEGER NOT NULL,
            assessed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, topic),
            UNIQUE(guest_code, topic)
        )
    """)
    print("   ✓ passport_topic_assessment created")
    
    # =========================================================
    # TABLE 3: passport_diagnostic - Quick check quiz results
    # =========================================================
    print("\n📋 Creating passport_diagnostic table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_diagnostic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            topic TEXT NOT NULL,
            strand TEXT,
            questions_asked INTEGER DEFAULT 0,
            questions_correct INTEGER DEFAULT 0,
            recommended_entry_level INTEGER,
            diagnosed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, topic),
            UNIQUE(guest_code, topic)
        )
    """)
    print("   ✓ passport_diagnostic created")
    
    # =========================================================
    # TABLE 4: passport_entry_levels - Calculated entry levels
    # =========================================================
    print("\n📋 Creating passport_entry_levels table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_entry_levels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            topic TEXT NOT NULL,
            progress_level INTEGER DEFAULT 0,
            confidence_modifier INTEGER DEFAULT 0,
            quiz_modifier INTEGER DEFAULT 0,
            final_entry_level INTEGER NOT NULL,
            calculated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, topic),
            UNIQUE(guest_code, topic)
        )
    """)
    print("   ✓ passport_entry_levels created")
    
    # =========================================================
    # TABLE 5: passport_weekly_plan - Weekly plan headers
    # =========================================================
    print("\n📋 Creating passport_weekly_plan table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_weekly_plan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            week_number INTEGER NOT NULL,
            week_start_date DATE NOT NULL,
            week_end_date DATE NOT NULL,
            focus_area TEXT,
            capacity_hours REAL DEFAULT 3.5,
            capacity_type TEXT DEFAULT 'normal',
            holiday_name TEXT,
            status TEXT DEFAULT 'upcoming',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, week_number),
            UNIQUE(guest_code, week_number)
        )
    """)
    print("   ✓ passport_weekly_plan created")
    
    # =========================================================
    # TABLE 6: passport_week_topics - Topics assigned to weeks
    # =========================================================
    print("\n📋 Creating passport_week_topics table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_week_topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_plan_id INTEGER NOT NULL,
            user_id INTEGER,
            guest_code TEXT,
            topic TEXT NOT NULL,
            strand TEXT,
            entry_level INTEGER NOT NULL,
            target_level INTEGER NOT NULL,
            priority TEXT DEFAULT 'normal',
            current_level INTEGER,
            questions_answered INTEGER DEFAULT 0,
            accuracy_percent REAL,
            time_spent_minutes INTEGER DEFAULT 0,
            status TEXT DEFAULT 'not_started',
            pinned BOOLEAN DEFAULT 0,
            pinned_at DATETIME,
            pinned_from_week INTEGER,
            auto_moved_count INTEGER DEFAULT 0,
            last_auto_moved_at DATETIME,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (week_plan_id) REFERENCES passport_weekly_plan(id)
        )
    """)
    print("   ✓ passport_week_topics created")
    
    # =========================================================
    # TABLE 7: passport_weekly_reports - End of week summaries
    # =========================================================
    print("\n📋 Creating passport_weekly_reports table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_weekly_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            week_number INTEGER NOT NULL,
            planned_topics INTEGER DEFAULT 0,
            completed_topics INTEGER DEFAULT 0,
            total_questions INTEGER DEFAULT 0,
            total_correct INTEGER DEFAULT 0,
            total_time_minutes INTEGER DEFAULT 0,
            accuracy_percent REAL,
            levels_gained INTEGER DEFAULT 0,
            on_track BOOLEAN DEFAULT 1,
            report_data JSON,
            generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, week_number),
            UNIQUE(guest_code, week_number)
        )
    """)
    print("   ✓ passport_weekly_reports created")
    
    # =========================================================
    # TABLE 8: passport_adjustments - Log of plan changes
    # =========================================================
    print("\n📋 Creating passport_adjustments table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_adjustments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            adjustment_type TEXT NOT NULL,
            topic TEXT,
            from_week INTEGER,
            to_week INTEGER,
            reason TEXT,
            is_auto BOOLEAN DEFAULT 1,
            adjustment_data JSON,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("   ✓ passport_adjustments created")
    
    # =========================================================
    # TABLE 9: passport_daily_snapshot - Daily progress tracking
    # =========================================================
    print("\n📋 Creating passport_daily_snapshot table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passport_daily_snapshot (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            guest_code TEXT,
            snapshot_date DATE NOT NULL,
            topics_worked JSON,
            total_questions INTEGER DEFAULT 0,
            total_time_minutes INTEGER DEFAULT 0,
            plan_adjustments JSON,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, snapshot_date),
            UNIQUE(guest_code, snapshot_date)
        )
    """)
    print("   ✓ passport_daily_snapshot created")
    
    # =========================================================
    # TABLE 10: irish_school_calendar - Holidays and breaks
    # =========================================================
    print("\n📋 Creating irish_school_calendar table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS irish_school_calendar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER NOT NULL,
            event_name TEXT NOT NULL,
            event_type TEXT NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            workload_modifier REAL DEFAULT 1.0,
            notes TEXT
        )
    """)
    print("   ✓ irish_school_calendar created")
    
    # =========================================================
    # Create indexes for performance
    # =========================================================
    print("\n📋 Creating indexes...")
    
    indexes = [
        "CREATE INDEX IF NOT EXISTS idx_passport_setup_user ON passport_setup(user_id)",
        "CREATE INDEX IF NOT EXISTS idx_passport_setup_guest ON passport_setup(guest_code)",
        "CREATE INDEX IF NOT EXISTS idx_passport_weekly_plan_user ON passport_weekly_plan(user_id)",
        "CREATE INDEX IF NOT EXISTS idx_passport_weekly_plan_guest ON passport_weekly_plan(guest_code)",
        "CREATE INDEX IF NOT EXISTS idx_passport_week_topics_week ON passport_week_topics(week_plan_id)",
        "CREATE INDEX IF NOT EXISTS idx_passport_week_topics_user ON passport_week_topics(user_id)",
        "CREATE INDEX IF NOT EXISTS idx_passport_week_topics_topic ON passport_week_topics(topic)",
        "CREATE INDEX IF NOT EXISTS idx_passport_adjustments_user ON passport_adjustments(user_id)",
        "CREATE INDEX IF NOT EXISTS idx_passport_adjustments_guest ON passport_adjustments(guest_code)",
        "CREATE INDEX IF NOT EXISTS idx_irish_calendar_dates ON irish_school_calendar(start_date, end_date)",
    ]
    
    for idx in indexes:
        cursor.execute(idx)
    print("   ✓ Indexes created")
    
    # =========================================================
    # Populate Irish School Calendar (2024-2026)
    # =========================================================
    print("\n📋 Populating Irish school calendar...")
    
    # Check if already populated
    cursor.execute("SELECT COUNT(*) FROM irish_school_calendar")
    if cursor.fetchone()[0] == 0:
        calendar_events = [
            # 2024-2025 School Year
            (2024, 'October Mid-Term', 'midterm', '2024-10-28', '2024-11-01', 0.5, 'Week off school'),
            (2024, 'Christmas Break', 'christmas', '2024-12-23', '2025-01-03', 1.5, 'Two weeks off - intensive for exam students'),
            (2025, 'February Mid-Term', 'midterm', '2025-02-17', '2025-02-21', 0.5, 'Week off school'),
            (2025, 'St Patricks Day', 'bank_holiday', '2025-03-17', '2025-03-17', 1.2, 'Bank holiday'),
            (2025, 'Easter Break', 'easter', '2025-04-14', '2025-04-25', 1.5, 'Two weeks off - intensive for exam students'),
            (2025, 'May Bank Holiday', 'bank_holiday', '2025-05-05', '2025-05-05', 1.2, 'Bank holiday'),
            (2025, 'June Bank Holiday', 'bank_holiday', '2025-06-02', '2025-06-02', 1.2, 'Bank holiday'),
            (2025, 'Summer Holidays', 'summer', '2025-06-30', '2025-08-31', 0.3, 'Summer break - light study'),
            
            # 2025-2026 School Year  
            (2025, 'October Mid-Term 2025', 'midterm', '2025-10-27', '2025-10-31', 0.5, 'Week off school'),
            (2025, 'Christmas Break 2025', 'christmas', '2025-12-22', '2026-01-02', 1.5, 'Two weeks off'),
            (2026, 'February Mid-Term 2026', 'midterm', '2026-02-16', '2026-02-20', 0.5, 'Week off school'),
            (2026, 'St Patricks Day 2026', 'bank_holiday', '2026-03-17', '2026-03-17', 1.2, 'Bank holiday'),
            (2026, 'Easter Break 2026', 'easter', '2026-03-30', '2026-04-10', 1.5, 'Two weeks off'),
            (2026, 'May Bank Holiday 2026', 'bank_holiday', '2026-05-04', '2026-05-04', 1.2, 'Bank holiday'),
            (2026, 'June Bank Holiday 2026', 'bank_holiday', '2026-06-01', '2026-06-01', 1.2, 'Bank holiday'),
        ]
        
        cursor.executemany("""
            INSERT INTO irish_school_calendar 
            (year, event_name, event_type, start_date, end_date, workload_modifier, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, calendar_events)
        print(f"   ✓ Added {len(calendar_events)} calendar events")
    else:
        print("   ✓ Calendar already populated")
    
    # =========================================================
    # Commit and close
    # =========================================================
    conn.commit()
    conn.close()
    
    print("\n" + "=" * 50)
    print("✅ Migration completed successfully!")
    print("=" * 50)
    
    # Print summary
    print("\n📊 Tables created:")
    print("   1. passport_setup - Core configuration")
    print("   2. passport_topic_assessment - Granular topic ratings")
    print("   3. passport_diagnostic - Quiz results per topic")
    print("   4. passport_entry_levels - Calculated entry levels")
    print("   5. passport_weekly_plan - Weekly plan headers")
    print("   6. passport_week_topics - Topics assigned to weeks")
    print("   7. passport_weekly_reports - End of week summaries")
    print("   8. passport_adjustments - Plan change log")
    print("   9. passport_daily_snapshot - Daily progress tracking")
    print("   10. irish_school_calendar - Holidays and breaks")
    
    print("\n🇮🇪 Irish calendar loaded with holidays through 2026")
    print("\n📝 Next steps:")
    print("   1. Upload the updated app.py with new configurations")
    print("   2. Upload the updated student_passport.html")
    print("   3. Reload the web app")


def verify_migration():
    """Verify all tables were created correctly"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    print("\n🔍 Verifying migration...")
    
    tables = [
        'passport_setup',
        'passport_topic_assessment', 
        'passport_diagnostic',
        'passport_entry_levels',
        'passport_weekly_plan',
        'passport_week_topics',
        'passport_weekly_reports',
        'passport_adjustments',
        'passport_daily_snapshot',
        'irish_school_calendar'
    ]
    
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='{table}'")
        exists = cursor.fetchone()[0] > 0
        status = "✓" if exists else "✗"
        print(f"   {status} {table}")
    
    # Check calendar data
    cursor.execute("SELECT COUNT(*) FROM irish_school_calendar")
    cal_count = cursor.fetchone()[0]
    print(f"\n   📅 Calendar events: {cal_count}")
    
    conn.close()


if __name__ == '__main__':
    run_migration()
    verify_migration()
