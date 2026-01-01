-- LC Ordinary Level - Calculus (Differentiation) Complete SQL
-- Generated: 2025-12-15
-- Total: 600 questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order, is_visible)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50, 1);

-- Add Calculus topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_ol_calculus', 'Calculus', id, '📐', 1, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_calculus';

-- Insert questions
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '4x⁴', 'x³', '4x³', '3x⁴', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁶, find dy/dx.', '6x⁵', '5x⁶', '6x⁶', 'x⁵', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 6x^5 = 6x⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁵, find dy/dx.', '5x⁵', 'x⁴', '5x⁴', '4x⁵', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 5x^4 = 5x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '4x⁴', 'x³', '3x⁴', '4x³', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁶, find dy/dx.', '6x⁶', '5x⁶', 'x⁵', '6x⁵', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 6x^5 = 6x⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁶, find dy/dx.', '6x⁵', '6x⁶', '5x⁶', 'x⁵', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 6x^5 = 6x⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '4x³', '3x⁴', 'x³', '4x⁴', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x², find dy/dx.', '2x', 'x', 'x²', '2x²', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 2x^1 = 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁶, find dy/dx.', '6x⁵', '5x⁶', '6x⁶', 'x⁵', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 6x^5 = 6x⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁵, find dy/dx.', '4x⁵', '5x⁴', '5x⁵', 'x⁴', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 5x^4 = 5x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '3x⁴', '4x³', 'x³', '4x⁴', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³, find dy/dx.', '3x³', 'x²', '3x²', '2x³', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 3x^2 = 3x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', 'x³', '3x⁴', '4x⁴', '4x³', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁶, find dy/dx.', '5x⁶', '6x⁶', '6x⁵', 'x⁵', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 6x^5 = 6x⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁵, find dy/dx.', '5x⁵', '5x⁴', 'x⁴', '4x⁵', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 5x^4 = 5x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '4x⁴', 'x³', '3x⁴', '4x³', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁵, find dy/dx.', '5x⁵', '5x⁴', '4x⁵', 'x⁴', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 5x^4 = 5x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁵, find dy/dx.', 'x⁴', '4x⁵', '5x⁴', '5x⁵', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 5x^4 = 5x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³, find dy/dx.', '3x³', 'x²', '3x²', '2x³', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 3x^2 = 3x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x², find dy/dx.', 'x', '2x', 'x²', '2x²', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 2x^1 = 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '4x⁴', 'x³', '4x³', '3x⁴', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '4x³', 'x³', '3x⁴', '4x⁴', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x², find dy/dx.', '2x', 'x', '2x²', 'x²', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 2x^1 = 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁴, find dy/dx.', '4x⁴', '4x³', '3x⁴', 'x³', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x^3 = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x², find dy/dx.', 'x', 'x²', '2x', '2x²', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 2x^1 = 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4x⁵, find dy/dx.', '20x⁴', '4x⁴', '20x⁵', '5x⁴', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 4 × 5x^4 = 20x^4 = 20x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x⁵, find dy/dx.', '10x⁵', '5x⁴', '2x⁴', '10x⁴', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 2 × 5x^4 = 10x^4 = 10x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x², find dy/dx.', '6x', '2x', '6x²', '3x', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 3 × 2x^1 = 6x^1 = 6x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 5x⁵, find dy/dx.', '25x⁵', '5x⁴', '25x⁴', 'Cannot determine', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 5 × 5x^4 = 25x^4 = 25x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4x³, find dy/dx.', '12x³', '3x²', '4x²', '12x²', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 4 × 3x^2 = 12x^2 = 12x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 5x⁵, find dy/dx.', '25x⁴', 'Cannot determine', '5x⁴', '25x⁵', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 5 × 5x^4 = 25x^4 = 25x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³, find dy/dx.', '6x³', '3x²', '2x²', '6x²', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 2 × 3x^2 = 6x^2 = 6x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³, find dy/dx.', '2x²', '6x²', '6x³', '3x²', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 2 × 3x^2 = 6x^2 = 6x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³, find dy/dx.', '2x²', '6x³', '3x²', '6x²', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 2 × 3x^2 = 6x^2 = 6x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 5x⁵, find dy/dx.', 'Cannot determine', '25x⁵', '25x⁴', '5x⁴', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 5 × 5x^4 = 25x^4 = 25x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x⁴, find dy/dx.', '12x³', '3x³', '4x³', '12x⁴', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 3 × 4x^3 = 12x^3 = 12x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 5x², find dy/dx.', '2x', '10x²', '5x', '10x', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 5 × 2x^1 = 10x^1 = 10x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x⁴, find dy/dx.', '4x³', '2x³', '8x³', '8x⁴', 2,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 2 × 4x^3 = 8x^3 = 8x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x², find dy/dx.', '3x', '6x', '6x²', '2x', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 3 × 2x^1 = 6x^1 = 6x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4x⁵, find dy/dx.', '4x⁴', '20x⁴', '5x⁴', '20x⁵', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'Power rule: dy/dx = 4 × 5x^4 = 20x^4 = 20x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 14, find dy/dx.', '14', '0', '1', '13', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 12, find dy/dx.', '11', '1', '12', '0', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 13, find dy/dx.', '0', '13', '1', '12', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 6, find dy/dx.', '1', '0', '5', '6', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3, find dy/dx.', '2', '1', '3', '0', 3,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 6, find dy/dx.', '0', '6', '1', '5', 0,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 18, find dy/dx.', '1', '0', '18', '17', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 10, find dy/dx.', '9', '0', '1', '10', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 6, find dy/dx.', '1', '0', '5', '6', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3, find dy/dx.', '2', '0', '1', '3', 1,
'lc_ol_calculus', 1, 'foundation', 'lc_ol', 'The derivative of a constant is always 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x⁴ - 3x, find f''(x).', '8x³ - 3', '9x³ - 3', '8x⁴ - 3x', '2x³ - 3', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 8x³ - 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x⁴ - 4x³, find f''(x).', '3x³ - 4x²', '12x³ - 12x²', '13x³ - 12x²', '12x⁴ - 12x³', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 12x³ - 12x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ - 6x², find f''(x).', '4x² - 12x', '3x² - 12x', 'x² - 6x', '3x³ - 12x²', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 3x² - 12x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x⁴ + 2, find f''(x).', '4x³ + 2', '16x³', '17x³', '16x⁴', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 16x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x² - 4x, find f''(x).', '8x² - 4x', '9x - 4', '8x - 4', '4x - 4', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 8x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ + 2x, find f''(x).', '6x² + 2', '7x² + 2', '2x² + 2', '6x³ + 2x', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 6x² + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x³ + 2x², find f''(x).', '9x³ + 4x²', '10x² + 4x', '9x² + 4x', '3x² + 2x', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 9x² + 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x² - 2x, find f''(x).', '4x - 2', '4x² - 2x', '5x - 2', '2x - 2', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 4x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x⁴ - 2x, find f''(x).', '4x³ - 2', '17x³ - 2', '16x³ - 2', '16x⁴ - 2x', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 16x³ - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x² + 2, find f''(x).', '4x²', '5x', '4x', '2x + 2', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x⁴ - 3x², find f''(x).', '12x⁴ - 6x²', '3x³ - 3x', '13x³ - 6x', '12x³ - 6x', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 12x³ - 6x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x⁴ + 5x, find f''(x).', '5x³ + 5', 'x³ + 5', '4x⁴ + 5x', '4x³ + 5', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 4x³ + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x² + 3, find f''(x).', '2x + 3', '4x', '5x', '4x²', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 3x, find f''(x).', 'x + 3', '2x² + 3x', '2x + 3', '3x + 3', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 2x + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x⁴ + x, find f''(x).', '16x³ + 1', '17x³ + 1', '4x³ + 1', '16x⁴ + x', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 16x³ + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x⁴ - 5x³, find f''(x).', '12x⁴ - 15x³', '13x³ - 15x²', '12x³ - 15x²', '3x³ - 5x²', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 12x³ - 15x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x⁴ - 6x², find f''(x).', '13x³ - 12x', '12x⁴ - 12x²', '12x³ - 12x', '3x³ - 6x', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 12x³ - 12x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x² + x, find f''(x).', '6x² + x', '3x + 1', '6x + 1', '7x + 1', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 6x + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 4x⁴ + x³, find f''(x).', '16x³ + 3x²', '16x⁴ + 3x³', '17x³ + 3x²', '4x³ + x²', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 16x³ + 3x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x² + 6, find f''(x).', 'x + 6', '3x', '2x²', '2x', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Differentiate term by term using the power rule: f''(x) = 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ + 2x² - 6, find dy/dx.', 'x² + 2x - 6', '3x³ + 4x²', '3x² + 4x', '4x² + 3x', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 3x² + 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ - 3x² + 3, find dy/dx.', 'x² - 3x + 3', '3x² - 6x', '4x² - 7x', '3x³ - 6x²', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 3x² - 6x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x³ - 4x² - 3x, find dy/dx.', '10x² - 9x', '9x³ - 8x²', '9x² - 8x - 3', '3x² - 4x - 3', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 9x² - 8x - 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ - 4x² - 6x, find dy/dx.', '7x² - 9x', '6x³ - 8x²', '2x² - 4x - 6', '6x² - 8x - 6', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 6x² - 8x - 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x³ + 3x² - 4x, find dy/dx.', '9x² + 6x - 4', '10x² + 5x', '9x³ + 6x²', '3x² + 3x - 4', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 9x² + 6x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ + 3x² + 2x, find dy/dx.', 'x² + 3x + 2', '4x² + 5x', '3x³ + 6x²', '3x² + 6x + 2', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 3x² + 6x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ - 4x² - 3, find dy/dx.', '3x² - 8x', '4x² - 9x', '3x³ - 8x²', 'x² - 4x - 3', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 3x² - 8x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ - x² + 3, find dy/dx.', '6x² - 2x', '7x² - 3x', '6x³ - 2x²', '2x² - x + 3', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 6x² - 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x³ + 4x² - 4, find dy/dx.', '10x² + 7x', '9x² + 8x', '9x³ + 8x²', '3x² + 4x - 4', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 9x² + 8x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ - 3x² - 2, find dy/dx.', '4x² - 7x', '3x² - 6x', '3x³ - 6x²', 'x² - 3x - 2', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 3x² - 6x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ - 3x² - 4x, find dy/dx.', '3x² - 6x - 4', 'x² - 3x - 4', '4x² - 7x', '3x³ - 6x²', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 3x² - 6x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ - 2x² - 4, find dy/dx.', '2x² - 2x - 4', '6x² - 4x', '7x² - 5x', '6x³ - 4x²', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 6x² - 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ + 2x² + 2x, find dy/dx.', '6x² + 4x + 2', '6x³ + 4x²', '7x² + 3x', '2x² + 2x + 2', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 6x² + 4x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ + x² - 1, find dy/dx.', '7x² + x', '6x³ + 2x²', '2x² + x - 1', '6x² + 2x', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 6x² + 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x³ + 2x² + 1, find dy/dx.', '9x² + 4x', '9x³ + 4x²', '10x² + 3x', '3x² + 2x + 1', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 9x² + 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ - 2x² - 2, find dy/dx.', '2x² - 2x - 2', '6x² - 4x', '7x² - 5x', '6x³ - 4x²', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 6x² - 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ + 3x² - 2x, find dy/dx.', '6x² + 6x - 2', '2x² + 3x - 2', '6x³ + 6x²', '7x² + 5x', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 6x² + 6x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x³ - 2x² + x, find dy/dx.', '9x² - 4x + 1', '9x³ - 4x²', '3x² - 2x + 1', '10x² - 5x', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 9x² - 4x + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x³ + x² - 2x, find dy/dx.', '9x³ + 2x²', '3x² + x - 2', '9x² + 2x - 2', '10x² + x', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 9x² + 2x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ + 3x² - 4, find dy/dx.', '4x² + 5x', '3x³ + 6x²', '3x² + 6x', 'x² + 3x - 4', 2,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Apply the power rule to each term: dy/dx = 3x² + 6x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³, what is dy/dx?', '3x²', '3x³', '3x', 'Cannot determine', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 3x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x⁴, what is f''(x)?', '4x³', '4x⁴', 'x³', '4x²', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: f''(x) = 4x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x², what is dy/dx?', '1', '4x', '0', 'x', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If g(x) = 5x³, what is g''(x)?', '15x³', '15x²', '15x', '1x³', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: g''(x) = 15x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If s(t) = t², what is s''(t)?', '2t', '0', '1', 'x', 0,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: s''(t) = 2t', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x⁵, what is dy/dx?', '5x⁵', '5x³', 'x⁴', '5x⁴', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 5x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If h(x) = 3x⁴, what is h''(x)?', '12x²', '12x³', 'x³', '12x⁴', 1,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: h''(x) = 12x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4x, what is dy/dx?', 'x', '1', '0', '4', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: dy/dx = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 6x², what is f''(x)?', 'x', '0', '1', '12x', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: f''(x) = 12x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P(t) = t³, what is P''(t)?', '0', 'x', '1', '3t²', 3,
'lc_ol_calculus', 2, 'foundation', 'lc_ol', 'Using the power rule: P''(t) = 3t²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 5/x³, rewrite as y = ax^n and find dy/dx.', '-5x⁻⁴', '-15x⁻³', '15x⁻⁴', '-15x⁻⁴', 3,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 5x^-3. Then dy/dx = -3 × 5x^-4 = -15x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4/x⁴, rewrite as y = ax^n and find dy/dx.', '-16x⁻⁴', '-16x⁻⁵', '-4x⁻⁵', '16x⁻⁵', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 4x^-4. Then dy/dx = -4 × 4x^-5 = -16x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3/x³, rewrite as y = ax^n and find dy/dx.', '-9x⁻⁴', '-3x⁻⁴', '9x⁻⁴', '-9x⁻³', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 3x^-3. Then dy/dx = -3 × 3x^-4 = -9x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4/x³, rewrite as y = ax^n and find dy/dx.', '-12x⁻⁴', '-4x⁻⁴', '12x⁻⁴', '-12x⁻³', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 4x^-3. Then dy/dx = -3 × 4x^-4 = -12x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 5/x², rewrite as y = ax^n and find dy/dx.', '-10x⁻³', '10x⁻³', '-5x⁻³', '-10x⁻²', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 5x^-2. Then dy/dx = -2 × 5x^-3 = -10x⁻³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 5/x², rewrite as y = ax^n and find dy/dx.', '-5x⁻³', '-10x⁻³', '-10x⁻²', '10x⁻³', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 5x^-2. Then dy/dx = -2 × 5x^-3 = -10x⁻³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4/x², rewrite as y = ax^n and find dy/dx.', '-4x⁻³', '-8x⁻³', '8x⁻³', '-8x⁻²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 4x^-2. Then dy/dx = -2 × 4x^-3 = -8x⁻³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4/x⁴, rewrite as y = ax^n and find dy/dx.', '-4x⁻⁵', '16x⁻⁵', '-16x⁻⁴', '-16x⁻⁵', 3,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 4x^-4. Then dy/dx = -4 × 4x^-5 = -16x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x⁴, rewrite as y = ax^n and find dy/dx.', '-1x⁻⁵', '-4x⁻⁵', '-4x⁻⁴', '4x⁻⁵', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 1x^-4. Then dy/dx = -4 × 1x^-5 = -4x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3/x⁴, rewrite as y = ax^n and find dy/dx.', '-12x⁻⁵', '12x⁻⁵', '-3x⁻⁵', '-12x⁻⁴', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 3x^-4. Then dy/dx = -4 × 3x^-5 = -12x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², rewrite as y = ax^n and find dy/dx.', '-2x⁻³', '-2x⁻²', '2x⁻³', '-1x⁻³', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 1x^-2. Then dy/dx = -2 × 1x^-3 = -2x⁻³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2/x³, rewrite as y = ax^n and find dy/dx.', '-6x⁻⁴', '6x⁻⁴', '-6x⁻³', '-2x⁻⁴', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 2x^-3. Then dy/dx = -3 × 2x^-4 = -6x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3/x⁴, rewrite as y = ax^n and find dy/dx.', '-12x⁻⁵', '-12x⁻⁴', '12x⁻⁵', '-3x⁻⁵', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 3x^-4. Then dy/dx = -4 × 3x^-5 = -12x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x³, rewrite as y = ax^n and find dy/dx.', '-3x⁻³', '3x⁻⁴', '-1x⁻⁴', '-3x⁻⁴', 3,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 1x^-3. Then dy/dx = -3 × 1x^-4 = -3x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x⁴, rewrite as y = ax^n and find dy/dx.', '4x⁻⁵', '-4x⁻⁵', '-1x⁻⁵', '-4x⁻⁴', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 1x^-4. Then dy/dx = -4 × 1x^-5 = -4x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4/x⁴, rewrite as y = ax^n and find dy/dx.', '-16x⁻⁵', '16x⁻⁵', '-4x⁻⁵', '-16x⁻⁴', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 4x^-4. Then dy/dx = -4 × 4x^-5 = -16x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 4/x³, rewrite as y = ax^n and find dy/dx.', '-12x⁻⁴', '-4x⁻⁴', '12x⁻⁴', '-12x⁻³', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 4x^-3. Then dy/dx = -3 × 4x^-4 = -12x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x³, rewrite as y = ax^n and find dy/dx.', '-3x⁻³', '-3x⁻⁴', '-1x⁻⁴', '3x⁻⁴', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 1x^-3. Then dy/dx = -3 × 1x^-4 = -3x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x⁴, rewrite as y = ax^n and find dy/dx.', '-1x⁻⁵', '4x⁻⁵', '-4x⁻⁵', '-4x⁻⁴', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 1x^-4. Then dy/dx = -4 × 1x^-5 = -4x⁻⁵', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2/x³, rewrite as y = ax^n and find dy/dx.', '-6x⁻³', '-6x⁻⁴', '-2x⁻⁴', '6x⁻⁴', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Rewrite as y = 2x^-3. Then dy/dx = -3 × 2x^-4 = -6x⁻⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x, find dy/dx.', '-1/x²', '-1/x', '1/x', '1/x²', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-1, apply power rule: dy/dx = -1x^-2 = -1/x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x³, find dy/dx.', '-1/x⁴', '3/x⁴', '-3/x³', '-3/x⁴', 3,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-3, apply power rule: dy/dx = -3x^-4 = -3/x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x, find dy/dx.', '-1/x', '1/x', '-1/x²', '1/x²', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-1, apply power rule: dy/dx = -1x^-2 = -1/x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x, find dy/dx.', '-1/x', '-1/x²', '1/x', '1/x²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-1, apply power rule: dy/dx = -1x^-2 = -1/x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², find dy/dx.', '-1/x³', '-2/x²', '-2/x³', '2/x³', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-2, apply power rule: dy/dx = -2x^-3 = -2/x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², find dy/dx.', '-1/x³', '2/x³', '-2/x³', '-2/x²', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-2, apply power rule: dy/dx = -2x^-3 = -2/x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², find dy/dx.', '-1/x³', '-2/x³', '2/x³', '-2/x²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-2, apply power rule: dy/dx = -2x^-3 = -2/x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x³, find dy/dx.', '-1/x⁴', '-3/x³', '-3/x⁴', '3/x⁴', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-3, apply power rule: dy/dx = -3x^-4 = -3/x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x³, find dy/dx.', '-1/x⁴', '3/x⁴', '-3/x⁴', '-3/x³', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-3, apply power rule: dy/dx = -3x^-4 = -3/x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x³, find dy/dx.', '-1/x⁴', '3/x⁴', '-3/x³', '-3/x⁴', 3,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-3, apply power rule: dy/dx = -3x^-4 = -3/x⁴', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x, find dy/dx.', '-1/x²', '1/x', '-1/x', '1/x²', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-1, apply power rule: dy/dx = -1x^-2 = -1/x²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², find dy/dx.', '2/x³', '-2/x²', '-2/x³', '-1/x³', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-2, apply power rule: dy/dx = -2x^-3 = -2/x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², find dy/dx.', '-2/x³', '2/x³', '-1/x³', '-2/x²', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-2, apply power rule: dy/dx = -2x^-3 = -2/x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², find dy/dx.', '-1/x³', '-2/x²', '-2/x³', '2/x³', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-2, apply power rule: dy/dx = -2x^-3 = -2/x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 1/x², find dy/dx.', '-1/x³', '-2/x²', '-2/x³', '2/x³', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Write as x^-2, apply power rule: dy/dx = -2x^-3 = -2/x³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ + 2/x, find dy/dx.', 'x² - 2/x²', '3x³ - 2/x', '3x² - 2/x²', '3x² + 2/x²', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 3x^2 from power rule, and -(2)x^-2 = -2/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ + 4/x, find dy/dx.', '6x² - 4/x²', '6x² + 4/x²', '6x³ - 4/x', '2x² - 4/x²', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 6x^2 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x² + 4/x, find dy/dx.', '6x² - 4/x', '6x - 4/x²', '6x + 4/x²', '3x - 4/x²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 6x^1 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x² + 4/x, find dy/dx.', '2x + 4/x²', '2x - 4/x²', '2x² - 4/x', 'x - 4/x²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 2x^1 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x² + 3/x, find dy/dx.', '4x - 3/x²', '4x + 3/x²', '2x - 3/x²', '4x² - 3/x', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 4x^1 from power rule, and -(3)x^-2 = -3/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x² + 1/x, find dy/dx.', '6x + 1/x²', '6x - 1/x²', '6x² - 1/x', '3x - 1/x²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 6x^1 from power rule, and -(1)x^-2 = -1/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x² + 1/x, find dy/dx.', '2x - 1/x²', '4x - 1/x²', '4x² - 1/x', '4x + 1/x²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 4x^1 from power rule, and -(1)x^-2 = -1/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ + 4/x, find dy/dx.', '6x³ - 4/x', '2x² - 4/x²', '6x² + 4/x²', '6x² - 4/x²', 3,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 6x^2 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x³ + 3/x, find dy/dx.', '9x³ - 3/x', '3x² - 3/x²', '9x² - 3/x²', '9x² + 3/x²', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 9x^2 from power rule, and -(3)x^-2 = -3/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x³ + 4/x, find dy/dx.', '2x² - 4/x²', '6x³ - 4/x', '6x² + 4/x²', '6x² - 4/x²', 3,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 6x^2 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x³ + 4/x, find dy/dx.', 'x² - 4/x²', '3x² - 4/x²', '3x³ - 4/x', '3x² + 4/x²', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 3x^2 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 2x² + 4/x, find dy/dx.', '4x - 4/x²', '4x² - 4/x', '2x - 4/x²', '4x + 4/x²', 0,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 4x^1 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x² + 2/x, find dy/dx.', '2x + 2/x²', '2x - 2/x²', 'x - 2/x²', '2x² - 2/x', 1,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 2x^1 from power rule, and -(2)x^-2 = -2/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = x² + 4/x, find dy/dx.', 'x - 4/x²', '2x + 4/x²', '2x - 4/x²', '2x² - 4/x', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 2x^1 from power rule, and -(4)x^-2 = -4/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If y = 3x² + 3/x, find dy/dx.', '6x + 3/x²', '6x² - 3/x', '6x - 3/x²', '3x - 3/x²', 2,
'lc_ol_calculus', 3, 'foundation', 'lc_ol', 'Differentiate each term: 6x^1 from power rule, and -(3)x^-2 = -3/x² from 1/x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ at x = 2.', '12', '16', '24', '30', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 6x². At x = 2: slope = 6(2)^2 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 3x² at x = 3.', '27', 'Cannot determine', '18', '24', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 6x. At x = 3: slope = 6(3)^1 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x² at x = 3.', '9', 'Cannot determine', '8', '6', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 3: slope = 2(3)^1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ at x = 4.', '48', '12', '51', '64', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 3x². At x = 4: slope = 3(4)^2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 3x³ at x = 4.', '144', '36', '192', '153', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 9x². At x = 4: slope = 9(4)^2 = 144', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x² at x = 1.', '1', '2', '4', 'Cannot determine', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 1: slope = 2(1)^1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 3x² at x = 4.', '24', '48', 'Cannot determine', '30', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 6x. At x = 4: slope = 6(4)^1 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ at x = 2.', '8', '12', '6', '15', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 3x². At x = 2: slope = 3(2)^2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ at x = 3.', '9', 'Cannot determine', '27', '30', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 3x². At x = 3: slope = 3(3)^2 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x² at x = 2.', 'Cannot determine', '8', '12', 'Cannot determine', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 2: slope = 4(2)^1 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x² at x = 2.', '12', 'Cannot determine', '8', 'Cannot determine', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 2: slope = 4(2)^1 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ at x = 4.', '102', '128', '24', '96', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 6x². At x = 4: slope = 6(4)^2 = 96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ at x = 4.', '102', '128', '96', '24', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 6x². At x = 4: slope = 6(4)^2 = 96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ at x = 3.', 'Cannot determine', '27', '30', '9', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 3x². At x = 3: slope = 3(3)^2 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 3x² at x = 2.', '18', 'Cannot determine', '12', 'Cannot determine', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 6x. At x = 2: slope = 6(2)^1 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x² at x = 1.', '4', '2', 'Cannot determine', '1', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 1: slope = 2(1)^1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 3x³ at x = 1.', '3', '9', '18', 'Cannot determine', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 9x². At x = 1: slope = 9(1)^2 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x² at x = 1.', '1', '2', 'Cannot determine', '4', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 1: slope = 2(1)^1 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ at x = 3.', 'Cannot determine', '30', '9', '27', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 3x². At x = 3: slope = 3(3)^2 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x² at x = 4.', '8', '10', 'Cannot determine', '16', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 4: slope = 2(4)^1 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 3x³ at x = 1.', 'Cannot determine', '18', '3', '9', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 9x². At x = 1: slope = 9(1)^2 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x² at x = 3.', '8', 'Cannot determine', '9', '6', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 3: slope = 2(3)^1 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ at x = 4.', '64', '48', '51', '12', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 3x². At x = 4: slope = 3(4)^2 = 48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 3x² at x = 3.', '24', '27', 'Cannot determine', '18', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 6x. At x = 3: slope = 6(3)^1 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x² at x = 2.', 'Cannot determine', 'Cannot determine', '4', '6', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 2: slope = 2(2)^1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ - 2x at x = 2.', '12', '10', '20', '22', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + -2. At x = 2: f''(2) = 6(2)² + -2 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ + 2x at x = 2.', '14', '28', '20', '26', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + 2. At x = 2: f''(2) = 6(2)² + 2 = 26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = x³ + x at x = 3.', '30', '29', '28', '10', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 3x² + 1. At x = 3: f''(3) = 3(3)² + 1 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = x³ - 2x at x = 2.', '10', '4', '8', 'Cannot determine', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 3x² + -2. At x = 2: f''(2) = 3(2)² + -2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = x³ - x at x = 2.', '10', '11', '5', '6', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 3x² + -1. At x = 2: f''(2) = 3(2)² + -1 = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = x³ + x at x = 3.', '30', '29', '28', '10', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 3x² + 1. At x = 3: f''(3) = 3(3)² + 1 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = x³ - 4x at x = 3.', '19', '23', '15', '5', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 3x² + -4. At x = 3: f''(3) = 3(3)² + -4 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ + x at x = 2.', '25', '13', '18', '26', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + 1. At x = 2: f''(2) = 6(2)² + 1 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ + 3x at x = 2.', '27', '30', '15', '22', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + 3. At x = 2: f''(2) = 6(2)² + 3 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ + x at x = 3.', '55', '56', '57', '19', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + 1. At x = 3: f''(3) = 6(3)² + 1 = 55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ + 3x at x = 2.', '27', '22', '15', '30', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + 3. At x = 2: f''(2) = 6(2)² + 3 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ - 2x at x = 2.', '10', '12', '22', '20', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + -2. At x = 2: f''(2) = 6(2)² + -2 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ - 2x at x = 2.', '10', '20', '12', '22', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + -2. At x = 2: f''(2) = 6(2)² + -2 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = 2x³ - x at x = 2.', '23', '14', '11', '22', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 6x² + -1. At x = 2: f''(2) = 6(2)² + -1 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of f(x) = x³ + x at x = 1.', '5', '4', 'Cannot determine', '2', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'f''(x) = 3x² + 1. At x = 1: f''(1) = 3(1)² + 1 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 3x + 4, find the slope of the tangent at x = 4.', '7', '19', '16', '12', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 4: slope = 3(4) + 4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 3x + -6, find the slope of the tangent at x = 3.', '-3', '3', '6', '9', 1,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 3: slope = 3(3) + -6 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 2x + 6, find the slope of the tangent at x = 3.', '6', '8', '12', '14', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 3: slope = 2(3) + 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 3x + 6, find the slope of the tangent at x = 4.', '18', '12', '9', '21', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 4: slope = 3(4) + 6 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 2x + 2, find the slope of the tangent at x = 1.', 'Cannot determine', '6', '2', '4', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 1: slope = 2(1) + 2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 2x + -1, find the slope of the tangent at x = 3.', '1', '6', '5', '7', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 3: slope = 2(3) + -1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 2x + 1, find the slope of the tangent at x = 2.', '4', '7', '3', '5', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 2: slope = 2(2) + 1 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 4x + -1, find the slope of the tangent at x = 1.', '3', '4', '7', 'Cannot determine', 0,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 1: slope = 4(1) + -1 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 3x + -5, find the slope of the tangent at x = 1.', '3', 'Cannot determine', '1', '-2', 3,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 1: slope = 3(1) + -5 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If dy/dx = 5x + -3, find the slope of the tangent at x = 3.', '15', '17', '12', '2', 2,
'lc_ol_calculus', 4, 'developing', 'lc_ol', 'Substitute x = 3: slope = 5(3) + -3 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (2, 8).', 'y = 8x - 8', 'y = 8x - -6', 'y = 4x + 8', 'y = 8x + 8', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 2: slope = 8. Using y - y₁ = m(x - x₁): y - 8 = 8(x - 2), so y = 8x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (2, 4).', 'y = 2x + 4', 'y = 4x - 4', 'y = 4x + 4', 'y = 4x - -2', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 2: slope = 4. Using y - y₁ = m(x - x₁): y - 4 = 4(x - 2), so y = 4x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (1, 2).', 'y = 4x - 0', 'Cannot determine', 'y = 4x + 2', 'y = 4x - 2', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 1: slope = 4. Using y - y₁ = m(x - x₁): y - 2 = 4(x - 1), so y = 4x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (2, 4).', 'y = 4x - -2', 'y = 4x + 4', 'y = 2x + 4', 'y = 4x - 4', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 2: slope = 4. Using y - y₁ = m(x - x₁): y - 4 = 4(x - 2), so y = 4x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (3, 9).', 'y = 6x - -7', 'y = 6x + 9', 'y = 6x - 9', 'y = 2x + 9', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 3: slope = 6. Using y - y₁ = m(x - x₁): y - 9 = 6(x - 3), so y = 6x - 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (1, 2).', 'Cannot determine', 'y = 4x - 2', 'y = 4x + 2', 'y = 4x - 0', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 1: slope = 4. Using y - y₁ = m(x - x₁): y - 2 = 4(x - 1), so y = 4x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (2, 4).', 'y = 4x - -2', 'y = 4x + 4', 'y = 2x + 4', 'y = 4x - 4', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 2: slope = 4. Using y - y₁ = m(x - x₁): y - 4 = 4(x - 2), so y = 4x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (2, 8).', 'y = 8x - -6', 'y = 4x + 8', 'y = 8x - 8', 'y = 8x + 8', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 2: slope = 8. Using y - y₁ = m(x - x₁): y - 8 = 8(x - 2), so y = 8x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (1, 2).', 'Cannot determine', 'y = 4x + 2', 'y = 4x - 2', 'y = 4x - 0', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 1: slope = 4. Using y - y₁ = m(x - x₁): y - 2 = 4(x - 1), so y = 4x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (1, 1).', 'y = 2x + 1', 'Cannot determine', 'y = 2x - 1', 'Cannot determine', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 1: slope = 2. Using y - y₁ = m(x - x₁): y - 1 = 2(x - 1), so y = 2x - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (3, 9).', 'y = 6x - -7', 'y = 2x + 9', 'y = 6x - 9', 'y = 6x + 9', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 3: slope = 6. Using y - y₁ = m(x - x₁): y - 9 = 6(x - 3), so y = 6x - 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (2, 8).', 'y = 8x - -6', 'y = 8x + 8', 'y = 4x + 8', 'y = 8x - 8', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 2: slope = 8. Using y - y₁ = m(x - x₁): y - 8 = 8(x - 2), so y = 8x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (2, 8).', 'y = 8x + 8', 'y = 8x - 8', 'y = 8x - -6', 'y = 4x + 8', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 2: slope = 8. Using y - y₁ = m(x - x₁): y - 8 = 8(x - 2), so y = 8x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (2, 4).', 'y = 4x - -2', 'y = 4x + 4', 'y = 4x - 4', 'y = 2x + 4', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 2: slope = 4. Using y - y₁ = m(x - x₁): y - 4 = 4(x - 2), so y = 4x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (3, 9).', 'y = 6x - 9', 'y = 2x + 9', 'y = 6x - -7', 'y = 6x + 9', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 3: slope = 6. Using y - y₁ = m(x - x₁): y - 9 = 6(x - 3), so y = 6x - 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (3, 18).', 'y = 4x + 18', 'y = 12x - -16', 'y = 12x + 18', 'y = 12x - 18', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 3: slope = 12. Using y - y₁ = m(x - x₁): y - 18 = 12(x - 3), so y = 12x - 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (3, 18).', 'y = 12x - -16', 'y = 12x - 18', 'y = 12x + 18', 'y = 4x + 18', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 3: slope = 12. Using y - y₁ = m(x - x₁): y - 18 = 12(x - 3), so y = 12x - 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (3, 9).', 'y = 6x + 9', 'y = 6x - -7', 'y = 6x - 9', 'y = 2x + 9', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 3: slope = 6. Using y - y₁ = m(x - x₁): y - 9 = 6(x - 3), so y = 6x - 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (3, 9).', 'y = 2x + 9', 'y = 6x - -7', 'y = 6x - 9', 'y = 6x + 9', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 3: slope = 6. Using y - y₁ = m(x - x₁): y - 9 = 6(x - 3), so y = 6x - 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (2, 4).', 'y = 2x + 4', 'y = 4x + 4', 'y = 4x - 4', 'y = 4x - -2', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 2: slope = 4. Using y - y₁ = m(x - x₁): y - 4 = 4(x - 2), so y = 4x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (2, 8).', 'y = 4x + 8', 'y = 8x + 8', 'y = 8x - 8', 'y = 8x - -6', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 2: slope = 8. Using y - y₁ = m(x - x₁): y - 8 = 8(x - 2), so y = 8x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (1, 1).', 'y = 2x - 1', 'y = 2x + 1', 'Cannot determine', 'Cannot determine', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 1: slope = 2. Using y - y₁ = m(x - x₁): y - 1 = 2(x - 1), so y = 2x - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = x² at the point (2, 4).', 'y = 4x + 4', 'y = 4x - 4', 'y = 4x - -2', 'y = 2x + 4', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x. At x = 2: slope = 4. Using y - y₁ = m(x - x₁): y - 4 = 4(x - 2), so y = 4x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (3, 18).', 'y = 12x - -16', 'y = 12x + 18', 'y = 12x - 18', 'y = 4x + 18', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 3: slope = 12. Using y - y₁ = m(x - x₁): y - 18 = 12(x - 3), so y = 12x - 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to y = 2x² at the point (3, 18).', 'y = 12x - -16', 'y = 12x + 18', 'y = 4x + 18', 'y = 12x - 18', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 4x. At x = 3: slope = 12. Using y - y₁ = m(x - x₁): y - 18 = 12(x - 3), so y = 12x - 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 4 has y-intercept at:', 'Cannot determine', '(0, 32)', '(0, 16)', '(0, -32)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 16, point (4, 32). Tangent: y = 16x + c. At (4, 32): 32 = 16(4) + c, so c = -32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = x² at x = 4 has y-intercept at:', '(0, 8)', '(0, 16)', 'Cannot determine', '(0, -16)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 8, point (4, 16). Tangent: y = 8x + c. At (4, 16): 16 = 8(4) + c, so c = -16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 2 has y-intercept at:', '(0, 8)', 'Cannot determine', 'Cannot determine', '(0, -8)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 8, point (2, 8). Tangent: y = 8x + c. At (2, 8): 8 = 8(2) + c, so c = -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 2 has y-intercept at:', 'Cannot determine', '(0, 8)', '(0, -8)', 'Cannot determine', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 8, point (2, 8). Tangent: y = 8x + c. At (2, 8): 8 = 8(2) + c, so c = -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 4 has y-intercept at:', '(0, -32)', '(0, 32)', 'Cannot determine', '(0, 16)', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 16, point (4, 32). Tangent: y = 16x + c. At (4, 32): 32 = 16(4) + c, so c = -32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 2 has y-intercept at:', 'Cannot determine', '(0, -8)', '(0, 8)', 'Cannot determine', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 8, point (2, 8). Tangent: y = 8x + c. At (2, 8): 8 = 8(2) + c, so c = -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = x² at x = 4 has y-intercept at:', '(0, 8)', '(0, 16)', 'Cannot determine', '(0, -16)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 8, point (4, 16). Tangent: y = 8x + c. At (4, 16): 16 = 8(4) + c, so c = -16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 4 has y-intercept at:', '(0, -32)', 'Cannot determine', '(0, 32)', '(0, 16)', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 16, point (4, 32). Tangent: y = 16x + c. At (4, 32): 32 = 16(4) + c, so c = -32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 4 has y-intercept at:', 'Cannot determine', '(0, -32)', '(0, 16)', '(0, 32)', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 16, point (4, 32). Tangent: y = 16x + c. At (4, 32): 32 = 16(4) + c, so c = -32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = x² at x = 3 has y-intercept at:', 'Cannot determine', '(0, -9)', '(0, 6)', '(0, 9)', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 6, point (3, 9). Tangent: y = 6x + c. At (3, 9): 9 = 6(3) + c, so c = -9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = x² at x = 2 has y-intercept at:', 'Cannot determine', '(0, 4)', 'Cannot determine', '(0, -4)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 4, point (2, 4). Tangent: y = 4x + c. At (2, 4): 4 = 4(2) + c, so c = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 4 has y-intercept at:', '(0, 32)', 'Cannot determine', '(0, 16)', '(0, -32)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 16, point (4, 32). Tangent: y = 16x + c. At (4, 32): 32 = 16(4) + c, so c = -32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = x² at x = 4 has y-intercept at:', '(0, -16)', '(0, 8)', 'Cannot determine', '(0, 16)', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 8, point (4, 16). Tangent: y = 8x + c. At (4, 16): 16 = 8(4) + c, so c = -16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 3 has y-intercept at:', 'Cannot determine', '(0, 12)', '(0, 18)', '(0, -18)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 12, point (3, 18). Tangent: y = 12x + c. At (3, 18): 18 = 12(3) + c, so c = -18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The tangent to y = 2x² at x = 2 has y-intercept at:', '(0, -8)', 'Cannot determine', 'Cannot determine', '(0, 8)', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'Slope = 8, point (2, 8). Tangent: y = 8x + c. At (2, 8): 8 = 8(2) + c, so c = -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 6?', '(3, 6)', '(3, 9)', '(4, 16)', '(6, 36)', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 6, so x = 3. At x = 3: y = 9. Point is (3, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 4?', '(2, 4)', 'Cannot determine', '(3, 9)', '(4, 16)', 0,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 4, so x = 2. At x = 2: y = 4. Point is (2, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 12?', '(7, 49)', '(6, 12)', '(12, 144)', '(6, 36)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 12, so x = 6. At x = 6: y = 36. Point is (6, 36)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 8?', '(8, 64)', '(5, 25)', '(4, 8)', '(4, 16)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 8, so x = 4. At x = 4: y = 16. Point is (4, 16)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 10?', '(5, 10)', '(5, 25)', '(6, 36)', '(10, 100)', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 10, so x = 5. At x = 5: y = 25. Point is (5, 25)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 16?', '(16, 256)', '(9, 81)', '(8, 64)', '(8, 16)', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 16, so x = 8. At x = 8: y = 64. Point is (8, 64)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 6?', '(4, 16)', '(3, 6)', '(3, 9)', '(6, 36)', 2,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 6, so x = 3. At x = 3: y = 9. Point is (3, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 12?', '(6, 12)', '(7, 49)', '(12, 144)', '(6, 36)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 12, so x = 6. At x = 6: y = 36. Point is (6, 36)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 8?', '(4, 8)', '(5, 25)', '(8, 64)', '(4, 16)', 3,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 8, so x = 4. At x = 4: y = 16. Point is (4, 16)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('At what point on y = x² does the tangent have slope 12?', '(6, 12)', '(6, 36)', '(7, 49)', '(12, 144)', 1,
'lc_ol_calculus', 5, 'developing', 'lc_ol', 'dy/dx = 2x = 12, so x = 6. At x = 6: y = 36. Point is (6, 36)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance s (metres) is given by d = 3t² - 4t + 2. Find the velocity when t = 1.', '-2 m/s', '2 m/s', '6 m/s', '1 m/s', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dd/dt = 6t + -4. At t = 1: rate = 6(1) + -4 = 2 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The population P (thousands) is given by p = 3t² - 2t. Find the rate of growth when t = 4.', '22 thousand/year', '20 thousand/year', '24 thousand/year', '40 thousand/year', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 6t + -2. At t = 4: rate = 6(4) + -2 = 22 thousand/year', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The temperature T (°C) is given by t = 3t² + t + 7. Find the rate of cooling when t = 1.', '11 °C/min', '6 °C/min', '7 °C/min', '8 °C/min', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dt/dt = 6t + 1. At t = 1: rate = 6(1) + 1 = 7 °C/min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The profit P (€ thousands) is given by p = 2t² - t. Find the marginal profit when t = 2.', '6 € thousand/unit', '7 € thousand/unit', 'Cannot determine', '8 € thousand/unit', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 4t + -1. At t = 2: rate = 4(2) + -1 = 7 € thousand/unit', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The height h (metres) is given by h = 2t² + 4t + 4. Find the velocity when t = 4.', '24 m/s', '20 m/s', '16 m/s', '52 m/s', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dh/dt = 4t + 4. At t = 4: rate = 4(4) + 4 = 20 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance s (metres) is given by d = 2t² + t + 5. Find the velocity when t = 1.', '6 m/s', '8 m/s', '5 m/s', '4 m/s', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dd/dt = 4t + 1. At t = 1: rate = 4(1) + 1 = 5 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The population P (thousands) is given by p = 2t² + 2t + 7. Find the rate of growth when t = 1.', '11 thousand/year', '6 thousand/year', '4 thousand/year', '8 thousand/year', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 4t + 2. At t = 1: rate = 4(1) + 2 = 6 thousand/year', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The temperature T (°C) is given by t = 3t² + 3t + 3. Find the rate of cooling when t = 2.', '15 °C/min', '18 °C/min', '12 °C/min', '21 °C/min', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dt/dt = 6t + 3. At t = 2: rate = 6(2) + 3 = 15 °C/min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The profit P (€ thousands) is given by p = 2t² - 4t + 6. Find the marginal profit when t = 1.', '0 € thousand/unit', '-4 € thousand/unit', 'Cannot determine', '4 € thousand/unit', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 4t + -4. At t = 1: rate = 4(1) + -4 = 0 € thousand/unit', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The height h (metres) is given by h = 2t² - 3t + 3. Find the velocity when t = 1.', '1 m/s', '2 m/s', '4 m/s', '-2 m/s', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dh/dt = 4t + -3. At t = 1: rate = 4(1) + -3 = 1 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance s (metres) is given by d = 2t² + 3t + 7. Find the velocity when t = 1.', '10 m/s', '12 m/s', '4 m/s', '7 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dd/dt = 4t + 3. At t = 1: rate = 4(1) + 3 = 7 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The population P (thousands) is given by p = 2t² + 2t + 4. Find the rate of growth when t = 2.', '12 thousand/year', '8 thousand/year', '10 thousand/year', '16 thousand/year', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 4t + 2. At t = 2: rate = 4(2) + 2 = 10 thousand/year', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The temperature T (°C) is given by t = 3t² - 4t + 4. Find the rate of cooling when t = 2.', '8 °C/min', '12 °C/min', '4 °C/min', 'Cannot determine', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dt/dt = 6t + -4. At t = 2: rate = 6(2) + -4 = 8 °C/min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The profit P (€ thousands) is given by p = 3t² + 3t + 2. Find the marginal profit when t = 2.', '20 € thousand/unit', '15 € thousand/unit', '18 € thousand/unit', '12 € thousand/unit', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 6t + 3. At t = 2: rate = 6(2) + 3 = 15 € thousand/unit', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The height h (metres) is given by h = t² + 2t + 3. Find the velocity when t = 2.', '8 m/s', '4 m/s', '11 m/s', '6 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dh/dt = 2t + 2. At t = 2: rate = 2(2) + 2 = 6 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The distance s (metres) is given by d = 3t² - 3t + 8. Find the velocity when t = 1.', '6 m/s', '0 m/s', '8 m/s', '3 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dd/dt = 6t + -3. At t = 1: rate = 6(1) + -3 = 3 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The population P (thousands) is given by p = t² - 4t + 5. Find the rate of growth when t = 1.', '2 thousand/year', '-2 thousand/year', '-6 thousand/year', 'Cannot determine', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 2t + -4. At t = 1: rate = 2(1) + -4 = -2 thousand/year', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The temperature T (°C) is given by t = 3t² - 2t + 3. Find the rate of cooling when t = 3.', '14 °C/min', '18 °C/min', '24 °C/min', '16 °C/min', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dt/dt = 6t + -2. At t = 3: rate = 6(3) + -2 = 16 °C/min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The profit P (€ thousands) is given by p = 3t² - t + 6. Find the marginal profit when t = 3.', '18 € thousand/unit', '30 € thousand/unit', '16 € thousand/unit', '17 € thousand/unit', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dp/dt = 6t + -1. At t = 3: rate = 6(3) + -1 = 17 € thousand/unit', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The height h (metres) is given by h = t² + 3t + 10. Find the velocity when t = 2.', '4 m/s', '20 m/s', '10 m/s', '7 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'dh/dt = 2t + 3. At t = 2: rate = 2(2) + 3 = 7 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the height h (in metres) of a ball is h = -1t² + 6t + 5, when is the velocity zero?', 't = 4 seconds', 't = 2 seconds', 't = 3 seconds', 't = 6 seconds', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = dh/dt = -2t + 6 = 0. Solving: 2t = 6, so t = 3 seconds', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the height h (in metres) of a ball is h = -1t² + 4t + 5, when is the velocity zero?', 't = 2 seconds', 't = 4 seconds', 'Cannot determine', 't = 3 seconds', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = dh/dt = -2t + 4 = 0. Solving: 2t = 4, so t = 2 seconds', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the height h (in metres) of a ball is h = -1t² + 4t + 5, when is the velocity zero?', 't = 3 seconds', 't = 2 seconds', 't = 4 seconds', 'Cannot determine', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = dh/dt = -2t + 4 = 0. Solving: 2t = 4, so t = 2 seconds', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the height h (in metres) of a ball is h = -2t² + 4t + 5, when is the velocity zero?', 't = 1 seconds', 't = 2 seconds', 'Cannot determine', 't = 4 seconds', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = dh/dt = -4t + 4 = 0. Solving: 4t = 4, so t = 1 seconds', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the height h (in metres) of a ball is h = -1t² + 2t + 5, when is the velocity zero?', 't = 2 seconds', 'Cannot determine', 'Cannot determine', 't = 1 seconds', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = dh/dt = -2t + 2 = 0. Solving: 2t = 2, so t = 1 seconds', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the height h (in metres) of a ball is h = -1t² + 2t + 5, when is the velocity zero?', 'Cannot determine', 'Cannot determine', 't = 2 seconds', 't = 1 seconds', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = dh/dt = -2t + 2 = 0. Solving: 2t = 2, so t = 1 seconds', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the height h (in metres) of a ball is h = -1t² + 6t + 5, when is the velocity zero?', 't = 6 seconds', 't = 2 seconds', 't = 4 seconds', 't = 3 seconds', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = dh/dt = -2t + 6 = 0. Solving: 2t = 6, so t = 3 seconds', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 3t² metres, find the velocity when t = 3 seconds.', '9 m/s', '18 m/s', '6 m/s', '27 m/s', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 6t. At t = 3: v = 18 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 4t² metres, find the velocity when t = 3 seconds.', '12 m/s', '8 m/s', '36 m/s', '24 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 8t. At t = 3: v = 24 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 4t² metres, find the velocity when t = 3 seconds.', '12 m/s', '36 m/s', '8 m/s', '24 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 8t. At t = 3: v = 24 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 3t² metres, find the velocity when t = 2 seconds.', 'Cannot determine', '12 m/s', '6 m/s', 'Cannot determine', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 6t. At t = 2: v = 12 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 3t² metres, find the velocity when t = 1 seconds.', 'Cannot determine', 'Cannot determine', '3 m/s', '6 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 6t. At t = 1: v = 6 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 5t² metres, find the velocity when t = 3 seconds.', '15 m/s', '45 m/s', '30 m/s', '10 m/s', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 10t. At t = 3: v = 30 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 3 seconds.', '18 m/s', '12 m/s', '4 m/s', '6 m/s', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 3: v = 12 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 4t² metres, find the velocity when t = 2 seconds.', 'Cannot determine', '16 m/s', 'Cannot determine', '8 m/s', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 8t. At t = 2: v = 16 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 4 seconds.', '32 m/s', '4 m/s', '8 m/s', '16 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 4: v = 16 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 5t² metres, find the velocity when t = 2 seconds.', 'Cannot determine', '10 m/s', 'Cannot determine', '20 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 10t. At t = 2: v = 20 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 4 seconds.', '4 m/s', '16 m/s', '8 m/s', '32 m/s', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 4: v = 16 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 4t² metres, find the velocity when t = 3 seconds.', '24 m/s', '36 m/s', '8 m/s', '12 m/s', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 8t. At t = 3: v = 24 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 3t² metres, find the velocity when t = 4 seconds.', '6 m/s', '12 m/s', '24 m/s', '48 m/s', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 6t. At t = 4: v = 24 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 5t² metres, find the velocity when t = 3 seconds.', '45 m/s', '15 m/s', '30 m/s', '10 m/s', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 10t. At t = 3: v = 30 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 5t² metres, find the velocity when t = 2 seconds.', '10 m/s', '20 m/s', 'Cannot determine', 'Cannot determine', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 10t. At t = 2: v = 20 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 3t² metres, find the velocity when t = 1 seconds.', '6 m/s', 'Cannot determine', 'Cannot determine', '3 m/s', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 6t. At t = 1: v = 6 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 4 seconds.', '32 m/s', '16 m/s', '8 m/s', '4 m/s', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 4: v = 16 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 3t² metres, find the velocity when t = 1 seconds.', '3 m/s', 'Cannot determine', '6 m/s', 'Cannot determine', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 6t. At t = 1: v = 6 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 4t² metres, find the velocity when t = 2 seconds.', '8 m/s', 'Cannot determine', 'Cannot determine', '16 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 8t. At t = 2: v = 16 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 4 seconds.', '8 m/s', '32 m/s', '16 m/s', '4 m/s', 2,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 4: v = 16 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 3 seconds.', '12 m/s', '4 m/s', '6 m/s', '18 m/s', 0,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 3: v = 12 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 2 seconds.', 'Cannot determine', '4 m/s', 'Cannot determine', '8 m/s', 3,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 2: v = 8 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If distance s = 2t² metres, find the velocity when t = 2 seconds.', 'Cannot determine', '8 m/s', '4 m/s', 'Cannot determine', 1,
'lc_ol_calculus', 6, 'developing', 'lc_ol', 'v = ds/dt = 4t. At t = 2: v = 8 m/s', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 6x increasing?', 'x < -3', 'x < 3', 'all x', 'x > 3', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 6. Function increases where f''(x) > 0: x < 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 6x increasing?', 'x < 3', 'x < -3', 'all x', 'x > 3', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 6. Function increases where f''(x) > 0: x < 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 2x increasing?', 'all x', 'x > 1', 'x < 1', 'x < -1', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 2. Function increases where f''(x) > 0: x < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = 2x² - 4x increasing?', 'x > -1', 'all x', 'x > 1', 'x < 1', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + -4. Function increases where f''(x) > 0: x > 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 4x increasing?', 'all x', 'x < 2', 'x > 2', 'x < -2', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 4. Function increases where f''(x) > 0: x < 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = 2x² - 4x increasing?', 'x > -1', 'all x', 'x > 1', 'x < 1', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + -4. Function increases where f''(x) > 0: x > 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -2x² + 4x increasing?', 'all x', 'x > 1', 'x < -1', 'x < 1', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -4x + 4. Function increases where f''(x) > 0: x < 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 6x increasing?', 'x > 3', 'x < 3', 'all x', 'x < -3', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 6. Function increases where f''(x) > 0: x < 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 6x increasing?', 'x > 3', 'x < 3', 'all x', 'x < -3', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 6. Function increases where f''(x) > 0: x < 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = 2x² - 4x increasing?', 'x > 1', 'all x', 'x > -1', 'x < 1', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + -4. Function increases where f''(x) > 0: x > 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 4x increasing?', 'x > 2', 'x < -2', 'all x', 'x < 2', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 4. Function increases where f''(x) > 0: x < 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = x² - 6x increasing?', 'x < 3', 'all x', 'x > -3', 'x > 3', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -6. Function increases where f''(x) > 0: x > 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = -x² + 4x increasing?', 'all x', 'x < -2', 'x < 2', 'x > 2', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = -2x + 4. Function increases where f''(x) > 0: x < 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = x² - 4x increasing?', 'x > 2', 'all x', 'x > -2', 'x < 2', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -4. Function increases where f''(x) > 0: x > 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = x² - 6x increasing?', 'x > -3', 'all x', 'x < 3', 'x > 3', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -6. Function increases where f''(x) > 0: x > 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = x² - 6x increasing?', 'x < 3', 'all x', 'x > 3', 'x > -3', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -6. Function increases where f''(x) > 0: x > 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = x² - 2x increasing?', 'all x', 'x > 1', 'x > -1', 'x < 1', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -2. Function increases where f''(x) > 0: x > 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = 2x² - 4x increasing?', 'all x', 'x > -1', 'x < 1', 'x > 1', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + -4. Function increases where f''(x) > 0: x > 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = x² - 2x increasing?', 'x > 1', 'x < 1', 'all x', 'x > -1', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -2. Function increases where f''(x) > 0: x > 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of x is f(x) = 2x² - 4x increasing?', 'x > 1', 'x < 1', 'all x', 'x > -1', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + -4. Function increases where f''(x) > 0: x > 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² + x increasing or decreasing at x = 1?', 'Decreasing (f''(1) = -3)', 'Increasing (f''(1) = 3 > 0)', 'Increasing (f''(1) = 3)', 'Cannot determine', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + 1. At x = 1: f''(1) = 3. Since 3 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² + x increasing or decreasing at x = 2?', 'Increasing (f''(2) = 5)', 'Decreasing (f''(2) = -5)', 'Increasing (f''(2) = 5 > 0)', 'Cannot determine', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + 1. At x = 2: f''(2) = 5. Since 5 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - 4x increasing or decreasing at x = 4?', 'Cannot determine', 'Increasing (f''(4) = 4 > 0)', 'Increasing (f''(4) = 4)', 'Decreasing (f''(4) = -4)', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -4. At x = 4: f''(4) = 4. Since 4 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 2x² + 2x increasing or decreasing at x = 4?', 'Decreasing (f''(4) = -18)', 'Cannot determine', 'Increasing (f''(4) = 18 > 0)', 'Increasing (f''(4) = 18)', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + 2. At x = 4: f''(4) = 18. Since 18 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - x increasing or decreasing at x = 1?', 'Increasing (f''(1) = 1)', 'Decreasing (f''(1) = -1)', 'Cannot determine', 'Increasing (f''(1) = 1 > 0)', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -1. At x = 1: f''(1) = 1. Since 1 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² + x increasing or decreasing at x = 1?', 'Increasing (f''(1) = 3)', 'Decreasing (f''(1) = -3)', 'Cannot determine', 'Increasing (f''(1) = 3 > 0)', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + 1. At x = 1: f''(1) = 3. Since 3 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² + 2x increasing or decreasing at x = 2?', 'Increasing (f''(2) = 6 > 0)', 'Decreasing (f''(2) = -6)', 'Increasing (f''(2) = 6)', 'Cannot determine', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + 2. At x = 2: f''(2) = 6. Since 6 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 2x² + 3x increasing or decreasing at x = 1?', 'Increasing (f''(1) = 7)', 'Increasing (f''(1) = 7 > 0)', 'Cannot determine', 'Decreasing (f''(1) = -7)', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + 3. At x = 1: f''(1) = 7. Since 7 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 2x² + 4x increasing or decreasing at x = 3?', 'Increasing (f''(3) = 16 > 0)', 'Cannot determine', 'Increasing (f''(3) = 16)', 'Decreasing (f''(3) = -16)', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + 4. At x = 3: f''(3) = 16. Since 16 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - 3x increasing or decreasing at x = 3?', 'Cannot determine', 'Increasing (f''(3) = 3)', 'Decreasing (f''(3) = -3)', 'Increasing (f''(3) = 3 > 0)', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -3. At x = 3: f''(3) = 3. Since 3 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² + 2x increasing or decreasing at x = 3?', 'Decreasing (f''(3) = -8)', 'Increasing (f''(3) = 8 > 0)', 'Cannot determine', 'Increasing (f''(3) = 8)', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + 2. At x = 3: f''(3) = 8. Since 8 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 2x² + 2x increasing or decreasing at x = 1?', 'Increasing (f''(1) = 6)', 'Decreasing (f''(1) = -6)', 'Cannot determine', 'Increasing (f''(1) = 6 > 0)', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + 2. At x = 1: f''(1) = 6. Since 6 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 2x² + 4x increasing or decreasing at x = 2?', 'Increasing (f''(2) = 12 > 0)', 'Cannot determine', 'Increasing (f''(2) = 12)', 'Decreasing (f''(2) = -12)', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + 4. At x = 2: f''(2) = 12. Since 12 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - 3x increasing or decreasing at x = 4?', 'Increasing (f''(4) = 5 > 0)', 'Cannot determine', 'Increasing (f''(4) = 5)', 'Decreasing (f''(4) = -5)', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -3. At x = 4: f''(4) = 5. Since 5 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 2x² + x increasing or decreasing at x = 3?', 'Increasing (f''(3) = 13 > 0)', 'Cannot determine', 'Increasing (f''(3) = 13)', 'Decreasing (f''(3) = -13)', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + 1. At x = 3: f''(3) = 13. Since 13 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - 3x increasing or decreasing at x = 1?', 'Decreasing (f''(1) = -1 < 0)', 'Decreasing (f''(1) = 1)', 'Cannot determine', 'Increasing (f''(1) = 1)', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -3. At x = 1: f''(1) = -1. Since -1 < 0, function is decreasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - 2x increasing or decreasing at x = 4?', 'Cannot determine', 'Increasing (f''(4) = 6)', 'Decreasing (f''(4) = -6)', 'Increasing (f''(4) = 6 > 0)', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -2. At x = 4: f''(4) = 6. Since 6 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - 3x increasing or decreasing at x = 1?', 'Increasing (f''(1) = 1)', 'Cannot determine', 'Decreasing (f''(1) = 1)', 'Decreasing (f''(1) = -1 < 0)', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -3. At x = 1: f''(1) = -1. Since -1 < 0, function is decreasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = 2x² - 4x increasing or decreasing at x = 3?', 'Decreasing (f''(3) = -8)', 'Increasing (f''(3) = 8)', 'Increasing (f''(3) = 8 > 0)', 'Cannot determine', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 4x + -4. At x = 3: f''(3) = 8. Since 8 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is f(x) = x² - x increasing or decreasing at x = 3?', 'Increasing (f''(3) = 5)', 'Increasing (f''(3) = 5 > 0)', 'Decreasing (f''(3) = -5)', 'Cannot determine', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'f''(x) = 2x + -1. At x = 3: f''(3) = 5. Since 5 > 0, function is increasing', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At point P where the curve is going upward (positive slope)?', 'f''(x) = f(x)', 'f''(x) > 0', 'f(x) = 0', 'f''(x) < 0', 1,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At point Q where the curve is going downward (negative slope)?', 'f(x) = 0', 'f''(x) = f(x)', 'f''(x) < 0', 'f''(x) > 0', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At a maximum point?', 'f''(x) > 0', 'f''(x) = f(x)', 'f(x) = 0', 'f''(x) = 0', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At a minimum point?', 'f''(x) = 0', 'f''(x) = f(x)', 'f''(x) < 0', 'f(x) = 0', 0,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative Where the tangent is horizontal?', 'f(x) = 0', 'f''(x) = 1', 'f''(x) = 0', 'f''(x) = f(x)', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At point P where the curve is going upward (positive slope)?', 'f''(x) < 0', 'f''(x) = f(x)', 'f''(x) > 0', 'f(x) = 0', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At point Q where the curve is going downward (negative slope)?', 'f''(x) = f(x)', 'f''(x) > 0', 'f''(x) < 0', 'f(x) = 0', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At a maximum point?', 'f(x) = 0', 'f''(x) = f(x)', 'f''(x) = 0', 'f''(x) > 0', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative At a minimum point?', 'f''(x) < 0', 'f''(x) = f(x)', 'f''(x) = 0', 'f(x) = 0', 2,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('On a graph of y = f(x), what is true about the derivative Where the tangent is horizontal?', 'f''(x) = 1', 'f''(x) = f(x)', 'f(x) = 0', 'f''(x) = 0', 3,
'lc_ol_calculus', 7, 'proficient', 'lc_ol', 'When curve goes up, f''(x) > 0. When down, f''(x) < 0. At turning points, f''(x) = 0.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = 2x² - 8x + 2 has a minimum.', 'x = -2', 'x = 2', 'x = 8', 'x = 3', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 4x + -8 = 0. Solving: x = --8/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -2x² + 8x + 1 has a maximum.', 'x = 8', 'x = -2', 'x = 3', 'x = 2', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -4x + 8 = 0. Solving: x = -8/-4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -x² + 8x + 6 has a maximum.', 'x = 4', 'x = 8', 'x = -4', 'x = 5', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 8 = 0. Solving: x = -8/-2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = x² - 2x + 1 has a minimum.', 'Cannot determine', 'x = 1', 'x = 2', 'x = -1', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + -2 = 0. Solving: x = --2/2 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -2x² + 4x + 8 has a maximum.', 'x = -1', 'x = 1', 'x = 4', 'x = 2', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -4x + 4 = 0. Solving: x = -4/-4 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = 2x² - 4x + 7 has a minimum.', 'x = 4', 'x = -1', 'x = 2', 'x = 1', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 4x + -4 = 0. Solving: x = --4/4 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -x² + 8x + 9 has a maximum.', 'x = 8', 'x = -4', 'x = 4', 'x = 5', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 8 = 0. Solving: x = -8/-2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -2x² + 8x + 2 has a maximum.', 'x = 8', 'x = 3', 'x = -2', 'x = 2', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -4x + 8 = 0. Solving: x = -8/-4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = x² - 6x has a minimum.', 'x = 3', 'x = -3', 'x = 4', 'x = 6', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + -6 = 0. Solving: x = --6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -x² + 8x + 10 has a maximum.', 'x = 4', 'x = 5', 'x = -4', 'x = 8', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 8 = 0. Solving: x = -8/-2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -x² + 4x + 9 has a maximum.', 'x = -2', 'x = 4', 'x = 2', 'x = 3', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 4 = 0. Solving: x = -4/-2 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -x² + 6x + 10 has a maximum.', 'x = -3', 'x = 3', 'x = 6', 'x = 4', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 6 = 0. Solving: x = -6/-2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = x² - 6x has a minimum.', 'x = 4', 'x = -3', 'x = 6', 'x = 3', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + -6 = 0. Solving: x = --6/2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = x² - 2x has a minimum.', 'x = 2', 'x = -1', 'x = 1', 'Cannot determine', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + -2 = 0. Solving: x = --2/2 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = x² - 2x + 1 has a minimum.', 'x = -1', 'x = 2', 'x = 1', 'Cannot determine', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + -2 = 0. Solving: x = --2/2 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -x² + 2x + 8 has a maximum.', 'Cannot determine', 'x = 2', 'x = 1', 'x = -1', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 2 = 0. Solving: x = -2/-2 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = x² - 2x + 6 has a minimum.', 'x = 1', 'x = 2', 'x = -1', 'Cannot determine', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + -2 = 0. Solving: x = --2/2 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = 2x² - 4x + 3 has a minimum.', 'x = 1', 'x = 2', 'x = 4', 'x = -1', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 4x + -4 = 0. Solving: x = --4/4 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -x² + 6x + 6 has a maximum.', 'x = 4', 'x = 6', 'x = 3', 'x = -3', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 6 = 0. Solving: x = -6/-2 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the x-value where f(x) = -2x² + 8x + 3 has a maximum.', 'x = 8', 'x = 2', 'x = -2', 'x = 3', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -4x + 8 = 0. Solving: x = -8/-4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 6x + 10.', '3', '18', '19', '10', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 6 = 0 gives x = 3. Maximum value = f(3) = 19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 6x + 3.', '3', '12', '11', 'Cannot determine', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 6 = 0 gives x = 3. Maximum value = f(3) = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 6x + 1.', '1', '-8', '-7', '-3', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 6 = 0 gives x = -3. Minimum value = f(-3) = -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 10x + 1.', '-23', '-5', '-24', '1', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 10 = 0 gives x = -5. Minimum value = f(-5) = -24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 12x + 9.', '44', '9', '6', '45', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 12 = 0 gives x = 6. Maximum value = f(6) = 45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 8x + 9.', '4', '9', '25', '24', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 8 = 0 gives x = 4. Maximum value = f(4) = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 8x + 2.', '-4', '2', '-14', '-13', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 8 = 0 gives x = -4. Minimum value = f(-4) = -14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 4x + 6.', '10', '2', '9', '6', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 4 = 0 gives x = 2. Maximum value = f(2) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 4x + 9.', '5', '6', '9', '-2', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 4 = 0 gives x = -2. Minimum value = f(-2) = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 10x + 7.', '-5', '-18', '-17', '7', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 10 = 0 gives x = -5. Minimum value = f(-5) = -18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 4x + 10.', '10', '14', '2', '13', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 4 = 0 gives x = 2. Maximum value = f(2) = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 8x + 7.', '7', '23', '22', '4', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 8 = 0 gives x = 4. Maximum value = f(4) = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 10x.', '-25', '0', '-24', '-5', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 10 = 0 gives x = -5. Minimum value = f(-5) = -25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 8x + 3.', '-12', '-4', '3', '-13', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 8 = 0 gives x = -4. Minimum value = f(-4) = -13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 4x + 6.', '3', '6', '-2', '2', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 4 = 0 gives x = -2. Minimum value = f(-2) = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 12x + 2.', '38', '6', '37', '2', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 12 = 0 gives x = 6. Maximum value = f(6) = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 12x + 2.', '6', '2', '37', '38', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 12 = 0 gives x = 6. Maximum value = f(6) = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 6x + 9.', '9', '1', '-3', '0', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 6 = 0 gives x = -3. Minimum value = f(-3) = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of f(x) = -x² + 8x + 5.', '21', '4', '20', '5', 0,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = -2x + 8 = 0 gives x = 4. Maximum value = f(4) = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of f(x) = x² + 6x + 1.', '-3', '-7', '-8', '1', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'f''(x) = 2x + 6 = 0 gives x = -3. Minimum value = f(-3) = -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = -x² + 7x + 5 have a maximum or minimum turning point?', 'Neither', 'Minimum (coefficient of x² is negative)', 'Maximum (coefficient of x² is negative)', 'Minimum (coefficient of x² is positive)', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a < 0, the parabola opens downward (maximum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = x² + 8x + 5 have a maximum or minimum turning point?', 'Maximum (coefficient of x² is negative)', 'Maximum (coefficient of x² is positive)', 'Neither', 'Minimum (coefficient of x² is positive)', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a > 0, the parabola opens upward (minimum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = x² + 4x + 5 have a maximum or minimum turning point?', 'Maximum (coefficient of x² is positive)', 'Minimum (coefficient of x² is positive)', 'Maximum (coefficient of x² is negative)', 'Neither', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a > 0, the parabola opens upward (minimum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = -2x² + 7x + 5 have a maximum or minimum turning point?', 'Minimum (coefficient of x² is positive)', 'Maximum (coefficient of x² is negative)', 'Neither', 'Minimum (coefficient of x² is negative)', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a < 0, the parabola opens downward (maximum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = -x² + 5x + 5 have a maximum or minimum turning point?', 'Minimum (coefficient of x² is positive)', 'Minimum (coefficient of x² is negative)', 'Neither', 'Maximum (coefficient of x² is negative)', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a < 0, the parabola opens downward (maximum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = 2x² + 6x + 5 have a maximum or minimum turning point?', 'Maximum (coefficient of x² is negative)', 'Maximum (coefficient of x² is positive)', 'Neither', 'Minimum (coefficient of x² is positive)', 3,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a > 0, the parabola opens upward (minimum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = -x² + 6x + 5 have a maximum or minimum turning point?', 'Neither', 'Minimum (coefficient of x² is positive)', 'Maximum (coefficient of x² is negative)', 'Minimum (coefficient of x² is negative)', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a < 0, the parabola opens downward (maximum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = 2x² + 2x + 5 have a maximum or minimum turning point?', 'Neither', 'Maximum (coefficient of x² is positive)', 'Minimum (coefficient of x² is positive)', 'Maximum (coefficient of x² is negative)', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a > 0, the parabola opens upward (minimum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = -x² + 7x + 5 have a maximum or minimum turning point?', 'Neither', 'Minimum (coefficient of x² is negative)', 'Maximum (coefficient of x² is negative)', 'Minimum (coefficient of x² is positive)', 2,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a < 0, the parabola opens downward (maximum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does f(x) = 2x² + 8x + 5 have a maximum or minimum turning point?', 'Maximum (coefficient of x² is positive)', 'Minimum (coefficient of x² is positive)', 'Maximum (coefficient of x² is negative)', 'Neither', 1,
'lc_ol_calculus', 8, 'proficient', 'lc_ol', 'When a > 0, the parabola opens upward (minimum)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ - 3x² + 3x, find f''''(x).', '6x + -3', '6x - 6', '1x + -6', '3x² + -6x', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + -6x + 3. f''''(x) = 6x + -6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ - 3x² + 5x, find f''''(x).', '6x + -3', '3x² + -6x', '1x + -6', '6x - 6', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + -6x + 5. f''''(x) = 6x + -6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ + x² + 5x, find f''''(x).', '1x + 2', '6x + 2', '6x + 1', '3x² + 2x', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + 2x + 5. f''''(x) = 6x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ + 6x² + x, find f''''(x).', '12x + 12', '6x² + 12x', '12x + 6', '2x + 12', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + 12x + 1. f''''(x) = 12x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x³ + x² + x, find f''''(x).', '18x + 2', '9x² + 2x', '18x + 1', '3x + 2', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 9x² + 2x + 1. f''''(x) = 18x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ + 2x² + 2x, find f''''(x).', '6x + 2', '1x + 4', '3x² + 4x', '6x + 4', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + 4x + 2. f''''(x) = 6x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ - 3x² + x, find f''''(x).', '6x² + -6x', '2x + -6', '12x + -3', '12x - 6', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + -6x + 1. f''''(x) = 12x + -6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ - 3x² + x, find f''''(x).', '3x² + -6x', '1x + -6', '6x + -3', '6x - 6', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + -6x + 1. f''''(x) = 6x + -6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ - 5x² + 3x, find f''''(x).', '12x - 10', '12x + -5', '2x + -10', '6x² + -10x', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + -10x + 3. f''''(x) = 12x + -10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ - 2x² + x, find f''''(x).', '6x² + -4x', '12x + -2', '2x + -4', '12x - 4', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + -4x + 1. f''''(x) = 12x + -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ + 4x² + 4x, find f''''(x).', '6x² + 8x', '2x + 8', '12x + 4', '12x + 8', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + 8x + 4. f''''(x) = 12x + 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ + 5x² + 3x, find f''''(x).', '2x + 10', '6x² + 10x', '12x + 10', '12x + 5', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + 10x + 3. f''''(x) = 12x + 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ - 3x² + 5x, find f''''(x).', '2x + -6', '12x + -3', '12x - 6', '6x² + -6x', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + -6x + 5. f''''(x) = 12x + -6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ + x² + 5x, find f''''(x).', '6x + 1', '1x + 2', '6x + 2', '3x² + 2x', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + 2x + 5. f''''(x) = 6x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ + 4x² + 5x, find f''''(x).', '12x + 8', '2x + 8', '12x + 4', '6x² + 8x', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + 8x + 5. f''''(x) = 12x + 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x³ - x² + 3x, find f''''(x).', '18x + -1', '9x² + -2x', '3x + -2', '18x - 2', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 9x² + -2x + 3. f''''(x) = 18x + -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ - 4x² + 4x, find f''''(x).', '2x + -8', '12x - 8', '12x + -4', '6x² + -8x', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + -8x + 4. f''''(x) = 12x + -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ + 6x² + 4x, find f''''(x).', '2x + 12', '12x + 12', '6x² + 12x', '12x + 6', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + 12x + 4. f''''(x) = 12x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x³ - 4x² + x, find f''''(x).', '18x + -4', '3x + -8', '18x - 8', '9x² + -8x', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 9x² + -8x + 1. f''''(x) = 18x + -8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 2x³ + 3x² + x, find f''''(x).', '2x + 6', '12x + 3', '12x + 6', '6x² + 6x', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 6x² + 6x + 1. f''''(x) = 12x + 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ + 2x² + 5x, find f''''(x).', '6x + 2', '3x² + 4x', '6x + 4', '1x + 4', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + 4x + 5. f''''(x) = 6x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ - 2x² + 3x, find f''''(x).', '6x - 4', '3x² + -4x', '6x + -2', '1x + -4', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + -4x + 3. f''''(x) = 6x + -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x³ - 2x² + x, find f''''(x).', '18x + -2', '9x² + -4x', '3x + -4', '18x - 4', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 9x² + -4x + 1. f''''(x) = 18x + -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = 3x³ + 6x² + 4x, find f''''(x).', '18x + 6', '3x + 12', '18x + 12', '9x² + 12x', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 9x² + 12x + 4. f''''(x) = 18x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If f(x) = x³ + 6x² + x, find f''''(x).', '6x + 6', '3x² + 12x', '6x + 12', '1x + 12', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''(x) = 3x² + 12x + 1. f''''(x) = 6x + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = 2x² + 7x + 5.', 'Minimum (f''''(x) = -4)', 'Maximum (f''''(x) = 4)', 'Point of inflection', 'Minimum (f''''(x) = 4 > 0)', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 4. Since f''''(x) > 0, turning point is a minimum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -2x² + 4x + 5.', 'Maximum (f''''(x) = -4 < 0)', 'Maximum (f''''(x) = 4)', 'Point of inflection', 'Minimum (f''''(x) = -4)', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -4. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = 2x² + 3x + 5.', 'Point of inflection', 'Minimum (f''''(x) = 4 > 0)', 'Minimum (f''''(x) = -4)', 'Maximum (f''''(x) = 4)', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 4. Since f''''(x) > 0, turning point is a minimum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = 2x² + 2x + 5.', 'Maximum (f''''(x) = 4)', 'Point of inflection', 'Minimum (f''''(x) = 4 > 0)', 'Minimum (f''''(x) = -4)', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 4. Since f''''(x) > 0, turning point is a minimum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = x² + 7x + 5.', 'Maximum (f''''(x) = 2)', 'Point of inflection', 'Minimum (f''''(x) = -2)', 'Minimum (f''''(x) = 2 > 0)', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 2. Since f''''(x) > 0, turning point is a minimum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -2x² + 6x + 5.', 'Maximum (f''''(x) = 4)', 'Point of inflection', 'Maximum (f''''(x) = -4 < 0)', 'Minimum (f''''(x) = -4)', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -4. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -2x² + 7x + 5.', 'Maximum (f''''(x) = 4)', 'Maximum (f''''(x) = -4 < 0)', 'Point of inflection', 'Minimum (f''''(x) = -4)', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -4. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = 2x² + 5x + 5.', 'Minimum (f''''(x) = -4)', 'Point of inflection', 'Minimum (f''''(x) = 4 > 0)', 'Maximum (f''''(x) = 4)', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 4. Since f''''(x) > 0, turning point is a minimum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = 2x² + 6x + 5.', 'Minimum (f''''(x) = 4 > 0)', 'Point of inflection', 'Minimum (f''''(x) = -4)', 'Maximum (f''''(x) = 4)', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 4. Since f''''(x) > 0, turning point is a minimum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -2x² + 5x + 5.', 'Maximum (f''''(x) = 4)', 'Point of inflection', 'Minimum (f''''(x) = -4)', 'Maximum (f''''(x) = -4 < 0)', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -4. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -x² + 6x + 5.', 'Maximum (f''''(x) = 2)', 'Maximum (f''''(x) = -2 < 0)', 'Point of inflection', 'Minimum (f''''(x) = -2)', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -2. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -x² + 4x + 5.', 'Point of inflection', 'Maximum (f''''(x) = -2 < 0)', 'Maximum (f''''(x) = 2)', 'Minimum (f''''(x) = -2)', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -2. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -2x² + 6x + 5.', 'Point of inflection', 'Maximum (f''''(x) = 4)', 'Minimum (f''''(x) = -4)', 'Maximum (f''''(x) = -4 < 0)', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -4. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = 2x² + 4x + 5.', 'Minimum (f''''(x) = -4)', 'Point of inflection', 'Maximum (f''''(x) = 4)', 'Minimum (f''''(x) = 4 > 0)', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 4. Since f''''(x) > 0, turning point is a minimum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the second derivative test to classify the turning point of f(x) = -x² + 6x + 5.', 'Maximum (f''''(x) = -2 < 0)', 'Maximum (f''''(x) = 2)', 'Point of inflection', 'Minimum (f''''(x) = -2)', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = -2. Since f''''(x) < 0, turning point is a maximum.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(3) for f(x) = 2x³ - 3x².', 'Cannot determine', '24', '30', '36', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 12x + -6. At x = 3: f''''(3) = 12(3) + -6 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(2) for f(x) = x³ + 3x².', '24', '18', 'Cannot determine', '12', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 6x + 6. At x = 2: f''''(2) = 6(2) + 6 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(2) for f(x) = 2x³ + 4x².', 'Cannot determine', '40', '32', '24', 2,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 12x + 8. At x = 2: f''''(2) = 12(2) + 8 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(1) for f(x) = x³ + 3x².', '12', '6', '9', '18', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 6x + 6. At x = 1: f''''(1) = 6(1) + 6 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(3) for f(x) = 2x³ - 4x².', '28', '30', '20', '36', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 12x + -8. At x = 3: f''''(3) = 12(3) + -8 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(2) for f(x) = x³ + 4x².', '20', 'Cannot determine', '28', '12', 0,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 6x + 8. At x = 2: f''''(2) = 6(2) + 8 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(2) for f(x) = 2x³ - 2x².', '16', '20', '24', 'Cannot determine', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 12x + -4. At x = 2: f''''(2) = 12(2) + -4 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(2) for f(x) = 2x³ - 4x².', 'Cannot determine', '16', '8', '24', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 12x + -8. At x = 2: f''''(2) = 12(2) + -8 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(1) for f(x) = 2x³ + 2x².', '12', '10', '20', '16', 3,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 12x + 4. At x = 1: f''''(1) = 12(1) + 4 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''''(3) for f(x) = 2x³ + x².', '40', '38', '60', '36', 1,
'lc_ol_calculus', 9, 'proficient', 'lc_ol', 'f''''(x) = 12x + 2. At x = 3: f''''(3) = 12(3) + 2 = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 21x - 62. How many units maximise profit?', '2 units', '10 units', '21 units', '11 units', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 21 = 0. Solving: x = 21/2 = 10 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 19x - 89. How many units maximise profit?', '6 units', '4 units', 'Cannot determine', '19 units', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 19 = 0. Solving: x = 19/4 = 4 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 30x - 66. How many units maximise profit?', '7 units', '30 units', '9 units', '4 units', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 30 = 0. Solving: x = 30/4 = 7 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 30x - 67. How many units maximise profit?', '4 units', '9 units', '7 units', '30 units', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 30 = 0. Solving: x = 30/4 = 7 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 17x - 77. How many units maximise profit?', '6 units', 'Cannot determine', '17 units', '4 units', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 17 = 0. Solving: x = 17/4 = 4 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 24x - 90. How many units maximise profit?', '4 units', '6 units', '24 units', '8 units', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 24 = 0. Solving: x = 24/4 = 6 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 30x - 80. How many units maximise profit?', '30 units', '16 units', '15 units', '2 units', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 30 = 0. Solving: x = 30/2 = 15 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 21x - 94. How many units maximise profit?', '10 units', '11 units', '2 units', '21 units', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 21 = 0. Solving: x = 21/2 = 10 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 26x - 75. How many units maximise profit?', '26 units', '6 units', '4 units', '8 units', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 26 = 0. Solving: x = 26/4 = 6 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 14x - 53. How many units maximise profit?', '2 units', '7 units', '14 units', '8 units', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 14 = 0. Solving: x = 14/2 = 7 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 10x - 58. How many units maximise profit?', '5 units', '6 units', '2 units', '10 units', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 10 = 0. Solving: x = 10/2 = 5 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 12x - 85. How many units maximise profit?', '4 units', '12 units', '5 units', '3 units', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 12 = 0. Solving: x = 12/4 = 3 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 29x - 71. How many units maximise profit?', '14 units', '2 units', '15 units', '29 units', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 29 = 0. Solving: x = 29/2 = 14 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 30x - 89. How many units maximise profit?', '30 units', '4 units', '9 units', '7 units', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 30 = 0. Solving: x = 30/4 = 7 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 20x - 81. How many units maximise profit?', '11 units', '20 units', '10 units', '2 units', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 20 = 0. Solving: x = 20/2 = 10 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 22x - 91. How many units maximise profit?', '22 units', '4 units', '5 units', '7 units', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 22 = 0. Solving: x = 22/4 = 5 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 25x - 65. How many units maximise profit?', '12 units', '2 units', '13 units', '25 units', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 25 = 0. Solving: x = 25/2 = 12 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 12x - 76. How many units maximise profit?', '3 units', '5 units', '12 units', '4 units', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 12 = 0. Solving: x = 12/4 = 3 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -2x² + 22x - 96. How many units maximise profit?', '5 units', '7 units', '4 units', '22 units', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -4x + 22 = 0. Solving: x = 22/4 = 5 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A company''s profit P (in €thousands) for producing x units is P(x) = -1x² + 17x - 85. How many units maximise profit?', '17 units', '8 units', '2 units', '9 units', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 17 = 0. Solving: x = 17/2 = 8 units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 12x - 12 (€thousands), find the maximum profit.', '€36,000', '€12,000', '€6,000', '€24,000', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 12 = 0 gives x = 6. Max profit = P(6) = -6² + 12(6) - 12 = €24,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 24x - 26 (€thousands), find the maximum profit.', '€12,000', '€118,000', '€24,000', '€144,000', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 24 = 0 gives x = 12. Max profit = P(12) = -12² + 24(12) - 26 = €118,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 22x - 29 (€thousands), find the maximum profit.', '€11,000', '€22,000', '€121,000', '€92,000', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 22 = 0 gives x = 11. Max profit = P(11) = -11² + 22(11) - 29 = €92,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 14x - 30 (€thousands), find the maximum profit.', '€14,000', '€19,000', '€7,000', '€49,000', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 14 = 0 gives x = 7. Max profit = P(7) = -7² + 14(7) - 30 = €19,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 22x - 18 (€thousands), find the maximum profit.', '€22,000', '€121,000', '€11,000', '€103,000', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 22 = 0 gives x = 11. Max profit = P(11) = -11² + 22(11) - 18 = €103,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 18x - 20 (€thousands), find the maximum profit.', '€18,000', '€9,000', '€61,000', '€81,000', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 18 = 0 gives x = 9. Max profit = P(9) = -9² + 18(9) - 20 = €61,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 24x - 13 (€thousands), find the maximum profit.', '€131,000', '€144,000', '€24,000', '€12,000', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 24 = 0 gives x = 12. Max profit = P(12) = -12² + 24(12) - 13 = €131,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 16x - 11 (€thousands), find the maximum profit.', '€53,000', '€16,000', '€8,000', '€64,000', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 16 = 0 gives x = 8. Max profit = P(8) = -8² + 16(8) - 11 = €53,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 14x - 13 (€thousands), find the maximum profit.', '€14,000', '€36,000', '€7,000', '€49,000', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 14 = 0 gives x = 7. Max profit = P(7) = -7² + 14(7) - 13 = €36,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 16x - 12 (€thousands), find the maximum profit.', '€16,000', '€8,000', '€52,000', '€64,000', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 16 = 0 gives x = 8. Max profit = P(8) = -8² + 16(8) - 12 = €52,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 24x - 30 (€thousands), find the maximum profit.', '€144,000', '€12,000', '€24,000', '€114,000', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 24 = 0 gives x = 12. Max profit = P(12) = -12² + 24(12) - 30 = €114,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 14x - 26 (€thousands), find the maximum profit.', '€7,000', '€49,000', '€23,000', '€14,000', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 14 = 0 gives x = 7. Max profit = P(7) = -7² + 14(7) - 26 = €23,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 20x - 21 (€thousands), find the maximum profit.', '€10,000', '€79,000', '€100,000', '€20,000', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 20 = 0 gives x = 10. Max profit = P(10) = -10² + 20(10) - 21 = €79,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 22x - 21 (€thousands), find the maximum profit.', '€22,000', '€100,000', '€11,000', '€121,000', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 22 = 0 gives x = 11. Max profit = P(11) = -11² + 22(11) - 21 = €100,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If profit P(x) = -x² + 18x - 23 (€thousands), find the maximum profit.', '€18,000', '€58,000', '€9,000', '€81,000', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'P''(x) = -2x + 18 = 0 gives x = 9. Max profit = P(9) = -9² + 18(9) - 23 = €58,000', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 2x² - 10x + 70 (€). Find x for minimum cost.', 'x = 4', 'x = 2', 'Cannot determine', 'x = 10', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 4x - 10 = 0. Solving: x = 10/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 2x² - 10x + 58 (€). Find x for minimum cost.', 'x = 4', 'x = 2', 'Cannot determine', 'x = 10', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 4x - 10 = 0. Solving: x = 10/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 10x + 52 (€). Find x for minimum cost.', 'x = 2', 'x = 7', 'x = 5', 'x = 10', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 10 = 0. Solving: x = 10/2 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 13x + 100 (€). Find x for minimum cost.', 'x = 6', 'x = 13', 'x = 2', 'x = 8', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 13 = 0. Solving: x = 13/2 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 10x + 58 (€). Find x for minimum cost.', 'x = 10', 'x = 7', 'x = 5', 'x = 2', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 10 = 0. Solving: x = 10/2 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 2x² - 9x + 65 (€). Find x for minimum cost.', 'x = 4', 'x = 9', 'x = 2', 'Cannot determine', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 4x - 9 = 0. Solving: x = 9/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 2x² - 15x + 60 (€). Find x for minimum cost.', 'x = 5', 'x = 4', 'x = 15', 'x = 3', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 4x - 15 = 0. Solving: x = 15/4 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 14x + 100 (€). Find x for minimum cost.', 'x = 14', 'x = 2', 'x = 9', 'x = 7', 3,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 14 = 0. Solving: x = 14/2 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 10x + 98 (€). Find x for minimum cost.', 'x = 10', 'x = 5', 'x = 2', 'x = 7', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 10 = 0. Solving: x = 10/2 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 12x + 73 (€). Find x for minimum cost.', 'x = 12', 'x = 6', 'x = 2', 'x = 8', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 12 = 0. Solving: x = 12/2 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 15x + 85 (€). Find x for minimum cost.', 'x = 7', 'x = 15', 'x = 9', 'x = 2', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 15 = 0. Solving: x = 15/2 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 2x² - 9x + 92 (€). Find x for minimum cost.', 'x = 9', 'x = 2', 'Cannot determine', 'x = 4', 1,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 4x - 9 = 0. Solving: x = 9/4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 12x + 61 (€). Find x for minimum cost.', 'x = 2', 'x = 8', 'x = 6', 'x = 12', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 12 = 0. Solving: x = 12/2 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 2x² - 14x + 88 (€). Find x for minimum cost.', 'x = 14', 'x = 4', 'x = 3', 'x = 5', 2,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 4x - 14 = 0. Solving: x = 14/4 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Production cost C(x) = 1x² - 9x + 54 (€). Find x for minimum cost.', 'x = 4', 'x = 6', 'x = 2', 'x = 9', 0,
'lc_ol_calculus', 10, 'advanced', 'lc_ol', 'C''(x) = 2x - 9 = 0. Solving: x = 9/2 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 56 cm. Find the length that maximises the area.', '28 cm', '56 cm', '14 cm', '19 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (56 - 2l)/2 = 28 - l. Area A = l(28 - l). dA/dl = 28 - 2l = 0 gives l = 14 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 62 cm. Find the length that maximises the area.', '62 cm', '15 cm', '31 cm', '20 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (62 - 2l)/2 = 31 - l. Area A = l(31 - l). dA/dl = 31 - 2l = 0 gives l = 15 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 82 cm. Find the length that maximises the area.', '82 cm', '20 cm', '41 cm', '25 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (82 - 2l)/2 = 41 - l. Area A = l(41 - l). dA/dl = 41 - 2l = 0 gives l = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 60 cm. Find the length that maximises the area.', '15 cm', '30 cm', '60 cm', '20 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (60 - 2l)/2 = 30 - l. Area A = l(30 - l). dA/dl = 30 - 2l = 0 gives l = 15 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 72 cm. Find the length that maximises the area.', '18 cm', '72 cm', '36 cm', '23 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (72 - 2l)/2 = 36 - l. Area A = l(36 - l). dA/dl = 36 - 2l = 0 gives l = 18 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 82 cm. Find the length that maximises the area.', '20 cm', '25 cm', '82 cm', '41 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (82 - 2l)/2 = 41 - l. Area A = l(41 - l). dA/dl = 41 - 2l = 0 gives l = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 46 cm. Find the length that maximises the area.', '46 cm', '11 cm', '23 cm', '16 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (46 - 2l)/2 = 23 - l. Area A = l(23 - l). dA/dl = 23 - 2l = 0 gives l = 11 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 64 cm. Find the length that maximises the area.', '64 cm', '32 cm', '16 cm', '21 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (64 - 2l)/2 = 32 - l. Area A = l(32 - l). dA/dl = 32 - 2l = 0 gives l = 16 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 80 cm. Find the length that maximises the area.', '80 cm', '25 cm', '40 cm', '20 cm', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (80 - 2l)/2 = 40 - l. Area A = l(40 - l). dA/dl = 40 - 2l = 0 gives l = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 80 cm. Find the length that maximises the area.', '40 cm', '25 cm', '20 cm', '80 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (80 - 2l)/2 = 40 - l. Area A = l(40 - l). dA/dl = 40 - 2l = 0 gives l = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 62 cm. Find the length that maximises the area.', '31 cm', '15 cm', '20 cm', '62 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (62 - 2l)/2 = 31 - l. Area A = l(31 - l). dA/dl = 31 - 2l = 0 gives l = 15 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 72 cm. Find the length that maximises the area.', '18 cm', '72 cm', '23 cm', '36 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (72 - 2l)/2 = 36 - l. Area A = l(36 - l). dA/dl = 36 - 2l = 0 gives l = 18 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 100 cm. Find the length that maximises the area.', '30 cm', '25 cm', '100 cm', '50 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (100 - 2l)/2 = 50 - l. Area A = l(50 - l). dA/dl = 50 - 2l = 0 gives l = 25 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 58 cm. Find the length that maximises the area.', '19 cm', '58 cm', '14 cm', '29 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (58 - 2l)/2 = 29 - l. Area A = l(29 - l). dA/dl = 29 - 2l = 0 gives l = 14 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 94 cm. Find the length that maximises the area.', '94 cm', '28 cm', '23 cm', '47 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (94 - 2l)/2 = 47 - l. Area A = l(47 - l). dA/dl = 47 - 2l = 0 gives l = 23 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 76 cm. Find the length that maximises the area.', '19 cm', '24 cm', '38 cm', '76 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (76 - 2l)/2 = 38 - l. Area A = l(38 - l). dA/dl = 38 - 2l = 0 gives l = 19 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 92 cm. Find the length that maximises the area.', '23 cm', '28 cm', '92 cm', '46 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (92 - 2l)/2 = 46 - l. Area A = l(46 - l). dA/dl = 46 - 2l = 0 gives l = 23 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 40 cm. Find the length that maximises the area.', '40 cm', '15 cm', '20 cm', '10 cm', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (40 - 2l)/2 = 20 - l. Area A = l(20 - l). dA/dl = 20 - 2l = 0 gives l = 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 46 cm. Find the length that maximises the area.', '11 cm', '23 cm', '16 cm', '46 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (46 - 2l)/2 = 23 - l. Area A = l(23 - l). dA/dl = 23 - 2l = 0 gives l = 11 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 46 cm. Find the length that maximises the area.', '46 cm', '11 cm', '16 cm', '23 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Let length = l. Width = (46 - 2l)/2 = 23 - l. Area A = l(23 - l). dA/dl = 23 - 2l = 0 gives l = 11 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 100 cm. What is the maximum possible area?', '650 cm²', '625 cm²', '2500 cm²', '50 cm²', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 100/4 = 25 cm. Area = 25² = 625 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 80 cm. What is the maximum possible area?', '1600 cm²', '420 cm²', '400 cm²', '40 cm²', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 80/4 = 20 cm. Area = 20² = 400 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 48 cm. What is the maximum possible area?', '24 cm²', '144 cm²', '576 cm²', '156 cm²', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 48/4 = 12 cm. Area = 12² = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 96 cm. What is the maximum possible area?', '2304 cm²', '600 cm²', '576 cm²', '48 cm²', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 96/4 = 24 cm. Area = 24² = 576 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 40 cm. What is the maximum possible area?', '100 cm²', '110 cm²', '400 cm²', '20 cm²', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 40/4 = 10 cm. Area = 10² = 100 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 60 cm. What is the maximum possible area?', '240 cm²', '900 cm²', '30 cm²', '225 cm²', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 60/4 = 15 cm. Area = 15² = 225 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 100 cm. What is the maximum possible area?', '650 cm²', '50 cm²', '625 cm²', '2500 cm²', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 100/4 = 25 cm. Area = 25² = 625 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 92 cm. What is the maximum possible area?', '529 cm²', '46 cm²', '552 cm²', '2116 cm²', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 92/4 = 23 cm. Area = 23² = 529 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 44 cm. What is the maximum possible area?', '132 cm²', '484 cm²', '22 cm²', '121 cm²', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 44/4 = 11 cm. Area = 11² = 121 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 72 cm. What is the maximum possible area?', '324 cm²', '342 cm²', '36 cm²', '1296 cm²', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 72/4 = 18 cm. Area = 18² = 324 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 80 cm. What is the maximum possible area?', '400 cm²', '1600 cm²', '420 cm²', '40 cm²', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 80/4 = 20 cm. Area = 20² = 400 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 48 cm. What is the maximum possible area?', '24 cm²', '144 cm²', '576 cm²', '156 cm²', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 48/4 = 12 cm. Area = 12² = 144 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 80 cm. What is the maximum possible area?', '420 cm²', '1600 cm²', '400 cm²', '40 cm²', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 80/4 = 20 cm. Area = 20² = 400 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 88 cm. What is the maximum possible area?', '506 cm²', '44 cm²', '1936 cm²', '484 cm²', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 88/4 = 22 cm. Area = 22² = 484 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangle has perimeter 40 cm. What is the maximum possible area?', '100 cm²', '110 cm²', '400 cm²', '20 cm²', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'Maximum area is a square with side 40/4 = 10 cm. Area = 10² = 100 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 18cm × 18cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '5 cm', '4 cm', '9 cm', '3 cm', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 18/6 = 3 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 30cm × 30cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '5 cm', '7 cm', 'Cannot determine', '15 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 30/6 = 5 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 30cm × 30cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '5 cm', '7 cm', '15 cm', 'Cannot determine', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 30/6 = 5 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 24cm × 24cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', 'Cannot determine', '6 cm', '12 cm', '4 cm', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 24/6 = 4 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 18cm × 18cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '3 cm', '5 cm', '9 cm', '4 cm', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 18/6 = 3 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 24cm × 24cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '12 cm', 'Cannot determine', '4 cm', '6 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 24/6 = 4 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 12cm × 12cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '6 cm', '4 cm', '3 cm', '2 cm', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 12/6 = 2 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 24cm × 24cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '4 cm', '6 cm', '12 cm', 'Cannot determine', 0,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 24/6 = 4 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 18cm × 18cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '5 cm', '3 cm', '4 cm', '9 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 18/6 = 3 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 24cm × 24cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '6 cm', '12 cm', '4 cm', 'Cannot determine', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 24/6 = 4 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 12cm × 12cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '6 cm', '3 cm', '2 cm', '4 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 12/6 = 2 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 18cm × 18cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '5 cm', '4 cm', '3 cm', '9 cm', 2,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 18/6 = 3 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 18cm × 18cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '4 cm', '3 cm', '5 cm', '9 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 18/6 = 3 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 30cm × 30cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '7 cm', '15 cm', 'Cannot determine', '5 cm', 3,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 30/6 = 5 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A box is made from a 18cm × 18cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?', '4 cm', '3 cm', '9 cm', '5 cm', 1,
'lc_ol_calculus', 11, 'advanced', 'lc_ol', 'For this box problem, the optimal cut size x = 18/6 = 3 cm gives maximum volume.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ + 2x at the point where x = 3.', '29', '27', '31', '33', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 3x² + 2. At x = 3: slope = 3(3)² + 2 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ + 3x at the point where x = 1.', '5', '6', '12', '9', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 6x² + 3. At x = 1: slope = 6(1)² + 3 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ - 3x at the point where x = 1.', '-1', '3', '0', '6', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 6x² + -3. At x = 1: slope = 6(1)² + -3 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ + 2x at the point where x = 1.', '7', '3', 'Cannot determine', '5', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 3x² + 2. At x = 1: slope = 3(1)² + 2 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ - 3x at the point where x = 3.', '54', '48', '51', '45', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 6x² + -3. At x = 3: slope = 6(3)² + -3 = 51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ + x at the point where x = 3.', '56', '55', '57', '54', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 6x² + 1. At x = 3: slope = 6(3)² + 1 = 55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ + 3x at the point where x = 3.', '33', '36', '30', '27', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 3x² + 3. At x = 3: slope = 3(3)² + 3 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ - 2x at the point where x = 2.', '24', '20', '12', '22', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 6x² + -2. At x = 2: slope = 6(2)² + -2 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = 2x³ + x at the point where x = 3.', '57', '55', '56', '54', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 6x² + 1. At x = 3: slope = 6(3)² + 1 = 55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to y = x³ - 3x at the point where x = 3.', '18', '27', '24', '21', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'dy/dx = 3x² + -3. At x = 3: slope = 3(3)² + -3 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P''(100) = 20, where profit P euros for x items sold. What does this mean?', 'The profit is constant', 'Cannot determine', 'Marginal profit is €20 per item when 100 sold', 'Maximum occurs at this point', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Marginal profit is €20 per item when 100 sold', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If s''(3) = 17, where distance s metres at time t seconds. What does this mean?', 'Cannot determine', 'The distance is constant', 'Maximum occurs at this point', 'Velocity is 17 m/s at t = 3', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Velocity is 17 m/s at t = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If T''(5) = -5, where temperature T°C at time t minutes. What does this mean?', 'Maximum occurs at this point', 'The temperature is constant', 'Temperature decreasing at 5°c/min at t = 5', 'Cannot determine', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Temperature decreasing at 5°c/min at t = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If h''(2) = 0, where height h metres at time t seconds. What does this mean?', 'Velocity is 0 at t = 2 (maximum height)', 'Cannot determine', 'The height is constant', 'Maximum occurs at this point', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Velocity is 0 at t = 2 (maximum height)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If h''(2) = 0, where height h metres at time t seconds. What does this mean?', 'Velocity is 0 at t = 2 (maximum height)', 'The height is constant', 'Maximum occurs at this point', 'Cannot determine', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Velocity is 0 at t = 2 (maximum height)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If s''(3) = 18, where distance s metres at time t seconds. What does this mean?', 'Maximum occurs at this point', 'Velocity is 18 m/s at t = 3', 'Cannot determine', 'The distance is constant', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Velocity is 18 m/s at t = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If T''(5) = -8, where temperature T°C at time t minutes. What does this mean?', 'Maximum occurs at this point', 'The temperature is constant', 'Temperature decreasing at 8°c/min at t = 5', 'Cannot determine', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Temperature decreasing at 8°c/min at t = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If T''(5) = -7, where temperature T°C at time t minutes. What does this mean?', 'The temperature is constant', 'Temperature decreasing at 7°c/min at t = 5', 'Cannot determine', 'Maximum occurs at this point', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Temperature decreasing at 7°c/min at t = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If T''(5) = -5, where temperature T°C at time t minutes. What does this mean?', 'Temperature decreasing at 5°c/min at t = 5', 'Cannot determine', 'The temperature is constant', 'Maximum occurs at this point', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Temperature decreasing at 5°c/min at t = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If s''(3) = 6, where distance s metres at time t seconds. What does this mean?', 'Maximum occurs at this point', 'Cannot determine', 'The distance is constant', 'Velocity is 6 m/s at t = 3', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'The derivative represents rate of change. Velocity is 6 m/s at t = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 16x. Find both the optimal x and maximum revenue.', 'x = 2, R = 65', 'x = 8, R = 128', 'x = 16, R = 256', 'x = 8, R = 64', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 16 = 0 gives x = 8. R(8) = -1(8)² + 16(8) = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 20x. Find both the optimal x and maximum revenue.', 'x = 20, R = 400', 'x = 10, R = 200', 'x = 2, R = 101', 'x = 10, R = 100', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 20 = 0 gives x = 10. R(10) = -1(10)² + 20(10) = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 11x. Find both the optimal x and maximum revenue.', 'x = 2, R = 31', 'x = 5, R = 55', 'x = 5, R = 30', 'x = 11, R = 121', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 11 = 0 gives x = 5. R(5) = -1(5)² + 11(5) = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 18x. Find both the optimal x and maximum revenue.', 'x = 9, R = 162', 'x = 2, R = 82', 'x = 9, R = 81', 'x = 18, R = 324', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 18 = 0 gives x = 9. R(9) = -1(9)² + 18(9) = 81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 14x. Find both the optimal x and maximum revenue.', 'x = 7, R = 49', 'x = 14, R = 196', 'x = 2, R = 50', 'x = 7, R = 98', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 14 = 0 gives x = 7. R(7) = -1(7)² + 14(7) = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 15x. Find both the optimal x and maximum revenue.', 'x = 2, R = 57', 'x = 7, R = 105', 'x = 7, R = 56', 'x = 15, R = 225', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 15 = 0 gives x = 7. R(7) = -1(7)² + 15(7) = 56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 16x. Find both the optimal x and maximum revenue.', 'x = 8, R = 128', 'x = 2, R = 65', 'x = 16, R = 256', 'x = 8, R = 64', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 16 = 0 gives x = 8. R(8) = -1(8)² + 16(8) = 64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 20x. Find both the optimal x and maximum revenue.', 'x = 20, R = 400', 'x = 10, R = 100', 'x = 10, R = 200', 'x = 2, R = 101', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 20 = 0 gives x = 10. R(10) = -1(10)² + 20(10) = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -2x² + 20x. Find both the optimal x and maximum revenue.', 'x = 5, R = 50', 'x = 5, R = 100', 'x = 4, R = 52', 'x = 20, R = 400', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -4x + 20 = 0 gives x = 5. R(5) = -2(5)² + 20(5) = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -2x² + 12x. Find both the optimal x and maximum revenue.', 'x = 3, R = 18', 'x = 12, R = 144', 'x = 3, R = 36', 'x = 4, R = 20', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -4x + 12 = 0 gives x = 3. R(3) = -2(3)² + 12(3) = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -2x² + 14x. Find both the optimal x and maximum revenue.', 'x = 3, R = 42', 'x = 4, R = 26', 'x = 3, R = 24', 'x = 14, R = 196', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -4x + 14 = 0 gives x = 3. R(3) = -2(3)² + 14(3) = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -2x² + 17x. Find both the optimal x and maximum revenue.', 'x = 4, R = 68', 'x = 17, R = 289', 'x = 4, R = 36', 'x = 4, R = 38', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -4x + 17 = 0 gives x = 4. R(4) = -2(4)² + 17(4) = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -1x² + 11x. Find both the optimal x and maximum revenue.', 'x = 11, R = 121', 'x = 5, R = 55', 'x = 5, R = 30', 'x = 2, R = 31', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -2x + 11 = 0 gives x = 5. R(5) = -1(5)² + 11(5) = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -2x² + 19x. Find both the optimal x and maximum revenue.', 'x = 19, R = 361', 'x = 4, R = 44', 'x = 4, R = 76', 'x = 4, R = 46', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -4x + 19 = 0 gives x = 4. R(4) = -2(4)² + 19(4) = 44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Revenue R(x) = -2x² + 17x. Find both the optimal x and maximum revenue.', 'x = 17, R = 289', 'x = 4, R = 38', 'x = 4, R = 36', 'x = 4, R = 68', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'R''(x) = -4x + 17 = 0 gives x = 4. R(4) = -2(4)² + 17(4) = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = x³ + 3x² - 2x + 8.', 'x² + 3x - 2', '3x² + 6x', '3x³ + 6x² - 2x', '3x² + 6x - 2', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 3x² + 6x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ - 2x² + 3x + 2.', '6x² - 4x', '2x² - 2x + 3', '6x² - 4x + 3', '6x³ - 4x² + 3x', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² - 4x + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ + 3x² - 2x + 2.', '6x² + 6x - 2', '6x³ + 6x² - 2x', '2x² + 3x - 2', '6x² + 6x', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² + 6x - 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = x³ - 2x² + 4x + 5.', '3x³ - 4x² + 4x', 'x² - 2x + 4', '3x² - 4x + 4', '3x² - 4x', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 3x² - 4x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ + 3x² + 5x + 4.', '6x² + 6x + 5', '6x² + 6x', '6x³ + 6x² + 5x', '2x² + 3x + 5', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² + 6x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = x³ - x² - 5x + 2.', 'x² - x - 5', '3x² - 2x', '3x³ - 2x² - 5x', '3x² - 2x - 5', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 3x² - 2x - 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ + 2x² + 2x + 10.', '6x² + 4x', '6x³ + 4x² + 2x', '2x² + 2x + 2', '6x² + 4x + 2', 3,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² + 4x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = x³ - x² + 3x + 1.', '3x³ - 2x² + 3x', '3x² - 2x + 3', 'x² - x + 3', '3x² - 2x', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 3x² - 2x + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = x³ - 2x² + 5x + 4.', '3x² - 4x + 5', '3x³ - 4x² + 5x', '3x² - 4x', 'x² - 2x + 5', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 3x² - 4x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ - 2x² + 5x + 1.', '6x³ - 4x² + 5x', '6x² - 4x + 5', '6x² - 4x', '2x² - 2x + 5', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² - 4x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ - x² + 5x + 1.', '2x² - x + 5', '6x² - 2x + 5', '6x³ - 2x² + 5x', '6x² - 2x', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² - 2x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = x³ + 3x² + 2x + 9.', '3x² + 6x', '3x³ + 6x² + 2x', '3x² + 6x + 2', 'x² + 3x + 2', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 3x² + 6x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ + x² + 2x + 10.', '6x³ + 2x² + 2x', '6x² + 2x + 2', '2x² + x + 2', '6x² + 2x', 1,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² + 2x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = x³ - 3x² + 2x + 1.', '3x³ - 6x² + 2x', 'x² - 3x + 2', '3x² - 6x + 2', '3x² - 6x', 2,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 3x² - 6x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find f''(x) for f(x) = 2x³ + x² - x + 9.', '6x² + 2x - 1', '6x³ + 2x² - x', '6x² + 2x', '2x² + x - 1', 0,
'lc_ol_calculus', 12, 'advanced', 'lc_ol', 'Apply power rule to each term: f''(x) = 6x² + 2x - 1', 1);

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_calculus';
