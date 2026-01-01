-- LC Higher Level - Measurement - Complete SQL
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_measurement_complete.sql
-- Generated: 2025-12-15

-- Add Measurement topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_measurement', 'Measurement', id, '📏', 14, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_measurement';

-- Questions (600 total, 50 per level x 12 levels)


INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 4 cm.', '12', 'None of these', '16', '8', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 4 = 12 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 12 cm.', '144', '24', '36', '48', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 12 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 16 cm and width 7 cm.', '112', '48', '23', '46', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(16 + 7) = 46 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 6 cm.', '36', 'None of these', '24', '30', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 6 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 4 cm.', '16', '24', 'None of these', '20', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 4 = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 12 cm.', '48', '144', '52', '24', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 12 = 48 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 12 cm.', '144', '48', '24', '52', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 12 = 48 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 10 cm.', '40', '100', '20', '44', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 10 = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 6 cm.', '24', '36', '12', '28', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 6 = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 8 cm.', '40', '48', '64', '32', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 8 = 48 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 10, 6, 6 cm.', '60', '23', '16', '22', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 10 + 6 + 6 = 22 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 7, 7, 11 cm.', '25', '26', '49', '14', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 7 + 7 + 11 = 25 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 12 cm.', '52', '24', '144', '48', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 12 = 48 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 4 cm.', '12', 'None of these', '16', '8', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 4 = 12 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 9 cm.', '18', '81', '36', '40', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 9 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 9 cm.', '18', '36', '81', '40', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 9 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 3 cm.', '18', '12', '9', '15', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 3 = 18 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 10 cm.', '44', '100', '20', '40', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 10 = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 10 cm.', '40', '50', '100', '60', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 10 = 60 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 6, 7, 7 cm.', '13', '20', '21', '42', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6 + 7 + 7 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 4 cm.', '24', 'None of these', '16', '20', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 4 = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 6, 6, 11 cm.', '24', '12', '36', '23', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6 + 6 + 11 = 23 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 3 cm.', '9', '18', '12', '15', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 3 = 18 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 7 cm and width 3 cm.', '20', '22', '21', '10', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(7 + 3) = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 8 cm.', '32', '24', '16', '64', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 8 = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 5, 11, 9 cm.', '55', '25', '26', '16', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 5 + 11 + 9 = 25 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 5, 6, 9 cm.', '30', '20', '11', '21', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 5 + 6 + 9 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 10 cm.', '100', '60', '50', '40', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 10 = 60 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 14 cm and width 14 cm.', '56', '28', '196', '58', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(14 + 14) = 56 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 9 cm.', '40', '18', '36', '81', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 9 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 10 cm.', '100', '40', '20', '44', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 10 = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 13 cm and width 13 cm.', '54', '169', '52', '26', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(13 + 13) = 52 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 9 cm.', '36', '18', '27', '81', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 9 = 27 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 6 cm and width 10 cm.', '32', '16', '34', '60', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(6 + 10) = 32 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 8 cm and width 9 cm.', '36', '72', '17', '34', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(8 + 9) = 34 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 9, 10, 10 cm.', '29', '19', '30', '90', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 9 + 10 + 10 = 29 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 6 cm.', '30', '36', 'None of these', '24', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 6 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 5 cm.', '25', '10', '24', '20', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 5 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 11, 10, 6 cm.', '28', '27', '21', '110', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 11 + 10 + 6 = 27 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 5, 12, 8 cm.', '17', '60', '25', '26', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 5 + 12 + 8 = 25 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 6, 12, 10 cm.', '18', '29', '28', '72', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6 + 12 + 10 = 28 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 6 cm.', '36', '18', '24', '12', 1,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 6 = 18 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 5 cm.', '20', '10', '15', '25', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 5 = 15 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 15 cm and width 11 cm.', '54', '165', '26', '52', 3,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(15 + 11) = 52 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 7 cm.', '28', '49', '32', '14', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 4s = 4 × 7 = 28 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 6, 9, 11 cm.', '26', '27', '15', '54', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6 + 9 + 11 = 26 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of an equilateral triangle with side 6 cm.', '18', '36', '24', '12', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 3s = 3 × 6 = 18 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a regular hexagon with side 7 cm.', '35', '49', '42', '28', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 6s = 6 × 7 = 42 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 10 cm and width 5 cm.', '30', '50', '15', '32', 0,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(10 + 5) = 30 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 16 cm and width 4 cm.', '20', '42', '40', '64', 2,
'lc_hl_measurement', 1, 'foundation', 'lc_hl', 'Perimeter = 2(l + w) = 2(16 + 4) = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 5 cm and height 9 cm.', '27', '14', '45', '22', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½bh = ½ × 5 × 9 = 22 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 11 cm and width 9 cm.', '99', '40', '110', '20', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = l × w = 11 × 9 = 99 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a parallelogram with base 6 cm and height 8 cm.', '14', '24', '48', '28', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = bh = 6 × 8 = 48 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 6 cm and 8 cm.', '48', '24', '14', '30', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 6 × 8 = 24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 6 cm.', '24', '36', '42', '12', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = s² = 6² = 36 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 14 cm and 8 cm.', '56', '112', '22', '70', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 14 × 8 = 56 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 12 cm and height 4 cm.', '48', '16', '36', '24', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½bh = ½ × 12 × 4 = 24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 6 cm and height 12 cm.', '72', '36', '18', '42', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½bh = ½ × 6 × 12 = 36 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 13 cm and height 4 cm.', '52', '39', '26', '17', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½bh = ½ × 13 × 4 = 26 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 10 cm and 9 cm, height 6 cm.', '63', '57', '114', '90', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(10 + 9) × 6 = 57 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 14 cm and width 6 cm.', '20', '98', '84', '40', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = l × w = 14 × 6 = 84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 12 cm.', '144', '24', '156', '48', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = s² = 12² = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 11 cm and height 13 cm.', '82', '24', '143', '71', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½bh = ½ × 11 × 13 = 71 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a parallelogram with base 8 cm and height 6 cm.', '48', '24', '28', '14', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = bh = 8 × 6 = 48 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 4 cm and 15 cm, height 6 cm.', '57', '63', '114', '60', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(4 + 15) × 6 = 57 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 11 cm and 11 cm.', '22', '121', '60', '71', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 11 × 11 = 60 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 6 cm and 15 cm, height 6 cm.', '69', '63', '90', '126', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(6 + 15) × 6 = 63 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 6 cm and 16 cm, height 9 cm.', '99', '96', '198', '108', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(6 + 16) × 9 = 99 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 8 cm and 14 cm, height 10 cm.', '110', '220', '120', '112', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(8 + 14) × 10 = 110 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 12 cm and width 12 cm.', '144', '48', '24', '156', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = l × w = 12 × 12 = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 8 cm and 16 cm, height 9 cm.', '117', '128', '216', '108', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(8 + 16) × 9 = 108 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 5 cm.', '10', '25', '30', '20', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = s² = 5² = 25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 5 cm and width 5 cm.', '30', '10', '25', '20', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = l × w = 5 × 5 = 25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 4 cm.', '8', '20', '16', 'None of these', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = s² = 4² = 16 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 7 cm and 12 cm.', '42', '84', '49', '19', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 7 × 12 = 42 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 10 cm and 13 cm, height 10 cm.', '130', '115', '230', '125', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(10 + 13) × 10 = 115 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 6 cm and 11 cm, height 9 cm.', '85', '76', '153', '66', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(6 + 11) × 9 = 76 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 4 cm and 8 cm, height 6 cm.', '72', '42', '32', '36', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(4 + 8) × 6 = 36 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 13 cm and 14 cm.', '27', '91', '104', '182', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 13 × 14 = 91 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 6 cm and 7 cm.', '42', '21', '13', '27', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 6 × 7 = 21 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 5 cm and width 12 cm.', '17', '65', '60', '34', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = l × w = 5 × 12 = 60 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 5 cm.', '20', '30', '10', '25', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = s² = 5² = 25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a parallelogram with base 9 cm and height 6 cm.', '27', '30', '15', '54', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = bh = 9 × 6 = 54 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 5 cm and 11 cm, height 10 cm.', '160', '90', '55', '80', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(5 + 11) × 10 = 80 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 7 cm and height 5 cm.', '12', '24', '35', '17', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½bh = ½ × 7 × 5 = 17 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 9 cm and 10 cm.', '45', '90', '54', '19', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 9 × 10 = 45 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a parallelogram with base 9 cm and height 6 cm.', '15', '54', '27', '30', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = bh = 9 × 6 = 54 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 8 cm.', '16', '32', '72', '64', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = s² = 8² = 64 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 5 cm.', '20', '10', '30', '25', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = s² = 5² = 25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 7 cm and 11 cm, height 6 cm.', '54', '77', '108', '60', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(7 + 11) × 6 = 54 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 8 cm and 9 cm, height 4 cm.', '34', '38', '68', '72', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(8 + 9) × 4 = 34 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 6 cm and height 11 cm.', '17', '66', '39', '33', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½bh = ½ × 6 × 11 = 33 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 6 cm and 13 cm, height 5 cm.', '47', '78', '95', '52', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(6 + 13) × 5 = 47 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 6 cm and 10 cm, height 6 cm.', '54', '48', '96', '60', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(6 + 10) × 6 = 48 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 9 cm and 14 cm.', '72', '126', '23', '63', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 9 × 14 = 63 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 14 cm and width 10 cm.', '140', '24', '48', '154', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = l × w = 14 × 10 = 140 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a parallelogram with base 5 cm and height 5 cm.', '10', '25', '12', '20', 1,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = bh = 5 × 5 = 25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a trapezium with parallel sides 9 cm and 10 cm, height 8 cm.', '90', '84', '152', '76', 3,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½(a + b)h = ½(9 + 10) × 8 = 76 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rhombus with diagonals 7 cm and 14 cm.', '49', '56', '98', '21', 0,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = ½d₁d₂ = ½ × 7 × 14 = 49 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 13 cm and width 8 cm.', '117', '42', '104', '21', 2,
'lc_hl_measurement', 2, 'foundation', 'lc_hl', 'Area = l × w = 13 × 8 = 104 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 16×11 cm has a 4×5 hole. Find the shaded area.', '196', '176', '156', '20', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 16×11 - 4×5 = 176 - 20 = 156 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 30 and 34 cm² with overlap 8 cm². Find total area.', '56', '64', '30', 'None of these', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 30 + 34 - 8 = 56 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square has side 9 cm. Find its area.', '81', '71', '91', '162', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 9² = 81 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 18×13 cm has a 5×3 hole. Find the shaded area.', '15', '234', '219', '249', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 18×13 - 5×3 = 234 - 15 = 219 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square has side 10 cm. Find its area.', '100', '90', '110', '200', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 10² = 100 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 11×8 cm has a triangle (base 4, height 3) removed. Find remaining area.', '94', '87', '82', '88', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 11×8 - ½×4×3 = 88 - 6 = 82 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 15×14 cm has a 5×3 hole. Find the shaded area.', '15', '195', '225', '210', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 15×14 - 5×3 = 210 - 15 = 195 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 15×13 cm has a 6×5 hole. Find the shaded area.', '30', '225', '165', '195', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 15×13 - 6×5 = 195 - 30 = 165 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 12×11 cm has a triangle (base 5, height 3) removed. Find remaining area.', '130', '132', '139', '125', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12×11 - ½×5×3 = 132 - 7 = 125 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square has side 12 cm. Find its area.', '134', '288', '144', '154', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12² = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 12×12 cm has a triangle (base 4, height 3) removed. Find remaining area.', '144', '138', '143', '150', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12×12 - ½×4×3 = 144 - 6 = 138 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 24 and 35 cm² with overlap 9 cm². Find total area.', 'None of these', '59', '50', '24', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 24 + 35 - 9 = 50 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 9×3 and 4×6 cm. Find total area.', '51', '27', '61', '24', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 9×3 + 4×6 = 27 + 24 = 51 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 18×13 cm has a 4×5 hole. Find the shaded area.', '214', '254', '20', '234', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 18×13 - 4×5 = 234 - 20 = 214 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square has side 9 cm. Find its area.', '91', '81', '162', '71', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 9² = 81 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 18×13 cm has a 4×4 hole. Find the shaded area.', '234', '218', '16', '250', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 18×13 - 4×4 = 234 - 16 = 218 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 15×14 cm has a 4×3 hole. Find the shaded area.', '198', '210', '222', '12', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 15×14 - 4×3 = 210 - 12 = 198 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 22 and 24 cm² with overlap 8 cm². Find total area.', 'None of these', '46', '38', '22', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 22 + 24 - 8 = 38 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 10×5 and 5×5 cm. Find total area.', '75', '25', '85', '50', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 10×5 + 5×5 = 50 + 25 = 75 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 12×3 and 5×8 cm. Find total area.', '86', '76', '40', '36', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12×3 + 5×8 = 36 + 40 = 76 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 8×5 and 5×7 cm. Find total area.', '35', '85', '75', '40', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 8×5 + 5×7 = 40 + 35 = 75 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 36 and 34 cm² with overlap 8 cm². Find total area.', '70', '36', '62', 'None of these', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 36 + 34 - 8 = 62 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 8×3 and 5×7 cm. Find total area.', '24', '35', '59', '69', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 8×3 + 5×7 = 24 + 35 = 59 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 14×11 cm has a triangle (base 5, height 5) removed. Find remaining area.', '154', '142', '166', '147', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 14×11 - ½×5×5 = 154 - 12 = 142 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 16×13 cm has a 4×3 hole. Find the shaded area.', '220', '208', '12', '196', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 16×13 - 4×3 = 208 - 12 = 196 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square has side 8 cm. Find its area.', '128', '54', '64', '74', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 8² = 64 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 9×5 and 5×5 cm. Find total area.', '25', '80', '45', '70', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 9×5 + 5×5 = 45 + 25 = 70 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 16×11 cm has a 6×3 hole. Find the shaded area.', '176', '158', '18', '194', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 16×11 - 6×3 = 176 - 18 = 158 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 12×5 and 4×6 cm. Find total area.', '24', '84', '60', '94', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12×5 + 4×6 = 60 + 24 = 84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 20 and 30 cm² with overlap 10 cm². Find total area.', '20', 'None of these', '40', '50', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 20 + 30 - 10 = 40 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 12×10 cm has a triangle (base 3, height 4) removed. Find remaining area.', '119', '126', '120', '114', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12×10 - ½×3×4 = 120 - 6 = 114 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 10×10 cm has a triangle (base 4, height 5) removed. Find remaining area.', '110', '95', '100', '90', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 10×10 - ½×4×5 = 100 - 10 = 90 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 10×4 and 3×6 cm. Find total area.', '18', '40', '58', '68', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 10×4 + 3×6 = 40 + 18 = 58 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 28 and 30 cm² with overlap 6 cm². Find total area.', '28', '52', '58', 'None of these', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 28 + 30 - 6 = 52 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 34 and 30 cm² with overlap 8 cm². Find total area.', '34', '64', 'None of these', '56', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 34 + 30 - 8 = 56 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 13×9 cm has a triangle (base 5, height 4) removed. Find remaining area.', '107', '117', '112', '127', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 13×9 - ½×5×4 = 117 - 10 = 107 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 14×9 cm has a triangle (base 3, height 3) removed. Find remaining area.', '122', '130', '126', '127', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 14×9 - ½×3×3 = 126 - 4 = 122 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 13×10 cm has a triangle (base 4, height 3) removed. Find remaining area.', '136', '129', '124', '130', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 13×10 - ½×4×3 = 130 - 6 = 124 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 15×10 cm has a triangle (base 5, height 5) removed. Find remaining area.', '150', '143', '138', '162', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 15×10 - ½×5×5 = 150 - 12 = 138 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 12×12 cm has a triangle (base 3, height 4) removed. Find remaining area.', '143', '144', '150', '138', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12×12 - ½×3×4 = 144 - 6 = 138 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 18×12 cm has a 6×3 hole. Find the shaded area.', '234', '216', '18', '198', 3,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 18×12 - 6×3 = 216 - 18 = 198 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 10×12 cm has a triangle (base 3, height 4) removed. Find remaining area.', '120', '114', '119', '126', 1,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 10×12 - ½×3×4 = 120 - 6 = 114 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square has side 10 cm. Find its area.', '200', '110', '100', '90', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 10² = 100 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 13×8 cm has a triangle (base 3, height 5) removed. Find remaining area.', '97', '104', '102', '111', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 13×8 - ½×3×5 = 104 - 7 = 97 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square has side 12 cm. Find its area.', '154', '288', '144', '134', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 12² = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two shapes have areas 38 and 35 cm² with overlap 6 cm². Find total area.', '67', 'None of these', '73', '38', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Total = 38 + 35 - 6 = 67 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 11×10 cm has a triangle (base 5, height 4) removed. Find remaining area.', '110', '105', '100', '120', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 11×10 - ½×5×4 = 110 - 10 = 100 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangle 15×10 cm has a triangle (base 3, height 4) removed. Find remaining area.', '149', '150', '144', '156', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 15×10 - ½×3×4 = 150 - 6 = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 9×5 and 5×8 cm. Find total area.', '85', '45', '40', '95', 0,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 9×5 + 5×8 = 45 + 40 = 85 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An L-shape consists of rectangles 11×4 and 5×8 cm. Find total area.', '94', '40', '84', '44', 2,
'lc_hl_measurement', 3, 'foundation', 'lc_hl', 'Area = 11×4 + 5×8 = 44 + 40 = 84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 11 cm. (In terms of π)', '11π', '121π', '5π', '22π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 11 = 11π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 8 cm. (In terms of π)', '8π', '64π', '32π', '16π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 8/2 = 4. A = πr² = π × 4² = 16π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 9 cm. (In terms of π)', '81π', '32π', '16π', '9π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 9/2 = 4. A = πr² = π × 4² = 16π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 6 cm. (Leave answer in terms of π)', '6π', '24π', '12π', '36π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 6 = 12π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 5 cm. (Leave answer in terms of π)', '20π', '5π', '10π', '25π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 5 = 10π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 5 cm. (In terms of π)', '8π', '5π', '25π', '4π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 5/2 = 2. A = πr² = π × 2² = 4π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has circumference 12π cm. Find its radius.', '6', 'None of these', '5', '12', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr, so 12π = 2πr. r = 12/2 = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has area 25π cm². Find its radius.', '6', '25', '10', '5', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr², so 25π = πr². r² = 25, r = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has area 9π cm². Find its radius.', '4', '9', '3', '6', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr², so 9π = πr². r² = 9, r = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 7 cm. (In terms of π)', '18π', '49π', '9π', '7π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 7/2 = 3. A = πr² = π × 3² = 9π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 3 cm. (Leave answer in terms of π)', '6π', '9π', '12π', '3π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 3 = 6π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 6 cm. (Leave answer in terms of π)', '36π', '6π', '24π', '12π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 6 = 12π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 11 cm. (In terms of π)', '11π', '22π', '121π', '5π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 11 = 11π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has area 16π cm². Find its radius.', '16', '4', '8', '5', 1,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr², so 16π = πr². r² = 16, r = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 15 cm. (In terms of π)', '15π', '7π', '225π', '30π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 15 = 15π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 4 cm. (Leave answer in terms of π)', '8π', '4π', 'None of these', '16π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 4 = 8π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 15 cm. (In terms of π)', '7π', '225π', '30π', '15π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 15 = 15π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has circumference 10π cm. Find its radius.', '4', 'None of these', '10', '5', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr, so 10π = 2πr. r = 10/2 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 8 cm. (In terms of π)', '64π', '16π', '4π', '8π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 8 = 8π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 14 cm. (In terms of π)', '49π', '14π', '196π', '98π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 14/2 = 7. A = πr² = π × 7² = 49π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has circumference 8π cm. Find its radius.', '3', '8', 'None of these', '4', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr, so 8π = 2πr. r = 8/2 = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has circumference 14π cm. Find its radius.', '14', '7', '6', 'None of these', 1,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr, so 14π = 2πr. r = 14/2 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 9 cm. (Leave answer in terms of π)', '18π', '81π', '9π', '36π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 9 = 18π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 15 cm. (In terms of π)', '225π', '15π', '7π', '30π', 1,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 15 = 15π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 11 cm. (In terms of π)', '11π', '5π', '121π', '22π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 11 = 11π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has area 36π cm². Find its radius.', '7', '36', '6', '12', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr², so 36π = πr². r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has area 36π cm². Find its radius.', '12', '7', '36', '6', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr², so 36π = πr². r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 4 cm. (In terms of π)', '8π', '32π', '4π', '16π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr² = π × 4² = 16π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 7 cm. (Leave answer in terms of π)', '28π', '49π', '14π', '7π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 7 = 14π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has area 49π cm². Find its radius.', '7', '14', '8', '49', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr², so 49π = πr². r² = 49, r = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has circumference 14π cm. Find its radius.', '14', '7', 'None of these', '6', 1,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr, so 14π = 2πr. r = 14/2 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 9 cm. (Leave answer in terms of π)', '81π', '9π', '36π', '18π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 9 = 18π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 13 cm. (In terms of π)', '13π', '72π', '169π', '36π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 13/2 = 6. A = πr² = π × 6² = 36π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 6 cm. (In terms of π)', '36π', '72π', '12π', '6π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr² = π × 6² = 36π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 10 cm. (In terms of π)', '10π', '200π', '100π', '20π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr² = π × 10² = 100π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 9 cm. (In terms of π)', '9π', '18π', '162π', '81π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr² = π × 9² = 81π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 9 cm. (In terms of π)', '18π', '81π', '9π', '4π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 9 = 9π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has circumference 6π cm. Find its radius.', '3', '2', '6', 'None of these', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr, so 6π = 2πr. r = 6/2 = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 16 cm. (In terms of π)', '8π', '32π', '256π', '16π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 16 = 16π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 9 cm. (Leave answer in terms of π)', '81π', '36π', '9π', '18π', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 9 = 18π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 8 cm. (In terms of π)', '64π', '16π', '8π', '4π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 8 = 8π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has area 49π cm². Find its radius.', '8', '14', '49', '7', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'A = πr², so 49π = πr². r² = 49, r = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has circumference 10π cm. Find its radius.', '4', '10', 'None of these', '5', 3,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr, so 10π = 2πr. r = 10/2 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 4 cm. (Leave answer in terms of π)', '8π', 'None of these', '4π', '16π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = 2πr = 2π × 4 = 8π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 4 cm. (In terms of π)', 'None of these', '16π', '4π', '8π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 4/2 = 2. A = πr² = π × 2² = 4π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 10 cm. (In terms of π)', '50π', '100π', '25π', '10π', 2,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 10/2 = 5. A = πr² = π × 5² = 25π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 12 cm. (In terms of π)', '144π', '36π', '72π', '12π', 1,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 12/2 = 6. A = πr² = π × 6² = 36π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with diameter 20 cm. (In terms of π)', '10π', '20π', '400π', '40π', 1,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'C = πd = π × 20 = 20π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 6 cm. (In terms of π)', '9π', '6π', '36π', '18π', 0,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 6/2 = 3. A = πr² = π × 3² = 9π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with diameter 9 cm. (In terms of π)', '32π', '16π', '81π', '9π', 1,
'lc_hl_measurement', 4, 'developing', 'lc_hl', 'r = 9/2 = 4. A = πr² = π × 4² = 16π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 4 cm.', '4π', '32π', '16π/2', '16π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 4² = 16π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sector area: radius 7 cm, angle 60°. (In terms of π)', '49π', '98π', '49π/6', '7π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = (θ/360) × πr² = (60/360) × π × 7² = 49π/6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 9 cm.', '162π', '81π', '81π/2', '9π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 9² = 81π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 5 cm.', '5π', '10π', '5π + 5', '5π + 10', 3,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 5π + 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 9 cm.', '81π', '162π', '81π/2', '9π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 9² = 81π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 7 cm.', '49π/4', '7π', '49π', '49π/2', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 7² = 49π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 9 cm.', '18π', '9π + 18', '9π', '9π + 9', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 9π + 18 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 4 cm.', '16π', '16π/2', '4π', '32π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 4² = 16π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 5 cm.', '25π', '5π', '25π/2', '25π/4', 3,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 5² = 25π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 9 cm.', '9π', '81π/4', '81π', '81π/2', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 9² = 81π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 9 cm.', '81π/4', '81π/2', '9π', '81π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 9² = 81π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sector area: radius 6 cm, angle 180°. (In terms of π)', '72π', '6π', '36π/2', '36π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = (θ/360) × πr² = (180/360) × π × 6² = 36π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length: radius 6 cm, angle 180°. (In terms of π)', 'None of these', '36π', '6π', '12π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Arc = (θ/360) × 2πr = (180/360) × 2π × 6 = 6π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 4 cm.', '32π', '16π/2', '4π', '16π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 4² = 16π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 4 cm.', '16π/4', '16π', '16π/2', '4π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 4² = 16π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 10 cm.', '20π', '10π', '10π + 10', '10π + 20', 3,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 10π + 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sector area: radius 9 cm, angle 180°. (In terms of π)', '81π/2', '162π', '9π', '81π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = (θ/360) × πr² = (180/360) × π × 9² = 81π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length: radius 9 cm, angle 90°. (In terms of π)', '81π', '9π/2', '9π', '18π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Arc = (θ/360) × 2πr = (90/360) × 2π × 9 = 9π/2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 5 cm.', '25π/2', '25π/4', '25π', '5π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 5² = 25π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 8 cm.', '16π', '8π', '8π + 8', '8π + 16', 3,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 8π + 16 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 9 cm.', '81π/4', '81π', '9π', '81π/2', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 9² = 81π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length: radius 8 cm, angle 180°. (In terms of π)', '8π', 'None of these', '16π', '64π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Arc = (θ/360) × 2πr = (180/360) × 2π × 8 = 8π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 7 cm.', '49π', '98π', '49π/2', '7π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 7² = 49π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 10 cm.', '10π', '20π', '10π + 20', '10π + 10', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 10π + 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 4 cm.', '4π + 8', '4π + 4', '4π', '8π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 4π + 8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length: radius 11 cm, angle 180°. (In terms of π)', '121π', 'None of these', '11π', '22π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Arc = (θ/360) × 2πr = (180/360) × 2π × 11 = 11π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 10 cm.', '10π + 10', '20π', '10π + 20', '10π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 10π + 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length: radius 8 cm, angle 180°. (In terms of π)', 'None of these', '64π', '8π', '16π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Arc = (θ/360) × 2πr = (180/360) × 2π × 8 = 8π cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sector area: radius 5 cm, angle 180°. (In terms of π)', '50π', '5π', '25π', '25π/2', 3,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = (θ/360) × πr² = (180/360) × π × 5² = 25π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 4 cm.', '4π', '16π/2', '32π', '16π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 4² = 16π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 10 cm.', '10π', '10π + 10', '20π', '10π + 20', 3,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 10π + 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 7 cm.', '49π', '7π', '49π/2', '98π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 7² = 49π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 5 cm.', '5π + 10', '5π', '10π', '5π + 5', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 5π + 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 8 cm.', '64π/2', '128π', '8π', '64π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 8² = 64π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 7 cm.', '49π/4', '7π', '49π', '49π/2', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 7² = 49π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length: radius 8 cm, angle 60°. (In terms of π)', '8π', '16π', '64π', '8π/3', 3,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Arc = (θ/360) × 2πr = (60/360) × 2π × 8 = 8π/3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a quarter circle with radius 9 cm.', '9π', '81π/4', '81π/2', '81π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ¼πr² = ¼ × π × 9² = 81π/4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length: radius 11 cm, angle 90°. (In terms of π)', '11π', '11π/2', '22π', '121π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Arc = (θ/360) × 2πr = (90/360) × 2π × 11 = 11π/2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 5 cm.', '5π + 5', '5π', '5π + 10', '10π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 5π + 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 7 cm.', '7π', '49π/2', '49π', '98π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 7² = 49π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 6 cm.', '6π', '6π + 12', '6π + 6', '12π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 6π + 12 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 7 cm.', '7π + 14', '7π', '7π + 7', '14π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 7π + 14 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 4 cm.', '8π', '4π + 8', '4π + 4', '4π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 4π + 8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sector area: radius 9 cm, angle 120°. (In terms of π)', '81π', '162π', '81π/3', '9π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = (θ/360) × πr² = (120/360) × π × 9² = 81π/3 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sector area: radius 10 cm, angle 60°. (In terms of π)', '10π', '100π/6', '200π', '100π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = (θ/360) × πr² = (60/360) × π × 10² = 100π/6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 10 cm.', '100π', '200π', '100π/2', '10π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 10² = 100π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 5 cm.', '25π/2', '25π', '50π', '5π', 0,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 5² = 25π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 6 cm.', '72π', '36π', '36π/2', '6π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 6² = 36π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a semicircle with radius 5 cm.', '5π + 5', '5π + 10', '10π', '5π', 1,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Perimeter = πr + 2r = 5π + 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a semicircle with radius 7 cm.', '7π', '49π', '49π/2', '98π', 2,
'lc_hl_measurement', 5, 'developing', 'lc_hl', 'Area = ½πr² = ½ × π × 7² = 49π/2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 5 cm, height 5 cm, length 6 cm. Find 2 × triangle area + perimeter × length.', '24', '114', '150', '72', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 5 × 5) + perimeter × 6 = 24 + ... ≈ 114 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 7 × 4 × 5 cm.', '140', '83', '166', '176', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(28 + 35 + 20) = 166 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 7 cm, height 8 cm, length 8 cm. Find 2 × triangle area + perimeter × length.', '448', '56', 'None of these', '224', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 7 × 8) + perimeter × 8 = 56 + ... ≈ 224 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 7 cm.', '343', '196', '300', '294', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 7² = 294 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Open-top box 8 × 5 × 5 cm. Find surface area.', 'None of these', '210', '200', '170', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = lw + 2lh + 2wh = 40 + 80 + 50 = 170 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Open-top box 9 × 7 × 3 cm. Find surface area.', '222', '189', '159', 'None of these', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = lw + 2lh + 2wh = 63 + 54 + 42 = 159 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 6 × 4 × 7 cm.', '94', '188', '168', '198', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(24 + 42 + 28) = 188 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 5 cm.', '125', '156', '100', '150', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 5² = 150 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 5 cm, height 3 cm, length 6 cm. Find 2 × triangle area + perimeter × length.', '42', '90', '14', '104', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 5 × 3) + perimeter × 6 = 14 + ... ≈ 104 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 8, width 4, SA = 160 cm². Find height.', '4', '5', '8', 'None of these', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 6 × 7 × 6 cm.', '252', '120', '250', '240', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(42 + 36 + 42) = 240 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 8, width 3, SA = 114 cm². Find height.', '3', '8', 'None of these', '4', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 5 cm.', '150', '125', '100', '156', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 5² = 150 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 3 cm.', '60', '54', '36', '27', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 3² = 54 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 8 × 6 × 4 cm.', '208', '218', '192', '104', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(48 + 32 + 24) = 208 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 4 cm.', 'None of these', '102', '96', '64', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 4² = 96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 6 × 6 × 8 cm.', '132', '274', '264', '288', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(36 + 48 + 48) = 264 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 10 cm.', '600', '606', '400', '1000', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 10² = 600 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 6 cm.', '144', '216', 'None of these', '222', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 6² = 216 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 5 × 7 × 3 cm.', '105', '152', '142', '71', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(35 + 15 + 21) = 142 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 4, width 5, SA = 112 cm². Find height.', 'None of these', 'None of these', '4', '5', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Open-top box 9 × 8 × 5 cm. Find surface area.', '314', '242', '360', 'None of these', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = lw + 2lh + 2wh = 72 + 90 + 80 = 242 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 6 cm, height 8 cm, length 8 cm. Find 2 × triangle area + perimeter × length.', 'None of these', '48', '384', '192', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 6 × 8) + perimeter × 8 = 48 + ... ≈ 192 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 5 × 7 × 3 cm.', '152', '142', '71', '105', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(35 + 15 + 21) = 142 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 8 cm.', '384', '256', '390', '512', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 8² = 384 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 7, width 3, SA = 162 cm². Find height.', '6', '3', '7', 'None of these', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 3 × 5 × 8 cm.', '168', '158', '79', '120', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(15 + 24 + 40) = 158 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Open-top box 10 × 8 × 5 cm. Find surface area.', '400', '260', '340', 'None of these', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = lw + 2lh + 2wh = 80 + 100 + 80 = 260 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 7, width 3, SA = 122 cm². Find height.', '3', '7', '5', '4', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 6 cm.', '222', '216', '144', 'None of these', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 6² = 216 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 4 cm, height 3 cm, length 5 cm. Find 2 × triangle area + perimeter × length.', '60', '30', '12', '72', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 4 × 3) + perimeter × 5 = 12 + ... ≈ 72 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 3 × 5 × 5 cm.', '110', '75', '55', '120', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(15 + 15 + 25) = 110 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 4 cm, height 8 cm, length 6 cm. Find 2 × triangle area + perimeter × length.', '32', '96', '192', '104', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 4 × 8) + perimeter × 6 = 32 + ... ≈ 104 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Open-top box 5 × 6 × 6 cm. Find surface area.', 'None of these', '180', '192', '162', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = lw + 2lh + 2wh = 30 + 60 + 72 = 162 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 5, width 4, SA = 94 cm². Find height.', '4', '5', 'None of these', '3', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 3 × 4 × 7 cm.', '122', '132', '84', '61', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(12 + 21 + 28) = 122 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 4, width 3, SA = 80 cm². Find height.', '4', '3', '5', 'None of these', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Open-top box 6 × 4 × 3 cm. Find surface area.', '72', '108', '84', 'None of these', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = lw + 2lh + 2wh = 24 + 36 + 24 = 84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 5, width 6, SA = 126 cm². Find height.', '4', '3', '6', '5', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 7 × 6 × 6 cm.', '240', '120', '250', '252', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(42 + 42 + 36) = 240 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 6 cm, height 3 cm, length 6 cm. Find 2 × triangle area + perimeter × length.', '18', '108', '54', '126', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 6 × 3) + perimeter × 6 = 18 + ... ≈ 126 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Open-top box 10 × 6 × 6 cm. Find surface area.', '252', '360', 'None of these', '312', 0,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = lw + 2lh + 2wh = 60 + 120 + 72 = 252 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 4, width 5, SA = 148 cm². Find height.', '4', '5', '7', '6', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 5 cm, height 6 cm, length 7 cm. Find 2 × triangle area + perimeter × length.', '105', '30', '135', '210', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 5 × 6) + perimeter × 7 = 30 + ... ≈ 135 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 7 × 4 × 8 cm.', '224', '232', '116', '242', 1,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(28 + 56 + 32) = 232 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of cuboid 8 × 5 × 6 cm.', '118', '246', '236', '240', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 2(lw + lh + wh) = 2(40 + 48 + 30) = 236 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 7, width 3, SA = 142 cm². Find height.', '7', '6', '3', '5', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find surface area of a cube with side 10 cm.', '1000', '606', '400', '600', 3,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'SA = 6s² = 6 × 10² = 600 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid: length 8, width 6, SA = 264 cm². Find height.', '7', '8', '6', 'None of these', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', 'Using SA = 2(lw + lh + wh), height = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 3 cm, height 6 cm, length 10 cm. Find 2 × triangle area + perimeter × length.', '180', '90', '108', '18', 2,
'lc_hl_measurement', 6, 'developing', 'lc_hl', '2 × (½ × 3 × 6) + perimeter × 10 = 18 + ... ≈ 108 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 7 cm, height 9 cm.', '126π', '441π', '224π', '112π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 7 × 16 = 224π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 6 cm, height 12 cm.', '108π', '216π', '144π', '432π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 6 × 18 = 216π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 4 cm, height 6 cm.', '80π', '40π', '96π', '48π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 4 × 10 = 80π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 4 cm, height 11 cm.', '120π', '44π', '88π', '176π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 4 × 11 = 88π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 4 cm.', '32π', '48π', '64π', '16π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 4² = 48π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 4 cm, slant height 9 cm.', '52π', '36π', '104π', '144π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 4 × 13 = 52π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 8 cm.', '192π', '256π', '64π', '128π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 8² = 192π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 5 cm, height 5 cm.', '125π', '100π', '25π', '50π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 5 × 5 = 50π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 3 cm, height 8 cm.', '66π', '72π', '48π', '33π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 3 × 11 = 66π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 6 cm.', '144π', '72π', '36π', '108π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 6² = 108π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 3 cm, slant height 6 cm.', '18π', 'None of these', '54π', '27π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 3 × 9 = 27π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 7 cm, height 8 cm.', '210π', '392π', '112π', '105π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 7 × 15 = 210π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cone: radius 6 cm, slant height 5 cm.', '60π', '66π', '30π', '180π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = πrl = π × 6 × 5 = 30π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cone: radius 7 cm, slant height 6 cm.', '91π', '42π', '294π', '84π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = πrl = π × 7 × 6 = 42π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 4 cm.', '32π', '64π', '16π', '48π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 4² = 48π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 7 cm, slant height 8 cm.', '56π', '210π', '105π', '392π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 7 × 15 = 105π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 6 cm.', '36π', '108π', '144π', '72π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 6² = 108π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 6 cm, slant height 8 cm.', '84π', '48π', '168π', '288π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 6 × 14 = 84π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 3 cm, height 8 cm.', '72π', '24π', '66π', '48π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 3 × 8 = 48π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cone: radius 7 cm, slant height 7 cm.', '343π', '49π', '98π', 'None of these', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = πrl = π × 7 × 7 = 49π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 7 cm.', '147π', '98π', '196π', '49π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 7² = 147π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 4 cm, slant height 7 cm.', '88π', '28π', '112π', '44π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 4 × 11 = 44π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 3 cm, slant height 8 cm.', '66π', '24π', '72π', '33π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 3 × 11 = 33π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 6 cm, height 12 cm.', '432π', '216π', '144π', '108π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 6 × 18 = 216π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 3 cm, slant height 9 cm.', '81π', '72π', '36π', '27π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 3 × 12 = 36π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 7 cm, slant height 8 cm.', '105π', '210π', '392π', '56π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 7 × 15 = 105π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 6 cm, height 5 cm.', '30π', '132π', '60π', '180π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 6 × 5 = 60π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 8 cm, height 8 cm.', '256π', '128π', '64π', '512π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 8 × 8 = 128π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 3 cm.', '18π', '36π', '27π', '9π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 3² = 27π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cone: radius 4 cm, slant height 5 cm.', '20π', '36π', '40π', '80π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = πrl = π × 4 × 5 = 20π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 3 cm.', '36π', '9π', '27π', '18π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 3² = 27π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 5 cm, height 10 cm.', '150π', '100π', '250π', '50π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 5 × 10 = 100π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 3 cm, height 9 cm.', '72π', '81π', '36π', '54π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 3 × 12 = 72π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 6 cm.', '144π', '36π', '108π', '72π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 6² = 108π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 3 cm.', '27π', '9π', '18π', '36π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 3² = 27π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 5 cm, slant height 9 cm.', '225π', '140π', '70π', '45π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 5 × 14 = 70π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 8 cm, height 10 cm.', '160π', '288π', '80π', '640π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 8 × 10 = 160π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 6 cm, slant height 5 cm.', '180π', '132π', '30π', '66π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 6 × 11 = 66π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 4 cm.', '64π', '48π', '32π', '16π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 4² = 48π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 4 cm.', '64π', '48π', '32π', '16π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 4² = 48π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cone: radius 5 cm, slant height 5 cm.', 'None of these', '125π', '25π', '50π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = πrl = π × 5 × 5 = 25π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 4 cm, slant height 7 cm.', '112π', '88π', '44π', '28π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 4 × 11 = 44π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 3 cm.', '27π', '9π', '18π', '36π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 3² = 27π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 7 cm, height 6 cm.', '84π', '91π', '182π', '294π', 2,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 7 × 13 = 182π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cone: radius 6 cm, slant height 8 cm.', '84π', '48π', '96π', '288π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = πrl = π × 6 × 8 = 48π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cone: radius 6 cm, slant height 7 cm.', '42π', '252π', '84π', '78π', 0,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = πrl = π × 6 × 7 = 42π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cone: radius 3 cm, slant height 8 cm.', '24π', '33π', '66π', '72π', 1,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = πr² + πrl = πr(r + l) = π × 3 × 11 = 33π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find curved surface area of cylinder: radius 5 cm, height 8 cm.', '200π', '40π', '130π', '80π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'CSA = 2πrh = 2π × 5 × 8 = 80π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of hemisphere with radius 5 cm.', '100π', '50π', '25π', '75π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + πr² = 3πr² = 3 × π × 5² = 75π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find total surface area of cylinder: radius 7 cm, height 5 cm.', '70π', '84π', '245π', '168π', 3,
'lc_hl_measurement', 7, 'proficient', 'lc_hl', 'SA = 2πr² + 2πrh = 2πr(r + h) = 2π × 7 × 12 = 168π cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prism with trapezium cross-section: parallel sides 6, 9 cm, height 3 cm, length 5 cm. Find volume.', '132', '225', '110', '22', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = ½(6+9)×3×5 = 22×5 = 110 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 120 cm³, length = 6 cm, width = 4 cm. Find height.', 'None of these', '4', '5', '6', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 120/(6×4) = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 6 cm, triangle height 7 cm, length 9 cm. Find volume.', '198', '189', '378', '21', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 6 × 7) × 9 = 21 × 9 = 189 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 4 cm.', '64', '68', '16', '96', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 4³ = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 8 cm.', '512', '384', '520', '64', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 8³ = 512 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 4 × 10 × 9 cm.', '332', '364', '23', '360', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 4 × 10 × 9 = 360 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 6 cm.', 'None of these', '222', '216', '36', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 6³ = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 3 cm.', '27', '30', '54', '9', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 3³ = 27 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 10 × 4 × 6 cm.', '248', '20', '250', '240', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 10 × 4 × 6 = 240 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 168 cm³, length = 8 cm, width = 3 cm. Find height.', '7', '8', 'None of these', '3', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 168/(8×3) = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 144 cm³, length = 6 cm, width = 4 cm. Find height.', '7', '6', '4', 'None of these', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 144/(6×4) = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 8 cm, triangle height 8 cm, length 12 cm. Find volume.', '768', '384', '396', '32', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 8 × 8) × 12 = 32 × 12 = 384 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 9 × 9 × 10 cm.', '522', '28', '810', '819', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 9 × 9 × 10 = 810 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 7 × 4 × 5 cm.', '16', '140', '166', '147', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 7 × 4 × 5 = 140 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prism with trapezium cross-section: parallel sides 4, 9 cm, height 3 cm, length 9 cm. Find volume.', '190', '19', '171', '351', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = ½(4+9)×3×9 = 19×9 = 171 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 9 cm, triangle height 8 cm, length 10 cm. Find volume.', '360', '370', '36', '720', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 9 × 8) × 10 = 36 × 10 = 360 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 10 × 5 × 5 cm.', '260', '250', 'None of these', '20', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 10 × 5 × 5 = 250 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 96 cm³, length = 4 cm, width = 4 cm. Find height.', '6', '7', 'None of these', '4', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 96/(4×4) = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 6 cm.', 'None of these', '222', '36', '216', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 6³ = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 8 × 4 × 6 cm.', '208', '18', '200', '192', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 8 × 4 × 6 = 192 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prism with trapezium cross-section: parallel sides 4, 6 cm, height 6 cm, length 10 cm. Find volume.', '30', '600', '300', '330', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = ½(4+6)×6×10 = 30×10 = 300 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 7 cm.', '343', '294', '350', '49', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 7³ = 343 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 7 × 3 × 6 cm.', '162', '16', '133', '126', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 7 × 3 × 6 = 126 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 9 cm, triangle height 4 cm, length 9 cm. Find volume.', '18', '324', '162', '171', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 9 × 4) × 9 = 18 × 9 = 162 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 6 × 6 × 7 cm.', '240', '252', '258', '19', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 6 × 6 × 7 = 252 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 10 cm, triangle height 7 cm, length 6 cm. Find volume.', '216', '420', '210', '35', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 10 × 7) × 6 = 35 × 6 = 210 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 6 × 7 × 3 cm.', '162', '132', '16', '126', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 6 × 7 × 3 = 126 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 4 cm.', '16', '64', '68', '96', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 4³ = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 7 cm, triangle height 10 cm, length 6 cm. Find volume.', '216', '420', '35', '210', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 7 × 10) × 6 = 35 × 6 = 210 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 4 cm.', '16', '96', '68', '64', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 4³ = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 120 cm³, length = 6 cm, width = 4 cm. Find height.', '5', 'None of these', '4', '6', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 120/(6×4) = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 4 cm.', '16', '64', '68', '96', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 4³ = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prism with trapezium cross-section: parallel sides 4, 10 cm, height 5 cm, length 5 cm. Find volume.', '175', '350', '210', '35', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = ½(4+10)×5×5 = 35×5 = 175 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 7 cm, triangle height 4 cm, length 7 cm. Find volume.', '105', '98', '14', '196', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 7 × 4) × 7 = 14 × 7 = 98 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 4 cm, triangle height 5 cm, length 6 cm. Find volume.', '120', '10', '60', '66', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 4 × 5) × 6 = 10 × 6 = 60 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 9 × 4 × 9 cm.', '22', '324', '306', '333', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 9 × 4 × 9 = 324 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 4 cm, triangle height 9 cm, length 8 cm. Find volume.', '152', '144', '18', '288', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 4 × 9) × 8 = 18 × 8 = 144 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 245 cm³, length = 7 cm, width = 5 cm. Find height.', '5', '8', 'None of these', '7', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 245/(7×5) = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 84 cm³, length = 4 cm, width = 3 cm. Find height.', '4', '7', '8', '3', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 84/(4×3) = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 4 × 7 × 5 cm.', '144', '166', '16', '140', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 4 × 7 × 5 = 140 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 7 cm, triangle height 7 cm, length 11 cm. Find volume.', '275', '264', '539', '24', 1,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 7 × 7) × 11 = 24 × 11 = 264 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 7 cm.', '294', '49', '350', '343', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 7³ = 343 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prism with trapezium cross-section: parallel sides 4, 10 cm, height 4 cm, length 9 cm. Find volume.', '28', '280', '252', '504', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = ½(4+10)×4×9 = 28×9 = 252 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 112 cm³, length = 7 cm, width = 4 cm. Find height.', '4', 'None of these', '5', '7', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 112/(7×4) = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 8 cm.', '64', '520', '384', '512', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 8³ = 512 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of a cube with side 6 cm.', '216', '222', '36', 'None of these', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = s³ = 6³ = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cuboid 10 × 7 × 6 cm.', '23', '344', '430', '420', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = lwh = 10 × 7 × 6 = 420 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 60 cm³, length = 5 cm, width = 3 cm. Find height.', 'None of these', '3', '5', '4', 3,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 60/(5×3) = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cuboid volume = 125 cm³, length = 5 cm, width = 5 cm. Find height.', '6', 'None of these', '5', 'None of these', 2,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'h = V/(lw) = 125/(5×5) = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangular prism: base 5 cm, triangle height 4 cm, length 12 cm. Find volume.', '120', '132', '10', '240', 0,
'lc_hl_measurement', 8, 'proficient', 'lc_hl', 'V = (½ × 5 × 4) × 12 = 10 × 12 = 120 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '4', '1/3', '3', '2', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 6 cm, height 8 cm.', '288π/2', '288π', '288π/3', '48π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 6² × 8 = 288π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 5 cm, inner radius 3 cm, height 13 cm. Find volume.', '442π', '208π', '325π', '117π', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(5² - 3²)×13 = 208π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 3 cm, height 7 cm.', '63π/2', '63π/3', '21π', '63π', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 3² × 7 = 63π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 3 cm, height 10 cm.', '30π', '90π', '90π/3', '90π/2', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 3² × 10 = 90π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cylinder: radius 4 cm, height 7 cm.', '16π', '28π', '112π', '56π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h = π × 4² × 7 = 112π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cylinder: radius 7 cm, height 10 cm.', '490π', '49π', '70π', '140π', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h = π × 7² × 10 = 490π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '2', '4', '1/3', '3', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 7 cm, inner radius 3 cm, height 11 cm. Find volume.', '99π', '539π', '440π', '638π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(7² - 3²)×11 = 440π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 360π cm³, height = 10 cm. Find radius.', '6', '7', '360', '10', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 360π = πr²×10. r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 252π cm³, height = 7 cm. Find radius.', '6', 'None of these', '7', '252', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 252π = πr²×7. r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '1/3', '4', '2', '3', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '4', '1/3', '3', '2', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 8 cm, inner radius 3 cm, height 14 cm. Find volume.', '1022π', '896π', '126π', '770π', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(8² - 3²)×14 = 770π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 7 cm, height 10 cm.', '70π', '490π/2', '490π', '490π/3', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 7² × 10 = 490π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cylinder: radius 8 cm, height 8 cm.', '64π', '512π', 'None of these', '128π', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h = π × 8² × 8 = 512π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '3', '4', '2', '1/3', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 7 cm, inner radius 2 cm, height 13 cm. Find volume.', '52π', '689π', '585π', '637π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(7² - 2²)×13 = 585π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '2', '1/3', '4', '3', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '4', '3', '1/3', '2', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 180π cm³, height = 5 cm. Find radius.', '6', '7', '180', '5', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 180π = πr²×5. r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '2', '4', '3', '1/3', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 6 cm, height 10 cm.', '360π', '360π/2', '360π/3', '60π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 6² × 10 = 360π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '3', '2', '1/3', '4', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 3 cm, height 8 cm.', '72π', '72π/3', '24π', '72π/2', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 3² × 8 = 72π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 180π cm³, height = 5 cm. Find radius.', '5', '7', '180', '6', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 180π = πr²×5. r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 490π cm³, height = 10 cm. Find radius.', '490', '10', '8', '7', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 490π = πr²×10. r² = 49, r = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 8 cm, inner radius 4 cm, height 13 cm. Find volume.', '624π', '832π', '208π', '1040π', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(8² - 4²)×13 = 624π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '4', '3', '2', '1/3', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '3', '1/3', '4', '2', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 5 cm, inner radius 4 cm, height 14 cm. Find volume.', '126π', '574π', '350π', '224π', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(5² - 4²)×14 = 126π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 81π cm³, height = 9 cm. Find radius.', '81', '3', '9', '4', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 81π = πr²×9. r² = 9, r = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '2', '3', '4', '1/3', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 7 cm, inner radius 3 cm, height 10 cm. Find volume.', '490π', '90π', '400π', '580π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(7² - 3²)×10 = 400π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cylinder: radius 7 cm, height 7 cm.', 'None of these', '343π', '98π', '49π', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h = π × 7² × 7 = 343π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '1/3', '3', '2', '4', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 7 cm, inner radius 3 cm, height 12 cm. Find volume.', '588π', '696π', '480π', '108π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(7² - 3²)×12 = 480π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 3 cm, height 9 cm.', '81π/3', '81π/2', '27π', '81π', 0,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 3² × 9 = 81π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cylinder: radius 6 cm, height 9 cm.', '54π', '108π', '36π', '324π', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h = π × 6² × 9 = 324π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 441π cm³, height = 9 cm. Find radius.', '9', '7', '441', '8', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 441π = πr²×9. r² = 49, r = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 3 cm, height 7 cm.', '63π', '63π/2', '21π', '63π/3', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 3² × 7 = 63π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cone and cylinder have the same radius and height. How many cones fill the cylinder?', '4', '1/3', '3', '2', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cylinder: radius 4 cm, height 9 cm.', '36π', '72π', '16π', '144π', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h = π × 4² × 9 = 144π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Hollow cylinder: outer radius 7 cm, inner radius 3 cm, height 15 cm. Find volume.', '135π', '870π', '735π', '600π', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = π(R² - r²)h = π(7² - 3²)×15 = 600π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 54π cm³, height = 6 cm. Find radius.', '4', '54', '6', '3', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 54π = πr²×6. r² = 9, r = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cylinder: radius 7 cm, height 11 cm.', '49π', '154π', '77π', '539π', 3,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h = π × 7² × 11 = 539π cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 216π cm³, height = 6 cm. Find radius.', '216', 'None of these', '6', '7', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 216π = πr²×6. r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of cone: radius 4 cm, height 9 cm.', '36π', '144π/2', '144π/3', '144π', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = ⅓πr²h = ⅓ × π × 4² × 9 = 144π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 175π cm³, height = 7 cm. Find radius.', '7', '6', '5', '175', 2,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 175π = πr²×7. r² = 25, r = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder: volume = 288π cm³, height = 8 cm. Find radius.', '7', '6', '8', '288', 1,
'lc_hl_measurement', 9, 'proficient', 'lc_hl', 'V = πr²h, so 288π = πr²×8. r² = 36, r = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 9 cm.', '2916π/3', '324π', '2916π', '729π', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×9³ = 2916π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 3 cm.', '36π', '27π', '108π/3', '108π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×3³ = 108π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 4×6 cm, height 7 cm. Find volume.', '168', '24', '56', '60', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 4 × 6 × 7 = 56 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 10 cm, height 7 cm. Find volume.', '240', '700', '100', '233', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 10² × 7 = 233 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of hemisphere with radius 7 cm.', '1372π/3', '686π/3', '686π', '343π', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (2/3)πr³ = (2/3)π×7³ = 686π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 4×6 cm, height 6 cm. Find volume.', '48', '24', '144', '52', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 4 × 6 × 6 = 48 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 5×5 cm, height 6 cm. Find volume.', '55', '25', '150', '50', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 5 × 5 × 6 = 50 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of hemisphere with radius 3 cm.', '27π', '54π', '108π/3', '54π/3', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (2/3)πr³ = (2/3)π×3³ = 54π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 8 cm.', '2048π/3', '256π', '512π', '2048π', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×8³ = 2048π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 9 cm.', '729π', '2916π', '2916π/3', '324π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×9³ = 2916π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 3 cm.', '108π', '27π', '108π/3', '36π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×3³ = 108π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 5 cm.', '125π', '100π', '500π/3', '500π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×5³ = 500π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sphere volume = 256π/3 cm³. Find radius.', '85', '5', '16', '4', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', '(4/3)πr³ = 256π/3, so r³ = 64, r = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sphere volume = 256π/3 cm³. Find radius.', '16', '4', '85', '5', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', '(4/3)πr³ = 256π/3, so r³ = 64, r = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 5 cm, height 9 cm. Find volume.', '225', '75', '25', '84', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 5² × 9 = 75 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 8 cm, height 8 cm. Find volume.', '178', '64', '170', '512', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 8² × 8 = 170 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sphere volume = 500π/3 cm³. Find radius.', '166', '5', '6', '25', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', '(4/3)πr³ = 500π/3, so r³ = 125, r = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sphere volume = 108π/3 cm³. Find radius.', '9', '3', '4', '36', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', '(4/3)πr³ = 108π/3, so r³ = 27, r = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 7 cm.', '196π', '1372π', '343π', '1372π/3', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×7³ = 1372π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 8 cm.', '2048π/3', '2048π', '256π', '512π', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×8³ = 2048π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of hemisphere with radius 6 cm.', '216π', '432π/3', '864π/3', '432π', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (2/3)πr³ = (2/3)π×6³ = 432π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 6×5 cm, height 10 cm. Find volume.', '100', '106', '300', '30', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 6 × 5 × 10 = 100 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 5 cm, height 10 cm. Find volume.', '93', '25', '250', '83', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 5² × 10 = 83 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 8 cm.', '2048π/3', '2048π', '512π', '256π', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×8³ = 2048π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 5 cm, height 6 cm. Find volume.', '50', '56', '150', '25', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 5² × 6 = 50 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 8×5 cm, height 6 cm. Find volume.', '80', '240', '88', '40', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 8 × 5 × 6 = 80 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 6 cm.', '864π', '864π/3', '216π', '144π', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×6³ = 864π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sphere volume = 108π/3 cm³. Find radius.', '9', '3', '4', '36', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', '(4/3)πr³ = 108π/3, so r³ = 27, r = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 6 cm, height 10 cm. Find volume.', '130', '360', '36', '120', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 6² × 10 = 120 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 5 cm, height 6 cm. Find volume.', '50', '25', '150', '56', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 5² × 6 = 50 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 6×4 cm, height 8 cm. Find volume.', '70', '192', '64', '24', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 6 × 4 × 8 = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 4 cm.', '256π', 'None of these', '64π', '256π/3', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×4³ = 256π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 7 cm.', '1372π', '196π', '1372π/3', '343π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×7³ = 1372π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 6 cm.', '864π/3', '864π', '144π', '216π', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×6³ = 864π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 8 cm.', '2048π', '512π', '256π', '2048π/3', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×8³ = 2048π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 7×4 cm, height 8 cm. Find volume.', '28', '224', '81', '74', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 7 × 4 × 8 = 74 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 4×6 cm, height 9 cm. Find volume.', '216', '24', '76', '72', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 4 × 6 × 9 = 72 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 10 cm, height 12 cm. Find volume.', '100', '412', '1200', '400', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 10² × 12 = 400 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sphere volume = 500π/3 cm³. Find radius.', '25', '166', '6', '5', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', '(4/3)πr³ = 500π/3, so r³ = 125, r = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rectangular pyramid: base 5×5 cm, height 6 cm. Find volume.', '150', '55', '50', '25', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × 5 × 5 × 6 = 50 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of hemisphere with radius 8 cm.', '1024π', '512π', '1024π/3', '2048π/3', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (2/3)πr³ = (2/3)π×8³ = 1024π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 6 cm, height 10 cm. Find volume.', '130', '360', '120', '36', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 6² × 10 = 120 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 8 cm, height 12 cm. Find volume.', '256', '64', '768', '268', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 8² × 12 = 256 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 10 cm, height 6 cm. Find volume.', '600', '100', '206', '200', 3,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 10² × 6 = 200 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 3 cm.', '108π/3', '108π', '27π', '36π', 0,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×3³ = 108π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 7 cm.', '343π', '196π', '1372π/3', '1372π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×7³ = 1372π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of hemisphere with radius 3 cm.', '108π/3', '27π', '54π/3', '54π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (2/3)πr³ = (2/3)π×3³ = 54π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 5 cm, height 11 cm. Find volume.', '25', '91', '102', '275', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 5² × 11 = 91 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find volume of sphere with radius 5 cm.', '100π', '500π', '500π/3', '125π', 2,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = (4/3)πr³ = (4/3)π×5³ = 500π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Square pyramid: base side 4 cm, height 8 cm. Find volume.', '128', '42', '50', '16', 1,
'lc_hl_measurement', 10, 'advanced', 'lc_hl', 'V = ⅓ × base area × height = ⅓ × 4² × 8 = 42 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3 m³ to cm³.', '30000', '300', '3000000', '3000', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 3 × 1,000,000 = 3000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1 m³ to cm³.', '10000', '1000000', '1000', '100', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 1 × 1,000,000 = 1000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1112 litres to m³.', '1112000', '11.12', '1.112', '1112', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 1112 ÷ 1000 = 1.112 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 352 litres to m³.', '3.52', '352', '352000', '0.352', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 352 ÷ 1000 = 0.352 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4521 mm² to cm².', '45.21', '4.521', '452.1', '452100', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 4521 ÷ 100 = 45.21 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 72116 cm² to m².', '7.2116', '7211600', '72.116', '721.16', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m² = 10000 cm². 72116 ÷ 10000 = 7.2116 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 52502 cm² to m².', '52.502', '525.02', '5250200', '5.2502', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m² = 10000 cm². 52502 ÷ 10000 = 5.2502 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4669 cm³ to litres.', '466.9', '4.669', '46.69', '4669000', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 litre = 1000 cm³. 4669 ÷ 1000 = 4.669 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1274 litres to m³.', '12.74', '1.274', '1274', '1274000', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 1274 ÷ 1000 = 1.274 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4 m³ to cm³.', '4000', '40000', '4000000', '400', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 4 × 1,000,000 = 4000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4 km² to m².', '400', '40000', '4000', '4000000', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 km² = 1,000,000 m². 4 × 1,000,000 = 4000000 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2 m³ to cm³.', '200', '2000', '2000000', '20000', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 2 × 1,000,000 = 2000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4240 mm² to cm².', '42.4', '424.0', '4.24', '424000', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 4240 ÷ 100 = 42.4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3 m³ to cm³.', '300', '3000000', '30000', '3000', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 3 × 1,000,000 = 3000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 871 cm³ to litres.', '871000', '8.71', '87.1', '0.871', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 litre = 1000 cm³. 871 ÷ 1000 = 0.871 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 36117 cm² to m².', '36.117', '3.6117', '361.17', '3611700', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m² = 10000 cm². 36117 ÷ 10000 = 3.6117 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 808 litres to m³.', '0.808', '808000', '8.08', '808', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 808 ÷ 1000 = 0.808 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 5 km² to m².', '5000', '50000', '5000000', '500', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 km² = 1,000,000 m². 5 × 1,000,000 = 5000000 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3 km² to m².', '3000000', '30000', '300', '3000', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 km² = 1,000,000 m². 3 × 1,000,000 = 3000000 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 8786 mm² to cm².', '87.86', '878600', '878.6', '8.786', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 8786 ÷ 100 = 87.86 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3803 mm² to cm².', '3.803', '38.03', '380300', '380.3', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 3803 ÷ 100 = 38.03 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1 km² to m².', '1000000', '100', '1000', '10000', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 km² = 1,000,000 m². 1 × 1,000,000 = 1000000 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 5 m³ to cm³.', '5000', '50000', '5000000', '500', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 5 × 1,000,000 = 5000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1 m³ to cm³.', '1000000', '1000', '100', '10000', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 1 × 1,000,000 = 1000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3809 cm³ to litres.', '38.09', '380.9', '3809000', '3.809', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 litre = 1000 cm³. 3809 ÷ 1000 = 3.809 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3657 cm³ to litres.', '36.57', '3.657', '3657000', '365.7', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 litre = 1000 cm³. 3657 ÷ 1000 = 3.657 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3755 cm³ to litres.', '37.55', '3755000', '375.5', '3.755', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 litre = 1000 cm³. 3755 ÷ 1000 = 3.755 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 5 m³ to cm³.', '50000', '5000000', '500', '5000', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 5 × 1,000,000 = 5000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 16552 cm² to m².', '165.52', '16.552', '1.6552', '1655200', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m² = 10000 cm². 16552 ÷ 10000 = 1.6552 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4 km² to m².', '400', '4000000', '40000', '4000', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 km² = 1,000,000 m². 4 × 1,000,000 = 4000000 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1946 litres to m³.', '19.46', '1.946', '1946000', '1946', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 1946 ÷ 1000 = 1.946 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 23072 cm² to m².', '2.3072', '2307200', '230.72', '23.072', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m² = 10000 cm². 23072 ÷ 10000 = 2.3072 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4 m³ to cm³.', '40000', '400', '4000', '4000000', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 4 × 1,000,000 = 4000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1 m³ to cm³.', '1000000', '100', '10000', '1000', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 1 × 1,000,000 = 1000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1569 litres to m³.', '15.69', '1.569', '1569000', '1569', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 1569 ÷ 1000 = 1.569 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2 m³ to cm³.', '200', '2000', '20000', '2000000', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1,000,000 cm³. 2 × 1,000,000 = 2000000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 6843 mm² to cm².', '6.843', '68.43', '684300', '684.3', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 6843 ÷ 100 = 68.43 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 5629 mm² to cm².', '562900', '562.9', '56.29', '5.629', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 5629 ÷ 100 = 56.29 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 6988 mm² to cm².', '69.88', '698.8', '6.988', '698800', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 6988 ÷ 100 = 69.88 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3 km² to m².', '30000', '3000', '300', '3000000', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 km² = 1,000,000 m². 3 × 1,000,000 = 3000000 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3567 mm² to cm².', '356.7', '35.67', '356700', '3.567', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 3567 ÷ 100 = 35.67 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 8182 mm² to cm².', '818.2', '8.182', '818200', '81.82', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 8182 ÷ 100 = 81.82 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3100 mm² to cm².', '310.0', '3.1', '31.0', '310000', 2,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 cm² = 100 mm². 3100 ÷ 100 = 31.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1541 litres to m³.', '1.541', '1541000', '15.41', '1541', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 1541 ÷ 1000 = 1.541 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4830 cm³ to litres.', '4830000', '4.83', '483.0', '48.3', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 litre = 1000 cm³. 4830 ÷ 1000 = 4.83 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 222 litres to m³.', '0.222', '222', '2.22', '222000', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 222 ÷ 1000 = 0.222 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 18661 cm² to m².', '1.8661', '18.661', '1866100', '186.61', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m² = 10000 cm². 18661 ÷ 10000 = 1.8661 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 117 litres to m³.', '1.17', '0.117', '117', '117000', 1,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 m³ = 1000 litres. 117 ÷ 1000 = 0.117 m³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1 km² to m².', '1000000', '100', '10000', '1000', 0,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 km² = 1,000,000 m². 1 × 1,000,000 = 1000000 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2660 cm³ to litres.', '26.6', '266.0', '2660000', '2.66', 3,
'lc_hl_measurement', 11, 'advanced', 'lc_hl', '1 litre = 1000 cm³. 2660 ÷ 1000 = 2.66 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A sphere radius 6 cm is submerged. Find water displaced.', '144π', '864π', '864π/3', '216π', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Water displaced = volume of sphere = (4/3)πr³ = 864π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 15 cm. Find capacity in litres (in terms of π).', '13500π', '3375π/3', '13500π/3', '13500π/3000', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 13500π/3 cm³ = 13500π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 7, find the ratio of surface area to volume.', '6/7', '7', '67', '7/6', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Room 10×7×4 m. Find wall area to paint (4 walls only).', '276', '206', '136', '70', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Walls = 2(lh + wh) = 2(10×4 + 7×4) = 136 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder (r=3, h=9) topped with cone (h=4). Find total volume.', '45π', '117π', '81π + 36π/3', '81π', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = πr²h + ⅓πr²h = 81π + 36π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 10 cm. Find capacity in litres (in terms of π).', '1000π/3', '4000π/3000', '4000π/3', '4000π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 4000π/3 cm³ = 4000π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 2. Small volume = 12 cm³. Find large volume.', '48', '14', '24', '96', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 2³ = 8. Large V = 12 × 8 = 96 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 4. Small volume = 21 cm³. Find large volume.', '84', '25', '1344', '336', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 4³ = 64. Large V = 21 × 64 = 1344 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 18 cm. Find capacity in litres (in terms of π).', '23328π', '23328π/3000', '5832π/3', '23328π/3', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 23328π/3 cm³ = 23328π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Room 9×7×3 m. Find wall area to paint (4 walls only).', '63', '222', '96', '159', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Walls = 2(lh + wh) = 2(9×3 + 7×3) = 96 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 3, find the ratio of surface area to volume.', '6/3', '63', '3', '3/6', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 2. Small volume = 20 cm³. Find large volume.', '80', '22', '40', '160', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 2³ = 8. Large V = 20 × 8 = 160 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A sphere radius 6 cm is submerged. Find water displaced.', '144π', '864π/3', '864π', '216π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Water displaced = volume of sphere = (4/3)πr³ = 864π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 4. Small volume = 10 cm³. Find large volume.', '640', '40', '14', '160', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 4³ = 64. Large V = 10 × 64 = 640 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder (r=5, h=8) topped with cone (h=4). Find total volume.', '100π', '200π + 100π/3', '200π', '300π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = πr²h + ⅓πr²h = 200π + 100π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder (r=3, h=9) topped with cone (h=6). Find total volume.', '27π', '81π + 54π/3', '135π', '81π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = πr²h + ⅓πr²h = 81π + 54π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A sphere radius 4 cm is submerged. Find water displaced.', '256π', '256π/3', 'None of these', '64π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Water displaced = volume of sphere = (4/3)πr³ = 256π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 4. Small volume = 23 cm³. Find large volume.', '1472', '368', '92', '27', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 4³ = 64. Large V = 23 × 64 = 1472 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Room 9×5×3 m. Find wall area to paint (4 walls only).', '45', '129', '174', '84', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Walls = 2(lh + wh) = 2(9×3 + 5×3) = 84 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 4. Small volume = 47 cm³. Find large volume.', '3008', '752', '188', '51', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 4³ = 64. Large V = 47 × 64 = 3008 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Room 9×7×3 m. Find wall area to paint (4 walls only).', '159', '63', '222', '96', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Walls = 2(lh + wh) = 2(9×3 + 7×3) = 96 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 17 cm. Find capacity in litres (in terms of π).', '19652π/3', '19652π/3000', '4913π/3', '19652π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 19652π/3 cm³ = 19652π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 3. Small volume = 42 cm³. Find large volume.', '1134', '378', '45', '126', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 3³ = 27. Large V = 42 × 27 = 1134 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder (r=5, h=10) topped with cone (h=4). Find total volume.', '250π + 100π/3', '250π', '150π', '350π', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = πr²h + ⅓πr²h = 250π + 100π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 2. Small volume = 42 cm³. Find large volume.', '168', '336', '44', '84', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 2³ = 8. Large V = 42 × 8 = 336 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 20 cm. Find capacity in litres (in terms of π).', '32000π/3', '32000π', '8000π/3', '32000π/3000', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 32000π/3 cm³ = 32000π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 10 cm. Find capacity in litres (in terms of π).', '4000π/3', '4000π', '1000π/3', '4000π/3000', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 4000π/3 cm³ = 4000π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 6, find the ratio of surface area to volume.', 'None of these', '6/6', '66', '6', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Room 5×6×3 m. Find wall area to paint (4 walls only).', '96', '66', '30', '126', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Walls = 2(lh + wh) = 2(5×3 + 6×3) = 66 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 19 cm. Find capacity in litres (in terms of π).', '27436π/3000', '6859π/3', '27436π/3', '27436π', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 27436π/3 cm³ = 27436π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 4, find the ratio of surface area to volume.', '64', '4/6', '6/4', '4', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 4, find the ratio of surface area to volume.', '4', '4/6', '64', '6/4', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 3. Small volume = 24 cm³. Find large volume.', '27', '648', '72', '216', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 3³ = 27. Large V = 24 × 27 = 648 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 17 cm. Find capacity in litres (in terms of π).', '19652π/3000', '19652π', '4913π/3', '19652π/3', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 19652π/3 cm³ = 19652π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 4. Small volume = 12 cm³. Find large volume.', '48', '16', '768', '192', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 4³ = 64. Large V = 12 × 64 = 768 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 4, find the ratio of surface area to volume.', '4', '4/6', '64', '6/4', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder (r=5, h=12) topped with cone (h=6). Find total volume.', '450π', '300π + 150π/3', '300π', '150π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = πr²h + ⅓πr²h = 300π + 150π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 18 cm. Find capacity in litres (in terms of π).', '5832π/3', '23328π', '23328π/3000', '23328π/3', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 23328π/3 cm³ = 23328π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 4, find the ratio of surface area to volume.', '4/6', '4', '64', '6/4', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 4. Small volume = 36 cm³. Find large volume.', '40', '576', '144', '2304', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 4³ = 64. Large V = 36 × 64 = 2304 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Room 10×7×5 m. Find wall area to paint (4 walls only).', '70', '170', '310', '240', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Walls = 2(lh + wh) = 2(10×5 + 7×5) = 170 m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cylinder (r=3, h=9) topped with cone (h=6). Find total volume.', '27π', '81π', '81π + 54π/3', '135π', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = πr²h + ⅓πr²h = 81π + 54π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A sphere radius 6 cm is submerged. Find water displaced.', '864π/3', '144π', '216π', '864π', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Water displaced = volume of sphere = (4/3)πr³ = 864π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 6, find the ratio of surface area to volume.', '66', '6', 'None of these', '6/6', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 10 cm. Find capacity in litres (in terms of π).', '4000π', '1000π/3', '4000π/3', '4000π/3000', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 4000π/3 cm³ = 4000π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar solids have scale factor 2. Small volume = 33 cm³. Find large volume.', '132', '35', '264', '66', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Volume ratio = k³ = 2³ = 8. Large V = 33 × 8 = 264 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A sphere radius 6 cm is submerged. Find water displaced.', '144π', '864π/3', '864π', '216π', 1,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Water displaced = volume of sphere = (4/3)πr³ = 864π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Spherical tank radius 15 cm. Find capacity in litres (in terms of π).', '13500π/3000', '13500π', '13500π/3', '3375π/3', 0,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'V = (4/3)πr³ = 13500π/3 cm³ = 13500π/3000 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A sphere radius 4 cm is submerged. Find water displaced.', 'None of these', '64π', '256π/3', '256π', 2,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'Water displaced = volume of sphere = (4/3)πr³ = 256π/3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a cube with side 4, find the ratio of surface area to volume.', '64', '4', '4/6', '6/4', 3,
'lc_hl_measurement', 12, 'advanced', 'lc_hl', 'SA/V = 6s²/s³ = 6/s = 6/4', 1);