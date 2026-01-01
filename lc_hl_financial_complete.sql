-- LC Higher Level - Financial Maths - Complete SQL
-- Includes topic creation + 600 questions
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_financial_complete.sql
-- Generated: 2025-12-14

-- Add Financial Maths topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_financial', 'Financial Maths', id, '💰', 7, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_financial';

-- Questions (600 total: 50 per level x 12 levels)
-- LC Higher Level - Financial Maths Questions
-- Generated: 2025-12-14
-- Total: 600 questions

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €100.00 at 3% per annum for 1 year.', 'Option 4', '€3.00', '€6.00', '€103.00', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 100 × 3 × 1 / 100 = €3.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €2,000.00 at 2% per annum for 3 years.', '€2,120.00', '€120.00', '€240.00', '€40.00', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 2000 × 2 × 3 / 100 = €120.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €200.00 at 4% per annum for 2 years.', '€216.00', '€16.00', '€8.00', '€32.00', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 200 × 4 × 2 / 100 = €16.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €1,000.00 at 6% per annum for 4 years.', '€480.00', '€240.00', '€60.00', '€1,240.00', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 1000 × 6 × 4 / 100 = €240.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €200.00 at 8% per annum for 1 year.', '€32.00', '€16.00', 'Option 4', '€216.00', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 200 × 8 × 1 / 100 = €16.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €200.00 at 3% per annum for 3 years.', '€18.00', '€36.00', '€6.00', '€218.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 200 × 3 × 3 / 100 = €18.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €2,000.00 at 2% per annum for 3 years.', '€120.00', '€40.00', '€2,120.00', '€240.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 2000 × 2 × 3 / 100 = €120.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €2,000.00 at 6% per annum for 4 years.', '€120.00', '€2,480.00', '€480.00', '€960.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 2000 × 6 × 4 / 100 = €480.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €500.00 at 2% per annum for 1 year.', '€10.00', '€510.00', 'Option 4', '€20.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 500 × 2 × 1 / 100 = €10.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €5,000.00 at 4% per annum for 5 years.', '€6,000.00', '€1,000.00', '€200.00', '€2,000.00', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 5000 × 4 × 5 / 100 = €1,000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €2,000.00 at 7% per annum for 5 years.', '€700.00', '€1,400.00', '€140.00', '€2,700.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 2000 × 7 × 5 / 100 = €700.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €1,000.00 at 4% per annum for 5 years.', '€200.00', '€1,200.00', '€400.00', '€40.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 1000 × 4 × 5 / 100 = €200.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €100.00 at 4% per annum for 2 years.', '€4.00', '€108.00', '€16.00', '€8.00', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 100 × 4 × 2 / 100 = €8.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €100.00 at 4% per annum for 5 years.', '€120.00', '€4.00', '€20.00', '€40.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 100 × 4 × 5 / 100 = €20.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €1,000.00 at 3% per annum for 1 year.', '€30.00', '€60.00', 'Option 4', '€1,030.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 1000 × 3 × 1 / 100 = €30.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €500.00 at 3% per annum for 1 year.', '€515.00', '€30.00', 'Option 4', '€15.00', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 500 × 3 × 1 / 100 = €15.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €200.00 at 6% per annum for 5 years.', '€260.00', '€120.00', '€12.00', '€60.00', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 200 × 6 × 5 / 100 = €60.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €5,000.00 at 10% per annum for 2 years.', '€1,000.00', '€2,000.00', '€6,000.00', '€500.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 5000 × 10 × 2 / 100 = €1,000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €500.00 at 6% per annum for 4 years.', '€120.00', '€240.00', '€620.00', '€30.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 500 × 6 × 4 / 100 = €120.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the simple interest on €2,000.00 at 8% per annum for 4 years.', '€160.00', '€1,280.00', '€2,640.00', '€640.00', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Simple Interest = PRT/100 = 2000 × 8 × 4 / 100 = €640.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 7% simple interest per annum for 2 years. What is the total amount at the end?', '€1,070.00', '€140.00', '€1,140.00', '€1,280.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 1000 × 7 × 2 / 100 = €140.00. Total = €1,000.00 + €140.00 = €1,140.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 5% simple interest per annum for 3 years. What is the total amount at the end?', '€2,300.00', '€2,100.00', '€300.00', '€2,600.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 2000 × 5 × 3 / 100 = €300.00. Total = €2,000.00 + €300.00 = €2,300.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 3% simple interest per annum for 2 years. What is the total amount at the end?', '€1,030.00', '€1,120.00', '€60.00', '€1,060.00', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 1000 × 3 × 2 / 100 = €60.00. Total = €1,000.00 + €60.00 = €1,060.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 5% simple interest per annum for 4 years. What is the total amount at the end?', '€1,200.00', '€1,400.00', '€1,050.00', '€200.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 1000 × 5 × 4 / 100 = €200.00. Total = €1,000.00 + €200.00 = €1,200.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 8% simple interest per annum for 2 years. What is the total amount at the end?', '€5,800.00', '€800.00', '€5,400.00', '€6,600.00', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 5000 × 8 × 2 / 100 = €800.00. Total = €5,000.00 + €800.00 = €5,800.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 7% simple interest per annum for 4 years. What is the total amount at the end?', '€3,120.00', '€2,140.00', '€2,560.00', '€560.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 2000 × 7 × 4 / 100 = €560.00. Total = €2,000.00 + €560.00 = €2,560.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 6% simple interest per annum for 2 years. What is the total amount at the end?', '€2,480.00', '€2,120.00', '€2,240.00', '€240.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 2000 × 6 × 2 / 100 = €240.00. Total = €2,000.00 + €240.00 = €2,240.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 4% simple interest per annum for 4 years. What is the total amount at the end?', '€160.00', '€1,320.00', '€1,160.00', '€1,040.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 1000 × 4 × 4 / 100 = €160.00. Total = €1,000.00 + €160.00 = €1,160.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 4% simple interest per annum for 5 years. What is the total amount at the end?', '€5,200.00', '€6,000.00', '€7,000.00', '€1,000.00', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 5000 × 4 × 5 / 100 = €1,000.00. Total = €5,000.00 + €1,000.00 = €6,000.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 7% simple interest per annum for 6 years. What is the total amount at the end?', '€1,070.00', '€420.00', '€1,840.00', '€1,420.00', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 1000 × 7 × 6 / 100 = €420.00. Total = €1,000.00 + €420.00 = €1,420.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 5% simple interest per annum for 2 years. What is the total amount at the end?', '€6,000.00', '€5,250.00', '€5,500.00', '€500.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 5000 × 5 × 2 / 100 = €500.00. Total = €5,000.00 + €500.00 = €5,500.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 3% simple interest per annum for 5 years. What is the total amount at the end?', '€2,060.00', '€300.00', '€2,300.00', '€2,600.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 2000 × 3 × 5 / 100 = €300.00. Total = €2,000.00 + €300.00 = €2,300.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at 4% simple interest per annum for 6 years. What is the total amount at the end?', '€740.00', '€120.00', '€520.00', '€620.00', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 500 × 4 × 6 / 100 = €120.00. Total = €500.00 + €120.00 = €620.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 4% simple interest per annum for 5 years. What is the total amount at the end?', '€400.00', '€2,800.00', '€2,400.00', '€2,080.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 2000 × 4 × 5 / 100 = €400.00. Total = €2,000.00 + €400.00 = €2,400.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€3,000 is invested at 3% simple interest per annum for 2 years. What is the total amount at the end?', '€3,090.00', '€3,360.00', '€3,180.00', '€180.00', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Interest = 3000 × 3 × 2 / 100 = €180.00. Total = €3,000.00 + €180.00 = €3,180.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 earns €320.00 simple interest over 4 years. What is the annual interest rate?', '8%', '7%', '9%', '16%', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (320.0 × 100) / (1000 × 4) = 8%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 earns €120.00 simple interest over 3 years. What is the annual interest rate?', '8%', '4%', '5%', '3%', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (120.0 × 100) / (1000 × 3) = 4%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 earns €180.00 simple interest over 2 years. What is the annual interest rate?', '8%', '9%', '18%', '10%', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (180.0 × 100) / (1000 × 2) = 9%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 earns €450.00 simple interest over 3 years. What is the annual interest rate?', '2%', '3%', '4%', '6%', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (450.0 × 100) / (5000 × 3) = 3%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 earns €700.00 simple interest over 2 years. What is the annual interest rate?', '7%', '6%', '14%', '8%', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (700.0 × 100) / (5000 × 2) = 7%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 earns €1,000.00 simple interest over 2 years. What is the annual interest rate?', '9%', '20%', '11%', '10%', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (1000.0 × 100) / (5000 × 2) = 10%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 earns €280.00 simple interest over 4 years. What is the annual interest rate?', '6%', '8%', '14%', '7%', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (280.0 × 100) / (1000 × 4) = 7%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 earns €240.00 simple interest over 4 years. What is the annual interest rate?', '5%', '6%', '12%', '7%', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (240.0 × 100) / (1000 × 4) = 6%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 earns €1,600.00 simple interest over 4 years. What is the annual interest rate?', '7%', '9%', '16%', '8%', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (1600.0 × 100) / (5000 × 4) = 8%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 earns €600.00 simple interest over 4 years. What is the annual interest rate?', '3%', '2%', '4%', '6%', 0,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Rate = (Interest × 100) / (Principal × Time) = (600.0 × 100) / (5000 × 4) = 3%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How long will it take for €1,000 to earn €200.00 at 5% simple interest per annum?', '5 years', '3 years', '4 years', '8 years', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Time = (Interest × 100) / (Principal × Rate) = (200.0 × 100) / (1000 × 5) = 4 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How long will it take for €4,000 to earn €600.00 at 5% simple interest per annum?', '2 years', '4 years', '3 years', '6 years', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Time = (Interest × 100) / (Principal × Rate) = (600.0 × 100) / (4000 × 5) = 3 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How long will it take for €4,000 to earn €1,200.00 at 6% simple interest per annum?', '4 years', '6 years', '5 years', '10 years', 2,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Time = (Interest × 100) / (Principal × Rate) = (1200.0 × 100) / (4000 × 6) = 5 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How long will it take for €4,000 to earn €1,200.00 at 6% simple interest per annum?', '6 years', '5 years', '10 years', '4 years', 1,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Time = (Interest × 100) / (Principal × Rate) = (1200.0 × 100) / (4000 × 6) = 5 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How long will it take for €4,000 to earn €640.00 at 4% simple interest per annum?', '8 years', '5 years', '3 years', '4 years', 3,
'lc_hl_financial', 1, 'foundation', 'lc_hl', 'Time = (Interest × 100) / (Principal × Rate) = (640.0 × 100) / (4000 × 4) = 4 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 8% compound interest per annum. Find the value after 2 years.', '€6,232.00', '€5,400.00', '€5,832.00', '€5,800.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 5000(1 + 0.08)^2 = 5000 × 1.0800^2 = €5,832.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 7% compound interest per annum. Find the value after 3 years.', '€5,350.00', '€6,050.00', '€6,125.22', '€6,475.22', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 5000(1 + 0.07)^3 = 5000 × 1.0700^3 = €6,125.22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 8% compound interest per annum. Find the value after 4 years.', '€2,640.00', '€2,880.98', '€2,720.98', '€2,160.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 2000(1 + 0.08)^4 = 2000 × 1.0800^4 = €2,720.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 7% compound interest per annum. Find the value after 3 years.', '€2,450.09', '€2,140.00', '€2,590.09', '€2,420.00', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 2000(1 + 0.07)^3 = 2000 × 1.0700^3 = €2,450.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 4% compound interest per annum. Find the value after 3 years.', '€1,040.00', '€1,120.00', '€1,124.86', '€1,164.86', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 1000(1 + 0.04)^3 = 1000 × 1.0400^3 = €1,124.86', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 7% compound interest per annum. Find the value after 3 years.', '€2,420.00', '€2,590.09', '€2,140.00', '€2,450.09', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 2000(1 + 0.07)^3 = 2000 × 1.0700^3 = €2,450.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 8% compound interest per annum. Find the value after 4 years.', '€2,880.98', '€2,720.98', '€2,160.00', '€2,640.00', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 2000(1 + 0.08)^4 = 2000 × 1.0800^4 = €2,720.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 7% compound interest per annum. Find the value after 2 years.', '€11,400.00', '€11,449.00', '€12,149.00', '€10,700.00', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 10000(1 + 0.07)^2 = 10000 × 1.0700^2 = €11,449.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 5% compound interest per annum. Find the value after 2 years.', '€5,512.50', '€5,500.00', '€5,250.00', '€5,762.50', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 5000(1 + 0.05)^2 = 5000 × 1.0500^2 = €5,512.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 6% compound interest per annum. Find the value after 4 years.', '€6,312.38', '€6,200.00', '€6,612.38', '€5,300.00', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 5000(1 + 0.06)^4 = 5000 × 1.0600^4 = €6,312.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 5% compound interest per annum. Find the value after 4 years.', '€1,200.00', '€1,215.51', '€1,050.00', '€1,265.51', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 1000(1 + 0.05)^4 = 1000 × 1.0500^4 = €1,215.51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€2,000 is invested at 5% compound interest per annum. Find the value after 3 years.', '€2,100.00', '€2,300.00', '€2,415.25', '€2,315.25', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 2000(1 + 0.05)^3 = 2000 × 1.0500^3 = €2,315.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 7% compound interest per annum. Find the value after 3 years.', '€10,700.00', '€12,250.43', '€12,100.00', '€12,950.43', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 10000(1 + 0.07)^3 = 10000 × 1.0700^3 = €12,250.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 8% compound interest per annum. Find the value after 4 years.', '€6,802.44', '€7,202.44', '€5,400.00', '€6,600.00', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 5000(1 + 0.08)^4 = 5000 × 1.0800^4 = €6,802.44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1,000 is invested at 8% compound interest per annum. Find the value after 2 years.', '€1,166.40', '€1,160.00', '€1,246.40', '€1,080.00', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 1000(1 + 0.08)^2 = 1000 × 1.0800^2 = €1,166.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 7% compound interest per annum. Find the value after 3 years.', '€10,700.00', '€12,100.00', '€12,250.43', '€12,950.43', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 10000(1 + 0.07)^3 = 10000 × 1.0700^3 = €12,250.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 8% compound interest per annum. Find the value after 3 years.', '€12,400.00', '€10,800.00', '€13,397.12', '€12,597.12', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 10000(1 + 0.08)^3 = 10000 × 1.0800^3 = €12,597.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 5% compound interest per annum. Find the value after 3 years.', '€10,500.00', '€11,500.00', '€11,576.25', '€12,076.25', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'A = P(1 + r)ⁿ = 10000(1 + 0.05)^3 = 10000 × 1.0500^3 = €11,576.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €8,000 is invested at 6% per annum for 4 years.', '€10,099.82', '€1,049.91', '€2,099.82', '€1,920.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 8000(1.06)^4 = €10,099.82. Interest = €10,099.82 - €8,000.00 = €2,099.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €2,000 is invested at 7% per annum for 5 years.', '€402.55', '€700.00', '€2,805.10', '€805.10', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 2000(1.07)^5 = €2,805.10. Interest = €2,805.10 - €2,000.00 = €805.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €5,000 is invested at 7% per annum for 2 years.', '€700.00', '€362.25', '€5,724.50', '€724.50', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 5000(1.07)^2 = €5,724.50. Interest = €5,724.50 - €5,000.00 = €724.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €10,000 is invested at 4% per annum for 4 years.', '€849.29', '€11,698.59', '€1,698.59', '€1,600.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 10000(1.04)^4 = €11,698.59. Interest = €11,698.59 - €10,000.00 = €1,698.59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €10,000 is invested at 6% per annum for 2 years.', '€618.00', '€1,200.00', '€11,236.00', '€1,236.00', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 10000(1.06)^2 = €11,236.00. Interest = €11,236.00 - €10,000.00 = €1,236.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €2,000 is invested at 6% per annum for 2 years.', '€240.00', '€2,247.20', '€123.60', '€247.20', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 2000(1.06)^2 = €2,247.20. Interest = €2,247.20 - €2,000.00 = €247.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €2,000 is invested at 7% per annum for 4 years.', '€310.80', '€2,621.59', '€621.59', '€560.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 2000(1.07)^4 = €2,621.59. Interest = €2,621.59 - €2,000.00 = €621.59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €5,000 is invested at 5% per annum for 4 years.', '€1,000.00', '€1,077.53', '€6,077.53', '€538.76', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 5000(1.05)^4 = €6,077.53. Interest = €6,077.53 - €5,000.00 = €1,077.53', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €5,000 is invested at 4% per annum for 5 years.', '€1,000.00', '€541.63', '€6,083.26', '€1,083.26', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 5000(1.04)^5 = €6,083.26. Interest = €6,083.26 - €5,000.00 = €1,083.26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €8,000 is invested at 5% per annum for 2 years.', '€800.00', '€410.00', '€820.00', '€8,820.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 8000(1.05)^2 = €8,820.00. Interest = €8,820.00 - €8,000.00 = €820.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €5,000 is invested at 5% per annum for 4 years.', '€1,000.00', '€538.76', '€1,077.53', '€6,077.53', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 5000(1.05)^4 = €6,077.53. Interest = €6,077.53 - €5,000.00 = €1,077.53', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €2,000 is invested at 6% per annum for 4 years.', '€2,524.95', '€480.00', '€524.95', '€262.48', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 2000(1.06)^4 = €2,524.95. Interest = €2,524.95 - €2,000.00 = €524.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €10,000 is invested at 5% per annum for 3 years.', '€1,500.00', '€1,576.25', '€788.12', '€11,576.25', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 10000(1.05)^3 = €11,576.25. Interest = €11,576.25 - €10,000.00 = €1,576.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €8,000 is invested at 6% per annum for 4 years.', '€1,049.91', '€10,099.82', '€1,920.00', '€2,099.82', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 8000(1.06)^4 = €10,099.82. Interest = €10,099.82 - €8,000.00 = €2,099.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the compound interest earned when €10,000 is invested at 7% per annum for 4 years.', '€3,107.96', '€1,553.98', '€13,107.96', '€2,800.00', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Amount = 10000(1.07)^4 = €13,107.96. Interest = €13,107.96 - €10,000.00 = €3,107.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested for 3 years at 6%. How much more is earned with compound interest than simple interest?', '€300.00', '€110.16', '€55.08', '€900.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €5,955.08, Simple: €5,900.00. Difference = €55.08', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested for 4 years at 7%. How much more is earned with compound interest than simple interest?', '€615.92', '€307.96', '€2,800.00', '€700.00', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €13,107.96, Simple: €12,800.00. Difference = €307.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested for 3 years at 6%. How much more is earned with compound interest than simple interest?', '€600.00', '€110.16', '€220.32', '€1,800.00', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €11,910.16, Simple: €11,800.00. Difference = €110.16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested for 5 years at 7%. How much more is earned with compound interest than simple interest?', '€1,750.00', '€525.52', '€262.76', '€350.00', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €7,012.76, Simple: €6,750.00. Difference = €262.76', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested for 4 years at 6%. How much more is earned with compound interest than simple interest?', '€112.38', '€1,200.00', '€224.76', '€300.00', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €6,312.38, Simple: €6,200.00. Difference = €112.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested for 5 years at 5%. How much more is earned with compound interest than simple interest?', '€500.00', '€262.82', '€2,500.00', '€525.64', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €12,762.82, Simple: €12,500.00. Difference = €262.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested for 4 years at 5%. How much more is earned with compound interest than simple interest?', '€155.06', '€77.53', '€1,000.00', '€250.00', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €6,077.53, Simple: €6,000.00. Difference = €77.53', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested for 4 years at 6%. How much more is earned with compound interest than simple interest?', '€600.00', '€224.77', '€2,400.00', '€449.54', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €12,624.77, Simple: €12,400.00. Difference = €224.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested for 5 years at 8%. How much more is earned with compound interest than simple interest?', '€2,000.00', '€400.00', '€346.64', '€693.28', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €7,346.64, Simple: €7,000.00. Difference = €346.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested for 4 years at 7%. How much more is earned with compound interest than simple interest?', '€307.96', '€350.00', '€1,400.00', '€153.98', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound: €6,553.98, Simple: €6,400.00. Difference = €153.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which formula gives compound interest?', 'A = P/r', 'A = P + PRT', 'A = P(1 + r)ⁿ', 'A = P × r × n', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'The compound interest formula multiplies by (1 + r) for each period.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In A = P(1 + r)ⁿ, what does P represent?', 'Period', 'Payment', 'Percentage', 'Principal (initial investment)', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'P is the principal or starting amount.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In A = P(1 + r)ⁿ, what does r represent?', 'Principal', 'Interest rate (as decimal)', 'Number of years', 'Final amount', 1,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'r is the interest rate expressed as a decimal.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In A = P(1 + r)ⁿ, what does n represent?', 'Number of time periods', 'Number of payments', 'Interest rate', 'Principal', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'n is the number of compounding periods.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What does ''compounding'' mean?', 'Rate changes yearly', 'Principal decreases', 'Interest earns interest', 'Interest stays fixed', 2,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Compound interest means interest is added to principal, then earns more interest.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If interest is compounded annually, how often is it added?', 'Once per year', 'Twice per year', 'Every month', 'Every quarter', 0,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'Annual compounding means interest is calculated and added once per year.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the multiplier for 5% compound interest?', '0.05', '1.5', '5', '1.05', 3,
'lc_hl_financial', 2, 'foundation', 'lc_hl', 'The multiplier is (1 + r) = 1 + 0.05 = 1.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10,000.00 depreciates at 12% per year. What is its value after 4 years?', '€8,800.00', '€5,200.00', '€7,196.95', '€5,996.95', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 10000(1 - 0.12)^4 = 10000 × 0.88^4 = €5,996.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15,000.00 depreciates at 15% per year. What is its value after 5 years?', '€6,655.58', '€3,750.00', '€8,905.58', '€12,750.00', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 15000(1 - 0.15)^5 = 15000 × 0.85^5 = €6,655.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15,000.00 depreciates at 23% per year. What is its value after 2 years?', '€8,893.50', '€8,100.00', '€11,550.00', '€12,343.50', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 15000(1 - 0.23)^2 = 15000 × 0.77^2 = €8,893.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20,000.00 depreciates at 22% per year. What is its value after 5 years?', '€10,174.35', '€-2,000.00', '€15,600.00', '€5,774.35', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 20000(1 - 0.22)^5 = 20000 × 0.78^5 = €5,774.35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10,000.00 depreciates at 22% per year. What is its value after 3 years?', '€6,945.52', '€3,400.00', '€4,745.52', '€7,800.00', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 10000(1 - 0.22)^3 = 10000 × 0.78^3 = €4,745.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25,000.00 depreciates at 21% per year. What is its value after 2 years?', '€14,500.00', '€19,750.00', '€20,852.50', '€15,602.50', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 25000(1 - 0.21)^2 = 25000 × 0.79^2 = €15,602.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15,000.00 depreciates at 21% per year. What is its value after 3 years?', '€5,550.00', '€10,545.59', '€7,395.59', '€11,850.00', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 15000(1 - 0.21)^3 = 15000 × 0.79^3 = €7,395.59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25,000.00 depreciates at 18% per year. What is its value after 4 years?', '€11,303.04', '€15,803.04', '€20,500.00', '€7,000.00', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 25000(1 - 0.18)^4 = 25000 × 0.82^4 = €11,303.04', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10,000.00 depreciates at 18% per year. What is its value after 3 years?', '€4,600.00', '€7,313.68', '€5,513.68', '€8,200.00', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 10000(1 - 0.18)^3 = 10000 × 0.82^3 = €5,513.68', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €15,000.00 depreciates at 25% per year. What is its value after 4 years?', '€8,496.09', '€0.00', '€11,250.00', '€4,746.09', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 15000(1 - 0.25)^4 = 15000 × 0.75^4 = €4,746.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10,000.00 depreciates at 12% per year. What is its value after 2 years?', '€7,744.00', '€7,600.00', '€8,944.00', '€8,800.00', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 10000(1 - 0.12)^2 = 10000 × 0.88^2 = €7,744.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30,000.00 depreciates at 15% per year. What is its value after 2 years?', '€21,000.00', '€21,675.00', '€25,500.00', '€26,175.00', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 30000(1 - 0.15)^2 = 30000 × 0.85^2 = €21,675.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20,000.00 depreciates at 18% per year. What is its value after 5 years?', '€16,400.00', '€2,000.00', '€7,414.80', '€11,014.80', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 20000(1 - 0.18)^5 = 20000 × 0.82^5 = €7,414.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25,000.00 depreciates at 13% per year. What is its value after 3 years?', '€15,250.00', '€21,750.00', '€19,712.57', '€16,462.57', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 25000(1 - 0.13)^3 = 25000 × 0.87^3 = €16,462.57', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20,000.00 depreciates at 14% per year. What is its value after 2 years?', '€17,200.00', '€14,400.00', '€17,592.00', '€14,792.00', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 20000(1 - 0.14)^2 = 20000 × 0.86^2 = €14,792.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30,000.00 depreciates at 20% per year. What is its value after 3 years?', '€24,000.00', '€12,000.00', '€21,360.00', '€15,360.00', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 30000(1 - 0.2)^3 = 30000 × 0.80^3 = €15,360.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €10,000.00 depreciates at 20% per year. What is its value after 5 years?', '€0.00', '€5,276.80', '€3,276.80', '€8,000.00', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 10000(1 - 0.2)^5 = 10000 × 0.80^5 = €3,276.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €25,000.00 depreciates at 22% per year. What is its value after 4 years?', '€9,253.76', '€14,753.76', '€3,000.00', '€19,500.00', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 25000(1 - 0.22)^4 = 25000 × 0.78^4 = €9,253.76', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €30,000.00 depreciates at 13% per year. What is its value after 3 years?', '€18,300.00', '€19,755.09', '€26,100.00', '€23,655.09', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 30000(1 - 0.13)^3 = 30000 × 0.87^3 = €19,755.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car worth €20,000.00 depreciates at 20% per year. What is its value after 5 years?', '€10,553.60', '€0.00', '€6,553.60', '€16,000.00', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'V = P(1 - r)ⁿ = 20000(1 - 0.2)^5 = 20000 × 0.80^5 = €6,553.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24,000.00 depreciates at 20% per annum. Find the total depreciation over 4 years.', '€14,169.60', '€9,830.40', '€19,200.00', '€7,084.80', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €9,830.40. Depreciation = €24,000.00 - €9,830.40 = €14,169.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €8,000.00 depreciates at 18% per annum. Find the total depreciation over 2 years.', '€2,620.80', '€1,310.40', '€2,880.00', '€5,379.20', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €5,379.20. Depreciation = €8,000.00 - €5,379.20 = €2,620.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €8,000.00 depreciates at 20% per annum. Find the total depreciation over 4 years.', '€4,723.20', '€6,400.00', '€3,276.80', '€2,361.60', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €3,276.80. Depreciation = €8,000.00 - €3,276.80 = €4,723.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18,000.00 depreciates at 20% per annum. Find the total depreciation over 4 years.', '€14,400.00', '€5,313.60', '€7,372.80', '€10,627.20', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €7,372.80. Depreciation = €18,000.00 - €7,372.80 = €10,627.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €8,000.00 depreciates at 17% per annum. Find the total depreciation over 4 years.', '€3,796.67', '€5,440.00', '€2,101.66', '€4,203.33', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €3,796.67. Depreciation = €8,000.00 - €3,796.67 = €4,203.33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18,000.00 depreciates at 13% per annum. Find the total depreciation over 3 years.', '€11,853.05', '€3,073.47', '€6,146.95', '€7,020.00', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €11,853.05. Depreciation = €18,000.00 - €11,853.05 = €6,146.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €8,000.00 depreciates at 20% per annum. Find the total depreciation over 3 years.', '€4,800.00', '€1,952.00', '€4,096.00', '€3,904.00', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €4,096.00. Depreciation = €8,000.00 - €4,096.00 = €3,904.00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18,000.00 depreciates at 19% per annum. Find the total depreciation over 2 years.', '€6,190.20', '€6,840.00', '€11,809.80', '€3,095.10', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €11,809.80. Depreciation = €18,000.00 - €11,809.80 = €6,190.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €18,000.00 depreciates at 13% per annum. Find the total depreciation over 2 years.', '€4,375.80', '€2,187.90', '€13,624.20', '€4,680.00', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €13,624.20. Depreciation = €18,000.00 - €13,624.20 = €4,375.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €8,000.00 depreciates at 19% per annum. Find the total depreciation over 3 years.', '€3,748.47', '€1,874.23', '€4,560.00', '€4,251.53', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €4,251.53. Depreciation = €8,000.00 - €4,251.53 = €3,748.47', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24,000.00 depreciates at 12% per annum. Find the total depreciation over 3 years.', '€8,640.00', '€3,822.34', '€16,355.33', '€7,644.67', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €16,355.33. Depreciation = €24,000.00 - €16,355.33 = €7,644.67', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €12,000.00 depreciates at 20% per annum. Find the total depreciation over 4 years.', '€7,084.80', '€9,600.00', '€4,915.20', '€3,542.40', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €4,915.20. Depreciation = €12,000.00 - €4,915.20 = €7,084.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €8,000.00 depreciates at 14% per annum. Find the total depreciation over 3 years.', '€1,455.78', '€5,088.45', '€3,360.00', '€2,911.55', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €5,088.45. Depreciation = €8,000.00 - €5,088.45 = €2,911.55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €12,000.00 depreciates at 19% per annum. Find the total depreciation over 3 years.', '€5,622.71', '€6,840.00', '€2,811.36', '€6,377.29', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €6,377.29. Depreciation = €12,000.00 - €6,377.29 = €5,622.71', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Equipment worth €24,000.00 depreciates at 13% per annum. Find the total depreciation over 3 years.', '€15,804.07', '€9,360.00', '€4,097.97', '€8,195.93', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Final value = €15,804.07. Depreciation = €24,000.00 - €15,804.07 = €8,195.93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 4 years of 15% annual depreciation, machinery is worth €6,000.00. What was its original value?', '€9,600.00', '€11,494.12', '€12,643.53', '€10,494.04', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 6000/0.5220 = €11,494.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 2 years of 21% annual depreciation, machinery is worth €10,000.00. What was its original value?', '€17,625.38', '€14,200.00', '€16,023.07', '€14,641.00', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 10000/0.6241 = €16,023.07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 3 years of 21% annual depreciation, machinery is worth €10,000.00. What was its original value?', '€20,282.37', '€22,310.61', '€16,300.00', '€17,715.61', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 10000/0.4930 = €20,282.37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 2 years of 24% annual depreciation, machinery is worth €5,000.00. What was its original value?', '€7,688.00', '€9,522.16', '€7,400.00', '€8,656.51', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 5000/0.5776 = €8,656.51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 3 years of 21% annual depreciation, machinery is worth €8,000.00. What was its original value?', '€13,040.00', '€16,225.90', '€17,848.49', '€14,172.49', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 8000/0.4930 = €16,225.90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 4 years of 19% annual depreciation, machinery is worth €10,000.00. What was its original value?', '€25,553.63', '€17,600.00', '€23,230.57', '€20,053.39', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 10000/0.4305 = €23,230.57', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 4 years of 22% annual depreciation, machinery is worth €8,000.00. What was its original value?', '€23,774.11', '€15,040.00', '€17,722.68', '€21,612.83', 3,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 8000/0.3702 = €21,612.83', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 3 years of 17% annual depreciation, machinery is worth €6,000.00. What was its original value?', '€9,060.00', '€10,493.42', '€11,542.76', '€9,609.68', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 6000/0.5718 = €10,493.42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 3 years of 19% annual depreciation, machinery is worth €6,000.00. What was its original value?', '€11,290.06', '€9,420.00', '€12,419.07', '€10,110.95', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 6000/0.5314 = €11,290.06', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After 2 years of 19% annual depreciation, machinery is worth €8,000.00. What was its original value?', '€13,412.59', '€12,193.26', '€11,040.00', '€11,328.80', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = 8000/0.6561 = €12,193.26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the depreciation multiplier for 20% annual depreciation?', '0.70', '1.20', '0.80', '0.20', 2,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Multiplier = 1 - 0.20 = 0.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the depreciation multiplier for 15% annual depreciation?', '0.75', '0.85', '0.15', '1.15', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Multiplier = 1 - 0.15 = 0.85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If an asset depreciates by 10% each year, what fraction of its value does it retain?', '90% or 0.9', '10% or 0.1', '100% or 1.0', '110% or 1.1', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'It retains 100% - 10% = 90% of its value each year.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which formula represents depreciation?', 'V = P - Prn', 'V = P(1 - r)ⁿ', 'V = P(1 + r)ⁿ', 'V = P/rⁿ', 1,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Depreciation uses subtraction: (1 - r) as the multiplier.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A laptop loses half its value in 3 years. Is this likely straight-line or reducing balance depreciation?', 'Reducing balance', 'Cannot determine', 'Straight-line', 'Neither', 0,
'lc_hl_financial', 3, 'foundation', 'lc_hl', 'Reducing balance depreciation is typically used for technology assets.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €25,000.00 due in 3 years if money can earn 8% per annum?', '€19,845.81', '€31,492.80', '€19,000.00', '€17,861.23', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 25000/(1.08)^3 = €19,845.81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €15,000.00 due in 4 years if money can earn 5% per annum?', '€12,340.54', '€11,106.49', '€18,232.59', '€12,000.00', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 15000/(1.05)^4 = €12,340.54', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €20,000.00 due in 5 years if money can earn 6% per annum?', '€14,000.00', '€13,450.64', '€14,945.16', '€26,764.51', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 20000/(1.06)^5 = €14,945.16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €5,000.00 due in 7 years if money can earn 4% per annum?', '€6,579.66', '€3,600.00', '€3,419.63', '€3,799.59', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 5000/(1.04)^7 = €3,799.59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €25,000.00 due in 7 years if money can earn 3% per annum?', '€18,294.56', '€20,327.29', '€19,750.00', '€30,746.85', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 25000/(1.03)^7 = €20,327.29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €20,000.00 due in 6 years if money can earn 8% per annum?', '€10,400.00', '€31,737.49', '€11,343.05', '€12,603.39', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 20000/(1.08)^6 = €12,603.39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €5,000.00 due in 7 years if money can earn 5% per annum?', '€7,035.50', '€3,250.00', '€3,553.41', '€3,198.07', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 5000/(1.05)^7 = €3,553.41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €5,000.00 due in 7 years if money can earn 8% per annum?', '€2,200.00', '€2,625.70', '€8,569.12', '€2,917.45', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 5000/(1.08)^7 = €2,917.45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €25,000.00 due in 7 years if money can earn 7% per annum?', '€40,144.54', '€15,568.74', '€12,750.00', '€14,011.87', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 25000/(1.07)^7 = €15,568.74', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €20,000.00 due in 4 years if money can earn 5% per annum?', '€24,310.13', '€14,808.65', '€16,454.05', '€16,000.00', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 20000/(1.05)^4 = €16,454.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €15,000.00 due in 5 years if money can earn 4% per annum?', '€12,328.91', '€11,096.02', '€12,000.00', '€18,249.79', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 15000/(1.04)^5 = €12,328.91', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €20,000.00 due in 7 years if money can earn 8% per annum?', '€11,669.81', '€8,800.00', '€34,276.49', '€10,502.83', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 20000/(1.08)^7 = €11,669.81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €20,000.00 due in 4 years if money can earn 7% per annum?', '€14,400.00', '€26,215.92', '€13,732.11', '€15,257.90', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 20000/(1.07)^4 = €15,257.90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €10,000.00 due in 7 years if money can earn 4% per annum?', '€6,839.26', '€7,599.18', '€7,200.00', '€13,159.32', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 10000/(1.04)^7 = €7,599.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €25,000.00 due in 3 years if money can earn 8% per annum?', '€19,845.81', '€31,492.80', '€19,000.00', '€17,861.23', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 25000/(1.08)^3 = €19,845.81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €25,000.00 due in 4 years if money can earn 7% per annum?', '€18,000.00', '€32,769.90', '€17,165.14', '€19,072.38', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 25000/(1.07)^4 = €19,072.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €15,000.00 due in 3 years if money can earn 6% per annum?', '€12,594.29', '€12,300.00', '€11,334.86', '€17,865.24', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 15000/(1.06)^3 = €12,594.29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €10,000.00 due in 7 years if money can earn 7% per annum?', '€5,604.75', '€16,057.81', '€5,100.00', '€6,227.50', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 10000/(1.07)^7 = €6,227.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €20,000.00 due in 4 years if money can earn 4% per annum?', '€23,397.17', '€17,096.08', '€15,386.47', '€16,800.00', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 20000/(1.04)^4 = €17,096.08', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €15,000.00 due in 5 years if money can earn 5% per annum?', '€19,144.22', '€11,250.00', '€10,577.60', '€11,752.89', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV = FV/(1 + r)ⁿ = 15000/(1.05)^5 = €11,752.89', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 7% interest, which is worth more today: €12,000.00 in 3 years or €13,495.00 in 5 years?', 'Cannot be determined', '€13,495.00 in 5 years', '€12,000.00 in 3 years', 'They have equal present value', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 12000/(1.07)^3 = €9,795.57. PV₂ = 13495/(1.07)^5 = €9,621.75. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 6% interest, which is worth more today: €10,000.00 in 2 years or €11,094.00 in 5 years?', 'Cannot be determined', 'They have equal present value', '€11,094.00 in 5 years', '€10,000.00 in 2 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 10000/(1.06)^2 = €8,899.96. PV₂ = 11094/(1.06)^5 = €8,290.08. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 4% interest, which is worth more today: €12,000.00 in 2 years or €14,478.00 in 5 years?', '€14,478.00 in 5 years', '€12,000.00 in 2 years', 'Cannot be determined', 'They have equal present value', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 12000/(1.04)^2 = €11,094.67. PV₂ = 14478/(1.04)^5 = €11,899.86. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 4% interest, which is worth more today: €10,000.00 in 3 years or €11,567.00 in 6 years?', 'They have equal present value', 'Cannot be determined', '€10,000.00 in 3 years', '€11,567.00 in 6 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 10000/(1.04)^3 = €8,889.96. PV₂ = 11567/(1.04)^6 = €9,141.57. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 4% interest, which is worth more today: €12,000.00 in 3 years or €14,841.00 in 6 years?', 'They have equal present value', 'Cannot be determined', '€14,841.00 in 6 years', '€12,000.00 in 3 years', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 12000/(1.04)^3 = €10,667.96. PV₂ = 14841/(1.04)^6 = €11,729.06. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 4% interest, which is worth more today: €15,000.00 in 2 years or €17,716.00 in 4 years?', '€17,716.00 in 4 years', 'They have equal present value', 'Cannot be determined', '€15,000.00 in 2 years', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 15000/(1.04)^2 = €13,868.34. PV₂ = 17716/(1.04)^4 = €15,143.71. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 4% interest, which is worth more today: €12,000.00 in 2 years or €14,744.00 in 5 years?', '€14,744.00 in 5 years', '€12,000.00 in 2 years', 'They have equal present value', 'Cannot be determined', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 12000/(1.04)^2 = €11,094.67. PV₂ = 14744/(1.04)^5 = €12,118.49. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 5% interest, which is worth more today: €15,000.00 in 3 years or €16,733.00 in 5 years?', '€16,733.00 in 5 years', 'They have equal present value', '€15,000.00 in 3 years', 'Cannot be determined', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 15000/(1.05)^3 = €12,957.56. PV₂ = 16733/(1.05)^5 = €13,110.74. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 6% interest, which is worth more today: €10,000.00 in 2 years or €11,695.00 in 5 years?', 'Cannot be determined', '€11,695.00 in 5 years', '€10,000.00 in 2 years', 'They have equal present value', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 10000/(1.06)^2 = €8,899.96. PV₂ = 11695/(1.06)^5 = €8,739.18. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 6% interest, which is worth more today: €12,000.00 in 4 years or €14,249.00 in 6 years?', '€12,000.00 in 4 years', 'Cannot be determined', 'They have equal present value', '€14,249.00 in 6 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 12000/(1.06)^4 = €9,505.12. PV₂ = 14249/(1.06)^6 = €10,044.98. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 4% interest, which is worth more today: €15,000.00 in 3 years or €17,084.00 in 6 years?', '€15,000.00 in 3 years', 'Cannot be determined', 'They have equal present value', '€17,084.00 in 6 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 15000/(1.04)^3 = €13,334.95. PV₂ = 17084/(1.04)^6 = €13,501.73. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 5% interest, which is worth more today: €15,000.00 in 3 years or €16,890.00 in 6 years?', 'They have equal present value', '€16,890.00 in 6 years', 'Cannot be determined', '€15,000.00 in 3 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 15000/(1.05)^3 = €12,957.56. PV₂ = 16890/(1.05)^6 = €12,603.58. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 6% interest, which is worth more today: €12,000.00 in 3 years or €14,178.00 in 6 years?', 'Cannot be determined', 'They have equal present value', '€14,178.00 in 6 years', '€12,000.00 in 3 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 12000/(1.06)^3 = €10,075.43. PV₂ = 14178/(1.06)^6 = €9,994.93. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 5% interest, which is worth more today: €10,000.00 in 3 years or €12,231.00 in 5 years?', 'Cannot be determined', '€12,231.00 in 5 years', 'They have equal present value', '€10,000.00 in 3 years', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 10000/(1.05)^3 = €8,638.38. PV₂ = 12231/(1.05)^5 = €9,583.31. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At 7% interest, which is worth more today: €12,000.00 in 4 years or €14,872.00 in 6 years?', 'They have equal present value', '€12,000.00 in 4 years', 'Cannot be determined', '€14,872.00 in 6 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV₁ = 12000/(1.07)^4 = €9,154.74. PV₂ = 14872/(1.07)^6 = €9,909.84. Higher PV is better.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why is €1,000 today worth more than €1,000 in 5 years?', 'Inflation reduces value', '€1,000 is always €1,000', 'Government regulations', 'Money today can earn interest', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'The time value of money means today''s money can be invested to grow.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What happens to present value when the interest rate increases?', 'Cannot determine', 'Present value increases', 'Present value decreases', 'Present value stays the same', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'Higher rates mean future money is discounted more heavily.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What happens to present value when time increases?', 'Present value increases', 'Present value decreases', 'Depends on the rate', 'Present value stays the same', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'The longer we wait, the more the future amount is discounted.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of €1,000 due today?', '€1,000', '€0', 'Cannot calculate', 'Depends on rate', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'If the payment is immediate, no discounting is needed.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If PV = €8,000 and FV = €10,000, what happened?', 'Cannot determine', 'Break-even', 'Money grew through interest', 'Unprofitable', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'The difference represents interest earned over time.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What discount rate makes PV = FV?', 'Any rate', 'Cannot exist', '100%', '0%', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'With 0% interest, there''s no time value of money.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Present value is also called:', 'Nominal value', 'Discounted value', 'Future value', 'Accumulated value', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'We ''discount'' future values to find their present worth.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which has higher PV: €5,000 in 2 years or €5,000 in 5 years (same rate)?', '€5,000 in 5 years', 'Cannot compare', 'They are equal', '€5,000 in 2 years', 3,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'Less time means less discounting, so higher present value.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The process of finding PV from FV is called:', 'Discounting', 'Compounding', 'Appreciating', 'Amortising', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'We discount future values back to the present.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In PV = FV/(1+r)ⁿ, what is (1+r)ⁿ called?', 'Discount factor or compound factor', 'Principal', 'Time period', 'Interest rate', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'This factor converts between present and future values.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 5% and n = 2, what is the discount factor (1+r)ⁿ?', '1.1025', '1.10', '0.9025', '1.025', 0,
'lc_hl_financial', 4, 'developing', 'lc_hl', '(1.05)² = 1.1025', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A present value calculation assumes money can be:', 'Kept under a mattress', 'Invested at the given rate', 'Spent immediately', 'Taxed at source', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'PV assumes the opportunity to earn the stated interest rate.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the relationship between PV and FV?', 'PV / FV = r', 'PV + FV = r', 'PV × (1+r)ⁿ = FV', 'PV - FV = n', 2,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'Present value grows to future value through compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Net Present Value (NPV) compares:', 'Nominal rates', 'Present values of cash flows', 'Simple interest amounts', 'Future values only', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'NPV sums discounted cash inflows and outflows.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If NPV > 0, the investment is:', 'Cannot determine', 'Profitable at the given rate', 'Break-even', 'Unprofitable', 1,
'lc_hl_financial', 4, 'developing', 'lc_hl', 'Positive NPV means returns exceed the discount rate.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 5% compound interest per annum. What will it be worth in 9 years?', '€14,500.00', '€10,500.00', '€12,410.62', '€15,513.28', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 10000(1.05)^9 = €15,513.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 6% compound interest per annum. What will it be worth in 10 years?', '€8,954.24', '€7,163.39', '€8,000.00', '€5,300.00', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 5000(1.06)^10 = €8,954.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 3% compound interest per annum. What will it be worth in 12 years?', '€10,300.00', '€14,257.61', '€13,600.00', '€11,406.09', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 10000(1.03)^12 = €14,257.61', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€15,000 is invested at 8% compound interest per annum. What will it be worth in 11 years?', '€27,979.66', '€28,200.00', '€34,974.58', '€16,200.00', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 15000(1.08)^11 = €34,974.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 5% compound interest per annum. What will it be worth in 5 years?', '€5,250.00', '€5,105.13', '€6,250.00', '€6,381.41', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 5000(1.05)^5 = €6,381.41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€8,000 is invested at 6% compound interest per annum. What will it be worth in 6 years?', '€11,348.15', '€9,078.52', '€10,880.00', '€8,480.00', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 8000(1.06)^6 = €11,348.15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 7% compound interest per annum. What will it be worth in 13 years?', '€9,550.00', '€12,049.23', '€5,350.00', '€9,639.38', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 5000(1.07)^13 = €12,049.23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 5% compound interest per annum. What will it be worth in 9 years?', '€10,500.00', '€14,500.00', '€12,410.62', '€15,513.28', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 10000(1.05)^9 = €15,513.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 8% compound interest per annum. What will it be worth in 10 years?', '€8,635.70', '€10,794.62', '€5,400.00', '€9,000.00', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 5000(1.08)^10 = €10,794.62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€8,000 is invested at 5% compound interest per annum. What will it be worth in 5 years?', '€10,000.00', '€10,210.25', '€8,400.00', '€8,168.20', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 8000(1.05)^5 = €10,210.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€15,000 is invested at 5% compound interest per annum. What will it be worth in 12 years?', '€21,550.27', '€15,750.00', '€24,000.00', '€26,937.84', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 15000(1.05)^12 = €26,937.84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 5% compound interest per annum. What will it be worth in 14 years?', '€7,919.73', '€8,500.00', '€9,899.66', '€5,250.00', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 5000(1.05)^14 = €9,899.66', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€15,000 is invested at 6% compound interest per annum. What will it be worth in 6 years?', '€20,400.00', '€17,022.23', '€21,277.79', '€15,900.00', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 15000(1.06)^6 = €21,277.79', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€15,000 is invested at 5% compound interest per annum. What will it be worth in 12 years?', '€24,000.00', '€21,550.27', '€15,750.00', '€26,937.84', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 15000(1.05)^12 = €26,937.84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 4% compound interest per annum. What will it be worth in 5 years?', '€12,000.00', '€9,733.22', '€10,400.00', '€12,166.53', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 10000(1.04)^5 = €12,166.53', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 5% compound interest per annum. What will it be worth in 11 years?', '€17,103.39', '€15,500.00', '€10,500.00', '€13,682.71', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 10000(1.05)^11 = €17,103.39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€15,000 is invested at 3% compound interest per annum. What will it be worth in 10 years?', '€16,127.00', '€19,500.00', '€15,450.00', '€20,158.75', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 15000(1.03)^10 = €20,158.75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€15,000 is invested at 4% compound interest per annum. What will it be worth in 8 years?', '€15,600.00', '€16,422.83', '€20,528.54', '€19,800.00', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r)ⁿ = 15000(1.04)^8 = €20,528.54', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 5% per annum to have €30,000.00 in 20 years?', '€10,754.58', '€13,568.02', '€11,306.68', '€15,000.00', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 30000/(1.05)^20 = €11,306.68', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 6% per annum to have €100,000.00 in 17 years?', '€34,927.98', '€37,136.44', '€44,563.73', '€49,504.95', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 100000/(1.06)^17 = €37,136.44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 4% per annum to have €30,000.00 in 12 years?', '€18,381.29', '€18,737.91', '€20,270.27', '€22,485.49', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 30000/(1.04)^12 = €18,737.91', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 4% per annum to have €20,000.00 in 10 years?', '€13,296.65', '€14,285.71', '€16,213.54', '€13,511.28', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 20000/(1.04)^10 = €13,511.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 5% per annum to have €30,000.00 in 19 years?', '€11,872.02', '€15,384.62', '€11,320.61', '€14,246.42', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 30000/(1.05)^19 = €11,872.02', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 5% per annum to have €20,000.00 in 13 years?', '€10,266.84', '€12,727.72', '€10,606.43', '€12,121.21', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 20000/(1.05)^13 = €10,606.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 6% per annum to have €30,000.00 in 11 years?', '€15,188.95', '€18,964.36', '€18,072.29', '€15,803.63', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 30000/(1.06)^11 = €15,803.63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 7% per annum to have €30,000.00 in 15 years?', '€10,873.38', '€14,634.15', '€10,101.03', '€13,048.06', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 30000/(1.07)^15 = €10,873.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 5% per annum to have €20,000.00 in 15 years?', '€9,620.34', '€9,265.82', '€11,544.41', '€11,428.57', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 20000/(1.05)^15 = €9,620.34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 5% per annum to have €20,000.00 in 17 years?', '€8,362.41', '€10,471.12', '€10,810.81', '€8,725.93', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 20000/(1.05)^17 = €8,725.93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 4% per annum to have €50,000.00 in 17 years?', '€24,979.34', '€29,761.90', '€30,802.39', '€25,668.66', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 50000/(1.04)^17 = €25,668.66', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 6% per annum to have €100,000.00 in 14 years?', '€53,076.12', '€44,230.10', '€42,052.32', '€54,347.83', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 100000/(1.06)^14 = €44,230.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 7% per annum to have €30,000.00 in 12 years?', '€13,320.36', '€12,557.89', '€15,984.43', '€16,304.35', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 30000/(1.07)^12 = €13,320.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 5% per annum to have €20,000.00 in 14 years?', '€9,753.50', '€11,764.71', '€10,101.36', '€12,121.63', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 20000/(1.05)^14 = €10,101.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested now at 5% per annum to have €50,000.00 in 18 years?', '€24,931.24', '€20,776.03', '€19,860.72', '€26,315.79', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'P = FV/(1 + r)ⁿ = 50000/(1.05)^18 = €20,776.03', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 8% per annum?', 'Approximately 7 years', 'Option 4', 'Approximately 9 years', 'Approximately 12 years', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/8 ≈ 9 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 9% per annum?', 'Approximately 6 years', 'Approximately 8 years', 'Option 4', 'Approximately 11 years', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/9 ≈ 8 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 10% per annum?', 'Approximately 10 years', 'Option 4', 'Approximately 7 years', 'Approximately 5 years', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/10 ≈ 7 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 6% per annum?', 'Approximately 12 years', 'Approximately 15 years', 'Approximately 10 years', 'Approximately 16 years', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/6 ≈ 12 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 7% per annum?', 'Approximately 8 years', 'Approximately 13 years', 'Approximately 10 years', 'Approximately 14 years', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/7 ≈ 10 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 10% per annum?', 'Approximately 5 years', 'Option 4', 'Approximately 10 years', 'Approximately 7 years', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/10 ≈ 7 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 8% per annum?', 'Option 4', 'Approximately 12 years', 'Approximately 9 years', 'Approximately 7 years', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/8 ≈ 9 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 6% per annum?', 'Approximately 16 years', 'Approximately 15 years', 'Approximately 12 years', 'Approximately 10 years', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/6 ≈ 12 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 6% per annum?', 'Approximately 12 years', 'Approximately 16 years', 'Approximately 15 years', 'Approximately 10 years', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/6 ≈ 12 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Using the Rule of 72, approximately how long will it take for money to double at 8% per annum?', 'Option 4', 'Approximately 7 years', 'Approximately 9 years', 'Approximately 12 years', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'Rule of 72: Time to double ≈ 72/rate = 72/8 ≈ 9 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000 is invested at 5% compounded quarterly (4 times per year) for 4 years. Find the future value.', '€12,198.90', '€12,000.00', '€12,155.06', '€11,588.95', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r/n)^(nt) = 10000(1 + 0.05/4)^(4×4) = €12,198.90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 8% compounded semi-annually (twice per year) for 2 years. Find the future value.', '€5,849.29', '€5,800.00', '€5,556.83', '€5,832.00', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r/n)^(nt) = 5000(1 + 0.08/2)^(2×2) = €5,849.29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 5% compounded quarterly (4 times per year) for 3 years. Find the future value.', '€5,750.00', '€5,513.58', '€5,803.77', '€5,788.13', 2,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r/n)^(nt) = 5000(1 + 0.05/4)^(4×3) = €5,803.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 6% compounded quarterly (4 times per year) for 3 years. Find the future value.', '€5,679.19', '€5,978.09', '€5,900.00', '€5,955.08', 1,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r/n)^(nt) = 5000(1 + 0.06/4)^(4×3) = €5,978.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 8% compounded monthly for 2 years. Find the future value.', '€5,571.22', '€5,800.00', '€5,832.00', '€5,864.44', 3,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r/n)^(nt) = 5000(1 + 0.08/12)^(12×2) = €5,864.44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 7% compounded semi-annually (twice per year) for 5 years. Find the future value.', '€7,052.99', '€6,750.00', '€7,012.76', '€6,700.34', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r/n)^(nt) = 5000(1 + 0.07/2)^(2×5) = €7,052.99', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000 is invested at 6% compounded quarterly (4 times per year) for 5 years. Find the future value.', '€6,734.28', '€6,397.57', '€6,500.00', '€6,691.13', 0,
'lc_hl_financial', 5, 'developing', 'lc_hl', 'FV = P(1 + r/n)^(nt) = 5000(1 + 0.06/4)^(4×5) = €6,734.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 11 years at 3% per annum. Find the future value.', '€6,403.90', '€5,500.00', '€5,665.00', '€5,123.12', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.03)^11 - 1]/0.03 = €6,403.90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€100 is invested at the end of each year for 14 years at 5% per annum. Find the future value.', '€1,567.89', '€1,959.86', '€1,400.00', '€1,470.00', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 100 × [(1.05)^14 - 1]/0.05 = €1,959.86', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€100 is invested at the end of each year for 6 years at 3% per annum. Find the future value.', '€600.00', '€646.84', '€618.00', '€517.47', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 100 × [(1.03)^6 - 1]/0.03 = €646.84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€200 is invested at the end of each year for 5 years at 5% per annum. Find the future value.', '€1,050.00', '€884.10', '€1,105.13', '€1,000.00', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 200 × [(1.05)^5 - 1]/0.05 = €1,105.13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€100 is invested at the end of each year for 7 years at 5% per annum. Find the future value.', '€814.20', '€735.00', '€651.36', '€700.00', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 100 × [(1.05)^7 - 1]/0.05 = €814.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€100 is invested at the end of each year for 10 years at 6% per annum. Find the future value.', '€1,318.08', '€1,000.00', '€1,054.46', '€1,060.00', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 100 × [(1.06)^10 - 1]/0.06 = €1,318.08', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€200 is invested at the end of each year for 14 years at 6% per annum. Find the future value.', '€3,362.41', '€4,203.01', '€2,800.00', '€2,968.00', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 200 × [(1.06)^14 - 1]/0.06 = €4,203.01', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 9 years at 3% per annum. Find the future value.', '€4,063.64', '€4,635.00', '€5,079.55', '€4,500.00', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.03)^9 - 1]/0.03 = €5,079.55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 12 years at 7% per annum. Find the future value.', '€6,420.00', '€7,155.38', '€8,944.23', '€6,000.00', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.07)^12 - 1]/0.07 = €8,944.23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 7 years at 3% per annum. Find the future value.', '€3,064.98', '€3,500.00', '€3,831.23', '€3,605.00', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.03)^7 - 1]/0.03 = €3,831.23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 10 years at 6% per annum. Find the future value.', '€5,000.00', '€5,300.00', '€5,272.32', '€6,590.40', 3,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.06)^10 - 1]/0.06 = €6,590.40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 5 years at 7% per annum. Find the future value.', '€2,300.30', '€2,875.37', '€2,675.00', '€2,500.00', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.07)^5 - 1]/0.07 = €2,875.37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at the end of each year for 7 years at 7% per annum. Find the future value.', '€6,923.22', '€7,490.00', '€7,000.00', '€8,654.02', 3,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 1000 × [(1.07)^7 - 1]/0.07 = €8,654.02', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 10 years at 4% per annum. Find the future value.', '€4,802.44', '€5,000.00', '€6,003.05', '€5,200.00', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.04)^10 - 1]/0.04 = €6,003.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€200 is invested at the end of each year for 5 years at 4% per annum. Find the future value.', '€866.61', '€1,083.26', '€1,040.00', '€1,000.00', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 200 × [(1.04)^5 - 1]/0.04 = €1,083.26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at the end of each year for 13 years at 3% per annum. Find the future value.', '€15,617.79', '€13,390.00', '€13,000.00', '€12,494.23', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 1000 × [(1.03)^13 - 1]/0.03 = €15,617.79', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 14 years at 7% per annum. Find the future value.', '€7,000.00', '€9,020.19', '€11,275.24', '€7,490.00', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.07)^14 - 1]/0.07 = €11,275.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 12 years at 5% per annum. Find the future value.', '€7,958.56', '€6,366.85', '€6,000.00', '€6,300.00', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.05)^12 - 1]/0.05 = €7,958.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 12 years at 5% per annum. Find the future value.', '€6,300.00', '€6,000.00', '€6,366.85', '€7,958.56', 3,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.05)^12 - 1]/0.05 = €7,958.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the end of each year for 11 years at 4% per annum. Find the future value.', '€5,720.00', '€6,743.18', '€5,394.54', '€5,500.00', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'FV = PMT × [(1+r)ⁿ - 1]/r = 500 × [(1.04)^11 - 1]/0.04 = €6,743.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €500 at the end of each year for 10 years, at 5% per annum?', '€5,000.00', '€4,633.04', '€6,288.95', '€3,860.87', 3,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 500 × [1 - (1.05)^(-10)]/0.05 = €3,860.87', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €1,000 at the end of each year for 7 years, at 6% per annum?', '€6,698.86', '€8,393.84', '€5,582.38', '€7,000.00', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 1000 × [1 - (1.06)^(-7)]/0.06 = €5,582.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €5,000 at the end of each year for 12 years, at 4% per annum?', '€60,000.00', '€75,129.03', '€46,925.37', '€56,310.44', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 5000 × [1 - (1.04)^(-12)]/0.04 = €46,925.37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €2,000 at the end of each year for 10 years, at 6% per annum?', '€20,000.00', '€14,720.17', '€17,664.20', '€26,361.58', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 2000 × [1 - (1.06)^(-10)]/0.06 = €14,720.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €5,000 at the end of each year for 11 years, at 7% per annum?', '€55,000.00', '€78,917.99', '€37,493.37', '€44,992.04', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 5000 × [1 - (1.07)^(-11)]/0.07 = €37,493.37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €1,000 at the end of each year for 5 years, at 6% per annum?', '€5,637.09', '€5,000.00', '€5,054.83', '€4,212.36', 3,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 1000 × [1 - (1.06)^(-5)]/0.06 = €4,212.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €5,000 at the end of each year for 8 years, at 8% per annum?', '€40,000.00', '€53,183.13', '€28,733.19', '€34,479.83', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 5000 × [1 - (1.08)^(-8)]/0.08 = €28,733.19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €500 at the end of each year for 12 years, at 7% per annum?', '€4,765.61', '€3,971.34', '€8,944.22', '€6,000.00', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 500 × [1 - (1.07)^(-12)]/0.07 = €3,971.34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €2,000 at the end of each year for 10 years, at 8% per annum?', '€28,973.12', '€13,420.16', '€20,000.00', '€16,104.19', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 2000 × [1 - (1.08)^(-10)]/0.08 = €13,420.16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €5,000 at the end of each year for 12 years, at 4% per annum?', '€46,925.37', '€75,129.03', '€56,310.44', '€60,000.00', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 5000 × [1 - (1.04)^(-12)]/0.04 = €46,925.37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €500 at the end of each year for 11 years, at 8% per annum?', '€3,569.48', '€8,322.74', '€4,283.38', '€5,500.00', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 500 × [1 - (1.08)^(-11)]/0.08 = €3,569.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €2,000 at the end of each year for 6 years, at 8% per annum?', '€14,671.86', '€9,245.76', '€12,000.00', '€11,094.91', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 2000 × [1 - (1.08)^(-6)]/0.08 = €9,245.76', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €2,000 at the end of each year for 7 years, at 6% per annum?', '€14,000.00', '€11,164.76', '€13,397.71', '€16,787.67', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 2000 × [1 - (1.06)^(-7)]/0.06 = €11,164.76', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €5,000 at the end of each year for 5 years, at 7% per annum?', '€20,500.99', '€24,601.19', '€25,000.00', '€28,753.70', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 5000 × [1 - (1.07)^(-5)]/0.07 = €20,500.99', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the present value of receiving €5,000 at the end of each year for 12 years, at 7% per annum?', '€39,713.43', '€47,656.12', '€60,000.00', '€89,442.25', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 5000 × [1 - (1.07)^(-12)]/0.07 = €39,713.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is an annuity?', 'A single lump sum payment', 'An insurance policy', 'A series of equal payments at regular intervals', 'A loan from a bank', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'An annuity involves identical payments made at fixed intervals.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an ordinary annuity, when are payments made?', 'At the end of each period', 'At the beginning', 'Randomly', 'In the middle', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Ordinary annuities have payments at period ends.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an annuity due, when are payments made?', 'In the middle', 'When convenient', 'At the beginning of each period', 'At the end', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Annuity due has payments at the start of each period.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which has higher future value: ordinary annuity or annuity due (same PMT, r, n)?', 'They are equal', 'Annuity due', 'Depends on rate', 'Ordinary annuity', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Annuity due payments earn interest for one extra period.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which has higher present value: ordinary annuity or annuity due (same PMT, r, n)?', 'Annuity due', 'Depends on rate', 'They are equal', 'Ordinary annuity', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Annuity due payments are received/paid earlier.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is a perpetuity?', 'An annuity that continues forever', 'A type of bond', 'A decreasing payment', 'An annuity for 100 years', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'A perpetuity is an infinite stream of payments.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The present value formula for a perpetuity is:', 'PV = PMT/r', 'PV = PMT/(1+r)', 'PV = PMT × n', 'PV = PMT × r', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'For infinite payments, PV = PMT/r.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If PMT = €1000 and r = 5%, what is the PV of a perpetuity?', '€20,000', '€5,000', '€1,000', '€50,000', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'PV = 1000/0.05 = €20,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of annuity is a mortgage payment?', 'Ordinary annuity', 'Perpetuity', 'Annuity due', 'Deferred annuity', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Mortgage payments are typically made at period ends.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of annuity is rent paid in advance?', 'Perpetuity', 'Ordinary annuity', 'Growing annuity', 'Annuity due', 3,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Rent paid at the start of each period is an annuity due.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The annuity factor [1 - (1+r)⁻ⁿ]/r is used for:', 'Interest rate calculations', 'Future value calculations', 'Present value calculations', 'Payment calculations', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'This factor converts a payment stream to present value.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The annuity factor [(1+r)ⁿ - 1]/r is used for:', 'Payment calculations', 'Future value calculations', 'Present value calculations', 'Interest rate calculations', 1,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'This factor converts a payment stream to future value.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('As the number of payments increases, the PV of an annuity:', 'Decreases', 'Stays the same', 'Increases (but at a decreasing rate)', 'Becomes negative', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'More payments add value, but distant payments contribute less.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('As the interest rate increases, the PV of an annuity:', 'Increases', 'Stays the same', 'Decreases', 'Doubles', 2,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Higher rates discount future payments more heavily.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A sinking fund is used to:', 'Accumulate money for a future obligation', 'Increase interest rate', 'Pay off a loan early', 'Avoid taxes', 0,
'lc_hl_financial', 6, 'developing', 'lc_hl', 'Sinking funds build up to meet a future payment.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 6% to accumulate €100,000.00 in 20 years?', '€4,077.69', '€2,718.46', '€1,902.92', '€5,000.00', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 100000 × 0.06 / [(1.06)^20 - 1] = €2,718.46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 7% to accumulate €200,000.00 in 24 years?', '€3,437.80', '€5,156.70', '€2,406.46', '€8,333.33', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 200000 × 0.07 / [(1.07)^24 - 1] = €3,437.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 6% to accumulate €50,000.00 in 29 years?', '€1,724.14', '€1,018.47', '€678.98', '€475.29', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 50000 × 0.06 / [(1.06)^29 - 1] = €678.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 6% to accumulate €500,000.00 in 28 years?', '€17,857.14', '€7,296.28', '€10,944.42', '€5,107.40', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 500000 × 0.06 / [(1.06)^28 - 1] = €7,296.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 7% to accumulate €500,000.00 in 30 years?', '€3,705.24', '€16,666.67', '€7,939.80', '€5,293.20', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 500000 × 0.07 / [(1.07)^30 - 1] = €5,293.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 6% to accumulate €50,000.00 in 30 years?', '€948.68', '€1,666.67', '€632.45', '€442.72', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 50000 × 0.06 / [(1.06)^30 - 1] = €632.45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 6% to accumulate €200,000.00 in 16 years?', '€7,790.43', '€12,500.00', '€11,685.65', '€5,453.30', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 200000 × 0.06 / [(1.06)^16 - 1] = €7,790.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 5% to accumulate €500,000.00 in 29 years?', '€17,241.38', '€8,022.76', '€12,034.14', '€5,615.93', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 500000 × 0.05 / [(1.05)^29 - 1] = €8,022.76', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 4% to accumulate €100,000.00 in 29 years?', '€2,831.99', '€1,887.99', '€1,321.59', '€3,448.28', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 100000 × 0.04 / [(1.04)^29 - 1] = €1,887.99', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 7% to accumulate €500,000.00 in 22 years?', '€10,202.89', '€22,727.27', '€7,142.02', '€15,304.33', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 500000 × 0.07 / [(1.07)^22 - 1] = €10,202.89', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 6% to accumulate €500,000.00 in 16 years?', '€13,633.25', '€29,214.10', '€19,476.07', '€31,250.00', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 500000 × 0.06 / [(1.06)^16 - 1] = €19,476.07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 7% to accumulate €50,000.00 in 29 years?', '€572.43', '€400.70', '€1,724.14', '€858.64', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 50000 × 0.07 / [(1.07)^29 - 1] = €572.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 6% to accumulate €50,000.00 in 30 years?', '€632.45', '€442.72', '€948.68', '€1,666.67', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 50000 × 0.06 / [(1.06)^30 - 1] = €632.45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 4% to accumulate €50,000.00 in 28 years?', '€700.45', '€1,500.97', '€1,785.71', '€1,000.65', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 50000 × 0.04 / [(1.04)^28 - 1] = €1,000.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How much should be invested each year at 7% to accumulate €500,000.00 in 28 years?', '€6,195.96', '€4,337.17', '€17,857.14', '€9,293.94', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PMT = FV × r / [(1+r)ⁿ - 1] = 500000 × 0.07 / [(1.07)^28 - 1] = €6,195.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €30,000.00 per year for 27 years at 5% interest?', '€571,078.31', '€439,291.01', '€263,574.61', '€810,000.00', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 30000 × [1 - (1.05)^(-27)]/0.05 = €439,291.01', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €40,000.00 per year for 25 years at 3% interest?', '€1,000,000.00', '€696,525.91', '€417,915.55', '€905,483.68', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 40000 × [1 - (1.03)^(-25)]/0.03 = €696,525.91', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €50,000.00 per year for 20 years at 6% interest?', '€573,496.06', '€344,097.64', '€745,544.88', '€1,000,000.00', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 50000 × [1 - (1.06)^(-20)]/0.06 = €573,496.06', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €30,000.00 per year for 21 years at 5% interest?', '€384,634.58', '€500,024.95', '€230,780.75', '€630,000.00', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 30000 × [1 - (1.05)^(-21)]/0.05 = €384,634.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €50,000.00 per year for 28 years at 5% interest?', '€1,400,000.00', '€744,906.36', '€446,943.82', '€968,378.27', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 50000 × [1 - (1.05)^(-28)]/0.05 = €744,906.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €40,000.00 per year for 21 years at 3% interest?', '€840,000.00', '€616,600.97', '€369,960.58', '€801,581.26', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 40000 × [1 - (1.03)^(-21)]/0.03 = €616,600.97', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €30,000.00 per year for 26 years at 3% interest?', '€321,783.16', '€780,000.00', '€697,196.85', '€536,305.27', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 30000 × [1 - (1.03)^(-26)]/0.03 = €536,305.27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €50,000.00 per year for 24 years at 5% interest?', '€689,932.09', '€896,911.72', '€1,200,000.00', '€413,959.25', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 50000 × [1 - (1.05)^(-24)]/0.05 = €689,932.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €50,000.00 per year for 26 years at 3% interest?', '€536,305.27', '€893,842.12', '€1,300,000.00', '€1,161,994.76', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 50000 × [1 - (1.03)^(-26)]/0.03 = €893,842.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €30,000.00 per year for 20 years at 3% interest?', '€600,000.00', '€267,794.55', '€446,324.25', '€580,221.53', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 30000 × [1 - (1.03)^(-20)]/0.03 = €446,324.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €50,000.00 per year for 27 years at 4% interest?', '€816,479.29', '€1,061,423.08', '€489,887.57', '€1,350,000.00', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 50000 × [1 - (1.04)^(-27)]/0.04 = €816,479.29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €30,000.00 per year for 30 years at 6% interest?', '€536,828.41', '€247,766.96', '€900,000.00', '€412,944.93', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 30000 × [1 - (1.06)^(-30)]/0.06 = €412,944.93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €40,000.00 per year for 29 years at 5% interest?', '€363,385.76', '€605,642.94', '€787,335.82', '€1,160,000.00', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 40000 × [1 - (1.05)^(-29)]/0.05 = €605,642.94', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €40,000.00 per year for 22 years at 5% interest?', '€684,476.13', '€880,000.00', '€315,912.06', '€526,520.10', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 40000 × [1 - (1.05)^(-22)]/0.05 = €526,520.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What pension fund is needed to provide €50,000.00 per year for 24 years at 4% interest?', '€991,052.61', '€1,200,000.00', '€457,408.90', '€762,348.16', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'PV = PMT × [1 - (1+r)⁻ⁿ]/r = 50000 × [1 - (1.04)^(-24)]/0.04 = €762,348.16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at the START of each year for 13 years at 5%. Find the future value (annuity due).', '€17,712.98', '€18,598.63', '€13,650.00', '€16,738.77', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €17,712.98 × 1.05 = €18,598.63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the START of each year for 12 years at 6%. Find the future value (annuity due).', '€6,360.00', '€8,434.97', '€8,941.07', '€8,046.96', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €8,434.97 × 1.06 = €8,941.07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at the START of each year for 8 years at 5%. Find the future value (annuity due).', '€8,400.00', '€9,023.90', '€10,026.56', '€9,549.11', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €9,549.11 × 1.05 = €10,026.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at the START of each year for 8 years at 6%. Find the future value (annuity due).', '€9,442.19', '€8,480.00', '€9,897.47', '€10,491.32', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €9,897.47 × 1.06 = €10,491.32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€200 is invested at the START of each year for 9 years at 5%. Find the future value (annuity due).', '€2,084.02', '€2,315.58', '€1,890.00', '€2,205.31', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €2,205.31 × 1.05 = €2,315.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€200 is invested at the START of each year for 12 years at 5%. Find the future value (annuity due).', '€3,183.43', '€3,342.60', '€2,520.00', '€3,008.34', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €3,183.43 × 1.05 = €3,342.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€200 is invested at the START of each year for 14 years at 7%. Find the future value (annuity due).', '€4,510.10', '€2,996.00', '€4,343.22', '€4,825.80', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €4,510.10 × 1.07 = €4,825.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€1000 is invested at the START of each year for 9 years at 7%. Find the future value (annuity due).', '€11,977.99', '€11,534.81', '€9,630.00', '€12,816.45', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €11,977.99 × 1.07 = €12,816.45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€500 is invested at the START of each year for 9 years at 7%. Find the future value (annuity due).', '€5,988.99', '€4,815.00', '€6,408.22', '€5,767.40', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €5,988.99 × 1.07 = €6,408.22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€200 is invested at the START of each year for 15 years at 4%. Find the future value (annuity due).', '€3,120.00', '€4,004.72', '€3,748.42', '€4,164.91', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Annuity due FV = Ordinary FV × (1+r) = €4,004.72 × 1.04 = €4,164.91', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €2,400/year vs €200/month at 5% for 13 years. How much more do monthly payments yield?', '€1,310.72', '€2,621.44', '€655.36', '€0.00', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €43,821.88, Annual: €42,511.16. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €12,000/year vs €1,000/month at 6% for 7 years. How much more do monthly payments yield?', '€3,347.88', '€6,695.76', '€0.00', '€1,673.94', 0,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €104,073.93, Annual: €100,726.05. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €12,000/year vs €1,000/month at 8% for 7 years. How much more do monthly payments yield?', '€0.00', '€2,519.84', '€10,079.34', '€5,039.67', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €112,113.31, Annual: €107,073.64. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €1,200/year vs €100/month at 4% for 12 years. How much more do monthly payments yield?', '€0.00', '€412.58', '€206.29', '€825.16', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €18,443.55, Annual: €18,030.97. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €2,400/year vs €200/month at 5% for 11 years. How much more do monthly payments yield?', '€502.43', '€1,004.85', '€2,009.70', '€0.00', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €35,101.13, Annual: €34,096.29. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €2,400/year vs €200/month at 7% for 10 years. How much more do monthly payments yield?', '€0.00', '€1,457.49', '€728.75', '€2,914.98', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €34,616.96, Annual: €33,159.48. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €6,000/year vs €500/month at 5% for 9 years. How much more do monthly payments yield?', '€931.11', '€1,862.21', '€0.00', '€3,724.42', 1,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €68,021.60, Annual: €66,159.39. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €2,400/year vs €200/month at 4% for 15 years. How much more do monthly payments yield?', '€2,322.98', '€580.75', '€1,161.49', '€0.00', 2,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €49,218.10, Annual: €48,056.61. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €12,000/year vs €1,000/month at 5% for 5 years. How much more do monthly payments yield?', '€3,397.02', '€0.00', '€849.25', '€1,698.51', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €68,006.08, Annual: €66,307.58. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Compare investing €1,200/year vs €100/month at 6% for 15 years. How much more do monthly payments yield?', '€0.00', '€575.36', '€2,301.42', '€1,150.71', 3,
'lc_hl_financial', 7, 'proficient', 'lc_hl', 'Monthly: €29,081.87, Annual: €27,931.16. Monthly payments accumulate more due to more frequent compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €250,000.00 mortgage at 5% per annum over 20 years.', '€1,979.87', '€1,319.91', '€1,649.89', '€1,041.67', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 5%/12 and n = 20×12 = 240. Payment = €1,649.89', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €100,000.00 mortgage at 6% per annum over 15 years.', '€555.56', '€675.09', '€1,012.63', '€843.86', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 6%/12 and n = 15×12 = 180. Payment = €843.86', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €250,000.00 mortgage at 6% per annum over 20 years.', '€1,041.67', '€2,149.30', '€1,791.08', '€1,432.86', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 6%/12 and n = 20×12 = 240. Payment = €1,791.08', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €250,000.00 mortgage at 5% per annum over 15 years.', '€2,372.38', '€1,388.89', '€1,976.98', '€1,581.58', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 5%/12 and n = 15×12 = 180. Payment = €1,976.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €200,000.00 mortgage at 5% per annum over 25 years.', '€666.67', '€1,403.02', '€1,169.18', '€935.34', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 5%/12 and n = 25×12 = 300. Payment = €1,169.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €100,000.00 mortgage at 3% per annum over 20 years.', '€554.60', '€416.67', '€665.52', '€443.68', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 3%/12 and n = 20×12 = 240. Payment = €554.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €100,000.00 mortgage at 5% per annum over 30 years.', '€277.78', '€536.82', '€429.46', '€644.18', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 5%/12 and n = 30×12 = 360. Payment = €536.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €300,000.00 mortgage at 6% per annum over 15 years.', '€1,666.67', '€2,531.57', '€3,037.88', '€2,025.26', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 6%/12 and n = 15×12 = 180. Payment = €2,531.57', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €150,000.00 mortgage at 3% per annum over 15 years.', '€1,035.87', '€828.70', '€833.33', '€1,243.04', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 3%/12 and n = 15×12 = 180. Payment = €1,035.87', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €100,000.00 mortgage at 6% per annum over 30 years.', '€277.78', '€479.64', '€599.55', '€719.46', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 6%/12 and n = 30×12 = 360. Payment = €599.55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €150,000.00 mortgage at 5% per annum over 15 years.', '€1,186.19', '€833.33', '€948.95', '€1,423.43', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 5%/12 and n = 15×12 = 180. Payment = €1,186.19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €300,000.00 mortgage at 5% per annum over 25 years.', '€1,403.02', '€1,753.77', '€1,000.00', '€2,104.52', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 5%/12 and n = 25×12 = 300. Payment = €1,753.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €300,000.00 mortgage at 5% per annum over 15 years.', '€1,897.90', '€2,372.38', '€2,846.86', '€1,666.67', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 5%/12 and n = 15×12 = 180. Payment = €2,372.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €100,000.00 mortgage at 6% per annum over 25 years.', '€515.44', '€333.33', '€644.30', '€773.16', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 6%/12 and n = 25×12 = 300. Payment = €644.30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €150,000.00 mortgage at 4% per annum over 25 years.', '€633.41', '€950.11', '€500.00', '€791.76', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 4%/12 and n = 25×12 = 300. Payment = €791.76', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €250,000.00 mortgage at 4% per annum over 25 years.', '€1,319.59', '€833.33', '€1,583.51', '€1,055.67', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 4%/12 and n = 25×12 = 300. Payment = €1,319.59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €200,000.00 mortgage at 3% per annum over 20 years.', '€887.36', '€1,331.04', '€833.33', '€1,109.20', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 3%/12 and n = 20×12 = 240. Payment = €1,109.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €200,000.00 mortgage at 6% per annum over 25 years.', '€1,288.60', '€666.67', '€1,546.32', '€1,030.88', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 6%/12 and n = 25×12 = 300. Payment = €1,288.60', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €300,000.00 mortgage at 4% per annum over 15 years.', '€1,666.67', '€1,775.25', '€2,662.87', '€2,219.06', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 4%/12 and n = 15×12 = 180. Payment = €2,219.06', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the monthly payment on a €250,000.00 mortgage at 4% per annum over 15 years.', '€1,849.22', '€1,479.38', '€2,219.06', '€1,388.89', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = 4%/12 and n = 15×12 = 180. Payment = €1,849.22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 4% over 30 years?', '€53,902.13', '€257,804.26', '€107,804.26', '€180,000.00', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €716.12 × 360 = €257,804.26. Interest = €257,804.26 - €150,000.00 = €107,804.26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €250,000.00 mortgage at 3% over 25 years?', '€187,500.00', '€52,829.25', '€105,658.49', '€355,658.49', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €1,185.53 × 300 = €355,658.49. Interest = €355,658.49 - €250,000.00 = €105,658.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €200,000.00 mortgage at 5% over 25 years?', '€250,000.00', '€350,754.02', '€75,377.01', '€150,754.02', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €1,169.18 × 300 = €350,754.02. Interest = €350,754.02 - €200,000.00 = €150,754.02', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 4% over 20 years?', '€34,076.46', '€218,152.92', '€68,152.92', '€120,000.00', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €908.97 × 240 = €218,152.92. Interest = €218,152.92 - €150,000.00 = €68,152.92', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 3% over 30 years?', '€135,000.00', '€227,666.18', '€77,666.18', '€38,833.09', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €632.41 × 360 = €227,666.18. Interest = €227,666.18 - €150,000.00 = €77,666.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 5% over 20 years?', '€87,584.07', '€43,792.04', '€237,584.07', '€150,000.00', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €989.93 × 240 = €237,584.07. Interest = €237,584.07 - €150,000.00 = €87,584.07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €200,000.00 mortgage at 5% over 25 years?', '€250,000.00', '€150,754.02', '€350,754.02', '€75,377.01', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €1,169.18 × 300 = €350,754.02. Interest = €350,754.02 - €200,000.00 = €150,754.02', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 5% over 25 years?', '€56,532.76', '€113,065.52', '€263,065.52', '€187,500.00', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €876.89 × 300 = €263,065.52. Interest = €263,065.52 - €150,000.00 = €113,065.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 5% over 25 years?', '€263,065.52', '€187,500.00', '€56,532.76', '€113,065.52', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €876.89 × 300 = €263,065.52. Interest = €263,065.52 - €150,000.00 = €113,065.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €250,000.00 mortgage at 3% over 25 years?', '€355,658.49', '€187,500.00', '€52,829.25', '€105,658.49', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €1,185.53 × 300 = €355,658.49. Interest = €355,658.49 - €250,000.00 = €105,658.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 3% over 20 years?', '€24,827.57', '€49,655.14', '€90,000.00', '€199,655.14', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €831.90 × 240 = €199,655.14. Interest = €199,655.14 - €150,000.00 = €49,655.14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €200,000.00 mortgage at 3% over 25 years?', '€150,000.00', '€84,526.79', '€42,263.39', '€284,526.79', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €948.42 × 300 = €284,526.79. Interest = €284,526.79 - €200,000.00 = €84,526.79', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €250,000.00 mortgage at 4% over 20 years?', '€113,588.20', '€363,588.20', '€56,794.10', '€200,000.00', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €1,514.95 × 240 = €363,588.20. Interest = €363,588.20 - €250,000.00 = €113,588.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €150,000.00 mortgage at 3% over 25 years?', '€31,697.54', '€112,500.00', '€213,395.09', '€63,395.09', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €711.32 × 300 = €213,395.09. Interest = €213,395.09 - €150,000.00 = €63,395.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the total interest paid on a €250,000.00 mortgage at 5% over 30 years?', '€233,139.46', '€483,139.46', '€116,569.73', '€375,000.00', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Total paid = €1,342.05 × 360 = €483,139.46. Interest = €483,139.46 - €250,000.00 = €233,139.46', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €250,000.00 mortgage at 5% over 20 years, how is the first monthly payment split?', 'Interest: €833.33, Principal: €729.87', 'Interest: €608.22, Principal: €1,041.67', 'Interest: €824.94, Principal: €824.94', 'Interest: €1,041.67, Principal: €608.22', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €250,000.00 × (5%/12) = €1,041.67. Principal = Payment - Interest = €608.22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €250,000.00 mortgage at 4% over 30 years, how is the first monthly payment split?', 'Interest: €360.20, Principal: €833.33', 'Interest: €833.33, Principal: €360.20', 'Interest: €596.77, Principal: €596.77', 'Interest: €666.67, Principal: €432.25', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €250,000.00 × (4%/12) = €833.33. Principal = Payment - Interest = €360.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €300,000.00 mortgage at 3% over 25 years, how is the first monthly payment split?', 'Interest: €711.32, Principal: €711.32', 'Interest: €750.00, Principal: €672.63', 'Interest: €672.63, Principal: €750.00', 'Interest: €600.00, Principal: €807.16', 1,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €300,000.00 × (3%/12) = €750.00. Principal = Payment - Interest = €672.63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €300,000.00 mortgage at 4% over 25 years, how is the first monthly payment split?', 'Interest: €800.00, Principal: €700.21', 'Interest: €583.51, Principal: €1,000.00', 'Interest: €791.76, Principal: €791.76', 'Interest: €1,000.00, Principal: €583.51', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €300,000.00 × (4%/12) = €1,000.00. Principal = Payment - Interest = €583.51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €200,000.00 mortgage at 3% over 30 years, how is the first monthly payment split?', 'Interest: €421.60, Principal: €421.60', 'Interest: €400.00, Principal: €411.85', 'Interest: €500.00, Principal: €343.21', 'Interest: €343.21, Principal: €500.00', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €200,000.00 × (3%/12) = €500.00. Principal = Payment - Interest = €343.21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €250,000.00 mortgage at 3% over 20 years, how is the first monthly payment split?', 'Interest: €761.49, Principal: €625.00', 'Interest: €500.00, Principal: €913.79', 'Interest: €625.00, Principal: €761.49', 'Interest: €693.25, Principal: €693.25', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €250,000.00 × (3%/12) = €625.00. Principal = Payment - Interest = €761.49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €250,000.00 mortgage at 3% over 30 years, how is the first monthly payment split?', 'Interest: €429.01, Principal: €625.00', 'Interest: €500.00, Principal: €514.81', 'Interest: €527.01, Principal: €527.01', 'Interest: €625.00, Principal: €429.01', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €250,000.00 × (3%/12) = €625.00. Principal = Payment - Interest = €429.01', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €250,000.00 mortgage at 4% over 20 years, how is the first monthly payment split?', 'Interest: €666.67, Principal: €817.94', 'Interest: €681.62, Principal: €833.33', 'Interest: €833.33, Principal: €681.62', 'Interest: €757.48, Principal: €757.48', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €250,000.00 × (4%/12) = €833.33. Principal = Payment - Interest = €681.62', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €300,000.00 mortgage at 5% over 25 years, how is the first monthly payment split?', 'Interest: €1,250.00, Principal: €503.77', 'Interest: €1,000.00, Principal: €604.52', 'Interest: €503.77, Principal: €1,250.00', 'Interest: €876.89, Principal: €876.89', 0,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €300,000.00 × (5%/12) = €1,250.00. Principal = Payment - Interest = €503.77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a €300,000.00 mortgage at 5% over 20 years, how is the first monthly payment split?', 'Interest: €729.87, Principal: €1,250.00', 'Interest: €989.93, Principal: €989.93', 'Interest: €1,000.00, Principal: €875.84', 'Interest: €1,250.00, Principal: €729.87', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'First month interest = €300,000.00 × (5%/12) = €1,250.00. Principal = Payment - Interest = €729.87', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an amortised loan, how does the interest portion change over time?', 'Varies randomly', 'Increases', 'Stays constant', 'Decreases', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'As the principal is paid down, less interest accrues each period.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an amortised loan, how does the principal portion change over time?', 'Varies randomly', 'Decreases', 'Stays constant', 'Increases', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'As interest decreases, more of each payment goes to principal.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What remains constant in an amortised loan?', 'Nothing', 'Interest amount', 'The payment amount', 'Principal amount', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Amortisation calculates a fixed payment that pays off the loan.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the balance after all payments on an amortised loan?', 'Half the original', 'The original principal', 'Depends on payments', '€0', 3,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Amortisation is designed to pay off the entire loan.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why is more interest paid in early loan years?', 'Interest rates are higher early', 'Banks charge more initially', 'The outstanding balance is highest', 'It''s a government rule', 2,
'lc_hl_financial', 8, 'proficient', 'lc_hl', 'Interest is calculated on the remaining balance, which is largest early on.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 10% compounded daily. What is the AER (Annual Equivalent Rate)?', '11.02%', '10%', '304.17%', '10.52%', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 10%/365)^365 - 1 = (1 + 0.000274)^365 - 1 = 10.52%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 11% compounded daily. What is the AER (Annual Equivalent Rate)?', '12.13%', '334.58%', '11.63%', '11%', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 11%/365)^365 - 1 = (1 + 0.000301)^365 - 1 = 11.63%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 5% compounded quarterly. What is the AER (Annual Equivalent Rate)?', '5.09%', '5.59%', '5%', '1.67%', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 5%/4)^4 - 1 = (1 + 0.012500)^4 - 1 = 5.09%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 10% compounded daily. What is the AER (Annual Equivalent Rate)?', '10%', '11.02%', '304.17%', '10.52%', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 10%/365)^365 - 1 = (1 + 0.000274)^365 - 1 = 10.52%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 9% compounded monthly. What is the AER (Annual Equivalent Rate)?', '9.38%', '9%', '9.0%', '9.88%', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 9%/12)^12 - 1 = (1 + 0.007500)^12 - 1 = 9.38%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 12% compounded quarterly. What is the AER (Annual Equivalent Rate)?', '12%', '13.05%', '4.0%', '12.55%', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 12%/4)^4 - 1 = (1 + 0.030000)^4 - 1 = 12.55%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 5% compounded quarterly. What is the AER (Annual Equivalent Rate)?', '5.59%', '5%', '5.09%', '1.67%', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 5%/4)^4 - 1 = (1 + 0.012500)^4 - 1 = 5.09%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 11% compounded daily. What is the AER (Annual Equivalent Rate)?', '11%', '11.63%', '12.13%', '334.58%', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 11%/365)^365 - 1 = (1 + 0.000301)^365 - 1 = 11.63%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 11% compounded daily. What is the AER (Annual Equivalent Rate)?', '12.13%', '334.58%', '11.63%', '11%', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 11%/365)^365 - 1 = (1 + 0.000301)^365 - 1 = 11.63%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 8% compounded monthly. What is the AER (Annual Equivalent Rate)?', '8.8%', '8.0%', '8.3%', '8%', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 8%/12)^12 - 1 = (1 + 0.006667)^12 - 1 = 8.3%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 6% compounded quarterly. What is the AER (Annual Equivalent Rate)?', '6.14%', '2.0%', '6%', '6.64%', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 6%/4)^4 - 1 = (1 + 0.015000)^4 - 1 = 6.14%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 8% compounded monthly. What is the AER (Annual Equivalent Rate)?', '8%', '8.0%', '8.8%', '8.3%', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 8%/12)^12 - 1 = (1 + 0.006667)^12 - 1 = 8.3%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 6% compounded monthly. What is the AER (Annual Equivalent Rate)?', '6%', '6.17%', '6.0%', '6.67%', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 6%/12)^12 - 1 = (1 + 0.005000)^12 - 1 = 6.17%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 12% compounded daily. What is the AER (Annual Equivalent Rate)?', '12.75%', '12%', '13.25%', '365.0%', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 12%/365)^365 - 1 = (1 + 0.000329)^365 - 1 = 12.75%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 5% compounded daily. What is the AER (Annual Equivalent Rate)?', '5.13%', '5.63%', '5%', '152.08%', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 5%/365)^365 - 1 = (1 + 0.000137)^365 - 1 = 5.13%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 10% compounded daily. What is the AER (Annual Equivalent Rate)?', '11.02%', '10%', '304.17%', '10.52%', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 10%/365)^365 - 1 = (1 + 0.000274)^365 - 1 = 10.52%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 4% compounded quarterly. What is the AER (Annual Equivalent Rate)?', '4.56%', '4.06%', '4%', '1.33%', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 4%/4)^4 - 1 = (1 + 0.010000)^4 - 1 = 4.06%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A bank offers 10% compounded monthly. What is the AER (Annual Equivalent Rate)?', '10.47%', '10%', '10.97%', '10.0%', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1 + 10%/12)^12 - 1 = (1 + 0.008333)^12 - 1 = 10.47%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 5% compounded annually. Bank B offers 5% compounded daily. Which is better for savings?', 'Bank B (5% daily)', 'Bank A (5% annually)', 'Cannot compare', 'They are equal', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 5.0%, AER for B: 5.13%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 7% compounded quarterly. Bank B offers 8% compounded monthly. Which is better for savings?', 'They are equal', 'Bank A (7% quarterly)', 'Cannot compare', 'Bank B (8% monthly)', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 7.19%, AER for B: 8.3%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 7% compounded annually. Bank B offers 8% compounded daily. Which is better for savings?', 'Bank A (7% annually)', 'Cannot compare', 'Bank B (8% daily)', 'They are equal', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 7.0%, AER for B: 8.33%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 7% compounded quarterly. Bank B offers 7% compounded daily. Which is better for savings?', 'Cannot compare', 'They are equal', 'Bank B (7% daily)', 'Bank A (7% quarterly)', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 7.19%, AER for B: 7.25%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 5% compounded annually. Bank B offers 6% compounded monthly. Which is better for savings?', 'Cannot compare', 'Bank A (5% annually)', 'Bank B (6% monthly)', 'They are equal', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 5.0%, AER for B: 6.17%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 5% compounded quarterly. Bank B offers 5% compounded daily. Which is better for savings?', 'They are equal', 'Bank A (5% quarterly)', 'Cannot compare', 'Bank B (5% daily)', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 5.09%, AER for B: 5.13%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 8% compounded annually. Bank B offers 8% compounded daily. Which is better for savings?', 'Bank A (8% annually)', 'They are equal', 'Cannot compare', 'Bank B (8% daily)', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 8.0%, AER for B: 8.33%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 6% compounded quarterly. Bank B offers 6% compounded monthly. Which is better for savings?', 'Bank B (6% monthly)', 'Cannot compare', 'Bank A (6% quarterly)', 'They are equal', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 6.14%, AER for B: 6.17%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 5% compounded quarterly. Bank B offers 5% compounded monthly. Which is better for savings?', 'Cannot compare', 'Bank A (5% quarterly)', 'Bank B (5% monthly)', 'They are equal', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 5.09%, AER for B: 5.12%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 6% compounded quarterly. Bank B offers 7% compounded monthly. Which is better for savings?', 'They are equal', 'Cannot compare', 'Bank A (6% quarterly)', 'Bank B (7% monthly)', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 6.14%, AER for B: 7.23%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 7% compounded quarterly. Bank B offers 7% compounded monthly. Which is better for savings?', 'Bank B (7% monthly)', 'They are equal', 'Cannot compare', 'Bank A (7% quarterly)', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 7.19%, AER for B: 7.23%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bank A offers 6% compounded quarterly. Bank B offers 7% compounded monthly. Which is better for savings?', 'Bank B (7% monthly)', 'Bank A (6% quarterly)', 'Cannot compare', 'They are equal', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER for A: 6.14%, AER for B: 7.23%. Choose higher AER for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What does APR stand for?', 'Average Payment Rate', 'Annual Percentage Rate', 'Adjusted Prime Rate', 'Actual Principal Returned', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'APR = Annual Percentage Rate, used for loans.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What does AER stand for?', 'Average Earning Rate', 'Actual Expense Ratio', 'Annual Expected Return', 'Annual Equivalent Rate', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = Annual Equivalent Rate, used for savings.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('APR is primarily used for:', 'Comparing savings returns', 'Setting exchange rates', 'Comparing loan costs', 'Calculating tax', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'APR helps borrowers compare the true cost of loans.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AER is primarily used for:', 'Comparing loan costs', 'Setting mortgages', 'Calculating tax', 'Comparing savings returns', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER helps savers compare actual returns.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If nominal rate is 6% compounded monthly, is AER higher or lower?', 'Cannot determine', 'Higher', 'Lower', 'Same', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'More frequent compounding increases the effective rate.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a loan has fees, how do they affect APR?', 'APR excludes fees', 'Fees don''t affect APR', 'APR includes fees, so it''s higher than the interest rate alone', 'APR is lower with fees', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'APR accounts for fees and charges over the loan term.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What''s the relationship between nominal rate and AER when compounding is annual?', 'They are equal', 'Nominal is always higher', 'AER is always higher', 'They are never equal', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'With annual compounding, AER equals the nominal rate.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('As compounding frequency increases, what happens to AER?', 'AER decreases', 'AER stays the same', 'Cannot determine', 'AER increases', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'More frequent compounding means interest earns interest sooner.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is continuous compounding?', 'Compounding infinitely often (limit as n→∞)', 'Compounding once per year', 'No compounding', 'Compounding twice per year', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'The theoretical maximum compounding frequency.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for continuous compounding is:', 'A = P(1+r)ⁿ', 'A = Peʳᵗ', 'A = P/e^rt', 'A = P + Prt', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'Where e ≈ 2.71828 is the natural base.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If nominal rate is 10% compounded continuously, AER is:', '11%', 'Approximately 10.52%', '9.52%', '10%', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = e^0.10 - 1 ≈ 10.52%.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must lenders disclose APR?', 'Only for mortgages', 'It''s optional', 'For consumer protection and fair comparison', 'To increase profits', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'Regulations require APR disclosure to help consumers compare loans.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A credit card has 1.5% monthly interest. What is the APR?', '15%', '18%', '21%', '1.5%', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'APR = 1.5% × 12 = 18% (simple calculation for disclosure).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The same credit card''s AER would be:', 'Approximately 19.56%', '15%', '18%', '20%', 0,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER = (1.015)¹² - 1 ≈ 19.56%.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which rate is typically higher: nominal or AER (if compounding > annually)?', 'Depends on the bank', 'Nominal', 'AER', 'They are always equal', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER captures the effect of compounding within the year.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 0% APR offer means:', 'The loan is free', 'No interest charged during the promotional period', 'Interest is deferred', 'You pay only fees', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', '0% APR = interest-free for the offer period.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Representative APR must be offered to at least:', '100% of applicants', '51% of applicants', '10% of applicants', '75% of applicants', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'At least 51% must qualify for the advertised rate.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What does ''nominal rate'' mean?', 'The final rate paid', 'The stated rate before compounding effects', 'The rate after tax', 'The rate including fees', 1,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'Nominal = named/stated rate, not accounting for compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('EAR (Effective Annual Rate) is the same as:', 'Nominal rate', 'Base rate', 'APR', 'AER', 3,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'EAR and AER both mean the effective yearly rate.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If you want the best savings account, look for:', 'Lowest fees only', 'Highest APR', 'Highest AER', 'Lowest AER', 2,
'lc_hl_financial', 9, 'proficient', 'lc_hl', 'AER shows actual returns after compounding.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €50,000.00 and returns €7,902.00, €5,261.00, €11,576.00 over 3 years. At 10% discount rate, what is the NPV?', '€29,771.21', '€-29,771.21', '€-44,656.82', '€-25,261.00', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -50000 + 7902/1.10 + 5261/1.10² + 11576/1.10³ = €-29,771.21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €50,000.00 and returns €4,843.00, €6,329.00, €10,027.00 over 3 years. At 9% discount rate, what is the NPV?', '€32,487.20', '€-32,487.20', '€-48,730.80', '€-28,801.00', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -50000 + 4843/1.09 + 6329/1.09² + 10027/1.09³ = €-32,487.20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €20,000.00 and returns €6,136.00, €8,859.00, €11,033.00 over 3 years. At 12% discount rate, what is the NPV?', '€-393.98', '€393.98', '€6,028.00', '€590.97', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -20000 + 6136/1.12 + 8859/1.12² + 11033/1.12³ = €393.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €50,000.00 and returns €7,661.00, €8,242.00, €9,906.00 over 3 years. At 10% discount rate, what is the NPV?', '€-24,191.00', '€28,781.36', '€-43,172.04', '€-28,781.36', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -50000 + 7661/1.10 + 8242/1.10² + 9906/1.10³ = €-28,781.36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €10,000.00 and returns €4,665.00, €8,449.00, €7,104.00 over 3 years. At 8% discount rate, what is the NPV?', '€-7,202.48', '€10,218.00', '€10,803.72', '€7,202.48', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -10000 + 4665/1.08 + 8449/1.08² + 7104/1.08³ = €7,202.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €20,000.00 and returns €6,591.00, €6,144.00, €9,712.00 over 3 years. At 5% discount rate, what is the NPV?', '€-239.52', '€359.28', '€2,447.00', '€239.52', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -20000 + 6591/1.05 + 6144/1.05² + 9712/1.05³ = €239.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €20,000.00 and returns €7,097.00, €7,131.00, €8,897.00 over 3 years. At 12% discount rate, what is the NPV?', '€-2,468.84', '€3,125.00', '€-1,645.89', '€1,645.89', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -20000 + 7097/1.12 + 7131/1.12² + 8897/1.12³ = €-1,645.89', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €20,000.00 and returns €4,694.00, €9,529.00, €7,311.00 over 3 years. At 5% discount rate, what is the NPV?', '€570.92', '€-570.92', '€-856.38', '€1,534.00', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -20000 + 4694/1.05 + 9529/1.05² + 7311/1.05³ = €-570.92', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €20,000.00 and returns €6,153.00, €4,009.00, €10,112.00 over 3 years. At 5% discount rate, what is the NPV?', '€1,768.59', '€-2,652.88', '€-1,768.59', '€274.00', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -20000 + 6153/1.05 + 4009/1.05² + 10112/1.05³ = €-1,768.59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €10,000.00 and returns €6,282.00, €9,405.00, €6,590.00 over 3 years. At 10% discount rate, what is the NPV?', '€12,277.00', '€8,434.80', '€-8,434.80', '€12,652.20', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -10000 + 6282/1.10 + 9405/1.10² + 6590/1.10³ = €8,434.80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €50,000.00 and returns €6,748.00, €8,086.00, €5,995.00 over 3 years. At 8% discount rate, what is the NPV?', '€-29,171.00', '€-48,090.58', '€-32,060.39', '€32,060.39', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -50000 + 6748/1.08 + 8086/1.08² + 5995/1.08³ = €-32,060.39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €10,000.00 and returns €4,938.00, €8,025.00, €9,779.00 over 3 years. At 11% discount rate, what is the NPV?', '€12,168.36', '€12,742.00', '€-8,112.24', '€8,112.24', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -10000 + 4938/1.11 + 8025/1.11² + 9779/1.11³ = €8,112.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €20,000.00 and returns €7,302.00, €4,212.00, €7,654.00 over 3 years. At 9% discount rate, what is the NPV?', '€-832.00', '€-3,845.47', '€3,845.47', '€-5,768.20', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -20000 + 7302/1.09 + 4212/1.09² + 7654/1.09³ = €-3,845.47', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €20,000.00 and returns €6,895.00, €5,420.00, €10,329.00 over 3 years. At 6% discount rate, what is the NPV?', '€0.93', '€-0.93', '€1.40', '€2,644.00', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -20000 + 6895/1.06 + 5420/1.06² + 10329/1.06³ = €0.93', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment costs €10,000.00 and returns €6,534.00, €9,557.00, €9,692.00 over 3 years. At 7% discount rate, what is the NPV?', '€15,783.00', '€18,548.34', '€-12,365.56', '€12,365.56', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV = -10000 + 6534/1.07 + 9557/1.07² + 9692/1.07³ = €12,365.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €75,000.00, returns €34,115.00/year for 4 years. Project B: costs €68,565.00, returns €20,364.00/year for 4 years. At 7% discount rate, which is better?', 'Project A', 'Project B', 'Both are equally good', 'Neither (both have negative NPV)', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €40,554.71, NPV(B) = €412.17. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €75,000.00, returns €29,721.00/year for 4 years. Project B: costs €66,809.00, returns €22,152.00/year for 4 years. At 7% discount rate, which is better?', 'Project B', 'Neither (both have negative NPV)', 'Both are equally good', 'Project A', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €25,671.31, NPV(B) = €8,224.50. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €75,000.00, returns €24,842.00/year for 4 years. Project B: costs €68,416.00, returns €19,061.00/year for 4 years. At 7% discount rate, which is better?', 'Neither (both have negative NPV)', 'Project A', 'Both are equally good', 'Project B', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €9,145.10, NPV(B) = €-3,852.37. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €75,000.00, returns €24,500.00/year for 4 years. Project B: costs €81,969.00, returns €22,656.00/year for 4 years. At 7% discount rate, which is better?', 'Project A', 'Neither (both have negative NPV)', 'Project B', 'Both are equally good', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €7,986.68, NPV(B) = €-5,228.34. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €75,000.00, returns €33,403.00/year for 4 years. Project B: costs €72,226.00, returns €18,742.00/year for 4 years. At 9% discount rate, which is better?', 'Project B', 'Both are equally good', 'Neither (both have negative NPV)', 'Project A', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €33,216.36, NPV(B) = €-11,507.17. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €50,000.00, returns €28,590.00/year for 4 years. Project B: costs €57,159.00, returns €31,908.00/year for 4 years. At 9% discount rate, which is better?', 'Project B', 'Project A', 'Both are equally good', 'Neither (both have negative NPV)', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €42,623.59, NPV(B) = €46,213.98. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €75,000.00, returns €26,349.00/year for 4 years. Project B: costs €76,728.00, returns €31,159.00/year for 4 years. At 6% discount rate, which is better?', 'Project B', 'Project A', 'Both are equally good', 'Neither (both have negative NPV)', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €16,302.07, NPV(B) = €31,241.23. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €100,000.00, returns €34,625.00/year for 4 years. Project B: costs €106,055.00, returns €19,017.00/year for 4 years. At 7% discount rate, which is better?', 'Project B', 'Neither (both have negative NPV)', 'Project A', 'Both are equally good', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €17,282.19, NPV(B) = €-41,640.40. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €100,000.00, returns €23,866.00/year for 4 years. Project B: costs €98,134.00, returns €21,574.00/year for 4 years. At 7% discount rate, which is better?', 'Option 4', 'Both are equally good', 'Neither (both have negative NPV)', 'Project A', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €-19,160.82, NPV(B) = €-25,058.30. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €50,000.00, returns €27,919.00/year for 4 years. Project B: costs €51,320.00, returns €25,529.00/year for 4 years. At 9% discount rate, which is better?', 'Neither (both have negative NPV)', 'Project B', 'Project A', 'Both are equally good', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €40,449.74, NPV(B) = €31,386.81. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €100,000.00, returns €26,209.00/year for 4 years. Project B: costs €90,876.00, returns €22,596.00/year for 4 years. At 7% discount rate, which is better?', 'Project A', 'Option 4', 'Neither (both have negative NPV)', 'Both are equally good', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €-11,224.58, NPV(B) = €-14,338.57. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Project A: costs €75,000.00, returns €22,265.00/year for 4 years. Project B: costs €65,262.00, returns €22,234.00/year for 4 years. At 7% discount rate, which is better?', 'Project B', 'Both are equally good', 'Project A', 'Neither (both have negative NPV)', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV(A) = €416.26, NPV(B) = €10,049.26. Choose highest positive NPV.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €20,000.00. Each unit sells for €28 with variable cost €9. What is the break-even point?', '714 units', '842 units', '1053 units', '1263 units', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 20000 / (28 - 9) = 20000/19 = 1053 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €10,000.00. Each unit sells for €70 with variable cost €21. What is the break-even point?', '163 units', '204 units', '244 units', '142 units', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 10000 / (70 - 21) = 10000/49 = 204 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €10,000.00. Each unit sells for €98 with variable cost €14. What is the break-even point?', '119 units', '95 units', '102 units', '142 units', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 10000 / (98 - 14) = 10000/84 = 119 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €10,000.00. Each unit sells for €90 with variable cost €85. What is the break-even point?', '111 units', '1600 units', '2000 units', '2400 units', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 10000 / (90 - 85) = 10000/5 = 2000 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €50,000.00. Each unit sells for €78 with variable cost €52. What is the break-even point?', '1538 units', '2307 units', '641 units', '1923 units', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 50000 / (78 - 52) = 50000/26 = 1923 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €50,000.00. Each unit sells for €51 with variable cost €41. What is the break-even point?', '980 units', '5000 units', '4000 units', '6000 units', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 50000 / (51 - 41) = 50000/10 = 5000 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €10,000.00. Each unit sells for €38 with variable cost €22. What is the break-even point?', '625 units', '263 units', '500 units', '750 units', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 10000 / (38 - 22) = 10000/16 = 625 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €20,000.00. Each unit sells for €93 with variable cost €72. What is the break-even point?', '952 units', '761 units', '215 units', '1142 units', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 20000 / (93 - 72) = 20000/21 = 952 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €10,000.00. Each unit sells for €53 with variable cost €19. What is the break-even point?', '294 units', '352 units', '188 units', '235 units', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 10000 / (53 - 19) = 10000/34 = 294 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €10,000.00. Each unit sells for €96 with variable cost €12. What is the break-even point?', '119 units', '95 units', '104 units', '142 units', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 10000 / (96 - 12) = 10000/84 = 119 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €20,000.00. Each unit sells for €34 with variable cost €29. What is the break-even point?', '4800 units', '588 units', '4000 units', '3200 units', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 20000 / (34 - 29) = 20000/5 = 4000 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €20,000.00. Each unit sells for €54 with variable cost €48. What is the break-even point?', '3333 units', '370 units', '3999 units', '2666 units', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 20000 / (54 - 48) = 20000/6 = 3333 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed costs are €20,000.00. Each unit sells for €62 with variable cost €11. What is the break-even point?', '470 units', '392 units', '313 units', '322 units', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Break-even = Fixed Costs / (Price - Variable Cost) = 20000 / (62 - 11) = 20000/51 = 392 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What does a positive NPV indicate?', 'The investment is risk-free', 'The investment earns more than the discount rate', 'The investment loses money', 'The investment breaks even', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Positive NPV means the project adds value above the required return.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What does a negative NPV indicate?', 'The investment is profitable', 'The investment has no risk', 'The investment earns less than the discount rate', 'The investment should be accepted', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Negative NPV means the project doesn''t meet the required return.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('IRR (Internal Rate of Return) is the rate where:', 'NPV is maximised', 'Profit is highest', 'NPV equals zero', 'Risk is lowest', 2,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'IRR is the discount rate that makes NPV = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If IRR > required rate of return, you should:', 'Need more information', 'Accept the project', 'The project is too risky', 'Reject the project', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'IRR exceeding the hurdle rate indicates a good investment.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the payback period?', 'Time to recover the initial investment', 'Annual return rate', 'Total profit earned', 'Net present value', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Payback period ignores time value of money.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A limitation of payback period is:', 'It''s too complicated', 'It ignores cash flows after payback', 'It considers too many factors', 'It requires a discount rate', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'Payback doesn''t consider total profitability.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which metric accounts for time value of money?', 'Payback period only', 'NPV and IRR', 'Accounting profit only', 'Simple return only', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'NPV and IRR discount future cash flows.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If two projects are mutually exclusive, choose the one with:', 'Lower initial cost', 'Higher IRR', 'Shorter payback', 'Higher NPV', 3,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'For mutually exclusive projects, NPV is the best criterion.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The discount rate in NPV is also called:', 'Cost of capital or hurdle rate', 'Inflation rate', 'Exchange rate', 'Tax rate', 0,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'It represents the minimum required return.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Profitability Index = PV of cash flows / Initial investment. If PI > 1:', 'Need more analysis', 'Accept the project', 'PI is irrelevant', 'Reject the project', 1,
'lc_hl_financial', 10, 'advanced', 'lc_hl', 'PI > 1 means NPV is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €200,000.00 mortgage at 5% over 25 years. What is the outstanding balance after 6 years?', '€115,819.03', '€152,000.00', '€154,681.24', '€171,868.05', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 6 years (72 payments), 228 payments remain. Balance = PV of remaining payments = €171,868.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €150,000.00 mortgage at 5% over 30 years. What is the outstanding balance after 6 years?', '€92,023.26', '€134,902.96', '€120,000.00', '€121,412.66', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 6 years (72 payments), 288 payments remain. Balance = PV of remaining payments = €134,902.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €250,000.00 mortgage at 5% over 30 years. What is the outstanding balance after 7 years?', '€219,862.54', '€191,666.67', '€137,267.46', '€197,876.29', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 7 years (84 payments), 276 payments remain. Balance = PV of remaining payments = €219,862.54', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €200,000.00 mortgage at 4% over 25 years. What is the outstanding balance after 7 years?', '€146,125.76', '€144,000.00', '€111,323.41', '€162,361.95', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 7 years (84 payments), 216 payments remain. Balance = PV of remaining payments = €162,361.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €200,000.00 mortgage at 4% over 25 years. What is the outstanding balance after 3 years?', '€185,147.10', '€176,000.00', '€166,632.39', '€161,995.75', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 3 years (36 payments), 264 payments remain. Balance = PV of remaining payments = €185,147.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €150,000.00 mortgage at 3% over 25 years. What is the outstanding balance after 5 years?', '€107,320.98', '€115,432.39', '€120,000.00', '€128,258.21', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 5 years (60 payments), 240 payments remain. Balance = PV of remaining payments = €128,258.21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €250,000.00 mortgage at 5% over 25 years. What is the outstanding balance after 5 years?', '€199,305.42', '€200,000.00', '€221,450.47', '€162,311.49', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 5 years (60 payments), 240 payments remain. Balance = PV of remaining payments = €221,450.47', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €150,000.00 mortgage at 4% over 30 years. What is the outstanding balance after 5 years?', '€135,671.27', '€107,032.62', '€125,000.00', '€122,104.14', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 5 years (60 payments), 300 payments remain. Balance = PV of remaining payments = €135,671.27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €250,000.00 mortgage at 3% over 25 years. What is the outstanding balance after 8 years?', '€136,189.28', '€189,268.23', '€170,000.00', '€170,341.41', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 8 years (96 payments), 204 payments remain. Balance = PV of remaining payments = €189,268.23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €150,000.00 mortgage at 4% over 30 years. What is the outstanding balance after 4 years?', '€130,000.00', '€138,770.34', '€124,893.31', '€115,626.10', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 4 years (48 payments), 312 payments remain. Balance = PV of remaining payments = €138,770.34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €150,000.00 mortgage at 3% over 20 years. What is the outstanding balance after 6 years?', '€102,605.38', '€90,103.46', '€105,000.00', '€114,005.98', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 6 years (72 payments), 168 payments remain. Balance = PV of remaining payments = €114,005.98', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €250,000.00 mortgage at 4% over 25 years. What is the outstanding balance after 8 years?', '€123,319.16', '€170,000.00', '€175,583.13', '€195,092.37', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 8 years (96 payments), 204 payments remain. Balance = PV of remaining payments = €195,092.37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €150,000.00 mortgage at 4% over 30 years. What is the outstanding balance after 5 years?', '€107,032.62', '€122,104.14', '€125,000.00', '€135,671.27', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 5 years (60 payments), 300 payments remain. Balance = PV of remaining payments = €135,671.27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €250,000.00 mortgage at 4% over 20 years. What is the outstanding balance after 6 years?', '€175,173.55', '€194,637.28', '€140,923.54', '€175,000.00', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 6 years (72 payments), 168 payments remain. Balance = PV of remaining payments = €194,637.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €150,000.00 mortgage at 5% over 25 years. What is the outstanding balance after 4 years?', '€126,000.00', '€136,646.34', '€122,981.71', '€107,909.52', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'After 4 years (48 payments), 252 payments remain. Balance = PV of remaining payments = €136,646.34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €250,000.00, 25-year mortgage at 5%, what''s the effect of paying an extra €100/month?', 'Save €12,691.36, pay off 1 year early', 'Save €25,382.72, pay off 3.0 years early', 'Save €30,000.00, same payoff time', 'No significant savings', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €200,000.00, 25-year mortgage at 5%, what''s the effect of paying an extra €100/month?', 'No significant savings', 'Save €12,252.72, pay off 1 year early', 'Save €24,505.43, pay off 3.6 years early', 'Save €30,000.00, same payoff time', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €200,000.00, 25-year mortgage at 3%, what''s the effect of paying an extra €500/month?', 'No significant savings', 'Save €38,897.92, pay off 10.9 years early', 'Save €150,000.00, same payoff time', 'Save €19,448.96, pay off 1 year early', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €200,000.00, 25-year mortgage at 5%, what''s the effect of paying an extra €500/month?', 'Save €73,102.96, pay off 11.1 years early', 'No significant savings', 'Save €150,000.00, same payoff time', 'Save €36,551.48, pay off 1 year early', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €200,000.00, 25-year mortgage at 3%, what''s the effect of paying an extra €200/month?', 'Save €10,811.23, pay off 1 year early', 'Save €21,622.45, pay off 5.9 years early', 'No significant savings', 'Save €60,000.00, same payoff time', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €250,000.00, 25-year mortgage at 5%, what''s the effect of paying an extra €500/month?', 'No significant savings', 'Save €150,000.00, same payoff time', 'Save €81,204.61, pay off 9.8 years early', 'Save €40,602.31, pay off 1 year early', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €250,000.00, 25-year mortgage at 3%, what''s the effect of paying an extra €100/month?', 'Save €30,000.00, same payoff time', 'No significant savings', 'Save €6,412.51, pay off 1 year early', 'Save €12,825.01, pay off 2.8 years early', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €250,000.00, 25-year mortgage at 5%, what''s the effect of paying an extra €200/month?', 'Save €22,216.15, pay off 1 year early', 'No significant savings', 'Save €60,000.00, same payoff time', 'Save €44,432.29, pay off 5.2 years early', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €200,000.00, 25-year mortgage at 3%, what''s the effect of paying an extra €200/month?', 'Save €60,000.00, same payoff time', 'Save €21,622.45, pay off 5.9 years early', 'No significant savings', 'Save €10,811.23, pay off 1 year early', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €250,000.00, 25-year mortgage at 3%, what''s the effect of paying an extra €500/month?', 'No significant savings', 'Save €42,898.08, pay off 9.5 years early', 'Save €21,449.04, pay off 1 year early', 'Save €150,000.00, same payoff time', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €200,000.00, 25-year mortgage at 4%, what''s the effect of paying an extra €500/month?', 'Save €150,000.00, same payoff time', 'No significant savings', 'Save €27,559.90, pay off 1 year early', 'Save €55,119.81, pay off 11.0 years early', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a €250,000.00, 25-year mortgage at 3%, what''s the effect of paying an extra €200/month?', 'Save €11,407.08, pay off 1 year early', 'No significant savings', 'Save €60,000.00, same payoff time', 'Save €22,814.17, pay off 5.0 years early', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Extra payments reduce principal faster, saving interest and shortening the loan term significantly.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €150,000.00 from 6% to 5% over 24 years with €3,000.00 closing costs. Is it worth it?', 'Save €88.62/month, break even in 34 months', 'Save €177.24/month, break even in 17 months', 'Not worth refinancing', 'Save €88.62/month, never break even', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €983.97 - €895.35 = €88.62. Break-even = €3,000.00 / €88.62 = 34 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €150,000.00 from 5% to 3% over 18 years with €5,000.00 closing costs. Is it worth it?', 'Save €154.97/month, break even in 32 months', 'Save €154.97/month, never break even', 'Save €309.94/month, break even in 16 months', 'Not worth refinancing', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,054.55 - €899.58 = €154.97. Break-even = €5,000.00 / €154.97 = 32 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €200,000.00 from 7% to 5% over 22 years with €2,000.00 closing costs. Is it worth it?', 'Save €472.58/month, break even in 4 months', 'Not worth refinancing', 'Save €236.29/month, never break even', 'Save €236.29/month, break even in 8 months', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,486.85 - €1,250.56 = €236.29. Break-even = €2,000.00 / €236.29 = 8 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €200,000.00 from 5% to 3% over 20 years with €5,000.00 closing costs. Is it worth it?', 'Save €210.72/month, break even in 24 months', 'Not worth refinancing', 'Save €210.72/month, never break even', 'Save €421.44/month, break even in 12 months', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,319.91 - €1,109.20 = €210.72. Break-even = €5,000.00 / €210.72 = 24 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €150,000.00 from 7% to 5% over 18 years with €5,000.00 closing costs. Is it worth it?', 'Not worth refinancing', 'Save €337.40/month, break even in 15 months', 'Save €168.70/month, never break even', 'Save €168.70/month, break even in 30 months', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,223.25 - €1,054.55 = €168.70. Break-even = €5,000.00 / €168.70 = 30 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €250,000.00 from 6% to 5% over 19 years with €2,000.00 closing costs. Is it worth it?', 'Save €139.51/month, never break even', 'Save €139.51/month, break even in 14 months', 'Not worth refinancing', 'Save €279.02/month, break even in 7 months', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,840.21 - €1,700.69 = €139.51. Break-even = €2,000.00 / €139.51 = 14 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €250,000.00 from 6% to 4% over 24 years with €2,000.00 closing costs. Is it worth it?', 'Save €576.44/month, break even in 3 months', 'Not worth refinancing', 'Save €288.22/month, never break even', 'Save €288.22/month, break even in 7 months', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,639.95 - €1,351.73 = €288.22. Break-even = €2,000.00 / €288.22 = 7 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €250,000.00 from 6% to 5% over 18 years with €2,000.00 closing costs. Is it worth it?', 'Save €137.82/month, break even in 15 months', 'Save €137.82/month, never break even', 'Not worth refinancing', 'Save €275.64/month, break even in 7 months', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,895.41 - €1,757.58 = €137.82. Break-even = €2,000.00 / €137.82 = 15 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €200,000.00 from 5% to 3% over 19 years with €3,000.00 closing costs. Is it worth it?', 'Save €208.67/month, break even in 14 months', 'Save €208.67/month, never break even', 'Not worth refinancing', 'Save €417.34/month, break even in 7 months', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,360.56 - €1,151.88 = €208.67. Break-even = €3,000.00 / €208.67 = 14 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €200,000.00 from 5% to 4% over 19 years with €5,000.00 closing costs. Is it worth it?', 'Save €106.81/month, break even in 47 months', 'Save €106.81/month, never break even', 'Not worth refinancing', 'Save €213.62/month, break even in 23 months', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,360.56 - €1,253.74 = €106.81. Break-even = €5,000.00 / €106.81 = 47 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €200,000.00 from 7% to 5% over 15 years with €5,000.00 closing costs. Is it worth it?', 'Save €216.07/month, never break even', 'Save €216.07/month, break even in 23 months', 'Save €432.14/month, break even in 11 months', 'Not worth refinancing', 1,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,797.66 - €1,581.59 = €216.07. Break-even = €5,000.00 / €216.07 = 23 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €150,000.00 from 6% to 4% over 19 years with €3,000.00 closing costs. Is it worth it?', 'Save €327.64/month, break even in 9 months', 'Not worth refinancing', 'Save €163.82/month, break even in 18 months', 'Save €163.82/month, never break even', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,104.12 - €940.31 = €163.82. Break-even = €3,000.00 / €163.82 = 18 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Refinance €200,000.00 from 5% to 4% over 23 years with €5,000.00 closing costs. Is it worth it?', 'Save €111.31/month, never break even', 'Not worth refinancing', 'Save €222.62/month, break even in 22 months', 'Save €111.31/month, break even in 45 months', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Monthly savings = €1,220.81 - €1,109.50 = €111.31. Break-even = €5,000.00 / €111.31 = 45 months.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('15-year vs 30-year mortgage: which has higher monthly payment?', '30-year mortgage', 'Depends on the rate', 'They are equal', '15-year mortgage', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Shorter term means higher payments but less total interest.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('15-year vs 30-year mortgage: which pays more total interest?', 'Cannot determine', 'They are equal', '30-year mortgage', '15-year mortgage', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Longer term accumulates much more interest despite lower payments.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fixed vs variable rate: which has predictable payments?', 'Variable rate', 'Both are predictable', 'Fixed rate', 'Neither', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Fixed rates lock in payment amounts; variable rates can change.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When might a variable rate be better than fixed?', 'When rates are rising', 'When you have bad credit', 'When rates are expected to fall', 'Never', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Variable rates benefit from falling interest rates.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is a balloon payment?', 'A large final payment to clear the loan', 'A type of insurance', 'Extra small payments', 'An early payoff penalty', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Balloon loans have low regular payments and a large lump sum at the end.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interest-only loans have lower monthly payments because:', 'The term is longer', 'There are no fees', 'Interest rates are lower', 'Principal is not being repaid monthly', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Only interest is paid; principal is due at term end.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is LTV (Loan-to-Value) ratio?', 'Loan amount divided by property value', 'Total interest paid', 'Years remaining', 'Monthly payment amount', 0,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'LTV measures how much of the property value is borrowed.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Higher LTV typically means:', 'No effect on terms', 'Lower interest rate', 'Higher interest rate and may require PMI', 'Faster approval', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'Lenders charge more for higher-risk, higher LTV loans.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is PMI (Private Mortgage Insurance)?', 'Principal and interest combined', 'Tax on mortgage interest', 'Insurance required when LTV is high (usually >80%)', 'A type of loan', 2,
'lc_hl_financial', 11, 'advanced', 'lc_hl', 'PMI protects the lender if the borrower defaults.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bi-weekly payments instead of monthly result in:', 'Larger final payment', 'Higher total interest', 'No difference from monthly', 'One extra monthly payment per year, faster payoff', 3,
'lc_hl_financial', 11, 'advanced', 'lc_hl', '26 bi-weekly payments = 13 monthly equivalents per year.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000.00 is invested at 4% compound interest. After 5 years, how much will be in the account after another 4 years?', '€7,828.22', '€6,083.26', '€7,116.56', '€6,800.00', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 5 years: €6,083.26. After 9 years total: €7,116.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000.00 is invested at 6% compound interest. After 6 years, how much will be in the account after another 2 years?', '€15,938.48', '€17,532.33', '€14,185.19', '€14,800.00', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 6 years: €14,185.19. After 8 years total: €15,938.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000.00 is invested at 6% compound interest. After 6 years, how much will be in the account after another 4 years?', '€7,092.60', '€9,849.66', '€8,954.24', '€8,000.00', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 6 years: €7,092.60. After 10 years total: €8,954.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000.00 is invested at 5% compound interest. After 6 years, how much will be in the account after another 3 years?', '€7,756.64', '€6,700.48', '€8,532.30', '€7,250.00', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 6 years: €6,700.48. After 9 years total: €7,756.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000.00 is invested at 6% compound interest. After 6 years, how much will be in the account after another 4 years?', '€16,000.00', '€19,699.33', '€17,908.48', '€14,185.19', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 6 years: €14,185.19. After 10 years total: €17,908.48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000.00 is invested at 8% compound interest. After 4 years, how much will be in the account after another 2 years?', '€14,800.00', '€13,604.89', '€17,455.61', '€15,868.74', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 4 years: €13,604.89. After 6 years total: €15,868.74', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€10,000.00 is invested at 6% compound interest. After 4 years, how much will be in the account after another 3 years?', '€15,036.30', '€14,200.00', '€16,539.93', '€12,624.77', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 4 years: €12,624.77. After 7 years total: €15,036.30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000.00 is invested at 6% compound interest. After 5 years, how much will be in the account after another 4 years?', '€7,700.00', '€6,691.13', '€8,447.39', '€9,292.13', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 5 years: €6,691.13. After 9 years total: €8,447.39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000.00 is invested at 4% compound interest. After 5 years, how much will be in the account after another 2 years?', '€6,083.26', '€6,579.66', '€6,400.00', '€7,237.63', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 5 years: €6,083.26. After 7 years total: €6,579.66', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€5,000.00 is invested at 4% compound interest. After 5 years, how much will be in the account after another 4 years?', '€7,828.22', '€7,116.56', '€6,800.00', '€6,083.26', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 5 years: €6,083.26. After 9 years total: €7,116.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €10,000.00 now plus €3,000.00 each year for 11 years at 4%. What is the total future value?', '€43,000.00', '€55,853.59', '€15,394.54', '€40,459.05', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €15,394.54. FV of annuity: €40,459.05. Total: €55,853.59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €20,000.00 now plus €3,000.00 each year for 11 years at 5%. What is the total future value?', '€42,620.36', '€34,206.79', '€76,827.15', '€53,000.00', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €34,206.79. FV of annuity: €42,620.36. Total: €76,827.15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €20,000.00 now plus €2,000.00 each year for 11 years at 7%. What is the total future value?', '€42,097.04', '€31,567.20', '€73,664.24', '€42,000.00', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €42,097.04. FV of annuity: €31,567.20. Total: €73,664.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €20,000.00 now plus €5,000.00 each year for 11 years at 7%. What is the total future value?', '€75,000.00', '€78,918.00', '€42,097.04', '€121,015.04', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €42,097.04. FV of annuity: €78,918.00. Total: €121,015.04', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €10,000.00 now plus €5,000.00 each year for 12 years at 4%. What is the total future value?', '€16,010.32', '€91,139.35', '€75,129.03', '€70,000.00', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €16,010.32. FV of annuity: €75,129.03. Total: €91,139.35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €10,000.00 now plus €2,000.00 each year for 14 years at 5%. What is the total future value?', '€19,799.32', '€39,197.26', '€38,000.00', '€58,996.58', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €19,799.32. FV of annuity: €39,197.26. Total: €58,996.58', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €10,000.00 now plus €2,000.00 each year for 14 years at 7%. What is the total future value?', '€45,100.98', '€38,000.00', '€25,785.34', '€70,886.32', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €25,785.34. FV of annuity: €45,100.98. Total: €70,886.32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €10,000.00 now plus €5,000.00 each year for 12 years at 7%. What is the total future value?', '€89,442.26', '€111,964.17', '€22,521.92', '€70,000.00', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €22,521.92. FV of annuity: €89,442.26. Total: €111,964.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €10,000.00 now plus €3,000.00 each year for 14 years at 4%. What is the total future value?', '€17,316.76', '€52,000.00', '€72,192.50', '€54,875.73', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €17,316.76. FV of annuity: €54,875.73. Total: €72,192.50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('You invest €20,000.00 now plus €2,000.00 each year for 15 years at 6%. What is the total future value?', '€94,483.10', '€47,931.16', '€46,551.94', '€50,000.00', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'FV of lump sum: €47,931.16. FV of annuity: €46,551.94. Total: €94,483.10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 7% nominally. If inflation is 3%, what is the real rate of return?', '3.88%', '7%', '10%', '4%', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.07) / (1 + 0.03) - 1 = 3.88% (or approximately 7% - 3% = 4%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 8% nominally. If inflation is 3%, what is the real rate of return?', '11%', '8%', '5%', '4.85%', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.08) / (1 + 0.03) - 1 = 4.85% (or approximately 8% - 3% = 5%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 8% nominally. If inflation is 4%, what is the real rate of return?', '8%', '4%', '3.85%', '12%', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.08) / (1 + 0.04) - 1 = 3.85% (or approximately 8% - 4% = 4%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 6% nominally. If inflation is 4%, what is the real rate of return?', '1.92%', '10%', '6%', '2%', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.06) / (1 + 0.04) - 1 = 1.92% (or approximately 6% - 4% = 2%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 7% nominally. If inflation is 3%, what is the real rate of return?', '10%', '4%', '7%', '3.88%', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.07) / (1 + 0.03) - 1 = 3.88% (or approximately 7% - 3% = 4%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 6% nominally. If inflation is 3%, what is the real rate of return?', '2.91%', '9%', '6%', '3%', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.06) / (1 + 0.03) - 1 = 2.91% (or approximately 6% - 3% = 3%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 10% nominally. If inflation is 4%, what is the real rate of return?', '10%', '5.77%', '14%', '6%', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.1) / (1 + 0.04) - 1 = 5.77% (or approximately 10% - 4% = 6%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 8% nominally. If inflation is 2%, what is the real rate of return?', '5.88%', '6%', '10%', '8%', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.08) / (1 + 0.02) - 1 = 5.88% (or approximately 8% - 2% = 6%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 8% nominally. If inflation is 4%, what is the real rate of return?', '8%', '12%', '3.85%', '4%', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.08) / (1 + 0.04) - 1 = 3.85% (or approximately 8% - 4% = 4%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An investment returns 10% nominally. If inflation is 2%, what is the real rate of return?', '10%', '7.84%', '12%', '8%', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Real rate = (1 + 0.1) / (1 + 0.02) - 1 = 7.84% (or approximately 10% - 2% = 8%)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 33, planning to retire at 65 and need €60,000.00/year until age 87. At 5%, how much must be saved annually?', '€10,488.61', '€24,680.63', '€13,635.19', '€7,342.03', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €789,780.15. Annual savings for 32 years: €10,488.61', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 30, planning to retire at 65 and need €40,000.00/year until age 95. At 6%, how much must be saved annually?', '€15,731.24', '€3,458.66', '€6,423.23', '€4,940.95', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €550,593.25. Annual savings for 35 years: €4,940.95', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 29, planning to retire at 65 and need €60,000.00/year until age 91. At 5%, how much must be saved annually?', '€11,699.79', '€23,958.64', '€8,999.84', '€6,299.89', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €862,511.12. Annual savings for 36 years: €8,999.84', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 26, planning to retire at 65 and need €40,000.00/year until age 93. At 5%, how much must be saved annually?', '€5,223.06', '€3,656.14', '€15,280.13', '€6,789.98', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €595,925.09. Annual savings for 39 years: €5,223.06', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 25, planning to retire at 65 and need €50,000.00/year until age 92. At 4%, how much must be saved annually?', '€11,169.87', '€8,592.21', '€20,411.98', '€6,014.55', 1,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €816,479.29. Annual savings for 40 years: €8,592.21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 31, planning to retire at 65 and need €40,000.00/year until age 85. At 4%, how much must be saved annually?', '€10,116.21', '€5,447.19', '€15,988.62', '€7,781.70', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €543,613.05. Annual savings for 34 years: €7,781.70', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 35, planning to retire at 65 and need €40,000.00/year until age 92. At 6%, how much must be saved annually?', '€6,683.96', '€4,678.77', '€8,689.15', '€17,614.05', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €528,421.37. Annual savings for 30 years: €6,683.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 29, planning to retire at 65 and need €40,000.00/year until age 88. At 4%, how much must be saved annually?', '€16,507.60', '€9,955.83', '€5,360.83', '€7,658.33', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €594,273.67. Annual savings for 36 years: €7,658.33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 27, planning to retire at 65 and need €60,000.00/year until age 87. At 4%, how much must be saved annually?', '€10,085.65', '€22,817.55', '€13,111.34', '€7,059.95', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €867,066.92. Annual savings for 38 years: €10,085.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Age 25, planning to retire at 65 and need €60,000.00/year until age 92. At 5%, how much must be saved annually?', '€21,964.55', '€5,091.13', '€7,273.04', '€9,454.95', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Fund needed at 65: €878,582.02. Annual savings for 40 years: €7,273.04', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A business borrows €100,000 at 6% for 5 years. After 2 years, they refinance the balance at 4% for 3 more years. Compare total interest paid vs. keeping original loan.', 'Refinancing saves money', 'Insufficient information', 'Cannot be determined', 'Both options are equivalent', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Original interest is higher over full term; refinancing at lower rate reduces total cost even with some early interest paid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Invest €500/month for 20 years at 7%, then stop contributing but leave invested for 10 more years. What''s the final amount?', 'Both options are equivalent', 'Cannot be determined', 'Insufficient information', 'Approximately €521,000', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'After 20 years: ~€260,000. This grows for 10 years at 7%: €260,000 × 1.07¹⁰ ≈ €521,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Person A invests €10,000 at age 25 and adds nothing. Person B waits until 35, then invests €10,000/year until 65. At 8%, who has more at 65?', 'Insufficient information', 'Cannot be determined', 'Likely Person B due to larger total contributions', 'Both options are equivalent', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'A: €10,000 × 1.08⁴⁰ ≈ €217,000. B: Annuity for 30 years ≈ €1.2 million. Contributions matter!', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A €300,000 mortgage at 4% over 30 years. How much is still owed after 15 years?', 'Insufficient information', 'Cannot be determined', 'Both options are equivalent', 'Approximately €194,000', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Payment ≈ €1,432/month. After 15 years, balance = PV of remaining 180 payments ≈ €194,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Investment A: 8% compounded quarterly. Investment B: 8.1% compounded annually. Which has higher AER?', 'Cannot be determined', 'Both options are equivalent', 'Investment A (AER ≈ 8.24%)', 'Insufficient information', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'A: AER = (1 + 0.08/4)⁴ - 1 = 8.24%. B: AER = 8.1%. A is better despite lower nominal rate.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Save €200/month at 6% for 10 years, or €400/month for 5 years. Same total contribution - which yields more?', 'Insufficient information', 'Cannot be determined', 'Both options are equivalent', '€200/month for 10 years yields more', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Longer investment period allows more compound growth despite same total deposits.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A loan has APR of 12%. What is the equivalent monthly rate?', 'Cannot be determined', 'Both options are equivalent', 'Insufficient information', '1% per month', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'APR / 12 = 12% / 12 = 1% per month', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€50,000 depreciates at 15% per year. €30,000 depreciates at 10% per year. When are they equal in value?', 'After approximately 9.5 years', 'Insufficient information', 'Both options are equivalent', 'Cannot be determined', 0,
'lc_hl_financial', 12, 'advanced', 'lc_hl', '50,000(0.85)ⁿ = 30,000(0.90)ⁿ. Solving: n ≈ 9.5 years', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A perpetuity pays €5,000/year. If sold for €100,000, what discount rate does this imply?', 'Cannot be determined', 'Both options are equivalent', 'Insufficient information', '5%', 3,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'PV = PMT/r, so r = PMT/PV = 5,000/100,000 = 5%', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('€100,000 is needed in 15 years. Should you invest €X now, or €Y per year? Rate is 5%.', 'Both options are equivalent', 'Insufficient information', 'Need €48,102 now OR €4,634 per year', 'Cannot be determined', 2,
'lc_hl_financial', 12, 'advanced', 'lc_hl', 'Lump sum: PV = 100,000/1.05¹⁵ = €48,102. Annuity: PMT = 100,000 × 0.05/(1.05¹⁵-1) = €4,634/year', 1);
-- Verification
SELECT 'Financial Maths questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_hl_financial';
SELECT difficulty_level, COUNT(*) as questions FROM questions_adaptive WHERE topic = 'lc_hl_financial' GROUP BY difficulty_level ORDER BY difficulty_level;
