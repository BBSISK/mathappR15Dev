-- ============================================================================
-- AgentMath: Fix Interactive Strand (without is_visible column)
-- ============================================================================
-- Run with:
-- sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < FIX_INTERACTIVE_STRAND.sql
-- ============================================================================

-- Check if strand 10 exists
SELECT '=== Checking for strand 10 ===' as '';
SELECT id, name FROM strands WHERE id = 10;

-- Create strand WITHOUT is_visible column
INSERT OR IGNORE INTO strands (id, name, sort_order)
VALUES (10, 'Numeracy - Interactive Play', 10);

-- Verify
SELECT '' as '';
SELECT '=== All Strands ===' as '';
SELECT id, name, sort_order FROM strands ORDER BY sort_order;

SELECT '' as '';
SELECT '=== Topics in Interactive Play strand ===' as '';
SELECT topic_id, display_name, sort_order FROM topics WHERE strand_id = 10 ORDER BY sort_order;
