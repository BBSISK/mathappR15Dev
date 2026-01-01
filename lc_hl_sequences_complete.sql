-- Add Sequences & Series topic to LC Higher Level strand

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_sequences', 'Sequences & Series', id, '🔢', 4, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_sequences';
-- LC Higher Level - Sequences & Series Questions
-- Generated: 2025-12-14
-- Total: 600 questions

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 6, 9, 12, 15, ...', '6', '3', '2', '4', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 9 - 6 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 1, 5, 9, 13, ...', '3', '1', '4', '5', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 5 - 1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 7, 15, 23, 31, ...', '7', '8', 'Option 4', '9', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 15 - 7 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 5, 9, 13, 17, ...', 'Option 4', '5', '4', '3', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 9 - 5 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 3, 8, 13, 18, ...', '4', '6', '3', '5', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 8 - 3 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 10, 16, 22, 28, ...', '6', '7', '5', '10', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 16 - 10 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 7, 13, 19, 25, ...', '5', 'Option 4', '7', '6', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 13 - 7 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 8, 10, 12, 14, ...', '1', '2', '3', '8', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 10 - 8 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 4, 12, 20, 28, ...', '4', '7', '9', '8', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 12 - 4 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 5, 10, 15, 20, ...', '6', '4', 'Option 4', '5', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 10 - 5 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 9, 14, 19, 24, ...', '4', '5', '9', '6', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 14 - 9 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 9, 15, 21, 27, ...', '7', '5', '9', '6', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 15 - 9 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 8, 15, 22, 29, ...', '6', '8', 'Option 4', '7', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 15 - 8 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 1, 5, 9, 13, ...', '5', '3', '4', '1', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 5 - 1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 10, 18, 26, 34, ...', '10', '7', '8', '9', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 18 - 10 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 9, 16, 23, 30, ...', '7', '6', '9', '8', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 16 - 9 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 2, 7, 12, 17, ...', '5', '2', '4', '6', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 7 - 2 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 9, 17, 25, 33, ...', '8', 'Option 4', '7', '9', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 17 - 9 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 9, 15, 21, 27, ...', '5', '9', '6', '7', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 15 - 9 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common difference: 3, 8, 13, 18, ...', '6', '5', '4', '3', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Common difference d = 8 - 3 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 13, 19, 25, 31, ?', '37', '31', '43', '56', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 6, next term = 31 + 6 = 37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 10, 16, 22, ?', '28', '22', '34', '38', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 6, next term = 22 + 6 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 3, 5, 7, 9, ?', '11', '16', '9', '13', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 2, next term = 9 + 2 = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 7, 10, 13, ?', '23', '16', '13', '19', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 3, next term = 13 + 3 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 9, 13, 17, 21, ?', '21', '25', '38', '29', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 4, next term = 21 + 4 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 12, 16, 20, 24, ?', '44', '28', '32', '24', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 4, next term = 24 + 4 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 13, 20, 27, 34, ?', '61', '48', '41', '34', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 7, next term = 34 + 7 = 41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 2, 7, 12, 17, ?', '29', '27', '17', '22', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 5, next term = 17 + 5 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 13, 15, 17, 19, ?', '19', '23', '36', '21', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 2, next term = 19 + 2 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 10, 15, 20, 25, ?', '45', '35', '30', '25', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 5, next term = 25 + 5 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 6, 8, 10, ?', '14', '10', '12', '18', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 2, next term = 10 + 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 8, 12, 16, ?', '16', '28', '20', '24', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 4, next term = 16 + 4 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 11, 16, 21, 26, ?', '47', '26', '31', '36', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 5, next term = 26 + 5 = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 8, 11, 14, 17, ?', '23', '17', '20', '31', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 3, next term = 17 + 3 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 10, 16, 22, ?', '28', '34', '38', '22', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'd = 6, next term = 22 + 6 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 2, 6, 10, 14', 'Cannot tell', 'No', 'Sometimes', 'Yes', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Constant difference of 4 between terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 2, 4, 8, 16', 'Yes', 'Sometimes', 'No', 'Cannot tell', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 2, 4, 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 8, 11, 14, 17', 'No', 'Sometimes', 'Cannot tell', 'Yes', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Constant difference of 3 between terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 9, 14, 19, 24', 'Yes', 'Cannot tell', 'No', 'Sometimes', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Constant difference of 5 between terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 10, 14, 18, 22', 'No', 'Sometimes', 'Yes', 'Cannot tell', 2,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Constant difference of 4 between terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 4, 12, 36, 108', 'No', 'Sometimes', 'Cannot tell', 'Yes', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 8, 24, 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 3, 9, 27, 81', 'Cannot tell', 'Sometimes', 'Yes', 'No', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 6, 18, 54', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 10, 12, 14, 16', 'Yes', 'Sometimes', 'No', 'Cannot tell', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Constant difference of 2 between terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 6, 9, 12, 15', 'No', 'Yes', 'Cannot tell', 'Sometimes', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Constant difference of 3 between terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 4, 12, 36, 108', 'Cannot tell', 'No', 'Yes', 'Sometimes', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 8, 24, 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 2, 6, 18, 54', 'Sometimes', 'No', 'Cannot tell', 'Yes', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 4, 12, 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 4, 8, 16, 32', 'Yes', 'Sometimes', 'Cannot tell', 'No', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 4, 8, 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 4, 12, 36, 108', 'Sometimes', 'No', 'Cannot tell', 'Yes', 1,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 8, 24, 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 5, 9, 13, 17', 'Sometimes', 'No', 'Cannot tell', 'Yes', 3,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Constant difference of 4 between terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this an arithmetic sequence? 4, 12, 36, 108', 'No', 'Yes', 'Sometimes', 'Cannot tell', 0,
'lc_hl_sequences', 1, 'foundation', 'lc_hl', 'Differences not constant: 8, 24, 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 7, d = 5, n = 5', 'Option 4', '22', '32', '27', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 7 + (5-1) x 5 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_9 for a = 5, d = 2, n = 9', 'Option 4', '23', '19', '21', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 5 + (9-1) x 2 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_7 for a = 10, d = 6, n = 7', '52', 'Option 4', '46', '40', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 10 + (7-1) x 6 = 46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_7 for a = 1, d = 2, n = 7', '13', '15', 'Option 4', '11', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 1 + (7-1) x 2 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_9 for a = 3, d = 6, n = 9', '45', '51', 'Option 4', '57', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 3 + (9-1) x 6 = 51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_12 for a = 8, d = 5, n = 12', '68', 'Option 4', '58', '63', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 8 + (12-1) x 5 = 63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 6, d = 3, n = 5', '15', '18', 'Option 4', '21', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 6 + (5-1) x 3 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 5, d = 5, n = 5', 'Option 4', '30', '25', '20', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 5 + (5-1) x 5 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_12 for a = 9, d = 6, n = 12', '75', 'Option 4', '69', '81', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 9 + (12-1) x 6 = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_10 for a = 9, d = 2, n = 10', '25', 'Option 4', '27', '29', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 9 + (10-1) x 2 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 for a = 7, d = 6, n = 8', '43', '55', '49', 'Option 4', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 7 + (8-1) x 6 = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_7 for a = 8, d = 6, n = 7', '44', 'Option 4', '50', '38', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 8 + (7-1) x 6 = 44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_7 for a = 10, d = 6, n = 7', '52', 'Option 4', '40', '46', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 10 + (7-1) x 6 = 46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 for a = 2, d = 2, n = 8', '16', '14', '18', 'Option 4', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 2 + (8-1) x 2 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_7 for a = 6, d = 3, n = 7', '21', 'Option 4', '27', '24', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 6 + (7-1) x 3 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 6, d = 4, n = 5', 'Option 4', '26', '22', '18', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 6 + (5-1) x 4 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 for a = 5, d = 4, n = 8', '37', 'Option 4', '29', '33', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 5 + (8-1) x 4 = 33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_12 for a = 2, d = 4, n = 12', '42', 'Option 4', '50', '46', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 2 + (12-1) x 4 = 46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_7 for a = 5, d = 2, n = 7', '17', 'Option 4', '19', '15', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 5 + (7-1) x 2 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 9, d = 4, n = 5', '29', '25', '21', 'Option 4', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 9 + (5-1) x 4 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 7, d = 6, n = 5', '25', 'Option 4', '37', '31', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 7 + (5-1) x 6 = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_7 for a = 6, d = 3, n = 7', '21', '24', 'Option 4', '27', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 6 + (7-1) x 3 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 1, d = 3, n = 5', 'Option 4', '10', '13', '16', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 1 + (5-1) x 3 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 3, d = 6, n = 6', '33', 'Option 4', '39', '27', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 3 + (6-1) x 6 = 33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_11 for a = 8, d = 6, n = 11', 'Option 4', '62', '68', '74', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'T_n = a + (n-1)d = 8 + (11-1) x 6 = 68', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 5, 9, 13, ...', '5n + 1', '5n + 4', '4n + 1', '4n + 5', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 5, d = 4. T_n = 5 + (n-1) x 4 = 4n + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 6, 9, ...', '3n + 0', 'Option 4', '4n + 0', '3n + 3', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 3, d = 3. T_n = 3 + (n-1) x 3 = 3n + 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 2, 6, 10, ...', '4n - 2', '5n + -2', '2n + 4', '4n + 2', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 2, d = 4. T_n = 2 + (n-1) x 4 = 4n - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 1, 4, 7, ...', '4n + -2', '1n + 3', '3n - 2', '3n + 1', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 1, d = 3. T_n = 1 + (n-1) x 3 = 3n - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 5, 7, 9, ...', '2n + 3', '3n + 3', '5n + 2', '2n + 5', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 5, d = 2. T_n = 5 + (n-1) x 2 = 2n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 1, 3, 5, ...', '3n + -1', '1n + 2', '2n + 1', '2n - 1', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 1, d = 2. T_n = 1 + (n-1) x 2 = 2n - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 7, 11, ...', '5n + -1', '4n + 3', '3n + 4', '4n - 1', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 3, d = 4. T_n = 3 + (n-1) x 4 = 4n - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 4, 8, 12, ...', '4n + 4', 'Option 4', '5n + 0', '4n + 0', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 4, d = 4. T_n = 4 + (n-1) x 4 = 4n + 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 5, 7, 9, ...', '3n + 3', '5n + 2', '2n + 3', '2n + 5', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 5, d = 2. T_n = 5 + (n-1) x 2 = 2n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 7, 11, ...', '4n - 1', '5n + -1', '4n + 3', '3n + 4', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 3, d = 4. T_n = 3 + (n-1) x 4 = 4n - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 2, 6, 10, ...', '4n + 2', '2n + 4', '4n - 2', '5n + -2', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 2, d = 4. T_n = 2 + (n-1) x 4 = 4n - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 4, 7, 10, ...', '3n + 1', '3n + 4', '4n + 3', '4n + 1', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 4, d = 3. T_n = 4 + (n-1) x 3 = 3n + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 4, 7, 10, ...', '3n + 1', '4n + 1', '4n + 3', '3n + 4', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 4, d = 3. T_n = 4 + (n-1) x 3 = 3n + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 5, 7, ...', '2n + 1', '3n + 2', '3n + 1', '2n + 3', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 3, d = 2. T_n = 3 + (n-1) x 2 = 2n + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 4, 6, 8, ...', '2n + 4', '2n + 2', '4n + 2', '3n + 2', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', 'a = 4, d = 2. T_n = 4 + (n-1) x 2 = 2n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 5, d = 5, which term equals 65?', '12', 'Option 4', '13', '14', 2,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '65 = 5 + (n-1) x 5, solving gives n = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 5, d = 4, which term equals 53?', '13', 'Option 4', '12', '14', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '53 = 5 + (n-1) x 4, solving gives n = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 2, d = 6, which term equals 80?', '13', '14', 'Option 4', '15', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '80 = 2 + (n-1) x 6, solving gives n = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 5, d = 5, which term equals 45?', '9', 'Option 4', '10', '8', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '45 = 5 + (n-1) x 5, solving gives n = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 5, d = 6, which term equals 65?', '11', 'Option 4', '10', '12', 0,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '65 = 5 + (n-1) x 6, solving gives n = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 2, d = 5, which term equals 72?', '16', '14', 'Option 4', '15', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '72 = 2 + (n-1) x 5, solving gives n = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 2, d = 6, which term equals 68?', 'Option 4', '11', '13', '12', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '68 = 2 + (n-1) x 6, solving gives n = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 5, d = 5, which term equals 65?', '14', '13', 'Option 4', '12', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '65 = 5 + (n-1) x 5, solving gives n = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 2, d = 5, which term equals 42?', 'Option 4', '9', '8', '10', 1,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '42 = 2 + (n-1) x 5, solving gives n = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an AP with a = 5, d = 6, which term equals 89?', '16', '14', 'Option 4', '15', 3,
'lc_hl_sequences', 2, 'foundation', 'lc_hl', '89 = 5 + (n-1) x 6, solving gives n = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_9 for a = 4, d = 3, n = 9', '144', '153', '140', '36', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 9/2(2 x 4 + 8 x 3) = 144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_10 for a = 2, d = 3, n = 10', '165', '20', '153', '155', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 10/2(2 x 2 + 9 x 3) = 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 1, d = 3, n = 5', '40', '34', '5', '35', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 5/2(2 x 1 + 4 x 3) = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_9 for a = 2, d = 4, n = 9', '162', '160', '18', '171', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 9/2(2 x 2 + 8 x 4) = 162', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_7 for a = 5, d = 3, n = 7', '35', '105', '93', '98', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 7/2(2 x 5 + 6 x 3) = 98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 4, d = 3, n = 6', '65', '69', '75', '24', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 6/2(2 x 4 + 5 x 3) = 69', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_9 for a = 5, d = 3, n = 9', '45', '153', '148', '162', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 9/2(2 x 5 + 8 x 3) = 153', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_9 for a = 3, d = 4, n = 9', '180', '27', '168', '171', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 9/2(2 x 3 + 8 x 4) = 171', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_10 for a = 2, d = 3, n = 10', '20', '165', '153', '155', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 10/2(2 x 2 + 9 x 3) = 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 2, d = 2, n = 5', '28', '10', '35', '30', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 5/2(2 x 2 + 4 x 2) = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 1, d = 4, n = 6', '66', '65', '6', '72', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 6/2(2 x 1 + 5 x 4) = 66', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_8 for a = 2, d = 2, n = 8', '72', '16', '80', '70', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 8/2(2 x 2 + 7 x 2) = 72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_7 for a = 2, d = 3, n = 7', '14', '84', '75', '77', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 7/2(2 x 2 + 6 x 3) = 77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 3, d = 4, n = 5', '15', '60', '52', '55', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 5/2(2 x 3 + 4 x 4) = 55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 5, d = 4, n = 5', '65', '60', '25', '70', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 5/2(2 x 5 + 4 x 4) = 65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 5, d = 3, n = 6', '75', '70', '30', '81', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 6/2(2 x 5 + 5 x 3) = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_10 for a = 3, d = 2, n = 10', '117', '120', '130', '30', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 10/2(2 x 3 + 9 x 2) = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 5, d = 4, n = 5', '70', '60', '25', '65', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 5/2(2 x 5 + 4 x 4) = 65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_8 for a = 3, d = 3, n = 8', '108', '105', '116', '24', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 8/2(2 x 3 + 7 x 3) = 108', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_8 for a = 3, d = 2, n = 8', '77', '80', '88', '24', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(2a + (n-1)d) = 8/2(2 x 3 + 7 x 2) = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 7, last term 79, and 10 terms', '430', '790', '86', '440', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 10/2(7 + 79) = 430', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 3, last term 51, and 9 terms', '252', '459', '54', '243', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 9/2(3 + 51) = 243', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 4, last term 29, and 6 terms', '33', '99', '174', '105', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 6/2(4 + 29) = 99', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 1, last term 33, and 9 terms', '297', '34', '162', '153', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 9/2(1 + 33) = 153', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 6, last term 46, and 9 terms', '234', '243', '414', '52', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 9/2(6 + 46) = 234', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 10, last term 40, and 7 terms', '175', '280', '50', '182', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 7/2(10 + 40) = 175', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 10, last term 82, and 10 terms', '820', '460', '92', '470', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 10/2(10 + 82) = 460', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 9, last term 45, and 7 terms', '189', '54', '196', '315', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 7/2(9 + 45) = 189', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 4, last term 32, and 8 terms', '256', '152', '36', '144', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 8/2(4 + 32) = 144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 4, last term 39, and 6 terms', '234', '135', '43', '129', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 6/2(4 + 39) = 129', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 2, last term 32, and 7 terms', '126', '34', '224', '119', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 7/2(2 + 32) = 119', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 3, last term 23, and 6 terms', '84', '78', '138', '26', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 6/2(3 + 23) = 78', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 3, last term 57, and 10 terms', '570', '300', '310', '60', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 10/2(3 + 57) = 300', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 4, last term 60, and 9 terms', '64', '288', '540', '297', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 9/2(4 + 60) = 288', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find sum of AP with first term 2, last term 22, and 5 terms', '60', '110', '65', '24', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'S_n = n/2(a + l) = 5/2(2 + 22) = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 50', '1225', '1325', '2500', '1275', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 50 = n(n+1)/2 = 50 x 51/2 = 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 24', '324', '276', '300', '576', 2,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 24 = n(n+1)/2 = 24 x 25/2 = 300', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 22', '484', '253', '231', '275', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 22 = n(n+1)/2 = 22 x 23/2 = 253', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 35', '665', '595', '630', '1225', 2,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 35 = n(n+1)/2 = 35 x 36/2 = 630', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 24', '276', '300', '576', '324', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 24 = n(n+1)/2 = 24 x 25/2 = 300', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 43', '946', '989', '1849', '903', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 43 = n(n+1)/2 = 43 x 44/2 = 946', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 47', '1128', '1081', '2209', '1175', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 47 = n(n+1)/2 = 47 x 48/2 = 1128', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 33', '561', '528', '594', '1089', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 33 = n(n+1)/2 = 33 x 34/2 = 561', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 35', '630', '595', '665', '1225', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 35 = n(n+1)/2 = 35 x 36/2 = 630', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 50', '2500', '1275', '1225', '1325', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 50 = n(n+1)/2 = 50 x 51/2 = 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 25', '325', '625', '350', '300', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 25 = n(n+1)/2 = 25 x 26/2 = 325', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 15', '105', '120', '135', '225', 1,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 15 = n(n+1)/2 = 15 x 16/2 = 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 26', '351', '676', '377', '325', 0,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 26 = n(n+1)/2 = 26 x 27/2 = 351', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 14', '91', '119', '196', '105', 3,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 14 = n(n+1)/2 = 14 x 15/2 = 105', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find 1 + 2 + 3 + ... + 40', '860', '1600', '820', '780', 2,
'lc_hl_sequences', 3, 'foundation', 'lc_hl', 'Sum 1 to 40 = n(n+1)/2 = 40 x 41/2 = 820', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 1, 3, 9, 27, ...', '4', '2', '3', 'Option 4', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 3/1 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 4, 16, 64, 256, ...', '5', '12', '3', '4', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 16/4 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 1, 2, 4, 8, ...', '1', '3', 'Option 4', '2', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 2/1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 5, 20, 80, 320, ...', '3', '4', '5', '15', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 20/5 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 1, 4, 16, 64, ...', 'Option 4', '4', '3', '5', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 4/1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 2, 6, 18, 54, ...', '4', 'Option 4', '3', '2', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 1, 2, 4, 8, ...', 'Option 4', '3', '1', '2', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 2/1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 2, 4, 8, 16, ...', 'Option 4', '1', '3', '2', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 4/2 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 4, 8, 16, 32, ...', '3', '4', '1', '2', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 8/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 3, 9, 27, 81, ...', '4', '3', '2', '6', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 9/3 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 4, 8, 16, 32, ...', '3', '1', '2', '4', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 8/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 5, 15, 45, 135, ...', '2', '10', '4', '3', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 15/5 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 2, 6, 18, 54, ...', '4', 'Option 4', '2', '3', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 2, 6, 18, 54, ...', 'Option 4', '4', '2', '3', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 2, 8, 32, 128, ...', '3', '4', '6', '5', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 8/2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 5, 15, 45, 135, ...', '2', '4', '3', '10', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 15/5 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 1, 2, 4, 8, ...', '3', 'Option 4', '2', '1', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 2/1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 3, 6, 12, 24, ...', '3', '1', 'Option 4', '2', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 6/3 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 4, 16, 64, 256, ...', '3', '5', '12', '4', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 16/4 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the common ratio: 4, 8, 16, 32, ...', '2', '3', '4', '1', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Common ratio r = 8/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 2, 6, 18, 54, ?', '108', '486', '72', '162', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 3, next term = 54 x 3 = 162', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 2, 6, 18, 54, ?', '72', '108', '162', '486', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 3, next term = 54 x 3 = 162', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 8, 16, 32, ?', '128', 'Option 4', '48', '64', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 32 x 2 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 8, 16, 32, ?', '128', '48', '64', 'Option 4', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 32 x 2 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 1, 2, 4, 8, ?', '12', '16', '32', 'Option 4', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 8 x 2 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 3, 9, 27, 81, ?', '162', '729', '108', '243', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 3, next term = 81 x 3 = 243', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 3, 9, 27, 81, ?', '108', '162', '729', '243', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 3, next term = 81 x 3 = 243', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 4, 8, 16, 32, ?', '128', 'Option 4', '48', '64', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 32 x 2 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 1, 2, 4, 8, ?', 'Option 4', '32', '12', '16', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 8 x 2 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 3, 9, 27, 81, ?', '108', '162', '243', '729', 2,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 3, next term = 81 x 3 = 243', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 2, 6, 18, 54, ?', '162', '486', '72', '108', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 3, next term = 54 x 3 = 162', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 1, 3, 9, 27, ?', '243', '36', '54', '81', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 3, next term = 27 x 3 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 3, 6, 12, 24, ?', 'Option 4', '48', '36', '96', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 24 x 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 1, 2, 4, 8, ?', '16', '12', '32', 'Option 4', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 8 x 2 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the next term: 3, 6, 12, 24, ?', 'Option 4', '48', '96', '36', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'r = 2, next term = 24 x 2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 5, 8, 11, 14', 'No', 'Sometimes', 'Cannot tell', 'Yes', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 5, 8, 11, 14', 'Cannot tell', 'Yes', 'Sometimes', 'No', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 5, 11, 17, 23', 'Yes', 'Sometimes', 'Cannot tell', 'No', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 2, 4, 8, 16', 'Yes', 'Sometimes', 'Cannot tell', 'No', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Constant ratio of 2 between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 1, 6, 11, 16', 'Yes', 'Cannot tell', 'Sometimes', 'No', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 2, 4, 8, 16', 'Yes', 'No', 'Cannot tell', 'Sometimes', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Constant ratio of 2 between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 4, 7, 10, 13', 'Sometimes', 'No', 'Yes', 'Cannot tell', 1,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 2, 6, 18, 54', 'Yes', 'Cannot tell', 'Sometimes', 'No', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Constant ratio of 3 between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 2, 6, 18, 54', 'Yes', 'Cannot tell', 'Sometimes', 'No', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Constant ratio of 3 between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 5, 10, 15, 20', 'No', 'Cannot tell', 'Yes', 'Sometimes', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 4, 12, 36, 108', 'Yes', 'No', 'Sometimes', 'Cannot tell', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Constant ratio of 3 between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 4, 7, 10, 13', 'Sometimes', 'Yes', 'Cannot tell', 'No', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 3, 6, 12, 24', 'Yes', 'Cannot tell', 'Sometimes', 'No', 0,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Constant ratio of 2 between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 5, 8, 11, 14', 'Yes', 'Sometimes', 'Cannot tell', 'No', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Ratios not constant between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a geometric sequence? 2, 4, 8, 16', 'Sometimes', 'Cannot tell', 'No', 'Yes', 3,
'lc_hl_sequences', 4, 'developing', 'lc_hl', 'Constant ratio of 2 between consecutive terms', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 4, r = 3, n = 5', '60', 'Option 4', '972', '324', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 4 x 3^4 = 4 x 81 = 324', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 2, r = 3, n = 5', 'Option 4', '30', '486', '162', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 3^4 = 2 x 81 = 162', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_4 for a = 1, r = 3, n = 4', '27', '81', '12', 'Option 4', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 1 x 3^3 = 1 x 27 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 4, r = 3, n = 5', 'Option 4', '60', '972', '324', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 4 x 3^4 = 4 x 81 = 324', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 2, r = 3, n = 6', 'Option 4', '36', '486', '1458', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 3^5 = 2 x 243 = 486', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 2, r = 2, n = 6', 'Option 4', '24', '128', '64', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 2^5 = 2 x 32 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_4 for a = 2, r = 3, n = 4', 'Option 4', '162', '24', '54', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 3^3 = 2 x 27 = 54', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 1, r = 2, n = 5', '16', 'Option 4', '10', '32', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 1 x 2^4 = 1 x 16 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 3, r = 3, n = 6', '729', '2187', '54', 'Option 4', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 3 x 3^5 = 3 x 243 = 729', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 3, r = 2, n = 5', 'Option 4', '30', '48', '96', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 3 x 2^4 = 3 x 16 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 2, r = 2, n = 5', '32', '20', 'Option 4', '64', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 2^4 = 2 x 16 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 1, r = 2, n = 5', 'Option 4', '32', '10', '16', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 1 x 2^4 = 1 x 16 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 3, r = 3, n = 6', '729', '2187', '54', 'Option 4', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 3 x 3^5 = 3 x 243 = 729', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_4 for a = 3, r = 3, n = 4', 'Option 4', '243', '36', '81', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 3 x 3^3 = 3 x 27 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 2, r = 2, n = 5', 'Option 4', '64', '20', '32', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 2^4 = 2 x 16 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 2, r = 2, n = 6', '24', 'Option 4', '64', '128', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 2^5 = 2 x 32 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 2, r = 2, n = 5', '32', '64', 'Option 4', '20', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 2^4 = 2 x 16 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 4, r = 2, n = 5', '40', '64', 'Option 4', '128', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 4 x 2^4 = 4 x 16 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 2, r = 2, n = 6', '128', '64', '24', 'Option 4', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 2^5 = 2 x 32 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_4 for a = 4, r = 3, n = 4', 'Option 4', '108', '324', '48', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 4 x 3^3 = 4 x 27 = 108', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 4, r = 3, n = 5', '972', 'Option 4', '60', '324', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 4 x 3^4 = 4 x 81 = 324', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_5 for a = 1, r = 3, n = 5', '243', '81', '15', 'Option 4', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 1 x 3^4 = 1 x 81 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_4 for a = 2, r = 2, n = 4', '32', 'Option 3', '16', 'Option 4', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 2 x 2^3 = 2 x 8 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_6 for a = 3, r = 3, n = 6', '2187', '54', 'Option 4', '729', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 3 x 3^5 = 3 x 243 = 729', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_4 for a = 3, r = 2, n = 4', '48', 'Option 3', 'Option 4', '24', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_n = ar^(n-1) = 3 x 2^3 = 3 x 8 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 5 and T_4 = 135. Find r.', '3', '4', '5', '27', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 135/5 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 4 and T_4 = 108. Find r.', '27', '3', '4', 'Option 4', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 108/4 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 5 and T_4 = 40. Find r.', '2', '5', '8', '3', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 40/5 = 8, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 4 and T_4 = 32. Find r.', '8', '2', '4', '3', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 32/4 = 8, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 3 and T_4 = 81. Find r.', 'Option 4', '4', '27', '3', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 81/3 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 3 and T_4 = 81. Find r.', 'Option 4', '3', '27', '4', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 81/3 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 2 and T_4 = 16. Find r.', 'Option 4', '8', '3', '2', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 16/2 = 8, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 3 and T_4 = 24. Find r.', '8', 'Option 4', '3', '2', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 24/3 = 8, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 4 and T_4 = 108. Find r.', '3', 'Option 4', '27', '4', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 108/4 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 5 and T_4 = 135. Find r.', '3', '4', '5', '27', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 135/5 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 2 and T_4 = 16. Find r.', '8', 'Option 4', '2', '3', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 16/2 = 8, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 2 and T_4 = 16. Find r.', 'Option 4', '2', '8', '3', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 16/2 = 8, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 4 and T_4 = 32. Find r.', '3', '4', '2', '8', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 32/4 = 8, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 2 and T_4 = 54. Find r.', '3', '2', '27', '4', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 54/2 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a GP, T_1 = 2 and T_4 = 54. Find r.', '3', '2', '4', '27', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'T_4/T_1 = r^3 = 54/2 = 27, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 6, 12, ...', '3 x 2^(n-1)', '2 x 3^(n-1)', '3 + 2(n-1)', '3 x 2^n', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 3, r = 2. T_n = ar^(n-1) = 3 x 2^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 6, 12, ...', '3 x 2^n', '2 x 3^(n-1)', '3 x 2^(n-1)', '3 + 2(n-1)', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 3, r = 2. T_n = ar^(n-1) = 3 x 2^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 9, 27, ...', 'Option 4', '3 + 3(n-1)', '3 x 3^(n-1)', '3 x 3^n', 2,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 3, r = 3. T_n = ar^(n-1) = 3 x 3^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 4, 8, 16, ...', '4 x 2^(n-1)', '4 + 2(n-1)', '4 x 2^n', '2 x 4^(n-1)', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 4, r = 2. T_n = ar^(n-1) = 4 x 2^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 2, 4, 8, ...', '2 x 2^(n-1)', '2 + 2(n-1)', 'Option 4', '2 x 2^n', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 2, r = 2. T_n = ar^(n-1) = 2 x 2^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 2, 4, 8, ...', 'Option 4', '2 + 2(n-1)', '2 x 2^n', '2 x 2^(n-1)', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 2, r = 2. T_n = ar^(n-1) = 2 x 2^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 4, 12, 36, ...', '4 x 3^(n-1)', '3 x 4^(n-1)', '4 + 3(n-1)', '4 x 3^n', 0,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 4, r = 3. T_n = ar^(n-1) = 4 x 3^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 9, 27, ...', '3 x 3^n', '3 + 3(n-1)', 'Option 4', '3 x 3^(n-1)', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 3, r = 3. T_n = ar^(n-1) = 3 x 3^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 2, 4, 8, ...', '2 x 2^n', '2 x 2^(n-1)', '2 + 2(n-1)', 'Option 4', 1,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 2, r = 2. T_n = ar^(n-1) = 2 x 2^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_n for: 3, 9, 27, ...', '3 + 3(n-1)', 'Option 4', '3 x 3^n', '3 x 3^(n-1)', 3,
'lc_hl_sequences', 5, 'developing', 'lc_hl', 'a = 3, r = 3. T_n = ar^(n-1) = 3 x 3^(n-1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 2, r = 2, n = 6', '252', '128', '126', '24', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 2(2^6 - 1)/(2 - 1) = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 4, r = 3, n = 6', '4368', '1456', '72', '1460', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(3^6 - 1)/(3 - 1) = 1456', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 4, r = 2, n = 6', '252', '504', '48', '256', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(2^6 - 1)/(2 - 1) = 252', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_4 for a = 3, r = 2, n = 4', '45', '90', '48', '24', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 3(2^4 - 1)/(2 - 1) = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 4, r = 2, n = 5', '248', '40', '128', '124', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(2^5 - 1)/(2 - 1) = 124', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 4, r = 2, n = 6', '504', '252', '48', '256', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(2^6 - 1)/(2 - 1) = 252', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_4 for a = 4, r = 2, n = 4', '32', '60', '64', '120', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(2^4 - 1)/(2 - 1) = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 4, r = 3, n = 5', '484', '1452', '60', '488', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(3^5 - 1)/(3 - 1) = 484', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 4, r = 2, n = 5', '128', '124', '248', '40', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(2^5 - 1)/(2 - 1) = 124', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 2, r = 2, n = 6', '126', '252', '128', '24', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 2(2^6 - 1)/(2 - 1) = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_4 for a = 2, r = 2, n = 4', '30', '32', '16', '60', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 2(2^4 - 1)/(2 - 1) = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_4 for a = 3, r = 2, n = 4', '48', '24', '90', '45', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 3(2^4 - 1)/(2 - 1) = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 1, r = 3, n = 6', '1092', '364', '365', '18', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 1(3^6 - 1)/(3 - 1) = 364', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 3, r = 2, n = 5', '30', '93', '186', '96', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 3(2^5 - 1)/(2 - 1) = 93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_4 for a = 1, r = 3, n = 4', '12', '120', '41', '40', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 1(3^4 - 1)/(3 - 1) = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_4 for a = 1, r = 2, n = 4', '16', '15', '30', '8', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 1(2^4 - 1)/(2 - 1) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 3, r = 3, n = 6', '1092', '1095', '3276', '54', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 3(3^6 - 1)/(3 - 1) = 1092', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_4 for a = 4, r = 3, n = 4', '164', '48', '480', '160', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(3^4 - 1)/(3 - 1) = 160', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 4, r = 3, n = 5', '484', '1452', '60', '488', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(3^5 - 1)/(3 - 1) = 484', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 2, r = 2, n = 6', '252', '24', '126', '128', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 2(2^6 - 1)/(2 - 1) = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 1, r = 3, n = 5', '122', '15', '363', '121', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 1(3^5 - 1)/(3 - 1) = 121', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 4, r = 3, n = 5', '484', '488', '1452', '60', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 4(3^5 - 1)/(3 - 1) = 484', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_5 for a = 2, r = 3, n = 5', '244', '726', '30', '242', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 2(3^5 - 1)/(3 - 1) = 242', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 2, r = 2, n = 6', '126', '24', '128', '252', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 2(2^6 - 1)/(2 - 1) = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_6 for a = 3, r = 2, n = 6', '378', '192', '189', '36', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'S_n = a(r^n - 1)/(r - 1) = 3(2^6 - 1)/(2 - 1) = 189', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 5 terms: 2, 4, 8, ...', '62', '14', '20', '64', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 2, r = 2, n = 5. S_5 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 6 terms: 3, 6, 12, ...', '189', '21', '36', '192', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 3, r = 2, n = 6. S_6 = 189', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 6 terms: 1, 2, 4, ...', '63', '7', '64', '12', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 1, r = 2, n = 6. S_6 = 63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 5 terms: 2, 4, 8, ...', '20', '14', '64', '62', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 2, r = 2, n = 5. S_5 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 4 terms: 3, 6, 12, ...', '48', '21', '45', '24', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 3, r = 2, n = 4. S_4 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 6 terms: 3, 6, 12, ...', '189', '36', '21', '192', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 3, r = 2, n = 6. S_6 = 189', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 6 terms: 1, 2, 4, ...', '63', '7', '12', '64', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 1, r = 2, n = 6. S_6 = 63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 5 terms: 2, 4, 8, ...', '14', '64', '20', '62', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 2, r = 2, n = 5. S_5 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 4 terms: 3, 6, 12, ...', '21', '48', '45', '24', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 3, r = 2, n = 4. S_4 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 4 terms: 3, 6, 12, ...', '21', '24', '45', '48', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 3, r = 2, n = 4. S_4 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 6 terms: 2, 4, 8, ...', '14', '24', '126', '128', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 2, r = 2, n = 6. S_6 = 126', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 4 terms: 3, 6, 12, ...', '48', '21', '24', '45', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 3, r = 2, n = 4. S_4 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 4 terms: 2, 4, 8, ...', '16', '30', '32', '14', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 2, r = 2, n = 4. S_4 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 6 terms: 1, 2, 4, ...', '7', '64', '12', '63', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 1, r = 2, n = 6. S_6 = 63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the sum of 5 terms: 2, 4, 8, ...', '62', '20', '14', '64', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'a = 2, r = 2, n = 5. S_5 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For r > 1, the sum formula S_n = ', 'a(r^n - 1)/(r - 1)', 'ar^n', 'a/(r - 1)', 'na x r', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: a(r^n - 1)/(r - 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In S_n = a(r^n - 1)/(r - 1), ''a'' represents', 'Last term', 'First term', 'Number of terms', 'Common ratio', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: First term', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For r > 1, the sum formula S_n = ', 'a/(r - 1)', 'a(r^n - 1)/(r - 1)', 'na x r', 'ar^n', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: a(r^n - 1)/(r - 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In S_n = a(r^n - 1)/(r - 1), ''a'' represents', 'Last term', 'First term', 'Common ratio', 'Number of terms', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: First term', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For r > 1, the sum formula S_n = ', 'ar^n', 'a(r^n - 1)/(r - 1)', 'na x r', 'a/(r - 1)', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: a(r^n - 1)/(r - 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For r > 1, the sum formula S_n = ', 'a/(r - 1)', 'a(r^n - 1)/(r - 1)', 'ar^n', 'na x r', 1,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: a(r^n - 1)/(r - 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In S_n = a(r^n - 1)/(r - 1), ''a'' represents', 'First term', 'Number of terms', 'Common ratio', 'Last term', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: First term', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For r > 1, the sum formula S_n = ', 'a/(r - 1)', 'ar^n', 'a(r^n - 1)/(r - 1)', 'na x r', 2,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: a(r^n - 1)/(r - 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In S_n = a(r^n - 1)/(r - 1), ''a'' represents', 'First term', 'Common ratio', 'Number of terms', 'Last term', 0,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: First term', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In S_n = a(r^n - 1)/(r - 1), ''a'' represents', 'Number of terms', 'Last term', 'Common ratio', 'First term', 3,
'lc_hl_sequences', 6, 'developing', 'lc_hl', 'Geometric series formula: First term', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 6, r = 2/3', '6', 'Option 4', '18', '21/1', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 6/(1 - 2/3) = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 8, r = 1/2', '16', '8', '18/1', 'Option 4', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 8/(1 - 1/2) = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 7, r = 3/4', '32/1', 'Option 4', '7', '28', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 7/(1 - 3/4) = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 9, r = 1/3', '9', '27', '30/2', '27/2', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 9/(1 - 1/3) = 27/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 3, r = 1/4', '12', '4', '3', '16/3', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 3/(1 - 1/4) = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 7, r = 2/3', '24/1', 'Option 4', '7', '21', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 7/(1 - 2/3) = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 4, r = 1/3', '15/2', '12', '6', '4', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 4/(1 - 1/3) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 11, r = 1/3', '33/2', '33', '11', '36/2', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 11/(1 - 1/3) = 33/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 9, r = 1/3', '27/2', '27', '9', '30/2', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 9/(1 - 1/3) = 27/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 10, r = 1/3', '10', '33/2', '30', '15', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 10/(1 - 1/3) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 3, r = 1/2', '8/1', '6', 'Option 4', '3', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 3/(1 - 1/2) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 11, r = 2/3', 'Option 4', '33', '11', '36/1', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 11/(1 - 2/3) = 33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 11, r = 1/2', '11', '24/1', '22', 'Option 4', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 11/(1 - 1/2) = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 3, r = 3/4', '12', 'Option 4', '3', '16/1', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 3/(1 - 3/4) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 10, r = 1/2', '10', '20', 'Option 4', '22/1', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 10/(1 - 1/2) = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 10, r = 1/4', '40/3', '10', '44/3', '40', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 10/(1 - 1/4) = 40/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 6, r = 1/2', '14/1', '12', 'Option 4', '6', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 6/(1 - 1/2) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 5, r = 1/2', 'Option 4', '12/1', '5', '10', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 5/(1 - 1/2) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 5, r = 1/2', 'Option 4', '5', '10', '12/1', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 5/(1 - 1/2) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity for a = 3, r = 3/4', '3', '16/1', 'Option 4', '12', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 3/(1 - 3/4) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.5, does S_infinity exist?', 'Yes', 'No', 'Cannot tell', 'Only if a > 0', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: Yes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For S_infinity to exist, we need', 'r > 0', '-1 < r < 1', 'r != 1', 'r < 1 only', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: -1 < r < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For S_infinity to exist, we need', 'r != 1', '-1 < r < 1', 'r < 1 only', 'r > 0', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: -1 < r < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 2, does S_infinity exist?', 'No', 'Yes', 'Depends on n', 'Only if a < 1', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: No', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.5, does S_infinity exist?', 'Only if a > 0', 'Yes', 'Cannot tell', 'No', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: Yes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 2, does S_infinity exist?', 'No', 'Only if a < 1', 'Yes', 'Depends on n', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: No', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For S_infinity to exist, we need', '-1 < r < 1', 'r != 1', 'r > 0', 'r < 1 only', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: -1 < r < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A geometric series converges if', 'r > 1', '|r| < 1', 'r < 0', '|r| > 1', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: |r| < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 2, does S_infinity exist?', 'No', 'Only if a < 1', 'Yes', 'Depends on n', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: No', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.5, does S_infinity exist?', 'Yes', 'Only if a > 0', 'No', 'Cannot tell', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: Yes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A geometric series converges if', 'r > 1', '|r| > 1', '|r| < 1', 'r < 0', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: |r| < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For S_infinity to exist, we need', 'r > 0', '-1 < r < 1', 'r != 1', 'r < 1 only', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: -1 < r < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For S_infinity to exist, we need', 'r < 1 only', 'r != 1', '-1 < r < 1', 'r > 0', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: -1 < r < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 2, does S_infinity exist?', 'Yes', 'No', 'Depends on n', 'Only if a < 1', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: No', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A geometric series converges if', '|r| < 1', '|r| > 1', 'r > 1', 'r < 0', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'Convergence condition: |r| < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 2 + 2/2 + 2/4 + 2/8 + ...', '4', '8', '2', '6', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 2/(1 - 1/2) = 2/(1/2) = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 4 + 4/2 + 4/4 + 4/8 + ...', '4', '8', '12', '16', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 4/(1 - 1/2) = 4/(1/2) = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 2 + 2/2 + 2/4 + 2/8 + ...', '6', '8', '4', '2', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 2/(1 - 1/2) = 2/(1/2) = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 5 + 5/2 + 5/4 + 5/8 + ...', '15', '10', '20', '5', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 5/(1 - 1/2) = 5/(1/2) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 4 + 4/2 + 4/4 + 4/8 + ...', '12', '8', '4', '16', 1,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 4/(1 - 1/2) = 4/(1/2) = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 2 + 2/2 + 2/4 + 2/8 + ...', '8', '2', '6', '4', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 2/(1 - 1/2) = 2/(1/2) = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 2 + 2/2 + 2/4 + 2/8 + ...', '8', '6', '2', '4', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 2/(1 - 1/2) = 2/(1/2) = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 3 + 3/2 + 3/4 + 3/8 + ...', '3', '12', '9', '6', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 3/(1 - 1/2) = 3/(1/2) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 5 + 5/2 + 5/4 + 5/8 + ...', '10', '20', '15', '5', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 5/(1 - 1/2) = 5/(1/2) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 2 + 2/2 + 2/4 + 2/8 + ...', '4', '6', '2', '8', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 2/(1 - 1/2) = 2/(1/2) = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 1 + 1/2 + 1/4 + 1/8 + ...', '3', '1', '4', '2', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 1/(1 - 1/2) = 1/(1/2) = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 4 + 4/2 + 4/4 + 4/8 + ...', '12', '16', '4', '8', 3,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 4/(1 - 1/2) = 4/(1/2) = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 4 + 4/2 + 4/4 + 4/8 + ...', '12', '4', '8', '16', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 4/(1 - 1/2) = 4/(1/2) = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 2 + 2/2 + 2/4 + 2/8 + ...', '8', '6', '4', '2', 2,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 2/(1 - 1/2) = 2/(1/2) = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find: 1 + 1/2 + 1/4 + 1/8 + ...', '2', '1', '3', '4', 0,
'lc_hl_sequences', 7, 'proficient', 'lc_hl', 'S_inf = a/(1-r) = 1/(1 - 1/2) = 1/(1/2) = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 7', '7', '35', '28', '49', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 7 = 7(7+1)/2 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 5', '20', '15', '5', '25', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 5 = 5(5+1)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 6', '21', '36', '6', '27', 0,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 6 = 6(6+1)/2 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 6', '6', '27', '21', '36', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 6 = 6(6+1)/2 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 8', '44', '36', '8', '64', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 8 = 8(8+1)/2 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 6', '6', '36', '27', '21', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 6 = 6(6+1)/2 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 7', '35', '49', '28', '7', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 7 = 7(7+1)/2 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 6', '21', '27', '36', '6', 0,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 6 = 6(6+1)/2 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 6', '36', '27', '21', '6', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 6 = 6(6+1)/2 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 7', '35', '28', '7', '49', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 7 = 7(7+1)/2 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 4', '14', '16', '10', '4', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 4 = 4(4+1)/2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 8', '8', '36', '44', '64', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 8 = 8(8+1)/2 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 7', '49', '7', '35', '28', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 7 = 7(7+1)/2 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 5', '5', '15', '25', '20', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 5 = 5(5+1)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 5', '20', '25', '15', '5', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 5 = 5(5+1)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 5', '25', '20', '15', '5', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 5 = 5(5+1)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 5', '25', '15', '5', '20', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 5 = 5(5+1)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 5', '5', '15', '20', '25', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 5 = 5(5+1)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 7', '49', '35', '28', '7', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 7 = 7(7+1)/2 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (i) from i=1 to 4', '16', '4', '14', '10', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of i from 1 to 4 = 4(4+1)/2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (3) from i=1 to 4', '15', '3', '7', '12', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 3 from i=1 to 4 = 3 x 4 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (3) from i=1 to 5', '8', '3', '18', '15', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 3 from i=1 to 5 = 3 x 5 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 5', '2', '12', '10', '7', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 5 = 2 x 5 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (3) from i=1 to 3', '3', '9', '12', '6', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 3 from i=1 to 3 = 3 x 3 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (3) from i=1 to 6', '21', '9', '3', '18', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 3 from i=1 to 6 = 3 x 6 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (5) from i=1 to 4', '9', '20', '5', '25', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 5 from i=1 to 4 = 5 x 4 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 6', '14', '2', '8', '12', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 6 = 2 x 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 3', '2', '5', '6', '8', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 3 = 2 x 3 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (4) from i=1 to 5', '24', '4', '20', '9', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 4 from i=1 to 5 = 4 x 5 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 6', '14', '8', '2', '12', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 6 = 2 x 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 6', '12', '8', '2', '14', 0,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 6 = 2 x 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 4', '8', '6', '10', '2', 0,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 4 = 2 x 4 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 5', '12', '10', '7', '2', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 5 = 2 x 5 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 5', '7', '12', '2', '10', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 5 = 2 x 5 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2) from i=1 to 3', '6', '8', '2', '5', 0,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum of 2 from i=1 to 3 = 2 x 3 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2 x 2^i) from i=0 to 4', '64', '62', '20', '60', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 2 + 4 + 8 + 16 + 32 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2 x 2^i) from i=0 to 3', '32', '16', '28', '30', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 2 + 4 + 8 + 16 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (3 x 2^i) from i=0 to 2', '21', 'Option 4', '24', '18', 0,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 3 + 6 + 12 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (1 x 2^i) from i=0 to 2', '6', '8', 'Option 4', '7', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 1 + 2 + 4 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (1 x 2^i) from i=0 to 2', '8', '6', '7', 'Option 4', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 1 + 2 + 4 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (1 x 2^i) from i=0 to 3', '16', '15', '14', '8', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 1 + 2 + 4 + 8 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (1 x 2^i) from i=0 to 3', '14', '16', '8', '15', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 1 + 2 + 4 + 8 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2 x 2^i) from i=0 to 4', '60', '20', '64', '62', 3,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 2 + 4 + 8 + 16 + 32 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2 x 2^i) from i=0 to 4', '20', '64', '62', '60', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 2 + 4 + 8 + 16 + 32 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2 x 2^i) from i=0 to 4', '60', '64', '62', '20', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 2 + 4 + 8 + 16 + 32 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (1 x 2^i) from i=0 to 3', '16', '14', '15', '8', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 1 + 2 + 4 + 8 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2 x 2^i) from i=0 to 4', '20', '64', '62', '60', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 2 + 4 + 8 + 16 + 32 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (3 x 2^i) from i=0 to 4', '93', '90', '30', '96', 0,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 3 + 6 + 12 + 24 + 48 = 93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (1 x 2^i) from i=0 to 3', '16', '15', '14', '8', 1,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 1 + 2 + 4 + 8 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: Sum (2 x 2^i) from i=0 to 2', '12', '16', '14', 'Option 4', 2,
'lc_hl_sequences', 8, 'proficient', 'lc_hl', 'Sum = 2 + 4 + 8 = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $355 and increases by $15 each year. What is the salary in year 7?', 'Option 4', '460', '445', '2485', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 355, d = 15. T_7 = 355 + (7-1) x 15 = 445', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $281 and increases by $20 each year. What is the salary in year 5?', '1405', 'Option 4', '381', '361', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 281, d = 20. T_5 = 281 + (5-1) x 20 = 361', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $447 and increases by $28 each year. What is the salary in year 10?', '699', 'Option 4', '4470', '727', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 447, d = 28. T_10 = 447 + (10-1) x 28 = 699', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $147 and increases by $11 each year. What is the salary in year 5?', '191', 'Option 4', '202', '735', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 147, d = 11. T_5 = 147 + (5-1) x 11 = 191', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $448 and increases by $24 each year. What is the salary in year 6?', '568', '592', '2688', 'Option 4', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 448, d = 24. T_6 = 448 + (6-1) x 24 = 568', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $269 and increases by $26 each year. What is the salary in year 6?', '425', '1614', '399', 'Option 4', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 269, d = 26. T_6 = 269 + (6-1) x 26 = 399', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $407 and increases by $30 each year. What is the salary in year 9?', '3663', '677', '647', 'Option 4', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 407, d = 30. T_9 = 407 + (9-1) x 30 = 647', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $412 and increases by $28 each year. What is the salary in year 5?', '552', '524', '2060', 'Option 4', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 412, d = 28. T_5 = 412 + (5-1) x 28 = 524', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $473 and increases by $20 each year. What is the salary in year 10?', 'Option 4', '4730', '653', '673', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 473, d = 20. T_10 = 473 + (10-1) x 20 = 653', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $489 and increases by $14 each year. What is the salary in year 8?', '601', '3912', 'Option 4', '587', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 489, d = 14. T_8 = 489 + (8-1) x 14 = 587', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $289 and increases by $13 each year. What is the salary in year 9?', '393', '2601', '406', 'Option 4', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 289, d = 13. T_9 = 289 + (9-1) x 13 = 393', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $201 and increases by $10 each year. What is the salary in year 6?', 'Option 4', '1206', '251', '261', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 201, d = 10. T_6 = 201 + (6-1) x 10 = 251', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $135 and increases by $18 each year. What is the salary in year 10?', 'Option 4', '297', '1350', '315', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 135, d = 18. T_10 = 135 + (10-1) x 18 = 297', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $157 and increases by $25 each year. What is the salary in year 7?', '332', '307', 'Option 4', '1099', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 157, d = 25. T_7 = 157 + (7-1) x 25 = 307', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $156 and increases by $21 each year. What is the salary in year 9?', '1404', 'Option 4', '345', '324', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 156, d = 21. T_9 = 156 + (9-1) x 21 = 324', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $357 and increases by $28 each year. What is the salary in year 8?', '553', '581', 'Option 4', '2856', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 357, d = 28. T_8 = 357 + (8-1) x 28 = 553', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $216 and increases by $21 each year. What is the salary in year 9?', '405', '384', 'Option 4', '1944', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 216, d = 21. T_9 = 216 + (9-1) x 21 = 384', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $224 and increases by $20 each year. What is the salary in year 8?', '364', '1792', '384', 'Option 4', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 224, d = 20. T_8 = 224 + (8-1) x 20 = 364', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $250 and increases by $19 each year. What is the salary in year 8?', '402', '383', '2000', 'Option 4', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 250, d = 19. T_8 = 250 + (8-1) x 19 = 383', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A salary starts at $420 and increases by $12 each year. What is the salary in year 9?', '528', '3780', '516', 'Option 4', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'AP: a = 420, d = 12. T_9 = 420 + (9-1) x 12 = 516', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$4276 grows at 10% per year. Value after 2 years?', '9449', '8552', '5173', '4703', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 4276, r = 1.1. After 2 years: 4276 x 1.1^2 = 5173', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$3117 grows at 50% per year. Value after 3 years?', '10519', '9351', '4675', '13636', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 3117, r = 1.5. After 3 years: 3117 x 1.5^3 = 10519', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$3660 grows at 10% per year. Value after 3 years?', '4026', '8531', '4871', '10980', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 3660, r = 1.1. After 3 years: 3660 x 1.1^3 = 4871', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$3979 grows at 50% per year. Value after 4 years?', '20143', '15916', '5968', '24122', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 3979, r = 1.5. After 4 years: 3979 x 1.5^4 = 20143', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$1404 grows at 50% per year. Value after 4 years?', '5616', '7107', '2106', '8511', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 1404, r = 1.5. After 4 years: 1404 x 1.5^4 = 7107', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$3935 grows at 50% per year. Value after 2 years?', '8853', '5902', '7870', '12788', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 3935, r = 1.5. After 2 years: 3935 x 1.5^2 = 8853', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$3187 grows at 50% per year. Value after 2 years?', '4780', '10357', '6374', '7170', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 3187, r = 1.5. After 2 years: 3187 x 1.5^2 = 7170', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$3750 grows at 50% per year. Value after 4 years?', '22734', '15000', '5625', '18984', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 3750, r = 1.5. After 4 years: 3750 x 1.5^4 = 18984', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$4386 grows at 20% per year. Value after 2 years?', '6315', '5263', '8772', '10701', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 4386, r = 1.2. After 2 years: 4386 x 1.2^2 = 6315', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$1002 grows at 10% per year. Value after 2 years?', '2214', '2004', '1212', '1102', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 1002, r = 1.1. After 2 years: 1002 x 1.1^2 = 1212', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$1014 grows at 10% per year. Value after 3 years?', '1115', '1349', '3042', '2363', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 1014, r = 1.1. After 3 years: 1014 x 1.1^3 = 1349', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$3949 grows at 50% per year. Value after 4 years?', '5923', '19991', '15796', '23940', 1,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 3949, r = 1.5. After 4 years: 3949 x 1.5^4 = 19991', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$1542 grows at 10% per year. Value after 2 years?', '3407', '1696', '3084', '1865', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 1542, r = 1.1. After 2 years: 1542 x 1.1^2 = 1865', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$2397 grows at 50% per year. Value after 2 years?', '5393', '7790', '3595', '4794', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 2397, r = 1.5. After 2 years: 2397 x 1.5^2 = 5393', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('$4266 grows at 10% per year. Value after 4 years?', '10511', '4692', '6245', '17064', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'GP: a = 4266, r = 1.1. After 4 years: 4266 x 1.1^4 = 6245', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 400cm and bounces to 1/4 its height. Height after 3 bounces?', '388', '100', '6', '12', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/4. After 3 bounces: 400/4^3 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 200cm and bounces to 1/2 its height. Height after 3 bounces?', '100', '50', '25', '194', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 3 bounces: 200/2^3 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 100cm and bounces to 1/2 its height. Height after 4 bounces?', '12', '50', '92', '6', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 4 bounces: 100/2^4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 200cm and bounces to 1/2 its height. Height after 4 bounces?', '12', '192', '100', '24', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 4 bounces: 200/2^4 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 200cm and bounces to 1/2 its height. Height after 4 bounces?', '24', '192', '100', '12', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 4 bounces: 200/2^4 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 400cm and bounces to 1/4 its height. Height after 2 bounces?', '392', '100', '50', '25', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/4. After 2 bounces: 400/4^2 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 100cm and bounces to 1/2 its height. Height after 4 bounces?', '92', '50', '12', '6', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 4 bounces: 100/2^4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 200cm and bounces to 1/2 its height. Height after 2 bounces?', '100', 'Option 4', '196', '50', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 2 bounces: 200/2^2 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 100cm and bounces to 1/2 its height. Height after 4 bounces?', '6', '12', '50', '92', 0,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 4 bounces: 100/2^4 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 400cm and bounces to 1/2 its height. Height after 3 bounces?', '394', '100', '200', '50', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 3 bounces: 400/2^3 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 200cm and bounces to 1/2 its height. Height after 2 bounces?', 'Option 4', '100', '196', '50', 3,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 2 bounces: 200/2^2 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 200cm and bounces to 1/4 its height. Height after 2 bounces?', '24', '192', '12', '50', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/4. After 2 bounces: 200/4^2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 100cm and bounces to 1/4 its height. Height after 4 bounces?', '84', 'Option 4', '0', '25', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/4. After 4 bounces: 100/4^4 = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 100cm and bounces to 1/4 its height. Height after 4 bounces?', '25', 'Option 4', '0', '84', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/4. After 4 bounces: 100/4^4 = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ball drops from 400cm and bounces to 1/2 its height. Height after 3 bounces?', '100', '394', '50', '200', 2,
'lc_hl_sequences', 9, 'proficient', 'lc_hl', 'Each bounce = height/2. After 3 bounces: 400/2^3 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 5, 7, 9, ...', 'T_n = 3 + 2n', 'T_(n+1) = T_n x 2', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n + 2', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 10, 15, 20, ...', 'T_(n+1) = T_n + 5', 'T_(n+1) = T_n + 6', 'T_n = 5 + 5n', 'T_(n+1) = T_n x 5', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 5, so T_(n+1) = T_n + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 4, 7, 10, 13, ...', 'T_n = 4 + 3n', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n + 4', 'T_(n+1) = T_n x 3', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 3, so T_(n+1) = T_n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 6, 8, ...', 'T_n = 2 + 2n', 'T_(n+1) = T_n x 2', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n + 2', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 3, 5, 7, ...', 'T_n = 1 + 2n', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n x 2', 'T_(n+1) = T_n + 2', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 6, 8, ...', 'T_(n+1) = T_n + 3', 'T_n = 2 + 2n', 'T_(n+1) = T_n x 2', 'T_(n+1) = T_n + 2', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 8, 11, 14, ...', 'T_n = 5 + 3n', 'T_(n+1) = T_n + 4', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n x 3', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 3, so T_(n+1) = T_n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 8, 11, 14, ...', 'T_n = 5 + 3n', 'T_(n+1) = T_n + 4', 'T_(n+1) = T_n x 3', 'T_(n+1) = T_n + 3', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 3, so T_(n+1) = T_n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 6, 9, 12, ...', 'T_n = 3 + 3n', 'T_(n+1) = T_n x 3', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n + 4', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 3, so T_(n+1) = T_n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 4, 6, 8, 10, ...', 'T_(n+1) = T_n x 2', 'T_(n+1) = T_n + 2', 'T_(n+1) = T_n + 3', 'T_n = 4 + 2n', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 7, 9, 11, ...', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n + 2', 'T_n = 5 + 2n', 'T_(n+1) = T_n x 2', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 7, 9, 11, ...', 'T_(n+1) = T_n + 2', 'T_n = 5 + 2n', 'T_(n+1) = T_n x 2', 'T_(n+1) = T_n + 3', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 10, 15, 20, ...', 'T_(n+1) = T_n x 5', 'T_n = 5 + 5n', 'T_(n+1) = T_n + 5', 'T_(n+1) = T_n + 6', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 5, so T_(n+1) = T_n + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 6, 11, 16, ...', 'T_(n+1) = T_n x 5', 'T_(n+1) = T_n + 5', 'T_n = 1 + 5n', 'T_(n+1) = T_n + 6', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 5, so T_(n+1) = T_n + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 9, 13, 17, ...', 'T_(n+1) = T_n x 4', 'T_(n+1) = T_n + 5', 'T_n = 5 + 4n', 'T_(n+1) = T_n + 4', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 4, so T_(n+1) = T_n + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 5, 8, 11, 14, ...', 'T_n = 5 + 3n', 'T_(n+1) = T_n x 3', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n + 4', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 3, so T_(n+1) = T_n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 4, 8, 12, 16, ...', 'T_(n+1) = T_n + 5', 'T_n = 4 + 4n', 'T_(n+1) = T_n x 4', 'T_(n+1) = T_n + 4', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 4, so T_(n+1) = T_n + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 6, 8, ...', 'T_(n+1) = T_n + 2', 'T_(n+1) = T_n + 3', 'T_n = 2 + 2n', 'T_(n+1) = T_n x 2', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 2, so T_(n+1) = T_n + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 4, 7, 10, ...', 'T_(n+1) = T_n + 3', 'T_n = 1 + 3n', 'T_(n+1) = T_n + 4', 'T_(n+1) = T_n x 3', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 3, so T_(n+1) = T_n + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 7, 12, 17, ...', 'T_(n+1) = T_n x 5', 'T_(n+1) = T_n + 6', 'T_(n+1) = T_n + 5', 'T_n = 2 + 5n', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous + 5, so T_(n+1) = T_n + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 9, 27, 81, ...', 'T_(n+1) = T_n^3', 'T_(n+1) = 3 x T_n', 'T_n = 3 x 3^n', 'T_(n+1) = T_n + 3', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 3, so T_(n+1) = 3 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 6, 12, 24, ...', 'T_n = 3 x 2^n', 'T_(n+1) = T_n + 2', 'T_(n+1) = T_n^2', 'T_(n+1) = 2 x T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 6, 12, 24, ...', 'T_n = 3 x 2^n', 'T_(n+1) = 2 x T_n', 'T_(n+1) = T_n^2', 'T_(n+1) = T_n + 2', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 6, 12, 24, ...', 'T_(n+1) = 2 x T_n', 'T_(n+1) = T_n + 2', 'T_n = 3 x 2^n', 'T_(n+1) = T_n^2', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 6, 12, 24, ...', 'T_(n+1) = T_n^2', 'T_(n+1) = T_n + 2', 'T_(n+1) = 2 x T_n', 'T_n = 3 x 2^n', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 8, 16, ...', 'T_(n+1) = 2 x T_n', 'T_(n+1) = T_n + 2', 'T_n = 2 x 2^n', 'T_(n+1) = T_n^2', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 9, 27, 81, ...', 'T_(n+1) = T_n^3', 'T_(n+1) = 3 x T_n', 'T_(n+1) = T_n + 3', 'T_n = 3 x 3^n', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 3, so T_(n+1) = 3 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 9, 27, 81, ...', 'T_n = 3 x 3^n', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n^3', 'T_(n+1) = 3 x T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 3, so T_(n+1) = 3 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 9, 27, 81, ...', 'T_(n+1) = T_n^3', 'T_(n+1) = 3 x T_n', 'T_(n+1) = T_n + 3', 'T_n = 3 x 3^n', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 3, so T_(n+1) = 3 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 2, 4, 8, ...', 'T_(n+1) = T_n + 2', 'T_(n+1) = T_n^2', 'T_(n+1) = 2 x T_n', 'T_n = 1 x 2^n', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 8, 16, ...', 'T_n = 2 x 2^n', 'T_(n+1) = 2 x T_n', 'T_(n+1) = T_n^2', 'T_(n+1) = T_n + 2', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 8, 16, ...', 'T_(n+1) = 2 x T_n', 'T_(n+1) = T_n + 2', 'T_(n+1) = T_n^2', 'T_n = 2 x 2^n', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 6, 18, 54, ...', 'T_(n+1) = T_n^3', 'T_n = 2 x 3^n', 'T_(n+1) = T_n + 3', 'T_(n+1) = 3 x T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 3, so T_(n+1) = 3 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 6, 18, 54, ...', 'T_n = 2 x 3^n', 'T_(n+1) = T_n + 3', 'T_(n+1) = T_n^3', 'T_(n+1) = 3 x T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 3, so T_(n+1) = 3 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 2, 4, 8, ...', 'T_(n+1) = T_n^2', 'T_(n+1) = T_n + 2', 'T_n = 1 x 2^n', 'T_(n+1) = 2 x T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = previous x 2, so T_(n+1) = 2 x T_n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 4, 5, 9, 14, ...', 'T_(n+2) = T_(n+1) + T_n', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_n x 2', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 2, 4, 6, 10, ...', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_n x 2', 'T_(n+2) = T_(n+1) + T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 3, 4, 7, 11, ...', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_n x 2', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+2) = T_(n+1) + T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 3, 6, 9, 15, ...', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+2) = T_n x 2', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_(n+1) + T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 6, 10, 16, ...', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_(n+1) + T_n', 'T_(n+2) = T_n x 2', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 4, 5, 9, 14, ...', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+2) = T_n x 2', 'T_(n+2) = T_(n+1) + T_n', 'T_(n+1) = 2 x T_n', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 3, 6, 9, 15, ...', 'T_(n+2) = T_n x 2', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_(n+1) + T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 4, 5, 9, 14, ...', 'T_(n+2) = T_n x 2', 'T_(n+2) = T_(n+1) + T_n', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+1) = 2 x T_n', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 5, 8, 13, 21, ...', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_(n+1) + T_n', 'T_(n+2) = T_n x 2', 'T_n = T_(n-1) x T_(n-2)', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 2, 3, 5, 8, ...', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_(n+1) + T_n', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+2) = T_n x 2', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 4, 5, 9, 14, ...', 'T_(n+1) = 2 x T_n', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+2) = T_n x 2', 'T_(n+2) = T_(n+1) + T_n', 3,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 4, 5, 9, 14, ...', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+2) = T_n x 2', 'T_(n+2) = T_(n+1) + T_n', 'T_(n+1) = 2 x T_n', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 3, 4, 7, 11, 18, ...', 'T_(n+2) = T_n x 2', 'T_(n+2) = T_(n+1) + T_n', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+1) = 2 x T_n', 1,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 2, 4, 6, 10, 16, ...', 'T_(n+2) = T_(n+1) + T_n', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+2) = T_n x 2', 'T_(n+1) = 2 x T_n', 0,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the recurrence relation: 1, 4, 5, 9, 14, ...', 'T_n = T_(n-1) x T_(n-2)', 'T_(n+1) = 2 x T_n', 'T_(n+2) = T_(n+1) + T_n', 'T_(n+2) = T_n x 2', 2,
'lc_hl_sequences', 10, 'advanced', 'lc_hl', 'Each term = sum of previous two (Fibonacci-type)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 3, 6, 12, 24, ...', 'Both', 'Geometric', 'Neither', 'Arithmetic', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 4, 9, 14, 19, ...', 'Geometric', 'Arithmetic', 'Both', 'Neither', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 9, 12, 15, 18, ...', 'Geometric', 'Arithmetic', 'Both', 'Neither', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 1, 3, 9, 27, ...', 'Geometric', 'Both', 'Arithmetic', 'Neither', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 1, 3, 9, 27, ...', 'Neither', 'Geometric', 'Both', 'Arithmetic', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 3, 9, 27, 81, ...', 'Arithmetic', 'Neither', 'Geometric', 'Both', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 10, 12, 14, 16, ...', 'Neither', 'Geometric', 'Both', 'Arithmetic', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 3, 9, 27, 81, ...', 'Geometric', 'Arithmetic', 'Both', 'Neither', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 1, 3, 9, 27, ...', 'Both', 'Geometric', 'Arithmetic', 'Neither', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 4, 6, 8, 10, ...', 'Arithmetic', 'Neither', 'Both', 'Geometric', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 7, 12, 17, 22, ...', 'Neither', 'Both', 'Arithmetic', 'Geometric', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 2, 4, 8, 16, ...', 'Both', 'Neither', 'Geometric', 'Arithmetic', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 2, 4, 6, 8, ...', 'Geometric', 'Arithmetic', 'Both', 'Neither', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 7, 11, 15, 19, ...', 'Both', 'Arithmetic', 'Neither', 'Geometric', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 1, 2, 4, 8, ...', 'Geometric', 'Arithmetic', 'Both', 'Neither', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 1, 3, 9, 27, ...', 'Arithmetic', 'Neither', 'Geometric', 'Both', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 3, 5, 7, 9, ...', 'Neither', 'Both', 'Arithmetic', 'Geometric', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 6, 11, 16, 21, ...', 'Neither', 'Geometric', 'Arithmetic', 'Both', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 6, 9, 12, 15, ...', 'Geometric', 'Both', 'Arithmetic', 'Neither', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 3, 6, 12, 24, ...', 'Both', 'Geometric', 'Neither', 'Arithmetic', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 6, 8, 10, 12, ...', 'Neither', 'Arithmetic', 'Both', 'Geometric', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 6, 11, 16, 21, ...', 'Neither', 'Both', 'Geometric', 'Arithmetic', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant difference d = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 4, 8, 16, 32, ...', 'Geometric', 'Arithmetic', 'Neither', 'Both', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 4, 8, 16, 32, ...', 'Both', 'Arithmetic', 'Geometric', 'Neither', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sequence type: 3, 6, 12, 24, ...', 'Arithmetic', 'Geometric', 'Both', 'Neither', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Constant ratio r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: T_2=6, T_4=54. Find r', '3', '9', '6', '2', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of GP: a=3, r=2, n=5', '93', '63', '90', '96', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('S_infinity: a=8, r=1/2', '8', '32', '4', '16', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: T_5=20, T_10=35. Find d', '2', '4', '5', '3', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: a=3, d=4. Find T_10', '43', '39', '40', '36', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('S_infinity: a=8, r=1/2', '16', '8', '4', '32', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of AP: a=5, d=3, n=8', '124', '120', '116', '132', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 124', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of GP: a=3, r=2, n=5', '93', '96', '90', '63', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: T_2=6, T_4=54. Find r', '3', '6', '2', '9', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: T_5=20, T_10=35. Find d', '3', '5', '2', '4', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: a=3, d=4. Find T_10', '40', '39', '43', '36', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of AP: a=5, d=3, n=8', '124', '116', '120', '132', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 124', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: a=3, d=4. Find T_10', '43', '36', '39', '40', 2,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of GP: a=3, r=2, n=5', '90', '96', '63', '93', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: T_2=6, T_4=54. Find r', '6', '3', '9', '2', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('S_infinity: a=8, r=1/2', '8', '16', '4', '32', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of AP: a=5, d=3, n=8', '132', '124', '120', '116', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 124', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('S_infinity: a=8, r=1/2', '8', '16', '4', '32', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: T_2=6, T_4=54. Find r', '2', '9', '6', '3', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: a=3, d=4. Find T_10', '40', '43', '36', '39', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('S_infinity: a=8, r=1/2', '32', '8', '4', '16', 3,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('S_infinity: a=8, r=1/2', '4', '16', '8', '32', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: T_5=20, T_10=35. Find d', '3', '4', '5', '2', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: a=3, d=4. Find T_10', '40', '39', '43', '36', 1,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of AP: a=5, d=3, n=8', '124', '120', '132', '116', 0,
'lc_hl_sequences', 11, 'advanced', 'lc_hl', 'Apply sequence formulas. Answer: 124', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP has T_3=11, T_7=23. Find a', '3', '7', '8', '5', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In AP: a=7, d=3. Find S_20', '690', '680', '670', '660', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 670', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity: 12 + 6 + 3 + 1.5 + ...', '24', '36', '18', '12', 0,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity: 12 + 6 + 3 + 1.5 + ...', '24', '36', '12', '18', 0,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: a=100, d=-7. First negative term position?', '14', '15', '17', '16', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: a=1, S_infinity=4. Find r', '2/3', '1/4', '3/4', '1/2', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In AP: a=7, d=3. Find S_20', '660', '680', '670', '690', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 670', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum 1 + 2 + 4 + 8 + ... + 512', '512', '511', '1024', '1023', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1023', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In AP: a=7, d=3. Find S_20', '660', '680', '670', '690', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 670', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP has T_3=11, T_7=23. Find a', '8', '3', '5', '7', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum: 2 + 5 + 8 + ... + 29', '160', '145', '150', '155', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms in AP: 5, 9, 13, ..., 85?', '21', '20', '22', '19', 0,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In GP: a=5, r=2. Find S_8', '1280', '1270', '1275', '640', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Insert 3 arithmetic means between 4 and 16', '8, 11, 14', '5, 8, 11', '7, 10, 13', '6, 9, 12', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 7, 10, 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum 1 + 2 + 4 + 8 + ... + 512', '511', '512', '1023', '1024', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1023', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms in AP: 5, 9, 13, ..., 85?', '22', '19', '21', '20', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: a=1, S_infinity=4. Find r', '2/3', '1/4', '3/4', '1/2', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: S_10=155, S_20=610. Find S_30', '765', '1360', '1370', '1365', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1365', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 in GP: 3, 6, 12, ...', '192', '768', '384', '96', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 384', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: S_10=155, S_20=610. Find S_30', '1360', '765', '1365', '1370', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1365', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum: 2 + 5 + 8 + ... + 29', '145', '150', '155', '160', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP has T_2=12, T_5=324. Find r', '2', '4', '3', '27', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum: 2 + 5 + 8 + ... + 29', '150', '155', '145', '160', 1,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In AP: a=7, d=3. Find S_20', '690', '660', '670', '680', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 670', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP has T_2=12, T_5=324. Find r', '27', '2', '3', '4', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In GP: a=5, r=2. Find S_8', '1270', '640', '1280', '1275', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 in GP: 3, 6, 12, ...', '96', '192', '768', '384', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 384', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum: 2 + 5 + 8 + ... + 29', '155', '160', '145', '150', 0,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity: 12 + 6 + 3 + 1.5 + ...', '36', '12', '24', '18', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 in GP: 3, 6, 12, ...', '96', '192', '768', '384', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 384', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many terms in AP: 5, 9, 13, ..., 85?', '22', '20', '19', '21', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In GP: a=5, r=2. Find S_8', '1270', '640', '1280', '1275', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Insert 3 arithmetic means between 4 and 16', '6, 9, 12', '7, 10, 13', '5, 8, 11', '8, 11, 14', 1,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 7, 10, 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP has T_3=11, T_7=23. Find a', '8', '5', '3', '7', 1,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AP: a=100, d=-7. First negative term position?', '17', '15', '14', '16', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP has T_2=12, T_5=324. Find r', '3', '2', '4', '27', 0,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: a=1, S_infinity=4. Find r', '1/2', '2/3', '3/4', '1/4', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In AP: a=7, d=3. Find S_20', '690', '680', '660', '670', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 670', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In AP: a=7, d=3. Find S_20', '680', '690', '670', '660', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 670', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('GP: a=1, S_infinity=4. Find r', '1/2', '1/4', '2/3', '3/4', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum: 2 + 5 + 8 + ... + 29', '145', '160', '155', '150', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 in GP: 3, 6, 12, ...', '192', '384', '96', '768', 1,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 384', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In GP: a=5, r=2. Find S_8', '640', '1280', '1270', '1275', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Insert 3 arithmetic means between 4 and 16', '6, 9, 12', '8, 11, 14', '7, 10, 13', '5, 8, 11', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 7, 10, 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum: 2 + 5 + 8 + ... + 29', '145', '150', '160', '155', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 155', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find T_8 in GP: 3, 6, 12, ...', '96', '384', '768', '192', 1,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 384', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In AP: a=7, d=3. Find S_20', '660', '690', '680', '670', 3,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 670', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In GP: a=5, r=2. Find S_8', '640', '1270', '1275', '1280', 2,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In GP: a=5, r=2. Find S_8', '1270', '1275', '640', '1280', 1,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 1275', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find S_infinity: 12 + 6 + 3 + 1.5 + ...', '36', '24', '18', '12', 1,
'lc_hl_sequences', 12, 'advanced', 'lc_hl', 'Apply sequence/series techniques. Answer: 24', 1);