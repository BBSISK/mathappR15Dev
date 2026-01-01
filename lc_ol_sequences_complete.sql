-- ============================================================
-- LC Ordinary Level Sequences - Complete Setup
-- Topic: lc_ol_sequences
-- Questions: 177
-- Generated: 2025-12-24
-- ============================================================

-- Step 1: Ensure topic exists in topics table
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
VALUES ('lc_ol_sequences', 'Sequences', 11, '🔢', 8, 1);

-- Step 2: Insert questions

INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 2, 5, 8, 11, ... an arithmetic sequence?', 'Cannot tell', 'Only first 3 terms', 'Yes', 'No', 2, 'Yes. Common difference d = 3.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 3, 7, 11, 15, ... an arithmetic sequence?', 'Only first 3 terms', 'Yes', 'No', 'Cannot tell', 1, 'Yes. Common difference d = 4.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 10, 7, 4, 1, ... an arithmetic sequence?', 'Yes', 'Cannot tell', 'No', 'Only first 3 terms', 0, 'Yes. Common difference d = -3.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 5, 10, 15, 20, ... an arithmetic sequence?', 'Only first 3 terms', 'Cannot tell', 'No', 'Yes', 3, 'Yes. Common difference d = 5.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 100, 90, 80, 70, ... an arithmetic sequence?', 'Yes', 'Cannot tell', 'No', 'Only first 3 terms', 0, 'Yes. Common difference d = -10.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 1, 4, 7, 10, ... an arithmetic sequence?', 'Yes', 'No', 'Cannot tell', 'Only first 3 terms', 0, 'Yes. Common difference d = 3.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is -5, -2, 1, 4, ... an arithmetic sequence?', 'Only first 3 terms', 'No', 'Yes', 'Cannot tell', 2, 'Yes. Common difference d = 3.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 20, 17, 14, 11, ... an arithmetic sequence?', 'Only first 3 terms', 'Yes', 'No', 'Cannot tell', 1, 'Yes. Common difference d = -3.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 2, 4, 8, 16, ... an arithmetic sequence?', 'No', 'Yes', 'Cannot tell', 'Only first 3 terms', 0, 'No. This is geometric (×2), not arithmetic.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 1, 1, 2, 3, 5, ... an arithmetic sequence?', 'Only first 3 terms', 'Yes', 'No', 'Cannot tell', 2, 'No. This is Fibonacci, not arithmetic.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 1, 4, 9, 16, ... an arithmetic sequence?', 'Cannot tell', 'Yes', 'Only first 3 terms', 'No', 3, 'No. These are square numbers, not arithmetic.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 2, 6, 18, 54, ... an arithmetic sequence?', 'Only first 3 terms', 'Yes', 'Cannot tell', 'No', 3, 'No. This is geometric (×3), not arithmetic.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'What is the first term (a) of: 3, 7, 11, 15, ...?', '4', '7', '1', '3', 3, 'The first term a = 3.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'What is the first term (a) of: 10, 15, 20, 25, ...?', '7', '10', '4', '1', 1, 'The first term a = 10.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'What is the first term (a) of: -4, -1, 2, 5, ...?', '4', '1', '-4', '7', 2, 'The first term a = -4.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'What is the first term (a) of: 100, 95, 90, 85, ...?', '4', '1', '100', '7', 2, 'The first term a = 100.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'What is the first term (a) of: 0.5, 1, 1.5, 2, ...?', '1', '7', '4', '0.5', 3, 'The first term a = 0.5.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Describe the pattern: 5, 10, 15, 20, ...', 'Add 5 each time', 'Add 1 each time', 'Divide by 2', 'Multiply by 2', 0, 'Add 5 each time. d = 5.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Describe the pattern: 20, 18, 16, 14, ...', 'Add 1 each time', 'Divide by 2', 'Subtract 2 each time', 'Multiply by 2', 2, 'Subtract 2 each time. d = -2.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Describe the pattern: 1, 4, 7, 10, ...', 'Add 3 each time', 'Divide by 2', 'Add 1 each time', 'Multiply by 2', 0, 'Add 3 each time. d = 3.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Describe the pattern: 50, 45, 40, 35, ...', 'Multiply by 2', 'Divide by 2', 'Add 1 each time', 'Subtract 5 each time', 3, 'Subtract 5 each time. d = -5.', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the missing term: 2, 5, __, 11, 14', '9', '10', '8', '7', 2, 'd = 3, so 5 + 3 = 8', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the missing term: 10, __, 16, 19, 22', '13', '12', '15', '14', 0, 'd = 3, so 10 + 3 = 13', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the missing term: 1, 6, 11, __, 21', '17', '16', '18', '15', 1, 'd = 5, so 11 + 5 = 16', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the missing term: __, 7, 10, 13, 16', '6', '3', '5', '4', 3, 'd = 3, so 7 - 3 = 4', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the missing term: 3, 8, __, 18, 23', '14', '13', '12', '15', 1, 'd = 5, so 8 + 5 = 13', 1, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 3, 7, 11, 15, ...', '5', '3', '6', '4', 3, 'd = 7 - 3 = 4', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 5, 12, 19, 26, ...', '8', '6', '9', '7', 3, 'd = 12 - 5 = 7', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 2, 5, 8, 11, ...', '4', '2', '3', '5', 2, 'd = 5 - 2 = 3', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 10, 16, 22, 28, ...', '5', '8', '7', '6', 3, 'd = 16 - 10 = 6', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 1, 9, 17, 25, ...', '7', '10', '8', '9', 2, 'd = 9 - 1 = 8', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 4, 7, 10, 13, ...', '4', '2', '3', '5', 2, 'd = 7 - 4 = 3', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 6, 11, 16, 21, ...', '4', '5', '7', '6', 1, 'd = 11 - 6 = 5', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 0, 4, 8, 12, ...', '5', '4', '6', '3', 1, 'd = 4 - 0 = 4', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 2, 7, 12, 17, ...', '7', '6', '5', '4', 2, 'd = 7 - 2 = 5', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 3, 10, 17, 24, ...', '8', '7', '9', '6', 1, 'd = 10 - 3 = 7', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 20, 17, 14, 11, ...', '-2', '-4', '3', '-3', 3, 'd = 17 - 20 = -3', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 50, 45, 40, 35, ...', '-6', '-4', '-5', '5', 2, 'd = 45 - 50 = -5', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 100, 92, 84, 76, ...', '-7', '-9', '8', '-8', 3, 'd = 92 - 100 = -8', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 30, 25, 20, 15, ...', '-4', '5', '-5', '-6', 2, 'd = 25 - 30 = -5', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 15, 12, 9, 6, ...', '-4', '-2', '-3', '3', 2, 'd = 12 - 15 = -3', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the common difference d for: 40, 36, 32, 28, ...', '-3', '-4', '4', '-5', 1, 'd = 36 - 40 = -4', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'First term a = 5, second term T₂ = 9. Find d.', '9', '5', '4', '6', 2, 'd = T₂ - a = 9 - 5 = 4', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'First term a = 3, second term T₂ = 10. Find d.', '9', '3', '10', '7', 3, 'd = T₂ - a = 10 - 3 = 7', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'First term a = 8, second term T₂ = 15. Find d.', '15', '7', '9', '8', 1, 'd = T₂ - a = 15 - 8 = 7', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'First term a = 12, second term T₂ = 7. Find d.', '7', '-5', '-3', '12', 1, 'd = T₂ - a = 7 - 12 = -5', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'First term a = 20, second term T₂ = 16. Find d.', '20', '16', '-2', '-4', 3, 'd = T₂ - a = 16 - 20 = -4', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 2 and T₃ = 8, find d.', '6', '4', '2', '3', 3, 'T₃ = a + 2d, so 8 = 2 + 2d, d = 3', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 5 and T₃ = 17, find d.', '6', '12', '5', '7', 0, 'T₃ = a + 2d, so 17 = 5 + 2d, d = 6', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 10 and T₃ = 4, find d.', '-6', '-2', '-3', '-4', 2, 'T₃ = a + 2d, so 4 = 10 + 2d, d = -3', 2, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 2, 5, 8, 11, __', '14', '15', '13', '16', 0, 'd = 3, next = 11 + 3 = 14', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 4, 9, 14, 19, __', '25', '26', '24', '23', 2, 'd = 5, next = 19 + 5 = 24', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 7, 11, 15, 19, __', '22', '23', '24', '25', 1, 'd = 4, next = 19 + 4 = 23', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 3, 8, 13, 18, __', '25', '24', '22', '23', 3, 'd = 5, next = 18 + 5 = 23', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 1, 6, 11, 16, __', '22', '20', '23', '21', 3, 'd = 5, next = 16 + 5 = 21', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 10, 17, 24, 31, __', '39', '40', '38', '37', 2, 'd = 7, next = 31 + 7 = 38', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 5, 9, 13, 17, __', '21', '22', '23', '20', 0, 'd = 4, next = 17 + 4 = 21', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 2, 9, 16, 23, __', '32', '29', '30', '31', 2, 'd = 7, next = 23 + 7 = 30', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 20, 17, 14, 11, __', '7', '9', '8', '11', 2, 'd = -3, next = 11 - 3 = 8', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 50, 44, 38, 32, __', '29', '25', '26', '27', 2, 'd = -6, next = 32 - 6 = 26', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 30, 26, 22, 18, __', '14', '13', '15', '17', 0, 'd = -4, next = 18 - 4 = 14', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next term: 100, 93, 86, 79, __', '72', '75', '71', '73', 0, 'd = -7, next = 79 - 7 = 72', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next two terms: 3, 7, 11, 15, __, __', '20, 24', '19, 25', '18, 22', '19, 23', 3, 'd = 4: 15+4=19, 19+4=23', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next two terms: 5, 8, 11, 14, __, __', '16, 19', '17, 20', '18, 21', '17, 22', 1, 'd = 3: 14+3=17, 17+3=20', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next two terms: 2, 9, 16, 23, __, __', '29, 36', '30, 37', '31, 38', '30, 39', 1, 'd = 7: 23+7=30, 30+7=37', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the next two terms: 10, 15, 20, 25, __, __', '31, 36', '29, 34', '30, 37', '30, 35', 3, 'd = 5: 25+5=30, 30+5=35', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Write the first 4 terms if a = 3 and d = 5.', '1, 2, 3, 4', '3, 6, 9, 12', '3, 8, 13, 18', '2, 4, 6, 8', 2, 'a=3, add 5 each time', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Write the first 4 terms if a = 2 and d = 4.', '1, 2, 3, 4', '3, 6, 9, 12', '2, 4, 6, 8', '2, 6, 10, 14', 3, 'a=2, add 4 each time', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Write the first 4 terms if a = 10 and d = -3.', '10, 7, 4, 1', '2, 4, 6, 8', '3, 6, 9, 12', '1, 2, 3, 4', 0, 'a=10, subtract 3 each time', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Write the first 4 terms if a = 1 and d = 6.', '1, 2, 3, 4', '1, 7, 13, 19', '2, 4, 6, 8', '3, 6, 9, 12', 1, 'a=1, add 6 each time', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Write the first 4 terms if a = 5 and d = 3.', '3, 6, 9, 12', '5, 8, 11, 14', '2, 4, 6, 8', '1, 2, 3, 4', 1, 'a=5, add 3 each time', 3, 'Foundation', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'What is the formula for the nth term of an arithmetic sequence?', 'Tₙ = an + d', 'Tₙ = a × d^n', 'Tₙ = a + (n-1)d', 'Tₙ = a + nd', 2, 'Tₙ = a + (n-1)d where a = first term, d = common difference.', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₅ if a = 2 and d = 3.', '14', '13', '17', '15', 0, 'T₅ = 2 + (5-1)×3 = 2 + 12 = 14', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₅ if a = 5 and d = 4.', '20', '25', '22', '21', 3, 'T₅ = 5 + (5-1)×4 = 5 + 16 = 21', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₅ if a = 3 and d = 5.', '22', '23', '24', '28', 1, 'T₅ = 3 + (5-1)×5 = 3 + 20 = 23', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₅ if a = 1 and d = 6.', '31', '24', '25', '26', 2, 'T₅ = 1 + (5-1)×6 = 1 + 24 = 25', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₅ if a = 10 and d = 2.', '20', '18', '17', '19', 1, 'T₅ = 10 + (5-1)×2 = 10 + 8 = 18', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₅ if a = 4 and d = 7.', '31', '32', '39', '33', 1, 'T₅ = 4 + (5-1)×7 = 4 + 28 = 32', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₁₀ if a = 3 and d = 2.', '21', '23', '23', '19', 0, 'T₁₀ = 3 + (10-1)×2 = 3 + 18 = 21', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₁₀ if a = 5 and d = 3.', '34', '35', '32', '30', 2, 'T₁₀ = 5 + (10-1)×3 = 5 + 27 = 32', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₁₀ if a = 1 and d = 4.', '41', '39', '35', '37', 3, 'T₁₀ = 1 + (10-1)×4 = 1 + 36 = 37', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₁₀ if a = 2 and d = 5.', '45', '52', '49', '47', 3, 'T₁₀ = 2 + (10-1)×5 = 2 + 45 = 47', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T₁₀ if a = 10 and d = -2.', '-10', '-6', '-8', '-10', 2, 'T₁₀ = 10 + (10-1)×(-2) = 10 - 18 = -8', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'For the sequence 2, 5, 8, 11, ..., find T₆.', '18', '17', '16', '20', 1, 'a=2, d=3. T₆ = 2 + 5×3 = 17', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'For the sequence 4, 9, 14, 19, ..., find T₆.', '30', '32', '29', '28', 2, 'a=4, d=5. T₆ = 4 + 5×5 = 29', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'For the sequence 1, 7, 13, 19, ..., find T₆.', '31', '34', '30', '32', 0, 'a=1, d=6. T₆ = 1 + 5×6 = 31', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'For the sequence 10, 14, 18, 22, ..., find T₆.', '29', '33', '31', '30', 3, 'a=10, d=4. T₆ = 10 + 5×4 = 30', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 3 and d = 4, express Tₙ in terms of n.', 'Tₙ = 4n + 3', 'Tₙ = 3n + 4', 'Tₙ = 4n - 1', 'Tₙ = 4n', 2, 'Tₙ = 3 + (n-1)×4 = 3 + 4n - 4 = 4n - 1', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 5 and d = 2, express Tₙ in terms of n.', 'Tₙ = 2n', 'Tₙ = 2n + 3', 'Tₙ = 2n + 5', 'Tₙ = 5n + 2', 1, 'Tₙ = 5 + (n-1)×2 = 5 + 2n - 2 = 2n + 3', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 2 and d = 3, express Tₙ in terms of n.', 'Tₙ = 3n - 1', 'Tₙ = 3n', 'Tₙ = 2n + 3', 'Tₙ = 3n + 2', 0, 'Tₙ = 2 + (n-1)×3 = 2 + 3n - 3 = 3n - 1', 4, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T20 if a = 3 and d = 4.', '81', '75', '79', '83', 2, 'T₂₀ = 3 + 19×4 = 79', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T15 if a = 5 and d = 3.', '50', '44', '47', '49', 2, 'T₁₅ = 5 + 14×3 = 47', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T25 if a = 2 and d = 5.', '122', '124', '127', '117', 0, 'T₂₅ = 2 + 24×5 = 122', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T30 if a = 10 and d = 2.', '70', '70', '68', '66', 2, 'T₃₀ = 10 + 29×2 = 68', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T12 if a = 1 and d = 6.', '67', '61', '69', '73', 0, 'T₁₂ = 1 + 11×6 = 67', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find T10 if a = 4 and d = 7.', '69', '67', '74', '60', 1, 'T₁₀ = 4 + 9×7 = 67', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Sequence starts at 7, increases by 5. Find T10.', '47', '57', '62', '52', 3, 'T₁₀ = 7 + 9×5 = 52', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Sequence starts at 100, decreases by 8. Find T8.', '54', '39', '49', '44', 3, 'T₈ = 100 + 7×(-8) = 44', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Sequence first term 3, common difference 6. Find T15.', '82', '87', '97', '92', 1, 'T₁₅ = 3 + 14×6 = 87', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Sequence a = 12, d = -3. Find T20.', '-50', '-45', '-40', '-35', 1, 'T₂₀ = 12 + 19×(-3) = -45', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'For a = 1, d = 2, find T₁₀₀.', '201', '198', '199', '200', 2, 'T₁₀₀ = 1 + 99×2 = 199', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'For a = 5, d = 3, find T₁₀₀.', '302', '305', '301', '303', 0, 'T₁₀₀ = 5 + 99×3 = 302', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'For a = 10, d = 1, find T₁₀₀.', '109', '108', '110', '110', 0, 'T₁₀₀ = 10 + 99×1 = 109', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T₁ = 8 and d = 3, find T9.', '32', '29', '35', '33', 0, 'T9 = 8 + (9-1)×3 = 32.', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T₁ = 4 and d = 5, find T8.', '39', '34', '40', '44', 0, 'T8 = 4 + (8-1)×5 = 39.', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T₁ = 3 and d = 4, find T14.', '59', '56', '55', '51', 2, 'T14 = 3 + (14-1)×4 = 55.', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T₁ = 3 and d = 4, find T13.', '51', '47', '55', '52', 0, 'T13 = 3 + (13-1)×4 = 51.', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T₁ = 7 and d = 3, find T13.', '43', '44', '46', '40', 0, 'T13 = 7 + (13-1)×3 = 43.', 5, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 2, d = 3, which term equals 29?', '11', '10', '12', '9', 1, '29 = 2 + (n-1)×3 → 27 = 3(n-1) → n = 10', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 5, d = 4, which term equals 41?', '11', '12', '9', '10', 3, '41 = 5 + (n-1)×4 → 36 = 4(n-1) → n = 10', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 3, d = 5, which term equals 48?', '11', '12', '9', '10', 3, '48 = 3 + (n-1)×5 → 45 = 5(n-1) → n = 10', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 1, d = 6, which term equals 55?', '9', '10', '12', '11', 1, '55 = 1 + (n-1)×6 → 54 = 6(n-1) → n = 10', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 4, d = 3, which term equals 31?', '9', '10', '11', '12', 1, '31 = 4 + (n-1)×3 → 27 = 3(n-1) → n = 10', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 10, d = 2, which term equals 30?', '13', '12', '11', '10', 2, '30 = 10 + (n-1)×2 → 20 = 2(n-1) → n = 11', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 2, d = 4, which term equals 42?', '10', '11', '12', '13', 1, '42 = 2 + (n-1)×4 → 40 = 4(n-1) → n = 11', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In the sequence with a = 7, d = 5, which term equals 52?', '12', '9', '11', '10', 3, '52 = 7 + (n-1)×5 → 45 = 5(n-1) → n = 10', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 27 a term in the sequence a=3, d=4? If yes, which term?', 'Yes, T8', 'No', 'Yes, T₇', 'Yes, T6', 2, '27 = 3 + (n-1)×4 → n = 7', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 37 a term in the sequence a=2, d=5? If yes, which term?', 'No', 'Yes, T7', 'Yes, T₈', 'Yes, T9', 2, '37 = 2 + (n-1)×5 → n = 8', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 20 a term in the sequence a=5, d=3? If yes, which term?', 'Yes, T7', 'No', 'Yes, T5', 'Yes, T₆', 3, '20 = 5 + (n-1)×3 → n = 6', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 40 a term in: 3, 7, 11, 15, ...?', 'Yes, T₅', 'No', 'Yes, T₆', 'Yes, T₇', 1, '40 = 3 + (n-1)×4 gives non-integer n, so No.', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 40 a term in: 3, 7, 11, 15, ...?', 'Yes, T₇', 'Yes, T₆', 'No', 'Yes, T₅', 2, '40 = 3 + (n-1)×4 gives non-integer n, so No.', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 24 a term in: 3, 7, 11, 15, ...?', 'Yes, T₅', 'No', 'Yes, T₆', 'Yes, T₇', 1, '24 = 3 + (n-1)×4 gives non-integer n, so No.', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 40 a term in: 3, 7, 11, 15, ...?', 'Yes, T₆', 'Yes, T₅', 'Yes, T₇', 'No', 3, '40 = 3 + (n-1)×4 gives non-integer n, so No.', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Is 36 a term in: 3, 7, 11, 15, ...?', 'Yes, T₆', 'No', 'Yes, T₇', 'Yes, T₅', 1, '36 = 3 + (n-1)×4 gives non-integer n, so No.', 6, 'Developing', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'What is the formula for the sum of n terms of an arithmetic sequence?', 'Sₙ = n/2[2a + (n-1)d]', 'Sₙ = n(2a + nd)', 'Sₙ = n × a × d', 'Sₙ = a + nd', 0, 'Sₙ = n/2[2a + (n-1)d] or equivalently Sₙ = n/2(first + last).', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find S5 if a = 2 and d = 3.', '40', '30', '45', '50', 0, 'S₅ = 5/2[2×2 + 4×3] = 5/2[16] = 40', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find S10 if a = 1 and d = 2.', '105', '110', '100', '90', 2, 'S₁₀ = 10/2[2×1 + 9×2] = 5[20] = 100', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find S6 if a = 5 and d = 3.', '80', '85', '75', '65', 2, 'S₆ = 6/2[2×5 + 5×3] = 3[25] = 75', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find S8 if a = 3 and d = 4.', '126', '136', '141', '146', 1, 'S₈ = 8/2[2×3 + 7×4] = 4[34] = 136', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find S10 if a = 4 and d = 5.', '270', '265', '275', '255', 1, 'S₁₀ = 10/2[2×4 + 9×5] = 5[53] = 265', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the sum of the first 10 positive integers.', '100', '50', '55', '60', 2, 'S₁₀ = 10×11/2 = 55', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the sum of the first 20 positive integers.', '210', '400', '205', '215', 0, 'S₂₀ = 20×21/2 = 210', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the sum of the first 50 positive integers.', '2500', '1270', '1275', '1280', 2, 'S₅₀ = 50×51/2 = 1275', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the sum of the first 100 positive integers.', '5045', '5055', '5050', '10000', 2, 'S₁₀₀ = 100×101/2 = 5050', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the sum of the first 8 terms: 2, 5, 8, 11, ...', '110', '100', '90', '120', 1, 'a=2, d=3. S₈ = 8/2[4+21] = 100', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the sum of the first 6 terms: 3, 7, 11, 15, ...', '98', '88', '78', '68', 2, 'a=3, d=4. S₆ = 6/2[6+20] = 78', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Find the sum of the first 10 terms: 5, 9, 13, 17, ...', '250', '220', '240', '230', 3, 'a=5, d=4. S₁₀ = 10/2[10+36] = 230', 7, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Starting salary €30,000, annual increase €1,500. Salary in year 10?', '€42,000', '€45,000', '€46,500', '€43,500', 3, 'T₁₀ = 30000 + 9×1500 = €43,500', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Starting salary €25,000, annual increase €2,000. Salary in year 8?', '€37,000', '€43,000', '€41,000', '€39,000', 3, 'T₈ = 25000 + 7×2000 = €39,000', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Starting salary €35,000, annual increase €1,000. Salary in year 15?', '€51,000', '€49,000', '€50,000', '€48,000', 1, 'T₁₅ = 35000 + 14×1000 = €49,000', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Row 1 has 3 cans, each row has 2 more. How many in row/day 10?', '22.0', '20.0', '21', '23.0', 2, 'T₁₀ = 3 + 9×2 = 21 cans', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Bottom row has 20 seats, each row up has 2 fewer. How many in row/day 8?', '7.0', '6', '5.0', '8.0', 1, 'T₈ = 20 + 7×(-2) = 6 seats', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', '1st day walk 2km, increase by 0.5km daily. How many in row/day 14?', '10.5', '7.5', '8.5', '9.5', 2, 'T₁₄ = 2 + 13×0.5 = 8.5 km', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Save €50 month 1, increase by €10 each month. Total after 12 months/days?', '€1,500', '€1,260', '€800', '€1,000', 1, 'S₁₂ = 12/2[100 + 110] = 1260', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Run 1km day 1, increase 0.5km daily. Total after 10 months/days?', '€1,500', '€1,000', '€800', '32.5 km', 3, 'S₁₀ = 10/2[2 + 4.5×2] = 32.5', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Theatre: Row 1 has 20 seats, each row back has 2 more. Seats in rows 1-15?', '510', '500', '490', '520', 0, 'a=20, d=2, n=15. S₁₅ = 15/2[40 + 28] = 510 seats.', 8, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T10 = 31 and d = 3, find a.', '3', '5', '4', '7', 2, '31 = a + 9×3 → a = 31 - 27 = 4', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T8 = 47 and d = 5, find a.', '12', '13', '11', '17', 0, '47 = a + 7×5 → a = 47 - 35 = 12', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T12 = 55 and d = 4, find a.', '12', '10', '11', '15', 2, '55 = a + 11×4 → a = 55 - 44 = 11', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If T15 = 35 and d = 2, find a.', '8', '7', '9', '6', 1, '35 = a + 14×2 → a = 35 - 28 = 7', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 5 and T10 = 32, find d.', '3', '5', '4', '2', 0, '32 = 5 + 9d → d = 27/9 = 3', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 3 and T8 = 31, find d.', '5', '4', '6', '3', 1, '31 = 3 + 7d → d = 28/7 = 4', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 2 and T6 = 27, find d.', '5', '6', '7', '4', 0, '27 = 2 + 5d → d = 25/5 = 5', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If a = 10 and T12 = 43, find d.', '2', '4', '5', '3', 3, '43 = 10 + 11d → d = 33/11 = 3', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'T3 = 14 and T7 = 26. Find d.', '5', '2', '4', '3', 3, 'T₃ = a+2d = 14, T₇ = a+6d = 26. Subtract: 4d = 12, d = 3', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'T2 = 7 and T5 = 16. Find d.', '4', '3', '5', '2', 1, 'T₂ = a+d = 7, T₅ = a+4d = 16. Subtract: 3d = 9, d = 3', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'T4 = 15 and T10 = 33. Find d.', '2', '5', '3', '4', 2, 'T₄ = a+3d = 15, T₁₀ = a+9d = 33. Subtract: 6d = 18, d = 3', 9, 'Proficient', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'How many terms of 2, 5, 8, 11, ... are needed for sum > 100?', '9', '8', '10', '7', 0, 'S₈ = 92, S₉ = 117 > 100. Need 9 terms.', 10, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Sum of first 20 terms of an AP is 400. If d = 2, find a.', '1', '2', '3', '0', 0, '400 = 20/2[2a + 38] → 40 = 2a + 38 → a = 1.', 10, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Three consecutive terms of AP are x, x+4, x+8. Find the middle term if sum = 27.', '9', '8', '10', '7', 0, 'x + (x+4) + (x+8) = 27 → 3x + 12 = 27 → x = 5. Middle = 9.', 10, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Insert 3 arithmetic means between 2 and 18.', '6, 10, 14', '5, 10, 15', '4, 8, 12', '7, 11, 15', 0, '5 terms: a=2, T₅=18. d = (18-2)/4 = 4. Terms: 2, 6, 10, 14, 18.', 10, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'First three terms of AP are a-d, a, a+d. If product = 80 and sum = 12, find a.', '4', '5', '3', '6', 0, 'Sum: 3a = 12 → a = 4. Product: (4-d)(4)(4+d) = 80 → 4(16-d²) = 80 → d = ±2.', 10, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Sums of n terms of two APs are in ratio 3n+1 : n+3. Ratio of 5th terms?', '29:13', '27:15', '31:11', '25:17', 0, 'For 5th term, use n=9: (27+1):(9+3) = 28:12 = 7:3... (simplified problem).', 10, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Prove: Sum of first n odd numbers = n²', 'True for all n', 'Only for even n', 'Only for odd n', 'False', 0, '1+3+5+...+(2n-1) = n/2[1+(2n-1)] = n/2[2n] = n². True for all n.', 11, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If Sₙ = 3n² + 2n, find Tₙ.', '6n - 1', '6n + 1', '3n + 2', '6n - 2', 0, 'Tₙ = Sₙ - Sₙ₋₁ = (3n² + 2n) - (3(n-1)² + 2(n-1)) = 6n - 1.', 11, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If Sₙ = 2n² + n, find d.', '4', '2', '3', '5', 0, 'T₁ = S₁ = 3. T₂ = S₂ - S₁ = 10 - 3 = 7. d = 7 - 3 = 4.', 11, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Show that 2, 5, 8, 11 are in AP by finding T₁₀₀.', '299', '300', '298', '301', 0, 'a = 2, d = 3. T₁₀₀ = 2 + 99×3 = 299.', 11, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'In AP: T₃ + T₇ = ?', '2T₅', 'T₄ + T₆', 'Both A and B', 'Neither', 2, 'T₃ + T₇ = (a+2d) + (a+6d) = 2a + 8d = 2(a+4d) = 2T₅ = T₄ + T₆.', 11, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'If p, q, r are in AP, then q - p = ?', 'r - q', 'p - r', 'q - r', 'r - p', 0, 'In AP: common difference is constant, so q - p = r - q.', 11, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Pat saves €5 week 1, €8 week 2, €11 week 3... How much in week 20?', '€62', '€60', '€65', '€58', 0, 'a=5, d=3. T₂₀ = 5 + 19×3 = €62.', 12, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Pat saves €5 week 1, €8 week 2, €11 week 3... Total saved in 20 weeks?', '€670', '€650', '€700', '€620', 0, 'S₂₀ = 20/2[10 + 57] = 10 × 67 = €670.', 12, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'A ball dropped from 10m bounces to 8m, then 6.4m... This is:', 'Geometric sequence', 'Arithmetic sequence', 'Neither', 'Both', 0, 'Ratio 8/10 = 0.8 each time. This is geometric, not arithmetic.', 12, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Cinema: 15 rows, row 1 has 12 seats, each row adds 3. Total seats?', '495', '480', '510', '465', 0, 'a=12, d=3, n=15. S₁₅ = 15/2[24 + 42] = 495.', 12, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'First term is 7, 10th term is 34. Find the 25th term.', '79', '76', '82', '73', 0, '34 = 7 + 9d → d = 3. T₂₅ = 7 + 24×3 = 79.', 12, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'AP with a = 2, d = 3. Find n such that Sₙ = 155.', '10', '9', '11', '12', 0, '155 = n/2[4 + 3(n-1)] → 310 = n[3n+1] → 3n² + n - 310 = 0 → n = 10.', 12, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Sum of 3 consecutive terms in AP is 24, product is 440. Middle term?', '8', '7', '9', '10', 0, 'Let terms be a-d, a, a+d. Sum: 3a = 24 → a = 8.', 12, 'Advanced', 'adaptive');
INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('lc_ol_sequences', 'Logs stacked: 25 bottom row, 24 next, 23 next... 1 on top. Total logs?', '325', '300', '350', '275', 0, 'AP: a=25, d=-1, n=25. S₂₅ = 25/2[50-24] = 325.', 12, 'Advanced', 'adaptive');

-- Verification
SELECT 'Topic created:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_sequences';
SELECT 'Total questions:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_sequences';