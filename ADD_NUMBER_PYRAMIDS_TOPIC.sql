-- ============================================================================
-- AgentMath: Add Number Pyramids Topic to Numeracy Strand
-- ============================================================================
-- Date: December 15, 2025
-- Database: /home/bbsisk/mathapp/instance/mathquiz.db
-- Numeracy strand_id = 6
-- ============================================================================

-- Insert Number Pyramids topic into Numeracy strand
INSERT OR IGNORE INTO topics (
    topic_id, 
    display_name, 
    icon,
    strand_id,
    sort_order,
    is_visible
)
VALUES (
    'number_pyramids',
    'Number Pyramids',
    'triangle',
    6,
    14,
    1
);

-- Verify the topic was added
SELECT 'Number Pyramids topic added successfully!' as status;
SELECT id, topic_id, display_name, strand_id, is_visible FROM topics WHERE topic_id = 'number_pyramids';
