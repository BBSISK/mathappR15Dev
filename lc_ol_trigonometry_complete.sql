-- LC Ordinary Level - Trigonometry Complete SQL
-- Generated: 2025-12-15
-- Total: 600 questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Trigonometry topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_ol_trigonometry', 'Trigonometry', id, '📐', 3, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_trigonometry';

-- Insert questions
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 16 cm and 30 cm. Find the hypotenuse.', '36 cm', '35 cm', '34 cm', '46 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 16² + 30² = 256 + 900 = 1156. So c = 34 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 14 cm and 48 cm. Find the hypotenuse.', '62 cm', '52 cm', '51 cm', '50 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 14² + 48² = 196 + 2304 = 2500. So c = 50 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 3 cm and 4 cm. Find the hypotenuse.', '5 cm', '6 cm', '7 cm', 'Cannot determine', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 3² + 4² = 9 + 16 = 25. So c = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 3 cm and 4 cm. Find the hypotenuse.', '7 cm', '6 cm', 'Cannot determine', '5 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 3² + 4² = 9 + 16 = 25. So c = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 24 cm and 32 cm. Find the hypotenuse.', '41 cm', '56 cm', '40 cm', '42 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 24² + 32² = 576 + 1024 = 1600. So c = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 5 cm and 12 cm. Find the hypotenuse.', '17 cm', '14 cm', '13 cm', '15 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 5² + 12² = 25 + 144 = 169. So c = 13 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 10 cm and 24 cm. Find the hypotenuse.', '28 cm', '34 cm', '26 cm', '27 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 10² + 24² = 100 + 576 = 676. So c = 26 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 6 cm and 8 cm. Find the hypotenuse.', '11 cm', '14 cm', '12 cm', '10 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 6² + 8² = 36 + 64 = 100. So c = 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 7 cm and 24 cm. Find the hypotenuse.', '27 cm', '25 cm', '31 cm', '26 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 7² + 24² = 49 + 576 = 625. So c = 25 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 24 cm and 32 cm. Find the hypotenuse.', '41 cm', '56 cm', '42 cm', '40 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 24² + 32² = 576 + 1024 = 1600. So c = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 6 cm and 8 cm. Find the hypotenuse.', '14 cm', '10 cm', '12 cm', '11 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 6² + 8² = 36 + 64 = 100. So c = 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 14 cm and 48 cm. Find the hypotenuse.', '51 cm', '50 cm', '52 cm', '62 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 14² + 48² = 196 + 2304 = 2500. So c = 50 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 12 cm and 16 cm. Find the hypotenuse.', '20 cm', '28 cm', '22 cm', '21 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 12² + 16² = 144 + 256 = 400. So c = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 16 cm and 30 cm. Find the hypotenuse.', '46 cm', '35 cm', '36 cm', '34 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 16² + 30² = 256 + 900 = 1156. So c = 34 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 6 cm and 8 cm. Find the hypotenuse.', '11 cm', '10 cm', '12 cm', '14 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 6² + 8² = 36 + 64 = 100. So c = 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 6 cm and 8 cm. Find the hypotenuse.', '14 cm', '12 cm', '10 cm', '11 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 6² + 8² = 36 + 64 = 100. So c = 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 9 cm and 12 cm. Find the hypotenuse.', '21 cm', '16 cm', '17 cm', '15 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 9² + 12² = 81 + 144 = 225. So c = 15 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 7 cm and 24 cm. Find the hypotenuse.', '31 cm', '26 cm', '25 cm', '27 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 7² + 24² = 49 + 576 = 625. So c = 25 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 3 cm and 4 cm. Find the hypotenuse.', '5 cm', 'Cannot determine', '7 cm', '6 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 3² + 4² = 9 + 16 = 25. So c = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the two shorter sides are 3 cm and 4 cm. Find the hypotenuse.', '5 cm', '7 cm', 'Cannot determine', '6 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'c² = a² + b² = 3² + 4² = 9 + 16 = 25. So c = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 34 cm and one side is 16 cm. Find the other side.', '18 cm', '50 cm', '31 cm', '30 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 34² - 16² = 1156 - 256 = 900. So b = 30 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 34 cm and one side is 16 cm. Find the other side.', '30 cm', '31 cm', '18 cm', '50 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 34² - 16² = 1156 - 256 = 900. So b = 30 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 13 cm and one side is 5 cm. Find the other side.', '12 cm', '13 cm', '8 cm', '18 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 13² - 5² = 169 - 25 = 144. So b = 12 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 40 cm and one side is 24 cm. Find the other side.', '16 cm', '64 cm', '33 cm', '32 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 40² - 24² = 1600 - 576 = 1024. So b = 32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 25 cm and one side is 7 cm. Find the other side.', '24 cm', '32 cm', '18 cm', '25 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 25² - 7² = 625 - 49 = 576. So b = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 40 cm and one side is 24 cm. Find the other side.', '33 cm', '16 cm', '64 cm', '32 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 40² - 24² = 1600 - 576 = 1024. So b = 32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 26 cm and one side is 10 cm. Find the other side.', '16 cm', '25 cm', '24 cm', '36 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 26² - 10² = 676 - 100 = 576. So b = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 20 cm and one side is 12 cm. Find the other side.', '32 cm', '16 cm', '8 cm', '17 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 20² - 12² = 400 - 144 = 256. So b = 16 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 15 cm and one side is 9 cm. Find the other side.', '12 cm', '24 cm', '13 cm', '6 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 15² - 9² = 225 - 81 = 144. So b = 12 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 5 cm and one side is 3 cm. Find the other side.', '8 cm', '2 cm', '5 cm', '4 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 5² - 3² = 25 - 9 = 16. So b = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 30 cm and one side is 18 cm. Find the other side.', '25 cm', '48 cm', '24 cm', '12 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 30² - 18² = 900 - 324 = 576. So b = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 20 cm and one side is 12 cm. Find the other side.', '8 cm', '16 cm', '17 cm', '32 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 20² - 12² = 400 - 144 = 256. So b = 16 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 20 cm and one side is 12 cm. Find the other side.', '16 cm', '17 cm', '8 cm', '32 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 20² - 12² = 400 - 144 = 256. So b = 16 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 10 cm and one side is 6 cm. Find the other side.', '16 cm', '9 cm', '8 cm', '4 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 10² - 6² = 100 - 36 = 64. So b = 8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 30 cm and one side is 18 cm. Find the other side.', '12 cm', '48 cm', '24 cm', '25 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 30² - 18² = 900 - 324 = 576. So b = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 5 cm and one side is 3 cm. Find the other side.', '8 cm', '4 cm', '2 cm', '5 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 5² - 3² = 25 - 9 = 16. So b = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 17 cm and one side is 8 cm. Find the other side.', '15 cm', '16 cm', '25 cm', '9 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 17² - 8² = 289 - 64 = 225. So b = 15 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 25 cm and one side is 7 cm. Find the other side.', '24 cm', '18 cm', '25 cm', '32 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 25² - 7² = 625 - 49 = 576. So b = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 34 cm and one side is 16 cm. Find the other side.', '30 cm', '31 cm', '18 cm', '50 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 34² - 16² = 1156 - 256 = 900. So b = 30 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, the hypotenuse is 40 cm and one side is 24 cm. Find the other side.', '32 cm', '64 cm', '33 cm', '16 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'b² = c² - a² = 40² - 24² = 1600 - 576 = 1024. So b = 32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 10 cm, 6 cm, and 8 cm. If this is a right-angled triangle, which is the hypotenuse?', '6 cm', '10 cm', '8 cm', '14 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 10 cm. Check: 6² + 8² = 100 = 10² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 5 cm, 3 cm, and 4 cm. If this is a right-angled triangle, which is the hypotenuse?', '4 cm', '3 cm', '5 cm', '7 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 5 cm. Check: 3² + 4² = 25 = 5² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 15 cm, 12 cm, and 9 cm. If this is a right-angled triangle, which is the hypotenuse?', '9 cm', '21 cm', '15 cm', '12 cm', 2,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 15 cm. Check: 9² + 12² = 225 = 15² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 9 cm, 15 cm, and 12 cm. If this is a right-angled triangle, which is the hypotenuse?', '15 cm', '9 cm', '21 cm', '12 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 15 cm. Check: 9² + 12² = 225 = 15² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 9 cm, 12 cm, and 15 cm. If this is a right-angled triangle, which is the hypotenuse?', '21 cm', '15 cm', '9 cm', '12 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 15 cm. Check: 9² + 12² = 225 = 15² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 20 cm, 16 cm, and 12 cm. If this is a right-angled triangle, which is the hypotenuse?', '16 cm', '28 cm', '12 cm', '20 cm', 3,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 20 cm. Check: 12² + 16² = 400 = 20² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 13 cm, 12 cm, and 5 cm. If this is a right-angled triangle, which is the hypotenuse?', '13 cm', '17 cm', '12 cm', '5 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 13 cm. Check: 5² + 12² = 169 = 13² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 8 cm, 15 cm, and 17 cm. If this is a right-angled triangle, which is the hypotenuse?', '23 cm', '17 cm', '15 cm', '8 cm', 1,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 17 cm. Check: 8² + 15² = 289 = 17² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 3 cm, 4 cm, and 5 cm. If this is a right-angled triangle, which is the hypotenuse?', '5 cm', '3 cm', '7 cm', '4 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 5 cm. Check: 3² + 4² = 25 = 5² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three sides of a triangle are 12 cm, 16 cm, and 20 cm. If this is a right-angled triangle, which is the hypotenuse?', '20 cm', '16 cm', '12 cm', '28 cm', 0,
'lc_ol_trigonometry', 1, 'foundation', 'lc_ol', 'The hypotenuse is the longest side = 20 cm. Check: 12² + 16² = 400 = 20² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and adjacent = 3 cm. Find angle θ.', 'Cannot determine', '26.6°', '63.4°', '73.4°', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 6/3 = 2.000. θ = tan⁻¹(2.000) = 63.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 10 cm and adjacent = 10 cm. Find angle θ.', '45.0°', 'Cannot determine', 'Cannot determine', '55.0°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 10/10 = 1.000. θ = tan⁻¹(1.000) = 45.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 5 cm and adjacent = 4 cm. Find angle θ.', 'Cannot determine', '51.3°', '38.7°', '61.3°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 5/4 = 1.250. θ = tan⁻¹(1.250) = 51.3°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 8 cm and adjacent = 5 cm. Find angle θ.', '58.0°', 'Cannot determine', '68.0°', '32.0°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 8/5 = 1.600. θ = tan⁻¹(1.600) = 58.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 10 cm and adjacent = 5 cm. Find angle θ.', '63.4°', '73.4°', 'Cannot determine', '26.6°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 10/5 = 2.000. θ = tan⁻¹(2.000) = 63.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 10 cm and adjacent = 10 cm. Find angle θ.', 'Cannot determine', 'Cannot determine', '55.0°', '45.0°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 10/10 = 1.000. θ = tan⁻¹(1.000) = 45.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 10 cm and adjacent = 12 cm. Find angle θ.', '49.8°', '50.2°', '39.8°', 'Cannot determine', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 10/12 = 0.833. θ = tan⁻¹(0.833) = 39.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 12 cm and adjacent = 6 cm. Find angle θ.', '63.4°', 'Cannot determine', '26.6°', '73.4°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 12/6 = 2.000. θ = tan⁻¹(2.000) = 63.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and adjacent = 8 cm. Find angle θ.', 'Cannot determine', '46.9°', '53.1°', '36.9°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 6/8 = 0.750. θ = tan⁻¹(0.750) = 36.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 4 cm and adjacent = 8 cm. Find angle θ.', '36.6°', '26.6°', 'Cannot determine', '63.4°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 4/8 = 0.500. θ = tan⁻¹(0.500) = 26.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and adjacent = 10 cm. Find angle θ.', '41.0°', 'Cannot determine', '59.0°', '31.0°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 6/10 = 0.600. θ = tan⁻¹(0.600) = 31.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 4 cm and adjacent = 4 cm. Find angle θ.', 'Cannot determine', '45.0°', 'Cannot determine', '55.0°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 4/4 = 1.000. θ = tan⁻¹(1.000) = 45.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 5 cm and adjacent = 12 cm. Find angle θ.', '32.6°', 'Cannot determine', '22.6°', '67.4°', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 5/12 = 0.417. θ = tan⁻¹(0.417) = 22.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 5 cm and adjacent = 3 cm. Find angle θ.', '31.0°', '59.0°', 'Cannot determine', '69.0°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 5/3 = 1.667. θ = tan⁻¹(1.667) = 59.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and adjacent = 3 cm. Find angle θ.', '73.4°', '26.6°', 'Cannot determine', '63.4°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 6/3 = 2.000. θ = tan⁻¹(2.000) = 63.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and adjacent = 12 cm. Find angle θ.', 'Cannot determine', '26.6°', '63.4°', '36.6°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 6/12 = 0.500. θ = tan⁻¹(0.500) = 26.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 4 cm and adjacent = 10 cm. Find angle θ.', '68.2°', '31.8°', 'Cannot determine', '21.8°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 4/10 = 0.400. θ = tan⁻¹(0.400) = 21.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 10 cm and adjacent = 3 cm. Find angle θ.', '16.7°', 'Cannot determine', '73.3°', '83.3°', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 10/3 = 3.333. θ = tan⁻¹(3.333) = 73.3°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 8 cm and adjacent = 4 cm. Find angle θ.', 'Cannot determine', '63.4°', '26.6°', '73.4°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 8/4 = 2.000. θ = tan⁻¹(2.000) = 63.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and adjacent = 6 cm. Find angle θ.', '55.0°', '45.0°', 'Cannot determine', 'Cannot determine', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'tan θ = opp/adj = 6/6 = 1.000. θ = tan⁻¹(1.000) = 45.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 8 cm and hypotenuse = 15 cm. Find angle θ.', '47.2°', '53.3°', '57.8°', '32.2°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 8/15 = 0.533. θ = sin⁻¹(0.533) = 32.2°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 3 cm and hypotenuse = 10 cm. Find angle θ.', '17.5°', '72.5°', '30.0°', '32.5°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 3/10 = 0.300. θ = sin⁻¹(0.300) = 17.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 7 cm and hypotenuse = 12 cm. Find angle θ.', '50.7°', '54.3°', '35.7°', '58.3°', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 7/12 = 0.583. θ = sin⁻¹(0.583) = 35.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 4 cm and hypotenuse = 15 cm. Find angle θ.', '74.5°', '15.5°', '30.5°', '26.7°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 4/15 = 0.267. θ = sin⁻¹(0.267) = 15.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 3 cm and hypotenuse = 13 cm. Find angle θ.', '23.1°', '76.7°', '28.3°', '13.3°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 3/13 = 0.231. θ = sin⁻¹(0.231) = 13.3°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 7 cm and hypotenuse = 13 cm. Find angle θ.', '32.6°', '57.4°', '47.6°', '53.8°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 7/13 = 0.538. θ = sin⁻¹(0.538) = 32.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 4 cm and hypotenuse = 10 cm. Find angle θ.', '66.4°', '38.6°', '23.6°', '40.0°', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 4/10 = 0.400. θ = sin⁻¹(0.400) = 23.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 3 cm and hypotenuse = 12 cm. Find angle θ.', '25.0°', '14.5°', '29.5°', '75.5°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 3/12 = 0.250. θ = sin⁻¹(0.250) = 14.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 4 cm and hypotenuse = 10 cm. Find angle θ.', '40.0°', '38.6°', '66.4°', '23.6°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 4/10 = 0.400. θ = sin⁻¹(0.400) = 23.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 5 cm and hypotenuse = 12 cm. Find angle θ.', '65.4°', '24.6°', '39.6°', '41.7°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 5/12 = 0.417. θ = sin⁻¹(0.417) = 24.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and hypotenuse = 17 cm. Find angle θ.', '20.7°', '69.3°', '35.7°', '35.3°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 6/17 = 0.353. θ = sin⁻¹(0.353) = 20.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 6 cm and hypotenuse = 15 cm. Find angle θ.', '38.6°', '40.0°', '66.4°', '23.6°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 6/15 = 0.400. θ = sin⁻¹(0.400) = 23.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 5 cm and hypotenuse = 17 cm. Find angle θ.', '32.1°', '17.1°', '72.9°', '29.4°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 5/17 = 0.294. θ = sin⁻¹(0.294) = 17.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 3 cm and hypotenuse = 12 cm. Find angle θ.', '75.5°', '25.0°', '29.5°', '14.5°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 3/12 = 0.250. θ = sin⁻¹(0.250) = 14.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, opposite = 5 cm and hypotenuse = 13 cm. Find angle θ.', '37.6°', '38.5°', '67.4°', '22.6°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'sin θ = opp/hyp = 5/13 = 0.385. θ = sin⁻¹(0.385) = 22.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 45°. Find the third angle.', 'Cannot determine', '45°', '135°', 'Cannot determine', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 45° = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 30°. Find the third angle.', '150°', '30°', 'Cannot determine', '60°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 30° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 50°. Find the third angle.', 'Cannot determine', '40°', '50°', '130°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 50° = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 55°. Find the third angle.', '35°', '55°', '125°', 'Cannot determine', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 55° = 35°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 30°. Find the third angle.', '150°', '30°', 'Cannot determine', '60°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 30° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 50°. Find the third angle.', '50°', '130°', 'Cannot determine', '40°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 50° = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 40°. Find the third angle.', '140°', '50°', '40°', 'Cannot determine', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 40° = 50°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 55°. Find the third angle.', '55°', '35°', 'Cannot determine', '125°', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 55° = 35°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 50°. Find the third angle.', 'Cannot determine', '50°', '40°', '130°', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 50° = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 45°. Find the third angle.', 'Cannot determine', '135°', '45°', 'Cannot determine', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 45° = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 30°. Find the third angle.', '30°', '150°', '60°', 'Cannot determine', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 30° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 55°. Find the third angle.', '35°', 'Cannot determine', '125°', '55°', 0,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 55° = 35°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 60°. Find the third angle.', '60°', '120°', 'Cannot determine', '30°', 3,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 60° = 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 55°. Find the third angle.', '125°', '35°', '55°', 'Cannot determine', 1,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 55° = 35°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A right-angled triangle has angles of 90° and 55°. Find the third angle.', '55°', '125°', '35°', 'Cannot determine', 2,
'lc_ol_trigonometry', 2, 'foundation', 'lc_ol', 'Angles in a triangle sum to 180°. Third angle = 180° - 90° - 55° = 35°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 10 cm. Find the opposite side.', '9.66 cm', '7.66 cm', '6.43 cm', '10 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 50° = opp/hyp. opp = 10 × sin 50° = 10 × 0.7660 = 7.66 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and hypotenuse = 10 cm. Find the opposite side.', '10 cm', '9.07 cm', '7.07 cm', 'Cannot determine', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 45° = opp/hyp. opp = 10 × sin 45° = 10 × 0.7071 = 7.07 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 20 cm. Find the opposite side.', '20 cm', '12.0 cm', '17.32 cm', '10.0 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 30° = opp/hyp. opp = 20 × sin 30° = 20 × 0.5000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 12 cm. Find the opposite side.', '12 cm', '9.19 cm', '7.71 cm', '11.19 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 50° = opp/hyp. opp = 12 × sin 50° = 12 × 0.7660 = 9.19 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and hypotenuse = 10 cm. Find the opposite side.', '9.07 cm', '10 cm', '7.07 cm', 'Cannot determine', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 45° = opp/hyp. opp = 10 × sin 45° = 10 × 0.7071 = 7.07 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and hypotenuse = 12 cm. Find the opposite side.', '12 cm', '10.39 cm', '6.0 cm', '12.39 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 60° = opp/hyp. opp = 12 × sin 60° = 12 × 0.8660 = 10.39 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and hypotenuse = 15 cm. Find the opposite side.', '15 cm', '12.99 cm', '14.99 cm', '7.5 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 60° = opp/hyp. opp = 15 × sin 60° = 15 × 0.8660 = 12.99 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 35° and hypotenuse = 10 cm. Find the opposite side.', '10 cm', '7.74 cm', '5.74 cm', '8.19 cm', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 35° = opp/hyp. opp = 10 × sin 35° = 10 × 0.5736 = 5.74 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 20 cm. Find the opposite side.', '20 cm', '17.32 cm', '12.86 cm', '15.32 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 50° = opp/hyp. opp = 20 × sin 50° = 20 × 0.7660 = 15.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 20 cm. Find the opposite side.', '20 cm', '12.86 cm', '17.32 cm', '15.32 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 50° = opp/hyp. opp = 20 × sin 50° = 20 × 0.7660 = 15.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 20 cm. Find the opposite side.', '15.32 cm', '20 cm', '12.86 cm', '17.32 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 50° = opp/hyp. opp = 20 × sin 50° = 20 × 0.7660 = 15.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 20 cm. Find the opposite side.', '20 cm', '15.32 cm', '12.86 cm', '17.32 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 50° = opp/hyp. opp = 20 × sin 50° = 20 × 0.7660 = 15.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and hypotenuse = 20 cm. Find the opposite side.', '17.32 cm', '10.0 cm', '19.32 cm', '20 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 60° = opp/hyp. opp = 20 × sin 60° = 20 × 0.8660 = 17.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 10 cm. Find the opposite side.', '7.66 cm', '6.43 cm', '9.66 cm', '10 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 50° = opp/hyp. opp = 10 × sin 50° = 10 × 0.7660 = 7.66 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 12 cm. Find the opposite side.', '8.0 cm', '12 cm', '6.0 cm', '10.39 cm', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 30° = opp/hyp. opp = 12 × sin 30° = 12 × 0.5000 = 6.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 20 cm. Find the opposite side.', '17.32 cm', '10.0 cm', '12.0 cm', '20 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 30° = opp/hyp. opp = 20 × sin 30° = 20 × 0.5000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 15 cm. Find the opposite side.', '12.99 cm', '7.5 cm', '15 cm', '9.5 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'sin 30° = opp/hyp. opp = 15 × sin 30° = 15 × 0.5000 = 7.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 20 cm. Find the adjacent side.', '17.32 cm', '10.0 cm', '20.32 cm', '20 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 30° = adj/hyp. adj = 20 × cos 30° = 20 × 0.8660 = 17.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and hypotenuse = 12 cm. Find the adjacent side.', '8.49 cm', '11.49 cm', 'Cannot determine', '12 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 45° = adj/hyp. adj = 12 × cos 45° = 12 × 0.7071 = 8.49 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and hypotenuse = 10 cm. Find the adjacent side.', '8.66 cm', '8.0 cm', '5.0 cm', '10 cm', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 60° = adj/hyp. adj = 10 × cos 60° = 10 × 0.5000 = 5.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 20 cm. Find the adjacent side.', '10.0 cm', '20 cm', '20.32 cm', '17.32 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 30° = adj/hyp. adj = 20 × cos 30° = 20 × 0.8660 = 17.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 20 cm. Find the adjacent side.', '15.32 cm', '15.86 cm', '20 cm', '12.86 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 50° = adj/hyp. adj = 20 × cos 50° = 20 × 0.6428 = 12.86 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and hypotenuse = 15 cm. Find the adjacent side.', '15 cm', '10.61 cm', '13.61 cm', 'Cannot determine', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 45° = adj/hyp. adj = 15 × cos 45° = 15 × 0.7071 = 10.61 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 15 cm. Find the adjacent side.', '11.49 cm', '9.64 cm', '15 cm', '12.64 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 50° = adj/hyp. adj = 15 × cos 50° = 15 × 0.6428 = 9.64 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 40° and hypotenuse = 20 cm. Find the adjacent side.', '15.32 cm', '18.32 cm', '12.86 cm', '20 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 40° = adj/hyp. adj = 20 × cos 40° = 20 × 0.7660 = 15.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and hypotenuse = 10 cm. Find the adjacent side.', '10 cm', '8.0 cm', '5.0 cm', '8.66 cm', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 60° = adj/hyp. adj = 10 × cos 60° = 10 × 0.5000 = 5.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and hypotenuse = 15 cm. Find the adjacent side.', '13.61 cm', '10.61 cm', 'Cannot determine', '15 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 45° = adj/hyp. adj = 15 × cos 45° = 15 × 0.7071 = 10.61 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 10 cm. Find the adjacent side.', '6.43 cm', '7.66 cm', '10 cm', '9.43 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 50° = adj/hyp. adj = 10 × cos 50° = 10 × 0.6428 = 6.43 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 40° and hypotenuse = 10 cm. Find the adjacent side.', '10 cm', '7.66 cm', '6.43 cm', '10.66 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 40° = adj/hyp. adj = 10 × cos 40° = 10 × 0.7660 = 7.66 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 10 cm. Find the adjacent side.', '5.0 cm', '8.66 cm', '10 cm', '11.66 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 30° = adj/hyp. adj = 10 × cos 30° = 10 × 0.8660 = 8.66 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 15 cm. Find the adjacent side.', '12.99 cm', '15.99 cm', '15 cm', '7.5 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 30° = adj/hyp. adj = 15 × cos 30° = 15 × 0.8660 = 12.99 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 20 cm. Find the adjacent side.', '20 cm', '15.86 cm', '15.32 cm', '12.86 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 50° = adj/hyp. adj = 20 × cos 50° = 20 × 0.6428 = 12.86 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and hypotenuse = 20 cm. Find the adjacent side.', '15.32 cm', '20 cm', '15.86 cm', '12.86 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 50° = adj/hyp. adj = 20 × cos 50° = 20 × 0.6428 = 12.86 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and hypotenuse = 20 cm. Find the adjacent side.', '17.32 cm', '10.0 cm', '20 cm', '20.32 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'cos 30° = adj/hyp. adj = 20 × cos 30° = 20 × 0.8660 = 17.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and adjacent = 12 cm. Find the opposite side.', '12 cm', '22.78 cm', '6.93 cm', '20.78 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 60° = opp/adj. opp = 12 × tan 60° = 12 × 1.7321 = 20.78 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 35° and adjacent = 12 cm. Find the opposite side.', '17.14 cm', '10.4 cm', '12 cm', '8.4 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 35° = opp/adj. opp = 12 × tan 35° = 12 × 0.7002 = 8.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and adjacent = 12 cm. Find the opposite side.', '12 cm', '12.0 cm', '14.0 cm', 'Cannot determine', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 45° = opp/adj. opp = 12 × tan 45° = 12 × 1.0000 = 12.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and adjacent = 10 cm. Find the opposite side.', '10 cm', 'Cannot determine', '12.0 cm', '10.0 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 45° = opp/adj. opp = 10 × tan 45° = 10 × 1.0000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 45° and adjacent = 15 cm. Find the opposite side.', '17.0 cm', '15 cm', '15.0 cm', 'Cannot determine', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 45° = opp/adj. opp = 15 × tan 45° = 15 × 1.0000 = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and adjacent = 10 cm. Find the opposite side.', '19.32 cm', '17.32 cm', '10 cm', '5.77 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 60° = opp/adj. opp = 10 × tan 60° = 10 × 1.7321 = 17.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 55° and adjacent = 8 cm. Find the opposite side.', '5.6 cm', '8 cm', '11.43 cm', '13.43 cm', 2,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 55° = opp/adj. opp = 8 × tan 55° = 8 × 1.4281 = 11.43 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 30° and adjacent = 12 cm. Find the opposite side.', '20.78 cm', '6.93 cm', '12 cm', '8.93 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 30° = opp/adj. opp = 12 × tan 30° = 12 × 0.5774 = 6.93 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 35° and adjacent = 8 cm. Find the opposite side.', '8 cm', '7.6 cm', '11.43 cm', '5.6 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 35° = opp/adj. opp = 8 × tan 35° = 8 × 0.7002 = 5.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and adjacent = 10 cm. Find the opposite side.', '17.32 cm', '19.32 cm', '5.77 cm', '10 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 60° = opp/adj. opp = 10 × tan 60° = 10 × 1.7321 = 17.32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 40° and adjacent = 8 cm. Find the opposite side.', '8.71 cm', '6.71 cm', '8 cm', '9.53 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 40° = opp/adj. opp = 8 × tan 40° = 8 × 0.8391 = 6.71 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and adjacent = 8 cm. Find the opposite side.', '8 cm', '13.86 cm', '15.86 cm', '4.62 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 60° = opp/adj. opp = 8 × tan 60° = 8 × 1.7321 = 13.86 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 55° and adjacent = 8 cm. Find the opposite side.', '11.43 cm', '5.6 cm', '13.43 cm', '8 cm', 0,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 55° = opp/adj. opp = 8 × tan 55° = 8 × 1.4281 = 11.43 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 55° and adjacent = 8 cm. Find the opposite side.', '13.43 cm', '11.43 cm', '8 cm', '5.6 cm', 1,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 55° = opp/adj. opp = 8 × tan 55° = 8 × 1.4281 = 11.43 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 60° and adjacent = 12 cm. Find the opposite side.', '12 cm', '22.78 cm', '6.93 cm', '20.78 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 60° = opp/adj. opp = 12 × tan 60° = 12 × 1.7321 = 20.78 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right-angled triangle, angle θ = 50° and adjacent = 8 cm. Find the opposite side.', '6.71 cm', '8 cm', '11.53 cm', '9.53 cm', 3,
'lc_ol_trigonometry', 3, 'foundation', 'lc_ol', 'tan 50° = opp/adj. opp = 8 × tan 50° = 8 × 1.1918 = 9.53 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, angle B = 55°, and side a = 12 cm. Find side b.', '15.9 cm', '16.7 cm', '13.9 cm', '14.7 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 55° / sin 45° = 13.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 60°, and side a = 12 cm. Find side b.', '19.4 cm', '16.2 cm', '18.0 cm', '18.2 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 60° / sin 40° = 16.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 60°, and side a = 10 cm. Find side b.', '16.2 cm', '13.5 cm', '15.5 cm', '15.0 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 10 × sin 60° / sin 40° = 13.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 60°, and side a = 18 cm. Find side b.', '27.0 cm', '26.3 cm', '24.3 cm', '29.1 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 60° / sin 40° = 24.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 40°, and side a = 10 cm. Find side b.', '6.2 cm', '7.1 cm', '8.5 cm', '9.1 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 10 × sin 40° / sin 65° = 7.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, angle B = 40°, and side a = 20 cm. Find side b.', '15.7 cm', '18.8 cm', '17.7 cm', '14.5 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 20 × sin 40° / sin 55° = 15.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, angle B = 50°, and side a = 16 cm. Find side b.', '18.0 cm', '17.0 cm', '15.0 cm', '14.5 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 16 × sin 50° / sin 55° = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 40°, and side a = 8 cm. Find side b.', '5.7 cm', '4.9 cm', '7.7 cm', '6.8 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 8 × sin 40° / sin 65° = 5.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, angle B = 50°, and side a = 20 cm. Find side b.', '19.6 cm', '18.3 cm', '14.3 cm', '16.3 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 20 × sin 50° / sin 70° = 16.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, angle B = 65°, and side a = 14 cm. Find side b.', '16.2 cm', '13.5 cm', '15.5 cm', '13.0 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 14 × sin 65° / sin 70° = 13.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 50°, and side a = 10 cm. Find side b.', 'Cannot determine', '12.0 cm', 'Cannot determine', '10.0 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 10 × sin 50° / sin 50° = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 65°, and side a = 14 cm. Find side b.', '14.0 cm', 'Cannot determine', '16.8 cm', '16.0 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 14 × sin 65° / sin 65° = 14.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, angle B = 55°, and side a = 8 cm. Find side b.', '7.6 cm', '9.1 cm', '7.3 cm', '9.6 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 8 × sin 55° / sin 60° = 7.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, angle B = 65°, and side a = 20 cm. Find side b.', '21.7 cm', '25.1 cm', '22.9 cm', '20.9 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 20 × sin 65° / sin 60° = 20.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 55°, and side a = 18 cm. Find side b.', '19.5 cm', '16.3 cm', '15.2 cm', '18.3 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 55° / sin 65° = 16.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 50°, and side a = 20 cm. Find side b.', '22.0 cm', 'Cannot determine', '24.0 cm', '20.0 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 20 × sin 50° / sin 50° = 20.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, angle B = 50°, and side a = 18 cm. Find side b.', '14.7 cm', '12.9 cm', '17.6 cm', '16.7 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 50° / sin 70° = 14.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 40°, and side a = 18 cm. Find side b.', '18.1 cm', '14.4 cm', '15.1 cm', '17.1 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 40° / sin 50° = 15.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, angle B = 55°, and side a = 8 cm. Find side b.', '7.6 cm', '7.3 cm', '9.1 cm', '9.6 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 8 × sin 55° / sin 60° = 7.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 40°, and side a = 15 cm. Find side b.', '14.6 cm', '12.0 cm', '15.1 cm', '12.6 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 15 × sin 40° / sin 50° = 12.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 60°, and side a = 8 cm. Find side b.', '9.6 cm', '9.2 cm', '7.4 cm', '7.6 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 8 × sin 60° / sin 65° = 7.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, angle B = 60°, and side a = 12 cm. Find side b.', '13.1 cm', '12.7 cm', '14.7 cm', '15.2 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 60° / sin 55° = 12.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 40°, and side a = 18 cm. Find side b.', '15.3 cm', '12.8 cm', '14.8 cm', '11.1 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 40° / sin 65° = 12.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 45°, and side a = 15 cm. Find side b.', '13.7 cm', '11.7 cm', '14.0 cm', '10.4 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 15 × sin 45° / sin 65° = 11.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, angle B = 45°, and side a = 14 cm. Find side b.', '10.5 cm', '13.4 cm', '13.7 cm', '11.4 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 14 × sin 45° / sin 60° = 11.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, angle B = 40°, and side a = 12 cm. Find side b.', '13.1 cm', '10.9 cm', '10.7 cm', '12.9 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 40° / sin 45° = 10.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 60°, and side a = 18 cm. Find side b.', '20.6 cm', '19.2 cm', '16.6 cm', '17.2 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 60° / sin 65° = 17.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 45°, and side a = 10 cm. Find side b.', '9.4 cm', '6.9 cm', '7.8 cm', '9.8 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 10 × sin 45° / sin 65° = 7.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, angle B = 45°, and side a = 12 cm. Find side b.', '11.0 cm', '9.0 cm', '10.8 cm', '7.7 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 45° / sin 70° = 9.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 55°, and side a = 16 cm. Find side b.', '19.1 cm', '20.5 cm', '17.1 cm', '17.6 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 16 × sin 55° / sin 50° = 17.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 45°, and side a = 15 cm. Find side b.', '18.5 cm', '16.5 cm', '16.9 cm', '19.8 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 15 × sin 45° / sin 40° = 16.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, angle B = 60°, and side a = 14 cm. Find side b.', '12.9 cm', '12.0 cm', '15.5 cm', '14.9 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 14 × sin 60° / sin 70° = 12.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, angle B = 60°, and side a = 12 cm. Find side b.', '13.3 cm', '13.1 cm', '11.1 cm', '10.3 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 60° / sin 70° = 11.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 60°, and side a = 16 cm. Find side b.', '24.0 cm', '23.6 cm', '25.9 cm', '21.6 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 16 × sin 60° / sin 40° = 21.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 50°, and side a = 14 cm. Find side b.', '14.2 cm', '10.8 cm', '11.8 cm', '13.8 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 14 × sin 50° / sin 65° = 11.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, angle B = 60°, and side a = 16 cm. Find side b.', '18.9 cm', '17.5 cm', '16.9 cm', '20.3 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 16 × sin 60° / sin 55° = 16.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 45°, and side a = 18 cm. Find side b.', '20.2 cm', '19.8 cm', '21.8 cm', '23.8 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 45° / sin 40° = 19.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 55°, and side a = 15 cm. Find side b.', '16.5 cm', '16.0 cm', '18.0 cm', '19.2 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 15 × sin 55° / sin 50° = 16.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 60°, and side a = 15 cm. Find side b.', '18.0 cm', '17.0 cm', '20.3 cm', '19.0 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 15 × sin 60° / sin 50° = 17.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 60°, and side a = 12 cm. Find side b.', '11.1 cm', '13.5 cm', '13.8 cm', '11.5 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 60° / sin 65° = 11.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, angle B = 50°, and side a = 18 cm. Find side b.', '16.4 cm', '20.2 cm', '16.8 cm', '18.8 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 18 × sin 50° / sin 55° = 16.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, angle B = 40°, and side a = 8 cm. Find side b.', '4.9 cm', '6.8 cm', '7.7 cm', '5.7 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 8 × sin 40° / sin 65° = 5.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 55°, and side a = 8 cm. Find side b.', 'Cannot determine', '11.0 cm', '10.2 cm', '12.2 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 8 × sin 55° / sin 40° = 10.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 55°, and side a = 14 cm. Find side b.', '17.0 cm', '15.0 cm', '15.4 cm', '18.0 cm', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 14 × sin 55° / sin 50° = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, angle B = 60°, and side a = 14 cm. Find side b.', '16.8 cm', '14.0 cm', '16.0 cm', 'Cannot determine', 1,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 14 × sin 60° / sin 60° = 14.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 50°, and side a = 15 cm. Find side b.', '18.0 cm', 'Cannot determine', '15.0 cm', '17.0 cm', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 15 × sin 50° / sin 50° = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, angle B = 40°, and side a = 20 cm. Find side b.', 'Cannot determine', '24.0 cm', '22.0 cm', '20.0 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 20 × sin 40° / sin 40° = 20.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, angle B = 60°, and side a = 15 cm. Find side b.', '17.9 cm', '16.4 cm', '19.0 cm', '15.9 cm', 3,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 15 × sin 60° / sin 55° = 15.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, angle B = 65°, and side a = 12 cm. Find side b.', '14.2 cm', '16.2 cm', '17.0 cm', '15.6 cm', 0,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 12 × sin 65° / sin 50° = 14.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, angle B = 60°, and side a = 8 cm. Find side b.', '9.6 cm', '10.0 cm', '8.0 cm', 'Cannot determine', 2,
'lc_ol_trigonometry', 4, 'developing', 'lc_ol', 'Sine Rule: b/sin B = a/sin A. b = 8 × sin 60° / sin 60° = 8.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, side a = 12 cm, side b = 8 cm. Find angle B.', '25.4°', '114.6°', '35.4°', '26.7°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 40° / 12 = 0.4285. B = 25.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 15 cm, side b = 8 cm. Find angle B.', '40.1°', '79.9°', '37.3°', '30.1°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 70° / 15 = 0.5012. B = 30.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 16 cm, side b = 8 cm. Find angle B.', '32.5°', '36.9°', '88.1°', '26.9°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 65° / 16 = 0.4532. B = 26.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, side a = 16 cm, side b = 9 cm. Find angle B.', '37.4°', '97.6°', '27.4°', '30.9°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 55° / 16 = 0.4608. B = 27.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, side a = 16 cm, side b = 8 cm. Find angle B.', '25.0°', '32.5°', '22.5°', '107.5°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 50° / 16 = 0.3830. B = 22.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 14 cm, side b = 9 cm. Find angle B.', '27.0°', '28.9°', '108.0°', '37.0°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 45° / 14 = 0.4546. B = 27.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, side a = 10 cm, side b = 8 cm. Find angle B.', '40.9°', '50.9°', '44.0°', '84.1°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 55° / 10 = 0.6553. B = 40.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, side a = 14 cm, side b = 10 cm. Find angle B.', '27.3°', '28.6°', '37.3°', '112.7°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 40° / 14 = 0.4591. B = 27.3°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 18 cm, side b = 8 cm. Find angle B.', '85.3°', '31.1°', '24.7°', '34.7°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 70° / 18 = 0.4176. B = 24.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 14 cm, side b = 9 cm. Find angle B.', '108.0°', '37.0°', '28.9°', '27.0°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 45° / 14 = 0.4546. B = 27.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 18 cm, side b = 12 cm. Find angle B.', '43.3°', '37.2°', '77.8°', '47.2°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 12 × sin 65° / 18 = 0.6042. B = 37.2°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, side a = 16 cm, side b = 12 cm. Find angle B.', '40.5°', '45.0°', '50.5°', '79.5°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 12 × sin 60° / 16 = 0.6495. B = 40.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, side a = 10 cm, side b = 9 cm. Find angle B.', '104.7°', '36.0°', '45.3°', '35.3°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 40° / 10 = 0.5785. B = 35.3°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, side a = 18 cm, side b = 8 cm. Find angle B.', '22.2°', '19.9°', '29.9°', '110.1°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 50° / 18 = 0.3405. B = 19.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 18 cm, side b = 10 cm. Find angle B.', '78.5°', '38.9°', '41.5°', '31.5°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 70° / 18 = 0.5221. B = 31.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 15 cm, side b = 11 cm. Find angle B.', '43.6°', '66.4°', '51.3°', '53.6°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 11 × sin 70° / 15 = 0.6891. B = 43.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 12 cm, side b = 10 cm. Find angle B.', '59.0°', '54.2°', '49.0°', '66.0°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 65° / 12 = 0.7553. B = 49.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 15 cm, side b = 13 cm. Find angle B.', '39.0°', '97.2°', '37.8°', '47.8°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 13 × sin 45° / 15 = 0.6128. B = 37.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, side a = 12 cm, side b = 10 cm. Find angle B.', '43.0°', '53.0°', '45.8°', '82.0°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 55° / 12 = 0.6826. B = 43.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, side a = 10 cm, side b = 8 cm. Find angle B.', '40.9°', '30.9°', '32.0°', '109.1°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 40° / 10 = 0.5142. B = 30.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 15 cm, side b = 9 cm. Find angle B.', '32.9°', '82.1°', '42.9°', '39.0°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 65° / 15 = 0.5438. B = 32.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 16 cm, side b = 12 cm. Find angle B.', '52.5°', '65.2°', '54.8°', '44.8°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 12 × sin 70° / 16 = 0.7048. B = 44.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 16 cm, side b = 13 cm. Find angle B.', '59.8°', '56.9°', '60.2°', '49.8°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 13 × sin 70° / 16 = 0.7635. B = 49.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 14 cm, side b = 12 cm. Find angle B.', '55.7°', '51.0°', '61.0°', '64.0°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 12 × sin 65° / 14 = 0.7768. B = 51.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 10 cm, side b = 8 cm. Find angle B.', '100.6°', '44.4°', '34.4°', '36.0°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 45° / 10 = 0.5657. B = 34.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 15 cm, side b = 9 cm. Find angle B.', '82.1°', '39.0°', '42.9°', '32.9°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 65° / 15 = 0.5438. B = 32.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, side a = 14 cm, side b = 10 cm. Find angle B.', '27.3°', '112.7°', '37.3°', '28.6°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 40° / 14 = 0.4591. B = 27.3°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, side a = 10 cm, side b = 8 cm. Find angle B.', '84.1°', '44.0°', '50.9°', '40.9°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 55° / 10 = 0.6553. B = 40.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 60°, side a = 18 cm, side b = 8 cm. Find angle B.', '26.7°', '22.6°', '97.4°', '32.6°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 60° / 18 = 0.3849. B = 22.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, side a = 18 cm, side b = 13 cm. Find angle B.', '43.6°', '96.4°', '33.6°', '36.1°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 13 × sin 50° / 18 = 0.5533. B = 33.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, side a = 15 cm, side b = 10 cm. Find angle B.', '43.1°', '36.7°', '91.9°', '33.1°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 55° / 15 = 0.5461. B = 33.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 12 cm, side b = 10 cm. Find angle B.', '54.2°', '49.0°', '59.0°', '66.0°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 65° / 12 = 0.7553. B = 49.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, side a = 16 cm, side b = 8 cm. Find angle B.', '121.3°', '20.0°', '28.7°', '18.7°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 40° / 16 = 0.3214. B = 18.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 15 cm, side b = 13 cm. Find angle B.', '39.0°', '37.8°', '97.2°', '47.8°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 13 × sin 45° / 15 = 0.6128. B = 37.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 18 cm, side b = 12 cm. Find angle B.', '106.9°', '28.1°', '30.0°', '38.1°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 12 × sin 45° / 18 = 0.4714. B = 28.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 15 cm, side b = 13 cm. Find angle B.', '51.8°', '56.3°', '63.2°', '61.8°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 13 × sin 65° / 15 = 0.7855. B = 51.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, side a = 15 cm, side b = 10 cm. Find angle B.', '99.3°', '40.7°', '30.7°', '33.3°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 50° / 15 = 0.5107. B = 30.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 12 cm, side b = 10 cm. Find angle B.', '58.3°', '58.5°', '51.5°', '61.5°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 70° / 12 = 0.7831. B = 51.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 65°, side a = 10 cm, side b = 8 cm. Find angle B.', '56.5°', '52.0°', '46.5°', '68.5°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 65° / 10 = 0.7250. B = 46.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 16 cm, side b = 8 cm. Find angle B.', '22.5°', '114.3°', '20.7°', '30.7°', 2,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 45° / 16 = 0.3536. B = 20.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 10 cm, side b = 9 cm. Find angle B.', '57.7°', '67.7°', '63.0°', '52.3°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 70° / 10 = 0.8457. B = 57.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 12 cm, side b = 9 cm. Find angle B.', '44.8°', '54.8°', '52.5°', '65.2°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 70° / 12 = 0.7048. B = 44.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 14 cm, side b = 8 cm. Find angle B.', '23.8°', '25.7°', '33.8°', '111.2°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 45° / 14 = 0.4041. B = 23.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 18 cm, side b = 11 cm. Find angle B.', '35.0°', '42.8°', '45.0°', '75.0°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 11 × sin 70° / 18 = 0.5743. B = 35.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 50°, side a = 16 cm, side b = 10 cm. Find angle B.', '31.2°', '101.4°', '38.6°', '28.6°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 50° / 16 = 0.4788. B = 28.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, side a = 16 cm, side b = 9 cm. Find angle B.', '30.9°', '27.4°', '37.4°', '97.6°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 55° / 16 = 0.4608. B = 27.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 55°, side a = 18 cm, side b = 9 cm. Find angle B.', '27.5°', '24.2°', '100.8°', '34.2°', 1,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 55° / 18 = 0.4096. B = 24.2°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 45°, side a = 12 cm, side b = 9 cm. Find angle B.', '32.0°', '42.0°', '33.8°', '103.0°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 9 × sin 45° / 12 = 0.5303. B = 32.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 70°, side a = 12 cm, side b = 10 cm. Find angle B.', '51.5°', '61.5°', '58.3°', '58.5°', 0,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 10 × sin 70° / 12 = 0.7831. B = 51.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: angle A = 40°, side a = 14 cm, side b = 8 cm. Find angle B.', '31.5°', '22.9°', '118.5°', '21.5°', 3,
'lc_ol_trigonometry', 5, 'developing', 'lc_ol', 'Sine Rule: sin B/b = sin A/a. sin B = 8 × sin 40° / 14 = 0.3673. B = 21.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 10 cm, c = 15 cm, angle A = 70°. Find side a.', '14.9 cm', '18.0 cm', '17.1 cm', '16.9 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 10² + 15² - 2(10)(15)cos 70° = 222.4. a = 14.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 8 cm, angle A = 50°. Find side a.', '16.1 cm', '12.8 cm', '12.4 cm', '10.8 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 8² - 2(14)(8)cos 50° = 116.0. a = 10.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 12 cm, c = 10 cm, angle A = 110°. Find side a.', '20.1 cm', '15.6 cm', '20.8 cm', '18.1 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 12² + 10² - 2(12)(10)cos 110° = 326.1. a = 18.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 15 cm, angle A = 120°. Find side a.', '27.1 cm', '20.5 cm', '25.1 cm', '28.9 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 15² - 2(14)(15)cos 120° = 631.0. a = 25.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 14 cm, angle A = 80°. Find side a.', '16.9 cm', '14.9 cm', '16.1 cm', '17.1 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 14² - 2(8)(14)cos 80° = 221.1. a = 14.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 14 cm, angle A = 110°. Find side a.', '27.3 cm', '23.8 cm', '20.5 cm', '25.8 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 14² - 2(15)(14)cos 110° = 564.6. a = 23.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 12 cm, c = 8 cm, angle A = 70°. Find side a.', '13.7 cm', '11.9 cm', '14.4 cm', '13.9 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 12² + 8² - 2(12)(8)cos 70° = 142.3. a = 11.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 12 cm, angle A = 120°. Find side a.', '14.4 cm', '20.1 cm', '19.4 cm', '17.4 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 12² - 2(8)(12)cos 120° = 304.0. a = 17.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 8 cm, angle A = 80°. Find side a.', '14.9 cm', '17.1 cm', '16.1 cm', '16.9 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 8² - 2(14)(8)cos 80° = 221.1. a = 14.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 10 cm, c = 14 cm, angle A = 60°. Find side a.', '14.4 cm', '12.5 cm', '14.5 cm', '17.2 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 10² + 14² - 2(10)(14)cos 60° = 156.0. a = 12.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 8 cm, angle A = 80°. Find side a.', '16.1 cm', '16.9 cm', '17.1 cm', '14.9 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 8² - 2(14)(8)cos 80° = 221.1. a = 14.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 8 cm, angle A = 110°. Find side a.', '15.1 cm', '11.3 cm', 'Cannot determine', '13.1 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 8² - 2(8)(8)cos 110° = 171.8. a = 13.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 15 cm, angle A = 50°. Find side a.', '14.6 cm', '14.7 cm', '12.7 cm', '21.2 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 15² - 2(15)(15)cos 50° = 160.7. a = 12.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 12 cm, angle A = 60°. Find side a.', '12.2 cm', '10.6 cm', '14.4 cm', '12.6 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 12² - 2(8)(12)cos 60° = 112.0. a = 10.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 10 cm, angle A = 40°. Find side a.', '11.2 cm', '18.0 cm', '9.8 cm', '11.8 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 10² - 2(15)(10)cos 40° = 95.2. a = 9.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 14 cm, angle A = 40°. Find side a.', '11.5 cm', '20.5 cm', '10.0 cm', '12.0 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 14² - 2(15)(14)cos 40° = 99.3. a = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 15 cm, angle A = 50°. Find side a.', '14.6 cm', '21.2 cm', '14.7 cm', '12.7 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 15² - 2(15)(15)cos 50° = 160.7. a = 12.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 8 cm, angle A = 100°. Find side a.', '20.9 cm', '17.0 cm', '18.2 cm', '20.2 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 8² - 2(15)(8)cos 100° = 330.7. a = 18.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 10 cm, c = 12 cm, angle A = 70°. Find side a.', '12.7 cm', '14.7 cm', '15.6 cm', '14.6 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 10² + 12² - 2(10)(12)cos 70° = 161.9. a = 12.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 14 cm, angle A = 80°. Find side a.', '20.7 cm', '19.8 cm', '20.0 cm', '18.0 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 14² - 2(14)(14)cos 80° = 323.9. a = 18.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 10 cm, angle A = 110°. Find side a.', '17.2 cm', '19.8 cm', '22.8 cm', '21.8 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 10² - 2(14)(10)cos 110° = 391.8. a = 19.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 15 cm, angle A = 50°. Find side a.', '14.7 cm', '14.6 cm', '21.2 cm', '12.7 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 15² - 2(15)(15)cos 50° = 160.7. a = 12.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 14 cm, angle A = 60°. Find side a.', '14.2 cm', '16.1 cm', '14.0 cm', '12.2 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 14² - 2(8)(14)cos 60° = 148.0. a = 12.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 10 cm, c = 14 cm, angle A = 80°. Find side a.', '18.1 cm', '15.7 cm', '17.7 cm', '17.2 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 10² + 14² - 2(10)(14)cos 80° = 247.4. a = 15.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 14 cm, angle A = 100°. Find side a.', '19.8 cm', '23.4 cm', '21.4 cm', '24.7 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 14² - 2(14)(14)cos 100° = 460.1. a = 21.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 12 cm, c = 12 cm, angle A = 40°. Find side a.', '8.2 cm', '17.0 cm', '10.2 cm', '9.4 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 12² + 12² - 2(12)(12)cos 40° = 67.4. a = 8.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 15 cm, angle A = 40°. Find side a.', '10.0 cm', '12.0 cm', '20.5 cm', '11.5 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 15² - 2(14)(15)cos 40° = 99.3. a = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 8 cm, angle A = 50°. Find side a.', '12.4 cm', '10.8 cm', '12.8 cm', '16.1 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 8² - 2(14)(8)cos 50° = 116.0. a = 10.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 12 cm, angle A = 50°. Find side a.', '9.2 cm', '14.4 cm', '10.6 cm', '11.2 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 12² - 2(8)(12)cos 50° = 84.6. a = 9.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 14 cm, angle A = 50°. Find side a.', '12.8 cm', '12.4 cm', '16.1 cm', '10.8 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 14² - 2(8)(14)cos 50° = 116.0. a = 10.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 15 cm, angle A = 110°. Find side a.', '17.0 cm', '19.3 cm', '22.2 cm', '21.3 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 15² - 2(8)(15)cos 110° = 371.1. a = 19.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 12 cm, c = 10 cm, angle A = 40°. Find side a.', '15.6 cm', '7.8 cm', '8.9 cm', '9.8 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 12² + 10² - 2(12)(10)cos 40° = 60.1. a = 7.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 12 cm, angle A = 60°. Find side a.', '15.8 cm', '19.2 cm', '15.7 cm', '13.7 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 12² - 2(15)(12)cos 60° = 189.0. a = 13.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 10 cm, c = 10 cm, angle A = 40°. Find side a.', '14.1 cm', '8.8 cm', '7.9 cm', '6.8 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 10² + 10² - 2(10)(10)cos 40° = 46.8. a = 6.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 10 cm, c = 12 cm, angle A = 50°. Find side a.', '9.5 cm', '15.6 cm', '11.5 cm', '10.9 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 10² + 12² - 2(10)(12)cos 50° = 89.7. a = 9.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 10 cm, angle A = 80°. Find side a.', '19.0 cm', '18.5 cm', '18.0 cm', '16.5 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 10² - 2(15)(10)cos 80° = 272.9. a = 16.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 8 cm, angle A = 100°. Find side a.', '14.3 cm', '12.3 cm', '11.3 cm', '14.1 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 8² - 2(8)(8)cos 100° = 150.2. a = 12.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 15 cm, angle A = 70°. Find side a.', '20.5 cm', '19.2 cm', '18.7 cm', '16.7 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 15² - 2(14)(15)cos 70° = 277.4. a = 16.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 8 cm, angle A = 70°. Find side a.', '15.6 cm', '15.5 cm', '16.1 cm', '13.5 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 8² - 2(14)(8)cos 70° = 183.4. a = 13.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 10 cm, c = 8 cm, angle A = 120°. Find side a.', '15.6 cm', '12.8 cm', '17.6 cm', '18.0 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 10² + 8² - 2(10)(8)cos 120° = 244.0. a = 15.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 8 cm, angle A = 50°. Find side a.', '10.8 cm', '12.8 cm', '12.4 cm', '16.1 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 8² - 2(14)(8)cos 50° = 116.0. a = 10.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 14 cm, angle A = 70°. Find side a.', '16.1 cm', '18.5 cm', '18.1 cm', '19.8 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 14² - 2(14)(14)cos 70° = 257.9. a = 16.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 8 cm, angle A = 50°. Find side a.', '6.8 cm', '8.8 cm', '7.8 cm', '11.3 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 8² - 2(8)(8)cos 50° = 45.7. a = 6.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 10 cm, angle A = 40°. Find side a.', '11.2 cm', '18.0 cm', '11.8 cm', '9.8 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 10² - 2(15)(10)cos 40° = 95.2. a = 9.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 15 cm, c = 8 cm, angle A = 80°. Find side a.', '18.1 cm', '17.0 cm', '15.7 cm', '17.7 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 15² + 8² - 2(15)(8)cos 80° = 247.3. a = 15.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 14 cm, c = 12 cm, angle A = 70°. Find side a.', '15.0 cm', '18.4 cm', '17.0 cm', '17.3 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 14² + 12² - 2(14)(12)cos 70° = 225.1. a = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 10 cm, angle A = 50°. Find side a.', '9.8 cm', '12.8 cm', '9.0 cm', '7.8 cm', 3,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 10² - 2(8)(10)cos 50° = 61.2. a = 7.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 14 cm, angle A = 120°. Find side a.', '22.2 cm', '16.1 cm', '19.3 cm', '21.3 cm', 2,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 14² - 2(8)(14)cos 120° = 372.0. a = 19.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 8 cm, angle A = 120°. Find side a.', 'Cannot determine', '13.9 cm', '11.3 cm', '15.9 cm', 1,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 8² - 2(8)(8)cos 120° = 192.0. a = 13.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: b = 8 cm, c = 14 cm, angle A = 60°. Find side a.', '12.2 cm', '14.0 cm', '14.2 cm', '16.1 cm', 0,
'lc_ol_trigonometry', 6, 'developing', 'lc_ol', 'Cosine Rule: a² = b² + c² - 2bc·cos A = 8² + 14² - 2(8)(14)cos 60° = 148.0. a = 12.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 13 cm, c = 6 cm. Find angle A.', '82.0°', '67.0°', '57.0°', '113.0°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (13² + 6² - 12²)/(2×13×6) = 0.3910. A = 67.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 13 cm, c = 8 cm. Find angle A.', '54.7°', '115.3°', '64.7°', '79.7°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (13² + 8² - 12²)/(2×13×8) = 0.4279. A = 64.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 8 cm, b = 12 cm, c = 11 cm. Find angle A.', '40.4°', '139.6°', '55.4°', '30.4°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 11² - 8²)/(2×12×11) = 0.7614. A = 40.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 12 cm, c = 11 cm. Find angle A.', '71.9°', '123.1°', '46.9°', '56.9°', 3,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 11² - 11²)/(2×12×11) = 0.5455. A = 56.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 13 cm, c = 8 cm. Find angle A.', '54.7°', '79.7°', '64.7°', '115.3°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (13² + 8² - 12²)/(2×13×8) = 0.4279. A = 64.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 8 cm, c = 6 cm. Find angle A.', '132.3°', '107.3°', '117.3°', '62.7°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 6² - 12²)/(2×8×6) = -0.4583. A = 117.3°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 12 cm, c = 6 cm. Find angle A.', '55.8°', '65.8°', '80.8°', '114.2°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 6² - 11²)/(2×12×6) = 0.4097. A = 65.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 10 cm, b = 11 cm, c = 11 cm. Find angle A.', '44.1°', '125.9°', '54.1°', '69.1°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 11² - 10²)/(2×11×11) = 0.5868. A = 54.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 9 cm, b = 13 cm, c = 9 cm. Find angle A.', '33.8°', '43.8°', '58.8°', '136.2°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (13² + 9² - 9²)/(2×13×9) = 0.7222. A = 43.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 9 cm, b = 8 cm, c = 8 cm. Find angle A.', '83.5°', '58.5°', '68.5°', '111.5°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 8² - 9²)/(2×8×8) = 0.3672. A = 68.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 9 cm, c = 11 cm. Find angle A.', '39.4°', '29.4°', '54.4°', '140.6°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (9² + 11² - 7²)/(2×9×11) = 0.7727. A = 39.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 8 cm, c = 8 cm. Find angle A.', '86.9°', '101.9°', '93.1°', '76.9°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 8² - 11²)/(2×8×8) = 0.0547. A = 86.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 9 cm, b = 12 cm, c = 11 cm. Find angle A.', '134.2°', '35.8°', '45.8°', '60.8°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 11² - 9²)/(2×12×11) = 0.6970. A = 45.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 10 cm, b = 11 cm, c = 8 cm. Find angle A.', '76.1°', '118.9°', '61.1°', '51.1°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 8² - 10²)/(2×11×8) = 0.4830. A = 61.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 9 cm, b = 12 cm, c = 9 cm. Find angle A.', '63.2°', '48.2°', '38.2°', '131.8°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 9² - 9²)/(2×12×9) = 0.6667. A = 48.2°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 10 cm, c = 6 cm. Find angle A.', '58.5°', '43.5°', '33.5°', '136.5°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (10² + 6² - 7²)/(2×10×6) = 0.7250. A = 43.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 10 cm, b = 8 cm, c = 8 cm. Find angle A.', '92.4°', '67.4°', '77.4°', '102.6°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 8² - 10²)/(2×8×8) = 0.2188. A = 77.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 10 cm, b = 12 cm, c = 8 cm. Find angle A.', '70.8°', '45.8°', '124.2°', '55.8°', 3,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 8² - 10²)/(2×12×8) = 0.5625. A = 55.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 10 cm, c = 6 cm. Find angle A.', '136.5°', '58.5°', '33.5°', '43.5°', 3,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (10² + 6² - 7²)/(2×10×6) = 0.7250. A = 43.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 8 cm, c = 9 cm. Find angle A.', '70.4°', '99.6°', '95.4°', '80.4°', 3,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 9² - 11²)/(2×8×9) = 0.1667. A = 80.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 12 cm, c = 6 cm. Find angle A.', '75.5°', '104.5°', '65.5°', '90.5°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 6² - 12²)/(2×12×6) = 0.2500. A = 75.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 11 cm, c = 6 cm. Find angle A.', '74.2°', '105.8°', '64.2°', '89.2°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 6² - 11²)/(2×11×6) = 0.2727. A = 74.2°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 10 cm, c = 11 cm. Find angle A.', '117.0°', '53.0°', '63.0°', '78.0°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (10² + 11² - 11²)/(2×10×11) = 0.4545. A = 63.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 11 cm, c = 10 cm. Find angle A.', '63.0°', '78.0°', '117.0°', '53.0°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 10² - 11²)/(2×11×10) = 0.4545. A = 63.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 13 cm, c = 8 cm. Find angle A.', '42.8°', '17.8°', '27.8°', '152.2°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (13² + 8² - 7²)/(2×13×8) = 0.8846. A = 27.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 8 cm, c = 6 cm. Find angle A.', '57.9°', '47.9°', '72.9°', '122.1°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 6² - 7²)/(2×8×6) = 0.5312. A = 57.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 8 cm, b = 9 cm, c = 8 cm. Find angle A.', '55.8°', '124.2°', '70.8°', '45.8°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (9² + 8² - 8²)/(2×9×8) = 0.5625. A = 55.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 9 cm, c = 7 cm. Find angle A.', '86.4°', '83.6°', '111.4°', '96.4°', 3,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (9² + 7² - 12²)/(2×9×7) = -0.1111. A = 96.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 10 cm, b = 12 cm, c = 10 cm. Find angle A.', '53.1°', '126.9°', '43.1°', '68.1°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 10² - 10²)/(2×12×10) = 0.6000. A = 53.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 10 cm, b = 10 cm, c = 7 cm. Find angle A.', '84.5°', '110.5°', '69.5°', '59.5°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (10² + 7² - 10²)/(2×10×7) = 0.3500. A = 69.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 12 cm, c = 6 cm. Find angle A.', '14.5°', '24.5°', '39.5°', '155.5°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 6² - 7²)/(2×12×6) = 0.9097. A = 24.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 10 cm, b = 10 cm, c = 8 cm. Find angle A.', '113.6°', '66.4°', '81.4°', '56.4°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (10² + 8² - 10²)/(2×10×8) = 0.4000. A = 66.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 9 cm, b = 12 cm, c = 9 cm. Find angle A.', '131.8°', '63.2°', '48.2°', '38.2°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (12² + 9² - 9²)/(2×12×9) = 0.6667. A = 48.2°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 9 cm, c = 8 cm. Find angle A.', '80.4°', '99.6°', '70.4°', '95.4°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (9² + 8² - 11²)/(2×9×8) = 0.1667. A = 80.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 8 cm, c = 6 cm. Find angle A.', '92.6°', '77.4°', '102.6°', '117.6°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 6² - 11²)/(2×8×6) = -0.2188. A = 102.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 11 cm, c = 9 cm. Find angle A.', '39.4°', '29.4°', '54.4°', '140.6°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 9² - 7²)/(2×11×9) = 0.7727. A = 39.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 8 cm, c = 11 cm. Find angle A.', '91.5°', '66.5°', '103.5°', '76.5°', 3,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 11² - 12²)/(2×8×11) = 0.2330. A = 76.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 8 cm, c = 7 cm. Find angle A.', '96.1°', '73.9°', '106.1°', '121.1°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 7² - 12²)/(2×8×7) = -0.2768. A = 106.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 13 cm, c = 8 cm. Find angle A.', '57.4°', '72.4°', '47.4°', '122.6°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (13² + 8² - 11²)/(2×13×8) = 0.5385. A = 57.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 11 cm, c = 9 cm. Find angle A.', '114.1°', '65.9°', '80.9°', '55.9°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 9² - 11²)/(2×11×9) = 0.4091. A = 65.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 8 cm, c = 9 cm. Find angle A.', '70.4°', '80.4°', '95.4°', '99.6°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 9² - 11²)/(2×8×9) = 0.1667. A = 80.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 12 cm, b = 11 cm, c = 8 cm. Find angle A.', '76.5°', '91.5°', '66.5°', '103.5°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 8² - 12²)/(2×11×8) = 0.2330. A = 76.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 11 cm, c = 9 cm. Find angle A.', '65.9°', '80.9°', '114.1°', '55.9°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 9² - 11²)/(2×11×9) = 0.4091. A = 65.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 10 cm, c = 9 cm. Find angle A.', '85.5°', '109.5°', '70.5°', '60.5°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (10² + 9² - 11²)/(2×10×9) = 0.3333. A = 70.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 7 cm, b = 8 cm, c = 8 cm. Find angle A.', '128.1°', '41.9°', '51.9°', '66.9°', 2,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (8² + 8² - 7²)/(2×8×8) = 0.6172. A = 51.9°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 11 cm, c = 8 cm. Find angle A.', '58.7°', '68.7°', '111.3°', '83.7°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 8² - 11²)/(2×11×8) = 0.3636. A = 68.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 10 cm, c = 11 cm. Find angle A.', '63.0°', '117.0°', '53.0°', '78.0°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (10² + 11² - 11²)/(2×10×11) = 0.4545. A = 63.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 8 cm, b = 11 cm, c = 9 cm. Find angle A.', '45.8°', '134.2°', '35.8°', '60.8°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (11² + 9² - 8²)/(2×11×9) = 0.6970. A = 45.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 11 cm, b = 13 cm, c = 9 cm. Find angle A.', '46.5°', '56.5°', '123.5°', '71.5°', 1,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (13² + 9² - 11²)/(2×13×9) = 0.5513. A = 56.5°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: a = 9 cm, b = 9 cm, c = 8 cm. Find angle A.', '63.6°', '116.4°', '53.6°', '78.6°', 0,
'lc_ol_trigonometry', 7, 'proficient', 'lc_ol', 'cos A = (b² + c² - a²)/(2bc) = (9² + 8² - 9²)/(2×9×8) = 0.4444. A = 63.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 12 cm, b = 10 cm, and angle C = 70°.', '56.4 cm²', '60.0 cm²', '61.4 cm²', '120 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 12 × 10 × sin 70° = 56.4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 15 cm, b = 12 cm, and angle C = 80°.', '90.0 cm²', '93.6 cm²', '88.6 cm²', '180 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 15 × 12 × sin 80° = 88.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 12 cm, b = 8 cm, and angle C = 45°.', '48.0 cm²', '33.9 cm²', '96 cm²', '38.9 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 12 × 8 × sin 45° = 33.9 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 14 cm, b = 6 cm, and angle C = 45°.', '42.0 cm²', '34.7 cm²', '84 cm²', '29.7 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 14 × 6 × sin 45° = 29.7 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 15 cm, b = 6 cm, and angle C = 110°.', '90 cm²', '45.0 cm²', '42.3 cm²', '47.3 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 15 × 6 × sin 110° = 42.3 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 15 cm, b = 10 cm, and angle C = 100°.', '78.9 cm²', '73.9 cm²', '75.0 cm²', '150 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 15 × 10 × sin 100° = 73.9 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 14 cm, b = 8 cm, and angle C = 45°.', '56.0 cm²', '112 cm²', '39.6 cm²', '44.6 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 14 × 8 × sin 45° = 39.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 8 cm, and angle C = 90°.', '29.0 cm²', '48 cm²', 'Cannot determine', '24.0 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 8 × sin 90° = 24.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 12 cm, b = 10 cm, and angle C = 80°.', '120 cm²', '59.1 cm²', '64.1 cm²', '60.0 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 12 × 10 × sin 80° = 59.1 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 12 cm, b = 14 cm, and angle C = 30°.', '168 cm²', '84.0 cm²', '47.0 cm²', '42.0 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 12 × 14 × sin 30° = 42.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 15 cm, b = 12 cm, and angle C = 60°.', '82.9 cm²', '77.9 cm²', '90.0 cm²', '180 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 15 × 12 × sin 60° = 77.9 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 8 cm, b = 14 cm, and angle C = 60°.', '53.5 cm²', '48.5 cm²', '56.0 cm²', '112 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 8 × 14 × sin 60° = 48.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 12 cm, b = 14 cm, and angle C = 80°.', '84.0 cm²', '168 cm²', '82.7 cm²', '87.7 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 12 × 14 × sin 80° = 82.7 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 15 cm, b = 10 cm, and angle C = 120°.', '75.0 cm²', '65.0 cm²', '70.0 cm²', '150 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 15 × 10 × sin 120° = 65.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 12 cm, and angle C = 45°.', '30.5 cm²', '36.0 cm²', '72 cm²', '25.5 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 12 × sin 45° = 25.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 14 cm, b = 8 cm, and angle C = 80°.', '55.1 cm²', '112 cm²', '56.0 cm²', '60.1 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 14 × 8 × sin 80° = 55.1 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 10 cm, b = 8 cm, and angle C = 110°.', '80 cm²', '42.6 cm²', '37.6 cm²', '40.0 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 10 × 8 × sin 110° = 37.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 15 cm, b = 8 cm, and angle C = 80°.', '59.1 cm²', '64.1 cm²', '60.0 cm²', '120 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 15 × 8 × sin 80° = 59.1 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 15 cm, and angle C = 80°.', '49.3 cm²', '45.0 cm²', '44.3 cm²', '90 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 15 × sin 80° = 44.3 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 10 cm, b = 15 cm, and angle C = 110°.', '150 cm²', '75.0 cm²', '75.5 cm²', '70.5 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 10 × 15 × sin 110° = 70.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 6 cm, and angle C = 30°.', '36 cm²', '9.0 cm²', '18.0 cm²', '14.0 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 6 × sin 30° = 9.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 10 cm, b = 12 cm, and angle C = 80°.', '120 cm²', '60.0 cm²', '59.1 cm²', '64.1 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 10 × 12 × sin 80° = 59.1 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 15 cm, b = 10 cm, and angle C = 50°.', '150 cm²', '62.5 cm²', '57.5 cm²', '75.0 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 15 × 10 × sin 50° = 57.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 6 cm, and angle C = 70°.', '16.9 cm²', '36 cm²', '21.9 cm²', '18.0 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 6 × sin 70° = 16.9 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 10 cm, and angle C = 90°.', '60 cm²', 'Cannot determine', '30.0 cm²', '35.0 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 10 × sin 90° = 30.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 8 cm, b = 14 cm, and angle C = 90°.', '56.0 cm²', '61.0 cm²', 'Cannot determine', '112 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 8 × 14 × sin 90° = 56.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 10 cm, b = 10 cm, and angle C = 30°.', '50.0 cm²', '100 cm²', '30.0 cm²', '25.0 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 10 × 10 × sin 30° = 25.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 14 cm, b = 12 cm, and angle C = 70°.', '78.9 cm²', '84.0 cm²', '83.9 cm²', '168 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 14 × 12 × sin 70° = 78.9 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 10 cm, b = 14 cm, and angle C = 50°.', '53.6 cm²', '140 cm²', '58.6 cm²', '70.0 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 10 × 14 × sin 50° = 53.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 14 cm, b = 10 cm, and angle C = 50°.', '58.6 cm²', '53.6 cm²', '70.0 cm²', '140 cm²', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 14 × 10 × sin 50° = 53.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 15 cm, and angle C = 100°.', '90 cm²', '45.0 cm²', '49.3 cm²', '44.3 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 15 × sin 100° = 44.3 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 12 cm, and angle C = 80°.', '36.0 cm²', '72 cm²', '40.5 cm²', '35.5 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 12 × sin 80° = 35.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 6 cm, b = 14 cm, and angle C = 80°.', '84 cm²', '46.4 cm²', '42.0 cm²', '41.4 cm²', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 6 × 14 × sin 80° = 41.4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 10 cm, b = 15 cm, and angle C = 80°.', '73.9 cm²', '75.0 cm²', '150 cm²', '78.9 cm²', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 10 × 15 × sin 80° = 73.9 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle ABC where a = 12 cm, b = 15 cm, and angle C = 60°.', '90.0 cm²', '180 cm²', '77.9 cm²', '82.9 cm²', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C = ½ × 12 × 15 × sin 60° = 77.9 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 24 cm², side a = 12 cm, angle C = 45°. Find side b.', '4.0 cm', '8.7 cm', '2.0 cm', '5.7 cm', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 24 = ½ × 12 × b × sin 45°. b = 5.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 20 cm², side a = 8 cm, angle C = 30°. Find side b.', '2.5 cm', '13.0 cm', '5.0 cm', '10.0 cm', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 20 = ½ × 8 × b × sin 30°. b = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 36 cm², side a = 10 cm, angle C = 30°. Find side b.', '3.6 cm', '14.4 cm', '17.4 cm', '7.2 cm', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 36 = ½ × 10 × b × sin 30°. b = 14.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 20 cm², side a = 14 cm, angle C = 60°. Find side b.', '3.3 cm', '2.9 cm', '6.3 cm', '1.4 cm', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 20 = ½ × 14 × b × sin 60°. b = 3.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 36 cm², side a = 12 cm, angle C = 60°. Find side b.', '6.9 cm', '9.9 cm', '3.0 cm', '6.0 cm', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 36 = ½ × 12 × b × sin 60°. b = 6.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 36 cm², side a = 8 cm, angle C = 90°. Find side b.', 'Cannot determine', '4.5 cm', '9.0 cm', '12.0 cm', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 36 = ½ × 8 × b × sin 90°. b = 9.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 40 cm², side a = 8 cm, angle C = 45°. Find side b.', '17.1 cm', '10.0 cm', '14.1 cm', '5.0 cm', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 40 = ½ × 8 × b × sin 45°. b = 14.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 48 cm², side a = 8 cm, angle C = 30°. Find side b.', '12.0 cm', '6.0 cm', '27.0 cm', '24.0 cm', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 48 = ½ × 8 × b × sin 30°. b = 24.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 48 cm², side a = 14 cm, angle C = 45°. Find side b.', '12.7 cm', '6.9 cm', '9.7 cm', '3.4 cm', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 48 = ½ × 14 × b × sin 45°. b = 9.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 48 cm², side a = 10 cm, angle C = 90°. Find side b.', 'Cannot determine', '12.6 cm', '4.8 cm', '9.6 cm', 3,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 48 = ½ × 10 × b × sin 90°. b = 9.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 36 cm², side a = 12 cm, angle C = 90°. Find side b.', 'Cannot determine', '3.0 cm', '6.0 cm', '9.0 cm', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 36 = ½ × 12 × b × sin 90°. b = 6.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 40 cm², side a = 10 cm, angle C = 45°. Find side b.', '11.3 cm', '8.0 cm', '14.3 cm', '4.0 cm', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 40 = ½ × 10 × b × sin 45°. b = 11.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 40 cm², side a = 10 cm, angle C = 90°. Find side b.', '11.0 cm', 'Cannot determine', '8.0 cm', '4.0 cm', 2,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 40 = ½ × 10 × b × sin 90°. b = 8.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 36 cm², side a = 12 cm, angle C = 60°. Find side b.', '6.9 cm', '3.0 cm', '9.9 cm', '6.0 cm', 0,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 36 = ½ × 12 × b × sin 60°. b = 6.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC has area 30 cm², side a = 14 cm, angle C = 90°. Find side b.', '2.1 cm', '4.3 cm', '7.3 cm', 'Cannot determine', 1,
'lc_ol_trigonometry', 8, 'proficient', 'lc_ol', 'Area = ½ab·sin C. 30 = ½ × 14 × b × sin 90°. b = 4.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of East?', '090°', '135°', '180°', '270°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. East = 090°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of South?', '225°', '270°', '180°', '000°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. South = 180°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of West?', '090°', '270°', '315°', '000°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. West = 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North-West?', '045°', '315°', '000°', '135°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North-West = 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North-West?', '000°', '045°', '315°', '135°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North-West = 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North?', '000°', '090°', '180°', '045°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North = 000°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of East?', '090°', '180°', '270°', '135°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. East = 090°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North-West?', '315°', '000°', '135°', '045°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North-West = 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North?', '045°', '090°', '180°', '000°', 3,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North = 000°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of South-West?', '270°', '315°', '225°', '045°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. South-West = 225°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of West?', '315°', '270°', '000°', '090°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. West = 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of East?', '270°', '090°', '135°', '180°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. East = 090°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North-West?', '045°', '000°', '315°', '135°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North-West = 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of East?', '090°', '270°', '180°', '135°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. East = 090°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of South-East?', '225°', '315°', '135°', '180°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. South-East = 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of South-East?', '225°', '180°', '315°', '135°', 3,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. South-East = 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North?', '090°', '000°', '045°', '180°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North = 000°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of West?', '315°', '000°', '270°', '090°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. West = 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North-East?', '090°', '045°', '135°', '225°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North-East = 045°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of South?', '225°', '180°', '000°', '270°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. South = 180°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of West?', '315°', '000°', '270°', '090°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. West = 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of South-East?', '315°', '180°', '225°', '135°', 3,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. South-East = 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of East?', '270°', '090°', '135°', '180°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. East = 090°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of West?', '315°', '000°', '270°', '090°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. West = 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the bearing of North?', '045°', '000°', '180°', '090°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Bearings are measured clockwise from North. North = 000°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 030°. What is the back bearing?', '330°', '210°', '120°', '030°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 30° + 180° = 210°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 060°. What is the back bearing?', '150°', '240°', '300°', '060°', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 60° + 180° = 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 135°. What is the back bearing?', '135°', 'Cannot determine', '315°', '225°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 135° + 180° = 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 300°. What is the back bearing?', '300°', '030°', '120°', '060°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 300° + 180° = 120°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 120°. What is the back bearing?', '300°', '210°', '240°', '120°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 120° + 180° = 300°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 045°. What is the back bearing?', '045°', '315°', '135°', '225°', 3,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 45° + 180° = 225°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 300°. What is the back bearing?', '120°', '030°', '060°', '300°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 300° + 180° = 120°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 330°. What is the back bearing?', '150°', '330°', '030°', '060°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 330° + 180° = 150°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 075°. What is the back bearing?', '285°', '165°', '255°', '075°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 75° + 180° = 255°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 270°. What is the back bearing?', '270°', 'Cannot determine', '000°', '090°', 3,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 270° + 180° = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 135°. What is the back bearing?', '225°', '315°', '135°', 'Cannot determine', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 135° + 180° = 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 060°. What is the back bearing?', '150°', '060°', '240°', '300°', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 60° + 180° = 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 075°. What is the back bearing?', '255°', '285°', '165°', '075°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 75° + 180° = 255°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 150°. What is the back bearing?', '330°', '240°', '150°', '210°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 150° + 180° = 330°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails on a bearing of 240°. What is the back bearing?', '060°', '120°', '240°', '330°', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'Back bearing = original ± 180°. 240° + 180° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 8 km on a bearing of 045°. How far East has it travelled?', 'Cannot determine', '8 km', '7.7 km', '5.7 km', 3,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 8 × sin 45° = 5.7 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 15 km on a bearing of 120°. How far East has it travelled?', '13.0 km', '15.0 km', '15 km', '-7.5 km', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 15 × sin 120° = 13.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 5 km on a bearing of 060°. How far East has it travelled?', '2.5 km', '4.3 km', '5 km', '6.3 km', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 5 × sin 60° = 4.3 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 15 km on a bearing of 030°. How far East has it travelled?', '9.5 km', '7.5 km', '13.0 km', '15 km', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 15 × sin 30° = 7.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 8 km on a bearing of 120°. How far East has it travelled?', '-4.0 km', '6.9 km', '8.9 km', '8 km', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 8 × sin 120° = 6.9 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 12 km on a bearing of 120°. How far East has it travelled?', '12 km', '10.4 km', '-6.0 km', '12.4 km', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 12 × sin 120° = 10.4 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 15 km on a bearing of 060°. How far East has it travelled?', '15 km', '13.0 km', '7.5 km', '15.0 km', 1,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 15 × sin 60° = 13.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 15 km on a bearing of 090°. How far East has it travelled?', '15 km', '17.0 km', '0.0 km', '15.0 km', 3,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 15 × sin 90° = 15.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 15 km on a bearing of 135°. How far East has it travelled?', '15 km', '12.6 km', '10.6 km', '-10.6 km', 2,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 15 × sin 135° = 10.6 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat travels 15 km on a bearing of 090°. How far East has it travelled?', '15.0 km', '17.0 km', '15 km', '0.0 km', 0,
'lc_ol_trigonometry', 9, 'proficient', 'lc_ol', 'East = 15 × sin 90° = 15.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 40 m away, the angle of elevation to the top of a building is 40°. Find the height.', '25.7 m', '40 m', '43.6 m', '33.6 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 40° = height/40. Height = 40 × tan 40° = 33.6 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 80 m away, the angle of elevation to the top of a building is 50°. Find the height.', '105.3 m', '61.3 m', '80 m', '95.3 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 50° = height/80. Height = 80 × tan 50° = 95.3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 100 m away, the angle of elevation to the top of a building is 50°. Find the height.', '129.2 m', '119.2 m', '100 m', '76.6 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 50° = height/100. Height = 100 × tan 50° = 119.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 50 m away, the angle of elevation to the top of a building is 35°. Find the height.', '35.0 m', '45.0 m', '28.7 m', '50 m', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 35° = height/50. Height = 50 × tan 35° = 35.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 50 m away, the angle of elevation to the top of a building is 55°. Find the height.', '71.4 m', '41.0 m', '50 m', '81.4 m', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 55° = height/50. Height = 50 × tan 55° = 71.4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 30 m away, the angle of elevation to the top of a building is 40°. Find the height.', '35.2 m', '25.2 m', '19.3 m', '30 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 40° = height/30. Height = 30 × tan 40° = 25.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 25 m away, the angle of elevation to the top of a building is 30°. Find the height.', '25 m', '14.4 m', '12.5 m', '24.4 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 30° = height/25. Height = 25 × tan 30° = 14.4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 20 m away, the angle of elevation to the top of a building is 60°. Find the height.', '17.3 m', '44.6 m', '34.6 m', '20 m', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 60° = height/20. Height = 20 × tan 60° = 34.6 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 30 m away, the angle of elevation to the top of a building is 40°. Find the height.', '35.2 m', '19.3 m', '30 m', '25.2 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 40° = height/30. Height = 30 × tan 40° = 25.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 100 m away, the angle of elevation to the top of a building is 60°. Find the height.', '100 m', '173.2 m', '183.2 m', '86.6 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 60° = height/100. Height = 100 × tan 60° = 173.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 100 m away, the angle of elevation to the top of a building is 45°. Find the height.', '110.0 m', '100 m', '70.7 m', '100.0 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 45° = height/100. Height = 100 × tan 45° = 100.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 25 m away, the angle of elevation to the top of a building is 60°. Find the height.', '25 m', '21.7 m', '53.3 m', '43.3 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 60° = height/25. Height = 25 × tan 60° = 43.3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 20 m away, the angle of elevation to the top of a building is 40°. Find the height.', '26.8 m', '12.9 m', '16.8 m', '20 m', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 40° = height/20. Height = 20 × tan 40° = 16.8 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 80 m away, the angle of elevation to the top of a building is 25°. Find the height.', '33.8 m', '37.3 m', '80 m', '47.3 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 25° = height/80. Height = 80 × tan 25° = 37.3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 60 m away, the angle of elevation to the top of a building is 60°. Find the height.', '113.9 m', '103.9 m', '60 m', '52.0 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 60° = height/60. Height = 60 × tan 60° = 103.9 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 20 m away, the angle of elevation to the top of a building is 30°. Find the height.', '21.5 m', '11.5 m', '20 m', '10.0 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 30° = height/20. Height = 20 × tan 30° = 11.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 30 m away, the angle of elevation to the top of a building is 45°. Find the height.', '21.2 m', '30 m', '30.0 m', '40.0 m', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 45° = height/30. Height = 30 × tan 45° = 30.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 100 m away, the angle of elevation to the top of a building is 40°. Find the height.', '83.9 m', '100 m', '64.3 m', '93.9 m', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 40° = height/100. Height = 100 × tan 40° = 83.9 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 40 m away, the angle of elevation to the top of a building is 50°. Find the height.', '30.6 m', '40 m', '47.7 m', '57.7 m', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 50° = height/40. Height = 40 × tan 50° = 47.7 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 25 m away, the angle of elevation to the top of a building is 60°. Find the height.', '21.7 m', '53.3 m', '25 m', '43.3 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 60° = height/25. Height = 25 × tan 60° = 43.3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 40 m high, the angle of depression to a boat is 45°. How far is the boat from the base?', '40.0 m', 'Cannot determine', '40 m', '55.0 m', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 45° = 40/distance. Distance = 40/tan 45° = 40.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 50 m high, the angle of depression to a boat is 20°. How far is the boat from the base?', '152.4 m', '50 m', '18.2 m', '137.4 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 20° = 50/distance. Distance = 50/tan 20° = 137.4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 50 m high, the angle of depression to a boat is 20°. How far is the boat from the base?', '18.2 m', '137.4 m', '152.4 m', '50 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 20° = 50/distance. Distance = 50/tan 20° = 137.4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 25 m high, the angle of depression to a boat is 35°. How far is the boat from the base?', '50.7 m', '35.7 m', '25 m', '17.5 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 35° = 25/distance. Distance = 25/tan 35° = 35.7 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 40 m high, the angle of depression to a boat is 45°. How far is the boat from the base?', '55.0 m', 'Cannot determine', '40 m', '40.0 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 45° = 40/distance. Distance = 40/tan 45° = 40.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 20 m high, the angle of depression to a boat is 20°. How far is the boat from the base?', '7.3 m', '54.9 m', '69.9 m', '20 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 20° = 20/distance. Distance = 20/tan 20° = 54.9 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 20 m high, the angle of depression to a boat is 45°. How far is the boat from the base?', 'Cannot determine', '20 m', '35.0 m', '20.0 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 45° = 20/distance. Distance = 20/tan 45° = 20.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 20 m high, the angle of depression to a boat is 40°. How far is the boat from the base?', '16.8 m', '20 m', '23.8 m', '38.8 m', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 40° = 20/distance. Distance = 20/tan 40° = 23.8 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 15 m high, the angle of depression to a boat is 25°. How far is the boat from the base?', '7.0 m', '47.2 m', '15 m', '32.2 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 25° = 15/distance. Distance = 15/tan 25° = 32.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 25 m high, the angle of depression to a boat is 20°. How far is the boat from the base?', '68.7 m', '9.1 m', '83.7 m', '25 m', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 20° = 25/distance. Distance = 25/tan 20° = 68.7 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 40 m high, the angle of depression to a boat is 20°. How far is the boat from the base?', '40 m', '109.9 m', '124.9 m', '14.6 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 20° = 40/distance. Distance = 40/tan 20° = 109.9 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 30 m high, the angle of depression to a boat is 45°. How far is the boat from the base?', 'Cannot determine', '45.0 m', '30 m', '30.0 m', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 45° = 30/distance. Distance = 30/tan 45° = 30.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 50 m high, the angle of depression to a boat is 40°. How far is the boat from the base?', '59.6 m', '50 m', '74.6 m', '42.0 m', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 40° = 50/distance. Distance = 50/tan 40° = 59.6 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 40 m high, the angle of depression to a boat is 25°. How far is the boat from the base?', '100.8 m', '85.8 m', '40 m', '18.7 m', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 25° = 40/distance. Distance = 40/tan 25° = 85.8 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a cliff 15 m high, the angle of depression to a boat is 45°. How far is the boat from the base?', '15 m', '15.0 m', '30.0 m', 'Cannot determine', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan 45° = 15/distance. Distance = 15/tan 45° = 15.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 20 m tall. From 50 m away, what is the angle of elevation to the top?', '21.8°', '31.8°', '4.0°', '68.2°', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 20/50 = 0.400. θ = tan⁻¹(0.400) = 21.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 25 m tall. From 50 m away, what is the angle of elevation to the top?', '63.4°', '5.0°', '26.6°', '36.6°', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 25/50 = 0.500. θ = tan⁻¹(0.500) = 26.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 15 m tall. From 30 m away, what is the angle of elevation to the top?', '63.4°', '36.6°', '5.0°', '26.6°', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 15/30 = 0.500. θ = tan⁻¹(0.500) = 26.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 15 m tall. From 15 m away, what is the angle of elevation to the top?', '10.0°', '45.0°', '55.0°', 'Cannot determine', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 15/15 = 1.000. θ = tan⁻¹(1.000) = 45.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 10 m tall. From 40 m away, what is the angle of elevation to the top?', '24.0°', '76.0°', '2.5°', '14.0°', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 10/40 = 0.250. θ = tan⁻¹(0.250) = 14.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 30 m tall. From 15 m away, what is the angle of elevation to the top?', '26.6°', '63.4°', '73.4°', '20.0°', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 30/15 = 2.000. θ = tan⁻¹(2.000) = 63.4°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 15 m tall. From 30 m away, what is the angle of elevation to the top?', '36.6°', '5.0°', '26.6°', '63.4°', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 15/30 = 0.500. θ = tan⁻¹(0.500) = 26.6°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 20 m tall. From 15 m away, what is the angle of elevation to the top?', '13.3°', '36.9°', '53.1°', '63.1°', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 20/15 = 1.333. θ = tan⁻¹(1.333) = 53.1°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 20 m tall. From 50 m away, what is the angle of elevation to the top?', '31.8°', '21.8°', '68.2°', '4.0°', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 20/50 = 0.400. θ = tan⁻¹(0.400) = 21.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 20 m tall. From 50 m away, what is the angle of elevation to the top?', '31.8°', '68.2°', '21.8°', '4.0°', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 20/50 = 0.400. θ = tan⁻¹(0.400) = 21.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 30 m tall. From 25 m away, what is the angle of elevation to the top?', '39.8°', '60.2°', '50.2°', '12.0°', 2,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 30/25 = 1.200. θ = tan⁻¹(1.200) = 50.2°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 25 m tall. From 30 m away, what is the angle of elevation to the top?', '49.8°', '8.3°', '50.2°', '39.8°', 3,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 25/30 = 0.833. θ = tan⁻¹(0.833) = 39.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 10 m tall. From 25 m away, what is the angle of elevation to the top?', '21.8°', '68.2°', '31.8°', '4.0°', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 10/25 = 0.400. θ = tan⁻¹(0.400) = 21.8°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 20 m tall. From 25 m away, what is the angle of elevation to the top?', '8.0°', '38.7°', '51.3°', '48.7°', 1,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 20/25 = 0.800. θ = tan⁻¹(0.800) = 38.7°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A tree is 20 m tall. From 20 m away, what is the angle of elevation to the top?', '45.0°', '55.0°', 'Cannot determine', '10.0°', 0,
'lc_ol_trigonometry', 10, 'advanced', 'lc_ol', 'tan θ = 20/20 = 1.000. θ = tan⁻¹(1.000) = 45.0°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 15 m over a horizontal distance of 100 m. What is the gradient as a percentage?', '6.7%', '17.0%', '15%', '15.0%', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (15/100) × 100 = 15.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 15 m over a horizontal distance of 50 m. What is the gradient as a percentage?', '3.3%', '30.0%', '15%', '32.0%', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (15/50) × 100 = 30.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 15 m over a horizontal distance of 50 m. What is the gradient as a percentage?', '3.3%', '30.0%', '15%', '32.0%', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (15/50) × 100 = 30.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 8 m over a horizontal distance of 100 m. What is the gradient as a percentage?', '8%', '8.0%', '12.5%', '10.0%', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (8/100) × 100 = 8.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 8 m over a horizontal distance of 150 m. What is the gradient as a percentage?', '5.3%', '18.8%', '7.3%', '8%', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (8/150) × 100 = 5.3%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 8 m over a horizontal distance of 150 m. What is the gradient as a percentage?', '7.3%', '18.8%', '8%', '5.3%', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (8/150) × 100 = 5.3%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 8 m over a horizontal distance of 150 m. What is the gradient as a percentage?', '18.8%', '5.3%', '7.3%', '8%', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (8/150) × 100 = 5.3%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 15 m over a horizontal distance of 80 m. What is the gradient as a percentage?', '5.3%', '18.8%', '20.8%', '15%', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (15/80) × 100 = 18.8%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 15 m over a horizontal distance of 120 m. What is the gradient as a percentage?', '12.5%', '8.0%', '15%', '14.5%', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (15/120) × 100 = 12.5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 15 m over a horizontal distance of 150 m. What is the gradient as a percentage?', '12.0%', 'Cannot determine', '10.0%', '15%', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (15/150) × 100 = 10.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 8 m over a horizontal distance of 120 m. What is the gradient as a percentage?', '8%', '15.0%', '6.7%', '8.7%', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (8/120) × 100 = 6.7%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 10 m over a horizontal distance of 100 m. What is the gradient as a percentage?', '10.0%', 'Cannot determine', '10%', '12.0%', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (10/100) × 100 = 10.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 8 m over a horizontal distance of 100 m. What is the gradient as a percentage?', '10.0%', '12.5%', '8%', '8.0%', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (8/100) × 100 = 8.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 5 m over a horizontal distance of 80 m. What is the gradient as a percentage?', '16.0%', '5%', '8.2%', '6.2%', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (5/80) × 100 = 6.2%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A road rises 15 m over a horizontal distance of 100 m. What is the gradient as a percentage?', '15%', '15.0%', '6.7%', '17.0%', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Gradient = (rise/run) × 100 = (15/100) × 100 = 15.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 80 m, CB = 100 m, angle ACB = 60°. Find AB.', '91.7 m', '180 m', '128.1 m', '111.7 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 80² + 100² - 2(80)(100)cos 60°. AB = 91.7 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 80 m, CB = 100 m, angle ACB = 50°. Find AB.', '78.2 m', '128.1 m', '180 m', '98.2 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 80² + 100² - 2(80)(100)cos 50°. AB = 78.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 100 m, CB = 120 m, angle ACB = 40°. Find AB.', '156.2 m', '97.6 m', '220 m', '77.6 m', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 100² + 120² - 2(100)(120)cos 40°. AB = 77.6 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 80 m, CB = 120 m, angle ACB = 40°. Find AB.', '78.1 m', '98.1 m', '144.2 m', '200 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 80² + 120² - 2(80)(120)cos 40°. AB = 78.1 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 150 m, CB = 120 m, angle ACB = 80°. Find AB.', '175.1 m', '192.1 m', '195.1 m', '270 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 150² + 120² - 2(150)(120)cos 80°. AB = 175.1 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 100 m, CB = 60 m, angle ACB = 50°. Find AB.', '76.7 m', '160 m', '96.7 m', '116.6 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 100² + 60² - 2(100)(60)cos 50°. AB = 76.7 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 150 m, CB = 100 m, angle ACB = 70°. Find AB.', '250 m', '169.1 m', '180.3 m', '149.1 m', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 150² + 100² - 2(150)(100)cos 70°. AB = 149.1 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 80 m, CB = 120 m, angle ACB = 60°. Find AB.', '200 m', '144.2 m', '105.8 m', '125.8 m', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 80² + 120² - 2(80)(120)cos 60°. AB = 105.8 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 120 m, CB = 100 m, angle ACB = 50°. Find AB.', '94.7 m', '114.7 m', '220 m', '156.2 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 120² + 100² - 2(120)(100)cos 50°. AB = 94.7 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 100 m, CB = 120 m, angle ACB = 70°. Find AB.', '147.2 m', '127.2 m', '156.2 m', '220 m', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 100² + 120² - 2(100)(120)cos 70°. AB = 127.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 100 m, CB = 80 m, angle ACB = 70°. Find AB.', '180 m', '128.1 m', '104.5 m', '124.5 m', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 100² + 80² - 2(100)(80)cos 70°. AB = 104.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 150 m, CB = 100 m, angle ACB = 50°. Find AB.', '135.0 m', '250 m', '115.0 m', '180.3 m', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 150² + 100² - 2(150)(100)cos 50°. AB = 115.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 120 m, CB = 80 m, angle ACB = 80°. Find AB.', '144.2 m', '200 m', '132.2 m', '152.2 m', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 120² + 80² - 2(120)(80)cos 80°. AB = 132.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 120 m, CB = 100 m, angle ACB = 40°. Find AB.', '77.6 m', '220 m', '97.6 m', '156.2 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 120² + 100² - 2(120)(100)cos 40°. AB = 77.6 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Points A and B are on opposite sides of a lake. From C, CA = 80 m, CB = 80 m, angle ACB = 80°. Find AB.', '102.8 m', '122.8 m', '113.1 m', '160 m', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'Cosine Rule: AB² = 80² + 80² - 2(80)(80)cos 80°. AB = 102.8 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 10 km on bearing 060°. How far North has it travelled?', '8.7 km', '5.0 km', '7.0 km', '10 km', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 10 × cos 60° = 5.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 030°. How far North has it travelled?', '4.3 km', '2.5 km', '6.3 km', '5 km', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 30° = 4.3 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 10 km on bearing 030°. How far North has it travelled?', '5.0 km', '10 km', '10.7 km', '8.7 km', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 10 × cos 30° = 8.7 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 045°. How far North has it travelled?', '3.5 km', '5 km', 'Cannot determine', '5.5 km', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 45° = 3.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 8 km on bearing 060°. How far North has it travelled?', '6.9 km', '4.0 km', '8 km', '6.0 km', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 8 × cos 60° = 4.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 12 km on bearing 030°. How far North has it travelled?', '10.4 km', '6.0 km', '12.4 km', '12 km', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 12 × cos 30° = 10.4 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 8 km on bearing 045°. How far North has it travelled?', '7.7 km', '5.7 km', 'Cannot determine', '8 km', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 8 × cos 45° = 5.7 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 060°. How far North has it travelled?', '5 km', '4.5 km', '2.5 km', '4.3 km', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 60° = 2.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 060°. How far North has it travelled?', '2.5 km', '4.3 km', '5 km', '4.5 km', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 60° = 2.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 030°. How far North has it travelled?', '2.5 km', '4.3 km', '5 km', '6.3 km', 1,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 30° = 4.3 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 12 km on bearing 030°. How far North has it travelled?', '10.4 km', '12 km', '12.4 km', '6.0 km', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 12 × cos 30° = 10.4 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 12 km on bearing 030°. How far North has it travelled?', '10.4 km', '6.0 km', '12 km', '12.4 km', 0,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 12 × cos 30° = 10.4 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 10 km on bearing 045°. How far North has it travelled?', 'Cannot determine', '9.1 km', '7.1 km', '10 km', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 10 × cos 45° = 7.1 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 030°. How far North has it travelled?', '5 km', '6.3 km', '2.5 km', '4.3 km', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 30° = 4.3 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 12 km on bearing 045°. How far North has it travelled?', 'Cannot determine', '12 km', '10.5 km', '8.5 km', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 12 × cos 45° = 8.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 12 km on bearing 060°. How far North has it travelled?', '12 km', '8.0 km', '6.0 km', '10.4 km', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 12 × cos 60° = 6.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 12 km on bearing 030°. How far North has it travelled?', '6.0 km', '12 km', '10.4 km', '12.4 km', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 12 × cos 30° = 10.4 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 12 km on bearing 045°. How far North has it travelled?', '10.5 km', 'Cannot determine', '12 km', '8.5 km', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 12 × cos 45° = 8.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 030°. How far North has it travelled?', '6.3 km', '5 km', '2.5 km', '4.3 km', 3,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 30° = 4.3 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A boat sails 5 km on bearing 030°. How far North has it travelled?', '5 km', '2.5 km', '4.3 km', '6.3 km', 2,
'lc_ol_trigonometry', 11, 'advanced', 'lc_ol', 'North = 5 × cos 30° = 4.3 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 70°, B = 55°, c = 10 cm. Find side a.', '13.5 cm', '11.5 cm', '12.7 cm', '10 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 70° - 55° = 55°. Sine rule: a = 10 × sin 70°/sin 55° = 11.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 70°, B = 55°, c = 10 cm. Find side a.', '11.5 cm', '10 cm', '13.5 cm', '12.7 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 70° - 55° = 55°. Sine rule: a = 10 × sin 70°/sin 55° = 11.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 55°, B = 50°, c = 14 cm. Find side a.', '10.3 cm', '11.9 cm', '14 cm', '13.9 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 55° - 50° = 75°. Sine rule: a = 14 × sin 55°/sin 75° = 11.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 60°, B = 50°, c = 10 cm. Find side a.', '11.2 cm', '8.6 cm', '9.2 cm', '10 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 60° - 50° = 70°. Sine rule: a = 10 × sin 60°/sin 70° = 9.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 60°, B = 55°, c = 15 cm. Find side a.', '16.3 cm', '14.3 cm', '13.8 cm', '15 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 60° - 55° = 65°. Sine rule: a = 15 × sin 60°/sin 65° = 14.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 70°, B = 45°, c = 15 cm. Find side a.', '15.6 cm', '16.2 cm', '15 cm', '17.6 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 70° - 45° = 65°. Sine rule: a = 15 × sin 70°/sin 65° = 15.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 60°, B = 45°, c = 12 cm. Find side a.', '12.8 cm', '12 cm', '10.8 cm', '9.6 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 60° - 45° = 75°. Sine rule: a = 12 × sin 60°/sin 75° = 10.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 65°, B = 40°, c = 10 cm. Find side a.', '9.4 cm', '11.4 cm', '8.7 cm', '10 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 65° - 40° = 75°. Sine rule: a = 10 × sin 65°/sin 75° = 9.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 65°, B = 50°, c = 10 cm. Find side a.', 'Cannot determine', '10.0 cm', '12.0 cm', '10 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 65° - 50° = 65°. Sine rule: a = 10 × sin 65°/sin 65° = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 65°, B = 40°, c = 12 cm. Find side a.', '12 cm', '11.3 cm', '10.4 cm', '13.3 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 65° - 40° = 75°. Sine rule: a = 12 × sin 65°/sin 75° = 11.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 55°, B = 45°, c = 12 cm. Find side a.', '10.0 cm', '12 cm', '8.2 cm', '12.0 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 55° - 45° = 80°. Sine rule: a = 12 × sin 55°/sin 80° = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 50°, B = 40°, c = 10 cm. Find side a.', '7.7 cm', '5.6 cm', '10 cm', '9.7 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 50° - 40° = 90°. Sine rule: a = 10 × sin 50°/sin 90° = 7.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 70°, B = 50°, c = 15 cm. Find side a.', '16.3 cm', '17.5 cm', '15 cm', '18.3 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 70° - 50° = 60°. Sine rule: a = 15 × sin 70°/sin 60° = 16.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 50°, B = 45°, c = 12 cm. Find side a.', '11.2 cm', '12 cm', '7.1 cm', '9.2 cm', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 50° - 45° = 85°. Sine rule: a = 12 × sin 50°/sin 85° = 9.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC: A = 50°, B = 45°, c = 14 cm. Find side a.', '10.8 cm', '8.2 cm', '14 cm', '12.8 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'C = 180° - 50° - 45° = 85°. Sine rule: a = 14 × sin 50°/sin 85° = 10.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 10 cm, b = 14 cm, C = 90°. Find the perimeter.', '44.2 cm', '24 cm', '41.2 cm', '94.0 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(10² + 14² - 2(10)(14)cos 90°) = 17.2 cm. Perimeter = 41.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 12 cm, b = 10 cm, C = 120°. Find the perimeter.', '41.1 cm', '44.1 cm', '74.0 cm', '22 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(12² + 10² - 2(12)(10)cos 120°) = 19.1 cm. Perimeter = 41.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 10 cm, b = 10 cm, C = 120°. Find the perimeter.', '37.3 cm', '20 cm', '40.3 cm', '63.3 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(10² + 10² - 2(10)(10)cos 120°) = 17.3 cm. Perimeter = 37.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 12 cm, b = 10 cm, C = 120°. Find the perimeter.', '22 cm', '44.1 cm', '74.0 cm', '41.1 cm', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(12² + 10² - 2(12)(10)cos 120°) = 19.1 cm. Perimeter = 41.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 8 cm, b = 14 cm, C = 45°. Find the perimeter.', '22 cm', '35.1 cm', '32.1 cm', '61.6 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(8² + 14² - 2(8)(14)cos 45°) = 10.1 cm. Perimeter = 32.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 8 cm, b = 14 cm, C = 120°. Find the perimeter.', '70.5 cm', '44.3 cm', '41.3 cm', '22 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(8² + 14² - 2(8)(14)cos 120°) = 19.3 cm. Perimeter = 41.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 10 cm, b = 14 cm, C = 45°. Find the perimeter.', '36.9 cm', '33.9 cm', '73.5 cm', '24 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(10² + 14² - 2(10)(14)cos 45°) = 9.9 cm. Perimeter = 33.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 12 cm, b = 12 cm, C = 90°. Find the perimeter.', '24 cm', '44.0 cm', '96.0 cm', '41.0 cm', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(12² + 12² - 2(12)(12)cos 90°) = 17.0 cm. Perimeter = 41.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 10 cm, b = 10 cm, C = 60°. Find the perimeter.', '63.3 cm', '20 cm', '33.0 cm', '30.0 cm', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(10² + 10² - 2(10)(10)cos 60°) = 10.0 cm. Perimeter = 30.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 10 cm, b = 12 cm, C = 90°. Find the perimeter.', '82.0 cm', '37.6 cm', '22 cm', '40.6 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(10² + 12² - 2(10)(12)cos 90°) = 15.6 cm. Perimeter = 37.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 12 cm, b = 12 cm, C = 60°. Find the perimeter.', '86.4 cm', '39.0 cm', '36.0 cm', '24 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(12² + 12² - 2(12)(12)cos 60°) = 12.0 cm. Perimeter = 36.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 8 cm, b = 10 cm, C = 120°. Find the perimeter.', '33.6 cm', '18 cm', '52.6 cm', '36.6 cm', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(8² + 10² - 2(8)(10)cos 120°) = 15.6 cm. Perimeter = 33.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 12 cm, b = 14 cm, C = 120°. Find the perimeter.', '51.5 cm', '26 cm', '48.5 cm', '98.7 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(12² + 14² - 2(12)(14)cos 120°) = 22.5 cm. Perimeter = 48.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 12 cm, b = 10 cm, C = 120°. Find the perimeter.', '22 cm', '74.0 cm', '41.1 cm', '44.1 cm', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(12² + 10² - 2(12)(10)cos 120°) = 19.1 cm. Perimeter = 41.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle ABC: a = 12 cm, b = 12 cm, C = 60°. Find the perimeter.', '86.4 cm', '36.0 cm', '39.0 cm', '24 cm', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'c = √(12² + 12² - 2(12)(12)cos 60°) = 12.0 cm. Perimeter = 36.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 60 m tower is 40°. Walking towards, it becomes 50°. How far walked?', '31.2 m', '50.3 m', '71.5 m', '21.2 m', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 60/tan 40° = 71.5 m. Dist 2 = 60/tan 50° = 50.3 m. Walked = 21.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 60 m tower is 30°. Walking towards, it becomes 50°. How far walked?', '63.6 m', '53.6 m', '103.9 m', '50.3 m', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 60/tan 30° = 103.9 m. Dist 2 = 60/tan 50° = 50.3 m. Walked = 53.6 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 100 m tower is 35°. Walking towards, it becomes 55°. How far walked?', '142.8 m', '72.8 m', '70.0 m', '82.8 m', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 100/tan 35° = 142.8 m. Dist 2 = 100/tan 55° = 70.0 m. Walked = 72.8 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 60 m tower is 30°. Walking towards, it becomes 55°. How far walked?', '42.0 m', '103.9 m', '61.9 m', '71.9 m', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 60/tan 30° = 103.9 m. Dist 2 = 60/tan 55° = 42.0 m. Walked = 61.9 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 50 m tower is 30°. Walking towards, it becomes 60°. How far walked?', '67.7 m', '28.9 m', '86.6 m', '57.7 m', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 50/tan 30° = 86.6 m. Dist 2 = 50/tan 60° = 28.9 m. Walked = 57.7 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 60 m tower is 35°. Walking towards, it becomes 50°. How far walked?', '45.3 m', '35.3 m', '85.7 m', '50.3 m', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 60/tan 35° = 85.7 m. Dist 2 = 60/tan 50° = 50.3 m. Walked = 35.3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 50 m tower is 35°. Walking towards, it becomes 50°. How far walked?', '29.5 m', '71.4 m', '42.0 m', '39.5 m', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 50/tan 35° = 71.4 m. Dist 2 = 50/tan 50° = 42.0 m. Walked = 29.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 100 m tower is 35°. Walking towards, it becomes 55°. How far walked?', '72.8 m', '70.0 m', '82.8 m', '142.8 m', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 100/tan 35° = 142.8 m. Dist 2 = 100/tan 55° = 70.0 m. Walked = 72.8 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 100 m tower is 30°. Walking towards, it becomes 60°. How far walked?', '57.7 m', '173.2 m', '125.5 m', '115.5 m', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 100/tan 30° = 173.2 m. Dist 2 = 100/tan 60° = 57.7 m. Walked = 115.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 80 m tower is 35°. Walking towards, it becomes 55°. How far walked?', '68.2 m', '58.2 m', '56.0 m', '114.3 m', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 80/tan 35° = 114.3 m. Dist 2 = 80/tan 55° = 56.0 m. Walked = 58.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 80 m tower is 40°. Walking towards, it becomes 55°. How far walked?', '95.3 m', '49.3 m', '56.0 m', '39.3 m', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 80/tan 40° = 95.3 m. Dist 2 = 80/tan 55° = 56.0 m. Walked = 39.3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 100 m tower is 40°. Walking towards, it becomes 60°. How far walked?', '61.4 m', '71.4 m', '119.2 m', '57.7 m', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 100/tan 40° = 119.2 m. Dist 2 = 100/tan 60° = 57.7 m. Walked = 61.4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 100 m tower is 30°. Walking towards, it becomes 60°. How far walked?', '115.5 m', '57.7 m', '173.2 m', '125.5 m', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 100/tan 30° = 173.2 m. Dist 2 = 100/tan 60° = 57.7 m. Walked = 115.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 50 m tower is 35°. Walking towards, it becomes 60°. How far walked?', '42.5 m', '71.4 m', '28.9 m', '52.5 m', 0,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 50/tan 35° = 71.4 m. Dist 2 = 50/tan 60° = 28.9 m. Walked = 42.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 80 m tower is 30°. Walking towards, it becomes 60°. How far walked?', '138.6 m', '46.2 m', '92.4 m', '102.4 m', 2,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 80/tan 30° = 138.6 m. Dist 2 = 80/tan 60° = 46.2 m. Walked = 92.4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 50 m tower is 35°. Walking towards, it becomes 55°. How far walked?', '71.4 m', '46.4 m', '35.0 m', '36.4 m', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 50/tan 35° = 71.4 m. Dist 2 = 50/tan 55° = 35.0 m. Walked = 36.4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 100 m tower is 40°. Walking towards, it becomes 50°. How far walked?', '83.9 m', '35.3 m', '45.3 m', '119.2 m', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 100/tan 40° = 119.2 m. Dist 2 = 100/tan 50° = 83.9 m. Walked = 35.3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 50 m tower is 35°. Walking towards, it becomes 60°. How far walked?', '71.4 m', '42.5 m', '28.9 m', '52.5 m', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 50/tan 35° = 71.4 m. Dist 2 = 50/tan 60° = 28.9 m. Walked = 42.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 80 m tower is 40°. Walking towards, it becomes 50°. How far walked?', '38.2 m', '28.2 m', '95.3 m', '67.1 m', 1,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 80/tan 40° = 95.3 m. Dist 2 = 80/tan 50° = 67.1 m. Walked = 28.2 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, angle of elevation to a 80 m tower is 30°. Walking towards, it becomes 55°. How far walked?', '92.5 m', '56.0 m', '138.6 m', '82.5 m', 3,
'lc_ol_trigonometry', 12, 'advanced', 'lc_ol', 'Dist 1 = 80/tan 30° = 138.6 m. Dist 2 = 80/tan 55° = 56.0 m. Walked = 82.5 m', 1);

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_trigonometry';
