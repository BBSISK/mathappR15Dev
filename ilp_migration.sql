-- =====================================================
-- ILP ENGINE DATABASE MIGRATION
-- Phase 12: Reactive Recommendations System
-- Run this manually if auto-creation fails
-- =====================================================

-- Question skill tags table
-- Links questions to skill tags for granular analysis
CREATE TABLE IF NOT EXISTS question_skill_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    skill_tag VARCHAR(50) NOT NULL,
    weight DECIMAL(3,2) DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_qst_question ON question_skill_tags(question_id);
CREATE INDEX IF NOT EXISTS idx_qst_skill ON question_skill_tags(skill_tag);

-- ILP recommendations table
-- Stores pending/applied/rejected plan modifications
CREATE TABLE IF NOT EXISTS ilp_recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',  -- pending, accepted, rejected, auto_applied, expired
    responded_at TIMESTAMP,
    analysis_data TEXT,      -- JSON: raw analysis results
    recommendations TEXT,    -- JSON: list of recommendations
    modifications TEXT,      -- JSON: planned plan changes
    reason_summary TEXT,     -- Human-readable summary
    auto_applied BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Indexes for recommendations
CREATE INDEX IF NOT EXISTS idx_ilp_rec_user ON ilp_recommendations(user_id);
CREATE INDEX IF NOT EXISTS idx_ilp_rec_guest ON ilp_recommendations(guest_code);
CREATE INDEX IF NOT EXISTS idx_ilp_rec_status ON ilp_recommendations(status);
CREATE INDEX IF NOT EXISTS idx_ilp_rec_expires ON ilp_recommendations(expires_at);

-- Modification log table
-- Audit trail of all plan modifications made by ILP engine
CREATE TABLE IF NOT EXISTS ilp_modification_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recommendation_id INTEGER,
    user_id INTEGER,
    guest_code VARCHAR(50),
    action VARCHAR(30) NOT NULL,  -- insert_topic, delay_topic, extend_practice, etc.
    topic_id VARCHAR(50),
    details TEXT,                 -- JSON: action-specific details
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reverted_at TIMESTAMP,        -- If user/teacher reverts the change
    FOREIGN KEY (recommendation_id) REFERENCES ilp_recommendations(id)
);

-- Index for modification log
CREATE INDEX IF NOT EXISTS idx_ilp_mod_rec ON ilp_modification_log(recommendation_id);
CREATE INDEX IF NOT EXISTS idx_ilp_mod_user ON ilp_modification_log(user_id);

-- =====================================================
-- SAMPLE QUERIES FOR TESTING
-- =====================================================

-- Check if tables were created
-- SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'ilp%' OR name LIKE 'question_skill%';

-- Count skill tags per topic (after running auto-tagger)
-- SELECT q.topic, COUNT(qst.id) as tag_count 
-- FROM questions q 
-- LEFT JOIN question_skill_tags qst ON q.id = qst.question_id 
-- GROUP BY q.topic;

-- Get skill breakdown for a student
-- SELECT qst.skill_tag, 
--        COUNT(*) as total,
--        SUM(CASE WHEN ua.is_correct THEN 1 ELSE 0 END) as correct,
--        ROUND(100.0 * SUM(CASE WHEN ua.is_correct THEN 1 ELSE 0 END) / COUNT(*), 1) as accuracy
-- FROM user_answers ua
-- JOIN question_skill_tags qst ON ua.question_id = qst.question_id
-- WHERE ua.user_id = ?
-- GROUP BY qst.skill_tag
-- ORDER BY accuracy ASC;
