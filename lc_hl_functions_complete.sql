-- LC Higher Level - Functions - Complete SQL
-- Includes topic creation + 600 questions
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_functions_complete.sql
-- Generated: 2025-12-14

-- Add Functions topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_functions', 'Functions', id, '📈', 6, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_functions';

-- Questions (600 total: 50 per level x 12 levels)
-- LC Higher Level - Functions Questions
-- Generated: 2025-12-14
-- Total: 600 questions

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 9, find f(1).', '13', '14', '4', '17', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(1) = 4(1) + 9 = 4 + 9 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x - 4, find f(1).', '0', '1', '4', 'Option 4', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(1) = 4(1) - 4 = 4 - 4 = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 7x + 3, find f(2).', '24', '17', '14', '18', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(2) = 7(2) + 3 = 14 + 3 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 5, find f(1).', '11', '10', '5', '15', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(1) = 5(1) + 5 = 5 + 5 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 2, find f(4).', '12', '11', '10', '8', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(4) = 2(4) + 2 = 8 + 2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 7x - 2, find f(5).', '33', '34', '40', '35', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = 7(5) - 2 = 35 - 2 = 33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 9, find f(4).', '20', '30', '34', '29', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(4) = 5(4) + 9 = 20 + 9 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x - 9, find f(5).', '10', '1', '2', '3', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = 2(5) - 9 = 10 - 9 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 6x - 1, find f(5).', '30', '35', '29', 'Option 4', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = 6(5) - 1 = 30 - 1 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 9x - 9, find f(2).', '9', '18', 'Option 4', '10', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(2) = 9(2) - 9 = 18 - 9 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x - 2, find f(4).', '18', '19', '20', '23', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(4) = 5(4) - 2 = 20 - 2 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 7, find f(3).', '19', '12', '23', '20', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(3) = 4(3) + 7 = 12 + 7 = 19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x - 5, find f(5).', '10', '11', '13', '15', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = 3(5) - 5 = 15 - 5 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 5, find f(5).', '26', '29', '25', '20', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = 4(5) + 5 = 20 + 5 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x - 8, find f(3).', '-1', '-2', '0', '6', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(3) = 2(3) - 8 = 6 - 8 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² - 5, find f(6).', '1', '7', '31', '36', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(6) = (6)² - 5 = 36 - 5 = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 7, find f(5).', '17', '32', '25', '12', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = (5)² + 7 = 25 + 7 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 5, find f(3).', '8', '14', '9', '11', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(3) = (3)² + 5 = 9 + 5 = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² - 4, find f(1).', '-3', 'Option 4', '-2', '1', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(1) = (1)² - 4 = 1 - 4 = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 4, find f(5).', '25', '14', '29', '9', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = (5)² + 4 = 25 + 4 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² - 2, find f(3).', '7', '9', '1', '4', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(3) = (3)² - 2 = 9 - 2 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x², find f(3).', '6', '3', '12', '9', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(3) = (3)² = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 9, find f(5).', '25', '14', '19', '34', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = (5)² + 9 = 25 + 9 = 34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 10, find f(5).', '15', '20', '25', '35', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(5) = (5)² + 10 = 25 + 10 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 7, find f(6).', '13', '36', '43', '19', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(6) = (6)² + 7 = 36 + 7 = 43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 6, find f(6).', '36', '18', '42', '12', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(6) = (6)² + 6 = 36 + 6 = 42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x², find f(6).', '6', '12', '42', '36', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(6) = (6)² = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 3, find f(2).', '9', '5', '4', '7', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(2) = (2)² + 3 = 4 + 3 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 1, find f(2).', '3', '7', '4', '5', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(2) = (2)² + 1 = 4 + 1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 3, find f(2).', '5', '9', '7', '4', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(2) = (2)² + 3 = 4 + 3 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 7x + 12, find f(0).', '0', '12', '7', '19', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 7(0) + 12 = 0 + 12 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 4, find f(0).', '4', '2', '6', '0', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 2(0) + 4 = 0 + 4 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1, find f(0).', '1', '4', '3', '0', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 3(0) + 1 = 0 + 1 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 4, find f(0).', '4', '0', '-4', '8', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 4(0) + 4 = 0 + 4 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 6x + 13, find f(0).', '0', '6', '19', '13', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 6(0) + 13 = 0 + 13 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1, find f(0).', '0', '4', '3', '1', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 3(0) + 1 = 0 + 1 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 7x + 8, find f(0).', '7', '15', '8', '0', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 7(0) + 8 = 0 + 8 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 13, find f(0).', '0', '17', '4', '13', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 4(0) + 13 = 0 + 13 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 6x + 2, find f(0).', '2', '0', '6', '8', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 6(0) + 2 = 0 + 2 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 10, find f(0).', '0', '14', '10', '4', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(0) = 4(0) + 10 = 0 + 10 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 6x + 9, find f(-3).', '9', '27', '-9', '-27', 2,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-3) = 6(-3) + 9 = -18 + 9 = -9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 9, find f(-4).', '7', '-29', '29', '-11', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-4) = 5(-4) + 9 = -20 + 9 = -11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 2, find f(-4).', '-10', '10', '-2', '-6', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-4) = 2(-4) + 2 = -8 + 2 = -6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 6, find f(-1).', '2', '14', '10', '-10', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-1) = 4(-1) + 6 = -4 + 6 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 9, find f(-5).', '-6', '24', '-24', '12', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-5) = 3(-5) + 9 = -15 + 9 = -6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 6x + 7, find f(-1).', '15', '-13', '13', '1', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-1) = 6(-1) + 7 = -6 + 7 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3, find f(-5).', '-12', '18', '-18', '-6', 0,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-5) = 3(-5) + 3 = -15 + 3 = -12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 10, find f(-2).', '-18', '22', '18', '2', 3,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-2) = 4(-2) + 10 = -8 + 10 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 7, find f(-1).', '10', '4', '-10', '18', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-1) = 3(-1) + 7 = -3 + 7 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 1, find f(-2).', '5', '-3', '-5', '-1', 1,
'lc_hl_functions', 1, 'foundation', 'lc_hl', 'f(-2) = 2(-2) + 1 = -4 + 1 = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 5x - 8?', 'x ≠ 0', 'x > 0', 'x ≥ 0', 'All real numbers (ℝ)', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 6x - 2?', 'All real numbers (ℝ)', 'x > 0', 'x ≠ 0', 'x ≥ 0', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 5x - 4?', 'x > 0', 'x ≠ 0', 'x ≥ 0', 'All real numbers (ℝ)', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 2x - 4?', 'x > 0', 'x ≥ 0', 'All real numbers (ℝ)', 'x ≠ 0', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 6x + 6?', 'All real numbers (ℝ)', 'x ≥ 0', 'x ≠ 0', 'x > 0', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 10x - 9?', 'x ≥ 0', 'All real numbers (ℝ)', 'x > 0', 'x ≠ 0', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 7x + 0?', 'All real numbers (ℝ)', 'x ≠ 0', 'x > 0', 'x ≥ 0', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 8x + 0?', 'x ≠ 0', 'All real numbers (ℝ)', 'x > 0', 'x ≥ 0', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 5x - 9?', 'x ≥ 0', 'All real numbers (ℝ)', 'x > 0', 'x ≠ 0', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 2x - 9?', 'All real numbers (ℝ)', 'x > 0', 'x ≠ 0', 'x ≥ 0', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 5)?', 'x > -5', 'All real numbers (ℝ)', 'x ≤ -5', 'x ≥ -5', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 5) to be defined, we need x + 5 ≥ 0, so x ≥ -5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 5)?', 'x ≥ -5', 'x ≤ -5', 'x > -5', 'All real numbers (ℝ)', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 5) to be defined, we need x + 5 ≥ 0, so x ≥ -5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 2)?', 'x ≥ -2', 'x ≤ -2', 'x > -2', 'All real numbers (ℝ)', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 2) to be defined, we need x + 2 ≥ 0, so x ≥ -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 7)?', 'x > -7', 'x ≤ -7', 'x ≥ -7', 'All real numbers (ℝ)', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 7) to be defined, we need x + 7 ≥ 0, so x ≥ -7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 8)?', 'x ≥ -8', 'All real numbers (ℝ)', 'x ≤ -8', 'x > -8', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 8) to be defined, we need x + 8 ≥ 0, so x ≥ -8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 1)?', 'x ≤ -1', 'x ≥ -1', 'All real numbers (ℝ)', 'x > -1', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 1) to be defined, we need x + 1 ≥ 0, so x ≥ -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 7)?', 'x > -7', 'x ≥ -7', 'All real numbers (ℝ)', 'x ≤ -7', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 7) to be defined, we need x + 7 ≥ 0, so x ≥ -7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 4)?', 'x > -4', 'All real numbers (ℝ)', 'x ≥ -4', 'x ≤ -4', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 4) to be defined, we need x + 4 ≥ 0, so x ≥ -4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 2)?', 'All real numbers (ℝ)', 'x > -2', 'x ≥ -2', 'x ≤ -2', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 2) to be defined, we need x + 2 ≥ 0, so x ≥ -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 5)?', 'All real numbers (ℝ)', 'x ≥ -5', 'x > -5', 'x ≤ -5', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 5) to be defined, we need x + 5 ≥ 0, so x ≥ -5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 3)?', 'x ≤ -3', 'x ≥ -3', 'x > -3', 'All real numbers (ℝ)', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 3) to be defined, we need x + 3 ≥ 0, so x ≥ -3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = √(x + 8)?', 'x ≤ -8', 'x > -8', 'x ≥ -8', 'All real numbers (ℝ)', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For √(x + 8) to be defined, we need x + 8 ≥ 0, so x ≥ -8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 1)?', 'x > 1', 'All real numbers (ℝ)', 'x ≠ 1', 'x ≥ 1', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 1) to be defined, we need x - 1 ≠ 0, so x ≠ 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 2)?', 'x > 2', 'All real numbers (ℝ)', 'x ≠ 2', 'x ≥ 2', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 2) to be defined, we need x - 2 ≠ 0, so x ≠ 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 2)?', 'All real numbers (ℝ)', 'x ≥ 2', 'x > 2', 'x ≠ 2', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 2) to be defined, we need x - 2 ≠ 0, so x ≠ 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 1)?', 'x ≠ 1', 'x > 1', 'All real numbers (ℝ)', 'x ≥ 1', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 1) to be defined, we need x - 1 ≠ 0, so x ≠ 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 1)?', 'x > 1', 'x ≠ 1', 'All real numbers (ℝ)', 'x ≥ 1', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 1) to be defined, we need x - 1 ≠ 0, so x ≠ 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 3)?', 'All real numbers (ℝ)', 'x > 3', 'x ≥ 3', 'x ≠ 3', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 3) to be defined, we need x - 3 ≠ 0, so x ≠ 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 4)?', 'x ≥ 4', 'x > 4', 'All real numbers (ℝ)', 'x ≠ 4', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 4) to be defined, we need x - 4 ≠ 0, so x ≠ 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 4)?', 'All real numbers (ℝ)', 'x > 4', 'x ≠ 4', 'x ≥ 4', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 4) to be defined, we need x - 4 ≠ 0, so x ≠ 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 6)?', 'x ≠ 6', 'All real numbers (ℝ)', 'x > 6', 'x ≥ 6', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 6) to be defined, we need x - 6 ≠ 0, so x ≠ 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 1/(x - 6)?', 'x > 6', 'x ≥ 6', 'All real numbers (ℝ)', 'x ≠ 6', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For 1/(x - 6) to be defined, we need x - 6 ≠ 0, so x ≠ 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² - 2?', 'y > -2', 'All real numbers (ℝ)', 'y ≥ -2', 'y ≤ -2', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² - 2, the minimum value is -2 (at x = 0), so the range is y ≥ -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 2?', 'y ≥ 2', 'y > 2', 'All real numbers (ℝ)', 'y ≤ 2', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 2, the minimum value is 2 (at x = 0), so the range is y ≥ 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 5?', 'y > 5', 'y ≤ 5', 'All real numbers (ℝ)', 'y ≥ 5', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 5, the minimum value is 5 (at x = 0), so the range is y ≥ 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 4?', 'All real numbers (ℝ)', 'y ≤ 4', 'y ≥ 4', 'y > 4', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 4, the minimum value is 4 (at x = 0), so the range is y ≥ 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 5?', 'y > 5', 'y ≥ 5', 'All real numbers (ℝ)', 'y ≤ 5', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 5, the minimum value is 5 (at x = 0), so the range is y ≥ 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² - 5?', 'All real numbers (ℝ)', 'y ≤ -5', 'y > -5', 'y ≥ -5', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² - 5, the minimum value is -5 (at x = 0), so the range is y ≥ -5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 3?', 'y > 3', 'y ≥ 3', 'y ≤ 3', 'All real numbers (ℝ)', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 3, the minimum value is 3 (at x = 0), so the range is y ≥ 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 5?', 'y > 5', 'y ≤ 5', 'All real numbers (ℝ)', 'y ≥ 5', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 5, the minimum value is 5 (at x = 0), so the range is y ≥ 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 2?', 'y > 2', 'y ≤ 2', 'y ≥ 2', 'All real numbers (ℝ)', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 2, the minimum value is 2 (at x = 0), so the range is y ≥ 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = x² + 3?', 'y > 3', 'All real numbers (ℝ)', 'y ≤ 3', 'y ≥ 3', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'For f(x) = x² + 3, the minimum value is 3 (at x = 0), so the range is y ≥ 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 3x + 1?', 'y > 0', 'y ≥ 0', 'y ≥ 1', 'All real numbers (ℝ)', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 5x - 2?', 'y > 0', 'y ≥ 0', 'All real numbers (ℝ)', 'y ≥ -2', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 8x - 4?', 'y ≥ 0', 'y > 0', 'y ≥ -4', 'All real numbers (ℝ)', 3,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 4x + 2?', 'y > 0', 'y ≥ 0', 'All real numbers (ℝ)', 'y ≥ 2', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 3x + 4?', 'y > 0', 'All real numbers (ℝ)', 'y ≥ 0', 'y ≥ 4', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 4x + 0?', 'y > 0', 'Option 4', 'All real numbers (ℝ)', 'y ≥ 0', 2,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 6x - 1?', 'y > 0', 'All real numbers (ℝ)', 'y ≥ 0', 'y ≥ -1', 1,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 4x - 1?', 'All real numbers (ℝ)', 'y ≥ 0', 'y > 0', 'y ≥ -1', 0,
'lc_hl_functions', 2, 'foundation', 'lc_hl', 'A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 6 and g(x) = 4x + 2, find f(g(x)).', '4x + 4', '6x + 8', '8x + 6', '8x + 10', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 2) = 2(4x + 2) + 6 = 8x + 4 + 6 = 8x + 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 3 and g(x) = 4x + 4, find f(g(x)).', '16x + 3', '16x + 19', '8x + 7', '4x + 16', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 4) = 4(4x + 4) + 3 = 16x + 16 + 3 = 16x + 19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 4 and g(x) = 2x + 4, find f(g(x)).', '2x + 16', '6x + 8', '8x + 20', '8x + 4', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(2x + 4) = 4(2x + 4) + 4 = 8x + 16 + 4 = 8x + 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 3 and g(x) = 2x + 3, find f(g(x)).', '4x + 3', '4x + 9', '4x + 6', '2x + 6', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(2x + 3) = 2(2x + 3) + 3 = 4x + 6 + 3 = 4x + 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 1 and g(x) = 4x + 1, find f(g(x)).', '20x + 1', '4x + 5', '20x + 6', '9x + 2', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 1) = 5(4x + 1) + 1 = 20x + 5 + 1 = 20x + 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 6 and g(x) = 2x + 1, find f(g(x)).', '8x + 6', '2x + 4', '6x + 7', '8x + 10', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(2x + 1) = 4(2x + 1) + 6 = 8x + 4 + 6 = 8x + 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 3 and g(x) = 3x + 2, find f(g(x)).', '6x + 3', '3x + 4', '5x + 5', '6x + 7', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(3x + 2) = 2(3x + 2) + 3 = 6x + 4 + 3 = 6x + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3 and g(x) = 2x + 4, find f(g(x)).', '6x + 3', '6x + 15', '5x + 7', '2x + 12', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(2x + 4) = 3(2x + 4) + 3 = 6x + 12 + 3 = 6x + 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 6 and g(x) = 4x + 5, find f(g(x)).', '8x + 11', '4x + 20', '16x + 6', '16x + 26', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 5) = 4(4x + 5) + 6 = 16x + 20 + 6 = 16x + 26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 6 and g(x) = 4x + 1, find f(g(x)).', '12x + 9', '7x + 7', '12x + 6', '4x + 3', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 1) = 3(4x + 1) + 6 = 12x + 3 + 6 = 12x + 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 2 and g(x) = 4x + 3, find f(g(x)).', '4x + 9', '12x + 2', '12x + 11', '7x + 5', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 3) = 3(4x + 3) + 2 = 12x + 9 + 2 = 12x + 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 6 and g(x) = 4x + 3, find f(g(x)).', '8x + 9', '4x + 12', '16x + 6', '16x + 18', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 3) = 4(4x + 3) + 6 = 16x + 12 + 6 = 16x + 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 6 and g(x) = 2x + 1, find f(g(x)).', '7x + 7', '10x + 6', '2x + 5', '10x + 11', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(2x + 1) = 5(2x + 1) + 6 = 10x + 5 + 6 = 10x + 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 3 and g(x) = 4x + 1, find f(g(x)).', '16x + 3', '8x + 4', '4x + 4', '16x + 7', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(4x + 1) = 4(4x + 1) + 3 = 16x + 4 + 3 = 16x + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 1 and g(x) = 2x + 1, find f(g(x)).', '8x + 1', '2x + 4', '6x + 2', '8x + 5', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(g(x)) = f(2x + 1) = 4(2x + 1) + 1 = 8x + 4 + 1 = 8x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 6 and g(x) = 3x + 3, find g(f(x)).', '9x + 21', '9x + 3', '6x + 9', '3x + 18', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(3x + 6) = 3(3x + 6) + 3 = 9x + 18 + 3 = 9x + 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 1 and g(x) = 2x + 4, find g(f(x)).', '2x + 2', '4x + 6', '4x + 5', '4x + 4', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(2x + 1) = 2(2x + 1) + 4 = 4x + 2 + 4 = 4x + 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 3 and g(x) = 3x + 2, find g(f(x)).', '12x + 2', '12x + 11', '7x + 5', '4x + 9', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(4x + 3) = 3(4x + 3) + 2 = 12x + 9 + 2 = 12x + 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 4 and g(x) = 4x + 4, find g(f(x)).', '16x + 20', '8x + 8', '16x + 4', '4x + 16', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(4x + 4) = 4(4x + 4) + 4 = 16x + 16 + 4 = 16x + 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1 and g(x) = 2x + 3, find g(f(x)).', '6x + 3', '3x + 2', '6x + 5', '5x + 4', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(3x + 1) = 2(3x + 1) + 3 = 6x + 2 + 3 = 6x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3 and g(x) = 3x + 3, find g(f(x)).', '9x + 12', '3x + 9', '9x + 3', '6x + 6', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(3x + 3) = 3(3x + 3) + 3 = 9x + 9 + 3 = 9x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 6 and g(x) = 2x + 2, find g(f(x)).', '6x + 14', '3x + 12', '6x + 2', '5x + 8', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(3x + 6) = 2(3x + 6) + 2 = 6x + 12 + 2 = 6x + 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 5 and g(x) = 2x + 5, find g(f(x)).', '10x + 15', '7x + 10', '10x + 5', '5x + 10', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(5x + 5) = 2(5x + 5) + 5 = 10x + 10 + 5 = 10x + 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 3 and g(x) = 3x + 1, find g(f(x)).', '15x + 10', '15x + 1', '5x + 9', '8x + 4', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(5x + 3) = 3(5x + 3) + 1 = 15x + 9 + 1 = 15x + 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1 and g(x) = 3x + 4, find g(f(x)).', '3x + 3', '9x + 4', '9x + 7', '6x + 5', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(3x + 1) = 3(3x + 1) + 4 = 9x + 3 + 4 = 9x + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 4 and g(x) = 4x + 3, find g(f(x)).', '20x + 19', '5x + 16', '20x + 3', '9x + 7', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(5x + 4) = 4(5x + 4) + 3 = 20x + 16 + 3 = 20x + 19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 3 and g(x) = 3x + 4, find g(f(x)).', '12x + 4', '4x + 9', '7x + 7', '12x + 13', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(4x + 3) = 3(4x + 3) + 4 = 12x + 9 + 4 = 12x + 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 3 and g(x) = 2x + 3, find g(f(x)).', '10x + 9', '5x + 6', '10x + 3', '7x + 6', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(5x + 3) = 2(5x + 3) + 3 = 10x + 6 + 3 = 10x + 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 4 and g(x) = 3x + 5, find g(f(x)).', '15x + 5', '8x + 9', '15x + 17', '5x + 12', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(5x + 4) = 3(5x + 4) + 5 = 15x + 12 + 5 = 15x + 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 5 and g(x) = 3x + 3, find g(f(x)).', '6x + 8', '3x + 15', '9x + 3', '9x + 18', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'g(f(x)) = g(3x + 5) = 3(3x + 5) + 3 = 9x + 15 + 3 = 9x + 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 3 and g(x) = 2x + 1, find f(g(3)).', '17', '12', '16', '19', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(3) = 2(3) + 1 = 7. Then f(g(3)) = f(7) = 2(7) + 3 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 5 and g(x) = 2x + 2, find f(g(2)).', '12', '28', '19', '29', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(2) = 2(2) + 2 = 6. Then f(g(2)) = f(6) = 4(6) + 5 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 3 and g(x) = 3x + 4, find f(g(1)).', '12', '17', '5', '19', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(1) = 3(1) + 4 = 7. Then f(g(1)) = f(7) = 2(7) + 3 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 5 and g(x) = 3x + 3, find f(g(2)).', '10', '23', '30', '18', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(2) = 3(2) + 3 = 9. Then f(g(2)) = f(9) = 2(9) + 5 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 4 and g(x) = 3x + 2, find f(g(1)).', '11', '5', '20', '14', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(1) = 3(1) + 2 = 5. Then f(g(1)) = f(5) = 2(5) + 4 = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 5 and g(x) = 2x + 4, find f(g(3)).', '25', '21', '12', '26', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(3) = 2(3) + 4 = 10. Then f(g(3)) = f(10) = 2(10) + 5 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 1 and g(x) = 3x + 2, find f(g(1)).', 'Option 4', '11', '8', '5', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(1) = 3(1) + 2 = 5. Then f(g(1)) = f(5) = 2(5) + 1 = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 4 and g(x) = 2x + 1, find f(g(3)).', '18', '21', '12', '17', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(3) = 2(3) + 1 = 7. Then f(g(3)) = f(7) = 2(7) + 4 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 1 and g(x) = 3x + 1, find f(g(1)).', '9', '17', '7', '16', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(1) = 3(1) + 1 = 4. Then f(g(1)) = f(4) = 4(4) + 1 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 4 and g(x) = 3x + 4, find f(g(1)).', 'Option 4', '25', '14', '6', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'First find g(1) = 3(1) + 4 = 7. Then f(g(1)) = f(7) = 3(7) + 4 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3, find f(f(x)).', '6x + 6', '9x + 12', '3x + 6', '9x + 3', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(3x + 3) = 3(3x + 3) + 3 = 9x + 9 + 3 = 9x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 2, find f(f(x)).', '4x + 6', '4x + 2', '2x + 4', '4x + 4', 0,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(2x + 2) = 2(2x + 2) + 2 = 4x + 4 + 2 = 4x + 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3, find f(f(x)).', '3x + 6', '9x + 3', '9x + 12', '6x + 6', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(3x + 3) = 3(3x + 3) + 3 = 9x + 9 + 3 = 9x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1, find f(f(x)).', '6x + 2', '9x + 4', '3x + 2', '9x + 1', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(3x + 1) = 3(3x + 1) + 1 = 9x + 3 + 1 = 9x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 2, find f(f(x)).', '4x + 2', '4x + 6', '4x + 4', '2x + 4', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(2x + 2) = 2(2x + 2) + 2 = 4x + 4 + 2 = 4x + 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 2, find f(f(x)).', '3x + 4', '6x + 4', '9x + 8', '9x + 2', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(3x + 2) = 3(3x + 2) + 2 = 9x + 6 + 2 = 9x + 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1, find f(f(x)).', '9x + 1', '6x + 2', '9x + 4', '3x + 2', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(3x + 1) = 3(3x + 1) + 1 = 9x + 3 + 1 = 9x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 4, find f(f(x)).', '2x + 8', '4x + 8', '4x + 4', '4x + 12', 3,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(2x + 4) = 2(2x + 4) + 4 = 4x + 8 + 4 = 4x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1, find f(f(x)).', '3x + 2', '9x + 4', '6x + 2', '9x + 1', 1,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(3x + 1) = 3(3x + 1) + 1 = 9x + 3 + 1 = 9x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 4, find f(f(x)).', '6x + 8', '3x + 8', '9x + 16', '9x + 4', 2,
'lc_hl_functions', 3, 'foundation', 'lc_hl', 'f(f(x)) = f(3x + 4) = 3(3x + 4) + 4 = 9x + 12 + 4 = 9x + 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 5x + 6.', '5x - 6', '(x + 6)/5', 'x/5 + 6', '(x - 6)/5', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 5x + 6. Swap x and y: x = 5y + 6. Solve for y: 5y = x - 6, so y = (x - 6)/5. Therefore f⁻¹(x) = (x - 6)/5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 2x + 3.', '(x + 3)/2', '(x - 3)/2', 'x/2 + 3', '2x - 3', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 2x + 3. Swap x and y: x = 2y + 3. Solve for y: 2y = x - 3, so y = (x - 3)/2. Therefore f⁻¹(x) = (x - 3)/2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 4x + 9.', 'x/4 + 9', '4x - 9', '(x + 9)/4', '(x - 9)/4', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 4x + 9. Swap x and y: x = 4y + 9. Solve for y: 4y = x - 9, so y = (x - 9)/4. Therefore f⁻¹(x) = (x - 9)/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 4x + 4.', '(x + 4)/4', '4x - 4', '(x - 4)/4', 'x/4 + 4', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 4x + 4. Swap x and y: x = 4y + 4. Solve for y: 4y = x - 4, so y = (x - 4)/4. Therefore f⁻¹(x) = (x - 4)/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 4x + 5.', '(x + 5)/4', 'x/4 + 5', '4x - 5', '(x - 5)/4', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 4x + 5. Swap x and y: x = 4y + 5. Solve for y: 4y = x - 5, so y = (x - 5)/4. Therefore f⁻¹(x) = (x - 5)/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 5x + 4.', '(x + 4)/5', '(x - 4)/5', '5x - 4', 'x/5 + 4', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 5x + 4. Swap x and y: x = 5y + 4. Solve for y: 5y = x - 4, so y = (x - 4)/5. Therefore f⁻¹(x) = (x - 4)/5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 2x + 4.', 'x/2 + 4', '(x - 4)/2', '2x - 4', '(x + 4)/2', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 2x + 4. Swap x and y: x = 2y + 4. Solve for y: 2y = x - 4, so y = (x - 4)/2. Therefore f⁻¹(x) = (x - 4)/2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 3x + 2.', '(x + 2)/3', 'x/3 + 2', '(x - 2)/3', '3x - 2', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 3x + 2. Swap x and y: x = 3y + 2. Solve for y: 3y = x - 2, so y = (x - 2)/3. Therefore f⁻¹(x) = (x - 2)/3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 2x + 5.', '2x - 5', 'x/2 + 5', '(x - 5)/2', '(x + 5)/2', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 2x + 5. Swap x and y: x = 2y + 5. Solve for y: 2y = x - 5, so y = (x - 5)/2. Therefore f⁻¹(x) = (x - 5)/2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 5x + 5.', '5x - 5', '(x + 5)/5', '(x - 5)/5', 'x/5 + 5', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 5x + 5. Swap x and y: x = 5y + 5. Solve for y: 5y = x - 5, so y = (x - 5)/5. Therefore f⁻¹(x) = (x - 5)/5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 4x + 6.', 'x/4 + 6', '(x - 6)/4', '4x - 6', '(x + 6)/4', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 4x + 6. Swap x and y: x = 4y + 6. Solve for y: 4y = x - 6, so y = (x - 6)/4. Therefore f⁻¹(x) = (x - 6)/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 3x + 6.', 'x/3 + 6', '(x + 6)/3', '3x - 6', '(x - 6)/3', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 3x + 6. Swap x and y: x = 3y + 6. Solve for y: 3y = x - 6, so y = (x - 6)/3. Therefore f⁻¹(x) = (x - 6)/3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 2x + 1.', '(x + 1)/2', '(x - 1)/2', 'x/2 + 1', '2x - 1', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 2x + 1. Swap x and y: x = 2y + 1. Solve for y: 2y = x - 1, so y = (x - 1)/2. Therefore f⁻¹(x) = (x - 1)/2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 6x + 8.', 'x/6 + 8', '(x - 8)/6', '(x + 8)/6', '6x - 8', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 6x + 8. Swap x and y: x = 6y + 8. Solve for y: 6y = x - 8, so y = (x - 8)/6. Therefore f⁻¹(x) = (x - 8)/6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = 3x + 5.', '3x - 5', '(x - 5)/3', 'x/3 + 5', '(x + 5)/3', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = 3x + 5. Swap x and y: x = 3y + 5. Solve for y: 3y = x - 5, so y = (x - 5)/3. Therefore f⁻¹(x) = (x - 5)/3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 4)/5.', '5x - 4', 'x/5 + 4', '(x + 4)/5', '5x + 4', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 4)/5. Swap x and y: x = (y - 4)/5. Solve for y: 5x = y - 4, so y = 5x + 4. Therefore f⁻¹(x) = 5x + 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 1)/3.', '3x + 1', '3x - 1', '(x + 1)/3', 'x/3 + 1', 0,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 1)/3. Swap x and y: x = (y - 1)/3. Solve for y: 3x = y - 1, so y = 3x + 1. Therefore f⁻¹(x) = 3x + 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 7)/2.', '2x + 7', '2x - 7', '(x + 7)/2', 'x/2 + 7', 0,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 7)/2. Swap x and y: x = (y - 7)/2. Solve for y: 2x = y - 7, so y = 2x + 7. Therefore f⁻¹(x) = 2x + 7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 1)/5.', '(x + 1)/5', '5x - 1', '5x + 1', 'x/5 + 1', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 1)/5. Swap x and y: x = (y - 1)/5. Solve for y: 5x = y - 1, so y = 5x + 1. Therefore f⁻¹(x) = 5x + 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 7)/2.', '2x - 7', 'x/2 + 7', '2x + 7', '(x + 7)/2', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 7)/2. Swap x and y: x = (y - 7)/2. Solve for y: 2x = y - 7, so y = 2x + 7. Therefore f⁻¹(x) = 2x + 7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 5)/5.', 'x/5 + 5', '5x + 5', '(x + 5)/5', '5x - 5', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 5)/5. Swap x and y: x = (y - 5)/5. Solve for y: 5x = y - 5, so y = 5x + 5. Therefore f⁻¹(x) = 5x + 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 7)/2.', '2x - 7', '2x + 7', 'x/2 + 7', '(x + 7)/2', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 7)/2. Swap x and y: x = (y - 7)/2. Solve for y: 2x = y - 7, so y = 2x + 7. Therefore f⁻¹(x) = 2x + 7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 2)/2.', '(x + 2)/2', '2x - 2', '2x + 2', 'x/2 + 2', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 2)/2. Swap x and y: x = (y - 2)/2. Solve for y: 2x = y - 2, so y = 2x + 2. Therefore f⁻¹(x) = 2x + 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 6)/3.', '3x - 6', '3x + 6', 'x/3 + 6', '(x + 6)/3', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 6)/3. Swap x and y: x = (y - 6)/3. Solve for y: 3x = y - 6, so y = 3x + 6. Therefore f⁻¹(x) = 3x + 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the inverse function f⁻¹(x) if f(x) = (x - 1)/4.', '(x + 1)/4', '4x + 1', '4x - 1', 'x/4 + 1', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'Let y = (x - 1)/4. Swap x and y: x = (y - 1)/4. Solve for y: 4x = y - 1, so y = 4x + 1. Therefore f⁻¹(x) = 4x + 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 4, find f⁻¹(16).', '7', '3', '2', '4', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 4)/4. So f⁻¹(16) = (16 - 4)/4 = 12/4 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 7, find f⁻¹(9).', '3', '0', '1', '4', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 7)/2. So f⁻¹(9) = (9 - 7)/2 = 2/2 = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 1, find f⁻¹(5).', '1', 'Option 4', '5', '0', 0,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 1)/4. So f⁻¹(5) = (5 - 1)/4 = 4/4 = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 5, find f⁻¹(25).', '5', '3', '9', '4', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 5)/5. So f⁻¹(25) = (25 - 5)/5 = 20/5 = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 4, find f⁻¹(7).', '4', '2', '0', '1', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 4)/3. So f⁻¹(7) = (7 - 4)/3 = 3/3 = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3, find f⁻¹(15).', '3', '7', '5', '4', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 3)/3. So f⁻¹(15) = (15 - 3)/3 = 12/3 = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 1, find f⁻¹(3).', '0', '3', 'Option 4', '1', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 1)/2. So f⁻¹(3) = (3 - 1)/2 = 2/2 = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 7, find f⁻¹(11).', '2', '5', '4', '1', 0,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 7)/2. So f⁻¹(11) = (11 - 7)/2 = 4/2 = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 4, find f⁻¹(19).', '3', '8', '2', 'Option 4', 0,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 4)/5. So f⁻¹(19) = (19 - 4)/5 = 15/5 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 6, find f⁻¹(18).', '7', '4', '6', '3', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 6)/3. So f⁻¹(18) = (18 - 6)/3 = 12/3 = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 3, find f⁻¹(18).', '3', '8', '2', 'Option 4', 0,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 3)/5. So f⁻¹(18) = (18 - 3)/5 = 15/5 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 5, find f⁻¹(17).', '4', '3', '2', '7', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 5)/4. So f⁻¹(17) = (17 - 5)/4 = 12/4 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 8, find f⁻¹(14).', '5', '2', '7', '3', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 8)/2. So f⁻¹(14) = (14 - 8)/2 = 6/2 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 7, find f⁻¹(22).', '4', '8', '2', '3', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 7)/5. So f⁻¹(22) = (22 - 7)/5 = 15/5 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 6, find f⁻¹(18).', '6', '7', '3', '4', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'f⁻¹(x) = (x - 6)/3. So f⁻¹(18) = (18 - 6)/3 = 12/3 = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 3, find f⁻¹(f(5)).', '23', '20', '5', '8', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(5) = 4(5) + 3 = 23. Then f⁻¹(23) = (23 - 3)/4 = 20/4 = 5. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3, find f⁻¹(f(4)).', '15', '4', '12', '7', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(4) = 3(4) + 3 = 15. Then f⁻¹(15) = (15 - 3)/3 = 12/3 = 4. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1, find f⁻¹(f(4)).', '5', '4', '12', '13', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(4) = 3(4) + 1 = 13. Then f⁻¹(13) = (13 - 1)/3 = 12/3 = 4. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 5, find f⁻¹(f(4)).', '9', '4', '13', '8', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(4) = 2(4) + 5 = 13. Then f⁻¹(13) = (13 - 5)/2 = 8/2 = 4. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 5, find f⁻¹(f(1)).', '9', '6', '4', '1', 3,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(1) = 4(1) + 5 = 9. Then f⁻¹(9) = (9 - 5)/4 = 4/4 = 1. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 5, find f⁻¹(f(5)).', '5', '15', '20', '10', 0,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(5) = 3(5) + 5 = 20. Then f⁻¹(20) = (20 - 5)/3 = 15/3 = 5. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 6, find f⁻¹(f(3)).', '18', '9', '3', '12', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(3) = 4(3) + 6 = 18. Then f⁻¹(18) = (18 - 6)/4 = 12/4 = 3. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 1, find f⁻¹(f(5)).', '6', '5', '20', '21', 1,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(5) = 4(5) + 1 = 21. Then f⁻¹(21) = (21 - 1)/4 = 20/4 = 5. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 6, find f⁻¹(f(3)).', '12', '6', '3', '9', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(3) = 2(3) + 6 = 12. Then f⁻¹(12) = (12 - 6)/2 = 6/2 = 3. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 2, find f⁻¹(f(1)).', '3', '6', '1', '4', 2,
'lc_hl_functions', 4, 'developing', 'lc_hl', 'First, f(1) = 4(1) + 2 = 6. Then f⁻¹(6) = (6 - 2)/4 = 4/4 = 1. This verifies f⁻¹(f(x)) = x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units to the right. What is the equation of the new graph?', 'f(x - 1)', 'f(x) + 1', 'f(x) - 1', 'f(x + 1)', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 1 units to the right is given by f(x - 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units to the left. What is the equation of the new graph?', 'f(x) - 3', 'f(x - 3)', 'f(x) + 3', 'f(x + 3)', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 3 units to the left is given by f(x + 3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 4 units to the right. What is the equation of the new graph?', 'f(x) + 4', 'f(x) - 4', 'f(x - 4)', 'f(x + 4)', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 4 units to the right is given by f(x - 4).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 6 units to the right. What is the equation of the new graph?', 'f(x + 6)', 'f(x - 6)', 'f(x) - 6', 'f(x) + 6', 1,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 6 units to the right is given by f(x - 6).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 2 units to the left. What is the equation of the new graph?', 'f(x) + 2', 'f(x - 2)', 'f(x) - 2', 'f(x + 2)', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 2 units to the left is given by f(x + 2).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units to the left. What is the equation of the new graph?', 'f(x - 3)', 'f(x) - 3', 'f(x) + 3', 'f(x + 3)', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 3 units to the left is given by f(x + 3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 2 units to the right. What is the equation of the new graph?', 'f(x - 2)', 'f(x) - 2', 'f(x + 2)', 'f(x) + 2', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 2 units to the right is given by f(x - 2).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units to the right. What is the equation of the new graph?', 'f(x) + 1', 'f(x - 1)', 'f(x + 1)', 'f(x) - 1', 1,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 1 units to the right is given by f(x - 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units to the left. What is the equation of the new graph?', 'f(x - 1)', 'f(x + 1)', 'f(x) + 1', 'f(x) - 1', 1,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 1 units to the left is given by f(x + 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 4 units to the right. What is the equation of the new graph?', 'f(x - 4)', 'f(x + 4)', 'f(x) - 4', 'f(x) + 4', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 4 units to the right is given by f(x - 4).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units to the left. What is the equation of the new graph?', 'f(x - 3)', 'f(x) - 3', 'f(x + 3)', 'f(x) + 3', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 3 units to the left is given by f(x + 3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units to the right. What is the equation of the new graph?', 'f(x + 3)', 'f(x - 3)', 'f(x) + 3', 'f(x) - 3', 1,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A horizontal translation 3 units to the right is given by f(x - 3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 6 units down. What is the equation of the new graph?', 'f(x + 6)', 'f(x - 6)', 'f(x) + 6', 'f(x) - 6', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 6 units down is given by f(x) - 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units up. What is the equation of the new graph?', 'f(x) + 1', 'f(x - 1)', 'f(x + 1)', 'f(x) - 1', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 1 units up is given by f(x) + 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units up. What is the equation of the new graph?', 'f(x - 3)', 'f(x + 3)', 'f(x) - 3', 'f(x) + 3', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 3 units up is given by f(x) + 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 6 units up. What is the equation of the new graph?', 'f(x) + 6', 'f(x + 6)', 'f(x - 6)', 'f(x) - 6', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 6 units up is given by f(x) + 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units up. What is the equation of the new graph?', 'f(x) - 3', 'f(x + 3)', 'f(x - 3)', 'f(x) + 3', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 3 units up is given by f(x) + 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 6 units up. What is the equation of the new graph?', 'f(x) - 6', 'f(x + 6)', 'f(x - 6)', 'f(x) + 6', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 6 units up is given by f(x) + 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 5 units down. What is the equation of the new graph?', 'f(x) + 5', 'f(x - 5)', 'f(x) - 5', 'f(x + 5)', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 5 units down is given by f(x) - 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 6 units up. What is the equation of the new graph?', 'f(x) + 6', 'f(x) - 6', 'f(x - 6)', 'f(x + 6)', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 6 units up is given by f(x) + 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 7 units up. What is the equation of the new graph?', 'f(x) - 7', 'f(x - 7)', 'f(x + 7)', 'f(x) + 7', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 7 units up is given by f(x) + 7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 4 units down. What is the equation of the new graph?', 'f(x) + 4', 'f(x - 4)', 'f(x) - 4', 'f(x + 4)', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 4 units down is given by f(x) - 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units down. What is the equation of the new graph?', 'f(x) - 3', 'f(x) + 3', 'f(x + 3)', 'f(x - 3)', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 3 units down is given by f(x) - 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 4 units up. What is the equation of the new graph?', 'f(x) - 4', 'f(x - 4)', 'f(x) + 4', 'f(x + 4)', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'A vertical translation 4 units up is given by f(x) + 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units right and 4 units up. What is the equation of the new graph?', 'f(x - 3) + 4', 'f(x + 3) + 4', 'f(x + 3) - 4', 'f(x - 3) - 4', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 3 units right uses f(x - 3). Moving 4 units up adds + 4. Combined: f(x - 3) + 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 5 units right and 2 units up. What is the equation of the new graph?', 'f(x - 5) + 2', 'f(x + 5) + 2', 'f(x + 5) - 2', 'f(x - 5) - 2', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 5 units right uses f(x - 5). Moving 2 units up adds + 2. Combined: f(x - 5) + 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 4 units left and 5 units down. What is the equation of the new graph?', 'f(x + 4) + 5', 'f(x + 4) - 5', 'f(x - 4) + 5', 'f(x - 4) - 5', 1,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 4 units left uses f(x + 4). Moving 5 units down adds - 5. Combined: f(x + 4) - 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units right and 5 units up. What is the equation of the new graph?', 'f(x - 1) + 5', 'f(x + 1) - 5', 'f(x + 1) + 5', 'f(x - 1) - 5', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 1 units right uses f(x - 1). Moving 5 units up adds + 5. Combined: f(x - 1) + 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units left and 5 units down. What is the equation of the new graph?', 'f(x - 1) - 5', 'f(x - 1) + 5', 'f(x + 1) - 5', 'f(x + 1) + 5', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 1 units left uses f(x + 1). Moving 5 units down adds - 5. Combined: f(x + 1) - 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 2 units right and 4 units up. What is the equation of the new graph?', 'f(x - 2) + 4', 'f(x + 2) + 4', 'f(x - 2) - 4', 'f(x + 2) - 4', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 2 units right uses f(x - 2). Moving 4 units up adds + 4. Combined: f(x - 2) + 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units left and 3 units up. What is the equation of the new graph?', 'f(x - 1) - 3', 'f(x + 1) - 3', 'f(x + 1) + 3', 'f(x - 1) + 3', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 1 units left uses f(x + 1). Moving 3 units up adds + 3. Combined: f(x + 1) + 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 4 units left and 4 units down. What is the equation of the new graph?', 'f(x + 4) - 4', 'f(x + 4) + 4', 'f(x - 4) + 4', 'f(x - 4) - 4', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 4 units left uses f(x + 4). Moving 4 units down adds - 4. Combined: f(x + 4) - 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units right and 5 units down. What is the equation of the new graph?', 'f(x + 1) + 5', 'f(x - 1) - 5', 'f(x + 1) - 5', 'f(x - 1) + 5', 1,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 1 units right uses f(x - 1). Moving 5 units down adds - 5. Combined: f(x - 1) - 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 3 units left and 4 units down. What is the equation of the new graph?', 'f(x - 3) - 4', 'f(x + 3) - 4', 'f(x + 3) + 4', 'f(x - 3) + 4', 1,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 3 units left uses f(x + 3). Moving 4 units down adds - 4. Combined: f(x + 3) - 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 2 units left and 3 units up. What is the equation of the new graph?', 'f(x - 2) + 3', 'f(x + 2) - 3', 'f(x + 2) + 3', 'f(x - 2) - 3', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 2 units left uses f(x + 2). Moving 3 units up adds + 3. Combined: f(x + 2) + 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 1 units right and 4 units up. What is the equation of the new graph?', 'f(x - 1) + 4', 'f(x + 1) - 4', 'f(x - 1) - 4', 'f(x + 1) + 4', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 1 units right uses f(x - 1). Moving 4 units up adds + 4. Combined: f(x - 1) + 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The graph of y = f(x) is translated 4 units left and 2 units down. What is the equation of the new graph?', 'f(x + 4) + 2', 'f(x - 4) + 2', 'f(x - 4) - 2', 'f(x + 4) - 2', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'Moving 4 units left uses f(x + 4). Moving 2 units down adds - 2. Combined: f(x + 4) - 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x + 4) + 1.', '4 units left and 1 units down', '4 units right and 1 units down', '4 units right and 1 units up', '4 units left and 1 units up', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x + 4) + 1: the term (x + 4) means 4 units left, and + 1 means 1 units up.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x - 2) - 4.', '2 units left and 4 units up', '2 units left and 4 units down', '2 units right and 4 units down', '2 units right and 4 units up', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x - 2) - 4: the term (x - 2) means 2 units right, and - 4 means 4 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x - 1) + 6.', '1 units left and 6 units down', '1 units right and 6 units down', '1 units right and 6 units up', '1 units left and 6 units up', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x - 1) + 6: the term (x - 1) means 1 units right, and + 6 means 6 units up.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x + 3) - 1.', '3 units right and 1 units up', '3 units left and 1 units up', '3 units right and 1 units down', '3 units left and 1 units down', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x + 3) - 1: the term (x + 3) means 3 units left, and - 1 means 1 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x + 6) - 3.', '6 units right and 3 units down', '6 units right and 3 units up', '6 units left and 3 units up', '6 units left and 3 units down', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x + 6) - 3: the term (x + 6) means 6 units left, and - 3 means 3 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x + 4) - 6.', '4 units right and 6 units down', '4 units left and 6 units up', '4 units right and 6 units up', '4 units left and 6 units down', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x + 4) - 6: the term (x + 4) means 4 units left, and - 6 means 6 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x - 2) - 6.', '2 units right and 6 units down', '2 units right and 6 units up', '2 units left and 6 units down', '2 units left and 6 units up', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x - 2) - 6: the term (x - 2) means 2 units right, and - 6 means 6 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x + 3) + 6.', '3 units right and 6 units up', '3 units right and 6 units down', '3 units left and 6 units down', '3 units left and 6 units up', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x + 3) + 6: the term (x + 3) means 3 units left, and + 6 means 6 units up.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x - 2) - 1.', '2 units right and 1 units up', '2 units left and 1 units up', '2 units right and 1 units down', '2 units left and 1 units down', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x - 2) - 1: the term (x - 2) means 2 units right, and - 1 means 1 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x - 6) + 1.', '6 units left and 1 units down', '6 units right and 1 units down', '6 units left and 1 units up', '6 units right and 1 units up', 3,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x - 6) + 1: the term (x - 6) means 6 units right, and + 1 means 1 units up.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x + 3) - 2.', '3 units right and 2 units up', '3 units right and 2 units down', '3 units left and 2 units down', '3 units left and 2 units up', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x + 3) - 2: the term (x + 3) means 3 units left, and - 2 means 2 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x - 4) - 5.', '4 units right and 5 units down', '4 units left and 5 units up', '4 units right and 5 units up', '4 units left and 5 units down', 0,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x - 4) - 5: the term (x - 4) means 4 units right, and - 5 means 5 units down.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the translation that maps y = f(x) to y = f(x - 5) + 1.', '5 units right and 1 units down', '5 units left and 1 units down', '5 units right and 1 units up', '5 units left and 1 units up', 2,
'lc_hl_functions', 5, 'developing', 'lc_hl', 'In f(x - 5) + 1: the term (x - 5) means 5 units right, and + 1 means 1 units up.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = x², what is the equation after reflecting in the x-axis?', 'f(-x)', '-f(x) or -x²', '1/f(x)', 'f(x) - 1', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = 2x + 1, what is the equation after reflecting in the x-axis?', 'f(-x)', '1/f(x)', 'f(x) - 1', '-f(x) or -2x + 1', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = x³, what is the equation after reflecting in the x-axis?', 'f(x) - 1', 'f(-x)', '-f(x) or -x³', '1/f(x)', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = √x, what is the equation after reflecting in the x-axis?', 'f(x) - 1', 'f(-x)', '1/f(x)', '-f(x) or -√x', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = 1/x, what is the equation after reflecting in the x-axis?', 'f(x) - 1', 'f(-x)', '1/f(x)', '-f(x) or -1/x', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = sin(x), what is the equation after reflecting in the x-axis?', '-f(x) or -sin(x)', 'f(x) - 1', '1/f(x)', 'f(-x)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = cos(x), what is the equation after reflecting in the x-axis?', '-f(x) or -cos(x)', '1/f(x)', 'f(-x)', 'f(x) - 1', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = |x|, what is the equation after reflecting in the x-axis?', '-f(x) or -|x|', 'f(-x)', 'f(x) - 1', '1/f(x)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = eˣ, what is the equation after reflecting in the x-axis?', 'f(-x)', 'f(x) - 1', '-f(x) or -eˣ', '1/f(x)', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = ln(x), what is the equation after reflecting in the x-axis?', '-f(x) or -ln(x)', 'f(x) - 1', 'f(-x)', '1/f(x)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the x-axis multiplies all y-values by -1, giving -f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = x², what is the equation after reflecting in the y-axis?', '-f(x)', '-f(-x)', 'f(x) reflected', 'f(-x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = 2x + 1, what is the equation after reflecting in the y-axis?', '-f(-x)', 'f(x) reflected', '-f(x)', 'f(-x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = x³, what is the equation after reflecting in the y-axis?', 'f(x) reflected', '-f(x)', '-f(-x)', 'f(-x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = √x, what is the equation after reflecting in the y-axis?', '-f(x)', 'f(x) reflected', 'f(-x)', '-f(-x)', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = eˣ, what is the equation after reflecting in the y-axis?', '-f(-x)', '-f(x)', 'f(x) reflected', 'f(-x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = ln(x), what is the equation after reflecting in the y-axis?', 'f(-x)', '-f(x)', '-f(-x)', 'f(x) reflected', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = x² + x, what is the equation after reflecting in the y-axis?', '-f(-x)', '-f(x)', 'f(-x)', 'f(x) reflected', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = 2x, what is the equation after reflecting in the y-axis?', 'f(-x)', '-f(-x)', 'f(x) reflected', '-f(x)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = x³ - x, what is the equation after reflecting in the y-axis?', '-f(x)', '-f(-x)', 'f(-x)', 'f(x) reflected', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = f(x) = 3x + 2, what is the equation after reflecting in the y-axis?', '-f(-x)', '-f(x)', 'f(-x)', 'f(x) reflected', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'Reflection in the y-axis replaces x with -x, giving f(-x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 3?', '3f(x)', 'f(x/3)', 'f(3x)', 'f(x) + 3', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 3 multiplies all y-values by 3, giving 3f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 4?', 'f(4x)', '4f(x)', 'f(x) + 4', 'f(x/4)', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 4 multiplies all y-values by 4, giving 4f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 3?', 'f(x/3)', 'f(x) + 3', 'f(3x)', '3f(x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 3 multiplies all y-values by 3, giving 3f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 5?', 'f(5x)', 'f(x) + 5', '5f(x)', 'f(x/5)', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 5 multiplies all y-values by 5, giving 5f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 2?', 'f(x) + 2', 'f(x/2)', 'f(2x)', '2f(x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 2 multiplies all y-values by 2, giving 2f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 5?', '5f(x)', 'f(5x)', 'f(x) + 5', 'f(x/5)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 5 multiplies all y-values by 5, giving 5f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 2?', 'f(2x)', '2f(x)', 'f(x) + 2', 'f(x/2)', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 2 multiplies all y-values by 2, giving 2f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 2?', 'f(2x)', '2f(x)', 'f(x) + 2', 'f(x/2)', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 2 multiplies all y-values by 2, giving 2f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 2?', '2f(x)', 'f(x/2)', 'f(2x)', 'f(x) + 2', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 2 multiplies all y-values by 2, giving 2f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched vertically by scale factor 3?', 'f(x/3)', 'f(x) + 3', 'f(3x)', '3f(x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A vertical stretch by scale factor 3 multiplies all y-values by 3, giving 3f(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 3?', 'f(x) × 3', 'f(3x)', '3f(x)', 'f(x/3)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 3 replaces x with x/3, giving f(x/3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 3?', 'f(3x)', 'f(x) × 3', 'f(x/3)', '3f(x)', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 3 replaces x with x/3, giving f(x/3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 3?', 'f(x) × 3', '3f(x)', 'f(x/3)', 'f(3x)', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 3 replaces x with x/3, giving f(x/3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 3?', 'f(3x)', '3f(x)', 'f(x/3)', 'f(x) × 3', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 3 replaces x with x/3, giving f(x/3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 4?', 'f(4x)', 'f(x) × 4', '4f(x)', 'f(x/4)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 4 replaces x with x/4, giving f(x/4).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 3?', '3f(x)', 'f(3x)', 'f(x) × 3', 'f(x/3)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 3 replaces x with x/3, giving f(x/3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 4?', 'f(x/4)', '4f(x)', 'f(x) × 4', 'f(4x)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 4 replaces x with x/4, giving f(x/4).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 2?', 'f(x) × 2', 'f(x/2)', '2f(x)', 'f(2x)', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 2 replaces x with x/2, giving f(x/2).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 3?', 'f(3x)', '3f(x)', 'f(x) × 3', 'f(x/3)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 3 replaces x with x/3, giving f(x/3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is stretched horizontally by scale factor 4?', 'f(4x)', 'f(x/4)', 'f(x) × 4', '4f(x)', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal stretch by scale factor 4 replaces x with x/4, giving f(x/4).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/4?', 'f(4x)', 'f(x/4)', '4f(x)', 'f(x)/4', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/4 (or stretch by factor 4 towards y-axis) replaces x with 4x, giving f(4x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/2?', 'f(2x)', 'f(x/2)', 'f(x)/2', '2f(x)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/2 (or stretch by factor 2 towards y-axis) replaces x with 2x, giving f(2x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/3?', 'f(x/3)', '3f(x)', 'f(x)/3', 'f(3x)', 3,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/3 (or stretch by factor 3 towards y-axis) replaces x with 3x, giving f(3x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/3?', 'f(x/3)', '3f(x)', 'f(3x)', 'f(x)/3', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/3 (or stretch by factor 3 towards y-axis) replaces x with 3x, giving f(3x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/3?', 'f(3x)', '3f(x)', 'f(x)/3', 'f(x/3)', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/3 (or stretch by factor 3 towards y-axis) replaces x with 3x, giving f(3x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/3?', 'f(x/3)', 'f(3x)', '3f(x)', 'f(x)/3', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/3 (or stretch by factor 3 towards y-axis) replaces x with 3x, giving f(3x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/4?', '4f(x)', 'f(4x)', 'f(x/4)', 'f(x)/4', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/4 (or stretch by factor 4 towards y-axis) replaces x with 4x, giving f(4x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/4?', 'f(x)/4', 'f(x/4)', 'f(4x)', '4f(x)', 2,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/4 (or stretch by factor 4 towards y-axis) replaces x with 4x, giving f(4x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/2?', 'f(2x)', 'f(x/2)', '2f(x)', 'f(x)/2', 0,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/2 (or stretch by factor 2 towards y-axis) replaces x with 2x, giving f(2x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the equation when y = f(x) is compressed horizontally by scale factor 1/3?', 'f(x)/3', 'f(3x)', '3f(x)', 'f(x/3)', 1,
'lc_hl_functions', 6, 'developing', 'lc_hl', 'A horizontal compression by scale factor 1/3 (or stretch by factor 3 towards y-axis) replaces x with 3x, giving f(3x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 3x² - 5x + 7.', '(0, 7)', '(7, 0)', '(0, 3)', '(0, -5)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 3(0)² - 5(0) + 7 = 7. Point: (0, 7).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 1x² + 0x + 8.', '(0, 0)', '(8, 0)', '(0, 1)', '(0, 8)', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 1(0)² + 0(0) + 8 = 8. Point: (0, 8).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 3x² - 5x + 0.', 'Option 4', '(0, 3)', '(0, 0)', '(0, -5)', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 3(0)² - 5(0) + 0 = 0. Point: (0, 0).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 1x² - 3x + 6.', '(0, 1)', '(0, 6)', '(0, -3)', '(6, 0)', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 1(0)² - 3(0) + 6 = 6. Point: (0, 6).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 1x² - 2x - 1.', '(0, -2)', '(-1, 0)', '(0, 1)', '(0, -1)', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 1(0)² - 2(0) - 1 = -1. Point: (0, -1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 2x² + 3x + 5.', '(0, 2)', '(0, 3)', '(0, 5)', '(5, 0)', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 2(0)² + 3(0) + 5 = 5. Point: (0, 5).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 1x² + 0x - 6.', '(0, 0)', '(0, 1)', '(-6, 0)', '(0, -6)', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 1(0)² + 0(0) - 6 = -6. Point: (0, -6).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 1x² - 1x + 0.', 'Option 4', '(0, 0)', '(0, -1)', '(0, 1)', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 1(0)² - 1(0) + 0 = 0. Point: (0, 0).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 1x² - 4x - 1.', '(-1, 0)', '(0, -4)', '(0, 1)', '(0, -1)', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 1(0)² - 4(0) - 1 = -1. Point: (0, -1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the y-intercept of f(x) = 1x² - 1x - 3.', '(0, -3)', '(0, 1)', '(-3, 0)', '(0, -1)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The y-intercept is found by setting x = 0: f(0) = 1(0)² - 1(0) - 3 = -3. Point: (0, -3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 5)(x + 3).', 'x = -5 only', 'x = -5 and x = -3', 'x = 5 and x = 3', 'x = -8 and x = 15', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 5)(x + 3) = 0. So x = -5 or x = -3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 0)(x - 2).', 'x = 0 and x = 2', 'x = 0 and x = -2', 'x = 0 only', 'x = 2 and x = 0', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 0)(x - 2) = 0. So x = 0 or x = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 4)(x - 5).', 'x = -4 and x = 5', 'x = 1 and x = -20', 'x = 4 and x = -5', 'x = -4 only', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 4)(x - 5) = 0. So x = -4 or x = 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 0)(x - 4).', 'x = 4 and x = 0', 'x = 0 only', 'x = 0 and x = 4', 'x = 0 and x = -4', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 0)(x - 4) = 0. So x = 0 or x = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 1)(x - 5).', 'x = 1 and x = -5', 'x = 4 and x = -5', 'x = -1 and x = 5', 'x = -1 only', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 1)(x - 5) = 0. So x = -1 or x = 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 1)(x - 5).', 'x = 1 and x = -5', 'x = -1 and x = 5', 'x = -1 only', 'x = 4 and x = -5', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 1)(x - 5) = 0. So x = -1 or x = 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 2)(x - 4).', 'x = 2 and x = -8', 'x = -2 only', 'x = -2 and x = 4', 'x = 2 and x = -4', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 2)(x - 4) = 0. So x = -2 or x = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 4)(x + 2).', 'x = -4 and x = -2', 'x = -6 and x = 8', 'x = -4 only', 'x = 4 and x = 2', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 4)(x + 2) = 0. So x = -4 or x = -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 4)(x + 3).', 'x = 4 and x = 3', 'x = -7 and x = 12', 'x = -4 and x = -3', 'x = -4 only', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 4)(x + 3) = 0. So x = -4 or x = -3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercepts of f(x) = (x + 4)(x + 0).', 'x = -4 only', 'x = -4 and x = 0', 'Option 4', 'x = 4 and x = 0', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'Setting f(x) = 0: (x + 4)(x + 0) = 0. So x = -4 or x = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -(x + 2)² - 1.', '(-2, -1)', '(2, -1)', '(-2, 1)', '(-1, -2)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = -2 and k = -1, so vertex is (-2, -1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -(x - 4)² + 8.', '(-4, 8)', '(4, -8)', '(4, 8)', '(8, 4)', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 4 and k = 8, so vertex is (4, 8).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -2(x - 4)² + 2.', '(4, 2)', '(-4, 2)', '(2, 4)', '(4, -2)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 4 and k = 2, so vertex is (4, 2).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -(x + 4)² + 5.', '(-4, 5)', '(4, 5)', '(-4, -5)', '(5, -4)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = -4 and k = 5, so vertex is (-4, 5).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = (x - 1)² - 1.', '(-1, -1)', '(1, 1)', '(1, -1)', '(-1, 1)', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 1 and k = -1, so vertex is (1, -1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -2(x + 4)² - 5.', '(-5, -4)', '(4, -5)', '(-4, -5)', '(-4, 5)', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = -4 and k = -5, so vertex is (-4, -5).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -(x + 5)² - 8.', '(-8, -5)', '(5, -8)', '(-5, 8)', '(-5, -8)', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = -5 and k = -8, so vertex is (-5, -8).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = 2(x - 4)² + 6.', '(-4, 6)', '(6, 4)', '(4, -6)', '(4, 6)', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 4 and k = 6, so vertex is (4, 6).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -(x + 1)² + 1.', '(1, -1)', '(-1, -1)', '(1, 1)', '(-1, 1)', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = -1 and k = 1, so vertex is (-1, 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = 2(x - 0)² + 3.', '(0, 3)', '(0, -3)', 'Option 4', '(3, 0)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 0 and k = 3, so vertex is (0, 3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = 2(x - 4)² + 6.', '(4, 6)', '(-4, 6)', '(4, -6)', '(6, 4)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 4 and k = 6, so vertex is (4, 6).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertex of f(x) = -(x - 5)² + 3.', '(5, 3)', '(-5, 3)', '(3, 5)', '(5, -3)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 5 and k = 3, so vertex is (5, 3).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function passes through the origin and is symmetric about the y-axis?', 'y = ln(x)', 'y = x²', 'y = aˣ (a > 1)', 'y = x³', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Even polynomial (parabola): y = x².', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function passes through the origin and is symmetric about the origin?', 'y = x³', 'y = x²', 'y = ln(x)', 'y = aˣ (a > 1)', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Odd polynomial (cubic): y = x³.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function has a horizontal asymptote at y = 0 and passes through (0, 1)?', 'y = x³', 'y = aˣ (a > 1)', 'y = x²', 'y = ln(x)', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Exponential function: y = aˣ (a > 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function has a vertical asymptote at x = 0 and passes through (1, 0)?', 'y = ln(x)', 'y = x³', 'y = aˣ (a > 1)', 'y = x²', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Logarithmic function: y = ln(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function has vertical asymptote at x = 0 and horizontal asymptote at y = 0?', 'y = 1/x', 'y = x³', 'y = aˣ (a > 1)', 'y = x²', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Reciprocal function: y = 1/x.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function is always positive and has minimum at x = 0?', 'y = x³', 'y = aˣ (a > 1)', 'y = x²', 'y = ln(x)', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Quadratic (parabola): y = x².', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function has period 2π and range [-1, 1]?', 'y = x³', 'y = sin(x) or y = cos(x)', 'y = aˣ (a > 1)', 'y = x²', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Trigonometric function: y = sin(x) or y = cos(x).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function approaches but never touches the x-axis as x → ∞?', 'y = aˣ (a > 1)', 'y = aˣ (0 < a < 1)', 'y = x³', 'y = x²', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Exponential decay: y = aˣ (0 < a < 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function has a V-shape with vertex at the origin?', 'y = aˣ (a > 1)', 'y = x³', 'y = x²', 'y = |x|', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Absolute value function: y = |x|.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which function is always increasing and passes through (0, 1)?', 'y = x³', 'y = aˣ (a > 1)', 'y = eˣ', 'y = x²', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'The description matches a Natural exponential function: y = eˣ.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = 2x² - 2x + 4.', 'x = 1/2', 'x = 2', 'x = -2', 'x = 4', 0,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = 2/(2×2) = 2/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = -2x² - 6x + 2.', 'x = 2', 'x = -3/2', 'x = 6', 'x = -6', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = 6/(2×-2) = 6/-4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = 2x² - 3x + 0.', 'x = -3', 'x = 3', 'x = 3/4', 'x = 0', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = 3/(2×2) = 3/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = x² + 1x + 4.', 'x = 1', 'x = -1', 'x = -1/2', 'x = 4', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = -1/(2×1) = -1/2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = x² + 0x - 3.', 'Option 3', 'x = -3', 'Option 4', 'x = 0', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = 0/(2×1) = 0/2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = -2x² - 6x + 4.', 'x = -6', 'x = 4', 'x = -3/2', 'x = 6', 2,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = 6/(2×-2) = 6/-4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = 2x² - 1x - 3.', 'x = -3', 'x = 1/4', 'x = 1', 'x = -1', 1,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = 1/(2×2) = 1/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the axis of symmetry of f(x) = 2x² + 4x + 3.', 'x = 4', 'x = 3', 'x = -4', 'x = -1', 3,
'lc_hl_functions', 7, 'proficient', 'lc_hl', 'For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = -4/(2×2) = -4/4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 10ˣ, find f(4).', '1000', '100000', '40', '10000', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(4) = 10⁴ = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 10ˣ, find f(3).', '30', '1000', '10000', '100', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(3) = 10³ = 1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 10ˣ, find f(2).', '1000', '20', '10', '100', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(2) = 10² = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2ˣ, find f(1).', '4', '2', '1', 'Option 4', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(1) = 2¹ = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3ˣ, find f(4).', '81', '12', '27', '243', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(4) = 3⁴ = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5ˣ, find f(1).', '5', 'Option 4', '1', '25', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(1) = 5¹ = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2ˣ, find f(1).', 'Option 4', '4', '2', '1', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(1) = 2¹ = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 10ˣ, find f(4).', '10000', '100000', '1000', '40', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(4) = 10⁴ = 10000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5ˣ, find f(4).', '20', '3125', '125', '625', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(4) = 5⁴ = 625', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3ˣ, find f(3).', '27', 'Option 4', '81', '9', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(3) = 3³ = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2ˣ, find f(2).', '8', '4', 'Option 4', '2', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(2) = 2² = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5ˣ, find f(0).', '0', '1', '5', 'Option 4', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(0) = 5⁰ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = 5ˣ.', 'Exponential decay', 'Polynomial growth', 'Exponential growth', 'Linear growth', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 5 > 1, the function represents exponential growth.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = (4/8)ˣ.', 'Exponential decay', 'Exponential growth', 'Linear growth', 'Polynomial growth', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 4/8 is between 0 and 1, the function represents exponential decay.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = 3ˣ.', 'Exponential decay', 'Exponential growth', 'Linear growth', 'Polynomial growth', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 3 > 1, the function represents exponential growth.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = 3ˣ.', 'Exponential growth', 'Linear growth', 'Polynomial growth', 'Exponential decay', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 3 > 1, the function represents exponential growth.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = (1/2)ˣ.', 'Exponential decay', 'Polynomial growth', 'Exponential growth', 'Linear growth', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 1/2 is between 0 and 1, the function represents exponential decay.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = (1/9)ˣ.', 'Polynomial growth', 'Exponential decay', 'Exponential growth', 'Linear growth', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 1/9 is between 0 and 1, the function represents exponential decay.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = 3ˣ.', 'Linear growth', 'Exponential decay', 'Polynomial growth', 'Exponential growth', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 3 > 1, the function represents exponential growth.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = 10ˣ.', 'Polynomial growth', 'Linear growth', 'Exponential decay', 'Exponential growth', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 10 > 1, the function represents exponential growth.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = (3/8)ˣ.', 'Linear growth', 'Exponential growth', 'Polynomial growth', 'Exponential decay', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 3/8 is between 0 and 1, the function represents exponential decay.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the function f(x) = 5ˣ.', 'Linear growth', 'Polynomial growth', 'Exponential growth', 'Exponential decay', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Since the base 5 > 1, the function represents exponential growth.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of f(x) = 3ˣ?', '(0, 1)', '(0, -1)', '(0, 0)', '(1, 0)', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'For any f(x) = aˣ where a > 0, f(0) = a⁰ = 1. Y-intercept is (0, 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of f(x) = 5ˣ?', '(1, 0)', '(0, -1)', '(0, 0)', '(0, 1)', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'For any f(x) = aˣ where a > 0, f(0) = a⁰ = 1. Y-intercept is (0, 1).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = 2ˣ?', 'y = 0', 'x = 0', 'y = -1', 'y = 1', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'As x → -∞, 2ˣ → 0. The horizontal asymptote is y = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = eˣ?', 'y = 1', 'y = 0', 'x = 0', 'y = -1', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'As x → -∞, eˣ → 0. The horizontal asymptote is y = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = 4ˣ?', 'All real numbers (ℝ)', 'x ≥ 0', 'x > 0', 'x ≠ 0', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Exponential functions are defined for all real x values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = 2ˣ?', 'y ≥ 0', 'All real numbers', 'y ≥ 1', 'y > 0', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'Exponential functions with base > 0 always give positive outputs.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 3ˣ increasing or decreasing?', 'Increasing then decreasing', 'Always decreasing', 'Always increasing', 'Neither', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'When base > 1, the exponential function is always increasing.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = (1/2)ˣ increasing or decreasing?', 'Neither', 'Always decreasing', 'Option 4', 'Increasing then decreasing', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'When 0 < base < 1, the exponential function is always decreasing.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of f(x) = 2 × 3ˣ?', '(0, -1)', '(1, 0)', '(0, 0)', '(0, 2)', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'f(0) = 2 × 3⁰ = 2 × 1 = 2. Y-intercept is (0, 2).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = 2ˣ + 3?', 'y = -1', 'y = 3', 'y = 1', 'x = 0', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The +3 shifts the asymptote up from y = 0 to y = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 3ˣ = 3', '2', '1', '3', 'Option 4', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 3ˣ = 3. Since 3¹ = 3, x = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 2ˣ = 4', '1', 'Option 4', '3', '2', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 2ˣ = 4. Since 2² = 4, x = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 4ˣ = 4', '2', 'Option 4', '3', '1', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 4ˣ = 4. Since 4¹ = 4, x = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 4ˣ = 64', '3', '16', '4', '2', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 4ˣ = 64. Since 4³ = 64, x = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 3ˣ = 3', 'Option 4', '1', '3', '2', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 3ˣ = 3. Since 3¹ = 3, x = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 5ˣ = 125', '3', '25', '4', '2', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 5ˣ = 125. Since 5³ = 125, x = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 4ˣ = 4', '1', 'Option 4', '3', '2', 0,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 4ˣ = 4. Since 4¹ = 4, x = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 4ˣ = 64', '4', '16', '2', '3', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 4ˣ = 64. Since 4³ = 64, x = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 4ˣ = 16', '3', '4', '1', '2', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 4ˣ = 16. Since 4² = 16, x = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve for x: 4ˣ = 256', '64', '5', '3', '4', 3,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'We need 4ˣ = 256. Since 4⁴ = 256, x = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = e⁽x + 1⁾ + 2?', 'y = -2', 'y = 2', 'y = 0', 'x = -1', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation + 2 shifts the horizontal asymptote from y = 0 to y = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = e⁽x - 3⁾ + 3?', 'y = -3', 'y = 3', 'y = 0', 'x = 3', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation + 3 shifts the horizontal asymptote from y = 0 to y = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = e⁽x + 4⁾ + 2?', 'y = -2', 'y = 0', 'y = 2', 'x = -4', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation + 2 shifts the horizontal asymptote from y = 0 to y = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = 3⁽x + 4⁾ - 3?', 'y = 3', 'x = -4', 'y = -3', 'y = 0', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation - 3 shifts the horizontal asymptote from y = 0 to y = -3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = 3⁽x - 1⁾ + 1?', 'y = -1', 'y = 1', 'x = 1', 'y = 0', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation + 1 shifts the horizontal asymptote from y = 0 to y = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = e⁽x + 4⁾ - 1?', 'y = 0', 'y = 1', 'y = -1', 'x = -4', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation - 1 shifts the horizontal asymptote from y = 0 to y = -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = 2⁽x - 2⁾ + 3?', 'y = 0', 'y = 3', 'y = -3', 'x = 2', 1,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation + 3 shifts the horizontal asymptote from y = 0 to y = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the horizontal asymptote of f(x) = 2⁽x + 1⁾ + 4?', 'y = 0', 'x = -1', 'y = 4', 'y = -4', 2,
'lc_hl_functions', 8, 'proficient', 'lc_hl', 'The transformation + 4 shifts the horizontal asymptote from y = 0 to y = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log2(8).', 'Option 4', '3', '2', '4', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log2(8) = 3 because 2³ = 8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log2(16).', '3', '8', '4', '5', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log2(16) = 4 because 2⁴ = 16.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log2(32).', '5', '4', '6', '16', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log2(32) = 5 because 2⁵ = 32.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log2(4).', '2', 'Option 4', '3', '1', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log2(4) = 2 because 2² = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log3(9).', '1', 'Option 4', '3', '2', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log3(9) = 2 because 3² = 9.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log3(27).', '9', '4', '2', '3', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log3(27) = 3 because 3³ = 27.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log3(81).', '3', '4', '27', '5', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log3(81) = 4 because 3⁴ = 81.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(100).', '1', '2', '10', '3', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(100) = 2 because 10² = 100.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(1000).', '4', '100', '2', '3', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(1000) = 3 because 10³ = 1000.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(10000).', '3', '4', '5', '1000', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(10000) = 4 because 10⁴ = 10000.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log5(25).', '5', '2', '1', '3', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log5(25) = 2 because 5² = 25.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log5(125).', '4', '25', '2', '3', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log5(125) = 3 because 5³ = 125.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x)?', 'All real numbers', 'x > 0', 'x ≥ 0', 'x ≠ 0', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Logarithms are only defined for positive arguments.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = log(x)?', 'x ≠ 0', 'x > 0', 'All real numbers', 'x ≥ 0', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Logarithms are only defined for positive arguments.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of f(x) = ln(x)?', 'y ≠ 0', 'y ≥ 0', 'All real numbers (ℝ)', 'y > 0', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Logarithmic functions can output any real number.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the x-intercept of f(x) = ln(x)?', '(e, 0)', '(1, 0)', '(0, 0)', '(0, 1)', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'ln(1) = 0, so the x-intercept is (1, 0).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the x-intercept of f(x) = log(x)?', '(0, 0)', '(1, 0)', '(0, 1)', '(e, 0)', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(1) = 0, so the x-intercept is (1, 0).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical asymptote of f(x) = ln(x)?', 'x = 0', 'x = 1', 'y = 0', 'y = 1', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'As x → 0⁺, ln(x) → -∞. The vertical asymptote is x = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = ln(x) increasing or decreasing for x > 0?', 'Always increasing', 'Sometimes increasing', 'Always decreasing', 'Neither', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'The natural logarithm is always increasing on its domain.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is ln(e)?', '-1', '0', '1', 'e', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'By definition, ln(e) = 1 since e¹ = e.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is log(10)?', '-1', '0', 'e', '1', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'By definition, log(10) = 1 since 10¹ = 10.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is ln(1)?', '0', '-1', 'Option 4', 'e', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'ln(1) = 0 because e⁰ = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(a) + log(b)', 'log(a) × log(b)', 'log(a+b)', 'log(ab)', 'log(a-b)', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Product rule: log(a) + log(b) = log(ab)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(a) - log(b)', 'log(a×b)', 'log(a/b)', 'log(a-b)', 'log(a)/log(b)', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Quotient rule: log(a) - log(b) = log(a/b)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2log(a)', 'log(a)/2', 'log(2a)', '2 × log(a)', 'log(a²)', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Power rule: nlog(a) = log(aⁿ)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3log(x)', 'log(a)/2', '2 × log(a)', 'log(x³)', 'log(2a)', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Power rule: nlog(a) = log(aⁿ)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(x) + log(y) + log(z)', 'Option 4', 'log(a) × log(b)', 'Option 3', 'log(xyz)', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'Product rule extended: log(xyz)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(100) + log(10)', 'Option 4', 'log(1000) or 3', 'log(a) × log(b)', 'Option 3', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(100 × 10) = log(1000) = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify ln(e²)', 'log(x)/log(y)', 'log(x) × log(y)', '2', 'log(x + y)', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'ln(e²) = 2ln(e) = 2 × 1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify ln(e³)', 'log(x + y)', 'log(x) × log(y)', '3', 'log(x)/log(y)', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'ln(e³) = 3ln(e) = 3 × 1 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log₂(4) + log₂(8)', 'log(x)/log(y)', 'log(x + y)', '5', 'log(x) × log(y)', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log₂(4 × 8) = log₂(32) = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log₃(27) - log₃(9)', 'log(x) × log(y)', 'log(x + y)', 'log(x)/log(y)', '1', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log₃(27/9) = log₃(3) = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(x²y) in terms of log(x) and log(y)', '2log(x) + log(y)', 'log(x)/log(y)', 'log(x) × log(y)', 'log(x + y)', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(x²y) = log(x²) + log(y) = 2log(x) + log(y)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(x/y²) in terms of log(x) and log(y)', 'log(x) × log(y)', 'log(x + y)', 'log(x) - 2log(y)', 'log(x)/log(y)', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(x/y²) = log(x) - log(y²) = log(x) - 2log(y)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(1/x)', 'log(x) × log(y)', 'log(x)/log(y)', 'log(x + y)', '-log(x)', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log(1/x) = log(1) - log(x) = 0 - log(x) = -log(x)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify ln(√x)', '½ln(x)', 'log(x) × log(y)', 'log(x)/log(y)', 'log(x + y)', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'ln(√x) = ln(x^½) = ½ln(x)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log₂(2⁵)', '5', 'log(x + y)', 'log(x) × log(y)', 'log(x)/log(y)', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'log₂(2⁵) = 5log₂(2) = 5 × 1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x + 4)?', 'All real numbers', 'x > -4', 'x > 0', 'x ≥ -4', 1,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x + 4) to be defined, we need x + 4 > 0, so x > -4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x + 3)?', 'x > 0', 'x ≥ -3', 'All real numbers', 'x > -3', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x + 3) to be defined, we need x + 3 > 0, so x > -3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 2)?', 'x > 0', 'All real numbers', 'x > 2', 'x ≥ 2', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 2) to be defined, we need x - 2 > 0, so x > 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x + 2)?', 'x ≥ -2', 'x > 0', 'x > -2', 'All real numbers', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x + 2) to be defined, we need x + 2 > 0, so x > -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 1)?', 'x ≥ 1', 'All real numbers', 'x > 1', 'x > 0', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 1) to be defined, we need x - 1 > 0, so x > 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 5)?', 'All real numbers', 'x ≥ 5', 'x > 5', 'x > 0', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 5) to be defined, we need x - 5 > 0, so x > 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 1)?', 'x > 1', 'All real numbers', 'x > 0', 'x ≥ 1', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 1) to be defined, we need x - 1 > 0, so x > 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 3)?', 'x > 0', 'x ≥ 3', 'x > 3', 'All real numbers', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 3) to be defined, we need x - 3 > 0, so x > 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 5)?', 'x > 5', 'x > 0', 'x ≥ 5', 'All real numbers', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 5) to be defined, we need x - 5 > 0, so x > 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 3)?', 'x > 3', 'x > 0', 'x ≥ 3', 'All real numbers', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 3) to be defined, we need x - 3 > 0, so x > 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x - 4)?', 'All real numbers', 'x > 0', 'x ≥ 4', 'x > 4', 3,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x - 4) to be defined, we need x - 4 > 0, so x > 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x + 1)?', 'x ≥ -1', 'All real numbers', 'x > -1', 'x > 0', 2,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x + 1) to be defined, we need x + 1 > 0, so x > -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = ln(x + 6)?', 'x > -6', 'x ≥ -6', 'x > 0', 'All real numbers', 0,
'lc_hl_functions', 9, 'proficient', 'lc_hl', 'For ln(x + 6) to be defined, we need x + 6 > 0, so x > -6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 6).', 'x = -6', 'x = 0', 'y = 6', 'x = 6', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 6 = 0, so x = 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 5).', 'x = 0', 'x = -5', 'x = 5', 'y = 5', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 5 = 0, so x = 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 8).', 'y = 8', 'x = 0', 'x = 8', 'x = -8', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 8 = 0, so x = 8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 5).', 'y = 5', 'x = 5', 'x = 0', 'x = -5', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 5 = 0, so x = 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 3).', 'y = 3', 'x = 0', 'x = 3', 'x = -3', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 3 = 0, so x = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x + 7).', 'x = -7', 'x = 7', 'y = -7', 'x = 0', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x + 7 = 0, so x = -7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 4).', 'y = 4', 'x = 0', 'x = -4', 'x = 4', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 4 = 0, so x = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 1).', 'x = -1', 'x = 0', 'y = 1', 'x = 1', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 1 = 0, so x = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 8).', 'x = 0', 'x = -8', 'y = 8', 'x = 8', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 8 = 0, so x = 8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x + 8).', 'x = 8', 'y = -8', 'x = 0', 'x = -8', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x + 8 = 0, so x = -8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x + 2).', 'y = -2', 'x = 2', 'x = 0', 'x = -2', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x + 2 = 0, so x = -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the vertical asymptote of f(x) = 1/(x - 4).', 'y = 4', 'x = 0', 'x = -4', 'x = 4', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The vertical asymptote occurs where the denominator equals zero: x - 4 = 0, so x = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = 1/x', 'y = 2', 'y = 0', 'No horizontal asymptote', 'y = 1', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degree of numerator < degree of denominator, HA is y = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = 3/(x + 2)', 'y = 2', 'y = 0', 'No horizontal asymptote', 'y = 1', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degree of numerator < degree of denominator, HA is y = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = (2x + 1)/(x - 3)', 'y = 2', 'y = 0', 'y = 4', 'y = 1', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = (leading coef of num)/(leading coef of denom) = 2/1 = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = (3x - 1)/(x + 5)', 'y = -1', 'No horizontal asymptote', 'y = 1', 'y = 3', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = 3/1 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = (x + 2)/(2x - 1)', 'No horizontal asymptote', 'y = 1/2', 'y = -1', 'y = 1', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = 1/2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = (4x + 3)/(2x - 7)', 'y = 4', 'y = 1', 'y = 2', 'y = 0', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = 4/2 = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = 5/(x² + 1)', 'y = 1', 'y = 0', 'y = 2', 'No horizontal asymptote', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degree of numerator < degree of denominator, HA is y = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = (x² + 1)/(x² - 4)', 'y = 1', 'y = -1', 'y = 2', 'y = 0', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = 1/1 = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = (3x² - 2)/(x² + x)', 'y = -1', 'y = 3', 'y = 1', 'No horizontal asymptote', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = 3/1 = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = 2x/(x + 1)', 'y = 2', 'y = 1', 'y = 4', 'y = 0', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = 2/1 = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = (x - 1)/(3x + 2)', 'y = 1/3', 'No horizontal asymptote', 'y = 1', 'y = -1', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degrees are equal, HA is y = 1/3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the horizontal asymptote of = 7/(2x - 5)', 'y = 1', 'y = 0', 'No horizontal asymptote', 'y = 2', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'When degree of numerator < degree of denominator, HA is y = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x + 3)(x - 2)]?', 'All real numbers', 'x ≠ 2', 'x ≠ -3 and x ≠ 2', 'x ≠ -3', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x + 3)(x - 2) = 0 when x = -3 or x = 2. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 3)(x + 6)]?', 'All real numbers', 'x ≠ -6', 'x ≠ 3 and x ≠ -6', 'x ≠ 3', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 3)(x + 6) = 0 when x = 3 or x = -6. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x + 3)(x - 4)]?', 'x ≠ 4', 'x ≠ -3 and x ≠ 4', 'x ≠ -3', 'All real numbers', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x + 3)(x - 4) = 0 when x = -3 or x = 4. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x + 1)(x - 6)]?', 'x ≠ 6', 'x ≠ -1', 'x ≠ -1 and x ≠ 6', 'All real numbers', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x + 1)(x - 6) = 0 when x = -1 or x = 6. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 5)(x + 2)]?', 'x ≠ 5', 'x ≠ 5 and x ≠ -2', 'x ≠ -2', 'All real numbers', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 5)(x + 2) = 0 when x = 5 or x = -2. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 2)(x - 6)]?', 'x ≠ 2 and x ≠ 6', 'x ≠ 2', 'x ≠ 6', 'All real numbers', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 2)(x - 6) = 0 when x = 2 or x = 6. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 2)(x - 1)]?', 'x ≠ 2', 'All real numbers', 'x ≠ 2 and x ≠ 1', 'x ≠ 1', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 2)(x - 1) = 0 when x = 2 or x = 1. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 5)(x - 3)]?', 'All real numbers', 'x ≠ 5', 'x ≠ 5 and x ≠ 3', 'x ≠ 3', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 5)(x - 3) = 0 when x = 5 or x = 3. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 4)(x + 5)]?', 'All real numbers', 'x ≠ -5', 'x ≠ 4', 'x ≠ 4 and x ≠ -5', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 4)(x + 5) = 0 when x = 4 or x = -5. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x + 1)(x + 6)]?', 'x ≠ -1 and x ≠ -6', 'x ≠ -1', 'All real numbers', 'x ≠ -6', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x + 1)(x + 6) = 0 when x = -1 or x = -6. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 3)(x - 6)]?', 'x ≠ 3 and x ≠ 6', 'x ≠ 3', 'x ≠ 6', 'All real numbers', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 3)(x - 6) = 0 when x = 3 or x = 6. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 4)(x + 3)]?', 'All real numbers', 'x ≠ 4', 'x ≠ 4 and x ≠ -3', 'x ≠ -3', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 4)(x + 3) = 0 when x = 4 or x = -3. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the domain of f(x) = x/[(x - 3)(x - 4)]?', 'x ≠ 3 and x ≠ 4', 'x ≠ 4', 'All real numbers', 'x ≠ 3', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'The denominator (x - 3)(x - 4) = 0 when x = 3 or x = 4. Domain excludes these values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x - 2)/(x + 4).', 'x = 2', 'No x-intercept', 'x = -2', 'x = 4', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x - 2 = 0, so x = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x - 3)/(x + 3).', 'No x-intercept', 'x = 3', 'x = -3', 'Option 4', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x - 3 = 0, so x = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x - 3)/(x + 2).', 'No x-intercept', 'x = 3', 'x = 2', 'x = -3', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x - 3 = 0, so x = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x + 0)/(x + 4).', 'No x-intercept', 'x = 4', 'Option 4', 'x = 0', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x + 0 = 0, so x = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x + 0)/(x + 1).', 'x = 1', 'No x-intercept', 'x = 0', 'Option 4', 2,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x + 0 = 0, so x = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x - 5)/(x + 5).', 'No x-intercept', 'x = 5', 'Option 4', 'x = -5', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x - 5 = 0, so x = 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x - 4)/(x + 2).', 'x = 4', 'x = -4', 'x = 2', 'No x-intercept', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x - 4 = 0, so x = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x + 4)/(x + 1).', 'x = 4', 'No x-intercept', 'x = 1', 'x = -4', 3,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x + 4 = 0, so x = -4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x - 1)/(x + 4).', 'x = 4', 'x = 1', 'No x-intercept', 'x = -1', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x - 1 = 0, so x = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x + 5)/(x + 3).', 'x = -5', 'x = 3', 'x = 5', 'No x-intercept', 0,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x + 5 = 0, so x = -5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x + 3)/(x + 1).', 'x = 3', 'x = -3', 'No x-intercept', 'x = 1', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x + 3 = 0, so x = -3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x - 4)/(x + 3).', 'x = 3', 'x = 4', 'No x-intercept', 'x = -4', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x - 4 = 0, so x = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-intercept of f(x) = (x + 3)/(x + 5).', 'x = 3', 'x = -3', 'x = 5', 'No x-intercept', 1,
'lc_hl_functions', 10, 'advanced', 'lc_hl', 'X-intercepts occur when numerator = 0: x + 3 = 0, so x = -3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {4x - 5 if x < 0, 4x - 3 if x ≥ 0}, find f(0).', '-3', '1', '2', '-5', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 0 = 0 (≥ 0), we use f(x) = 4x - 3. f(0) = 4(0) - 3 = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {4x + 3 if x < 1, 3x - 1 if x ≥ 1}, find f(1).', '7', '-1', '2', '6', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 1 = 1 (≥ 1), we use f(x) = 3x - 1. f(1) = 3(1) - 1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {2x + 1 if x < 0, 3x + 1 if x ≥ 0}, find f(-2).', '-1', '-4', '-5', '-3', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since -2 < 0, we use f(x) = 2x + 1. f(-2) = 2(-2) + 1 = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {4x - 4 if x < 0, 2x + 4 if x ≥ 0}, find f(0).', '-4', '4', 'Option 4', '8', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 0 = 0 (≥ 0), we use f(x) = 2x + 4. f(0) = 2(0) + 4 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {4x + 1 if x < -1, 4x + 3 if x ≥ -1}, find f(-3).', '-12', '-9', '-7', '-11', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since -3 < -1, we use f(x) = 4x + 1. f(-3) = 4(-3) + 1 = -11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {3x + 1 if x < 1, 1x - 5 if x ≥ 1}, find f(1).', '4', '-4', '-5', '-1', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 1 = 1 (≥ 1), we use f(x) = 1x - 5. f(1) = 1(1) - 5 = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {2x + 4 if x < -2, 1x + 5 if x ≥ -2}, find f(-4).', '1', '-2', '-8', '-4', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since -4 < -2, we use f(x) = 2x + 4. f(-4) = 2(-4) + 4 = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {4x + 3 if x < 1, 3x + 4 if x ≥ 1}, find f(1).', '11', 'Option 4', '7', '4', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 1 = 1 (≥ 1), we use f(x) = 3x + 4. f(1) = 3(1) + 4 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {3x - 2 if x < 2, 1x + 3 if x ≥ 2}, find f(3).', '7', '8', '6', '9', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 3 ≥ 2, we use f(x) = 1x + 3. f(3) = 1(3) + 3 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {3x + 1 if x < 3, 4x - 5 if x ≥ 3}, find f(3).', '7', '6', '10', 'Option 4', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 3 = 3 (≥ 3), we use f(x) = 4x - 5. f(3) = 4(3) - 5 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {3x + 1 if x < -3, 3x + 4 if x ≥ -3}, find f(-6).', '-14', 'Option 4', '-18', '-17', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since -6 < -3, we use f(x) = 3x + 1. f(-6) = 3(-6) + 1 = -17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {4x - 4 if x < 3, 4x + 5 if x ≥ 3}, find f(-1).', '-8', '-4', '1', 'Option 4', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since -1 < 3, we use f(x) = 4x - 4. f(-1) = 4(-1) - 4 = -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {3x - 3 if x < -2, 3x - 1 if x ≥ -2}, find f(2).', '8', '3', 'Option 4', '5', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 2 ≥ -2, we use f(x) = 3x - 1. f(2) = 3(2) - 1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {3x + 4 if x < -3, 1x + 1 if x ≥ -3}, find f(-3).', '-5', '-2', '-6', '1', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since -3 = -3 (≥ -3), we use f(x) = 1x + 1. f(-3) = 1(-3) + 1 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = {2x + 4 if x < 2, 2x + 5 if x ≥ 2}, find f(2).', '5', '11', '9', '8', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Since 2 = 2 (≥ 2), we use f(x) = 2x + 5. f(2) = 2(2) + 5 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {3x + 1 if x < 0, 2x + 1 if x ≥ 0} continuous at x = 0?', 'Cannot be determined', 'No, it is discontinuous', 'Yes, it is continuous', 'Only continuous from the left', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = 0: left limit = 3(0) + 1 = 1, right limit = 2(0) + 1 = 1. Since they''re equal, f is continuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {2x - 2 if x < 0, 1x + 0 if x ≥ 0} continuous at x = 0?', 'Yes, it is continuous', 'Cannot be determined', 'Only continuous from the left', 'No, it is discontinuous', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = 0: left limit = 2(0) + -2 = -2, right limit = 1(0) + 0 = 0. Since -2 ≠ 0, f is discontinuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {1x - 1 if x < 1, 3x - 3 if x ≥ 1} continuous at x = 1?', 'Cannot be determined', 'Yes, it is continuous', 'Only continuous from the left', 'No, it is discontinuous', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = 1: left limit = 1(1) + -1 = 0, right limit = 3(1) + -3 = 0. Since they''re equal, f is continuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {3x + 0 if x < 0, 1x + 0 if x ≥ 0} continuous at x = 0?', 'Only continuous from the left', 'No, it is discontinuous', 'Yes, it is continuous', 'Cannot be determined', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = 0: left limit = 3(0) + 0 = 0, right limit = 1(0) + 0 = 0. Since they''re equal, f is continuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {2x + 1 if x < -1, 2x + 1 if x ≥ -1} continuous at x = -1?', 'Yes, it is continuous', 'Only continuous from the left', 'Cannot be determined', 'No, it is discontinuous', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = -1: left limit = 2(-1) + 1 = -1, right limit = 2(-1) + 1 = -1. Since they''re equal, f is continuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {3x + 0 if x < -2, 1x - 4 if x ≥ -2} continuous at x = -2?', 'Yes, it is continuous', 'Cannot be determined', 'Only continuous from the left', 'No, it is discontinuous', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = -2: left limit = 3(-2) + 0 = -6, right limit = 1(-2) + -4 = -6. Since they''re equal, f is continuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {3x - 1 if x < 2, 1x + 1 if x ≥ 2} continuous at x = 2?', 'No, it is discontinuous', 'Cannot be determined', 'Only continuous from the left', 'Yes, it is continuous', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = 2: left limit = 3(2) + -1 = 5, right limit = 1(2) + 1 = 3. Since 5 ≠ 3, f is discontinuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {1x - 2 if x < -2, 3x + 4 if x ≥ -2} continuous at x = -2?', 'Cannot be determined', 'Yes, it is continuous', 'No, it is discontinuous', 'Only continuous from the left', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = -2: left limit = 1(-2) + -2 = -4, right limit = 3(-2) + 4 = -2. Since -4 ≠ -2, f is discontinuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {3x + 0 if x < -2, 3x + 0 if x ≥ -2} continuous at x = -2?', 'No, it is discontinuous', 'Cannot be determined', 'Only continuous from the left', 'Yes, it is continuous', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = -2: left limit = 3(-2) + 0 = -6, right limit = 3(-2) + 0 = -6. Since they''re equal, f is continuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {2x + 3 if x < 2, 2x + 2 if x ≥ 2} continuous at x = 2?', 'Cannot be determined', 'Only continuous from the left', 'No, it is discontinuous', 'Yes, it is continuous', 2,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = 2: left limit = 2(2) + 3 = 7, right limit = 2(2) + 2 = 6. Since 7 ≠ 6, f is discontinuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {1x - 1 if x < -1, 2x + 0 if x ≥ -1} continuous at x = -1?', 'Only continuous from the left', 'Yes, it is continuous', 'No, it is discontinuous', 'Cannot be determined', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = -1: left limit = 1(-1) + -1 = -2, right limit = 2(-1) + 0 = -2. Since they''re equal, f is continuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = {2x + 0 if x < 0, 2x - 1 if x ≥ 0} continuous at x = 0?', 'Only continuous from the left', 'Yes, it is continuous', 'Cannot be determined', 'No, it is discontinuous', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x = 0: left limit = 2(0) + 0 = 0, right limit = 2(0) + -1 = -1. Since 0 ≠ -1, f is discontinuous.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {2x + 1 if x < 1, 3x + k if x ≥ 1} is continuous at x = 1.', '0', '-1', '3', '1', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = 1: left limit = 2(1) + 1 = 3 must equal right limit = 3(1) + k. So 3(1) + k = 3, giving k = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {1x - 3 if x < 1, 3x + k if x ≥ 1} is continuous at x = 1.', '-6', '-5', '-4', '-2', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = 1: left limit = 1(1) + -3 = -2 must equal right limit = 3(1) + k. So 3(1) + k = -2, giving k = -5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {1x + 2 if x < -1, 3x + k if x ≥ -1} is continuous at x = -1.', '4', '1', '3', '5', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = -1: left limit = 1(-1) + 2 = 1 must equal right limit = 3(-1) + k. So 3(-1) + k = 1, giving k = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {4x + 1 if x < 3, 4x + k if x ≥ 3} is continuous at x = 3.', '1', '0', '13', '2', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = 3: left limit = 4(3) + 1 = 13 must equal right limit = 4(3) + k. So 4(3) + k = 13, giving k = 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {4x + 0 if x < -2, 2x + k if x ≥ -2} is continuous at x = -2.', '-5', '-4', '-3', '-8', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = -2: left limit = 4(-2) + 0 = -8 must equal right limit = 2(-2) + k. So 2(-2) + k = -8, giving k = -4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {4x - 1 if x < -1, 4x + k if x ≥ -1} is continuous at x = -1.', '-2', '-5', '0', '-1', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = -1: left limit = 4(-1) + -1 = -5 must equal right limit = 4(-1) + k. So 4(-1) + k = -5, giving k = -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {2x + 4 if x < 1, 1x + k if x ≥ 1} is continuous at x = 1.', 'Option 4', '6', '4', '5', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = 1: left limit = 2(1) + 4 = 6 must equal right limit = 1(1) + k. So 1(1) + k = 6, giving k = 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {4x - 2 if x < 0, 4x + k if x ≥ 0} is continuous at x = 0.', '-2', 'Option 4', '-1', '-3', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = 0: left limit = 4(0) + -2 = -2 must equal right limit = 4(0) + k. So 4(0) + k = -2, giving k = -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {1x - 1 if x < 2, 1x + k if x ≥ 2} is continuous at x = 2.', '-1', '-2', '0', '1', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = 2: left limit = 1(2) + -1 = 1 must equal right limit = 1(2) + k. So 1(2) + k = 1, giving k = -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {2x - 4 if x < -2, 4x + k if x ≥ -2} is continuous at x = -2.', '-8', '-1', '1', '0', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = -2: left limit = 2(-2) + -4 = -8 must equal right limit = 4(-2) + k. So 4(-2) + k = -8, giving k = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {2x - 1 if x < 3, 1x + k if x ≥ 3} is continuous at x = 3.', '2', '5', '1', '3', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = 3: left limit = 2(3) + -1 = 5 must equal right limit = 1(3) + k. So 1(3) + k = 5, giving k = 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k so that f(x) = {2x + 0 if x < -2, 2x + k if x ≥ -2} is continuous at x = -2.', '1', '0', '-1', '-4', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'For continuity at x = -2: left limit = 2(-2) + 0 = -4 must equal right limit = 2(-2) + k. So 2(-2) + k = -4, giving k = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {x if x ≤ 0, x² if x > 0}.', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: all real numbers; Range: y > 0', 'Domain: x > 0; Range: y > 0', 'Domain: all real numbers; Range: all real numbers', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Both pieces cover all x values; y can be any real number.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {2x if x < 1, 3 if x ≥ 1}.', 'Domain: all real numbers; Range: y > 0', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: x > 0; Range: y > 0', 'Domain: all real numbers; Range: y < 2 or y = 3', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Left piece gives y < 2, right piece gives y = 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {-x if x ≤ 0, x if x > 0}.', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: all real numbers; Range: y > 0', 'Domain: x > 0; Range: y > 0', 'Domain: all real numbers; Range: y ≥ 0', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'This is |x|, which is always non-negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {1/x if x > 0, x if x ≤ 0}.', 'Domain: all real numbers; Range: all real numbers', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: all real numbers; Range: y > 0', 'Domain: x > 0; Range: y > 0', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Left piece: y > 0; Right piece: y ≤ 0. Combined: all reals.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {x² if x ≤ 1, 2x - 1 if x > 1}.', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: all real numbers; Range: y ≥ 0', 'Domain: all real numbers; Range: y > 0', 'Domain: x > 0; Range: y > 0', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Both pieces produce non-negative outputs for their domains.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {3 if x < 0, x + 3 if x ≥ 0}.', 'Domain: all real numbers; Range: y ≥ 3', 'Domain: all real numbers; Range: y > 0', 'Domain: x > 0; Range: y > 0', 'Domain: x ≥ 0; Range: all real numbers', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Left piece: y = 3; Right piece: y ≥ 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {√x if x ≥ 0}.', 'Domain: all real numbers; Range: y > 0', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: x > 0; Range: y > 0', 'Domain: x ≥ 0; Range: y ≥ 0', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Square root requires non-negative input and produces non-negative output.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {|x| if x ≠ 0, 1 if x = 0}.', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: x > 0; Range: y > 0', 'Option 4', 'Domain: all real numbers; Range: y > 0', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'At x ≠ 0, y = |x| > 0; at x = 0, y = 1 > 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {x² if x < 2, 4 if x ≥ 2}.', 'Domain: x ≥ 0; Range: all real numbers', 'Domain: x > 0; Range: y > 0', 'Domain: all real numbers; Range: y > 0', 'Domain: all real numbers; Range: y ≥ 0', 3,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Left piece gives 0 ≤ y < 4, right piece gives y = 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {-x² if x ≤ 0, -x if x > 0}.', 'Domain: x > 0; Range: y > 0', 'Domain: all real numbers; Range: y ≤ 0', 'Domain: all real numbers; Range: y > 0', 'Domain: x ≥ 0; Range: all real numbers', 1,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Both pieces produce non-positive outputs.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain and range of f(x) = {2 if x < 0, x² if x ≥ 0}.', 'Domain: all real numbers; Range: y = 2 or y ≥ 0', 'Domain: x > 0; Range: y > 0', 'Domain: all real numbers; Range: y > 0', 'Domain: x ≥ 0; Range: all real numbers', 0,
'lc_hl_functions', 11, 'advanced', 'lc_hl', 'Left: y = 2; Right: y ≥ 0. Combined range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 1 and g(x) = x², find f(g(x)).', '4x² - 1', '4x² + 1', 'x² + 4x + 1', '16x + 1', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'f(g(x)) = f(x²) = 4(x²) + 1 = 4x² + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 2 and g(x) = x², find f(g(x)).', '4x + 2', 'x² + 2x + 2', '2x² - 2', '2x² + 2', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'f(g(x)) = f(x²) = 2(x²) + 2 = 2x² + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 2 and g(x) = x², find g(f(x)).', 'x² + 3x + 2', '3x² - 2', '(3x + 2)² or 9x² + 12x + 4', '9x + 2', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = g(3x + 2) = (3x + 2)² = 9x² + 12x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 5 and g(x) = x², find g(f(x)).', '9x + 5', '(3x + 5)² or 9x² + 30x + 25', '3x² - 5', 'x² + 3x + 5', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = g(3x + 5) = (3x + 5)² = 9x² + 30x + 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 3 and g(x) = x², find f(g(x)).', '2x² + 3', '2x² - 3', 'x² + 2x + 3', '4x + 3', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'f(g(x)) = f(x²) = 2(x²) + 3 = 2x² + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1 and g(x) = x², find g(f(x)).', 'x² + 3x + 1', '9x + 1', '(3x + 1)² or 9x² + 6x + 1', '3x² - 1', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = g(3x + 1) = (3x + 1)² = 9x² + 6x + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3 and g(x) = x², find g(f(x)).', '9x + 3', '3x² - 3', 'x² + 3x + 3', '(3x + 3)² or 9x² + 18x + 9', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = g(3x + 3) = (3x + 3)² = 9x² + 18x + 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 1 and g(x) = x², find g(f(x)).', '(4x + 1)² or 16x² + 8x + 1', 'x² + 4x + 1', '16x + 1', '4x² - 1', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = g(4x + 1) = (4x + 1)² = 16x² + 8x + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 1, find f⁻¹(f(x)).', '4x + 1', 'x', '4x', '(x - 1)/4', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 6, find f⁻¹(f(x)).', '3x', '3x + 6', 'x', '(x - 6)/3', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 6, find f⁻¹(f(x)).', 'x', '(x - 6)/3', '3x', '3x + 6', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 3, find f⁻¹(f(x)).', '2x', '2x + 3', '(x - 3)/2', 'x', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 5, find f⁻¹(f(x)).', '(x - 5)/4', '4x + 5', 'x', '4x', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 4, find f⁻¹(f(x)).', '4x + 4', '4x', '(x - 4)/4', 'x', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 5, find f⁻¹(f(x)).', '4x', 'x', '4x + 5', '(x - 5)/4', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 2, find f⁻¹(f(x)).', '4x + 2', '4x', '(x - 2)/4', 'x', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 2f(x - 1) + 4.', 'Vertical stretch by 2, right 1, up 4', 'Horizontal stretch by 2, right 1, down 4', 'Vertical stretch by 2, left 1, up 4', 'Vertical stretch by 2, right 1, down 4', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 2f(x - 1) + 4: the 2 is a vertical stretch, (x - 1) shifts right 1, and +4 shifts up 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 3f(x - 2) + 4.', 'Vertical stretch by 3, right 2, up 4', 'Vertical stretch by 3, right 2, down 4', 'Horizontal stretch by 3, right 2, down 4', 'Vertical stretch by 3, left 2, up 4', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 3f(x - 2) + 4: the 3 is a vertical stretch, (x - 2) shifts right 2, and +4 shifts up 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 3f(x - 1) + 1.', 'Horizontal stretch by 3, right 1, down 1', 'Vertical stretch by 3, right 1, down 1', 'Vertical stretch by 3, right 1, up 1', 'Vertical stretch by 3, left 1, up 1', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 3f(x - 1) + 1: the 3 is a vertical stretch, (x - 1) shifts right 1, and +1 shifts up 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 3f(x - 4) + 2.', 'Horizontal stretch by 3, right 4, down 2', 'Vertical stretch by 3, left 4, up 2', 'Vertical stretch by 3, right 4, up 2', 'Vertical stretch by 3, right 4, down 2', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 3f(x - 4) + 2: the 3 is a vertical stretch, (x - 4) shifts right 4, and +2 shifts up 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 2f(x - 3) + 4.', 'Vertical stretch by 2, left 3, up 4', 'Vertical stretch by 2, right 3, up 4', 'Vertical stretch by 2, right 3, down 4', 'Horizontal stretch by 2, right 3, down 4', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 2f(x - 3) + 4: the 2 is a vertical stretch, (x - 3) shifts right 3, and +4 shifts up 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 3f(x - 4) + 4.', 'Vertical stretch by 3, right 4, up 4', 'Horizontal stretch by 3, right 4, down 4', 'Vertical stretch by 3, left 4, up 4', 'Vertical stretch by 3, right 4, down 4', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 3f(x - 4) + 4: the 3 is a vertical stretch, (x - 4) shifts right 4, and +4 shifts up 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 3f(x - 1) + 4.', 'Vertical stretch by 3, right 1, down 4', 'Vertical stretch by 3, left 1, up 4', 'Horizontal stretch by 3, right 1, down 4', 'Vertical stretch by 3, right 1, up 4', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 3f(x - 1) + 4: the 3 is a vertical stretch, (x - 1) shifts right 1, and +4 shifts up 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe all transformations mapping y = f(x) to y = 2f(x - 3) + 2.', 'Horizontal stretch by 2, right 3, down 2', 'Vertical stretch by 2, right 3, down 2', 'Vertical stretch by 2, right 3, up 2', 'Vertical stretch by 2, left 3, up 2', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'In y = 2f(x - 3) + 2: the 2 is a vertical stretch, (x - 3) shifts right 3, and +2 shifts up 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 7, solve f(x) = 22.', '9', '5', '7', '15', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 3x + 7 = 22: 3x = 15, x = 15/3 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 3, solve f(x) = 17.', '5', '6', '14/3', '14', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 3x + 3 = 17: 3x = 14, x = 14/3 = 14/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 7, solve f(x) = 24.', '6', '4', '17', '17/5', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 5x + 7 = 24: 5x = 17, x = 17/5 = 17/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 5x + 3, solve f(x) = 18.', '3', '4', 'Option 4', '15', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 5x + 3 = 18: 5x = 15, x = 15/5 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x + 4, solve f(x) = 12.', '6', 'Option 4', '4', '8', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 2x + 4 = 12: 2x = 8, x = 8/2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x + 2, solve f(x) = 19.', '17/4', '4', '5', '17', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 4x + 2 = 19: 4x = 17, x = 17/4 = 17/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 1, solve f(x) = 25.', '8', 'Option 3', '24', 'Option 4', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 3x + 1 = 25: 3x = 24, x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x + 5, solve f(x) = 26.', '7', '10', '21', '8', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Solve 3x + 5 = 26: 3x = 21, x = 21/3 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2ˣ and g(x) = log₂(x), what is f(g(x))?', '1', 'x', '2x', 'x²', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'f(g(x)) = 2^(log₂(x)) = x, since exponential and log with same base are inverses.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = eˣ and g(x) = ln(x), what is g(f(x))?', '2x', 'x', '1', 'x²', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = ln(eˣ) = x, since ln and eˣ are inverse functions.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² and g(x) = √x, what is f(g(x)) for x ≥ 0?', 'x', '2x', 'x²', '1', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'f(g(x)) = (√x)² = x for x ≥ 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x - 6 and g(x) = (x + 6)/3, what is g(f(x))?', 'x²', '2x', 'x', '1', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = (3x - 6 + 6)/3 = 3x/3 = x. They are inverses.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 10ˣ and g(x) = log(x), what is f(g(100))?', '1', '100', 'x²', '2x', 1,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(100) = log(100) = 2, then f(2) = 10² = 100.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ and g(x) = ∛x, what is g(f(x))?', 'x', '2x', '1', 'x²', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'g(f(x)) = ∛(x³) = x. Cube and cube root are inverses.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x and g(x) = x/2, verify that f and g are inverses by computing f(g(x)).', '2x', '1', 'x²', 'x', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'f(g(x)) = f(x/2) = 2(x/2) = x. ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x + 5 and g(x) = x - 5, what is f(g(f(1)))?', '6', '1', '2x', 'x²', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'f(1) = 6, g(6) = 1, f(1) = 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = ln(x²  - 4).', 'x > 0', 'x ≥ 0', 'All real numbers', 'x < -2 or x > 2', 3,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x² - 4 > 0, so x² > 4, meaning |x| > 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = √(9 - x²).', 'x > 0', 'x ≥ 0', '-3 ≤ x ≤ 3', 'All real numbers', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need 9 - x² ≥ 0, so x² ≤ 9, meaning -3 ≤ x ≤ 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = 1/√(x - 2).', 'x ≥ 0', 'x > 0', 'x > 2', 'All real numbers', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x - 2 > 0 (strictly, since in denominator), so x > 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = ln(x) + ln(4 - x).', '0 < x < 4', 'x > 0', 'x ≥ 0', 'All real numbers', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x > 0 AND 4 - x > 0, so 0 < x < 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = √x + √(1 - x).', '0 ≤ x ≤ 1', 'x > 0', 'x ≥ 0', 'All real numbers', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x ≥ 0 AND 1 - x ≥ 0, so 0 ≤ x ≤ 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = 1/(x² - 1).', 'x ≠ 1 and x ≠ -1', 'x > 0', 'x ≥ 0', 'All real numbers', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x² - 1 ≠ 0, so x ≠ ±1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = √(x - 1)/√(x + 2).', 'x > 0', 'x ≥ 0', 'x ≥ 1', 'All real numbers', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x - 1 ≥ 0 AND x + 2 > 0. First gives x ≥ 1, which satisfies second.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = log(x + 3) - log(x - 1).', 'x > 1', 'All real numbers', 'x > 0', 'x ≥ 0', 0,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x + 3 > 0 AND x - 1 > 0. Second is stricter: x > 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = √(x² - 9).', 'x ≥ 0', 'All real numbers', 'x ≤ -3 or x ≥ 3', 'x > 0', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need x² - 9 ≥ 0, so x² ≥ 9, meaning |x| ≥ 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the domain of f(x) = ln((x - 1)(x + 3)).', 'x > 0', 'x ≥ 0', 'x < -3 or x > 1', 'All real numbers', 2,
'lc_hl_functions', 12, 'advanced', 'lc_hl', 'Need (x-1)(x+3) > 0. Positive when x < -3 or x > 1.', 1);
-- Verification
SELECT 'Functions questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_hl_functions';
SELECT difficulty_level, COUNT(*) as questions FROM questions_adaptive WHERE topic = 'lc_hl_functions' GROUP BY difficulty_level ORDER BY difficulty_level;
