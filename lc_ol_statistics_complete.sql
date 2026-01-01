-- LC Ordinary Level - Statistics (Descriptive) Complete SQL
-- Generated: 2025-12-15
-- Total: 600 questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Statistics topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_ol_statistics', 'Statistics', id, '📊', 4, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_statistics';

-- Insert questions
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 4, 13, 13, 15, 5', '50', '10', '9.0', '11.0', 1,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (4 + 13 + 13 + 15 + 5) ÷ 5 = 50 ÷ 5 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 6, 6, 4, 11, 13, 7', '8.8', '7.8', '47', '6.8', 1,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (6 + 6 + 4 + 11 + 13 + 7) ÷ 6 = 47 ÷ 6 = 7.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 15, 7, 4, 8, 14', '9.6', '10.6', '48', '8.6', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (15 + 7 + 4 + 8 + 14) ÷ 5 = 48 ÷ 5 = 9.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 3, 14, 10, 8, 14, 14', '10.5', '9.5', '11.5', '63', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (3 + 14 + 10 + 8 + 14 + 14) ÷ 6 = 63 ÷ 6 = 10.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 3, 5, 10, 15', '7.2', '33', '9.2', '8.2', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (3 + 5 + 10 + 15) ÷ 4 = 33 ÷ 4 = 8.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 6, 15, 10, 8', '8.8', '10.8', '9.8', '39', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (6 + 15 + 10 + 8) ÷ 4 = 39 ÷ 4 = 9.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 11, 4, 12, 3', '6.5', '30', '7.5', '8.5', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (11 + 4 + 12 + 3) ÷ 4 = 30 ÷ 4 = 7.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 2, 13, 6, 9', '30', '8.5', '6.5', '7.5', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (2 + 13 + 6 + 9) ÷ 4 = 30 ÷ 4 = 7.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 8, 10, 2, 11', '8.8', '7.8', '6.8', '31', 1,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (8 + 10 + 2 + 11) ÷ 4 = 31 ÷ 4 = 7.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 8, 12, 15, 7, 12', '54', '9.8', '10.8', '11.8', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (8 + 12 + 15 + 7 + 12) ÷ 5 = 54 ÷ 5 = 10.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 4, 8, 6, 5, 5', '5.6', '4.6', '6.6', '28', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (4 + 8 + 6 + 5 + 5) ÷ 5 = 28 ÷ 5 = 5.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 6, 4, 15, 12, 10, 3', '9.3', '7.3', '8.3', '50', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (6 + 4 + 15 + 12 + 10 + 3) ÷ 6 = 50 ÷ 6 = 8.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 3, 8, 2, 4', '5.2', '3.2', '4.2', '17', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (3 + 8 + 2 + 4) ÷ 4 = 17 ÷ 4 = 4.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 8, 15, 4, 2', '29', '6.2', '7.2', '8.2', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (8 + 15 + 4 + 2) ÷ 4 = 29 ÷ 4 = 7.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 13, 10, 9, 7, 5, 6', '7.3', '50', '9.3', '8.3', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (13 + 10 + 9 + 7 + 5 + 6) ÷ 6 = 50 ÷ 6 = 8.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 2, 10, 8, 6, 6, 2', '4.7', '6.7', '34', '5.7', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (2 + 10 + 8 + 6 + 6 + 2) ÷ 6 = 34 ÷ 6 = 5.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 7, 10, 12, 2, 2, 15', '9.0', '8', '7.0', '48', 1,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (7 + 10 + 12 + 2 + 2 + 15) ÷ 6 = 48 ÷ 6 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 5, 4, 9, 11', '29', '7.2', '6.2', '8.2', 1,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (5 + 4 + 9 + 11) ÷ 4 = 29 ÷ 4 = 7.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 5, 4, 7, 7', '5.8', '4.8', '6.8', '23', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (5 + 4 + 7 + 7) ÷ 4 = 23 ÷ 4 = 5.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 4, 8, 9, 3, 9', '6.6', '7.6', '5.6', '33', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (4 + 8 + 9 + 3 + 9) ÷ 5 = 33 ÷ 5 = 6.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 13, 12, 7, 10, 2', '8.8', '7.8', '9.8', '44', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (13 + 12 + 7 + 10 + 2) ÷ 5 = 44 ÷ 5 = 8.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 7, 3, 7, 5, 13, 10', '45', '8.5', '7.5', '6.5', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (7 + 3 + 7 + 5 + 13 + 10) ÷ 6 = 45 ÷ 6 = 7.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 5, 5, 8, 8', '6.5', '26', '5.5', '7.5', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (5 + 5 + 8 + 8) ÷ 4 = 26 ÷ 4 = 6.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 8, 6, 3, 2, 5', '4.8', '24', '5.8', '3.8', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (8 + 6 + 3 + 2 + 5) ÷ 5 = 24 ÷ 5 = 4.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 4, 3, 8, 10, 6', '5.2', '7.2', '6.2', '31', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Mean = (4 + 3 + 8 + 10 + 6) ÷ 5 = 31 ÷ 5 = 6.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 11, 13, 19, 2, 20, 19, 2', '12.3', '11', '19', '13', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 2, 2, 11, 13, 19, 19, 20. Middle value (position 4) = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 2, 10, 10, 11, 20, 13', '10', 'Cannot determine', '10.0', '11', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 2, 4, 10, 10, 11, 13, 20. Middle value (position 4) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 5, 7, 10, 12, 20, 10, 11', '11', '10.7', '10', 'Cannot determine', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 5, 7, 10, 10, 11, 12, 20. Middle value (position 4) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 3, 7, 16, 13, 1', '13', '7', '8.0', '3', 1,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 1, 3, 7, 13, 16. Middle value (position 3) = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 6, 2, 9, 12, 19', '6', '12', '9.6', '9', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 2, 6, 9, 12, 19. Middle value (position 3) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 19, 2, 1, 13, 2, 16, 10', '2', '13', '9.0', '10', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 1, 2, 2, 10, 13, 16, 19. Middle value (position 4) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 10, 10, 18, 13, 10, 5, 5, 1, 5', '8.6', 'Cannot determine', '5', '10', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 1, 5, 5, 5, 10, 10, 10, 13, 18. Middle value (position 5) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 12, 17, 16, 12, 7', '12.8', 'Cannot determine', '16', '12', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 7, 12, 12, 16, 17. Middle value (position 3) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 7, 2, 3, 14, 10, 17, 1, 9, 10', '7', '10', '8.1', '9', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 1, 2, 3, 7, 9, 10, 10, 14, 17. Middle value (position 5) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 12, 13, 12, 6', 'Cannot determine', '9.4', '6', '12', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 4, 6, 12, 12, 13. Middle value (position 3) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 17, 3, 9, 16, 14, 15, 19', '13.3', '16', '15', '14', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 3, 9, 14, 15, 16, 17, 19. Middle value (position 4) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 9, 10, 14, 10, 18', '10', '12.2', '14', 'Cannot determine', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 9, 10, 10, 14, 18. Middle value (position 3) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 13, 5, 12, 4, 8, 7, 1, 7, 12', 'Cannot determine', '7.7', '8', '7', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 1, 4, 5, 7, 7, 8, 12, 12, 13. Middle value (position 5) = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 9, 20, 17, 2, 14, 2, 7', '10.1', '14', '9', '7', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 2, 2, 7, 9, 14, 17, 20. Middle value (position 4) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 17, 7, 16, 10, 5, 3, 11', '9.9', '11', '10', '7', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 3, 5, 7, 10, 11, 16, 17. Middle value (position 4) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 1, 13, 3, 3, 19, 16, 11, 12', '11.5', '9.8', '12', '11', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 1, 3, 3, 11, 12, 13, 16, 19. Median = (11 + 12) ÷ 2 = 11.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 15, 17, 3, 13, 9, 11', '13', '12.0', '11', '11.3', 1,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 3, 9, 11, 13, 15, 17. Median = (11 + 13) ÷ 2 = 12.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 18, 12, 19, 6', '13.8', '12', '18', '15.0', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 6, 12, 18, 19. Median = (12 + 18) ÷ 2 = 15.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 14, 9, 7', '8.0', '7', '8.5', '9', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 4, 7, 9, 14. Median = (7 + 9) ÷ 2 = 8.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 17, 4, 13, 18, 10, 1', '11.5', '10.5', '10', '13', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 1, 4, 10, 13, 17, 18. Median = (10 + 13) ÷ 2 = 11.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 5, 12, 8, 17', '10.5', '12', '10.0', '8', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 5, 8, 12, 17. Median = (8 + 12) ÷ 2 = 10.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 3, 14, 19, 19, 12, 19, 20, 19', '19.0', '19', '15.6', 'Cannot determine', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 3, 12, 14, 19, 19, 19, 19, 20. Median = (19 + 19) ÷ 2 = 19.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 7, 17, 18, 14', '14', '14.0', '17', '15.5', 3,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 7, 14, 17, 18. Median = (14 + 17) ÷ 2 = 15.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 5, 8, 18, 7, 9, 11', '9.7', '8', '8.5', '9', 2,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 5, 7, 8, 9, 11, 18. Median = (8 + 9) ÷ 2 = 8.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 10, 13, 11', '10.5', '11', '9.5', '10', 0,
'lc_ol_statistics', 1, 'foundation', 'lc_ol', 'Ordered: 4, 10, 11, 13. Median = (10 + 11) ÷ 2 = 10.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 10, 9, 3, 9, 11, 9', '8.5', '11', '9', '10', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 9 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 15, 12, 9, 12, 12, 2, 16, 10', '9', '11.0', '2', '12', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 12 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 14, 14, 14, 12, 20, 12', '14', '20', '12', '14.3', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 14 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 8, 13, 15, 11, 13, 18, 14, 13', '8', '13.1', '13', '11', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 13 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 13, 11, 13, 19, 18, 7, 13, 6', '13', '12.5', '6', '7', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 13 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 4, 8, 18, 15, 15, 15', '15', '18', '12.5', '8', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 15 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 14, 14, 14, 17, 20, 13', '14', '17', '15.3', '20', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 14 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 14, 14, 14, 8, 9', '14', '8', '9', '11.8', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 14 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 13, 10, 13, 12, 19, 3, 13, 2', '13', '10.6', '3', '2', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 13 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 6, 6, 6, 20, 3, 20, 19', '6', '19', '11.4', '3', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 6 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 10, 3, 7, 3, 3, 14, 16', '8.0', '10', '3', '7', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 3 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 10, 10, 3, 17, 12, 10', '3', '10', '10.3', '17', 1,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 10 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 11, 12, 11, 17, 10, 11, 17, 20', '12', '11', '13.6', '10', 1,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 11 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 16, 4, 11, 4, 4, 19', '16', '9.7', '4', '19', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 4 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 18, 8, 8, 8, 1, 7, 14, 15', '9.9', '8', '7', '1', 1,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 8 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 12, 7, 9, 7, 7, 5, 6', '7.6', '6', '7', '5', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 7 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 6, 20, 18, 8, 6, 8, 6', '8', '10.3', '6', '18', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 6 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 3, 9, 9, 9, 15, 4, 18', '9', '9.6', '3', '4', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 9 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 14, 1, 1, 11, 14, 14, 9, 19', '1', '9', '14', '10.4', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 14 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 15, 5, 15, 15, 12', '5', '12', '12.4', '15', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 15 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 11, 13, 13, 16, 12, 5, 13', '5', '11', '11.9', '13', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 13 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 13, 8, 10, 7, 13, 19, 5, 13', '7', '5', '11.0', '13', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 13 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 1, 20, 4, 4, 4, 5', '5', '6.3', '1', '4', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 4 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 15, 15, 1, 15, 12, 13, 12, 9', '1', '11.5', '15', '9', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 15 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 12, 12, 7, 12, 10', '7', '10.6', '10', '12', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'The mode is 12 as it appears most frequently (3 times)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 39, 15, 38, 11, 11, 31', '28', '33', '11', '39', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 39 - 11 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 23, 28, 31, 6, 40, 9', '40', '34', '6', '39', 1,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 40 - 6 = 34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 44, 38, 17, 7, 9, 16, 36', '42', '44', '37', '7', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 44 - 7 = 37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 21, 9, 5, 50, 19, 47, 49, 21', '50', 'Cannot determine', '5', '45', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 50 - 5 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 7, 6, 32, 38, 17, 30, 44', '43', '44', '6', '38', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 44 - 6 = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 34, 34, 6, 36, 17', '30', '6', '35', '36', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 36 - 6 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 31, 50, 15, 41, 34, 15', '35', '40', '50', '15', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 50 - 15 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 42, 34, 31, 17, 35', '30', '42', '17', '25', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 42 - 17 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 39, 34, 25, 17, 10, 29', '10', '34', '39', '29', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 39 - 10 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 18, 49, 37, 13, 5, 27, 18, 23', '44', 'Cannot determine', '5', '49', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 49 - 5 = 44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 25, 43, 37, 8, 38, 26, 17', '8', '35', '40', '43', 1,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 43 - 8 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 21, 6, 47, 8, 23, 26, 49', '6', '48', '49', '43', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 49 - 6 = 43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 16, 29, 5, 27, 38, 11', '33', 'Cannot determine', '5', '38', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 38 - 5 = 33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 29, 6, 42, 46, 49, 46, 38, 39', '6', '49', '43', '48', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 49 - 6 = 43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 15, 44, 39, 18, 25, 44, 28, 13', '36', '31', '13', '44', 1,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Range = Maximum - Minimum = 44 - 13 = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 8, 5, 11, 14, 2', 'No mode', '2', '14', '11', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Each value appears only once, so there is no mode', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 8, 2, 18, 12, 10', 'No mode', 'Cannot determine', '2', '18', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Each value appears only once, so there is no mode', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 15, 19, 10, 7, 8', '10', '19', 'No mode', '7', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Each value appears only once, so there is no mode', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 13, 6, 17, 10, 8', 'No mode', '17', 'Cannot determine', '6', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Each value appears only once, so there is no mode', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 14, 1, 11, 19, 12', '1', '19', 'No mode', '11', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Each value appears only once, so there is no mode', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode(s) of: 9, 16, 12, 16, 9', 'No mode', '9', '16', '9 and 16', 3,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Both 9 and 16 appear twice, so the data is bimodal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode(s) of: 16, 7, 16, 7, 4', '7', '7 and 16', 'No mode', '16', 1,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Both 7 and 16 appear twice, so the data is bimodal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode(s) of: 9, 9, 15, 15, 14', 'No mode', '15', '9 and 15', '9', 2,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Both 9 and 15 appear twice, so the data is bimodal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode(s) of: 7, 7, 13, 7, 13', '7 and 13', '13', '7', 'No mode', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Both 7 and 13 appear twice, so the data is bimodal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode(s) of: 14, 6, 6, 14, 15', '6 and 14', 'No mode', '14', '6', 0,
'lc_ol_statistics', 2, 'foundation', 'lc_ol', 'Both 6 and 14 appear twice, so the data is bimodal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 9, 11, 13, 9, 9, 10. Find the total frequency.', '58', '13', '66', '61', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 9 + 11 + 13 + 9 + 9 + 10 = 61', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 4 categories with frequencies: 4, 11, 5, 12. Find the total frequency.', '32', '31', '37', '12', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 4 + 11 + 5 + 12 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 9, 9, 8, 6, 6, 9. Find the total frequency.', '44', '47', '9', '52', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 9 + 9 + 8 + 6 + 6 + 9 = 47', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 11, 12, 3, 9, 3, 8. Find the total frequency.', '48', '12', '46', '43', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 11 + 12 + 3 + 9 + 3 + 8 = 46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 10, 13, 10, 9, 11. Find the total frequency.', '55', '53', '13', '50', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 10 + 13 + 10 + 9 + 11 = 53', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 7, 10, 9, 5, 4. Find the total frequency.', '35', '32', '10', '40', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 7 + 10 + 9 + 5 + 4 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 5, 12, 5, 14, 7, 9. Find the total frequency.', '47', '53', '14', '52', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 5 + 12 + 5 + 14 + 7 + 9 = 52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 11, 11, 15, 5, 12, 11. Find the total frequency.', '15', '66', '65', '64', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 11 + 11 + 15 + 5 + 12 + 11 = 65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 14, 12, 3, 3, 15, 3. Find the total frequency.', '49', '50', '15', '54', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 14 + 12 + 3 + 3 + 15 + 3 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 11, 15, 12, 10, 4. Find the total frequency.', '51', '56', '52', '15', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 11 + 15 + 12 + 10 + 4 = 52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 12, 13, 3, 15, 12, 8. Find the total frequency.', '59', '65', '15', '63', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 12 + 13 + 3 + 15 + 12 + 8 = 63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 5, 4, 14, 10, 11. Find the total frequency.', '49', '14', '44', '39', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 5 + 4 + 14 + 10 + 11 = 44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 14, 11, 3, 4, 4. Find the total frequency.', '14', '36', '32', '39', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 14 + 11 + 3 + 4 + 4 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 4 categories with frequencies: 8, 14, 7, 6. Find the total frequency.', '14', '35', '38', '33', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 8 + 14 + 7 + 6 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 6 categories with frequencies: 4, 9, 6, 5, 15, 3. Find the total frequency.', '47', '42', '38', '15', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 4 + 9 + 6 + 5 + 15 + 3 = 42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 6, 15, 4, 5, 11. Find the total frequency.', '44', '36', '15', '41', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 6 + 15 + 4 + 5 + 11 = 41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 4 categories with frequencies: 7, 9, 11, 12. Find the total frequency.', '12', '43', '39', '36', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 7 + 9 + 11 + 12 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 4 categories with frequencies: 4, 11, 5, 9. Find the total frequency.', '29', '26', '11', '31', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 4 + 11 + 5 + 9 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 13, 5, 13, 10, 8. Find the total frequency.', '49', '45', '13', '51', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 13 + 5 + 13 + 10 + 8 = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has 5 categories with frequencies: 8, 10, 8, 3, 14. Find the total frequency.', '41', '43', '48', '14', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Total frequency = 8 + 10 + 8 + 3 + 14 = 43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 5, Value 2: 8, Value 3: 4, Value 4: 2, Value 5: 6), find the mode.', '1', '8', '2', '3', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 2 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 4, Value 2: 2, Value 3: 7, Value 4: 4, Value 5: 8), find the mode.', '5', '4', '8', '1', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 5 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 6, Value 2: 6, Value 3: 8, Value 4: 8, Value 5: 2), find the mode.', '4', '3', '8', '2', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 3 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 2, Value 2: 4, Value 3: 7, Value 4: 2, Value 5: 8), find the mode.', '5', '4', '1', '8', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 5 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 6, Value 2: 4, Value 3: 4, Value 4: 4, Value 5: 5), find the mode.', '2', '1', '5', '6', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 1 as it has the highest frequency (6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 3, Value 2: 5, Value 3: 7, Value 4: 7, Value 5: 7), find the mode.', '7', '3', '4', '2', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 3 as it has the highest frequency (7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 4, Value 2: 2, Value 3: 7, Value 4: 6, Value 5: 8), find the mode.', '4', '8', '5', '1', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 5 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 7, Value 2: 5, Value 3: 8, Value 4: 3, Value 5: 6), find the mode.', '8', '2', '4', '3', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 3 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 2, Value 2: 8, Value 3: 5, Value 4: 3, Value 5: 5), find the mode.', '2', '3', '1', '8', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 2 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 7, Value 2: 6, Value 3: 4, Value 4: 7, Value 5: 7), find the mode.', '7', '2', '1', '5', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 1 as it has the highest frequency (7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 8, Value 2: 4, Value 3: 7, Value 4: 4, Value 5: 3), find the mode.', '5', '8', '2', '1', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 1 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 5, Value 2: 7, Value 3: 2, Value 4: 7, Value 5: 2), find the mode.', '3', '7', '2', '1', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 2 as it has the highest frequency (7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 5, Value 2: 5, Value 3: 6, Value 4: 7, Value 5: 3), find the mode.', '5', '3', '4', '7', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 4 as it has the highest frequency (7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 3, Value 2: 3, Value 3: 7, Value 4: 4, Value 5: 8), find the mode.', '8', '1', '5', '4', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 5 as it has the highest frequency (8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the frequency table (Value 1: 7, Value 2: 7, Value 3: 2, Value 4: 3, Value 5: 3), find the mode.', '1', '7', '5', '2', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'The mode is 1 as it has the highest frequency (7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are ?, 5, 6, 6. Total = 40. Find the missing frequency.', '15', '40', '12', '10', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 40 - (5 + 6 + 6) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are ?, 8, 7, 12. Total = 41. Find the missing frequency.', '9', '7', '41', '12', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 41 - (8 + 7 + 12) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are ?, 5, 8, 7. Total = 42. Find the missing frequency.', '13', '8', '10', '42', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 42 - (5 + 8 + 7) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 10, 11, 5, ?. Total = 47. Find the missing frequency.', '47', '11', '9', '14', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 47 - (11 + 5) = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 11, 10, ?, 9. Total = 51. Find the missing frequency.', '9', '14', '51', '11', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 51 - (11 + 9) = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 9, 10, ?, 11. Total = 56. Find the missing frequency.', '56', '15', '13', '18', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 56 - (9 + 10) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are ?, 6, 11, 11. Total = 45. Find the missing frequency.', '14', '11', '45', '9', 1,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 45 - (11 + 11) = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 8, 11, 5, ?. Total = 43. Find the missing frequency.', '11', '9', '43', '14', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 43 - (11 + 5) = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 9, 5, 7, ?. Total = 41. Find the missing frequency.', '41', '10', '15', '12', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 41 - (9 + 5 + 7) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are ?, 12, 10, 10. Total = 45. Find the missing frequency.', '8', '45', '6', '11', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 45 - (12 + 10 + 10) = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are ?, 10, 11, 7. Total = 50. Find the missing frequency.', '11', '16', '50', '13', 3,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 50 - (10 + 11 + 7) = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 10, ?, 6, 10. Total = 47. Find the missing frequency.', '13', '47', '10', '8', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 47 - (10 + 6 + 10) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 7, 6, 11, ?. Total = 49. Find the missing frequency.', '18', '49', '15', '13', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 49 - (7 + 6 + 11) = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are ?, 12, 9, 5. Total = 50. Find the missing frequency.', '17', '12', '14', '50', 2,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 50 - (12 + 9 + 5) = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 6, 7, 6, ?. Total = 39. Find the missing frequency.', '8', '6', '11', '39', 0,
'lc_ol_statistics', 3, 'foundation', 'lc_ol', 'Missing = 39 - (6 + 7 + 6) = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 4), (2, 8), (3, 2), (4, 5), (5, 3), calculate the mean.', '2.77', '6.1', '3.27', '3.0', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 61 / 22 = 2.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 4), (2, 2), (3, 2), (4, 5), (5, 8), calculate the mean.', '4.02', '3.0', '3.52', '7.4', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 74 / 21 = 3.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 4), (2, 8), (3, 2), (4, 5), (5, 3), calculate the mean.', '3.0', '2.77', '3.27', '6.1', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 61 / 22 = 2.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 6), (2, 5), (3, 4), (4, 5), (5, 6), calculate the mean.', '7.8', '3.5', '3.0', 'Cannot determine', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 78 / 26 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 6), (2, 5), (3, 6), (4, 8), (5, 4), calculate the mean.', '8.6', '3.0', '2.97', '3.47', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 86 / 29 = 2.97', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 5), (2, 6), (3, 3), (4, 5), (5, 8), calculate the mean.', '3.69', '3.19', '3.0', '8.6', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 86 / 27 = 3.19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 8), (2, 4), (3, 2), (4, 4), (5, 8), calculate the mean.', '7.8', '3.5', '3.0', 'Cannot determine', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 78 / 26 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 2), (2, 6), (3, 6), (4, 3), (5, 5), calculate the mean.', '3.64', '3.0', '6.9', '3.14', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 69 / 22 = 3.14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 3), (2, 6), (3, 7), (4, 4), (5, 8), calculate the mean.', '9.2', '3.79', '3.29', '3.0', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 92 / 28 = 3.29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 8), (2, 5), (3, 3), (4, 3), (5, 8), calculate the mean.', '2.93', '3.0', '7.9', '3.43', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 79 / 27 = 2.93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 8), (2, 7), (3, 5), (4, 8), (5, 4), calculate the mean.', '3.0', '2.78', '3.28', '8.9', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 89 / 32 = 2.78', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 8), (2, 2), (3, 7), (4, 6), (5, 3), calculate the mean.', '3.0', '7.2', '2.77', '3.27', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 72 / 26 = 2.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 6), (2, 2), (3, 3), (4, 6), (5, 3), calculate the mean.', '3.0', '2.9', '3.4', '5.8', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 58 / 20 = 2.9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 6), (2, 4), (3, 3), (4, 4), (5, 8), calculate the mean.', '3.0', '7.9', '3.66', '3.16', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 79 / 25 = 3.16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 8), (2, 6), (3, 7), (4, 7), (5, 6), calculate the mean.', '9.9', '3.0', '2.91', '3.41', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 99 / 34 = 2.91', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 7), (2, 7), (3, 5), (4, 8), (5, 4), calculate the mean.', '3.34', '8.8', '3.0', '2.84', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 88 / 31 = 2.84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 6), (2, 6), (3, 7), (4, 2), (5, 8), calculate the mean.', '8.7', '3.0', 'Cannot determine', '3.5', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 87 / 29 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 5), (2, 2), (3, 2), (4, 8), (5, 3), calculate the mean.', '3.0', '3.6', '3.1', '6.2', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 62 / 20 = 3.1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 3), (2, 5), (3, 2), (4, 3), (5, 6), calculate the mean.', '3.71', '3.0', '6.1', '3.21', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 61 / 19 = 3.21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 5), (2, 8), (3, 7), (4, 5), (5, 5), calculate the mean.', '8.7', '3.4', '3.0', '2.9', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 87 / 30 = 2.9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 7), (2, 6), (3, 5), (4, 5), (5, 7), calculate the mean.', '3.0', '8.9', '2.97', '3.47', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 89 / 30 = 2.97', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 7), (2, 3), (3, 6), (4, 7), (5, 7), calculate the mean.', '9.4', '3.13', '3.63', '3.0', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 94 / 30 = 3.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 6), (2, 6), (3, 8), (4, 3), (5, 5), calculate the mean.', '2.82', '7.9', '3.0', '3.32', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 79 / 28 = 2.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 8), (2, 3), (3, 7), (4, 5), (5, 4), calculate the mean.', '3.28', '7.5', '2.78', '3.0', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 75 / 27 = 2.78', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From (value, frequency) pairs: (1, 5), (2, 7), (3, 2), (4, 4), (5, 8), calculate the mean.', '3.12', '3.0', '8.1', '3.62', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Mean = Σfx / Σf = 81 / 26 = 3.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 6), (2: 5), (3: 10), (4: 6), (5: 6). Find the median score.', '3', 'Cannot determine', '4', '2', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 33. Median position = 17.0. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 7), (2: 3), (3: 6), (4: 4), (5: 8). Find the median score.', '2', 'Cannot determine', '4', '3', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 28. Median position = 14.5. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 10), (2: 8), (3: 10), (4: 9), (5: 9). Find the median score.', '2', '3', 'Cannot determine', '4', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 46. Median position = 23.5. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 10), (2: 5), (3: 9), (4: 4), (5: 7). Find the median score.', '2', 'Cannot determine', '4', '3', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 35. Median position = 18.0. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 10), (2: 3), (3: 8), (4: 6), (5: 7). Find the median score.', '2', 'Cannot determine', '4', '3', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 34. Median position = 17.5. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 4), (2: 3), (3: 7), (4: 9), (5: 9). Find the median score.', '5', '4', '3', 'Cannot determine', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 32. Median position = 16.5. Counting through frequencies, median = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 5), (2: 10), (3: 5), (4: 9), (5: 6). Find the median score.', 'Cannot determine', '4', '2', '3', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 35. Median position = 18.0. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 5), (2: 9), (3: 9), (4: 4), (5: 8). Find the median score.', '2', 'Cannot determine', '3', '4', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 35. Median position = 18.0. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 5), (2: 9), (3: 9), (4: 7), (5: 4). Find the median score.', '2', '4', '3', 'Cannot determine', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 34. Median position = 17.5. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 8), (2: 9), (3: 5), (4: 10), (5: 3). Find the median score.', '3', '2', 'Cannot determine', '4', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 35. Median position = 18.0. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 3), (2: 8), (3: 4), (4: 7), (5: 8). Find the median score.', '4', '5', '3', 'Cannot determine', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 30. Median position = 15.5. Counting through frequencies, median = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 9), (2: 3), (3: 8), (4: 10), (5: 8). Find the median score.', 'Cannot determine', '3', '4', '2', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 38. Median position = 19.5. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 5), (2: 7), (3: 5), (4: 4), (5: 8). Find the median score.', '4', 'Cannot determine', '3', '2', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 29. Median position = 15.0. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 5), (2: 10), (3: 9), (4: 4), (5: 10). Find the median score.', '3', '4', '2', 'Cannot determine', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 38. Median position = 19.5. Counting through frequencies, median = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Score frequencies: (1: 4), (2: 7), (3: 4), (4: 6), (5: 9). Find the median score.', '5', '3', 'Cannot determine', '4', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Total = 30. Median position = 15.5. Counting through frequencies, median = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 3, 10-20: 3, 20-30: 7, 30-40: 10). Using midpoints, estimate the mean.', '28.4', '20.0', '22.4', '25.4', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 585 / 23 = 25.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 3, 10-20: 8, 20-30: 8, 30-40: 10). Using midpoints, estimate the mean.', '23.6', '20.6', '26.6', '20.0', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 685 / 29 = 23.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 4, 10-20: 10, 20-30: 9, 30-40: 5). Using midpoints, estimate the mean.', '23.4', '20.0', '17.4', '20.4', 3,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 570 / 28 = 20.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 5, 10-20: 3, 20-30: 10, 30-40: 6). Using midpoints, estimate the mean.', '22.1', '20.0', '19.1', '25.1', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 530 / 24 = 22.1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 4, 10-20: 8, 20-30: 7, 30-40: 8). Using midpoints, estimate the mean.', '20.0', '25.0', '22.0', '19.0', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 595 / 27 = 22.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 6, 10-20: 5, 20-30: 10, 30-40: 3). Using midpoints, estimate the mean.', '19.2', '16.2', '22.2', '20.0', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 460 / 24 = 19.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 9, 10-20: 3, 20-30: 9, 30-40: 4). Using midpoints, estimate the mean.', '18.2', '21.2', '20.0', '15.2', 0,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 455 / 25 = 18.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 5, 10-20: 4, 20-30: 6, 30-40: 5). Using midpoints, estimate the mean.', '23.5', '20.0', '20.5', '17.5', 2,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 410 / 20 = 20.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 5, 10-20: 10, 20-30: 4, 30-40: 8). Using midpoints, estimate the mean.', '20.0', '20.6', '23.6', '17.6', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 555 / 27 = 20.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Grouped data (0-10: 6, 10-20: 8, 20-30: 6, 30-40: 8). Using midpoints, estimate the mean.', '20.0', '20.7', '17.7', '23.7', 1,
'lc_ol_statistics', 4, 'developing', 'lc_ol', 'Midpoints: [5, 15, 25, 35]. Mean = Σfx / Σf = 580 / 28 = 20.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=10, B=20, C=17, D=9, E=6. Which category has the highest value and what is the total?', 'B, total = 62', 'B, total = 20', 'C, total = 62', 'B, total = 72', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: B with 20. Total = 10 + 20 + 17 + 9 + 6 = 62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=22, B=11, C=22, D=13, E=5. Which category has the highest value and what is the total?', 'A, total = 83', 'A, total = 73', 'B, total = 73', 'A, total = 22', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: A with 22. Total = 22 + 11 + 22 + 13 + 5 = 73', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=13, B=12, C=17, D=19, E=22. Which category has the highest value and what is the total?', 'E, total = 22', 'E, total = 93', 'E, total = 83', 'A, total = 83', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: E with 22. Total = 13 + 12 + 17 + 19 + 22 = 83', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=10, B=8, C=23, D=13, E=6. Which category has the highest value and what is the total?', 'D, total = 60', 'C, total = 60', 'C, total = 70', 'C, total = 23', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: C with 23. Total = 10 + 8 + 23 + 13 + 6 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=12, B=7, C=12, D=19, E=15. Which category has the highest value and what is the total?', 'D, total = 65', 'D, total = 75', 'D, total = 19', 'E, total = 65', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: D with 19. Total = 12 + 7 + 12 + 19 + 15 = 65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=7, B=11, C=16, D=6, E=15. Which category has the highest value and what is the total?', 'C, total = 55', 'C, total = 16', 'D, total = 55', 'C, total = 65', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: C with 16. Total = 7 + 11 + 16 + 6 + 15 = 55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=8, B=17, C=14, D=17, E=8. Which category has the highest value and what is the total?', 'C, total = 64', 'B, total = 64', 'B, total = 17', 'B, total = 74', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: B with 17. Total = 8 + 17 + 14 + 17 + 8 = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=17, B=11, C=25, D=22, E=7. Which category has the highest value and what is the total?', 'D, total = 82', 'C, total = 92', 'C, total = 25', 'C, total = 82', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: C with 25. Total = 17 + 11 + 25 + 22 + 7 = 82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=13, B=24, C=17, D=17, E=22. Which category has the highest value and what is the total?', 'C, total = 93', 'B, total = 24', 'B, total = 93', 'B, total = 103', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: B with 24. Total = 13 + 24 + 17 + 17 + 22 = 93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=9, B=22, C=23, D=9, E=12. Which category has the highest value and what is the total?', 'C, total = 75', 'D, total = 75', 'C, total = 23', 'C, total = 85', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: C with 23. Total = 9 + 22 + 23 + 9 + 12 = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=6, B=11, C=7, D=20, E=7. Which category has the highest value and what is the total?', 'E, total = 51', 'D, total = 61', 'D, total = 51', 'D, total = 20', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: D with 20. Total = 6 + 11 + 7 + 20 + 7 = 51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=11, B=8, C=17, D=12, E=22. Which category has the highest value and what is the total?', 'E, total = 22', 'E, total = 70', 'E, total = 80', 'A, total = 70', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: E with 22. Total = 11 + 8 + 17 + 12 + 22 = 70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=21, B=18, C=17, D=21, E=21. Which category has the highest value and what is the total?', 'A, total = 98', 'A, total = 108', 'B, total = 98', 'A, total = 21', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: A with 21. Total = 21 + 18 + 17 + 21 + 21 = 98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=25, B=20, C=13, D=22, E=25. Which category has the highest value and what is the total?', 'A, total = 115', 'B, total = 105', 'A, total = 105', 'A, total = 25', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: A with 25. Total = 25 + 20 + 13 + 22 + 25 = 105', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=11, B=17, C=22, D=9, E=10. Which category has the highest value and what is the total?', 'C, total = 69', 'C, total = 22', 'D, total = 69', 'C, total = 79', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: C with 22. Total = 11 + 17 + 22 + 9 + 10 = 69', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=8, B=23, C=13, D=16, E=22. Which category has the highest value and what is the total?', 'C, total = 82', 'B, total = 23', 'B, total = 82', 'B, total = 92', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: B with 23. Total = 8 + 23 + 13 + 16 + 22 = 82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=14, B=15, C=6, D=5, E=10. Which category has the highest value and what is the total?', 'B, total = 60', 'C, total = 50', 'B, total = 50', 'B, total = 15', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: B with 15. Total = 14 + 15 + 6 + 5 + 10 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=24, B=24, C=7, D=24, E=25. Which category has the highest value and what is the total?', 'E, total = 104', 'E, total = 114', 'E, total = 25', 'A, total = 104', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: E with 25. Total = 24 + 24 + 7 + 24 + 25 = 104', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=7, B=8, C=21, D=7, E=13. Which category has the highest value and what is the total?', 'D, total = 56', 'C, total = 21', 'C, total = 56', 'C, total = 66', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: C with 21. Total = 7 + 8 + 21 + 7 + 13 = 56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bar chart shows: A=17, B=21, C=15, D=15, E=12. Which category has the highest value and what is the total?', 'C, total = 80', 'B, total = 90', 'B, total = 21', 'B, total = 80', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Highest: B with 21. Total = 17 + 21 + 15 + 15 + 12 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 40 out of 100 people chose option A. What angle represents this?', '164.0°', '40.0°', '40°', '144°', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (40/100) × 360° = 144°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 20 out of 120 people chose option A. What angle represents this?', '20°', '16.7°', '60°', '80.0°', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (20/120) × 360° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 25 out of 60 people chose option A. What angle represents this?', '170.0°', '25°', '41.7°', '150°', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (25/60) × 360° = 150°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 18 out of 72 people chose option A. What angle represents this?', '90°', '110.0°', '18°', '25.0°', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (18/72) × 360° = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 15 out of 120 people chose option A. What angle represents this?', '15°', '65.0°', '45°', '12.5°', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (15/120) × 360° = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 20 out of 120 people chose option A. What angle represents this?', '80.0°', '20°', '16.7°', '60°', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (20/120) × 360° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 20 out of 180 people chose option A. What angle represents this?', '40°', '11.1°', '60.0°', '20°', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (20/180) × 360° = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 10 out of 90 people chose option A. What angle represents this?', '60.0°', '10°', '40°', '11.1°', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (10/90) × 360° = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 18 out of 60 people chose option A. What angle represents this?', '18°', '108°', '30.0°', '128.0°', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (18/60) × 360° = 108°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 10 out of 60 people chose option A. What angle represents this?', '10°', '16.7°', '80.0°', '60°', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (10/60) × 360° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 25 out of 90 people chose option A. What angle represents this?', '27.8°', '100°', '120.0°', '25°', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (25/90) × 360° = 100°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 24 out of 90 people chose option A. What angle represents this?', '26.7°', '116.0°', '24°', '96°', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (24/90) × 360° = 96°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 18 out of 72 people chose option A. What angle represents this?', '110.0°', '90°', '18°', '25.0°', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (18/72) × 360° = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 25 out of 72 people chose option A. What angle represents this?', '145.0°', '125°', '25°', '34.7°', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (25/72) × 360° = 125°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 18 out of 120 people chose option A. What angle represents this?', '15.0°', '54°', '18°', '74.0°', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (18/120) × 360° = 54°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 10 out of 180 people chose option A. What angle represents this?', '20°', '10°', '5.6°', '40.0°', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (10/180) × 360° = 20°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 20 out of 72 people chose option A. What angle represents this?', '20°', '100°', '120.0°', '27.8°', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (20/72) × 360° = 100°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 40 out of 100 people chose option A. What angle represents this?', '164.0°', '40.0°', '144°', '40°', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (40/100) × 360° = 144°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 20 out of 72 people chose option A. What angle represents this?', '27.8°', '100°', '120.0°', '20°', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (20/72) × 360° = 100°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a pie chart, 12 out of 60 people chose option A. What angle represents this?', '20.0°', '12°', '92.0°', '72°', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Angle = (12/60) × 360° = 72°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 120 items. A sector has angle 72°. How many items does it represent?', '24', '120', '29', '20', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (72/360) × 120 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 180 items. A sector has angle 72°. How many items does it represent?', '180', '41', '36', '20', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (72/360) × 180 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 180 items. A sector has angle 60°. How many items does it represent?', '17', '35', '30', '180', 2,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (60/360) × 180 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 180 items. A sector has angle 45°. How many items does it represent?', '12', '28', '180', '22.5', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (45/360) × 180 = 22.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 120 items. A sector has angle 90°. How many items does it represent?', '25', '120', '35', '30', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (90/360) × 120 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 90 items. A sector has angle 45°. How many items does it represent?', '11.2', '12', '90', '16', 0,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (45/360) × 90 = 11.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 120 items. A sector has angle 90°. How many items does it represent?', '35', '30', '120', '25', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (90/360) × 120 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 60 items. A sector has angle 30°. How many items does it represent?', '10', '5', '8', '60', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (30/360) × 60 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 60 items. A sector has angle 72°. How many items does it represent?', '17', '60', '20', '12', 3,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (72/360) × 60 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A pie chart represents 60 items. A sector has angle 120°. How many items does it represent?', '33', '20', '60', '25', 1,
'lc_ol_statistics', 5, 'developing', 'lc_ol', 'Frequency = (120/360) × 60 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 9, 10-20: 9, 20-30: 4, 30-40: 7, 40-50: 8). How many values are in the 30-40 group?', '37', '5', '10', '7', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 30-40 bar has frequency 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 5, 10-20: 5, 20-30: 3, 30-40: 9, 40-50: 14). How many values are in the 30-40 group?', '7', '12', '36', '9', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 30-40 bar has frequency 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 9, 10-20: 12, 20-30: 12, 30-40: 9, 40-50: 14). How many values are in the 30-40 group?', '12', '9', '7', '56', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 30-40 bar has frequency 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 3, 10-20: 4, 20-30: 10, 30-40: 14, 40-50: 4). How many values are in the 0-10 group?', '1', '6', '3', '35', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 9, 10-20: 5, 20-30: 3, 30-40: 12, 40-50: 6). How many values are in the 0-10 group?', '35', '7', '12', '9', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 4, 10-20: 7, 20-30: 3, 30-40: 7, 40-50: 14). How many values are in the 40-50 group?', '17', '35', '14', '12', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 40-50 bar has frequency 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 12, 10-20: 4, 20-30: 3, 30-40: 13, 40-50: 9). How many values are in the 20-30 group?', '41', '1', '3', '6', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 20-30 bar has frequency 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 12, 10-20: 12, 20-30: 15, 30-40: 7, 40-50: 12). How many values are in the 40-50 group?', '10', '12', '58', '15', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 40-50 bar has frequency 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 5, 10-20: 14, 20-30: 4, 30-40: 11, 40-50: 6). How many values are in the 0-10 group?', '5', '40', '8', '3', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 5, 10-20: 5, 20-30: 6, 30-40: 11, 40-50: 14). How many values are in the 0-10 group?', '3', '5', '8', '41', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 14, 10-20: 15, 20-30: 14, 30-40: 13, 40-50: 12). How many values are in the 40-50 group?', '15', '68', '12', '10', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 40-50 bar has frequency 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 11, 10-20: 3, 20-30: 6, 30-40: 13, 40-50: 5). How many values are in the 10-20 group?', '38', '6', '1', '3', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 10-20 bar has frequency 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 15, 10-20: 14, 20-30: 9, 30-40: 4, 40-50: 9). How many values are in the 40-50 group?', '51', '9', '12', '7', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 40-50 bar has frequency 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 8, 10-20: 13, 20-30: 4, 30-40: 5, 40-50: 4). How many values are in the 0-10 group?', '8', '34', '11', '6', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 7, 10-20: 10, 20-30: 5, 30-40: 14, 40-50: 5). How many values are in the 40-50 group?', '8', '41', '3', '5', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 40-50 bar has frequency 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 15, 10-20: 10, 20-30: 7, 30-40: 8, 40-50: 12). How many values are in the 0-10 group?', '13', '18', '52', '15', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 5, 10-20: 4, 20-30: 11, 30-40: 14, 40-50: 15). How many values are in the 30-40 group?', '12', '14', '17', '49', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 30-40 bar has frequency 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 3, 10-20: 7, 20-30: 8, 30-40: 14, 40-50: 14). How many values are in the 0-10 group?', '3', '46', '1', '6', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 7, 10-20: 5, 20-30: 15, 30-40: 11, 40-50: 8). How many values are in the 0-10 group?', '7', '46', '10', '5', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 0-10 bar has frequency 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows (0-10: 11, 10-20: 6, 20-30: 7, 30-40: 13, 40-50: 9). How many values are in the 40-50 group?', '7', '12', '46', '9', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Reading from the histogram, the 40-50 bar has frequency 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 11, 12, 8, 8, 7. How many data values are there in total?', '46', '39', '12', '51', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 11 + 12 + 8 + 8 + 7 = 46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 6, 12, 6, 4, 12. How many data values are there in total?', '12', '36', '45', '40', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 6 + 12 + 6 + 4 + 12 = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 8, 4, 9, 8, 9. How many data values are there in total?', '43', '9', '38', '34', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 8 + 4 + 9 + 8 + 9 = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 10, 6, 5, 7, 10. How many data values are there in total?', '33', '38', '10', '43', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 10 + 6 + 5 + 7 + 10 = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 10, 12, 9, 11, 11. How many data values are there in total?', '58', '53', '12', '44', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 10 + 12 + 9 + 11 + 11 = 53', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 8, 7, 11, 6, 9. How many data values are there in total?', '11', '46', '35', '41', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 8 + 7 + 11 + 6 + 9 = 41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 6, 6, 6, 12, 10. How many data values are there in total?', '34', '45', '40', '12', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 6 + 6 + 6 + 12 + 10 = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 7, 5, 10, 4, 5. How many data values are there in total?', '27', '10', '36', '31', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 7 + 5 + 10 + 4 + 5 = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 10, 8, 11, 4, 5. How many data values are there in total?', '43', '11', '38', '34', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 10 + 8 + 11 + 4 + 5 = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 10, 12, 5, 4, 10. How many data values are there in total?', '37', '46', '41', '12', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 10 + 12 + 5 + 4 + 10 = 41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 4, 5, 5, 12, 5. How many data values are there in total?', '31', '36', '27', '12', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 4 + 5 + 5 + 12 + 5 = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 7, 6, 5, 12, 7. How many data values are there in total?', '42', '12', '32', '37', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 7 + 6 + 5 + 12 + 7 = 37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 11, 12, 8, 8, 5. How many data values are there in total?', '49', '44', '39', '12', 1,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 11 + 12 + 8 + 8 + 5 = 44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 7, 6, 5, 9, 11. How many data values are there in total?', '43', '11', '33', '38', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 7 + 6 + 5 + 9 + 11 = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram has 5 bars with frequencies: 5, 9, 5, 10, 11. How many data values are there in total?', '45', '35', '40', '11', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'Total = 5 + 9 + 5 + 10 + 11 = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 4, 10-20: 13, 20-30: 5, 30-40: 5, 40-50: 6), identify the modal class.', '13', '20-30', '10-20', '0-10', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 10-20 with the highest frequency (13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 11, 10-20: 11, 20-30: 7, 30-40: 15, 40-50: 12), identify the modal class.', '30-40', '15', '20-30', '40-50', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 30-40 with the highest frequency (15)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 3, 10-20: 8, 20-30: 3, 30-40: 11, 40-50: 12), identify the modal class.', '30-40', '0-10', '40-50', '12', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 40-50 with the highest frequency (12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 5, 10-20: 15, 20-30: 14, 30-40: 5, 40-50: 11), identify the modal class.', '20-30', '15', '10-20', '0-10', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 10-20 with the highest frequency (15)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 11, 10-20: 7, 20-30: 4, 30-40: 15, 40-50: 13), identify the modal class.', '40-50', '20-30', '15', '30-40', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 30-40 with the highest frequency (15)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 11, 10-20: 13, 20-30: 11, 30-40: 6, 40-50: 7), identify the modal class.', '10-20', '20-30', '13', '0-10', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 10-20 with the highest frequency (13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 5, 10-20: 5, 20-30: 12, 30-40: 11, 40-50: 13), identify the modal class.', '40-50', '0-10', '30-40', '13', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 40-50 with the highest frequency (13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 9, 10-20: 6, 20-30: 11, 30-40: 13, 40-50: 14), identify the modal class.', '40-50', '0-10', '14', '30-40', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 40-50 with the highest frequency (14)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 14, 10-20: 4, 20-30: 9, 30-40: 5, 40-50: 13), identify the modal class.', '0-10', '10-20', '40-50', '14', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 0-10 with the highest frequency (14)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 15, 10-20: 13, 20-30: 8, 30-40: 12, 40-50: 11), identify the modal class.', '15', '10-20', '40-50', '0-10', 3,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 0-10 with the highest frequency (15)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 3, 10-20: 12, 20-30: 8, 30-40: 4, 40-50: 3), identify the modal class.', '10-20', '12', '0-10', '20-30', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 10-20 with the highest frequency (12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 15, 10-20: 10, 20-30: 3, 30-40: 13, 40-50: 15), identify the modal class.', '0-10', '15', '40-50', '10-20', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 0-10 with the highest frequency (15)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 15, 10-20: 5, 20-30: 11, 30-40: 13, 40-50: 10), identify the modal class.', '40-50', '10-20', '0-10', '15', 2,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 0-10 with the highest frequency (15)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 11, 10-20: 11, 20-30: 10, 30-40: 13, 40-50: 10), identify the modal class.', '30-40', '13', '40-50', '20-30', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 30-40 with the highest frequency (13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the histogram (0-10: 7, 10-20: 9, 20-30: 10, 30-40: 6, 40-50: 6), identify the modal class.', '20-30', '10-20', '30-40', '10', 0,
'lc_ol_statistics', 6, 'developing', 'lc_ol', 'The modal class is 20-30 with the highest frequency (10)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 2 has leaves: 0 1 3 4 9. What is the largest value?', 'Cannot determine', '20', '29', '39', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 2 with leaf 9 gives 29 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 3 has leaves: 1 3 4 5 6 9. What is the largest value?', '31', '49', '30', '39', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 3 with leaf 9 gives 39 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 5 has leaves: 1 2 4 6 9. What is the largest value?', '50', '51', '69', '59', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 5 with leaf 9 gives 59 = 59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 4 has leaves: 0 2 4 6 8. What is the largest value?', '58', '40', 'Cannot determine', '48', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 4 with leaf 8 gives 48 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 3 has leaves: 1 3 4 6 7 9. What is the largest value?', '39', '49', '31', '30', 0,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 3 with leaf 9 gives 39 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 5 has leaves: 0 4 5 7 8 9. What is the largest value?', 'Cannot determine', '69', '59', '50', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 5 with leaf 9 gives 59 = 59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 3 has leaves: 2 3 4 6 8 9. What is the largest value?', '49', '39', '30', '32', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 3 with leaf 9 gives 39 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 4 has leaves: 0 1 2 6 7 8. What is the largest value?', '58', 'Cannot determine', '40', '48', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 4 with leaf 8 gives 48 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 4 has leaves: 0 2 6 7 9. What is the largest value?', '40', 'Cannot determine', '59', '49', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 4 with leaf 9 gives 49 = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 3 has leaves: 0 1 3 5 7 9. What is the largest value?', '30', '39', '49', 'Cannot determine', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 3 with leaf 9 gives 39 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 4 has leaves: 3 4 8 9. What is the largest value?', '40', '59', '49', '43', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 4 with leaf 9 gives 49 = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 4 has leaves: 2 5 6 7 8. What is the largest value?', '42', '48', '40', '58', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 4 with leaf 8 gives 48 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 5 has leaves: 3 4 5 6 8. What is the largest value?', '68', '58', '53', '50', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 5 with leaf 8 gives 58 = 58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 4 has leaves: 1 3 4 8 9. What is the largest value?', '59', '40', '41', '49', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 4 with leaf 9 gives 49 = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 4 has leaves: 1 6 7 8 9. What is the largest value?', '59', '40', '49', '41', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 4 with leaf 9 gives 49 = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 3 has leaves: 0 3 5 8 9. What is the largest value?', '30', '39', 'Cannot determine', '49', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 3 with leaf 9 gives 39 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 2 has leaves: 0 1 4 5 8. What is the largest value?', '38', '20', 'Cannot determine', '28', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 2 with leaf 8 gives 28 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 5 has leaves: 2 3 4 5 8 9. What is the largest value?', '52', '59', '50', '69', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 5 with leaf 9 gives 59 = 59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 2 has leaves: 0 3 5 6. What is the largest value?', 'Cannot determine', '26', '20', '36', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 2 with leaf 6 gives 26 = 26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a stem-and-leaf plot, stem 3 has leaves: 0 2 4 6. What is the largest value?', '46', '36', '30', 'Cannot determine', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Stem 3 with leaf 6 gives 36 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 0 2 4; Stem 3: 0; Stem 4: 4 9; Stem 5: 5 6 7. Find the median.', '43', '45', '44', '30', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 20, 22, 24, 30, 44, 49, 55, 56, 57. Median = 44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 3: 2 2 6 6 8; Stem 4: 2 6; Stem 5: 1 6. Find the median.', '39', '38', '36', '37', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 32, 32, 36, 36, 38, 42, 46, 51, 56. Median = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 3: 1 3; Stem 4: 3 7 8; Stem 5: 3 3 5 9. Find the median.', '49', '47', 'Cannot determine', '48', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 31, 33, 43, 47, 48, 53, 53, 55, 59. Median = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 6 7 8; Stem 3: 2 5 5; Stem 4: 3; Stem 5: 3 9. Find the median.', '35', '32', '34', '36', 0,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 26, 27, 28, 32, 35, 35, 43, 53, 59. Median = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 7 7; Stem 3: 1 7; Stem 4: 3; Stem 5: 0 2 3 7. Find the median.', '43', '42', '44', '37', 0,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 27, 27, 31, 37, 43, 50, 52, 53, 57. Median = 43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 0; Stem 3: 1 3 7 8; Stem 4: 0; Stem 5: 7 8 9. Find the median.', 'Cannot determine', '37', '39', '38', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 20, 31, 33, 37, 38, 40, 57, 58, 59. Median = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 6; Stem 3: 3; Stem 4: 2 7 9; Stem 5: 4 5 7 9. Find the median.', '48', '49', '47', '50', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 26, 33, 42, 47, 49, 54, 55, 57, 59. Median = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 0; Stem 3: 3 8; Stem 4: 2 6; Stem 5: 1 2 7 9. Find the median.', '47', '46', '45', '42', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 20, 33, 38, 42, 46, 51, 52, 57, 59. Median = 46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 6; Stem 3: 1 3 5; Stem 4: 0 5 7; Stem 5: 3 9. Find the median.', '39', '40', '41', '35', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 26, 31, 33, 35, 40, 45, 47, 53, 59. Median = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 4; Stem 3: 7 7 9; Stem 4: 0 4 5 8; Stem 5: 8. Find the median.', 'Cannot determine', '40', '41', '39', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 24, 37, 37, 39, 40, 44, 45, 48, 58. Median = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 7; Stem 3: 3 6 7; Stem 4: 4 6 7; Stem 5: 4 9. Find the median.', '45', '44', '43', '37', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 27, 33, 36, 37, 44, 46, 47, 54, 59. Median = 44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 0 8 9; Stem 3: 0 1 4 6; Stem 4: 0 3. Find the median.', '32', '30', 'Cannot determine', '31', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 20, 28, 29, 30, 31, 34, 36, 40, 43. Median = 31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 3 6; Stem 3: 0 0 2 6 9; Stem 4: 2; Stem 5: 9. Find the median.', '33', '31', '30', '32', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 23, 26, 30, 30, 32, 36, 39, 42, 59. Median = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 2 7; Stem 3: 6 6 9; Stem 4: 0 6; Stem 5: 4 4. Find the median.', '39', '36', '40', '38', 0,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 22, 27, 36, 36, 39, 40, 46, 54, 54. Median = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A stem-leaf plot shows: Stem 2: 1 7 8 9; Stem 3: 7 9; Stem 4: 5 7; Stem 5: 2. Find the median.', '29', '37', '38', '36', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', '9 values, so median is the 5th value. Ordered: 21, 27, 28, 29, 37, 39, 45, 47, 52. Median = 37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|5 6; 2|0 0 4; 4|2 7 7; 5|7 8 8; 6|3. How many data values are there?', '5', '12', '14', '11', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 12 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|5; 2|4; 3|1 3 9; 4|5; 5|3 7 7. How many data values are there?', '11', '9', '8', '5', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 9 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 2|0 2 2; 3|5 9; 4|0 2 8; 5|1 5; 6|1. How many data values are there?', '5', '13', '10', '11', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 11 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 3|4 5 9 9; 4|7 9; 6|1 4. How many data values are there?', '8', '10', '7', '3', 0,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 8 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|5 6 7; 2|2 8; 3|1 1 9; 4|3 8; 5|6 7. How many data values are there?', '5', '14', '11', '12', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 12 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 2|2 9; 4|0 0 2 4 8; 5|4 6; 6|0. How many data values are there?', '9', '10', '4', '12', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 10 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 2|0 2 4; 3|0; 4|1 2 3; 5|4 7; 6|4. How many data values are there?', '12', '9', '10', '5', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 10 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|6; 2|0 0 0; 3|5; 4|2 3 3 4; 5|0 5. How many data values are there?', '13', '10', '11', '5', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 11 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 2|3 4 8 8 9; 4|2 7; 5|4; 6|0. How many data values are there?', '11', '4', '9', '8', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 9 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|8; 2|6 9; 3|2 8; 4|6; 5|2 5 5; 6|0 3 4. How many data values are there?', '6', '11', '12', '14', 2,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 12 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|9; 3|1 9; 4|1 2 5 7; 5|2 2 6; 6|1. How many data values are there?', '11', '13', '5', '10', 0,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 11 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|5; 2|0; 3|4; 4|3 3 9; 5|3 3 4; 6|0. How many data values are there?', '10', '12', '6', '9', 0,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 10 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|7; 2|6 7; 3|6; 5|6 7; 6|0 2. How many data values are there?', '10', '8', '7', '5', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 8 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 2|0 3 6; 4|1 3 5; 5|0 3 8; 6|0 4. How many data values are there?', '4', '11', '13', '10', 1,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 11 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Stem-leaf plot: 1|8 9 9; 2|3; 3|5 5; 4|0 0 0; 5|0; 6|0. How many data values are there?', '6', '10', '13', '11', 3,
'lc_ol_statistics', 7, 'proficient', 'lc_ol', 'Count all leaves: 11 data values', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 65, SD = 5. Dataset B has mean 65, SD = 18. Which is more spread out?', 'Both the same (same mean)', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 'Cannot tell without the data', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (18 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 73, SD = 6. Dataset B has mean 73, SD = 16. Which is more spread out?', 'Cannot tell without the data', 'Dataset A (lower SD = more spread)', 'Both the same (same mean)', 'Dataset B (higher SD = more spread)', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (16 > 6) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 80, SD = 3. Dataset B has mean 80, SD = 14. Which is more spread out?', 'Both the same (same mean)', 'Dataset B (higher SD = more spread)', 'Dataset A (lower SD = more spread)', 'Cannot tell without the data', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (14 > 3) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 60, SD = 5. Dataset B has mean 60, SD = 15. Which is more spread out?', 'Dataset A (lower SD = more spread)', 'Cannot tell without the data', 'Both the same (same mean)', 'Dataset B (higher SD = more spread)', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (15 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 80, SD = 7. Dataset B has mean 80, SD = 13. Which is more spread out?', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 'Cannot tell without the data', 'Both the same (same mean)', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (13 > 7) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 69, SD = 5. Dataset B has mean 69, SD = 17. Which is more spread out?', 'Cannot tell without the data', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 'Both the same (same mean)', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (17 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 56, SD = 6. Dataset B has mean 56, SD = 14. Which is more spread out?', 'Dataset B (higher SD = more spread)', 'Both the same (same mean)', 'Cannot tell without the data', 'Dataset A (lower SD = more spread)', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (14 > 6) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 79, SD = 7. Dataset B has mean 79, SD = 19. Which is more spread out?', 'Cannot tell without the data', 'Both the same (same mean)', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (19 > 7) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 77, SD = 5. Dataset B has mean 77, SD = 14. Which is more spread out?', 'Dataset A (lower SD = more spread)', 'Both the same (same mean)', 'Cannot tell without the data', 'Dataset B (higher SD = more spread)', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (14 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 61, SD = 5. Dataset B has mean 61, SD = 20. Which is more spread out?', 'Dataset A (lower SD = more spread)', 'Both the same (same mean)', 'Dataset B (higher SD = more spread)', 'Cannot tell without the data', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (20 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 80, SD = 5. Dataset B has mean 80, SD = 13. Which is more spread out?', 'Both the same (same mean)', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 'Cannot tell without the data', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (13 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 79, SD = 6. Dataset B has mean 79, SD = 15. Which is more spread out?', 'Cannot tell without the data', 'Dataset B (higher SD = more spread)', 'Dataset A (lower SD = more spread)', 'Both the same (same mean)', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (15 > 6) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 53, SD = 6. Dataset B has mean 53, SD = 13. Which is more spread out?', 'Dataset A (lower SD = more spread)', 'Both the same (same mean)', 'Dataset B (higher SD = more spread)', 'Cannot tell without the data', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (13 > 6) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 51, SD = 5. Dataset B has mean 51, SD = 14. Which is more spread out?', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 'Cannot tell without the data', 'Both the same (same mean)', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (14 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 58, SD = 8. Dataset B has mean 58, SD = 18. Which is more spread out?', 'Dataset B (higher SD = more spread)', 'Dataset A (lower SD = more spread)', 'Both the same (same mean)', 'Cannot tell without the data', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (18 > 8) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 74, SD = 3. Dataset B has mean 74, SD = 19. Which is more spread out?', 'Dataset B (higher SD = more spread)', 'Both the same (same mean)', 'Dataset A (lower SD = more spread)', 'Cannot tell without the data', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (19 > 3) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 58, SD = 3. Dataset B has mean 58, SD = 17. Which is more spread out?', 'Dataset B (higher SD = more spread)', 'Dataset A (lower SD = more spread)', 'Both the same (same mean)', 'Cannot tell without the data', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (17 > 3) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 60, SD = 5. Dataset B has mean 60, SD = 14. Which is more spread out?', 'Cannot tell without the data', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 'Both the same (same mean)', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (14 > 5) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 51, SD = 7. Dataset B has mean 51, SD = 16. Which is more spread out?', 'Dataset B (higher SD = more spread)', 'Dataset A (lower SD = more spread)', 'Cannot tell without the data', 'Both the same (same mean)', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (16 > 7) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Dataset A has mean 60, SD = 7. Dataset B has mean 60, SD = 12. Which is more spread out?', 'Dataset A (lower SD = more spread)', 'Dataset B (higher SD = more spread)', 'Cannot tell without the data', 'Both the same (same mean)', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Standard deviation measures spread. Higher SD (12 > 7) means more spread out.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 6, 7, 7, 3 (population SD)', '1.64', '2.69', '5.75', '2.14', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 5.75. Variance = Σ(x-μ)²/n = 2.69. SD = √2.69 = 1.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 3, 9, 9, 6 (population SD)', '6.19', '2.49', '2.99', '6.75', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 6.75. Variance = Σ(x-μ)²/n = 6.19. SD = √6.19 = 2.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 2, 7, 4, 6 (population SD)', '4.75', '3.69', '2.42', '1.92', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 4.75. Variance = Σ(x-μ)²/n = 3.69. SD = √3.69 = 1.92', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 9, 3, 2, 5 (population SD)', '7.19', '4.75', '2.68', '3.18', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 4.75. Variance = Σ(x-μ)²/n = 7.19. SD = √7.19 = 2.68', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 9, 3, 7, 10 (population SD)', '7.25', '3.18', '7.19', '2.68', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 7.25. Variance = Σ(x-μ)²/n = 7.19. SD = √7.19 = 2.68', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 5, 7, 8, 8 (population SD)', '1.5', '1.22', '7.0', '1.72', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 7.0. Variance = Σ(x-μ)²/n = 1.5. SD = √1.5 = 1.22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 3, 5, 9, 4 (population SD)', '5.25', '2.28', '2.78', '5.19', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 5.25. Variance = Σ(x-μ)²/n = 5.19. SD = √5.19 = 2.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 2, 10, 4, 10 (population SD)', '12.75', '6.5', '4.07', '3.57', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 6.5. Variance = Σ(x-μ)²/n = 12.75. SD = √12.75 = 3.57', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 6, 8, 4, 3 (population SD)', '2.42', '1.92', '5.25', '3.69', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 5.25. Variance = Σ(x-μ)²/n = 3.69. SD = √3.69 = 1.92', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 6, 10, 10, 3 (population SD)', '3.45', '8.69', '2.95', '7.25', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 7.25. Variance = Σ(x-μ)²/n = 8.69. SD = √8.69 = 2.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 6, 7, 2, 5 (population SD)', '3.5', '2.37', '5.0', '1.87', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 5.0. Variance = Σ(x-μ)²/n = 3.5. SD = √3.5 = 1.87', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 9, 6, 2, 3 (population SD)', '3.24', '7.5', '2.74', '5.0', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 5.0. Variance = Σ(x-μ)²/n = 7.5. SD = √7.5 = 2.74', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 4, 5, 9, 7 (population SD)', '3.69', '6.25', '2.42', '1.92', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 6.25. Variance = Σ(x-μ)²/n = 3.69. SD = √3.69 = 1.92', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 5, 3, 4, 2 (population SD)', '1.62', '1.12', '1.25', '3.5', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 3.5. Variance = Σ(x-μ)²/n = 1.25. SD = √1.25 = 1.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 10, 7, 4, 7 (population SD)', '7.0', '4.5', '2.62', '2.12', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 7.0. Variance = Σ(x-μ)²/n = 4.5. SD = √4.5 = 2.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 5, 10, 2, 8 (population SD)', '6.25', '9.19', '3.53', '3.03', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 6.25. Variance = Σ(x-μ)²/n = 9.19. SD = √9.19 = 3.03', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 2, 3, 10, 6 (population SD)', '3.61', '9.69', '5.25', '3.11', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 5.25. Variance = Σ(x-μ)²/n = 9.69. SD = √9.69 = 3.11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 8, 7, 10, 9 (population SD)', '1.25', '1.62', '1.12', '8.5', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 8.5. Variance = Σ(x-μ)²/n = 1.25. SD = √1.25 = 1.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 10, 2, 4, 5 (population SD)', '2.95', '8.69', '3.45', '5.25', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 5.25. Variance = Σ(x-μ)²/n = 8.69. SD = √8.69 = 2.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the standard deviation of: 7, 9, 5, 8 (population SD)', '1.98', '1.48', '7.25', '2.19', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Mean = 7.25. Variance = Σ(x-μ)²/n = 2.19. SD = √2.19 = 1.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 10. If 12 is added to every value, what is the new SD?', '20', '22', '10', '2', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 10.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 11. If 17 is added to every value, what is the new SD?', '6', '11', '22', '28', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 11.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 11. If 12 is added to every value, what is the new SD?', '11', '23', '22', '1', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 11.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 13. If 8 is added to every value, what is the new SD?', '21', '13', '26', '5', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 13.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 9. If 17 is added to every value, what is the new SD?', '9', '26', '18', '8', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 9.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 13. If 8 is added to every value, what is the new SD?', '21', '13', '26', '5', 1,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 13.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 14. If 14 is added to every value, what is the new SD?', '28', '0', 'Cannot determine', '14', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 14.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 13. If 18 is added to every value, what is the new SD?', '26', '31', '13', '5', 2,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 13.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 6. If 8 is added to every value, what is the new SD?', '14', '12', '2', '6', 3,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 9. If 7 is added to every value, what is the new SD?', '9', '18', '2', '16', 0,
'lc_ol_statistics', 8, 'proficient', 'lc_ol', 'Adding a constant shifts all values but doesn''t change the spread. SD stays 9.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 12, 11, 8, 8, 12. What is the cumulative frequency after group 2?', '35', '51', '23', '11', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 12 + 11 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 6, 3, 5, 11, 5. What is the cumulative frequency after group 5?', '36', 'Cannot determine', '5', '30', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 6 + 3 + 5 + 11 + 5 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 11, 5, 4, 7, 7. What is the cumulative frequency after group 5?', '45', 'Cannot determine', '7', '34', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 11 + 5 + 4 + 7 + 7 = 34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 9, 12, 9, 9, 3. What is the cumulative frequency after group 4?', '48', '9', '42', '39', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 9 + 12 + 9 + 9 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 6, 7, 9, 8, 11. What is the cumulative frequency after group 5?', 'Cannot determine', '47', '11', '41', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 6 + 7 + 9 + 8 + 11 = 41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 4, 11, 6, 8, 4. What is the cumulative frequency after group 4?', '29', '33', '8', 'Cannot determine', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 4 + 11 + 6 + 8 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 10, 5, 8, 4, 6. What is the cumulative frequency after group 5?', 'Cannot determine', '33', '6', '43', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 10 + 5 + 8 + 4 + 6 = 33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 7, 9, 10, 12, 11. What is the cumulative frequency after group 5?', '49', '56', '11', 'Cannot determine', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 7 + 9 + 10 + 12 + 11 = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 7, 8, 10, 5, 8. What is the cumulative frequency after group 4?', '30', '5', '38', '37', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 7 + 8 + 10 + 5 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 9, 3, 6, 6, 8. What is the cumulative frequency after group 4?', '32', '24', '6', '33', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 9 + 3 + 6 + 6 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 10, 10, 10, 3, 10. What is the cumulative frequency after group 2?', '10', '30', '43', '20', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 10 + 10 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 5, 3, 10, 10, 4. What is the cumulative frequency after group 2?', '13', '32', '3', '8', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 5 + 3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 6, 6, 4, 11, 3. What is the cumulative frequency after group 3?', '16', '30', '22', '4', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 6 + 6 + 4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 5, 12, 8, 7, 8. What is the cumulative frequency after group 2?', '40', '17', '12', '22', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 5 + 12 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 4, 4, 11, 4, 8. What is the cumulative frequency after group 4?', '27', '31', '4', '23', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 4 + 4 + 11 + 4 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 6, 5, 7, 9, 5. What is the cumulative frequency after group 3?', '24', '32', '7', '18', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 6 + 5 + 7 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 7, 11, 11, 6, 6. What is the cumulative frequency after group 5?', '48', '6', '41', 'Cannot determine', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 7 + 11 + 11 + 6 + 6 = 41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 3, 4, 3, 12, 8. What is the cumulative frequency after group 4?', '12', '30', '22', '25', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 3 + 4 + 3 + 12 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 11, 8, 9, 7, 6. What is the cumulative frequency after group 4?', '35', '46', '41', '7', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 11 + 8 + 9 + 7 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies: 7, 4, 11, 11, 12. What is the cumulative frequency after group 5?', '52', 'Cannot determine', '45', '12', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Cumulative = 7 + 4 + 11 + 11 + 12 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 13, 21, 33, 39, 46 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', 'Cannot determine', '10-20', '30-40', '20-30', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 46. Median position = 23.0. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 15, 22, 32, 44, 59 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', 'Cannot determine', '20-30', '30-40', '10-20', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 59. Median position = 29.5. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 6, 12, 25, 31, 36 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', 'Cannot determine', '20-30', '10-20', '30-40', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 36. Median position = 18.0. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 7, 15, 22, 27, 41 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '10-20', 'Cannot determine', '30-40', '20-30', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 41. Median position = 20.5. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 6, 15, 24, 34, 44 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', 'Cannot determine', '20-30', '10-20', '30-40', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 44. Median position = 22.0. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 9, 16, 27, 35, 45 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', 'Cannot determine', '30-40', '10-20', '20-30', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 45. Median position = 22.5. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 10, 20, 35, 48, 62 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', 'Cannot determine', '30-40', '10-20', '20-30', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 62. Median position = 31.0. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 6, 19, 26, 34, 49 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '20-30', '10-20', 'Cannot determine', '30-40', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 49. Median position = 24.5. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 5, 10, 18, 33, 45 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '40-50', '20-30', 'Cannot determine', '30-40', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 45. Median position = 22.5. Median class is 30-40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 6, 16, 21, 29, 44 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '20-30', '40-50', 'Cannot determine', '30-40', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 44. Median position = 22.0. Median class is 30-40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 12, 17, 23, 36, 47 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '20-30', '30-40', '40-50', 'Cannot determine', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 47. Median position = 23.5. Median class is 30-40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 10, 23, 30, 38, 53 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '20-30', 'Cannot determine', '30-40', '10-20', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 53. Median position = 26.5. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 14, 20, 26, 38, 53 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '40-50', '30-40', '20-30', 'Cannot determine', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 53. Median position = 26.5. Median class is 30-40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 7, 16, 21, 33, 43 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '40-50', '30-40', 'Cannot determine', '20-30', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 43. Median position = 21.5. Median class is 30-40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cumulative frequencies: 8, 18, 32, 38, 49 for groups 0-10, 10-20, 20-30, 30-40, 40-50. Which is the median class?', '10-20', 'Cannot determine', '20-30', '30-40', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', 'Total = 49. Median position = 24.5. Median class is 20-30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 40 data points. At what cumulative frequency is the 50th percentile?', '40', '50', '20', '24', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '50th percentile position = 50% of 40 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 100 data points. At what cumulative frequency is the 50th percentile?', '50', 'Cannot determine', '60', '100', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '50th percentile position = 50% of 100 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 40 data points. At what cumulative frequency is the 25th percentile?', '25', '10', '14', '40', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '25th percentile position = 25% of 40 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 60 data points. At what cumulative frequency is the 75th percentile?', '51', '60', '45', '75', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '75th percentile position = 75% of 60 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 50 data points. At what cumulative frequency is the 25th percentile?', '25', '17', '50', '12', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '25th percentile position = 25% of 50 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 50 data points. At what cumulative frequency is the 75th percentile?', '42', '50', '37', '75', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '75th percentile position = 75% of 50 = 37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 40 data points. At what cumulative frequency is the 25th percentile?', '40', '14', '10', '25', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '25th percentile position = 25% of 40 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 80 data points. At what cumulative frequency is the 25th percentile?', '20', '80', '28', '25', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '25th percentile position = 25% of 80 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 80 data points. At what cumulative frequency is the 50th percentile?', '40', '48', '80', '50', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '50th percentile position = 50% of 80 = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 80 data points. At what cumulative frequency is the 75th percentile?', '80', '75', '68', '60', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '75th percentile position = 75% of 80 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 60 data points. At what cumulative frequency is the 75th percentile?', '45', '60', '75', '51', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '75th percentile position = 75% of 60 = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 50 data points. At what cumulative frequency is the 50th percentile?', '25', 'Cannot determine', '30', '50', 0,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '50th percentile position = 50% of 50 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 40 data points. At what cumulative frequency is the 25th percentile?', '40', '10', '14', '25', 1,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '25th percentile position = 25% of 40 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 50 data points. At what cumulative frequency is the 75th percentile?', '75', '50', '37', '42', 2,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '75th percentile position = 75% of 50 = 37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cumulative frequency diagram has 40 data points. At what cumulative frequency is the 50th percentile?', '40', '24', '50', '20', 3,
'lc_ol_statistics', 9, 'proficient', 'lc_ol', '50th percentile position = 50% of 40 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 70 and SD 12. What percentage lies within 1 SD of the mean?', '99.7%', '95%', '68%', '50%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 58 and 82)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 80 and SD 15. What percentage lies within 1 SD of the mean?', '99.7%', '50%', '95%', '68%', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 65 and 95)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 70 and SD 10. What percentage lies within 1 SD of the mean?', '99.7%', '95%', '50%', '68%', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 60 and 80)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 60 and SD 5. What percentage lies within 1 SD of the mean?', '99.7%', '95%', '50%', '68%', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 55 and 65)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 100 and SD 10. What percentage lies within 1 SD of the mean?', '95%', '68%', '50%', '99.7%', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 90 and 110)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 100 and SD 8. What percentage lies within 1 SD of the mean?', '68%', '95%', '99.7%', '50%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 92 and 108)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 50 and SD 8. What percentage lies within 1 SD of the mean?', '68%', '50%', '99.7%', '95%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 42 and 58)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 100 and SD 5. What percentage lies within 1 SD of the mean?', '95%', '50%', '68%', '99.7%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 95 and 105)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 70 and SD 5. What percentage lies within 1 SD of the mean?', '50%', '68%', '95%', '99.7%', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 65 and 75)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 60 and SD 5. What percentage lies within 1 SD of the mean?', '99.7%', '95%', '68%', '50%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 55 and 65)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 70 and SD 8. What percentage lies within 1 SD of the mean?', '68%', '99.7%', '95%', '50%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 62 and 78)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 80 and SD 10. What percentage lies within 1 SD of the mean?', '50%', '99.7%', '68%', '95%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 70 and 90)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 70 and SD 10. What percentage lies within 1 SD of the mean?', '95%', '99.7%', '50%', '68%', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 60 and 80)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 50 and SD 12. What percentage lies within 1 SD of the mean?', '99.7%', '95%', '68%', '50%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 38 and 62)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 60 and SD 5. What percentage lies within 1 SD of the mean?', '68%', '99.7%', '50%', '95%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 55 and 65)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 60 and SD 15. What percentage lies within 1 SD of the mean?', '68%', '95%', '50%', '99.7%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 45 and 75)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 50 and SD 10. What percentage lies within 1 SD of the mean?', '95%', '99.7%', '50%', '68%', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 40 and 60)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 50 and SD 12. What percentage lies within 1 SD of the mean?', '95%', '99.7%', '68%', '50%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 38 and 62)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 100 and SD 10. What percentage lies within 1 SD of the mean?', '50%', '95%', '68%', '99.7%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 90 and 110)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data is normally distributed with mean 100 and SD 10. What percentage lies within 1 SD of the mean?', '95%', '68%', '50%', '99.7%', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'By the Empirical Rule, 68% of data lies within 1 SD (between 90 and 110)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 50, SD = 10. What percentage lies between 30 and 70?', '99.7%', '50%', '68%', '95%', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±2 SD. By Empirical Rule, 95% lies within 2 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 70, SD = 5. What percentage lies between 55 and 85?', '50%', '99.7%', '68%', '95%', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 80, SD = 5. What percentage lies between 65 and 95?', '68%', '50%', '99.7%', '95%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 100, SD = 10. What percentage lies between 80 and 120?', '99.7%', '50%', '95%', '68%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±2 SD. By Empirical Rule, 95% lies within 2 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 70, SD = 12. What percentage lies between 34 and 106?', '50%', '95%', '99.7%', '68%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 50, SD = 8. What percentage lies between 26 and 74?', '50%', '99.7%', '95%', '68%', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 80, SD = 8. What percentage lies between 64 and 96?', '68%', '95%', '50%', '99.7%', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±2 SD. By Empirical Rule, 95% lies within 2 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 70, SD = 10. What percentage lies between 40 and 100?', '95%', '99.7%', '68%', '50%', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 70, SD = 5. What percentage lies between 60 and 80?', '68%', '99.7%', '95%', '50%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±2 SD. By Empirical Rule, 95% lies within 2 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 80, SD = 5. What percentage lies between 70 and 90?', '95%', '99.7%', '68%', '50%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±2 SD. By Empirical Rule, 95% lies within 2 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 60, SD = 10. What percentage lies between 30 and 90?', '99.7%', '50%', '68%', '95%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 50, SD = 5. What percentage lies between 35 and 65?', '50%', '68%', '99.7%', '95%', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 50, SD = 8. What percentage lies between 34 and 66?', '95%', '68%', '50%', '99.7%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±2 SD. By Empirical Rule, 95% lies within 2 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 100, SD = 8. What percentage lies between 76 and 124?', '99.7%', '68%', '50%', '95%', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±3 SD. By Empirical Rule, 99.7% lies within 3 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 100, SD = 8. What percentage lies between 84 and 116?', '50%', '99.7%', '68%', '95%', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', 'Range is ±2 SD. By Empirical Rule, 95% lies within 2 SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 150, SD = 25. Find the range containing 68% of the data.', '125 to 175', '150 to 175', '100 to 200', 'Cannot determine', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '68% within 1 SD: 150 ± 1×25 = 125 to 175', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 150, SD = 10. Find the range containing 95% of the data.', '140 to 160', '120 to 180', '150 to 170', '130 to 170', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 150 ± 2×10 = 130 to 170', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 100, SD = 15. Find the range containing 95% of the data.', '55 to 145', '85 to 115', '70 to 130', '100 to 130', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 100 ± 2×15 = 70 to 130', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 200, SD = 25. Find the range containing 95% of the data.', '125 to 275', '175 to 225', '150 to 250', '200 to 250', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 200 ± 2×25 = 150 to 250', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 150, SD = 15. Find the range containing 68% of the data.', '135 to 165', 'Cannot determine', '120 to 180', '150 to 165', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '68% within 1 SD: 150 ± 1×15 = 135 to 165', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 150, SD = 10. Find the range containing 95% of the data.', '120 to 180', '130 to 170', '140 to 160', '150 to 170', 1,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 150 ± 2×10 = 130 to 170', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 200, SD = 15. Find the range containing 68% of the data.', '185 to 215', 'Cannot determine', '170 to 230', '200 to 215', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '68% within 1 SD: 200 ± 1×15 = 185 to 215', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 100, SD = 25. Find the range containing 68% of the data.', '75 to 125', '100 to 125', '50 to 150', 'Cannot determine', 0,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '68% within 1 SD: 100 ± 1×25 = 75 to 125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 150, SD = 20. Find the range containing 68% of the data.', '110 to 190', '150 to 170', '130 to 170', 'Cannot determine', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '68% within 1 SD: 150 ± 1×20 = 130 to 170', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 200, SD = 15. Find the range containing 68% of the data.', '200 to 215', '170 to 230', 'Cannot determine', '185 to 215', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '68% within 1 SD: 200 ± 1×15 = 185 to 215', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 200, SD = 25. Find the range containing 95% of the data.', '200 to 250', '125 to 275', '150 to 250', '175 to 225', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 200 ± 2×25 = 150 to 250', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 150, SD = 15. Find the range containing 68% of the data.', '120 to 180', 'Cannot determine', '150 to 165', '135 to 165', 3,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '68% within 1 SD: 150 ± 1×15 = 135 to 165', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 200, SD = 10. Find the range containing 95% of the data.', '170 to 230', '190 to 210', '180 to 220', '200 to 220', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 200 ± 2×10 = 180 to 220', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 150, SD = 10. Find the range containing 95% of the data.', '120 to 180', '140 to 160', '130 to 170', '150 to 170', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 150 ± 2×10 = 130 to 170', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mean = 100, SD = 10. Find the range containing 95% of the data.', '70 to 130', '90 to 110', '80 to 120', '100 to 120', 2,
'lc_ol_statistics', 10, 'advanced', 'lc_ol', '95% within 2 SD: 100 ± 2×10 = 80 to 120', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.3. Describe the relationship.', 'Weak positive', 'Strong positive', 'Moderate positive', 'Strong negative', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.3 indicates weak positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.1. Describe the relationship.', 'Strong negative', 'Very weak positive', 'Strong positive', 'Moderate positive', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.1 indicates very weak positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.3. Describe the relationship.', 'Strong negative', 'Weak negative', 'Strong positive', 'Moderate positive', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.3 indicates weak negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.1. Describe the relationship.', 'Strong positive', 'Strong negative', 'Very weak positive', 'Moderate positive', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.1 indicates very weak positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.3. Describe the relationship.', 'Weak negative', 'Strong negative', 'Strong positive', 'Moderate positive', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.3 indicates weak negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.6. Describe the relationship.', 'Moderate positive', 'Strong negative', 'Moderate negative', 'Strong positive', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.6 indicates moderate positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.3. Describe the relationship.', 'Moderate positive', 'Strong positive', 'Strong negative', 'Weak positive', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.3 indicates weak positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.3. Describe the relationship.', 'Strong negative', 'Strong positive', 'Moderate positive', 'Weak positive', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.3 indicates weak positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.85. Describe the relationship.', 'Moderate positive', 'Strong negative', 'Strong positive', 'Moderate negative', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.85 indicates strong negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.85. Describe the relationship.', 'Strong negative', 'Moderate negative', 'Strong positive', 'Moderate positive', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.85 indicates strong negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.95. Describe the relationship.', 'Moderate positive', 'Strong negative', 'Moderate negative', 'Strong positive', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.95 indicates strong negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.85. Describe the relationship.', 'Moderate positive', 'Strong positive', 'Moderate negative', 'Strong negative', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.85 indicates strong negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.95. Describe the relationship.', 'Moderate negative', 'Moderate positive', 'Strong negative', 'Strong positive', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.95 indicates strong positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.3. Describe the relationship.', 'Strong positive', 'Moderate positive', 'Weak positive', 'Strong negative', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.3 indicates weak positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.6. Describe the relationship.', 'Moderate negative', 'Strong negative', 'Moderate positive', 'Strong positive', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.6 indicates moderate positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.3. Describe the relationship.', 'Moderate positive', 'Strong negative', 'Strong positive', 'Weak negative', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.3 indicates weak negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.95. Describe the relationship.', 'Strong negative', 'Moderate negative', 'Strong positive', 'Moderate positive', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.95 indicates strong negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.95. Describe the relationship.', 'Moderate negative', 'Strong positive', 'Moderate positive', 'Strong negative', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.95 indicates strong negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.6. Describe the relationship.', 'Strong positive', 'Moderate positive', 'Moderate negative', 'Strong negative', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.6 indicates moderate positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.95. Describe the relationship.', 'Strong negative', 'Strong positive', 'Moderate positive', 'Moderate negative', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.95 indicates strong positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.1. Describe the relationship.', 'Strong positive', 'Very weak positive', 'Moderate positive', 'Strong negative', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.1 indicates very weak positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = -0.6. Describe the relationship.', 'Strong negative', 'Moderate positive', 'Strong positive', 'Moderate negative', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = -0.6 indicates moderate negative correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.85. Describe the relationship.', 'Strong positive', 'Moderate positive', 'Strong negative', 'Moderate negative', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.85 indicates strong positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.95. Describe the relationship.', 'Moderate positive', 'Strong negative', 'Moderate negative', 'Strong positive', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.95 indicates strong positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A correlation coefficient r = 0.95. Describe the relationship.', 'Strong positive', 'Strong negative', 'Moderate positive', 'Moderate negative', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'r = 0.95 indicates strong positive correlation. Closer to ±1 = stronger, closer to 0 = weaker.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.3. Is this valid?', 'Yes, but it''s unusual', 'No, r must be between -1 and 1', 'Yes, this is a strong correlation', 'No, r must be positive', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.3 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.8. Is this valid?', 'No, r must be positive', 'Yes, this is a strong correlation', 'No, r must be between -1 and 1', 'Yes, but it''s unusual', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.8 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.3. Is this valid?', 'No, r must be positive', 'Yes, but it''s unusual', 'No, r must be between -1 and 1', 'Yes, this is a strong correlation', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.3 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = 5. Is this valid?', 'No, r must be positive', 'Yes, this is a strong correlation', 'Yes, but it''s unusual', 'No, r must be between -1 and 1', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = 5 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.3. Is this valid?', 'Yes, but it''s unusual', 'Yes, this is a strong correlation', 'No, r must be between -1 and 1', 'No, r must be positive', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.3 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.8. Is this valid?', 'Yes, but it''s unusual', 'No, r must be positive', 'No, r must be between -1 and 1', 'Yes, this is a strong correlation', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.8 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.3. Is this valid?', 'Yes, this is a strong correlation', 'Yes, but it''s unusual', 'No, r must be positive', 'No, r must be between -1 and 1', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.3 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = 2. Is this valid?', 'No, r must be between -1 and 1', 'Yes, but it''s unusual', 'Yes, this is a strong correlation', 'No, r must be positive', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = 2 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = 2. Is this valid?', 'Yes, this is a strong correlation', 'No, r must be between -1 and 1', 'Yes, but it''s unusual', 'No, r must be positive', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = 2 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = 2. Is this valid?', 'No, r must be positive', 'Yes, this is a strong correlation', 'Yes, but it''s unusual', 'No, r must be between -1 and 1', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = 2 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = 1.2. Is this valid?', 'Yes, but it''s unusual', 'No, r must be positive', 'Yes, this is a strong correlation', 'No, r must be between -1 and 1', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = 1.2 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = 1.5. Is this valid?', 'No, r must be between -1 and 1', 'Yes, but it''s unusual', 'No, r must be positive', 'Yes, this is a strong correlation', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = 1.5 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.3. Is this valid?', 'Yes, but it''s unusual', 'No, r must be positive', 'Yes, this is a strong correlation', 'No, r must be between -1 and 1', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.3 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = 2. Is this valid?', 'Yes, this is a strong correlation', 'Yes, but it''s unusual', 'No, r must be positive', 'No, r must be between -1 and 1', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = 2 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A student calculated r = -1.3. Is this valid?', 'Yes, but it''s unusual', 'Yes, this is a strong correlation', 'No, r must be between -1 and 1', 'No, r must be positive', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = -1.3 is invalid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Ice cream sales and drowning rates both increase in summer. Does this prove causation?', 'Yes, correlation always means causation', 'Yes, the data proves it', 'Cannot determine from correlation', 'No - both caused by hot weather (confounding variable)', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Study time and test scores show positive correlation. Does this prove causation?', 'Cannot determine from correlation', 'Yes, the data proves it', 'Yes, correlation always means causation', 'Possibly - but other factors may contribute', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Shoe size and reading ability correlate in children. Does this prove causation?', 'Cannot determine from correlation', 'Yes, correlation always means causation', 'Yes, the data proves it', 'No - both increase with age (confounding variable)', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Smoking and lung cancer show strong correlation. Does this prove causation?', 'Correlation suggests relationship but doesn''t prove causation directly', 'Yes, the data proves it', 'Cannot determine from correlation', 'Yes, correlation always means causation', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Number of firefighters and fire damage correlate. Does this prove causation?', 'Yes, correlation always means causation', 'Cannot determine from correlation', 'No - larger fires need more firefighters (reverse causation)', 'Yes, the data proves it', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Ice cream sales and drowning rates both increase in summer. Does this prove causation?', 'Yes, correlation always means causation', 'No - both caused by hot weather (confounding variable)', 'Yes, the data proves it', 'Cannot determine from correlation', 1,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Study time and test scores show positive correlation. Does this prove causation?', 'Possibly - but other factors may contribute', 'Yes, the data proves it', 'Cannot determine from correlation', 'Yes, correlation always means causation', 0,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Shoe size and reading ability correlate in children. Does this prove causation?', 'Cannot determine from correlation', 'Yes, correlation always means causation', 'No - both increase with age (confounding variable)', 'Yes, the data proves it', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Smoking and lung cancer show strong correlation. Does this prove causation?', 'Yes, the data proves it', 'Yes, correlation always means causation', 'Cannot determine from correlation', 'Correlation suggests relationship but doesn''t prove causation directly', 3,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Number of firefighters and fire damage correlate. Does this prove causation?', 'Yes, correlation always means causation', 'Cannot determine from correlation', 'No - larger fires need more firefighters (reverse causation)', 'Yes, the data proves it', 2,
'lc_ol_statistics', 11, 'advanced', 'lc_ol', 'Correlation does not imply causation. Consider confounding variables and reverse causation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 21, 20, 15, 30, 11. If 30 is added, what is the new mean?', '21.2', '22.2', '19.4', '30', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 127, n = 6. New mean = 21.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 20, 14, 16, 22, 21. If 16 is added, what is the new mean?', '18.2', '16', '18.6', '19.2', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 109, n = 6. New mean = 18.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 19, 29, 18, 10, 16. If 16 is added, what is the new mean?', '18.4', '19.0', '18.0', '16', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 108, n = 6. New mean = 18.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 17, 28, 18, 30, 12. If 12 is added, what is the new mean?', '21.0', '20.5', '19.5', '12', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 117, n = 6. New mean = 19.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 29, 16, 15, 20, 17. If 17 is added, what is the new mean?', '19.0', '20.0', '19.4', '17', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 114, n = 6. New mean = 19.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 18, 25, 21, 24, 18. If 24 is added, what is the new mean?', '24', '21.7', '21.2', '22.7', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 130, n = 6. New mean = 21.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 10, 12, 18, 17, 10. If 18 is added, what is the new mean?', '15.2', '13.4', '14.2', '18', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 85, n = 6. New mean = 14.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 15, 22, 22, 12, 17. If 15 is added, what is the new mean?', '18.2', '17.2', '15', '17.6', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 103, n = 6. New mean = 17.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 24, 29, 11, 21, 23. If 21 is added, what is the new mean?', '22.5', '21.6', '21', '21.5', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 129, n = 6. New mean = 21.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 28, 16, 19, 26, 17. If 19 is added, what is the new mean?', '21.2', '19', '21.8', '20.8', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 125, n = 6. New mean = 20.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 15, 15, 25, 23, 16. If 15 is added, what is the new mean?', '18.8', '15', '19.2', '18.2', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 109, n = 6. New mean = 18.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 22, 24, 14, 24, 27. If 14 is added, what is the new mean?', '21.8', '14', '22.2', '20.8', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 125, n = 6. New mean = 20.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 22, 25, 27, 10, 26. If 22 is added, what is the new mean?', '23.0', '22', 'Cannot determine', '22.0', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 132, n = 6. New mean = 22.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 24, 15, 21, 13, 13. If 13 is added, what is the new mean?', '16.5', '13', '17.5', '17.2', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 99, n = 6. New mean = 16.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data: 19, 10, 15, 30, 29. If 29 is added, what is the new mean?', '22.0', '23.0', '29', '20.6', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'New total = 132, n = 6. New mean = 22.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=52, SD=6. Set B: mean=57, SD=12. Which set has more consistent values?', 'Set B (higher SD = more consistent)', 'Set A (lower SD = more consistent)', 'Cannot compare without raw data', 'Same consistency (similar means)', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 6 < 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=67, SD=6. Set B: mean=67, SD=9. Which set has more consistent values?', 'Set B (higher SD = more consistent)', 'Same consistency (similar means)', 'Cannot compare without raw data', 'Set A (lower SD = more consistent)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 6 < 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=64, SD=9. Set B: mean=63, SD=16. Which set has more consistent values?', 'Set B (higher SD = more consistent)', 'Same consistency (similar means)', 'Set A (lower SD = more consistent)', 'Cannot compare without raw data', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 9 < 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=50, SD=9. Set B: mean=51, SD=17. Which set has more consistent values?', 'Same consistency (similar means)', 'Set B (higher SD = more consistent)', 'Cannot compare without raw data', 'Set A (lower SD = more consistent)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 9 < 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=65, SD=10. Set B: mean=70, SD=16. Which set has more consistent values?', 'Set B (higher SD = more consistent)', 'Set A (lower SD = more consistent)', 'Cannot compare without raw data', 'Same consistency (similar means)', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 10 < 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=59, SD=7. Set B: mean=62, SD=13. Which set has more consistent values?', 'Cannot compare without raw data', 'Set B (higher SD = more consistent)', 'Same consistency (similar means)', 'Set A (lower SD = more consistent)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 7 < 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=63, SD=8. Set B: mean=66, SD=12. Which set has more consistent values?', 'Set B (higher SD = more consistent)', 'Set A (lower SD = more consistent)', 'Same consistency (similar means)', 'Cannot compare without raw data', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 8 < 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=59, SD=10. Set B: mean=57, SD=15. Which set has more consistent values?', 'Set A (lower SD = more consistent)', 'Cannot compare without raw data', 'Set B (higher SD = more consistent)', 'Same consistency (similar means)', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 10 < 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=69, SD=10. Set B: mean=69, SD=18. Which set has more consistent values?', 'Cannot compare without raw data', 'Same consistency (similar means)', 'Set B (higher SD = more consistent)', 'Set A (lower SD = more consistent)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 10 < 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=67, SD=5. Set B: mean=66, SD=13. Which set has more consistent values?', 'Cannot compare without raw data', 'Same consistency (similar means)', 'Set A (lower SD = more consistent)', 'Set B (higher SD = more consistent)', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 5 < 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=70, SD=5. Set B: mean=70, SD=9. Which set has more consistent values?', 'Same consistency (similar means)', 'Cannot compare without raw data', 'Set A (lower SD = more consistent)', 'Set B (higher SD = more consistent)', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 5 < 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=68, SD=6. Set B: mean=64, SD=13. Which set has more consistent values?', 'Same consistency (similar means)', 'Cannot compare without raw data', 'Set B (higher SD = more consistent)', 'Set A (lower SD = more consistent)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 6 < 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=63, SD=9. Set B: mean=62, SD=13. Which set has more consistent values?', 'Cannot compare without raw data', 'Set A (lower SD = more consistent)', 'Set B (higher SD = more consistent)', 'Same consistency (similar means)', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 9 < 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=68, SD=8. Set B: mean=71, SD=11. Which set has more consistent values?', 'Cannot compare without raw data', 'Same consistency (similar means)', 'Set B (higher SD = more consistent)', 'Set A (lower SD = more consistent)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 8 < 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Set A: mean=51, SD=7. Set B: mean=46, SD=14. Which set has more consistent values?', 'Set B (higher SD = more consistent)', 'Same consistency (similar means)', 'Cannot compare without raw data', 'Set A (lower SD = more consistent)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'Lower SD means less spread, so more consistent. Set A has SD 7 < 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For weights (kg): mean = 70, SD = 10. How would you describe a value of 80?', 'Typical (within 1 sd)', 'Very unusual (beyond 3 SD)', 'Unusual (beyond 2 SD)', 'Cannot determine', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (80 - 70)/10 = 1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For temperatures (°C): mean = 20, SD = 5. How would you describe a value of 15?', 'Unusual (beyond 2 SD)', 'Very unusual (beyond 3 SD)', 'Typical (within 1 sd)', 'Cannot determine', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (15 - 20)/5 = -1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For waiting times (min): mean = 15, SD = 4. How would you describe a value of 7?', 'Typical (within 1 SD)', 'Cannot determine', 'Somewhat unusual (between 1-2 sd)', 'Unusual (beyond 2 SD)', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (7 - 15)/4 = -2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For heights (cm): mean = 170, SD = 8. How would you describe a value of 154?', 'Cannot determine', 'Somewhat unusual (between 1-2 sd)', 'Typical (within 1 SD)', 'Unusual (beyond 2 SD)', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (154 - 170)/8 = -2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For temperatures (°C): mean = 20, SD = 5. How would you describe a value of 15?', 'Unusual (beyond 2 SD)', 'Typical (within 1 sd)', 'Very unusual (beyond 3 SD)', 'Cannot determine', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (15 - 20)/5 = -1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For exam scores: mean = 65, SD = 12. How would you describe a value of 77?', 'Unusual (beyond 2 SD)', 'Very unusual (beyond 3 SD)', 'Typical (within 1 sd)', 'Cannot determine', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (77 - 65)/12 = 1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For waiting times (min): mean = 15, SD = 4. How would you describe a value of 19?', 'Cannot determine', 'Very unusual (beyond 3 SD)', 'Unusual (beyond 2 SD)', 'Typical (within 1 sd)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (19 - 15)/4 = 1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For exam scores: mean = 65, SD = 12. How would you describe a value of 53?', 'Unusual (beyond 2 SD)', 'Typical (within 1 sd)', 'Very unusual (beyond 3 SD)', 'Cannot determine', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (53 - 65)/12 = -1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For exam scores: mean = 65, SD = 12. How would you describe a value of 89?', 'Typical (within 1 SD)', 'Somewhat unusual (between 1-2 sd)', 'Unusual (beyond 2 SD)', 'Cannot determine', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (89 - 65)/12 = 2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For exam scores: mean = 65, SD = 12. How would you describe a value of 53?', 'Unusual (beyond 2 SD)', 'Cannot determine', 'Typical (within 1 sd)', 'Very unusual (beyond 3 SD)', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (53 - 65)/12 = -1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For waiting times (min): mean = 15, SD = 4. How would you describe a value of 19?', 'Unusual (beyond 2 SD)', 'Typical (within 1 sd)', 'Cannot determine', 'Very unusual (beyond 3 SD)', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (19 - 15)/4 = 1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For temperatures (°C): mean = 20, SD = 5. How would you describe a value of 30?', 'Unusual (beyond 2 SD)', 'Cannot determine', 'Typical (within 1 SD)', 'Somewhat unusual (between 1-2 sd)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (30 - 20)/5 = 2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For waiting times (min): mean = 15, SD = 4. How would you describe a value of 7?', 'Typical (within 1 SD)', 'Somewhat unusual (between 1-2 sd)', 'Cannot determine', 'Unusual (beyond 2 SD)', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (7 - 15)/4 = -2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For weights (kg): mean = 70, SD = 10. How would you describe a value of 60?', 'Unusual (beyond 2 SD)', 'Typical (within 1 sd)', 'Cannot determine', 'Very unusual (beyond 3 SD)', 1,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (60 - 70)/10 = -1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For heights (cm): mean = 170, SD = 8. How would you describe a value of 178?', 'Very unusual (beyond 3 SD)', 'Unusual (beyond 2 SD)', 'Cannot determine', 'Typical (within 1 sd)', 3,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (178 - 170)/8 = 1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For weights (kg): mean = 70, SD = 10. How would you describe a value of 60?', 'Typical (within 1 sd)', 'Cannot determine', 'Very unusual (beyond 3 SD)', 'Unusual (beyond 2 SD)', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (60 - 70)/10 = -1.0. This is typical (within 1 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For waiting times (min): mean = 15, SD = 4. How would you describe a value of 7?', 'Cannot determine', 'Unusual (beyond 2 SD)', 'Somewhat unusual (between 1-2 sd)', 'Typical (within 1 SD)', 2,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (7 - 15)/4 = -2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For weights (kg): mean = 70, SD = 10. How would you describe a value of 90?', 'Somewhat unusual (between 1-2 sd)', 'Unusual (beyond 2 SD)', 'Typical (within 1 SD)', 'Cannot determine', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (90 - 70)/10 = 2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For heights (cm): mean = 170, SD = 8. How would you describe a value of 186?', 'Somewhat unusual (between 1-2 sd)', 'Cannot determine', 'Unusual (beyond 2 SD)', 'Typical (within 1 SD)', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (186 - 170)/8 = 2.0. This is somewhat unusual (between 1-2 SD)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For exam scores: mean = 65, SD = 12. How would you describe a value of 41?', 'Somewhat unusual (between 1-2 sd)', 'Unusual (beyond 2 SD)', 'Cannot determine', 'Typical (within 1 SD)', 0,
'lc_ol_statistics', 12, 'advanced', 'lc_ol', 'z = (41 - 65)/12 = -2.0. This is somewhat unusual (between 1-2 SD)', 1);

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_statistics';
