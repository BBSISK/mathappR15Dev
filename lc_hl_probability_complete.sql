-- LC Higher Level - Probability - Complete SQL
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_probability_complete.sql
-- Generated: 2025-12-15

-- Add Probability topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_probability', 'Probability', id, '🎲', 9, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_probability';

-- Questions (600 total, 50 per level x 12 levels)

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting number less than 3?', '1/2', '1/3', '2/3', '1/6', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 2 favourable outcomes out of 6 possible outcomes. P = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting odd number?', 'None of these', '2/3', '1/6', '1/2', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 3 favourable outcomes out of 6 possible outcomes. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting prime number?', '1/6', '1/2', '2/3', 'None of these', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 3 favourable outcomes out of 6 possible outcomes. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting a number greater than 2?', '1/3', '5/6', '1/6', '2/3', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 4 favourable outcomes out of 6 possible outcomes. P = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting odd number?', '1/2', '1/6', '2/3', 'None of these', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 3 favourable outcomes out of 6 possible outcomes. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting prime number?', '2/3', '1/6', '1/2', 'None of these', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 3 favourable outcomes out of 6 possible outcomes. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting odd number?', '1/2', '1/6', 'None of these', '2/3', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 3 favourable outcomes out of 6 possible outcomes. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting number greater than 4?', '1/2', '1/3', '2/3', '1/6', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 2 favourable outcomes out of 6 possible outcomes. P = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting odd number?', '1/2', 'None of these', '1/6', '2/3', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 3 favourable outcomes out of 6 possible outcomes. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair six-sided die is rolled once. What is the probability of getting prime number?', '1/6', '1/2', '2/3', 'None of these', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 3 favourable outcomes out of 6 possible outcomes. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing a king?', '2/13', '1/13', '12/13', '2/27', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 4 favourable outcomes out of 52 cards. P = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing an ace?', '1/13', '2/27', '12/13', '2/13', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 4 favourable outcomes out of 52 cards. P = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing an ace?', '2/13', '12/13', '1/13', '2/27', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 4 favourable outcomes out of 52 cards. P = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing a black card?', '13/27', 'None of these', '15/26', '1/2', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 26 favourable outcomes out of 52 cards. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing a spade?', '1/4', '17/52', '13/54', '3/4', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 13 favourable outcomes out of 52 cards. P = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing a heart?', '1/4', '13/54', '3/4', '17/52', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 13 favourable outcomes out of 52 cards. P = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing a spade?', '1/4', '13/54', '17/52', '3/4', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 13 favourable outcomes out of 52 cards. P = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing a black card?', 'None of these', '1/2', '15/26', '13/27', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 26 favourable outcomes out of 52 cards. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing an ace?', '12/13', '2/27', '2/13', '1/13', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 4 favourable outcomes out of 52 cards. P = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random from a standard 52-card deck. What is the probability of drawing a spade?', '3/4', '1/4', '17/52', '13/54', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'There are 13 favourable outcomes out of 52 cards. P = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 3 red, 5 blue, and 2 green balls. One ball is drawn at random. What is the probability it is red?', '3/11', '7/10', '3/10', '2/5', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 10. Number of red balls = 3. P = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 4 red, 6 blue, and 2 green balls. One ball is drawn at random. What is the probability it is blue?', 'None of these', '1/2', '7/12', '6/13', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 12. Number of blue balls = 6. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 5 red, 5 blue, and 1 green balls. One ball is drawn at random. What is the probability it is blue?', 'None of these', '6/11', '5/11', '5/12', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 11. Number of blue balls = 5. P = 5/11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 5 red, 2 blue, and 2 green balls. One ball is drawn at random. What is the probability it is blue?', '7/9', '2/9', '1/5', '1/3', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 9. Number of blue balls = 2. P = 2/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 6 red, 3 blue, and 1 green balls. One ball is drawn at random. What is the probability it is red?', '3/5', '6/11', '2/5', '7/10', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 10. Number of red balls = 6. P = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 3 red, 5 blue, and 1 green balls. One ball is drawn at random. What is the probability it is blue?', '2/3', '1/2', '4/9', '5/9', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 9. Number of blue balls = 5. P = 5/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 4 red, 5 blue, and 2 green balls. One ball is drawn at random. What is the probability it is red?', '1/3', '7/11', '4/11', '5/11', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 11. Number of red balls = 4. P = 4/11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 3 red, 2 blue, and 4 green balls. One ball is drawn at random. What is the probability it is blue?', '7/9', '2/9', '1/3', '1/5', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 9. Number of blue balls = 2. P = 2/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 6 red, 6 blue, and 2 green balls. One ball is drawn at random. What is the probability it is red?', '1/2', '3/7', '4/7', '2/5', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 14. Number of red balls = 6. P = 3/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag contains 6 red, 2 blue, and 2 green balls. One ball is drawn at random. What is the probability it is red?', '6/11', '2/5', '7/10', '3/5', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'Total balls = 10. Number of red balls = 6. P = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 8 equal sections. 6 sections are yellow. What is the probability of landing on yellow?', '2/3', '7/8', '1/4', '3/4', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on yellow) = 6/8 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 8 equal sections. 6 sections are yellow. What is the probability of landing on yellow?', '1/4', '2/3', '7/8', '3/4', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on yellow) = 6/8 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 8 equal sections. 2 sections are green. What is the probability of landing on green?', '2/9', '1/4', '3/4', '3/8', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on green) = 2/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 5 equal sections. 3 sections are red. What is the probability of landing on red?', '2/5', '4/5', '1/2', '3/5', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on red) = 3/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 7 equal sections. 1 sections are yellow. What is the probability of landing on yellow?', '1/8', '2/7', '1/7', '6/7', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on yellow) = 1/7 = 1/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 5 equal sections. 2 sections are blue. What is the probability of landing on blue?', '2/5', '3/5', '1/3', 'None of these', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on blue) = 2/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 5 equal sections. 2 sections are green. What is the probability of landing on green?', '3/5', 'None of these', '1/3', '2/5', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on green) = 2/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 7 equal sections. 6 sections are green. What is the probability of landing on green?', '1', '6/7', '3/4', '1/7', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on green) = 6/7 = 6/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 7 equal sections. 5 sections are yellow. What is the probability of landing on yellow?', '6/7', '5/8', '5/7', '2/7', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on yellow) = 5/7 = 5/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 10 equal sections. 5 sections are blue. What is the probability of landing on blue?', '5/11', '3/5', '1/2', 'None of these', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'P(landing on blue) = 5/10 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the probability of a certain event?', 'Cannot be determined', '1/2', '1', '0', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 1. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the probability of an impossible event?', 'Cannot be determined', '1/2', '1', '0', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 0. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 0.3, what is P(not A)?', '0.6', '0.3', '1.3', '0.7', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 0.7. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 1/4, what is P(not A)?', '1/2', '4/4', '3/4', '1/4', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 3/4. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 2/5, what is P(not A)?', '1/5', '2/5', '5/5', '3/5', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 3/5. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 0.45, what is P(not A)?', '1.45', '0.45', '0.55', '0.65', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 0.55. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 5/8, what is P(not A)?', '3/8', '5/8', '1/8', '8/8', 0,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 3/8. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of an event must be between which values?', '0 and 100', '-1 and 1', '1 and 2', '0 and 1', 3,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 0 and 1. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 0.6, what is P(A′)?', '1.6', '0.4', '0.5', '0.6', 1,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 0.4. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(B) = 7/10, what is P(B′)?', '1', '10/7', '3/10', '7/10', 2,
'lc_hl_probability', 1, 'foundation', 'lc_hl', 'The answer is 3/10. P(not A) = 1 - P(A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. How many outcomes are in the sample space?', '6', '3', '8', '4', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space: {HH, HT, TH, TT}. Total = 4 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. How many outcomes are in the sample space?', '3', '4', '6', '8', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space: {HH, HT, TH, TT}. Total = 4 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. How many outcomes are in the sample space?', '4', '8', '3', '6', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space: {HH, HT, TH, TT}. Total = 4 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. How many outcomes are in the sample space?', '6', '8', '4', '3', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space: {HH, HT, TH, TT}. Total = 4 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three coins are flipped. How many outcomes are in the sample space?', '16', '8', '10', '7', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space has 2³ = 8 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. How many outcomes are in the sample space?', '8', '6', '3', '4', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space: {HH, HT, TH, TT}. Total = 4 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Three coins are flipped. How many outcomes are in the sample space?', '10', '8', '16', '7', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space has 2³ = 8 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. How many outcomes are in the sample space?', '3', '4', '8', '6', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Sample space: {HH, HT, TH, TT}. Total = 4 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 5?', '6', '3', '5', '4', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 5. There are 4 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 5?', '6', '3', '4', '5', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 5. There are 4 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 2?', '3', '1', 'None of these', '2', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 2. There are 1 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 11?', '1', '4', '3', '2', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 11. There are 2 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 11?', '3', '1', '4', '2', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 11. There are 2 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 3?', '1', '2', '4', '3', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 3. There are 2 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 7?', '7', '6', '5', '8', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 7. There are 6 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many ways can the sum equal 2?', 'None of these', '1', '3', '2', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Count the pairs that sum to 2. There are 1 ways.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 8?', '5/12', 'None of these', '1/6', '5/36', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 8 = 5. P = 5/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 10?', '1/4', '1/6', '1/12', '1/9', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 10 = 3. P = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 4?', '1/6', '1/9', '1/12', '1/4', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 4 = 3. P = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 4?', '1/12', '1/4', '1/6', '1/9', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 4 = 3. P = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 7?', '1/2', '7/36', '1/6', 'None of these', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 7 = 6. P = 1/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 4?', '1/12', '1/6', '1/9', '1/4', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 4 = 3. P = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 9?', '1/3', '1/6', '5/36', '1/9', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 9 = 4. P = 1/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair dice are rolled. What is the probability the sum equals 5?', '1/6', '1/3', '1/9', '5/36', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Total outcomes = 36. Ways to get 5 = 4. P = 1/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 4 dishes and 3 meals, how many combinations are possible if repetition is allowed?', '68', '12', '60', '64', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 4^3 = 64 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 3 flavours and 3 meals, how many combinations are possible if repetition is allowed?', '24', '27', '30', '9', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 3^3 = 27 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 3 flavours and 3 items, how many combinations are possible if repetition is allowed?', '24', '27', '9', '30', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 3^3 = 27 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 5 colours and 2 meals, how many combinations are possible if repetition is allowed?', '10', '20', '25', '30', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 5^2 = 25 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 5 flavours and 2 meals, how many combinations are possible if repetition is allowed?', '20', '30', '10', '25', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 5^2 = 25 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 5 flavours and 2 items, how many combinations are possible if repetition is allowed?', '10', '30', '20', '25', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 5^2 = 25 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 3 shirts and 3 days, how many combinations are possible if repetition is allowed?', '27', '24', '9', '30', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 3^3 = 27 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 3 dishes and 2 meals, how many combinations are possible if repetition is allowed?', 'None of these', '6', '12', '9', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 3^2 = 9 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 4 shirts and 3 days, how many combinations are possible if repetition is allowed?', '68', '64', '60', '12', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 4^3 = 64 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If there are 5 dishes and 3 items, how many combinations are possible if repetition is allowed?', '15', '130', '120', '125', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'With repetition: 5^3 = 125 combinations', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 4 fair dice are rolled?', '1296', '648', '1302', '24', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^4 = 1296', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 4 fair dice are rolled?', '24', '1296', '648', '1302', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^4 = 1296', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 3 fair dice are rolled?', '216', '18', '108', '222', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^3 = 216', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 4 fair dice are rolled?', '648', '1302', '24', '1296', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^4 = 1296', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 2 fair dice are rolled?', '12', '36', '18', '42', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^2 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 2 fair dice are rolled?', '12', '18', '36', '42', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^2 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 2 fair dice are rolled?', '36', '12', '42', '18', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^2 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when 4 fair dice are rolled?', '1302', '1296', '24', '648', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Each die has 6 outcomes. Total = 6^4 = 1296', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting at least one head?', '1/2', '3/4', '3/2', '1/4', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: HH, HT, TH. P = 3/4 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting at least one head?', '1/4', '3/2', '1/2', '3/4', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: HH, HT, TH. P = 3/4 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting at least one head?', '3/4', '1/2', '3/2', '1/4', 0,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: HH, HT, TH. P = 3/4 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting at most one head?', '3/2', '1/2', '1/4', '3/4', 3,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: HT, TH, TT. P = 3/4 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting exactly one head?', '1', 'None of these', '1/2', 'None of these', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: HT, TH. P = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting exactly one head?', 'None of these', '1/2', 'None of these', '1', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: HT, TH. P = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting no heads?', '1/2', '1/4', '3/4', 'None of these', 1,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: TT. P = 1/4 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. What is the probability of getting at least one head?', '1/4', '1/2', '3/4', '3/2', 2,
'lc_hl_probability', 2, 'foundation', 'lc_hl', 'Favourable outcomes: HH, HT, TH. P = 3/4 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 2/10 and P(B) = 1/10, find P(A or B).', '2/5', '1/50', '1/5', '3/10', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 2/10 + 1/10 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 2/10 and P(B) = 4/10, find P(A or B).', '7/10', '2/25', '1/5', '3/5', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 2/10 + 4/10 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 2/10 and P(B) = 2/10, find P(A or B).', '1/25', '1/2', '1/5', '2/5', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 2/10 + 2/10 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 2/10 and P(B) = 2/10, find P(A or B).', '1/5', '2/5', '1/2', '1/25', 1,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 2/10 + 2/10 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 3/10 and P(B) = 2/10, find P(A or B).', '1/2', '3/10', '3/50', '3/5', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 3/10 + 2/10 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 4/10 and P(B) = 2/10, find P(A or B).', '2/5', '3/5', '2/25', '7/10', 1,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 4/10 + 2/10 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 4/10 and P(B) = 4/10, find P(A or B).', '9/10', '2/5', '4/5', '4/25', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 4/10 + 4/10 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 3/10 and P(B) = 1/10, find P(A or B).', '1/2', '3/100', '3/10', '2/5', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 3/10 + 1/10 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 4/10 and P(B) = 1/10, find P(A or B).', '3/5', '1/25', '1/2', '2/5', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 4/10 + 1/10 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are mutually exclusive. If P(A) = 2/10 and P(B) = 1/10, find P(A or B).', '1/5', '2/5', '1/50', '3/10', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For mutually exclusive events: P(A or B) = P(A) + P(B) = 2/10 + 1/10 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 2/5 and P(B) = 3/5, find P(A and B).', '6/25', '2/5', '1', '1/5', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 2/5 × 3/5 = 6/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 3/5 and P(B) = 1/4, find P(A and B).', '4/5', '3/25', '3/20', '3/5', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 3/5 × 1/4 = 3/20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 3/4 and P(B) = 2/4, find P(A and B).', '2/7', '3/4', '3/8', '5/4', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 3/4 × 2/4 = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 1/4 and P(B) = 2/4, find P(A and B).', '1/8', '3/4', '2/21', '1/4', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 1/4 × 2/4 = 1/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 2/4 and P(B) = 3/4, find P(A and B).', '3/8', '1/2', '2/7', '5/4', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 2/4 × 3/4 = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 3/5 and P(B) = 2/4, find P(A and B).', '6/25', '3/5', '1', '3/10', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 1/5 and P(B) = 1/4, find P(A and B).', '2/5', '1/5', '1/25', '1/20', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 1/5 × 1/4 = 1/20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 2/4 and P(B) = 2/5, find P(A and B).', '1/2', '1/5', '4/25', '1', 1,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 2/4 × 2/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 3/5 and P(B) = 1/4, find P(A and B).', '3/20', '3/5', '3/25', '4/5', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 3/5 × 1/4 = 3/20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Events A and B are independent. If P(A) = 2/4 and P(B) = 2/5, find P(A and B).', '1/5', '1', '4/25', '1/2', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'For independent events: P(A and B) = P(A) × P(B) = 2/4 × 2/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 5/10, P(B) = 5/10, and P(A and B) = 3/10, find P(A or B).', '13/10', '3/10', '7/10', '1', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 5/10 + 5/10 - 3/10 = 7/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 4/10, P(B) = 4/10, and P(A and B) = 3/10, find P(A or B).', '3/10', '11/10', '4/5', '1/2', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 4/10 + 4/10 - 3/10 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 4/10, P(B) = 5/10, and P(A and B) = 3/10, find P(A or B).', '3/10', '9/10', '3/5', '6/5', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 4/10 + 5/10 - 3/10 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 3/10, P(B) = 6/10, and P(A and B) = 1/10, find P(A or B).', '1', '1/10', '9/10', '4/5', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 3/10 + 6/10 - 1/10 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 4/10, P(B) = 6/10, and P(A and B) = 1/10, find P(A or B).', '9/10', '1', '11/10', '1/10', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 4/10 + 6/10 - 1/10 = 9/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 4/10, P(B) = 3/10, and P(A and B) = 1/10, find P(A or B).', '4/5', '3/5', '7/10', '1/10', 1,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 4/10 + 3/10 - 1/10 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 5/10, P(B) = 6/10, and P(A and B) = 2/10, find P(A or B).', '13/10', '11/10', '9/10', '1/5', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 5/10 + 6/10 - 2/10 = 9/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 4/10, P(B) = 6/10, and P(A and B) = 1/10, find P(A or B).', '11/10', '1', '9/10', '1/10', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 4/10 + 6/10 - 1/10 = 9/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 5/10, P(B) = 6/10, and P(A and B) = 2/10, find P(A or B).', '13/10', '1/5', '11/10', '9/10', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 5/10 + 6/10 - 2/10 = 9/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 6/10, P(B) = 5/10, and P(A and B) = 4/10, find P(A or B).', '7/10', '3/2', '11/10', '2/5', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A or B) = P(A) + P(B) - P(A and B) = 6/10 + 5/10 - 4/10 = 7/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 3/5, what is P(A′)?', '2/5', '1', '4/5', '3/5', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 3/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 2/5, what is P(A′)?', 'None of these', '3/5', '1', '2/5', 1,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 2/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 1/5, what is P(A′)?', '2/5', '1/5', '1', '4/5', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 1/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 1/5, what is P(A′)?', '4/5', '2/5', '1', '1/5', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 1/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 1/5, what is P(A′)?', '4/5', '2/5', '1/5', '1', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 1/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 1/5, what is P(A′)?', '2/5', '1', '4/5', '1/5', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 1/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 3/5, what is P(A′)?', '3/5', '4/5', '1', '2/5', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 3/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 1/5, what is P(A′)?', '1/5', '2/5', '1', '4/5', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 1/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 4/5, what is P(A′)?', '1', '1/5', 'None of these', '4/5', 1,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 4/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A) = 4/5, what is P(A′)?', '4/5', 'None of these', '1/5', '1', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', 'P(A′) = 1 - P(A) = 1 - 4/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a face card or a spade?', '11/27', '9/26', '1/2', '11/26', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '12 face + 13 spades - 3 spade faces = 22. P = 11/26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a face card or a spade?', '11/26', '11/27', '9/26', '1/2', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '12 face + 13 spades - 3 spade faces = 22. P = 11/26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a club or a king?', '3/13', '5/13', '8/27', '4/13', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '13 clubs + 4 kings - 1 king of clubs = 16. P = 4/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a red card or an ace?', '14/27', '8/13', '6/13', '7/13', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '26 red + 4 aces - 2 red aces = 28. P = 7/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a heart or a diamond?', '15/26', '13/27', '11/26', '1/2', 3,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '13 hearts + 13 diamonds = 26. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a face card or a spade?', '11/26', '11/27', '9/26', '1/2', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '12 face + 13 spades - 3 spade faces = 22. P = 11/26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a face card or a spade?', '11/27', '9/26', '11/26', '1/2', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '12 face + 13 spades - 3 spade faces = 22. P = 11/26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a face card or a spade?', '9/26', '1/2', '11/26', '11/27', 2,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '12 face + 13 spades - 3 spade faces = 22. P = 11/26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a face card or a spade?', '11/26', '11/27', '9/26', '1/2', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '12 face + 13 spades - 3 spade faces = 22. P = 11/26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn at random. What is the probability of drawing a king or a queen?', '2/13', '1/13', '3/13', '4/27', 0,
'lc_hl_probability', 3, 'foundation', 'lc_hl', '4 kings + 4 queens = 8. P = 2/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 3/10 and P(B) = 8/10, find P(A|B).', '3/8', '11/10', '8/3', '3/10', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (3/10) ÷ (8/10) = 3/8 = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 2/10 and P(B) = 6/10, find P(A|B).', '3', '1/3', '4/5', '1/5', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (2/10) ÷ (6/10) = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 2/10 and P(B) = 6/10, find P(A|B).', '1/3', '1/5', '4/5', '3', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (2/10) ÷ (6/10) = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 3/10 and P(B) = 8/10, find P(A|B).', '3/8', '8/3', '3/10', '11/10', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (3/10) ÷ (8/10) = 3/8 = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 2/10 and P(B) = 6/10, find P(A|B).', '1/5', '4/5', '3', '1/3', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (2/10) ÷ (6/10) = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 1/10 and P(B) = 5/10, find P(A|B).', '5', '1/10', '3/5', '1/5', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (1/10) ÷ (5/10) = 1/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 3/10 and P(B) = 5/10, find P(A|B).', '3/10', '5/3', '3/5', '4/5', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (3/10) ÷ (5/10) = 3/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 1/10 and P(B) = 7/10, find P(A|B).', '1/10', '4/5', '1/7', '7', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (1/10) ÷ (7/10) = 1/7 = 1/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 1/10 and P(B) = 8/10, find P(A|B).', '9/10', '1/10', '1/8', '8', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (1/10) ÷ (8/10) = 1/8 = 1/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A and B) = 3/10 and P(B) = 5/10, find P(A|B).', '3/10', '3/5', '4/5', '5/3', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A|B) = P(A and B) / P(B) = (3/10) ÷ (5/10) = 3/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 14 have A and B, 28 have A only, 27 have B only, 23 have neither. Given someone has B, what is P(A|B)?', '14/41', '1/3', '7/46', '27/41', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 41. Those with A and B = 14. P(A|B) = 14/41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 27 have A and B, 24 have A only, 23 have B only, 15 have neither. Given someone has B, what is P(A|B)?', '27/50', '9/17', '23/50', '27/89', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 50. Those with A and B = 27. P(A|B) = 27/50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 23 have A and B, 18 have A only, 20 have B only, 14 have neither. Given someone has B, what is P(A|B)?', '23/43', '20/43', '23/75', '23/41', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 43. Those with A and B = 23. P(A|B) = 23/43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 13 have A and B, 24 have A only, 28 have B only, 26 have neither. Given someone has B, what is P(A|B)?', '13/41', '1/7', '13/37', '28/41', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 41. Those with A and B = 13. P(A|B) = 13/41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 27 have A and B, 23 have A only, 22 have B only, 18 have neither. Given someone has B, what is P(A|B)?', '3/10', '22/49', '27/49', '27/50', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 49. Those with A and B = 27. P(A|B) = 27/49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 22 have A and B, 26 have A only, 22 have B only, 10 have neither. Given someone has B, what is P(A|B)?', '11/40', '1/2', 'None of these', '11/24', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 44. Those with A and B = 22. P(A|B) = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 13 have A and B, 23 have A only, 20 have B only, 16 have neither. Given someone has B, what is P(A|B)?', '13/72', '20/33', '13/33', '13/36', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 33. Those with A and B = 13. P(A|B) = 13/33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 28 have A and B, 21 have A only, 27 have B only, 28 have neither. Given someone has B, what is P(A|B)?', '27/55', '7/26', '28/55', '4/7', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 55. Those with A and B = 28. P(A|B) = 28/55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 29 have A and B, 13 have A only, 30 have B only, 25 have neither. Given someone has B, what is P(A|B)?', '29/59', '30/59', '29/97', '29/42', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 59. Those with A and B = 29. P(A|B) = 29/59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a group: 19 have A and B, 25 have A only, 15 have B only, 22 have neither. Given someone has B, what is P(A|B)?', '19/44', '19/81', '15/34', '19/34', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Total with B = 34. Those with A and B = 19. P(A|B) = 19/34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 27 study both Biology and Irish, 15 study only Biology, 27 study only Irish. Given a student studies Biology, what is the probability they also study Irish?', '27/50', 'None of these', '9/14', '27/100', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Biology = 42. Of these, 27 also study Irish. P = 9/14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 19 study both Biology and German, 21 study only Biology, 29 study only German. Given a student studies Biology, what is the probability they also study German?', '19/100', '19/40', '29/100', '12/25', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Biology = 40. Of these, 19 also study German. P = 19/40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 26 study both Physics and French, 15 study only Physics, 28 study only French. Given a student studies Physics, what is the probability they also study French?', '27/50', '13/50', '26/41', '7/25', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Physics = 41. Of these, 26 also study French. P = 26/41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 28 study both Maths and German, 18 study only Maths, 23 study only German. Given a student studies Maths, what is the probability they also study German?', '23/100', '51/100', '14/23', '7/25', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Maths = 46. Of these, 28 also study German. P = 14/23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 33 study both Physics and German, 18 study only Physics, 28 study only German. Given a student studies Physics, what is the probability they also study German?', '33/100', '61/100', '7/25', '11/17', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Physics = 51. Of these, 33 also study German. P = 11/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 33 study both Biology and French, 18 study only Biology, 25 study only French. Given a student studies Biology, what is the probability they also study French?', '1/4', '29/50', '11/17', '33/100', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Biology = 51. Of these, 33 also study French. P = 11/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 28 study both Biology and German, 20 study only Biology, 18 study only German. Given a student studies Biology, what is the probability they also study German?', '23/50', '7/12', '7/25', '9/50', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Biology = 48. Of these, 28 also study German. P = 7/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 33 study both Physics and Irish, 21 study only Physics, 28 study only Irish. Given a student studies Physics, what is the probability they also study Irish?', '7/25', '61/100', '33/100', '11/18', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Physics = 54. Of these, 33 also study Irish. P = 11/18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 26 study both Physics and German, 28 study only Physics, 23 study only German. Given a student studies Physics, what is the probability they also study German?', '49/100', '23/100', '13/27', '13/50', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Physics = 54. Of these, 26 also study German. P = 13/27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Of 100 students: 29 study both Biology and German, 19 study only Biology, 20 study only German. Given a student studies Biology, what is the probability they also study German?', '1/5', '29/100', '29/48', '49/100', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Students studying Biology = 48. Of these, 29 also study German. P = 29/48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is less than 5, what is the probability the number is odd?', '1/2', 'None of these', '1/3', '3/4', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is less than 5, sample space is [1, 2, 3, 4]. Favourable: [1, 3]. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is even, what is the probability the number is greater than 3?', '1', '2/3', '1/3', 'None of these', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is even, sample space is [2, 4, 6]. Favourable: [4, 6]. P = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is less than 5, what is the probability the number is odd?', 'None of these', '1/2', '3/4', '1/3', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is less than 5, sample space is [1, 2, 3, 4]. Favourable: [1, 3]. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is greater than 2, what is the probability the number is even?', '1/2', '1/3', 'None of these', '3/4', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is greater than 2, sample space is [3, 4, 5, 6]. Favourable: [4, 6]. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is even, what is the probability the number is greater than 3?', '2/3', '1/3', 'None of these', '1', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is even, sample space is [2, 4, 6]. Favourable: [4, 6]. P = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is less than 5, what is the probability the number is odd?', 'None of these', '1/2', '1/3', '3/4', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is less than 5, sample space is [1, 2, 3, 4]. Favourable: [1, 3]. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is even, what is the probability the number is greater than 3?', 'None of these', '1/3', '1', '2/3', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is even, sample space is [2, 4, 6]. Favourable: [4, 6]. P = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is odd, what is the probability the number is less than 4?', 'None of these', '1/3', '2/3', '1', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is odd, sample space is [1, 3, 5]. Favourable: [1, 3]. P = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is even, what is the probability the number is greater than 3?', 'None of these', '1/3', '1', '2/3', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is even, sample space is [2, 4, 6]. Favourable: [4, 6]. P = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. Given that the number is less than 5, what is the probability the number is odd?', '3/4', '1/2', 'None of these', '1/3', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'Given the number is less than 5, sample space is [1, 2, 3, 4]. Favourable: [1, 3]. P = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 3/5 and P(B) = 3/5, find P(A and B).', 'None of these', '6/5', '3/5', '9/25', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 3/5 × 3/5 = 9/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 4/5 and P(B) = 5/5, find P(A and B).', '9/5', '4/5', '1', 'None of these', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 4/5 × 5/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 4/5 and P(B) = 5/5, find P(A and B).', '4/5', '1', 'None of these', '9/5', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 4/5 × 5/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 4/5 and P(B) = 4/5, find P(A and B).', '4/5', '16/25', '8/5', 'None of these', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 4/5 × 4/5 = 16/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 3/5 and P(B) = 3/5, find P(A and B).', 'None of these', '3/5', '9/25', '6/5', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 3/5 × 3/5 = 9/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 2/5 and P(B) = 4/5, find P(A and B).', '2/5', '4/5', '6/5', '8/25', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 2/5 × 4/5 = 8/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 3/5 and P(B) = 5/5, find P(A and B).', '3/5', '1', '8/5', 'None of these', 0,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 3/5 × 5/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 1/5 and P(B) = 5/5, find P(A and B).', 'None of these', '1', '1/5', '6/5', 2,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 1/5 × 5/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 3/5 and P(B) = 4/5, find P(A and B).', '4/5', '12/25', '7/5', '3/5', 1,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 3/5 × 4/5 = 12/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(A|B) = 2/5 and P(B) = 5/5, find P(A and B).', '7/5', 'None of these', '1', '2/5', 3,
'lc_hl_probability', 4, 'developing', 'lc_hl', 'P(A and B) = P(A|B) × P(B) = 2/5 × 5/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 2/10, P(B) = 2/10, P(A and B) = 4/100. Are A and B independent?', 'They are mutually exclusive', 'Cannot determine', 'No, they are not independent', 'Yes, they are independent', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 2/10 × 2/10 = 4/100 = P(A and B). Independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 3/10, P(B) = 3/10, P(A and B) = 9/100. Are A and B independent?', 'Yes, they are independent', 'They are mutually exclusive', 'Cannot determine', 'No, they are not independent', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 3/10 × 3/10 = 9/100 = P(A and B). Independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 4/10, P(B) = 4/10, P(A and B) = 23/100. Are A and B independent?', 'Yes, they are independent', 'No, they are not independent', 'Cannot determine', 'They are mutually exclusive', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 16/100 ≠ 23/100 = P(A and B). Not independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 4/10, P(B) = 3/10, P(A and B) = 12/100. Are A and B independent?', 'No, they are not independent', 'Yes, they are independent', 'They are mutually exclusive', 'Cannot determine', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 4/10 × 3/10 = 12/100 = P(A and B). Independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 4/10, P(B) = 3/10, P(A and B) = 12/100. Are A and B independent?', 'Yes, they are independent', 'Cannot determine', 'They are mutually exclusive', 'No, they are not independent', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 4/10 × 3/10 = 12/100 = P(A and B). Independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 3/10, P(B) = 4/10, P(A and B) = 12/100. Are A and B independent?', 'Cannot determine', 'No, they are not independent', 'They are mutually exclusive', 'Yes, they are independent', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 3/10 × 4/10 = 12/100 = P(A and B). Independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 2/10, P(B) = 3/10, P(A and B) = 13/100. Are A and B independent?', 'Cannot determine', 'No, they are not independent', 'They are mutually exclusive', 'Yes, they are independent', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 6/100 ≠ 13/100 = P(A and B). Not independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 4/10, P(B) = 3/10, P(A and B) = 12/100. Are A and B independent?', 'They are mutually exclusive', 'Cannot determine', 'No, they are not independent', 'Yes, they are independent', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 4/10 × 3/10 = 12/100 = P(A and B). Independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 3/10, P(B) = 3/10, P(A and B) = 22/100. Are A and B independent?', 'They are mutually exclusive', 'No, they are not independent', 'Cannot determine', 'Yes, they are independent', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 9/100 ≠ 22/100 = P(A and B). Not independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(A) = 3/10, P(B) = 4/10, P(A and B) = 26/100. Are A and B independent?', 'Cannot determine', 'Yes, they are independent', 'They are mutually exclusive', 'No, they are not independent', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(A) × P(B) = 12/100 ≠ 26/100 = P(A and B). Not independent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.4 and 0.5. What is the probability both occur?', '0.9', '0.7', '0.4', '0.2', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.4 × 0.5 = 0.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.3 and 0.3. What is the probability both occur?', '0.51', '0.09', '0.6', '0.3', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.3 × 0.3 = 0.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.8 and 0.8. What is the probability both occur?', '1.6', '0.8', '0.64', '0.96', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.8 × 0.8 = 0.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.3 and 0.7. What is the probability both occur?', '0.21', '1.0', '0.3', '0.79', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.3 × 0.7 = 0.21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.7 and 0.6. What is the probability both occur?', '0.7', '1.3', '0.42', '0.88', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.7 × 0.6 = 0.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.7 and 0.8. What is the probability both occur?', '0.56', '0.7', '0.94', '1.5', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.7 × 0.8 = 0.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.6 and 0.3. What is the probability both occur?', '0.18', '0.6', '0.72', '0.9', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.6 × 0.3 = 0.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.8 and 0.6. What is the probability both occur?', '0.92', '1.4', '0.48', '0.8', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.8 × 0.6 = 0.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.5 and 0.6. What is the probability both occur?', '0.3', '0.5', '0.8', '1.1', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.5 × 0.6 = 0.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.4 and 0.5. What is the probability both occur?', '0.9', '0.4', '0.2', '0.7', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(both) = 0.4 × 0.5 = 0.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.3 and 0.5. What is the probability at least one occurs?', '0.35', '0.8', '0.15', '0.65', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.7 × 0.5 = 1 - 0.35 = 0.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.3 and 0.4. What is the probability at least one occurs?', '0.7', '0.42', '0.58', '0.12', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.7 × 0.6 = 1 - 0.42 = 0.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.3 and 0.5. What is the probability at least one occurs?', '0.65', '0.15', '0.35', '0.8', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.7 × 0.5 = 1 - 0.35 = 0.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.4 and 0.5. What is the probability at least one occurs?', '0.9', '0.2', '0.7', '0.3', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.6 × 0.5 = 1 - 0.3 = 0.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.4 and 0.2. What is the probability at least one occurs?', '0.48', '0.52', '0.6', '0.08', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.6 × 0.8 = 1 - 0.48 = 0.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.3 and 0.5. What is the probability at least one occurs?', '0.35', '0.8', '0.15', '0.65', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.7 × 0.5 = 1 - 0.35 = 0.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.4 and 0.3. What is the probability at least one occurs?', '0.58', '0.7', '0.42', '0.12', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.6 × 0.7 = 1 - 0.42 = 0.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.5 and 0.3. What is the probability at least one occurs?', '0.8', '0.15', '0.65', '0.35', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.5 × 0.7 = 1 - 0.35 = 0.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.4 and 0.3. What is the probability at least one occurs?', '0.7', '0.12', '0.58', '0.42', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.6 × 0.7 = 1 - 0.42 = 0.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events have probabilities 0.2 and 0.3. What is the probability at least one occurs?', '0.06', '0.56', '0.44', '0.5', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(at least one) = 1 - P(neither) = 1 - 0.8 × 0.7 = 1 - 0.56 = 0.44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.7. If 2 independent trials are performed, what is the probability of success on all trials?', '1.4', '0.51', '0.7', '0.49', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.7^2 = 0.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.7. If 3 independent trials are performed, what is the probability of success on all trials?', '0.657', '2.1', '0.343', '0.7', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.7^3 = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.6. If 2 independent trials are performed, what is the probability of success on all trials?', '0.36', '0.6', '1.2', '0.64', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.6^2 = 0.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.5. If 3 independent trials are performed, what is the probability of success on all trials?', '0.125', '0.875', '1.5', '0.5', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.5^3 = 0.125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.5. If 2 independent trials are performed, what is the probability of success on all trials?', '0.25', '1.0', '0.5', '0.75', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.5^2 = 0.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.5. If 4 independent trials are performed, what is the probability of success on all trials?', '0.5', '0.0625', '0.9375', '2.0', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.5^4 = 0.0625', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.8. If 4 independent trials are performed, what is the probability of success on all trials?', '3.2', '0.5904', '0.8', '0.4096', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.8^4 = 0.4096', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.7. If 2 independent trials are performed, what is the probability of success on all trials?', '0.51', '0.7', '0.49', '1.4', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.7^2 = 0.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.8. If 2 independent trials are performed, what is the probability of success on all trials?', '0.64', '1.6', '0.36', '0.8', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.8^2 = 0.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of success on each trial is 0.5. If 4 independent trials are performed, what is the probability of success on all trials?', '0.0625', '2.0', '0.9375', '0.5', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(all succeed) = 0.5^4 = 0.0625', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.3. Assuming days are independent, what is the probability of no rain over 3 consecutive days?', '0.7', '0.343', '0.027', '0.9', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.7^3 = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.3. Assuming days are independent, what is the probability of no rain over 2 consecutive days?', '0.7', '0.6', '0.49', '0.09', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.7^2 = 0.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.3. Assuming days are independent, what is the probability of no rain over 2 consecutive days?', '0.6', '0.09', '0.7', '0.49', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.7^2 = 0.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.2. Assuming days are independent, what is the probability of no rain over 3 consecutive days?', '0.512', '0.8', '0.008', '0.6', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.8^3 = 0.512', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.4. Assuming days are independent, what is the probability of no rain over 2 consecutive days?', '0.8', '0.36', '0.16', '0.6', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.6^2 = 0.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.4. Assuming days are independent, what is the probability of no rain over 2 consecutive days?', '0.36', '0.16', '0.8', '0.6', 0,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.6^2 = 0.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.3. Assuming days are independent, what is the probability of no rain over 3 consecutive days?', '0.027', '0.9', '0.343', '0.7', 2,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.7^3 = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.3. Assuming days are independent, what is the probability of no rain over 3 consecutive days?', '0.9', '0.343', '0.7', '0.027', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.7^3 = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.4. Assuming days are independent, what is the probability of no rain over 3 consecutive days?', '0.064', '0.6', '1.2', '0.216', 3,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.6^3 = 0.216', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of rain on any day is 0.3. Assuming days are independent, what is the probability of no rain over 3 consecutive days?', '0.027', '0.343', '0.9', '0.7', 1,
'lc_hl_probability', 5, 'developing', 'lc_hl', 'P(no rain all days) = 0.7^3 = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 4 blue balls. Two balls are drawn with replacement. What is P(two blue balls)?', '4/9', '16/81', '25/81', '5/9', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 4/9 × 4/9 = 16/81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 4 red and 3 blue balls. Two balls are drawn with replacement. What is P(two red balls)?', '3/7', '16/49', '23/49', '4/7', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 4/7 × 4/7 = 16/49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Two balls are drawn with replacement. What is P(one of each colour)?', '3/5', '2/5', '12/25', '17/25', 2,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 2/5 × 3/5 = 12/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 3 blue balls. Two balls are drawn with replacement. What is P(one of each colour)?', '15/32', '5/8', '3/8', '19/32', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 5/8 × 3/8 = 15/32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 2 blue balls. Two balls are drawn with replacement. What is P(one of each colour)?', '17/25', '2/5', '12/25', '3/5', 2,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 3/5 × 2/5 = 12/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 4 red and 5 blue balls. Two balls are drawn with replacement. What is P(two red balls)?', '4/9', '25/81', '5/9', '16/81', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 4/9 × 4/9 = 16/81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Two balls are drawn with replacement. What is P(one of each colour)?', '2/5', '3/5', '12/25', '17/25', 2,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 2/5 × 3/5 = 12/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 3 blue balls. Two balls are drawn with replacement. What is P(two blue balls)?', '3/8', '5/8', '17/64', '9/64', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 3/8 × 3/8 = 9/64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 5 blue balls. Two balls are drawn with replacement. What is P(two blue balls)?', '25/64', '33/64', '5/8', '3/8', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 5/8 × 5/8 = 25/64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 2 blue balls. Two balls are drawn with replacement. What is P(one of each colour)?', '1/2', 'None of these', '3/4', 'None of these', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 2/4 × 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 6 blue balls. Two balls are drawn without replacement. What is P(two blue balls)?', '1/4', '5/12', '1/3', '10/27', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 6/9 × 5/8 = 5/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 6 blue balls. Two balls are drawn without replacement. What is P(one of each colour)?', '4/9', '1/2', '1/4', '1/3', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 3/9 × 6/8 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 6 blue balls. Two balls are drawn without replacement. What is P(two blue balls)?', '5/11', '3/11', 'None of these', '30/121', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 6/11 × 5/10 = 3/11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 6 red and 4 blue balls. Two balls are drawn without replacement. What is P(two red balls)?', '1/3', '3/10', '3/5', '4/15', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 6/10 × 5/9 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 6 red and 5 blue balls. Two balls are drawn without replacement. What is P(two blue balls)?', '20/121', '2/11', '3/11', '6/11', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 5/11 × 4/10 = 2/11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 4 red and 3 blue balls. Two balls are drawn without replacement. What is P(one of each colour)?', '2/7', '24/49', 'None of these', '4/7', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 4/7 × 3/6 = 4/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 3 blue balls. Two balls are drawn without replacement. What is P(one of each colour)?', '15/32', '5/8', '15/56', '15/28', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 2 × 5/8 × 3/7 = 15/28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 5 blue balls. Two balls are drawn without replacement. What is P(two blue balls)?', '1/2', '1/5', '5/18', '2/9', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 5/10 × 4/9 = 2/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 6 red and 4 blue balls. Two balls are drawn without replacement. What is P(two blue balls)?', '4/15', '2/15', '3/25', '3/5', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 4/10 × 3/9 = 2/15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 6 blue balls. Two balls are drawn without replacement. What is P(two blue balls)?', '1/4', '10/27', '5/12', '1/3', 2,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P = 6/9 × 5/8 = 5/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.7 of passing Exam 1 and 0.6 of passing Exam 2 (independent). What is P(passing both)?', '0.7', '0.42', '1.3', '0.12', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.7 × 0.6 = 0.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.7 of passing Exam 1 and 0.6 of passing Exam 2 (independent). What is P(passing both)?', '0.12', '0.7', '1.3', '0.42', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.7 × 0.6 = 0.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.6 of passing Exam 1 and 0.5 of passing Exam 2 (independent). What is P(passing both)?', '1.1', '0.3', '0.2', '0.6', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.6 × 0.5 = 0.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.6 of passing Exam 1 and 0.5 of passing Exam 2 (independent). What is P(passing both)?', '0.3', '0.6', '0.2', '1.1', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.6 × 0.5 = 0.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.7 of passing Exam 1 and 0.5 of passing Exam 2 (independent). What is P(passing both)?', '0.15', '0.35', '1.2', '0.7', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.7 × 0.5 = 0.35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.6 of passing Exam 1 and 0.5 of passing Exam 2 (independent). What is P(passing both)?', '0.3', '0.6', '0.2', '1.1', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.6 × 0.5 = 0.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.8 of passing Exam 1 and 0.6 of passing Exam 2 (independent). What is P(passing both)?', '0.48', '1.4', '0.08', '0.8', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.8 × 0.6 = 0.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.8 of passing Exam 1 and 0.7 of passing Exam 2 (independent). What is P(passing both)?', '0.8', '0.56', '1.5', '0.06', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.8 × 0.7 = 0.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.8 of passing Exam 1 and 0.5 of passing Exam 2 (independent). What is P(passing both)?', '1.3', '0.4', '0.8', '0.1', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.8 × 0.5 = 0.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student has probability 0.6 of passing Exam 1 and 0.6 of passing Exam 2 (independent). What is P(passing both)?', '0.36', '1.2', '0.16', '0.6', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(both pass) = 0.6 × 0.6 = 0.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.6. What is P(at least one occurs)?', '0.36', '0.6', '0.16', '0.84', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.4² = 1 - 0.16 = 0.84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.5. What is P(at least one occurs)?', '0.25', '0.5', 'None of these', '0.75', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.5² = 1 - 0.25 = 0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.5. What is P(at least one occurs)?', '0.5', 'None of these', '0.25', '0.75', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.5² = 1 - 0.25 = 0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.5. What is P(at least one occurs)?', '0.5', '0.75', 'None of these', '0.25', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.5² = 1 - 0.25 = 0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.5. What is P(at least one occurs)?', 'None of these', '0.75', '0.25', '0.5', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.5² = 1 - 0.25 = 0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.4. What is P(at least one occurs)?', '0.64', '0.4', '0.36', '0.16', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.6² = 1 - 0.36 = 0.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.5. What is P(at least one occurs)?', '0.25', '0.75', '0.5', 'None of these', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.5² = 1 - 0.25 = 0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.3. What is P(at least one occurs)?', '0.49', '0.09', '0.3', '0.51', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.7² = 1 - 0.49 = 0.51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.3. What is P(at least one occurs)?', '0.09', '0.3', '0.49', '0.51', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.7² = 1 - 0.49 = 0.51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two independent events each have probability 0.5. What is P(at least one occurs)?', 'None of these', '0.25', '0.5', '0.75', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(at least one) = 1 - P(none) = 1 - 0.5² = 1 - 0.25 = 0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.8. If flipped 3 times, what is P(3 heads)?', '0.512', '0.488', '2.4', '0.64', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.8³ = 0.512', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.7. If flipped 3 times, what is P(3 heads)?', '0.343', '2.1', '0.49', '0.657', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.7³ = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.6. If flipped 3 times, what is P(3 heads)?', '0.784', '1.8', '0.36', '0.216', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.6³ = 0.216', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.6. If flipped 3 times, what is P(3 heads)?', '0.216', '0.36', '0.784', '1.8', 0,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.6³ = 0.216', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.8. If flipped 3 times, what is P(3 heads)?', '0.64', '0.512', '0.488', '2.4', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.8³ = 0.512', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.7. If flipped 3 times, what is P(3 heads)?', '0.657', '2.1', '0.49', '0.343', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.7³ = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.8. If flipped 3 times, what is P(3 heads)?', '0.64', '0.512', '0.488', '2.4', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.8³ = 0.512', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.8. If flipped 3 times, what is P(3 heads)?', '0.64', '0.512', '0.488', '2.4', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.8³ = 0.512', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.5. If flipped 3 times, what is P(3 heads)?', '1.5', '0.25', '0.875', '0.125', 3,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.5³ = 0.125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin lands heads with probability 0.8. If flipped 3 times, what is P(3 heads)?', '0.488', '0.512', '0.64', '2.4', 1,
'lc_hl_probability', 6, 'developing', 'lc_hl', 'P(3 heads) = 0.8³ = 0.512', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=1/10, P(X=2)=4/10, P(X=3)=1/10, P(X=4)=4/10', 'No, probabilities do not sum to 1', 'Cannot determine', 'Yes, it is valid', 'No, negative probability', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Valid since sum = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=4/10, P(X=2)=1/10, P(X=3)=4/10, P(X=4)=1/10', 'No, probabilities do not sum to 1', 'Cannot determine', 'No, negative probability', 'Yes, it is valid', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Valid since sum = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=4/10, P(X=2)=3/10, P(X=3)=2/10, P(X=4)=1/10', 'No, probabilities do not sum to 1', 'Cannot determine', 'No, negative probability', 'Yes, it is valid', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Valid since sum = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=4/10, P(X=2)=2/10, P(X=3)=1/10, P(X=4)=3/10', 'Yes, it is valid', 'No, probabilities do not sum to 1', 'No, negative probability', 'Cannot determine', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Valid since sum = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=3/10, P(X=2)=3/10, P(X=3)=4/10, P(X=4)=0/10', 'No, negative probability', 'Yes, it is valid', 'No, probabilities do not sum to 1', 'Cannot determine', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Valid since sum = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=2/10, P(X=2)=4/10, P(X=3)=2/10, P(X=4)=2/10', 'Yes, it is valid', 'No, probabilities do not sum to 1', 'Cannot determine', 'No, negative probability', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Invalid since sum ≠ 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=1/10, P(X=2)=4/10, P(X=3)=4/10, P(X=4)=1/10', 'No, probabilities do not sum to 1', 'Yes, it is valid', 'Cannot determine', 'No, negative probability', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Valid since sum = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=4/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=4/10', 'Cannot determine', 'No, negative probability', 'No, probabilities do not sum to 1', 'Yes, it is valid', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 13/10. Invalid since sum ≠ 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=3/10, P(X=2)=1/10, P(X=3)=3/10, P(X=4)=3/10', 'No, negative probability', 'No, probabilities do not sum to 1', 'Yes, it is valid', 'Cannot determine', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 10/10. Valid since sum = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a valid probability distribution? P(X=1)=3/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=4/10', 'No, negative probability', 'No, probabilities do not sum to 1', 'Yes, it is valid', 'Cannot determine', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum = 12/10. Invalid since sum ≠ 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=1/10, P(X=2)=3/10, P(X=3)=2/10, P(X=4)=k. Find k.', '2/5', '3/5', 'None of these', '1/10', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 1/10 + 3/10 + 2/10 + k = 1, so k = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=1/10, P(X=2)=3/10, P(X=3)=2/10, P(X=4)=k. Find k.', '1/10', 'None of these', '2/5', '3/5', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 1/10 + 3/10 + 2/10 + k = 1, so k = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=3/10, P(X=2)=3/10, P(X=3)=3/10, P(X=4)=k. Find k.', '3/5', '9/10', '1/10', '3/10', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 3/10 + 3/10 + 3/10 + k = 1, so k = 1/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=3/10, P(X=2)=2/10, P(X=3)=2/10, P(X=4)=k. Find k.', '7/10', 'None of these', '1/2', '3/10', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 3/10 + 2/10 + 2/10 + k = 1, so k = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=2/10, P(X=2)=1/10, P(X=3)=3/10, P(X=4)=k. Find k.', '3/5', '3/10', '2/5', '1/5', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 2/10 + 1/10 + 3/10 + k = 1, so k = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=3/10, P(X=2)=3/10, P(X=3)=1/10, P(X=4)=k. Find k.', 'None of these', '3/5', '3/10', '7/10', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 3/10 + 3/10 + 1/10 + k = 1, so k = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=1/10, P(X=2)=1/10, P(X=3)=3/10, P(X=4)=k. Find k.', '1/2', 'None of these', '1/5', '1/10', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 1/10 + 1/10 + 3/10 + k = 1, so k = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=3/10, P(X=2)=3/10, P(X=3)=1/10, P(X=4)=k. Find k.', '7/10', '3/5', 'None of these', '3/10', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 3/10 + 3/10 + 1/10 + k = 1, so k = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=1/10, P(X=2)=2/10, P(X=3)=2/10, P(X=4)=k. Find k.', '1/10', '3/10', 'None of these', '1/2', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 1/10 + 2/10 + 2/10 + k = 1, so k = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has distribution: P(X=1)=3/10, P(X=2)=1/10, P(X=3)=3/10, P(X=4)=k. Find k.', 'None of these', '2/5', '3/10', '7/10', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Sum must equal 1: 3/10 + 1/10 + 3/10 + k = 1, so k = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 2).', '3/10', '7/10', '2/5', '1/5', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 2) = sum of probabilities from 1 to 2 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 2).', '7/10', '3/10', '1/5', '2/5', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 2) = sum of probabilities from 1 to 2 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 2).', '2/5', '7/10', '3/10', '1/5', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 2) = sum of probabilities from 1 to 2 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 4).', '4/5', '9/10', '1/5', 'None of these', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 4) = sum of probabilities from 1 to 4 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 4).', '4/5', 'None of these', '9/10', '1/5', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 4) = sum of probabilities from 1 to 4 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 4).', '9/10', '1/5', '4/5', 'None of these', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 4) = sum of probabilities from 1 to 4 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 3).', '7/10', '3/10', '2/5', '3/5', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 3) = sum of probabilities from 1 to 3 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 1).', '1/10', '9/10', 'None of these', '1/5', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 1) = sum of probabilities from 1 to 1 = 1/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 3).', '3/5', '2/5', '7/10', '3/10', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 3) = sum of probabilities from 1 to 3 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ 1).', '1/10', '9/10', 'None of these', '1/5', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(X ≤ 1) = sum of probabilities from 1 to 1 = 1/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(1 ≤ X ≤ 5).', 'None of these', '1', '11/10', '1/10', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(1 ≤ X ≤ 5) = sum from X=1 to X=5 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(1 ≤ X ≤ 2).', '3/10', '2/5', '1/10', 'None of these', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(1 ≤ X ≤ 2) = sum from X=1 to X=2 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(1 ≤ X ≤ 4).', '4/5', 'None of these', '1/10', '9/10', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(1 ≤ X ≤ 4) = sum from X=1 to X=4 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(2 ≤ X ≤ 4).', '1/5', '7/10', 'None of these', '4/5', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(2 ≤ X ≤ 4) = sum from X=2 to X=4 = 7/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(3 ≤ X ≤ 4).', '4/5', '1/2', '3/10', '3/5', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(3 ≤ X ≤ 4) = sum from X=3 to X=4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(2 ≤ X ≤ 5).', '1/5', 'None of these', '1', '9/10', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(2 ≤ X ≤ 5) = sum from X=2 to X=5 = 9/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(3 ≤ X ≤ 5).', '7/10', '1', '3/10', '4/5', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(3 ≤ X ≤ 5) = sum from X=3 to X=5 = 7/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(1 ≤ X ≤ 4).', 'None of these', '9/10', '1/10', '4/5', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(1 ≤ X ≤ 4) = sum from X=1 to X=4 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(2 ≤ X ≤ 5).', '9/10', '1', '1/5', 'None of these', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(2 ≤ X ≤ 5) = sum from X=2 to X=5 = 9/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(1 ≤ X ≤ 4).', '9/10', '1/10', '4/5', 'None of these', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'P(1 ≤ X ≤ 4) = sum from X=1 to X=4 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 5}. Find P(3 ≤ X ≤ 4).', '1/5', '3/5', 'None of these', '2/5', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/5. P(3 ≤ X ≤ 4) = 2/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 7}. Find P(1 ≤ X ≤ 7).', '1', '1/7', 'None of these', '6/7', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/7. P(1 ≤ X ≤ 7) = 7/7 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 5}. Find P(3 ≤ X ≤ 4).', '1/5', '2/5', '3/5', 'None of these', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/5. P(3 ≤ X ≤ 4) = 2/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 5}. Find P(3 ≤ X ≤ 5).', '3/5', '1/5', '2/5', 'None of these', 0,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/5. P(3 ≤ X ≤ 5) = 3/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 6}. Find P(1 ≤ X ≤ 3).', '1/6', '1/2', '1/3', 'None of these', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/6. P(1 ≤ X ≤ 3) = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 5}. Find P(3 ≤ X ≤ 5).', '1/5', '3/5', '2/5', 'None of these', 1,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/5. P(3 ≤ X ≤ 5) = 3/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 4}. Find P(2 ≤ X ≤ 3).', 'None of these', 'None of these', '1/4', '1/2', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/4. P(2 ≤ X ≤ 3) = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 8}. Find P(6 ≤ X ≤ 8).', '1/8', '3/4', '1/4', '3/8', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/8. P(6 ≤ X ≤ 8) = 3/8 = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 7}. Find P(5 ≤ X ≤ 7).', '1/7', '2/7', '3/7', '5/7', 2,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/7. P(5 ≤ X ≤ 7) = 3/7 = 3/7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X is uniformly distributed on {1, 2, ..., 8}. Find P(2 ≤ X ≤ 6).', '1/4', '1/2', '1/8', '5/8', 3,
'lc_hl_probability', 7, 'proficient', 'lc_hl', 'Uniform: each outcome has probability 1/8. P(2 ≤ X ≤ 6) = 5/8 = 5/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=3/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10', '1.9', '2.9', '2.5', '2.4', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 2.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=2/10, P(X=2)=3/10, P(X=3)=2/10, P(X=4)=3/10', '3.1', '2.5', '2.6', '2.1', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 2.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=2/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=3/10', '2.2', '2.7', '3.2', '2.5', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 2.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=2/10, P(X=2)=3/10, P(X=3)=1/10, P(X=4)=4/10', '3.2', '2.5', '2.2', '2.7', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 2.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=3/10, P(X=2)=1/10, P(X=3)=1/10, P(X=4)=5/10', '2.5', '3.3', '2.8', '2.3', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 2.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=2/10, P(X=2)=1/10, P(X=3)=2/10, P(X=4)=5/10', 'None of these', '2.5', '3.0', '3.5', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=4/10', 'None of these', '3.5', '2.5', '3.0', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=1/10, P(X=2)=3/10, P(X=3)=1/10, P(X=4)=5/10', '3.0', 'None of these', '2.5', '3.5', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=3/10, P(X=2)=1/10, P(X=3)=3/10, P(X=4)=3/10', '2.6', '3.1', '2.1', '2.5', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 2.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find E(X) for: P(X=1)=3/10, P(X=2)=2/10, P(X=3)=1/10, P(X=4)=4/10', '2.5', '2.6', '2.1', '3.1', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = Σ(x × P(X=x)) = 2.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is squared, what is the expected value?', '3.5', '16.17', '15.17', '14.17', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 15.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is squared, what is the expected value?', '14.17', '16.17', '15.17', '3.5', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 15.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is increased by 3, what is the expected value?', '7.5', '6.5', '5.5', '3.5', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 6.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is increased by 3, what is the expected value?', '6.5', '3.5', '7.5', '5.5', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 6.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is increased by 3, what is the expected value?', '3.5', '6.5', '5.5', '7.5', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 6.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is squared, what is the expected value?', '14.17', '3.5', '15.17', '16.17', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 15.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is squared, what is the expected value?', '14.17', '3.5', '15.17', '16.17', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 15.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. If the score is squared, what is the expected value?', '14.17', '16.17', '15.17', '3.5', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 3.5 for fair die. After transformation: E = 15.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €35 with probability 1/4 and loses €9 otherwise. What is E(X)?', '2.0', '-2.0', '7.0', '26', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 35 × 1/4 - 9 × 3/4 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €22 with probability 1/3 and loses €10 otherwise. What is E(X)?', '12', '5.67', '0.67', '-0.67', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 22 × 1/3 - 10 × 2/3 = 0.67', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €38 with probability 1/4 and loses €15 otherwise. What is E(X)?', '-1.75', '1.75', '23', '3.25', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 38 × 1/4 - 15 × 3/4 = -1.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €45 with probability 2/5 and loses €10 otherwise. What is E(X)?', '12.0', '17.0', '35', '-12.0', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 45 × 2/5 - 10 × 3/5 = 12.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €26 with probability 1/4 and loses €17 otherwise. What is E(X)?', '-6.25', '9', '6.25', '-1.25', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 26 × 1/4 - 17 × 3/4 = -6.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €19 with probability 2/5 and loses €16 otherwise. What is E(X)?', '3', '-2.0', '2.0', '3.0', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 19 × 2/5 - 16 × 3/5 = -2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €48 with probability 1/3 and loses €14 otherwise. What is E(X)?', '6.67', '-6.67', '11.67', '34', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 48 × 1/3 - 14 × 2/3 = 6.67', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game pays €19 with probability 1/4 and loses €11 otherwise. What is E(X)?', '8', '3.5', '1.5', '-3.5', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(X) = 19 × 1/4 - 11 × 3/4 = -3.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 8, find E(3X +5).', '24', '16', '29', '13', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(3X +5) = 3×E(X) +5 = 3×8 +5 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 3, find E(3X +10).', '13', '19', '16', '9', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(3X +10) = 3×E(X) +10 = 3×3 +10 = 19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 6, find E(5X -5).', '25', '6', '1', '30', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(5X -5) = 5×E(X) -5 = 5×6 -5 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 3, find E(2X -3).', '3', '6', '2', '0', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(2X -3) = 2×E(X) -3 = 2×3 -3 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 4, find E(5X +10).', '19', '30', '14', '20', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(5X +10) = 5×E(X) +10 = 5×4 +10 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 7, find E(2X -1).', '6', '8', '14', '13', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(2X -1) = 2×E(X) -1 = 2×7 -1 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 5, find E(4X -3).', '6', '2', '17', '20', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(4X -3) = 4×E(X) -3 = 4×5 -3 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 6, find E(2X +1).', '7', '12', '9', '13', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'E(2X +1) = 2×E(X) +1 = 2×6 +1 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 6 and E(X²) = 42, find Var(X).', '12', '42', '36', '6', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 42 - 6² = 42 - 36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 4 and E(X²) = 22, find Var(X).', '22', '16', '6', '10', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 22 - 4² = 22 - 16 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 6 and E(X²) = 42, find Var(X).', '36', '6', '42', '12', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 42 - 6² = 42 - 36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 5 and E(X²) = 27, find Var(X).', '27', '7', '2', '25', 2,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 27 - 5² = 27 - 25 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 6 and E(X²) = 41, find Var(X).', '5', '36', '41', '11', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 41 - 6² = 41 - 36 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 5 and E(X²) = 28, find Var(X).', '25', '3', '28', '8', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 28 - 5² = 28 - 25 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 5 and E(X²) = 27, find Var(X).', '27', '7', '25', '2', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 27 - 5² = 27 - 25 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If E(X) = 7 and E(X²) = 51, find Var(X).', '49', '2', '9', '51', 1,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(X) = E(X²) - [E(X)]² = 51 - 7² = 51 - 49 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 10, find Var(3X + 1).', '90', '30', '11', '31', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(3X + 1) = 3² × 10 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 6, find Var(2X + 4).', '16', '12', '10', '24', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(2X + 4) = 2² × 6 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 9, find Var(3X + 9).', '18', '27', '36', '81', 3,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(3X + 9) = 3² × 9 = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 8, find Var(2X + 1).', '32', '16', '9', '17', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(2X + 1) = 2² × 8 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 6, find Var(3X + 2).', '54', '18', '8', '20', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(3X + 2) = 3² × 6 = 54', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 10, find Var(3X + 1).', '90', '11', '31', '30', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(3X + 1) = 3² × 10 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 7, find Var(4X + 7).', '112', '14', '28', '35', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(4X + 7) = 4² × 7 = 112', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Var(X) = 4, find Var(4X + 2).', '64', '6', '18', '16', 0,
'lc_hl_probability', 8, 'proficient', 'lc_hl', 'Var(aX + b) = a²Var(X). Var(4X + 2) = 4² × 4 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A biased die lands on 6 with probability 0.5. It is rolled 10 times. X = number of successes. Identify the binomial parameters.', 'n = 11, p = 0.5', 'None of these', 'n = 10, p = 0.5', 'n = 9, p = 0.5', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(10, 0.5). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin (P(H) = 0.3) is flipped 12 times. X = number of successes. Identify the binomial parameters.', 'n = 12, p = 0.3', 'n = 12, p = 0.7', 'n = 11, p = 0.3', 'n = 13, p = 0.3', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(12, 0.3). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin (P(H) = 0.3) is flipped 9 times. X = number of successes. Identify the binomial parameters.', 'n = 8, p = 0.3', 'n = 9, p = 0.7', 'n = 10, p = 0.3', 'n = 9, p = 0.3', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(9, 0.3). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin (P(H) = 0.4) is flipped 15 times. X = number of successes. Identify the binomial parameters.', 'n = 16, p = 0.4', 'n = 15, p = 0.6', 'n = 14, p = 0.4', 'n = 15, p = 0.4', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(15, 0.4). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A biased die lands on 6 with probability 0.5. It is rolled 9 times. X = number of successes. Identify the binomial parameters.', 'None of these', 'n = 8, p = 0.5', 'n = 10, p = 0.5', 'n = 9, p = 0.5', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(9, 0.5). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A biased die lands on 6 with probability 0.5. It is rolled 7 times. X = number of successes. Identify the binomial parameters.', 'n = 7, p = 0.5', 'None of these', 'n = 6, p = 0.5', 'n = 8, p = 0.5', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(7, 0.5). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Each trial has success probability 0.4. There are 7 independent trials. X = number of successes. Identify the binomial parameters.', 'n = 7, p = 0.4', 'n = 6, p = 0.4', 'n = 8, p = 0.4', 'n = 7, p = 0.6', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(7, 0.4). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A biased die lands on 6 with probability 0.2. It is rolled 14 times. X = number of successes. Identify the binomial parameters.', 'n = 15, p = 0.2', 'n = 14, p = 0.2', 'n = 13, p = 0.2', 'n = 14, p = 0.8', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'X ~ B(14, 0.2). n = number of trials, p = probability of success', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(5, 2/3). Calculate P(X = 1).', '0.0823', '0.0412', '0.0206', '0.9588', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 1) = C(5,1) × (2/3)^1 × (1/3)^4 = 0.0412', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(5, 1/4). Calculate P(X = 2).', '0.1318', '0.5273', '0.2637', '0.7363', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 2) = C(5,2) × (1/4)^2 × (3/4)^3 = 0.2637', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(3, 1/2). Calculate P(X = 2).', '0.375', '0.625', '0.1875', '0.75', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 2) = C(3,2) × (1/2)^2 × (1/2)^1 = 0.375', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(4, 2/3). Calculate P(X = 3).', '0.1975', '0.7901', '0.3951', '0.6049', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 3) = C(4,3) × (2/3)^3 × (1/3)^1 = 0.3951', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(3, 2/3). Calculate P(X = 1).', '0.7778', '0.2222', '0.4444', '0.1111', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 1) = C(3,1) × (2/3)^1 × (1/3)^2 = 0.2222', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(3, 1/2). Calculate P(X = 1).', '0.625', '0.375', '0.1875', '0.75', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 1) = C(3,1) × (1/2)^1 × (1/2)^2 = 0.375', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(3, 1/4). Calculate P(X = 1).', '0.2109', '0.4219', '0.5781', '0.8438', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 1) = C(3,1) × (1/4)^1 × (3/4)^2 = 0.4219', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(3, 1/4). Calculate P(X = 1).', '0.8438', '0.2109', '0.5781', '0.4219', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 1) = C(3,1) × (1/4)^1 × (3/4)^2 = 0.4219', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(5, 2/3). Calculate P(X = 2).', '0.0823', '0.3292', '0.1646', '0.8354', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 2) = C(5,2) × (2/3)^2 × (1/3)^3 = 0.1646', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(3, 1/3). Calculate P(X = 1).', '0.5556', '0.2222', '0.8889', '0.4444', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X = 1) = C(3,1) × (1/3)^1 × (2/3)^2 = 0.4444', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(40, 0.2). Find E(X).', '200.0', '40.2', '8.0', '32.0', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 40 × 0.2 = 8.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(24, 0.3). Find E(X).', '7.199999999999999', '80.0', '16.799999999999997', '24.3', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 24 × 0.3 = 7.199999999999999', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(13, 0.4). Find E(X).', '7.8', '5.2', '13.4', '32.5', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 13 × 0.4 = 5.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(31, 0.2). Find E(X).', '6.2', '24.8', '155.0', '31.2', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 31 × 0.2 = 6.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(43, 0.2). Find E(X).', '215.0', '34.4', '8.6', '43.2', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 43 × 0.2 = 8.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(30, 0.3). Find E(X).', '100.0', '21.0', '9.0', '30.3', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 30 × 0.3 = 9.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(29, 0.2). Find E(X).', '23.200000000000003', '5.800000000000001', '145.0', '29.2', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 29 × 0.2 = 5.800000000000001', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(19, 0.25). Find E(X).', '14.25', '4.75', '76.0', '19.25', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'E(X) = np = 19 × 0.25 = 4.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(19, 0.2). Find Var(X).', '3.8000000000000003', '15.200000000000001', '1.74', '3.0400000000000005', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 19 × 0.2 × 0.8 = 3.0400000000000005', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(13, 0.5). Find Var(X).', '3.25', '1.8', 'None of these', '6.5', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 13 × 0.5 × 0.5 = 3.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(27, 0.2). Find Var(X).', '5.4', '21.6', '4.32', '2.08', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 27 × 0.2 × 0.8 = 4.32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(36, 0.2). Find Var(X).', '28.8', '2.4', '5.760000000000001', '7.2', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 36 × 0.2 × 0.8 = 5.760000000000001', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(14, 0.5). Find Var(X).', 'None of these', '3.5', '1.87', '7.0', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 14 × 0.5 × 0.5 = 3.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(32, 0.2). Find Var(X).', '5.120000000000001', '2.26', '6.4', '25.6', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 32 × 0.2 × 0.8 = 5.120000000000001', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(34, 0.3). Find Var(X).', '2.67', '10.2', '7.139999999999999', '23.799999999999997', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 34 × 0.3 × 0.7 = 7.139999999999999', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(20, 0.5). Find Var(X).', 'None of these', '5.0', '10.0', '2.24', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'Var(X) = np(1-p) = 20 × 0.5 × 0.5 = 5.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.2). Find P(X ≥ 1).', '0.2621', '0.7379', '1.2', '0.2', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.8^6 = 1 - 0.2621 = 0.7379', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(4, 0.2). Find P(X ≥ 1).', '0.4096', '0.2', '0.5904', '0.8', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.8^4 = 1 - 0.4096 = 0.5904', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.1). Find P(X ≥ 1).', '0.4686', '0.6', '0.5314', '0.1', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.9^6 = 1 - 0.5314 = 0.4686', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.1). Find P(X ≥ 1).', '0.4686', '0.5314', '0.1', '0.6', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.9^6 = 1 - 0.5314 = 0.4686', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.2). Find P(X ≥ 1).', '0.2', '0.2621', '1.2', '0.7379', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.8^6 = 1 - 0.2621 = 0.7379', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(4, 0.3). Find P(X ≥ 1).', '0.3', '0.7599', '1.2', '0.2401', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.7^4 = 1 - 0.2401 = 0.7599', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.2). Find P(X ≥ 1).', '0.2621', '0.2', '0.7379', '1.2', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.8^6 = 1 - 0.2621 = 0.7379', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(3, 0.1). Find P(X ≥ 1).', '0.3', '0.271', '0.1', '0.729', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(X ≥ 1) = 1 - P(X = 0) = 1 - 0.9^3 = 1 - 0.729 = 0.271', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 4 times. What is the probability of getting all heads?', '2.0', '0.125', '0.0625', '0.9375', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^4 = 0.0625', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 5 times. What is the probability of getting all heads?', '0.9688', '2.5', '0.0625', '0.0312', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^5 = 0.0312', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 4 times. What is the probability of getting all heads?', '0.0625', '0.9375', '0.125', '2.0', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^4 = 0.0625', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 7 times. What is the probability of getting all heads?', '3.5', '0.9922', '0.0156', '0.0078', 3,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^7 = 0.0078', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 6 times. What is the probability of getting all heads?', '0.0312', '3.0', '0.0156', '0.9844', 2,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^6 = 0.0156', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 6 times. What is the probability of getting all heads?', '3.0', '0.0156', '0.9844', '0.0312', 1,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^6 = 0.0156', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 4 times. What is the probability of getting all heads?', '0.0625', '2.0', '0.9375', '0.125', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^4 = 0.0625', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped 6 times. What is the probability of getting all heads?', '0.0156', '3.0', '0.0312', '0.9844', 0,
'lc_hl_probability', 9, 'proficient', 'lc_hl', 'P(all heads) = 0.5^6 = 0.0156', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = -2 represent?', '2 standard deviation(s) below the mean', '2 standard deviation(s) above the mean', '-2 units from 0', 'At the mean', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = -2 means the value is 2 standard deviation(s) below the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = -1 represent?', '1 standard deviation(s) above the mean', '1 standard deviation(s) below the mean', '-1 units from 0', 'At the mean', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = -1 means the value is 1 standard deviation(s) below the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = -1 represent?', 'At the mean', '-1 units from 0', '1 standard deviation(s) above the mean', '1 standard deviation(s) below the mean', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = -1 means the value is 1 standard deviation(s) below the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = 1 represent?', '1 units from 0', '1 standard deviation(s) below the mean', '1 standard deviation(s) above the mean', 'At the mean', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = 1 means the value is 1 standard deviation(s) above the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = 1 represent?', 'At the mean', '1 standard deviation(s) below the mean', '1 units from 0', '1 standard deviation(s) above the mean', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = 1 means the value is 1 standard deviation(s) above the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = -2 represent?', '-2 units from 0', '2 standard deviation(s) below the mean', 'At the mean', '2 standard deviation(s) above the mean', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = -2 means the value is 2 standard deviation(s) below the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = 2 represent?', '2 standard deviation(s) above the mean', '2 standard deviation(s) below the mean', 'At the mean', '2 units from 0', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = 2 means the value is 2 standard deviation(s) above the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a standard normal distribution, what does z = 3 represent?', '3 standard deviation(s) below the mean', 'At the mean', '3 units from 0', '3 standard deviation(s) above the mean', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = 3 means the value is 3 standard deviation(s) above the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 10²). Find the z-score for x = 40.', '0', '1', '-2', '-1', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (40 - 50)/10 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(70, 15²). Find the z-score for x = 55.', '1', '-2', '-1', '0', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (55 - 70)/15 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(60, 10²). Find the z-score for x = 40.', '-2', '2', '-1', '-3', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (40 - 60)/10 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(80, 5²). Find the z-score for x = 85.', '2', '1', '0', '-1', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (85 - 80)/5 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 15²). Find the z-score for x = 65.', '0', '1', '-1', '2', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (65 - 50)/15 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(60, 15²). Find the z-score for x = 90.', '2', '-2', '3', '1', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (90 - 60)/15 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(70, 10²). Find the z-score for x = 80.', '-1', '2', '0', '1', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (80 - 70)/10 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(70, 15²). Find the z-score for x = 40.', '-2', '-1', '2', '-3', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (40 - 70)/15 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 5²). Find the z-score for x = 105.', '-1', '2', '0', '1', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (105 - 100)/5 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(60, 5²). Find the z-score for x = 50.', '-3', '-1', '2', '-2', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (x - μ)/σ = (50 - 60)/5 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies within 1 standard deviation of the mean?', '95%', '68%', '99.7%', '34%', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 68% of data lies within 1 standard deviation of the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies within 2 standard deviations of the mean?', '95%', '99.7%', '47.5%', '68%', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 95% of data lies within 2 standard deviations of the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies between the mean and +1σ?', '50%', '68%', '34%', '16%', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 34% of data lies between the mean and +1σ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies within 2 standard deviations of the mean?', '95%', '47.5%', '68%', '99.7%', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 95% of data lies within 2 standard deviations of the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies above the mean?', '84%', '50%', '34%', '68%', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 50% of data lies above the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies within 1 standard deviation of the mean?', '95%', '34%', '68%', '99.7%', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 68% of data lies within 1 standard deviation of the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies above the mean?', '68%', '34%', '50%', '84%', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 50% of data lies above the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies within 2 standard deviations of the mean?', '68%', '47.5%', '95%', '99.7%', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 95% of data lies within 2 standard deviations of the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies within 2 standard deviations of the mean?', '47.5%', '95%', '99.7%', '68%', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 95% of data lies within 2 standard deviations of the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a normal distribution, what percentage of data lies above the mean?', '84%', '50%', '34%', '68%', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'By the empirical rule, approximately 50% of data lies above the mean', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 115?', 'z = 1.0', 'z = 0.5', 'z = 2.0', 'z = -1.0', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (115 - 100)/15 = 1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 115?', 'z = 1.0', 'z = 0.5', 'z = -1.0', 'z = 2.0', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (115 - 100)/15 = 1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 70?', 'None of these', 'z = -2.0', 'z = 2.0', 'z = -1.0', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (70 - 100)/15 = -2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 70?', 'None of these', 'z = 2.0', 'z = -2.0', 'z = -1.0', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (70 - 100)/15 = -2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 130?', 'z = 2.0', 'z = -2.0', 'z = 1.0', 'z = 3.0', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (130 - 100)/15 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 85?', 'z = 0.0', 'z = -0.5', 'z = 1.0', 'z = -1.0', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (85 - 100)/15 = -1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 130?', 'z = 1.0', 'z = 2.0', 'z = 3.0', 'z = -2.0', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (130 - 100)/15 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 130?', 'z = 3.0', 'z = 2.0', 'z = -2.0', 'z = 1.0', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (130 - 100)/15 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 130?', 'z = 3.0', 'z = 1.0', 'z = -2.0', 'z = 2.0', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (130 - 100)/15 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IQ scores are N(100, 15²). What is the z-score for an IQ of 70?', 'z = 2.0', 'None of these', 'z = -1.0', 'z = -2.0', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'z = (70 - 100)/15 = -2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 5²). If z = -1, find x.', '40', '50', '45', '55', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 50 + (-1)(5) = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(60, 5²). If z = 2, find x.', '75', '70', '50', '65', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 60 + (2)(5) = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 5²). If z = 2, find x.', '115', '90', '110', '105', 2,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 100 + (2)(5) = 110', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 15²). If z = -1, find x.', '50', '35', '20', '65', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 50 + (-1)(15) = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(60, 10²). If z = 1, find x.', '60', '50', '80', '70', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 60 + (1)(10) = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 10²). If z = -1, find x.', '80', '90', '100', '110', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 100 + (-1)(10) = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(60, 15²). If z = 1, find x.', '90', '60', '45', '75', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 60 + (1)(15) = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). If z = 2, find x.', '70', '115', '145', '130', 3,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 100 + (2)(15) = 130', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 15²). If z = 2, find x.', '65', '80', '20', '95', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 50 + (2)(15) = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 10²). If z = -2, find x.', '120', '80', '70', '90', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 100 + (-2)(10) = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 15²). If z = 2, find x.', '80', '20', '65', '95', 0,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 50 + (2)(15) = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(60, 10²). If z = 2, find x.', '90', '80', '70', '40', 1,
'lc_hl_probability', 10, 'advanced', 'lc_hl', 'x = μ + zσ = 60 + (2)(10) = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < 2.0) ≈ 0.9772. What is P(Z > 2.0)?', '0.0228', '0.8272', '0.9772', '1.0772', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > 2.0) = 1 - P(Z < 2.0) = 1 - 0.9772 = 0.0228', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < 1.0) ≈ 0.8413. What is P(Z > 1.0)?', '0.6913', '0.1587', '0.8413', '0.9413', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > 1.0) = 1 - P(Z < 1.0) = 1 - 0.8413 = 0.1587', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < -1.5) ≈ 0.0668. What is P(Z > -1.5)?', '0.0668', '0.9332', '0.1668', '-0.0832', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > -1.5) = 1 - P(Z < -1.5) = 1 - 0.0668 = 0.9332', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < -1.0) ≈ 0.1587. What is P(Z > -1.0)?', '0.1587', '0.8413', '0.0087', '0.2587', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > -1.0) = 1 - P(Z < -1.0) = 1 - 0.1587 = 0.8413', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < -1.5) ≈ 0.0668. What is P(Z > -1.5)?', '0.1668', '0.0668', '-0.0832', '0.9332', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > -1.5) = 1 - P(Z < -1.5) = 1 - 0.0668 = 0.9332', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < 2.0) ≈ 0.9772. What is P(Z > 2.0)?', '0.9772', '0.0228', '0.8272', '1.0772', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > 2.0) = 1 - P(Z < 2.0) = 1 - 0.9772 = 0.0228', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < -1.0) ≈ 0.1587. What is P(Z > -1.0)?', '0.0087', '0.2587', '0.8413', '0.1587', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > -1.0) = 1 - P(Z < -1.0) = 1 - 0.1587 = 0.8413', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For Z ~ N(0,1), P(Z < -1.0) ≈ 0.1587. What is P(Z > -1.0)?', '0.2587', '0.8413', '0.1587', '0.0087', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'P(Z > -1.0) = 1 - P(Z < -1.0) = 1 - 0.1587 = 0.8413', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 160 cm.', '-0.5', 'None of these', '-1.0', '1.0', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (160 - 170)/10 = -1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 160 cm.', '1.0', 'None of these', '-1.0', '-0.5', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (160 - 170)/10 = -1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 160 cm.', 'None of these', '-1.0', '-0.5', '1.0', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (160 - 170)/10 = -1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 190 cm.', '-2.0', '2.0', '1.0', '2.5', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (190 - 170)/10 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 160 cm.', 'None of these', '1.0', '-1.0', '-0.5', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (160 - 170)/10 = -1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 160 cm.', '-0.5', 'None of these', '-1.0', '1.0', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (160 - 170)/10 = -1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 190 cm.', '2.5', '1.0', '2.0', '-2.0', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (190 - 170)/10 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Heights are normally distributed with μ = 170 cm and σ = 10 cm. Find the z-score for a height of 180 cm.', '-1.0', '1.5', '0.5', '1.0', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'z = (180 - 170)/10 = 1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 97.5th percentile corresponds to z = 2.0. What score is the 97.5th percentile?', '800', '500', '600', '700', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (2.0)(100) = 700', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 97.5th percentile corresponds to z = 2.0. What score is the 97.5th percentile?', '500', '800', '700', '600', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (2.0)(100) = 700', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 16th percentile corresponds to z = -1.0. What score is the 16th percentile?', '500', 'None of these', '400', '300', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (-1.0)(100) = 400', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 16th percentile corresponds to z = -1.0. What score is the 16th percentile?', 'None of these', '300', '500', '400', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (-1.0)(100) = 400', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 84th percentile corresponds to z = 1.0. What score is the 84th percentile?', '700', 'None of these', '500', '600', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (1.0)(100) = 600', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 84th percentile corresponds to z = 1.0. What score is the 84th percentile?', 'None of these', '500', '600', '700', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (1.0)(100) = 600', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 84th percentile corresponds to z = 1.0. What score is the 84th percentile?', '700', 'None of these', '600', '500', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (1.0)(100) = 600', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('SAT scores are N(500, 100²). The 97.5th percentile corresponds to z = 2.0. What score is the 97.5th percentile?', '800', '500', '600', '700', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = μ + zσ = 500 + (2.0)(100) = 700', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 25²). The 97.5th percentile has z = 1.96. Find x.', '99.0', '50', '1.0', '124.0', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 50 + 1.96 × 25 = 99.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 15²). The 90th percentile has z = 1.28. Find x.', '50', '84.2', '69.2', '30.8', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 50 + 1.28 × 15 = 69.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 10²). The 90th percentile has z = 1.28. Find x.', '122.8', '100', '87.2', '112.8', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 100 + 1.28 × 10 = 112.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 10²). The 95th percentile has z = 1.645. Find x.', '33.5', '76.5', '66.5', '50', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 50 + 1.645 × 10 = 66.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(200, 10²). The 90th percentile has z = 1.28. Find x.', '200', '212.8', '187.2', '222.8', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 200 + 1.28 × 10 = 212.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(200, 15²). The 95th percentile has z = 1.645. Find x.', '239.7', '224.7', '175.3', '200', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 200 + 1.645 × 15 = 224.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(200, 10²). The 99th percentile has z = 2.33. Find x.', '176.7', '233.3', '200', '223.3', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 200 + 2.33 × 10 = 223.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(50, 10²). The 95th percentile has z = 1.645. Find x.', '76.5', '50', '33.5', '66.5', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'x = 50 + 1.645 × 10 = 66.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '99.7%', '95%', '50%', '68%', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '95%', '50%', '68%', '99.7%', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '95%', '68%', '99.7%', '50%', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '99.7%', '95%', '68%', '50%', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '99.7%', '50%', '68%', '95%', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '95%', '50%', '68%', '99.7%', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '68%', '95%', '50%', '99.7%', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ N(100, 15²). What percentage of values lie between 85 and 115?', '99.7%', '95%', '50%', '68%', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', '85 and 115 are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(300, 10²). Acceptable range is 290 to 310. What percentage passes?', '99.7%', '95%', '68%', '50%', 2,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 1σ. By empirical rule: 68%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(200, 5²). Acceptable range is 195 to 205. What percentage passes?', '99.7%', '50%', '95%', '68%', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 1σ. By empirical rule: 68%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(300, 5²). Acceptable range is 285 to 315. What percentage passes?', '99.7%', '50%', '95%', '68%', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 3σ. By empirical rule: 99.7%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(300, 10²). Acceptable range is 270 to 330. What percentage passes?', '50%', '99.7%', '68%', '95%', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 3σ. By empirical rule: 99.7%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(200, 10²). Acceptable range is 190 to 210. What percentage passes?', '68%', '95%', '99.7%', '50%', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 1σ. By empirical rule: 68%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(300, 10²). Acceptable range is 280 to 320. What percentage passes?', '99.7%', '95%', '68%', '50%', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 2σ. By empirical rule: 95%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(200, 10²). Acceptable range is 180 to 220. What percentage passes?', '95%', '99.7%', '50%', '68%', 0,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 2σ. By empirical rule: 95%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(300, 5²). Acceptable range is 290 to 310. What percentage passes?', '50%', '95%', '68%', '99.7%', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 2σ. By empirical rule: 95%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(200, 5²). Acceptable range is 195 to 205. What percentage passes?', '95%', '68%', '50%', '99.7%', 1,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 1σ. By empirical rule: 68%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Machine output ~ N(200, 10²). Acceptable range is 190 to 210. What percentage passes?', '95%', '99.7%', '50%', '68%', 3,
'lc_hl_probability', 11, 'advanced', 'lc_hl', 'Range is μ ± 1σ. By empirical rule: 68%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 5% of people. A test is 99% accurate for positive cases and has a 10% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.145', '0.343', '0.543', '0.99', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.05 × 0.99 / 0.1445 = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 2% of people. A test is 98% accurate for positive cases and has a 5% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.069', '0.98', '0.286', '0.486', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.02 × 0.98 / 0.0686 = 0.286', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 2% of people. A test is 98% accurate for positive cases and has a 5% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.486', '0.286', '0.98', '0.069', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.02 × 0.98 / 0.0686 = 0.286', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 5% of people. A test is 99% accurate for positive cases and has a 5% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.99', '0.097', '0.71', '0.51', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.05 × 0.99 / 0.097 = 0.51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 2% of people. A test is 95% accurate for positive cases and has a 5% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.95', '0.479', '0.068', '0.279', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.02 × 0.95 / 0.068 = 0.279', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 2% of people. A test is 99% accurate for positive cases and has a 5% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.488', '0.99', '0.288', '0.069', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.02 × 0.99 / 0.0688 = 0.288', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 1% of people. A test is 99% accurate for positive cases and has a 10% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.99', '0.109', '0.091', '0.291', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.01 × 0.99 / 0.1089 = 0.091', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A disease affects 5% of people. A test is 99% accurate for positive cases and has a 10% false positive rate. If someone tests positive, what is P(disease|positive)?', '0.145', '0.99', '0.343', '0.543', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = 0.05 × 0.99 / 0.1445 = 0.343', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.5). Find P(X ≥ 2).', '0.1094', '0.9906', '0.8906', '0.4453', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 2) = Σ P(X = i) for i = 2 to 6 = 0.8906', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(8, 0.5). Find P(X ≥ 4).', '0.3184', '0.7367', '0.3633', '0.6367', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 4) = Σ P(X = i) for i = 4 to 8 = 0.6367', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(5, 0.5). Find P(X ≥ 3).', 'None of these', '0.6', '0.5', '0.25', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 3) = Σ P(X = i) for i = 3 to 5 = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(7, 0.5). Find P(X ≥ 2).', '1.0375', '0.9375', '0.0625', '0.4688', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 2) = Σ P(X = i) for i = 2 to 7 = 0.9375', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.5). Find P(X ≥ 3).', '0.7562', '0.6562', '0.3438', '0.3281', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 3) = Σ P(X = i) for i = 3 to 6 = 0.6562', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.5). Find P(X ≥ 2).', '0.1094', '0.9906', '0.4453', '0.8906', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 2) = Σ P(X = i) for i = 2 to 6 = 0.8906', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.5). Find P(X ≥ 4).', '0.1719', '0.3438', '0.6562', '0.4437', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 4) = Σ P(X = i) for i = 4 to 6 = 0.3438', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(6, 0.5). Find P(X ≥ 4).', '0.3438', '0.6562', '0.4437', '0.1719', 0,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(X ≥ 4) = Σ P(X = i) for i = 4 to 6 = 0.3438', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(100, 0.5) can be approximated by N(μ, σ²). Find μ and σ.', 'μ = 50, σ ≈ 2.5', 'μ = 50, σ ≈ 10.0', 'μ = 25, σ ≈ 5.0', 'μ = 50, σ ≈ 5.0', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For binomial: μ = np = 50, σ = √(np(1-p)) ≈ 5.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(200, 0.5) can be approximated by N(μ, σ²). Find μ and σ.', 'μ = 100, σ ≈ 14.14', 'μ = 100, σ ≈ 3.54', 'μ = 50, σ ≈ 7.07', 'μ = 100, σ ≈ 7.07', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For binomial: μ = np = 100, σ = √(np(1-p)) ≈ 7.07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(200, 0.5) can be approximated by N(μ, σ²). Find μ and σ.', 'μ = 50, σ ≈ 7.07', 'μ = 100, σ ≈ 7.07', 'μ = 100, σ ≈ 3.54', 'μ = 100, σ ≈ 14.14', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For binomial: μ = np = 100, σ = √(np(1-p)) ≈ 7.07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(200, 0.5) can be approximated by N(μ, σ²). Find μ and σ.', 'μ = 100, σ ≈ 14.14', 'μ = 100, σ ≈ 3.54', 'μ = 100, σ ≈ 7.07', 'μ = 50, σ ≈ 7.07', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For binomial: μ = np = 100, σ = √(np(1-p)) ≈ 7.07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(100, 0.5) can be approximated by N(μ, σ²). Find μ and σ.', 'μ = 50, σ ≈ 10.0', 'μ = 25, σ ≈ 5.0', 'μ = 50, σ ≈ 5.0', 'μ = 50, σ ≈ 2.5', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For binomial: μ = np = 50, σ = √(np(1-p)) ≈ 5.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('X ~ B(100, 0.5) can be approximated by N(μ, σ²). Find μ and σ.', 'μ = 25, σ ≈ 5.0', 'μ = 50, σ ≈ 10.0', 'μ = 50, σ ≈ 2.5', 'μ = 50, σ ≈ 5.0', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For binomial: μ = np = 50, σ = √(np(1-p)) ≈ 5.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.4 and P(B) = 0.6. Find P(exactly one of A or B).', '0.62', '0.52', '0.76', '0.24', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(exactly one of A or B) = 0.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.3 and P(B) = 0.5. Find P(exactly one of A or B).', '0.5', '0.6', '0.65', '0.15', 0,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(exactly one of A or B) = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.4 and P(B) = 0.3. Find P(neither A nor B).', '0.58', '0.12', '0.42', '0.52', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(neither A nor B) = 0.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.3 and P(B) = 0.5. Find P(exactly one of A or B).', '0.5', '0.15', '0.6', '0.65', 0,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(exactly one of A or B) = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.4 and P(B) = 0.3. Find P(neither A nor B).', '0.52', '0.42', '0.58', '0.12', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(neither A nor B) = 0.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.3 and P(B) = 0.5. Find P(exactly one of A or B).', '0.65', '0.6', '0.15', '0.5', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(exactly one of A or B) = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.3 and P(B) = 0.5. Find P(neither A nor B).', '0.15', '0.45', '0.65', '0.35', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(neither A nor B) = 0.35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are independent with P(A) = 0.6 and P(B) = 0.6. Find P(neither A nor B).', '0.26', '0.16', '0.84', '0.36', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'For independent events: P(neither A nor B) = 0.16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Probability of success is 0.2. What is P(first success on trial 5)?', '0.3277', '0.0819', '0.0003', '0.2', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Geometric: P(X = 5) = (1-0.2)^4 × 0.2 = 0.0819', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Probability of success is 0.4. What is P(first success on trial 5)?', '0.4', '0.0102', '0.0778', '0.0518', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Geometric: P(X = 5) = (1-0.4)^4 × 0.4 = 0.0518', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Probability of success is 0.4. What is P(first success on trial 5)?', '0.0778', '0.0102', '0.4', '0.0518', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Geometric: P(X = 5) = (1-0.4)^4 × 0.4 = 0.0518', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Probability of success is 0.2. What is P(first success on trial 5)?', '0.0003', '0.0819', '0.2', '0.3277', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Geometric: P(X = 5) = (1-0.2)^4 × 0.2 = 0.0819', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Probability of success is 0.2. What is P(first success on trial 3)?', '0.512', '0.008', '0.2', '0.128', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Geometric: P(X = 3) = (1-0.2)^2 × 0.2 = 0.128', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Probability of success is 0.25. What is P(first success on trial 3)?', '0.0156', '0.25', '0.1406', '0.4219', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Geometric: P(X = 3) = (1-0.25)^2 × 0.25 = 0.1406', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. Find E(X | X is even).', '5', '4', '3.5', '3', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Given X is even, possible values are [2, 4, 6]. E(X | X is even) = 2+4+6/3 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. Find E(X | X > 3).', '3.5', '5', '6', '4', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Given X > 3, possible values are [4, 5, 6]. E(X | X > 3) = 4+5+6/3 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. Find E(X | X ≤ 3).', '3.5', '2', '3', '1', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Given X ≤ 3, possible values are [1, 2, 3]. E(X | X ≤ 3) = 1+2+3/3 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. Find E(X | X ≤ 3).', '2', '3', '1', '3.5', 0,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Given X ≤ 3, possible values are [1, 2, 3]. E(X | X ≤ 3) = 1+2+3/3 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. Find E(X | X > 3).', '5', '6', '4', '3.5', 0,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Given X > 3, possible values are [4, 5, 6]. E(X | X > 3) = 4+5+6/3 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. Find E(X | X is even).', '3.5', '5', '3', '4', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'Given X is even, possible values are [2, 4, 6]. E(X | X is even) = 2+4+6/3 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.4. If it rains, P(late) = 0.7. Otherwise, P(late) = 0.1. Find P(late).', '0.44', '0.7', '0.34', '1.1', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.4×0.7 + 0.6×0.1 = 0.34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.4. If it rains, P(late) = 0.7. Otherwise, P(late) = 0.2. Find P(late).', '0.5', '0.4', '1.1', '0.7', 1,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.4×0.7 + 0.6×0.2 = 0.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.3. If it rains, P(late) = 0.7. Otherwise, P(late) = 0.1. Find P(late).', '0.38', '1.0', '0.28', '0.7', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.3×0.7 + 0.7×0.1 = 0.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.4. If it rains, P(late) = 0.6. Otherwise, P(late) = 0.2. Find P(late).', '0.46', '0.6', '1.0', '0.36', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.4×0.6 + 0.6×0.2 = 0.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.3. If it rains, P(late) = 0.7. Otherwise, P(late) = 0.2. Find P(late).', '0.35', '0.45', '1.0', '0.7', 0,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.3×0.7 + 0.7×0.2 = 0.35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.4. If it rains, P(late) = 0.6. Otherwise, P(late) = 0.2. Find P(late).', '1.0', '0.46', '0.36', '0.6', 2,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.4×0.6 + 0.6×0.2 = 0.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.3. If it rains, P(late) = 0.6. Otherwise, P(late) = 0.1. Find P(late).', '0.9', '0.6', '0.35', '0.25', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.3×0.6 + 0.7×0.1 = 0.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain) = 0.3. If it rains, P(late) = 0.7. Otherwise, P(late) = 0.2. Find P(late).', '0.45', '1.0', '0.7', '0.35', 3,
'lc_hl_probability', 12, 'advanced', 'lc_hl', 'P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = 0.3×0.7 + 0.7×0.2 = 0.35', 1);