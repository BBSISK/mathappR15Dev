-- Add Indices & Scientific Notation Topic to AgentMath
-- Run this in PythonAnywhere MySQL console or via Flask-SQLAlchemy

-- Step 1: Insert the topic into the topics table
INSERT INTO topics (topic_id, topic_name, strand, display_order, is_visible)
VALUES ('indices', 'Indices & Scientific Notation', 'Number', 8, 1);

-- Verify it was added:
SELECT * FROM topics WHERE topic_id = 'indices';

-- Note: After running this SQL:
-- 1. The topic will appear in the student dashboard
-- 2. Run generate_jc_indices_v1.py to populate questions
-- 3. Upload the updated student_app.html and admin_dashboard.html
