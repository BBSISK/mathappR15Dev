-- ============================================================================
-- AgentMath: Add Server-Side Duplicate Prevention for Adaptive Quiz
-- ============================================================================
-- Date: December 15, 2025
-- Purpose: Create user_adaptive_question_history table to track which questions
--          each student has seen in Learning in Stages mode
-- ============================================================================

-- Create the table
CREATE TABLE IF NOT EXISTS user_adaptive_question_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code VARCHAR(20),
    question_id INTEGER NOT NULL,
    topic VARCHAR(50) NOT NULL,
    difficulty_level INTEGER NOT NULL,
    seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create indexes for fast lookups
CREATE INDEX IF NOT EXISTS idx_adaptive_user_question 
    ON user_adaptive_question_history(user_id, question_id);

CREATE INDEX IF NOT EXISTS idx_adaptive_guest_question 
    ON user_adaptive_question_history(guest_code, question_id);

CREATE INDEX IF NOT EXISTS idx_adaptive_user_topic_level 
    ON user_adaptive_question_history(user_id, topic, difficulty_level);

CREATE INDEX IF NOT EXISTS idx_adaptive_guest_topic_level 
    ON user_adaptive_question_history(guest_code, topic, difficulty_level);

-- Verify the table was created
SELECT 'Table created successfully!' as status;
SELECT COUNT(*) as record_count FROM user_adaptive_question_history;

-- ============================================================================
-- NOTES:
-- ============================================================================
-- 
-- After running this script, the adaptive quiz will:
-- 1. Track all questions shown to each user/guest per topic/level
-- 2. Automatically exclude seen questions from selection
-- 3. Reset history when all questions at a level have been seen
-- 4. Work across page refreshes, sessions, and devices
--
-- Admin endpoints available:
-- GET  /api/admin/adaptive-question-history/stats - View statistics
-- POST /api/admin/adaptive-question-history/clear - Clear history
--
-- To clear history for testing:
-- DELETE FROM user_adaptive_question_history;
-- ============================================================================
