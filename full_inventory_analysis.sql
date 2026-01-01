-- ============================================
-- LC OL FULL QUESTION INVENTORY ANALYSIS
-- Run on PythonAnywhere to identify gaps
-- ============================================

.mode column
.headers on

-- 1. COMPLETE BREAKDOWN BY TOPIC AND LEVEL
SELECT '=== COMPLETE LC OL INVENTORY BY TOPIC/LEVEL ===' as section;

SELECT 
    topic,
    difficulty_level as lvl,
    COUNT(*) as qty
FROM questions_adaptive 
WHERE topic LIKE 'lc_ol_%'
GROUP BY topic, difficulty_level
ORDER BY topic, difficulty_level;

-- 2. SUMMARY BY TOPIC WITH LEVEL COUNTS
SELECT '';
SELECT '=== SUMMARY BY TOPIC (with level distribution) ===' as section;

SELECT 
    topic,
    COUNT(*) as total,
    MIN(CASE WHEN difficulty_level BETWEEN 1 AND 12 THEN 
        (SELECT COUNT(*) FROM questions_adaptive q2 
         WHERE q2.topic = questions_adaptive.topic 
         AND q2.difficulty_level = questions_adaptive.difficulty_level)
    END) as min_per_level,
    MAX(CASE WHEN difficulty_level BETWEEN 1 AND 12 THEN 
        (SELECT COUNT(*) FROM questions_adaptive q2 
         WHERE q2.topic = questions_adaptive.topic 
         AND q2.difficulty_level = questions_adaptive.difficulty_level)
    END) as max_per_level
FROM questions_adaptive 
WHERE topic LIKE 'lc_ol_%'
GROUP BY topic
ORDER BY topic;

-- 3. LEVELS WITH FEWER THAN 45 QUESTIONS (ACTION REQUIRED)
SELECT '';
SELECT '=== LEVELS NEEDING TOP-UP (< 45 questions) ===' as section;

SELECT 
    topic,
    difficulty_level as level,
    COUNT(*) as current_count,
    45 - COUNT(*) as needed_to_reach_45,
    50 - COUNT(*) as needed_to_reach_50
FROM questions_adaptive 
WHERE topic LIKE 'lc_ol_%'
GROUP BY topic, difficulty_level
HAVING COUNT(*) < 45
ORDER BY COUNT(*) ASC, topic, difficulty_level;

-- 4. TOPICS MISSING ANY LEVELS (1-12)
SELECT '';
SELECT '=== TOPICS MISSING LEVELS ===' as section;

WITH all_levels AS (
    SELECT DISTINCT topic FROM questions_adaptive WHERE topic LIKE 'lc_ol_%'
    CROSS JOIN (SELECT 1 as lvl UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 
                UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 
                UNION SELECT 9 UNION SELECT 10 UNION SELECT 11 UNION SELECT 12)
),
existing AS (
    SELECT topic, difficulty_level as lvl, COUNT(*) as cnt
    FROM questions_adaptive WHERE topic LIKE 'lc_ol_%'
    GROUP BY topic, difficulty_level
)
SELECT a.topic, a.lvl as missing_level
FROM all_levels a
LEFT JOIN existing e ON a.topic = e.topic AND a.lvl = e.lvl
WHERE e.cnt IS NULL OR e.cnt = 0
ORDER BY a.topic, a.lvl;

-- 5. GRAND TOTALS
SELECT '';
SELECT '=== GRAND TOTALS ===' as section;

SELECT 
    COUNT(DISTINCT topic) as total_topics,
    COUNT(*) as total_questions,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT topic), 1) as avg_per_topic
FROM questions_adaptive 
WHERE topic LIKE 'lc_ol_%';

SELECT '';
SELECT '=== QUESTIONS NEEDED TO REACH 600 PER TOPIC ===' as section;

SELECT 
    topic,
    COUNT(*) as current,
    600 - COUNT(*) as needed_for_600
FROM questions_adaptive 
WHERE topic LIKE 'lc_ol_%'
GROUP BY topic
HAVING COUNT(*) < 600
ORDER BY COUNT(*) ASC;
