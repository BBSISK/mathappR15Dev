#!/usr/bin/env python3
"""
Adaptive Learning System - Database Migration
==============================================
Run this script to add all tables required for the Adaptive Learning System.

Usage:
    python adaptive_learning_migration.py

This script:
1. Creates new tables: topic_mastery, question_performance, skill_prerequisites, 
   learning_recommendations, adaptive_quiz_config
2. Migrates existing TopicProgress data to new topic_mastery table
3. Seeds skill_prerequisites with Irish Junior Cycle curriculum relationships
4. Sets up default configuration values

Safe to run multiple times - checks for existing tables/data.
"""

import sqlite3
import os
from datetime import datetime, timedelta

# Database path
DB_PATH = 'instance/mathquiz.db'

def get_connection():
    """Get database connection"""
    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}")
        print("Please run this script from the mathapp-main directory")
        exit(1)
    return sqlite3.connect(DB_PATH)

def table_exists(cursor, table_name):
    """Check if a table already exists"""
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name=?
    """, (table_name,))
    return cursor.fetchone() is not None

def create_topic_mastery_table(cursor):
    """Create topic_mastery table for detailed mastery tracking"""
    if table_exists(cursor, 'topic_mastery'):
        print("✓ topic_mastery table already exists")
        return False
    
    cursor.execute("""
        CREATE TABLE topic_mastery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic VARCHAR(50) NOT NULL,
            difficulty VARCHAR(20) NOT NULL,
            
            -- Mastery metrics
            mastery_level REAL DEFAULT 0.0,
            confidence_score REAL DEFAULT 0.0,
            total_attempts INTEGER DEFAULT 0,
            correct_attempts INTEGER DEFAULT 0,
            streak_current INTEGER DEFAULT 0,
            streak_best INTEGER DEFAULT 0,
            
            -- Recent performance (JSON array of last 10 scores)
            recent_scores TEXT DEFAULT '[]',
            
            -- Spaced repetition fields
            last_attempt_at DATETIME,
            next_review_at DATETIME,
            review_interval_days INTEGER DEFAULT 1,
            ease_factor REAL DEFAULT 2.5,
            
            -- Status
            is_mastered BOOLEAN DEFAULT 0,
            mastered_at DATETIME,
            
            -- Timestamps
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, topic, difficulty)
        )
    """)
    
    # Create indexes for fast lookups
    cursor.execute("""
        CREATE INDEX idx_topic_mastery_user ON topic_mastery(user_id)
    """)
    cursor.execute("""
        CREATE INDEX idx_topic_mastery_topic ON topic_mastery(topic)
    """)
    cursor.execute("""
        CREATE INDEX idx_topic_mastery_review ON topic_mastery(next_review_at)
    """)
    cursor.execute("""
        CREATE INDEX idx_topic_mastery_mastered ON topic_mastery(is_mastered)
    """)
    
    print("✓ Created topic_mastery table")
    return True

def create_question_performance_table(cursor):
    """Create question_performance table for per-question tracking"""
    if table_exists(cursor, 'question_performance'):
        print("✓ question_performance table already exists")
        return False
    
    cursor.execute("""
        CREATE TABLE question_performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            topic VARCHAR(50) NOT NULL,
            difficulty VARCHAR(20) NOT NULL,
            
            -- Performance metrics
            attempts INTEGER DEFAULT 0,
            correct INTEGER DEFAULT 0,
            last_attempt_at DATETIME,
            last_response_time INTEGER,
            avg_response_time REAL,
            
            -- Flags
            is_problematic BOOLEAN DEFAULT 0,
            
            -- Timestamps
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE,
            UNIQUE(user_id, question_id)
        )
    """)
    
    # Create indexes
    cursor.execute("""
        CREATE INDEX idx_question_perf_user ON question_performance(user_id)
    """)
    cursor.execute("""
        CREATE INDEX idx_question_perf_question ON question_performance(question_id)
    """)
    cursor.execute("""
        CREATE INDEX idx_question_perf_problematic ON question_performance(user_id, is_problematic)
    """)
    
    print("✓ Created question_performance table")
    return True

def create_skill_prerequisites_table(cursor):
    """Create skill_prerequisites table for topic dependencies"""
    if table_exists(cursor, 'skill_prerequisites'):
        print("✓ skill_prerequisites table already exists")
        return False
    
    cursor.execute("""
        CREATE TABLE skill_prerequisites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic VARCHAR(50) NOT NULL,
            prerequisite_topic VARCHAR(50) NOT NULL,
            required_mastery_level REAL DEFAULT 0.7,
            difficulty_context VARCHAR(20),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            
            UNIQUE(topic, prerequisite_topic, difficulty_context)
        )
    """)
    
    cursor.execute("""
        CREATE INDEX idx_prerequisites_topic ON skill_prerequisites(topic)
    """)
    
    print("✓ Created skill_prerequisites table")
    return True

def create_learning_recommendations_table(cursor):
    """Create learning_recommendations table for personalised suggestions"""
    if table_exists(cursor, 'learning_recommendations'):
        print("✓ learning_recommendations table already exists")
        return False
    
    cursor.execute("""
        CREATE TABLE learning_recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            recommendation_type VARCHAR(30) NOT NULL,
            topic VARCHAR(50) NOT NULL,
            difficulty VARCHAR(20),
            priority INTEGER DEFAULT 1,
            reason VARCHAR(200),
            is_active BOOLEAN DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            expires_at DATETIME,
            completed_at DATETIME,
            
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)
    
    cursor.execute("""
        CREATE INDEX idx_recommendations_user ON learning_recommendations(user_id, is_active)
    """)
    cursor.execute("""
        CREATE INDEX idx_recommendations_type ON learning_recommendations(recommendation_type)
    """)
    
    print("✓ Created learning_recommendations table")
    return True

