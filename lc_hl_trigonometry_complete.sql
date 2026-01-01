-- LC Higher Level - Trigonometry - Complete SQL
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_trigonometry_complete.sql
-- Generated: 2025-12-15

-- Add Trigonometry topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_trigonometry', 'Trigonometry', id, '📐', 12, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_trigonometry';

-- Questions (600 total, 50 per level x 12 levels)

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'adjacent/hypotenuse', 'opposite/hypotenuse', 'hypotenuse/opposite', 'opposite/adjacent', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 12 and the hypotenuse is 13. Find cos θ.', '12/13', '12/5', '13/12', '5/13', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 12/13 = 12/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, tan θ equals:', 'adjacent/hypotenuse', 'opposite/hypotenuse', 'opposite/adjacent', 'adjacent/opposite', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, cos θ equals:', 'opposite/hypotenuse', 'adjacent/hypotenuse', 'hypotenuse/adjacent', 'opposite/adjacent', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'adjacent/hypotenuse', 'opposite/hypotenuse', 'hypotenuse/opposite', 'opposite/adjacent', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = 8/17 and the hypotenuse is 17, find the opposite side.', '17', '9', '8', '15', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opp/hyp, so opp = sin θ × hyp = (8/17) × 17 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If tan θ = 3/4 and the adjacent side is 4, find the opposite side.', '5', '3', 'None of these', '4', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opp/adj, so opp = tan θ × adj = (3/4) × 4 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'opposite/adjacent', 'adjacent/hypotenuse', 'opposite/hypotenuse', 'hypotenuse/opposite', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'adjacent/hypotenuse', 'hypotenuse/opposite', 'opposite/adjacent', 'opposite/hypotenuse', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 24/25 and the hypotenuse is 25, find the adjacent side.', '24', '25', 'None of these', '7', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adj/hyp, so adj = cos θ × hyp = (24/25) × 25 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 5 and the hypotenuse is 13. Find sin θ.', '5/13', '13/5', '12/13', '5/12', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 5/13 = 5/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'adjacent/hypotenuse', 'opposite/hypotenuse', 'opposite/adjacent', 'hypotenuse/opposite', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 12 and the hypotenuse is 13. Find cos θ.', '12/13', '13/12', '5/13', '12/5', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 12/13 = 12/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, cos θ equals:', 'opposite/hypotenuse', 'adjacent/hypotenuse', 'hypotenuse/adjacent', 'opposite/adjacent', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If tan θ = 3/4 and the adjacent side is 4, find the opposite side.', '5', '3', 'None of these', '4', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opp/adj, so opp = tan θ × adj = (3/4) × 4 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If tan θ = 8/15 and the adjacent side is 15, find the opposite side.', '9', '17', '15', '8', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opp/adj, so opp = tan θ × adj = (8/15) × 15 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 4 and the hypotenuse is 5. Find cos θ.', '3/5', '4/3', '4/5', '5/4', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 4/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 7 and the adjacent side is 24. Find tan θ.', '24/25', '7/25', '7/24', '24/7', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent = 7/24 = 7/24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 7 and the hypotenuse is 25. Find sin θ.', '7/24', '25/7', '7/25', '24/25', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 7/25 = 7/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 5 and the hypotenuse is 13. Find sin θ.', '13/5', '5/13', '5/12', '12/13', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 5/13 = 5/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, tan θ equals:', 'opposite/adjacent', 'opposite/hypotenuse', 'adjacent/hypotenuse', 'adjacent/opposite', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 24 and the hypotenuse is 25. Find cos θ.', '24/7', '25/24', '24/25', '7/25', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 24/25 = 24/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 3 and the adjacent side is 4. Find tan θ.', '3/5', '3/4', '4/3', '4/5', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent = 3/4 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 4 and the hypotenuse is 5. Find cos θ.', '4/5', '5/4', '4/3', '3/5', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 4/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 15 and the hypotenuse is 17. Find cos θ.', '17/15', '15/17', '15/8', '8/17', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 15/17 = 15/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 5 and the hypotenuse is 13. Find sin θ.', '12/13', '5/13', '13/5', '5/12', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 5/13 = 5/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 8 and the hypotenuse is 17. Find sin θ.', '8/15', '15/17', '8/17', '17/8', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 8/17 = 8/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'opposite/adjacent', 'hypotenuse/opposite', 'adjacent/hypotenuse', 'opposite/hypotenuse', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 12/13 and the hypotenuse is 13, find the adjacent side.', '5', '13', '12', 'None of these', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adj/hyp, so adj = cos θ × hyp = (12/13) × 13 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, tan θ equals:', 'adjacent/opposite', 'opposite/adjacent', 'adjacent/hypotenuse', 'opposite/hypotenuse', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 8 and the adjacent side is 15. Find tan θ.', '8/15', '8/17', '15/8', '15/17', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent = 8/15 = 8/15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 5 and the adjacent side is 12. Find tan θ.', '5/13', '5/12', '12/5', '12/13', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent = 5/12 = 5/12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 3 and the hypotenuse is 5. Find sin θ.', '3/5', '3/4', '4/5', '5/3', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 3/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 15 and the hypotenuse is 17. Find cos θ.', '17/15', '15/8', '8/17', '15/17', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 15/17 = 15/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If tan θ = 5/12 and the adjacent side is 12, find the opposite side.', '6', '13', '5', '12', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opp/adj, so opp = tan θ × adj = (5/12) × 12 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = 7/25 and the hypotenuse is 25, find the opposite side.', '25', '8', '7', '24', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opp/hyp, so opp = sin θ × hyp = (7/25) × 25 = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 15 and the hypotenuse is 17. Find cos θ.', '8/17', '15/8', '17/15', '15/17', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 15/17 = 15/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 5 and the hypotenuse is 13. Find sin θ.', '13/5', '5/13', '12/13', '5/12', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 5/13 = 5/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 3 and the adjacent side is 4. Find tan θ.', '4/5', '3/5', '3/4', '4/3', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opposite/adjacent = 3/4 = 3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 4 and the hypotenuse is 5. Find cos θ.', '3/5', '5/4', '4/5', '4/3', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 4/5 = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 3 and the hypotenuse is 5. Find sin θ.', '3/4', '4/5', '5/3', '3/5', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 3/5 = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side opposite angle θ is 5 and the hypotenuse is 13. Find sin θ.', '5/12', '12/13', '5/13', '13/5', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse = 5/13 = 5/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'adjacent/hypotenuse', 'opposite/adjacent', 'opposite/hypotenuse', 'hypotenuse/opposite', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, cos θ equals:', 'opposite/hypotenuse', 'opposite/adjacent', 'adjacent/hypotenuse', 'hypotenuse/adjacent', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, sin θ equals:', 'adjacent/hypotenuse', 'opposite/adjacent', 'hypotenuse/opposite', 'opposite/hypotenuse', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'sin θ = opposite/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, cos θ equals:', 'opposite/adjacent', 'adjacent/hypotenuse', 'hypotenuse/adjacent', 'opposite/hypotenuse', 1,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, cos θ equals:', 'opposite/adjacent', 'opposite/hypotenuse', 'hypotenuse/adjacent', 'adjacent/hypotenuse', 3,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, the side adjacent to angle θ is 15 and the hypotenuse is 17. Find cos θ.', '15/17', '15/8', '17/15', '8/17', 0,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adjacent/hypotenuse = 15/17 = 15/17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 15/17 and the hypotenuse is 17, find the adjacent side.', '17', '16', '15', '8', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'cos θ = adj/hyp, so adj = cos θ × hyp = (15/17) × 17 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If tan θ = 3/4 and the adjacent side is 4, find the opposite side.', '5', 'None of these', '3', '4', 2,
'lc_hl_trigonometry', 1, 'foundation', 'lc_hl', 'tan θ = opp/adj, so opp = tan θ × adj = (3/4) × 4 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = √2/2, find θ (where 0° ≤ θ ≤ 90°).', '60°', '90°', '45°', '30°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos θ = √2/2, so θ = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sin 45°?', '√2/2', '1/2', '√3/2', '1', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 45° = √2/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is tan 30°?', '√3', '√3/3', '1', '0', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'tan 30° = √3/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin 30° / cos 30°', '1/2', '√3/2', '√3/3', '1', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 30° / cos 30° = √3/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: sin 30° compared to sin 45°?', 'sin 30° < sin 45°', 'sin 30° = sin 45°', 'Cannot be determined', 'sin 30° > sin 45°', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 30° = 1/2, sin 45° = √2/2. So sin 30° < sin 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = √2/2, find θ (where 0° ≤ θ ≤ 90°).', '45°', '90°', '60°', '30°', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin θ = √2/2, so θ = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is cos 0°?', '√2/2', '1', '√3/2', '1/2', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 0° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²45° + cos²45°', '0', '1', '1/2', '2', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²45° + cos²45° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = √2/2, find θ (where 0° ≤ θ ≤ 90°).', '60°', '90°', '45°', '30°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin θ = √2/2, so θ = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sin 30°?', '√3/2', '√2/2', '1/2', '1', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 30° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 1/2, find θ (where 0° ≤ θ ≤ 90°).', '30°', '90°', '60°', '45°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos θ = 1/2, so θ = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²60° + cos²60°', '0', '1', '2', '1/2', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²60° + cos²60° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin 60° / cos 60°', '1', '√3', '√3/2', '1/2', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 60° / cos 60° = √3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 60° compared to cos 30°?', 'cos 60° > cos 30°', 'Cannot be determined', 'cos 60° = cos 30°', 'cos 60° < cos 30°', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 60° = 1/2, cos 30° = √3/2. So cos 60° < cos 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²60° + cos²60°', '2', '1/2', '1', '0', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²60° + cos²60° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin 45° / cos 45°', '1', '√3/2', '1/2', 'None of these', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 45° / cos 45° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: sin 60° compared to sin 30°?', 'sin 60° < sin 30°', 'Cannot be determined', 'sin 60° > sin 30°', 'sin 60° = sin 30°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 60° = √3/2, sin 30° = 1/2. So sin 60° > sin 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin 30° / cos 30°', '1/2', '√3/2', '√3/3', '1', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 30° / cos 30° = √3/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 30° compared to cos 45°?', 'cos 30° > cos 45°', 'Cannot be determined', 'cos 30° < cos 45°', 'cos 30° = cos 45°', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 30° = √3/2, cos 45° = √2/2. So cos 30° > cos 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: sin 45° compared to sin 60°?', 'sin 45° = sin 60°', 'Cannot be determined', 'sin 45° < sin 60°', 'sin 45° > sin 60°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 45° = √2/2, sin 60° = √3/2. So sin 45° < sin 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²45° + cos²45°', '1/2', '2', '1', '0', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²45° + cos²45° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 60° compared to cos 45°?', 'cos 60° < cos 45°', 'cos 60° = cos 45°', 'Cannot be determined', 'cos 60° > cos 45°', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 60° = 1/2, cos 45° = √2/2. So cos 60° < cos 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 45° compared to cos 30°?', 'Cannot be determined', 'cos 45° < cos 30°', 'cos 45° = cos 30°', 'cos 45° > cos 30°', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 45° = √2/2, cos 30° = √3/2. So cos 45° < cos 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is cos 60°?', '1/2', '√2/2', '0', '√3/2', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 45° compared to cos 30°?', 'Cannot be determined', 'cos 45° > cos 30°', 'cos 45° = cos 30°', 'cos 45° < cos 30°', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 45° = √2/2, cos 30° = √3/2. So cos 45° < cos 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is cos 90°?', '0', '1', '1/2', '√3/2', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 90° = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 60° compared to cos 30°?', 'cos 60° = cos 30°', 'Cannot be determined', 'cos 60° < cos 30°', 'cos 60° > cos 30°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 60° = 1/2, cos 30° = √3/2. So cos 60° < cos 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 1/2, find θ (where 0° ≤ θ ≤ 90°).', '45°', '30°', '90°', '60°', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos θ = 1/2, so θ = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 60° compared to cos 30°?', 'cos 60° > cos 30°', 'Cannot be determined', 'cos 60° = cos 30°', 'cos 60° < cos 30°', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 60° = 1/2, cos 30° = √3/2. So cos 60° < cos 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 30° compared to cos 60°?', 'Cannot be determined', 'cos 30° < cos 60°', 'cos 30° > cos 60°', 'cos 30° = cos 60°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 30° = √3/2, cos 60° = 1/2. So cos 30° > cos 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is cos 90°?', '1', '0', '√2/2', '1/2', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 90° = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = √2/2, find θ (where 0° ≤ θ ≤ 90°).', '60°', '30°', '90°', '45°', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin θ = √2/2, so θ = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²60° + cos²60°', '2', '0', '1/2', '1', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²60° + cos²60° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin 30° / cos 30°', '1/2', '√3/3', '√3/2', '1', 1,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 30° / cos 30° = √3/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is tan 30°?', '1', '0', '√3/3', '√3', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'tan 30° = √3/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²30° + cos²30°', '0', '2', '1/2', '1', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²30° + cos²30° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is cos 30°?', '1', '0', '1/2', '√3/2', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 30° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin 45° / cos 45°', 'None of these', '√3/2', '1', '1/2', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 45° / cos 45° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is sin 60°?', '√2/2', '0', '1/2', '√3/2', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²30° + cos²30°', '0', '2', '1', '1/2', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²30° + cos²30° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 60° compared to cos 30°?', 'cos 60° > cos 30°', 'Cannot be determined', 'cos 60° < cos 30°', 'cos 60° = cos 30°', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 60° = 1/2, cos 30° = √3/2. So cos 60° < cos 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = √2/2, find θ (where 0° ≤ θ ≤ 90°).', '30°', '60°', '90°', '45°', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin θ = √2/2, so θ = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²45° + cos²45°', '1', '2', '1/2', '0', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²45° + cos²45° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²30° + cos²30°', '1/2', '0', '1', '2', 2,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²30° + cos²30° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is cos 0°?', '1', '√2/2', '√3/2', '1/2', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 0° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²30° + cos²30°', '0', '1/2', '2', '1', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²30° + cos²30° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = √3/2, find θ (where 0° ≤ θ ≤ 90°).', '30°', '90°', '60°', '45°', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos θ = √3/2, so θ = 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: sin²45° + cos²45°', '1', '2', '1/2', '0', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'sin²45° + cos²45° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = √3/2, find θ (where 0° ≤ θ ≤ 90°).', '30°', '45°', '60°', '90°', 0,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos θ = √3/2, so θ = 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is true: cos 60° compared to cos 45°?', 'cos 60° > cos 45°', 'cos 60° = cos 45°', 'Cannot be determined', 'cos 60° < cos 45°', 3,
'lc_hl_trigonometry', 2, 'foundation', 'lc_hl', 'cos 60° = 1/2, cos 45° = √2/2. So cos 60° < cos 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate tan 225°.', '√3/2', '-1/2', '1/2', '1', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 45°. In Q3, tan 225° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reference angle for 300°.', '30°', '120°', '60°', '70°', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', '300° is in Quadrant 4. Reference angle = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 315°.', '√3/2', '-1/2', '√2/2', '1/2', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 45°. In Q4, cos 315° = √2/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 315°.', '1/2', '√2/2', '√3/2', '-1/2', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 45°. In Q4, cos 315° = √2/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 3, sin θ is:', 'Undefined', 'Negative', 'Zero', 'Positive', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q3, sin θ is negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ > 0 and cos θ < 0, in which quadrant does θ lie?', 'Quadrant 2', 'Quadrant 4', 'Quadrant 1', 'Quadrant 3', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ > 0 and cos θ < 0, θ is in Quadrant 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reference angle for 135°.', '45°', '55°', 'None of these', '135°', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', '135° is in Quadrant 2. Reference angle = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 4, cos θ is:', 'Undefined', 'Positive', 'Negative', 'Zero', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q4, cos θ is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 150°.', '-√3/2', '1/2', '-1/2', '√3/2', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 30°. In Q2, sin 150° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 1, cos θ is:', 'Positive', 'Undefined', 'Zero', 'Negative', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q1, cos θ is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 120°.', '-√3/2', '1/2', '√3/2', '-1/2', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 60°. In Q2, cos 120° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 180°?', '(0, -1)', '(0, 1)', '(1, 0)', '(-1, 0)', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 180°, the coordinates (cos θ, sin θ) = (-1, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 0°?', '(0, -1)', '(0, 1)', '(-1, 0)', '(1, 0)', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 0°, the coordinates (cos θ, sin θ) = (1, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate tan 225°.', '1/2', '1', '√3/2', '-1/2', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 45°. In Q3, tan 225° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 0°?', '(-1, 0)', '(0, -1)', '(0, 1)', '(1, 0)', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 0°, the coordinates (cos θ, sin θ) = (1, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 330°.', '1/2', '-√3/2', '-1/2', '√3/2', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 30°. In Q4, sin 330° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ < 0 and cos θ > 0, in which quadrant does θ lie?', 'Quadrant 2', 'Quadrant 1', 'Quadrant 4', 'Quadrant 3', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ < 0 and cos θ > 0, θ is in Quadrant 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 240°.', '-1/2', '-√3/2', '1/2', '√3/2', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 60°. In Q3, cos 240° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reference angle for 135°.', 'None of these', '45°', '135°', '55°', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', '135° is in Quadrant 2. Reference angle = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 45°?', '(1, 0)', '(√2/2, √2/2)', '(0, 1)', '(-1, 0)', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 45°, the coordinates (cos θ, sin θ) = (√2/2, √2/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ > 0 and cos θ > 0, in which quadrant does θ lie?', 'Quadrant 4', 'Quadrant 3', 'Quadrant 1', 'Quadrant 2', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ > 0 and cos θ > 0, θ is in Quadrant 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ < 0 and cos θ > 0, in which quadrant does θ lie?', 'Quadrant 1', 'Quadrant 3', 'Quadrant 4', 'Quadrant 2', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ < 0 and cos θ > 0, θ is in Quadrant 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 240°.', '-√3/2', '√3/2', '-1/2', '1/2', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 60°. In Q3, cos 240° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 330°.', '-1/2', '-√3/2', '1/2', '√3/2', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 30°. In Q4, sin 330° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 45°?', '(1, 0)', '(√2/2, √2/2)', '(-1, 0)', '(0, 1)', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 45°, the coordinates (cos θ, sin θ) = (√2/2, √2/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 0°?', '(-1, 0)', '(0, -1)', '(1, 0)', '(0, 1)', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 0°, the coordinates (cos θ, sin θ) = (1, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ > 0 and cos θ < 0, in which quadrant does θ lie?', 'Quadrant 3', 'Quadrant 2', 'Quadrant 4', 'Quadrant 1', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ > 0 and cos θ < 0, θ is in Quadrant 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ > 0 and cos θ > 0, in which quadrant does θ lie?', 'Quadrant 1', 'Quadrant 3', 'Quadrant 2', 'Quadrant 4', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ > 0 and cos θ > 0, θ is in Quadrant 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 2, sin θ is:', 'Zero', 'Undefined', 'Positive', 'Negative', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q2, sin θ is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 180°?', '(1, 0)', '(0, -1)', '(-1, 0)', '(0, 1)', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 180°, the coordinates (cos θ, sin θ) = (-1, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 120°.', '1/2', '-1/2', '√3/2', '-√3/2', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 60°. In Q2, cos 120° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 240°.', '1/2', '-√3/2', '√3/2', '-1/2', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 60°. In Q3, cos 240° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What are the coordinates of the point on the unit circle at 135°?', '(1, 0)', '(-1, 0)', '(-√2/2, √2/2)', '(0, 1)', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'At 135°, the coordinates (cos θ, sin θ) = (-√2/2, √2/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 150°.', '√3/2', '-√3/2', '1/2', '-1/2', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 30°. In Q2, sin 150° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reference angle for 210°.', '30°', '150°', '40°', '60°', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', '210° is in Quadrant 3. Reference angle = 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 3, tan θ is:', 'Undefined', 'Negative', 'Zero', 'Positive', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q3, tan θ is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 2, tan θ is:', 'Positive', 'Zero', 'Undefined', 'Negative', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q2, tan θ is negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ < 0 and cos θ > 0, in which quadrant does θ lie?', 'Quadrant 2', 'Quadrant 1', 'Quadrant 4', 'Quadrant 3', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ < 0 and cos θ > 0, θ is in Quadrant 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reference angle for 300°.', '30°', '60°', '70°', '120°', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', '300° is in Quadrant 4. Reference angle = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate tan 225°.', '-1/2', '1', '√3/2', '1/2', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 45°. In Q3, tan 225° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 150°.', '-√3/2', '-1/2', '√3/2', '1/2', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 30°. In Q2, sin 150° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 1, tan θ is:', 'Negative', 'Zero', 'Positive', 'Undefined', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q1, tan θ is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 240°.', '1/2', '√3/2', '-1/2', '-√3/2', 2,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 60°. In Q3, cos 240° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate tan 225°.', '√3/2', '1', '1/2', '-1/2', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 45°. In Q3, tan 225° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 4, cos θ is:', 'Negative', 'Undefined', 'Zero', 'Positive', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q4, cos θ is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reference angle for 135°.', '45°', '135°', 'None of these', '55°', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', '135° is in Quadrant 2. Reference angle = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In Quadrant 3, sin θ is:', 'Zero', 'Undefined', 'Positive', 'Negative', 3,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'In Q3, sin θ is negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 120°.', '-1/2', '√3/2', '-√3/2', '1/2', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Reference angle is 60°. In Q2, cos 120° = -1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ > 0 and cos θ < 0, in which quadrant does θ lie?', 'Quadrant 3', 'Quadrant 2', 'Quadrant 1', 'Quadrant 4', 1,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ > 0 and cos θ < 0, θ is in Quadrant 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ > 0 and cos θ < 0, in which quadrant does θ lie?', 'Quadrant 2', 'Quadrant 1', 'Quadrant 4', 'Quadrant 3', 0,
'lc_hl_trigonometry', 3, 'foundation', 'lc_hl', 'Given sin θ > 0 and cos θ < 0, θ is in Quadrant 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 7 and central angle π/2.', '14π', '8π', '7π/2', '7π/3', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 7 × π/2 = 7π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π radians to degrees.', '360°', '150°', '180°', '210°', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π = π × 180/π = 180°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/2 radians to degrees.', '180°', '120°', '90°', '60°', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/2 = π/2 × 180/π = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 135° to radians.', 'π/3', '3π/4', 'π/4', 'π/6', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '135° = 135 × π/180 = 3π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 6 and central angle π.', '18π', '6π', '36π', '72π', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 6² × π = 18π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 120° to radians.', 'π/4', 'π/6', 'π/3', '2π/3', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '120° = 120 × π/180 = 2π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 45° to radians.', 'π/6', 'π/2', 'π/3', 'π/4', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '45° = 45 × π/180 = π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 2 and central angle 2π.', '4π', '3π', 'None of these', '2π/3', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 2 × 2π = 4π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 180° to radians.', 'π', 'π/6', 'π/3', 'π/4', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '180° = 180 × π/180 = π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3π/4 radians to degrees.', '270°', '165°', '105°', '135°', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '3π/4 = 3π/4 × 180/π = 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 180° to radians.', 'π/3', 'π/6', 'π', 'π/4', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '180° = 180 × π/180 = π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 4 and central angle π.', '8π', '4π', '16π', '32π', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 4² × π = 8π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 2 and central angle π.', '2π', '8π', '4π', 'None of these', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 2² × π = 2π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 8 and central angle π.', '9π', '8π/3', '8π', '16π', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 8 × π = 8π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3π/4 radians to degrees.', '270°', '135°', '165°', '105°', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '3π/4 = 3π/4 × 180/π = 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 3 and central angle π/2.', '9π', '18π', '9π/4', '3π', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 3² × π/2 = 9π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin(π/4).', '1', '√2/2', '-1', '0', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'sin(π/4) = √2/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 5 and central angle π/2.', '25π/4', '5π', '25π', '50π', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 5² × π/2 = 25π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/2 radians to degrees.', '180°', '90°', '60°', '120°', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/2 = π/2 × 180/π = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate tan(π/4).', '1', '0', '1/2', '-1', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'tan(π/4) = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 90° to radians.', 'π/4', 'π/2', 'π/3', 'π/6', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '90° = 90 × π/180 = π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 3 and central angle π/2.', '3π', '18π', '9π', '9π/4', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 3² × π/2 = 9π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin(π/2).', '1', '1/2', '-1', '0', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'sin(π/2) = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/6 radians to degrees.', 'None of these', '60°', '90°', '30°', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/6 = π/6 × 180/π = 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/6 radians to degrees.', '60°', '90°', 'None of these', '30°', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/6 = π/6 × 180/π = 30°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 5π/6 radians to degrees.', '150°', '120°', '300°', '180°', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '5π/6 = 5π/6 × 180/π = 150°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 2 and central angle π.', '8π', '2π', '4π', 'None of these', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 2² × π = 2π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 3 and central angle π/2.', '3π', '18π', '9π', '9π/4', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 3² × π/2 = 9π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 5 and central angle 2π.', '10π', '6π', '5π/3', 'None of these', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 5 × 2π = 10π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 8 and central angle π/2.', '9π', '8π/2', '16π', '8π/3', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 8 × π/2 = 8π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin(π/2).', '1', '1/2', '-1', '0', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'sin(π/2) = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 2 and central angle π/2.', '4π', '2π', '1π', '8π', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 2² × π/2 = 1π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/4 radians to degrees.', '75°', '45°', '90°', '15°', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/4 = π/4 × 180/π = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/2 radians to degrees.', '60°', '90°', '180°', '120°', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/2 = π/2 × 180/π = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 2 and central angle 2π.', '2π/3', '4π', '3π', 'None of these', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 2 × 2π = 4π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 3 and central angle π.', '6π', '4π', '3π', '3π/3', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 3 × π = 3π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 3 and central angle π/2.', '18π', '9π', '9π/4', '3π', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 3² × π/2 = 9π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 90° to radians.', 'π/6', 'π/4', 'π/2', 'π/3', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '90° = 90 × π/180 = π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 4 and central angle π/2.', '16π', 'None of these', '32π', '4π', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 4² × π/2 = 4π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 4 and central angle π.', '5π', '4π/3', '8π', '4π', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 4 × π = 4π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos(π/3).', '-1', '1', '1/2', '0', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'cos(π/3) = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 8 and central angle π/2.', '8π/3', '9π', '8π/2', '16π', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 8 × π/2 = 8π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos(π/3).', '1', '1/2', '0', '-1', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'cos(π/3) = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/2 radians to degrees.', '180°', '60°', '120°', '90°', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/2 = π/2 × 180/π = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 4 and central angle π.', '4π', '8π', '16π', '32π', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 4² × π = 8π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 2 and central angle π.', '8π', 'None of these', '4π', '2π', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 2² × π = 2π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the arc length of a circle with radius 3 and central angle π/2.', '4π', '3π/3', '3π/2', '6π', 2,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Arc length = rθ = 3 × π/2 = 3π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a sector with radius 2 and central angle π/2.', '8π', '1π', '4π', '2π', 1,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'Sector area = ½r²θ = ½ × 2² × π/2 = 1π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 60° to radians.', 'π/4', 'π/2', 'π/6', 'π/3', 3,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', '60° = 60 × π/180 = π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert π/4 radians to degrees.', '45°', '75°', '90°', '15°', 0,
'lc_hl_trigonometry', 4, 'developing', 'lc_hl', 'π/4 = π/4 × 180/π = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = 5/13 and θ is in Quadrant 1, find cos θ.', '1/2', '5/13', '3/4', '12/13', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using sin²θ + cos²θ = 1: cos θ = 12/13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin²θ + cos²θ', '2', '1', 'sin θ cos θ', '0', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: sin²θ + cos²θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ/cos θ', 'tan θ', 'cot θ', 'csc θ', 'sec θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: sin θ/cos θ = tan θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? sin(-θ) = -sin θ', 'Sometimes true', 'False', 'Only for acute angles', 'True', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''sin(-θ) = -sin θ'' is True.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? tan(-θ) = -tan θ', 'False', 'Sometimes true', 'Only for acute angles', 'True', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''tan(-θ) = -tan θ'' is True.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ/cos θ', 'tan θ', 'cot θ', 'csc θ', 'sec θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: sin θ/cos θ = tan θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + tan²θ', 'sec²θ', '1', 'cot²θ', 'csc²θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + tan²θ = sec²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ/cos θ', 'csc θ', 'tan θ', 'sec θ', 'cot θ', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: sin θ/cos θ = tan θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + cot²θ', 'csc²θ', 'sec²θ', '1', 'tan²θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + cot²θ = csc²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + cot²θ', 'tan²θ', '1', 'csc²θ', 'sec²θ', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + cot²θ = csc²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ/cos θ', 'tan θ', 'csc θ', 'sec θ', 'cot θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: sin θ/cos θ = tan θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? cos(-θ) = cos θ', 'False', 'Only for acute angles', 'True', 'Sometimes true', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''cos(-θ) = cos θ'' is True.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 4/5 and θ is in Quadrant 1, find sin θ.', '3/5', '3/4', '1/2', '4/5', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using sin²θ + cos²θ = 1: sin θ = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + cot²θ', '1', 'csc²θ', 'tan²θ', 'sec²θ', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + cot²θ = csc²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 4/5 and θ is in Quadrant 1, find sin θ.', '4/5', '1/2', '3/4', '3/5', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using sin²θ + cos²θ = 1: sin θ = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ csc θ', '0', 'sin²θ', 'cos θ', '1', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'sin θ csc θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/cos θ', 'cot θ', 'tan θ', 'sec θ', 'csc θ', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/cos θ = sec θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ csc θ', '0', 'cos θ', 'sin²θ', '1', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'sin θ csc θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin²θ + cos²θ', '1', '0', '2', 'sin θ cos θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: sin²θ + cos²θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/sin θ', 'sec θ', 'tan θ', 'cot θ', 'csc θ', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/sin θ = csc θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? tan(-θ) = tan θ', 'Only for acute angles', 'False', 'Sometimes true', 'True', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''tan(-θ) = tan θ'' is False.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? tan(-θ) = tan θ', 'Only for acute angles', 'Sometimes true', 'False', 'True', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''tan(-θ) = tan θ'' is False.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? sin(-θ) = sin θ', 'False', 'True', 'Only for acute angles', 'Sometimes true', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''sin(-θ) = sin θ'' is False.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos θ = 4/5 and θ is in Quadrant 1, find sin θ.', '4/5', '3/5', '3/4', '1/2', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using sin²θ + cos²θ = 1: sin θ = 3/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/cos θ', 'tan θ', 'csc θ', 'cot θ', 'sec θ', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/cos θ = sec θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + tan²θ', 'csc²θ', 'cot²θ', 'sec²θ', '1', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + tan²θ = sec²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/cos θ', 'csc θ', 'cot θ', 'sec θ', 'tan θ', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/cos θ = sec θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ/cos θ', 'sec θ', 'csc θ', 'cot θ', 'tan θ', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: sin θ/cos θ = tan θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + cot²θ', '1', 'csc²θ', 'tan²θ', 'sec²θ', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + cot²θ = csc²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ csc θ', 'sin²θ', 'cos θ', '0', '1', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'sin θ csc θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin²θ + cos²θ', '2', '0', 'sin θ cos θ', '1', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: sin²θ + cos²θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: cos θ sec θ', '1', 'cos²θ', '0', 'sin θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'cos θ sec θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: cos θ sec θ', '0', 'sin θ', 'cos²θ', '1', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'cos θ sec θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: cos θ sec θ', 'cos²θ', '0', '1', 'sin θ', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'cos θ sec θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? cos(-θ) = -cos θ', 'Sometimes true', 'Only for acute angles', 'True', 'False', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''cos(-θ) = -cos θ'' is False.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: cos θ sec θ', 'sin θ', '0', 'cos²θ', '1', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'cos θ sec θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + tan²θ', '1', 'csc²θ', 'cot²θ', 'sec²θ', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + tan²θ = sec²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/sin θ', 'tan θ', 'csc θ', 'sec θ', 'cot θ', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/sin θ = csc θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? cos(-θ) = -cos θ', 'Only for acute angles', 'False', 'True', 'Sometimes true', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''cos(-θ) = -cos θ'' is False.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/sin θ', 'tan θ', 'sec θ', 'csc θ', 'cot θ', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/sin θ = csc θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/sin θ', 'csc θ', 'sec θ', 'tan θ', 'cot θ', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/sin θ = csc θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ csc θ', 'sin²θ', '1', '0', 'cos θ', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'sin θ csc θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ csc θ', 'cos θ', '0', 'sin²θ', '1', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'sin θ csc θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1/cos θ', 'tan θ', 'cot θ', 'sec θ', 'csc θ', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: 1/cos θ = sec θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = 3/5 and θ is in Quadrant 1, find cos θ.', '1/2', '4/5', '3/5', '3/4', 1,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using sin²θ + cos²θ = 1: cos θ = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin θ/cos θ', 'csc θ', 'cot θ', 'sec θ', 'tan θ', 3,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using reciprocal/quotient identity: sin θ/cos θ = tan θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin²θ + cos²θ', '0', 'sin θ cos θ', '1', '2', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: sin²θ + cos²θ = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: 1 + cot²θ', 'tan²θ', 'sec²θ', 'csc²θ', '1', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using Pythagorean identity: 1 + cot²θ = csc²θ', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin θ = 3/5 and θ is in Quadrant 1, find cos θ.', '4/5', '3/4', '1/2', '3/5', 0,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'Using sin²θ + cos²θ = 1: cos θ = 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this identity correct? cos(-θ) = cos θ', 'False', 'Sometimes true', 'True', 'Only for acute angles', 2,
'lc_hl_trigonometry', 5, 'developing', 'lc_hl', 'The statement ''cos(-θ) = cos θ'' is True.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0° ≤ θ < 360°.', '45° and 315°', '45° and 135°', '30° and 210°', '45° and 225°', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 225°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = -1 for 0° ≤ θ < 360°.', '45° and 225°', '45° and 315°', '135° and 225°', '135° and 315°', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 135° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = 1/2 for 0° ≤ θ < 360°.', '60° and 120°', '30° and 330°', '60° and 300°', '45° and 315°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 300°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = 1/2 for 0 ≤ θ < 2π.', 'π/4 and 3π/4', 'π/6 and 7π/6', 'π/3 and 2π/3', 'π/6 and 5π/6', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/6 and 5π/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = √3 for 0° ≤ θ < 360°.', '45° and 225°', '60° and 240°', '60° and 120°', '30° and 210°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0 ≤ θ < 2π.', 'π/4 and 7π/4', 'π/4 and 3π/4', 'π/3 and 4π/3', 'π/4 and 5π/4', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/4 and 5π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0° ≤ θ < 360°.', '45° and 135°', '30° and 210°', '45° and 315°', '45° and 225°', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 225°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = √2/2 for 0° ≤ θ < 360°.', '30° and 150°', '60° and 120°', '45° and 225°', '45° and 135°', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = √3 for 0° ≤ θ < 360°.', '60° and 120°', '30° and 210°', '60° and 240°', '45° and 225°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = 1/2 for 0° ≤ θ < 360°.', '30° and 210°', '45° and 135°', '30° and 150°', '60° and 120°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 30° and 150°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = √2/2 for 0° ≤ θ < 360°.', '30° and 330°', '45° and 315°', '45° and 135°', '60° and 300°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many solutions does cos θ = 0 for 0° ≤ θ < 360° have?', '3', '4', '2', '1', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The equation has 2 solution(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = √3/2 for 0° ≤ θ < 360°.', '30° and 150°', '45° and 315°', '30° and 330°', '60° and 300°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 30° and 330°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = -1 for 0° ≤ θ < 360°.', '135° and 225°', '135° and 315°', '45° and 315°', '45° and 225°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 135° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many solutions does cos θ = 0 for 0° ≤ θ < 360° have?', '1', '2', '3', '4', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The equation has 2 solution(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = 1/2 for 0° ≤ θ < 360°.', '60° and 120°', '45° and 315°', '60° and 300°', '30° and 330°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 300°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0 ≤ θ < 2π.', 'π/3 and 4π/3', 'π/4 and 3π/4', 'π/4 and 5π/4', 'π/4 and 7π/4', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/4 and 5π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0° ≤ θ < 360°.', '45° and 315°', '45° and 135°', '45° and 225°', '30° and 210°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 225°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0 ≤ θ < 2π.', 'π/3 and 4π/3', 'π/4 and 5π/4', 'π/4 and 3π/4', 'π/4 and 7π/4', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/4 and 5π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = 1/2 for 0 ≤ θ < 2π.', 'π/4 and 3π/4', 'π/6 and 5π/6', 'π/3 and 2π/3', 'π/6 and 7π/6', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/6 and 5π/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0 ≤ θ < 2π.', 'π/4 and 3π/4', 'π/4 and 5π/4', 'π/3 and 4π/3', 'π/4 and 7π/4', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/4 and 5π/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = √3 for 0° ≤ θ < 360°.', '45° and 225°', '60° and 240°', '60° and 120°', '30° and 210°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = √3/2 for 0° ≤ θ < 360°.', '60° and 120°', '30° and 150°', '60° and 240°', '45° and 135°', 0,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 120°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = √2/2 for 0° ≤ θ < 360°.', '45° and 135°', '60° and 120°', '45° and 225°', '30° and 150°', 0,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = √3 for 0° ≤ θ < 360°.', '60° and 120°', '60° and 240°', '30° and 210°', '45° and 225°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = 1/2 for 0 ≤ θ < 2π.', 'π/3 and 5π/3', 'π/4 and 7π/4', 'π/6 and 11π/6', 'π/3 and 2π/3', 0,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/3 and 5π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = √3 for 0° ≤ θ < 360°.', '45° and 225°', '60° and 240°', '30° and 210°', '60° and 120°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = 1/2 for 0° ≤ θ < 360°.', '45° and 315°', '30° and 330°', '60° and 300°', '60° and 120°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 300°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = -1 for 0° ≤ θ < 360°.', '135° and 315°', '45° and 225°', '45° and 315°', '135° and 225°', 0,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 135° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = √3/2 for 0° ≤ θ < 360°.', '60° and 300°', '30° and 330°', '45° and 315°', '30° and 150°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 30° and 330°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = 1 for 0° ≤ θ < 360°.', '45° and 135°', '45° and 225°', '45° and 315°', '30° and 210°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 225°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = √3/2 for 0° ≤ θ < 360°.', '45° and 135°', '60° and 120°', '60° and 240°', '30° and 150°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 120°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many solutions does cos θ = 2 for 0° ≤ θ < 360° have?', '2', '4', '1', '0', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The equation has 0 solution(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = -1 for 0° ≤ θ < 360°.', '45° and 225°', '135° and 315°', '135° and 225°', '45° and 315°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 135° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = √2/2 for 0° ≤ θ < 360°.', '30° and 330°', '60° and 300°', '45° and 135°', '45° and 315°', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many solutions does cos θ = 2 for 0° ≤ θ < 360° have?', '2', '4', '1', '0', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The equation has 0 solution(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = 1/2 for 0° ≤ θ < 360°.', '30° and 330°', '60° and 300°', '45° and 315°', '60° and 120°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 300°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = 1/2 for 0° ≤ θ < 360°.', '60° and 300°', '45° and 315°', '60° and 120°', '30° and 330°', 0,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 300°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = √2/2 for 0° ≤ θ < 360°.', '45° and 225°', '45° and 135°', '60° and 120°', '30° and 150°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = 1/2 for 0 ≤ θ < 2π.', 'π/6 and 5π/6', 'π/3 and 2π/3', 'π/4 and 3π/4', 'π/6 and 7π/6', 0,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = π/6 and 5π/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = √2/2 for 0° ≤ θ < 360°.', '60° and 300°', '30° and 330°', '45° and 315°', '45° and 135°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = 1/2 for 0° ≤ θ < 360°.', '30° and 210°', '60° and 120°', '30° and 150°', '45° and 135°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 30° and 150°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = 1/2 for 0° ≤ θ < 360°.', '60° and 120°', '60° and 300°', '45° and 315°', '30° and 330°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 300°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = √3 for 0° ≤ θ < 360°.', '60° and 240°', '45° and 225°', '60° and 120°', '30° and 210°', 0,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve cos θ = √2/2 for 0° ≤ θ < 360°.', '60° and 300°', '45° and 135°', '30° and 330°', '45° and 315°', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 45° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = 1/2 for 0° ≤ θ < 360°.', '30° and 210°', '30° and 150°', '45° and 135°', '60° and 120°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 30° and 150°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve tan θ = -1 for 0° ≤ θ < 360°.', '45° and 315°', '45° and 225°', '135° and 315°', '135° and 225°', 2,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 135° and 315°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many solutions does cos θ = 0 for 0° ≤ θ < 360° have?', '1', '3', '4', '2', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The equation has 2 solution(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve sin θ = √3/2 for 0° ≤ θ < 360°.', '60° and 240°', '60° and 120°', '30° and 150°', '45° and 135°', 1,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The solutions are θ = 60° and 120°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many solutions does cos θ = 0 for 0° ≤ θ < 360° have?', '4', '1', '3', '2', 3,
'lc_hl_trigonometry', 6, 'developing', 'lc_hl', 'The equation has 2 solution(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x + 2?', '2 units up', '2 units down', 'No vertical shift', '3 units up', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 2 units up', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x - 2?', 'No vertical shift', '2 units down', '3 units down', '2 units up', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 2 units down', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = cos x - 2?', 'No vertical shift', '2 units down', '3 units down', '2 units up', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 2 units down', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = 3sin x - 3?', '[-6, 0]', '[-4, -2]', '[-7, 1]', '[-3, 3]', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [-6, 0]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = 4cos x - 3?', '[-4, -2]', '[-4, 4]', '[-8, 2]', '[-7, 1]', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [-7, 1]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = 2sin x + 3?', '[2, 4]', '[0, 6]', '[1, 5]', '[-2, 2]', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [1, 5]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = cos(4x)?', '2π', '2π/3', 'π', 'π/2', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(bx), period = 2π/b = 2π/4 = π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 5sin x?', '10', '6', '4', '5', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·sin x, the amplitude is |a| = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 4sin x?', '4', '3', '5', '8', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·sin x, the amplitude is |a| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x - 3?', '3 units up', '3 units down', '4 units down', 'No vertical shift', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 3 units down', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = cos(2x)?', '2π', 'π/2', '2π/3', 'π', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(bx), period = 2π/b = 2π/2 = π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 2cos x?', '2', '4', '3', '1', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 3cos x?', '6', '3', '4', '2', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = cos(1x)?', 'π', '2π', 'π/2', '2π/3', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(bx), period = 2π/b = 2π/1 = 2π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 4cos x?', '3', '8', '4', '5', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = sin(x + π/3)?', 'π/3 left', 'No shift', 'π/6 left', 'π/3 right', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = sin(x + π/3), the phase shift is π/3 left', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 2cos x?', '2', '4', '3', '1', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = sin(x + π/3)?', 'π/3 right', 'π/3 left', 'π/6 left', 'No shift', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = sin(x + π/3), the phase shift is π/3 left', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = cos(3x)?', '2π', 'π', '2π/3', 'π/2', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(bx), period = 2π/b = 2π/3 = 2π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = sin(4x)?', '2π/3', '2π', 'π', 'π/2', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = sin(bx), period = 2π/b = 2π/4 = π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = cos(x - π/2)?', 'π/2 left', 'No shift', 'π right', 'π/2 right', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(x - π/2), the phase shift is π/2 right', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = cos(3x)?', '2π/3', '2π', 'π/2', 'π', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(bx), period = 2π/b = 2π/3 = 2π/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 3sin x?', '3', '4', '2', '6', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·sin x, the amplitude is |a| = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = cos(x - π/2)?', 'No shift', 'π/2 left', 'π right', 'π/2 right', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(x - π/2), the phase shift is π/2 right', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x + 5?', '5 units down', '6 units up', 'No vertical shift', '5 units up', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 5 units up', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = sin(x - π/4)?', 'π/4 left', 'π/4 right', 'π/2 right', 'No shift', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = sin(x - π/4), the phase shift is π/4 right', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x - 3?', 'No vertical shift', '4 units down', '3 units up', '3 units down', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 3 units down', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = sin(x - π/4)?', 'π/4 left', 'π/2 right', 'No shift', 'π/4 right', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = sin(x - π/4), the phase shift is π/4 right', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = sin x - 1?', 'None of these', '[-1, 1]', '[-2, 0]', '[-3, 1]', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [-2, 0]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 4cos x?', '4', '5', '8', '3', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = sin(x + π/3)?', 'π/3 left', 'π/3 right', 'π/6 left', 'No shift', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = sin(x + π/3), the phase shift is π/3 left', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x - 2?', '3 units down', 'No vertical shift', '2 units up', '2 units down', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 2 units down', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 2sin x?', '1', '4', '2', '3', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·sin x, the amplitude is |a| = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x + 1?', '1 units down', '1 units up', 'No vertical shift', '2 units up', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 1 units up', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 3sin x?', '6', '4', '2', '3', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·sin x, the amplitude is |a| = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = cos(4x)?', 'π/2', '2π', '2π/3', 'π', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(bx), period = 2π/b = 2π/4 = π/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x - 1?', '2 units down', '1 units up', '1 units down', 'No vertical shift', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 1 units down', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 4cos x?', '8', '4', '5', '3', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 6cos x?', '12', '7', '5', '6', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = 4cos x - 2?', '[-3, -1]', '[-4, 4]', '[-7, 3]', '[-6, 2]', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [-6, 2]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x + 3?', '4 units up', '3 units up', '3 units down', 'No vertical shift', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 3 units up', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 4sin x?', '3', '4', '5', '8', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·sin x, the amplitude is |a| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the period of y = sin(1x)?', 'π', '2π', 'π/2', '2π/3', 1,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = sin(bx), period = 2π/b = 2π/1 = 2π', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the amplitude of y = 2cos x?', '2', '3', '1', '4', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = a·cos x, the amplitude is |a| = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = 2sin x + 1?', '[-2, 4]', '[0, 2]', '[-2, 2]', '[-1, 3]', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [-1, 3]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = sin x - 4?', '4 units down', '4 units up', 'No vertical shift', '5 units down', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 4 units down', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the vertical shift of y = cos x + 4?', '4 units up', '4 units down', '5 units up', 'No vertical shift', 0,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'The graph is shifted 4 units up', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = 3cos x + 2?', '[-2, 6]', '[1, 3]', '[-1, 5]', '[-3, 3]', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [-1, 5]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the phase shift of y = cos(x - π/2)?', 'π right', 'No shift', 'π/2 right', 'π/2 left', 2,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'For y = cos(x - π/2), the phase shift is π/2 right', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the range of y = 3sin x - 2?', '[-3, 3]', '[-6, 2]', '[-3, -1]', '[-5, 1]', 3,
'lc_hl_trigonometry', 7, 'proficient', 'lc_hl', 'Range = [-a + k, a + k] = [-5, 1]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A - B) is:', '(tan A + tan B)/(1 - tan A tan B)', '(tan A - tan B)/(1 + tan A tan B)', 'tan A / tan B', 'tan A - tan B', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A - B) = (tan A - tan B)/(1 + tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 75° using compound angle formulas.', '(√2 + 1)/2', '√3/2', '(√6 + √2)/4', '(√6 - √2)/4', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 75° = sin(45° + 30°) = (√6 + √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of sin(A + B) is:', 'sin A sin B + cos A cos B', 'sin A cos B - cos A sin B', 'sin A cos B + cos A sin B', 'cos A cos B - sin A sin B', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin(A + B) = sin A cos B + cos A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A - B) is:', '(tan A + tan B)/(1 - tan A tan B)', 'tan A - tan B', 'tan A / tan B', '(tan A - tan B)/(1 + tan A tan B)', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A - B) = (tan A - tan B)/(1 + tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '√3/4', '(√6 + √2)/4', '(√6 - √2)/4', '(√2 - 1)/2', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A - B) is:', 'tan A - tan B', '(tan A + tan B)/(1 - tan A tan B)', 'tan A / tan B', '(tan A - tan B)/(1 + tan A tan B)', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A - B) = (tan A - tan B)/(1 + tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 50° cos 40° + cos 50° sin 40°', '√3/2', '0', '1', '√2/2', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 50° cos 40° + cos 50° sin 40° = sin 90° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A - B) is:', 'tan A / tan B', '(tan A - tan B)/(1 + tan A tan B)', 'tan A - tan B', '(tan A + tan B)/(1 - tan A tan B)', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A - B) = (tan A - tan B)/(1 + tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 and cos B = 12/13 (A, B in Q1), find sin(A + B)', '20/65', '56/65', '16/65', '36/65', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin A cos B + cos A sin B = (3/5)(12/13) + (4/5)(5/13) = 56/65 = 56/65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of sin(A + B) is:', 'sin A cos B + cos A sin B', 'sin A sin B + cos A cos B', 'cos A cos B - sin A sin B', 'sin A cos B - cos A sin B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin(A + B) = sin A cos B + cos A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '(√2 - 1)/2', '(√6 + √2)/4', '(√6 - √2)/4', '√3/4', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 and cos B = 12/13 (A, B in Q1), find sin(A + B)', '36/65', '56/65', '16/65', '20/65', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin A cos B + cos A sin B = (3/5)(12/13) + (4/5)(5/13) = 56/65 = 56/65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A + B) is:', '(tan A + tan B)/(1 - tan A tan B)', 'tan A + tan B', '(tan A - tan B)/(1 + tan A tan B)', 'tan A tan B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A + B) = (tan A + tan B)/(1 - tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of cos(A + B) is:', 'sin A cos B + cos A sin B', 'sin A sin B - cos A cos B', 'cos A cos B + sin A sin B', 'cos A cos B - sin A sin B', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos(A + B) = cos A cos B - sin A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 75° using compound angle formulas.', '(√6 + √2)/4', '(√3 - 1)/2', '(√6 - √2)/4', '√2/2', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos 75° = cos(45° + 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 75° using compound angle formulas.', '√3/2', '(√6 + √2)/4', '(√2 + 1)/2', '(√6 - √2)/4', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 75° = sin(45° + 30°) = (√6 + √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '(√2 - 1)/2', '(√6 - √2)/4', '√3/4', '(√6 + √2)/4', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 and cos B = 12/13 (A, B in Q1), find sin(A + B)', '20/65', '36/65', '56/65', '16/65', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin A cos B + cos A sin B = (3/5)(12/13) + (4/5)(5/13) = 56/65 = 56/65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 50° cos 40° + cos 50° sin 40°', '√3/2', '√2/2', '1', '0', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 50° cos 40° + cos 50° sin 40° = sin 90° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 50° cos 40° + cos 50° sin 40°', '√2/2', '√3/2', '0', '1', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 50° cos 40° + cos 50° sin 40° = sin 90° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of cos(A + B) is:', 'cos A cos B - sin A sin B', 'sin A cos B + cos A sin B', 'sin A sin B - cos A cos B', 'cos A cos B + sin A sin B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos(A + B) = cos A cos B - sin A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 and cos B = 12/13 (A, B in Q1), find sin(A + B)', '36/65', '20/65', '56/65', '16/65', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin A cos B + cos A sin B = (3/5)(12/13) + (4/5)(5/13) = 56/65 = 56/65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A + B) is:', '(tan A + tan B)/(1 - tan A tan B)', 'tan A + tan B', '(tan A - tan B)/(1 + tan A tan B)', 'tan A tan B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A + B) = (tan A + tan B)/(1 - tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of sin(A - B) is:', 'sin A cos B - cos A sin B', 'sin A sin B - cos A cos B', 'cos A cos B + sin A sin B', 'sin A cos B + cos A sin B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin(A - B) = sin A cos B - cos A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 80° cos 20° - cos 80° sin 20°', '√3/2', '1', '1/2', '√2/2', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 80° cos 20° - cos 80° sin 20° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 75° using compound angle formulas.', '(√6 + √2)/4', '√3/2', '(√6 - √2)/4', '(√2 + 1)/2', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 75° = sin(45° + 30°) = (√6 + √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '(√2 - 1)/2', '(√6 + √2)/4', '√3/4', '(√6 - √2)/4', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '(√6 + √2)/4', '(√6 - √2)/4', '(√2 - 1)/2', '√3/4', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 80° cos 20° - cos 80° sin 20°', '√2/2', '√3/2', '1', '1/2', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 80° cos 20° - cos 80° sin 20° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: cos 70° cos 20° + sin 70° sin 20°', '0', '1', 'sin 50°', 'cos 50°', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos 70° cos 20° + sin 70° sin 20° = cos 50° = cos 50°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '(√6 - √2)/4', '√3/4', '(√6 + √2)/4', '(√2 - 1)/2', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 75° using compound angle formulas.', '(√3 - 1)/2', '(√6 + √2)/4', '(√6 - √2)/4', '√2/2', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos 75° = cos(45° + 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 and cos B = 12/13 (A, B in Q1), find sin(A + B)', '20/65', '56/65', '16/65', '36/65', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin A cos B + cos A sin B = (3/5)(12/13) + (4/5)(5/13) = 56/65 = 56/65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 75° using compound angle formulas.', '(√6 + √2)/4', '(√2 + 1)/2', '(√6 - √2)/4', '√3/2', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 75° = sin(45° + 30°) = (√6 + √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A - B) is:', 'tan A - tan B', '(tan A - tan B)/(1 + tan A tan B)', 'tan A / tan B', '(tan A + tan B)/(1 - tan A tan B)', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A - B) = (tan A - tan B)/(1 + tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: cos 70° cos 20° + sin 70° sin 20°', '0', 'sin 50°', 'cos 50°', '1', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos 70° cos 20° + sin 70° sin 20° = cos 50° = cos 50°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of cos(A - B) is:', 'cos A cos B - sin A sin B', 'sin A sin B + cos A cos B', 'sin A cos B - cos A sin B', 'cos A cos B + sin A sin B', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos(A - B) = cos A cos B + sin A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A + B) is:', '(tan A + tan B)/(1 - tan A tan B)', '(tan A - tan B)/(1 + tan A tan B)', 'tan A tan B', 'tan A + tan B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A + B) = (tan A + tan B)/(1 - tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of sin(A + B) is:', 'sin A sin B + cos A cos B', 'sin A cos B + cos A sin B', 'sin A cos B - cos A sin B', 'cos A cos B - sin A sin B', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin(A + B) = sin A cos B + cos A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A - B) is:', '(tan A - tan B)/(1 + tan A tan B)', 'tan A / tan B', '(tan A + tan B)/(1 - tan A tan B)', 'tan A - tan B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A - B) = (tan A - tan B)/(1 + tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of cos(A + B) is:', 'cos A cos B - sin A sin B', 'sin A sin B - cos A cos B', 'cos A cos B + sin A sin B', 'sin A cos B + cos A sin B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos(A + B) = cos A cos B - sin A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '(√6 - √2)/4', '√3/4', '(√6 + √2)/4', '(√2 - 1)/2', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 and cos B = 12/13 (A, B in Q1), find sin(A + B)', '16/65', '20/65', '36/65', '56/65', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin A cos B + cos A sin B = (3/5)(12/13) + (4/5)(5/13) = 56/65 = 56/65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 15° using compound angle formulas.', '√3/4', '(√6 + √2)/4', '(√2 - 1)/2', '(√6 - √2)/4', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 15° = sin(45° - 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 50° cos 40° + cos 50° sin 40°', '√2/2', '√3/2', '0', '1', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 50° cos 40° + cos 50° sin 40° = sin 90° = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate sin 75° using compound angle formulas.', '(√6 - √2)/4', '√3/2', '(√2 + 1)/2', '(√6 + √2)/4', 3,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin 75° = sin(45° + 30°) = (√6 + √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A - B) is:', 'tan A / tan B', '(tan A + tan B)/(1 - tan A tan B)', '(tan A - tan B)/(1 + tan A tan B)', 'tan A - tan B', 2,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A - B) = (tan A - tan B)/(1 + tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The formula for tan(A + B) is:', '(tan A + tan B)/(1 - tan A tan B)', '(tan A - tan B)/(1 + tan A tan B)', 'tan A + tan B', 'tan A tan B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'tan(A + B) = (tan A + tan B)/(1 - tan A tan B)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The expansion of sin(A + B) is:', 'sin A cos B + cos A sin B', 'cos A cos B - sin A sin B', 'sin A cos B - cos A sin B', 'sin A sin B + cos A cos B', 0,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'sin(A + B) = sin A cos B + cos A sin B', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate cos 75° using compound angle formulas.', '(√6 + √2)/4', '(√6 - √2)/4', '(√3 - 1)/2', '√2/2', 1,
'lc_hl_trigonometry', 8, 'proficient', 'lc_hl', 'cos 75° = cos(45° + 30°) = (√6 - √2)/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (sin x + cos x)²', 'cos 2x', '1 + sin 2x', 'sin 2x', '1 - sin 2x', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(sin x + cos x)² = 1 + sin 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2cos²30° - 1', '0', '√3/2', '1/2', '√2/2', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2cos²30° - 1 = cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 (A in Q1), find sin 2A.', '12/25', '18/25', '24/25', '7/25', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 2A = 2 sin A cos A = 2(3/5)(4/5) = 24/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 (A in Q1), find sin 2A.', '18/25', '24/25', '7/25', '12/25', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 2A = 2 sin A cos A = 2(3/5)(4/5) = 24/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 4x', '4 sin x cos x', '2 sin 2x cos 2x', 'sin²2x + cos²2x', 'sin 2x + cos 2x', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 4x = 2 sin 2x cos 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2cos²30° - 1', '√2/2', '√3/2', '0', '1/2', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2cos²30° - 1 = cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express tan 2A in terms of single angles:', '2tan A', '2tan A/(1 + tan²A)', 'tan²A - 1', '2tan A/(1 - tan²A)', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'tan 2A = 2tan A/(1 - tan²A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2cos²30° - 1', '1/2', '0', '√2/2', '√3/2', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2cos²30° - 1 = cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2 sin 30° cos 30°', '1', '1/2', '√2/2', '√3/2', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2 sin 30° cos 30° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 4x', 'sin²2x + cos²2x', '4 sin x cos x', '2 sin 2x cos 2x', 'sin 2x + cos 2x', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 4x = 2 sin 2x cos 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (sin x + cos x)²', '1 + sin 2x', 'sin 2x', 'cos 2x', '1 - sin 2x', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(sin x + cos x)² = 1 + sin 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 4x', '4 sin x cos x', 'sin 2x + cos 2x', '2 sin 2x cos 2x', 'sin²2x + cos²2x', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 4x = 2 sin 2x cos 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 2A in terms of single angles:', '2 sin A + 2 cos A', 'sin²A - cos²A', 'sin²A + cos²A', '2 sin A cos A', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 2A = 2 sin A cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 4x', 'sin²2x + cos²2x', '4 sin x cos x', 'sin 2x + cos 2x', '2 sin 2x cos 2x', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 4x = 2 sin 2x cos 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 4x', '4 sin x cos x', 'sin²2x + cos²2x', '2 sin 2x cos 2x', 'sin 2x + cos 2x', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 4x = 2 sin 2x cos 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2cos²30° - 1', '√3/2', '1/2', '0', '√2/2', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2cos²30° - 1 = cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2cos²30° - 1', '√2/2', '√3/2', '1/2', '0', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2cos²30° - 1 = cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: cos²45° - sin²45°', '√2/2', '1/2', '0', '1', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos²45° - sin²45° = cos 90° = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 (A in Q1), find cos 2A.', '18/25', '7/25', '-7/25', '24/25', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos 2A = 1 - 2sin²A = 1 - 2(9/25) = 7/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos 2A = 7/25, find sin²A (A in Q1)', '9/25', '7/25', '16/25', '18/25', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(1 - cos 2A)/2 = (1 - 7/25)/2 = 9/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express tan 2A in terms of single angles:', '2tan A/(1 + tan²A)', 'tan²A - 1', '2tan A', '2tan A/(1 - tan²A)', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'tan 2A = 2tan A/(1 - tan²A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (sin x + cos x)²', 'sin 2x', '1 + sin 2x', 'cos 2x', '1 - sin 2x', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(sin x + cos x)² = 1 + sin 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2 sin 30° cos 30°', '1/2', '√3/2', '1', '√2/2', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2 sin 30° cos 30° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2 sin 30° cos 30°', '1/2', '√2/2', '1', '√3/2', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2 sin 30° cos 30° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 (A in Q1), find cos 2A.', '7/25', '-7/25', '24/25', '18/25', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos 2A = 1 - 2sin²A = 1 - 2(9/25) = 7/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2 sin 30° cos 30°', '1/2', '√3/2', '1', '√2/2', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2 sin 30° cos 30° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 4x', 'sin²2x + cos²2x', 'sin 2x + cos 2x', '4 sin x cos x', '2 sin 2x cos 2x', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 4x = 2 sin 2x cos 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: cos²45° - sin²45°', '√2/2', '1', '0', '1/2', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos²45° - sin²45° = cos 90° = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos 2A = 7/25, find cos²A (A in Q1)', '9/25', '7/25', '18/25', '16/25', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(1 + cos 2A)/2 = (1 + 7/25)/2 = 16/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 (A in Q1), find sin 2A.', '18/25', '24/25', '12/25', '7/25', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 2A = 2 sin A cos A = 2(3/5)(4/5) = 24/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: cos²45° - sin²45°', '0', '1', '1/2', '√2/2', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos²45° - sin²45° = cos 90° = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2cos²30° - 1', '√3/2', '√2/2', '1/2', '0', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2cos²30° - 1 = cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2cos²30° - 1', '1/2', '0', '√3/2', '√2/2', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2cos²30° - 1 = cos 60° = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos 2A = 7/25, find cos²A (A in Q1)', '16/25', '18/25', '7/25', '9/25', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(1 + cos 2A)/2 = (1 + 7/25)/2 = 16/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 2A in terms of single angles:', '2 sin A + 2 cos A', '2 sin A cos A', 'sin²A - cos²A', 'sin²A + cos²A', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 2A = 2 sin A cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 2A in terms of single angles:', '2 sin A cos A', 'sin²A - cos²A', '2 sin A + 2 cos A', 'sin²A + cos²A', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 2A = 2 sin A cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2 sin 30° cos 30°', '√3/2', '√2/2', '1/2', '1', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2 sin 30° cos 30° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express cos 2A (first form) in terms of single angles:', '2 sin²A', 'sin²A - cos²A', '2 cos²A', 'cos²A - sin²A', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos 2A (first form) = cos²A - sin²A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 (A in Q1), find cos 2A.', '24/25', '18/25', '-7/25', '7/25', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos 2A = 1 - 2sin²A = 1 - 2(9/25) = 7/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: cos²45° - sin²45°', '0', '1/2', '1', '√2/2', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos²45° - sin²45° = cos 90° = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos 2A = 7/25, find cos²A (A in Q1)', '18/25', '16/25', '7/25', '9/25', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(1 + cos 2A)/2 = (1 + 7/25)/2 = 16/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: sin 4x', '4 sin x cos x', '2 sin 2x cos 2x', 'sin 2x + cos 2x', 'sin²2x + cos²2x', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 4x = 2 sin 2x cos 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2 sin 30° cos 30°', '√2/2', '1/2', '1', '√3/2', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2 sin 30° cos 30° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (sin x + cos x)²', 'cos 2x', '1 + sin 2x', 'sin 2x', '1 - sin 2x', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(sin x + cos x)² = 1 + sin 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If sin A = 3/5 (A in Q1), find cos 2A.', '18/25', '-7/25', '7/25', '24/25', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos 2A = 1 - 2sin²A = 1 - 2(9/25) = 7/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If cos 2A = 7/25, find sin²A (A in Q1)', '7/25', '16/25', '9/25', '18/25', 2,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(1 - cos 2A)/2 = (1 - 7/25)/2 = 9/25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express cos 2A (first form) in terms of single angles:', 'sin²A - cos²A', 'cos²A - sin²A', '2 cos²A', '2 sin²A', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'cos 2A (first form) = cos²A - sin²A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 2A in terms of single angles:', '2 sin A + 2 cos A', 'sin²A - cos²A', 'sin²A + cos²A', '2 sin A cos A', 3,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', 'sin 2A = 2 sin A cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Evaluate: 2 sin 30° cos 30°', '√3/2', '√2/2', '1/2', '1', 0,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '2 sin 30° cos 30° = sin 60° = √3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Simplify: (sin x + cos x)²', 'cos 2x', '1 + sin 2x', '1 - sin 2x', 'sin 2x', 1,
'lc_hl_trigonometry', 9, 'proficient', 'lc_hl', '(sin x + cos x)² = 1 + sin 2x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Cosine Rule (find side):', 'a² = b² + c² - 2bc cos A', 'a² = b² + c² + 2bc cos A', 'a² = b² - c² + 2bc cos A', 'a = b + c - 2bc cos A', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Cosine Rule (find side) states: a² = b² + c² - 2bc cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '10√2', '20', '10', '5√2', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '9', '8', '7', '6', 2,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '10√2', '5√2', '20', '10', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 7, b = 5, c = 8. Find cos A.', '1/4', '1/2', '√3/2', '3/4', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (25 + 64 - 49)/(80) = 40/80 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '90°', '60°', '45°', '30°', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 5, b = 4, c = 3. Find cos A.', '√3/2', '1/2', '1/4', '0', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (16 + 9 - 25)/(24) = 0/24 = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Sine Rule:', 'a sin A = b sin B', 'a² = b² + c²', 'a/sin A = b/sin B = c/sin C', 'a/cos A = b/cos B', 2,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Sine Rule states: a/sin A = b/sin B = c/sin C', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '5√2', '10√2', '20', '10', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 5, b = 4, c = 3. Find cos A.', '1/2', '1/4', '0', '√3/2', 2,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (16 + 9 - 25)/(24) = 0/24 = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '8', '9', '7', '6', 2,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '9', '8', '6', '7', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 5, b = 4, c = 3. Find cos A.', '√3/2', '0', '1/2', '1/4', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (16 + 9 - 25)/(24) = 0/24 = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '60°', '45°', '90°', '30°', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '10√2', '5√2', '20', '10', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '9', '8', '6', '7', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '30°', '45°', '90°', '60°', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 3, c = 4, A = 90°. Find a.', '4', '7', '6', '5', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos 90° = 9 + 16 - 0 = 25, so a = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '20', '10√2', '5√2', '10', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '45°', '30°', '60°', '90°', 2,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '7', '8', '6', '9', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Cosine Rule (find side):', 'a² = b² + c² - 2bc cos A', 'a² = b² - c² + 2bc cos A', 'a = b + c - 2bc cos A', 'a² = b² + c² + 2bc cos A', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Cosine Rule (find side) states: a² = b² + c² - 2bc cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '10', '5√2', '10√2', '20', 2,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '10√2', '20', '5√2', '10', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 3, c = 4, A = 90°. Find a.', '5', '6', '4', '7', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos 90° = 9 + 16 - 0 = 25, so a = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '6', '7', '9', '8', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '90°', '45°', '30°', '60°', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '9', '6', '7', '8', 2,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Cosine Rule (find side):', 'a² = b² - c² + 2bc cos A', 'a = b + c - 2bc cos A', 'a² = b² + c² + 2bc cos A', 'a² = b² + c² - 2bc cos A', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Cosine Rule (find side) states: a² = b² + c² - 2bc cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 7, b = 5, c = 8. Find cos A.', '1/2', '1/4', '3/4', '√3/2', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (25 + 64 - 49)/(80) = 40/80 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '30°', '45°', '90°', '60°', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Sine Rule:', 'a/sin A = b/sin B = c/sin C', 'a² = b² + c²', 'a/cos A = b/cos B', 'a sin A = b sin B', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Sine Rule states: a/sin A = b/sin B = c/sin C', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Sine Rule:', 'a sin A = b sin B', 'a² = b² + c²', 'a/cos A = b/cos B', 'a/sin A = b/sin B = c/sin C', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Sine Rule states: a/sin A = b/sin B = c/sin C', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '7', '6', '9', '8', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Sine Rule:', 'a² = b² + c²', 'a/sin A = b/sin B = c/sin C', 'a sin A = b sin B', 'a/cos A = b/cos B', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Sine Rule states: a/sin A = b/sin B = c/sin C', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Cosine Rule (find side):', 'a² = b² - c² + 2bc cos A', 'a² = b² + c² + 2bc cos A', 'a = b + c - 2bc cos A', 'a² = b² + c² - 2bc cos A', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Cosine Rule (find side) states: a² = b² + c² - 2bc cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '10', '10√2', '20', '5√2', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 7, b = 5, c = 8. Find cos A.', '3/4', '1/2', '√3/2', '1/4', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (25 + 64 - 49)/(80) = 40/80 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '6', '8', '9', '7', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '7', '8', '9', '6', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '30°', '60°', '90°', '45°', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '10√2', '10', '20', '5√2', 0,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Cosine Rule (find side):', 'a² = b² + c² + 2bc cos A', 'a² = b² + c² - 2bc cos A', 'a = b + c - 2bc cos A', 'a² = b² - c² + 2bc cos A', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Cosine Rule (find side) states: a² = b² + c² - 2bc cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 5, b = 4, c = 3. Find cos A.', '√3/2', '0', '1/2', '1/4', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (16 + 9 - 25)/(24) = 0/24 = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, b = 10, A = 60°. Find B.', '90°', '45°', '30°', '60°', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'Since a = b, the triangle is isosceles, so B = A = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, b = 5, c = 8, A = 60°. Find a.', '6', '7', '8', '9', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49, so a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 7, b = 5, c = 8. Find cos A.', '√3/2', '1/2', '3/4', '1/4', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (25 + 64 - 49)/(80) = 40/80 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.', '20', '10√2', '10', '5√2', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'b = a sin B / sin A = 10 × sin 45° / sin 30° = 10√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('State the Cosine Rule (find side):', 'a = b + c - 2bc cos A', 'a² = b² + c² + 2bc cos A', 'a² = b² - c² + 2bc cos A', 'a² = b² + c² - 2bc cos A', 3,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'The Cosine Rule (find side) states: a² = b² + c² - 2bc cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, a = 7, b = 5, c = 8. Find cos A.', '√3/2', '1/2', '1/4', '3/4', 1,
'lc_hl_trigonometry', 10, 'advanced', 'lc_hl', 'cos A = (b² + c² - a²)/(2bc) = (25 + 64 - 49)/(80) = 40/80 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 9 and 9 and included angle 90°.', 'None of these', '81', '81/2', '40', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 9 × 9 × sin 90° = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '15', '13', '17', '12', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 7 and 8 and included angle 45°.', '56/2', '56√2/4', '28', '56', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 7 × 8 × sin 45° = 56√2/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 4 and 4 and included angle 30°.', '16/2', '4', '16', '8', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 4 × 4 × sin 30° = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 5 and 4 and included angle 30°.', '20/2', '10', '5', '20', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 5 × 4 × sin 30° = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 10 and 10 and included angle 30°.', '100', '100/2', '50', '25', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 10 × 10 × sin 30° = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 50m away, the angle of elevation to a tower top is 45°. Find the tower height.', '25 m', '50 m', '100 m', '50√2 m', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 45° = h/50, so h = 50 = 50 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 50m away, the angle of elevation to a tower top is 45°. Find the tower height.', '100 m', '50√2 m', '25 m', '50 m', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 45° = h/50, so h = 50 = 50 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '8', '12', '6', '7', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '15', '13', '12', '17', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '7', '12', '6', '8', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flagpole casts a shadow 20m long when the angle of elevation of the sun is 60°. Find the height.', '10√3 m', '40 m', '20 m', '20√3 m', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 60° = h/20, so h = 20 × tan 60° = 20√3 = 20√3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 50m away, the angle of elevation to a tower top is 45°. Find the tower height.', '50 m', '25 m', '50√2 m', '100 m', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 45° = h/50, so h = 50 = 50 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '20 km', '15 km', '10 km', '10√2 km', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 50m away, the angle of elevation to a tower top is 45°. Find the tower height.', '50√2 m', '50 m', '100 m', '25 m', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 45° = h/50, so h = 50 = 50 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '6', '7', '12', '8', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From 50m away, the angle of elevation to a tower top is 45°. Find the tower height.', '25 m', '100 m', '50√2 m', '50 m', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 45° = h/50, so h = 50 = 50 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '7', '12', '6', '8', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 4 and 5 and included angle 45°.', '20/2', '20', '20√2/4', '10', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 4 × 5 × sin 45° = 20√2/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '12', '6', '8', '7', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flagpole casts a shadow 20m long when the angle of elevation of the sun is 60°. Find the height.', '20√3 m', '20 m', '10√3 m', '40 m', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 60° = h/20, so h = 20 × tan 60° = 20√3 = 20√3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '20 km', '10 km', '10√2 km', '15 km', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '12', '15', '13', '17', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '7', '6', '8', '12', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '7', '6', '8', '12', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 8 and 4 and included angle 30°.', '16', '32', '8', '32/2', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 8 × 4 × sin 30° = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '17', '12', '15', '13', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 5 and 8 and included angle 90°.', 'None of these', '40', '40/2', '20', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 5 × 8 × sin 90° = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '10 km', '15 km', '10√2 km', '20 km', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 4. Find the length of a space diagonal.', '8', '4√3', '4√2', '12', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Space diagonal = √(4² + 4² + 4²) = √48 = 4√3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A cube has side 4. Find the length of a space diagonal.', '8', '12', '4√3', '4√2', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Space diagonal = √(4² + 4² + 4²) = √48 = 4√3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '10√2 km', '10 km', '20 km', '15 km', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 6 and 5 and included angle 45°.', '30/2', '15', '30√2/4', '30', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 6 × 5 × sin 45° = 30√2/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '12', '17', '15', '13', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flagpole casts a shadow 20m long when the angle of elevation of the sun is 60°. Find the height.', '40 m', '20 m', '20√3 m', '10√3 m', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'tan 60° = h/20, so h = 20 × tan 60° = 20√3 = 20√3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 5 and 4 and included angle 45°.', '20√2/4', '20/2', '20', '10', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 5 × 4 × sin 45° = 20√2/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 7 and 6 and included angle 30°.', '42', '42/2', '42/4', '21', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 7 × 6 × sin 30° = 42/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '12', '15', '13', '17', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '12', '8', '6', '7', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '13', '12', '15', '17', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '20 km', '10√2 km', '10 km', '15 km', 1,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '6', '12', '7', '8', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '10√2 km', '10 km', '20 km', '15 km', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '20 km', '15 km', '10√2 km', '10 km', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '10 km', '15 km', '20 km', '10√2 km', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '10√2 km', '10 km', '20 km', '15 km', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.', '15 km', '20 km', '10√2 km', '10 km', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'The angle between paths is 90°. Using Pythagoras: d = √(100 + 100) = 10√2 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A rectangular box has dimensions 3×4×12. Find the space diagonal.', '13', '15', '12', '17', 0,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Diagonal = √(9 + 16 + 144) = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of a triangle with sides 3, 4, 5.', '8', '12', '6', '7', 2,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Using Heron''s formula: Area = √(6×3×2×1) = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of triangle with sides 7 and 8 and included angle 90°.', '56', '56/2', 'None of these', '28', 3,
'lc_hl_trigonometry', 11, 'advanced', 'lc_hl', 'Area = ½ab sin C = ½ × 7 × 8 × sin 90° = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, a tower has angle of elevation 30°. From B, 100m closer, it''s 60°. Find tower height.', '100√3 m', '50√3 m', '100 m', '50 m', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan relationships. Answer = 50√3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', 'sin A + cos A = 1', 'tan A = sin A / cos A only', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'cot A = 1', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '√2 - 1', '√2 + 1', '1/√2', '2 - √2', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'sin A + cos A = 1', 'cot A = 1', 'tan A = sin A / cos A only', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of 5 - 3cos x', '-3', '8', '5', '2', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos x has max 1, so minimum is 5 - 3(1) = 2. Answer = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of 5 - 3cos x', '5', '-3', '8', '2', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos x has max 1, so minimum is 5 - 3(1) = 2. Answer = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '1/√2', '√2 - 1', '√2 + 1', '2 - √2', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express cos 3A in terms of cos A:', 'cos³A - 3 cos A', '4 cos³A - 3 cos A', '3 cos A - 4 cos³A', '4 cos³A + 3 cos A', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos 3A in terms of cos A = 4 cos³A - 3 cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'sin A + cos A = 1', 'tan A = sin A / cos A only', 'cot A = 1', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', 'sin A + cos A = 1', 'cot A = 1', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'tan A = sin A / cos A only', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2sin²x + sinx - 1 = 0 for 0° ≤ x < 360°', '60°, 300°', '30°, 150°, 270°', '45°, 135°, 225°, 315°', '30°, 150°', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2sinx - 1)(sinx + 1) = 0, so sinx = 1/2 or sinx = -1. Solutions: 30°, 150°, 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '2 - √2', '√2 - 1', '√2 + 1', '1/√2', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '2 - √2', '√2 - 1', '√2 + 1', '1/√2', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of 5 - 3cos x', '8', '5', '2', '-3', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos x has max 1, so minimum is 5 - 3(1) = 2. Answer = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, a tower has angle of elevation 30°. From B, 100m closer, it''s 60°. Find tower height.', '100 m', '50√3 m', '100√3 m', '50 m', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan relationships. Answer = 50√3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 3A in terms of sin A:', 'sin³A - 3 sin A', '3 sin A + 4 sin³A', '3 sin A - 4 sin³A', '4 sin³A - 3 sin A', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'sin 3A in terms of sin A = 3 sin A - 4 sin³A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '2 - √2', '√2 + 1', '1/√2', '√2 - 1', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', 'sin A + cos A = 1', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'cot A = 1', 'tan A = sin A / cos A only', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of 3sin x + 4cos x', '4', '7', '5', '3', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'R sin(x + α) form where R = √(9+16) = 5. Answer = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2sin²x + sinx - 1 = 0 for 0° ≤ x < 360°', '45°, 135°, 225°, 315°', '60°, 300°', '30°, 150°, 270°', '30°, 150°', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2sinx - 1)(sinx + 1) = 0, so sinx = 1/2 or sinx = -1. Solutions: 30°, 150°, 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2cos²x - cosx - 1 = 0 for 0° ≤ x < 360°', '0°, 180°', '90°, 270°', '0°, 120°, 240°', '60°, 300°', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2cosx + 1)(cosx - 1) = 0. Solutions: 0°, 120°, 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', 'sin A + cos A = 1', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'cot A = 1', 'tan A = sin A / cos A only', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '√2 - 1', '1/√2', '√2 + 1', '2 - √2', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '√2 - 1', '1/√2', '2 - √2', '√2 + 1', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '1/√2', '2 - √2', '√2 + 1', '√2 - 1', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 3A in terms of sin A:', '3 sin A + 4 sin³A', '3 sin A - 4 sin³A', 'sin³A - 3 sin A', '4 sin³A - 3 sin A', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'sin 3A in terms of sin A = 3 sin A - 4 sin³A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 3A in terms of sin A:', '3 sin A + 4 sin³A', '4 sin³A - 3 sin A', 'sin³A - 3 sin A', '3 sin A - 4 sin³A', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'sin 3A in terms of sin A = 3 sin A - 4 sin³A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '√2 - 1', '√2 + 1', '2 - √2', '1/√2', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', 'cot A = 1', 'tan A = sin A / cos A only', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'sin A + cos A = 1', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of 5 - 3cos x', '-3', '8', '5', '2', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos x has max 1, so minimum is 5 - 3(1) = 2. Answer = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2sin²x + sinx - 1 = 0 for 0° ≤ x < 360°', '60°, 300°', '30°, 150°, 270°', '30°, 150°', '45°, 135°, 225°, 315°', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2sinx - 1)(sinx + 1) = 0, so sinx = 1/2 or sinx = -1. Solutions: 30°, 150°, 270°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '2 - √2', '√2 + 1', '√2 - 1', '1/√2', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', 'tan A = sin A / cos A only', 'cot A = 1', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'sin A + cos A = 1', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', 'tan A = sin A / cos A only', 'sin A + cos A = 1', 'cot A = 1', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the maximum value of 3sin x + 4cos x', '4', '7', '3', '5', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'R sin(x + α) form where R = √(9+16) = 5. Answer = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2cos²x - cosx - 1 = 0 for 0° ≤ x < 360°', '60°, 300°', '90°, 270°', '0°, 180°', '0°, 120°, 240°', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2cosx + 1)(cosx - 1) = 0. Solutions: 0°, 120°, 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From point A, a tower has angle of elevation 30°. From B, 100m closer, it''s 60°. Find tower height.', '100 m', '100√3 m', '50√3 m', '50 m', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan relationships. Answer = 50√3 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '√2 + 1', '1/√2', '√2 - 1', '2 - √2', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '1/√2', '2 - √2', '√2 - 1', '√2 + 1', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '√2 + 1', '2 - √2', '1/√2', '√2 - 1', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the minimum value of 5 - 3cos x', '-3', '5', '8', '2', 3,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos x has max 1, so minimum is 5 - 3(1) = 2. Answer = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2cos²x - cosx - 1 = 0 for 0° ≤ x < 360°', '90°, 270°', '60°, 300°', '0°, 120°, 240°', '0°, 180°', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2cosx + 1)(cosx - 1) = 0. Solutions: 0°, 120°, 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express cos 3A in terms of cos A:', '4 cos³A - 3 cos A', '4 cos³A + 3 cos A', 'cos³A - 3 cos A', '3 cos A - 4 cos³A', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos 3A in terms of cos A = 4 cos³A - 3 cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of 2 + 3sin x', '[-1, 5]', '[2, 5]', '[-1, 3]', '[-3, 3]', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '-1 ≤ sin x ≤ 1, so -1 ≤ 2 + 3sin x ≤ 5. Answer = [-1, 5]', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2cos²x - cosx - 1 = 0 for 0° ≤ x < 360°', '60°, 300°', '0°, 120°, 240°', '90°, 270°', '0°, 180°', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2cosx + 1)(cosx - 1) = 0. Solutions: 0°, 120°, 240°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove tan A + cot A = sec A csc A, the key step is:', '(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 'cot A = 1', 'tan A = sin A / cos A only', 'sin A + cos A = 1', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'The key step: (sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the exact value of tan 22.5°.', '√2 + 1', '√2 - 1', '1/√2', '2 - √2', 1,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'Using tan 45° = 2tan22.5°/(1-tan²22.5°): tan 22.5° = √2 - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express cos 3A in terms of cos A:', '4 cos³A - 3 cos A', '3 cos A - 4 cos³A', '4 cos³A + 3 cos A', 'cos³A - 3 cos A', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'cos 3A in terms of cos A = 4 cos³A - 3 cos A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Express sin 3A in terms of sin A:', '3 sin A - 4 sin³A', 'sin³A - 3 sin A', '4 sin³A - 3 sin A', '3 sin A + 4 sin³A', 0,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', 'sin 3A in terms of sin A = 3 sin A - 4 sin³A', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Solve: 2sin²x + sinx - 1 = 0 for 0° ≤ x < 360°', '30°, 150°', '60°, 300°', '30°, 150°, 270°', '45°, 135°, 225°, 315°', 2,
'lc_hl_trigonometry', 12, 'advanced', 'lc_hl', '(2sinx - 1)(sinx + 1) = 0, so sinx = 1/2 or sinx = -1. Solutions: 30°, 150°, 270°', 1);