-- =====================================================
-- FIX: Remove answer-revealing visuals from introductory_algebra
-- The image_svg field contains "worked example" visuals that show the answer
-- =====================================================

-- First, see what we're dealing with
SELECT id, question_text, image_svg 
FROM questions_adaptive 
WHERE topic = 'introductory_algebra' 
AND image_svg IS NOT NULL 
AND image_svg != ''
LIMIT 5;

-- Count affected questions
SELECT COUNT(*) as affected_questions
FROM questions_adaptive 
WHERE topic = 'introductory_algebra' 
AND image_svg IS NOT NULL 
AND image_svg != '';

-- BACKUP: Export affected questions first (run in Python or use sqlite3 .output)
-- SELECT * FROM questions_adaptive WHERE topic = 'introductory_algebra';

-- =====================================================
-- THE FIX: Clear the image_svg field for these questions
-- =====================================================

UPDATE questions_adaptive 
SET image_svg = NULL 
WHERE topic = 'introductory_algebra' 
AND image_svg IS NOT NULL;

-- Verify the fix
SELECT COUNT(*) as questions_with_visuals_after
FROM questions_adaptive 
WHERE topic = 'introductory_algebra' 
AND image_svg IS NOT NULL 
AND image_svg != '';

-- Should return 0