def create_adaptive_quiz_config_table(cursor):
    """Create adaptive_quiz_config table for configurable thresholds"""
    if table_exists(cursor, 'adaptive_quiz_config'):
        print("✓ adaptive_quiz_config table already exists")
        return False
    
    cursor.execute("""
        CREATE TABLE adaptive_quiz_config (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic VARCHAR(50),
            mastery_threshold REAL DEFAULT 0.85,
            promotion_threshold REAL DEFAULT 0.80,
            demotion_threshold REAL DEFAULT 0.40,
            min_attempts_for_promotion INTEGER DEFAULT 20,
            review_interval_initial INTEGER DEFAULT 1,
            review_interval_max INTEGER DEFAULT 90,
            ease_factor_default REAL DEFAULT 2.5,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            
            UNIQUE(topic)
        )
    """)
    
    print("✓ Created adaptive_quiz_config table")
    return True

def migrate_existing_progress(cursor):
    """Migrate existing TopicProgress data to topic_mastery"""
    # Check if there's existing data to migrate
    cursor.execute("SELECT COUNT(*) FROM topic_mastery")
    if cursor.fetchone()[0] > 0:
        print("✓ topic_mastery already has data - skipping migration")
        return
    
    # Check if topic_progress table exists and has data
    if not table_exists(cursor, 'topic_progress'):
        print("ℹ No topic_progress table to migrate from")
        return
    
    cursor.execute("SELECT COUNT(*) FROM topic_progress")
    count = cursor.fetchone()[0]
    if count == 0:
        print("ℹ No existing progress data to migrate")
        return
    
    print(f"Migrating {count} records from topic_progress...")
    
    cursor.execute("""
        INSERT INTO topic_mastery (
            user_id, topic, difficulty, 
            mastery_level, total_attempts, correct_attempts,
            is_mastered, last_attempt_at, created_at, updated_at
        )
        SELECT 
            user_id, topic, difficulty,
            CASE 
                WHEN total_questions_answered > 0 
                THEN CAST(total_correct AS REAL) / total_questions_answered
                ELSE 0.0
            END as mastery_level,
            total_questions_answered,
            total_correct,
            is_mastered,
            last_attempt_at,
            CURRENT_TIMESTAMP,
            CURRENT_TIMESTAMP
        FROM topic_progress
        WHERE user_id IS NOT NULL
    """)
    
    migrated = cursor.rowcount
    print(f"✓ Migrated {migrated} records to topic_mastery")

def seed_skill_prerequisites(cursor):
    """Seed skill_prerequisites with Junior Cycle curriculum relationships"""
    cursor.execute("SELECT COUNT(*) FROM skill_prerequisites")
    if cursor.fetchone()[0] > 0:
        print("✓ skill_prerequisites already has data - skipping seed")
        return
    
    prerequisites = [
        # Number Strand
        ('fractions', 'arithmetic', 0.7, None),
        ('decimals', 'arithmetic', 0.7, None),
        ('decimals', 'fractions', 0.6, None),
        ('multiplication_division', 'arithmetic', 0.7, None),
        ('bodmas', 'arithmetic', 0.7, None),
        ('bodmas', 'multiplication_division', 0.6, None),
        ('number_systems', 'arithmetic', 0.6, None),
        ('surds', 'number_systems', 0.7, None),
        ('sets', 'arithmetic', 0.6, None),
        
        # Algebra Strand
        ('introductory_algebra', 'arithmetic', 0.7, None),
        ('patterns', 'arithmetic', 0.6, None),
        ('functions', 'introductory_algebra', 0.7, None),
        ('solving_equations', 'introductory_algebra', 0.7, None),
        ('simplifying_expressions', 'introductory_algebra', 0.7, None),
        ('expanding_factorising', 'simplifying_expressions', 0.7, None),
        ('simultaneous_equations', 'solving_equations', 0.7, None),
        ('complex_numbers_intro', 'surds', 0.7, None),
        ('complex_numbers_expanded', 'complex_numbers_intro', 0.8, None),
        
        # Geometry Strand
        ('coordinate_geometry', 'introductory_algebra', 0.7, None),
        ('trigonometry', 'coordinate_geometry', 0.6, None),
        
        # Statistics Strand
        ('probability', 'fractions', 0.7, None),
        ('probability', 'decimals', 0.6, None),
        ('descriptive_statistics', 'arithmetic', 0.6, None),
    ]
    
    cursor.executemany("""
        INSERT INTO skill_prerequisites (topic, prerequisite_topic, required_mastery_level, difficulty_context)
        VALUES (?, ?, ?, ?)
    """, prerequisites)
    
    print(f"✓ Seeded {len(prerequisites)} skill prerequisites")

