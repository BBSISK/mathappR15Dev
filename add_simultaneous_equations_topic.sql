-- SQL script to add Simultaneous Equations topic to AgentMath database
-- Run this BEFORE running the generator to insert questions

-- First, check if topic already exists
SELECT * FROM topics WHERE topic_id = 'simultaneous_equations';

-- Insert the topic (adjust strand_id based on your database)
-- The strand should be 'Algebra and Functions'
INSERT OR IGNORE INTO topics (topic_id, display_name, icon, strand_id, sort_order, is_visible)
SELECT 
    'simultaneous_equations',
    'Simultaneous Equations',
    'balance-scale',
    s.id,
    (SELECT COALESCE(MAX(sort_order), 0) + 1 FROM topics WHERE strand_id = s.id),
    1
FROM strands s 
WHERE s.name LIKE '%Algebra%' 
LIMIT 1;

-- Verify insertion
SELECT t.*, s.name as strand_name 
FROM topics t 
LEFT JOIN strands s ON t.strand_id = s.id 
WHERE t.topic_id = 'simultaneous_equations';

-- Show all Algebra topics for verification
SELECT t.topic_id, t.display_name, t.sort_order, s.name as strand_name
FROM topics t
LEFT JOIN strands s ON t.strand_id = s.id
WHERE s.name LIKE '%Algebra%'
ORDER BY t.sort_order;
