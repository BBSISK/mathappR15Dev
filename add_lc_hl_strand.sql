-- ============================================================
-- Add LC Higher Level Strand and Topics to Database
-- Run on PythonAnywhere: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < add_lc_hl_strand.sql
-- ============================================================

-- Step 1: Add the LC Higher Level strand
INSERT OR IGNORE INTO strands (name, description, icon, color, sort_order, is_visible)
VALUES ('LC Higher Level', 'Leaving Certificate Higher Level Mathematics', '🎓', '#6366f1', 8, 1);

-- Get the strand_id for LC Higher Level
-- We'll use a subquery to reference it

-- Step 2: Add LC HL topics (Calculus first since we have questions)
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_calculus_diff', 'Calculus - Differentiation', id, '📈', 1, 1, 'Differentiation techniques for LC Higher Level'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_calculus_int', 'Calculus - Integration', id, '📉', 2, 1, 'Integration techniques for LC Higher Level'
FROM strands WHERE name = 'LC Higher Level';

-- Add remaining LC HL topics (for future question generation)
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_algebra', 'Algebra', id, '🔤', 3, 1, 'Advanced algebra for LC Higher Level'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_sequences', 'Sequences & Series', id, '🔢', 4, 1, 'Arithmetic and geometric sequences'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_complex', 'Complex Numbers', id, '🌀', 5, 1, 'Complex number operations and applications'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_functions', 'Functions', id, '📊', 6, 1, 'Function types, transformations, and analysis'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_financial', 'Financial Maths', id, '💰', 7, 1, 'Compound interest, depreciation, and amortisation'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_proof', 'Proof', id, '✓', 8, 1, 'Mathematical proof and reasoning'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_probability', 'Probability', id, '🎲', 9, 1, 'Advanced probability including distributions'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_statistics', 'Statistics', id, '📊', 10, 1, 'Descriptive and inferential statistics'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_coord_geom', 'Coordinate Geometry', id, '📐', 11, 1, 'Lines, circles, and coordinate geometry'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_trigonometry', 'Trigonometry', id, '📐', 12, 1, 'Advanced trigonometry and identities'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_geometry', 'Geometry', id, '🔺', 13, 1, 'Synthetic geometry and theorems'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_mensuration', 'Mensuration', id, '📦', 14, 1, 'Area, volume, and surface area calculations'
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible, description)
SELECT 'lc_hl_counting', 'Counting & Combinatorics', id, '🔄', 15, 1, 'Permutations, combinations, and counting principles'
FROM strands WHERE name = 'LC Higher Level';

-- Verify the strand was added
SELECT 'Strand added:' as status, name, id FROM strands WHERE name = 'LC Higher Level';

-- Verify topics were added
SELECT 'Topics added:' as status, COUNT(*) as count FROM topics WHERE topic_id LIKE 'lc_hl_%';

-- Show all LC HL topics
SELECT topic_id, display_name, is_visible FROM topics WHERE topic_id LIKE 'lc_hl_%' ORDER BY sort_order;