def seed_default_config(cursor):
    """Seed default adaptive configuration"""
    cursor.execute("SELECT COUNT(*) FROM adaptive_quiz_config")
    if cursor.fetchone()[0] > 0:
        print("✓ adaptive_quiz_config already has data - skipping seed")
        return
    
    # Insert global default (topic = NULL)
    cursor.execute("""
        INSERT INTO adaptive_quiz_config (
            topic, mastery_threshold, promotion_threshold, demotion_threshold,
            min_attempts_for_promotion, review_interval_initial, review_interval_max
        ) VALUES (NULL, 0.85, 0.80, 0.40, 20, 1, 90)
    """)
    
    print("✓ Seeded default adaptive configuration")

def add_user_stats_columns(cursor):
    """Add new columns to user_stats for adaptive tracking"""
    # Check if columns already exist
    cursor.execute("PRAGMA table_info(user_stats)")
    columns = [col[1] for col in cursor.fetchall()]
    
    new_columns = [
        ('adaptive_enabled', 'BOOLEAN DEFAULT 1'),
        ('preferred_session_length', 'INTEGER DEFAULT 10'),
        ('last_recommendation_at', 'DATETIME'),
    ]
    
    added = 0
    for col_name, col_def in new_columns:
        if col_name not in columns:
            cursor.execute(f"ALTER TABLE user_stats ADD COLUMN {col_name} {col_def}")
            added += 1
    
    if added:
        print(f"✓ Added {added} new columns to user_stats")
    else:
        print("✓ user_stats already has adaptive columns")

def verify_migration(cursor):
    """Verify all tables were created successfully"""
    required_tables = [
        'topic_mastery',
        'question_performance', 
        'skill_prerequisites',
        'learning_recommendations',
        'adaptive_quiz_config'
    ]
    
    print("\n--- Verification ---")
    all_good = True
    for table in required_tables:
        if table_exists(cursor, table):
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"✓ {table}: {count} records")
        else:
            print(f"✗ {table}: MISSING!")
            all_good = False
    
    return all_good

def main():
    """Run the migration"""
    print("=" * 60)
    print("Adaptive Learning System - Database Migration")
    print("=" * 60)
    print(f"Database: {DB_PATH}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("-" * 60)
    
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Create tables
        print("\n[1/6] Creating topic_mastery table...")
        create_topic_mastery_table(cursor)
        
        print("\n[2/6] Creating question_performance table...")
        create_question_performance_table(cursor)
        
        print("\n[3/6] Creating skill_prerequisites table...")
        create_skill_prerequisites_table(cursor)
        
        print("\n[4/6] Creating learning_recommendations table...")
        create_learning_recommendations_table(cursor)
        
        print("\n[5/6] Creating adaptive_quiz_config table...")
        create_adaptive_quiz_config_table(cursor)
        
        print("\n[6/6] Adding columns to user_stats...")
        add_user_stats_columns(cursor)
        
        # Commit table creation
        conn.commit()
        
        # Migrate data
        print("\n--- Data Migration ---")
        migrate_existing_progress(cursor)
        seed_skill_prerequisites(cursor)
        seed_default_config(cursor)
        
        # Commit data
        conn.commit()
        
        # Verify
        if verify_migration(cursor):
            print("\n" + "=" * 60)
            print("✓ MIGRATION COMPLETE - All tables created successfully!")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("⚠ MIGRATION INCOMPLETE - Some tables missing!")
            print("=" * 60)
            
    except Exception as e:
        conn.rollback()
        print(f"\n✗ ERROR: {e}")
        print("Migration rolled back.")
        raise
    finally:
        conn.close()

if __name__ == '__main__':
    main()
