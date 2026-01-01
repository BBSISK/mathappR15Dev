-- ============================================================================
-- AgentMath: Add Flow Sums Topic to Numeracy Strand
-- ============================================================================
-- Date: December 15, 2025
-- Database: /home/bbsisk/mathapp/instance/mathquiz.db
-- Numeracy strand_id = 6
-- ============================================================================

-- Insert Flow Sums topic into Numeracy strand
INSERT OR IGNORE INTO topics (
    topic_id, 
    display_name, 
    icon,
    strand_id,
    sort_order,
    is_visible
)
VALUES (
    'flow_sums',
    'Flow Sums',
    'waves',
    6,
    13,
    1
);

-- Verify the topic was added
SELECT 'Flow Sums topic added successfully!' as status;
SELECT id, topic_id, display_name, strand_id, is_visible FROM topics WHERE topic_id = 'flow_sums';
