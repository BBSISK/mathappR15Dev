-- ============================================================================
-- AgentMath: DIAGNOSE AND FIX Interactive Play Topics
-- ============================================================================
-- Run with:
-- sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < FIX_INTERACTIVE_PLAY_TOPICS.sql
-- ============================================================================

-- Show current structure
.headers on
.mode column

SELECT '=== TOPICS TABLE STRUCTURE ===' as info;
PRAGMA table_info(topics);

SELECT '' as '';
SELECT '=== CURRENT TOPICS IN STRAND 10 ===' as info;
SELECT topic_id, display_name, strand_id, sort_order FROM topics WHERE strand_id = 10 ORDER BY sort_order;

-- Now insert the 3 new topics
-- Using INSERT OR IGNORE to avoid duplicates
SELECT '' as '';
SELECT '=== INSERTING NEW TOPICS ===' as info;

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, sort_order)
VALUES ('number_bonds', 'Number Bonds Pop', 10, 7);

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, sort_order)
VALUES ('place_value', 'Place Value Builder', 10, 8);

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, sort_order)
VALUES ('double_trouble', 'Double Trouble', 10, 9);

SELECT '' as '';
SELECT '=== UPDATED TOPICS IN STRAND 10 ===' as info;
SELECT topic_id, display_name, strand_id, sort_order FROM topics WHERE strand_id = 10 ORDER BY sort_order;

SELECT '' as '';
SELECT '=== TOPIC COUNTS BY STRAND ===' as info;
SELECT s.id, s.name, COUNT(t.topic_id) as topics 
FROM strands s 
LEFT JOIN topics t ON s.id = t.strand_id 
GROUP BY s.id 
ORDER BY s.sort_order
LIMIT 5;

SELECT '' as '';
SELECT '=== DONE! Reload web app to see changes ===' as info;
