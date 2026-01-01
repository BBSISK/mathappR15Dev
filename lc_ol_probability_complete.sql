-- LC Ordinary Level - Probability Complete SQL
-- Generated: 2025-12-15
-- Total: 600 questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Probability topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_ol_probability', 'Probability', id, '🎲', 6, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_probability';

-- Insert questions
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Getting a month with 32 days''', 'Certain (1)', 'Likely', 'Impossible (0)', 'Unlikely', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Getting a month with 32 days'' is impossible (0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''The sun will rise tomorrow''', 'Certain (1)', 'Impossible (0)', 'Even chance (0.5)', 'Unlikely', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''The sun will rise tomorrow'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''The sun will rise tomorrow''', 'Even chance (0.5)', 'Unlikely', 'Certain (1)', 'Impossible (0)', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''The sun will rise tomorrow'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Picking a vowel from A,E,I,O,U''', 'Impossible (0)', 'Unlikely', 'Certain (1)', 'Even chance (0.5)', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Picking a vowel from A,E,I,O,U'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Rolling less than 7 on a standard die''', 'Even chance (0.5)', 'Impossible (0)', 'Certain (1)', 'Unlikely', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Rolling less than 7 on a standard die'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Drawing a red card from a standard deck''', 'Certain (1)', 'Very likely', 'Even chance (0.5)', 'Impossible (0)', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Drawing a red card from a standard deck'' is even chance (0.5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Rolling less than 7 on a standard die''', 'Certain (1)', 'Unlikely', 'Even chance (0.5)', 'Impossible (0)', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Rolling less than 7 on a standard die'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Rolling a 7 on a standard die''', 'Unlikely', 'Even chance (0.5)', 'Certain (1)', 'Impossible (0)', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Rolling a 7 on a standard die'' is impossible (0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''The sun will rise tomorrow''', 'Impossible (0)', 'Unlikely', 'Even chance (0.5)', 'Certain (1)', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''The sun will rise tomorrow'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Picking a vowel from A,E,I,O,U''', 'Unlikely', 'Impossible (0)', 'Certain (1)', 'Even chance (0.5)', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Picking a vowel from A,E,I,O,U'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Rolling an even number on a die''', 'Certain (1)', 'Even chance (0.5)', 'Impossible (0)', 'Unlikely', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Rolling an even number on a die'' is even chance (0.5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''The sun will rise tomorrow''', 'Unlikely', 'Certain (1)', 'Even chance (0.5)', 'Impossible (0)', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''The sun will rise tomorrow'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Rolling an even number on a die''', 'Certain (1)', 'Even chance (0.5)', 'Impossible (0)', 'Unlikely', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Rolling an even number on a die'' is even chance (0.5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''The sun will rise tomorrow''', 'Unlikely', 'Certain (1)', 'Even chance (0.5)', 'Impossible (0)', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''The sun will rise tomorrow'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Rolling a 7 on a standard die''', 'Unlikely', 'Even chance (0.5)', 'Impossible (0)', 'Certain (1)', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Rolling a 7 on a standard die'' is impossible (0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''It will rain sometime this year''', 'Impossible (0)', 'Very likely', 'Unlikely', 'Even chance (0.5)', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''It will rain sometime this year'' is very likely', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''A baby being born on a weekday''', 'Likely', 'Unlikely', 'Certain (1)', 'Impossible (0)', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''A baby being born on a weekday'' is likely', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Rolling less than 7 on a standard die''', 'Impossible (0)', 'Certain (1)', 'Unlikely', 'Even chance (0.5)', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Rolling less than 7 on a standard die'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Drawing a red card from a standard deck''', 'Impossible (0)', 'Even chance (0.5)', 'Very likely', 'Certain (1)', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Drawing a red card from a standard deck'' is even chance (0.5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify the probability: ''Picking a vowel from A,E,I,O,U''', 'Certain (1)', 'Unlikely', 'Even chance (0.5)', 'Impossible (0)', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '''Picking a vowel from A,E,I,O,U'' is certain (1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/10 to a percentage.', '20.0%', '0.1', 'Cannot determine', '10%', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/10 = 0.1 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 0.125 to a percentage.', '6.25%', '17.5%', '1/8', '12.5%', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/8 = 0.125 = 12.5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/2 to a decimal.', '50%', '0.5', '0.6', '1.0', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/2 = 0.5 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/5 to a decimal.', '0.4', '0.2', '0.30000000000000004', '20%', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/5 = 0.2 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/8 to a decimal.', '0.125', '12.5%', '0.25', '0.225', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/8 = 0.125 = 12.5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3/10 to a percentage.', '60.0%', '40.0%', '0.3', '30%', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '3/10 = 0.3 = 30%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/8 to a percentage.', '22.5%', '12.5%', '25.0%', '0.125', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/8 = 0.125 = 12.5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3/4 to a percentage.', '85.0%', '150.0%', '75%', '0.75', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '3/4 = 0.75 = 75%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 0.25 to a percentage.', '12.5%', '25%', '1/4', '30.0%', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/4 = 0.25 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 0.2 to a percentage.', '20%', '1/5', '25.0%', '10.0%', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/5 = 0.2 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/8 to a percentage.', '0.125', '25.0%', '12.5%', '22.5%', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/8 = 0.125 = 12.5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/2 to a decimal.', '1.0', '0.5', '50%', '0.6', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/2 = 0.5 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/5 to a percentage.', '0.2', '30.0%', '40.0%', '20%', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/5 = 0.2 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3/10 to a percentage.', '60.0%', '40.0%', '0.3', '30%', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '3/10 = 0.3 = 30%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/8 to a decimal.', '0.125', '0.25', '12.5%', '0.225', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/8 = 0.125 = 12.5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/5 to a percentage.', '20%', '0.2', '30.0%', '40.0%', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/5 = 0.2 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/10 to a percentage.', '20.0%', '0.1', 'Cannot determine', '10%', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/10 = 0.1 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3/4 to a decimal.', '0.85', '0.75', '75%', '1.5', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '3/4 = 0.75 = 75%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/2 to a percentage.', '50%', '0.5', '60.0%', '100.0%', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/2 = 0.5 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1/4 to a decimal.', '0.5', '25%', '0.35', '0.25', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1/4 = 0.25 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '-0.1', '0.5', '0', '1', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '-0.1 cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '0', '1', '110%', '0.5', 2,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '110% cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '1', '2%', '0', '0.5', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '2% cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '0', '1.5', '0.5', '1', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1.5 cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '0.5', '0', '1', '-0.1', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '-0.1 cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '2%', '1', '0', '0.5', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '2% cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '0.5', '1', '0', '2%', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '2% cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '0.5', '0', '1', '-0.3', 3,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '-0.3 cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '1.5', '0.5', '0', '1', 0,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '1.5 cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which of these CANNOT be a probability?', '1', '110%', '0', '0.5', 1,
'lc_ol_probability', 1, 'foundation', 'lc_ol', '110% cannot be a probability as probabilities must be between 0 and 1 (or 0% and 100%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting a number divisible by 3?', '2/3', '1/2', '1/3', '1/6', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Divisible by 3: 3, 6. P = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an even number?', '1/6', '1/2', '2/3', '1/3', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Even numbers: 2, 4, 6. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting a 2?', '2/6', '1/3', '1/2', '1/6', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(2) = 1/6 (one outcome out of six)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting greater than 3?', '1/2', 'Cannot determine', 'Cannot determine', '1/3', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers greater than 3: [4, 5, 6]. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting less than 5?', '2/3', '1/6', 'Cannot determine', '5/6', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers less than 5: [1, 2, 3, 4]. P = 4/6 = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an even number?', '1/3', '2/3', '1/2', '1/6', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Even numbers: 2, 4, 6. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting less than 4?', 'Cannot determine', '2/3', '1/6', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers less than 4: [1, 2, 3]. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an odd number?', '1/2', '1/3', '1/6', '2/3', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Odd numbers: 1, 3, 5. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an even number?', '1/3', '1/6', '2/3', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Even numbers: 2, 4, 6. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting less than 5?', '5/6', '2/3', 'Cannot determine', '1/6', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers less than 5: [1, 2, 3, 4]. P = 4/6 = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting less than 4?', '1/2', '1/6', '2/3', 'Cannot determine', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers less than 4: [1, 2, 3]. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting a 4?', '1/3', '1/6', '2/6', '1/2', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(4) = 1/6 (one outcome out of six)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting a 5?', '1/6', '2/6', '1/3', '1/2', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(5) = 1/6 (one outcome out of six)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting less than 4?', '2/3', '1/2', '1/6', 'Cannot determine', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers less than 4: [1, 2, 3]. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting greater than 4?', '1/6', '2/3', '1/3', '1/2', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers greater than 4: [5, 6]. P = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting a 5?', '2/6', '1/2', '1/3', '1/6', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(5) = 1/6 (one outcome out of six)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting less than 5?', '1/6', '5/6', 'Cannot determine', '2/3', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers less than 5: [1, 2, 3, 4]. P = 4/6 = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting a 1?', '2/6', '1/6', '1/2', '1/3', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(1) = 1/6 (one outcome out of six)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an odd number?', '1/2', '2/3', '1/6', '1/3', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Odd numbers: 1, 3, 5. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an even number?', '1/6', '2/3', '1/3', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Even numbers: 2, 4, 6. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting a number divisible by 3?', '1/3', '2/3', '1/6', '1/2', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Divisible by 3: 3, 6. P = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an even number?', '1/2', '1/3', '1/6', '2/3', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Even numbers: 2, 4, 6. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting greater than 3?', '1/2', 'Cannot determine', '1/3', 'Cannot determine', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Numbers greater than 3: [4, 5, 6]. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an even number?', '1/3', '2/3', '1/6', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Even numbers: 2, 4, 6. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair die is rolled. What is the probability of getting an even number?', '1/6', '1/2', '1/3', '2/3', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Even numbers: 2, 4, 6. P = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability of getting two heads?', '1/3', '1/4', '1/2', '2/4', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Outcomes: HH, HT, TH, TT. P(HH) = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped. What is the probability of getting heads?', '1/3', '2/3', '1/4', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(Heads) = 1/2 for a fair coin', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability of getting two heads?', '1/4', '1/3', '2/4', '1/2', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Outcomes: HH, HT, TH, TT. P(HH) = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped. What is the probability of getting heads?', '1/4', '2/3', '1/2', '1/3', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(Heads) = 1/2 for a fair coin', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability of getting at least one head?', '3/4', '1/4', '1/2', '2/3', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Outcomes with at least one H: HH, HT, TH. P = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped. What is the probability of getting heads?', '1/2', '1/3', '2/3', '1/4', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(Heads) = 1/2 for a fair coin', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability of getting at least one head?', '1/2', '2/3', '1/4', '3/4', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Outcomes with at least one H: HH, HT, TH. P = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped. What is the probability of getting heads?', '1/4', '2/3', '1/3', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(Heads) = 1/2 for a fair coin', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability of getting at least one head?', '2/3', '1/4', '3/4', '1/2', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Outcomes with at least one H: HH, HT, TH. P = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped. What is the probability of getting heads?', '1/4', '1/3', '1/2', '2/3', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(Heads) = 1/2 for a fair coin', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped. What is the probability of getting heads?', '1/3', '2/3', '1/4', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(Heads) = 1/2 for a fair coin', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability both land the same?', '3/4', '1/3', '1/4', '1/2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Same outcomes: HH, TT. P = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A fair coin is flipped. What is the probability of getting heads?', '1/4', '1/3', '1/2', '2/3', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(Heads) = 1/2 for a fair coin', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability of getting at least one head?', '3/4', '2/3', '1/4', '1/2', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Outcomes with at least one H: HH, HT, TH. P = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two fair coins are flipped. What is the probability both land the same?', '1/3', '1/4', '1/2', '3/4', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'Same outcomes: HH, TT. P = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.2. What is P(not A)?', '0.8', '1.0', '0.3', '0.2', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.2 = 0.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.8. What is P(not A)?', '0.8', '0.9', '0.4', '0.2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.8 = 0.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.6. What is P(not A)?', '0.6', '0.4', '0.7', 'Cannot determine', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.6 = 0.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.3. What is P(not A)?', '0.4', '0.9', '0.7', '0.3', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.3 = 0.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.3. What is P(not A)?', '0.9', '0.3', '0.4', '0.7', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.3 = 0.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.4. What is P(not A)?', '0.8', '0.5', '0.6', '0.4', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.4 = 0.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.2. What is P(not A)?', '0.3', '0.2', '0.8', '1.0', 2,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.2 = 0.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.8. What is P(not A)?', '0.4', '0.9', '0.8', '0.2', 3,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.8 = 0.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.7. What is P(not A)?', '0.3', '0.8', '0.5', '0.7', 0,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.7 = 0.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of event A is 0.8. What is P(not A)?', '0.4', '0.2', '0.9', '0.8', 1,
'lc_ol_probability', 2, 'foundation', 'lc_ol', 'P(not A) = 1 - P(A) = 1 - 0.8 = 0.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 6)?', '1/4', '4/52', '1/13', '1/52', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 6 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a face card - J, Q, K)?', '1/4', '3/13', '4/13', '1/13', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '12 face cards (4 Jacks, 4 Queens, 4 Kings). P = 12/52 = 3/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 7)?', '4/52', '1/13', '1/4', '1/52', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 7 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 9)?', '1/52', '4/52', '1/13', '1/4', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 9 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a red card)?', '26/52', '1/4', '1/13', '1/2', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '26 red cards in 52. P = 26/52 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 6)?', '1/4', '1/13', '4/52', '1/52', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 6 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing the Ace of Spades)?', '4/52', '1/13', '1/52', '1/4', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'Only 1 Ace of Spades in 52 cards. P = 1/52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing the Ace of Spades)?', '4/52', '1/13', '1/52', '1/4', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'Only 1 Ace of Spades in 52 cards. P = 1/52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 6)?', '1/13', '1/4', '4/52', '1/52', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 6 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 10)?', '1/4', '4/52', '1/52', '1/13', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 10 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard 52-card deck. What is P(drawing a diamond)?', '1/4', '1/2', '1/13', '1/52', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '13 diamonds in 52 cards. P = 13/52 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a face card - J, Q, K)?', '3/13', '4/13', '1/4', '1/13', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '12 face cards (4 Jacks, 4 Queens, 4 Kings). P = 12/52 = 3/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 3)?', '1/52', '1/4', '1/13', '4/52', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 3 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a black card)?', '1/4', '1/2', '26/52', '1/13', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '26 black cards in 52. P = 26/52 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 7)?', '1/52', '4/52', '1/13', '1/4', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 7 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing the Ace of Spades)?', '1/4', '4/52', '1/52', '1/13', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'Only 1 Ace of Spades in 52 cards. P = 1/52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 5)?', '1/13', '1/52', '1/4', '4/52', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 5 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 5)?', '1/52', '4/52', '1/4', '1/13', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 5 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing the Ace of Spades)?', '1/4', '4/52', '1/52', '1/13', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'Only 1 Ace of Spades in 52 cards. P = 1/52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a black card)?', '1/13', '26/52', '1/4', '1/2', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '26 black cards in 52. P = 26/52 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a 4)?', '1/13', '1/52', '4/52', '1/4', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '4 cards with value 4 in 52. P = 4/52 = 1/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a face card - J, Q, K)?', '3/13', '1/13', '4/13', '1/4', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '12 face cards (4 Jacks, 4 Queens, 4 Kings). P = 12/52 = 3/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a black card)?', '1/4', '26/52', '1/2', '1/13', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '26 black cards in 52. P = 26/52 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard 52-card deck. What is P(drawing a diamond)?', '1/52', '1/13', '1/4', '1/2', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '13 diamonds in 52 cards. P = 13/52 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing the Ace of Spades)?', '1/13', '1/52', '4/52', '1/4', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'Only 1 Ace of Spades in 52 cards. P = 1/52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a black card)?', '1/4', '26/52', '1/2', '1/13', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '26 black cards in 52. P = 26/52 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing a face card - J, Q, K)?', '4/13', '1/4', '3/13', '1/13', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '12 face cards (4 Jacks, 4 Queens, 4 Kings). P = 12/52 = 3/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard 52-card deck. What is P(drawing a spade)?', '1/4', '1/2', '1/52', '1/13', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', '13 spades in 52 cards. P = 13/52 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing the Ace of Spades)?', '4/52', '1/4', '1/52', '1/13', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'Only 1 Ace of Spades in 52 cards. P = 1/52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn from a standard deck. What is P(drawing the Ace of Spades)?', '4/52', '1/13', '1/52', '1/4', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'Only 1 Ace of Spades in 52 cards. P = 1/52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 1 section(s) are blue. What is P(blue)?', 'Cannot determine', '3/4', '1/2', '1/4', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(blue) = 1/4 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 2 section(s) are yellow. What is P(yellow)?', 'Cannot determine', '1/2', '3/4', '1/4', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(yellow) = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 8 equal sections. 1 section(s) are blue. What is P(blue)?', 'Cannot determine', '1/8', '1/4', '7/8', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(blue) = 1/8 = 1/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 5 equal sections. 2 section(s) are yellow. What is P(yellow)?', '3/5', '1/5', 'Cannot determine', '2/5', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(yellow) = 2/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections. 2 section(s) are orange. What is P(orange)?', '1/3', '1/2', '1/6', '2/3', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(orange) = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections. 3 section(s) are red. What is P(red)?', '1/6', '2/3', '1/2', 'Cannot determine', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(red) = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections. 3 section(s) are orange. What is P(orange)?', 'Cannot determine', '1/6', '1/2', '2/3', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(orange) = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections. 3 section(s) are yellow. What is P(yellow)?', '2/3', 'Cannot determine', '1/6', '1/2', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(yellow) = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 8 equal sections. 1 section(s) are white. What is P(white)?', '7/8', '1/4', '1/8', 'Cannot determine', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(white) = 1/8 = 1/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections. 1 section(s) are orange. What is P(orange)?', '1/6', '5/6', 'Cannot determine', '1/3', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(orange) = 1/6 = 1/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 2 section(s) are red. What is P(red)?', '1/4', '1/2', 'Cannot determine', '3/4', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(red) = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 5 equal sections. 1 section(s) are red. What is P(red)?', 'Cannot determine', '4/5', '1/5', '2/5', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(red) = 1/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 2 section(s) are blue. What is P(blue)?', '1/4', '1/2', 'Cannot determine', '3/4', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(blue) = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections. 2 section(s) are orange. What is P(orange)?', '1/3', '1/6', '2/3', '1/2', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(orange) = 2/6 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections. 3 section(s) are green. What is P(green)?', 'Cannot determine', '1/6', '2/3', '1/2', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(green) = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 8 equal sections. 3 section(s) are white. What is P(white)?', '1/2', '5/8', '1/8', '3/8', 3,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(white) = 3/8 = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 2 section(s) are green. What is P(green)?', '3/4', '1/2', '1/4', 'Cannot determine', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(green) = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 2 section(s) are blue. What is P(blue)?', '1/4', '1/2', '3/4', 'Cannot determine', 1,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(blue) = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 1 section(s) are red. What is P(red)?', 'Cannot determine', '3/4', '1/4', '1/2', 2,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(red) = 1/4 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 4 equal sections. 2 section(s) are yellow. What is P(yellow)?', '1/2', 'Cannot determine', '3/4', '1/4', 0,
'lc_ol_probability', 3, 'foundation', 'lc_ol', 'P(yellow) = 2/4 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when flipping 2 coins?', '8', '2', 'Cannot determine', '4', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 2^2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when rolling one die?', '6', '1', '12', '36', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 6^1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes when drawing one card from a standard deck?', '13', '4', '52', '26', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'A standard deck has 52 cards', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes when drawing one card from a standard deck?', '13', '52', '26', '4', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'A standard deck has 52 cards', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when flipping 2 coins?', '2', '4', 'Cannot determine', '8', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 2^2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner with 3 sections is spun and a die is rolled. How many outcomes are possible?', '18', '9', '6', '24', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 3 × 6 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when rolling one die?', '12', '1', '36', '6', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 6^1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when flipping 3 coins?', '16', '4', '8', '6', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 2^3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when rolling one die?', '1', '36', '6', '12', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 6^1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner with 3 sections is spun and a die is rolled. How many outcomes are possible?', '18', '9', '24', '6', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 3 × 6 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner with 4 sections is spun and a die is rolled. How many outcomes are possible?', '10', '24', '8', '30', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 4 × 6 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when flipping 4 coins?', '16', '8', 'Cannot determine', '32', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when flipping 3 coins?', '8', '16', '6', '4', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 2^3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when flipping 4 coins?', '16', '32', '8', 'Cannot determine', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 2^4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when rolling one die?', '1', '36', '12', '6', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 6^1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes when drawing one card from a standard deck?', '13', '52', '4', '26', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'A standard deck has 52 cards', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when rolling two dice?', '24', '12', '6', '36', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 6^2 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner with 4 sections is spun and a die is rolled. How many outcomes are possible?', '24', '30', '10', '8', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 4 × 6 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many outcomes are in the sample space when rolling two dice?', '12', '24', '36', '6', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 6^2 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner with 4 sections is spun and a die is rolled. How many outcomes are possible?', '8', '24', '10', '30', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Sample space size = 4 × 6 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, HT, TT', 'HH, TT', 'HH, HT, TH, TT', 'H, T, HH, TT', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, TT', 'HH, HT, TT', 'HH, HT, TH, TT', 'H, T, HH, TT', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'H, T, HH, TT', 'HH, HT, TH, TT', 'HH, HT, TT', 'HH, TT', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'H, T, HH, TT', 'HH, HT, TH, TT', 'HH, TT', 'HH, HT, TT', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'H, T, HH, TT', 'HH, HT, TT', 'HH, TT', 'HH, HT, TH, TT', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, TT', 'H, T, HH, TT', 'HH, HT, TT', 'HH, HT, TH, TT', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'H, T, HH, TT', 'HH, HT, TT', 'HH, TT', 'HH, HT, TH, TT', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, TT', 'HH, HT, TT', 'HH, HT, TH, TT', 'H, T, HH, TT', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'H, T, HH, TT', 'HH, HT, TT', 'HH, TT', 'HH, HT, TH, TT', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, TT', 'H, T, HH, TT', 'HH, HT, TH, TT', 'HH, HT, TT', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'H, T, HH, TT', 'HH, TT', 'HH, HT, TH, TT', 'HH, HT, TT', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, TT', 'HH, HT, TT', 'H, T, HH, TT', 'HH, HT, TH, TT', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'H, T, HH, TT', 'HH, HT, TH, TT', 'HH, HT, TT', 'HH, TT', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, HT, TH, TT', 'H, T, HH, TT', 'HH, TT', 'HH, HT, TT', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two coins are flipped. Which lists ALL possible outcomes?', 'HH, TT', 'H, T, HH, TT', 'HH, HT, TH, TT', 'HH, HT, TT', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'All combinations of H and T for 2 coins: HH, HT, TH, TT (4 outcomes)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '5', '12', '7', '6', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '7', '6', '5', '12', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '12', '5', '7', '6', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '5', '6', '7', '12', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '7', '5', '12', '6', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '7', '12', '6', '5', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '7', '6', '5', '12', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '6', '5', '12', '7', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '5', '12', '7', '6', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '7', '12', '6', '5', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '5', '6', '12', '7', 1,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '6', '5', '12', '7', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '12', '5', '7', '6', 3,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '12', '7', '6', '5', 2,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two dice are rolled. How many outcomes give a sum of 7?', '6', '5', '12', '7', 0,
'lc_ol_probability', 4, 'developing', 'lc_ol', 'Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/6', '1/2', '1/12', '7/12', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/6', '1/12', '2/6', '1/36', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/12', '7/12', '1/6', '1/2', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/12', '1/36', '2/6', '1/6', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/2', '7/12', '1/12', '1/6', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/2', '1/6', '7/12', '1/12', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/12', '1/6', '2/6', '1/36', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '2/6', '1/36', '1/6', '1/12', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/12', '1/6', '2/6', '1/36', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/12', '7/12', '1/6', '1/2', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/12', '1/6', '7/12', '1/2', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/6', '1/12', '1/36', '2/6', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/36', '2/6', '1/6', '1/12', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/12', '1/2', '1/6', '7/12', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all heads)?', '1/8', '1/4', '1/16', '3/2', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(all H) = (1/2)^3 = 1/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 2 times. What is P(all heads)?', '1/2', '2/2', '1/8', '1/4', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(all H) = (1/2)^2 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped and a die is rolled. What is P(heads AND 6)?', '1/2', '1/6', '7/12', '1/12', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(H and 6) = 1/2 × 1/6 = 1/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all heads)?', '1/16', '1/8', '1/4', '3/2', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(all H) = (1/2)^3 = 1/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all heads)?', '1/8', '3/2', '1/16', '1/4', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(all H) = (1/2)^3 = 1/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/6', '1/12', '2/6', '1/36', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/36', '2/6', '1/12', '1/6', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '2/6', '1/12', '1/36', '1/6', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/6', '1/36', '1/12', '2/6', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '1/6', '2/6', '1/36', '1/12', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled twice. What is P(getting 6 both times)?', '2/6', '1/6', '1/36', '1/12', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(6 and 6) = 1/6 × 1/6 = 1/36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 8 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/5', '1/9', '1/25', '1/45', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 2/10 × 1/9 = 1/45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 3 blue balls. Two balls are drawn without replacement. What is P(both red)?', '4/7', '5/8', '25/64', '5/14', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 5/8 × 4/7 = 5/14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 4 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/3', '1/9', '1/15', '1/5', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 2/6 × 1/5 = 1/15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 4 red and 4 blue balls. Two balls are drawn without replacement. What is P(both red)?', '3/14', '1/2', '1/4', '3/7', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 4/8 × 3/7 = 3/14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 8 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/5', '1/45', '1/9', '1/25', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 2/10 × 1/9 = 1/45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 8 red and 2 blue balls. Two balls are drawn without replacement. What is P(both red)?', '28/45', '16/25', '7/9', '4/5', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 8/10 × 7/9 = 28/45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 2 blue balls. Two balls are drawn without replacement. What is P(both red)?', '9/25', '3/5', '3/10', '1/2', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 4 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/3', '1/15', '1/5', '1/9', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 2/6 × 1/5 = 1/15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 8 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/45', '1/25', '1/5', '1/9', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 2/10 × 1/9 = 1/45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 6 red and 4 blue balls. Two balls are drawn without replacement. What is P(both red)?', '9/25', '5/9', '3/5', '1/3', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 6/10 × 5/9 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 2 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/2', '9/25', '3/5', '3/10', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 2 blue balls. Two balls are drawn without replacement. What is P(both red)?', '9/25', '3/10', '3/5', '1/2', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 6 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/28', '1/7', '1/4', '1/16', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 2/8 × 1/7 = 1/28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 5 red and 3 blue balls. Two balls are drawn without replacement. What is P(both red)?', '5/14', '25/64', '4/7', '5/8', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 5/8 × 4/7 = 5/14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 7 blue balls. Two balls are drawn without replacement. What is P(both red)?', '3/10', '1/15', '9/100', '2/9', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/10 × 2/9 = 1/15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 5 blue balls. Two balls are drawn without replacement. What is P(both red)?', '9/64', '2/7', '3/8', '3/28', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/8 × 2/7 = 3/28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 2 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/2', '3/10', '9/25', '3/5', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 2 blue balls. Two balls are drawn without replacement. What is P(both red)?', '9/25', '3/10', '1/2', '3/5', 1,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 4 red and 4 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/2', '3/7', '1/4', '3/14', 3,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 4/8 × 3/7 = 3/14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/10', '1/4', '2/5', '4/25', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 2/5 × 1/4 = 1/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 3 blue balls. Two balls are drawn without replacement. What is P(both red)?', '1/4', '1/2', '1/5', '2/5', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/6 × 2/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 5 blue balls. Two balls are drawn without replacement. What is P(both red)?', '9/64', '3/8', '3/28', '2/7', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/8 × 2/7 = 3/28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 3 red and 5 blue balls. Two balls are drawn without replacement. What is P(both red)?', '9/64', '2/7', '3/28', '3/8', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 3/8 × 2/7 = 3/28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 7 red and 3 blue balls. Two balls are drawn without replacement. What is P(both red)?', '7/15', '49/100', '7/10', '2/3', 0,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 7/10 × 6/9 = 7/15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 7 red and 3 blue balls. Two balls are drawn without replacement. What is P(both red)?', '49/100', '2/3', '7/15', '7/10', 2,
'lc_ol_probability', 5, 'developing', 'lc_ol', 'P(red, then red) = 7/10 × 6/9 = 7/15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '4/13', '2/13', '8/52', '1/13', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. What is P(getting 4 OR 2)?', '1/6', '2/36', '1/2', '1/3', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(4 or 2) = 1/6 + 1/6 = 2/6 = 1/3 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '1/13', '8/52', '2/13', '4/13', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '1/13', '8/52', '4/13', '2/13', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '1/13', '8/52', '4/13', '2/13', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '8/52', '1/13', '4/13', '2/13', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '8/52', '2/13', '1/13', '4/13', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '8/52', '2/13', '1/13', '4/13', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. What is P(getting 1 OR 6)?', '1/6', '1/3', '1/2', '2/36', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(1 or 6) = 1/6 + 1/6 = 2/6 = 1/3 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/3', '2/6', '1/2', '1/6', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/3', '1/6', '2/6', '1/2', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '2/6', '1/3', '1/6', '1/2', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/6', '2/6', '1/2', '1/3', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '2/6', '1/6', '1/3', '1/2', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '2/6', '1/3', '1/2', '1/6', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. What is P(getting 4 OR 5)?', '2/36', '1/6', '1/3', '1/2', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(4 or 5) = 1/6 + 1/6 = 2/6 = 1/3 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die is rolled. What is P(getting 4 OR 2)?', '1/3', '1/2', '1/6', '2/36', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(4 or 2) = 1/6 + 1/6 = 2/6 = 1/3 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '8/52', '4/13', '1/13', '2/13', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/3', '2/6', '1/2', '1/6', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(drawing a King OR a Queen)?', '2/13', '1/13', '8/52', '4/13', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(K or Q) = 4/52 + 4/52 = 8/52 = 2/13 (mutually exclusive)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/3', '1/2', '1/6', '2/6', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/6', '1/2', '2/6', '1/3', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/2', '2/6', '1/3', '1/6', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '2/6', '1/3', '1/2', '1/6', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A spinner has 6 equal sections: 2 red, 1 blue, 3 green. What is P(red OR blue)?', '1/3', '2/6', '1/2', '1/6', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or blue) = 2/6 + 1/6 = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '4/52', '26/52', '30/52', '7/13', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '7/13', '4/52', '26/52', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '26/52', '4/52', '7/13', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '4/52', '7/13', '30/52', '26/52', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '26/52', '7/13', '4/52', '30/52', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '7/13', '26/52', '30/52', '4/52', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '4/52', '30/52', '7/13', '26/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '7/13', '26/52', '4/52', '30/52', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '7/13', '26/52', '4/52', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '4/52', '30/52', '7/13', '26/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '4/52', '7/13', '26/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '26/52', '7/13', '30/52', '4/52', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '26/52', '30/52', '7/13', '4/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '26/52', '4/52', '7/13', '30/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '7/13', '4/52', '26/52', '30/52', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '4/52', '30/52', '7/13', '26/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '26/52', '7/13', '4/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '4/52', '7/13', '26/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '7/13', '4/52', '26/52', 1,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '4/52', '30/52', '26/52', '7/13', 3,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '7/13', '26/52', '30/52', '4/52', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '7/13', '26/52', '30/52', '4/52', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '7/13', '4/52', '26/52', '30/52', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '30/52', '26/52', '7/13', '4/52', 2,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A card is drawn. What is P(red card OR King)?', '7/13', '4/52', '30/52', '26/52', 0,
'lc_ol_probability', 6, 'developing', 'lc_ol', 'P(red or King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13 (subtract overlap)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '9/49', '12/49', '1/7', '3/7', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 3/7 × 3/7 = 9/49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 3 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '1/7', '9/49', '12/49', '4/7', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 3/7 × 3/7 = 9/49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 2 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '4/49', '1/7', '10/49', '5/7', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 2/7 × 2/7 = 4/49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 3 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '1/2', '1/6', 'Cannot determine', '1/4', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 3/6 × 3/6 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 3 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '15/64', '1/8', '25/64', '5/8', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 5/8 × 5/8 = 25/64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 2 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '2/9', '1/6', '4/9', '2/3', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 4/6 × 4/6 = 4/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 2 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '4/9', '2/9', '1/6', '2/3', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 4/6 × 4/6 = 4/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 3 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', 'Cannot determine', '1/6', '1/2', '1/4', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 3/6 × 3/6 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 3 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '15/64', '5/8', '15/32', '1/8', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 5/8 × 3/8 = 15/32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '1/5', '9/25', '3/5', '6/25', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 3/5 × 3/5 = 9/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 3 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '1/4', 'Cannot determine', '1/6', '1/2', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 3/6 × 3/6 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 3 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '4/7', '12/49', '16/49', '1/7', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 4/7 × 4/7 = 16/49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 4 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '5/9', '20/81', '25/81', '1/9', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 5/9 × 5/9 = 25/81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 4 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '1/9', '5/9', '40/81', '20/81', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 5/9 × 4/9 = 40/81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 4 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '1/8', '1/4', '1/2', 'Cannot determine', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 4/8 × 4/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '1/5', '6/25', '3/5', '9/25', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 3/5 × 3/5 = 9/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 3 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '1/2', '1/4', 'Cannot determine', '1/6', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 3/6 × 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 4 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '20/81', '5/9', '40/81', '1/9', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 5/9 × 4/9 = 40/81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 4 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '1/8', '1/2', '1/4', 'Cannot determine', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 4/8 × 4/8 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 3 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '12/49', '24/49', '4/7', '1/7', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 4/7 × 3/7 = 24/49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '6/25', '1/5', '4/25', '3/5', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 2/5 × 2/5 = 4/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 4 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '1/2', '1/4', '1/8', 'Cannot determine', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 4/8 × 4/8 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 4 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '5/9', '20/81', '1/9', '16/81', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 4/9 × 4/9 = 16/81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 3 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '15/64', '15/32', '5/8', '1/8', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 5/8 × 3/8 = 15/32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 4 blue balls. One drawn, replaced, another drawn. What is P(both red)?', '20/81', '1/9', '25/81', '5/9', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R,R) = 5/9 × 5/9 = 25/81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 2 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '4/9', '2/9', '2/3', '1/6', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 4/6 × 2/6 = 4/9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 3 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '1/4', 'Cannot determine', '1/6', '1/2', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 3/6 × 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 3 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '9/64', '15/64', '1/8', '5/8', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 3/8 × 3/8 = 9/64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 5 red, 3 blue balls. One drawn, replaced, another drawn. What is P(different colors)?', '5/8', '1/8', '15/64', '15/32', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(different) = P(R,B) + P(B,R) = 2 × 5/8 × 3/8 = 15/32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 4 red, 4 blue balls. One drawn, replaced, another drawn. What is P(both blue)?', '1/8', '1/2', 'Cannot determine', '1/4', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(B,B) = 4/8 × 4/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/10', '3/5', '1/2', '6/25', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '1/2', '3/10', '3/5', '6/25', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '3/5', '3/10', '1/2', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '1/2', '3/10', '3/5', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '1/2', '3/5', '3/10', 3,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/5', '6/25', '3/10', '1/2', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '1/2', '3/10', '3/5', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '3/10', '3/5', '1/2', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/5', '3/10', '1/2', '6/25', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '1/2', '3/10', '3/5', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '1/2', '3/10', '3/5', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '1/2', '3/5', '3/10', '6/25', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/5', '3/10', '6/25', '1/2', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/5', '3/10', '1/2', '6/25', 1,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/5', '1/2', '3/10', '6/25', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/5', '6/25', '3/10', '1/2', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '6/25', '1/2', '3/10', '3/5', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/5', '6/25', '3/10', '1/2', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '1/2', '6/25', '3/10', '3/5', 2,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 2 blue balls. Two drawn WITHOUT replacement. What is P(red then blue)?', '3/10', '6/25', '3/5', '1/2', 0,
'lc_ol_probability', 7, 'proficient', 'lc_ol', 'P(R then B) = 3/5 × 2/4 = 3/10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '7/8', '3/8', '6/8', '1/2', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '3/8', '1/8', '1/4', '1/2', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '1/4', '3/8', '1/2', '1/8', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '3/8', '7/8', '6/8', '1/2', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '1/8', '3/8', '1/2', '1/4', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '3/8', '1/2', '7/8', '6/8', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '3/8', '1/8', '1/4', '1/2', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '7/8', '3/8', '1/2', '6/8', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '1/8', '1/4', '3/8', '1/2', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '7/8', '6/8', '1/2', '3/8', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '6/8', '7/8', '3/8', '1/2', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '1/2', '7/8', '6/8', '3/8', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '1/4', '1/2', '3/8', '1/8', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all the same result)?', '1/8', '2/8', '1/4', '3/8', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(HHH or TTT) = 1/8 + 1/8 = 2/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all the same result)?', '1/8', '3/8', '2/8', '1/4', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(HHH or TTT) = 1/8 + 1/8 = 2/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '1/8', '1/4', '1/2', '3/8', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all the same result)?', '3/8', '1/8', '1/4', '2/8', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(HHH or TTT) = 1/8 + 1/8 = 2/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '6/8', '1/2', '7/8', '3/8', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all the same result)?', '2/8', '1/8', '3/8', '1/4', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(HHH or TTT) = 1/8 + 1/8 = 2/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '1/2', '6/8', '3/8', '7/8', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all the same result)?', '1/4', '3/8', '1/8', '2/8', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(HHH or TTT) = 1/8 + 1/8 = 2/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(at least one head)?', '6/8', '7/8', '1/2', '3/8', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(at least 1 H) = 1 - P(no H) = 1 - 1/8 = 7/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '1/8', '1/2', '3/8', '1/4', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(exactly 2 heads)?', '1/4', '1/8', '3/8', '1/2', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'Outcomes: HHT, HTH, THH = 3 outcomes. P = 3/8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin is flipped 3 times. What is P(all the same result)?', '3/8', '1/8', '2/8', '1/4', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(HHH or TTT) = 1/8 + 1/8 = 2/8 = 1/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '6/125', '1/125', '8/125', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '1/125', '8/125', '6/125', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '6/125', '1/125', '2/5', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '1/125', '8/125', '2/5', '6/125', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '6/125', '2/5', '1/125', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '1/125', '8/125', '2/5', '6/125', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '1/125', '6/125', '8/125', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '1/125', '2/5', '6/125', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '6/125', '8/125', '1/125', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '6/125', '8/125', '2/5', '1/125', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '6/125', '1/125', '2/5', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '1/125', '6/125', '8/125', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '2/5', '1/125', '6/125', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '1/125', '8/125', '2/5', '6/125', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '8/125', '6/125', '1/125', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '2/5', '6/125', '1/125', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '6/125', '8/125', '2/5', '1/125', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '1/125', '2/5', '6/125', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '1/125', '6/125', '2/5', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '6/125', '8/125', '2/5', '1/125', 1,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '1/125', '6/125', '8/125', '2/5', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '8/125', '6/125', '1/125', '2/5', 0,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '6/125', '2/5', '8/125', '1/125', 2,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '6/125', '1/125', '8/125', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bag has 2 red and 3 blue balls. Three drawn WITH replacement. What is P(all red)?', '2/5', '1/125', '6/125', '8/125', 3,
'lc_ol_probability', 8, 'proficient', 'lc_ol', 'P(R,R,R) = (2/5)³ = 8/125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:16, Male-No:13, Female-Yes:24, Female-No:14. What is P(Yes)?', '16/67', '40/67', '24/67', '13/67', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 40/67 = 40/67', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:24, Male-No:19, Female-Yes:21, Female-No:15. What is P(Yes | male)?', '21/79', '19/79', '24/79', '24/43', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes | male) = 24/43 = 24/43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:22, Male-No:24, Female-Yes:28, Female-No:18. What is P(Yes)?', '11/46', '7/23', '25/46', '6/23', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 50/92 = 25/46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:19, Male-No:19, Female-Yes:21, Female-No:20. What is P(male)?', 'Cannot determine', '38/79', '21/79', '19/79', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male) = 38/79 = 38/79', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:29, Male-No:15, Female-Yes:32, Female-No:16. What is P(male)?', '15/92', '8/23', '11/23', '29/92', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male) = 44/92 = 11/23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:29, Male-No:12, Female-Yes:34, Female-No:14. What is P(male)?', '41/89', '34/89', '12/89', '29/89', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male) = 41/89 = 41/89', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:16, Male-No:19, Female-Yes:30, Female-No:12. What is P(Yes | male)?', '19/77', '30/77', '16/35', '16/77', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes | male) = 16/35 = 16/35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:20, Male-No:24, Female-Yes:34, Female-No:14. What is P(male)?', '17/46', '5/23', '11/23', '6/23', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male) = 44/92 = 11/23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:30, Male-No:15, Female-Yes:25, Female-No:17. What is P(Yes | male)?', '5/29', '10/29', '2/3', '25/87', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes | male) = 30/45 = 2/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:27, Male-No:18, Female-Yes:23, Female-No:10. What is P(Yes)?', '23/78', '9/26', '25/39', '3/13', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 50/78 = 25/39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:22, Male-No:23, Female-Yes:21, Female-No:10. What is P(Yes)?', '21/76', '43/76', '23/76', '11/38', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 43/76 = 43/76', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:17, Male-No:17, Female-Yes:30, Female-No:18. What is P(male | Yes)?', '15/41', 'Cannot determine', '17/82', '17/47', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male | Yes) = 17/47 = 17/47', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:17, Male-No:11, Female-Yes:27, Female-No:17. What is P(Yes)?', '3/8', '11/18', '17/72', '11/72', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 44/72 = 11/18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:30, Male-No:11, Female-Yes:25, Female-No:20. What is P(Yes | male)?', '15/43', '30/41', '11/86', '25/86', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes | male) = 30/41 = 30/41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:25, Male-No:23, Female-Yes:20, Female-No:15. What is P(male)?', '20/83', '23/83', '48/83', '25/83', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male) = 48/83 = 48/83', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:27, Male-No:15, Female-Yes:35, Female-No:13. What is P(male | Yes)?', '27/62', '7/18', '3/10', '1/6', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male | Yes) = 27/62 = 27/62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:15, Male-No:24, Female-Yes:29, Female-No:14. What is P(Yes | male)?', '15/82', '12/41', '5/13', '29/82', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes | male) = 15/39 = 5/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:26, Male-No:19, Female-Yes:27, Female-No:20. What is P(Yes)?', '27/92', '19/92', '13/46', '53/92', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 53/92 = 53/92', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:18, Male-No:11, Female-Yes:29, Female-No:17. What is P(Yes)?', '29/75', '11/75', '6/25', '47/75', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 47/75 = 47/75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:18, Male-No:11, Female-Yes:34, Female-No:15. What is P(male | Yes)?', '9/26', '3/13', '17/39', '11/78', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male | Yes) = 18/52 = 9/26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:23, Male-No:23, Female-Yes:20, Female-No:12. What is P(male)?', '23/39', '23/78', 'Cannot determine', '10/39', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male) = 46/78 = 23/39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:30, Male-No:10, Female-Yes:32, Female-No:11. What is P(male | Yes)?', '30/83', '32/83', '10/83', '15/31', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male | Yes) = 30/62 = 15/31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:24, Male-No:17, Female-Yes:34, Female-No:10. What is P(Yes)?', '58/85', '24/85', '1/5', '2/5', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes) = 58/85 = 58/85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:24, Male-No:24, Female-Yes:27, Female-No:19. What is P(Yes | male)?', '12/47', 'Cannot determine', '27/94', '1/2', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(Yes | male) = 24/48 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Survey: Male-Yes:20, Male-No:20, Female-Yes:31, Female-No:14. What is P(male)?', '8/17', '31/85', '4/17', 'Cannot determine', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'P(male) = 40/85 = 8/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 17, 17, 15 and total is 76. Find the fourth value.', '32', '76', '27', '24', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 76 - 17 - 17 - 15 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 13, 17, 18 and total is 74. Find the fourth value.', '74', '26', '23', '31', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 74 - 13 - 17 - 18 = 26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 19, 21, 12 and total is 62. Find the fourth value.', '15', '7', '10', '62', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 62 - 19 - 21 - 12 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 19, 15, 19 and total is 71. Find the fourth value.', '15', '71', '18', '23', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 71 - 19 - 15 - 19 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 16, 21, 20 and total is 78. Find the fourth value.', '18', '78', '21', '26', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 78 - 16 - 21 - 20 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 13, 19, 17 and total is 70. Find the fourth value.', '70', '21', '18', '26', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 70 - 13 - 19 - 17 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 11, 15, 22 and total is 70. Find the fourth value.', '22', '70', '19', '27', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 70 - 11 - 15 - 22 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 13, 19, 14 and total is 68. Find the fourth value.', '19', '22', '68', '27', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 68 - 13 - 19 - 14 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 13, 16, 12 and total is 68. Find the fourth value.', '27', '32', '68', '24', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 68 - 13 - 16 - 12 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 14, 20, 14 and total is 60. Find the fourth value.', '60', '12', '9', '17', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 60 - 14 - 20 - 14 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 20, 19, 14 and total is 61. Find the fourth value.', '61', '13', '5', '8', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 61 - 20 - 19 - 14 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 16, 25, 17 and total is 79. Find the fourth value.', '21', '79', '18', '26', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 79 - 16 - 25 - 17 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 18, 17, 15 and total is 74. Find the fourth value.', '74', '24', '29', '21', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 74 - 18 - 17 - 15 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 15, 20, 19 and total is 77. Find the fourth value.', '28', '23', '20', '77', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 77 - 15 - 20 - 19 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 13, 18, 13 and total is 66. Find the fourth value.', '19', '27', '66', '22', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 66 - 13 - 18 - 13 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 17, 25, 13 and total is 60. Find the fourth value.', '60', '2', '5', '10', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 60 - 17 - 25 - 13 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 18, 25, 16 and total is 67. Find the fourth value.', '8', '13', '67', '5', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 67 - 18 - 25 - 16 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 10, 18, 20 and total is 72. Find the fourth value.', '24', '72', '29', '21', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 72 - 10 - 18 - 20 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 10, 22, 13 and total is 76. Find the fourth value.', '76', '28', '31', '36', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 76 - 10 - 22 - 13 = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 19, 17, 20 and total is 76. Find the fourth value.', '17', '20', '25', '76', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 76 - 19 - 17 - 20 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 17, 25, 19 and total is 63. Find the fourth value.', '2', '-1', '63', '7', 0,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 63 - 17 - 25 - 19 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 12, 16, 13 and total is 80. Find the fourth value.', '80', '44', '39', '36', 2,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 80 - 12 - 16 - 13 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 12, 20, 18 and total is 72. Find the fourth value.', '19', '27', '72', '22', 3,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 72 - 12 - 20 - 18 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 11, 16, 14 and total is 75. Find the fourth value.', '39', '34', '31', '75', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 75 - 11 - 16 - 14 = 34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a two-way table, three cells have values 15, 19, 16 and total is 64. Find the fourth value.', '64', '14', '19', '11', 1,
'lc_ol_probability', 9, 'proficient', 'lc_ol', 'Fourth value = 64 - 15 - 19 - 16 = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.4. If flipped 25 times, how many heads expected?', '15', '25', '12', '10', 3,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 25 × 0.4 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.5. If flipped 43 times, how many heads expected?', '43', '32', '21.5', '23', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 43 × 0.5 = 21.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.3. If flipped 27 times, how many heads expected?', '12', '27', '10', '8.1', 3,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 27 × 0.3 = 8.1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.1. If flipped 23 times, how many heads expected?', '2.3000000000000003', '4', '3', '23', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 23 × 0.1 = 2.3000000000000003', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.5. If flipped 18 times, how many heads expected?', '9', '18', '11', '14', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 18 × 0.5 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.1. If flipped 16 times, how many heads expected?', '1.6', '2', '3', '16', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 16 × 0.1 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.4. If flipped 49 times, how many heads expected?', '29', '19.6', '49', '21', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 49 × 0.4 = 19.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.4. If flipped 20 times, how many heads expected?', '12', '10', '8', '20', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 20 × 0.4 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.4. If flipped 16 times, how many heads expected?', '8', '6.4', '16', '10', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 16 × 0.4 = 6.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.3. If flipped 21 times, how many heads expected?', '21', '8', '6.3', '9', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 21 × 0.3 = 6.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.1. If flipped 50 times, how many heads expected?', '50', '8', '5', '7', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 50 × 0.1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.1. If flipped 16 times, how many heads expected?', '1.6', '16', '3', '2', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 16 × 0.1 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.2. If flipped 33 times, how many heads expected?', '33', '10', '8', '6.6000000000000005', 3,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 33 × 0.2 = 6.6000000000000005', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.3. If flipped 20 times, how many heads expected?', '9', '20', '6', '8', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 20 × 0.3 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.5. If flipped 17 times, how many heads expected?', '8.5', '10', '17', '13', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 17 × 0.5 = 8.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.1. If flipped 11 times, how many heads expected?', '1.1', '11', '2', '3', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 11 × 0.1 = 1.1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.1. If flipped 29 times, how many heads expected?', '2.9000000000000004', 'Cannot determine', '4', '29', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 29 × 0.1 = 2.9000000000000004', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.25. If flipped 43 times, how many heads expected?', '16', '12', '10.75', '43', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 43 × 0.25 = 10.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.4. If flipped 37 times, how many heads expected?', '16', '14.8', '37', '22', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 37 × 0.4 = 14.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.25. If flipped 46 times, how many heads expected?', '17', '13', '11.5', '46', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 46 × 0.25 = 11.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.3. If flipped 44 times, how many heads expected?', '15', '20', '13.2', '44', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 44 × 0.3 = 13.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.3. If flipped 12 times, how many heads expected?', 'Cannot determine', '3.5999999999999996', '12', '5', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 12 × 0.3 = 3.5999999999999996', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.5. If flipped 29 times, how many heads expected?', '16', '14.5', '22', '29', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 29 × 0.5 = 14.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.5. If flipped 46 times, how many heads expected?', '23', '46', '25', '34', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 46 × 0.5 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A coin has P(heads) = 0.4. If flipped 18 times, how many heads expected?', '11', '9', '7.2', '18', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'Expected = n × P = 18 × 0.4 = 7.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €25 with probability 2/5, lose €6 otherwise. What is the expected value?', '€8.4', '€6.4', '€25', '€19', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 2/5×25 - 3/5×6 = 6.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €29 with probability 1/5, lose €8 otherwise. What is the expected value?', '€29', '€21', '-€0.6', '€1.4', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×29 - 4/5×8 = -0.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €21 with probability 1/5, lose €7 otherwise. What is the expected value?', '€14', '€0.6', '€21', '-€1.4', 3,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×21 - 4/5×7 = -1.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €28 with probability 1/5, lose €2 otherwise. What is the expected value?', '€6.0', '€26', '€28', '€4.0', 3,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×28 - 4/5×2 = 4.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €20 with probability 1/5, lose €3 otherwise. What is the expected value?', '€1.6', '€3.6', '€17', '€20', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×20 - 4/5×3 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €11 with probability 1/5, lose €8 otherwise. What is the expected value?', '€-2.2', '€3', '€11', '-€4.2', 3,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×11 - 4/5×8 = -4.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €25 with probability 2/5, lose €3 otherwise. What is the expected value?', '€10.2', '€25', '€8.2', '€22', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 2/5×25 - 3/5×3 = 8.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €22 with probability 1/5, lose €6 otherwise. What is the expected value?', '€1.6', '€16', '-€0.4', '€22', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×22 - 4/5×6 = -0.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €29 with probability 1/5, lose €4 otherwise. What is the expected value?', '€29', '€4.6', '€2.6', '€25', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×29 - 4/5×4 = 2.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €13 with probability 1/6, lose €8 otherwise. What is the expected value?', '€-2.5', '€5', '-€4.5', '€13', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/6×13 - 5/6×8 = -4.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €18 with probability 1/6, lose €3 otherwise. What is the expected value?', '€2.5', '€18', '€0.5', '€15', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/6×18 - 5/6×3 = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €19 with probability 1/4, lose €7 otherwise. What is the expected value?', '€19', '-€0.5', '€12', '€1.5', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/4×19 - 3/4×7 = -0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €28 with probability 1/6, lose €2 otherwise. What is the expected value?', '€28', '€3.0', '€5.0', '€26', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/6×28 - 5/6×2 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €24 with probability 2/5, lose €7 otherwise. What is the expected value?', '€5.4', '€24', '€7.4', '€17', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 2/5×24 - 3/5×7 = 5.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €14 with probability 1/5, lose €8 otherwise. What is the expected value?', '€6', '€-1.6', '€14', '-€3.6', 3,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×14 - 4/5×8 = -3.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €24 with probability 1/4, lose €7 otherwise. What is the expected value?', '€17', '€0.75', '€2.75', '€24', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/4×24 - 3/4×7 = 0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €17 with probability 2/5, lose €4 otherwise. What is the expected value?', '€4.4', '€6.4', '€17', '€13', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 2/5×17 - 3/5×4 = 4.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €17 with probability 2/5, lose €3 otherwise. What is the expected value?', '€14', '€5.0', '€17', '€7.0', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 2/5×17 - 3/5×3 = 5.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €21 with probability 2/5, lose €4 otherwise. What is the expected value?', '€6.0', '€21', '€8.0', '€17', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 2/5×21 - 3/5×4 = 6.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €16 with probability 2/5, lose €8 otherwise. What is the expected value?', '€3.6', '€1.6', '€16', '€8', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 2/5×16 - 3/5×8 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €19 with probability 1/4, lose €2 otherwise. What is the expected value?', '€19', '€3.25', '€17', '€5.25', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/4×19 - 3/4×2 = 3.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €16 with probability 1/4, lose €5 otherwise. What is the expected value?', '€0.25', '€16', '€2.25', '€11', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/4×16 - 3/4×5 = 0.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €21 with probability 1/6, lose €4 otherwise. What is the expected value?', '€0.17', '€2.17', '€21', '€17', 0,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/6×21 - 5/6×4 = 0.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €28 with probability 1/5, lose €6 otherwise. What is the expected value?', '€2.8', '€28', '€0.8', '€22', 2,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/5×28 - 4/5×6 = 0.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A game: Win €18 with probability 1/4, lose €7 otherwise. What is the expected value?', '€11', '-€0.75', '€18', '€1.25', 1,
'lc_ol_probability', 10, 'advanced', 'lc_ol', 'E = 1/4×18 - 3/4×7 = -0.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 38 times. What is the experimental probability?', '2.63', '0.62', '0.48', '0.38', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 38/100 = 0.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 49 times. What is the experimental probability?', '0.49', '0.59', '0.51', '2.04', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 49/100 = 0.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 31 times. What is the experimental probability?', '0.69', '0.31', '3.23', '0.41', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 31/100 = 0.31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 42 times. What is the experimental probability?', '0.52', '2.38', '0.42', '0.58', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 42/100 = 0.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 25 trials, an event occurred 6 times. What is the experimental probability?', '0.34', '0.76', '4.17', '0.24', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 6/25 = 0.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 40 trials, an event occurred 15 times. What is the experimental probability?', '2.67', '0.62', '0.47', '0.38', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 15/40 = 0.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 39 times. What is the experimental probability?', '0.49', '0.39', '2.56', '0.61', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 39/100 = 0.39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 25 trials, an event occurred 6 times. What is the experimental probability?', '0.34', '0.76', '0.24', '4.17', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 6/25 = 0.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 40 trials, an event occurred 8 times. What is the experimental probability?', '0.3', '5.0', '0.8', '0.2', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 8/40 = 0.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 50 trials, an event occurred 20 times. What is the experimental probability?', '0.6', '0.5', '2.5', '0.4', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 20/50 = 0.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 25 trials, an event occurred 5 times. What is the experimental probability?', '0.8', '0.2', '5.0', '0.3', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 5/25 = 0.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 39 times. What is the experimental probability?', '2.56', '0.39', '0.49', '0.61', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 39/100 = 0.39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 25 trials, an event occurred 8 times. What is the experimental probability?', '0.68', '0.32', '0.42', '3.12', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 8/25 = 0.32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 28 times. What is the experimental probability?', '3.57', '0.72', '0.28', '0.38', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 28/100 = 0.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 50 trials, an event occurred 23 times. What is the experimental probability?', '0.54', '2.17', '0.56', '0.46', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 23/50 = 0.46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 20 trials, an event occurred 10 times. What is the experimental probability?', '2.0', '0.6', '0.5', 'Cannot determine', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 10/20 = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 25 trials, an event occurred 6 times. What is the experimental probability?', '0.76', '0.24', '4.17', '0.34', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 6/25 = 0.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 50 trials, an event occurred 18 times. What is the experimental probability?', '0.64', '0.46', '2.78', '0.36', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 18/50 = 0.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 47 times. What is the experimental probability?', '0.53', '2.13', '0.47', '0.57', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 47/100 = 0.47', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 24 times. What is the experimental probability?', '0.24', '0.34', '4.17', '0.76', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 24/100 = 0.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 45 times. What is the experimental probability?', '0.45', 'Cannot determine', '2.22', '0.55', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 45/100 = 0.45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 100 trials, an event occurred 43 times. What is the experimental probability?', '0.57', '2.33', '0.43', '0.53', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 43/100 = 0.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 40 trials, an event occurred 20 times. What is the experimental probability?', '2.0', 'Cannot determine', '0.5', '0.6', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 20/40 = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 40 trials, an event occurred 11 times. What is the experimental probability?', '3.64', '0.28', '0.72', '0.38', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 11/40 = 0.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 25 trials, an event occurred 12 times. What is the experimental probability?', '0.52', '0.48', '2.08', '0.58', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental P = 12/25 = 0.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 7 times. Compare experimental to theoretical probability.', 'Exp: 0.234, Theo: 0.167', 'Exp: 0.117, Theo: 0.167', 'Exp: 0.167, Theo: 0.117', 'Both are 0.167', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 7/60 = 0.117. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 7 times. Compare experimental to theoretical probability.', 'Exp: 0.117, Theo: 0.167', 'Exp: 0.167, Theo: 0.117', 'Both are 0.167', 'Exp: 0.234, Theo: 0.167', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 7/60 = 0.117. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 180 times. A 6 appeared 33 times. Compare experimental to theoretical probability.', 'Exp: 0.167, Theo: 0.183', 'Both are 0.167', 'Exp: 0.183, Theo: 0.167', 'Exp: 0.366, Theo: 0.167', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 33/180 = 0.183. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 120 times. A 6 appeared 24 times. Compare experimental to theoretical probability.', 'Exp: 0.167, Theo: 0.2', 'Exp: 0.2, Theo: 0.167', 'Exp: 0.4, Theo: 0.167', 'Both are 0.167', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 24/120 = 0.2. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 7 times. Compare experimental to theoretical probability.', 'Exp: 0.117, Theo: 0.167', 'Exp: 0.167, Theo: 0.117', 'Both are 0.167', 'Exp: 0.234, Theo: 0.167', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 7/60 = 0.117. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 8 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.266, Theo: 0.167', 'Exp: 0.167, Theo: 0.133', 'Exp: 0.133, Theo: 0.167', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 8/60 = 0.133. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 120 times. A 6 appeared 27 times. Compare experimental to theoretical probability.', 'Exp: 0.225, Theo: 0.167', 'Exp: 0.45, Theo: 0.167', 'Exp: 0.167, Theo: 0.225', 'Both are 0.167', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 27/120 = 0.225. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 14 times. Compare experimental to theoretical probability.', 'Exp: 0.233, Theo: 0.167', 'Exp: 0.466, Theo: 0.167', 'Exp: 0.167, Theo: 0.233', 'Both are 0.167', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 14/60 = 0.233. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 120 times. A 6 appeared 20 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.334, Theo: 0.167', 'Exp: 0.167, Theo: 0.167', 'Cannot determine', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 20/120 = 0.167. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 120 times. A 6 appeared 29 times. Compare experimental to theoretical probability.', 'Exp: 0.242, Theo: 0.167', 'Both are 0.167', 'Exp: 0.167, Theo: 0.242', 'Exp: 0.484, Theo: 0.167', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 29/120 = 0.242. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 14 times. Compare experimental to theoretical probability.', 'Exp: 0.466, Theo: 0.167', 'Exp: 0.233, Theo: 0.167', 'Both are 0.167', 'Exp: 0.167, Theo: 0.233', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 14/60 = 0.233. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 180 times. A 6 appeared 33 times. Compare experimental to theoretical probability.', 'Exp: 0.366, Theo: 0.167', 'Both are 0.167', 'Exp: 0.167, Theo: 0.183', 'Exp: 0.183, Theo: 0.167', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 33/180 = 0.183. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 11 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.366, Theo: 0.167', 'Exp: 0.167, Theo: 0.183', 'Exp: 0.183, Theo: 0.167', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 11/60 = 0.183. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 180 times. A 6 appeared 26 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.144, Theo: 0.167', 'Exp: 0.167, Theo: 0.144', 'Exp: 0.288, Theo: 0.167', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 26/180 = 0.144. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 120 times. A 6 appeared 17 times. Compare experimental to theoretical probability.', 'Exp: 0.284, Theo: 0.167', 'Both are 0.167', 'Exp: 0.142, Theo: 0.167', 'Exp: 0.167, Theo: 0.142', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 17/120 = 0.142. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 120 times. A 6 appeared 18 times. Compare experimental to theoretical probability.', 'Exp: 0.15, Theo: 0.167', 'Both are 0.167', 'Exp: 0.167, Theo: 0.15', 'Exp: 0.3, Theo: 0.167', 0,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 18/120 = 0.15. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 120 times. A 6 appeared 23 times. Compare experimental to theoretical probability.', 'Exp: 0.384, Theo: 0.167', 'Both are 0.167', 'Exp: 0.167, Theo: 0.192', 'Exp: 0.192, Theo: 0.167', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 23/120 = 0.192. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 15 times. Compare experimental to theoretical probability.', 'Exp: 0.167, Theo: 0.25', 'Exp: 0.5, Theo: 0.167', 'Exp: 0.25, Theo: 0.167', 'Both are 0.167', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 15/60 = 0.25. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 7 times. Compare experimental to theoretical probability.', 'Exp: 0.167, Theo: 0.117', 'Both are 0.167', 'Exp: 0.234, Theo: 0.167', 'Exp: 0.117, Theo: 0.167', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 7/60 = 0.117. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 12 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.167, Theo: 0.2', 'Exp: 0.2, Theo: 0.167', 'Exp: 0.4, Theo: 0.167', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 12/60 = 0.2. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 180 times. A 6 appeared 32 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.178, Theo: 0.167', 'Exp: 0.356, Theo: 0.167', 'Exp: 0.167, Theo: 0.178', 1,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 32/180 = 0.178. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 12 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.4, Theo: 0.167', 'Exp: 0.2, Theo: 0.167', 'Exp: 0.167, Theo: 0.2', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 12/60 = 0.2. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 60 times. A 6 appeared 9 times. Compare experimental to theoretical probability.', 'Exp: 0.167, Theo: 0.15', 'Both are 0.167', 'Exp: 0.15, Theo: 0.167', 'Exp: 0.3, Theo: 0.167', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 9/60 = 0.15. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 180 times. A 6 appeared 22 times. Compare experimental to theoretical probability.', 'Both are 0.167', 'Exp: 0.244, Theo: 0.167', 'Exp: 0.122, Theo: 0.167', 'Exp: 0.167, Theo: 0.122', 2,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 22/180 = 0.122. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A die was rolled 180 times. A 6 appeared 24 times. Compare experimental to theoretical probability.', 'Exp: 0.167, Theo: 0.133', 'Exp: 0.266, Theo: 0.167', 'Both are 0.167', 'Exp: 0.133, Theo: 0.167', 3,
'lc_ol_probability', 11, 'advanced', 'lc_ol', 'Experimental = 24/180 = 0.133. Theoretical = 1/6 ≈ 0.167', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '4/15', '1/3', '29/90', '1', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '29/90', '4/15', '1', '1/3', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1', '1/3', '29/90', '4/15', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '4/15', '1', '29/90', '1/3', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '4/15', '1/3', '1', '29/90', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '4/15', '1/3', '1', '29/90', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '4/15', '1/3', '29/90', '1', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '4/15', '1/3', '29/90', '1', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '29/90', '4/15', '1/3', '1', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1/3', '29/90', '4/15', '1', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1', '4/15', '29/90', '1/3', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '29/90', '4/15', '1', '1/3', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '29/90', '4/15', '1/3', '1', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1/3', '4/15', '29/90', '1', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1/3', '4/15', '29/90', '1', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '29/90', '4/15', '1', '1/3', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1/3', '1', '29/90', '4/15', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1', '1/3', '4/15', '29/90', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1/3', '29/90', '1', '4/15', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bag: 3 red, 4 blue, 3 green. Two drawn WITHOUT replacement. What is P(same color)?', '1', '4/15', '29/90', '1/3', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(same) = P(RR) + P(BB) + P(GG) = 0.267', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/51', '1/17', '4/52', '3/52', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '1/17', '3/52', '4/51', '4/52', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '3/52', '1/17', '4/51', '4/52', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/52', '4/51', '3/52', '1/17', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/51', '3/52', '1/17', '4/52', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/51', '3/52', '4/52', '1/17', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/52', '4/51', '1/17', '3/52', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/52', '1/17', '3/52', '4/51', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '3/52', '1/17', '4/51', '4/52', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/51', '4/52', '1/17', '3/52', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '1/17', '4/51', '4/52', '3/52', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/52', '4/51', '1/17', '3/52', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '1/17', '4/52', '4/51', '3/52', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/51', '4/52', '1/17', '3/52', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two cards drawn without replacement. Given the first is a King, what is P(second is also a King)?', '4/52', '1/17', '3/52', '4/51', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'After first King drawn, 3 Kings remain from 51 cards. P = 3/51 = 1/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.2681', '0.0024', '0.1681', '0.7', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.7', '0.1681', '0.2681', '0.0024', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.7', '0.0024', '0.1681', '0.2681', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.2681', '0.7', '0.1681', '0.0024', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.1681', '0.7', '0.2681', '0.0024', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.2681', '0.0024', '0.1681', '0.7', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.0024', '0.2681', '0.7', '0.1681', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.2681', '0.0024', '0.1681', '0.7', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.0024', '0.7', '0.2681', '0.1681', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.2681', '0.1681', '0.0024', '0.7', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.0024', '0.1681', '0.2681', '0.7', 1,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.1681', '0.7', '0.2681', '0.0024', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.2681', '0.0024', '0.7', '0.1681', 3,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.7', '0.2681', '0.1681', '0.0024', 2,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('P(rain on any day) = 0.3. What is P(no rain for 5 consecutive days)?', '0.1681', '0.7', '0.2681', '0.0024', 0,
'lc_ol_probability', 12, 'advanced', 'lc_ol', 'P(no rain all 5 days) = (1-0.3)^5 = 0.1681', 1);

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_probability';
