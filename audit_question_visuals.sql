-- =====================================================
-- AUDIT: Check all topics for visuals that might reveal answers
-- Run this to see which topics have image_svg content
-- =====================================================

-- Count questions with visuals per topic
SELECT 
    topic,
    COUNT(*) as total_questions,
    SUM(CASE WHEN image_svg IS NOT NULL AND image_svg != '' THEN 1 ELSE 0 END) as with_visuals,
    ROUND(100.0 * SUM(CASE WHEN image_svg IS NOT NULL AND image_svg != '' THEN 1 ELSE 0 END) / COUNT(*), 1) as visual_percent
FROM questions_adaptive
WHERE is_active = 1
GROUP BY topic
HAVING with_visuals > 0
ORDER BY with_visuals DESC;

-- Sample visuals from each topic to manually check
-- (Look for ones that show the answer!)

-- Check introductory_algebra
SELECT id, question_text, SUBSTR(image_svg, 1, 200) as visual_preview
FROM questions_adaptive 
WHERE topic = 'introductory_algebra' AND image_svg IS NOT NULL
LIMIT 3;

-- Check expanding_factorising
SELECT id, question_text, SUBSTR(image_svg, 1, 200) as visual_preview
FROM questions_adaptive 
WHERE topic = 'expanding_factorising' AND image_svg IS NOT NULL
LIMIT 3;

-- Check simplifying_expressions
SELECT id, question_text, SUBSTR(image_svg, 1, 200) as visual_preview
FROM questions_adaptive 
WHERE topic = 'simplifying_expressions' AND image_svg IS NOT NULL
LIMIT 3;

-- Check solving_equations
SELECT id, question_text, SUBSTR(image_svg, 1, 200) as visual_preview
FROM questions_adaptive 
WHERE topic = 'solving_equations' AND image_svg IS NOT NULL
LIMIT 3;

-- =====================================================
-- BULK FIX: Clear visuals from ALL algebra-type topics
-- Use this if multiple topics have the same issue
-- =====================================================

-- Uncomment to run:
/*
UPDATE questions_adaptive 
SET image_svg = NULL 
WHERE topic IN (
    'introductory_algebra',
    'expanding_factorising', 
    'simplifying_expressions',
    'solving_equations',
    'simultaneous_equations',
    'linear_inequalities'
)
AND image_svg IS NOT NULL;
*/

-- Verify counts after fix
SELECT topic, COUNT(*) as remaining_visuals
FROM questions_adaptive
WHERE image_svg IS NOT NULL AND image_svg != ''
GROUP BY topic;
