-- Add Complex Numbers topic to LC Higher Level strand

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_complex', 'Complex Numbers', id, '🔮', 5, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_complex';
-- LC Higher Level - Complex Numbers Questions
-- Generated: 2025-12-14
-- Total: 600 questions

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^12', 'i', '-1', '1', '-i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^12: divide 12 by 4, remainder = 0. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^12', 'i', '-i', '-1', '1', 3,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^12: divide 12 by 4, remainder = 0. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^1', '-1', '1', '-i', 'i', 3,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^1: divide 1 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^8', '-i', '-1', '1', 'i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^8: divide 8 by 4, remainder = 0. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^1', '1', '-i', 'i', '-1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^1: divide 1 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^10', '-i', 'i', '1', '-1', 3,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^10: divide 10 by 4, remainder = 2. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^11', '1', '-i', '-1', 'i', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^11: divide 11 by 4, remainder = 3. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^17', '-i', '1', 'i', '-1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^17: divide 17 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^17', 'i', '-1', '1', '-i', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^17: divide 17 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^13', '-1', 'i', '1', '-i', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^13: divide 13 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^3', '1', '-1', '-i', 'i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^3: divide 3 by 4, remainder = 3. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^2', '1', '-1', '-i', 'i', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^2: divide 2 by 4, remainder = 2. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^1', 'i', '-i', '-1', '1', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^1: divide 1 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^7', '1', 'i', '-i', '-1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^7: divide 7 by 4, remainder = 3. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^10', '-1', 'i', '1', '-i', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^10: divide 10 by 4, remainder = 2. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^4', '-i', '1', 'i', '-1', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^4: divide 4 by 4, remainder = 0. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^1', '-i', '-1', 'i', '1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^1: divide 1 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^9', '-i', '1', '-1', 'i', 3,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^9: divide 9 by 4, remainder = 1. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^20', '1', 'i', '-i', '-1', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^20: divide 20 by 4, remainder = 0. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^18', '-1', 'i', '-i', '1', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'i^18: divide 18 by 4, remainder = 2. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('i is defined as the square root of', '0', '1', '-1', '-2', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is i^3?', '-1', 'i', '-i', '1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('i^4 equals', '-i', '1', 'i', '-1', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is i^3?', 'i', '-1', '-i', '1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is i^3?', '-1', 'i', '-i', '1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is i^2?', '1', '-i', '-1', 'i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sqrt(-1)?', '1', '-1', 'i', '-i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sqrt(-1)?', '-i', 'i', '-1', '1', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('i^4 equals', 'i', '-1', '1', '-i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sqrt(-1)?', '-i', '1', 'i', '-1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sqrt(-1)?', '-1', '-i', '1', 'i', 3,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('i is defined as the square root of', '-2', '0', '-1', '1', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('i^4 equals', '-1', '-i', 'i', '1', 3,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sqrt(-1)?', '-i', 'i', '-1', '1', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('i is defined as the square root of', '-1', '0', '-2', '1', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'Definition of i: i = sqrt(-1), so i^2 = -1. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-4)', '2', '-2', '2i', '-2i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-4) = sqrt(4) x sqrt(-1) = 2 x i = 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-4)', '-2i', '-2', '2i', '2', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-4) = sqrt(4) x sqrt(-1) = 2 x i = 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-16)', '4', '-4', '4i', '-4i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-16) = sqrt(16) x sqrt(-1) = 4 x i = 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-9)', '-3i', '-3', '3i', '3', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-9) = sqrt(9) x sqrt(-1) = 3 x i = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-4)', '-2', '-2i', '2i', '2', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-4) = sqrt(4) x sqrt(-1) = 2 x i = 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-9)', '-3', '-3i', '3i', '3', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-9) = sqrt(9) x sqrt(-1) = 3 x i = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-9)', '3i', '-3', '-3i', '3', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-9) = sqrt(9) x sqrt(-1) = 3 x i = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-25)', '5i', '5', '-5i', '-5', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-25) = sqrt(25) x sqrt(-1) = 5 x i = 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-36)', '-6i', '-6', '6', '6i', 3,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-36) = sqrt(36) x sqrt(-1) = 6 x i = 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-16)', '4i', '-4', '-4i', '4', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-16) = sqrt(16) x sqrt(-1) = 4 x i = 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-36)', '-6', '6', '6i', '-6i', 2,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-36) = sqrt(36) x sqrt(-1) = 6 x i = 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-9)', '3i', '-3', '3', '-3i', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-9) = sqrt(9) x sqrt(-1) = 3 x i = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-16)', '4i', '-4', '4', '-4i', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-16) = sqrt(16) x sqrt(-1) = 4 x i = 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-25)', '5i', '5', '-5', '-5i', 0,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-25) = sqrt(25) x sqrt(-1) = 5 x i = 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify sqrt(-36)', '6', '6i', '-6', '-6i', 1,
'lc_hl_complex', 1, 'foundation', 'lc_hl', 'sqrt(-36) = sqrt(36) x sqrt(-1) = 6 x i = 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = 1 + 6i?', '1', '7', 'Option 4', '6', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = 8 - 3i?', '5', '-3', '8', '3', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = 4 - 8i?', '4', '-8', 'Option 4', '-4', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = 4 - 3i?', '4', '3', '1', '-3', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = 2 + i?', 'Option 4', '1', '3', '2', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = -3 + 4i?', 'Option 4', '4', '-3', '1', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = -7 + 6i?', '-7', '6', '-1', 'Option 4', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = -3 + 5i?', '3', '5', '-3', '2', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = -7 + 5i?', '5', 'Option 4', '-7', '-2', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = -i?', 'Option 4', '0', 'Option 3', '-1', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = 3 - 4i?', '-1', '4', '3', '-4', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = -8i?', 'Option 4', '-8', 'Option 3', '0', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = -10 - 9i?', '9', '-10', '-19', '-9', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = -9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = -4 + 3i?', '-1', '4', '3', '-4', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = 10 + 3i?', '3', '13', 'Option 4', '10', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = 1 - 3i?', '-3', 'Option 4', '-2', '1', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = 10 - 10i?', '0', 'Option 4', '10', '-10', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = -3 + 5i?', '5', '-3', 'Option 4', '2', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the real part of z = 8 + 2i?', '2', '8', '10', 'Option 4', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, real part = a. Here a = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the imaginary part of z = -9 + 4i?', 'Option 4', '-9', '4', '-5', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'For z = a + bi, imaginary part = b. Here b = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 1 + 4i = x + yi, find x', '4', '1', '-3', '5', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8 + 6i = x + yi, find x', '6', '8', '14', '2', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8 + 4i = x + yi, find x', '8', '12', '4', 'Option 4', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 2 + 2i = x + yi, find x', 'Option 4', '2', '4', '0', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 1 + 2i = x + yi, find x', '3', '1', '2', '-1', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5 + 6i = x + yi, find x', '-1', '6', '11', '5', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5 + 6i = x + yi, find x', '5', '11', '-1', '6', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5 + 6i = x + yi, find x', '5', '6', '11', '-1', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 4 + 6i = x + yi, find x', '6', '10', '4', '-2', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5 + 2i = x + yi, find x', '2', '5', '7', '3', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 4 + 2i = x + yi, find x', '6', '2', 'Option 4', '4', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 3 + 1i = x + yi, find x', '3', '2', '4', '1', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 1 + 8i = x + yi, find x', '1', '-7', '8', '9', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 2 + 3i = x + yi, find x', '5', '-1', '2', '3', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 3 + 4i = x + yi, find x', '4', '-1', '7', '3', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Two complex numbers are equal when real parts equal and imaginary parts equal. x = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sqrt(-9) + 5 in standard form', '8i', '5 + 3i', '3i + 5', '5 - 3i', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 7 written as a complex number?', '7i', '0 + 7i', '7 + 7i', '7 + 0i', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sqrt(-9) + 5 in standard form', '8i', '5 - 3i', '5 + 3i', '3i + 5', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sqrt(-9) + 5 in standard form', '5 - 3i', '3i + 5', '8i', '5 + 3i', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 4i written in standard form?', '4 + 0i', '4i + 0', '0 + 4i', '4 + 4i', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is in standard form a + bi?', '3 + 4i', 'i4 + 3', '4i + 3', '3 + i4', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is in standard form a + bi?', '4i + 3', '3 + 4i', '3 + i4', 'i4 + 3', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 4i written in standard form?', '0 + 4i', '4 + 0i', '4 + 4i', '4i + 0', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 7 written as a complex number?', '7 + 7i', '7 + 0i', '7i', '0 + 7i', 1,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 7 written as a complex number?', '7 + 7i', '7i', '7 + 0i', '0 + 7i', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sqrt(-9) + 5 in standard form', '8i', '5 - 3i', '5 + 3i', '3i + 5', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 7 written as a complex number?', '7 + 0i', '7 + 7i', '7i', '0 + 7i', 0,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is in standard form a + bi?', 'i4 + 3', '3 + i4', '3 + 4i', '4i + 3', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 4i written in standard form?', '4 + 0i', '4 + 4i', '0 + 4i', '4i + 0', 2,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sqrt(-9) + 5 in standard form', '3i + 5', '5 - 3i', '8i', '5 + 3i', 3,
'lc_hl_complex', 2, 'foundation', 'lc_hl', 'Standard form is a + bi where a is real, b is imaginary coefficient', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-4 + 8i) + (2 + 6i)', '-2 + 15i', '-2 + 14i', '-3 + 14i', '-8 + 48i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-4 + 8i) + (2 + 6i) = (-4+2) + (8+6)i = -2 + 14i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (7 + 2i) + (5 + 2i)', '12 + 5i', '12 + 4i', '35 + 4i', '11 + 4i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(7 + 2i) + (5 + 2i) = (7+5) + (2+2)i = 12 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (7 + 6i) + (-3 + 3i)', '-21 + 18i', '3 + 9i', '4 + 9i', '4 + 10i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(7 + 6i) + (-3 + 3i) = (7+-3) + (6+3)i = 4 + 9i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + i) + (3 - 4i)', '9 - 4i', '5 - 3i', '6 - 2i', '6 - 3i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(3 + i) + (3 - 4i) = (3+3) + (1+-4)i = 6 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-5 + 5i) + (-1 + i)', '-7 + 6i', '-6 + 6i', '5 + 5i', '-6 + 7i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-5 + 5i) + (-1 + i) = (-5+-1) + (5+1)i = -6 + 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 - 3i) + (2 + 6i)', '16 - 18i', '10 + 3i', '9 + 3i', '10 + 4i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(8 - 3i) + (2 + 6i) = (8+2) + (-3+6)i = 10 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 - 2i) + (-2 + 2i)', '-8 - 4i', '2', '2 + i', '1', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(4 - 2i) + (-2 + 2i) = (4+-2) + (-2+2)i = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 - 2i) + (7 - 4i)', '8 - 6i', '14 + 8i', '9 - 5i', '9 - 6i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(2 - 2i) + (7 - 4i) = (2+7) + (-2+-4)i = 9 - 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 + 8i) + (1 + 2i)', '5 + 16i', '5 + 10i', '6 + 11i', '6 + 10i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 + 8i) + (1 + 2i) = (5+1) + (8+2)i = 6 + 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-2 - 2i) + (4 - 4i)', '1 - 6i', '-8 + 8i', '2 - 5i', '2 - 6i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-2 - 2i) + (4 - 4i) = (-2+4) + (-2+-4)i = 2 - 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 7i) + (-2 + 3i)', '4 + 11i', '3 + 10i', '-12 + 21i', '4 + 10i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(6 + 7i) + (-2 + 3i) = (6+-2) + (7+3)i = 4 + 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 + 7i) + (-5 + 5i)', '13i', '-25 + 35i', '12i', '-1 + 12i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 + 7i) + (-5 + 5i) = (5+-5) + (7+5)i = 12i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 4i) + (-2 + 8i)', '-16 + 32i', '5 + 12i', '6 + 13i', '6 + 12i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(8 + 4i) + (-2 + 8i) = (8+-2) + (4+8)i = 6 + 12i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 - 3i) + (-5 - 4i)', '-25 + 12i', '-1 - 7i', '-6i', '-7i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 - 3i) + (-5 - 4i) = (5+-5) + (-3+-4)i = -7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-5 + 8i) + (7 - i)', '2 + 8i', '1 + 7i', '-35 - 8i', '2 + 7i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-5 + 8i) + (7 - i) = (-5+7) + (8+-1)i = 2 + 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 - 3i) + (2i)', '3 - i', '4 - i', '4', '-6i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(4 - 3i) + (2i) = (4+0) + (-3+2)i = 4 - i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 - 5i) + (2i)', '2 - 2i', '1 - 3i', '-10i', '2 - 3i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(2 - 5i) + (2i) = (2+0) + (-5+2)i = 2 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 + 4i) + (-3 + 8i)', '2 + 13i', '2 + 12i', '-15 + 32i', '1 + 12i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 + 4i) + (-3 + 8i) = (5+-3) + (4+8)i = 2 + 12i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + 2i) + (-4 + 8i)', '-8 + 16i', '-2 + 11i', '-2 + 10i', '-3 + 10i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(2 + 2i) + (-4 + 8i) = (2+-4) + (2+8)i = -2 + 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + i) + (3 - 4i)', '5 - 3i', '6 - 3i', '6 - 2i', '9 - 4i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(3 + i) + (3 - 4i) = (3+3) + (1+-4)i = 6 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (7 + 8i) + (-1 + 5i)', '6 + 14i', '6 + 13i', '5 + 13i', '-7 + 40i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(7 + 8i) + (-1 + 5i) = (7+-1) + (8+5)i = 6 + 13i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + 7i) + (7 + 3i)', '8 + 11i', '7 + 21i', '7 + 10i', '8 + 10i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(1 + 7i) + (7 + 3i) = (1+7) + (7+3)i = 8 + 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + 3i) + (2i)', '5i', '6i', '1 + 6i', '1 + 5i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(1 + 3i) + (2i) = (1+0) + (3+2)i = 1 + 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-i) + (6 + 2i)', '-2i', '6 + 2i', '5 + i', '6 + i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-i) + (6 + 2i) = (0+6) + (-1+2)i = 6 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-1 + 3i) + (3 - 3i)', '2', '-3 - 9i', '1', '2 + i', 0,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-1 + 3i) + (3 - 3i) = (-1+3) + (3+-3)i = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + i) - (-2 + 8i)', '4 - 8i', '5 - 7i', '4 - 7i', '9i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(2 + i) - (-2 + 8i) = (2--2) + (1-8)i = 4 - 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 + 3i) - (7 + 2i)', '-2', '12 + 5i', '-1 + i', '-2 + i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 + 3i) - (7 + 2i) = (5-7) + (3-2)i = -2 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 7i) - (2 + 6i)', '3 + i', '2', '6 + 13i', '2 + i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(4 + 7i) - (2 + 6i) = (4-2) + (7-6)i = 2 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 6i) - (7 - 5i)', '2 + 11i', '1 + 11i', '1 + 10i', '15 + i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(8 + 6i) - (7 - 5i) = (8-7) + (6--5)i = 1 + 11i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 5i) - (-3 + 5i)', '9', '3 + 10i', '10', '9 - i', 0,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(6 + 5i) - (-3 + 5i) = (6--3) + (5-5)i = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 - 4i) - (5 + 2i)', '-4 - 6i', '-3 - 6i', '-4 - 7i', '6 - 2i', 0,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(1 - 4i) - (5 + 2i) = (1-5) + (-4-2)i = -4 - 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 - i) - (6 + 3i)', '-1 - 4i', '-2 - 4i', '10 + 2i', '-2 - 5i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(4 - i) - (6 + 3i) = (4-6) + (-1-3)i = -2 - 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 - i) - (2 + 3i)', '7 + 2i', '3 - 5i', '4 - 4i', '3 - 4i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 - i) - (2 + 3i) = (5-2) + (-1-3)i = 3 - 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + i) - (-5 - 5i)', '9 + 6i', '-1 - 4i', '9 + 5i', '10 + 6i', 0,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(4 + i) - (-5 - 5i) = (4--5) + (1--5)i = 9 + 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-1 + 3i) - (1 + 4i)', '-1 - i', '-2 - 2i', '-2 - i', '7i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-1 + 3i) - (1 + 4i) = (-1-1) + (3-4)i = -2 - i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-4 + i) - (6 - 3i)', '-10 + 3i', '2 - 2i', '-10 + 4i', '-9 + 4i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-4 + i) - (6 - 3i) = (-4-6) + (1--3)i = -10 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-2 + 4i) - (2 - i)', '-3 + 5i', '3i', '-4 + 4i', '-4 + 5i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-2 + 4i) - (2 - i) = (-2-2) + (4--1)i = -4 + 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-3 + 5i) - (2 + 2i)', '-4 + 3i', '-5 + 2i', '-5 + 3i', '-1 + 7i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-3 + 5i) - (2 + 2i) = (-3-2) + (5-2)i = -5 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 + 4i) - (2 + i)', '7 + 5i', '3 + 3i', '3 + 2i', '4 + 3i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 + 4i) - (2 + i) = (5-2) + (4-1)i = 3 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 - 5i) - (4 + 3i)', '1 - 9i', '9 - 2i', '2 - 8i', '1 - 8i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(5 - 5i) - (4 + 3i) = (5-4) + (-5-3)i = 1 - 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 2i) - (5 + 5i)', '-3i', '-1 - 3i', '-1 - 4i', '9 + 7i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(4 + 2i) - (5 + 5i) = (4-5) + (2-5)i = -1 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 5i) - (-4 + i)', '12 + 4i', '13 + 4i', '4 + 6i', '12 + 3i', 0,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(8 + 5i) - (-4 + i) = (8--4) + (5-1)i = 12 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-5 - 3i) - (-1 + 8i)', '-6 + 5i', '-3 - 11i', '-4 - 11i', '-4 - 12i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-5 - 3i) - (-1 + 8i) = (-5--1) + (-3-8)i = -4 - 11i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-5 - 2i) - (5 + 8i)', '-10 - 11i', '-9 - 10i', '-10 - 10i', '6i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-5 - 2i) - (5 + 8i) = (-5-5) + (-2-8)i = -10 - 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 7i) - (2 + 3i)', '6 + 10i', '2 + 3i', '2 + 4i', '3 + 4i', 2,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(4 + 7i) - (2 + 3i) = (4-2) + (7-3)i = 2 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-4 - 3i) - (1 - i)', '-5 - 2i', '-3 - 4i', '-4 - 2i', '-5 - 3i', 0,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-4 - 3i) - (1 - i) = (-4-1) + (-3--1)i = -5 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 6i) - (1 + 3i)', '5 + 2i', '5 + 3i', '6 + 3i', '7 + 9i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(6 + 6i) - (1 + 3i) = (6-1) + (6-3)i = 5 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 - 2i) - (1 + i)', '8 - 3i', '9 - i', '7 - 4i', '7 - 3i', 3,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(8 - 2i) - (1 + i) = (8-1) + (-2-1)i = 7 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-2 + 8i) - (-1 + 2i)', '-1 + 6i', '-1 + 5i', '-3 + 10i', '6i', 0,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(-2 + 8i) - (-1 + 2i) = (-2--1) + (8-2)i = -1 + 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 - i) - (6 - 4i)', '8 - 5i', '-4 + 3i', '-4 + 2i', '-3 + 3i', 1,
'lc_hl_complex', 3, 'foundation', 'lc_hl', '(2 - i) - (6 - 4i) = (2-6) + (-1--4)i = -4 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5(4 + i)', '20 + 5i', '9 + 6i', '4 + 5i', '20 + i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '5(4 + i) = 5(4) + 5(1)i = 20 + 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5(1 + i)', '5 + 5i', '1 + 5i', '5 + i', '6 + 6i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '5(1 + i) = 5(1) + 5(1)i = 5 + 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4(2 + 3i)', '6 + 7i', '8 + 12i', '8 + 3i', '2 + 12i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '4(2 + 3i) = 4(2) + 4(3)i = 8 + 12i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5(1 + 6i)', '5 + 30i', '1 + 30i', '6 + 11i', '5 + 6i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '5(1 + 6i) = 5(1) + 5(6)i = 5 + 30i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4(4 + 5i)', '16 + 5i', '8 + 9i', '4 + 20i', '16 + 20i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '4(4 + 5i) = 4(4) + 4(5)i = 16 + 20i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 3(3 + 3i)', '6 + 6i', '3 + 9i', '9 + 9i', '9 + 3i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', '3(3 + 3i) = 3(3) + 3(3)i = 9 + 9i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5(2 + 2i)', '10 + 10i', '10 + 2i', '2 + 10i', '7 + 7i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '5(2 + 2i) = 5(2) + 5(2)i = 10 + 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 3(5 + 6i)', '8 + 9i', '15 + 18i', '5 + 18i', '15 + 6i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '3(5 + 6i) = 3(5) + 3(6)i = 15 + 18i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4(1 + 4i)', '1 + 16i', '4 + 16i', '4 + 4i', '5 + 8i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '4(1 + 4i) = 4(1) + 4(4)i = 4 + 16i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5(4 + 5i)', '9 + 10i', '4 + 25i', '20 + 5i', '20 + 25i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '5(4 + 5i) = 5(4) + 5(5)i = 20 + 25i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 5(4 + 5i)', '4 + 25i', '20 + 25i', '20 + 5i', '9 + 10i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '5(4 + 5i) = 5(4) + 5(5)i = 20 + 25i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4(4 + 3i)', '16 + 3i', '4 + 12i', '8 + 7i', '16 + 12i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '4(4 + 3i) = 4(4) + 4(3)i = 16 + 12i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 2(3 + 6i)', '6 + 6i', '6 + 12i', '5 + 8i', '3 + 12i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '2(3 + 6i) = 2(3) + 2(6)i = 6 + 12i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 4(6 + 4i)', '24 + 16i', '6 + 16i', '24 + 4i', '10 + 8i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '4(6 + 4i) = 4(6) + 4(4)i = 24 + 16i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate 2(6 + i)', '8 + 3i', '6 + 2i', '12 + i', '12 + 2i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '2(6 + i) = 2(6) + 2(1)i = 12 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (7 + 5i)', '5 + 7i', '-7 - 5i', '-5 + 7i', '7 + 5i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(7 + 5i) = 7i + 5i^2 = 7i - 5 = -5 + 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (6 + 8i)', '6 + 8i', '8 + 6i', '-6 - 8i', '-8 + 6i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(6 + 8i) = 6i + 8i^2 = 6i - 8 = -8 + 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (2 + 6i)', '-2 - 6i', '2 + 6i', '6 + 2i', '-6 + 2i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(2 + 6i) = 2i + 6i^2 = 2i - 6 = -6 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (7 + i)', '7 + i', '-7 - i', '1 + 7i', '-1 + 7i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(7 + i) = 7i + 1i^2 = 7i - 1 = -1 + 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (8 + i)', '1 + 8i', '8 + i', '-1 + 8i', '-8 - i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(8 + i) = 8i + 1i^2 = 8i - 1 = -1 + 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (3 + 3i)', 'Option 4', '3 + 3i', '-3 + 3i', '-3 - 3i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(3 + 3i) = 3i + 3i^2 = 3i - 3 = -3 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (7 + 2i)', '7 + 2i', '-7 - 2i', '-2 + 7i', '2 + 7i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(7 + 2i) = 7i + 2i^2 = 7i - 2 = -2 + 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (3 + i)', '-1 + 3i', '3 + i', '1 + 3i', '-3 - i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(3 + i) = 3i + 1i^2 = 3i - 1 = -1 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (4 + 4i)', 'Option 4', '4 + 4i', '-4 - 4i', '-4 + 4i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(4 + 4i) = 4i + 4i^2 = 4i - 4 = -4 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate i x (8 + 4i)', '4 + 8i', '-4 + 8i', '-8 - 4i', '8 + 4i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', 'i(8 + 4i) = 8i + 4i^2 = 8i - 4 = -4 + 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + i) x (4 + 2i)', '8 + 2i', '7 + 8i', '10', '6 + 8i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + i)(4 + 2i) = 8 + 4i + 4i + 2i^2 = (8 - 2) + (4 + 4)i = 6 + 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + i) x (1 + i)', '4 + 5i', '3 + 5i', '4 + i', '5 + 3i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + i)(1 + i) = 4 + 4i + 1i + 1i^2 = (4 - 1) + (4 + 1)i = 3 + 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + i) x (2 + 4i)', '-1 + 6i', '6 + 2i', '-2 + 6i', '2 + 4i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(1 + i)(2 + 4i) = 2 + 4i + 2i + 4i^2 = (2 - 4) + (4 + 2)i = -2 + 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + 4i) x (4 + 2i)', '20i', '1 + 20i', '8 + 8i', '16 - 12i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + 4i)(4 + 2i) = 8 + 4i + 16i + 8i^2 = (8 - 8) + (4 + 16)i = 20i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 2i) x (1 + 4i)', '4 + 8i', '-4 + 18i', '-3 + 18i', '12 + 14i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + 2i)(1 + 4i) = 4 + 16i + 2i + 8i^2 = (4 - 8) + (16 + 2)i = -4 + 18i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + i) x (3 + 3i)', '6i', '6', '1 + 6i', '3 + 3i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(1 + i)(3 + 3i) = 3 + 3i + 3i + 3i^2 = (3 - 3) + (3 + 3)i = 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + i) x (1 + i)', '2 + 3i', '3 + i', '1 + 3i', '2 + i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + i)(1 + i) = 2 + 2i + 1i + 1i^2 = (2 - 1) + (2 + 1)i = 1 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 2i) x (4 + 4i)', '9 + 24i', '16 + 8i', '8 + 24i', '24 + 8i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + 2i)(4 + 4i) = 16 + 16i + 8i + 8i^2 = (16 - 8) + (16 + 8)i = 8 + 24i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + 3i) x (3 + 4i)', '6 + 12i', '-6 + 17i', '18 - i', '-5 + 17i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + 3i)(3 + 4i) = 6 + 8i + 9i + 12i^2 = (6 - 12) + (8 + 9)i = -6 + 17i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + 2i) x (4 + 4i)', '20 + 4i', '4 + 20i', '5 + 20i', '12 + 8i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(3 + 2i)(4 + 4i) = 12 + 12i + 8i + 8i^2 = (12 - 8) + (12 + 8)i = 4 + 20i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 2i) x (3 + 2i)', '16 + 2i', '12 + 4i', '8 + 14i', '9 + 14i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + 2i)(3 + 2i) = 12 + 8i + 6i + 4i^2 = (12 - 4) + (8 + 6)i = 8 + 14i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + i) x (3 + 3i)', '6 + 3i', '4 + 9i', '3 + 9i', '9 + 3i', 2,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + i)(3 + 3i) = 6 + 6i + 3i + 3i^2 = (6 - 3) + (6 + 3)i = 3 + 9i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + i) x (2 + 3i)', '1 + 8i', '4 + 3i', '7 + 4i', '2 + 8i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + i)(2 + 3i) = 4 + 6i + 2i + 3i^2 = (4 - 3) + (6 + 2)i = 1 + 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 4i) x (2 + 2i)', '1 + 16i', '16i', '16', '8 + 8i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + 4i)(2 + 2i) = 8 + 8i + 8i + 8i^2 = (8 - 8) + (8 + 8)i = 16i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 4i) x (1 + i)', '1 + 8i', '8i', '8', '4 + 4i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + 4i)(1 + i) = 4 + 4i + 4i + 4i^2 = (4 - 4) + (4 + 4)i = 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + 4i) x (1 + 2i)', '-7 + 6i', '1 + 8i', '-6 + 6i', '9 - 2i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(1 + 4i)(1 + 2i) = 1 + 2i + 4i + 8i^2 = (1 - 8) + (2 + 4)i = -7 + 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + 2i) x (2 + 4i)', '-1 + 16i', '14 + 8i', '6 + 8i', '-2 + 16i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(3 + 2i)(2 + 4i) = 6 + 12i + 4i + 8i^2 = (6 - 8) + (12 + 4)i = -2 + 16i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + 3i) x (4 + 2i)', '-2 + 14i', '4 + 6i', '-1 + 14i', '10 - 10i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(1 + 3i)(4 + 2i) = 4 + 2i + 12i + 6i^2 = (4 - 6) + (2 + 12)i = -2 + 14i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + i) x (4 + i)', '16 + 8i', '15 + 8i', '17', '16 + i', 1,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + i)(4 + i) = 16 + 4i + 4i + 1i^2 = (16 - 1) + (4 + 4)i = 15 + 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + 2i) x (3 + 4i)', '-5 + 10i', '11 - 2i', '-4 + 10i', '3 + 8i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(1 + 2i)(3 + 4i) = 3 + 4i + 6i + 8i^2 = (3 - 8) + (4 + 6)i = -5 + 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + i) x (2 + i)', '7 + 6i', '9 + 2i', '8 + 6i', '8 + i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + i)(2 + i) = 8 + 4i + 2i + 1i^2 = (8 - 1) + (4 + 2)i = 7 + 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + 2i) x (2 + 3i)', '6 + 6i', '12 + 5i', '1 + 13i', '13i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(3 + 2i)(2 + 3i) = 6 + 9i + 4i + 6i^2 = (6 - 6) + (9 + 4)i = 13i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + i) x (2 + 4i)', '8 + 6i', '4 + 4i', '1 + 10i', '10i', 3,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + i)(2 + 4i) = 4 + 8i + 2i + 4i^2 = (4 - 4) + (8 + 2)i = 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + 2i) x (3 + 4i)', '-2 + 14i', '14 + 2i', '6 + 8i', '-1 + 14i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(2 + 2i)(3 + 4i) = 6 + 8i + 6i + 8i^2 = (6 - 8) + (8 + 6)i = -2 + 14i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + i) x (1 + 2i)', '2 + 9i', '6 + 7i', '4 + 2i', '3 + 9i', 0,
'lc_hl_complex', 4, 'developing', 'lc_hl', '(4 + i)(1 + 2i) = 4 + 8i + 1i + 2i^2 = (4 - 2) + (8 + 1)i = 2 + 9i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 2i) / 2', '8 + i', '4 + i', '6', '4 + 2i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(8 + 2i)/2 = 8/2 + (2/2)i = 4 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 16i) / 4', '2 + 4i', '8 + 4i', '4 + 12i', '2 + 16i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(8 + 16i)/4 = 8/4 + (16/4)i = 2 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (12 + 6i) / 3', '4 + 6i', '9 + 3i', '12 + 2i', '4 + 2i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(12 + 6i)/3 = 12/3 + (6/3)i = 4 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 12i) / 3', '6 + 4i', '2 + 12i', '3 + 9i', '2 + 4i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(6 + 12i)/3 = 6/3 + (12/3)i = 2 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (20 + 5i) / 5', '20 + i', '4 + 5i', '4 + i', '15', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(20 + 5i)/5 = 20/5 + (5/5)i = 4 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 9i) / 3', '2 + 9i', '2 + 3i', '3 + 6i', '6 + 3i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(6 + 9i)/3 = 6/3 + (9/3)i = 2 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + 2i) / 2', '1 + i', '1 + 2i', '0', '2 + i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(2 + 2i)/2 = 2/2 + (2/2)i = 1 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 + 15i) / 5', '1 + 15i', '5 + 3i', '1 + 3i', '10i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(5 + 15i)/5 = 5/5 + (15/5)i = 1 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 8i) / 2', '4 + 4i', '6 + 6i', '8 + 4i', '4 + 8i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(8 + 8i)/2 = 8/2 + (8/2)i = 4 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (12 + 16i) / 4', '3 + 16i', '3 + 4i', '12 + 4i', '8 + 12i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(12 + 16i)/4 = 12/4 + (16/4)i = 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (15 + 5i) / 5', '10', '3 + 5i', '3 + i', '15 + i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(15 + 5i)/5 = 15/5 + (5/5)i = 3 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 16i) / 4', '2 + 4i', '2 + 16i', '8 + 4i', '4 + 12i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(8 + 16i)/4 = 8/4 + (16/4)i = 2 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (9 + 12i) / 3', '6 + 9i', '3 + 4i', '3 + 12i', '9 + 4i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(9 + 12i)/3 = 9/3 + (12/3)i = 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 3i) / 3', '2 + 3i', '6 + i', '3', '2 + i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(6 + 3i)/3 = 6/3 + (3/3)i = 2 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (10 + 15i) / 5', '5 + 10i', '10 + 3i', '2 + 3i', '2 + 15i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(10 + 15i)/5 = 10/5 + (15/5)i = 2 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + i) / i', '-3 + i', '1 - 3i', '3 - i', '-1 + 3i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(3 + i)/i = (3 + i) x (-i)/(i x -i) = (3 + i)(-i)/1 = -ai + b = 1 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 2i) / i', '2 - 6i', '6 - 2i', '-6 + 2i', '-2 + 6i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(6 + 2i)/i = (6 + 2i) x (-i)/(i x -i) = (6 + 2i)(-i)/1 = -ai + b = 2 - 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + 4i) / i', '-3 + 4i', '-4 + 3i', '3 - 4i', '4 - 3i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(3 + 4i)/i = (3 + 4i) x (-i)/(i x -i) = (3 + 4i)(-i)/1 = -ai + b = 4 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + i) / i', '3 - i', '-3 + i', '1 - 3i', '-1 + 3i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(3 + i)/i = (3 + i) x (-i)/(i x -i) = (3 + i)(-i)/1 = -ai + b = 1 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (5 + 3i) / i', '3 - 5i', '5 - 3i', '-3 + 5i', '-5 + 3i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(5 + 3i)/i = (5 + 3i) x (-i)/(i x -i) = (5 + 3i)(-i)/1 = -ai + b = 3 - 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 5i) / i', '-4 + 5i', '4 - 5i', '-5 + 4i', '5 - 4i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(4 + 5i)/i = (4 + 5i) x (-i)/(i x -i) = (4 + 5i)(-i)/1 = -ai + b = 5 - 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 + 2i) / i', '3 - 2i', '-3 + 2i', '2 - 3i', '-2 + 3i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(3 + 2i)/i = (3 + 2i) x (-i)/(i x -i) = (3 + 2i)(-i)/1 = -ai + b = 2 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 5i) / i', '4 - 5i', '5 - 4i', '-4 + 5i', '-5 + 4i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(4 + 5i)/i = (4 + 5i) x (-i)/(i x -i) = (4 + 5i)(-i)/1 = -ai + b = 5 - 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 4i) / i', '-4 + 4i', 'Option 3', 'Option 4', '4 - 4i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(4 + 4i)/i = (4 + 4i) x (-i)/(i x -i) = (4 + 4i)(-i)/1 = -ai + b = 4 - 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + i) / i', 'Option 4', '1 - i', 'Option 3', '-1 + i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(1 + i)/i = (1 + i) x (-i)/(i x -i) = (1 + i)(-i)/1 = -ai + b = 1 - i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-5 + i) / (3 + 2i)', '1 + i', '-1 + 2i', 'i', '-1 + i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(-5 + i)/(3 + 2i): Multiply by conjugate. Result = -1 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-6 - 2i) / (1 + 2i)', '-2 + 2i', '-1 + 2i', '2 + 2i', '-2 + 3i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(-6 - 2i)/(1 + 2i): Multiply by conjugate. Result = -2 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (6 + 2i) / (1 + 2i)', '2 - 2i', '3 - 2i', '-2 - 2i', '2 - i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(6 + 2i)/(1 + 2i): Multiply by conjugate. Result = 2 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 - 7i) / (2 + 3i)', '-2i', '-1 - 2i', '-1 - i', '1 - 2i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(4 - 7i)/(2 + 3i): Multiply by conjugate. Result = -1 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-13) / (3 + 2i)', '-3 + 3i', '-2 + 2i', '-3 + 2i', '3 + 2i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(-13)/(3 + 2i): Multiply by conjugate. Result = -3 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 - 3i) / (1 + i)', '-1 - 2i', '-1 - i', '1 - 2i', '-2i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(1 - 3i)/(1 + i): Multiply by conjugate. Result = -1 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (11 - 3i) / (3 + i)', '3 - 2i', '4 - 2i', '-3 - 2i', '3 - i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(11 - 3i)/(3 + i): Multiply by conjugate. Result = 3 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 - 3i) / (2 + i)', '1 - i', '-1 - 2i', '2 - 2i', '1 - 2i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(4 - 3i)/(2 + i): Multiply by conjugate. Result = 1 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (4 + 2i) / (2 + i)', '2 + i', '3', '-2', '2', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(4 + 2i)/(2 + i): Multiply by conjugate. Result = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (13i) / (2 + 3i)', '3 + 2i', '-3 + 2i', '3 + 3i', '4 + 2i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(13i)/(2 + 3i): Multiply by conjugate. Result = 3 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + 8i) / (2 + i)', '-2 + 3i', '2 + 4i', '2 + 3i', '3 + 3i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(1 + 8i)/(2 + i): Multiply by conjugate. Result = 2 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 - 6i) / (1 + 3i)', '-3i', '-1 - 2i', '-1 - 3i', '1 - 3i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(8 - 6i)/(1 + 3i): Multiply by conjugate. Result = -1 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (15 - 3i) / (3 + 2i)', '4 - 3i', '3 - 2i', '3 - 3i', '-3 - 3i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(15 - 3i)/(3 + 2i): Multiply by conjugate. Result = 3 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-6 + 12i) / (1 + 3i)', '4 + 3i', '3 + 4i', '3 + 3i', '-3 + 3i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(-6 + 12i)/(1 + 3i): Multiply by conjugate. Result = 3 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + 10i) / (2 + 2i)', '-3 + 2i', '3 + 3i', '4 + 2i', '3 + 2i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(2 + 10i)/(2 + 2i): Multiply by conjugate. Result = 3 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 - 7i) / (1 + 3i)', '-1 - i', '2 - i', '-2 - i', '-2', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(1 - 7i)/(1 + 3i): Multiply by conjugate. Result = -2 - i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-6 + 2i) / (2 + i)', '2 + 2i', '-2 + 2i', '-2 + 3i', '-1 + 2i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(-6 + 2i)/(2 + i): Multiply by conjugate. Result = -2 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (15 + 3i) / (3 + 3i)', '3 - i', '4 - 2i', '3 - 2i', '-3 - 2i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(15 + 3i)/(3 + 3i): Multiply by conjugate. Result = 3 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 - 2i) / (2 + i)', '0', 'Option 4', '-i', '1 - i', 2,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(1 - 2i)/(2 + i): Multiply by conjugate. Result = -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-9 + 7i) / (3 + i)', '2 + 3i', '-2 + 3i', '-1 + 3i', '-2 + 4i', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(-9 + 7i)/(3 + i): Multiply by conjugate. Result = -2 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (15 - 3i) / (3 + 3i)', '2 - 3i', '2 - 2i', '-2 - 3i', '3 - 3i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(15 - 3i)/(3 + 3i): Multiply by conjugate. Result = 2 - 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (3 - i) / (1 + i)', '1 - 2i', '1 - i', '2 - 2i', '-1 - 2i', 0,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(3 - i)/(1 + i): Multiply by conjugate. Result = 1 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + 2i) / (2 + 2i)', '1 + i', '1', '2', '-1', 1,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(2 + 2i)/(2 + 2i): Multiply by conjugate. Result = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (8 + 6i) / (3 + i)', '-3 + i', '4 + i', '3 + 2i', '3 + i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(8 + 6i)/(3 + i): Multiply by conjugate. Result = 3 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (-8 + 4i) / (3 + i)', '2 + 2i', '-1 + 2i', '-2 + 3i', '-2 + 2i', 3,
'lc_hl_complex', 5, 'developing', 'lc_hl', '(-8 + 4i)/(3 + i): Multiply by conjugate. Result = -2 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -3 - i', '-1 - 3i', '3 - i', '3 + i', '-3 + i', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -3 - i is -3 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 3 + 5i', '-3 + 5i', '-3 - 5i', '5 + 3i', '3 - 5i', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 3 + 5i is 3 - 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 4 + 4i', '-4 + 4i', '4 - 4i', '4 + 4i', '-4 - 4i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 4 + 4i is 4 - 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -2 + 6i', '2 + 6i', '6 - 2i', '2 - 6i', '-2 - 6i', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -2 + 6i is -2 - 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -5 - i', '5 - i', '-5 + i', '5 + i', '-1 - 5i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -5 - i is -5 + i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -6 - 3i', '-3 - 6i', '6 - 3i', '-6 + 3i', '6 + 3i', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -6 - 3i is -6 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 6 - 7i', '-6 + 7i', '6 + 7i', '-7 + 6i', '-6 - 7i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 6 - 7i is 6 + 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -2 - 2i', '2 - 2i', '2 + 2i', '-2 + 2i', '-2 - 2i', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -2 - 2i is -2 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -7 + 8i', '-7 - 8i', '8 - 7i', '7 - 8i', '7 + 8i', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -7 + 8i is -7 - 8i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -2 - 4i', '2 + 4i', '2 - 4i', '-2 + 4i', '-4 - 2i', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -2 - 4i is -2 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -3 + 7i', '3 - 7i', '-3 - 7i', '3 + 7i', '7 - 3i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -3 + 7i is -3 - 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 4 - 7i', '-7 + 4i', '4 + 7i', '-4 - 7i', '-4 + 7i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 4 - 7i is 4 + 7i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -4 + 2i', '-4 - 2i', '4 + 2i', '2 - 4i', '4 - 2i', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -4 + 2i is -4 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 6 - 3i', '-6 - 3i', '-3 + 6i', '6 + 3i', '-6 + 3i', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 6 - 3i is 6 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 2 + 2i', '-2 - 2i', '2 - 2i', '2 + 2i', '-2 + 2i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 2 + 2i is 2 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 4 + 6i', '6 + 4i', '4 - 6i', '-4 + 6i', '-4 - 6i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 4 + 6i is 4 - 6i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 8 - 3i', '-3 + 8i', '-8 + 3i', '-8 - 3i', '8 + 3i', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 8 - 3i is 8 + 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = -3 + 2i', '2 - 3i', '3 - 2i', '-3 - 2i', '3 + 2i', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of -3 + 2i is -3 - 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 4i', '4i', '-4i', '4', 'Option 4', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 4i is -4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the conjugate of z = 5 - 5i', '-5 + 5i', 'Option 4', '5 + 5i', '-5 - 5i', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate of a + bi is a - bi. Conjugate of 5 - 5i is 5 + 5i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 4 + 2i', '12', '21', '20', '16', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 4^2 + 2^2 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 2 + 4i', '20', '-12', '16', '21', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 2^2 + 4^2 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 2 + 4i', '20', '16', '21', '-12', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 2^2 + 4^2 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 3 + 2i', '13', '12', '14', '5', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 3^2 + 2^2 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 2 + 4i', '16', '20', '21', '-12', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 2^2 + 4^2 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 1 + 5i', '26', '10', '27', '-24', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 1^2 + 5^2 = 26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 2 + 3i', '12', '14', '-5', '13', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 2^2 + 3^2 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 5 + 3i', '30', '16', '34', '35', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 5^2 + 3^2 = 34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 2 + 5i', '29', '30', '-21', '20', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 2^2 + 5^2 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 5 + 5i', '50', '51', 'Option 4', '0', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 5^2 + 5^2 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 5 + 5i', 'Option 4', '0', '51', '50', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 5^2 + 5^2 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 1 + i', 'Option 4', '2', '3', '0', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 1^2 + 1^2 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 3 + i', '11', '6', '8', '10', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 3^2 + 1^2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 5 + 2i', '21', '29', '20', '30', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 5^2 + 2^2 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate z x z* where z = 3 + 4i', '25', '24', '26', '-7', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = 3^2 + 4^2 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(z*)* equals', '|z|', 'z', 'z*', '-z', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: z', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(z*)* equals', '|z|', 'z', 'z*', '-z', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: z', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(z*)* equals', '-z', 'z*', '|z|', 'z', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: z', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of i is', '-i', '-1', '1', 'i', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 3 + 4i, then z + z* equals', '6 + 8i', '8i', '0', '6', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of i is', '1', '-1', '-i', 'i', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(z*)* equals', '-z', 'z', '|z|', 'z*', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: z', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(z*)* equals', 'z*', '-z', '|z|', 'z', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: z', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of a real number is', 'zero', 'undefined', 'itself', 'its negative', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: itself', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of i is', 'i', '1', '-1', '-i', 3,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of i is', 'i', '-i', '1', '-1', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of a real number is', 'zero', 'its negative', 'itself', 'undefined', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: itself', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 3 + 4i, then z + z* equals', '0', '6', '6 + 8i', '8i', 1,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of i is', '-i', 'i', '1', '-1', 0,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 2 + 5i, then z - z* equals', '4 + 10i', '4', '10i', '0', 2,
'lc_hl_complex', 6, 'developing', 'lc_hl', 'Conjugate property: 10i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 1 - 4i on an Argand diagram?', '(-1, -4)', '(-4, 1)', '(1, 4)', '(1, -4)', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (1, -4) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -3 - 2i on an Argand diagram?', '(-3, -2)', '(-3, 2)', '(-2, -3)', '(3, -2)', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-3, -2) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 5 - 3i on an Argand diagram?', '(-5, -3)', '(-3, 5)', '(5, 3)', '(5, -3)', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (5, -3) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -3 + 5i on an Argand diagram?', '(5, -3)', '(-3, -5)', '(-3, 5)', '(3, 5)', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-3, 5) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -6 - 3i on an Argand diagram?', '(-6, -3)', '(6, -3)', '(-3, -6)', '(-6, 3)', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-6, -3) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -6 - 5i on an Argand diagram?', '(-5, -6)', '(-6, -5)', '(6, -5)', '(-6, 5)', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-6, -5) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -2 + 4i on an Argand diagram?', '(-2, -4)', '(2, 4)', '(-2, 4)', '(4, -2)', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-2, 4) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -1 - 5i on an Argand diagram?', '(-1, 5)', '(-5, -1)', '(-1, -5)', '(1, -5)', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-1, -5) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -3 + 4i on an Argand diagram?', '(-3, -4)', '(-3, 4)', '(4, -3)', '(3, 4)', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-3, 4) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -6 - 5i on an Argand diagram?', '(-6, 5)', '(-5, -6)', '(6, -5)', '(-6, -5)', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-6, -5) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 3 - 5i on an Argand diagram?', '(-3, -5)', '(3, -5)', '(-5, 3)', '(3, 5)', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (3, -5) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 2 + i on an Argand diagram?', '(2, 1)', '(2, -1)', '(1, 2)', '(-2, 1)', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (2, 1) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 6 - 4i on an Argand diagram?', '(-6, -4)', '(-4, 6)', '(6, 4)', '(6, -4)', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (6, -4) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 6 - 2i on an Argand diagram?', '(-2, 6)', '(6, -2)', '(6, 2)', '(-6, -2)', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (6, -2) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -1 - 4i on an Argand diagram?', '(-4, -1)', '(-1, 4)', '(1, -4)', '(-1, -4)', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-1, -4) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 4 + 4i on an Argand diagram?', '(4, -4)', '(-4, 4)', 'Option 4', '(4, 4)', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (4, 4) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -3 - 3i on an Argand diagram?', '(3, -3)', 'Option 4', '(-3, 3)', '(-3, -3)', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-3, -3) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -5 - 6i on an Argand diagram?', '(-5, -6)', '(-5, 6)', '(5, -6)', '(-6, -5)', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-5, -6) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = 1 - 3i on an Argand diagram?', '(-1, -3)', '(-3, 1)', '(1, -3)', '(1, 3)', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (1, -3) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What point represents z = -2 + 3i on an Argand diagram?', '(-2, -3)', '(3, -2)', '(-2, 3)', '(2, 3)', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'z = a + bi is plotted at (a, b) = (-2, 3) on Argand diagram', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -5 - 3i located?', 'Third quadrant', 'Fourth quadrant', 'First quadrant', 'Second quadrant', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -5 (negative), b = -3 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -2 - 4i located?', 'Third quadrant', 'First quadrant', 'Second quadrant', 'Fourth quadrant', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -2 (negative), b = -4 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = 1 + 3i located?', 'Second quadrant', 'First quadrant', 'Fourth quadrant', 'Third quadrant', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = 1 (positive), b = 3 (positive). First quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -3 - i located?', 'First quadrant', 'Fourth quadrant', 'Second quadrant', 'Third quadrant', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -3 (negative), b = -1 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -5 - 2i located?', 'First quadrant', 'Fourth quadrant', 'Third quadrant', 'Second quadrant', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -5 (negative), b = -2 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -3 - i located?', 'Second quadrant', 'Third quadrant', 'First quadrant', 'Fourth quadrant', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -3 (negative), b = -1 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = 1 + 2i located?', 'First quadrant', 'Third quadrant', 'Fourth quadrant', 'Second quadrant', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = 1 (positive), b = 2 (positive). First quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -3 - 4i located?', 'Second quadrant', 'First quadrant', 'Third quadrant', 'Fourth quadrant', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -3 (negative), b = -4 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -1 - 4i located?', 'Fourth quadrant', 'Second quadrant', 'Third quadrant', 'First quadrant', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -1 (negative), b = -4 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = 2 - 3i located?', 'First quadrant', 'Second quadrant', 'Fourth quadrant', 'Third quadrant', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = 2 (positive), b = -3 (negative). Fourth quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = 1 - 3i located?', 'First quadrant', 'Third quadrant', 'Second quadrant', 'Fourth quadrant', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = 1 (positive), b = -3 (negative). Fourth quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = 5 - 4i located?', 'Fourth quadrant', 'Third quadrant', 'Second quadrant', 'First quadrant', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = 5 (positive), b = -4 (negative). Fourth quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -1 - 3i located?', 'Second quadrant', 'Third quadrant', 'Fourth quadrant', 'First quadrant', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -1 (negative), b = -3 (negative). Third quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -4 + 5i located?', 'Third quadrant', 'Second quadrant', 'First quadrant', 'Fourth quadrant', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -4 (negative), b = 5 (positive). Second quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In which quadrant is z = -2 + 3i located?', 'Fourth quadrant', 'Second quadrant', 'Third quadrant', 'First quadrant', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'a = -2 (negative), b = 3 (positive). Second quadrant', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance from origin to z on Argand diagram is', '|z|', 'z*', 'Re(z)', 'arg(z)', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: |z|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On an Argand diagram, the y-axis represents', 'Real numbers', 'Imaginary numbers', 'Conjugates', 'Arguments', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Imaginary numbers', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Conjugate of z is reflected across the', 'Line y = x', 'Imaginary axis', 'Real axis', 'Origin', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Real axis', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance from origin to z on Argand diagram is', '|z|', 'Re(z)', 'arg(z)', 'z*', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: |z|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance from origin to z on Argand diagram is', 'arg(z)', 'Re(z)', '|z|', 'z*', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: |z|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On an Argand diagram, the x-axis represents', 'Complex numbers', 'Imaginary numbers', 'Modulus', 'Real numbers', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Real numbers', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Adding complex numbers is like adding', 'Scalars', 'Vectors', 'Matrices', 'Angles', 1,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Vectors', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance from origin to z on Argand diagram is', 'z*', 'Re(z)', 'arg(z)', '|z|', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: |z|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On an Argand diagram, the y-axis represents', 'Conjugates', 'Real numbers', 'Arguments', 'Imaginary numbers', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Imaginary numbers', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On an Argand diagram, the x-axis represents', 'Imaginary numbers', 'Complex numbers', 'Modulus', 'Real numbers', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Real numbers', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Conjugate of z is reflected across the', 'Imaginary axis', 'Line y = x', 'Real axis', 'Origin', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Real axis', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Conjugate of z is reflected across the', 'Line y = x', 'Origin', 'Imaginary axis', 'Real axis', 3,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Real axis', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Conjugate of z is reflected across the', 'Imaginary axis', 'Origin', 'Real axis', 'Line y = x', 2,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Real axis', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Conjugate of z is reflected across the', 'Real axis', 'Origin', 'Imaginary axis', 'Line y = x', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Real axis', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On an Argand diagram, the y-axis represents', 'Imaginary numbers', 'Conjugates', 'Arguments', 'Real numbers', 0,
'lc_hl_complex', 7, 'proficient', 'lc_hl', 'Argand diagram property: Imaginary numbers', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 3 - 4i', '7', '4', '5', '6', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(3^2 + -4^2) = sqrt(9 + 16) = sqrt(25) = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -8 + 15i', '23', '17', '16', '18', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-8^2 + 15^2) = sqrt(64 + 225) = sqrt(289) = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -8 - 15i', '23', '18', '16', '17', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-8^2 + -15^2) = sqrt(64 + 225) = sqrt(289) = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 6 + 8i', '10', '11', '14', '9', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 9 + 12i', '14', '21', '16', '15', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(9^2 + 12^2) = sqrt(81 + 144) = sqrt(225) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -9 + 12i', '16', '15', '21', '14', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-9^2 + 12^2) = sqrt(81 + 144) = sqrt(225) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 9 - 12i', '21', '15', '14', '16', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(9^2 + -12^2) = sqrt(81 + 144) = sqrt(225) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -8 + 15i', '17', '16', '18', '23', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-8^2 + 15^2) = sqrt(64 + 225) = sqrt(289) = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 8 + 15i', '16', '18', '17', '23', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(8^2 + 15^2) = sqrt(64 + 225) = sqrt(289) = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 5 - 12i', '13', '12', '17', '14', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(5^2 + -12^2) = sqrt(25 + 144) = sqrt(169) = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 9 + 12i', '14', '16', '21', '15', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(9^2 + 12^2) = sqrt(81 + 144) = sqrt(225) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 5 - 12i', '17', '13', '12', '14', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(5^2 + -12^2) = sqrt(25 + 144) = sqrt(169) = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -8 - 15i', '23', '17', '18', '16', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-8^2 + -15^2) = sqrt(64 + 225) = sqrt(289) = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 9 + 12i', '21', '16', '14', '15', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(9^2 + 12^2) = sqrt(81 + 144) = sqrt(225) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -3 + 4i', '7', '5', '4', '6', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -9 + 12i', '14', '15', '16', '21', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-9^2 + 12^2) = sqrt(81 + 144) = sqrt(225) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 5 - 12i', '14', '17', '12', '13', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(5^2 + -12^2) = sqrt(25 + 144) = sqrt(169) = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 3 - 4i', '5', '4', '6', '7', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(3^2 + -4^2) = sqrt(9 + 16) = sqrt(25) = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = 8 + 15i', '16', '18', '23', '17', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(8^2 + 15^2) = sqrt(64 + 225) = sqrt(289) = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |z| where z = -6 - 8i', '9', '10', '14', '11', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', '|z| = sqrt(-6^2 + -8^2) = sqrt(36 + 64) = sqrt(100) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -4', 'pi/2', 'pi', '-pi/2', '0', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -4 lies on axis. arg(z) = pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -i', 'pi/2', '0', 'pi', '-pi/2', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -i lies on axis. arg(z) = -pi/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 3i', '0', 'pi', 'pi/2', '-pi/2', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 3i lies on axis. arg(z) = pi/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -4', 'pi', 'pi/2', '0', '-pi/2', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -4 lies on axis. arg(z) = pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -2i', 'pi', '-pi/2', '0', 'pi/2', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -2i lies on axis. arg(z) = -pi/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -i', '-pi/2', 'pi', 'pi/2', '0', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -i lies on axis. arg(z) = -pi/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 2', 'pi/2', 'pi', '-pi/2', '0', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 2 lies on axis. arg(z) = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -4', '-pi/2', 'pi/2', 'pi', '0', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -4 lies on axis. arg(z) = pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -1', 'pi', '-pi/2', '0', 'pi/2', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -1 lies on axis. arg(z) = pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -2i', '-pi/2', 'pi/2', 'pi', '0', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -2i lies on axis. arg(z) = -pi/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 2', 'pi', 'pi/2', '-pi/2', '0', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 2 lies on axis. arg(z) = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 1', '0', 'pi', 'pi/2', '-pi/2', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 1 lies on axis. arg(z) = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -i', '-pi/2', 'pi/2', 'pi', '0', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -i lies on axis. arg(z) = -pi/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -4', 'pi/2', 'pi', '0', '-pi/2', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -4 lies on axis. arg(z) = pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -i', '0', 'pi', '-pi/2', 'pi/2', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -i lies on axis. arg(z) = -pi/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 2 + 2i', '-3pi/4', '-pi/4', 'pi/4', '3pi/4', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 2 + 2i: tan(theta) = 2/2. arg(z) = pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -3 + 3i', '-pi/4', '3pi/4', 'pi/4', '-3pi/4', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -3 + 3i: tan(theta) = 3/-3. arg(z) = 3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 1 - i', '-pi/4', 'pi/4', '-3pi/4', '3pi/4', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 1 - i: tan(theta) = -1/1. arg(z) = -pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -1 - i', 'pi/4', '3pi/4', '-3pi/4', '-pi/4', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -1 - i: tan(theta) = -1/-1. arg(z) = -3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -1 - i', '3pi/4', 'pi/4', '-3pi/4', '-pi/4', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -1 - i: tan(theta) = -1/-1. arg(z) = -3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 1 + i', '3pi/4', '-pi/4', 'pi/4', '-3pi/4', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 1 + i: tan(theta) = 1/1. arg(z) = pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 1 - i', 'pi/4', '-3pi/4', '3pi/4', '-pi/4', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 1 - i: tan(theta) = -1/1. arg(z) = -pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 2 + 2i', '3pi/4', 'pi/4', '-pi/4', '-3pi/4', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 2 + 2i: tan(theta) = 2/2. arg(z) = pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 1 - i', '-pi/4', 'pi/4', '-3pi/4', '3pi/4', 0,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 1 - i: tan(theta) = -1/1. arg(z) = -pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -1 - i', '3pi/4', '-3pi/4', '-pi/4', 'pi/4', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -1 - i: tan(theta) = -1/-1. arg(z) = -3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 1 + i', '3pi/4', '-3pi/4', 'pi/4', '-pi/4', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 1 + i: tan(theta) = 1/1. arg(z) = pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = 1 + i', '-pi/4', 'pi/4', '-3pi/4', '3pi/4', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = 1 + i: tan(theta) = 1/1. arg(z) = pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -1 - i', '-pi/4', '-3pi/4', 'pi/4', '3pi/4', 1,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -1 - i: tan(theta) = -1/-1. arg(z) = -3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -1 + i', '-3pi/4', 'pi/4', '-pi/4', '3pi/4', 3,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -1 + i: tan(theta) = 1/-1. arg(z) = 3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find arg(z) where z = -1 - i', 'pi/4', '3pi/4', '-3pi/4', '-pi/4', 2,
'lc_hl_complex', 8, 'proficient', 'lc_hl', 'z = -1 - i: tan(theta) = -1/-1. arg(z) = -3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', '3(cos(pi/2) - isin(pi/2))', '3(sin(pi/2) + icos(pi/2))', '3(cos(pi/2) + isin(pi/2))', 'cos(pi/2) + isin(pi/2)', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 1 in polar form', 'cos(0) + isin(0)', '1(sin(0) + icos(0))', '1(cos(0) - isin(0))', '1(cos(0) + isin(0))', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 1 has r = 1, theta = 0. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 2 in polar form', 'cos(0) + isin(0)', '2(sin(0) + icos(0))', '2(cos(0) - isin(0))', '2(cos(0) + isin(0))', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 2 has r = 2, theta = 0. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 2 in polar form', '2(sin(0) + icos(0))', 'cos(0) + isin(0)', '2(cos(0) - isin(0))', '2(cos(0) + isin(0))', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 2 has r = 2, theta = 0. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 1 + i in polar form', 'cos(pi/4) + isin(pi/4)', 'sqrt(2)(sin(pi/4) + icos(pi/4))', 'sqrt(2)(cos(pi/4) - isin(pi/4))', 'sqrt(2)(cos(pi/4) + isin(pi/4))', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 1 + i has r = sqrt(2), theta = pi/4. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', 'cos(pi/2) + isin(pi/2)', '3(cos(pi/2) + isin(pi/2))', '3(sin(pi/2) + icos(pi/2))', '3(cos(pi/2) - isin(pi/2))', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = -1 in polar form', '1(cos(pi) - isin(pi))', '1(cos(pi) + isin(pi))', '1(sin(pi) + icos(pi))', 'cos(pi) + isin(pi)', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = -1 has r = 1, theta = pi. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', 'cos(pi/2) + isin(pi/2)', '3(cos(pi/2) + isin(pi/2))', '3(sin(pi/2) + icos(pi/2))', '3(cos(pi/2) - isin(pi/2))', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 1 + i in polar form', 'sqrt(2)(cos(pi/4) - isin(pi/4))', 'sqrt(2)(cos(pi/4) + isin(pi/4))', 'sqrt(2)(sin(pi/4) + icos(pi/4))', 'cos(pi/4) + isin(pi/4)', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 1 + i has r = sqrt(2), theta = pi/4. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', 'cos(pi/2) + isin(pi/2)', '3(cos(pi/2) - isin(pi/2))', '3(cos(pi/2) + isin(pi/2))', '3(sin(pi/2) + icos(pi/2))', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = i in polar form', '1(cos(pi/2) - isin(pi/2))', 'cos(pi/2) + isin(pi/2)', '1(cos(pi/2) + isin(pi/2))', '1(sin(pi/2) + icos(pi/2))', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = i has r = 1, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 1 in polar form', '1(cos(0) - isin(0))', '1(cos(0) + isin(0))', '1(sin(0) + icos(0))', 'cos(0) + isin(0)', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 1 has r = 1, theta = 0. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', '3(sin(pi/2) + icos(pi/2))', '3(cos(pi/2) - isin(pi/2))', '3(cos(pi/2) + isin(pi/2))', 'cos(pi/2) + isin(pi/2)', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', '3(sin(pi/2) + icos(pi/2))', '3(cos(pi/2) - isin(pi/2))', '3(cos(pi/2) + isin(pi/2))', 'cos(pi/2) + isin(pi/2)', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', '3(cos(pi/2) + isin(pi/2))', 'cos(pi/2) + isin(pi/2)', '3(sin(pi/2) + icos(pi/2))', '3(cos(pi/2) - isin(pi/2))', 0,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 1 in polar form', '1(cos(0) - isin(0))', '1(cos(0) + isin(0))', 'cos(0) + isin(0)', '1(sin(0) + icos(0))', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 1 has r = 1, theta = 0. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 3i in polar form', 'cos(pi/2) + isin(pi/2)', '3(cos(pi/2) + isin(pi/2))', '3(cos(pi/2) - isin(pi/2))', '3(sin(pi/2) + icos(pi/2))', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 3i has r = 3, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = i in polar form', '1(sin(pi/2) + icos(pi/2))', 'cos(pi/2) + isin(pi/2)', '1(cos(pi/2) - isin(pi/2))', '1(cos(pi/2) + isin(pi/2))', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = i has r = 1, theta = pi/2. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 1 in polar form', 'cos(0) + isin(0)', '1(cos(0) + isin(0))', '1(sin(0) + icos(0))', '1(cos(0) - isin(0))', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 1 has r = 1, theta = 0. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write z = 1 + i in polar form', 'sqrt(2)(cos(pi/4) + isin(pi/4))', 'cos(pi/4) + isin(pi/4)', 'sqrt(2)(cos(pi/4) - isin(pi/4))', 'sqrt(2)(sin(pi/4) + icos(pi/4))', 0,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'z = 1 + i has r = sqrt(2), theta = pi/4. Polar form: r(cos(theta) + isin(theta))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 4(cos(pi) + isin(pi))', '4', '-4', '4i', 'Option 4', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '4(cos(pi) + isin(pi)) = 4cos(pi) + 4isin(pi) = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 3(cos(pi/2) + isin(pi/2))', '3', '3i', 'Option 4', 'Option 3', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '3(cos(pi/2) + isin(pi/2)) = 3cos(pi/2) + 3isin(pi/2) = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 3(cos(pi/2) + isin(pi/2))', 'Option 3', '3i', '3', 'Option 4', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '3(cos(pi/2) + isin(pi/2)) = 3cos(pi/2) + 3isin(pi/2) = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 2(cos(-pi/2) + isin(-pi/2))', '2', '-2i', 'Option 4', '2i', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '2(cos(-pi/2) + isin(-pi/2)) = 2cos(-pi/2) + 2isin(-pi/2) = -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 4(cos(pi) + isin(pi))', '4', 'Option 4', '4i', '-4', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '4(cos(pi) + isin(pi)) = 4cos(pi) + 4isin(pi) = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 2(cos(0) + isin(0))', '2', '2i', 'Option 4', 'Option 3', 0,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '2(cos(0) + isin(0)) = 2cos(0) + 2isin(0) = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 2(cos(-pi/2) + isin(-pi/2))', '2i', 'Option 4', '2', '-2i', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '2(cos(-pi/2) + isin(-pi/2)) = 2cos(-pi/2) + 2isin(-pi/2) = -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 2(cos(0) + isin(0))', '2i', 'Option 3', '2', 'Option 4', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '2(cos(0) + isin(0)) = 2cos(0) + 2isin(0) = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 3(cos(pi/2) + isin(pi/2))', 'Option 4', 'Option 3', '3i', '3', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '3(cos(pi/2) + isin(pi/2)) = 3cos(pi/2) + 3isin(pi/2) = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 4(cos(pi) + isin(pi))', '4i', 'Option 4', '4', '-4', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '4(cos(pi) + isin(pi)) = 4cos(pi) + 4isin(pi) = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 2(cos(-pi/2) + isin(-pi/2))', '2i', '2', '-2i', 'Option 4', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '2(cos(-pi/2) + isin(-pi/2)) = 2cos(-pi/2) + 2isin(-pi/2) = -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 2(cos(0) + isin(0))', '2', 'Option 4', '2i', 'Option 3', 0,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '2(cos(0) + isin(0)) = 2cos(0) + 2isin(0) = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 2(cos(0) + isin(0))', 'Option 3', 'Option 4', '2i', '2', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '2(cos(0) + isin(0)) = 2cos(0) + 2isin(0) = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 3(cos(pi/2) + isin(pi/2))', '3', 'Option 4', 'Option 3', '3i', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '3(cos(pi/2) + isin(pi/2)) = 3cos(pi/2) + 3isin(pi/2) = 3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert to rectangular form: 4(cos(pi) + isin(pi))', '-4', '4', '4i', 'Option 4', 0,
'lc_hl_complex', 9, 'proficient', 'lc_hl', '4(cos(pi) + isin(pi)) = 4cos(pi) + 4isin(pi) = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 3, find r for z1 x z2', 'r = 3', 'r = 12', 'r = 4', 'r = 7', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 3 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 2, find r for z1 x z2', 'r = 6', 'r = 8', 'r = 2', 'r = 4', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 2 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 3 and z2 has r = 3, find r for z1 x z2', 'r = 9', 'Option 4', 'r = 6', 'r = 3', 0,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 3 x 3 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 2, find r for z1 x z2', 'r = 4', 'r = 2', 'r = 6', 'r = 8', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 2 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 3, find r for z1 x z2', 'r = 12', 'r = 7', 'r = 4', 'r = 3', 0,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 3 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 3 and z2 has r = 2, find r for z1 x z2', 'r = 3', 'r = 5', 'r = 6', 'r = 2', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 3 x 2 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 3 and z2 has r = 3, find r for z1 x z2', 'r = 6', 'Option 4', 'r = 9', 'r = 3', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 3 x 3 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 2 and z2 has r = 3, find r for z1 x z2', 'r = 2', 'r = 3', 'r = 6', 'r = 5', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 2 x 3 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 3 and z2 has r = 2, find r for z1 x z2', 'r = 2', 'r = 5', 'r = 3', 'r = 6', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 3 x 2 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 3 and z2 has r = 3, find r for z1 x z2', 'r = 6', 'r = 9', 'r = 3', 'Option 4', 1,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 3 x 3 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 2, find r for z1 x z2', 'r = 4', 'r = 2', 'r = 6', 'r = 8', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 2 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 2, find r for z1 x z2', 'r = 4', 'r = 2', 'r = 8', 'r = 6', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 2 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 2, find r for z1 x z2', 'r = 2', 'r = 4', 'r = 8', 'r = 6', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 2 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 4 and z2 has r = 2, find r for z1 x z2', 'r = 4', 'r = 6', 'r = 2', 'r = 8', 3,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 4 x 2 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z1 has r = 2 and z2 has r = 2, find r for z1 x z2', 'Option 3', 'r = 2', 'r = 4', 'Option 4', 2,
'lc_hl_complex', 9, 'proficient', 'lc_hl', 'When multiplying, moduli multiply: r = 2 x 2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [2(cos(3pi/4) + isin(3pi/4))]^4', '16(cos(12pi/4) + isin(12pi/4))', '16(cos(4pi/4) + isin(4pi/4))', '8(cos(12pi/4) + isin(12pi/4))', '16(cos(3pi/4) + isin(3pi/4))', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 16, 4 x 3pi/4 = 12pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [2(cos(1pi/4) + isin(1pi/4))]^2', '4(cos(2pi/4) + isin(2pi/4))', '4(cos(1pi/4) + isin(1pi/4))', 'Option 4', 'Option 3', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^2 = 4, 2 x 1pi/4 = 2pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [2(cos(1pi/6) + isin(1pi/6))]^4', '16(cos(1pi/6) + isin(1pi/6))', '16(cos(4pi/6) + isin(4pi/6))', 'Option 4', '8(cos(4pi/6) + isin(4pi/6))', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 16, 4 x 1pi/6 = 4pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [3(cos(2pi/6) + isin(2pi/6))]^3', '27(cos(2pi/6) + isin(2pi/6))', '9(cos(6pi/6) + isin(6pi/6))', '27(cos(3pi/6) + isin(3pi/6))', '27(cos(6pi/6) + isin(6pi/6))', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 27, 3 x 2pi/6 = 6pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [2(cos(3pi/4) + isin(3pi/4))]^3', '8(cos(3pi/4) + isin(3pi/4))', 'Option 4', '8(cos(9pi/4) + isin(9pi/4))', '6(cos(9pi/4) + isin(9pi/4))', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 8, 3 x 3pi/4 = 9pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(1pi/4) + isin(1pi/4))]^4', '1(cos(1pi/4) + isin(1pi/4))', 'Option 4', '1(cos(4pi/4) + isin(4pi/4))', '4(cos(4pi/4) + isin(4pi/4))', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 1, 4 x 1pi/4 = 4pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(2pi/6) + isin(2pi/6))]^4', '1(cos(2pi/6) + isin(2pi/6))', '1(cos(4pi/6) + isin(4pi/6))', '4(cos(8pi/6) + isin(8pi/6))', '1(cos(8pi/6) + isin(8pi/6))', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 1, 4 x 2pi/6 = 8pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(2pi/6) + isin(2pi/6))]^3', '3(cos(6pi/6) + isin(6pi/6))', '1(cos(2pi/6) + isin(2pi/6))', '1(cos(3pi/6) + isin(3pi/6))', '1(cos(6pi/6) + isin(6pi/6))', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 1, 3 x 2pi/6 = 6pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [2(cos(3pi/6) + isin(3pi/6))]^2', '4(cos(6pi/6) + isin(6pi/6))', '4(cos(2pi/6) + isin(2pi/6))', 'Option 4', '4(cos(3pi/6) + isin(3pi/6))', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^2 = 4, 2 x 3pi/6 = 6pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(3pi/6) + isin(3pi/6))]^3', '3(cos(9pi/6) + isin(9pi/6))', '1(cos(3pi/6) + isin(3pi/6))', '1(cos(9pi/6) + isin(9pi/6))', 'Option 4', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 1, 3 x 3pi/6 = 9pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [3(cos(2pi/4) + isin(2pi/4))]^2', '6(cos(4pi/4) + isin(4pi/4))', 'Option 4', '9(cos(4pi/4) + isin(4pi/4))', '9(cos(2pi/4) + isin(2pi/4))', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^2 = 9, 2 x 2pi/4 = 4pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(2pi/4) + isin(2pi/4))]^3', '1(cos(2pi/4) + isin(2pi/4))', '1(cos(3pi/4) + isin(3pi/4))', '1(cos(6pi/4) + isin(6pi/4))', '3(cos(6pi/4) + isin(6pi/4))', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 1, 3 x 2pi/4 = 6pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [2(cos(3pi/6) + isin(3pi/6))]^3', '8(cos(9pi/6) + isin(9pi/6))', '6(cos(9pi/6) + isin(9pi/6))', 'Option 4', '8(cos(3pi/6) + isin(3pi/6))', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 8, 3 x 3pi/6 = 9pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [3(cos(1pi/6) + isin(1pi/6))]^3', '27(cos(3pi/6) + isin(3pi/6))', 'Option 4', '27(cos(1pi/6) + isin(1pi/6))', '9(cos(3pi/6) + isin(3pi/6))', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 27, 3 x 1pi/6 = 3pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(2pi/4) + isin(2pi/4))]^3', '1(cos(6pi/4) + isin(6pi/4))', '1(cos(3pi/4) + isin(3pi/4))', '1(cos(2pi/4) + isin(2pi/4))', '3(cos(6pi/4) + isin(6pi/4))', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 1, 3 x 2pi/4 = 6pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [2(cos(3pi/6) + isin(3pi/6))]^4', '16(cos(12pi/6) + isin(12pi/6))', '16(cos(4pi/6) + isin(4pi/6))', '16(cos(3pi/6) + isin(3pi/6))', '8(cos(12pi/6) + isin(12pi/6))', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 16, 4 x 3pi/6 = 12pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [3(cos(2pi/4) + isin(2pi/4))]^4', '12(cos(8pi/4) + isin(8pi/4))', '81(cos(8pi/4) + isin(8pi/4))', '81(cos(4pi/4) + isin(4pi/4))', '81(cos(2pi/4) + isin(2pi/4))', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 81, 4 x 2pi/4 = 8pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(1pi/4) + isin(1pi/4))]^3', 'Option 4', '1(cos(3pi/4) + isin(3pi/4))', '3(cos(3pi/4) + isin(3pi/4))', '1(cos(1pi/4) + isin(1pi/4))', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^3 = 1, 3 x 1pi/4 = 3pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(2pi/6) + isin(2pi/6))]^4', '1(cos(2pi/6) + isin(2pi/6))', '1(cos(4pi/6) + isin(4pi/6))', '1(cos(8pi/6) + isin(8pi/6))', '4(cos(8pi/6) + isin(8pi/6))', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 1, 4 x 2pi/6 = 8pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use De Moivre: [1(cos(3pi/6) + isin(3pi/6))]^4', '4(cos(12pi/6) + isin(12pi/6))', '1(cos(12pi/6) + isin(12pi/6))', '1(cos(4pi/6) + isin(4pi/6))', '1(cos(3pi/6) + isin(3pi/6))', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^4 = 1, 4 x 3pi/6 = 12pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/2) + isin(pi/2))^2', '1', '-i', '-1', 'i', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/2) + isin(pi/2))^2 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/4) + isin(pi/4))^4', '-i', '-1', '1', 'i', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/4) + isin(pi/4))^4 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/3) + isin(pi/3))^3', 'i', '1', '-i', '-1', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/3) + isin(pi/3))^3 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/4) + isin(pi/4))^8', '-1', 'i', '1', '-i', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/4) + isin(pi/4))^8 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/3) + isin(pi/3))^3', '1', 'i', '-i', '-1', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/3) + isin(pi/3))^3 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/6) + isin(pi/6))^6', '-1', 'i', '-i', '1', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/6) + isin(pi/6))^6 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/3) + isin(pi/3))^3', '1', '-1', '-i', 'i', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/3) + isin(pi/3))^3 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/3) + isin(pi/3))^3', '1', '-i', 'i', '-1', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/3) + isin(pi/3))^3 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/4) + isin(pi/4))^4', '1', '-1', 'i', '-i', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/4) + isin(pi/4))^4 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/2) + isin(pi/2))^2', 'i', '-1', '-i', '1', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/2) + isin(pi/2))^2 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/2) + isin(pi/2))^2', 'i', '1', '-i', '-1', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/2) + isin(pi/2))^2 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/6) + isin(pi/6))^6', '-1', '1', 'i', '-i', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/6) + isin(pi/6))^6 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/4) + isin(pi/4))^8', '-i', '-1', 'i', '1', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/4) + isin(pi/4))^8 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/4) + isin(pi/4))^4', '-1', '-i', '1', 'i', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/4) + isin(pi/4))^4 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (cos(pi/4) + isin(pi/4))^8', 'i', '1', '-1', '-i', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', '(cos(pi/4) + isin(pi/4))^8 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', '|z|/n', '|z|^n', '|z| + n', 'n|z|', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('De Moivre: (cos(t) + isin(t))^n = ', 'cos(t)^n + isin(t)^n', 'ncos(t) + nisin(t)', 'cos(n) + isin(n)', 'cos(nt) + isin(nt)', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: cos(nt) + isin(nt)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('De Moivre: (cos(t) + isin(t))^n = ', 'cos(t)^n + isin(t)^n', 'ncos(t) + nisin(t)', 'cos(nt) + isin(nt)', 'cos(n) + isin(n)', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: cos(nt) + isin(nt)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', '|z|^n', '|z|/n', '|z| + n', 'n|z|', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the argument of z^n is', 'n x arg(z)', 'arg(z^n)', 'arg(z) + n', 'arg(z)/n', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: n x arg(z)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('De Moivre: (cos(t) + isin(t))^n = ', 'cos(t)^n + isin(t)^n', 'cos(n) + isin(n)', 'cos(nt) + isin(nt)', 'ncos(t) + nisin(t)', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: cos(nt) + isin(nt)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('De Moivre: (cos(t) + isin(t))^n = ', 'ncos(t) + nisin(t)', 'cos(nt) + isin(nt)', 'cos(n) + isin(n)', 'cos(t)^n + isin(t)^n', 1,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: cos(nt) + isin(nt)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', '|z|^n', '|z| + n', '|z|/n', 'n|z|', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', '|z|^n', 'n|z|', '|z| + n', '|z|/n', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the argument of z^n is', 'arg(z)/n', 'arg(z^n)', 'arg(z) + n', 'n x arg(z)', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: n x arg(z)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', '|z| + n', 'n|z|', '|z|/n', '|z|^n', 3,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', '|z|^n', '|z|/n', 'n|z|', '|z| + n', 0,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the argument of z^n is', 'arg(z^n)', 'arg(z) + n', 'n x arg(z)', 'arg(z)/n', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: n x arg(z)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', 'n|z|', '|z|/n', '|z|^n', '|z| + n', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using De Moivre, the modulus of z^n is', '|z|/n', 'n|z|', '|z|^n', '|z| + n', 2,
'lc_hl_complex', 10, 'advanced', 'lc_hl', 'De Moivre''s Theorem: |z|^n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 4th roots does a non-zero complex number have?', '5', '8', '4', '3', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 5th roots does a non-zero complex number have?', '6', '10', '5', '4', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 2th roots does a non-zero complex number have?', '3', '2', '1', '4', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 5th roots does a non-zero complex number have?', '6', '4', '10', '5', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 5th roots does a non-zero complex number have?', '10', '4', '5', '6', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 5th roots does a non-zero complex number have?', '5', '10', '4', '6', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 4th roots does a non-zero complex number have?', '8', '3', '5', '4', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 5th roots does a non-zero complex number have?', '4', '6', '5', '10', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 2th roots does a non-zero complex number have?', '3', '2', '4', '1', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 6th roots does a non-zero complex number have?', '6', '7', '12', '5', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 4th roots does a non-zero complex number have?', '3', '5', '4', '8', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 6th roots does a non-zero complex number have?', '6', '12', '7', '5', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 4th roots does a non-zero complex number have?', '4', '8', '5', '3', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 5th roots does a non-zero complex number have?', '6', '10', '5', '4', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many distinct 4th roots does a non-zero complex number have?', '8', '4', '3', '5', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Every non-zero complex number has exactly n distinct nth roots. n = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '4', '3', '2', '1', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -4 have in C?', '4', '3', '1', '2', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-4) has 2 solutions: 2i and -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '4', '3', '2', '1', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '3', '1', '4', '2', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '4', '1', '3', '2', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -4 have in C?', '3', '4', '1', '2', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-4) has 2 solutions: 2i and -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '1', '4', '2', '3', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '1', '2', '3', '4', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -1 have in C?', '4', '1', '2', '3', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-1) has 2 solutions: i and -i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -4 have in C?', '3', '4', '1', '2', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-4) has 2 solutions: 2i and -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '2', '4', '1', '3', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '1', '4', '3', '2', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -9 have in C?', '2', '3', '4', '1', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-9) has 2 solutions: 3i and -3i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -4 have in C?', '1', '4', '2', '3', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-4) has 2 solutions: 2i and -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many square roots does -4 have in C?', '3', '2', '4', '1', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'sqrt(-4) has 2 solutions: 2i and -2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The angle between consecutive 3th roots of unity is', 'pi/6', '2pi', '2pi/3', 'pi/3', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 2pi/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The 6th roots of unity are equally spaced on a circle of radius', '1/6', 'n', '1', '6', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The angle between consecutive 6th roots of unity is', '2pi/6', 'pi/6', 'pi/12', '2pi', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 2pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The 6th roots of unity are equally spaced on a circle of radius', 'n', '6', '1', '1/6', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The angle between consecutive 5th roots of unity is', 'pi/5', 'pi/10', '2pi/5', '2pi', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 2pi/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The angle between consecutive 6th roots of unity is', '2pi', '2pi/6', 'pi/12', 'pi/6', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 2pi/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sum of all 4th roots of unity equals', '0', '-1', '1', '4', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The 3th roots of unity are equally spaced on a circle of radius', '1/3', 'n', '3', '1', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The angle between consecutive 4th roots of unity is', 'pi/8', 'pi/4', '2pi/4', '2pi', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 2pi/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sum of all 4th roots of unity equals', '-1', '4', '1', '0', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The angle between consecutive 3th roots of unity is', '2pi', '2pi/3', 'pi/6', 'pi/3', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 2pi/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sum of all 6th roots of unity equals', '1', '0', '-1', '6', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The 5th roots of unity are equally spaced on a circle of radius', '1', '1/5', '5', 'n', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sum of all 6th roots of unity equals', '1', '0', '6', '-1', 1,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sum of all 6th roots of unity equals', '-1', '6', '0', '1', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The 4th roots of unity are equally spaced on a circle of radius', '4', '1/4', 'n', '1', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The angle between consecutive 5th roots of unity is', '2pi/5', 'pi/10', 'pi/5', '2pi', 0,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 2pi/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The 4th roots of unity are equally spaced on a circle of radius', '4', 'n', '1', '1/4', 2,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sum of all 6th roots of unity equals', '6', '-1', '1', '0', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The 6th roots of unity are equally spaced on a circle of radius', '6', '1/6', 'n', '1', 3,
'lc_hl_complex', 11, 'advanced', 'lc_hl', 'Roots of unity property: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is Re((2+3i)(1-i))?', '5', '2', '3', '-1', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('arg(-1) equals', 'pi/2', 'pi', '0', '-pi', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('arg(-1) equals', 'pi/2', '0', '-pi', 'pi', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('|z1 x z2| equals', '|z1|/|z2|', '|z1| x |z2|', '|z1| + |z2|', '|z1| - |z2|', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: |z1| x |z2|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('arg(z1 x z2) equals', 'arg(z1) - arg(z2)', 'arg(z1)/arg(z2)', 'arg(z1) + arg(z2)', 'arg(z1) x arg(z2)', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: arg(z1) + arg(z2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z* = 3 - 4i, find z', '-3 + 4i', '-3 - 4i', '3 + 4i', '3 - 4i', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z* = 3 - 4i, find z', '-3 - 4i', '3 - 4i', '3 + 4i', '-3 + 4i', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^42', '1', '-1', 'i', '-i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (2 + i)(2 - i)', '3', '4 + i', '5', '4', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z* = 3 - 4i, find z', '-3 + 4i', '3 - 4i', '-3 - 4i', '3 + 4i', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + i)^4', '-4', '4i', '-4i', '4', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 4i in polar form', '4(cos(pi) + isin(pi))', '4i', '4(cos(0) + isin(0))', '4(cos(pi/2) + isin(pi/2))', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 4(cos(pi/2) + isin(pi/2))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is Re((2+3i)(1-i))?', '-1', '2', '3', '5', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 1 + i, find z^2', '2 + 2i', '2', '1 + 2i', '2i', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('arg(z1 x z2) equals', 'arg(z1) x arg(z2)', 'arg(z1) - arg(z2)', 'arg(z1)/arg(z2)', 'arg(z1) + arg(z2)', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: arg(z1) + arg(z2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z* = 3 - 4i, find z', '3 - 4i', '-3 - 4i', '3 + 4i', '-3 + 4i', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The cube roots of 1 are', '1, i, -i', '1, omega, omega^2', '1, -1, i', '1, 2, 3', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1, omega, omega^2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('|z1 x z2| equals', '|z1| + |z2|', '|z1| x |z2|', '|z1|/|z2|', '|z1| - |z2|', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: |z1| x |z2|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The cube roots of 1 are', '1, 2, 3', '1, -1, i', '1, i, -i', '1, omega, omega^2', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1, omega, omega^2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^42', '-1', 'i', '1', '-i', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + i)^4', '-4i', '4i', '-4', '4', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 1 + i, find z^2', '1 + 2i', '2 + 2i', '2', '2i', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is Re((2+3i)(1-i))?', '5', '3', '2', '-1', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('|z1 x z2| equals', '|z1| - |z2|', '|z1|/|z2|', '|z1| x |z2|', '|z1| + |z2|', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: |z1| x |z2|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is Re((2+3i)(1-i))?', '3', '-1', '5', '2', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = cos(pi/3) + isin(pi/3), find z^6', 'i', '1', '-i', '-1', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of 5 - 2i is', '5 - 2i', '-5 + 2i', '5 + 2i', '-5 - 2i', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find |3 + 4i|', '7', '5', '1', '25', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of 5 - 2i is', '-5 - 2i', '5 + 2i', '-5 + 2i', '5 - 2i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 5 + 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 4i in polar form', '4(cos(pi/2) + isin(pi/2))', '4i', '4(cos(pi) + isin(pi))', '4(cos(0) + isin(0))', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 4(cos(pi/2) + isin(pi/2))', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^42', 'i', '-1', '1', '-i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If |z| = 3 and arg(z) = pi/4, find |z^2|', '3', '27', '6', '9', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate (1 + i)^4', '4', '-4i', '-4', '4i', 2,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 1 + i, find z^2', '2i', '1 + 2i', '2 + 2i', '2', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = cos(pi/3) + isin(pi/3), find z^6', '1', '-i', 'i', '-1', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If |z| = 3 and arg(z) = pi/4, find |z^2|', '9', '3', '6', '27', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The cube roots of 1 are', '1, omega, omega^2', '1, -1, i', '1, 2, 3', '1, i, -i', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1, omega, omega^2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z* = 3 - 4i, find z', '-3 + 4i', '3 + 4i', '3 - 4i', '-3 - 4i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('|z1 x z2| equals', '|z1| - |z2|', '|z1| x |z2|', '|z1| + |z2|', '|z1|/|z2|', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: |z1| x |z2|', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If |z| = 3 and arg(z) = pi/4, find |z^2|', '6', '3', '27', '9', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z* = 3 - 4i, find z', '3 - 4i', '3 + 4i', '-3 - 4i', '-3 + 4i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 3 + 4i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = cos(pi/3) + isin(pi/3), find z^6', '1', '-i', '-1', 'i', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If |z| = 3 and arg(z) = pi/4, find |z^2|', '27', '6', '3', '9', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify i^42', '-i', '-1', '1', 'i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('arg(-1) equals', '0', 'pi', 'pi/2', '-pi', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: pi', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 1 + i, find z^2', '1 + 2i', '2i', '2', '2 + 2i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 2i', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('arg(z1 x z2) equals', 'arg(z1) - arg(z2)', 'arg(z1) + arg(z2)', 'arg(z1)/arg(z2)', 'arg(z1) x arg(z2)', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: arg(z1) + arg(z2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The cube roots of 1 are', '1, i, -i', '1, 2, 3', '1, -1, i', '1, omega, omega^2', 3,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1, omega, omega^2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = cos(pi/3) + isin(pi/3), find z^6', '1', '-i', 'i', '-1', 0,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If z = 1 + i, find z^2', '2 + 2i', '2i', '2', '1 + 2i', 1,
'lc_hl_complex', 12, 'advanced', 'lc_hl', 'Apply complex number techniques. Answer: 2i', 1);