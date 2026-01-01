-- LC Higher Level - Counting & Combinatorics - Complete SQL
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_counting_complete.sql
-- Generated: 2025-12-15

-- Add Counting & Combinatorics topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_counting', 'Counting & Combinatorics', id, '🔢', 15, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_counting';

-- Questions (600 total, 50 per level x 12 levels)


INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit PIN codes are possible (digits can repeat)?', '100', '1000', '30', '1001', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 4, 1 trouser from 3, and 1 tie from 3. How many outfits?', '10', '40', '12', '36', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 3 × 3 = 36 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A restaurant offers 8 starters and 8 mains. How many different two-course meals are possible?', '64', '63', '16', '65', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'By multiplication principle: 8 × 8 = 64 meals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 2 roads from A to B and 4 roads from B to C. How many routes from A to C via B?', '8', '16', '7', '6', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '2 × 4 = 8 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 2-digit numbers can be formed using digits 0-9 (no repetition)?', '72', '81', '90', '100', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 5, 1 trouser from 4, and 1 tie from 2. How many outfits?', '11', '20', '45', '40', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '5 × 4 × 2 = 40 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 3, 1 trouser from 6, and 1 tie from 4. How many outfits?', '75', '18', '72', '13', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 6 × 4 = 72 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit PIN codes are possible (digits can repeat)?', '10001', '1000', '10000', '40', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A restaurant offers 5 starters and 4 mains. How many different two-course meals are possible?', '20', '19', '9', '21', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'By multiplication principle: 5 × 4 = 20 meals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 2, 1 trouser from 6, and 1 tie from 3. How many outfits?', '11', '38', '36', '12', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '2 × 6 × 3 = 36 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 4 roads from A to B and 2 roads from B to C. How many routes from A to C via B?', '7', '6', '16', '8', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 2 = 8 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 2, 1 trouser from 5, and 1 tie from 3. How many outfits?', 'None of these', '10', '32', '30', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '2 × 5 × 3 = 30 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 4, 1 trouser from 6, and 1 tie from 4. How many outfits?', '24', '14', '100', '96', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 6 × 4 = 96 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 3 roads from A to B and 4 roads from B to C. How many routes from A to C via B?', '11', '7', '24', '12', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 4 = 12 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 5, 1 trouser from 3, and 1 tie from 3. How many outfits?', '50', '15', '11', '45', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '5 × 3 × 3 = 45 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 5, 1 trouser from 5, and 1 tie from 4. How many outfits?', '105', '25', '100', '14', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '5 × 5 × 4 = 100 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A restaurant offers 7 starters and 5 mains. How many different two-course meals are possible?', '35', '34', '36', '12', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'By multiplication principle: 7 × 5 = 35 meals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit PIN codes are possible (digits can repeat)?', '10000', '10001', '40', '1000', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 2-digit numbers can be formed using digits 0-9 (no repetition)?', '100', '72', '90', '81', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 5, 1 trouser from 4, and 1 tie from 2. How many outfits?', '20', '45', '11', '40', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '5 × 4 × 2 = 40 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A restaurant offers 7 starters and 7 mains. How many different two-course meals are possible?', '50', '49', '14', '48', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'By multiplication principle: 7 × 7 = 49 meals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 3 roads from A to B and 2 roads from B to C. How many routes from A to C via B?', '6', 'None of these', '5', '12', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 2 = 6 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 4 roads from A to B and 3 roads from B to C. How many routes from A to C via B?', '24', '12', '11', '7', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 3 = 12 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit PIN codes are possible (digits can repeat)?', '100', '30', '1000', '1001', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 4, 1 trouser from 3, and 1 tie from 3. How many outfits?', '36', '12', '10', '40', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 3 × 3 = 36 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 2-digit numbers can be formed using digits 0-9 (no repetition)?', '90', '100', '81', '72', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 4 roads from A to B and 3 roads from B to C. How many routes from A to C via B?', '11', '24', '7', '12', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 3 = 12 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 2-digit numbers can be formed using digits 0-9 (no repetition)?', '90', '72', '81', '100', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 2-digit numbers can be formed using digits 0-9 (no repetition)?', '100', '81', '72', '90', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 3, 1 trouser from 6, and 1 tie from 3. How many outfits?', '18', '54', '57', '12', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 6 × 3 = 54 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit PIN codes are possible (digits can repeat)?', '40', '1000', '10001', '10000', 3,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit PIN codes are possible (digits can repeat)?', '1000', '1001', '30', '100', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 2-digit numbers can be formed using digits 0-9 (no repetition)?', '100', '90', '81', '72', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 4, 1 trouser from 5, and 1 tie from 3. How many outfits?', '20', '64', '60', '12', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 5 × 3 = 60 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 3, 1 trouser from 4, and 1 tie from 4. How many outfits?', '48', '11', '12', '51', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 4 × 4 = 48 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 2, 1 trouser from 4, and 1 tie from 2. How many outfits?', '16', 'None of these', '8', '18', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '2 × 4 × 2 = 16 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 2-digit numbers can be formed using digits 0-9 (no repetition)?', '81', '72', '100', '90', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 3, 1 trouser from 4, and 1 tie from 4. How many outfits?', '11', '51', '48', '12', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 4 × 4 = 48 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit PIN codes are possible (digits can repeat)?', '40', '10000', '1000', '10001', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit PIN codes are possible (digits can repeat)?', '40', '10000', '10001', '1000', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 2 roads from A to B and 4 roads from B to C. How many routes from A to C via B?', '8', '6', '16', '7', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '2 × 4 = 8 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 4 roads from A to B and 3 roads from B to C. How many routes from A to C via B?', '7', '11', '12', '24', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 3 = 12 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A restaurant offers 3 starters and 7 mains. How many different two-course meals are possible?', '22', '20', '21', '10', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'By multiplication principle: 3 × 7 = 21 meals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 5, 1 trouser from 4, and 1 tie from 3. How many outfits?', '60', '20', '65', '12', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '5 × 4 × 3 = 60 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 3 roads from A to B and 3 roads from B to C. How many routes from A to C via B?', '9', '8', '6', '18', 0,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 3 = 9 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A restaurant offers 4 starters and 8 mains. How many different two-course meals are possible?', '12', '32', '31', '33', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', 'By multiplication principle: 4 × 8 = 32 meals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit PIN codes are possible (digits can repeat)?', '100', '30', '1000', '1001', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '10 choices for each digit: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 4 roads from A to B and 2 roads from B to C. How many routes from A to C via B?', '16', '6', '8', '7', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 2 = 8 routes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 4, 1 trouser from 3, and 1 tie from 2. How many outfits?', '12', '9', '24', '28', 2,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '4 × 3 × 2 = 24 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 1 shirt from 3, 1 trouser from 4, and 1 tie from 3. How many outfits?', '10', '36', '12', '39', 1,
'lc_hl_counting', 1, 'foundation', 'lc_hl', '3 × 4 × 3 = 36 outfits', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 10!/8!', '91', '8', '100', '90', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '10!/8! = 10 × 9 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 10!/8!', '91', '100', '90', '8', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '10!/8! = 10 × 9 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 12!/11!', '479001600', '13', '12', '11', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '12!/11! = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8!/7!', '8', '9', '40320', '7', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '8!/7! = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 11!/10!', '39916800', '10', '11', '12', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '11!/10! = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 12!/11!', '12', '11', '479001600', '13', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '12!/11! = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 0!?', '0', '1', '∞', 'undefined', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', 'By definition, 0! = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (7)!/6!', '7', '8', '720', '6', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(7)!/6! = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7!', '5047', '5040', '720', '49', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 7!/5!', '42', '49', '35', '2', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7!/5! = 7 × 6 × ... × 6 = 42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 12!/11!', '479001600', '13', '11', '12', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '12!/11! = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6!/3!', '6', '126', '120', '18', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '6!/3! = 6 × 5 × ... × 4 = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 0!?', 'undefined', '0', '1', '∞', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', 'By definition, 0! = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4!', '6', '24', '28', '16', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '4! = 4 × 3 × 2 × 1 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 0!?', 'undefined', '0', '∞', '1', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', 'By definition, 0! = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8!/7!', '8', '40320', '7', '9', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '8!/7! = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 0!?', 'undefined', '1', '0', '∞', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', 'By definition, 0! = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7!', '5047', '5040', '49', '720', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6!/4!', '31', '30', '36', '4', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '6!/4! = 6 × 5 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8!/6!', '64', '56', '57', '6', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '8!/6! = 8 × 7 = 56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 7!/5!', '2', '42', '49', '35', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7!/5! = 7 × 6 × ... × 6 = 42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5!', '120', '125', '25', '24', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '5! = 5 × 4 × 3 × 2 × 1 = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (7)!/6!', '7', '720', '6', '8', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(7)!/6! = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 0!?', 'undefined', '0', '∞', '1', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', 'By definition, 0! = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 12!/11!', '12', '13', '479001600', '11', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '12!/11! = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 0!?', '0', 'undefined', '∞', '1', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', 'By definition, 0! = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (7)!/6!', '7', '6', '720', '8', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(7)!/6! = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7!', '720', '5047', '49', '5040', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 0!?', 'undefined', '0', '1', '∞', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', 'By definition, 0! = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5!/3!', '20', '21', '25', '3', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '5!/3! = 5 × 4 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 7!/5!', '2', '49', '42', '35', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7!/5! = 7 × 6 × ... × 6 = 42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (6)!/5!', '6', '7', '5', '120', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(6)!/5! = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (7)!/6!', '720', '6', '7', '8', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(7)!/6! = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8!/5!', '40', '336', '344', '6', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '8!/5! = 8 × 7 × ... × 6 = 336', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (6)!/5!', '6', '120', '7', '5', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(6)!/5! = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5!/4!', '120', '6', '5', '4', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '5!/4! = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5!', '25', '125', '120', '24', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '5! = 5 × 4 × 3 × 2 × 1 = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (6)!/5!', '6', '7', '120', '5', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(6)!/5! = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 10!/8!', '90', '91', '100', '8', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '10!/8! = 10 × 9 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 10!/8!', '100', '90', '91', '8', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '10!/8! = 10 × 9 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 10!/8!', '100', '90', '80', '2', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '10!/8! = 10 × 9 × ... × 9 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4!', '24', '6', '28', '16', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '4! = 4 × 3 × 2 × 1 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4!', '28', '24', '16', '6', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '4! = 4 × 3 × 2 × 1 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8!/6!', '57', '64', '56', '6', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '8!/6! = 8 × 7 = 56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7!', '5047', '49', '720', '5040', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (7)!/6!', '8', '7', '720', '6', 1,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '(7)!/6! = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 7!/6!', '6', '5040', '7', '8', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '7!/6! = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6!/4!', '4', '36', '31', '30', 3,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '6!/4! = 6 × 5 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 9!/7!', '81', '63', '72', '2', 2,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '9!/7! = 9 × 8 × ... × 8 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5!/3!', '20', '25', '3', '21', 0,
'lc_hl_counting', 2, 'foundation', 'lc_hl', '5!/3! = 5 × 4 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 7 athletes, how many ways to award gold, silver, bronze (3 positions)?', '21', '210', '5040', '35', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '7P3 = 210 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 7 athletes, how many ways to award gold, silver, bronze (4 positions)?', '5040', '28', '35', '840', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '7P4 = 840 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 4 different books be arranged on a shelf?', '4', '6', '16', '24', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4! = 24 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 6 different books be arranged on a shelf?', '720', '120', '6', '36', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 6 different books be arranged on a shelf?', '6', '720', '120', '36', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 athletes, how many ways to award gold, silver, bronze (3 positions)?', '120', '20', '18', '720', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6P3 = 120 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 8 athletes, how many ways to award gold, silver, bronze (4 positions)?', '32', '70', '40320', '1680', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '8P4 = 1680 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7P4 (permutations of 4 from 7).', '28', '847', '35', '840', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '7P4 = 7!/(7-4)! = 840', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''MATHS''?', '25', '125', '60', '120', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5 different letters: 5! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 students sit in 6 chairs in a row. How many seating arrangements?', '360', '720', '36', '12', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 6 different books be arranged on a shelf?', '6', '120', '36', '720', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''CARD''?', '16', '28', '12', '24', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 8 athletes, how many ways to award gold, silver, bronze (3 positions)?', '24', '336', '40320', '56', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '8P3 = 336 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''STUDY''?', '60', '125', '120', '25', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5 different letters: 5! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 students sit in 5 chairs in a row. How many seating arrangements?', '120', '60', '25', '10', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5! = 120 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''STUDY''?', '120', '125', '25', '60', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5 different letters: 5! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''MATHS''?', '25', '125', '60', '120', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5 different letters: 5! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 6P2 (permutations of 2 from 6).', '30', '36', '15', '12', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6P2 = 6!/(6-2)! = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7P2 (permutations of 2 from 7).', '49', '14', '21', '42', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '7P2 = 7!/(7-2)! = 42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''CARD''?', '28', '16', '24', '12', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''STUDY''?', '120', '125', '60', '25', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5 different letters: 5! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 students sit in 5 chairs in a row. How many seating arrangements?', '10', '25', '60', '120', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5! = 120 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''HELP''?', '16', '28', '12', '24', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''CARD''?', '28', '12', '16', '24', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 8P3 (permutations of 3 from 8).', '24', '336', '56', '344', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '8P3 = 8!/(8-3)! = 336', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 students sit in 4 chairs in a row. How many seating arrangements?', '24', '16', '12', '8', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4! = 24 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 students sit in 6 chairs in a row. How many seating arrangements?', '360', '36', '12', '720', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 students sit in 6 chairs in a row. How many seating arrangements?', '720', '36', '12', '360', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 7 athletes, how many ways to award gold, silver, bronze (4 positions)?', '35', '840', '28', '5040', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '7P4 = 840 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7P3 (permutations of 3 from 7).', '21', '217', '35', '210', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '7P3 = 7!/(7-3)! = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 8P2 (permutations of 2 from 8).', '64', '56', '16', '28', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '8P2 = 8!/(8-2)! = 56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 6 different books be arranged on a shelf?', '6', '720', '120', '36', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5P4 (permutations of 4 from 5).', '5', '20', '120', '125', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5P4 = 5!/(5-4)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 6 different books be arranged on a shelf?', '720', '120', '36', '6', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 students sit in 4 chairs in a row. How many seating arrangements?', '16', '12', '24', '8', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4! = 24 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 students sit in 4 chairs in a row. How many seating arrangements?', '12', '24', '16', '8', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4! = 24 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 4 different books be arranged on a shelf?', '6', '16', '24', '4', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4! = 24 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 4 different books be arranged on a shelf?', '16', '4', '24', '6', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4! = 24 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''HELP''?', '12', '24', '16', '28', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 6P2 (permutations of 2 from 6).', '36', '30', '12', '15', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6P2 = 6!/(6-2)! = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''CARD''?', '28', '24', '16', '12', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5P4 (permutations of 4 from 5).', '20', '5', '120', '125', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5P4 = 5!/(5-4)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 7 athletes, how many ways to award gold, silver, bronze (4 positions)?', '5040', '840', '35', '28', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '7P4 = 840 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 students sit in 4 chairs in a row. How many seating arrangements?', '12', '24', '16', '8', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4! = 24 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''CARD''?', '28', '16', '24', '12', 2,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 6 different books be arranged on a shelf?', '720', '36', '120', '6', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many arrangements of the letters in ''CARD''?', '16', '24', '12', '28', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '4 different letters: 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5P2 (permutations of 2 from 5).', '20', '10', '25', 'None of these', 0,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '5P2 = 5!/(5-2)! = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In how many ways can 6 different books be arranged on a shelf?', '36', '720', '120', '6', 1,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 students sit in 6 chairs in a row. How many seating arrangements?', '36', '12', '360', '720', 3,
'lc_hl_counting', 3, 'foundation', 'lc_hl', '6! = 720 arrangements', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, but one specific person must be first. How many arrangements?', '24', '120', '48', '4', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 4: (4)! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people at the ends. How many arrangements?', '48', '720', '96', '24', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (4)! for middle: 2 × 24 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must NOT be adjacent. How many arrangements?', '720', 'None of these', '240', '480', 3,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Total - together = 6! - (5)!×2 = 720 - 240 = 480', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must be adjacent. How many arrangements?', '720', '240', 'None of these', '120', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (5)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, 2 specific people at the ends. How many arrangements?', '5040', '240', '480', '120', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (5)! for middle: 2 × 120 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must be adjacent. How many arrangements?', '24', '48', '120', 'None of these', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (4)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must be adjacent. How many arrangements?', '240', '720', 'None of these', '120', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (5)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, but one specific person must be first. How many arrangements?', '720', '240', '120', '5', 2,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 5: (5)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people at the ends. How many arrangements?', '24', '48', '96', '720', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (4)! for middle: 2 × 24 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', '6', '12', 'None of these', '24', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must NOT be adjacent. How many arrangements?', '480', '720', '240', 'None of these', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Total - together = 6! - (5)!×2 = 720 - 240 = 480', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', '24', '12', 'None of these', '6', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must be adjacent. How many arrangements?', '48', '24', '120', 'None of these', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (4)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, but one specific person must be first. How many arrangements?', '4', '24', '120', '48', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 4: (4)! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people at the ends. How many arrangements?', '96', '24', '48', '720', 2,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (4)! for middle: 2 × 24 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', 'None of these', '24', '6', '12', 3,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people at the ends. How many arrangements?', '12', '6', '120', '24', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (3)! for middle: 2 × 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, but one specific person must be first. How many arrangements?', '720', '1440', '6', '5040', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 6: (6)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must be adjacent. How many arrangements?', '120', 'None of these', '720', '240', 3,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (5)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', 'None of these', '12', '6', '24', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, but one specific person must be first. How many arrangements?', '720', '1440', '6', '5040', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 6: (6)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, but one specific person must be first. How many arrangements?', '6', '720', '1440', '5040', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 6: (6)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, 2 specific people at the ends. How many arrangements?', '480', '5040', '240', '120', 2,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (5)! for middle: 2 × 120 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must NOT be adjacent. How many arrangements?', 'None of these', '72', '48', '120', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Total - together = 5! - (4)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', 'None of these', '12', '24', '6', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must be adjacent. How many arrangements?', '48', 'None of these', '24', '120', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (4)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people at the ends. How many arrangements?', '48', '720', '24', '96', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (4)! for middle: 2 × 24 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people at the ends. How many arrangements?', '48', '24', '96', '720', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (4)! for middle: 2 × 24 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', '12', 'None of these', '6', '24', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must be adjacent. How many arrangements?', 'None of these', '48', '120', '24', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (4)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', '6', 'None of these', '24', '12', 3,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must NOT be adjacent. How many arrangements?', 'None of these', '480', '720', '240', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Total - together = 6! - (5)!×2 = 720 - 240 = 480', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must NOT be adjacent. How many arrangements?', '120', 'None of these', '72', '48', 2,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Total - together = 5! - (4)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, but one specific person must be first. How many arrangements?', '48', '24', '4', '120', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 4: (4)! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people at the ends. How many arrangements?', '720', '24', '96', '48', 3,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (4)! for middle: 2 × 24 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, 2 specific people at the ends. How many arrangements?', '5040', '240', '120', '480', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (5)! for middle: 2 × 120 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange letters of TEAM keeping vowels (E,A) together. How many ways?', '24', '12', '6', 'None of these', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must be adjacent. How many arrangements?', '48', '120', 'None of these', '24', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (4)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, but one specific person must be first. How many arrangements?', '6', '720', '5040', '1440', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 6: (6)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people at the ends. How many arrangements?', '48', '24', '720', '96', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (4)! for middle: 2 × 24 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must be adjacent. How many arrangements?', 'None of these', '240', '120', '720', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (5)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people at the ends. How many arrangements?', '120', '6', '12', '24', 2,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (3)! for middle: 2 × 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people at the ends. How many arrangements?', '6', '12', '24', '120', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', '2 ways for ends, (3)! for middle: 2 × 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must be adjacent. How many arrangements?', '720', 'None of these', '240', '120', 2,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (5)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must be adjacent. How many arrangements?', '120', '48', '24', 'None of these', 1,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (4)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people in a row, 2 specific people must be adjacent. How many arrangements?', '48', 'None of these', '120', '24', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Treat pair as unit: (4)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, but one specific person must be first. How many arrangements?', '5040', '6', '1440', '720', 3,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 6: (6)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, but one specific person must be first. How many arrangements?', '720', '1440', '6', '5040', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 6: (6)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people in a row, 2 specific people must NOT be adjacent. How many arrangements?', '480', 'None of these', '240', '720', 0,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Total - together = 6! - (5)!×2 = 720 - 240 = 480', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people in a row, but one specific person must be first. How many arrangements?', '5040', '1440', '720', '6', 2,
'lc_hl_counting', 4, 'developing', 'lc_hl', 'Fix 1 person first, arrange remaining 6: (6)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 15 players, select 6 for a team. How many selections?', '90', '5005', '2502', '3603600', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '15C6 = 5005 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 13 players, select 6 for a team. How many selections?', '858', '78', '1235520', '1716', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '13C6 = 1716 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 people from 9 for a committee. How many ways?', '6', '84', '27', '504', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '9C3 = 84 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 people from 11 for a committee. How many ways?', '330', '44', '24', '7920', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '11C4 = 330 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 14 players, select 4 for a team. How many selections?', '1001', '500', '56', '24024', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '14C4 = 1001 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 11 players, select 5 for a team. How many selections?', '55440', '55', '231', '462', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '11C5 = 462 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 6C6?', '0', '720', '1', '6', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '6C6 = 1 (only one way to choose all)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 13 players, select 4 for a team. How many selections?', '52', '715', '17160', '357', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '13C4 = 715 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 9C9?', '1', '9', '362880', '0', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '9C9 = 1 (only one way to choose all)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 people from 12 for a committee. How many ways?', '48', '11880', '24', '495', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '12C4 = 495 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 10C3 (combinations of 3 from 10).', '130', '120', '30', '720', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C3 = 10!/(3!(10-3)!) = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 12 players, select 4 for a team. How many selections?', '48', '495', '11880', '247', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '12C4 = 495 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 5C5?', '5', '120', '1', '0', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '5C5 = 1 (only one way to choose all)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 people from 9 for a committee. How many ways?', '24', '36', '3024', '126', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '9C4 = 126 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 10C10?', '10', '1', '0', '3628800', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C10 = 1 (only one way to choose all)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 people from 12 for a committee. How many ways?', '495', '11880', '24', '48', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '12C4 = 495 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 12C4 = 495, what is 12C8?', '8', '495', '496', '792', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '12C4 = 12C8 = 495', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 people from 8 for a committee. How many ways?', '6', '24', '336', '56', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '8C3 = 56 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 12 players, select 6 for a team. How many selections?', '462', '72', '924', '665280', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '12C6 = 924 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 6C2 (combinations of 2 from 6).', '30', '15', '21', '12', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '6C2 = 6!/(2!(6-2)!) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 7C4 (combinations of 4 from 7).', '28', '840', '35', '42', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '7C4 = 7!/(4!(7-4)!) = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 5C5?', '0', '120', '1', '5', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '5C5 = 1 (only one way to choose all)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 10C3 (combinations of 3 from 10).', '130', '30', '120', '720', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C3 = 10!/(3!(10-3)!) = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 10C0?', '1', '10', '0', '3628800', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C0 = 1 (only one way to choose none)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 13 players, select 6 for a team. How many selections?', '858', '1235520', '1716', '78', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '13C6 = 1716 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 10C3 (combinations of 3 from 10).', '130', '720', '120', '30', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C3 = 10!/(3!(10-3)!) = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 10C4 (combinations of 4 from 10).', '5040', '220', '40', '210', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C4 = 10!/(4!(10-4)!) = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 people from 11 for a committee. How many ways?', '24', '7920', '44', '330', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '11C4 = 330 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 9C0?', '1', '0', '362880', '9', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '9C0 = 1 (only one way to choose none)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 5C0?', '0', '1', '120', '5', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '5C0 = 1 (only one way to choose none)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8C3 = 56, what is 8C5?', '5', '57', '70', '56', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '8C3 = 8C5 = 56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10C4 = 210, what is 10C6?', '210', '211', '252', '6', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C4 = 10C6 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 6C3 (combinations of 3 from 6).', '120', '26', '20', '18', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '6C3 = 6!/(3!(6-3)!) = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 8C2 (combinations of 2 from 8).', '28', '56', '36', '16', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '8C2 = 8!/(2!(8-2)!) = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 11C2 = 55, what is 11C9?', '165', '55', '9', '56', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '11C2 = 11C9 = 55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 people from 8 for a committee. How many ways?', '120', '6720', '56', '40', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '8C5 = 56 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 15 players, select 6 for a team. How many selections?', '5005', '3603600', '90', '2502', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '15C6 = 5005 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 9C0?', '0', '9', '362880', '1', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '9C0 = 1 (only one way to choose none)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 13 players, select 6 for a team. How many selections?', '1716', '1235520', '78', '858', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '13C6 = 1716 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 8C2 (combinations of 2 from 8).', '36', '56', '28', '16', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '8C2 = 8!/(2!(8-2)!) = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 people from 10 for a committee. How many ways?', '120', '252', '30240', '50', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C5 = 252 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 10C2 (combinations of 2 from 10).', '45', '90', '20', '55', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C2 = 10!/(2!(10-2)!) = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 11 players, select 5 for a team. How many selections?', '55', '462', '55440', '231', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '11C5 = 462 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 13 players, select 6 for a team. How many selections?', '1235520', '858', '78', '1716', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '13C6 = 1716 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 12 players, select 6 for a team. How many selections?', '462', '665280', '72', '924', 3,
'lc_hl_counting', 5, 'developing', 'lc_hl', '12C6 = 924 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 9C3 (combinations of 3 from 9).', '84', '27', '93', '504', 0,
'lc_hl_counting', 5, 'developing', 'lc_hl', '9C3 = 9!/(3!(9-3)!) = 84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10C3 = 120, what is 10C7?', '121', '7', '120', '210', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '10C3 = 10C7 = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 11C2 = 55, what is 11C9?', '9', '55', '56', '165', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '11C2 = 11C9 = 55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 people from 8 for a committee. How many ways?', '6', '56', '336', '24', 1,
'lc_hl_counting', 5, 'developing', 'lc_hl', '8C3 = 56 ways (order doesn''t matter)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 11 players, select 4 for a team. How many selections?', '7920', '44', '330', '165', 2,
'lc_hl_counting', 5, 'developing', 'lc_hl', '11C4 = 330 selections', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 9 people, must include the captain. How many ways?', '70', '57', '126', '56', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 3 from 8: 8C3 = 56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 4 men and 5 women, choose 3 with at least 1 woman. How many ways?', '4', '10', '84', '80', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 9C3 - 4C3 = 84 - 4 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 9 people, must NOT include Tom. How many ways?', '69', '56', '126', '70', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 4 from 8: 8C4 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 10 people, must include the captain. How many ways?', '126', '85', '210', '84', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 3 from 9: 9C3 = 84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '70', '16', '126', '60', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 8 people, must NOT include Tom. How many ways?', '34', 'None of these', '35', '70', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 4 from 7: 7C4 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 5 women, choose 3 with at least 1 woman. How many ways?', '10', '110', '120', 'None of these', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 10C3 - 5C3 = 120 - 10 = 110', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 6 women, choose 3 with at least 1 woman. How many ways?', 'None of these', '200', '220', '20', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 12C3 - 6C3 = 220 - 20 = 200', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 8 people, must NOT include Tom. How many ways?', '20', '56', '21', '35', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 5 from 7: 7C5 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '126', '60', '16', '70', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 3 with at least 1 woman. How many ways?', '84', '10', '74', '4', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 9C3 - 5C3 = 84 - 10 = 74', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 9 people, must NOT include Tom. How many ways?', '69', '56', '126', '70', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 4 from 8: 8C4 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 8 people, must include the captain. How many ways?', '56', '35', '21', '36', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 4 from 7: 7C4 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 9 people, must include the captain. How many ways?', '126', '71', '56', '70', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 4 from 8: 8C4 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 11 people, must NOT include Tom. How many ways?', '120', '330', '210', '209', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 4 from 10: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 4 men and 5 women, choose 3 with at least 1 woman. How many ways?', '10', '80', '84', '4', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 9C3 - 4C3 = 84 - 4 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '60', '126', '16', '70', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 12 people, must include the captain. How many ways?', '495', '166', '330', '165', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 3 from 11: 11C3 = 165', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a standard deck, choose 4 hearts. How many ways?', '728', '52', '270725', '715', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '13C4 = 715 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '60', '126', '16', '70', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 9 people, must include the captain. How many ways?', '70', '56', '71', '126', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 4 from 8: 8C4 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 9 people, must NOT include Tom. How many ways?', '70', '126', '69', '56', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 4 from 8: 8C4 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '70', '126', '60', '16', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, choose 3 with at least 1 woman. How many ways?', '145', '20', '10', '165', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 11C3 - 6C3 = 165 - 20 = 145', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 4 men and 4 women, choose 3 with at least 1 woman. How many ways?', 'None of these', '56', '52', '4', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 8C3 - 4C3 = 56 - 4 = 52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, choose 3 with at least 1 woman. How many ways?', '145', '10', '20', '165', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 11C3 - 6C3 = 165 - 20 = 145', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 4 women, choose 3 with at least 1 woman. How many ways?', '20', '4', '120', '100', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 10C3 - 6C3 = 120 - 20 = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a standard deck, choose 5 hearts. How many ways?', '1300', '1287', '65', '2598960', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', '13C5 = 1287 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a standard deck, choose 3 hearts. How many ways?', '39', '299', '22100', '286', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '13C3 = 286 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '16', '60', '126', '70', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '70', '126', '16', '60', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 4 men and 6 women, choose 3 with at least 1 woman. How many ways?', '116', '20', '120', '4', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 10C3 - 4C3 = 120 - 4 = 116', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 10 people, must NOT include Tom. How many ways?', '210', '84', '125', '126', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 4 from 9: 9C4 = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a standard deck, choose 3 hearts. How many ways?', '299', '22100', '39', '286', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '13C3 = 286 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 4 from 8 people, must include the captain. How many ways?', '70', '35', 'None of these', '36', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 3 from 7: 7C3 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 12 people, must NOT include Tom. How many ways?', '461', '792', '462', '330', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Exclude Tom, choose 5 from 11: 11C5 = 462', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '16', '70', '126', '60', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 6 women, choose 3 with at least 1 woman. How many ways?', '10', '165', '20', '155', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 11C3 - 5C3 = 165 - 10 = 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 12 people, must include the captain. How many ways?', '331', '330', '792', '462', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 4 from 11: 11C4 = 330', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '60', '70', '126', '16', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 6 women, choose 3 with at least 1 woman. How many ways?', '20', 'None of these', '200', '220', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 12C3 - 6C3 = 220 - 20 = 200', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 10 people, must include the captain. How many ways?', 'None of these', '252', '127', '126', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 4 from 9: 9C4 = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 11 people, must include the captain. How many ways?', '252', '211', '210', '462', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 4 from 10: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 4 men and 5 women, choose 3 with at least 1 woman. How many ways?', '80', '84', '10', '4', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 9C3 - 4C3 = 84 - 4 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a standard deck, choose 5 hearts. How many ways?', '1287', '1300', '2598960', '65', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', '13C5 = 1287 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a standard deck, choose 3 hearts. How many ways?', '22100', '286', '299', '39', 1,
'lc_hl_counting', 6, 'developing', 'lc_hl', '13C3 = 286 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 5 from 8 people, must include the captain. How many ways?', '35', '21', '36', '56', 0,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Fix captain, choose 4 from 7: 7C4 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 5 men and 4 women, choose 4 with exactly 2 men and 2 women.', '16', '70', '126', '60', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '5C2 × 4C2 = 10 × 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From a standard deck, choose 4 hearts. How many ways?', '270725', '728', '52', '715', 3,
'lc_hl_counting', 6, 'developing', 'lc_hl', '13C4 = 715 ways', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 4 men and 4 women, choose 3 with at least 1 woman. How many ways?', '56', '4', '52', 'None of these', 2,
'lc_hl_counting', 6, 'developing', 'lc_hl', 'Total - all men = 8C3 - 4C3 = 56 - 4 = 52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 runners: how many ways to arrange them at the finish line?', '1', '2520', '7', '5040', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 7! = 5040', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 6P3 = 120 and 6C3 = 20, what is 6P3 ÷ 6C3?', '7', 'None of these', '3', '6', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '6P3/6C3 = 3! = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8C3 = 56, find 8P3.', '336', '62', '168', '112', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '8P3 = 8C3 × 3! = 56 × 6 = 336', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 6P4 = 360 and 6C4 = 15, what is 6P4 ÷ 6C4?', '6', '25', '24', '4', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '6P4/6C4 = 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 8 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '70 and 70', '70 and 1680', '1680 and 1680', '1680 and 70', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 8P4 = 1680. Subsets: 8C4 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10C3 = 120, find 10P3.', '720', '360', '126', '240', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '10P3 = 10C3 × 3! = 120 × 6 = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 runners: how many ways to arrange them at the finish line?', '5040', '7', '2520', '1', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 7! = 5040', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Choosing 4 cards from a deck''', 'Combination', 'Both', 'Permutation', 'Neither', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order does not matter: Combination', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 7C3 = 35, find 7P3.', '210', '70', '41', '105', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '7P3 = 7C3 × 3! = 35 × 6 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 runners: how many ways to arrange them at the finish line?', '7', '5040', '2520', '1', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 7! = 5040', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 6P4 = 360 and 6C4 = 15, what is 6P4 ÷ 6C4?', '6', '24', '25', '4', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '6P4/6C4 = 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 10 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '210 and 5040', '210 and 210', '5040 and 210', '5040 and 5040', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 10P4 = 5040. Subsets: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 10 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '5040 and 210', '5040 and 5040', '210 and 210', '210 and 5040', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 10P4 = 5040. Subsets: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Ranking top 3 in a race''', 'Both', 'Neither', 'Permutation', 'Combination', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8C3 = 56, find 8P3.', '336', '62', '112', '168', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '8P3 = 8C3 × 3! = 56 × 6 = 336', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 9C3 = 84, find 9P3.', '90', '252', '168', '504', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '9P3 = 9C3 × 3! = 84 × 6 = 504', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10C3 = 120, find 10P3.', '360', '240', '126', '720', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '10P3 = 10C3 × 3! = 120 × 6 = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 10 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '5040 and 5040', '210 and 5040', '210 and 210', '5040 and 210', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 10P4 = 5040. Subsets: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 8 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '70 and 70', '1680 and 1680', '1680 and 70', '70 and 1680', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 8P4 = 1680. Subsets: 8C4 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 runners: how many ways to arrange them at the finish line?', '1', '720', '6', '360', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 6! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Choosing 4 cards from a deck''', 'Both', 'Neither', 'Permutation', 'Combination', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order does not matter: Combination', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 10 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '5040 and 5040', '210 and 5040', '210 and 210', '5040 and 210', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 10P4 = 5040. Subsets: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 10 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '5040 and 210', '210 and 210', '210 and 5040', '5040 and 5040', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 10P4 = 5040. Subsets: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Choosing 4 cards from a deck''', 'Both', 'Combination', 'Neither', 'Permutation', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order does not matter: Combination', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Choosing a 4-digit PIN''', 'Permutation', 'Neither', 'Both', 'Combination', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 7P3 = 210 and 7C3 = 35, what is 7P3 ÷ 7C3?', 'None of these', '6', '3', '7', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '7P3/7C3 = 3! = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 10 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '5040 and 210', '210 and 210', '5040 and 5040', '210 and 5040', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 10P4 = 5040. Subsets: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8C3 = 56, find 8P3.', '336', '62', '112', '168', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '8P3 = 8C3 × 3! = 56 × 6 = 336', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 runners: how many ways to arrange them at the finish line?', '720', '360', '6', '1', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 6! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Choosing a 4-digit PIN''', 'Neither', 'Combination', 'Permutation', 'Both', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 9P4 = 3024 and 9C4 = 126, what is 9P4 ÷ 9C4?', '25', '4', '9', '24', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '9P4/9C4 = 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 runners: how many ways to arrange them at the finish line?', '1', '60', '5', '120', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 5! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 10 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '210 and 210', '210 and 5040', '5040 and 210', '5040 and 5040', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 10P4 = 5040. Subsets: 10C4 = 210', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8P4 = 1680 and 8C4 = 70, what is 8P4 ÷ 8C4?', '4', '8', '24', '25', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '8P4/8C4 = 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 9 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '3024 and 3024', '3024 and 126', '126 and 126', '126 and 3024', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 9P4 = 3024. Subsets: 9C4 = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Arranging 5 people in a queue''', 'Both', 'Neither', 'Combination', 'Permutation', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 runners: how many ways to arrange them at the finish line?', '6', '720', '1', '360', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 6! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Choosing a 4-digit PIN''', 'Combination', 'Permutation', 'Neither', 'Both', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10C3 = 120, find 10P3.', '360', '240', '720', '126', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '10P3 = 10C3 × 3! = 120 × 6 = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Ranking top 3 in a race''', 'Combination', 'Both', 'Permutation', 'Neither', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 runners: how many ways to arrange them at the finish line?', '6', '360', '720', '1', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 6! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 runners: how many ways to arrange them at the finish line?', '6', '1', '720', '360', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters (permutation): 6! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8P4 = 1680 and 8C4 = 70, what is 8P4 ÷ 8C4?', '24', '4', '25', '8', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '8P4/8C4 = 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Ranking top 3 in a race''', 'Combination', 'Neither', 'Both', 'Permutation', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 9P4 = 3024 and 9C4 = 126, what is 9P4 ÷ 9C4?', '9', '24', '4', '25', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '9P4/9C4 = 4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Arranging 5 people in a queue''', 'Permutation', 'Both', 'Neither', 'Combination', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a permutation or combination? ''Choosing a 4-digit PIN''', 'Neither', 'Both', 'Combination', 'Permutation', 3,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Order matters: Permutation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 9 letters: (a) 4-letter passwords (b) 4-letter subsets. How many each?', '3024 and 3024', '126 and 126', '3024 and 126', '126 and 3024', 2,
'lc_hl_counting', 7, 'proficient', 'lc_hl', 'Passwords (order matters): 9P4 = 3024. Subsets: 9C4 = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10C3 = 120, find 10P3.', '720', '126', '360', '240', 0,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '10P3 = 10C3 × 3! = 120 × 6 = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10C3 = 120, find 10P3.', '240', '720', '360', '126', 1,
'lc_hl_counting', 7, 'proficient', 'lc_hl', '10P3 = 10C3 × 3! = 120 × 6 = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 4?', '16', '8', '15', '24', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''BOOK''?', 'None of these', '12', '24', '16', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '30', '15', '120', '35', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''MOON''?', '16', '24', '12', 'None of these', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit numbers (including those starting with 0) if digits can repeat?', '30', '1000', '100', '720', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 3 positions: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit numbers (including those starting with 0) if digits can repeat?', '1000', '720', '100', '30', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 3 positions: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''PEPPER''?', '60', '120', '720', '66', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '6! ÷ (repeated letters factorials) = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''PEPPER''?', '720', '66', '120', '60', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '6! ÷ (repeated letters factorials) = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 4?', '8', '16', '15', '24', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 6?', '63', '64', '720', '12', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^6 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''MOON''?', '24', 'None of these', '16', '12', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''BOOK''?', '16', '12', '24', 'None of these', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''PEPPER''?', '120', '60', '720', '66', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '6! ÷ (repeated letters factorials) = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''BOOK''?', '12', '16', '24', 'None of these', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '4', '8', '6', '24', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '120', '15', '35', '30', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 5?', '10', '31', '32', '120', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^5 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 4?', '24', '16', '8', '15', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '24', '4', '6', '8', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '6', '24', '8', '4', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit numbers (including those starting with 0) if digits can repeat?', '5040', '40', '10000', '1000', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 4 positions: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''MOON''?', 'None of these', '12', '16', '24', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''MOON''?', 'None of these', '24', '12', '16', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 4?', '24', '15', '16', '8', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''SEES''?', '12', '6', '10', '24', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit numbers (including those starting with 0) if digits can repeat?', '5040', '10000', '40', '1000', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 4 positions: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit numbers (including those starting with 0) if digits can repeat?', '1000', '30', '100', '720', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 3 positions: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''PEPPER''?', '120', '720', '66', '60', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '6! ÷ (repeated letters factorials) = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 5?', '10', '120', '31', '32', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^5 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit numbers (including those starting with 0) if digits can repeat?', '1000', '40', '10000', '5040', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 4 positions: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '120', '30', '15', '35', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 4-digit numbers (including those starting with 0) if digits can repeat?', '1000', '5040', '40', '10000', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 4 positions: 10^4 = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '30', '120', '35', '15', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '35', '30', '120', '15', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''BOOK''?', 'None of these', '16', '12', '24', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''MOON''?', '16', '12', 'None of these', '24', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '30', '120', '35', '15', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '6', '8', '4', '24', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '15', '35', '30', '120', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '4', '24', '6', '8', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many 3-digit numbers (including those starting with 0) if digits can repeat?', '100', '30', '720', '1000', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '10 choices for each of 3 positions: 10^3 = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '6', '24', '4', '8', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many binary strings of length 6?', '720', '12', '63', '64', 3,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '2 choices (0 or 1) for each position: 2^6 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '6', '8', '4', '24', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''TOOTH''?', '30', '15', '35', '120', 0,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '5!/(2!×2!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''BOOK''?', '16', 'None of these', '12', '24', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''SEES''?', '24', '6', '12', '10', 1,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of the letters in ''SEES''?', '24', '10', '6', '12', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4! ÷ (repeated letters factorials) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '4', '8', '6', '24', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?', '24', '8', '6', '4', 2,
'lc_hl_counting', 8, 'proficient', 'lc_hl', '4!/(2!×2!) = 24/4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must NOT sit together. How many arrangements?', '12', 'None of these', 'None of these', '24', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (5-1)! - (5-2)!×2 = 24 - 12 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people sit around a circular table. How many distinct arrangements?', '120', '720', 'None of these', '6', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (6-1)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 different beads on a bracelet (can be flipped). How many distinct arrangements?', '3', 'None of these', '24', '6', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Bracelet = circular ÷ 2 = (n-1)!/2 = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people sit around a circular table. How many distinct arrangements?', 'None of these', '720', '7', '5040', 1,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (7-1)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 keys on a keyring (can be flipped). How many distinct arrangements?', 'None of these', '120', '720', '60', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 120/2 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people around a table, 2 must sit together. How many arrangements?', '720', '120', '240', 'None of these', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (7-2)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', '48', '72', '120', 'None of these', 1,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must NOT sit together. How many arrangements?', '12', 'None of these', 'None of these', '24', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (5-1)! - (5-2)!×2 = 24 - 12 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must sit together. How many arrangements?', '24', 'None of these', '48', '120', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (6-2)! × 2! = 24 × 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', '72', 'None of these', '120', '48', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 keys on a keyring (can be flipped). How many distinct arrangements?', 'None of these', '120', '12', '24', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 different beads on a bracelet (can be flipped). How many distinct arrangements?', '60', '720', 'None of these', '120', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Bracelet = circular ÷ 2 = (n-1)!/2 = 120/2 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', '48', 'None of these', '120', '72', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', 'None of these', '48', '120', '72', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 keys on a keyring (can be flipped). How many distinct arrangements?', '24', '3', 'None of these', '6', 1,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 different beads on a bracelet (can be flipped). How many distinct arrangements?', '120', 'None of these', '24', '12', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Bracelet = circular ÷ 2 = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 keys on a keyring (can be flipped). How many distinct arrangements?', 'None of these', '3', '24', '6', 1,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must sit together. How many arrangements?', 'None of these', '6', '12', '24', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (5-2)! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people sit around a circular table. How many distinct arrangements?', '720', '120', 'None of these', '6', 1,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (6-1)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must sit together. How many arrangements?', '12', '24', 'None of these', '6', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (5-2)! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', '120', 'None of these', '72', '48', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people around a table, 2 must sit together. How many arrangements?', '240', '720', 'None of these', '120', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (7-2)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 keys on a keyring (can be flipped). How many distinct arrangements?', '3', '24', '6', 'None of these', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people sit around a circular table. How many distinct arrangements?', '720', '6', '120', 'None of these', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (6-1)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 keys on a keyring (can be flipped). How many distinct arrangements?', 'None of these', '12', '24', '120', 1,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people sit around a circular table. How many distinct arrangements?', '120', 'None of these', '24', '5', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (5-1)! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 keys on a keyring (can be flipped). How many distinct arrangements?', 'None of these', '24', '12', '120', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', '48', '120', '72', 'None of these', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 different beads on a bracelet (can be flipped). How many distinct arrangements?', '24', '120', 'None of these', '12', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Bracelet = circular ÷ 2 = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', '72', 'None of these', '48', '120', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people sit around a circular table. How many distinct arrangements?', 'None of these', '24', '5', '120', 1,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (5-1)! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 different beads on a bracelet (can be flipped). How many distinct arrangements?', '24', '120', 'None of these', '12', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Bracelet = circular ÷ 2 = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 different beads on a bracelet (can be flipped). How many distinct arrangements?', '6', 'None of these', '3', '24', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Bracelet = circular ÷ 2 = (n-1)!/2 = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people sit around a circular table. How many distinct arrangements?', '120', '720', '6', 'None of these', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (6-1)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must sit together. How many arrangements?', '24', '6', 'None of these', '12', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (5-2)! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people sit around a circular table. How many distinct arrangements?', '120', '6', '720', 'None of these', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (6-1)! = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people sit around a circular table. How many distinct arrangements?', '720', '7', 'None of these', '5040', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (7-1)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people sit around a circular table. How many distinct arrangements?', '5', 'None of these', '24', '120', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (5-1)! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people around a table, 2 must sit together. How many arrangements?', '240', '720', 'None of these', '120', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (7-2)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 people sit around a circular table. How many distinct arrangements?', '6', '4', 'None of these', '24', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (4-1)! = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people sit around a circular table. How many distinct arrangements?', 'None of these', '5040', '7', '720', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Circular arrangements: (n-1)! = (7-1)! = 720', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must sit together. How many arrangements?', 'None of these', '6', '12', '24', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (5-2)! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 keys on a keyring (can be flipped). How many distinct arrangements?', '120', 'None of these', '12', '24', 2,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 keys on a keyring (can be flipped). How many distinct arrangements?', '24', '6', 'None of these', '3', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Keyring = (n-1)!/2 = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', 'None of these', '48', '120', '72', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must NOT sit together. How many arrangements?', '12', 'None of these', 'None of these', '24', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (5-1)! - (5-2)!×2 = 24 - 12 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, 2 must NOT sit together. How many arrangements?', 'None of these', '120', '48', '72', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Total - together = (6-1)! - (6-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7 people around a table, 2 must sit together. How many arrangements?', '240', '720', '120', 'None of these', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (7-2)! × 2! = 120 × 2 = 240', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 different beads on a bracelet (can be flipped). How many distinct arrangements?', 'None of these', '24', '120', '12', 3,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Bracelet = circular ÷ 2 = (n-1)!/2 = 24/2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5 people around a table, 2 must sit together. How many arrangements?', '12', '6', 'None of these', '24', 0,
'lc_hl_counting', 9, 'proficient', 'lc_hl', 'Treat pair as unit: (5-2)! × 2! = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 6 identical balls into 2 distinct boxes. How many ways?', '15', '12', '9', '7', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (6+2-1)C(2-1) = 7C1 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '24', '3', '6', 'None of these', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '20', '60', '720', '70', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '720', '60', '20', '70', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '24', '6', '3', 'None of these', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '120', '35', '30', '15', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 4 distinct gifts to 3 people (each person can get any number). How many ways?', '0', '84', '81', '12', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '3 choices for each gift: 3^4 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 6 identical balls into 2 distinct boxes. How many ways?', '12', '15', '7', '9', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (6+2-1)C(2-1) = 7C1 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '6', '3', 'None of these', '24', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 4 identical balls into 2 distinct boxes. How many ways?', '6', '5', '8', '7', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (4+2-1)C(2-1) = 5C1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', 'None of these', '3', '6', '24', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '35', '15', '120', '30', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 4 identical balls into 2 distinct boxes. How many ways?', '6', '7', '8', '5', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (4+2-1)C(2-1) = 5C1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 3 distinct gifts to 2 people (each person can get any number). How many ways?', '8', '6', '0', '10', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '2 choices for each gift: 2^3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '30', '120', '15', '35', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '30', '35', '120', '15', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '720', '70', '60', '20', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 3 distinct gifts to 2 people (each person can get any number). How many ways?', '0', '8', '10', '6', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '2 choices for each gift: 2^3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 6 identical balls into 3 distinct boxes. How many ways?', '31', '20', '28', '18', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (6+3-1)C(3-1) = 8C2 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '720', '70', '20', '60', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '35', '15', '120', '30', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '24', '3', 'None of these', '6', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '3', '24', 'None of these', '6', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '24', '6', 'None of these', '3', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 5 identical balls into 2 distinct boxes. How many ways?', '10', '6', '8', 'None of these', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (5+2-1)C(2-1) = 6C1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '35', '120', '15', '30', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '30', '15', '35', '120', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', 'None of these', '24', '3', '6', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '720', '20', '60', '70', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '70', '60', '720', '20', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 3 distinct gifts to 2 people (each person can get any number). How many ways?', '8', '0', '10', '6', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '2 choices for each gift: 2^3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '70', '720', '60', '20', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '15', '35', '30', '120', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 4 identical balls into 3 distinct boxes. How many ways?', '12', '18', '15', '4', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (4+3-1)C(3-1) = 6C2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '24', 'None of these', '6', '3', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', 'None of these', '3', '24', '6', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '15', '30', '120', '35', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 3 distinct gifts to 2 people (each person can get any number). How many ways?', '10', '8', '6', '0', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '2 choices for each gift: 2^3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 4 identical balls into 2 distinct boxes. How many ways?', '7', '5', '6', '8', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (4+2-1)C(2-1) = 5C1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '15', '120', '30', '35', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '20', '70', '720', '60', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '120', '30', '15', '35', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '70', '720', '60', '20', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '3', '24', 'None of these', '6', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many ways to arrange 2 A''s, 2 B''s, and 1 C?', '15', '30', '35', '120', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '5!/(2!×2!×1!) = 120/4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 4 distinct gifts to 2 people (each person can get any number). How many ways?', '18', '0', '8', '16', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '2 choices for each gift: 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 4 people into 2 unlabeled groups of 2. How many ways?', '24', '6', 'None of these', '3', 3,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '4C2 ÷ 2! = 6 ÷ 2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 6 identical balls into 2 distinct boxes. How many ways?', '9', '7', '15', '12', 1,
'lc_hl_counting', 10, 'advanced', 'lc_hl', 'Stars and bars: (6+2-1)C(2-1) = 7C1 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Distribute 3 distinct gifts to 2 people (each person can get any number). How many ways?', '6', '0', '8', '10', 2,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '2 choices for each gift: 2^3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide 6 people into groups of 3, 2, and 1. How many ways?', '60', '720', '70', '20', 0,
'lc_hl_counting', 10, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^6?', '5', '6', '7', '12', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 6 + 1 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the sum of all entries in row 5 of Pascal''s triangle?', '10', '32', '120', '31', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Sum of row n = 2^n = 2^5 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^10?', '9', '11', '20', '10', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 10 + 1 = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using Pascal''s identity, find 6C3 + 6C4.', '15', '35', '20', '34', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '6C3 + 6C4 = 7C4 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (a + b)^6, what is the coefficient of a^3b^3?', '26', '20', '18', '15', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Coefficient = 6C3 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using Pascal''s identity, find 4C2 + 4C3.', '4', '9', '10', '6', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 + 4C3 = 5C3 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^8?', '7', '16', '9', '8', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 8 + 1 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the sum of all entries in row 6 of Pascal''s triangle?', '64', '63', '720', '12', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Sum of row n = 2^n = 2^6 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^8?', '9', '16', '8', '7', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 8 + 1 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the sum of all entries in row 4 of Pascal''s triangle?', '15', '8', '16', '24', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Sum of row n = 2^n = 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^7?', '8', '7', '6', '14', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 7 + 1 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using Pascal''s identity, find 4C1 + 4C2.', '4', '9', '6', '10', 3,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C1 + 4C2 = 5C2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '16', '30', '6', '24', 3,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Pascal''s triangle, what is the entry in row 6, position 4? (Row 0 = top, position 0 = left)', '15', '20', '16', '5', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Entry = 6C4 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^7?', '8', '14', '6', '7', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 7 + 1 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (a + b)^6, what is the coefficient of a^1b^5?', '1', '12', '6', '30', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Coefficient = 6C5 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '24', '30', '16', '6', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (a + b)^4, what is the coefficient of a^3b^1?', '4', '6', '8', 'None of these', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Coefficient = 4C1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Pascal''s triangle, what is the entry in row 4, position 3? (Row 0 = top, position 0 = left)', '1', '5', '4', '6', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Entry = 4C3 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using Pascal''s identity, find 4C2 + 4C3.', '4', '6', '9', '10', 3,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 + 4C3 = 5C3 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Pascal''s triangle, what is the entry in row 5, position 3? (Row 0 = top, position 0 = left)', '4', 'None of these', '10', '11', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Entry = 5C3 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Pascal''s triangle, what is the entry in row 4, position 1? (Row 0 = top, position 0 = left)', '1', '3', '4', '5', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Entry = 4C1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^8?', '9', '8', '16', '7', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 8 + 1 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (a + b)^6, what is the coefficient of a^1b^5?', '6', '1', '30', '12', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Coefficient = 6C5 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using Pascal''s identity, find 5C3 + 5C4.', '14', '15', '10', '5', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '5C3 + 5C4 = 6C4 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Pascal''s triangle, what is the entry in row 4, position 2? (Row 0 = top, position 0 = left)', '6', '7', '3', '4', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Entry = 4C2 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (a + b)^6, what is the coefficient of a^2b^4?', '15', '24', '21', '6', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Coefficient = 6C4 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Pascal''s triangle, what is the entry in row 6, position 2? (Row 0 = top, position 0 = left)', '10', '6', '15', '16', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Entry = 6C2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^7?', '8', '14', '7', '6', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 7 + 1 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^9?', '9', '10', '18', '8', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 9 + 1 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '30', '24', '6', '16', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (a + b)^4, what is the coefficient of a^3b^1?', '4', '6', 'None of these', '8', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Coefficient = 4C1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '30', '6', '24', '16', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Pascal''s triangle, what is the entry in row 5, position 2? (Row 0 = top, position 0 = left)', '10', '6', '5', '11', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Entry = 5C2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using Pascal''s identity, find 6C2 + 6C3.', '15', '20', '35', '34', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '6C2 + 6C3 = 7C3 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^5?', '10', '5', '6', '4', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 5 + 1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^6?', '5', '7', '6', '12', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 6 + 1 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the sum of all entries in row 7 of Pascal''s triangle?', '127', '5040', '14', '128', 3,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Sum of row n = 2^n = 2^7 = 128', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '16', '30', '6', '24', 3,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the sum of all entries in row 5 of Pascal''s triangle?', '31', '10', '32', '120', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Sum of row n = 2^n = 2^5 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '16', '6', '24', '30', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (a + b)^5, what is the coefficient of a^4b^1?', '5', 'None of these', 'None of these', '10', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Coefficient = 5C1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^6?', '6', '7', '12', '5', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 6 + 1 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '16', '6', '30', '24', 3,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^6?', '12', '7', '6', '5', 1,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 6 + 1 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the sum of all entries in row 6 of Pascal''s triangle?', '12', '720', '64', '63', 2,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Sum of row n = 2^n = 2^6 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the sum of all entries in row 6 of Pascal''s triangle?', '12', '720', '63', '64', 3,
'lc_hl_counting', 11, 'advanced', 'lc_hl', 'Sum of row n = 2^n = 2^6 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using Pascal''s identity, find 6C2 + 6C3.', '35', '20', '34', '15', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '6C2 + 6C3 = 7C3 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In (x + 2)^4, find the coefficient of x².', '24', '16', '30', '6', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '4C2 × 2² = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms are in the expansion of (a + b)^7?', '8', '14', '6', '7', 0,
'lc_hl_counting', 11, 'advanced', 'lc_hl', '(a + b)^n has n + 1 terms: 7 + 1 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '381', '431', '75', '462', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '381', '462', '75', '431', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Paths from (0,0) to (2,2) moving only right or up. How many?', '6', '4', '11', 'None of these', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Need 2 rights and 2 ups: (2+2)!/(2!2!) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '15', '6', '24', '9', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '431', '75', '381', '462', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '48', '72', '120', '96', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '72', '48', '120', '96', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '286', '1244', '1144', '22100', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '96', '48', '72', '120', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '6', '24', '9', '15', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '24', '9', '15', '6', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '462', '381', '431', '75', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '72', '96', '48', '120', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Paths from (0,0) to (4,3) moving only right or up. How many?', '12', '35', '7', '40', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Need 4 rights and 3 ups: (4+3)!/(4!3!) = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '22100', '286', '1244', '1144', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''BANANA''?', '60', '720', '30', '66', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''BANANA''?', '66', '30', '60', '720', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '22100', '1144', '286', '1244', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '286', '1244', '22100', '1144', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Paths from (0,0) to (2,3) moving only right or up. How many?', '6', '5', '10', '15', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Need 2 rights and 3 ups: (2+3)!/(2!3!) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''BANANA''?', '66', '60', '720', '30', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '9', '15', '24', '6', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '462', '431', '75', '381', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '72', '48', '120', '96', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '1244', '286', '22100', '1144', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Paths from (0,0) to (4,3) moving only right or up. How many?', '40', '12', '7', '35', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Need 4 rights and 3 ups: (4+3)!/(4!3!) = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '24', '9', '15', '6', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '48', '72', '120', '96', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '431', '75', '462', '381', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Paths from (0,0) to (3,3) moving only right or up. How many?', '6', '20', '25', '9', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Need 3 rights and 3 ups: (3+3)!/(3!3!) = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '22100', '1144', '1244', '286', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '22100', '1144', '1244', '286', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '9', '6', '24', '15', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '286', '1144', '1244', '22100', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '75', '462', '431', '381', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '96', '48', '120', '72', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '15', '9', '6', '24', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '286', '22100', '1244', '1144', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '72', '120', '96', '48', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '462', '381', '431', '75', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '381', '462', '431', '75', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)', '9', '6', '24', '15', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Choose 3 cards from a deck, all from the same suit. How many ways?', '286', '22100', '1144', '1244', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '4 suits × 13C3 = 4 × 286 = 1144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Paths from (0,0) to (4,2) moving only right or up. How many?', '20', '6', '15', '8', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Need 4 rights and 2 ups: (4+2)!/(4!2!) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''BANANA''?', '30', '66', '720', '60', 3,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '48', '96', '72', '120', 2,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Paths from (0,0) to (4,2) moving only right or up. How many?', '15', '6', '8', '20', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Need 4 rights and 2 ups: (4+2)!/(4!2!) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 people around a table, A and B must NOT sit together. How many arrangements?', '96', '72', '48', '120', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - together = (n-1)! - (n-2)!×2 = 120 - 48 = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 6 men and 5 women, form 5-person committee with at least 2 women. How many ways?', '75', '381', '462', '431', 1,
'lc_hl_counting', 12, 'advanced', 'lc_hl', 'Total - (0 women) - (1 woman) = 462 - 6 - 75 = 381', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct arrangements of ''BANANA''?', '60', '30', '66', '720', 0,
'lc_hl_counting', 12, 'advanced', 'lc_hl', '6!/(3!×2!×1!) = 720/12 = 60', 1);