-- =====================================================
-- AUDIT: Find questions with \n syntax errors
-- Run this on PythonAnywhere to identify problematic questions
-- =====================================================

-- Find questions with literal \n in question text
SELECT id, topic, difficulty_level, 
       SUBSTR(question_text, 1, 100) as preview
FROM questions_adaptive
WHERE question_text LIKE '%\n%'
   OR question_text LIKE '%' || char(10) || '%'
ORDER BY topic, difficulty_level;

-- Count affected questions by topic
SELECT topic, COUNT(*) as questions_with_newlines
FROM questions_adaptive
WHERE question_text LIKE '%\n%'
   OR question_text LIKE '%' || char(10) || '%'
GROUP BY topic;

-- Find questions with \n in options
SELECT id, topic, difficulty_level, 'option_a' as field
FROM questions_adaptive WHERE option_a LIKE '%\n%'
UNION ALL
SELECT id, topic, difficulty_level, 'option_b' as field
FROM questions_adaptive WHERE option_b LIKE '%\n%'
UNION ALL
SELECT id, topic, difficulty_level, 'option_c' as field
FROM questions_adaptive WHERE option_c LIKE '%\n%'
UNION ALL
SELECT id, topic, difficulty_level, 'option_d' as field
FROM questions_adaptive WHERE option_d LIKE '%\n%';

-- Find questions with \n in explanation
SELECT id, topic, difficulty_level,
       SUBSTR(explanation, 1, 80) as explanation_preview
FROM questions_adaptive
WHERE explanation LIKE '%\n%'
LIMIT 20;

-- =====================================================
-- SUMMARY
-- =====================================================

SELECT 
    'Questions with newlines in text' as issue,
    COUNT(*) as count
FROM questions_adaptive
WHERE question_text LIKE '%\n%'
   OR question_text LIKE '%' || char(10) || '%'

UNION ALL

SELECT 
    'Questions with newlines in options' as issue,
    COUNT(*) as count
FROM questions_adaptive
WHERE option_a LIKE '%\n%'
   OR option_b LIKE '%\n%'
   OR option_c LIKE '%\n%'
   OR option_d LIKE '%\n%'

UNION ALL

SELECT 
    'Questions with answer-revealing visuals' as issue,
    COUNT(*) as count
FROM questions_adaptive
WHERE image_svg IS NOT NULL 
  AND image_svg != ''
  AND topic IN ('introductory_algebra', 'expanding_factorising', 
                'simplifying_expressions', 'solving_equations');

-- =====================================================
-- FIX: Remove newlines from question text (replace with space)
-- Uncomment to run
-- =====================================================

/*
UPDATE questions_adaptive
SET question_text = REPLACE(question_text, char(10), ' ')
WHERE question_text LIKE '%' || char(10) || '%';

UPDATE questions_adaptive
SET question_text = REPLACE(question_text, '\n', ' ')
WHERE question_text LIKE '%\n%';

UPDATE questions_adaptive
SET explanation = REPLACE(explanation, char(10), ' ')
WHERE explanation LIKE '%' || char(10) || '%';

UPDATE questions_adaptive
SET explanation = REPLACE(explanation, '\n', ' ')
WHERE explanation LIKE '%\n%';
*/

-- =====================================================
-- VERIFICATION after running generator
-- =====================================================

SELECT 
    topic,
    difficulty_level,
    COUNT(*) as question_count,
    SUM(CASE WHEN image_svg IS NOT NULL AND image_svg != '' THEN 1 ELSE 0 END) as with_visuals
FROM questions_adaptive
WHERE topic = 'introductory_algebra'
GROUP BY difficulty_level
ORDER BY difficulty_level;
