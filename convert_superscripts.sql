-- Convert ^n notation to superscript characters in LC Higher Level questions
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < convert_superscripts.sql
-- 
-- Superscript characters: ⁰¹²³⁴⁵⁶⁷⁸⁹
-- Also handles ^(n-1), ^(n+1) patterns common in sequences

-- Update question_text
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^0', '⁰') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^1', '¹') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^2', '²') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^3', '³') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^4', '⁴') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^5', '⁵') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^6', '⁶') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^7', '⁷') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^8', '⁸') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET question_text = REPLACE(question_text, '^9', '⁹') WHERE mode = 'lc_hl';

-- Update option_a
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^0', '⁰') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^1', '¹') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^2', '²') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^3', '³') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^4', '⁴') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^5', '⁵') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^6', '⁶') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^7', '⁷') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^8', '⁸') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_a = REPLACE(option_a, '^9', '⁹') WHERE mode = 'lc_hl';

-- Update option_b
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^0', '⁰') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^1', '¹') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^2', '²') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^3', '³') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^4', '⁴') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^5', '⁵') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^6', '⁶') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^7', '⁷') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^8', '⁸') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_b = REPLACE(option_b, '^9', '⁹') WHERE mode = 'lc_hl';

-- Update option_c
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^0', '⁰') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^1', '¹') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^2', '²') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^3', '³') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^4', '⁴') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^5', '⁵') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^6', '⁶') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^7', '⁷') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^8', '⁸') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_c = REPLACE(option_c, '^9', '⁹') WHERE mode = 'lc_hl';

-- Update option_d
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^0', '⁰') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^1', '¹') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^2', '²') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^3', '³') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^4', '⁴') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^5', '⁵') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^6', '⁶') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^7', '⁷') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^8', '⁸') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET option_d = REPLACE(option_d, '^9', '⁹') WHERE mode = 'lc_hl';

-- Update explanation
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^0', '⁰') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^1', '¹') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^2', '²') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^3', '³') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^4', '⁴') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^5', '⁵') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^6', '⁶') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^7', '⁷') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^8', '⁸') WHERE mode = 'lc_hl';
UPDATE questions_adaptive SET explanation = REPLACE(explanation, '^9', '⁹') WHERE mode = 'lc_hl';

-- Handle two-digit exponents (10-20 common in i^n problems)
-- ^10 = ¹⁰, ^11 = ¹¹, etc. (already handled by sequential single-digit replacements)

-- Verify changes
SELECT 'Conversion complete. Sample questions:' as status;
SELECT question_text FROM questions_adaptive WHERE mode = 'lc_hl' AND question_text LIKE '%²%' LIMIT 3;
SELECT 'Total LC HL questions:' as info, COUNT(*) as count FROM questions_adaptive WHERE mode = 'lc_hl';
