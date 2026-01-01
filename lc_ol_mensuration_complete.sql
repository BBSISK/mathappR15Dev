-- LC Ordinary Level - Mensuration Complete SQL
-- Generated: 2025-12-15
-- Total: 600 questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Mensuration topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_ol_mensuration', 'Measurement', id, '📏', 5, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_mensuration';

-- Insert questions
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 10 cm and width 11 cm.', '42 cm', '46 cm', '21 cm', '110 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(10 + 11) = 2 × 21 = 42 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 12 cm and width 3 cm.', '30 cm', '34 cm', '36 cm', '15 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(12 + 3) = 2 × 15 = 30 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 8 cm and width 15 cm.', '50 cm', '23 cm', '46 cm', '120 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(8 + 15) = 2 × 23 = 46 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 11 cm and width 6 cm.', '38 cm', '34 cm', '17 cm', '66 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(11 + 6) = 2 × 17 = 34 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 14 cm and width 10 cm.', '52 cm', '140 cm', '48 cm', '24 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(14 + 10) = 2 × 24 = 48 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 7 cm and width 10 cm.', '70 cm', '34 cm', '38 cm', '17 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(7 + 10) = 2 × 17 = 34 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 10 cm and width 11 cm.', '46 cm', '110 cm', '42 cm', '21 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(10 + 11) = 2 × 21 = 42 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 5 cm and width 8 cm.', '30 cm', '40 cm', '26 cm', '13 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(5 + 8) = 2 × 13 = 26 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 8 cm and width 9 cm.', '38 cm', '34 cm', '17 cm', '72 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(8 + 9) = 2 × 17 = 34 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 16 cm and width 12 cm.', '192 cm', '60 cm', '56 cm', '28 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(16 + 12) = 2 × 28 = 56 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 18 cm and width 7 cm.', '126 cm', '54 cm', '25 cm', '50 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(18 + 7) = 2 × 25 = 50 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 19 cm and width 10 cm.', '29 cm', '62 cm', '190 cm', '58 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(19 + 10) = 2 × 29 = 58 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 14 cm and width 9 cm.', '23 cm', '50 cm', '126 cm', '46 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(14 + 9) = 2 × 23 = 46 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 20 cm and width 5 cm.', '25 cm', '100 cm', '54 cm', '50 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(20 + 5) = 2 × 25 = 50 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 9 cm and width 3 cm.', '27 cm', '24 cm', '28 cm', '12 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(9 + 3) = 2 × 12 = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 19 cm and width 11 cm.', '64 cm', '30 cm', '60 cm', '209 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(19 + 11) = 2 × 30 = 60 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 19 cm and width 11 cm.', '64 cm', '60 cm', '30 cm', '209 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(19 + 11) = 2 × 30 = 60 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 16 cm and width 7 cm.', '23 cm', '46 cm', '112 cm', '50 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(16 + 7) = 2 × 23 = 46 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 9 cm and width 11 cm.', '44 cm', '40 cm', '20 cm', '99 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(9 + 11) = 2 × 20 = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a rectangle with length 6 cm and width 14 cm.', '40 cm', '20 cm', '44 cm', '84 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 2(l + w) = 2(6 + 14) = 2 × 20 = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 9 cm.', '45 cm', '18 cm', '36 cm', '81 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 9 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 5 cm.', 'Cannot determine', '10 cm', '20 cm', '25 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 5 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 4 cm.', '20 cm', '8 cm', '16 cm', 'Cannot determine', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 4 = 16 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 9 cm.', '36 cm', '81 cm', '45 cm', '18 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 9 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 9 cm.', '36 cm', '18 cm', '45 cm', '81 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 9 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 12 cm.', '60 cm', '24 cm', '144 cm', '48 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 12 = 48 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 10 cm.', '50 cm', '20 cm', '40 cm', '100 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 10 = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 9 cm.', '81 cm', '36 cm', '45 cm', '18 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 9 = 36 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 5 cm.', '20 cm', '10 cm', 'Cannot determine', '25 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 5 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 10 cm.', '50 cm', '40 cm', '20 cm', '100 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 10 = 40 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 4 cm.', '16 cm', '8 cm', 'Cannot determine', '20 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 4 = 16 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 5 cm.', '10 cm', 'Cannot determine', '25 cm', '20 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 5 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 7 cm.', '28 cm', '14 cm', '35 cm', '49 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 7 = 28 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 13 cm.', '26 cm', '169 cm', '65 cm', '52 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 13 = 52 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a square with side 12 cm.', '60 cm', '48 cm', '144 cm', '24 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 4 × side = 4 × 12 = 48 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 12 cm, 12 cm, and 21 cm.', '144 cm', '48 cm', '45 cm', '22 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 12 + 12 + 21 = 45 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 11 cm, 9 cm, and 13 cm.', '36 cm', '16 cm', '99 cm', '33 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 11 + 9 + 13 = 33 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 7 cm, 5 cm, and 11 cm.', '11 cm', '26 cm', '23 cm', '35 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 7 + 5 + 11 = 23 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 7 cm, 7 cm, and 6 cm.', '49 cm', '23 cm', '20 cm', '10 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 7 + 7 + 6 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 10 cm, 8 cm, and 6 cm.', '24 cm', '12 cm', '80 cm', '27 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 10 + 8 + 6 = 24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 12 cm, 10 cm, and 15 cm.', '120 cm', '40 cm', '18 cm', '37 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 12 + 10 + 15 = 37 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 11 cm, 7 cm, and 5 cm.', '23 cm', '11 cm', '77 cm', '26 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 11 + 7 + 5 = 23 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 11 cm, 10 cm, and 9 cm.', '15 cm', '110 cm', '30 cm', '33 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 11 + 10 + 9 = 30 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 7 cm, 10 cm, and 5 cm.', '70 cm', '22 cm', '11 cm', '25 cm', 1,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 7 + 10 + 5 = 22 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 7 cm, 8 cm, and 8 cm.', '11 cm', '56 cm', '26 cm', '23 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 7 + 8 + 8 = 23 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 8 cm, 8 cm, and 9 cm.', '25 cm', '64 cm', '28 cm', '12 cm', 0,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 8 + 8 + 9 = 25 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 6 cm, 9 cm, and 13 cm.', '54 cm', '14 cm', '28 cm', '31 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 6 + 9 + 13 = 28 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 9 cm, 9 cm, and 4 cm.', '81 cm', '25 cm', '11 cm', '22 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 9 + 9 + 4 = 22 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 11 cm, 7 cm, and 15 cm.', '77 cm', '36 cm', '33 cm', '16 cm', 2,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 11 + 7 + 15 = 33 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perimeter of a triangle with sides 6 cm, 9 cm, and 11 cm.', '29 cm', '54 cm', '13 cm', '26 cm', 3,
'lc_ol_mensuration', 1, 'foundation', 'lc_ol', 'Perimeter = 6 + 9 + 11 = 26 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 6 cm and width 12 cm.', '72 cm²', '36 cm²', '18 cm²', '78 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 6 × 12 = 72 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 7 cm and width 11 cm.', '77 cm²', '84 cm²', '18 cm²', '36 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 7 × 11 = 77 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 11 cm and width 6 cm.', '34 cm²', '66 cm²', '17 cm²', '77 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 11 × 6 = 66 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 8 cm and width 11 cm.', '19 cm²', '88 cm²', '38 cm²', '96 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 8 × 11 = 88 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 12 cm and width 8 cm.', '40 cm²', '96 cm²', '108 cm²', '20 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 12 × 8 = 96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 7 cm and width 6 cm.', '13 cm²', '26 cm²', '42 cm²', '49 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 7 × 6 = 42 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 5 cm and width 4 cm.', '20 cm²', '9 cm²', '18 cm²', '25 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 5 × 4 = 20 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 6 cm and width 5 cm.', '11 cm²', '30 cm²', '36 cm²', '22 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 6 × 5 = 30 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 11 cm and width 4 cm.', '15 cm²', '44 cm²', '30 cm²', '55 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 11 × 4 = 44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 11 cm and width 12 cm.', '143 cm²', '132 cm²', '23 cm²', '46 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 11 × 12 = 132 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 6 cm and width 6 cm.', '24 cm²', '42 cm²', '12 cm²', '36 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 6 × 6 = 36 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 5 cm and width 7 cm.', '12 cm²', '40 cm²', '24 cm²', '35 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 5 × 7 = 35 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 7 cm and width 3 cm.', '20 cm²', '28 cm²', '10 cm²', '21 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 7 × 3 = 21 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 11 cm and width 6 cm.', '66 cm²', '17 cm²', '34 cm²', '77 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 11 × 6 = 66 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 14 cm and width 3 cm.', '56 cm²', '34 cm²', '17 cm²', '42 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 14 × 3 = 42 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 13 cm and width 5 cm.', '36 cm²', '65 cm²', '78 cm²', '18 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 13 × 5 = 65 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 14 cm and width 4 cm.', '70 cm²', '18 cm²', '36 cm²', '56 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 14 × 4 = 56 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 6 cm and width 11 cm.', '72 cm²', '66 cm²', '17 cm²', '34 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 6 × 11 = 66 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 11 cm and width 8 cm.', '38 cm²', '19 cm²', '88 cm²', '99 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 11 × 8 = 88 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a rectangle with length 13 cm and width 8 cm.', '21 cm²', '42 cm²', '104 cm²', '117 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = length × width = 13 × 8 = 104 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 11 cm and height 14 cm.', '88.0 cm²', '25 cm²', '77.0 cm²', '154 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 11 × 14 = 77.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 12 cm and height 5 cm.', '17 cm²', '60 cm²', '30.0 cm²', '42.0 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 12 × 5 = 30.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 7 cm and height 4 cm.', '21.0 cm²', '28 cm²', '14.0 cm²', '11 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 7 × 4 = 14.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 14 cm and height 6 cm.', '42.0 cm²', '56.0 cm²', '20 cm²', '84 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 14 × 6 = 42.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 11 cm and height 8 cm.', '44.0 cm²', '55.0 cm²', '88 cm²', '19 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 11 × 8 = 44.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 13 cm and height 12 cm.', '156 cm²', '78.0 cm²', '91.0 cm²', '25 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 13 × 12 = 78.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 11 cm and height 6 cm.', '17 cm²', '33.0 cm²', '66 cm²', '44.0 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 11 × 6 = 33.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 9 cm and height 7 cm.', '31.5 cm²', '63 cm²', '40.5 cm²', '16 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 9 × 7 = 31.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 7 cm and height 6 cm.', '28.0 cm²', '42 cm²', '13 cm²', '21.0 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 7 × 6 = 21.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 9 cm and height 9 cm.', '40.5 cm²', '81 cm²', '18 cm²', '49.5 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 9 × 9 = 40.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 6 cm and height 9 cm.', '15 cm²', '54 cm²', '33.0 cm²', '27.0 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 6 × 9 = 27.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 9 cm and height 8 cm.', '45.0 cm²', '17 cm²', '72 cm²', '36.0 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 9 × 8 = 36.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 12 cm and height 10 cm.', '60.0 cm²', '72.0 cm²', '120 cm²', '22 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 12 × 10 = 60.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 14 cm and height 5 cm.', '70 cm²', '19 cm²', '35.0 cm²', '49.0 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 14 × 5 = 35.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 6 cm and height 8 cm.', '14 cm²', '48 cm²', '24.0 cm²', '30.0 cm²', 2,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 6 × 8 = 24.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 14 cm and height 10 cm.', '140 cm²', '24 cm²', '84.0 cm²', '70.0 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 14 × 10 = 70.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 11 cm and height 7 cm.', '49.5 cm²', '38.5 cm²', '77 cm²', '18 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 11 × 7 = 38.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 14 cm and height 7 cm.', '49.0 cm²', '21 cm²', '98 cm²', '63.0 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 14 × 7 = 49.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 8 cm and height 6 cm.', '14 cm²', '24.0 cm²', '48 cm²', '32.0 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 8 × 6 = 24.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with base 11 cm and height 10 cm.', '55.0 cm²', '21 cm²', '66.0 cm²', '110 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = ½ × base × height = ½ × 11 × 10 = 55.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 8 cm.', '72 cm²', '64 cm²', '16 cm²', '32 cm²', 1,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 8² = 64 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 14 cm.', '210 cm²', '56 cm²', '28 cm²', '196 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 14² = 196 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 13 cm.', '169 cm²', '52 cm²', '26 cm²', '182 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 13² = 169 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 5 cm.', '25 cm²', '20 cm²', '10 cm²', '30 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 5² = 25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 13 cm.', '52 cm²', '26 cm²', '182 cm²', '169 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 13² = 169 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 9 cm.', '90 cm²', '36 cm²', '18 cm²', '81 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 9² = 81 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 14 cm.', '210 cm²', '28 cm²', '56 cm²', '196 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 14² = 196 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 7 cm.', '49 cm²', '56 cm²', '28 cm²', '14 cm²', 0,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 7² = 49 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 12 cm.', '48 cm²', '24 cm²', '156 cm²', '144 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 12² = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a square with side 7 cm.', '56 cm²', '14 cm²', '28 cm²', '49 cm²', 3,
'lc_ol_mensuration', 2, 'foundation', 'lc_ol', 'Area = side² = 7² = 49 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 3 cm. (Use π = 3.14)', '18.84 cm²', '38.26 cm²', '9.42 cm²', '28.26 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 3² = 3.14 × 9 = 28.26 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 7 cm. (Use π = 3.14)', '21.98 cm²', '163.86 cm²', '43.96 cm²', '153.86 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 7² = 3.14 × 49 = 153.86 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 10 cm. (Use π = 3.14)', '314.0 cm²', '62.8 cm²', '324.0 cm²', '31.4 cm²', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 10² = 3.14 × 100 = 314.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 9 cm. (Use π = 3.14)', '264.34 cm²', '254.34 cm²', '56.52 cm²', '28.26 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 9² = 3.14 × 81 = 254.34 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 5 cm. (Use π = 3.14)', '88.5 cm²', '31.4 cm²', '15.7 cm²', '78.5 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 5² = 3.14 × 25 = 78.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 9 cm. (Use π = 3.14)', '264.34 cm²', '254.34 cm²', '28.26 cm²', '56.52 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 9² = 3.14 × 81 = 254.34 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 3 cm. (Use π = 3.14)', '28.26 cm²', '9.42 cm²', '18.84 cm²', '38.26 cm²', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 3² = 3.14 × 9 = 28.26 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 4 cm. (Use π = 3.14)', '60.24 cm²', '50.24 cm²', '25.12 cm²', '12.56 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 4² = 3.14 × 16 = 50.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 10 cm. (Use π = 3.14)', '62.8 cm²', '314.0 cm²', '324.0 cm²', '31.4 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 10² = 3.14 × 100 = 314.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 8 cm. (Use π = 3.14)', '50.24 cm²', '210.96 cm²', '200.96 cm²', '25.12 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 8² = 3.14 × 64 = 200.96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 5 cm. (Use π = 3.14)', '15.7 cm²', '31.4 cm²', '78.5 cm²', '88.5 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 5² = 3.14 × 25 = 78.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 3 cm. (Use π = 3.14)', '38.26 cm²', '18.84 cm²', '28.26 cm²', '9.42 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 3² = 3.14 × 9 = 28.26 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 4 cm. (Use π = 3.14)', '25.12 cm²', '12.56 cm²', '60.24 cm²', '50.24 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 4² = 3.14 × 16 = 50.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 5 cm. (Use π = 3.14)', '88.5 cm²', '15.7 cm²', '78.5 cm²', '31.4 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 5² = 3.14 × 25 = 78.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 3 cm. (Use π = 3.14)', '38.26 cm²', '28.26 cm²', '18.84 cm²', '9.42 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 3² = 3.14 × 9 = 28.26 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 9 cm. (Use π = 3.14)', '28.26 cm²', '264.34 cm²', '254.34 cm²', '56.52 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 9² = 3.14 × 81 = 254.34 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 4 cm. (Use π = 3.14)', '50.24 cm²', '60.24 cm²', '25.12 cm²', '12.56 cm²', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 4² = 3.14 × 16 = 50.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 6 cm. (Use π = 3.14)', '113.04 cm²', '37.68 cm²', '18.84 cm²', '123.04 cm²', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 6² = 3.14 × 36 = 113.04 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 5 cm. (Use π = 3.14)', '15.7 cm²', '78.5 cm²', '31.4 cm²', '88.5 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 5² = 3.14 × 25 = 78.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a circle with radius 4 cm. (Use π = 3.14)', '12.56 cm²', '50.24 cm²', '25.12 cm²', '60.24 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Area = πr² = 3.14 × 4² = 3.14 × 16 = 50.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 10 cm. (Use π = 3.14)', '314.0 cm', '62.8 cm', '67.8 cm', '31.4 cm', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 10 = 62.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 10 cm. (Use π = 3.14)', '67.8 cm', '62.8 cm', '314.0 cm', '31.4 cm', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 10 = 62.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 4 cm. (Use π = 3.14)', '50.24 cm', '30.12 cm', '25.12 cm', '12.56 cm', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 4 = 25.12 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 8 cm. (Use π = 3.14)', '55.24 cm', '50.24 cm', '200.96 cm', '25.12 cm', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 8 = 50.24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 6 cm. (Use π = 3.14)', '42.68 cm', '113.04 cm', '18.84 cm', '37.68 cm', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 6 = 37.68 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 8 cm. (Use π = 3.14)', '50.24 cm', '200.96 cm', '55.24 cm', '25.12 cm', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 8 = 50.24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 3 cm. (Use π = 3.14)', '23.84 cm', '18.84 cm', '9.42 cm', '28.26 cm', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 3 = 18.84 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 3 cm. (Use π = 3.14)', '23.84 cm', '9.42 cm', '18.84 cm', '28.26 cm', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 3 = 18.84 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 9 cm. (Use π = 3.14)', '61.52 cm', '56.52 cm', '254.34 cm', '28.26 cm', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 9 = 56.52 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 8 cm. (Use π = 3.14)', '55.24 cm', '200.96 cm', '50.24 cm', '25.12 cm', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 8 = 50.24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 7 cm. (Use π = 3.14)', '48.96 cm', '43.96 cm', '21.98 cm', '153.86 cm', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 7 = 43.96 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 6 cm. (Use π = 3.14)', '113.04 cm', '42.68 cm', '18.84 cm', '37.68 cm', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 6 = 37.68 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 5 cm. (Use π = 3.14)', '36.4 cm', '15.7 cm', '31.4 cm', '78.5 cm', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 5 = 31.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 8 cm. (Use π = 3.14)', '50.24 cm', '200.96 cm', '55.24 cm', '25.12 cm', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 8 = 50.24 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumference of a circle with radius 3 cm. (Use π = 3.14)', '28.26 cm', '9.42 cm', '18.84 cm', '23.84 cm', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Circumference = 2πr = 2 × 3.14 × 3 = 18.84 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 10 cm and angle 180°. (Use π = 3.14)', 'Cannot determine', '157.0 cm²', '167.0 cm²', '314.0 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (180/360) × 3.14 × 10² = 157.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 10 cm and angle 45°. (Use π = 3.14)', '39.25 cm²', '78.5 cm²', '49.25 cm²', '314.0 cm²', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (45/360) × 3.14 × 10² = 39.25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 4 cm and angle 60°. (Use π = 3.14)', '50.24 cm²', '16.75 cm²', '12.37 cm²', '8.37 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (60/360) × 3.14 × 4² = 8.37 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 10 cm and angle 120°. (Use π = 3.14)', '209.33 cm²', '114.67 cm²', '104.67 cm²', '314.0 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (120/360) × 3.14 × 10² = 104.67 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 9 cm and angle 45°. (Use π = 3.14)', '63.58 cm²', '40.79 cm²', '254.34 cm²', '31.79 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (45/360) × 3.14 × 9² = 31.79 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 9 cm and angle 60°. (Use π = 3.14)', '254.34 cm²', '51.39 cm²', '42.39 cm²', '84.78 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (60/360) × 3.14 × 9² = 42.39 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 8 cm and angle 120°. (Use π = 3.14)', '74.99 cm²', '66.99 cm²', '133.97 cm²', '200.96 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (120/360) × 3.14 × 8² = 66.99 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 9 cm and angle 180°. (Use π = 3.14)', 'Cannot determine', '136.17 cm²', '254.34 cm²', '127.17 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (180/360) × 3.14 × 9² = 127.17 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 8 cm and angle 90°. (Use π = 3.14)', '50.24 cm²', '100.48 cm²', '58.24 cm²', '200.96 cm²', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (90/360) × 3.14 × 8² = 50.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 9 cm and angle 45°. (Use π = 3.14)', '254.34 cm²', '63.58 cm²', '31.79 cm²', '40.79 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (45/360) × 3.14 × 9² = 31.79 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 10 cm and angle 60°. (Use π = 3.14)', '62.33 cm²', '314.0 cm²', '104.67 cm²', '52.33 cm²', 3,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (60/360) × 3.14 × 10² = 52.33 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 6 cm and angle 60°. (Use π = 3.14)', '37.68 cm²', '18.84 cm²', '113.04 cm²', '24.84 cm²', 1,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (60/360) × 3.14 × 6² = 18.84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 5 cm and angle 90°. (Use π = 3.14)', '78.5 cm²', '24.62 cm²', '19.62 cm²', '39.25 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (90/360) × 3.14 × 5² = 19.62 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 7 cm and angle 180°. (Use π = 3.14)', '76.93 cm²', '83.93 cm²', '153.86 cm²', 'Cannot determine', 0,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (180/360) × 3.14 × 7² = 76.93 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 7 cm and angle 90°. (Use π = 3.14)', '45.47 cm²', '76.93 cm²', '38.47 cm²', '153.86 cm²', 2,
'lc_ol_mensuration', 3, 'foundation', 'lc_ol', 'Sector area = (θ/360) × πr² = (90/360) × 3.14 × 7² = 38.47 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (11×5 cm) with a triangle (base 11 cm, height 3 cm) on top. Find the total area.', '58 cm²', '76.5 cm²', '71.5 cm²', '55 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 55 cm². Triangle = 16.5 cm². Total = 71.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (9×8 cm) with a triangle (base 9 cm, height 3 cm) on top. Find the total area.', '75 cm²', '85.5 cm²', '93.5 cm²', '72 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 72 cm². Triangle = 13.5 cm². Total = 85.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (8×8 cm) with a triangle (base 8 cm, height 5 cm) on top. Find the total area.', '69 cm²', '84.0 cm²', '64 cm²', '92.0 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 64 cm². Triangle = 20.0 cm². Total = 84.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (15×5 cm) with a triangle (base 15 cm, height 4 cm) on top. Find the total area.', '79 cm²', '110.0 cm²', '105.0 cm²', '75 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 75 cm². Triangle = 30.0 cm². Total = 105.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (9×9 cm) with a triangle (base 9 cm, height 6 cm) on top. Find the total area.', '87 cm²', '117.0 cm²', '108.0 cm²', '81 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 81 cm². Triangle = 27.0 cm². Total = 108.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (14×9 cm) with a triangle (base 14 cm, height 5 cm) on top. Find the total area.', '131 cm²', '170.0 cm²', '126 cm²', '161.0 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 126 cm². Triangle = 35.0 cm². Total = 161.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (12×7 cm) with a triangle (base 12 cm, height 4 cm) on top. Find the total area.', '84 cm²', '115.0 cm²', '88 cm²', '108.0 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 84 cm². Triangle = 24.0 cm². Total = 108.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (15×5 cm) with a triangle (base 15 cm, height 6 cm) on top. Find the total area.', '125.0 cm²', '120.0 cm²', '75 cm²', '81 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 75 cm². Triangle = 45.0 cm². Total = 120.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (10×5 cm) with a triangle (base 10 cm, height 7 cm) on top. Find the total area.', '85.0 cm²', '57 cm²', '90.0 cm²', '50 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 50 cm². Triangle = 35.0 cm². Total = 85.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (12×5 cm) with a triangle (base 12 cm, height 3 cm) on top. Find the total area.', '63 cm²', '60 cm²', '78.0 cm²', '83.0 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 60 cm². Triangle = 18.0 cm². Total = 78.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (12×6 cm) with a triangle (base 12 cm, height 5 cm) on top. Find the total area.', '102.0 cm²', '77 cm²', '72 cm²', '108.0 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 72 cm². Triangle = 30.0 cm². Total = 102.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (13×10 cm) with a triangle (base 13 cm, height 6 cm) on top. Find the total area.', '179.0 cm²', '136 cm²', '169.0 cm²', '130 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 130 cm². Triangle = 39.0 cm². Total = 169.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (11×5 cm) with a triangle (base 11 cm, height 6 cm) on top. Find the total area.', '93.0 cm²', '88.0 cm²', '55 cm²', '61 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 55 cm². Triangle = 33.0 cm². Total = 88.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (15×10 cm) with a triangle (base 15 cm, height 4 cm) on top. Find the total area.', '150 cm²', '190.0 cm²', '180.0 cm²', '154 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 150 cm². Triangle = 30.0 cm². Total = 180.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (13×7 cm) with a triangle (base 13 cm, height 5 cm) on top. Find the total area.', '130.5 cm²', '96 cm²', '123.5 cm²', '91 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 91 cm². Triangle = 32.5 cm². Total = 123.5 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (9×6 cm) with a triangle (base 9 cm, height 4 cm) on top. Find the total area.', '58 cm²', '72.0 cm²', '78.0 cm²', '54 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 54 cm². Triangle = 18.0 cm². Total = 72.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (11×6 cm) with a triangle (base 11 cm, height 6 cm) on top. Find the total area.', '66 cm²', '72 cm²', '105.0 cm²', '99.0 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 66 cm². Triangle = 33.0 cm². Total = 99.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (10×10 cm) with a triangle (base 10 cm, height 3 cm) on top. Find the total area.', '103 cm²', '100 cm²', '125.0 cm²', '115.0 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 100 cm². Triangle = 15.0 cm². Total = 115.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (13×5 cm) with a triangle (base 13 cm, height 4 cm) on top. Find the total area.', '96.0 cm²', '65 cm²', '91.0 cm²', '69 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 65 cm². Triangle = 26.0 cm². Total = 91.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shape consists of a rectangle (14×9 cm) with a triangle (base 14 cm, height 4 cm) on top. Find the total area.', '163.0 cm²', '130 cm²', '154.0 cm²', '126 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 126 cm². Triangle = 28.0 cm². Total = 154.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (13×7 cm) has a semicircle (diameter 7 cm) attached. Find total area. (π = 3.14)', '91 cm²', '120.23 cm²', '110.23 cm²', '129.47 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 91. Semicircle = ½πr² = 19.23. Total = 110.23 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (14×6 cm) has a semicircle (diameter 6 cm) attached. Find total area. (π = 3.14)', '108.13 cm²', '112.26 cm²', '84 cm²', '98.13 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 84. Semicircle = ½πr² = 14.13. Total = 98.13 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (11×10 cm) has a semicircle (diameter 10 cm) attached. Find total area. (π = 3.14)', '188.5 cm²', '149.25 cm²', '159.25 cm²', '110 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 110. Semicircle = ½πr² = 39.25. Total = 149.25 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (12×6 cm) has a semicircle (diameter 6 cm) attached. Find total area. (π = 3.14)', '86.13 cm²', '96.13 cm²', '72 cm²', '100.26 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 72. Semicircle = ½πr² = 14.13. Total = 86.13 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (14×9 cm) has a semicircle (diameter 9 cm) attached. Find total area. (π = 3.14)', '157.79 cm²', '189.59 cm²', '167.79 cm²', '126 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 126. Semicircle = ½πr² = 31.79. Total = 157.79 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (15×7 cm) has a semicircle (diameter 7 cm) attached. Find total area. (π = 3.14)', '134.23 cm²', '124.23 cm²', '105 cm²', '143.47 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 105. Semicircle = ½πr² = 19.23. Total = 124.23 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (14×6 cm) has a semicircle (diameter 6 cm) attached. Find total area. (π = 3.14)', '108.13 cm²', '112.26 cm²', '98.13 cm²', '84 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 84. Semicircle = ½πr² = 14.13. Total = 98.13 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (16×7 cm) has a semicircle (diameter 7 cm) attached. Find total area. (π = 3.14)', '112 cm²', '150.47 cm²', '131.23 cm²', '141.23 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 112. Semicircle = ½πr² = 19.23. Total = 131.23 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (10×7 cm) has a semicircle (diameter 7 cm) attached. Find total area. (π = 3.14)', '108.47 cm²', '70 cm²', '89.23 cm²', '99.23 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 70. Semicircle = ½πr² = 19.23. Total = 89.23 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (10×6 cm) has a semicircle (diameter 6 cm) attached. Find total area. (π = 3.14)', '84.13 cm²', '60 cm²', '88.26 cm²', '74.13 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 60. Semicircle = ½πr² = 14.13. Total = 74.13 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (13×7 cm) has a semicircle (diameter 7 cm) attached. Find total area. (π = 3.14)', '110.23 cm²', '129.47 cm²', '91 cm²', '120.23 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 91. Semicircle = ½πr² = 19.23. Total = 110.23 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (12×8 cm) has a semicircle (diameter 8 cm) attached. Find total area. (π = 3.14)', '96 cm²', '146.24 cm²', '121.12 cm²', '131.12 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 96. Semicircle = ½πr² = 25.12. Total = 121.12 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (11×8 cm) has a semicircle (diameter 8 cm) attached. Find total area. (π = 3.14)', '123.12 cm²', '88 cm²', '138.24 cm²', '113.12 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 88. Semicircle = ½πr² = 25.12. Total = 113.12 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (12×7 cm) has a semicircle (diameter 7 cm) attached. Find total area. (π = 3.14)', '84 cm²', '122.47 cm²', '103.23 cm²', '113.23 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 84. Semicircle = ½πr² = 19.23. Total = 103.23 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle (16×7 cm) has a semicircle (diameter 7 cm) attached. Find total area. (π = 3.14)', '131.23 cm²', '150.47 cm²', '141.23 cm²', '112 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Rectangle = 112. Semicircle = ½πr² = 19.23. Total = 131.23 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (14×14 cm) has a smaller square (3×3 cm) cut from its center. Find the remaining area.', '196 cm²', '205 cm²', '9 cm²', '187 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 196 - 9 = 187 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (15×15 cm) has a smaller square (4×4 cm) cut from its center. Find the remaining area.', '16 cm²', '209 cm²', '225 cm²', '241 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 225 - 16 = 209 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (11×11 cm) has a smaller square (4×4 cm) cut from its center. Find the remaining area.', '137 cm²', '16 cm²', '121 cm²', '105 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 121 - 16 = 105 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (12×12 cm) has a smaller square (7×7 cm) cut from its center. Find the remaining area.', '193 cm²', '144 cm²', '95 cm²', '49 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 144 - 49 = 95 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (10×10 cm) has a smaller square (6×6 cm) cut from its center. Find the remaining area.', '36 cm²', '100 cm²', '64 cm²', '136 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 100 - 36 = 64 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (16×16 cm) has a smaller square (9×9 cm) cut from its center. Find the remaining area.', '81 cm²', '256 cm²', '337 cm²', '175 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 256 - 81 = 175 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (16×16 cm) has a smaller square (3×3 cm) cut from its center. Find the remaining area.', '247 cm²', '265 cm²', '9 cm²', '256 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 256 - 9 = 247 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (11×11 cm) has a smaller square (7×7 cm) cut from its center. Find the remaining area.', '49 cm²', '170 cm²', '72 cm²', '121 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 121 - 49 = 72 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (10×10 cm) has a smaller square (4×4 cm) cut from its center. Find the remaining area.', '100 cm²', '16 cm²', '116 cm²', '84 cm²', 3,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 100 - 16 = 84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (13×13 cm) has a smaller square (7×7 cm) cut from its center. Find the remaining area.', '120 cm²', '218 cm²', '49 cm²', '169 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 169 - 49 = 120 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (15×15 cm) has a smaller square (11×11 cm) cut from its center. Find the remaining area.', '104 cm²', '225 cm²', '346 cm²', '121 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 225 - 121 = 104 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (15×15 cm) has a smaller square (10×10 cm) cut from its center. Find the remaining area.', '100 cm²', '225 cm²', '125 cm²', '325 cm²', 2,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 225 - 100 = 125 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (13×13 cm) has a smaller square (4×4 cm) cut from its center. Find the remaining area.', '169 cm²', '153 cm²', '16 cm²', '185 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 169 - 16 = 153 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (14×14 cm) has a smaller square (6×6 cm) cut from its center. Find the remaining area.', '160 cm²', '36 cm²', '232 cm²', '196 cm²', 0,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 196 - 36 = 160 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A square (15×15 cm) has a smaller square (11×11 cm) cut from its center. Find the remaining area.', '346 cm²', '104 cm²', '225 cm²', '121 cm²', 1,
'lc_ol_mensuration', 4, 'developing', 'lc_ol', 'Remaining = 225 - 121 = 104 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 11 cm × 9 cm × 4 cm.', '179 cm²', '457 cm²', '358 cm²', '396 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(11×9 + 11×4 + 9×4) = 2(99 + 44 + 36) = 358 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 9 cm × 6 cm × 6 cm.', '144 cm²', '342 cm²', '324 cm²', '288 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(9×6 + 9×6 + 6×6) = 2(54 + 54 + 36) = 288 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 11 cm × 6 cm × 6 cm.', '336 cm²', '168 cm²', '396 cm²', '402 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(11×6 + 11×6 + 6×6) = 2(66 + 66 + 36) = 336 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 6 cm × 7 cm × 8 cm.', '336 cm²', '146 cm²', '292 cm²', '334 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(6×7 + 6×8 + 7×8) = 2(42 + 48 + 56) = 292 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 10 cm × 10 cm × 3 cm.', '420 cm²', '320 cm²', '160 cm²', '300 cm²', 1,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(10×10 + 10×3 + 10×3) = 2(100 + 30 + 30) = 320 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 12 cm × 5 cm × 8 cm.', '452 cm²', '480 cm²', '196 cm²', '392 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(12×5 + 12×8 + 5×8) = 2(60 + 96 + 40) = 392 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 4 cm × 3 cm × 4 cm.', '92 cm²', '40 cm²', '48 cm²', '80 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(4×3 + 4×4 + 3×4) = 2(12 + 16 + 12) = 80 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 8 cm × 10 cm × 7 cm.', '206 cm²', '492 cm²', '560 cm²', '412 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(8×10 + 8×7 + 10×7) = 2(80 + 56 + 70) = 412 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 12 cm × 5 cm × 7 cm.', '420 cm²', '418 cm²', '179 cm²', '358 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(12×5 + 12×7 + 5×7) = 2(60 + 84 + 35) = 358 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 7 cm × 5 cm × 3 cm.', '142 cm²', '177 cm²', '71 cm²', '105 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(7×5 + 7×3 + 5×3) = 2(35 + 21 + 15) = 142 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 6 cm × 6 cm × 5 cm.', '228 cm²', '96 cm²', '192 cm²', '180 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(6×6 + 6×5 + 6×5) = 2(36 + 30 + 30) = 192 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 9 cm × 4 cm × 4 cm.', '88 cm²', '144 cm²', '212 cm²', '176 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(9×4 + 9×4 + 4×4) = 2(36 + 36 + 16) = 176 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 8 cm × 7 cm × 5 cm.', '131 cm²', '318 cm²', '280 cm²', '262 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(8×7 + 8×5 + 7×5) = 2(56 + 40 + 35) = 262 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 7 cm × 7 cm × 5 cm.', '245 cm²', '287 cm²', '238 cm²', '119 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(7×7 + 7×5 + 7×5) = 2(49 + 35 + 35) = 238 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 8 cm × 5 cm × 6 cm.', '276 cm²', '240 cm²', '236 cm²', '118 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(8×5 + 8×6 + 5×6) = 2(40 + 48 + 30) = 236 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 8 cm × 8 cm × 5 cm.', '144 cm²', '352 cm²', '288 cm²', '320 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(8×8 + 8×5 + 8×5) = 2(64 + 40 + 40) = 288 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 5 cm × 6 cm × 8 cm.', '266 cm²', '240 cm²', '236 cm²', '118 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(5×6 + 5×8 + 6×8) = 2(30 + 40 + 48) = 236 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 8 cm × 10 cm × 3 cm.', '134 cm²', '348 cm²', '268 cm²', '240 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(8×10 + 8×3 + 10×3) = 2(80 + 24 + 30) = 268 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 11 cm × 5 cm × 2 cm.', '110 cm²', '229 cm²', '174 cm²', '87 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(11×5 + 11×2 + 5×2) = 2(55 + 22 + 10) = 174 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 10 cm × 6 cm × 3 cm.', '180 cm²', '108 cm²', '216 cm²', '276 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(10×6 + 10×3 + 6×3) = 2(60 + 30 + 18) = 216 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 9 cm × 5 cm × 5 cm.', '275 cm²', '225 cm²', '115 cm²', '230 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(9×5 + 9×5 + 5×5) = 2(45 + 45 + 25) = 230 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 4 cm × 10 cm × 5 cm.', '110 cm²', '260 cm²', '200 cm²', '220 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(4×10 + 4×5 + 10×5) = 2(40 + 20 + 50) = 220 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 11 cm × 7 cm × 7 cm.', '406 cm²', '539 cm²', '483 cm²', '203 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(11×7 + 11×7 + 7×7) = 2(77 + 77 + 49) = 406 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 12 cm × 7 cm × 4 cm.', '160 cm²', '336 cm²', '320 cm²', '404 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(12×7 + 12×4 + 7×4) = 2(84 + 48 + 28) = 320 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 9 cm × 6 cm × 3 cm.', '99 cm²', '252 cm²', '198 cm²', '162 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(9×6 + 9×3 + 6×3) = 2(54 + 27 + 18) = 198 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 10 cm × 5 cm × 3 cm.', '240 cm²', '150 cm²', '95 cm²', '190 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(10×5 + 10×3 + 5×3) = 2(50 + 30 + 15) = 190 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 5 cm × 5 cm × 3 cm.', '110 cm²', '75 cm²', '135 cm²', '55 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(5×5 + 5×3 + 5×3) = 2(25 + 15 + 15) = 110 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 11 cm × 6 cm × 7 cm.', '436 cm²', '462 cm²', '185 cm²', '370 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(11×6 + 11×7 + 6×7) = 2(66 + 77 + 42) = 370 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 5 cm × 5 cm × 2 cm.', '90 cm²', '45 cm²', '115 cm²', '50 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(5×5 + 5×2 + 5×2) = 2(25 + 10 + 10) = 90 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cuboid with dimensions 11 cm × 8 cm × 3 cm.', '145 cm²', '264 cm²', '290 cm²', '378 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 2(lw + lh + wh) = 2(11×8 + 11×3 + 8×3) = 2(88 + 33 + 24) = 290 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 5 cm.', '150 cm²', '25 cm²', '125 cm²', '100 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 5² = 6 × 25 = 150 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 3 cm.', '54 cm²', '36 cm²', '27 cm²', '9 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 3² = 6 × 9 = 54 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 7 cm.', '343 cm²', '294 cm²', '49 cm²', '196 cm²', 1,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 7² = 6 × 49 = 294 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 11 cm.', '484 cm²', '726 cm²', '121 cm²', '1331 cm²', 1,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 11² = 6 × 121 = 726 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 9 cm.', '729 cm²', '486 cm²', '81 cm²', '324 cm²', 1,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 9² = 6 × 81 = 486 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 11 cm.', '726 cm²', '121 cm²', '1331 cm²', '484 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 11² = 6 × 121 = 726 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 10 cm.', '1000 cm²', '600 cm²', '100 cm²', '400 cm²', 1,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 10² = 6 × 100 = 600 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 10 cm.', '100 cm²', '600 cm²', '400 cm²', '1000 cm²', 1,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 10² = 6 × 100 = 600 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 11 cm.', '1331 cm²', '121 cm²', '484 cm²', '726 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 11² = 6 × 121 = 726 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 12 cm.', '864 cm²', '1728 cm²', '144 cm²', '576 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 12² = 6 × 144 = 864 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 7 cm.', '49 cm²', '343 cm²', '294 cm²', '196 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 7² = 6 × 49 = 294 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 4 cm.', 'Cannot determine', '96 cm²', '16 cm²', '64 cm²', 1,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 4² = 6 × 16 = 96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 9 cm.', '486 cm²', '324 cm²', '729 cm²', '81 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 9² = 6 × 81 = 486 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 7 cm.', '343 cm²', '196 cm²', '294 cm²', '49 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 7² = 6 × 49 = 294 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 12 cm.', '864 cm²', '576 cm²', '144 cm²', '1728 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 12² = 6 × 144 = 864 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 6 cm.', '216 cm²', '36 cm²', '144 cm²', 'Cannot determine', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 6² = 6 × 36 = 216 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 6 cm.', '36 cm²', 'Cannot determine', '144 cm²', '216 cm²', 3,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 6² = 6 × 36 = 216 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 7 cm.', '294 cm²', '49 cm²', '196 cm²', '343 cm²', 0,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 7² = 6 × 49 = 294 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 3 cm.', '36 cm²', '9 cm²', '54 cm²', '27 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 3² = 6 × 9 = 54 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a cube with side 8 cm.', '64 cm²', '512 cm²', '384 cm²', '256 cm²', 2,
'lc_ol_mensuration', 5, 'developing', 'lc_ol', 'SA = 6s² = 6 × 8² = 6 × 64 = 384 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 8 cm and height 8 cm. (π = 3.14)', '200.96 cm²', '401.92 cm²', '451.92 cm²', '1607.68 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 8 × 8 = 401.92 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 5 cm and height 7 cm. (π = 3.14)', '269.8 cm²', '109.9 cm²', '549.5 cm²', '219.8 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 5 × 7 = 219.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 7 cm and height 8 cm. (π = 3.14)', '401.68 cm²', '175.84 cm²', '1230.88 cm²', '351.68 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 7 × 8 = 351.68 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 5 cm and height 14 cm. (π = 3.14)', '489.6 cm²', '1099.0 cm²', '439.6 cm²', '219.8 cm²', 2,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 5 × 14 = 439.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 6 cm and height 14 cm. (π = 3.14)', '263.76 cm²', '527.52 cm²', '577.52 cm²', '1582.56 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 6 × 14 = 527.52 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 5 cm and height 14 cm. (π = 3.14)', '439.6 cm²', '219.8 cm²', '489.6 cm²', '1099.0 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 5 × 14 = 439.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 4 cm and height 9 cm. (π = 3.14)', '226.08 cm²', '452.16 cm²', '276.08 cm²', '113.04 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 4 × 9 = 226.08 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 7 cm and height 8 cm. (π = 3.14)', '401.68 cm²', '1230.88 cm²', '351.68 cm²', '175.84 cm²', 2,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 7 × 8 = 351.68 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 3 cm and height 14 cm. (π = 3.14)', '395.64 cm²', '263.76 cm²', '131.88 cm²', '313.76 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 3 × 14 = 263.76 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 8 cm and height 7 cm. (π = 3.14)', '401.68 cm²', '351.68 cm²', '175.84 cm²', '1406.72 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 8 × 7 = 351.68 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 3 cm and height 15 cm. (π = 3.14)', '282.6 cm²', '423.9 cm²', '332.6 cm²', '141.3 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 3 × 15 = 282.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 4 cm and height 13 cm. (π = 3.14)', '326.56 cm²', '653.12 cm²', '376.56 cm²', '163.28 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 4 × 13 = 326.56 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 7 cm and height 14 cm. (π = 3.14)', '665.44 cm²', '2154.04 cm²', '307.72 cm²', '615.44 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 7 × 14 = 615.44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 8 cm and height 13 cm. (π = 3.14)', '653.12 cm²', '326.56 cm²', '703.12 cm²', '2612.48 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 8 × 13 = 653.12 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 4 cm and height 15 cm. (π = 3.14)', '376.8 cm²', '753.6 cm²', '426.8 cm²', '188.4 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 4 × 15 = 376.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 5 cm and height 15 cm. (π = 3.14)', '471.0 cm²', '1177.5 cm²', '521.0 cm²', '235.5 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 5 × 15 = 471.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 7 cm and height 12 cm. (π = 3.14)', '527.52 cm²', '263.76 cm²', '577.52 cm²', '1846.32 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 7 × 12 = 527.52 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 5 cm and height 14 cm. (π = 3.14)', '439.6 cm²', '489.6 cm²', '219.8 cm²', '1099.0 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 5 × 14 = 439.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 6 cm and height 6 cm. (π = 3.14)', '276.08 cm²', '226.08 cm²', '113.04 cm²', '678.24 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 6 × 6 = 226.08 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cylinder with radius 5 cm and height 11 cm. (π = 3.14)', '863.5 cm²', '345.4 cm²', '395.4 cm²', '172.7 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'CSA = 2πrh = 2 × 3.14 × 5 × 11 = 345.4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 11 cm. (π = 3.14)', '376.8 cm²', '276.32 cm²', '396.8 cm²', '100.48 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 276.32 + 100.48 = 376.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 6 cm. (π = 3.14)', '271.2 cm²', '251.2 cm²', '100.48 cm²', '150.72 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 150.72 + 100.48 = 251.2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 5 cm and height 10 cm. (π = 3.14)', '491.0 cm²', '157.0 cm²', '471.0 cm²', '314.0 cm²', 2,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 314.0 + 157.0 = 471.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 7 cm and height 6 cm. (π = 3.14)', '591.48 cm²', '263.76 cm²', '307.72 cm²', '571.48 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 263.76 + 307.72 = 571.48 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 10 cm. (π = 3.14)', '351.68 cm²', '251.2 cm²', '100.48 cm²', '371.68 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 251.2 + 100.48 = 351.68 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 6 cm and height 8 cm. (π = 3.14)', '527.52 cm²', '301.44 cm²', '226.08 cm²', '547.52 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 301.44 + 226.08 = 527.52 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 3 cm and height 8 cm. (π = 3.14)', '207.24 cm²', '56.52 cm²', '227.24 cm²', '150.72 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 150.72 + 56.52 = 207.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 7 cm and height 11 cm. (π = 3.14)', '791.28 cm²', '483.56 cm²', '811.28 cm²', '307.72 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 483.56 + 307.72 = 791.28 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 5 cm and height 11 cm. (π = 3.14)', '502.4 cm²', '345.4 cm²', '157.0 cm²', '522.4 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 345.4 + 157.0 = 502.4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 9 cm. (π = 3.14)', '100.48 cm²', '226.08 cm²', '346.56 cm²', '326.56 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 226.08 + 100.48 = 326.56 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 6 cm and height 6 cm. (π = 3.14)', '472.16 cm²', '226.08 cm²', '452.16 cm²', 'Cannot determine', 2,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 226.08 + 226.08 = 452.16 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 7 cm and height 5 cm. (π = 3.14)', '527.52 cm²', '547.52 cm²', '219.8 cm²', '307.72 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 219.8 + 307.72 = 527.52 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 6 cm. (π = 3.14)', '100.48 cm²', '271.2 cm²', '251.2 cm²', '150.72 cm²', 2,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 150.72 + 100.48 = 251.2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 5 cm and height 7 cm. (π = 3.14)', '376.8 cm²', '157.0 cm²', '219.8 cm²', '396.8 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 219.8 + 157.0 = 376.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 10 cm. (π = 3.14)', '100.48 cm²', '371.68 cm²', '251.2 cm²', '351.68 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 251.2 + 100.48 = 351.68 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 3 cm and height 8 cm. (π = 3.14)', '56.52 cm²', '150.72 cm²', '227.24 cm²', '207.24 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 150.72 + 56.52 = 207.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 5 cm and height 5 cm. (π = 3.14)', '157.0 cm²', '334.0 cm²', '314.0 cm²', 'Cannot determine', 2,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 157.0 + 157.0 = 314.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 3 cm and height 10 cm. (π = 3.14)', '188.4 cm²', '56.52 cm²', '264.92 cm²', '244.92 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 188.4 + 56.52 = 244.92 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 11 cm. (π = 3.14)', '276.32 cm²', '396.8 cm²', '100.48 cm²', '376.8 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 276.32 + 100.48 = 376.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 5 cm and height 6 cm. (π = 3.14)', '157.0 cm²', '365.4 cm²', '345.4 cm²', '188.4 cm²', 2,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 188.4 + 157.0 = 345.4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 6 cm and height 9 cm. (π = 3.14)', '565.2 cm²', '339.12 cm²', '585.2 cm²', '226.08 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 339.12 + 226.08 = 565.2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 12 cm. (π = 3.14)', '401.92 cm²', '301.44 cm²', '100.48 cm²', '421.92 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 301.44 + 100.48 = 401.92 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 3 cm and height 5 cm. (π = 3.14)', '170.72 cm²', '150.72 cm²', '56.52 cm²', '94.2 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 94.2 + 56.52 = 150.72 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 6 cm and height 10 cm. (π = 3.14)', '226.08 cm²', '602.88 cm²', '622.88 cm²', '376.8 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 376.8 + 226.08 = 602.88 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 5 cm and height 11 cm. (π = 3.14)', '502.4 cm²', '345.4 cm²', '157.0 cm²', '522.4 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 345.4 + 157.0 = 502.4 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 4 cm and height 11 cm. (π = 3.14)', '376.8 cm²', '100.48 cm²', '396.8 cm²', '276.32 cm²', 0,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 276.32 + 100.48 = 376.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 5 cm and height 10 cm. (π = 3.14)', '491.0 cm²', '157.0 cm²', '314.0 cm²', '471.0 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 314.0 + 157.0 = 471.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 7 cm and height 11 cm. (π = 3.14)', '811.28 cm²', '307.72 cm²', '483.56 cm²', '791.28 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 483.56 + 307.72 = 791.28 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 7 cm and height 12 cm. (π = 3.14)', '855.24 cm²', '527.52 cm²', '307.72 cm²', '835.24 cm²', 3,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 527.52 + 307.72 = 835.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the total surface area of a closed cylinder with radius 7 cm and height 11 cm. (π = 3.14)', '811.28 cm²', '791.28 cm²', '307.72 cm²', '483.56 cm²', 1,
'lc_ol_mensuration', 6, 'developing', 'lc_ol', 'Total SA = 2πrh + 2πr² = 483.56 + 307.72 = 791.28 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 4 cm. (π = 3.14)', '50.24 cm²', '200.96 cm²', '267.95 cm²', '230.96 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 4² = 200.96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 7 cm. (π = 3.14)', '615.44 cm²', '645.44 cm²', '153.86 cm²', '1436.03 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 7² = 615.44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 10 cm. (π = 3.14)', '4186.67 cm²', '314.0 cm²', '1256.0 cm²', '1286.0 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 10² = 1256.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 4 cm. (π = 3.14)', '200.96 cm²', '230.96 cm²', '267.95 cm²', '50.24 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 4² = 200.96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 6 cm. (π = 3.14)', '904.32 cm²', '452.16 cm²', '482.16 cm²', '113.04 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 6² = 452.16 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 3 cm. (π = 3.14)', '143.04 cm²', '28.26 cm²', 'Cannot determine', '113.04 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 3² = 113.04 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 6 cm. (π = 3.14)', '904.32 cm²', '482.16 cm²', '113.04 cm²', '452.16 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 6² = 452.16 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 3 cm. (π = 3.14)', '28.26 cm²', 'Cannot determine', '143.04 cm²', '113.04 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 3² = 113.04 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 7 cm. (π = 3.14)', '615.44 cm²', '153.86 cm²', '645.44 cm²', '1436.03 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 7² = 615.44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 10 cm. (π = 3.14)', '4186.67 cm²', '1286.0 cm²', '1256.0 cm²', '314.0 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 10² = 1256.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 7 cm. (π = 3.14)', '615.44 cm²', '153.86 cm²', '645.44 cm²', '1436.03 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 7² = 615.44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 4 cm. (π = 3.14)', '50.24 cm²', '267.95 cm²', '200.96 cm²', '230.96 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 4² = 200.96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 8 cm. (π = 3.14)', '200.96 cm²', '833.84 cm²', '2143.57 cm²', '803.84 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 8² = 803.84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 8 cm. (π = 3.14)', '2143.57 cm²', '833.84 cm²', '803.84 cm²', '200.96 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 8² = 803.84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 6 cm. (π = 3.14)', '113.04 cm²', '904.32 cm²', '482.16 cm²', '452.16 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 6² = 452.16 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 4 cm. (π = 3.14)', '50.24 cm²', '267.95 cm²', '230.96 cm²', '200.96 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 4² = 200.96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 7 cm. (π = 3.14)', '645.44 cm²', '615.44 cm²', '1436.03 cm²', '153.86 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 7² = 615.44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 4 cm. (π = 3.14)', '200.96 cm²', '230.96 cm²', '50.24 cm²', '267.95 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 4² = 200.96 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 10 cm. (π = 3.14)', '1286.0 cm²', '314.0 cm²', '1256.0 cm²', '4186.67 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 10² = 1256.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 7 cm. (π = 3.14)', '1436.03 cm²', '153.86 cm²', '645.44 cm²', '615.44 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 7² = 615.44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 5 cm. (π = 3.14)', '78.5 cm²', '314.0 cm²', '523.33 cm²', '344.0 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 5² = 314.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 8 cm. (π = 3.14)', '803.84 cm²', '2143.57 cm²', '200.96 cm²', '833.84 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 8² = 803.84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 8 cm. (π = 3.14)', '2143.57 cm²', '200.96 cm²', '833.84 cm²', '803.84 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 8² = 803.84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 7 cm. (π = 3.14)', '1436.03 cm²', '615.44 cm²', '645.44 cm²', '153.86 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 7² = 615.44 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the surface area of a sphere with radius 9 cm. (π = 3.14)', '1017.36 cm²', '254.34 cm²', '1047.36 cm²', '3052.08 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'SA = 4πr² = 4 × 3.14 × 9² = 1017.36 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 7 cm and slant height 10 cm. (π = 3.14)', '373.66 cm²', '239.8 cm²', '153.86 cm²', '219.8 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 7 × 10 = 219.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 3 cm and slant height 12 cm. (π = 3.14)', '28.26 cm²', '141.3 cm²', '133.04 cm²', '113.04 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 3 × 12 = 113.04 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 4 cm and slant height 8 cm. (π = 3.14)', '100.48 cm²', '50.24 cm²', '150.72 cm²', '120.48 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 4 × 8 = 100.48 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 7 cm and slant height 12 cm. (π = 3.14)', '153.86 cm²', '283.76 cm²', '263.76 cm²', '417.62 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 7 × 12 = 263.76 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 5 cm and slant height 9 cm. (π = 3.14)', '161.3 cm²', '219.8 cm²', '78.5 cm²', '141.3 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 5 × 9 = 141.3 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 7 cm and slant height 17 cm. (π = 3.14)', '373.66 cm²', '393.66 cm²', '153.86 cm²', '527.52 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 7 × 17 = 373.66 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 3 cm and slant height 8 cm. (π = 3.14)', '75.36 cm²', '28.26 cm²', '95.36 cm²', '103.62 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 3 × 8 = 75.36 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 5 cm and slant height 9 cm. (π = 3.14)', '78.5 cm²', '141.3 cm²', '161.3 cm²', '219.8 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 5 × 9 = 141.3 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 8 cm and slant height 16 cm. (π = 3.14)', '421.92 cm²', '602.88 cm²', '200.96 cm²', '401.92 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 8 × 16 = 401.92 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 6 cm and slant height 11 cm. (π = 3.14)', '227.24 cm²', '207.24 cm²', '113.04 cm²', '320.28 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 6 × 11 = 207.24 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 3 cm and slant height 7 cm. (π = 3.14)', '65.94 cm²', '28.26 cm²', '94.2 cm²', '85.94 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 3 × 7 = 65.94 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 6 cm and slant height 13 cm. (π = 3.14)', '264.92 cm²', '244.92 cm²', '357.96 cm²', '113.04 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 6 × 13 = 244.92 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 5 cm and slant height 14 cm. (π = 3.14)', '78.5 cm²', '219.8 cm²', '239.8 cm²', '298.3 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 5 × 14 = 219.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 7 cm and slant height 10 cm. (π = 3.14)', '219.8 cm²', '373.66 cm²', '239.8 cm²', '153.86 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 7 × 10 = 219.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 3 cm and slant height 6 cm. (π = 3.14)', '84.78 cm²', '56.52 cm²', '28.26 cm²', '76.52 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 3 × 6 = 56.52 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 5 cm and slant height 9 cm. (π = 3.14)', '78.5 cm²', '219.8 cm²', '161.3 cm²', '141.3 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 5 × 9 = 141.3 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 7 cm and slant height 14 cm. (π = 3.14)', '461.58 cm²', '153.86 cm²', '307.72 cm²', '327.72 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 7 × 14 = 307.72 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 3 cm and slant height 6 cm. (π = 3.14)', '84.78 cm²', '76.52 cm²', '56.52 cm²', '28.26 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 3 × 6 = 56.52 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 7 cm and slant height 10 cm. (π = 3.14)', '153.86 cm²', '239.8 cm²', '373.66 cm²', '219.8 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 7 × 10 = 219.8 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 5 cm and slant height 13 cm. (π = 3.14)', '282.6 cm²', '224.1 cm²', '204.1 cm²', '78.5 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 5 × 13 = 204.1 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 4 cm and slant height 6 cm. (π = 3.14)', '125.6 cm²', '95.36 cm²', '75.36 cm²', '50.24 cm²', 2,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 4 × 6 = 75.36 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 8 cm and slant height 10 cm. (π = 3.14)', '271.2 cm²', '251.2 cm²', '452.16 cm²', '200.96 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 8 × 10 = 251.2 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 5 cm and slant height 8 cm. (π = 3.14)', '204.1 cm²', '125.6 cm²', '78.5 cm²', '145.6 cm²', 1,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 5 × 8 = 125.6 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 5 cm and slant height 10 cm. (π = 3.14)', '235.5 cm²', '177.0 cm²', '78.5 cm²', '157.0 cm²', 3,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 5 × 10 = 157.0 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the curved surface area of a cone with radius 4 cm and slant height 8 cm. (π = 3.14)', '100.48 cm²', '50.24 cm²', '120.48 cm²', '150.72 cm²', 0,
'lc_ol_mensuration', 7, 'proficient', 'lc_ol', 'CSA = πrl = 3.14 × 4 × 8 = 100.48 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 12 cm × 5 cm × 7 cm.', '420 cm³', '24 cm³', '358 cm³', '480 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 12 × 5 × 7 = 420 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 9 cm × 8 cm × 3 cm.', '288 cm³', '20 cm³', '216 cm³', '246 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 9 × 8 × 3 = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 10 cm × 8 cm × 2 cm.', '160 cm³', '20 cm³', '232 cm³', '240 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 10 × 8 × 2 = 160 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 9 cm × 4 cm × 2 cm.', '72 cm³', '108 cm³', '124 cm³', '15 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 9 × 4 × 2 = 72 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 11 cm × 6 cm × 5 cm.', '302 cm³', '22 cm³', '330 cm³', '396 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 11 × 6 × 5 = 330 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 9 cm × 5 cm × 7 cm.', '360 cm³', '21 cm³', '315 cm³', '286 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 9 × 5 × 7 = 315 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 9 cm × 3 cm × 2 cm.', '81 cm³', '102 cm³', '54 cm³', '14 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 9 × 3 × 2 = 54 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 12 cm × 3 cm × 4 cm.', '144 cm³', '192 cm³', '180 cm³', '19 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 12 × 3 × 4 = 144 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 8 cm × 4 cm × 6 cm.', '18 cm³', '208 cm³', '192 cm³', '224 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 8 × 4 × 6 = 192 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 11 cm × 10 cm × 4 cm.', '388 cm³', '440 cm³', '550 cm³', '25 cm³', 1,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 11 × 10 × 4 = 440 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 10 cm × 7 cm × 3 cm.', '20 cm³', '280 cm³', '210 cm³', '242 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 10 × 7 × 3 = 210 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 9 cm × 3 cm × 7 cm.', '189 cm³', '19 cm³', '216 cm³', '222 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 9 × 3 × 7 = 189 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 11 cm × 4 cm × 8 cm.', '352 cm³', '396 cm³', '23 cm³', '328 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 11 × 4 × 8 = 352 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 9 cm × 3 cm × 4 cm.', '16 cm³', '135 cm³', '108 cm³', '150 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 9 × 3 × 4 = 108 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 8 cm × 8 cm × 7 cm.', '23 cm³', '352 cm³', '448 cm³', '512 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 8 × 8 × 7 = 448 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 6 cm × 6 cm × 6 cm.', '18 cm³', 'Cannot determine', '216 cm³', '252 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 6 × 6 × 6 = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 6 cm × 3 cm × 7 cm.', '126 cm³', '144 cm³', '16 cm³', '162 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 6 × 3 × 7 = 126 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 7 cm × 5 cm × 2 cm.', '70 cm³', '105 cm³', '14 cm³', '118 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 7 × 5 × 2 = 70 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 5 cm × 8 cm × 7 cm.', '280 cm³', '262 cm³', '320 cm³', '20 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 5 × 8 × 7 = 280 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 5 cm × 5 cm × 6 cm.', '175 cm³', '150 cm³', '16 cm³', '170 cm³', 1,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 5 × 5 × 6 = 150 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 10 cm × 9 cm × 4 cm.', '450 cm³', '360 cm³', '23 cm³', '332 cm³', 1,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 10 × 9 × 4 = 360 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 6 cm × 4 cm × 3 cm.', '108 cm³', '96 cm³', '72 cm³', '13 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 6 × 4 × 3 = 72 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 10 cm × 3 cm × 7 cm.', '210 cm³', '242 cm³', '240 cm³', '20 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 10 × 3 × 7 = 210 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 4 cm × 5 cm × 4 cm.', '100 cm³', '13 cm³', '112 cm³', '80 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 4 × 5 × 4 = 80 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cuboid with dimensions 7 cm × 4 cm × 2 cm.', '13 cm³', '56 cm³', '84 cm³', '100 cm³', 1,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = l × w × h = 7 × 4 × 2 = 56 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 10 cm.', '600 cm³', '1000 cm³', '4000 cm³', '100 cm³', 1,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 10³ = 1000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 10 cm.', '600 cm³', '4000 cm³', '1000 cm³', '100 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 10³ = 1000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 4 cm.', '64 cm³', '256 cm³', '16 cm³', '96 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 4³ = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 6 cm.', '36 cm³', '864 cm³', 'Cannot determine', '216 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 6³ = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 5 cm.', '500 cm³', '150 cm³', '25 cm³', '125 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 5³ = 125 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 7 cm.', '343 cm³', '49 cm³', '294 cm³', '1372 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 7³ = 343 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 4 cm.', '64 cm³', '96 cm³', '16 cm³', '256 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 4³ = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 5 cm.', '125 cm³', '500 cm³', '150 cm³', '25 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 5³ = 125 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 4 cm.', '16 cm³', '96 cm³', '256 cm³', '64 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 4³ = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 6 cm.', 'Cannot determine', '864 cm³', '216 cm³', '36 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 6³ = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 5 cm.', '125 cm³', '25 cm³', '150 cm³', '500 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 5³ = 125 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 6 cm.', '864 cm³', '36 cm³', 'Cannot determine', '216 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 6³ = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 9 cm.', '729 cm³', '2916 cm³', '81 cm³', '486 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 9³ = 729 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 10 cm.', '1000 cm³', '4000 cm³', '600 cm³', '100 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 10³ = 1000 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cube with side 9 cm.', '81 cm³', '2916 cm³', '729 cm³', '486 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = s³ = 9³ = 729 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 5 cm, height 4 cm, and length 6 cm. Find the volume.', '120 cm³', '10.0 cm³', '66.0 cm³', '60.0 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 5 × 4) × 6 = 10.0 × 6 = 60.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 9 cm, height 4 cm, and length 10 cm. Find the volume.', '190.0 cm³', '18.0 cm³', '360 cm³', '180.0 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 9 × 4) × 10 = 18.0 × 10 = 180.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 6 cm, height 6 cm, and length 5 cm. Find the volume.', '95.0 cm³', '18.0 cm³', '180 cm³', '90.0 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 6 × 6) × 5 = 18.0 × 5 = 90.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 10 cm, height 6 cm, and length 10 cm. Find the volume.', '310.0 cm³', '30.0 cm³', '600 cm³', '300.0 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 10 × 6) × 10 = 30.0 × 10 = 300.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 5 cm, height 4 cm, and length 7 cm. Find the volume.', '10.0 cm³', '140 cm³', '70.0 cm³', '77.0 cm³', 2,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 5 × 4) × 7 = 10.0 × 7 = 70.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 4 cm, height 8 cm, and length 12 cm. Find the volume.', '384 cm³', '192.0 cm³', '204.0 cm³', '16.0 cm³', 1,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 4 × 8) × 12 = 16.0 × 12 = 192.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 10 cm, height 5 cm, and length 9 cm. Find the volume.', '225.0 cm³', '25.0 cm³', '450 cm³', '234.0 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 10 × 5) × 9 = 25.0 × 9 = 225.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 4 cm, height 7 cm, and length 10 cm. Find the volume.', '150.0 cm³', '14.0 cm³', '280 cm³', '140.0 cm³', 3,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 4 × 7) × 10 = 14.0 × 10 = 140.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 8 cm, height 3 cm, and length 12 cm. Find the volume.', '144.0 cm³', '288 cm³', '12.0 cm³', '156.0 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 8 × 3) × 12 = 12.0 × 12 = 144.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangular prism has triangle base 6 cm, height 7 cm, and length 11 cm. Find the volume.', '231.0 cm³', '242.0 cm³', '21.0 cm³', '462 cm³', 0,
'lc_ol_mensuration', 8, 'proficient', 'lc_ol', 'Volume = Area of triangle × length = (½ × 6 × 7) × 11 = 21.0 × 11 = 231.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 5 cm and height 10 cm. (π = 3.14)', '835.0 cm³', '314.0 cm³', '157.0 cm³', '785.0 cm³', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 5² × 10 = 3.14 × 25 × 10 = 785.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 5 cm and height 5 cm. (π = 3.14)', '442.5 cm³', '157.0 cm³', '78.5 cm³', '392.5 cm³', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 5² × 5 = 3.14 × 25 × 5 = 392.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 9 cm and height 13 cm. (π = 3.14)', '734.76 cm³', '3306.42 cm³', '367.38 cm³', '3356.42 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 9² × 13 = 3.14 × 81 × 13 = 3306.42 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 8 cm and height 7 cm. (π = 3.14)', '175.84 cm³', '351.68 cm³', '1456.72 cm³', '1406.72 cm³', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 8² × 7 = 3.14 × 64 × 7 = 1406.72 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 6 cm and height 15 cm. (π = 3.14)', '282.6 cm³', '1695.6 cm³', '565.2 cm³', '1745.6 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 6² × 15 = 3.14 × 36 × 15 = 1695.6 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 6 cm and height 11 cm. (π = 3.14)', '1243.44 cm³', '414.48 cm³', '207.24 cm³', '1293.44 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 6² × 11 = 3.14 × 36 × 11 = 1243.44 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 10 cm and height 13 cm. (π = 3.14)', '816.4 cm³', '4082.0 cm³', '4132.0 cm³', '408.2 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 10² × 13 = 3.14 × 100 × 13 = 4082.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 4 cm and height 15 cm. (π = 3.14)', '376.8 cm³', '753.6 cm³', '803.6 cm³', '188.4 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 4² × 15 = 3.14 × 16 × 15 = 753.6 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 6 cm and height 10 cm. (π = 3.14)', '376.8 cm³', '1180.4 cm³', '1130.4 cm³', '188.4 cm³', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 6² × 10 = 3.14 × 36 × 10 = 1130.4 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 3 cm and height 14 cm. (π = 3.14)', '395.64 cm³', '131.88 cm³', '445.64 cm³', '263.76 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 3² × 14 = 3.14 × 9 × 14 = 395.64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 3 cm and height 8 cm. (π = 3.14)', '75.36 cm³', '150.72 cm³', '276.08 cm³', '226.08 cm³', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 3² × 8 = 3.14 × 9 × 8 = 226.08 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 8 cm and height 8 cm. (π = 3.14)', '1657.68 cm³', '1607.68 cm³', '401.92 cm³', '200.96 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 8² × 8 = 3.14 × 64 × 8 = 1607.68 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 10 cm and height 14 cm. (π = 3.14)', '4396.0 cm³', '879.2 cm³', '439.6 cm³', '4446.0 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 10² × 14 = 3.14 × 100 × 14 = 4396.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 8 cm and height 7 cm. (π = 3.14)', '1406.72 cm³', '1456.72 cm³', '351.68 cm³', '175.84 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 8² × 7 = 3.14 × 64 × 7 = 1406.72 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 10 cm and height 6 cm. (π = 3.14)', '1884.0 cm³', '1934.0 cm³', '376.8 cm³', '188.4 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 10² × 6 = 3.14 × 100 × 6 = 1884.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 4 cm and height 10 cm. (π = 3.14)', '552.4 cm³', '125.6 cm³', '251.2 cm³', '502.4 cm³', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 4² × 10 = 3.14 × 16 × 10 = 502.4 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 7 cm and height 5 cm. (π = 3.14)', '819.3 cm³', '769.3 cm³', '109.9 cm³', '219.8 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 7² × 5 = 3.14 × 49 × 5 = 769.3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 8 cm and height 12 cm. (π = 3.14)', '2411.52 cm³', '301.44 cm³', '2461.52 cm³', '602.88 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 8² × 12 = 3.14 × 64 × 12 = 2411.52 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 7 cm and height 5 cm. (π = 3.14)', '769.3 cm³', '819.3 cm³', '219.8 cm³', '109.9 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 7² × 5 = 3.14 × 49 × 5 = 769.3 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 8 cm and height 5 cm. (π = 3.14)', '251.2 cm³', '125.6 cm³', '1004.8 cm³', '1054.8 cm³', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 8² × 5 = 3.14 × 64 × 5 = 1004.8 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 3 cm and height 9 cm. (π = 3.14)', '169.56 cm³', '254.34 cm³', '84.78 cm³', '304.34 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 3² × 9 = 3.14 × 9 × 9 = 254.34 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 10 cm and height 6 cm. (π = 3.14)', '1884.0 cm³', '1934.0 cm³', '188.4 cm³', '376.8 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 10² × 6 = 3.14 × 100 × 6 = 1884.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 10 cm and height 13 cm. (π = 3.14)', '4082.0 cm³', '408.2 cm³', '816.4 cm³', '4132.0 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 10² × 13 = 3.14 × 100 × 13 = 4082.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 10 cm and height 11 cm. (π = 3.14)', '3504.0 cm³', '345.4 cm³', '3454.0 cm³', '690.8 cm³', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 10² × 11 = 3.14 × 100 × 11 = 3454.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 5 cm and height 7 cm. (π = 3.14)', '599.5 cm³', '219.8 cm³', '549.5 cm³', '109.9 cm³', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 5² × 7 = 3.14 × 25 × 7 = 549.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 4 cm and height 11 cm. (π = 3.14)', '552.64 cm³', '602.64 cm³', '276.32 cm³', '138.16 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 4² × 11 = 3.14 × 16 × 11 = 552.64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 3 cm and height 7 cm. (π = 3.14)', '247.82 cm³', '131.88 cm³', '197.82 cm³', '65.94 cm³', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 3² × 7 = 3.14 × 9 × 7 = 197.82 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 10 cm and height 15 cm. (π = 3.14)', '471.0 cm³', '4760.0 cm³', '4710.0 cm³', '942.0 cm³', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 10² × 15 = 3.14 × 100 × 15 = 4710.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 7 cm and height 6 cm. (π = 3.14)', '923.16 cm³', '263.76 cm³', '131.88 cm³', '973.16 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 7² × 6 = 3.14 × 49 × 6 = 923.16 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 3 cm and height 6 cm. (π = 3.14)', '113.04 cm³', '219.56 cm³', '169.56 cm³', '56.52 cm³', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 3² × 6 = 3.14 × 9 × 6 = 169.56 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 5 cm and height 8 cm. (π = 3.14)', '125.6 cm³', '628.0 cm³', '678.0 cm³', '251.2 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 5² × 8 = 3.14 × 25 × 8 = 628.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 9 cm and height 10 cm. (π = 3.14)', '2593.4 cm³', '2543.4 cm³', '565.2 cm³', '282.6 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 9² × 10 = 3.14 × 81 × 10 = 2543.4 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 5 cm and height 15 cm. (π = 3.14)', '1227.5 cm³', '471.0 cm³', '235.5 cm³', '1177.5 cm³', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 5² × 15 = 3.14 × 25 × 15 = 1177.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 9 cm and height 10 cm. (π = 3.14)', '2543.4 cm³', '282.6 cm³', '565.2 cm³', '2593.4 cm³', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 9² × 10 = 3.14 × 81 × 10 = 2543.4 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cylinder with radius 5 cm and height 9 cm. (π = 3.14)', '756.5 cm³', '706.5 cm³', '282.6 cm³', '141.3 cm³', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'Volume = πr²h = 3.14 × 5² × 9 = 3.14 × 25 × 9 = 706.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 6 cm and volume 565.2 cm³. Find its height. (π = 3.14)', '6 cm', '5 cm', '7 cm', '30.0 cm', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 565.2 / (3.14 × 6²) = 565.2 / 113.04 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 7 cm and volume 1846.32 cm³. Find its height. (π = 3.14)', '84.0 cm', '14 cm', '12 cm', '7 cm', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 1846.32 / (3.14 × 7²) = 1846.32 / 153.86 = 12 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 4 cm and volume 502.4 cm³. Find its height. (π = 3.14)', '4 cm', '10 cm', '12 cm', '40.0 cm', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 502.4 / (3.14 × 4²) = 502.4 / 50.24 = 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 6 cm and volume 791.28 cm³. Find its height. (π = 3.14)', '42.0 cm', '7 cm', '9 cm', '6 cm', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 791.28 / (3.14 × 6²) = 791.28 / 113.04 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 4 cm and volume 401.92 cm³. Find its height. (π = 3.14)', '8 cm', '4 cm', '32.0 cm', '10 cm', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 401.92 / (3.14 × 4²) = 401.92 / 50.24 = 8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 4 cm and volume 251.2 cm³. Find its height. (π = 3.14)', '5 cm', '7 cm', '4 cm', '20.0 cm', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 251.2 / (3.14 × 4²) = 251.2 / 50.24 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 5 cm and volume 706.5 cm³. Find its height. (π = 3.14)', '9 cm', '45.0 cm', '11 cm', '5 cm', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 706.5 / (3.14 × 5²) = 706.5 / 78.5 = 9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 7 cm and volume 1077.02 cm³. Find its height. (π = 3.14)', 'Cannot determine', '9 cm', '7 cm', '49.0 cm', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 1077.02 / (3.14 × 7²) = 1077.02 / 153.86 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 7 cm and volume 1077.02 cm³. Find its height. (π = 3.14)', '9 cm', 'Cannot determine', '49.0 cm', '7 cm', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 1077.02 / (3.14 × 7²) = 1077.02 / 153.86 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 3 cm and volume 197.82 cm³. Find its height. (π = 3.14)', '7 cm', '21.0 cm', '9 cm', '3 cm', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 197.82 / (3.14 × 3²) = 197.82 / 28.26 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 6 cm and volume 791.28 cm³. Find its height. (π = 3.14)', '9 cm', '42.0 cm', '6 cm', '7 cm', 3,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 791.28 / (3.14 × 6²) = 791.28 / 113.04 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 4 cm and volume 351.68 cm³. Find its height. (π = 3.14)', '28.0 cm', '7 cm', '9 cm', '4 cm', 1,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 351.68 / (3.14 × 4²) = 351.68 / 50.24 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 5 cm and volume 392.5 cm³. Find its height. (π = 3.14)', '5 cm', '25.0 cm', '7 cm', 'Cannot determine', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 392.5 / (3.14 × 5²) = 392.5 / 78.5 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 6 cm and volume 904.32 cm³. Find its height. (π = 3.14)', '8 cm', '6 cm', '10 cm', '48.0 cm', 0,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 904.32 / (3.14 × 6²) = 904.32 / 113.04 = 8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylinder has radius 3 cm and volume 169.56 cm³. Find its height. (π = 3.14)', '18.0 cm', '3 cm', '6 cm', '8 cm', 2,
'lc_ol_mensuration', 9, 'proficient', 'lc_ol', 'h = V / (πr²) = 169.56 / (3.14 × 3²) = 169.56 / 28.26 = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 3 cm and height 9 cm. (π = 3.14)', '169.56 cm³', '254.34 cm³', '84.78 cm³', '104.78 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 3² × 9 = 84.78 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 7 cm and height 7 cm. (π = 3.14)', '359.01 cm³', '379.01 cm³', '1077.02 cm³', '718.01 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 7² × 7 = 359.01 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 5 cm and height 11 cm. (π = 3.14)', '307.83 cm³', '287.83 cm³', '863.5 cm³', '575.67 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 5² × 11 = 287.83 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 4 cm and height 11 cm. (π = 3.14)', '184.21 cm³', '368.43 cm³', '552.64 cm³', '204.21 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 4² × 11 = 184.21 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 4 cm and height 6 cm. (π = 3.14)', '200.96 cm³', '100.48 cm³', '301.44 cm³', '120.48 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 4² × 6 = 100.48 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 5 cm and height 8 cm. (π = 3.14)', '209.33 cm³', '628.0 cm³', '418.67 cm³', '229.33 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 5² × 8 = 209.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 5 cm and height 9 cm. (π = 3.14)', '706.5 cm³', '235.5 cm³', '471.0 cm³', '255.5 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 5² × 9 = 235.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 5 cm and height 5 cm. (π = 3.14)', '130.83 cm³', '392.5 cm³', '261.67 cm³', '150.83 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 5² × 5 = 130.83 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 3 cm and height 7 cm. (π = 3.14)', '85.94 cm³', '65.94 cm³', '197.82 cm³', '131.88 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 3² × 7 = 65.94 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 6 cm and height 8 cm. (π = 3.14)', '904.32 cm³', '602.88 cm³', '301.44 cm³', '321.44 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 6² × 8 = 301.44 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 7 cm and height 5 cm. (π = 3.14)', '512.87 cm³', '276.43 cm³', '256.43 cm³', '769.3 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 7² × 5 = 256.43 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 8 cm and height 6 cm. (π = 3.14)', '421.92 cm³', '1205.76 cm³', '803.84 cm³', '401.92 cm³', 3,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 8² × 6 = 401.92 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 7 cm and height 10 cm. (π = 3.14)', '532.87 cm³', '1538.6 cm³', '1025.73 cm³', '512.87 cm³', 3,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 7² × 10 = 512.87 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 3 cm and height 12 cm. (π = 3.14)', '226.08 cm³', '133.04 cm³', '113.04 cm³', '339.12 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 3² × 12 = 113.04 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 7 cm and height 11 cm. (π = 3.14)', '584.15 cm³', '1128.31 cm³', '564.15 cm³', '1692.46 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 7² × 11 = 564.15 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 3 cm and height 12 cm. (π = 3.14)', '113.04 cm³', '339.12 cm³', '133.04 cm³', '226.08 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 3² × 12 = 113.04 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 4 cm and height 10 cm. (π = 3.14)', '187.47 cm³', '167.47 cm³', '502.4 cm³', '334.93 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 4² × 10 = 167.47 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 4 cm and height 6 cm. (π = 3.14)', '100.48 cm³', '200.96 cm³', '301.44 cm³', '120.48 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 4² × 6 = 100.48 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 6 cm and height 5 cm. (π = 3.14)', '188.4 cm³', '565.2 cm³', '208.4 cm³', '376.8 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 6² × 5 = 188.4 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 6 cm and height 12 cm. (π = 3.14)', '904.32 cm³', '472.16 cm³', '1356.48 cm³', '452.16 cm³', 3,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 6² × 12 = 452.16 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 6 cm and height 11 cm. (π = 3.14)', '1243.44 cm³', '828.96 cm³', '414.48 cm³', '434.48 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 6² × 11 = 414.48 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 6 cm and height 11 cm. (π = 3.14)', '434.48 cm³', '414.48 cm³', '828.96 cm³', '1243.44 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 6² × 11 = 414.48 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 4 cm and height 5 cm. (π = 3.14)', '103.73 cm³', '251.2 cm³', '83.73 cm³', '167.47 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 4² × 5 = 83.73 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 3 cm and height 9 cm. (π = 3.14)', '104.78 cm³', '254.34 cm³', '169.56 cm³', '84.78 cm³', 3,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 3² × 9 = 84.78 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a cone with radius 4 cm and height 5 cm. (π = 3.14)', '83.73 cm³', '251.2 cm³', '103.73 cm³', '167.47 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓πr²h = ⅓ × 3.14 × 4² × 5 = 83.73 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 8 cm and height 6 cm.', '384 cm³', '256.0 cm³', '64 cm³', '128 cm³', 3,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 64 × 6 = 128 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 9 cm and height 10 cm.', '810 cm³', '540.0 cm³', '270 cm³', '81 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 81 × 10 = 270 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 10 cm and height 8 cm.', '533.33 cm³', '100 cm³', '266.67 cm³', '800 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 100 × 8 = 266.67 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 6 cm and height 12 cm.', '144 cm³', '432 cm³', '36 cm³', '288.0 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 36 × 12 = 144 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 5 cm and height 9 cm.', '25 cm³', '150.0 cm³', '225 cm³', '75.0 cm³', 3,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 25 × 9 = 75.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 5 cm and height 7 cm.', '58.33 cm³', '175 cm³', '116.67 cm³', '25 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 25 × 7 = 58.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 10 cm and height 10 cm.', '333.33 cm³', '1000 cm³', '100 cm³', '666.67 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 100 × 10 = 333.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 6 cm and height 10 cm.', '240.0 cm³', '120 cm³', '36 cm³', '360 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 36 × 10 = 120 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 7 cm and height 7 cm.', '114.33 cm³', '49 cm³', '228.67 cm³', '343 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 49 × 7 = 114.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 6 cm and height 12 cm.', '432 cm³', '36 cm³', '144 cm³', '288.0 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 36 × 12 = 144 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 7 cm and height 12 cm.', '49 cm³', '588 cm³', '196 cm³', '392.0 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 49 × 12 = 196 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 4 cm and height 12 cm.', '64 cm³', '128.0 cm³', '16 cm³', '192 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 16 × 12 = 64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 7 cm and height 5 cm.', '245 cm³', '81.67 cm³', '49 cm³', '163.33 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 49 × 5 = 81.67 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 9 cm and height 8 cm.', '81 cm³', '216 cm³', '648 cm³', '432.0 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 81 × 8 = 216 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 8 cm and height 9 cm.', '384.0 cm³', '192 cm³', '64 cm³', '576 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 64 × 9 = 192 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 10 cm and height 12 cm.', '1200 cm³', '100 cm³', '400.0 cm³', '800.0 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 100 × 12 = 400.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 4 cm and height 11 cm.', '117.33 cm³', '58.67 cm³', '176 cm³', '16 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 16 × 11 = 58.67 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 5 cm and height 10 cm.', '83.33 cm³', '166.67 cm³', '25 cm³', '250 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 25 × 10 = 83.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 10 cm and height 6 cm.', '600 cm³', '200.0 cm³', '100 cm³', '400.0 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 100 × 6 = 200.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 10 cm and height 11 cm.', '733.33 cm³', '366.67 cm³', '100 cm³', '1100 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 100 × 11 = 366.67 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 4 cm and height 9 cm.', '144 cm³', '16 cm³', '48 cm³', '96.0 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 16 × 9 = 48 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 7 cm and height 5 cm.', '245 cm³', '81.67 cm³', '163.33 cm³', '49 cm³', 1,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 49 × 5 = 81.67 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 10 cm and height 10 cm.', '666.67 cm³', '100 cm³', '333.33 cm³', '1000 cm³', 2,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 100 × 10 = 333.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 9 cm and height 7 cm.', '189 cm³', '81 cm³', '378.0 cm³', '567 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 81 × 7 = 189 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a square-based pyramid with base side 6 cm and height 8 cm.', '96 cm³', '288 cm³', '192.0 cm³', '36 cm³', 0,
'lc_ol_mensuration', 10, 'advanced', 'lc_ol', 'Volume = ⅓ × base area × height = ⅓ × 36 × 8 = 96 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 3 cm. (π = 3.14)', '163.04 cm³', 'Cannot determine', '113.04 cm³', '84.78 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 3³ = 113.04 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 4 cm. (π = 3.14)', '317.95 cm³', '200.96 cm³', 'Cannot determine', '267.95 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 4³ = 267.95 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 3 cm. (π = 3.14)', '113.04 cm³', '84.78 cm³', '163.04 cm³', 'Cannot determine', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 3³ = 113.04 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 5 cm. (π = 3.14)', '314.0 cm³', '523.33 cm³', '392.5 cm³', '573.33 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 5³ = 523.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 9 cm. (π = 3.14)', '3102.08 cm³', '1017.36 cm³', '2289.06 cm³', '3052.08 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 9³ = 3052.08 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 7 cm. (π = 3.14)', '1486.03 cm³', '615.44 cm³', '1077.02 cm³', '1436.03 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 7³ = 1436.03 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 9 cm. (π = 3.14)', '1017.36 cm³', '3052.08 cm³', '3102.08 cm³', '2289.06 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 9³ = 3052.08 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 8 cm. (π = 3.14)', '803.84 cm³', '1607.68 cm³', '2193.57 cm³', '2143.57 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 8³ = 2143.57 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 6 cm. (π = 3.14)', '452.16 cm³', '904.32 cm³', '678.24 cm³', '954.32 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 6³ = 904.32 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 6 cm. (π = 3.14)', '678.24 cm³', '954.32 cm³', '904.32 cm³', '452.16 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 6³ = 904.32 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 6 cm. (π = 3.14)', '954.32 cm³', '904.32 cm³', '452.16 cm³', '678.24 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 6³ = 904.32 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 8 cm. (π = 3.14)', '2143.57 cm³', '803.84 cm³', '1607.68 cm³', '2193.57 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 8³ = 2143.57 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 4 cm. (π = 3.14)', '317.95 cm³', 'Cannot determine', '267.95 cm³', '200.96 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 4³ = 267.95 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 5 cm. (π = 3.14)', '523.33 cm³', '573.33 cm³', '314.0 cm³', '392.5 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 5³ = 523.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 4 cm. (π = 3.14)', '267.95 cm³', '317.95 cm³', '200.96 cm³', 'Cannot determine', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 4³ = 267.95 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 6 cm. (π = 3.14)', '904.32 cm³', '954.32 cm³', '452.16 cm³', '678.24 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 6³ = 904.32 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 5 cm. (π = 3.14)', '314.0 cm³', '573.33 cm³', '392.5 cm³', '523.33 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 5³ = 523.33 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 6 cm. (π = 3.14)', '954.32 cm³', '678.24 cm³', '904.32 cm³', '452.16 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 6³ = 904.32 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 6 cm. (π = 3.14)', '904.32 cm³', '954.32 cm³', '452.16 cm³', '678.24 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 6³ = 904.32 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 8 cm. (π = 3.14)', '2143.57 cm³', '1607.68 cm³', '803.84 cm³', '2193.57 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 8³ = 2143.57 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 8 cm. (π = 3.14)', '2143.57 cm³', '803.84 cm³', '1607.68 cm³', '2193.57 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 8³ = 2143.57 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 9 cm. (π = 3.14)', '3102.08 cm³', '2289.06 cm³', '3052.08 cm³', '1017.36 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 9³ = 3052.08 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 9 cm. (π = 3.14)', '2289.06 cm³', '3052.08 cm³', '1017.36 cm³', '3102.08 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 9³ = 3052.08 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 8 cm. (π = 3.14)', '2193.57 cm³', '1607.68 cm³', '2143.57 cm³', '803.84 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 8³ = 2143.57 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a sphere with radius 6 cm. (π = 3.14)', '904.32 cm³', '452.16 cm³', '954.32 cm³', '678.24 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = (4/3)πr³ = (4/3) × 3.14 × 6³ = 904.32 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 7 cm. (π = 3.14)', '1436.03 cm³', '307.72 cm³', '718.01 cm³', 'Cannot determine', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 7³ = 718.01 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 7 cm. (π = 3.14)', '1436.03 cm³', '718.01 cm³', '307.72 cm³', 'Cannot determine', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 7³ = 718.01 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 6 cm. (π = 3.14)', 'Cannot determine', '904.32 cm³', '452.16 cm³', '226.08 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 6³ = 452.16 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 3 cm. (π = 3.14)', 'Cannot determine', '113.04 cm³', 'Cannot determine', '56.52 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 3³ = 56.52 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 8 cm. (π = 3.14)', '401.92 cm³', '1071.79 cm³', '2143.57 cm³', 'Cannot determine', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 8³ = 1071.79 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 8 cm. (π = 3.14)', 'Cannot determine', '1071.79 cm³', '2143.57 cm³', '401.92 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 8³ = 1071.79 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 5 cm. (π = 3.14)', '523.33 cm³', 'Cannot determine', '157.0 cm³', '261.67 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 5³ = 261.67 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 4 cm. (π = 3.14)', 'Cannot determine', '267.95 cm³', '133.97 cm³', '100.48 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 4³ = 133.97 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 6 cm. (π = 3.14)', 'Cannot determine', '226.08 cm³', '904.32 cm³', '452.16 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 6³ = 452.16 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 7 cm. (π = 3.14)', '718.01 cm³', '307.72 cm³', 'Cannot determine', '1436.03 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 7³ = 718.01 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 6 cm. (π = 3.14)', '226.08 cm³', 'Cannot determine', '904.32 cm³', '452.16 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 6³ = 452.16 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 8 cm. (π = 3.14)', '1071.79 cm³', '401.92 cm³', 'Cannot determine', '2143.57 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 8³ = 1071.79 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 7 cm. (π = 3.14)', 'Cannot determine', '1436.03 cm³', '307.72 cm³', '718.01 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 7³ = 718.01 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 7 cm. (π = 3.14)', 'Cannot determine', '1436.03 cm³', '718.01 cm³', '307.72 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 7³ = 718.01 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the volume of a hemisphere with radius 8 cm. (π = 3.14)', '1071.79 cm³', '401.92 cm³', 'Cannot determine', '2143.57 cm³', 0,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × 8³ = 1071.79 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=5, h=10) with a cone (r=5, h=3) on top. Find total volume. (π=3.14)', '1020.5 cm³', '785.0 cm³', '913.5 cm³', '863.5 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 785.0 cm³. Cone = 78.5 cm³. Total = 863.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=6, h=6) with a cone (r=6, h=3) on top. Find total volume. (π=3.14)', '841.28 cm³', '1017.36 cm³', '791.28 cm³', '678.24 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 678.24 cm³. Cone = 113.04 cm³. Total = 791.28 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=3, h=8) with a cone (r=3, h=5) on top. Find total volume. (π=3.14)', '226.08 cm³', '367.38 cm³', '323.18 cm³', '273.18 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 226.08 cm³. Cone = 47.1 cm³. Total = 273.18 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=4, h=10) with a cone (r=4, h=3) on top. Find total volume. (π=3.14)', '502.4 cm³', '653.12 cm³', '552.64 cm³', '602.64 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 502.4 cm³. Cone = 50.24 cm³. Total = 552.64 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=5, h=8) with a cone (r=5, h=4) on top. Find total volume. (π=3.14)', '942.0 cm³', '732.67 cm³', '628.0 cm³', '782.67 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 628.0 cm³. Cone = 104.67 cm³. Total = 732.67 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=3, h=8) with a cone (r=3, h=3) on top. Find total volume. (π=3.14)', '226.08 cm³', '310.86 cm³', '254.34 cm³', '304.34 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 226.08 cm³. Cone = 28.26 cm³. Total = 254.34 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=5, h=6) with a cone (r=5, h=5) on top. Find total volume. (π=3.14)', '471.0 cm³', '601.83 cm³', '651.83 cm³', '863.5 cm³', 1,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 471.0 cm³. Cone = 130.83 cm³. Total = 601.83 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=3, h=6) with a cone (r=3, h=4) on top. Find total volume. (π=3.14)', '282.6 cm³', '169.56 cm³', '257.24 cm³', '207.24 cm³', 3,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 169.56 cm³. Cone = 37.68 cm³. Total = 207.24 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=6, h=10) with a cone (r=6, h=4) on top. Find total volume. (π=3.14)', '1331.12 cm³', '1582.56 cm³', '1281.12 cm³', '1130.4 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 1130.4 cm³. Cone = 150.72 cm³. Total = 1281.12 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A solid has a cylinder (r=3, h=7) with a cone (r=3, h=6) on top. Find total volume. (π=3.14)', '367.38 cm³', '304.34 cm³', '254.34 cm³', '197.82 cm³', 2,
'lc_ol_mensuration', 11, 'advanced', 'lc_ol', 'Cylinder = 197.82 cm³. Cone = 56.52 cm³. Total = 254.34 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 196 cm³. If length = 7 cm and width = 4 cm, find the height.', '9 cm', '7 cm', '4 cm', '8 cm', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 196 / (7 × 4) = 196 / 28 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 75 cm³. If length = 5 cm and width = 5 cm, find the height.', '3 cm', 'Cannot determine', '5 cm', '4 cm', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 75 / (5 × 5) = 75 / 25 = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 192 cm³. If length = 8 cm and width = 4 cm, find the height.', '7 cm', '8 cm', '4 cm', '6 cm', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 192 / (8 × 4) = 192 / 32 = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 200 cm³. If length = 5 cm and width = 8 cm, find the height.', '5 cm', '6 cm', '8 cm', '7 cm', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 200 / (5 × 8) = 200 / 40 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 400 cm³. If length = 10 cm and width = 8 cm, find the height.', '6 cm', '5 cm', '8 cm', '7 cm', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 400 / (10 × 8) = 400 / 80 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 168 cm³. If length = 6 cm and width = 4 cm, find the height.', '7 cm', '8 cm', '9 cm', '4 cm', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 168 / (6 × 4) = 168 / 24 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 280 cm³. If length = 7 cm and width = 8 cm, find the height.', '5 cm', '7 cm', '6 cm', '8 cm', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 280 / (7 × 8) = 280 / 56 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 336 cm³. If length = 8 cm and width = 7 cm, find the height.', 'Cannot determine', '6 cm', '8 cm', '7 cm', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 336 / (8 × 7) = 336 / 56 = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 400 cm³. If length = 10 cm and width = 8 cm, find the height.', '7 cm', '8 cm', '6 cm', '5 cm', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 400 / (10 × 8) = 400 / 80 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 80 cm³. If length = 5 cm and width = 4 cm, find the height.', 'Cannot determine', '4 cm', '6 cm', '5 cm', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 80 / (5 × 4) = 80 / 20 = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 90 cm³. If length = 5 cm and width = 6 cm, find the height.', '6 cm', '5 cm', '4 cm', '3 cm', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 90 / (5 × 6) = 90 / 30 = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 336 cm³. If length = 8 cm and width = 6 cm, find the height.', '8 cm', '9 cm', '7 cm', '6 cm', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 336 / (8 × 6) = 336 / 48 = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 125 cm³. If length = 5 cm and width = 5 cm, find the height.', '5 cm', '6 cm', '7 cm', 'Cannot determine', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 125 / (5 × 5) = 125 / 25 = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 108 cm³. If length = 6 cm and width = 6 cm, find the height.', '4 cm', '6 cm', '5 cm', '3 cm', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 108 / (6 × 6) = 108 / 36 = 3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cuboid has volume 270 cm³. If length = 9 cm and width = 5 cm, find the height.', '5 cm', '7 cm', '8 cm', '6 cm', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'h = V / (l × w) = 270 / (9 × 5) = 270 / 45 = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 29 cm. What is its volume in litres? (1 litre = 1000 cm³)', '24389 litres', '29 litres', '243.89 litres', '24.389 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 29³ = 24389 cm³ = 24389/1000 = 24.389 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 10 cm. What is its volume in litres? (1 litre = 1000 cm³)', '10 litres', '1.0 litres', '10.0 litres', '1000 litres', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 10³ = 1000 cm³ = 1000/1000 = 1.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 18 cm. What is its volume in litres? (1 litre = 1000 cm³)', '5832 litres', '5.832 litres', '58.32 litres', '18 litres', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 18³ = 5832 cm³ = 5832/1000 = 5.832 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 13 cm. What is its volume in litres? (1 litre = 1000 cm³)', '13 litres', '21.97 litres', '2.197 litres', '2197 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 13³ = 2197 cm³ = 2197/1000 = 2.197 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 21 cm. What is its volume in litres? (1 litre = 1000 cm³)', '9.261 litres', '9261 litres', '21 litres', '92.60999999999999 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 21³ = 9261 cm³ = 9261/1000 = 9.261 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 30 cm. What is its volume in litres? (1 litre = 1000 cm³)', '27000 litres', '270.0 litres', '27.0 litres', '30 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 30³ = 27000 cm³ = 27000/1000 = 27.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 25 cm. What is its volume in litres? (1 litre = 1000 cm³)', '25 litres', '15.625 litres', '15625 litres', '156.25 litres', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 25³ = 15625 cm³ = 15625/1000 = 15.625 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 13 cm. What is its volume in litres? (1 litre = 1000 cm³)', '21.97 litres', '13 litres', '2.197 litres', '2197 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 13³ = 2197 cm³ = 2197/1000 = 2.197 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 28 cm. What is its volume in litres? (1 litre = 1000 cm³)', '28 litres', '21952 litres', '219.52 litres', '21.952 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 28³ = 21952 cm³ = 21952/1000 = 21.952 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 17 cm. What is its volume in litres? (1 litre = 1000 cm³)', '4913 litres', '49.13 litres', '4.913 litres', '17 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 17³ = 4913 cm³ = 4913/1000 = 4.913 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 30 cm. What is its volume in litres? (1 litre = 1000 cm³)', '30 litres', '27000 litres', '270.0 litres', '27.0 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 30³ = 27000 cm³ = 27000/1000 = 27.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 27 cm. What is its volume in litres? (1 litre = 1000 cm³)', '27 litres', '196.82999999999998 litres', '19683 litres', '19.683 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 27³ = 19683 cm³ = 19683/1000 = 19.683 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 17 cm. What is its volume in litres? (1 litre = 1000 cm³)', '17 litres', '49.13 litres', '4.913 litres', '4913 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 17³ = 4913 cm³ = 4913/1000 = 4.913 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 10 cm. What is its volume in litres? (1 litre = 1000 cm³)', '1000 litres', '10.0 litres', '1.0 litres', '10 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 10³ = 1000 cm³ = 1000/1000 = 1.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 21 cm. What is its volume in litres? (1 litre = 1000 cm³)', '9.261 litres', '9261 litres', '21 litres', '92.60999999999999 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = 21³ = 9261 cm³ = 9261/1000 = 9.261 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 6 cm and height 17 cm. How many litres of water can it hold? (π=3.14)', '1.92 litres', '0.32 litres', '2.92 litres', '1921.68 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 1921.68 cm³ = 1921.68/1000 = 1.92 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 5 cm and height 22 cm. How many litres of water can it hold? (π=3.14)', '1.73 litres', '1727.0 litres', '2.73 litres', '0.35 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 1727.0 cm³ = 1727.0/1000 = 1.73 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 7 cm and height 23 cm. How many litres of water can it hold? (π=3.14)', '0.51 litres', '3538.78 litres', '4.54 litres', '3.54 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 3538.78 cm³ = 3538.78/1000 = 3.54 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 6 cm and height 19 cm. How many litres of water can it hold? (π=3.14)', '0.36 litres', '3.15 litres', '2.15 litres', '2147.76 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 2147.76 cm³ = 2147.76/1000 = 2.15 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 6 cm and height 21 cm. How many litres of water can it hold? (π=3.14)', '3.37 litres', '0.4 litres', '2373.84 litres', '2.37 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 2373.84 cm³ = 2373.84/1000 = 2.37 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 6 cm and height 18 cm. How many litres of water can it hold? (π=3.14)', '2.03 litres', '2034.72 litres', '3.03 litres', '0.34 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 2034.72 cm³ = 2034.72/1000 = 2.03 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 9 cm and height 21 cm. How many litres of water can it hold? (π=3.14)', '6.34 litres', '0.59 litres', '5341.14 litres', '5.34 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 5341.14 cm³ = 5341.14/1000 = 5.34 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 6 cm and height 18 cm. How many litres of water can it hold? (π=3.14)', '2.03 litres', '3.03 litres', '2034.72 litres', '0.34 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 2034.72 cm³ = 2034.72/1000 = 2.03 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 5 cm and height 19 cm. How many litres of water can it hold? (π=3.14)', '1.49 litres', '0.3 litres', '2.49 litres', '1491.5 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 1491.5 cm³ = 1491.5/1000 = 1.49 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 8 cm and height 16 cm. How many litres of water can it hold? (π=3.14)', '4.22 litres', '3.22 litres', '3215.36 litres', '0.4 litres', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 3215.36 cm³ = 3215.36/1000 = 3.22 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 6 cm and height 23 cm. How many litres of water can it hold? (π=3.14)', '3.6 litres', '0.43 litres', '2.6 litres', '2599.92 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 2599.92 cm³ = 2599.92/1000 = 2.6 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 9 cm and height 23 cm. How many litres of water can it hold? (π=3.14)', '5.85 litres', '6.85 litres', '5849.82 litres', '0.65 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 5849.82 cm³ = 5849.82/1000 = 5.85 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 8 cm and height 24 cm. How many litres of water can it hold? (π=3.14)', '5.82 litres', '4.82 litres', '4823.04 litres', '0.6 litres', 1,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 4823.04 cm³ = 4823.04/1000 = 4.82 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 7 cm and height 21 cm. How many litres of water can it hold? (π=3.14)', '4.23 litres', '0.46 litres', '3.23 litres', '3231.06 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 3231.06 cm³ = 3231.06/1000 = 3.23 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 5 cm and height 19 cm. How many litres of water can it hold? (π=3.14)', '0.3 litres', '1491.5 litres', '2.49 litres', '1.49 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 1491.5 cm³ = 1491.5/1000 = 1.49 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 9 cm and height 18 cm. How many litres of water can it hold? (π=3.14)', '5.58 litres', '4578.12 litres', '0.51 litres', '4.58 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 4578.12 cm³ = 4578.12/1000 = 4.58 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 5 cm and height 16 cm. How many litres of water can it hold? (π=3.14)', '1.26 litres', '1256.0 litres', '2.26 litres', '0.25 litres', 0,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 1256.0 cm³ = 1256.0/1000 = 1.26 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 7 cm and height 15 cm. How many litres of water can it hold? (π=3.14)', '3.31 litres', '2307.9 litres', '2.31 litres', '0.33 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 2307.9 cm³ = 2307.9/1000 = 2.31 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 5 cm and height 20 cm. How many litres of water can it hold? (π=3.14)', '0.31 litres', '1570.0 litres', '2.57 litres', '1.57 litres', 3,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 1570.0 cm³ = 1570.0/1000 = 1.57 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cylindrical tank has radius 6 cm and height 20 cm. How many litres of water can it hold? (π=3.14)', '0.38 litres', '2260.8 litres', '2.26 litres', '3.26 litres', 2,
'lc_ol_mensuration', 12, 'advanced', 'lc_ol', 'Volume = πr²h = 2260.8 cm³ = 2260.8/1000 = 2.26 litres', 1);

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_mensuration';
