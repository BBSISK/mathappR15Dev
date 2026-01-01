-- ============================================================
-- Add LC Higher Level Strand and Topics to Database (v2 - simplified)
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < add_lc_hl_strand_v2.sql
-- ============================================================

-- Step 1: Add the LC Higher Level strand (minimal columns)
INSERT OR IGNORE INTO strands (name, icon, color, sort_order)
VALUES ('LC Higher Level', '🎓', '#6366f1', 8);

-- Step 2: Add LC HL topics (minimal columns - no description)
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_calculus_diff', 'Calculus - Differentiation', id, '📈', 1, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_calculus_int', 'Calculus - Integration', id, '📉', 2, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_algebra', 'Algebra', id, '🔤', 3, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_sequences', 'Sequences & Series', id, '🔢', 4, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_complex', 'Complex Numbers', id, '🌀', 5, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_functions', 'Functions', id, '📊', 6, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_financial', 'Financial Maths', id, '💰', 7, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_proof', 'Proof', id, '✓', 8, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_probability', 'Probability', id, '🎲', 9, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_statistics', 'Statistics', id, '📊', 10, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_coord_geom', 'Coordinate Geometry', id, '📐', 11, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_trigonometry', 'Trigonometry', id, '📐', 12, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_geometry', 'Geometry', id, '🔺', 13, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_mensuration', 'Mensuration', id, '📦', 14, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_counting', 'Counting & Combinatorics', id, '🔄', 15, 1
FROM strands WHERE name = 'LC Higher Level';

-- Verify
SELECT 'Strand:' as info, name, id FROM strands WHERE name = 'LC Higher Level';
SELECT 'Topics added:' as info, COUNT(*) as count FROM topics WHERE topic_id LIKE 'lc_hl_%';
SELECT topic_id, display_name FROM topics WHERE topic_id LIKE 'lc_hl_%' ORDER BY sort_order;
