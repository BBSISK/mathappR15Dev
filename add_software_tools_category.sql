-- =============================================================
-- Add "Useful Maths Software Tools" Resource Category
-- This category should appear LAST in the listing
-- =============================================================

-- First, check current max display_order
-- SELECT MAX(display_order) FROM resource_categories;

-- Insert new category with high display_order to ensure it appears last
INSERT INTO resource_categories (name, description, display_order, is_active)
VALUES (
    'Useful Maths Software Tools',
    'Software tools and applications to help with mathematics learning and problem solving',
    100,  -- High number to ensure it appears last
    1     -- Active
);

-- Verify the category was added
SELECT id, name, display_order, is_active 
FROM resource_categories 
ORDER BY display_order;
