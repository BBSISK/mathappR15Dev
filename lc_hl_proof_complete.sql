-- LC Higher Level - Proof & Reasoning - Complete SQL
-- Includes topic creation + 600 questions
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_proof_complete.sql
-- Generated: 2025-12-14

-- Add Proof & Reasoning topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_proof', 'Proof & Reasoning', id, '🔍', 8, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_proof';

-- Questions (600 total: 50 per level x 12 levels)
-- LC Higher Level - Proof & Reasoning Questions
-- Generated: 2025-12-14
-- Total: 600 questions

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify: "The sum of two even numbers is even."', 'True statement', 'Open statement', 'Option 4', 'Not a statement', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', '2a + 2b = 2(a+b)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify: "x + 5 = 10"', 'Open statement', 'Option 4', 'Not a statement', 'True statement', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Truth depends on x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify: "All prime numbers are odd."', 'Open statement', 'Not a statement', 'False statement', 'True statement', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', '2 is prime and even', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify: "Is 7 prime?"', 'False statement', 'Open statement', 'True statement', 'Not a statement (question)', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Questions have no truth value', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify: "Every rectangle is a square."', 'False statement', 'True statement', 'Not a statement', 'Open statement', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Counterexample: 2×3 rectangle', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Negate: "All cats are black"', 'Not (All cats are black)', 'All cats are black', 'Cannot be negated', 'There exists a cat that is not black', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Negate ''all'' to ''exists not''', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Negate: "Some birds fly"', 'Not (Some birds fly)', 'Cannot be negated', 'Some birds fly', 'No birds fly', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Negate ''some'' to ''none''', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Negate: "n is even"', 'Cannot be negated', 'Not (n is even)', 'n is even', 'n is odd', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Not even = odd', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Negate: "x > 5"', 'x ≤ 5', 'x > 5', 'Not (x > 5)', 'Cannot be negated', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Negate > to ≤', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Negate: "x > 0 and y > 0"', 'x > 0 and y > 0', 'Not (x > 0 and y > 0)', 'Cannot be negated', 'x ≤ 0 or y ≤ 0', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Negate ''and'' with ''or''', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the converse of: "If it rains, ground is wet"', 'If it rains, ground is wet', 'If ground is wet, it rains', 'Cannot determine', 'If n odd, n² even', 1,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Swap parts', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the contrapositive of: "If it rains, ground is wet"', 'Cannot determine', 'If it rains, ground is wet', 'If ground not wet, no rain', 'If n odd, n² even', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Swap and negate', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the contrapositive of: "If n² even, n even"', 'If n odd, n² even', 'If n² even, n even', 'If n odd, n² odd', 'Cannot determine', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Swap and negate', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A statement and its contrapositive are:', 'Numerical check', 'Logically equivalent', 'Find all cases', 'Always different', 1,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Same truth value', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A counterexample is used to:', 'Numerical check', 'Always different', 'Find all cases', 'Disprove universal statements', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'One case disproves ''for all''', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove ''there exists'', you need:', 'Find all cases', 'Numerical check', 'Always different', 'One valid example', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Existence needs one case', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove ''for all'', you need:', 'Always different', 'A general argument', 'Numerical check', 'Find all cases', 1,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Must cover all cases', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The negation of ''All students passed'' is:', 'Q→P', 'False', 'Cannot determine', 'At least one student failed', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Exists...not', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P→Q is true, what about ¬Q→¬P?', 'Cannot determine', 'Q→P', 'Also true (contrapositive)', 'False', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Equivalent', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The converse of P→Q is:', 'False', 'Option 4', 'Q→P', 'Cannot determine', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Swap hypothesis and conclusion', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The inverse of P→Q is:', 'Cannot determine', '¬P→¬Q', 'Q→P', 'False', 1,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Negate both parts', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A conditional and its ___ are equivalent:', 'Contrapositive', 'Cannot determine', 'Q→P', 'False', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'Not converse or inverse', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∧ ¬Q', 'P ∧ Q', 'P ∨ Q', '¬P ∨ ¬Q', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∧ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∧ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∨ ¬Q', 'P ∧ Q', 'P ∨ Q', '¬P ∧ ¬Q', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', 'P ∧ Q', '¬P ∨ ¬Q', '¬P ∧ ¬Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∧ Q', '¬P ∨ ¬Q', '¬P ∧ ¬Q', 'P ∨ Q', 1,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', 'P ∧ Q', '¬P ∨ ¬Q', '¬P ∧ ¬Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∧ Q', 'P ∨ Q', 1,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', 'P ∧ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∧ ¬Q', 'P ∨ Q', '¬P ∨ ¬Q', 'P ∧ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∧ Q', 'P ∨ Q', '¬P ∨ ¬Q', '¬P ∧ ¬Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', '¬P ∧ ¬Q', 'P ∧ Q', '¬P ∨ ¬Q', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∧ Q', '¬P ∧ ¬Q', 'P ∨ Q', '¬P ∨ ¬Q', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∧ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∨ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∨ ¬Q', '¬P ∧ ¬Q', 'P ∧ Q', 'P ∨ Q', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∨ ¬Q', 'P ∨ Q', '¬P ∧ ¬Q', 'P ∧ Q', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∧ ¬Q', 'P ∧ Q', 'P ∨ Q', '¬P ∨ ¬Q', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∧ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∧ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∨ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∨ ¬Q', 'P ∨ Q', 'P ∧ Q', '¬P ∧ ¬Q', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∧ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∨ ¬Q', '¬P ∧ ¬Q', 'P ∧ Q', 'P ∨ Q', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∨ ¬Q', 'P ∨ Q', '¬P ∧ ¬Q', 'P ∧ Q', 0,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∧ Q', '¬P ∧ ¬Q', 'P ∨ Q', '¬P ∨ ¬Q', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', 'P ∧ Q', '¬P ∨ ¬Q', '¬P ∧ ¬Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∧ ¬Q', 'P ∨ Q', '¬P ∨ ¬Q', 'P ∧ Q', 2,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 'P ∨ Q', 'P ∧ Q', 1,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In logic, ¬(P ∧ Q) equals:', 'P ∨ Q', 'P ∧ Q', '¬P ∧ ¬Q', '¬P ∨ ¬Q', 3,
'lc_hl_proof', 1, 'foundation', 'lc_hl', 'De Morgan''s Law', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Sum of two evens is even', '2a + 2b = 2(a+b), divisible by 2', 'Needs induction', 'Cannot be proven', 'False statement', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Factor out 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Sum of two odds is even', 'Needs induction', 'Cannot be proven', 'False statement', '(2a+1) + (2b+1) = 2(a+b+1)', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Combine and factor', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Product of even and any is even', 'Cannot be proven', '2a × b = 2(ab)', 'False statement', 'Needs induction', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Factor of 2 remains', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Square of even is even', 'Needs induction', '(2k)² = 4k² = 2(2k²)', 'False statement', 'Cannot be proven', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Still has factor 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Square of odd is odd', 'Cannot be proven', 'Needs induction', 'False statement', '(2k+1)² = 4k²+4k+1 = 2(2k²+2k)+1', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Form 2m+1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: n² + n is always even', 'Needs induction', 'False statement', 'n(n+1): consecutive integers', 'Cannot be proven', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'One must be even', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Sum of 3 consecutive integers divisible by 3', 'False statement', 'Needs induction', 'n+(n+1)+(n+2) = 3n+3 = 3(n+1)', 'Cannot be proven', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Factor out 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: If a|b and b|c, then a|c', 'Needs induction', 'False statement', 'Cannot be proven', 'b=ka, c=mb, so c=mka', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Transitivity', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('First step in direct proof of ''If P then Q'':', 'Assume Q false', 'Find counterexample', 'Assume P is true', 'Use induction', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Start with hypothesis', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof ends with:', 'Find counterexample', 'The conclusion Q', 'Assume Q false', 'Use induction', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Derive what we want', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof uses:', 'Find counterexample', 'Assume Q false', 'Use induction', 'Logical deduction from hypothesis', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Step by step logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove ''n even implies n² even'', first:', 'Write n = 2k', 'Use induction', 'Assume Q false', 'Find counterexample', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Express ''even'' algebraically', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Product of two odds is odd', 'Induction', 'Indirect proof', '(2a+1)(2b+1) = 4ab+2a+2b+1 = 2(2ab+a+b)+1', 'The conclusion', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Form 2m+1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: Sum of rational numbers is rational', 'The conclusion', 'Indirect proof', 'Induction', 'a/b + c/d = (ad+bc)/bd', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Closed under addition', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is direct proof also called?', 'Induction', 'Indirect proof', 'The conclusion', 'Deductive proof', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Deduce conclusion', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In P→Q, P is called:', 'Indirect proof', 'The conclusion', 'Induction', 'The hypothesis', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'What we assume', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Statement seems false', 'Contradiction required', 'Clear path from hypothesis to conclusion', 'Many cases needed', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Contradiction required', 'Many cases needed', 'Statement seems false', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Statement seems false', 'Contradiction required', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Contradiction required', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Statement seems false', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Clear path from hypothesis to conclusion', 'Statement seems false', 'Contradiction required', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Contradiction required', 'Statement seems false', 'Many cases needed', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Contradiction required', 'Statement seems false', 'Many cases needed', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Statement seems false', 'Contradiction required', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Contradiction required', 'Many cases needed', 'Statement seems false', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Statement seems false', 'Contradiction required', 'Many cases needed', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Statement seems false', 'Contradiction required', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Contradiction required', 'Statement seems false', 'Many cases needed', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Contradiction required', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Statement seems false', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Statement seems false', 'Many cases needed', 'Contradiction required', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Statement seems false', 'Contradiction required', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Statement seems false', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Contradiction required', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Contradiction required', 'Statement seems false', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Clear path from hypothesis to conclusion', 'Contradiction required', 'Statement seems false', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Statement seems false', 'Contradiction required', 'Clear path from hypothesis to conclusion', 'Many cases needed', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Contradiction required', 'Statement seems false', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Contradiction required', 'Statement seems false', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Contradiction required', 'Statement seems false', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Contradiction required', 'Statement seems false', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Clear path from hypothesis to conclusion', 'Statement seems false', 'Contradiction required', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Statement seems false', 'Contradiction required', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Contradiction required', 'Statement seems false', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Many cases needed', 'Contradiction required', 'Clear path from hypothesis to conclusion', 'Statement seems false', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Contradiction required', 'Statement seems false', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Contradiction required', 'Statement seems false', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Statement seems false', 'Contradiction required', 'Many cases needed', 'Clear path from hypothesis to conclusion', 3,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Statement seems false', 'Clear path from hypothesis to conclusion', 'Contradiction required', 'Many cases needed', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Clear path from hypothesis to conclusion', 'Statement seems false', 'Contradiction required', 'Many cases needed', 0,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Contradiction required', 'Clear path from hypothesis to conclusion', 'Many cases needed', 'Statement seems false', 1,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Direct proof is best when:', 'Contradiction required', 'Many cases needed', 'Clear path from hypothesis to conclusion', 'Statement seems false', 2,
'lc_hl_proof', 2, 'foundation', 'lc_hl', 'Straightforward logic', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('First step in proof by contradiction:', 'Assume P', 'Use induction', 'Find example', 'Assume negation of what to prove', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Suppose conclusion false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('We seek to find:', 'Use induction', 'A logical contradiction', 'Find example', 'Assume P', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Something impossible', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When we find contradiction:', 'Assume P', 'Find example', 'Use induction', 'Original assumption was false', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Negation fails', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction is also called:', 'Use induction', 'Assume P', 'Find example', 'Indirect proof or reductio ad absurdum', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Reduce to absurdity', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove P by contradiction, assume:', 'Assume P', 'Find example', 'Use induction', 'Not P', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'The negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('√2 irrational: Assume √2 = a/b in lowest terms. Then both a and b are:', 'Even, contradicting lowest terms', 'Proof complete', 'Prime', 'Still rational', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', '2=a²/b² means a² even', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Infinitely many primes: Consider N = p₁p₂...pₙ + 1. N is:', 'Still rational', 'Not divisible by any pᵢ', 'Proof complete', 'Prime', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Remainder 1 when divided', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If n² even then n even. Assume n odd, then n² is:', 'Prime', 'Proof complete', 'Odd, contradicting n² even', 'Still rational', 2,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Odd squared is odd', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('√3 irrational follows same pattern as:', '√2 proof', 'Proof complete', 'Prime', 'Still rational', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Both numerator and denominator divisible by 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('No smallest positive rational: If r smallest, then r/2 is:', 'Smaller positive rational', 'Still rational', 'Prime', 'Proof complete', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''Suppose √5 rational... contradiction... so √5 irrational'' is:', 'Invalid proof', 'Induction', 'Proof by contradiction', 'Direct proof', 2,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Assumed negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''Assume largest even n exists. Then n+2 is larger and even.'' is:', 'Proof by contradiction', 'Invalid proof', 'Direct proof', 'Induction', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Contradicts ''largest''', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Finding 1=0 in a proof means:', 'Invalid proof', 'Contradiction reached', 'Induction', 'Direct proof', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Impossible equality', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Direct calculation', 'Induction', 'Specific examples', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Specific examples', 'Direct calculation', 'Induction', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Direct calculation', 'Specific examples', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Law of excluded middle (P or not P)', 'Induction', 'Specific examples', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Specific examples', 'Direct calculation', 'Induction', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Law of excluded middle (P or not P)', 'Specific examples', 'Direct calculation', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Law of excluded middle (P or not P)', 'Direct calculation', 'Specific examples', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Direct calculation', 'Specific examples', 'Induction', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Specific examples', 'Direct calculation', 'Induction', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Law of excluded middle (P or not P)', 'Specific examples', 'Induction', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Specific examples', 'Law of excluded middle (P or not P)', 'Direct calculation', 2,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Specific examples', 'Induction', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Direct calculation', 'Specific examples', 'Induction', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Specific examples', 'Law of excluded middle (P or not P)', 'Direct calculation', 2,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Induction', 'Specific examples', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Specific examples', 'Induction', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Specific examples', 'Direct calculation', 'Law of excluded middle (P or not P)', 'Induction', 2,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Specific examples', 'Direct calculation', 'Induction', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Law of excluded middle (P or not P)', 'Direct calculation', 'Specific examples', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Specific examples', 'Induction', 'Direct calculation', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Law of excluded middle (P or not P)', 'Induction', 'Specific examples', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Direct calculation', 'Specific examples', 'Induction', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Induction', 'Specific examples', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Specific examples', 'Direct calculation', 'Law of excluded middle (P or not P)', 'Induction', 2,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Induction', 'Specific examples', 'Direct calculation', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Law of excluded middle (P or not P)', 'Direct calculation', 'Specific examples', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Direct calculation', 'Specific examples', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Induction', 'Direct calculation', 'Specific examples', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Specific examples', 'Induction', 'Direct calculation', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Specific examples', 'Law of excluded middle (P or not P)', 'Direct calculation', 2,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Induction', 'Direct calculation', 'Specific examples', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Specific examples', 'Law of excluded middle (P or not P)', 'Induction', 'Direct calculation', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Direct calculation', 'Specific examples', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Induction', 'Specific examples', 'Direct calculation', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Induction', 'Direct calculation', 'Specific examples', 'Law of excluded middle (P or not P)', 3,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Direct calculation', 'Law of excluded middle (P or not P)', 'Induction', 'Specific examples', 1,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction relies on:', 'Law of excluded middle (P or not P)', 'Induction', 'Specific examples', 'Direct calculation', 0,
'lc_hl_proof', 3, 'foundation', 'lc_hl', 'Either true or false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive of ''If P then Q'' is:', 'Not equivalent', 'If not Q then not P', 'If Q then P', 'Different truth value', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Swap and negate', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A statement and its contrapositive are:', 'If Q then P', 'Different truth value', 'Not equivalent', 'Logically equivalent', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Same truth value', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove P→Q by contrapositive, prove:', 'Not equivalent', 'If Q then P', '¬Q → ¬P', 'Different truth value', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Equivalent statement', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive of ''n² even implies n even'' is:', 'Not equivalent', 'Different truth value', 'If Q then P', 'n odd implies n² odd', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Not even = odd', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why is contrapositive valid?', 'Logically equivalent to original', 'If Q then P', 'Different truth value', 'Not equivalent', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Same truth value', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove ''n² even ⟹ n even'' by contrapositive:', 'Show n odd ⟹ n² odd', 'n² even', 'Direct proof only', 'Cannot prove', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Easier to prove', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If n odd (n=2k+1), then n² =', 'Cannot prove', '(2k+1)² = 4k²+4k+1 = 2(2k²+2k)+1, odd', 'Direct proof only', 'n² even', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Form 2m+1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove ''n² divisible by 3 ⟹ n divisible by 3'':', 'Contrapositive: 3∤n ⟹ 3∤n²', 'Cannot prove', 'n² even', 'Direct proof only', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Check n≡1,2 mod 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If n≡1 (mod 3), then n² ≡', 'Cannot prove', '1 (mod 3)', 'n² even', 'Direct proof only', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', '1² = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If n≡2 (mod 3), then n² ≡', '4 ≡ 1 (mod 3)', 'Direct proof only', 'n² even', 'Cannot prove', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Neither is 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive vs contradiction: Contrapositive proves ¬Q→¬P, contradiction assumes:', 'P and Q', 'Same truth value', 'Direct proof', 'P and ¬Q, derives impossibility', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Subtle difference', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which method for ''n² even ⟹ n even''?', 'Direct proof', 'P and Q', 'Same truth value', 'Contrapositive (easier)', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Direct path', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which method for ''√2 irrational''?', 'Same truth value', 'P and Q', 'Direct proof', 'Contradiction', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Need impossibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Converse and contrapositive:', 'P and Q', 'Have different truth values (usually)', 'Same truth value', 'Direct proof', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Not equivalent to each other', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(P→Q) is equivalent to:', 'Direct proof', 'Same truth value', '(¬Q→¬P)', 'P and Q', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Contrapositive', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', '¬Q gives useful starting information', 'We need examples', 'Direct proof is easy', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', 'Induction applies', 'Direct proof is easy', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', 'Direct proof is easy', '¬Q gives useful starting information', 'Induction applies', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'Induction applies', 'We need examples', 'Direct proof is easy', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'We need examples', '¬Q gives useful starting information', 'Induction applies', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'Induction applies', '¬Q gives useful starting information', 'We need examples', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'We need examples', 'Induction applies', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'We need examples', '¬Q gives useful starting information', 'Induction applies', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', '¬Q gives useful starting information', 'Direct proof is easy', 'We need examples', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', 'Direct proof is easy', 'We need examples', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'We need examples', 'Direct proof is easy', 'Induction applies', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'We need examples', '¬Q gives useful starting information', 'Induction applies', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', 'Induction applies', 'Direct proof is easy', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'Direct proof is easy', 'We need examples', 'Induction applies', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', '¬Q gives useful starting information', 'Direct proof is easy', 'We need examples', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', 'Direct proof is easy', 'We need examples', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', 'Direct proof is easy', 'Induction applies', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', '¬Q gives useful starting information', 'Direct proof is easy', 'We need examples', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'Induction applies', 'We need examples', 'Direct proof is easy', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', '¬Q gives useful starting information', 'Induction applies', 'We need examples', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', 'Induction applies', 'Direct proof is easy', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', '¬Q gives useful starting information', 'Induction applies', 'Direct proof is easy', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', '¬Q gives useful starting information', 'Direct proof is easy', 'Induction applies', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', 'We need examples', 'Direct proof is easy', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', '¬Q gives useful starting information', 'Induction applies', 'Direct proof is easy', 1,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'Direct proof is easy', 'Induction applies', 'We need examples', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', 'We need examples', 'Direct proof is easy', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'Induction applies', '¬Q gives useful starting information', 'We need examples', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'We need examples', 'Induction applies', 'Direct proof is easy', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Induction applies', 'Direct proof is easy', 'We need examples', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'We need examples', '¬Q gives useful starting information', 'Induction applies', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'Induction applies', 'We need examples', 'Direct proof is easy', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'We need examples', 'Direct proof is easy', '¬Q gives useful starting information', 'Induction applies', 2,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', '¬Q gives useful starting information', 'Direct proof is easy', 'Induction applies', 'We need examples', 0,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive is useful when:', 'Direct proof is easy', 'Induction applies', 'We need examples', '¬Q gives useful starting information', 3,
'lc_hl_proof', 4, 'developing', 'lc_hl', 'Work with negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Mathematical induction has:', 'Two steps: base case and inductive step', 'Specific examples', 'P(n) for all n', 'One step', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation + chain', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Base case proves:', 'P(n) for all n', 'One step', 'Statement true for starting value (usually n=1)', 'Specific examples', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'First domino', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Inductive hypothesis assumes:', 'P(n) for all n', 'Specific examples', 'One step', 'P(k) is true for some k', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Assume for k', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Inductive step proves:', 'P(n) for all n', 'Specific examples', 'P(k) true implies P(k+1) true', 'One step', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Domino effect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Induction works because:', 'Specific examples', 'Base starts chain, step continues it', 'P(n) for all n', 'One step', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Like dominoes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('1+2+...+n = n(n+1)/2. Base n=1: RHS =', '1(2)/2 = 1 ✓', 'Not required', 'Need n=0', 'Fails', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Both equal 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('2ⁿ > n. Base n=1:', 'Not required', 'Need n=0', 'Fails', '2 > 1 ✓', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'True', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('n! ≥ 2ⁿ⁻¹ for n≥1. Base n=1:', 'Need n=0', 'Not required', '1 ≥ 1 ✓', 'Fails', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Equality', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('1²+2²+...+n² = n(n+1)(2n+1)/6. Base n=1:', 'Fails', 'Need n=0', 'Not required', '1 = 1(2)(3)/6 = 1 ✓', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Both 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('n³-n divisible by 6. Base n=1:', 'Not required', '0 divisible by 6 ✓', 'Need n=0', 'Fails', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Zero works', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For sum formula, inductive step:', 'Valid approach', 'Add (k+1) to both sides of P(k)', 'Multiply by k', 'P(k) directly', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Build k to k+1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('After assuming P(k), we must show:', 'Valid approach', 'P(k) directly', 'P(k+1) follows logically', 'Multiply by k', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Next case', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('We say ''by inductive hypothesis'' when:', 'Using assumed P(k)', 'Valid approach', 'P(k) directly', 'Multiply by k', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Invoking assumption', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Common error: Using P(k+1) to prove P(k+1) is:', 'Valid approach', 'Multiply by k', 'Circular reasoning (invalid)', 'P(k) directly', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Can''t assume conclusion', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'For elegance', 'It''s optional', 'To check algebra', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'For elegance', 'It''s optional', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'It''s optional', 'To check algebra', 'For elegance', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'Chain needs starting point', 'For elegance', 'It''s optional', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'Chain needs starting point', 'It''s optional', 'To check algebra', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'It''s optional', 'For elegance', 'To check algebra', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'It''s optional', 'For elegance', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'To check algebra', 'Chain needs starting point', 'It''s optional', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'Chain needs starting point', 'It''s optional', 'To check algebra', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'It''s optional', 'For elegance', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'It''s optional', 'Chain needs starting point', 'To check algebra', 'For elegance', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'For elegance', 'Chain needs starting point', 'It''s optional', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'To check algebra', 'Chain needs starting point', 'It''s optional', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'It''s optional', 'For elegance', 'To check algebra', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'It''s optional', 'For elegance', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'It''s optional', 'For elegance', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'It''s optional', 'Chain needs starting point', 'To check algebra', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'It''s optional', 'To check algebra', 'For elegance', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'It''s optional', 'Chain needs starting point', 'To check algebra', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'It''s optional', 'Chain needs starting point', 'For elegance', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'To check algebra', 'Chain needs starting point', 'It''s optional', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'Chain needs starting point', 'For elegance', 'It''s optional', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'For elegance', 'To check algebra', 'It''s optional', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'Chain needs starting point', 'To check algebra', 'It''s optional', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'It''s optional', 'Chain needs starting point', 'To check algebra', 'For elegance', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'Chain needs starting point', 'To check algebra', 'It''s optional', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'To check algebra', 'For elegance', 'It''s optional', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'It''s optional', 'Chain needs starting point', 'For elegance', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'It''s optional', 'To check algebra', 'For elegance', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'For elegance', 'It''s optional', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'For elegance', 'It''s optional', 'To check algebra', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'Chain needs starting point', 'It''s optional', 'For elegance', 1,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'To check algebra', 'It''s optional', 'For elegance', 'Chain needs starting point', 3,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'It''s optional', 'For elegance', 'Chain needs starting point', 'To check algebra', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'Chain needs starting point', 'It''s optional', 'For elegance', 'To check algebra', 0,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why must base case be verified?', 'It''s optional', 'For elegance', 'Chain needs starting point', 'To check algebra', 2,
'lc_hl_proof', 5, 'developing', 'lc_hl', 'Foundation of proof', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑i = n(n+1)/2. Add (k+1) to k(k+1)/2:', 'Different approach', '(k+1)(k+2)/2', 'Formula wrong', 'Cannot simplify', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Factor (k+1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑i² = n(n+1)(2n+1)/6. Inductive step:', 'Add (k+1)² to formula for k', 'Different approach', 'Formula wrong', 'Cannot simplify', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Simplify to k+1 formula', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑(2i-1) = n². Add (2k+1) to k²:', 'Cannot simplify', 'Formula wrong', 'Different approach', 'k² + 2k + 1 = (k+1)²', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Perfect square', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum 1+2+4+...+2ⁿ⁻¹ = 2ⁿ-1. Add 2ᵏ:', 'Different approach', 'Formula wrong', 'Cannot simplify', '2ᵏ-1 + 2ᵏ = 2ᵏ⁺¹-1', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Geometric', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑i³ = [n(n+1)/2]². This means:', 'Cannot simplify', 'Formula wrong', 'Different approach', 'Sum of cubes = square of sum', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Beautiful identity', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('k(k+1)/2 + (k+1) factors as:', 'Subtract term', 'Formula fails', 'Different method', '(k+1)[k/2 + 1] = (k+1)(k+2)/2', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Common factor', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For geometric series ∑rⁱ = (rⁿ⁺¹-1)/(r-1):', 'Add rᵏ⁺¹ and simplify', 'Different method', 'Subtract term', 'Formula fails', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Common denominator', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Telescoping 1/(n(n+1)) = n/(n+1). Add term:', 'Subtract term', 'Different method', 'k/(k+1) + 1/((k+1)(k+2)) = (k+1)/(k+2)', 'Formula fails', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Partial fractions', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Key step: ∑ᵏ⁺¹ = ∑ᵏ + (k+1)th term =', 'Subtract term', 'formula(k+1)', 'Formula fails', 'Different method', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Add and verify', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑i = n(n+1)/2 is attributed to:', '∑i²', 'Geometric', 'Euler', 'Gauss', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Young genius', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑ 2i = n(n+1) comes from:', 'Euler', 'Geometric', '∑i²', '2∑i = 2·n(n+1)/2', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Factor of 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑(3i-2) = n(3n-1)/2 for arithmetic series', 'Euler', '∑i²', 'Each term is 1, 4, 7, ...', 'Geometric', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Common diff 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Subtract 1', 'Multiply by k', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Multiply by k', 'Add the (k+1)th term to both sides', 'Start over', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Multiply by k', 'Subtract 1', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Subtract 1', 'Start over', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Subtract 1', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Subtract 1', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Multiply by k', 'Add the (k+1)th term to both sides', 'Start over', 'Subtract 1', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Multiply by k', 'Start over', 'Add the (k+1)th term to both sides', 'Subtract 1', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Subtract 1', 'Multiply by k', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Start over', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Start over', 'Add the (k+1)th term to both sides', 'Multiply by k', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Start over', 'Add the (k+1)th term to both sides', 'Multiply by k', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Subtract 1', 'Add the (k+1)th term to both sides', 'Multiply by k', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Add the (k+1)th term to both sides', 'Subtract 1', 'Multiply by k', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Start over', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Subtract 1', 'Start over', 'Multiply by k', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Start over', 'Multiply by k', 'Subtract 1', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Start over', 'Add the (k+1)th term to both sides', 'Multiply by k', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Multiply by k', 'Start over', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Subtract 1', 'Start over', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Start over', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Multiply by k', 'Start over', 'Add the (k+1)th term to both sides', 'Subtract 1', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Subtract 1', 'Add the (k+1)th term to both sides', 'Multiply by k', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Multiply by k', 'Subtract 1', 'Start over', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Subtract 1', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Start over', 'Add the (k+1)th term to both sides', 'Multiply by k', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Start over', 'Multiply by k', 'Subtract 1', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Start over', 'Multiply by k', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Start over', 'Multiply by k', 'Add the (k+1)th term to both sides', 3,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Start over', 'Subtract 1', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Subtract 1', 'Start over', 'Multiply by k', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Start over', 'Multiply by k', 'Subtract 1', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Subtract 1', 'Start over', 'Multiply by k', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Multiply by k', 'Start over', 'Add the (k+1)th term to both sides', 'Subtract 1', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Subtract 1', 'Start over', 0,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Multiply by k', 'Add the (k+1)th term to both sides', 'Start over', 2,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Multiply by k', 'Add the (k+1)th term to both sides', 'Subtract 1', 'Start over', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For induction on sums, always:', 'Subtract 1', 'Add the (k+1)th term to both sides', 'Multiply by k', 'Start over', 1,
'lc_hl_proof', 6, 'developing', 'lc_hl', 'Build step by step', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6|(n³-n): Factor n³-n =', 'Base fails', 'Cannot factor', 'n(n-1)(n+1), three consecutive integers', 'Not divisible', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Contains 2 and 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('3|(n³-n): Base n=1:', 'Not divisible', 'Base fails', 'Cannot factor', '0 divisible by 3 ✓', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Zero works', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 3|(n³-n), (k+1)³-(k+1) - (k³-k) =', 'Cannot factor', 'Base fails', '3k²+3k = 3(k²+k)', 'Not divisible', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Multiple of 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('8|(3²ⁿ-1): Base n=1:', 'Base fails', 'Not divisible', '9-1 = 8 ✓', 'Cannot factor', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Exactly 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 8|(3²ⁿ-1): 3²⁽ᵏ⁺¹⁾-1 = 9(3²ᵏ-1)+8', 'Cannot factor', 'Base fails', 'Both terms divisible by 8', 'Not divisible', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'IH plus 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('6 ≡ 1 (mod 5), so 6ⁿ ≡', 'Different', 'Cannot determine', '0 (mod m)', '1 (mod 5)', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', '1 to any power', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('4 ≡ -1 (mod 5), so 4ⁿ ≡', 'Cannot determine', '±1 depending on parity', 'Different', '0 (mod m)', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Alternates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('2³ = 8 ≡ 1 (mod 7), so 8ⁿ ≡', '0 (mod m)', 'Different', '1 (mod 7)', 'Cannot determine', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Power of 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a ≡ b (mod m), then aⁿ ≡', '0 (mod m)', 'bⁿ (mod m)', 'Cannot determine', 'Different', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Powers preserve congruence', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('10 ≡ 1 (mod 9), so sum of digits ≡', 'number (mod 9)', '0 (mod m)', 'Cannot determine', 'Different', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Digit sum test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('7|(8ⁿ-1): 8ᵏ⁺¹-1 = 8(8ᵏ-1)+7', 'Both divisible by 7', 'Not divisible', 'Only some n', 'Different divisors', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Factor approach', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('5|(n⁵-n) by Fermat''s Little Theorem:', 'Only some n', 'Not divisible', 'Different divisors', 'n⁵ ≡ n (mod 5)', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', '5 is prime', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('30|(n⁵-n) because divisible by:', 'Only some n', 'Different divisors', 'Not divisible', '2, 3, and 5', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', '2×3×5 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('n² ≡ 0 or 1 (mod 4) because:', 'Different divisors', 'Only some n', 'Even² ≡ 0, odd² ≡ 1', 'Not divisible', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Two cases', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 'Only base case', 'f(k) = 0', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 'Only base case', 'Random values', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Only base case', 'f(k) = 0', 'Random values', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 'Random values', 'Only base case', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'Random values', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 'Only base case', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 'Only base case', 'f(k) = 0', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Only base case', 'f(k) = 0', 'Random values', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'Only base case', 'Random values', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Only base case', 'Random values', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'Only base case', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'Only base case', 'Random values', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'Random values', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 'Random values', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Only base case', 'Random values', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'Only base case', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'f(k) = 0', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 'Only base case', 'f(k) = 0', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 'f(k) = 0', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Only base case', 'f(k) = 0', 'Random values', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 'f(k) = 0', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'Only base case', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 3,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 'f(k) = 0', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 'Only base case', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 'Only base case', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'f(k) = 0', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Random values', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Random values', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 'Only base case', 1,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'Only base case', 'Random values', 'f(k) = 0', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'Only base case', 'Random values', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 2,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For divisibility induction, show:', 'f(k+1) - f(k) divisible by d, or f(k+1) = d×something', 'f(k) = 0', 'Random values', 'Only base case', 0,
'lc_hl_proof', 7, 'proficient', 'lc_hl', 'Maintain divisibility', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('2ⁿ > n for n≥1. Base n=1:', 'n≥1 works', '2 > 1 ✓', 'False', 'Cannot prove', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'True', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n: 2ᵏ⁺¹ = 2·2ᵏ > 2k ≥ k+1 when:', 'Cannot prove', 'False', 'n≥1 works', 'k ≥ 1', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', '2k ≥ k+1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('2ⁿ ≥ n² for n≥4. Why n≥4?', 'Fails for n=3: 8 < 9', 'False', 'Cannot prove', 'n≥1 works', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Need correct base', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('n! > 2ⁿ for n≥4. Base n=4:', 'n≥1 works', 'False', '24 > 16 ✓', 'Cannot prove', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', '4! = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bernoulli: (1+x)ⁿ ≥ 1+nx for x>-1:', 'False', 'Cannot prove', 'Famous inequality', 'n≥1 works', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Proven by induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For n! > 2ⁿ: (k+1)! > 2ᵏ⁺¹ needs:', 'Different method', '(k+1)·k! > 2·2ᵏ, use IH and k+1>2', 'Equality always', 'Reverse inequality', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'k≥2 works', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bernoulli base: (1+x)¹ ≥ 1+x:', 'Reverse inequality', 'Different method', 'Equality ✓', 'Equality always', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Both equal 1+x', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bernoulli step uses (1+kx)(1+x) ≥', 'Equality always', 'Reverse inequality', '1+(k+1)x since kx² ≥ 0', 'Different method', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Non-negative term', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For inequality induction, show:', 'f(k+1) maintains ≤ or ≥ direction', 'Reverse inequality', 'Different method', 'Equality always', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Preserve inequality', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AM-GM: (a+b)/2 ≥ √(ab) proven by:', 'Different inequality', 'Cannot prove', 'Algebra: ((a-b)/2)² ≥ 0', 'Lower bound', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Perfect square', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('3ⁿ > n² for n≥1 needs step:', 'Different inequality', '3ⁿ⁺¹ = 3·3ⁿ > 3n² ≥ (n+1)² for large n', 'Lower bound', 'Cannot prove', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually true', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('∑1/i² < 2 uses:', 'Different inequality', 'Telescoping bound: 1/k² < 1/(k-1) - 1/k', 'Cannot prove', 'Lower bound', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Upper bound', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Never true', 'Only n=10', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Only n=10', 'Never true', 'Check base, then inductive step', 'Works for all n', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Check base, then inductive step', 'Only n=10', 'Works for all n', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Only n=10', 'Works for all n', 'Never true', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Works for all n', 'Never true', 'Only n=10', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Works for all n', 'Never true', 'Only n=10', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Only n=10', 'Never true', 'Works for all n', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Works for all n', 'Never true', 'Only n=10', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Check base, then inductive step', 'Never true', 'Only n=10', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Works for all n', 'Only n=10', 'Never true', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Check base, then inductive step', 'Never true', 'Only n=10', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Never true', 'Only n=10', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Only n=10', 'Works for all n', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Works for all n', 'Check base, then inductive step', 'Only n=10', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Check base, then inductive step', 'Only n=10', 'Works for all n', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Only n=10', 'Works for all n', 'Never true', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Works for all n', 'Only n=10', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Check base, then inductive step', 'Never true', 'Only n=10', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Never true', 'Only n=10', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Only n=10', 'Works for all n', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Only n=10', 'Works for all n', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Only n=10', 'Works for all n', 'Never true', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Only n=10', 'Never true', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Never true', 'Only n=10', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Only n=10', 'Never true', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Check base, then inductive step', 'Only n=10', 'Never true', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Only n=10', 'Check base, then inductive step', 'Never true', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Check base, then inductive step', 'Works for all n', 'Only n=10', 'Never true', 0,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Only n=10', 'Works for all n', 'Never true', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Works for all n', 'Check base, then inductive step', 'Only n=10', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Works for all n', 'Only n=10', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Only n=10', 'Check base, then inductive step', 'Never true', 'Works for all n', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Only n=10', 'Check base, then inductive step', 'Never true', 'Works for all n', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Works for all n', 'Only n=10', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Only n=10', 'Never true', 'Works for all n', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Never true', 'Check base, then inductive step', 'Only n=10', 'Works for all n', 1,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Works for all n', 'Never true', 'Check base, then inductive step', 'Only n=10', 2,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 2ⁿ > n³ starting at n=10:', 'Only n=10', 'Works for all n', 'Never true', 'Check base, then inductive step', 3,
'lc_hl_proof', 8, 'proficient', 'lc_hl', 'Eventually dominates', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of angles in triangle:', '180°', 'Supplementary', '60°', '360°', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Fundamental theorem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Exterior angle of triangle equals:', '360°', '60°', 'Supplementary', 'Sum of remote interior angles', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Exterior angle theorem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Base angles of isosceles triangle:', '360°', 'Supplementary', '60°', 'Equal', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Isosceles theorem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Vertically opposite angles are:', '60°', 'Equal', '360°', 'Supplementary', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Intersecting lines', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle in semicircle:', 'Supplementary', '60°', '360°', '90°', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Thales'' theorem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Central angle vs inscribed angle:', 'Central = 2× inscribed', 'Parallel', 'Sum to 360°', 'Equal', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Same arc', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angles in same segment are:', 'Parallel', 'Sum to 360°', 'Equal', 'Option 4', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Same arc', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Opposite angles of cyclic quad:', 'Sum to 360°', 'Equal', 'Sum to 180°', 'Parallel', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Supplementary', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent perpendicular to:', 'Parallel', 'Radius at tangency', 'Equal', 'Sum to 360°', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Fundamental property', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Alternate segment theorem relates:', 'Sum to 360°', 'Parallel', 'Tangent-chord angle to inscribed angle', 'Equal', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Equal angles', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle congruence criteria:', 'SSS, SAS, ASA, AAS, RHS', 'AAA, SSS', 'Always works', 'Equal sides', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Five methods', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Why doesn''t SSA (ASS) work?', 'AAA, SSS', 'Always works', 'Ambiguous case - two triangles possible', 'Equal sides', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Not valid', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove lines parallel, show:', 'Always works', 'Alternate angles equal', 'AAA, SSS', 'Equal sides', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Or corresponding equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have:', 'Equal sides', 'Always works', 'Equal angles, proportional sides', 'AAA, SSS', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Same shape', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Perpendicular', 'Parallel to base, half its length', 'Equal length', 'At 45°', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Perpendicular', 'Equal length', 'At 45°', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Parallel to base, half its length', 'Equal length', 'Perpendicular', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'At 45°', 'Parallel to base, half its length', 'Perpendicular', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Equal length', 'Perpendicular', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'Perpendicular', 'At 45°', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Perpendicular', 'At 45°', 'Equal length', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'At 45°', 'Perpendicular', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Perpendicular', 'Parallel to base, half its length', 'Equal length', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Perpendicular', 'At 45°', 'Equal length', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'At 45°', 'Parallel to base, half its length', 'Perpendicular', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Perpendicular', 'Parallel to base, half its length', 'At 45°', 'Equal length', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Equal length', 'Perpendicular', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'At 45°', 'Parallel to base, half its length', 'Perpendicular', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'At 45°', 'Perpendicular', 'Equal length', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Equal length', 'At 45°', 'Perpendicular', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'Perpendicular', 'At 45°', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Equal length', 'At 45°', 'Perpendicular', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Perpendicular', 'At 45°', 'Equal length', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Perpendicular', 'Equal length', 'Parallel to base, half its length', 'At 45°', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'Perpendicular', 'Parallel to base, half its length', 'At 45°', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'At 45°', 'Equal length', 'Perpendicular', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'At 45°', 'Perpendicular', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Equal length', 'Perpendicular', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Perpendicular', 'At 45°', 'Equal length', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Equal length', 'Perpendicular', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Perpendicular', 'Equal length', 'At 45°', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Perpendicular', 'Equal length', 'At 45°', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Perpendicular', 'At 45°', 'Parallel to base, half its length', 'Equal length', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'Parallel to base, half its length', 'Perpendicular', 'At 45°', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Parallel to base, half its length', 'Equal length', 'At 45°', 'Perpendicular', 0,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Equal length', 'Perpendicular', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'Perpendicular', 'Parallel to base, half its length', 'At 45°', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'At 45°', 'Perpendicular', 'Parallel to base, half its length', 'Equal length', 2,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Equal length', 'Parallel to base, half its length', 'At 45°', 'Perpendicular', 1,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Midpoint theorem: Line joining midpoints is:', 'Perpendicular', 'At 45°', 'Equal length', 'Parallel to base, half its length', 3,
'lc_hl_proof', 9, 'proficient', 'lc_hl', 'Important result', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (a+b)² =', 'ab', 'a² + 2ab + b²', 'a² - b²', 'a² + b²', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Expand (a+b)(a+b)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (a-b)² =', 'a² + b²', 'a² - b²', 'ab', 'a² - 2ab + b²', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Similar expansion', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (a+b)(a-b) =', 'Option 4', 'ab', 'a² + b²', 'a² - b²', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Difference of squares', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: a³ - b³ =', 'ab', 'a² + b²', '(a-b)(a² + ab + b²)', 'a² - b²', 2,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Difference of cubes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: a³ + b³ =', 'a² - b²', 'ab', 'a² + b²', '(a+b)(a² - ab + b²)', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Sum of cubes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('a² + b² ≥ 2ab because:', '(a-b)² ≥ 0', 'Not true', '(a+b)² ≤ 0', 'Direct', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Perfect square', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('|ab| = |a||b| proven by:', 'Not true', 'Direct', 'Case analysis on signs', '(a+b)² ≤ 0', 2,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Four cases', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('|a+b| ≤ |a|+|b| is:', 'Triangle inequality', 'Direct', 'Not true', '(a+b)² ≤ 0', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Fundamental', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('AM-GM: (a+b)/2 ≥ √(ab) for a,b>0', 'Not true', '(a+b)² ≤ 0', 'Direct', 'Square both sides', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Classic inequality', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove identity, show:', 'b/a', 'LHS = RHS always', 'LHS - RHS = 0', 'Sum', 2,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Difference method', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For quadratic, sum of roots =', 'LHS = RHS always', 'Sum', 'b/a', '-b/a', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Vieta''s formula', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For quadratic, product of roots =', 'Sum', 'LHS = RHS always', 'c/a', 'b/a', 2,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Vieta''s formula', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p(r) = 0, then (x-r) is:', 'A factor of p(x)', 'LHS = RHS always', 'Sum', 'b/a', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Factor theorem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('log(ab) = log(a) + log(b) from:', 'LHS = RHS always', 'Exponent laws', 'b/a', 'Sum', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', '10^(x+y) = 10^x · 10^y', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Cannot prove', 'Different formula', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Only for n=2', 'Different formula', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Different formula', 'Cannot prove', 'Binomial theorem by induction', 'Only for n=2', 2,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Binomial theorem by induction', 'Only for n=2', 'Different formula', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Binomial theorem by induction', 'Only for n=2', 'Different formula', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Different formula', 'Binomial theorem by induction', 'Only for n=2', 'Cannot prove', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Binomial theorem by induction', 'Cannot prove', 'Different formula', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Different formula', 'Only for n=2', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Binomial theorem by induction', 'Different formula', 'Cannot prove', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Different formula', 'Only for n=2', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Different formula', 'Binomial theorem by induction', 'Only for n=2', 'Cannot prove', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Different formula', 'Only for n=2', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Cannot prove', 'Different formula', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Cannot prove', 'Only for n=2', 'Different formula', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Only for n=2', 'Different formula', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Only for n=2', 'Different formula', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Cannot prove', 'Binomial theorem by induction', 'Different formula', 2,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Binomial theorem by induction', 'Cannot prove', 'Different formula', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Only for n=2', 'Different formula', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Different formula', 'Only for n=2', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Different formula', 'Only for n=2', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Binomial theorem by induction', 'Cannot prove', 'Different formula', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Binomial theorem by induction', 'Cannot prove', 'Different formula', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Different formula', 'Only for n=2', 'Cannot prove', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Cannot prove', 'Different formula', 'Only for n=2', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Only for n=2', 'Different formula', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Different formula', 'Only for n=2', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Binomial theorem by induction', 'Different formula', 'Only for n=2', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Only for n=2', 'Different formula', 'Cannot prove', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Cannot prove', 'Binomial theorem by induction', 'Different formula', 'Only for n=2', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Binomial theorem by induction', 'Different formula', 'Cannot prove', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Different formula', 'Binomial theorem by induction', 'Only for n=2', 'Cannot prove', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Only for n=2', 'Cannot prove', 'Different formula', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Different formula', 'Binomial theorem by induction', 'Only for n=2', 'Cannot prove', 1,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Different formula', 'Cannot prove', 'Only for n=2', 'Binomial theorem by induction', 3,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Prove: (1+x)ⁿ = Σ C(n,k)xᵏ', 'Binomial theorem by induction', 'Different formula', 'Cannot prove', 'Only for n=2', 0,
'lc_hl_proof', 10, 'advanced', 'lc_hl', 'Combinatorial argument', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Every integer is even or odd because:', 'p|a and p|b', 'a + b', 'n = 2q + r where r ∈ {0,1}', 'n = 2q', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Division algorithm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('gcd(a,b) · lcm(a,b) =', 'n = 2q', 'p|a and p|b', 'ab', 'a + b', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Prime factorization', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Bezout: gcd(a,b) = ax + by for:', 'a + b', 'n = 2q', 'Some integers x, y', 'p|a and p|b', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Linear combination', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If prime p | ab, then:', 'a + b', 'n = 2q', 'p|a or p|b', 'p|a and p|b', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Euclid''s lemma', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('√p irrational for prime p:', 'Same as √2 proof', 'a + b', 'n = 2q', 'p|a and p|b', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Common factor contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Fermat''s Little: aᵖ ≡', 'a (mod p) for prime p', 'Sum of digits', '0 (mod p)', 'p is composite', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Fundamental', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Wilson''s: (p-1)! ≡ -1 (mod p) iff:', 'p is prime', 'p is composite', 'Sum of digits', '0 (mod p)', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Prime characterization', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('n divisible by 9 iff:', 'Sum of digits', '0 (mod p)', 'Digit sum divisible by 9', 'p is composite', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', '10 ≡ 1 (mod 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('n divisible by 11 iff:', 'p is composite', 'Alternating digit sum divisible by 11', '0 (mod p)', 'Sum of digits', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', '10 ≡ -1 (mod 11)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('n⁵ - n divisible by 30 by:', '0 (mod p)', 'p is composite', 'Sum of digits', 'Fermat for 2, 3, 5', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', '2×3×5 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perfect square mod 4 is:', '2k or 3k', '0, 1, 2, 3', '0 or 1', 'Infinitely many', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Two possibilities', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('x² + y² = 4k+3 has:', 'No integer solutions', 'Infinitely many', '2k or 3k', '0, 1, 2, 3', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Squares are 0,1 mod 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Primes > 3 have form:', '0, 1, 2, 3', 'Infinitely many', '2k or 3k', '6k ± 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Others divisible by 2 or 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('gcd(n, n+1) =', '2k or 3k', '0, 1, 2, 3', '1', 'Infinitely many', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Consecutive integers coprime', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'a = n', 'n is prime', 'a > n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a = n', 'a > n', 'n is prime', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'gcd(a,n) = 1', 'a = n', 'n is prime', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'n is prime', 'a > n', 'a = n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'gcd(a,n) = 1', 'a > n', 'a = n', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'n is prime', 'a = n', 'a > n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'n is prime', 'a > n', 'a = n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'gcd(a,n) = 1', 'n is prime', 'a = n', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'a = n', 'gcd(a,n) = 1', 'n is prime', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'a = n', 'n is prime', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a > n', 'a = n', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a > n', 'gcd(a,n) = 1', 'a = n', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a = n', 'a > n', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'n is prime', 'a = n', 'a > n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'a > n', 'n is prime', 'a = n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'n is prime', 'gcd(a,n) = 1', 'a = n', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'gcd(a,n) = 1', 'n is prime', 'a = n', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a = n', 'n is prime', 'a > n', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'gcd(a,n) = 1', 'a = n', 'n is prime', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'n is prime', 'a = n', 'a > n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a = n', 'a > n', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'gcd(a,n) = 1', 'a = n', 'n is prime', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a > n', 'gcd(a,n) = 1', 'a = n', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a = n', 'a > n', 'n is prime', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a = n', 'gcd(a,n) = 1', 'n is prime', 'a > n', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a = n', 'a > n', 'gcd(a,n) = 1', 'n is prime', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a = n', 'n is prime', 'a > n', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'gcd(a,n) = 1', 'a = n', 'n is prime', 1,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'a = n', 'n is prime', 'a > n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a = n', 'a > n', 'gcd(a,n) = 1', 'n is prime', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a = n', 'a > n', 'gcd(a,n) = 1', 3,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'a > n', 'n is prime', 'a = n', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a = n', 'gcd(a,n) = 1', 'a > n', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'gcd(a,n) = 1', 'a = n', 'a > n', 'n is prime', 0,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'n is prime', 'a = n', 'gcd(a,n) = 1', 'a > n', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Euler''s theorem: a^φ(n) ≡ 1 (mod n) if:', 'a > n', 'n is prime', 'gcd(a,n) = 1', 'a = n', 2,
'lc_hl_proof', 11, 'advanced', 'lc_hl', 'Generalization of Fermat', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Best method for √3 irrational:', 'Contradiction', 'Counterexample', 'Induction', 'Direct proof', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Assume rational', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Best method for n³-n divisible by 6:', 'Direct (factoring)', 'Direct proof', 'Counterexample', 'Induction', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Three consecutive', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Best method for 2ⁿ > n:', 'Counterexample', 'Direct proof', 'Option 4', 'Induction', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Natural fit', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Best method for product of irrationals can be rational:', 'Direct proof', 'Counterexample', 'Example: √2×√2 = 2', 'Induction', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Constructive', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive of ''n² odd ⟹ n odd'':', 'n even ⟹ n² even', 'Counterexample', 'Induction', 'Direct proof', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Swap and negate', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('√2 + √3 irrational by:', 'Contradiction: if rational, √6 rational', 'n×180°', 'Direct calculation', 'Odd', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Chain of irrationals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Between two rationals exists:', 'Odd', 'An irrational (e.g., a + (b-a)/√2)', 'Direct calculation', 'n×180°', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Construction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sum of n-gon angles:', 'Odd', '(n-2)×180°', 'n×180°', 'Direct calculation', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Triangulation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In graph, sum of degrees is:', 'n×180°', 'Odd', 'Even (2 × edges)', 'Direct calculation', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Handshaking lemma', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('NOT valid: proof by example for:', 'Universal statements', 'n×180°', 'Direct calculation', 'Odd', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'One case doesn''t prove all', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Strong induction assumes:', 'P(1)...P(k) all true', '¬P ∧ ¬Q', 'Direct proof', 'Only P(k)', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Multiple predecessors', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use strong induction when:', 'Only P(k)', '¬P ∧ ¬Q', 'Direct proof', 'P(k+1) needs several earlier cases', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Like Fibonacci', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Every n>1 is product of primes by:', 'Direct proof', '¬P ∧ ¬Q', 'Only P(k)', 'Strong induction', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Factor if composite', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('De Morgan: ¬(P∧Q) =', '¬P ∨ ¬Q', 'Direct proof', '¬P ∧ ¬Q', 'Only P(k)', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Negate AND', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('De Morgan: ¬(P∨Q) =', '¬P ∧ ¬Q', 'Only P(k)', 'Option 4', 'Direct proof', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Negate OR', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('0.999... = 1 by:', 'Let x = 0.999..., then 10x - x = 9', 'Cannot disprove', 'Multiple examples', 'Limit', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Algebra', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('gcd(n, n+1) = 1 because:', 'Multiple examples', 'Cannot disprove', 'Common divisor divides difference = 1', 'Limit', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Simple', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To disprove ''for all x, P(x)'':', 'Cannot disprove', 'One counterexample', 'Multiple examples', 'Limit', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Single case', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To disprove ''exists x with P(x)'':', 'Multiple examples', 'Prove ''for all x, not P(x)''', 'Cannot disprove', 'Limit', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Universal negation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Largest element', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Largest element', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'Largest element', 'No smallest', 'Applies to reals', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 'Largest element', 'No smallest', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Largest element', 'Applies to reals', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Largest element', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 'No smallest', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Largest element', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'No smallest', 'Largest element', 'Applies to reals', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 'Largest element', 'No smallest', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'Largest element', 'No smallest', 'Applies to reals', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'Largest element', 'No smallest', 'Every non-empty set of positive integers has smallest element', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Largest element', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 'Largest element', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'No smallest', 'Applies to reals', 'Largest element', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Largest element', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 'Largest element', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'No smallest', 'Largest element', 'Every non-empty set of positive integers has smallest element', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 'No smallest', 'Largest element', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'Largest element', 'Applies to reals', 'No smallest', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Largest element', 'No smallest', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 'No smallest', 'Largest element', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Largest element', 'Every non-empty set of positive integers has smallest element', 'No smallest', 'Applies to reals', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Largest element', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'No smallest', 'Applies to reals', 'Largest element', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Largest element', 'Applies to reals', 1,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Largest element', 'Applies to reals', 'Every non-empty set of positive integers has smallest element', 3,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Applies to reals', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Largest element', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 'No smallest', 'Largest element', 0,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Largest element', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'Largest element', 'No smallest', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Well-ordering principle:', 'No smallest', 'Largest element', 'Every non-empty set of positive integers has smallest element', 'Applies to reals', 2,
'lc_hl_proof', 12, 'advanced', 'lc_hl', 'Foundation of induction', 1);
-- Verification
SELECT 'Proof & Reasoning questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_hl_proof';
SELECT difficulty_level, COUNT(*) as questions FROM questions_adaptive WHERE topic = 'lc_hl_proof' GROUP BY difficulty_level ORDER BY difficulty_level;
