-- ============================================================
-- Add LC Higher Level Strand - ONLY topics with questions (v3)
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < add_lc_hl_strand_v3.sql
-- ============================================================

-- Step 0: Clean up any LC HL topics that were added but have no questions
DELETE FROM topics WHERE topic_id LIKE 'lc_hl_%' 
AND topic_id NOT IN ('lc_hl_calculus_diff', 'lc_hl_calculus_int');

-- Step 1: Add the LC Higher Level strand
INSERT OR IGNORE INTO strands (name, icon, color, sort_order)
VALUES ('LC Higher Level', '🎓', '#6366f1', 8);

-- Step 2: Add ONLY the 2 topics that have questions
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_calculus_diff', 'Calculus - Differentiation', id, '📈', 1, 1
FROM strands WHERE name = 'LC Higher Level';

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_calculus_int', 'Calculus - Integration', id, '📉', 2, 1
FROM strands WHERE name = 'LC Higher Level';

-- Verify
SELECT 'Strand added:' as info, name, id FROM strands WHERE name = 'LC Higher Level';
SELECT 'Topics added:' as info, COUNT(*) as count FROM topics WHERE topic_id LIKE 'lc_hl_%';
SELECT topic_id, display_name, is_visible FROM topics WHERE topic_id LIKE 'lc_hl_%' ORDER BY sort_order;

-- Show question counts
SELECT 'Questions per topic:' as info;
SELECT topic, COUNT(*) as questions FROM questions_adaptive WHERE topic LIKE 'lc_hl_%' GROUP BY topic;
