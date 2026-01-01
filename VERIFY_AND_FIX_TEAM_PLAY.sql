-- ============================================================================
-- AgentMath: Verify and Fix Team Play Tables
-- ============================================================================
-- Run with:
-- sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < VERIFY_AND_FIX_TEAM_PLAY.sql
-- ============================================================================

-- Check existing tables
SELECT '=== Checking for Team Play tables ===' as '';
SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'team%';

-- Create tables if they don't exist
SELECT '' as '';
SELECT '=== Creating tables if needed ===' as '';

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
    last_activity TIMESTAMP
);

CREATE TABLE IF NOT EXISTS team_session_players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    user_id INTEGER,
    guest_code VARCHAR(20),
    display_name VARCHAR(50),
    is_organiser BOOLEAN DEFAULT 0,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'active'
);

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
    locked_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS team_session_invites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    invited_user_id INTEGER,
    invited_guest_code VARCHAR(20),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP
);

-- Create indexes if they don't exist
CREATE INDEX IF NOT EXISTS idx_team_sessions_code ON team_sessions(session_code);
CREATE INDEX IF NOT EXISTS idx_team_sessions_status ON team_sessions(status);
CREATE INDEX IF NOT EXISTS idx_team_players_session ON team_session_players(session_id);

-- Verify
SELECT '' as '';
SELECT '=== Tables now present ===' as '';
SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'team%';
SELECT '=== Done! ===' as '';
