-- ============================================================
-- PRE-FLIGHT CLEANUP SQL FOR AREA, PERIMETER & VOLUME TOPIC
-- Run these commands in PythonAnywhere bash using sqlite3
-- ============================================================
-- ⚠️ This ONLY deletes from questions_adaptive (SEC Exam mode)
-- ⚠️ Legacy Practice Mode questions in 'questions' table are PRESERVED
-- ============================================================

-- Step 1: Check current ADAPTIVE questions (before cleanup)
SELECT topic, COUNT(*) as question_count 
FROM questions_adaptive 
GROUP BY topic 
ORDER BY topic;

-- Step 2: Check existing area_perimeter_volume ADAPTIVE questions
SELECT difficulty_level, COUNT(*) as count 
FROM questions_adaptive 
WHERE topic = 'area_perimeter_volume' 
GROUP BY difficulty_level 
ORDER BY difficulty_level;

-- Step 3: DELETE existing area_perimeter_volume ADAPTIVE questions ONLY
DELETE FROM questions_adaptive WHERE topic = 'area_perimeter_volume';

-- Step 4: Verify cleanup
SELECT topic, COUNT(*) as question_count 
FROM questions_adaptive 
GROUP BY topic 
ORDER BY topic;

-- ============================================================
-- VERIFICATION SQL (run AFTER generator completes)
-- ============================================================

-- Verify 600 questions inserted (50 per level × 12 levels)
SELECT difficulty_level, COUNT(*) as count,
       COUNT(CASE WHEN explanation != '' AND explanation IS NOT NULL THEN 1 END) as with_explanation,
       COUNT(CASE WHEN image_svg IS NOT NULL THEN 1 END) as with_visual
FROM questions_adaptive 
WHERE topic = 'area_perimeter_volume' AND mode = 'jc_exam'
GROUP BY difficulty_level
ORDER BY difficulty_level;

-- Total count should be 600
SELECT COUNT(*) as total_questions 
FROM questions_adaptive 
WHERE topic = 'area_perimeter_volume';

-- ============================================================
-- BASH COMMANDS (copy and paste these directly)
-- ============================================================

-- Delete existing questions:
-- sqlite3 instance/mathquiz.db "DELETE FROM questions_adaptive WHERE topic = 'area_perimeter_volume';"

-- Check count:
-- sqlite3 instance/mathquiz.db "SELECT COUNT(*) FROM questions_adaptive WHERE topic = 'area_perimeter_volume';"

-- After running generator, verify by level:
-- sqlite3 instance/mathquiz.db "SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = 'area_perimeter_volume' GROUP BY difficulty_level;"
