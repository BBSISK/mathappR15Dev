-- Feedback System Migration
-- Run this in your SQLite database

CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,                          -- NULL if guest
    guest_code TEXT,                          -- NULL if logged in
    username TEXT,                            -- Captured for easy reference
    
    -- Feedback content
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),  -- 1-5 stars
    category TEXT DEFAULT 'general',          -- bug, feature, question, praise, general
    feedback_text TEXT NOT NULL,
    
    -- Context
    page_context TEXT,                        -- Which screen they were on
    topic_context TEXT,                       -- Which topic (if in quiz)
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Admin review
    status TEXT DEFAULT 'new',                -- new, reviewed, in_progress, resolved, dismissed
    admin_notes TEXT,
    reviewed_by INTEGER,                      -- Admin user_id
    reviewed_at TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (reviewed_by) REFERENCES users(id)
);

-- Index for faster queries
CREATE INDEX IF NOT EXISTS idx_feedback_status ON feedback(status);
CREATE INDEX IF NOT EXISTS idx_feedback_created ON feedback(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_feedback_user ON feedback(user_id);
