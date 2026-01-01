-- ============================================================
-- PRE-FLIGHT CLEANUP SQL FOR DESCRIPTIVE STATISTICS
-- Run these commands in PythonAnywhere's MySQL console or SQLite
-- ============================================================

-- Step 1: Check current state (BEFORE cleanup)
SELECT topic, COUNT(*) as question_count 
FROM questions_adaptive 
GROUP BY topic 
ORDER BY topic;

-- Step 2: Check existing descriptive_statistics questions
SELECT difficulty_level, COUNT(*) as count 
FROM questions_adaptive 
WHERE topic = 'descriptive_statistics' 
GROUP BY difficulty_level 
ORDER BY difficulty_level;

-- Step 3: DELETE existing descriptive_statistics questions
DELETE FROM questions_adaptive WHERE topic = 'descriptive_statistics';

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
WHERE topic = 'descriptive_statistics' AND mode = 'jc_exam'
GROUP BY difficulty_level
ORDER BY difficulty_level;

-- Total count should be 600
SELECT COUNT(*) as total_questions 
FROM questions_adaptive 
WHERE topic = 'descriptive_statistics';

-- ============================================================
-- CLEAR TEST PROGRESS (optional - run before going live)
-- ============================================================

-- Reset all users' progress for descriptive_statistics to Level 1
UPDATE adaptive_progress 
SET current_level = 1, current_points = 0 
WHERE topic = 'descriptive_statistics';

-- Or delete test progress entirely
-- DELETE FROM adaptive_progress WHERE topic = 'descriptive_statistics';
