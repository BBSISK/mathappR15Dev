"""
Team Play Database Migration Script
Run this once to create the required tables for Team Play functionality.

Usage:
    python team_play_migration.py

Or from Flask shell:
    from team_play_migration import run_migration
    run_migration(db)
"""

from datetime import datetime

MIGRATION_SQL = """
-- ========================================
-- Team Play Database Tables
-- AgentMath - December 2025
-- ========================================

-- Team Play Sessions
CREATE TABLE IF NOT EXISTS team_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_code VARCHAR(10) UNIQUE NOT NULL,
    organiser_user_id INTEGER,
    organiser_guest_code VARCHAR(20),
    topic VARCHAR(50) NOT NULL,
    difficulty_levels VARCHAR(20) DEFAULT '1-12',
    question_count INTEGER DEFAULT 10,
    time_limit_minutes INTEGER,
    status VARCHAR(20) DEFAULT 'waiting',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    last_activity TIMESTAMP,
    FOREIGN KEY (organiser_user_id) REFERENCES users(id)
);

-- Index for quick session lookups
CREATE INDEX IF NOT EXISTS idx_team_sessions_code ON team_sessions(session_code);
CREATE INDEX IF NOT EXISTS idx_team_sessions_status ON team_sessions(status);
CREATE INDEX IF NOT EXISTS idx_team_sessions_organiser ON team_sessions(organiser_user_id);

-- Team Session Players
CREATE TABLE IF NOT EXISTS team_session_players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    user_id INTEGER,
    guest_code VARCHAR(20),
    display_name VARCHAR(50),
    is_organiser BOOLEAN DEFAULT 0,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'active',
    FOREIGN KEY (session_id) REFERENCES team_sessions(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Index for player lookups
CREATE INDEX IF NOT EXISTS idx_team_players_session ON team_session_players(session_id);
CREATE INDEX IF NOT EXISTS idx_team_players_user ON team_session_players(user_id);
CREATE INDEX IF NOT EXISTS idx_team_players_guest ON team_session_players(guest_code);

-- Team Session Answers (per question per player)
CREATE TABLE IF NOT EXISTS team_session_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    question_number INTEGER NOT NULL,
    question_id INTEGER,
    player_id INTEGER NOT NULL,
    answer VARCHAR(1),
    is_correct BOOLEAN DEFAULT 0,
    points_earned INTEGER DEFAULT 0,
    bonus_earned INTEGER DEFAULT 0,
    locked_at TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES team_sessions(id),
    FOREIGN KEY (player_id) REFERENCES team_session_players(id)
);

-- Index for answer lookups
CREATE INDEX IF NOT EXISTS idx_team_answers_session_q ON team_session_answers(session_id, question_number);
CREATE INDEX IF NOT EXISTS idx_team_answers_player ON team_session_answers(player_id);

-- Team Session Invitations
CREATE TABLE IF NOT EXISTS team_session_invites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    invited_user_id INTEGER,
    invited_guest_code VARCHAR(20),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES team_sessions(id),
    FOREIGN KEY (invited_user_id) REFERENCES users(id)
);

-- Index for invitation lookups
CREATE INDEX IF NOT EXISTS idx_team_invites_user ON team_session_invites(invited_user_id);
CREATE INDEX IF NOT EXISTS idx_team_invites_guest ON team_session_invites(invited_guest_code);
CREATE INDEX IF NOT EXISTS idx_team_invites_status ON team_session_invites(status);
"""


def run_migration(db):
    """Run the migration using Flask-SQLAlchemy db object"""
    from sqlalchemy import text
    
    print("=" * 50)
    print("Team Play Database Migration")
    print("=" * 50)
    
    # Split into individual statements and execute
    statements = [s.strip() for s in MIGRATION_SQL.split(';') if s.strip() and not s.strip().startswith('--')]
    
    success_count = 0
    skip_count = 0
    
    for stmt in statements:
        if not stmt:
            continue
        try:
            db.session.execute(text(stmt))
            db.session.commit()
            
            # Extract table/index name for logging
            if 'CREATE TABLE' in stmt.upper():
                name = stmt.split('(')[0].split()[-1]
                print(f"  ✅ Created table: {name}")
            elif 'CREATE INDEX' in stmt.upper():
                name = stmt.split(' ON ')[0].split()[-1]
                print(f"  ✅ Created index: {name}")
            
            success_count += 1
        except Exception as e:
            if 'already exists' in str(e).lower():
                skip_count += 1
            else:
                print(f"  ⚠️  Warning: {e}")
    
    print("-" * 50)
    print(f"Migration complete: {success_count} created, {skip_count} skipped (already exist)")
    print("=" * 50)
    
    return True


def verify_tables(db):
    """Verify all Team Play tables exist"""
    from sqlalchemy import text
    
    tables = ['team_sessions', 'team_session_players', 'team_session_answers', 'team_session_invites']
    
    print("\nVerifying Team Play tables:")
    all_exist = True
    
    for table in tables:
        try:
            result = db.session.execute(text(f"SELECT COUNT(*) FROM {table}")).fetchone()
            print(f"  ✅ {table}: OK ({result[0]} rows)")
        except Exception as e:
            print(f"  ❌ {table}: MISSING")
            all_exist = False
    
    return all_exist


# Standalone execution
if __name__ == '__main__':
    print("This script should be run from your Flask app context.")
    print("")
    print("Option 1 - From Flask shell:")
    print("  flask shell")
    print("  from team_play_migration import run_migration")
    print("  run_migration(db)")
    print("")
    print("Option 2 - Add to your app.py:")
    print("  from team_play_migration import run_migration")
    print("  with app.app_context():")
    print("      run_migration(db)")
