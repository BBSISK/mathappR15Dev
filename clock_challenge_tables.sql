-- =====================================================
-- CLOCK CHALLENGE: Table Verification & Creation
-- Run this to ensure all required tables exist
-- =====================================================

-- Check if tables exist
SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'clock_challenge%';

-- Create clock_challenge_state if missing
CREATE TABLE IF NOT EXISTS clock_challenge_state (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code TEXT,
    topic TEXT NOT NULL,
    level INTEGER NOT NULL,
    clock_available INTEGER DEFAULT 1,
    clock_completed INTEGER DEFAULT 0,
    attempts INTEGER DEFAULT 0,
    best_time_remaining INTEGER,
    last_attempt_at DATETIME,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, topic, level),
    UNIQUE(guest_code, topic, level)
);

-- Create clock_challenge_timing if missing
CREATE TABLE IF NOT EXISTS clock_challenge_timing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code TEXT,
    topic TEXT NOT NULL,
    level INTEGER NOT NULL,
    session_id TEXT NOT NULL,
    time_allowed INTEGER NOT NULL,
    started_at DATETIME NOT NULL,
    completed_at DATETIME,
    time_remaining INTEGER,
    questions_answered INTEGER DEFAULT 0,
    questions_correct INTEGER DEFAULT 0,
    bonus_tier TEXT,
    bonus_points INTEGER DEFAULT 0,
    success INTEGER DEFAULT 0
);

-- Create clock_challenge_intro_seen if missing
CREATE TABLE IF NOT EXISTS clock_challenge_intro_seen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    guest_code TEXT UNIQUE,
    seen_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Verify tables were created
SELECT 'Tables after creation:' as status;
SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'clock_challenge%';

-- Check sample data
SELECT 'clock_challenge_state rows:' as info, COUNT(*) as count FROM clock_challenge_state;
SELECT 'clock_challenge_timing rows:' as info, COUNT(*) as count FROM clock_challenge_timing;
SELECT 'clock_challenge_intro_seen rows:' as info, COUNT(*) as count FROM clock_challenge_intro_seen;

-- =====================================================
-- DEBUG: Test the check query directly
-- Replace 'YOUR_GUEST_CODE' with an actual guest code to test
-- =====================================================

/*
SELECT clock_available, clock_completed, attempts, best_time_remaining
FROM clock_challenge_state 
WHERE guest_code = 'YOUR_GUEST_CODE' AND topic = 'introductory_algebra' AND level = 6;
*/

-- If no rows returned, the API defaults to available=True
-- If row exists with clock_available=0, the clock is NOT available

-- =====================================================
-- RESET: Make clock challenge available again for testing
-- Uncomment and modify as needed
-- =====================================================

/*
-- Option 1: Delete all state (fresh start)
DELETE FROM clock_challenge_state;
DELETE FROM clock_challenge_timing;
DELETE FROM clock_challenge_intro_seen;

-- Option 2: Reset just for a specific user/guest
UPDATE clock_challenge_state SET clock_available = 1 WHERE guest_code = 'YOUR_GUEST_CODE';

-- Option 3: Reset intro seen flag (to see intro again)
DELETE FROM clock_challenge_intro_seen WHERE guest_code = 'YOUR_GUEST_CODE';
*/
