-- ============================================================================
-- AgentMath: Add 3 New Interactive Games to "Numeracy - Interactive Play" Strand
-- ============================================================================
-- Date: December 16, 2025
-- Games: Number Bonds Pop, Place Value Builder, Double Trouble
-- ============================================================================
-- Run with:
-- sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < ADD_THREE_NEW_GAMES.sql
-- ============================================================================

-- Ensure the Interactive Play strand exists (id=10)
INSERT OR IGNORE INTO strands (id, name, sort_order)
VALUES (10, 'Numeracy - Interactive Play', 10);

-- Add Number Bonds Pop (sort_order 7)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('number_bonds', 'Number Bonds Pop', 'circle', 10, 7, 1);

-- Add Place Value Builder (sort_order 8)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('place_value', 'Place Value Builder', 'building', 10, 8, 1);

-- Add Double Trouble (sort_order 9)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('double_trouble', 'Double Trouble', 'bolt', 10, 9, 1);

-- Verification
SELECT '================================================' as '';
SELECT 'Three New Interactive Games Added!' as status;
SELECT '================================================' as '';
SELECT '' as '';
SELECT 'All Interactive Play Topics:' as '';
SELECT sort_order, topic_id, display_name 
FROM topics 
WHERE strand_id = 10 
ORDER BY sort_order;
