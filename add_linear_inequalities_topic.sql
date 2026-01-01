-- =============================================================
-- Add Linear Inequalities Topic to AgentMath Database
-- Run this BEFORE running the question generator
-- =============================================================

-- Check if topic already exists, if not add it
INSERT OR IGNORE INTO topics (name, display_name, strand, description, icon, is_active, display_order)
VALUES (
    'linear_inequalities',
    'Linear Inequalities',
    'Algebra and Functions',
    'Solving and graphing linear inequalities, number line representations, compound inequalities, and real-world applications. Covers SEC Junior Cycle topics including domain restrictions (ℤ, ℕ, ℝ), rounding/tolerance ranges, and the flip rule for negative coefficients.',
    '📊',
    1,
    28
);

-- Verify the topic was added
SELECT id, name, display_name, strand, is_active 
FROM topics 
WHERE name = 'linear_inequalities';

-- Show all Algebra and Functions topics for reference
SELECT id, name, display_name, display_order 
FROM topics 
WHERE strand = 'Algebra and Functions'
ORDER BY display_order;
