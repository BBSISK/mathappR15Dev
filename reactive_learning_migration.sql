-- Migration: Passport System + Reactive Learning Engine
-- Date: 2025-12-20
-- Purpose: Complete passport system with preferences, stamps, and reactive learning

-- User preferences table (for storing passport data)
CREATE TABLE IF NOT EXISTS user_preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    key TEXT NOT NULL,
    value TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, key),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Guest preferences table
CREATE TABLE IF NOT EXISTS guest_preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_code TEXT NOT NULL,
    key TEXT NOT NULL,
    value TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(guest_code, key)
);

-- Passport stamps table
CREATE TABLE IF NOT EXISTS passport_stamps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code TEXT,
    destination_id TEXT NOT NULL,
    tier TEXT NOT NULL,  -- 'bronze', 'silver', 'gold'
    earned_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, destination_id),
    UNIQUE(guest_code, destination_id)
);

-- Track individual question responses for reactive learning analysis
CREATE TABLE IF NOT EXISTS passport_performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code TEXT,
    topic TEXT NOT NULL,
    level INTEGER NOT NULL,
    question_number INTEGER NOT NULL,
    is_correct BOOLEAN NOT NULL,
    time_taken_seconds INTEGER,
    session_id TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Store recommendations for each topic
CREATE TABLE IF NOT EXISTS passport_recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code TEXT,
    topic TEXT NOT NULL,
    current_level INTEGER NOT NULL,
    recommended_level INTEGER NOT NULL,
    recommendation_type TEXT NOT NULL,
    confidence_score REAL,
    reason TEXT,
    is_acknowledged BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    acknowledged_at DATETIME,
    UNIQUE(user_id, topic),
    UNIQUE(guest_code, topic)
);

-- Track level changes triggered by reactive engine
CREATE TABLE IF NOT EXISTS passport_level_adjustments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code TEXT,
    topic TEXT NOT NULL,
    from_level INTEGER NOT NULL,
    to_level INTEGER NOT NULL,
    adjustment_reason TEXT NOT NULL,
    performance_accuracy REAL,
    questions_analyzed INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_user_pref ON user_preferences(user_id, key);
CREATE INDEX IF NOT EXISTS idx_guest_pref ON guest_preferences(guest_code, key);
CREATE INDEX IF NOT EXISTS idx_stamps_user ON passport_stamps(user_id);
CREATE INDEX IF NOT EXISTS idx_stamps_guest ON passport_stamps(guest_code);
CREATE INDEX IF NOT EXISTS idx_passport_perf_user ON passport_performance(user_id, topic, session_id);
CREATE INDEX IF NOT EXISTS idx_passport_perf_guest ON passport_performance(guest_code, topic, session_id);
CREATE INDEX IF NOT EXISTS idx_passport_rec_user ON passport_recommendations(user_id, topic);
CREATE INDEX IF NOT EXISTS idx_passport_rec_guest ON passport_recommendations(guest_code, topic);
