-- ============================================================================
-- AgentMath: Add Code Breaker Topic to Numeracy Strand
-- ============================================================================
-- Date: December 15, 2025
-- Database: /home/bbsisk/mathapp/instance/mathquiz.db
-- Numeracy strand_id = 6
-- ============================================================================
--
-- Run with:
-- sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < ADD_CODE_BREAKER_TOPIC.sql
--
-- ============================================================================

-- Insert Code Breaker topic into Numeracy strand
INSERT OR IGNORE INTO topics (
    topic_id, 
    display_name, 
    icon,
    strand_id,
    sort_order,
    is_visible
)
VALUES (
    'code_breaker',
    'Code Breaker',
    'lock',
    6,
    15,
    1
);

-- Verify the topic was added
SELECT 'Code Breaker topic added successfully!' as status;
SELECT id, topic_id, display_name, strand_id, is_visible FROM topics WHERE topic_id = 'code_breaker';
