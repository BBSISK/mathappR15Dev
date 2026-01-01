-- LC Ordinary Level - Financial Maths Complete SQL
-- Generated: 2025-12-15
-- Total: 600 questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Financial Maths topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_ol_financial', 'Financial Maths', id, '💰', 2, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_financial';

-- Insert questions
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 15% of €100?', '€15', '€25.00', '€85.00', '€150.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '15% of €100 = 15/100 × 100 = €15.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 10% of €50?', '€5', '€10.00', '€50.00', '€40.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '10% of €50 = 10/100 × 50 = €5.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 30% of €80?', '€24', '€50.00', '€32.00', '€240.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '30% of €80 = 30/100 × 80 = €24.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 75% of €100?', '€85.00', '€25.00', '€750.00', '€75', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '75% of €100 = 75/100 × 100 = €75.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 25% of €200?', '€175.00', '€50', '€500.00', '€70.00', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '25% of €200 = 25/100 × 200 = €50.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 40% of €120?', '€80.00', '€480.00', '€60.00', '€48', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '40% of €120 = 40/100 × 120 = €48.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 10% of €120?', '€12', '€110.00', '€120.00', '€24.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '10% of €120 = 10/100 × 120 = €12.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 30% of €500?', '€150', '€200.00', '€470.00', '€1500.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '30% of €500 = 30/100 × 500 = €150.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 40% of €100?', '€40', '€400.00', '€50.00', '€60.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '40% of €100 = 40/100 × 100 = €40.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 75% of €200?', '€1500.00', '€125.00', '€150', '€170.00', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '75% of €200 = 75/100 × 200 = €150.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 25% of €150?', '€37.50', '€52.50', '€125.00', '€375.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '25% of €150 = 25/100 × 150 = €37.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 20% of €400?', '€380.00', '€800.00', '€120.00', '€80', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '20% of €400 = 20/100 × 400 = €80.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 50% of €500?', '€2500.00', '€300.00', '€250', '€450.00', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '50% of €500 = 50/100 × 500 = €250.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 75% of €120?', '€102.00', '€45.00', '€900.00', '€90', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '75% of €120 = 75/100 × 120 = €90.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 30% of €100?', '€300.00', '€30', '€40.00', '€70.00', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '30% of €100 = 30/100 × 100 = €30.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 25% of €80?', '€200.00', '€55.00', '€28.00', '€20', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '25% of €80 = 25/100 × 80 = €20.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 30% of €250?', '€100.00', '€750.00', '€75', '€220.00', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '30% of €250 = 30/100 × 250 = €75.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 10% of €50?', '€40.00', '€10.00', '€50.00', '€5', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '10% of €50 = 10/100 × 50 = €5.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 75% of €100?', '€750.00', '€75', '€25.00', '€85.00', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '75% of €100 = 75/100 × 100 = €75.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 30% of €80?', '€24', '€32.00', '€240.00', '€50.00', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '30% of €80 = 30/100 × 80 = €24.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 30 as a percentage of 50.', '70%', '2%', '60%', '30%', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '30/50 × 100 = 60.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 15 as a percentage of 250.', '3%', '16%', '17%', '6%', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '15/250 × 100 = 6.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 40 as a percentage of 200.', '5%', '10%', '20%', '30%', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '40/200 × 100 = 20.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 20 as a percentage of 50.', '20%', '50%', '2%', '40%', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '20/50 × 100 = 40.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 5 as a percentage of 250.', '50%', '2%', '1%', '12%', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '5/250 × 100 = 2.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 5 as a percentage of 100.', '15%', '20%', '2%', '5%', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '5/100 × 100 = 5.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 10 as a percentage of 200.', '5%', '15%', '20%', '2%', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '10/200 × 100 = 5.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 45 as a percentage of 250.', '9%', '28%', '6%', '18%', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '45/250 × 100 = 18.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 20 as a percentage of 200.', '10%', 'Cannot determine', '5%', '20%', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '20/200 × 100 = 10.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 10 as a percentage of 500.', '2%', '12%', '50%', '1%', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '10/500 × 100 = 2.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 45 as a percentage of 50.', '1%', '90%', '45%', '100%', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '45/50 × 100 = 90.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 10 as a percentage of 250.', '25%', '4%', '2%', '14%', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '10/250 × 100 = 4.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 40 as a percentage of 200.', '10%', '5%', '30%', '20%', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '40/200 × 100 = 20.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 15 as a percentage of 250.', '16%', '3%', '6%', '17%', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '15/250 × 100 = 6.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 25 as a percentage of 50.', '2%', '50%', '60%', '25%', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', '25/50 × 100 = 50.0%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 50% of a number is 40, what is the number?', '80', '40', '20', '120', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 50% = 40, then 100% = 40 × 100/50 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 50% of a number is 30, what is the number?', '60', '15', '30', '90', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 50% = 30, then 100% = 30 × 100/50 = 60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 20% of a number is 10, what is the number?', '2', '50', '60', '25', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 20% = 10, then 100% = 10 × 100/20 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 50% of a number is 10, what is the number?', '10', '30', '20', '5', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 50% = 10, then 100% = 10 × 100/50 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 50% of a number is 20, what is the number?', '20', '40', '60', '10', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 50% = 20, then 100% = 20 × 100/50 = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 25% of a number is 20, what is the number?', '40', '100', '5', '80', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 25% = 20, then 100% = 20 × 100/25 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 50% of a number is 40, what is the number?', '120', '80', '40', '20', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 50% = 40, then 100% = 40 × 100/50 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 25% of a number is 25, what is the number?', '6', '50', '100', '125', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 25% = 25, then 100% = 25 × 100/25 = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10% of a number is 20, what is the number?', '220', '100', '2', '200', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 10% = 20, then 100% = 20 × 100/10 = 200', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 50% of a number is 40, what is the number?', '20', '40', '80', '120', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 50% = 40, then 100% = 40 × 100/50 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 50% of a number is 50, what is the number?', '100', '50', '25', '150', 0,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 50% = 50, then 100% = 50 × 100/50 = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 25% of a number is 20, what is the number?', '5', '100', '80', '40', 2,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 25% = 20, then 100% = 20 × 100/25 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 10% of a number is 30, what is the number?', '3', '300', '150', '330', 1,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 10% = 30, then 100% = 30 × 100/10 = 300', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 20% of a number is 25, what is the number?', '150', '62', '5', '125', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 20% = 25, then 100% = 25 × 100/20 = 125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 25% of a number is 20, what is the number?', '40', '100', '5', '80', 3,
'lc_ol_financial', 1, 'foundation', 'lc_ol', 'If 25% = 20, then 100% = 20 × 100/25 = 80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €160 before VAT. If VAT is 13.5%, find the price including VAT.', '€181.60', '€21.60', '€191.60', '€173.50', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €160 = €21.60. Total = €160 + €21.60 = €181.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €65 before VAT. If VAT is 13.5%, find the price including VAT.', '€73.78', '€83.78', '€78.50', '€8.78', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €65 = €8.78. Total = €65 + €8.78 = €73.78', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €455 before VAT. If VAT is 13.5%, find the price including VAT.', '€526.42', '€516.42', '€468.50', '€61.42', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €455 = €61.42. Total = €455 + €61.42 = €516.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €250 before VAT. If VAT is 13.5%, find the price including VAT.', '€293.75', '€33.75', '€263.50', '€283.75', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €250 = €33.75. Total = €250 + €33.75 = €283.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €95 before VAT. If VAT is 23%, find the price including VAT.', '€21.85', '€116.85', '€126.85', '€118.00', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €95 = €21.85. Total = €95 + €21.85 = €116.85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €145 before VAT. If VAT is 23%, find the price including VAT.', '€178.35', '€188.35', '€33.35', '€168.00', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €145 = €33.35. Total = €145 + €33.35 = €178.35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €360 before VAT. If VAT is 13.5%, find the price including VAT.', '€373.50', '€408.60', '€418.60', '€48.60', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €360 = €48.60. Total = €360 + €48.60 = €408.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €400 before VAT. If VAT is 13.5%, find the price including VAT.', '€464.00', '€413.50', '€454.00', '€54.00', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €400 = €54.00. Total = €400 + €54.00 = €454.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €265 before VAT. If VAT is 13.5%, find the price including VAT.', '€278.50', '€35.77', '€310.77', '€300.77', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €265 = €35.77. Total = €265 + €35.77 = €300.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €70 before VAT. If VAT is 13.5%, find the price including VAT.', '€9.45', '€83.50', '€89.45', '€79.45', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €70 = €9.45. Total = €70 + €9.45 = €79.45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €330 before VAT. If VAT is 13.5%, find the price including VAT.', '€384.55', '€343.50', '€374.55', '€44.55', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €330 = €44.55. Total = €330 + €44.55 = €374.55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €55 before VAT. If VAT is 13.5%, find the price including VAT.', '€68.50', '€7.42', '€72.42', '€62.42', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €55 = €7.42. Total = €55 + €7.42 = €62.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €355 before VAT. If VAT is 23%, find the price including VAT.', '€446.65', '€378.00', '€436.65', '€81.65', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €355 = €81.65. Total = €355 + €81.65 = €436.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €280 before VAT. If VAT is 23%, find the price including VAT.', '€354.40', '€303.00', '€344.40', '€64.40', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €280 = €64.40. Total = €280 + €64.40 = €344.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €375 before VAT. If VAT is 23%, find the price including VAT.', '€398.00', '€86.25', '€471.25', '€461.25', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €375 = €86.25. Total = €375 + €86.25 = €461.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €195 before VAT. If VAT is 23%, find the price including VAT.', '€239.85', '€44.85', '€249.85', '€218.00', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €195 = €44.85. Total = €195 + €44.85 = €239.85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €360 before VAT. If VAT is 23%, find the price including VAT.', '€383.00', '€452.80', '€82.80', '€442.80', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €360 = €82.80. Total = €360 + €82.80 = €442.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €300 before VAT. If VAT is 23%, find the price including VAT.', '€379.00', '€369.00', '€323.00', '€69.00', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €300 = €69.00. Total = €300 + €69.00 = €369.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €85 before VAT. If VAT is 23%, find the price including VAT.', '€114.55', '€19.55', '€108.00', '€104.55', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €85 = €19.55. Total = €85 + €19.55 = €104.55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A product costs €340 before VAT. If VAT is 13.5%, find the price including VAT.', '€353.50', '€395.90', '€385.90', '€45.90', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 13.5% of €340 = €45.90. Total = €340 + €45.90 = €385.90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €590 excluding VAT.', '€135.70', '€158.70', '€725.70', '€76.70', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €590 = 0.23 × 590 = €135.70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €940 excluding VAT.', '€216.20', '€239.20', '€122.20', '€1156.20', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €940 = 0.23 × 940 = €216.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €620 excluding VAT.', '€142.60', '€165.60', '€80.60', '€762.60', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €620 = 0.23 × 620 = €142.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €180 excluding VAT.', '€23.40', '€221.40', '€64.40', '€41.40', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €180 = 0.23 × 180 = €41.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €480 excluding VAT.', '€62.40', '€133.40', '€590.40', '€110.40', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €480 = 0.23 × 480 = €110.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €365 excluding VAT.', '€106.95', '€83.95', '€448.95', '€47.45', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €365 = 0.23 × 365 = €83.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €540 excluding VAT.', '€124.20', '€70.20', '€147.20', '€664.20', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €540 = 0.23 × 540 = €124.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €965 excluding VAT.', '€244.95', '€125.45', '€1186.95', '€221.95', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €965 = 0.23 × 965 = €221.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €425 excluding VAT.', '€55.25', '€97.75', '€120.75', '€522.75', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €425 = 0.23 × 425 = €97.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €440 excluding VAT.', '€101.20', '€124.20', '€541.20', '€57.20', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €440 = 0.23 × 440 = €101.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €610 excluding VAT.', '€163.30', '€79.30', '€750.30', '€140.30', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €610 = 0.23 × 610 = €140.30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €855 excluding VAT.', '€219.65', '€1051.65', '€111.15', '€196.65', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €855 = 0.23 × 855 = €196.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €510 excluding VAT.', '€627.30', '€66.30', '€140.30', '€117.30', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €510 = 0.23 × 510 = €117.30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €860 excluding VAT.', '€1057.80', '€220.80', '€111.80', '€197.80', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €860 = 0.23 × 860 = €197.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the VAT (at 23%) on an item priced at €965 excluding VAT.', '€125.45', '€221.95', '€244.95', '€1186.95', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'VAT = 23% of €965 = 0.23 × 965 = €221.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €172 including VAT at 23%. Find the price before VAT.', '€139.84', '€149.00', 'Cannot determine', '€132.44', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €172 ÷ 1.23 = €139.84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €220 including VAT at 23%. Find the price before VAT.', '€197.00', '€178.86', 'Cannot determine', '€169.40', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €220 ÷ 1.23 = €178.86', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €254 including VAT at 23%. Find the price before VAT.', '€206.50', '€195.58', '€231.00', 'Cannot determine', 0,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €254 ÷ 1.23 = €206.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €248 including VAT at 23%. Find the price before VAT.', '€190.96', '€225.00', '€201.63', 'Cannot determine', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €248 ÷ 1.23 = €201.63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €186 including VAT at 23%. Find the price before VAT.', 'Cannot determine', '€143.22', '€163.00', '€151.22', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €186 ÷ 1.23 = €151.22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €492 including VAT at 23%. Find the price before VAT.', '€378.84', 'Cannot determine', '€469.00', '€400.00', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €492 ÷ 1.23 = €400.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €190 including VAT at 23%. Find the price before VAT.', '€146.30', 'Cannot determine', '€154.47', '€167.00', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €190 ÷ 1.23 = €154.47', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €138 including VAT at 23%. Find the price before VAT.', 'Cannot determine', '€106.26', '€112.20', '€115.00', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €138 ÷ 1.23 = €112.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €132 including VAT at 23%. Find the price before VAT.', '€101.64', '€109.00', '€107.32', 'Cannot determine', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €132 ÷ 1.23 = €107.32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €282 including VAT at 23%. Find the price before VAT.', '€217.14', '€259.00', 'Cannot determine', '€229.27', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €282 ÷ 1.23 = €229.27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €404 including VAT at 23%. Find the price before VAT.', 'Cannot determine', '€328.46', '€381.00', '€311.08', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €404 ÷ 1.23 = €328.46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €186 including VAT at 23%. Find the price before VAT.', '€163.00', '€143.22', 'Cannot determine', '€151.22', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €186 ÷ 1.23 = €151.22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €438 including VAT at 23%. Find the price before VAT.', '€337.26', 'Cannot determine', '€415.00', '€356.10', 3,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €438 ÷ 1.23 = €356.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €460 including VAT at 23%. Find the price before VAT.', '€437.00', '€373.98', 'Cannot determine', '€354.20', 1,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €460 ÷ 1.23 = €373.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €412 including VAT at 23%. Find the price before VAT.', 'Cannot determine', '€389.00', '€334.96', '€317.24', 2,
'lc_ol_financial', 2, 'foundation', 'lc_ol', 'Price before VAT = €412 ÷ 1.23 = €334.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €168 is increased by 30%. What is the new price?', '€198.00', '€218.40', '€268.80', '€50.40', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 30% of €168 = €50.4. New price = €168 + €50.4 = €218.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €188 is increased by 30%. What is the new price?', '€244.40', '€218.00', '€56.40', '€300.80', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 30% of €188 = €56.4. New price = €188 + €56.4 = €244.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €104 is increased by 15%. What is the new price?', '€15.60', '€119.60', '€135.20', '€119.00', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 15% of €104 = €15.6. New price = €104 + €15.6 = €119.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €360 is increased by 5%. What is the new price?', '€378', '€18.00', '€396.00', '€365.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 5% of €360 = €18.0. New price = €360 + €18.0 = €378.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €328 is increased by 25%. What is the new price?', '€353.00', '€410', '€82.00', '€492.00', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 25% of €328 = €82.0. New price = €328 + €82.0 = €410.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €224 is increased by 20%. What is the new price?', '€313.60', '€44.80', '€244.00', '€268.80', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 20% of €224 = €44.8. New price = €224 + €44.8 = €268.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €362 is increased by 25%. What is the new price?', '€387.00', '€452.50', '€90.50', '€543.00', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 25% of €362 = €90.5. New price = €362 + €90.5 = €452.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €178 is increased by 25%. What is the new price?', '€203.00', '€222.50', '€267.00', '€44.50', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 25% of €178 = €44.5. New price = €178 + €44.5 = €222.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €186 is increased by 5%. What is the new price?', '€204.60', '€195.30', '€191.00', '€9.30', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 5% of €186 = €9.3. New price = €186 + €9.3 = €195.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €206 is increased by 10%. What is the new price?', '€216.00', '€226.60', '€20.60', '€247.20', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 10% of €206 = €20.6. New price = €206 + €20.6 = €226.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €316 is increased by 30%. What is the new price?', '€410.80', '€94.80', '€505.60', '€346.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 30% of €316 = €94.8. New price = €316 + €94.8 = €410.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €220 is increased by 10%. What is the new price?', '€230.00', '€22.00', '€242', '€264.00', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 10% of €220 = €22.0. New price = €220 + €22.0 = €242.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €238 is increased by 20%. What is the new price?', '€285.60', '€333.20', '€47.60', '€258.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 20% of €238 = €47.6. New price = €238 + €47.6 = €285.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €252 is increased by 10%. What is the new price?', '€25.20', '€262.00', '€302.40', '€277.20', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 10% of €252 = €25.2. New price = €252 + €25.2 = €277.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €328 is increased by 30%. What is the new price?', '€358.00', '€426.40', '€98.40', '€524.80', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 30% of €328 = €98.4. New price = €328 + €98.4 = €426.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €142 is increased by 15%. What is the new price?', '€163.30', '€184.60', '€21.30', '€157.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 15% of €142 = €21.3. New price = €142 + €21.3 = €163.3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €326 is increased by 10%. What is the new price?', '€32.60', '€336.00', '€358.60', '€391.20', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 10% of €326 = €32.6. New price = €326 + €32.6 = €358.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €186 is increased by 15%. What is the new price?', '€213.90', '€241.80', '€27.90', '€201.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 15% of €186 = €27.9. New price = €186 + €27.9 = €213.9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €348 is increased by 20%. What is the new price?', '€368.00', '€417.60', '€69.60', '€487.20', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 20% of €348 = €69.6. New price = €348 + €69.6 = €417.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €132 is increased by 20%. What is the new price?', '€158.40', '€26.40', '€184.80', '€152.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Increase = 20% of €132 = €26.4. New price = €132 + €26.4 = €158.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €440 item is reduced by 10%. What is the sale price?', '€440.00', '€44.00', '€430.00', '€396', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 10% of €440 = €44.0. Sale price = €440 - €44.0 = €396.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €496 item is reduced by 10%. What is the sale price?', '€486.00', '€496.00', '€49.60', '€446.40', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 10% of €496 = €49.6. Sale price = €496 - €49.6 = €446.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €232 item is reduced by 10%. What is the sale price?', '€232.00', '€23.20', '€222.00', '€208.80', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 10% of €232 = €23.2. Sale price = €232 - €23.2 = €208.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €756 item is reduced by 15%. What is the sale price?', '€642.60', '€741.00', '€1134.00', '€113.40', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 15% of €756 = €113.4. Sale price = €756 - €113.4 = €642.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €344 item is reduced by 40%. What is the sale price?', '€304.00', '€1376.00', '€137.60', '€206.40', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 40% of €344 = €137.6. Sale price = €344 - €137.6 = €206.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €762 item is reduced by 30%. What is the sale price?', '€533.40', '€732.00', '€228.60', '€2286.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 30% of €762 = €228.6. Sale price = €762 - €228.6 = €533.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €932 item is reduced by 25%. What is the sale price?', '€699', '€907.00', '€2330.00', '€233.00', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 25% of €932 = €233.0. Sale price = €932 - €233.0 = €699.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €222 item is reduced by 10%. What is the sale price?', '€222.00', '€199.80', '€22.20', '€212.00', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 10% of €222 = €22.2. Sale price = €222 - €22.2 = €199.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €810 item is reduced by 10%. What is the sale price?', '€81.00', '€800.00', '€729', '€810.00', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 10% of €810 = €81.0. Sale price = €810 - €81.0 = €729.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €568 item is reduced by 15%. What is the sale price?', '€85.20', '€553.00', '€482.80', '€852.00', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 15% of €568 = €85.2. Sale price = €568 - €85.2 = €482.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €530 item is reduced by 30%. What is the sale price?', '€1590.00', '€159.00', '€371', '€500.00', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 30% of €530 = €159.0. Sale price = €530 - €159.0 = €371.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €372 item is reduced by 25%. What is the sale price?', '€347.00', '€93.00', '€279', '€930.00', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 25% of €372 = €93.0. Sale price = €372 - €93.0 = €279.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €764 item is reduced by 20%. What is the sale price?', '€1528.00', '€744.00', '€152.80', '€611.20', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 20% of €764 = €152.8. Sale price = €764 - €152.8 = €611.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €618 item is reduced by 25%. What is the sale price?', '€154.50', '€593.00', '€1545.00', '€463.50', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 25% of €618 = €154.5. Sale price = €618 - €154.5 = €463.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €898 item is reduced by 10%. What is the sale price?', '€888.00', '€89.80', '€898.00', '€808.20', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Decrease = 10% of €898 = €89.8. Sale price = €898 - €89.8 = €808.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €480 to €600. What is the percentage increase?', '25%', '35%', '120%', '50%', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €600 - €480 = €120. Percentage = (120/480) × 100 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €425 to €510. What is the percentage increase?', '85%', '20%', '30%', '40%', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €510 - €425 = €85. Percentage = (85/425) × 100 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €275 to €302. What is the percentage increase?', 'Cannot determine', '10%', '27%', '20%', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €302 - €275 = €27. Percentage = (27/275) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €165 to €181. What is the percentage increase?', '10%', '16%', '20%', 'Cannot determine', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €181 - €165 = €16. Percentage = (16/165) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €500 to €550. What is the percentage increase?', '50%', '20%', 'Cannot determine', '10%', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €550 - €500 = €50. Percentage = (50/500) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €155 to €186. What is the percentage increase?', '31%', '30%', '20%', '40%', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €186 - €155 = €31. Percentage = (31/155) × 100 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €265 to €291. What is the percentage increase?', '10%', '20%', 'Cannot determine', '26%', 0,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €291 - €265 = €26. Percentage = (26/265) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €105 to €131. What is the percentage increase?', '35%', '50%', '26%', '25%', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €131 - €105 = €26. Percentage = (26/105) × 100 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €335 to €502. What is the percentage increase?', '60%', '50%', '100%', '167%', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €502 - €335 = €167. Percentage = (167/335) × 100 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €430 to €537. What is the percentage increase?', '107%', '25%', '50%', '35%', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €537 - €430 = €107. Percentage = (107/430) × 100 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €315 to €441. What is the percentage increase?', '80%', '40%', '126%', '50%', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €441 - €315 = €126. Percentage = (126/315) × 100 = 40%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €150 to €180. What is the percentage increase?', '30%', '20%', 'Cannot determine', '40%', 1,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €180 - €150 = €30. Percentage = (30/150) × 100 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €105 to €126. What is the percentage increase?', '30%', '21%', '40%', '20%', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €126 - €105 = €21. Percentage = (21/105) × 100 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €345 to €517. What is the percentage increase?', '172%', '100%', '50%', '60%', 2,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €517 - €345 = €172. Percentage = (172/345) × 100 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A value changed from €130 to €182. What is the percentage increase?', '50%', '52%', '80%', '40%', 3,
'lc_ol_financial', 3, 'foundation', 'lc_ol', 'Change = €182 - €130 = €52. Percentage = (52/130) × 100 = 40%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €165 and sells them at 40% profit. Find the selling price.', '€205.00', '€231', '€396.00', '€66.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 40% of €165 = €66.0. Selling price = €165 + €66.0 = €231.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €285 and sells them at 50% profit. Find the selling price.', '€142.50', '€427.50', '€712.50', '€335.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 50% of €285 = €142.5. Selling price = €285 + €142.5 = €427.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €325 and sells them at 30% profit. Find the selling price.', '€355.00', '€747.50', '€422.50', '€97.50', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 30% of €325 = €97.5. Selling price = €325 + €97.5 = €422.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €380 and sells them at 25% profit. Find the selling price.', '€405.00', '€475', '€855.00', '€95.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 25% of €380 = €95.0. Selling price = €380 + €95.0 = €475.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €200 and sells them at 15% profit. Find the selling price.', '€215.00', '€30.00', '€430.00', '€230', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 15% of €200 = €30.0. Selling price = €200 + €30.0 = €230.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €205 and sells them at 40% profit. Find the selling price.', '€245.00', '€82.00', '€287', '€492.00', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 40% of €205 = €82.0. Selling price = €205 + €82.0 = €287.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €280 and sells them at 25% profit. Find the selling price.', '€70.00', '€305.00', '€630.00', '€350', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 25% of €280 = €70.0. Selling price = €280 + €70.0 = €350.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €475 and sells them at 50% profit. Find the selling price.', '€525.00', '€712.50', '€1187.50', '€237.50', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 50% of €475 = €237.5. Selling price = €475 + €237.5 = €712.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €300 and sells them at 20% profit. Find the selling price.', '€660.00', '€320.00', '€360', '€60.00', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 20% of €300 = €60.0. Selling price = €300 + €60.0 = €360.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €265 and sells them at 15% profit. Find the selling price.', '€569.75', '€39.75', '€280.00', '€304.75', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 15% of €265 = €39.75. Selling price = €265 + €39.75 = €304.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €275 and sells them at 10% profit. Find the selling price.', '€577.50', '€285.00', '€302.50', '€27.50', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 10% of €275 = €27.5. Selling price = €275 + €27.5 = €302.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €175 and sells them at 40% profit. Find the selling price.', '€420.00', '€245', '€215.00', '€70.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 40% of €175 = €70.0. Selling price = €175 + €70.0 = €245.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €330 and sells them at 10% profit. Find the selling price.', '€340.00', '€693.00', '€363', '€33.00', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 10% of €330 = €33.0. Selling price = €330 + €33.0 = €363.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €165 and sells them at 40% profit. Find the selling price.', '€231', '€396.00', '€66.00', '€205.00', 0,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 40% of €165 = €66.0. Selling price = €165 + €66.0 = €231.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €400 and sells them at 15% profit. Find the selling price.', '€460', '€415.00', '€60.00', '€860.00', 0,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 15% of €400 = €60.0. Selling price = €400 + €60.0 = €460.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €410 and sells them at 25% profit. Find the selling price.', '€922.50', '€512.50', '€102.50', '€435.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 25% of €410 = €102.5. Selling price = €410 + €102.5 = €512.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €140 and sells them at 15% profit. Find the selling price.', '€301.00', '€155.00', '€21.00', '€161', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 15% of €140 = €21.0. Selling price = €140 + €21.0 = €161.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €180 and sells them at 40% profit. Find the selling price.', '€72.00', '€220.00', '€432.00', '€252', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 40% of €180 = €72.0. Selling price = €180 + €72.0 = €252.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €360 and sells them at 40% profit. Find the selling price.', '€400.00', '€144.00', '€864.00', '€504', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 40% of €360 = €144.0. Selling price = €360 + €144.0 = €504.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A shopkeeper buys goods for €475 and sells them at 15% profit. Find the selling price.', '€1021.25', '€71.25', '€546.25', '€490.00', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = 15% of €475 = €71.25. Selling price = €475 + €71.25 = €546.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €250 is sold at a 10% loss. What is the selling price?', '€275.00', '€225', '€25.00', '€240.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 10% of €250 = €25.0. Selling price = €250 - €25.0 = €225.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €335 is sold at a 5% loss. What is the selling price?', '€318.25', '€330.00', '€351.75', '€16.75', 0,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 5% of €335 = €16.75. Selling price = €335 - €16.75 = €318.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €630 is sold at a 15% loss. What is the selling price?', '€94.50', '€615.00', '€535.50', '€724.50', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 15% of €630 = €94.5. Selling price = €630 - €94.5 = €535.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €985 is sold at a 25% loss. What is the selling price?', '€1231.25', '€960.00', '€738.75', '€246.25', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 25% of €985 = €246.25. Selling price = €985 - €246.25 = €738.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €920 is sold at a 10% loss. What is the selling price?', '€828', '€910.00', '€92.00', '€1012.00', 0,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 10% of €920 = €92.0. Selling price = €920 - €92.0 = €828.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €875 is sold at a 25% loss. What is the selling price?', '€850.00', '€656.25', '€218.75', '€1093.75', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 25% of €875 = €218.75. Selling price = €875 - €218.75 = €656.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €880 is sold at a 5% loss. What is the selling price?', '€44.00', '€836', '€875.00', '€924.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 5% of €880 = €44.0. Selling price = €880 - €44.0 = €836.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €435 is sold at a 5% loss. What is the selling price?', '€430.00', '€456.75', '€413.25', '€21.75', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 5% of €435 = €21.75. Selling price = €435 - €21.75 = €413.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €940 is sold at a 20% loss. What is the selling price?', '€752', '€920.00', '€188.00', '€1128.00', 0,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 20% of €940 = €188.0. Selling price = €940 - €188.0 = €752.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €900 is sold at a 10% loss. What is the selling price?', '€990.00', '€810', '€890.00', '€90.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 10% of €900 = €90.0. Selling price = €900 - €90.0 = €810.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €815 is sold at a 10% loss. What is the selling price?', '€805.00', '€896.50', '€81.50', '€733.50', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 10% of €815 = €81.5. Selling price = €815 - €81.5 = €733.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €260 is sold at a 5% loss. What is the selling price?', '€273.00', '€247', '€13.00', '€255.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 5% of €260 = €13.0. Selling price = €260 - €13.0 = €247.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €810 is sold at a 20% loss. What is the selling price?', '€790.00', '€972.00', '€648', '€162.00', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 20% of €810 = €162.0. Selling price = €810 - €162.0 = €648.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €270 is sold at a 10% loss. What is the selling price?', '€27.00', '€243', '€260.00', '€297.00', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 10% of €270 = €27.0. Selling price = €270 - €27.0 = €243.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €255 is sold at a 10% loss. What is the selling price?', '€25.50', '€280.50', '€229.50', '€245.00', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Loss = 10% of €255 = €25.5. Selling price = €255 - €25.5 = €229.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €368 and sold for €460. What is the percentage profit?', '50%', '92%', '35%', '25%', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €460 - €368 = €92. Percentage = (92/368) × 100 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €288 and sold for €432. What is the percentage profit?', '100%', '50%', '60%', '144%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €432 - €288 = €144. Percentage = (144/288) × 100 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €140 and sold for €154. What is the percentage profit?', '20%', '10%', '14%', 'Cannot determine', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €154 - €140 = €14. Percentage = (14/140) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €144 and sold for €216. What is the percentage profit?', '72%', '100%', '50%', '60%', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €216 - €144 = €72. Percentage = (72/144) × 100 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €80 and sold for €88. What is the percentage profit?', '10%', '8%', 'Cannot determine', '20%', 0,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €88 - €80 = €8. Percentage = (8/80) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €348 and sold for €435. What is the percentage profit?', '50%', '25%', '35%', '87%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €435 - €348 = €87. Percentage = (87/348) × 100 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €372 and sold for €446. What is the percentage profit?', '30%', '20%', '74%', '40%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €446 - €372 = €74. Percentage = (74/372) × 100 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €312 and sold for €343. What is the percentage profit?', 'Cannot determine', '20%', '10%', '31%', 2,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €343 - €312 = €31. Percentage = (31/312) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €276 and sold for €345. What is the percentage profit?', '25%', '69%', '35%', '50%', 0,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €345 - €276 = €69. Percentage = (69/276) × 100 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €80 and sold for €100. What is the percentage profit?', '20%', '25%', '35%', '50%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €100 - €80 = €20. Percentage = (20/80) × 100 = 25%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €108 and sold for €129. What is the percentage profit?', '30%', '20%', '21%', '40%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €129 - €108 = €21. Percentage = (21/108) × 100 = 20%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €400 and sold for €440. What is the percentage profit?', '20%', '10%', 'Cannot determine', '40%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €440 - €400 = €40. Percentage = (40/400) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €144 and sold for €158. What is the percentage profit?', '20%', '10%', 'Cannot determine', '14%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €158 - €144 = €14. Percentage = (14/144) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €360 and sold for €396. What is the percentage profit?', '20%', 'Cannot determine', '36%', '10%', 3,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €396 - €360 = €36. Percentage = (36/360) × 100 = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item is bought for €308 and sold for €462. What is the percentage profit?', '154%', '50%', '100%', '60%', 1,
'lc_ol_financial', 4, 'developing', 'lc_ol', 'Profit = €462 - €308 = €154. Percentage = (154/308) × 100 = 50%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €3000 at 5% per annum for 3 years.', '€3450.00', '€150.00', '€450', '€900.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (3000 × 5 × 3)/100 = €450.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €5000 at 5% per annum for 2 years.', '€500', '€1000.00', '€5500.00', '€250.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (5000 × 5 × 2)/100 = €500.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €3000 at 4% per annum for 1 year.', '€120.00', '€120', '€3120.00', '€240.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (3000 × 4 × 1)/100 = €120.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €1000 at 2% per annum for 4 years.', '€1080.00', '€80', '€20.00', '€160.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (1000 × 2 × 4)/100 = €80.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €2500 at 2% per annum for 1 year.', '€2550.00', '€100.00', '€50.00', '€50', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (2500 × 2 × 1)/100 = €50.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €2500 at 2% per annum for 1 year.', '€2550.00', '€50.00', '€50', '€100.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (2500 × 2 × 1)/100 = €50.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €4000 at 6% per annum for 1 year.', '€240.00', '€240', '€4240.00', '€480.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (4000 × 6 × 1)/100 = €240.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €500 at 2% per annum for 4 years.', '€540.00', '€10.00', '€80.00', '€40', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (500 × 2 × 4)/100 = €40.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €4000 at 4% per annum for 3 years.', '€480', '€4480.00', '€960.00', '€160.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (4000 × 4 × 3)/100 = €480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €2500 at 6% per annum for 3 years.', '€900.00', '€150.00', '€2950.00', '€450', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (2500 × 6 × 3)/100 = €450.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €3000 at 6% per annum for 5 years.', '€3900.00', '€900', '€180.00', '€1800.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (3000 × 6 × 5)/100 = €900.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €2500 at 2% per annum for 1 year.', '€50.00', '€100.00', '€2550.00', '€50', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (2500 × 2 × 1)/100 = €50.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €2000 at 4% per annum for 3 years.', '€240', '€80.00', '€2240.00', '€480.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (2000 × 4 × 3)/100 = €240.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €3000 at 4% per annum for 3 years.', '€360', '€120.00', '€3360.00', '€720.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (3000 × 4 × 3)/100 = €360.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €1000 at 3% per annum for 3 years.', '€1090.00', '€30.00', '€90', '€180.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (1000 × 3 × 3)/100 = €90.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €3000 at 4% per annum for 4 years.', '€3480.00', '€120.00', '€480', '€960.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (3000 × 4 × 4)/100 = €480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €500 at 2% per annum for 5 years.', '€10.00', '€100.00', '€50', '€550.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (500 × 2 × 5)/100 = €50.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €500 at 5% per annum for 5 years.', '€250.00', '€625.00', '€125', '€25.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (500 × 5 × 5)/100 = €125.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €1500 at 4% per annum for 2 years.', '€240.00', '€60.00', '€1620.00', '€120', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (1500 × 4 × 2)/100 = €120.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €2000 at 5% per annum for 2 years.', '€200', '€400.00', '€100.00', '€2200.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (2000 × 5 × 2)/100 = €200.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €1500 at 5% per annum for 3 years.', '€450.00', '€75.00', '€225', '€1725.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (1500 × 5 × 3)/100 = €225.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €5000 at 2% per annum for 4 years.', '€400', '€800.00', '€5400.00', '€100.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (5000 × 2 × 4)/100 = €400.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €1500 at 6% per annum for 5 years.', '€1950.00', '€450', '€900.00', '€90.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (1500 × 6 × 5)/100 = €450.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €1500 at 5% per annum for 2 years.', '€1650.00', '€150', '€300.00', '€75.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (1500 × 5 × 2)/100 = €150.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the simple interest on €2000 at 5% per annum for 4 years.', '€100.00', '€2400.00', '€800.00', '€400', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'I = PRT/100 = (2000 × 5 × 4)/100 = €400.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 is invested at 5% simple interest for 2 years. Find the total amount after 2 years.', '€2400.00', '€200.00', '€2010.00', '€2200', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (2000 × 5 × 2)/100 = €200.0. Total = €2000 + €200.0 = €2200.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 is invested at 6% simple interest for 4 years. Find the total amount after 4 years.', '€4960', '€960.00', '€5920.00', '€4024.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (4000 × 6 × 4)/100 = €960.0. Total = €4000 + €960.0 = €4960.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 6% simple interest for 4 years. Find the total amount after 4 years.', '€4440.00', '€3720', '€3024.00', '€720.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (3000 × 6 × 4)/100 = €720.0. Total = €3000 + €720.0 = €3720.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at 4% simple interest for 4 years. Find the total amount after 4 years.', '€1016.00', '€1160', '€1320.00', '€160.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (1000 × 4 × 4)/100 = €160.0. Total = €1000 + €160.0 = €1160.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 4% simple interest for 4 years. Find the total amount after 4 years.', '€3480', '€480.00', '€3960.00', '€3016.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (3000 × 4 × 4)/100 = €480.0. Total = €3000 + €480.0 = €3480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 4% simple interest for 2 years. Find the total amount after 2 years.', '€240.00', '€3008.00', '€3240', '€3480.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (3000 × 4 × 2)/100 = €240.0. Total = €3000 + €240.0 = €3240.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 is invested at 4% simple interest for 2 years. Find the total amount after 2 years.', '€4640.00', '€320.00', '€4008.00', '€4320', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (4000 × 4 × 2)/100 = €320.0. Total = €4000 + €320.0 = €4320.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 4% simple interest for 2 years. Find the total amount after 2 years.', '€240.00', '€3008.00', '€3240', '€3480.00', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (3000 × 4 × 2)/100 = €240.0. Total = €3000 + €240.0 = €3240.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 is invested at 4% simple interest for 2 years. Find the total amount after 2 years.', '€160.00', '€2160', '€2008.00', '€2320.00', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (2000 × 4 × 2)/100 = €160.0. Total = €2000 + €160.0 = €2160.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 is invested at 3% simple interest for 4 years. Find the total amount after 4 years.', '€2240', '€240.00', '€2480.00', '€2012.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (2000 × 3 × 4)/100 = €240.0. Total = €2000 + €240.0 = €2240.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 is invested at 5% simple interest for 2 years. Find the total amount after 2 years.', '€400.00', '€4800.00', '€4010.00', '€4400', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (4000 × 5 × 2)/100 = €400.0. Total = €4000 + €400.0 = €4400.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 4% simple interest for 4 years. Find the total amount after 4 years.', '€5800', '€6600.00', '€5016.00', '€800.00', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (5000 × 4 × 4)/100 = €800.0. Total = €5000 + €800.0 = €5800.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 4% simple interest for 2 years. Find the total amount after 2 years.', '€5800.00', '€400.00', '€5008.00', '€5400', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (5000 × 4 × 2)/100 = €400.0. Total = €5000 + €400.0 = €5400.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 3% simple interest for 2 years. Find the total amount after 2 years.', '€5006.00', '€5600.00', '€300.00', '€5300', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (5000 × 3 × 2)/100 = €300.0. Total = €5000 + €300.0 = €5300.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at 5% simple interest for 3 years. Find the total amount after 3 years.', '€150.00', '€1015.00', '€1300.00', '€1150', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'Interest = (1000 × 5 × 3)/100 = €150.0. Total = €1000 + €150.0 = €1150.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 earns €400 simple interest in 2 years. What is the annual interest rate?', 'Cannot determine', '7%', '10%', '5%', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (400 × 100)/(4000 × 2) = 5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 earns €320 simple interest in 2 years. What is the annual interest rate?', 'Cannot determine', '4%', '6%', '8%', 1,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (320 × 100)/(4000 × 2) = 4%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 earns €320 simple interest in 2 years. What is the annual interest rate?', '10%', '16%', '8%', 'Cannot determine', 2,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (320 × 100)/(2000 × 2) = 8%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 earns €200 simple interest in 2 years. What is the annual interest rate?', 'Cannot determine', '10%', '7%', '5%', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (200 × 100)/(2000 × 2) = 5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 earns €400 simple interest in 2 years. What is the annual interest rate?', 'Cannot determine', '20%', '12%', '10%', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (400 × 100)/(2000 × 2) = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 earns €160 simple interest in 2 years. What is the annual interest rate?', '4%', 'Cannot determine', '8%', '6%', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (160 × 100)/(2000 × 2) = 4%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 earns €400 simple interest in 2 years. What is the annual interest rate?', 'Cannot determine', '8%', '6%', '4%', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (400 × 100)/(5000 × 2) = 4%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 earns €200 simple interest in 2 years. What is the annual interest rate?', '20%', 'Cannot determine', '12%', '10%', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (200 × 100)/(1000 × 2) = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 earns €400 simple interest in 2 years. What is the annual interest rate?', '5%', 'Cannot determine', '10%', '7%', 0,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (400 × 100)/(4000 × 2) = 5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 earns €80 simple interest in 2 years. What is the annual interest rate?', 'Cannot determine', '6%', '8%', '4%', 3,
'lc_ol_financial', 5, 'developing', 'lc_ol', 'R = (I × 100)/(P × T) = (80 × 100)/(1000 × 2) = 4%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 is invested at 2% compound interest per annum. Find the value after 2 years.', '€2080.00', '€2080.80', '€2180.80', '€2040.00', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 2000(1 + 0.02)^2 = 2000 × 1.0404 = €2080.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 is invested at 6% compound interest per annum. Find the value after 1 year.', 'Cannot determine', '€4340.00', 'Cannot determine', '€4240.00', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 4000(1 + 0.06)^1 = 4000 × 1.0600 = €4240.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 4% compound interest per annum. Find the value after 2 years.', '€3244.80', '€3120.00', '€3344.80', '€3240.00', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.04)^2 = 3000 × 1.0816 = €3244.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at 6% compound interest per annum. Find the value after 3 years.', '€1180.00', '€1291.02', '€1060.00', '€1191.02', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 1000(1 + 0.06)^3 = 1000 × 1.1910 = €1191.02', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 3% compound interest per annum. Find the value after 3 years.', '€3090.00', '€3270.00', '€3378.18', '€3278.18', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.03)^3 = 3000 × 1.0927 = €3278.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 6% compound interest per annum. Find the value after 3 years.', '€6055.08', '€5955.08', '€5900.00', '€5300.00', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 5000(1 + 0.06)^3 = 5000 × 1.1910 = €5955.08', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 6% compound interest per annum. Find the value after 1 year.', '€5400.00', 'Cannot determine', '€5300.00', 'Cannot determine', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 5000(1 + 0.06)^1 = 5000 × 1.0600 = €5300.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at 2% compound interest per annum. Find the value after 1 year.', 'Cannot determine', '€1120.00', '€1020.00', 'Cannot determine', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 1000(1 + 0.02)^1 = 1000 × 1.0200 = €1020.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 is invested at 4% compound interest per annum. Find the value after 1 year.', '€2080.00', 'Cannot determine', '€2180.00', 'Cannot determine', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 2000(1 + 0.04)^1 = 2000 × 1.0400 = €2080.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 is invested at 6% compound interest per annum. Find the value after 3 years.', '€2482.03', '€2360.00', '€2382.03', '€2120.00', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 2000(1 + 0.06)^3 = 2000 × 1.1910 = €2382.03', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 5% compound interest per annum. Find the value after 1 year.', 'Cannot determine', '€3150.00', 'Cannot determine', '€3250.00', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.05)^1 = 3000 × 1.0500 = €3150.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 4% compound interest per annum. Find the value after 2 years.', '€3120.00', '€3244.80', '€3240.00', '€3344.80', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.04)^2 = 3000 × 1.0816 = €3244.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 2% compound interest per annum. Find the value after 1 year.', '€3060.00', '€3160.00', 'Cannot determine', 'Cannot determine', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.02)^1 = 3000 × 1.0200 = €3060.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 is invested at 5% compound interest per annum. Find the value after 3 years.', '€4600.00', '€4730.50', '€4200.00', '€4630.50', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 4000(1 + 0.05)^3 = 4000 × 1.1576 = €4630.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 3% compound interest per annum. Find the value after 3 years.', '€3378.18', '€3270.00', '€3278.18', '€3090.00', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.03)^3 = 3000 × 1.0927 = €3278.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 2% compound interest per annum. Find the value after 1 year.', 'Cannot determine', 'Cannot determine', '€5200.00', '€5100.00', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 5000(1 + 0.02)^1 = 5000 × 1.0200 = €5100.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 3% compound interest per annum. Find the value after 2 years.', '€3182.70', '€3180.00', '€3090.00', '€3282.70', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.03)^2 = 3000 × 1.0609 = €3182.70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 6% compound interest per annum. Find the value after 1 year.', '€5400.00', '€5300.00', 'Cannot determine', 'Cannot determine', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 5000(1 + 0.06)^1 = 5000 × 1.0600 = €5300.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 is invested at 4% compound interest per annum. Find the value after 3 years.', '€4160.00', '€4499.46', '€4480.00', '€4599.46', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 4000(1 + 0.04)^3 = 4000 × 1.1249 = €4499.46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 6% compound interest per annum. Find the value after 1 year.', '€3280.00', 'Cannot determine', 'Cannot determine', '€3180.00', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.06)^1 = 3000 × 1.0600 = €3180.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 is invested at 5% compound interest per annum. Find the value after 3 years.', '€5888.13', '€5750.00', '€5250.00', '€5788.13', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 5000(1 + 0.05)^3 = 5000 × 1.1576 = €5788.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 6% compound interest per annum. Find the value after 2 years.', '€3470.80', '€3360.00', '€3370.80', '€3180.00', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.06)^2 = 3000 × 1.1236 = €3370.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 is invested at 6% compound interest per annum. Find the value after 1 year.', 'Cannot determine', '€4240.00', '€4340.00', 'Cannot determine', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 4000(1 + 0.06)^1 = 4000 × 1.0600 = €4240.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3000 is invested at 4% compound interest per annum. Find the value after 2 years.', '€3120.00', '€3240.00', '€3344.80', '€3244.80', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 3000(1 + 0.04)^2 = 3000 × 1.0816 = €3244.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 is invested at 6% compound interest per annum. Find the value after 3 years.', '€2120.00', '€2360.00', '€2382.03', '€2482.03', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'A = P(1 + r)ⁿ = 2000(1 + 0.06)^3 = 2000 × 1.1910 = €2382.03', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €5000 at 4% per annum for 2 years.', '€608.00', '€400.00', '€5408.00', '€408.00', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 5000(1.04)^2 = €5408.00. Interest = €5408.00 - €5000 = €408.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €5000 at 3% per annum for 2 years.', '€5304.50', '€454.50', '€300.00', '€304.50', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 5000(1.03)^2 = €5304.50. Interest = €5304.50 - €5000 = €304.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €3000 at 4% per annum for 2 years.', '€3244.80', '€240.00', '€244.80', '€364.80', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 3000(1.04)^2 = €3244.80. Interest = €3244.80 - €3000 = €244.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €2000 at 3% per annum for 2 years.', '€120.00', '€181.80', '€121.80', '€2121.80', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 2000(1.03)^2 = €2121.80. Interest = €2121.80 - €2000 = €121.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €2000 at 5% per annum for 3 years.', '€415.25', '€315.25', '€300.00', '€2315.25', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 2000(1.05)^3 = €2315.25. Interest = €2315.25 - €2000 = €315.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €2000 at 3% per annum for 3 years.', '€185.45', '€2185.45', '€245.45', '€180.00', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 2000(1.03)^3 = €2185.45. Interest = €2185.45 - €2000 = €185.45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €2000 at 4% per annum for 3 years.', '€249.73', '€2249.73', '€329.73', '€240.00', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 2000(1.04)^3 = €2249.73. Interest = €2249.73 - €2000 = €249.73', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €5000 at 3% per annum for 3 years.', '€463.64', '€613.64', '€450.00', '€5463.64', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 5000(1.03)^3 = €5463.64. Interest = €5463.64 - €5000 = €463.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €5000 at 3% per annum for 2 years.', '€304.50', '€300.00', '€454.50', '€5304.50', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 5000(1.03)^2 = €5304.50. Interest = €5304.50 - €5000 = €304.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €5000 at 3% per annum for 2 years.', '€304.50', '€300.00', '€454.50', '€5304.50', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 5000(1.03)^2 = €5304.50. Interest = €5304.50 - €5000 = €304.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €5000 at 3% per annum for 3 years.', '€450.00', '€463.64', '€5463.64', '€613.64', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 5000(1.03)^3 = €5463.64. Interest = €5463.64 - €5000 = €463.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €2000 at 4% per annum for 3 years.', '€2249.73', '€249.73', '€329.73', '€240.00', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 2000(1.04)^3 = €2249.73. Interest = €2249.73 - €2000 = €249.73', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €6000 at 5% per annum for 3 years.', '€6945.75', '€945.75', '€1245.75', '€900.00', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 6000(1.05)^3 = €6945.75. Interest = €6945.75 - €6000 = €945.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €5000 at 4% per annum for 2 years.', '€408.00', '€5408.00', '€400.00', '€608.00', 0,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 5000(1.04)^2 = €5408.00. Interest = €5408.00 - €5000 = €408.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned on €3000 at 4% per annum for 2 years.', '€240.00', '€3244.80', '€364.80', '€244.80', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Amount = 3000(1.04)^2 = €3244.80. Interest = €3244.80 - €3000 = €244.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€10.00', '€200.00', '€5.00', '€205.00', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €200.0. Compound interest = €205.00. Difference = €5.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€205.00', '€10.00', '€5.00', '€200.00', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €200.0. Compound interest = €205.00. Difference = €5.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€512.50', '€12.50', '€25.00', '€500.00', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €500.0. Compound interest = €512.50. Difference = €12.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€500.00', '€512.50', '€12.50', '€25.00', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €500.0. Compound interest = €512.50. Difference = €12.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€410.00', '€20.00', '€400.00', '€10.00', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €400.0. Compound interest = €410.00. Difference = €10.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€4000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€20.00', '€410.00', '€10.00', '€400.00', 2,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €400.0. Compound interest = €410.00. Difference = €10.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€205.00', '€10.00', '€200.00', '€5.00', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €200.0. Compound interest = €205.00. Difference = €5.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€25.00', '€500.00', '€512.50', '€12.50', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €500.0. Compound interest = €512.50. Difference = €12.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€512.50', '€12.50', '€500.00', '€25.00', 1,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €500.0. Compound interest = €512.50. Difference = €12.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2000 invested for 2 years at 5%. How much MORE is earned with compound interest than simple interest?', '€200.00', '€10.00', '€205.00', '€5.00', 3,
'lc_ol_financial', 6, 'developing', 'lc_ol', 'Simple interest = €200.0. Compound interest = €205.00. Difference = €5.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20000 depreciates by 25% per year. Find its value after 1 year.', 'Cannot determine', 'Cannot determine', '€15000.00', '€16000.00', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 20000 × (1 - 0.25)^1 = 20000 × 0.7500 = €15000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15000 depreciates by 10% per year. Find its value after 3 years.', '€11935.00', '€10500.00', '€10935.00', '€13500.00', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 15000 × (1 - 0.1)^3 = 15000 × 0.7290 = €10935.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15000 depreciates by 10% per year. Find its value after 3 years.', '€13500.00', '€10500.00', '€11935.00', '€10935.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 15000 × (1 - 0.1)^3 = 15000 × 0.7290 = €10935.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15000 depreciates by 20% per year. Find its value after 1 year.', 'Cannot determine', '€12000.00', 'Cannot determine', '€13000.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 15000 × (1 - 0.2)^1 = 15000 × 0.8000 = €12000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 10% per year. Find its value after 1 year.', 'Cannot determine', 'Cannot determine', '€27000.00', '€28000.00', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.1)^1 = 30000 × 0.9000 = €27000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 20% per year. Find its value after 3 years.', '€24000.00', '€15360.00', '€12000.00', '€16360.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.2)^3 = 30000 × 0.5120 = €15360.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 10% per year. Find its value after 2 years.', '€25300.00', '€24000.00', '€24300.00', '€27000.00', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.1)^2 = 30000 × 0.8100 = €24300.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10000 depreciates by 25% per year. Find its value after 3 years.', '€2500.00', '€7500.00', '€5218.75', '€4218.75', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 10000 × (1 - 0.25)^3 = 10000 × 0.4219 = €4218.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 25% per year. Find its value after 1 year.', '€23500.00', 'Cannot determine', 'Cannot determine', '€22500.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.25)^1 = 30000 × 0.7500 = €22500.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15000 depreciates by 20% per year. Find its value after 3 years.', '€8680.00', '€7680.00', '€6000.00', '€12000.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 15000 × (1 - 0.2)^3 = 15000 × 0.5120 = €7680.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 15% per year. Find its value after 1 year.', 'Cannot determine', '€26500.00', 'Cannot determine', '€25500.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.15)^1 = 30000 × 0.8500 = €25500.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20000 depreciates by 20% per year. Find its value after 1 year.', 'Cannot determine', 'Cannot determine', '€17000.00', '€16000.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 20000 × (1 - 0.2)^1 = 20000 × 0.8000 = €16000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25000 depreciates by 25% per year. Find its value after 2 years.', '€12500.00', '€14062.50', '€18750.00', '€15062.50', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 25000 × (1 - 0.25)^2 = 25000 × 0.5625 = €14062.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10000 depreciates by 10% per year. Find its value after 3 years.', '€8290.00', '€9000.00', '€7290.00', '€7000.00', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 10000 × (1 - 0.1)^3 = 10000 × 0.7290 = €7290.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25000 depreciates by 20% per year. Find its value after 1 year.', 'Cannot determine', 'Cannot determine', '€21000.00', '€20000.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 25000 × (1 - 0.2)^1 = 25000 × 0.8000 = €20000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20000 depreciates by 25% per year. Find its value after 1 year.', '€16000.00', '€15000.00', 'Cannot determine', 'Cannot determine', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 20000 × (1 - 0.25)^1 = 20000 × 0.7500 = €15000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 25% per year. Find its value after 2 years.', '€15000.00', '€22500.00', '€17875.00', '€16875.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.25)^2 = 30000 × 0.5625 = €16875.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25000 depreciates by 15% per year. Find its value after 3 years.', '€15353.12', '€16353.12', '€21250.00', '€13750.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 25000 × (1 - 0.15)^3 = 25000 × 0.6141 = €15353.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 20% per year. Find its value after 2 years.', '€20200.00', '€18000.00', '€19200.00', '€24000.00', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.2)^2 = 30000 × 0.6400 = €19200.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 15% per year. Find its value after 3 years.', '€19423.75', '€18423.75', '€25500.00', '€16500.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.15)^3 = 30000 × 0.6141 = €18423.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20000 depreciates by 10% per year. Find its value after 2 years.', '€17200.00', '€16200.00', '€18000.00', '€16000.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 20000 × (1 - 0.1)^2 = 20000 × 0.8100 = €16200.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30000 depreciates by 10% per year. Find its value after 2 years.', '€24300.00', '€27000.00', '€25300.00', '€24000.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 30000 × (1 - 0.1)^2 = 30000 × 0.8100 = €24300.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20000 depreciates by 15% per year. Find its value after 3 years.', '€17000.00', '€13282.50', '€11000.00', '€12282.50', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 20000 × (1 - 0.15)^3 = 20000 × 0.6141 = €12282.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25000 depreciates by 10% per year. Find its value after 1 year.', '€22500.00', 'Cannot determine', '€23500.00', 'Cannot determine', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 25000 × (1 - 0.1)^1 = 25000 × 0.9000 = €22500.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10000 depreciates by 15% per year. Find its value after 2 years.', '€8500.00', '€7225.00', '€7000.00', '€8225.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value = 10000 × (1 - 0.15)^2 = 10000 × 0.7225 = €7225.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24000 depreciates at 20% per year. Find the total depreciation after 2 years.', '€8640.00', '€15360.00', '€9600.00', '€4320.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €15360.00. Depreciation = €24000 - €15360.00 = €8640.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€13005.00', '€2497.50', '€5400.00', '€4995.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €13005.00. Depreciation = €18000 - €13005.00 = €4995.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €12000 depreciates at 20% per year. Find the total depreciation after 2 years.', '€4800.00', '€4320.00', '€7680.00', '€2160.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €7680.00. Depreciation = €12000 - €7680.00 = €4320.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€4995.00', '€2497.50', '€13005.00', '€5400.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €13005.00. Depreciation = €18000 - €13005.00 = €4995.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €12000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€1665.00', '€3600.00', '€8670.00', '€3330.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €8670.00. Depreciation = €12000 - €8670.00 = €3330.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €12000 depreciates at 20% per year. Find the total depreciation after 2 years.', '€2160.00', '€4320.00', '€7680.00', '€4800.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €7680.00. Depreciation = €12000 - €7680.00 = €4320.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24000 depreciates at 10% per year. Find the total depreciation after 2 years.', '€4800.00', '€4560.00', '€19440.00', '€2280.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €19440.00. Depreciation = €24000 - €19440.00 = €4560.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€4995.00', '€5400.00', '€13005.00', '€2497.50', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €13005.00. Depreciation = €18000 - €13005.00 = €4995.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€6660.00', '€17340.00', '€7200.00', '€3330.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €17340.00. Depreciation = €24000 - €17340.00 = €6660.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24000 depreciates at 10% per year. Find the total depreciation after 2 years.', '€19440.00', '€4800.00', '€4560.00', '€2280.00', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €19440.00. Depreciation = €24000 - €19440.00 = €4560.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€4995.00', '€5400.00', '€2497.50', '€13005.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €13005.00. Depreciation = €18000 - €13005.00 = €4995.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€2497.50', '€5400.00', '€13005.00', '€4995.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €13005.00. Depreciation = €18000 - €13005.00 = €4995.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €12000 depreciates at 10% per year. Find the total depreciation after 2 years.', '€2280.00', '€1140.00', '€2400.00', '€9720.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €9720.00. Depreciation = €12000 - €9720.00 = €2280.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€5400.00', '€13005.00', '€4995.00', '€2497.50', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €13005.00. Depreciation = €18000 - €13005.00 = €4995.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24000 depreciates at 15% per year. Find the total depreciation after 2 years.', '€6660.00', '€7200.00', '€3330.00', '€17340.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Value after 2 years = €17340.00. Depreciation = €24000 - €17340.00 = €6660.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €8000. What was its original value?', 'Cannot determine', '€9600.00', '€11000.00', '€10000.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €8000 ÷ 0.8 = €10000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €16000. What was its original value?', '€19200.00', '€20000.00', '€21000.00', 'Cannot determine', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €16000 ÷ 0.8 = €20000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €12000. What was its original value?', '€14400.00', '€16000.00', '€15000.00', 'Cannot determine', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €12000 ÷ 0.8 = €15000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €16000. What was its original value?', 'Cannot determine', '€20000.00', '€21000.00', '€19200.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €16000 ÷ 0.8 = €20000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €20000. What was its original value?', '€24000.00', '€25000.00', '€26000.00', 'Cannot determine', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €20000 ÷ 0.8 = €25000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €8000. What was its original value?', '€9600.00', 'Cannot determine', '€11000.00', '€10000.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €8000 ÷ 0.8 = €10000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €8000. What was its original value?', '€9600.00', '€11000.00', 'Cannot determine', '€10000.00', 3,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €8000 ÷ 0.8 = €10000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €20000. What was its original value?', '€25000.00', 'Cannot determine', '€26000.00', '€24000.00', 0,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €20000 ÷ 0.8 = €25000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €16000. What was its original value?', '€21000.00', '€19200.00', '€20000.00', 'Cannot determine', 2,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €16000 ÷ 0.8 = €20000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 1 year of 20% depreciation, a machine is worth €16000. What was its original value?', 'Cannot determine', '€20000.00', '€19200.00', '€21000.00', 1,
'lc_ol_financial', 7, 'proficient', 'lc_ol', 'Original = Current ÷ (1 - 0.2) = €16000 ÷ 0.8 = €20000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €30000 at a rate of 20%.', '€24000.00', '€3000.00', '€6000', '€7500.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €30000 = €6000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€8750.00', '€7000', '€28000.00', '€3500.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€3500.00', '€7000', '€28000.00', '€8750.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €25000 at a rate of 20%.', '€20000.00', '€6250.00', '€2500.00', '€5000', 3,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €25000 = €5000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€28000.00', '€7000', '€3500.00', '€8750.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€8750.00', '€3500.00', '€28000.00', '€7000', 3,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €40000 at a rate of 20%.', '€32000.00', '€10000.00', '€8000', '€4000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €40000 = €8000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €30000 at a rate of 20%.', '€24000.00', '€3000.00', '€6000', '€7500.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €30000 = €6000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €30000 at a rate of 20%.', '€3000.00', '€6000', '€7500.00', '€24000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €30000 = €6000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€8750.00', '€3500.00', '€7000', '€28000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€8750.00', '€3500.00', '€28000.00', '€7000', 3,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €30000 at a rate of 20%.', '€7500.00', '€6000', '€24000.00', '€3000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €30000 = €6000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €30000 at a rate of 20%.', '€24000.00', '€6000', '€3000.00', '€7500.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €30000 = €6000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€28000.00', '€3500.00', '€8750.00', '€7000', 3,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€8750.00', '€7000', '€3500.00', '€28000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €30000 at a rate of 20%.', '€7500.00', '€3000.00', '€6000', '€24000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €30000 = €6000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€8750.00', '€3500.00', '€7000', '€28000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €40000 at a rate of 20%.', '€10000.00', '€4000.00', '€8000', '€32000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €40000 = €8000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €35000 at a rate of 20%.', '€7000', '€28000.00', '€8750.00', '€3500.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €35000 = €7000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the income tax on €30000 at a rate of 20%.', '€7500.00', '€24000.00', '€3000.00', '€6000', 3,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = 20% of €30000 = €6000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €40000 gross. After 20% tax, what is the net pay?', '€31000.00', '€48000.00', '€32000', '€8000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €8000.0. Net pay = €40000 - €8000.0 = €32000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €40000 gross. After 20% tax, what is the net pay?', '€32000', '€31000.00', '€8000.00', '€48000.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €8000.0. Net pay = €40000 - €8000.0 = €32000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €45000 gross. After 20% tax, what is the net pay?', '€54000.00', '€36000', '€9000.00', '€35000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €9000.0. Net pay = €45000 - €9000.0 = €36000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €45000 gross. After 20% tax, what is the net pay?', '€35000.00', '€36000', '€9000.00', '€54000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €9000.0. Net pay = €45000 - €9000.0 = €36000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €45000 gross. After 20% tax, what is the net pay?', '€54000.00', '€35000.00', '€36000', '€9000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €9000.0. Net pay = €45000 - €9000.0 = €36000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €40000 gross. After 20% tax, what is the net pay?', '€8000.00', '€32000', '€31000.00', '€48000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €8000.0. Net pay = €40000 - €8000.0 = €32000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €35000 gross. After 20% tax, what is the net pay?', '€42000.00', '€28000', '€7000.00', '€27000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €7000.0. Net pay = €35000 - €7000.0 = €28000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €45000 gross. After 20% tax, what is the net pay?', '€36000', '€9000.00', '€54000.00', '€35000.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €9000.0. Net pay = €45000 - €9000.0 = €36000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €50000 gross. After 20% tax, what is the net pay?', '€40000', '€10000.00', '€39000.00', '€60000.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €10000.0. Net pay = €50000 - €10000.0 = €40000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €40000 gross. After 20% tax, what is the net pay?', '€31000.00', '€32000', '€8000.00', '€48000.00', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €8000.0. Net pay = €40000 - €8000.0 = €32000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €45000 gross. After 20% tax, what is the net pay?', '€54000.00', '€9000.00', '€36000', '€35000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €9000.0. Net pay = €45000 - €9000.0 = €36000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €45000 gross. After 20% tax, what is the net pay?', '€35000.00', '€9000.00', '€36000', '€54000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €9000.0. Net pay = €45000 - €9000.0 = €36000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €50000 gross. After 20% tax, what is the net pay?', '€40000', '€10000.00', '€60000.00', '€39000.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €10000.0. Net pay = €50000 - €10000.0 = €40000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €35000 gross. After 20% tax, what is the net pay?', '€7000.00', '€27000.00', '€28000', '€42000.00', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €7000.0. Net pay = €35000 - €7000.0 = €28000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €35000 gross. After 20% tax, what is the net pay?', '€28000', '€27000.00', '€7000.00', '€42000.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'Tax = €7000.0. Net pay = €35000 - €7000.0 = €28000.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €30000.', '€469.82', '€419.82', '€600.00', '€60.06', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €17988) = €60.06 + €359.76 = €419.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €25000.', '€500.00', '€319.82', '€60.06', '€369.82', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €12988) = €60.06 + €259.76 = €319.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €22000.', '€440.00', '€309.82', '€60.06', '€259.82', 3,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €9988) = €60.06 + €199.76 = €259.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €30000.', '€600.00', '€419.82', '€60.06', '€469.82', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €17988) = €60.06 + €359.76 = €419.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €18000.', '€360.00', '€60.06', '€229.82', '€179.82', 3,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €5988) = €60.06 + €119.76 = €179.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €18000.', '€179.82', '€60.06', '€229.82', '€360.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €5988) = €60.06 + €119.76 = €179.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €22000.', '€259.82', '€60.06', '€440.00', '€309.82', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €9988) = €60.06 + €199.76 = €259.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €18000.', '€179.82', '€360.00', '€229.82', '€60.06', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €5988) = €60.06 + €119.76 = €179.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €22000.', '€309.82', '€440.00', '€259.82', '€60.06', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €9988) = €60.06 + €199.76 = €259.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €30000.', '€60.06', '€419.82', '€600.00', '€469.82', 1,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €17988) = €60.06 + €359.76 = €419.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €25000.', '€319.82', '€369.82', '€500.00', '€60.06', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €12988) = €60.06 + €259.76 = €319.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €18000.', '€179.82', '€60.06', '€229.82', '€360.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €5988) = €60.06 + €119.76 = €179.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €30000.', '€419.82', '€60.06', '€469.82', '€600.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €17988) = €60.06 + €359.76 = €419.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €30000.', '€60.06', '€600.00', '€419.82', '€469.82', 2,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €17988) = €60.06 + €359.76 = €419.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('USC is charged at 0.5% on the first €12012 and 2% on the balance. Calculate USC on €25000.', '€319.82', '€369.82', '€60.06', '€500.00', 0,
'lc_ol_financial', 8, 'proficient', 'lc_ol', 'USC = (0.5% of €12012) + (2% of €12988) = €60.06 + €259.76 = €319.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €250 to Swiss Francs at a rate of €1 = 0.95 CHF.', '263.16 CHF', '487.50 CHF', '237.50 CHF', '95.00 CHF', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€250 × 0.95 = 237.50 CHF', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €300 to Australian Dollars at a rate of €1 = 1.63 AUD.', '163.00 AUD', '489.00 AUD', '184.05 AUD', '789.00 AUD', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€300 × 1.63 = 489.00 AUD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €500 to US Dollars at a rate of €1 = 1.11 USD.', '555.00 USD', '111.00 USD', '1055.00 USD', '450.45 USD', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€500 × 1.11 = 555.00 USD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €100 to Swiss Francs at a rate of €1 = 0.97 CHF.', '97.00 CHF', '197.00 CHF', '103.09 CHF', 'Cannot determine', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€100 × 0.97 = 97.00 CHF', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €400 to Japanese Yen at a rate of €1 = 157.67 JPY.', '63468.00 JPY', '15767.00 JPY', '2.54 JPY', '63068.00 JPY', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€400 × 157.67 = 63068.00 JPY', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €400 to Japanese Yen at a rate of €1 = 157.83 JPY.', '2.53 JPY', '15783.00 JPY', '63132.00 JPY', '63532.00 JPY', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€400 × 157.83 = 63132.00 JPY', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €100 to Australian Dollars at a rate of €1 = 1.64 AUD.', '264.00 AUD', '60.98 AUD', '164.00 AUD', 'Cannot determine', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€100 × 1.64 = 164.00 AUD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €500 to US Dollars at a rate of €1 = 1.11 USD.', '1055.00 USD', '555.00 USD', '450.45 USD', '111.00 USD', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€500 × 1.11 = 555.00 USD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €300 to Swiss Francs at a rate of €1 = 0.97 CHF.', '591.00 CHF', '291.00 CHF', '97.00 CHF', '309.28 CHF', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€300 × 0.97 = 291.00 CHF', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €400 to British Pounds at a rate of €1 = 0.86 GBP.', '86.00 GBP', '744.00 GBP', '344.00 GBP', '465.12 GBP', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€400 × 0.86 = 344.00 GBP', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €250 to British Pounds at a rate of €1 = 0.87 GBP.', '217.50 GBP', '287.36 GBP', '467.50 GBP', '87.00 GBP', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€250 × 0.87 = 217.50 GBP', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €400 to Japanese Yen at a rate of €1 = 157.21 JPY.', '15721.00 JPY', '62884.00 JPY', '2.54 JPY', '63284.00 JPY', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€400 × 157.21 = 62884.00 JPY', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €200 to Australian Dollars at a rate of €1 = 1.64 AUD.', '164.00 AUD', '528.00 AUD', '328.00 AUD', '121.95 AUD', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€200 × 1.64 = 328.00 AUD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €400 to Japanese Yen at a rate of €1 = 160.41 JPY.', '64164.00 JPY', '64564.00 JPY', '16041.00 JPY', '2.49 JPY', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€400 × 160.41 = 64164.00 JPY', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €300 to British Pounds at a rate of €1 = 0.85 GBP.', '255.00 GBP', '85.00 GBP', '555.00 GBP', '352.94 GBP', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€300 × 0.85 = 255.00 GBP', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €200 to British Pounds at a rate of €1 = 0.88 GBP.', '227.27 GBP', '88.00 GBP', '376.00 GBP', '176.00 GBP', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€200 × 0.88 = 176.00 GBP', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €400 to Japanese Yen at a rate of €1 = 155.54 JPY.', '15554.00 JPY', '62216.00 JPY', '2.57 JPY', '62616.00 JPY', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€400 × 155.54 = 62216.00 JPY', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €300 to US Dollars at a rate of €1 = 1.09 USD.', '627.00 USD', '327.00 USD', '275.23 USD', '109.00 USD', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€300 × 1.09 = 327.00 USD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €200 to Japanese Yen at a rate of €1 = 157.57 JPY.', '1.27 JPY', '15757.00 JPY', '31514.00 JPY', '31714.00 JPY', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€200 × 157.57 = 31514.00 JPY', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert €250 to Japanese Yen at a rate of €1 = 161.2 JPY.', '40550.00 JPY', '1.55 JPY', '40300.00 JPY', '16120.00 JPY', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '€250 × 161.2 = 40300.00 JPY', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 300 USD to Euro at a rate of €1 = 1.08 USD.', '€277.78', '€327.78', '€324.00', '€300.00', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '300 USD ÷ 1.08 = €277.78', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 10000 JPY to Euro at a rate of €1 = 158.44 JPY.', '€63.12', '€10000.00', '€1584400.00', '€113.12', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '10000 JPY ÷ 158.44 = €63.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 150 CHF to Euro at a rate of €1 = 0.98 CHF.', '€203.06', '€147.00', '€150.00', '€153.06', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '150 CHF ÷ 0.98 = €153.06', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 200 GBP to Euro at a rate of €1 = 0.86 GBP.', '€282.56', '€200.00', '€232.56', '€172.00', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '200 GBP ÷ 0.86 = €232.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 150 GBP to Euro at a rate of €1 = 0.86 GBP.', '€150.00', '€129.00', '€224.42', '€174.42', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '150 GBP ÷ 0.86 = €174.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 100 GBP to Euro at a rate of €1 = 0.85 GBP.', '€117.65', '€167.65', '€100.00', '€85.00', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '100 GBP ÷ 0.85 = €117.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 200 GBP to Euro at a rate of €1 = 0.87 GBP.', '€174.00', '€200.00', '€279.89', '€229.89', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '200 GBP ÷ 0.87 = €229.89', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 150 USD to Euro at a rate of €1 = 1.09 USD.', '€150.00', '€137.61', '€163.50', '€187.61', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '150 USD ÷ 1.09 = €137.61', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 150 USD to Euro at a rate of €1 = 1.11 USD.', '€185.14', '€150.00', '€166.50', '€135.14', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '150 USD ÷ 1.11 = €135.14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 250 USD to Euro at a rate of €1 = 1.08 USD.', '€270.00', '€250.00', '€231.48', '€281.48', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '250 USD ÷ 1.08 = €231.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 150 CHF to Euro at a rate of €1 = 0.97 CHF.', '€154.64', '€150.00', '€204.64', '€145.50', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '150 CHF ÷ 0.97 = €154.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 10000 JPY to Euro at a rate of €1 = 155.28 JPY.', '€10000.00', '€64.40', '€114.40', '€1552800.00', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '10000 JPY ÷ 155.28 = €64.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 300 AUD to Euro at a rate of €1 = 1.64 AUD.', '€492.00', '€300.00', '€182.93', '€232.93', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '300 AUD ÷ 1.64 = €182.93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 100 AUD to Euro at a rate of €1 = 1.63 AUD.', '€61.35', '€111.35', '€163.00', '€100.00', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '100 AUD ÷ 1.63 = €61.35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 15000 JPY to Euro at a rate of €1 = 158.51 JPY.', '€144.63', '€2377650.00', '€94.63', '€15000.00', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '15000 JPY ÷ 158.51 = €94.63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 100 GBP to Euro at a rate of €1 = 0.87 GBP.', '€87.00', '€164.94', '€114.94', '€100.00', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '100 GBP ÷ 0.87 = €114.94', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 300 AUD to Euro at a rate of €1 = 1.66 AUD.', '€230.72', '€498.00', '€180.72', '€300.00', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '300 AUD ÷ 1.66 = €180.72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 150 CHF to Euro at a rate of €1 = 0.96 CHF.', '€206.25', '€150.00', '€156.25', '€144.00', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '150 CHF ÷ 0.96 = €156.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 300 AUD to Euro at a rate of €1 = 1.63 AUD.', '€300.00', '€184.05', '€489.00', '€234.05', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '300 AUD ÷ 1.63 = €184.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 100 GBP to Euro at a rate of €1 = 0.86 GBP.', '€116.28', '€100.00', '€166.28', '€86.00', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', '100 GBP ÷ 0.86 = €116.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 5% commission. How many USD do you get for €200 at €1 = $1.1?', '$209.00', 'Cannot determine', '$220.00', '$190.00', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €10.0. Amount = €190.0. USD = 190.0 × 1.1 = $209.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 5% commission. How many USD do you get for €400 at €1 = $1.1?', 'Cannot determine', '$380.00', '$418.00', '$440.00', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €20.0. Amount = €380.0. USD = 380.0 × 1.1 = $418.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 2% commission. How many USD do you get for €400 at €1 = $1.1?', '$440.00', '$392.00', 'Cannot determine', '$431.20', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €8.0. Amount = €392.0. USD = 392.0 × 1.1 = $431.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 2% commission. How many USD do you get for €300 at €1 = $1.1?', '$323.40', '$330.00', 'Cannot determine', '$294.00', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €6.0. Amount = €294.0. USD = 294.0 × 1.1 = $323.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 2% commission. How many USD do you get for €500 at €1 = $1.1?', 'Cannot determine', '$539.00', '$490.00', '$550.00', 1,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €10.0. Amount = €490.0. USD = 490.0 × 1.1 = $539.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 5% commission. How many USD do you get for €500 at €1 = $1.1?', '$550.00', 'Cannot determine', '$475.00', '$522.50', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €25.0. Amount = €475.0. USD = 475.0 × 1.1 = $522.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 3% commission. How many USD do you get for €500 at €1 = $1.1?', '$485.00', 'Cannot determine', '$533.50', '$550.00', 2,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €15.0. Amount = €485.0. USD = 485.0 × 1.1 = $533.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 3% commission. How many USD do you get for €300 at €1 = $1.1?', '$320.10', 'Cannot determine', '$291.00', '$330.00', 0,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €9.0. Amount = €291.0. USD = 291.0 × 1.1 = $320.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 2% commission. How many USD do you get for €500 at €1 = $1.1?', 'Cannot determine', '$490.00', '$550.00', '$539.00', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €10.0. Amount = €490.0. USD = 490.0 × 1.1 = $539.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bureau charges 5% commission. How many USD do you get for €500 at €1 = $1.1?', 'Cannot determine', '$550.00', '$475.00', '$522.50', 3,
'lc_ol_financial', 9, 'proficient', 'lc_ol', 'Commission = €25.0. Amount = €475.0. USD = 475.0 × 1.1 = $522.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €15 per hour for a 35-hour week. Calculate their weekly wage.', '€525', '€450.00', '€540.00', '€50.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 15 × 35 = €525', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €15 per hour for a 38-hour week. Calculate their weekly wage.', '€570', '€585.00', '€53.00', '€495.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 15 × 38 = €570', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €18 per hour for a 37.5-hour week. Calculate their weekly wage.', '€693.00', '€585.00', '€55.50', '€675', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 18 × 37.5 = €675.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20 per hour for a 39-hour week. Calculate their weekly wage.', '€680.00', '€780', '€800.00', '€59.00', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 20 × 39 = €780', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €13 per hour for a 39-hour week. Calculate their weekly wage.', '€507', '€520.00', '€52.00', '€442.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 13 × 39 = €507', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €16 per hour for a 40-hour week. Calculate their weekly wage.', '€56.00', '€560.00', '€640', '€656.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 16 × 40 = €640', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €15 per hour for a 37.5-hour week. Calculate their weekly wage.', '€487.50', '€577.50', '€562.50', '€52.50', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 15 × 37.5 = €562.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €14 per hour for a 40-hour week. Calculate their weekly wage.', '€574.00', '€490.00', '€54.00', '€560', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 14 × 40 = €560', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €12 per hour for a 38-hour week. Calculate their weekly wage.', '€50.00', '€396.00', '€456', '€468.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 12 × 38 = €456', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €16 per hour for a 37.5-hour week. Calculate their weekly wage.', '€520.00', '€616.00', '€600', '€53.50', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 16 × 37.5 = €600.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20 per hour for a 38-hour week. Calculate their weekly wage.', '€760', '€780.00', '€660.00', '€58.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 20 × 38 = €760', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20 per hour for a 35-hour week. Calculate their weekly wage.', '€700', '€720.00', '€55.00', '€600.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 20 × 35 = €700', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €18 per hour for a 39-hour week. Calculate their weekly wage.', '€57.00', '€612.00', '€720.00', '€702', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 18 × 39 = €702', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €12 per hour for a 35-hour week. Calculate their weekly wage.', '€360.00', '€432.00', '€420', '€47.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 12 × 35 = €420', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €13 per hour for a 35-hour week. Calculate their weekly wage.', '€390.00', '€48.00', '€455', '€468.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Weekly wage = 13 × 35 = €455', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €14/hour for 40 hours, plus time-and-a-half for 6 hours overtime. Find total pay.', '€644.00', '€812.00', '€560.00', '€686', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €560. Overtime = 6 × €21.0 = €126.0. Total = €686.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €16/hour for 40 hours, plus time-and-a-half for 8 hours overtime. Find total pay.', '€832', '€1024.00', '€768.00', '€640.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €640. Overtime = 8 × €24.0 = €192.0. Total = €832.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €16/hour for 40 hours, plus time-and-a-half for 6 hours overtime. Find total pay.', '€736.00', '€784', '€928.00', '€640.00', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €640. Overtime = 6 × €24.0 = €144.0. Total = €784.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €18/hour for 40 hours, plus time-and-a-half for 10 hours overtime. Find total pay.', '€990', '€720.00', '€1260.00', '€900.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €720. Overtime = 10 × €27.0 = €270.0. Total = €990.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €16/hour for 40 hours, plus time-and-a-half for 4 hours overtime. Find total pay.', '€640.00', '€736', '€832.00', '€704.00', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €640. Overtime = 4 × €24.0 = €96.0. Total = €736.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €18/hour for 40 hours, plus time-and-a-half for 8 hours overtime. Find total pay.', '€936', '€864.00', '€1152.00', '€720.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €720. Overtime = 8 × €27.0 = €216.0. Total = €936.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, plus time-and-a-half for 6 hours overtime. Find total pay.', '€1160.00', '€800.00', '€980', '€920.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime = 6 × €30.0 = €180.0. Total = €980.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €15/hour for 40 hours, plus time-and-a-half for 8 hours overtime. Find total pay.', '€720.00', '€600.00', '€960.00', '€780', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €600. Overtime = 8 × €22.5 = €180.0. Total = €780.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, plus time-and-a-half for 10 hours overtime. Find total pay.', '€800.00', '€1400.00', '€1100', '€1000.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime = 10 × €30.0 = €300.0. Total = €1100.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €14/hour for 40 hours, plus time-and-a-half for 10 hours overtime. Find total pay.', '€770', '€560.00', '€980.00', '€700.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €560. Overtime = 10 × €21.0 = €210.0. Total = €770.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €14/hour for 40 hours, plus time-and-a-half for 10 hours overtime. Find total pay.', '€770', '€700.00', '€980.00', '€560.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €560. Overtime = 10 × €21.0 = €210.0. Total = €770.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €14/hour for 40 hours, plus time-and-a-half for 10 hours overtime. Find total pay.', '€980.00', '€770', '€560.00', '€700.00', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €560. Overtime = 10 × €21.0 = €210.0. Total = €770.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €18/hour for 40 hours, plus time-and-a-half for 6 hours overtime. Find total pay.', '€1044.00', '€828.00', '€882', '€720.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €720. Overtime = 6 × €27.0 = €162.0. Total = €882.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €15/hour for 40 hours, plus time-and-a-half for 5 hours overtime. Find total pay.', '€600.00', '€825.00', '€712.50', '€675.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €600. Overtime = 5 × €22.5 = €112.5. Total = €712.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, plus time-and-a-half for 5 hours overtime. Find total pay.', '€900.00', '€1100.00', '€800.00', '€950', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime = 5 × €30.0 = €150.0. Total = €950.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €18/hour for 40 hours, plus time-and-a-half for 5 hours overtime. Find total pay.', '€810.00', '€720.00', '€990.00', '€855', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €720. Overtime = 5 × €27.0 = €135.0. Total = €855.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €16/hour for 40 hours, plus time-and-a-half for 6 hours overtime. Find total pay.', '€640.00', '€928.00', '€784', '€736.00', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €640. Overtime = 6 × €24.0 = €144.0. Total = €784.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €18/hour for 40 hours, plus time-and-a-half for 10 hours overtime. Find total pay.', '€990', '€1260.00', '€720.00', '€900.00', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €720. Overtime = 10 × €27.0 = €270.0. Total = €990.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €14/hour for 40 hours, plus time-and-a-half for 6 hours overtime. Find total pay.', '€812.00', '€686', '€560.00', '€644.00', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €560. Overtime = 6 × €21.0 = €126.0. Total = €686.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €15/hour for 40 hours, plus time-and-a-half for 5 hours overtime. Find total pay.', '€600.00', '€825.00', '€675.00', '€712.50', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €600. Overtime = 5 × €22.5 = €112.5. Total = €712.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €950. How many overtime hours?', '5 hours', '10 hours', 'Cannot determine', '7 hours', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €950 - €800 = €150. Hours = 150 ÷ 30.0 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €1010. How many overtime hours?', '7 hours', '14 hours', '9 hours', '10 hours', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €1010 - €800 = €210. Hours = 210 ÷ 30.0 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €920. How many overtime hours?', '4 hours', 'Cannot determine', '8 hours', '6 hours', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €920 - €800 = €120. Hours = 120 ÷ 30.0 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €920. How many overtime hours?', '8 hours', 'Cannot determine', '6 hours', '4 hours', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €920 - €800 = €120. Hours = 120 ÷ 30.0 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €980. How many overtime hours?', '9 hours', '6 hours', '8 hours', '12 hours', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €980 - €800 = €180. Hours = 180 ÷ 30.0 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €1010. How many overtime hours?', '7 hours', '9 hours', '14 hours', '10 hours', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €1010 - €800 = €210. Hours = 210 ÷ 30.0 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €980. How many overtime hours?', '8 hours', '6 hours', '12 hours', '9 hours', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €980 - €800 = €180. Hours = 180 ÷ 30.0 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €920. How many overtime hours?', '4 hours', 'Cannot determine', '6 hours', '8 hours', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €920 - €800 = €120. Hours = 120 ÷ 30.0 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €1040. How many overtime hours?', '12 hours', '8 hours', '10 hours', '16 hours', 1,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €1040 - €800 = €240. Hours = 240 ÷ 30.0 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €1010. How many overtime hours?', '14 hours', '9 hours', '7 hours', '10 hours', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €1010 - €800 = €210. Hours = 210 ÷ 30.0 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €920. How many overtime hours?', '4 hours', 'Cannot determine', '8 hours', '6 hours', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €920 - €800 = €120. Hours = 120 ÷ 30.0 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €1010. How many overtime hours?', '10 hours', '14 hours', '7 hours', '9 hours', 2,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €1010 - €800 = €210. Hours = 210 ÷ 30.0 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €920. How many overtime hours?', '4 hours', '6 hours', '8 hours', 'Cannot determine', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €920 - €800 = €120. Hours = 120 ÷ 30.0 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €1040. How many overtime hours?', '8 hours', '12 hours', '10 hours', '16 hours', 0,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €1040 - €800 = €240. Hours = 240 ÷ 30.0 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A worker earns €20/hour for 40 hours, time-and-a-half for overtime. Total pay is €920. How many overtime hours?', '6 hours', 'Cannot determine', '8 hours', '4 hours', 3,
'lc_ol_financial', 10, 'advanced', 'lc_ol', 'Basic = €800. Overtime pay = €920 - €800 = €120. Hours = 120 ÷ 30.0 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €150. After a 15% discount, 23% VAT is added. Find the final price.', '€156.82', '€162.00', 'Cannot determine', '€127.50', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 15% off: €127.50. After VAT: €127.50 × 1.23 = €156.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 20% discount, 23% VAT is added. Find the final price.', '€196.80', 'Cannot determine', '€160.00', '€206.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 20% off: €160.00. After VAT: €160.00 × 1.23 = €196.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 25% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€196.00', '€150.00', '€184.50', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €150.00. After VAT: €150.00 × 1.23 = €184.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €150. After a 20% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€120.00', '€154.50', '€147.60', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 20% off: €120.00. After VAT: €120.00 × 1.23 = €147.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €150. After a 25% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€112.50', '€147.00', '€138.38', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €112.50. After VAT: €112.50 × 1.23 = €138.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 15% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€170.00', '€209.10', '€216.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 15% off: €170.00. After VAT: €170.00 × 1.23 = €209.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €300. After a 20% discount, 23% VAT is added. Find the final price.', '€240.00', '€295.20', 'Cannot determine', '€309.00', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 20% off: €240.00. After VAT: €240.00 × 1.23 = €295.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €100. After a 20% discount, 23% VAT is added. Find the final price.', '€103.00', 'Cannot determine', '€80.00', '€98.40', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 20% off: €80.00. After VAT: €80.00 × 1.23 = €98.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €300. After a 25% discount, 23% VAT is added. Find the final price.', '€276.75', 'Cannot determine', '€294.00', '€225.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €225.00. After VAT: €225.00 × 1.23 = €276.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €150. After a 20% discount, 23% VAT is added. Find the final price.', '€147.60', 'Cannot determine', '€120.00', '€154.50', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 20% off: €120.00. After VAT: €120.00 × 1.23 = €147.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €300. After a 25% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€294.00', '€225.00', '€276.75', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €225.00. After VAT: €225.00 × 1.23 = €276.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €250. After a 25% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€187.50', '€245.00', '€230.62', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €187.50. After VAT: €187.50 × 1.23 = €230.62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 25% discount, 23% VAT is added. Find the final price.', '€184.50', '€150.00', 'Cannot determine', '€196.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €150.00. After VAT: €150.00 × 1.23 = €184.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €100. After a 25% discount, 23% VAT is added. Find the final price.', '€75.00', 'Cannot determine', '€92.25', '€98.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €75.00. After VAT: €75.00 × 1.23 = €92.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 10% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€221.40', '€226.00', '€180.00', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 10% off: €180.00. After VAT: €180.00 × 1.23 = €221.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €100. After a 15% discount, 23% VAT is added. Find the final price.', '€104.55', '€85.00', '€108.00', 'Cannot determine', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 15% off: €85.00. After VAT: €85.00 × 1.23 = €104.55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 25% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€184.50', '€196.00', '€150.00', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €150.00. After VAT: €150.00 × 1.23 = €184.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 25% discount, 23% VAT is added. Find the final price.', '€150.00', '€196.00', '€184.50', 'Cannot determine', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 25% off: €150.00. After VAT: €150.00 × 1.23 = €184.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €200. After a 10% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€180.00', '€221.40', '€226.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 10% off: €180.00. After VAT: €180.00 × 1.23 = €221.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item costs €150. After a 15% discount, 23% VAT is added. Find the final price.', 'Cannot determine', '€156.82', '€162.00', '€127.50', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After 15% off: €127.50. After VAT: €127.50 × 1.23 = €156.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €800 increases by 10%, then decreases by 20%. Find the final price.', '€704.00', '€720.00', '€880.00', '€800.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +10%: €880.00. After -20%: €704.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €1000 increases by 25%, then decreases by 20%. Find the final price.', '€1250.00', 'Cannot determine', '€1000.00', '€1050.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +25%: €1250.00. After -20%: €1000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €500 increases by 25%, then decreases by 20%. Find the final price.', 'Cannot determine', '€500.00', '€525.00', '€625.00', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +25%: €625.00. After -20%: €500.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €500 increases by 25%, then decreases by 10%. Find the final price.', '€500.00', '€625.00', '€562.50', '€575.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +25%: €625.00. After -10%: €562.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €600 increases by 20%, then decreases by 20%. Find the final price.', 'Cannot determine', '€720.00', '€576.00', '€600.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +20%: €720.00. After -20%: €576.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €800 increases by 10%, then decreases by 20%. Find the final price.', '€880.00', '€704.00', '€720.00', '€800.00', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +10%: €880.00. After -20%: €704.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €600 increases by 10%, then decreases by 20%. Find the final price.', '€600.00', '€660.00', '€540.00', '€528.00', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +10%: €660.00. After -20%: €528.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €500 increases by 25%, then decreases by 10%. Find the final price.', '€562.50', '€500.00', '€625.00', '€575.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +25%: €625.00. After -10%: €562.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €500 increases by 20%, then decreases by 10%. Find the final price.', '€550.00', '€600.00', '€500.00', '€540.00', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +20%: €600.00. After -10%: €540.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €800 increases by 25%, then decreases by 10%. Find the final price.', '€920.00', '€900.00', '€800.00', '€1000.00', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +25%: €1000.00. After -10%: €900.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €800 increases by 25%, then decreases by 10%. Find the final price.', '€800.00', '€1000.00', '€920.00', '€900.00', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +25%: €1000.00. After -10%: €900.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €500 increases by 25%, then decreases by 10%. Find the final price.', '€500.00', '€575.00', '€625.00', '€562.50', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +25%: €625.00. After -10%: €562.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €1000 increases by 10%, then decreases by 10%. Find the final price.', '€1000.00', '€990.00', '€1100.00', 'Cannot determine', 1,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +10%: €1100.00. After -10%: €990.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €600 increases by 20%, then decreases by 20%. Find the final price.', '€600.00', '€720.00', '€576.00', 'Cannot determine', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +20%: €720.00. After -20%: €576.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A price of €1000 increases by 20%, then decreases by 20%. Find the final price.', 'Cannot determine', '€1200.00', '€1000.00', '€960.00', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'After +20%: €1200.00. After -20%: €960.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €1000 is sold at 30% markup. If expenses are €50, what is the net profit?', 'Cannot determine', '€1300.00', '€300.00', '€250', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1300.00. Net profit = €1300.00 - €1000 - €50 = €250.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €500 is sold at 30% markup. If expenses are €50, what is the net profit?', '€650.00', 'Cannot determine', '€150.00', '€100', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €650.00. Net profit = €650.00 - €500 - €50 = €100.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €500 is sold at 40% markup. If expenses are €50, what is the net profit?', '€700.00', '€200.00', 'Cannot determine', '€150', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €700.00. Net profit = €700.00 - €500 - €50 = €150.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €1000 is sold at 50% markup. If expenses are €100, what is the net profit?', 'Cannot determine', '€1500.00', '€400', '€500.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1500.00. Net profit = €1500.00 - €1000 - €100 = €400.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €1000 is sold at 30% markup. If expenses are €100, what is the net profit?', 'Cannot determine', '€300.00', '€1300.00', '€200', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1300.00. Net profit = €1300.00 - €1000 - €100 = €200.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €500 is sold at 30% markup. If expenses are €50, what is the net profit?', '€100', 'Cannot determine', '€150.00', '€650.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €650.00. Net profit = €650.00 - €500 - €50 = €100.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €500 is sold at 50% markup. If expenses are €80, what is the net profit?', '€170', 'Cannot determine', '€750.00', '€250.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €750.00. Net profit = €750.00 - €500 - €80 = €170.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €1000 is sold at 30% markup. If expenses are €100, what is the net profit?', '€200', '€1300.00', '€300.00', 'Cannot determine', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1300.00. Net profit = €1300.00 - €1000 - €100 = €200.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €1200 is sold at 50% markup. If expenses are €100, what is the net profit?', 'Cannot determine', '€600.00', '€500', '€1800.00', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1800.00. Net profit = €1800.00 - €1200 - €100 = €500.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €1200 is sold at 30% markup. If expenses are €50, what is the net profit?', '€360.00', 'Cannot determine', '€1560.00', '€310', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1560.00. Net profit = €1560.00 - €1200 - €50 = €310.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €500 is sold at 40% markup. If expenses are €100, what is the net profit?', '€100', 'Cannot determine', '€700.00', '€200.00', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €700.00. Net profit = €700.00 - €500 - €100 = €100.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €800 is sold at 50% markup. If expenses are €80, what is the net profit?', '€400.00', '€1200.00', 'Cannot determine', '€320', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1200.00. Net profit = €1200.00 - €800 - €80 = €320.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €500 is sold at 40% markup. If expenses are €100, what is the net profit?', '€100', '€200.00', '€700.00', 'Cannot determine', 0,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €700.00. Net profit = €700.00 - €500 - €100 = €100.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €500 is sold at 50% markup. If expenses are €80, what is the net profit?', '€250.00', '€750.00', '€170', 'Cannot determine', 2,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €750.00. Net profit = €750.00 - €500 - €80 = €170.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An item bought for €1200 is sold at 40% markup. If expenses are €50, what is the net profit?', 'Cannot determine', '€1680.00', '€480.00', '€430', 3,
'lc_ol_financial', 11, 'advanced', 'lc_ol', 'Selling price = €1680.00. Net profit = €1680.00 - €1200 - €50 = €430.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €600.00', 'Compound by €188.13', 'Compound by €788.13', 'Simple by €188.13', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €188.13', 'Compound by €788.13', 'Simple by €600.00', 'Compound by €188.13', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Compound by €788.13', 'Simple by €600.00', 'Simple by €188.13', 'Compound by €188.13', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €600.00', 'Compound by €188.13', 'Simple by €188.13', 'Compound by €788.13', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €1200.00', 'Compound by €1576.25', 'Simple by €376.25', 'Compound by €376.25', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €11200.00. Compound: €11576.25. Compound better by €376.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Compound by €1576.25', 'Simple by €1200.00', 'Compound by €376.25', 'Simple by €376.25', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €11200.00. Compound: €11576.25. Compound better by €376.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €376.25', 'Compound by €376.25', 'Simple by €1200.00', 'Compound by €1576.25', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €11200.00. Compound: €11576.25. Compound better by €376.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Compound by €188.13', 'Simple by €188.13', 'Simple by €600.00', 'Compound by €788.13', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €376.25', 'Simple by €1200.00', 'Compound by €1576.25', 'Compound by €376.25', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €11200.00. Compound: €11576.25. Compound better by €376.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€8000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Compound by €1261.00', 'Simple by €960.00', 'Simple by €301.00', 'Compound by €301.00', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €8960.00. Compound: €9261.00. Compound better by €301.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Compound by €788.13', 'Compound by €188.13', 'Simple by €600.00', 'Simple by €188.13', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Compound by €188.13', 'Simple by €188.13', 'Simple by €600.00', 'Compound by €788.13', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Compound by €788.13', 'Simple by €188.13', 'Simple by €600.00', 'Compound by €188.13', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€8000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €301.00', 'Compound by €1261.00', 'Simple by €960.00', 'Compound by €301.00', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €8960.00. Compound: €9261.00. Compound better by €301.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5000 for 3 years: Option A is 4% simple interest, Option B is 5% compound. Which gives more and by how much?', 'Simple by €600.00', 'Compound by €188.13', 'Simple by €188.13', 'Compound by €788.13', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Simple: €5600.00. Compound: €5788.13. Compound better by €188.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €42000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€33600.00', '€31920', '€32920.00', '€10080.00', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €8400.0. PRSI = €1680.0. Net = €42000 - €8400.0 - €1680.0 = €31920.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €42000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€33600.00', '€32920.00', '€31920', '€10080.00', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €8400.0. PRSI = €1680.0. Net = €42000 - €8400.0 - €1680.0 = €31920.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €48000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€37480.00', '€36480', '€11520.00', '€38400.00', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €9600.0. PRSI = €1920.0. Net = €48000 - €9600.0 - €1920.0 = €36480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €42000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€10080.00', '€33600.00', '€31920', '€32920.00', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €8400.0. PRSI = €1680.0. Net = €42000 - €8400.0 - €1680.0 = €31920.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €42000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€31920', '€32920.00', '€33600.00', '€10080.00', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €8400.0. PRSI = €1680.0. Net = €42000 - €8400.0 - €1680.0 = €31920.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €48000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€37480.00', '€38400.00', '€36480', '€11520.00', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €9600.0. PRSI = €1920.0. Net = €48000 - €9600.0 - €1920.0 = €36480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €48000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€37480.00', '€11520.00', '€36480', '€38400.00', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €9600.0. PRSI = €1920.0. Net = €48000 - €9600.0 - €1920.0 = €36480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €36000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€27360', '€8640.00', '€28800.00', '€28360.00', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €7200.0. PRSI = €1440.0. Net = €36000 - €7200.0 - €1440.0 = €27360.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €48000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€11520.00', '€38400.00', '€36480', '€37480.00', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €9600.0. PRSI = €1920.0. Net = €48000 - €9600.0 - €1920.0 = €36480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €42000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€31920', '€10080.00', '€32920.00', '€33600.00', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €8400.0. PRSI = €1680.0. Net = €42000 - €8400.0 - €1680.0 = €31920.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €42000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€33600.00', '€31920', '€32920.00', '€10080.00', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €8400.0. PRSI = €1680.0. Net = €42000 - €8400.0 - €1680.0 = €31920.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €42000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€33600.00', '€32920.00', '€10080.00', '€31920', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €8400.0. PRSI = €1680.0. Net = €42000 - €8400.0 - €1680.0 = €31920.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €48000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€37480.00', '€11520.00', '€38400.00', '€36480', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €9600.0. PRSI = €1920.0. Net = €48000 - €9600.0 - €1920.0 = €36480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €48000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€11520.00', '€36480', '€37480.00', '€38400.00', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €9600.0. PRSI = €1920.0. Net = €48000 - €9600.0 - €1920.0 = €36480.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Annual salary €36000. Income tax 20%, PRSI 4%. Calculate annual net pay.', '€27360', '€28800.00', '€28360.00', '€8640.00', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Tax = €7200.0. PRSI = €1440.0. Net = €36000 - €7200.0 - €1440.0 = €27360.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €400 at €1 = $1.1. After buying an item for $150, how many euros is your change worth?', '€250.00', '€290.00', '€283.64', '€263.64', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €400 × 1.1 = $440.00000000000006. Change = $290.00000000000006. In EUR: $290.00000000000006 ÷ 1.1 = €263.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €500 at €1 = $1.1. After buying an item for $250, how many euros is your change worth?', '€292.73', '€300.00', '€250.00', '€272.73', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €500 × 1.1 = $550.0. Change = $300.0. In EUR: $300.0 ÷ 1.1 = €272.73', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €500 at €1 = $1.1. After buying an item for $150, how many euros is your change worth?', '€363.64', '€350.00', '€400.00', '€383.64', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €500 × 1.1 = $550.0. Change = $400.0. In EUR: $400.0 ÷ 1.1 = €363.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €300 at €1 = $1.1. After buying an item for $250, how many euros is your change worth?', '€92.73', '€50.00', '€80.00', '€72.73', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €300 × 1.1 = $330.0. Change = $80.0. In EUR: $80.0 ÷ 1.1 = €72.73', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €500 at €1 = $1.1. After buying an item for $250, how many euros is your change worth?', '€292.73', '€300.00', '€250.00', '€272.73', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €500 × 1.1 = $550.0. Change = $300.0. In EUR: $300.0 ÷ 1.1 = €272.73', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €400 at €1 = $1.1. After buying an item for $250, how many euros is your change worth?', '€172.73', '€192.73', '€150.00', '€190.00', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €400 × 1.1 = $440.00000000000006. Change = $190.00000000000006. In EUR: $190.00000000000006 ÷ 1.1 = €172.73', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €400 at €1 = $1.1. After buying an item for $150, how many euros is your change worth?', '€290.00', '€283.64', '€263.64', '€250.00', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €400 × 1.1 = $440.00000000000006. Change = $290.00000000000006. In EUR: $290.00000000000006 ÷ 1.1 = €263.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €500 at €1 = $1.1. After buying an item for $150, how many euros is your change worth?', '€363.64', '€350.00', '€383.64', '€400.00', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €500 × 1.1 = $550.0. Change = $400.0. In EUR: $400.0 ÷ 1.1 = €363.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €400 at €1 = $1.1. After buying an item for $200, how many euros is your change worth?', '€240.00', '€200.00', '€238.18', '€218.18', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €400 × 1.1 = $440.00000000000006. Change = $240.00000000000006. In EUR: $240.00000000000006 ÷ 1.1 = €218.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You exchange €300 at €1 = $1.1. After buying an item for $150, how many euros is your change worth?', '€180.00', '€183.64', '€163.64', '€150.00', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'USD = €300 × 1.1 = $330.0. Change = $180.0. In EUR: $180.0 ÷ 1.1 = €163.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €20000 depreciates 15% annually. After 2 years it sells for €14950. Profit or loss on book value?', 'Loss €5550', 'Profit €500', 'Profit €5050', 'Loss €500', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €14450.00. Sold for €14950. Profit = €500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €25000 depreciates 15% annually. After 2 years it sells for €18562. Profit or loss on book value?', 'Loss €500', 'Profit €6438', 'Loss €6938', 'Profit €500', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €18062.50. Sold for €18562. Profit = €500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €30000 depreciates 15% annually. After 2 years it sells for €23175. Profit or loss on book value?', 'Profit €1500', 'Loss €8325', 'Loss €1500', 'Profit €6825', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €21675.00. Sold for €23175. Profit = €1500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €30000 depreciates 15% annually. After 2 years it sells for €23175. Profit or loss on book value?', 'Loss €1500', 'Profit €6825', 'Loss €8325', 'Profit €1500', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €21675.00. Sold for €23175. Profit = €1500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €25000 depreciates 15% annually. After 2 years it sells for €19562. Profit or loss on book value?', 'Loss €1500', 'Loss €6938', 'Profit €1500', 'Profit €5438', 2,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €18062.50. Sold for €19562. Profit = €1500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €30000 depreciates 15% annually. After 2 years it sells for €22175. Profit or loss on book value?', 'Profit €7825', 'Loss €8325', 'Loss €500', 'Profit €500', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €21675.00. Sold for €22175. Profit = €500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €20000 depreciates 15% annually. After 2 years it sells for €15450. Profit or loss on book value?', 'Profit €1000', 'Profit €4550', 'Loss €5550', 'Loss €1000', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €14450.00. Sold for €15450. Profit = €1000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €20000 depreciates 15% annually. After 2 years it sells for €15950. Profit or loss on book value?', 'Profit €1500', 'Profit €4050', 'Loss €1500', 'Loss €5550', 0,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €14450.00. Sold for €15950. Profit = €1500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €25000 depreciates 15% annually. After 2 years it sells for €19562. Profit or loss on book value?', 'Loss €6938', 'Profit €5438', 'Loss €1500', 'Profit €1500', 3,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €18062.50. Sold for €19562. Profit = €1500', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car costing €20000 depreciates 15% annually. After 2 years it sells for €14950. Profit or loss on book value?', 'Loss €500', 'Profit €500', 'Loss €5550', 'Profit €5050', 1,
'lc_ol_financial', 12, 'advanced', 'lc_ol', 'Book value = €14450.00. Sold for €14950. Profit = €500', 1);

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_financial';
