-- ============================================================================
-- AgentMath: Add ALL Interactive Topics to "Numeracy - Interactive Play" Strand
-- ============================================================================
-- Date: December 16, 2025
-- Database: /home/bbsisk/mathapp/instance/mathquiz.db
-- ============================================================================
--
-- This script:
-- 1. Creates the new "Numeracy - Interactive Play" strand (id=10)
-- 2. Adds all 6 interactive topics in the correct order:
--    1. Mastering Counting
--    2. Words & Numbers  
--    3. Ordering & Number Lines (NEW)
--    4. Flow Sums
--    5. Number Pyramids
--    6. Code Breaker
--
-- Run with:
-- sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < ADD_ALL_INTERACTIVE_TOPICS.sql
--
-- ============================================================================

-- Create the new strand for Interactive Play (id=10)
-- Note: strands table doesn't have is_visible column
INSERT OR IGNORE INTO strands (id, name, sort_order)
VALUES (10, 'Numeracy - Interactive Play', 10);

-- 1. Mastering Counting (first - basic counting)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('mastering_counting', 'Mastering Counting', 'list-ol', 10, 1, 1);

-- 2. Words & Numbers (word-number matching)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('words_to_numbers', 'Words & Numbers', 'font', 10, 2, 1);

-- 3. Ordering & Number Lines (NEW - ordering and magnitude)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('ordering_magnitude', 'Ordering & Number Lines', 'ruler-horizontal', 10, 3, 1);

-- 4. Flow Sums (arithmetic chains)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('flow_sums', 'Flow Sums', 'water', 10, 4, 1);

-- 5. Number Pyramids (addition pyramids)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('number_pyramids', 'Number Pyramids', 'triangle', 10, 5, 1);

-- 6. Code Breaker (logic puzzles - most challenging)
INSERT OR REPLACE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
VALUES ('code_breaker', 'Code Breaker', 'lock', 10, 6, 1);

-- Verification
SELECT '================================================' as '';
SELECT 'Interactive Play Strand Setup Complete!' as status;
SELECT '================================================' as '';
SELECT '' as '';
SELECT 'Strand:' as '';
SELECT id, name, sort_order FROM strands WHERE id = 10;
SELECT '' as '';
SELECT 'Topics in order:' as '';
SELECT sort_order, topic_id, display_name 
FROM topics 
WHERE strand_id = 10 
ORDER BY sort_order;
