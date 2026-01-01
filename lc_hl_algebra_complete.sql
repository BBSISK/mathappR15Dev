-- Add Algebra topic to LC Higher Level strand
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < add_lc_hl_algebra_topic.sql

INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_algebra', 'Algebra', id, '🔤', 3, 1
FROM strands WHERE name = 'LC Higher Level';

-- Verify
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_algebra';
-- LC Higher Level - Algebra Questions
-- Generated: 2025-12-14
-- Total: 600 questions

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify x^3 × x^2', 'x^1', 'x^5', 'x^3', 'x^6', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So x^3 × x^2 = x^5 = x^5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^5 × 3^5', '3^0', '3^10', '3^5', '3^25', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 3^5 × 3^5 = 3^10 = 3^10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify a^2 × a^5', 'a^2', 'a^10', 'a^3', 'a^7', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So a^2 × a^5 = a^7 = a^7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify a^5 × a^2', 'a^10', 'a^7', 'a^5', 'a^3', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So a^5 × a^2 = a^7 = a^7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify x^5 × x^4', 'x^1', 'x^9', 'x^5', 'x^20', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So x^5 × x^4 = x^9 = x^9 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^4 × 3^4', '3^4', '3^0', '3^8', '3^16', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 3^4 × 3^4 = 3^8 = 3^8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2^3 × 2^5', '2^15', '2^3', '2^8', '2^2', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 2^3 × 2^5 = 2^8 = 2^8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^4 × 3^3', '3^4', '3^12', '3^7', '3^1', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 3^4 × 3^3 = 3^7 = 3^7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify x^4 × x^4', 'x^8', 'x^16', 'x^4', 'x^0', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So x^4 × x^4 = x^8 = x^8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^3 × 3^4', '3^1', '3^12', '3^7', '3^3', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 3^3 × 3^4 = 3^7 = 3^7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^3 × 3^5', '3^3', '3^8', '3^15', '3^2', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 3^3 × 3^5 = 3^8 = 3^8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify x^3 × x^3', 'x^3', 'x^9', 'x^6', 'x^0', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So x^3 × x^3 = x^6 = x^6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^3 × 3^2', '3^3', '3^5', '3^1', '3^6', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 3^3 × 3^2 = 3^5 = 3^5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^5 × 3^3', '3^2', '3^5', '3^15', '3^8', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 3^5 × 3^3 = 3^8 = 3^8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2^3 × 2^5', '2^2', '2^8', '2^15', '2^3', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m × a^n = a^(m+n). So 2^3 × 2^5 = 2^8 = 2^8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5^5 ÷ 5^4', '5^4', '5^20', '5^1', '5^9', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 5^5 ÷ 5^4 = 5^1 = 5^1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify a^6 ÷ a^3', 'a^9', 'a^18', 'a^3', 'Option 4', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So a^6 ÷ a^3 = a^3 = a^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify x^5 ÷ x^4', 'x^9', 'x^4', 'x^20', 'x^1', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So x^5 ÷ x^4 = x^1 = x^1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2^6 ÷ 2^4', '2^4', '2^2', '2^10', '2^24', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 2^6 ÷ 2^4 = 2^2 = 2^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^6 ÷ 3^4', '3^24', '3^4', '3^2', '3^10', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 3^6 ÷ 3^4 = 3^2 = 3^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^7 ÷ 3^4', '3^4', '3^11', '3^28', '3^3', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 3^7 ÷ 3^4 = 3^3 = 3^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify x^8 ÷ x^2', 'x^6', 'x^2', 'x^10', 'x^16', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So x^8 ÷ x^2 = x^6 = x^6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^5 ÷ 3^2', '3^10', '3^2', '3^3', '3^7', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 3^5 ÷ 3^2 = 3^3 = 3^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5^6 ÷ 5^3', '5^18', '5^3', '5^9', 'Option 4', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 5^6 ÷ 5^3 = 5^3 = 5^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^6 ÷ 3^2', '3^4', '3^12', '3^8', '3^2', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 3^6 ÷ 3^2 = 3^4 = 3^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2^7 ÷ 2^2', '2^5', '2^14', '2^2', '2^9', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 2^7 ÷ 2^2 = 2^5 = 2^5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3^5 ÷ 3^2', '3^7', '3^3', '3^2', '3^10', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 3^5 ÷ 3^2 = 3^3 = 3^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2^8 ÷ 2^3', '2^24', '2^5', '2^11', '2^3', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So 2^8 ÷ 2^3 = 2^5 = 2^5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify a^8 ÷ a^3', 'a^24', 'a^3', 'a^5', 'a^11', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So a^8 ÷ a^3 = a^5 = a^5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify x^6 ÷ x^2', 'x^8', 'x^12', 'x^2', 'x^4', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Index law: a^m ÷ a^n = a^(m-n). So x^6 ÷ x^2 = x^4 = x^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (a^2)^3', 'a^2', 'a^6', 'a^3', 'a^5', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (a^2)^3 = a^(m*n) = a^6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (x^2)^2', 'x^2', 'Option 4', 'Option 3', 'x^4', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (x^2)^2 = x^(m*n) = x^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (2^2)^3', '2^6', '2^5', '2^3', '2^2', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (2^2)^3 = 2^(m*n) = 2^6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (x^3)^2', 'x^3', 'x^6', 'x^2', 'x^5', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (x^3)^2 = x^(m*n) = x^6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (2^4)^3', '2^7', '2^12', '2^4', '2^3', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (2^4)^3 = 2^(m*n) = 2^12 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (a^3)^3', 'a^6', 'Option 4', 'a^3', 'a^9', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (a^3)^3 = a^(m*n) = a^9 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (x^4)^3', 'x^12', 'x^7', 'x^3', 'x^4', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (x^4)^3 = x^(m*n) = x^12 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (2^3)^3', '2^6', 'Option 4', '2^9', '2^3', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (2^3)^3 = 2^(m*n) = 2^9 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (3^4)^2', '3^4', '3^8', '3^6', '3^2', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (3^4)^2 = 3^(m*n) = 3^8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (a^2)^2', 'a^2', 'Option 4', 'Option 3', 'a^4', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Power law: (a^m)^n = a^(mn). So (a^2)^2 = a^(m*n) = a^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 5^(-1) with positive indices', '5^1', '1/5^1', '-1/5^1', '-5^1', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'a^(-n) = 1/a^n. So 5^(-1) = 1/5^1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 5^0?', '5', '0', '1', '-1', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Any number to the power of 0 equals 1. 5^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 5^(-1) with positive indices', '-5^1', '1/5^1', '-1/5^1', '5^1', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'a^(-n) = 1/a^n. So 5^(-1) = 1/5^1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 5^0?', '5', '0', '-1', '1', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Any number to the power of 0 equals 1. 5^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 3^(-1) with positive indices', '-3^1', '-1/3^1', '1/3^1', '3^1', 2,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'a^(-n) = 1/a^n. So 3^(-1) = 1/3^1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 2^(-3) with positive indices', '-1/2^3', '1/2^3', '2^3', '-2^3', 1,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'a^(-n) = 1/a^n. So 2^(-3) = 1/2^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 3^0?', '0', '-1', '3', '1', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Any number to the power of 0 equals 1. 3^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 2^0?', '1', '2', '-1', '0', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Any number to the power of 0 equals 1. 2^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 3^(-2) with positive indices', '-1/3^2', '3^2', '-3^2', '1/3^2', 3,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'a^(-n) = 1/a^n. So 3^(-2) = 1/3^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is 5^0?', '1', '5', '0', '-1', 0,
'lc_hl_algebra', 1, 'foundation', 'lc_hl', 'Any number to the power of 0 equals 1. 5^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √216', '6√6', '12', 'Option 4', '√216', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√216 = √(36×6) = √36 × √6 = 6√6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √150', '11', '6√5', '√150', '5√6', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√150 = √(25×6) = √25 × √6 = 5√6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √96', '4√6', '10', '6√4', '√96', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√96 = √(16×6) = √16 × √6 = 4√6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √245', '7√5', '12', '5√7', '√245', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√245 = √(49×5) = √49 × √5 = 7√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √294', '7√6', '√294', '6√7', '13', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√294 = √(49×6) = √49 × √6 = 7√6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √112', '4√7', '11', '√112', '7√4', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√112 = √(16×7) = √16 × √7 = 4√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √63', '7√3', '10', '√63', '3√7', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√63 = √(9×7) = √9 × √7 = 3√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √108', '6√3', '√108', '9', '3√6', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√108 = √(36×3) = √36 × √3 = 6√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √175', '7√5', '12', '√175', '5√7', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√175 = √(25×7) = √25 × √7 = 5√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √50', '√50', '2√5', '7', '5√2', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√50 = √(25×2) = √25 × √2 = 5√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √12', '5', '2√3', '√12', '3√2', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√12 = √(4×3) = √4 × √3 = 2√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √175', '√175', '5√7', '12', '7√5', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√175 = √(25×7) = √25 × √7 = 5√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √150', '5√6', '6√5', '√150', '11', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√150 = √(25×6) = √25 × √6 = 5√6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √27', '6', '3√3', 'Option 4', '√27', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√27 = √(9×3) = √9 × √3 = 3√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √50', '5√2', '7', '2√5', '√50', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√50 = √(25×2) = √25 × √2 = 5√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √98', '7√2', '2√7', '9', '√98', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√98 = √(49×2) = √49 × √2 = 7√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √343', '√343', '14', '7√7', 'Option 4', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√343 = √(49×7) = √49 × √7 = 7√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √54', '3√6', '√54', '6√3', '9', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√54 = √(9×6) = √9 × √6 = 3√6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √125', 'Option 4', '√125', '5√5', '10', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√125 = √(25×5) = √25 × √5 = 5√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √75', '3√5', '5√3', '8', '√75', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√75 = √(25×3) = √25 × √3 = 5√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √32', '6', '√32', '4√2', '2√4', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√32 = √(16×2) = √16 × √2 = 4√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √54', '6√3', '9', '3√6', '√54', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√54 = √(9×6) = √9 × √6 = 3√6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √147', '√147', '7√3', '3√7', '10', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√147 = √(49×3) = √49 × √3 = 7√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √175', '12', '7√5', '5√7', '√175', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√175 = √(25×7) = √25 × √7 = 5√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √125', 'Option 4', '10', '√125', '5√5', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√125 = √(25×5) = √25 × √5 = 5√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √5', '√10', '5', '√5', '1', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√5 is already in simplest form (5 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √11', '11', '1', '√11', '√22', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√11 is already in simplest form (11 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √7', '√14', '7', '√7', '1', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√7 is already in simplest form (7 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √11', '√22', '11', '√11', '1', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√11 is already in simplest form (11 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3', '√6', '1', '√3', '3', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√3 is already in simplest form (3 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √11', '1', '√11', '11', '√22', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√11 is already in simplest form (11 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √11', '√22', '11', '√11', '1', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√11 is already in simplest form (11 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √13', '√13', '13', '1', '√26', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√13 is already in simplest form (13 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3', '√3', '3', '√6', '1', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√3 is already in simplest form (3 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3', '1', '√6', '√3', '3', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√3 is already in simplest form (3 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √11', '1', '√22', '√11', '11', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√11 is already in simplest form (11 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √2', '2', '√2', '1', '√4', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√2 is already in simplest form (2 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √11', '√11', '√22', '1', '11', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√11 is already in simplest form (11 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3', '3', '√3', '1', '√6', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√3 is already in simplest form (3 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √11', '√22', '11', '1', '√11', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√11 is already in simplest form (11 is prime) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √64', '7', '8', '64', '9', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√64 = 8 (since 8² = 64) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √16', '16', '3', '5', '4', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√16 = 4 (since 4² = 16) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √16', '4', '16', '3', '5', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√16 = 4 (since 4² = 16) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √81', '81', '9', '10', '8', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√81 = 9 (since 9² = 81) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √49', '6', '7', '8', '49', 1,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√49 = 7 (since 7² = 49) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √4', '4', '3', '2', '1', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√4 = 2 (since 2² = 4) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √49', '49', '8', '7', '6', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√49 = 7 (since 7² = 49) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √25', '5', '6', '25', '4', 0,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√25 = 5 (since 5² = 25) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √16', '16', '5', '4', '3', 2,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√16 = 4 (since 4² = 16) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate √100', '100', '9', '11', '10', 3,
'lc_hl_algebra', 2, 'foundation', 'lc_hl', '√100 = 10 (since 10² = 100) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5√7 + 3√7', '15', '15√7', '8√7', '√56', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '5√7 + 3√7 = (5+3)√7 = 8√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√3 + 2√3', '7', '4√3', 'Option 4', '√12', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√3 + 2√3 = (2+2)√3 = 4√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√7 + 4√7', '√42', '6√7', '13', '8√7', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√7 + 4√7 = (2+4)√7 = 6√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√3 + 3√3', '√15', '8', '6√3', '5√3', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√3 + 3√3 = (2+3)√3 = 5√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 4√7 + 5√7', '16', '20√7', '√63', '9√7', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '4√7 + 5√7 = (4+5)√7 = 9√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√7 + 3√7', '12', '5√7', '6√7', '√35', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√7 + 3√7 = (2+3)√7 = 5√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√5 + 3√5', '√25', '10', '6√5', '5√5', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√5 + 3√5 = (2+3)√5 = 5√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√2 + 4√2', '6√2', '8', '8√2', '√12', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√2 + 4√2 = (2+4)√2 = 6√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 4√2 + 2√2', '8√2', '6√2', '8', '√12', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '4√2 + 2√2 = (4+2)√2 = 6√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√7 + 5√7', '14', '10√7', '√49', '7√7', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√7 + 5√7 = (2+5)√7 = 7√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 2√7 + 3√7', '√35', '5√7', '6√7', '12', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '2√7 + 3√7 = (2+3)√7 = 5√7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 4√2 + 3√2', '7√2', '√14', '12√2', '9', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '4√2 + 3√2 = (4+3)√2 = 7√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5√2 + 3√2', '√16', '15√2', '8√2', '10', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '5√2 + 3√2 = (5+3)√2 = 8√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 3√3 + 5√3', '8√3', '√24', '15√3', '11', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '3√3 + 5√3 = (3+5)√3 = 8√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 4√2 + 4√2', '8√2', '10', '√16', '16√2', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '4√2 + 4√2 = (4+4)√2 = 8√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6√2 - 4√2', '10√2', '2', '2√2', '√4', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '6√2 - 4√2 = (6-4)√2 = 2√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6√2 - 3√2', '√6', '9√2', '3√2', '3', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '6√2 - 3√2 = (6-3)√2 = 3√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 7√5 - 4√5', '√15', '3√5', '3', '11√5', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '7√5 - 4√5 = (7-4)√5 = 3√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6√3 - 3√3', '√9', '3', '9√3', '3√3', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '6√3 - 3√3 = (6-3)√3 = 3√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8√2 - 3√2', '√10', '5√2', '11√2', '5', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '8√2 - 3√2 = (8-3)√2 = 5√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6√3 - 3√3', '9√3', '√9', '3√3', '3', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '6√3 - 3√3 = (6-3)√3 = 3√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5√5 - 2√5', '3√5', '7√5', '3', '√15', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '5√5 - 2√5 = (5-2)√5 = 3√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6√2 - 4√2', '10√2', '2', '√4', '2√2', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '6√2 - 4√2 = (6-4)√2 = 2√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5√5 - 3√5', '8√5', '2', '2√5', '√10', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '5√5 - 3√5 = (5-3)√5 = 2√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 6√5 - 2√5', '8√5', '√20', '4', '4√5', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '6√5 - 2√5 = (6-2)√5 = 4√5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √5 × √6', '√30', '√5 + √6', '√11', '5√6', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√5 × √6 = √(5×6) = √30 = √30 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3 × √2', '√3 + √2', '√6', '√5', '3√2', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√3 × √2 = √(3×2) = √6 = √6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3 × √6', '√3 + √6', '3√6', '3√2', '√9', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√3 × √6 = √(3×6) = √18 = 3√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √5 × √6', '√30', '√5 + √6', '√11', '5√6', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√5 × √6 = √(5×6) = √30 = √30 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3 × √6', '√3 + √6', '3√6', '√9', '3√2', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√3 × √6 = √(3×6) = √18 = 3√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √5 × √3', '√8', '√5 + √3', '√15', '5√3', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√5 × √3 = √(5×3) = √15 = √15 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3 × √3', '3√3', '√6', '3', '√3 + √3', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√3 × √3 = √(3×3) = √9 = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √5 × √2', '√10', '√7', '√5 + √2', '5√2', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√5 × √2 = √(5×2) = √10 = √10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3 × √5', '√3 + √5', '√15', '3√5', '√8', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√3 × √5 = √(3×5) = √15 = √15 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √2 × √6', '√8', '2√3', '√2 + √6', '2√6', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√2 × √6 = √(2×6) = √12 = 2√3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √2 × √3', '2√3', '√5', '√2 + √3', '√6', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√2 × √3 = √(2×3) = √6 = √6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √3 × √3', '3√3', '3', '√6', '√3 + √3', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√3 × √3 = √(3×3) = √9 = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √2 × √3', '2√3', '√2 + √3', '√6', '√5', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√2 × √3 = √(2×3) = √6 = √6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √2 × √5', '√10', '√7', '√2 + √5', '2√5', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√2 × √5 = √(2×5) = √10 = √10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √5 × √2', '5√2', '√10', '√5 + √2', '√7', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '√5 × √2 = √(5×2) = √10 = √10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√7)²', '√7', '7', '49', '2√7', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√7)² = 7. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√5)²', '5', '√5', '25', '2√5', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√5)² = 5. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√2)²', '2√2', '√2', '4', '2', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√2)² = 2. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√11)²', '2√11', '11', '121', '√11', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√11)² = 11. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√7)²', '7', '49', '√7', '2√7', 0,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√7)² = 7. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√2)²', '2√2', '4', '√2', '2', 3,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√2)² = 2. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√2)²', '4', '2', '√2', '2√2', 1,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√2)² = 2. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√3)²', '9', '2√3', '3', '√3', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√3)² = 3. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√11)²', '√11', '121', '11', '2√11', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√11)² = 11. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (√5)²', '√5', '2√5', '5', '25', 2,
'lc_hl_algebra', 3, 'foundation', 'lc_hl', '(√5)² = 5. Square root squared gives the original number ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 1/√5', '1/√5', '√5/1', '5', '1√5/5', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '1/√5 = 1/√5 × √5/√5 = 1√5/5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 2/√5', '2/√5', '√5/2', '2√5/5', '10', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '2/√5 = 2/√5 × √5/√5 = 2√5/5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 3/√3', '√3', '√3/3', '3/√3', '9', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '3/√3 = 3/√3 × √3/√3 = 3√3/3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 4/√5', '4√5/5', '√5/4', '20', '4/√5', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '4/√5 = 4/√5 × √5/√5 = 4√5/5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 1/√7', '1√7/7', '1/√7', '√7/1', '7', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '1/√7 = 1/√7 × √7/√7 = 1√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 4/√7', '√7/4', '28', '4√7/7', '4/√7', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '4/√7 = 4/√7 × √7/√7 = 4√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 3/√5', '3/√5', '√5/3', '3√5/5', '15', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '3/√5 = 3/√5 × √5/√5 = 3√5/5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 5/√7', '5√7/7', '√7/5', '35', '5/√7', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '5/√7 = 5/√7 × √7/√7 = 5√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 5/√3', '√3/5', '15', '5/√3', '5√3/3', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '5/√3 = 5/√3 × √3/√3 = 5√3/3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 4/√7', '√7/4', '28', '4/√7', '4√7/7', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '4/√7 = 4/√7 × √7/√7 = 4√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 2/√7', '√7/2', '2/√7', '14', '2√7/7', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '2/√7 = 2/√7 × √7/√7 = 2√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 1/√7', '7', '√7/1', '1/√7', '1√7/7', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '1/√7 = 1/√7 × √7/√7 = 1√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 3/√3', '3/√3', '9', '√3', '√3/3', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '3/√3 = 3/√3 × √3/√3 = 3√3/3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 4/√7', '4/√7', '√7/4', '28', '4√7/7', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '4/√7 = 4/√7 × √7/√7 = 4√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 5/√3', '5/√3', '√3/5', '5√3/3', '15', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '5/√3 = 5/√3 × √3/√3 = 5√3/3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 4/√5', '20', '4√5/5', '√5/4', '4/√5', 1,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '4/√5 = 4/√5 × √5/√5 = 4√5/5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 4/√2', '8', '√2/4', '4/√2', '4√2/2', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '4/√2 = 4/√2 × √2/√2 = 4√2/2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 2/√3', '2√3/3', '2/√3', '6', '√3/2', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '2/√3 = 2/√3 × √3/√3 = 2√3/3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 3/√7', '21', '√7/3', '3√7/7', '3/√7', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '3/√7 = 3/√7 × √7/√7 = 3√7/7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise the denominator: 2/√5', '√5/2', '2/√5', '10', '2√5/5', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', '2/√5 = 2/√5 × √5/√5 = 2√5/5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(1 + √3)', '(1 + √3)/2', '1/(1 - √3)', '-(1 - √3)/2', '1 - √3', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (1 - √3)/(1 - √3). Denominator: 1² - (√3)² = 1 - 3 = -2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(1 + √3)', '-(1 - √3)/2', '(1 + √3)/2', '1/(1 - √3)', '1 - √3', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (1 - √3)/(1 - √3). Denominator: 1² - (√3)² = 1 - 3 = -2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(3 + √3)', '(3 + √3)/6', '(3 - √3)/6', '3 - √3', '1/(3 - √3)', 1,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (3 - √3)/(3 - √3). Denominator: 3² - (√3)² = 9 - 3 = 6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(1 + √3)', '-(1 - √3)/2', '1 - √3', '(1 + √3)/2', '1/(1 - √3)', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (1 - √3)/(1 - √3). Denominator: 1² - (√3)² = 1 - 3 = -2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(3 + √2)', '(3 - √2)/7', '1/(3 - √2)', '(3 + √2)/7', '3 - √2', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (3 - √2)/(3 - √2). Denominator: 3² - (√2)² = 9 - 2 = 7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(3 + √5)', '3 - √5', '(3 - √5)/4', '1/(3 - √5)', '(3 + √5)/4', 1,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (3 - √5)/(3 - √5). Denominator: 3² - (√5)² = 9 - 5 = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(2 + √2)', '1/(2 - √2)', '2 - √2', '(2 - √2)/2', '(2 + √2)/2', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (2 - √2)/(2 - √2). Denominator: 2² - (√2)² = 4 - 2 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(1 + √2)', '(1 + √2)/1', '1 - √2', '-(1 - √2)/1', '1/(1 - √2)', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (1 - √2)/(1 - √2). Denominator: 1² - (√2)² = 1 - 2 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(2 + √3)', '2 - √3', '1/(2 - √3)', '(2 + √3)/1', '(2 - √3)/1', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (2 - √3)/(2 - √3). Denominator: 2² - (√3)² = 4 - 3 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(1 + √2)', '1/(1 - √2)', '(1 + √2)/1', '-(1 - √2)/1', '1 - √2', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (1 - √2)/(1 - √2). Denominator: 1² - (√2)² = 1 - 2 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(3 + √2)', '1/(3 - √2)', '(3 + √2)/7', '(3 - √2)/7', '3 - √2', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (3 - √2)/(3 - √2). Denominator: 3² - (√2)² = 9 - 2 = 7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(3 + √5)', '3 - √5', '(3 + √5)/4', '(3 - √5)/4', '1/(3 - √5)', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (3 - √5)/(3 - √5). Denominator: 3² - (√5)² = 9 - 5 = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(2 + √5)', '1/(2 - √5)', '2 - √5', '-(2 - √5)/1', '(2 + √5)/1', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (2 - √5)/(2 - √5). Denominator: 2² - (√5)² = 4 - 5 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(2 + √3)', '(2 + √3)/1', '2 - √3', '(2 - √3)/1', '1/(2 - √3)', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (2 - √3)/(2 - √3). Denominator: 2² - (√3)² = 4 - 3 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise: 1/(2 + √2)', '(2 - √2)/2', '(2 + √2)/2', '1/(2 - √2)', '2 - √2', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Multiply by conjugate (2 - √2)/(2 - √2). Denominator: 2² - (√2)² = 4 - 2 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To rationalise a/√b, multiply by...', '1/√b', 'b/b', 'a/a', '√b/√b', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: √b/√b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of (a + √b) is...', '(a + √b)', '(√b - a)', '(-a + √b)', '(a - √b)', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: (a - √b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of (a + √b) is...', '(√b - a)', '(-a + √b)', '(a - √b)', '(a + √b)', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: (a - √b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of (a + √b) is...', '(a - √b)', '(a + √b)', '(-a + √b)', '(√b - a)', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: (a - √b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(a + √b)(a - √b) equals...', 'a² + b', 'a² - 2√b', '2a', 'a² - b', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: a² - b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of (a + √b) is...', '(-a + √b)', '(√b - a)', '(a - √b)', '(a + √b)', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: (a - √b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To rationalise a/√b, multiply by...', 'b/b', '√b/√b', '1/√b', 'a/a', 1,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: √b/√b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To rationalise a/√b, multiply by...', 'b/b', '√b/√b', '1/√b', 'a/a', 1,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: √b/√b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of (a + √b) is...', '(-a + √b)', '(a - √b)', '(a + √b)', '(√b - a)', 1,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: (a - √b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(a + √b)(a - √b) equals...', 'a² + b', 'a² - 2√b', 'a² - b', '2a', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: a² - b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of (a + √b) is...', '(a + √b)', '(a - √b)', '(-a + √b)', '(√b - a)', 1,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: (a - √b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To rationalise a/√b, multiply by...', '1/√b', 'a/a', 'b/b', '√b/√b', 3,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: √b/√b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To rationalise a/√b, multiply by...', 'b/b', '1/√b', '√b/√b', 'a/a', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: √b/√b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The conjugate of (a + √b) is...', '(a - √b)', '(-a + √b)', '(√b - a)', '(a + √b)', 0,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: (a - √b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To rationalise a/√b, multiply by...', 'a/a', 'b/b', '√b/√b', '1/√b', 2,
'lc_hl_algebra', 4, 'developing', 'lc_hl', 'Rationalising principle: √b/√b ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(3125)', 'Option 4', '6', '3125', '5', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(3125) = 5 because 5^5 = 3125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(125)', '3', '5', '4', '125', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(125) = 3 because 5^3 = 125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(32)', '6', '5', '32', '2', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(32) = 5 because 2^5 = 32 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(2)', '1', 'Option 4', 'Option 3', '2', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(2) = 1 because 2^1 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(125)', '4', '125', '3', '5', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(125) = 3 because 5^3 = 125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(2)', '2', 'Option 3', '1', 'Option 4', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(2) = 1 because 2^1 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(2)', 'Option 3', '1', '2', 'Option 4', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(2) = 1 because 2^1 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(125)', '3', '4', '125', '5', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(125) = 3 because 5^3 = 125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_3(81)', '4', '3', '81', '5', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_3(81) = 4 because 3^4 = 81 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_3(3)', '3', 'Option 4', '2', '1', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_3(3) = 1 because 3^1 = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_3(9)', 'Option 4', '9', '3', '2', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_3(9) = 2 because 3^2 = 9 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(10)', '2', 'Option 4', '10', '1', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(10) = 1 because 10^1 = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(2)', 'Option 4', 'Option 3', '1', '2', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(2) = 1 because 2^1 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(1000)', '1000', '10', '3', '4', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(1000) = 3 because 10^3 = 1000 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(32)', '2', '5', '32', '6', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(32) = 5 because 2^5 = 32 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(3125)', '3125', '5', 'Option 4', '6', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(3125) = 5 because 5^5 = 3125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(8)', '3', '2', '8', '4', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(8) = 3 because 2^3 = 8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(100000)', '100000', '6', '5', '10', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(100000) = 5 because 10^5 = 100000 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(1000)', '10', '3', '4', '1000', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(1000) = 3 because 10^3 = 1000 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(4)', '3', 'Option 4', '4', '2', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(4) = 2 because 2^2 = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(1)', '1', '2', '-1', '0', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(1) = 0 because 2^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate ln(1)', 'e', '0', '1', '-1', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'ln(1) = 0 because e^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate ln(1)', '0', '1', '-1', 'e', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'ln(1) = 0 because e^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(1)', '1', '-1', '2', '0', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(1) = 0 because 2^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_3(1)', '3', '1', '0', '-1', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_3(1) = 0 because 3^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(1)', '-1', '0', '1', '2', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(1) = 0 because 2^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(1)', '5', '0', '-1', '1', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(1) = 0 because 5^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(1)', '-1', '5', '0', '1', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(1) = 0 because 5^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(1)', '1', '0', '-1', '2', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(1) = 0 because 2^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_3(1)', '3', '-1', '1', '0', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_3(1) = 0 because 3^0 = 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(2)', '1', 'Option 4', '0', '2', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(2) = 1 because 2^1 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(2)', '1', '0', 'Option 4', '2', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(2) = 1 because 2^1 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(10)', '0', '9', '10', '1', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(10) = 1 because 10^1 = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(5)', '4', '5', '1', '0', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(5) = 1 because 5^1 = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(10)', '0', '9', '10', '1', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(10) = 1 because 10^1 = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(10)', '1', '10', '9', '0', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(10) = 1 because 10^1 = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(10)', '10', '9', '1', '0', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(10) = 1 because 10^1 = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_5(5)', '1', '0', '4', '5', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_5(5) = 1 because 5^1 = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log(10)', '1', '9', '0', '10', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log(10) = 1 because 10^1 = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate log_2(2)', '2', '1', '0', 'Option 4', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_2(2) = 1 because 2^1 = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write 3^2 = 9 in logarithmic form', 'log_2(9) = 3', 'log_3(2) = 9', 'log_9(3) = 2', 'log_3(9) = 2', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: log_3(9) = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write log_2(16) = 4 in exponential form', '2^4 = 16', '16^4 = 2', '4^2 = 16', '2^16 = 4', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: 2^4 = 16 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write 2^3 = 8 in logarithmic form', 'log_8(2) = 3', 'log_2(3) = 8', 'log_2(8) = 3', 'log_3(8) = 2', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: log_2(8) = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write log_5(125) = 3 in exponential form', '125^3 = 5', '5^3 = 125', '3^5 = 125', '5^125 = 3', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: 5^3 = 125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write log_5(125) = 3 in exponential form', '5^125 = 3', '125^3 = 5', '3^5 = 125', '5^3 = 125', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: 5^3 = 125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write log_2(16) = 4 in exponential form', '2^4 = 16', '2^16 = 4', '4^2 = 16', '16^4 = 2', 0,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: 2^4 = 16 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write log_5(25) = 2 in exponential form', '5^25 = 2', '25^2 = 5', '5^2 = 25', '2^5 = 25', 2,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: 5^2 = 25 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write log_5(25) = 2 in exponential form', '5^25 = 2', '5^2 = 25', '2^5 = 25', '25^2 = 5', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: 5^2 = 25 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write 2^3 = 8 in logarithmic form', 'log_2(3) = 8', 'log_8(2) = 3', 'log_3(8) = 2', 'log_2(8) = 3', 3,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: log_2(8) = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Write log_2(4) = 2 in exponential form', '2^4 = 2', '2^2 = 4', 'Option 4', '4^2 = 2', 1,
'lc_hl_algebra', 5, 'developing', 'lc_hl', 'log_a(b) = c ⟺ a^c = b. Answer: 2^2 = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(10) as a sum of logarithms', 'log(5) × log(2)', 'log(5) + log(2)', 'log(7)', 'log(5) - log(2)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(10) = log(5) + log(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(21) as a sum of logarithms', 'log(3) × log(7)', 'log(10)', 'log(3) + log(7)', 'log(3) - log(7)', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(21) = log(3) + log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(6) as a sum of logarithms', 'log(3) × log(2)', 'log(3) - log(2)', 'log(5)', 'log(3) + log(2)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(6) = log(3) + log(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(4) as a sum of logarithms', 'log(4)', 'log(2) - log(2)', 'log(2) + log(2)', 'log(2) × log(2)', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(4) = log(2) + log(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(8) as a sum of logarithms', 'log(2) + log(4)', 'log(2) - log(4)', 'log(6)', 'log(2) × log(4)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(8) = log(2) + log(4) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(15) as a sum of logarithms', 'log(3) - log(5)', 'log(3) + log(5)', 'log(8)', 'log(3) × log(5)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(15) = log(3) + log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(15) as a sum of logarithms', 'log(3) + log(5)', 'log(3) × log(5)', 'log(3) - log(5)', 'log(8)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(15) = log(3) + log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(15) as a sum of logarithms', 'log(8)', 'log(3) - log(5)', 'log(3) × log(5)', 'log(3) + log(5)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(15) = log(3) + log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(21) as a sum of logarithms', 'log(3) - log(7)', 'log(3) + log(7)', 'log(3) × log(7)', 'log(10)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(21) = log(3) + log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(6) as a sum of logarithms', 'log(5)', 'log(3) × log(2)', 'log(3) - log(2)', 'log(3) + log(2)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(6) = log(3) + log(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(21) as a sum of logarithms', 'log(3) + log(7)', 'log(3) - log(7)', 'log(10)', 'log(3) × log(7)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(21) = log(3) + log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(21) as a sum of logarithms', 'log(3) + log(7)', 'log(10)', 'log(3) - log(7)', 'log(3) × log(7)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(21) = log(3) + log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(14) as a sum of logarithms', 'log(2) + log(7)', 'log(2) × log(7)', 'log(2) - log(7)', 'log(9)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(14) = log(2) + log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(21) as a sum of logarithms', 'log(3) - log(7)', 'log(3) + log(7)', 'log(10)', 'log(3) × log(7)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(21) = log(3) + log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(21) as a sum of logarithms', 'log(3) × log(7)', 'log(3) + log(7)', 'log(3) - log(7)', 'log(10)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Product rule: log(ab) = log(a) + log(b). log(21) = log(3) + log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(6/5) as a difference of logarithms', 'log(6) × log(5)', 'log(6) - log(5)', 'log(6)/log(5)', 'log(6) + log(5)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(6/5) as a difference of logarithms', 'log(6) + log(5)', 'log(6) - log(5)', 'log(6)/log(5)', 'log(6) × log(5)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(15/2) as a difference of logarithms', 'log(15) - log(2)', 'log(15) × log(2)', 'log(15)/log(2)', 'log(15) + log(2)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(8/5) as a difference of logarithms', 'log(8)/log(5)', 'log(8) × log(5)', 'log(8) + log(5)', 'log(8) - log(5)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(15/2) as a difference of logarithms', 'log(15) - log(2)', 'log(15) + log(2)', 'log(15) × log(2)', 'log(15)/log(2)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(15/3) as a difference of logarithms', 'log(15) - log(3)', 'log(15)/log(3)', 'log(15) + log(3)', 'log(15) × log(3)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(10/2) as a difference of logarithms', 'log(10) + log(2)', 'log(10) - log(2)', 'log(10)/log(2)', 'log(10) × log(2)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(6/3) as a difference of logarithms', 'log(6) - log(3)', 'log(6) + log(3)', 'log(6) × log(3)', 'log(6)/log(3)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(8/2) as a difference of logarithms', 'log(8) + log(2)', 'log(8) - log(2)', 'log(8)/log(2)', 'log(8) × log(2)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(6/5) as a difference of logarithms', 'log(6)/log(5)', 'log(6) - log(5)', 'log(6) × log(5)', 'log(6) + log(5)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Quotient rule: log(a/b) = log(a) - log(b) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(7^4)', '4log(7)', 'log(7)^4', 'log(7^4)', 'log(28)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(7^4) = 4log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(5^2)', '2log(5)', 'log(5)^2', 'log(5^2)', 'log(10)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(5^2) = 2log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(7^2)', 'log(7^2)', 'log(14)', '2log(7)', 'log(7)^2', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(7^2) = 2log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(5^3)', 'log(15)', 'log(5^3)', 'log(5)^3', '3log(5)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(5^3) = 3log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(3^4)', '4log(3)', 'log(3)^4', 'log(12)', 'log(3^4)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(3^4) = 4log(3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(7^2)', '2log(7)', 'log(7^2)', 'log(7)^2', 'log(14)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(7^2) = 2log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(5^5)', 'log(5)^5', 'log(25)', '5log(5)', 'log(5^5)', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(5^5) = 5log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(3^5)', 'log(3^5)', 'log(3)^5', 'log(15)', '5log(3)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(3^5) = 5log(3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(5^2)', 'log(10)', 'log(5^2)', 'log(5)^2', '2log(5)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(5^2) = 2log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(5^3)', 'log(5)^3', '3log(5)', 'log(15)', 'log(5^3)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(5^3) = 3log(5) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(7^5)', 'log(7^5)', '5log(7)', 'log(35)', 'log(7)^5', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(7^5) = 5log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(2^2)', 'log(2)^2', 'log(4)', '2log(2)', 'log(2^2)', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(2^2) = 2log(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(7^2)', 'log(14)', 'log(7^2)', 'log(7)^2', '2log(7)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(7^2) = 2log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(3^5)', 'log(3)^5', 'log(15)', '5log(3)', 'log(3^5)', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(3^5) = 5log(3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(7^5)', '5log(7)', 'log(7^5)', 'log(35)', 'log(7)^5', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'Power rule: log(a^n) = n·log(a). log(7^5) = 5log(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(4) + log(5) to a single logarithm', 'log(4) × log(5)', 'log(9)', 'log(20)', 'log(40)', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(4) + log(5) = log(4 × 5) = log(20) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(3) + log(7) to a single logarithm', 'log(42)', 'log(21)', 'log(3) × log(7)', 'log(10)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(3) + log(7) = log(3 × 7) = log(21) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(3) + log(6) to a single logarithm', 'log(36)', 'log(18)', 'log(3) × log(6)', 'log(9)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(3) + log(6) = log(3 × 6) = log(18) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(4) + log(5) to a single logarithm', 'log(40)', 'log(4) × log(5)', 'log(9)', 'log(20)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(4) + log(5) = log(4 × 5) = log(20) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(3) + log(5) to a single logarithm', 'log(8)', 'log(15)', 'log(3) × log(5)', 'log(30)', 1,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(3) + log(5) = log(3 × 5) = log(15) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(2) + log(7) to a single logarithm', 'log(14)', 'log(28)', 'log(9)', 'log(2) × log(7)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(2) + log(7) = log(2 × 7) = log(14) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(2) + log(7) to a single logarithm', 'log(9)', 'log(28)', 'log(2) × log(7)', 'log(14)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(2) + log(7) = log(2 × 7) = log(14) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(4) + log(6) to a single logarithm', 'log(4) × log(6)', 'log(48)', 'log(24)', 'log(10)', 2,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(4) + log(6) = log(4 × 6) = log(24) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(3) + log(7) to a single logarithm', 'log(21)', 'log(3) × log(7)', 'log(42)', 'log(10)', 0,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(3) + log(7) = log(3 × 7) = log(21) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify log(4) + log(6) to a single logarithm', 'log(10)', 'log(48)', 'log(4) × log(6)', 'log(24)', 3,
'lc_hl_algebra', 6, 'developing', 'lc_hl', 'log(4) + log(6) = log(4 × 6) = log(24) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 5^x = 125', '4', '3', '15', '5', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 5^x = 5^3, then x = 3 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 81', '3', '12', '4', '5', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 3^x = 3^4, then x = 4 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 64', '6', '2', '12', '7', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 2^x = 2^6, then x = 6 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 5^x = 625', 'Option 4', '4', '5', '20', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 5^x = 5^4, then x = 4 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 9', '2', 'Option 4', '6', '3', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 3^x = 3^2, then x = 2 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 32', '2', '10', '6', '5', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 2^x = 2^5, then x = 5 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 16', '4', '5', '2', '8', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 2^x = 2^4, then x = 4 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 9', '3', 'Option 4', '2', '6', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 3^x = 3^2, then x = 2 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 8', '3', '6', '2', '4', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 2^x = 2^3, then x = 3 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 32', '2', '5', '10', '6', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 2^x = 2^5, then x = 5 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 5^x = 625', 'Option 4', '5', '4', '20', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 5^x = 5^4, then x = 4 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 5^x = 15625', '5', '7', '30', '6', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 5^x = 5^6, then x = 6 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 32', '10', '2', '5', '6', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 2^x = 2^5, then x = 5 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 32', '6', '2', '10', '5', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 2^x = 2^5, then x = 5 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 5^x = 15625', '7', '30', '6', '5', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If 5^x = 5^6, then x = 6 (equal bases means equal exponents) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 3^2 × 3^1', '3', 'Option 4', '2', '1', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '3^x = 3^2 × 3^1 = 3^3 = 3^3. So x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 2^3 × 2^1', '4', '3', 'Option 4', '1', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '2^x = 2^3 × 2^1 = 2^4 = 2^4. So x = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 2^4 × 2^1', 'Option 4', '1', '4', '5', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '2^x = 2^4 × 2^1 = 2^5 = 2^5. So x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 2^3 × 2^3', '9', '6', '3', 'Option 4', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '2^x = 2^3 × 2^3 = 2^6 = 2^6. So x = 6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 3^2 × 3^2', '4', '2', 'Option 3', 'Option 4', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '3^x = 3^2 × 3^2 = 3^4 = 3^4. So x = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 3^3 × 3^3', '9', '6', '3', 'Option 4', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '3^x = 3^3 × 3^3 = 3^6 = 3^6. So x = 6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 2^4 × 2^2', '2', '4', '6', '8', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '2^x = 2^4 × 2^2 = 2^6 = 2^6. So x = 6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^x = 2^2 × 2^3', '2', '3', '6', '5', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '2^x = 2^2 × 2^3 = 2^5 = 2^5. So x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 3^4 × 3^1', '5', 'Option 4', '4', '1', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '3^x = 3^4 × 3^1 = 3^5 = 3^5. So x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^x = 3^2 × 3^3', '6', '5', '3', '2', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '3^x = 3^2 × 3^3 = 3^5 = 3^5. So x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^6', '3', '4', '12', '6', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^6. Since 4 = 2², we have (2²)^x = 2^6, so 2x = 6, x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^10', '5', '6', '10', '20', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^10. Since 4 = 2², we have (2²)^x = 2^10, so 2x = 10, x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^10', '10', '20', '6', '5', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^10. Since 4 = 2², we have (2²)^x = 2^10, so 2x = 10, x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^4', '4', '3', '2', '8', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^4. Since 4 = 2², we have (2²)^x = 2^4, so 2x = 4, x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^8', '8', '5', '4', '16', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^8. Since 4 = 2², we have (2²)^x = 2^8, so 2x = 8, x = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^4', '4', '8', '3', '2', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^4. Since 4 = 2², we have (2²)^x = 2^4, so 2x = 4, x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^6', '12', '3', '4', '6', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^6. Since 4 = 2², we have (2²)^x = 2^6, so 2x = 6, x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^4', '3', '8', '4', '2', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^4. Since 4 = 2², we have (2²)^x = 2^4, so 2x = 4, x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^10', '5', '20', '10', '6', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^10. Since 4 = 2², we have (2²)^x = 2^10, so 2x = 10, x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^6', '6', '4', '3', '12', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^6. Since 4 = 2², we have (2²)^x = 2^6, so 2x = 6, x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^4', '8', '2', '3', '4', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^4. Since 4 = 2², we have (2²)^x = 2^4, so 2x = 4, x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^4', '3', '2', '8', '4', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^4. Since 4 = 2², we have (2²)^x = 2^4, so 2x = 4, x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^6', '3', '6', '12', '4', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^6. Since 4 = 2², we have (2²)^x = 2^6, so 2x = 6, x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^4', '2', '4', '3', '8', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^4. Since 4 = 2², we have (2²)^x = 2^4, so 2x = 4, x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^8', '8', '16', '5', '4', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', '4^x = 2^8. Since 4 = 2², we have (2²)^x = 2^8, so 2x = 8, x = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^2', '3', 'e^2', 'ln(2)', '2', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^2, then x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^5', 'ln(5)', 'e^5', '6', '5', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^5, then x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^2', 'ln(2)', '2', '3', 'e^2', 1,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^2, then x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^3', '4', 'ln(3)', 'e^3', '3', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^3, then x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^4', '5', 'e^4', '4', 'ln(4)', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^4, then x = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^5', 'ln(5)', '6', 'e^5', '5', 3,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^5, then x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^2', 'ln(2)', '3', '2', 'e^2', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^2, then x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^5', '5', 'ln(5)', 'e^5', '6', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^5, then x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^3', '3', '4', 'e^3', 'ln(3)', 0,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^3, then x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve e^x = e^5', 'ln(5)', '6', '5', 'e^5', 2,
'lc_hl_algebra', 7, 'proficient', 'lc_hl', 'If e^x = e^5, then x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_5(x) = 4', '9', '4', '20', '625', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_5(x) = 4 means 5^4 = x, so x = 625 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_2(x) = 4', '8', '4', '16', '6', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_2(x) = 4 means 2^4 = x, so x = 16 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) = 2', '12', '100', '20', '2', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) = 2 means 10^2 = x, so x = 100 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_3(x) = 3', '6', '9', '3', '27', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_3(x) = 3 means 3^3 = x, so x = 27 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) = 1', '1', '11', '10', 'Option 4', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) = 1 means 10^1 = x, so x = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_5(x) = 3', '3', '125', '8', '15', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_5(x) = 3 means 5^3 = x, so x = 125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) = 3', '1000', '13', '3', '30', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) = 3 means 10^3 = x, so x = 1000 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_3(x) = 1', '3', '1', 'Option 4', '4', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_3(x) = 1 means 3^1 = x, so x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_3(x) = 4', '4', '81', '12', '7', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_3(x) = 4 means 3^4 = x, so x = 81 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) = 2', '12', '2', '100', '20', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) = 2 means 10^2 = x, so x = 100 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_5(x) = 2', '2', '25', '7', '10', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_5(x) = 2 means 5^2 = x, so x = 25 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) = 1', '11', 'Option 4', '10', '1', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) = 1 means 10^1 = x, so x = 10 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_2(x) = 3', '5', '3', '6', '8', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_2(x) = 3 means 2^3 = x, so x = 8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_5(x) = 1', '5', '6', '1', 'Option 4', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_5(x) = 1 means 5^1 = x, so x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_5(x) = 1', '1', 'Option 4', '5', '6', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_5(x) = 1 means 5^1 = x, so x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_5(x) = 2', '25', '10', '7', '2', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_5(x) = 2 means 5^2 = x, so x = 25 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_2(x) = 2', 'Option 4', '2', 'Option 3', '4', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_2(x) = 2 means 2^2 = x, so x = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_3(x) = 1', '1', '3', 'Option 4', '4', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_3(x) = 1 means 3^1 = x, so x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) = 2', '20', '12', '2', '100', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) = 2 means 10^2 = x, so x = 100 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log_3(x) = 2', '5', '2', '6', '9', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log_3(x) = 2 means 3^2 = x, so x = 9 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(4) = log(16)', '12', '16', '4', '20', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(4) = log(16) → log(4x) = log(16) → 4x = 16 → x = 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(2) = log(6)', '3', '4', '8', '6', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(2) = log(6) → log(2x) = log(6) → 2x = 6 → x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(5) = log(15)', '3', '10', '15', '20', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(5) = log(15) → log(5x) = log(15) → 5x = 15 → x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(4) = log(8)', '12', '4', '8', '2', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(4) = log(8) → log(4x) = log(8) → 4x = 8 → x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(5) = log(25)', '20', '25', '30', '5', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(5) = log(25) → log(5x) = log(25) → 5x = 25 → x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(4) = log(12)', '3', '8', '12', '16', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(4) = log(12) → log(4x) = log(12) → 4x = 12 → x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(3) = log(6)', '3', '6', '9', '2', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(3) = log(6) → log(3x) = log(6) → 3x = 6 → x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(5) = log(25)', '20', '5', '25', '30', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(5) = log(25) → log(5x) = log(25) → 5x = 25 → x = 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(4) = log(12)', '3', '12', '16', '8', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(4) = log(12) → log(4x) = log(12) → 4x = 12 → x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(4) = log(12)', '3', '8', '12', '16', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(4) = log(12) → log(4x) = log(12) → 4x = 12 → x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(3) = log(6)', '9', '6', '3', '2', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(3) = log(6) → log(3x) = log(6) → 3x = 6 → x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(5) = log(10)', '10', '2', '15', '5', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(5) = log(10) → log(5x) = log(10) → 5x = 10 → x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(3) = log(6)', '2', '9', '3', '6', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(3) = log(6) → log(3x) = log(6) → 3x = 6 → x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(3) = log(6)', '2', '3', '9', '6', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(3) = log(6) → log(3x) = log(6) → 3x = 6 → x = 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log(x) + log(3) = log(9)', '3', '12', '9', '6', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'log(x) + log(3) = log(9) → log(3x) = log(9) → 3x = 9 → x = 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 3', 'e^3', '3e', 'ln(3)', '3', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 3 means x = e^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 4', '4e', 'e^4', '4', 'ln(4)', 1,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 4 means x = e^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 4', 'e^4', 'ln(4)', '4e', '4', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 4 means x = e^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 2', '2', 'ln(2)', 'e^2', '2e', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 2 means x = e^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 4', 'ln(4)', '4e', 'e^4', '4', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 4 means x = e^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 4', 'ln(4)', '4e', 'e^4', '4', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 4 means x = e^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 3', 'e^3', '3e', '3', 'ln(3)', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 3 means x = e^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 3', 'e^3', '3', '3e', 'ln(3)', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 3 means x = e^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 2', '2e', '2', 'ln(2)', 'e^2', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 2 means x = e^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 3', '3', 'ln(3)', 'e^3', '3e', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 3 means x = e^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 4', '4', 'ln(4)', 'e^4', '4e', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 4 means x = e^4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 2', 'ln(2)', '2e', 'e^2', '2', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 2 means x = e^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 3', '3e', '3', 'e^3', 'ln(3)', 2,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 3 means x = e^3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 2', 'e^2', '2', '2e', 'ln(2)', 0,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 2 means x = e^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve ln(x) = 2', '2', 'ln(2)', '2e', 'e^2', 3,
'lc_hl_algebra', 8, 'proficient', 'lc_hl', 'ln(x) = 2 means x = e^2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 6x + 9) by (x + 3)', 'x + 3', 'x - 3', 'Option 4', 'x + 6', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 6x + 9) ÷ (x + 3) = x + 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 5x + 4) by (x + 1)', 'x - 4', 'x + 1', 'x + 4', 'x + 5', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 5x + 4) ÷ (x + 1) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 5x + 4) by (x + 1)', 'x + 4', 'x + 5', 'x - 4', 'x + 1', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 5x + 4) ÷ (x + 1) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 6x + 9) by (x + 3)', 'x - 3', 'Option 4', 'x + 3', 'x + 6', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 6x + 9) ÷ (x + 3) = x + 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 4x + 3) by (x + 1)', 'x + 4', 'x + 3', 'x - 3', 'x + 1', 1,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 4x + 3) ÷ (x + 1) = x + 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 6x + 8) by (x + 2)', 'x + 2', 'x + 4', 'x - 4', 'x + 6', 1,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 6x + 8) ÷ (x + 2) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 3x + 2) by (x + 1)', 'x + 3', 'x + 1', 'x + 2', 'x - 2', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 3x + 2) ÷ (x + 1) = x + 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 3x + 2) by (x + 2)', 'x + 1', 'x + 2', 'x - 1', 'x + 3', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 3x + 2) ÷ (x + 2) = x + 1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 6x + 8) by (x + 2)', 'x - 4', 'x + 2', 'x + 6', 'x + 4', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 6x + 8) ÷ (x + 2) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 5x + 6) by (x + 3)', 'x + 3', 'x + 5', 'x + 2', 'x - 2', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 5x + 6) ÷ (x + 3) = x + 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 5x + 4) by (x + 1)', 'x + 4', 'x - 4', 'x + 1', 'x + 5', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 5x + 4) ÷ (x + 1) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 3x + 2) by (x + 1)', 'x + 1', 'x + 2', 'x - 2', 'x + 3', 1,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 3x + 2) ÷ (x + 1) = x + 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 5x + 6) by (x + 3)', 'x + 3', 'x - 2', 'x + 5', 'x + 2', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 5x + 6) ÷ (x + 3) = x + 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 6x + 9) by (x + 3)', 'Option 4', 'x + 6', 'x + 3', 'x - 3', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 6x + 9) ÷ (x + 3) = x + 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 7x + 12) by (x + 3)', 'x - 4', 'x + 4', 'x + 7', 'x + 3', 1,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 7x + 12) ÷ (x + 3) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 5x + 4) by (x + 1)', 'x - 4', 'x + 4', 'x + 5', 'x + 1', 1,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 5x + 4) ÷ (x + 1) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 5x + 6) by (x + 3)', 'x + 3', 'x + 5', 'x + 2', 'x - 2', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 5x + 6) ÷ (x + 3) = x + 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 4x + 3) by (x + 1)', 'x + 3', 'x - 3', 'x + 1', 'x + 4', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 4x + 3) ÷ (x + 1) = x + 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 7x + 12) by (x + 3)', 'x + 3', 'x + 7', 'x + 4', 'x - 4', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 7x + 12) ÷ (x + 3) = x + 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Divide (x² + 6x + 9) by (x + 3)', 'x - 3', 'Option 4', 'x + 6', 'x + 3', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', '(x² + 6x + 9) ÷ (x + 3) = x + 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When dividing f(x) by (x - 2), the remainder equals', 'f(2)', 'f(-2)', 'f(x)', 'f(0)', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: f(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) ÷ (x - 3) has remainder 0, then x = 3 is a', 'coefficient', 'factor', 'root', 'quotient', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: root ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) ÷ (x - 3) has remainder 0, then x = 3 is a', 'quotient', 'factor', 'root', 'coefficient', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: root ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) ÷ (x - 3) has remainder 0, then x = 3 is a', 'coefficient', 'factor', 'quotient', 'root', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: root ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When dividing f(x) by (x - 2), the remainder equals', 'f(0)', 'f(2)', 'f(-2)', 'f(x)', 1,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: f(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) ÷ (x - 3) has remainder 0, then x = 3 is a', 'factor', 'quotient', 'root', 'coefficient', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: root ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) ÷ (x - 3) has remainder 0, then x = 3 is a', 'root', 'coefficient', 'quotient', 'factor', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: root ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When dividing f(x) by (x - 2), the remainder equals', 'f(0)', 'f(-2)', 'f(2)', 'f(x)', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: f(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (x - a) is a factor of f(x), then f(a) = ', '0', '-a', 'a', '1', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When dividing f(x) by (x - 2), the remainder equals', 'f(x)', 'f(2)', 'f(0)', 'f(-2)', 1,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: f(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When dividing f(x) by (x - 2), the remainder equals', 'f(2)', 'f(-2)', 'f(0)', 'f(x)', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: f(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When dividing f(x) by (x - 2), the remainder equals', 'f(2)', 'f(0)', 'f(-2)', 'f(x)', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: f(2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (x - a) is a factor of f(x), then f(a) = ', '0', '-a', '1', 'a', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (x - a) is a factor of f(x), then f(a) = ', 'a', '1', '0', '-a', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (x - a) is a factor of f(x), then f(a) = ', 'a', '1', '0', '-a', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder theorem: 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 3x + 1 is divided by (x - 3)', '3', '22', '19', '4', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 3(3) + 1 = 9 + 9 + 1 = 19 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 2x + 3 is divided by (x - 2)', '2', '13', '11', '5', 2,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(2) = 2² + 2(2) + 3 = 4 + 4 + 3 = 11 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 2x + 2 is divided by (x - 3)', '3', '4', '20', '17', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 2(3) + 2 = 9 + 6 + 2 = 17 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 1x + 4 is divided by (x - 3)', '5', '3', '19', '16', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 1(3) + 4 = 9 + 3 + 4 = 16 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 3x + 2 is divided by (x - 3)', '5', '3', '23', '20', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 3(3) + 2 = 9 + 9 + 2 = 20 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 3x + 1 is divided by (x - 3)', '19', '3', '4', '22', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 3(3) + 1 = 9 + 9 + 1 = 19 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 1x + 3 is divided by (x - 2)', '9', '4', '11', '2', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(2) = 2² + 1(2) + 3 = 4 + 2 + 3 = 9 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 1x + 4 is divided by (x - 1)', '5', '7', '1', '6', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(1) = 1² + 1(1) + 4 = 1 + 1 + 4 = 6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 3x + 4 is divided by (x - 3)', '25', '7', '3', '22', 3,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 3(3) + 4 = 9 + 9 + 4 = 22 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 1x + 5 is divided by (x - 3)', '17', '3', '6', '20', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 1(3) + 5 = 9 + 3 + 5 = 17 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 4x + 4 is divided by (x - 2)', '16', '18', '8', '2', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(2) = 2² + 4(2) + 4 = 4 + 8 + 4 = 16 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 2x + 3 is divided by (x - 3)', '18', '5', '21', '3', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 2(3) + 3 = 9 + 6 + 3 = 18 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 4x + 4 is divided by (x - 3)', '25', '8', '28', '3', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 4(3) + 4 = 9 + 12 + 4 = 25 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 1x + 1 is divided by (x - 2)', '7', '2', 'Option 4', '9', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(2) = 2² + 1(2) + 1 = 4 + 2 + 1 = 7 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the remainder when x² + 2x + 2 is divided by (x - 3)', '17', '20', '3', '4', 0,
'lc_hl_algebra', 9, 'proficient', 'lc_hl', 'Remainder = f(3) = 3² + 2(3) + 2 = 9 + 6 + 2 = 17 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 4) a factor of x² - 2x - 3?', 'Cannot determine', 'No', 'Only if x > 0', 'Yes', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(4) = 4² + -2(4) + (-3) = 5 ≠ 0, so (x - 4) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 3) a factor of x² - 1x - 6?', 'No', 'Only if x > 0', 'Cannot determine', 'Yes', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(3) = 3² + -1(3) + (-6) = 0, so (x - 3) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 3) a factor of x² + 0x - 4?', 'Cannot determine', 'Only if x > 0', 'No', 'Yes', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(3) = 3² + 0(3) + (-4) = 5 ≠ 0, so (x - 3) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 2) a factor of x² + 0x - 1?', 'No', 'Yes', 'Cannot determine', 'Only if x > 0', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(2) = 2² + 0(2) + (-1) = 3 ≠ 0, so (x - 2) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 3) a factor of x² - 2x - 3?', 'Cannot determine', 'No', 'Yes', 'Only if x > 0', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(3) = 3² + -2(3) + (-3) = 0, so (x - 3) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 2) a factor of x² + 2x - 3?', 'No', 'Only if x > 0', 'Cannot determine', 'Yes', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(2) = 2² + 2(2) + (-3) = 5 ≠ 0, so (x - 2) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 4) a factor of x² - 1x - 6?', 'No', 'Yes', 'Only if x > 0', 'Cannot determine', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(4) = 4² + -1(4) + (-6) = 6 ≠ 0, so (x - 4) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 3) a factor of x² + 0x - 4?', 'Yes', 'Cannot determine', 'No', 'Only if x > 0', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(3) = 3² + 0(3) + (-4) = 5 ≠ 0, so (x - 3) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 2) a factor of x² + 0x - 4?', 'Cannot determine', 'Only if x > 0', 'No', 'Yes', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(2) = 2² + 0(2) + (-4) = 0, so (x - 2) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 3) a factor of x² + 0x - 4?', 'No', 'Cannot determine', 'Only if x > 0', 'Yes', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(3) = 3² + 0(3) + (-4) = 5 ≠ 0, so (x - 3) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 1) a factor of x² + 1x - 2?', 'Cannot determine', 'Only if x > 0', 'No', 'Yes', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(1) = 1² + 1(1) + (-2) = 0, so (x - 1) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 2) a factor of x² - 1x - 2?', 'Only if x > 0', 'Cannot determine', 'No', 'Yes', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(2) = 2² + -1(2) + (-2) = 0, so (x - 2) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 3) a factor of x² + 0x - 9?', 'Only if x > 0', 'Yes', 'Cannot determine', 'No', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(3) = 3² + 0(3) + (-9) = 0, so (x - 3) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 4) a factor of x² - 1x - 6?', 'No', 'Yes', 'Only if x > 0', 'Cannot determine', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(4) = 4² + -1(4) + (-6) = 6 ≠ 0, so (x - 4) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 1) a factor of x² + 1x - 2?', 'Yes', 'No', 'Cannot determine', 'Only if x > 0', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(1) = 1² + 1(1) + (-2) = 0, so (x - 1) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 2) a factor of x² + 1x - 6?', 'Yes', 'Cannot determine', 'No', 'Only if x > 0', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(2) = 2² + 1(2) + (-6) = 0, so (x - 2) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 2) a factor of x² + 1x - 6?', 'Only if x > 0', 'Cannot determine', 'Yes', 'No', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(2) = 2² + 1(2) + (-6) = 0, so (x - 2) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 2) a factor of x² - 1x - 2?', 'Yes', 'No', 'Cannot determine', 'Only if x > 0', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(2) = 2² + -1(2) + (-2) = 0, so (x - 2) is a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 4) a factor of x² + 0x - 9?', 'Cannot determine', 'Yes', 'Only if x > 0', 'No', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(4) = 4² + 0(4) + (-9) = 7 ≠ 0, so (x - 4) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is (x - 4) a factor of x² + 0x - 9?', 'Yes', 'Only if x > 0', 'No', 'Cannot determine', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'f(4) = 4² + 0(4) + (-9) = 7 ≠ 0, so (x - 4) is not a factor ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 2) is a factor of x² + 1x + k', '6', '1', '2', '-6', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 2) to be a factor: f(2) = 0. 2² + 1(2) + k = 0. 4 + 2 + k = 0. k = -6 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 2) is a factor of x² + 2x + k', '8', 'Option 4', '-8', '2', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 2) to be a factor: f(2) = 0. 2² + 2(2) + k = 0. 4 + 4 + k = 0. k = -8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 1) is a factor of x² + 1x + k', '1', '-2', '2', 'Option 4', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 1) to be a factor: f(1) = 0. 1² + 1(1) + k = 0. 1 + 1 + k = 0. k = -2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 3) is a factor of x² + 4x + k', '-21', '21', '3', '4', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 3) to be a factor: f(3) = 0. 3² + 4(3) + k = 0. 9 + 12 + k = 0. k = -21 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 2) is a factor of x² + 2x + k', 'Option 4', '2', '8', '-8', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 2) to be a factor: f(2) = 0. 2² + 2(2) + k = 0. 4 + 4 + k = 0. k = -8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 2) is a factor of x² + 4x + k', '12', '4', '2', '-12', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 2) to be a factor: f(2) = 0. 2² + 4(2) + k = 0. 4 + 8 + k = 0. k = -12 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 3) is a factor of x² + 2x + k', '15', '2', '3', '-15', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 3) to be a factor: f(3) = 0. 3² + 2(3) + k = 0. 9 + 6 + k = 0. k = -15 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 3) is a factor of x² + 4x + k', '3', '4', '21', '-21', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 3) to be a factor: f(3) = 0. 3² + 4(3) + k = 0. 9 + 12 + k = 0. k = -21 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 1) is a factor of x² + 1x + k', '1', 'Option 4', '-2', '2', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 1) to be a factor: f(1) = 0. 1² + 1(1) + k = 0. 1 + 1 + k = 0. k = -2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 1) is a factor of x² + 2x + k', '-3', '1', '3', '2', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 1) to be a factor: f(1) = 0. 1² + 2(1) + k = 0. 1 + 2 + k = 0. k = -3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 1) is a factor of x² + 1x + k', '-2', '1', 'Option 4', '2', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 1) to be a factor: f(1) = 0. 1² + 1(1) + k = 0. 1 + 1 + k = 0. k = -2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 1) is a factor of x² + 2x + k', '3', '2', '1', '-3', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 1) to be a factor: f(1) = 0. 1² + 2(1) + k = 0. 1 + 2 + k = 0. k = -3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 2) is a factor of x² + 2x + k', '-8', '2', 'Option 4', '8', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 2) to be a factor: f(2) = 0. 2² + 2(2) + k = 0. 4 + 4 + k = 0. k = -8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 2) is a factor of x² + 2x + k', '2', '8', 'Option 4', '-8', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 2) to be a factor: f(2) = 0. 2² + 2(2) + k = 0. 4 + 4 + k = 0. k = -8 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find k if (x - 3) is a factor of x² + 2x + k', '-15', '2', '15', '3', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'For (x - 3) to be a factor: f(3) = 0. 3² + 2(3) + k = 0. 9 + 6 + k = 0. k = -15 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To check if (x + 3) is a factor of f(x), evaluate f at x = ', '3', '1/3', '-3', '0', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: -3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(2) = 0, which is definitely a factor of f(x)?', '(x + 2)', '(x - 4)', '(x - 2)', '(2x - 1)', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: (x - 2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(2) = 0, which is definitely a factor of f(x)?', '(x - 4)', '(x - 2)', '(x + 2)', '(2x - 1)', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: (x - 2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The Factor Theorem states: (x - a) is a factor of f(x) if and only if...', 'f(0) = a', 'f(a) = 0', 'f(-a) = 0', 'f(a) = 1', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: f(a) = 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(2) = 0, which is definitely a factor of f(x)?', '(x - 4)', '(x - 2)', '(2x - 1)', '(x + 2)', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: (x - 2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(2) = 0, which is definitely a factor of f(x)?', '(2x - 1)', '(x + 2)', '(x - 4)', '(x - 2)', 3,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: (x - 2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To check if (x + 3) is a factor of f(x), evaluate f at x = ', '1/3', '-3', '0', '3', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: -3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The Factor Theorem states: (x - a) is a factor of f(x) if and only if...', 'f(a) = 1', 'f(-a) = 0', 'f(a) = 0', 'f(0) = a', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: f(a) = 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The Factor Theorem states: (x - a) is a factor of f(x) if and only if...', 'f(a) = 0', 'f(-a) = 0', 'f(0) = a', 'f(a) = 1', 0,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: f(a) = 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(2) = 0, which is definitely a factor of f(x)?', '(x + 2)', '(x - 2)', '(2x - 1)', '(x - 4)', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: (x - 2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(2) = 0, which is definitely a factor of f(x)?', '(x - 4)', '(x - 2)', '(x + 2)', '(2x - 1)', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: (x - 2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The Factor Theorem states: (x - a) is a factor of f(x) if and only if...', 'f(a) = 1', 'f(a) = 0', 'f(0) = a', 'f(-a) = 0', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: f(a) = 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The Factor Theorem states: (x - a) is a factor of f(x) if and only if...', 'f(0) = a', 'f(a) = 1', 'f(a) = 0', 'f(-a) = 0', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: f(a) = 0 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To check if (x + 3) is a factor of f(x), evaluate f at x = ', '0', '1/3', '-3', '3', 2,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: -3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To check if (x + 3) is a factor of f(x), evaluate f at x = ', '0', '-3', '3', '1/3', 1,
'lc_hl_algebra', 10, 'advanced', 'lc_hl', 'Factor theorem: -3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', '(A+B)/[(x-1)(x+2)]', 'A/(x-1) × B/(x+2)', 'A(x-1) + B(x+2)', 'A/(x-1) + B/(x+2)', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', 'A/(x-1) × B/(x+2)', 'A(x-1) + B(x+2)', 'A/(x-1) + B/(x+2)', '(A+B)/[(x-1)(x+2)]', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', '(A+B)/[(x-1)(x+2)]', 'A/(x-1) × B/(x+2)', 'A/(x-1) + B/(x+2)', 'A(x-1) + B(x+2)', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 1/[(x-1)²(x+1)], the form is', '(A+B)/(x-1)² + C/(x+1)', 'A/(x-1) + B/(x+1)', 'A/(x-1) + B/(x-1)² + C/(x+1)', 'A/(x-1)² + B/(x+1)', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x-1)² + C/(x+1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (2x+1)/[(x-2)(x+3)], the form is', '(A+B)/(x-2)(x+3)', 'A(x-2) + B(x+3)', '(2x+1)/A + (2x+1)/B', 'A/(x-2) + B/(x+3)', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-2) + B/(x+3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 1/[(x-1)²(x+1)], the form is', 'A/(x-1) + B/(x+1)', 'A/(x-1)² + B/(x+1)', '(A+B)/(x-1)² + C/(x+1)', 'A/(x-1) + B/(x-1)² + C/(x+1)', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x-1)² + C/(x+1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', 'A/(x-1) + B/(x+2)', '(A+B)/[(x-1)(x+2)]', 'A/(x-1) × B/(x+2)', 'A(x-1) + B(x+2)', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', 'A/(x-1) + B/(x+2)', '(A+B)/[(x-1)(x+2)]', 'A/(x-1) × B/(x+2)', 'A(x-1) + B(x+2)', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', '(A+B)/[(x-1)(x+2)]', 'A/(x-1) + B/(x+2)', 'A/(x-1) × B/(x+2)', 'A(x-1) + B(x+2)', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', 'A/(x-1) × B/(x+2)', '(A+B)/[(x-1)(x+2)]', 'A/(x-1) + B/(x+2)', 'A(x-1) + B(x+2)', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (2x+1)/[(x-2)(x+3)], the form is', '(A+B)/(x-2)(x+3)', '(2x+1)/A + (2x+1)/B', 'A(x-2) + B(x+3)', 'A/(x-2) + B/(x+3)', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-2) + B/(x+3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 1/[(x-1)²(x+1)], the form is', 'A/(x-1) + B/(x-1)² + C/(x+1)', 'A/(x-1)² + B/(x+1)', 'A/(x-1) + B/(x+1)', '(A+B)/(x-1)² + C/(x+1)', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x-1)² + C/(x+1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (2x+1)/[(x-2)(x+3)], the form is', 'A(x-2) + B(x+3)', 'A/(x-2) + B/(x+3)', '(A+B)/(x-2)(x+3)', '(2x+1)/A + (2x+1)/B', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-2) + B/(x+3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (2x+1)/[(x-2)(x+3)], the form is', 'A(x-2) + B(x+3)', 'A/(x-2) + B/(x+3)', '(A+B)/(x-2)(x+3)', '(2x+1)/A + (2x+1)/B', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-2) + B/(x+3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (2x+1)/[(x-2)(x+3)], the form is', '(2x+1)/A + (2x+1)/B', 'A(x-2) + B(x+3)', '(A+B)/(x-2)(x+3)', 'A/(x-2) + B/(x+3)', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-2) + B/(x+3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (2x+1)/[(x-2)(x+3)], the form is', 'A/(x-2) + B/(x+3)', 'A(x-2) + B(x+3)', '(A+B)/(x-2)(x+3)', '(2x+1)/A + (2x+1)/B', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-2) + B/(x+3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (2x+1)/[(x-2)(x+3)], the form is', 'A/(x-2) + B/(x+3)', '(2x+1)/A + (2x+1)/B', 'A(x-2) + B(x+3)', '(A+B)/(x-2)(x+3)', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-2) + B/(x+3) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 1/[(x-1)²(x+1)], the form is', 'A/(x-1)² + B/(x+1)', 'A/(x-1) + B/(x+1)', '(A+B)/(x-1)² + C/(x+1)', 'A/(x-1) + B/(x-1)² + C/(x+1)', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x-1)² + C/(x+1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', '(A+B)/[(x-1)(x+2)]', 'A/(x-1) + B/(x+2)', 'A(x-1) + B(x+2)', 'A/(x-1) × B/(x+2)', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The partial fraction form of 1/[(x-1)(x+2)] is', 'A/(x-1) × B/(x+2)', 'A/(x-1) + B/(x+2)', 'A(x-1) + B(x+2)', '(A+B)/[(x-1)(x+2)]', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Partial fraction decomposition: A/(x-1) + B/(x+2) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-3)(x-6)] = A/(x-3) + B/(x-6), find A', '3', '1/3', '1', '1/-3', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 3: 1/(3-6) = A. A = 1/-3 = 1/-3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-3)(x-4)] = A/(x-3) + B/(x-4), find A', '-1', '1/1', '3', '1', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 3: 1/(3-4) = A. A = 1/-1 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-3)(x-6)] = A/(x-3) + B/(x-6), find A', '3', '1/3', '1', '1/-3', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 3: 1/(3-6) = A. A = 1/-3 = 1/-3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-2)(x-5)] = A/(x-2) + B/(x-5), find A', '1/-3', '1', '1/3', '2', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 2: 1/(2-5) = A. A = 1/-3 = 1/-3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-3)(x-6)] = A/(x-3) + B/(x-6), find A', '1', '3', '1/-3', '1/3', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 3: 1/(3-6) = A. A = 1/-3 = 1/-3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-2)(x-3)] = A/(x-2) + B/(x-3), find A', '-1', '1', '1/1', '2', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 2: 1/(2-3) = A. A = 1/-1 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-1)(x-2)] = A/(x-1) + B/(x-2), find A', '1', 'Option 4', '-1', '1/1', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 1: 1/(1-2) = A. A = 1/-1 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-1)(x-2)] = A/(x-1) + B/(x-2), find A', '1/1', '-1', '1', 'Option 4', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 1: 1/(1-2) = A. A = 1/-1 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-3)(x-6)] = A/(x-3) + B/(x-6), find A', '1/3', '1', '3', '1/-3', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 3: 1/(3-6) = A. A = 1/-3 = 1/-3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-2)(x-4)] = A/(x-2) + B/(x-4), find A', '1', '1/2', '2', '-1/2', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 2: 1/(2-4) = A. A = 1/-2 = -1/2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-1)(x-3)] = A/(x-1) + B/(x-3), find A', 'Option 4', '1', '1/2', '-1/2', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 1: 1/(1-3) = A. A = 1/-2 = -1/2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-3)(x-5)] = A/(x-3) + B/(x-5), find A', '1/2', '3', '1', '-1/2', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 3: 1/(3-5) = A. A = 1/-2 = -1/2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-2)(x-5)] = A/(x-2) + B/(x-5), find A', '1', '2', '1/3', '1/-3', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 2: 1/(2-5) = A. A = 1/-3 = 1/-3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-3)(x-4)] = A/(x-3) + B/(x-4), find A', '3', '1/1', '-1', '1', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 3: 1/(3-4) = A. A = 1/-1 = -1 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In 1/[(x-2)(x-4)] = A/(x-2) + B/(x-4), find A', '1/2', '1', '-1/2', '2', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Set x = 2: 1/(2-4) = A. A = 1/-2 = -1/2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '2', '3', '1', '4', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '1', '3', '4', '2', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '3', '2', '4', '1', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '1', '3', '2', '4', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For repeated factor (x-a)², the decomposition includes', 'A/(x-a)²', '(A+B)/(x-a)²', 'A/(x-a) only', 'A/(x-a) + B/(x-a)²', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: A/(x-a) + B/(x-a)² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '3', '4', '2', '1', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (x-3)³ in denominator, we need terms with', '(x-3) only', '(x-3)³ only', '(x-3), (x-3)², (x-3)³', '(x-3)² only', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: (x-3), (x-3)², (x-3)³ ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For repeated factor (x-a)², the decomposition includes', 'A/(x-a) only', '(A+B)/(x-a)²', 'A/(x-a) + B/(x-a)²', 'A/(x-a)²', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: A/(x-a) + B/(x-a)² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For repeated factor (x-a)², the decomposition includes', 'A/(x-a)²', 'A/(x-a) + B/(x-a)²', '(A+B)/(x-a)²', 'A/(x-a) only', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: A/(x-a) + B/(x-a)² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '1', '3', '4', '2', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '4', '3', '2', '1', 1,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For repeated factor (x-a)², the decomposition includes', 'A/(x-a)²', 'A/(x-a) only', 'A/(x-a) + B/(x-a)²', '(A+B)/(x-a)²', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: A/(x-a) + B/(x-a)² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For (x-3)³ in denominator, we need terms with', '(x-3)³ only', '(x-3) only', '(x-3), (x-3)², (x-3)³', '(x-3)² only', 2,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: (x-3), (x-3)², (x-3)³ ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For repeated factor (x-a)², the decomposition includes', 'A/(x-a) + B/(x-a)²', 'A/(x-a) only', 'A/(x-a)²', '(A+B)/(x-a)²', 0,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: A/(x-a) + B/(x-a)² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many constants are needed for 1/[(x-1)²(x+2)]?', '1', '2', '4', '3', 3,
'lc_hl_algebra', 11, 'advanced', 'lc_hl', 'Repeated factors: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If e^x = 7, then x = ', '7', 'e^7', 'log(7)', 'ln(7)', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: ln(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise 6/(√3 - 1)', '3(√3 + 1)', '3√3 - 3', '6/(√3 + 1)', '6√3 + 6', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3(√3 + 1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If e^x = 7, then x = ', 'ln(7)', 'log(7)', '7', 'e^7', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: ln(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √(72) ÷ √(8)', '√64', '9', '√9', '3', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 2log(3) - log(9) as a single log', 'log(6)', 'log(3)', 'log(0)', 'log(1)', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: log(1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √50 + √18', '8√2', '4√17', '6√2', '√68', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 8√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^(2x) = 81', '3', '27', '4', '2', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log(x) + log(4) = log(20), find x', '4', '80', '5', '16', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise 1/(2 + √3)', '(2 - √3)/1', '2 + √3', '1/(2 - √3)', '2 - √3', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 2 - √3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise 1/(2 + √3)', '2 + √3', '2 - √3', '1/(2 - √3)', '(2 - √3)/1', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 2 - √3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 5^0 × 5^3', '0', '125', '1', '15', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 125 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log₂(x) = 5, find x', '32', '64', '10', '25', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 32 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 2log(3) - log(9) as a single log', 'log(3)', 'log(0)', 'log(6)', 'log(1)', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: log(1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log₂(x) = 5, find x', '10', '25', '64', '32', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 32 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √50 + √18', '6√2', '4√17', '8√2', '√68', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 8√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log(x) + log(4) = log(20), find x', '4', '16', '80', '5', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log(a) = 2 and log(b) = 3, find log(ab)', '8', '5', '1', '6', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √50 + √18', '8√2', '4√17', '6√2', '√68', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 8√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (x^3)^(2/3)', 'x^(5/3)', 'x^5', 'x²', 'x^(9/2)', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: x² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log₂(x) = 5, find x', '10', '64', '32', '25', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 32 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise 1/(2 + √3)', '(2 - √3)/1', '1/(2 - √3)', '2 - √3', '2 + √3', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 2 - √3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If e^x = 7, then x = ', 'e^7', 'ln(7)', '7', 'log(7)', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: ln(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5^x = 125, find x', '2', '5', '25', '3', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8^(2/3)', '2', '4', '8', '16', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve log₃(x) = 4', '81', '64', '27', '12', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 81 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (x^3)^(2/3)', 'x^(9/2)', 'x^(5/3)', 'x²', 'x^5', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: x² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √50 + √18', '√68', '8√2', '6√2', '4√17', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 8√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^6', '3', '2', '6', '12', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 2log(3) - log(9) as a single log', 'log(1)', 'log(0)', 'log(3)', 'log(6)', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: log(1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 2log(3) - log(9) as a single log', 'log(6)', 'log(3)', 'log(1)', 'log(0)', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: log(1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log₂(x) = 5, find x', '32', '10', '25', '64', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 32 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5^x = 125, find x', '2', '25', '5', '3', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √50 + √18', '8√2', '6√2', '4√17', '√68', 0,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 8√2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √(72) ÷ √(8)', '√64', '9', '3', '√9', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rationalise 1/(2 + √3)', '1/(2 - √3)', '2 - √3', '2 + √3', '(2 - √3)/1', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 2 - √3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify 8^(2/3)', '2', '16', '8', '4', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 4 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If log(x) + log(4) = log(20), find x', '4', '80', '5', '16', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 5 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express 2log(3) - log(9) as a single log', 'log(3)', 'log(6)', 'log(1)', 'log(0)', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: log(1) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The value of log₁₀(1000) is', '100', '1000', '3', '10', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^6', '6', '3', '12', '2', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (x^3)^(2/3)', 'x^(5/3)', 'x²', 'x^5', 'x^(9/2)', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: x² ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √(72) ÷ √(8)', '√9', '9', '√64', '3', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 4^x = 2^6', '2', '3', '12', '6', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(x³y²) in terms of log x and log y', '5log(xy)', '6log(xy)', '3log x + 2log y', 'log(3x) + log(2y)', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3log x + 2log y ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 3^(2x) = 81', '3', '4', '2', '27', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express log(x³y²) in terms of log x and log y', '6log(xy)', '5log(xy)', 'log(3x) + log(2y)', '3log x + 2log y', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3log x + 2log y ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve 2^(x+1) = 8', '4', '3', '1', '2', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 2 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify √(72) ÷ √(8)', '√9', '√64', '9', '3', 3,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 3 ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If e^x = 7, then x = ', 'log(7)', '7', 'ln(7)', 'e^7', 2,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: ln(7) ✓', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify (27)^(-1/3)', '-3', '1/3', '3', '-1/3', 1,
'lc_hl_algebra', 12, 'advanced', 'lc_hl', 'Apply algebra techniques. Answer: 1/3 ✓', 1);