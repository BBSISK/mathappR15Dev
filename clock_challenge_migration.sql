-- =====================================================
-- CLOCK CHALLENGE DATABASE MIGRATION
-- Beat the Clock feature for Levels 6-10
-- =====================================================

-- Table to track clock challenge state per user/topic/level
CREATE TABLE IF NOT EXISTS clock_challenge_state (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code VARCHAR(50),
    topic VARCHAR(100) NOT NULL,
    level INTEGER NOT NULL,
    
    -- State flags
    clock_available BOOLEAN DEFAULT 1,       -- Can they attempt?
    clock_completed BOOLEAN DEFAULT 0,       -- Have they beaten it?
    attempts INTEGER DEFAULT 0,              -- Total attempts at this level
    
    -- Best performance (for potential leaderboard)
    best_time_remaining INTEGER,             -- Seconds remaining on best run
    best_bonus_earned INTEGER,               -- Bonus points from best run
    
    -- Timestamps
    last_attempt_at DATETIME,
    first_completed_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Constraints
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE(user_id, topic, level),
    UNIQUE(guest_code, topic, level)
);

-- Table to collect timing data for future calibration
CREATE TABLE IF NOT EXISTS clock_challenge_timing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code VARCHAR(50),
    topic VARCHAR(100) NOT NULL,
    level INTEGER NOT NULL,
    
    -- Session data
    session_id VARCHAR(50),                  -- Unique session identifier
    questions_answered INTEGER DEFAULT 0,
    questions_correct INTEGER DEFAULT 0,
    
    -- Time tracking
    time_allowed INTEGER NOT NULL,           -- Total seconds allowed
    time_used INTEGER,                       -- Seconds used
    time_remaining INTEGER,                  -- Seconds remaining (or 0 if timeout)
    
    -- Penalties
    wrong_answer_penalties INTEGER DEFAULT 0, -- Total penalty seconds
    
    -- Outcome
    completed BOOLEAN DEFAULT 0,             -- Did they finish in time?
    bonus_tier VARCHAR(20),                  -- 'lightning', 'fast', 'on_time', or NULL
    bonus_points INTEGER DEFAULT 0,
    
    -- Timestamps
    started_at DATETIME,
    ended_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Table to track if user has seen the intro splash
CREATE TABLE IF NOT EXISTS clock_challenge_intro_seen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code VARCHAR(50),
    seen_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE(user_id),
    UNIQUE(guest_code)
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_clock_state_user ON clock_challenge_state(user_id, topic, level);
CREATE INDEX IF NOT EXISTS idx_clock_state_guest ON clock_challenge_state(guest_code, topic, level);
CREATE INDEX IF NOT EXISTS idx_clock_timing_topic_level ON clock_challenge_timing(topic, level);
CREATE INDEX IF NOT EXISTS idx_clock_timing_completed ON clock_challenge_timing(completed, level);

-- View for aggregated timing stats (for future calibration)
-- Note: SQLite doesn't support CREATE OR REPLACE VIEW, so we drop first
DROP VIEW IF EXISTS clock_challenge_stats;
CREATE VIEW clock_challenge_stats AS
SELECT 
    topic,
    level,
    COUNT(*) as total_attempts,
    SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as successful_attempts,
    ROUND(AVG(CASE WHEN completed = 1 THEN time_used END), 1) as avg_completion_time,
    ROUND(100.0 * SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) / COUNT(*), 1) as success_rate
FROM clock_challenge_timing
GROUP BY topic, level;
