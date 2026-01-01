-- ============================================================================
-- AgentMath: Add Addition Blitz and Times Tables Blitz
-- ============================================================================
-- Run with:
-- sqlite3 /home/bbsisk/mathappR14/instance/mathquiz.db < ADD_BLITZ_GAMES.sql
-- ============================================================================

-- Add Addition Blitz
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, sort_order, is_visible)
VALUES ('addition_blitz', 'Addition Blitz', 10, 10, 1);

-- Add Times Tables Blitz
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, sort_order, is_visible)
VALUES ('times_tables_blitz', 'Times Tables Blitz', 10, 11, 1);

-- Verify
SELECT '=== Interactive Play Topics ===' as info;
SELECT topic_id, display_name, sort_order, is_visible 
FROM topics 
WHERE strand_id = 10 
ORDER BY sort_order;

SELECT '' as '';
SELECT '=== Total Topics in Interactive Play ===' as info;
SELECT COUNT(*) as count FROM topics WHERE strand_id = 10;
