-- LC Higher Level - Statistics - Complete SQL
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_statistics_complete.sql
-- Generated: 2025-12-15

-- Add Statistics topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_statistics', 'Statistics', id, '📊', 10, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_statistics';

-- Questions (600 total, 50 per level x 12 levels)

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: The number of students in a class', 'Categorical nominal', 'Categorical ordinal', 'Discrete numerical', 'Continuous numerical', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''The number of students in a class'' is Discrete numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: A person''s height in centimetres', 'Continuous numerical', 'Categorical nominal', 'Discrete numerical', 'Categorical ordinal', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''A person''s height in centimetres'' is Continuous numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Favourite colour', 'Continuous numerical', 'Categorical ordinal', 'Categorical nominal', 'Discrete numerical', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Favourite colour'' is Categorical nominal data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Rating on a scale of 1-5', 'Discrete numerical', 'Categorical nominal', 'Continuous numerical', 'Categorical ordinal', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Rating on a scale of 1-5'' is Categorical ordinal data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Temperature in degrees Celsius', 'Categorical nominal', 'Continuous numerical', 'Discrete numerical', 'Categorical ordinal', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Temperature in degrees Celsius'' is Continuous numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Number of goals scored', 'Discrete numerical', 'Categorical nominal', 'Categorical ordinal', 'Continuous numerical', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Number of goals scored'' is Discrete numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Blood type (A, B, AB, O)', 'Categorical nominal', 'Categorical ordinal', 'Continuous numerical', 'Discrete numerical', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Blood type (A, B, AB, O)'' is Categorical nominal data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Education level (Primary, Secondary, Third Level)', 'Continuous numerical', 'Categorical nominal', 'Categorical ordinal', 'Discrete numerical', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Education level (Primary, Secondary, Third Level)'' is Categorical ordinal data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Weight in kilograms', 'Discrete numerical', 'Continuous numerical', 'Categorical nominal', 'Categorical ordinal', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Weight in kilograms'' is Continuous numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Number of siblings', 'Categorical ordinal', 'Continuous numerical', 'Discrete numerical', 'Categorical nominal', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Number of siblings'' is Discrete numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Time taken to complete a race', 'Categorical ordinal', 'Continuous numerical', 'Categorical nominal', 'Discrete numerical', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Time taken to complete a race'' is Continuous numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data type: Shoe size (35, 36, 37, ...)', 'Continuous numerical', 'Categorical nominal', 'Discrete numerical', 'Categorical ordinal', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Shoe size (35, 36, 37, ...)'' is Discrete numerical data.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: Every 10th person on a list is selected', 'Simple random sampling', 'Cluster sampling', 'Systematic sampling', 'Stratified sampling', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Systematic sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: Names are drawn from a hat', 'Systematic sampling', 'Simple random sampling', 'Convenience sampling', 'Stratified sampling', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Simple random sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: Students are sampled proportionally from each year group', 'Systematic sampling', 'Cluster sampling', 'Stratified sampling', 'Simple random sampling', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Stratified sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: All students in randomly selected classes are surveyed', 'Simple random sampling', 'Systematic sampling', 'Cluster sampling', 'Stratified sampling', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Cluster sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: Surveying people walking past a shop', 'Systematic sampling', 'Convenience sampling', 'Stratified sampling', 'Simple random sampling', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Convenience sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: Using a random number generator to select participants', 'Cluster sampling', 'Convenience sampling', 'Simple random sampling', 'Systematic sampling', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Simple random sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: Selecting every 5th item on a production line', 'Simple random sampling', 'Stratified sampling', 'Systematic sampling', 'Cluster sampling', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Systematic sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Identify the sampling method: Sampling equal numbers from each age group', 'Systematic sampling', 'Cluster sampling', 'Simple random sampling', 'Stratified sampling', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This describes Stratified sampling.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? All students in Ireland', 'Survey', 'Census', 'Population', 'Sample', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''All students in Ireland'' is a population.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? 100 voters selected for a poll', 'Sample', 'Population', 'Census', 'Parameter', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''100 voters selected for a poll'' is a sample.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? Every registered voter in a constituency', 'Survey', 'Sample', 'Statistic', 'Population', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Every registered voter in a constituency'' is a population.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? 50 products tested from a factory', 'Sample', 'Census', 'Parameter', 'Population', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''50 products tested from a factory'' is a sample.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? All employees of a company', 'Population', 'Sample', 'Statistic', 'Survey', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''All employees of a company'' is a population.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? 20 patients selected for a clinical trial', 'Parameter', 'Population', 'Sample', 'Census', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''20 patients selected for a clinical trial'' is a sample.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? All students in Ireland', 'Sample', 'Survey', 'Population', 'Census', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''All students in Ireland'' is a population.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? 100 voters selected for a poll', 'Census', 'Sample', 'Population', 'Parameter', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''100 voters selected for a poll'' is a sample.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? Every registered voter in a constituency', 'Sample', 'Population', 'Survey', 'Statistic', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''Every registered voter in a constituency'' is a population.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is this a population or a sample? 50 products tested from a factory', 'Parameter', 'Population', 'Sample', 'Census', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', '''50 products tested from a factory'' is a sample.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? A survey about exercise conducted at a gym', 'Response bias', 'Measurement bias', 'Yes, sampling bias (unrepresentative location)', 'No bias', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, sampling bias (unrepresentative location)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? A questionnaire asking ''Don''t you agree that...?''', 'Sampling bias', 'No bias', 'Non-response bias', 'Yes, leading question bias', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, leading question bias', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? Only 20% of surveys were returned', 'Yes, non-response bias', 'Leading question bias', 'No bias', 'Sampling bias', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, non-response bias', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? Random selection of voters from electoral register', 'Sampling bias', 'Response bias', 'No bias (proper random sampling)', 'Non-response bias', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'No bias (proper random sampling)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? Online survey about internet usage', 'Yes, sampling bias (excludes non-internet users)', 'Response bias', 'Measurement bias', 'No bias', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, sampling bias (excludes non-internet users)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? A survey about exercise conducted at a gym', 'Response bias', 'No bias', 'Yes, sampling bias (unrepresentative location)', 'Measurement bias', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, sampling bias (unrepresentative location)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? A questionnaire asking ''Don''t you agree that...?''', 'Yes, leading question bias', 'No bias', 'Sampling bias', 'Non-response bias', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, leading question bias', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? Only 20% of surveys were returned', 'Yes, non-response bias', 'Leading question bias', 'Sampling bias', 'No bias', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, non-response bias', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? Random selection of voters from electoral register', 'Sampling bias', 'Response bias', 'Non-response bias', 'No bias (proper random sampling)', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'No bias (proper random sampling)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is there bias in this scenario? Online survey about internet usage', 'Response bias', 'Yes, sampling bias (excludes non-internet users)', 'No bias', 'Measurement bias', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'Yes, sampling bias (excludes non-internet users)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Data collected through your own survey', 'Tertiary data', 'Primary data', 'Sample data', 'Secondary data', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is primary data because it was collected by the researcher.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Using census data from the CSO', 'Primary data', 'Tertiary data', 'Population data', 'Secondary data', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is secondary data because it was collected by someone else.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Conducting interviews for your research', 'Secondary data', 'Tertiary data', 'Primary data', 'Sample data', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is primary data because it was collected by the researcher.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Data from a published research paper', 'Primary data', 'Raw data', 'Tertiary data', 'Secondary data', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is secondary data because it was collected by someone else.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Observations recorded during an experiment', 'Tertiary data', 'Derived data', 'Secondary data', 'Primary data', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is primary data because it was collected by the researcher.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Data collected through your own survey', 'Sample data', 'Secondary data', 'Tertiary data', 'Primary data', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is primary data because it was collected by the researcher.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Using census data from the CSO', 'Tertiary data', 'Primary data', 'Population data', 'Secondary data', 3,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is secondary data because it was collected by someone else.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Conducting interviews for your research', 'Tertiary data', 'Sample data', 'Primary data', 'Secondary data', 2,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is primary data because it was collected by the researcher.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Data from a published research paper', 'Raw data', 'Secondary data', 'Tertiary data', 'Primary data', 1,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is secondary data because it was collected by someone else.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Classify this data source: Observations recorded during an experiment', 'Primary data', 'Secondary data', 'Tertiary data', 'Derived data', 0,
'lc_hl_statistics', 1, 'foundation', 'lc_hl', 'This is primary data because it was collected by the researcher.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (4, 5), (2, 7), (3, 3), (1, 4), (1, 5). What is the frequency of value 1?', '24', '4', '5', '3', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 1 is 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (2, 7), (2, 6), (2, 2), (2, 6), (4, 2). What is the frequency of value 2?', '7', '6', '23', '5', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 2 is 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (4, 7), (5, 5), (3, 2), (5, 3), (2, 3). What is the frequency of value 5?', '20', '6', '4', '5', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 5 is 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (2, 8), (2, 6), (5, 5), (5, 4), (1, 6). What is the frequency of value 5?', '29', '4', '5', '6', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 5 is 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (2, 2), (1, 3), (1, 6), (5, 3), (3, 5). What is the frequency of value 5?', '4', '19', '3', '2', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 5 is 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (3, 6), (5, 7), (4, 3), (3, 7), (5, 7). What is the frequency of value 5?', '8', '30', '7', '6', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 5 is 7.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (3, 3), (3, 8), (2, 3), (3, 5), (5, 7). What is the frequency of value 3?', '6', '4', '26', '5', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 3 is 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (1, 5), (3, 6), (2, 2), (2, 5), (1, 7). What is the frequency of value 1?', '5', '4', '25', '6', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 1 is 5.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (3, 5), (1, 6), (3, 2), (4, 5), (2, 8). What is the frequency of value 3?', '26', '1', '3', '2', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 3 is 2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From the (value, frequency) pairs: (5, 8), (2, 8), (1, 6), (4, 6), (5, 4). What is the frequency of value 5?', '9', '7', '8', '32', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'The frequency of 5 is 8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 10, 7, 7, 8. What is the total frequency (n)?', '34', '32', '4', '30', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 10 + 7 + 7 + 8 = 32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 5, 6, 7, 7. What is the total frequency (n)?', '27', '4', '23', '25', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 5 + 6 + 7 + 7 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 6, 10, 8, 3. What is the total frequency (n)?', '27', '29', '25', '4', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 6 + 10 + 8 + 3 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 8, 10, 6, 3. What is the total frequency (n)?', '29', '4', '25', '27', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 8 + 10 + 6 + 3 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 4, 7, 7, 4. What is the total frequency (n)?', '4', '24', '20', '22', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 4 + 7 + 7 + 4 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 6, 9, 6, 6. What is the total frequency (n)?', '27', '25', '4', '29', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 6 + 9 + 6 + 6 = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 4, 3, 4, 7. What is the total frequency (n)?', '16', '20', '18', '4', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 4 + 3 + 4 + 7 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 4, 10, 3, 7. What is the total frequency (n)?', '24', '26', '4', '22', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 4 + 10 + 3 + 7 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 7, 8, 5, 3. What is the total frequency (n)?', '21', '25', '23', '4', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 7 + 8 + 5 + 3 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A frequency table has frequencies: 10, 3, 5, 6. What is the total frequency (n)?', '26', '22', '4', '24', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Total n = 10 + 3 + 5 + 6 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 20 out of 72 observations, what is its relative frequency?', '0.2', '0.38', '0.28', '3.6', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 20/72 = 0.28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 18 out of 80 observations, what is its relative frequency?', '0.23', '4.44', '0.18', '0.33', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 18/80 = 0.23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 15 out of 90 observations, what is its relative frequency?', '0.15', '0.17', '6.0', '0.27', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 15/90 = 0.17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 11 out of 57 observations, what is its relative frequency?', '0.11', '0.29', '5.18', '0.19', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 11/57 = 0.19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 12 out of 48 observations, what is its relative frequency?', '0.12', '4.0', '0.25', '0.35', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 12/48 = 0.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 17 out of 45 observations, what is its relative frequency?', '0.38', '0.48', '2.65', '0.17', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 17/45 = 0.38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 5 out of 86 observations, what is its relative frequency?', '17.2', '0.06', '0.05', '0.16', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 5/86 = 0.06', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 13 out of 73 observations, what is its relative frequency?', '0.13', '0.28', '0.18', '5.62', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 13/73 = 0.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 18 out of 58 observations, what is its relative frequency?', '3.22', '0.31', '0.41', '0.18', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 18/58 = 0.31', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If a value has frequency 14 out of 98 observations, what is its relative frequency?', '0.14', '0.24', '7.0', 'Cannot determine', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Relative frequency = 14/98 = 0.14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 100 - 110?', '110', '5', '10', '15', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 110 - 100 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 10 - 60?', '45', '60', '50', '55', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 60 - 10 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 0 - 50?', '50', 'Cannot determine', '45', '55', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 50 - 0 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 10 - 35?', '30', '35', '20', '25', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 35 - 10 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 0 - 50?', 'Cannot determine', '50', '45', '55', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 50 - 0 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 50 - 60?', '10', '15', '60', '5', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 60 - 50 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 100 - 120?', '25', '15', '120', '20', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 120 - 100 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 20 - 70?', '45', '55', '70', '50', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 70 - 20 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 20 - 30?', '5', '10', '15', '30', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 30 - 20 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the class width of the interval 50 - 70?', '25', '70', '15', '20', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Class width = 70 - 50 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 10 - 20?', '10', 'Cannot determine', '15', '20', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (10 + 20)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 20 - 40?', '35', '20', '25', '30', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (20 + 40)/2 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 40 - 60?', '55', '50', '45', '20', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (40 + 60)/2 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 10 - 20?', 'Cannot determine', '10', '20', '15', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (10 + 20)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 10 - 20?', '20', '10', 'Cannot determine', '15', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (10 + 20)/2 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 30 - 40?', '10', '40', '30', '35', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (30 + 40)/2 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 20 - 40?', '25', '35', '20', '30', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (20 + 40)/2 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 20 - 40?', '20', '25', '35', '30', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (20 + 40)/2 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 20 - 40?', '20', '25', '30', '35', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (20 + 40)/2 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the midpoint of the class interval 20 - 40?', '30', '35', '20', '25', 0,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Midpoint = (20 + 40)/2 = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 5, 3, 4, 3. What is the cumulative frequency after class 4?', '20', '15', '3', 'Cannot determine', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 5 + 3 + 4 + 3 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 3, 8, 3, 4. What is the cumulative frequency after class 4?', '4', '21', 'Cannot determine', '18', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 3 + 8 + 3 + 4 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 3, 7, 7, 4. What is the cumulative frequency after class 3?', '7', '17', '20', '21', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 3 + 7 + 7 = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 5, 8, 5, 4. What is the cumulative frequency after class 4?', 'Cannot determine', '27', '22', '4', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 5 + 8 + 5 + 4 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 7, 5, 5, 6. What is the cumulative frequency after class 4?', 'Cannot determine', '23', '6', '30', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 7 + 5 + 5 + 6 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 8, 5, 3, 6. What is the cumulative frequency after class 2?', '21', '13', '5', '22', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 8 + 5 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 6, 8, 8, 7. What is the cumulative frequency after class 4?', 'Cannot determine', '29', '7', '35', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 6 + 8 + 8 + 7 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 3, 5, 5, 3. What is the cumulative frequency after class 4?', '19', '16', '3', 'Cannot determine', 1,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 3 + 5 + 5 + 3 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 8, 4, 8, 7. What is the cumulative frequency after class 2?', '20', '27', '12', '4', 2,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 8 + 4 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 3, 3, 3, 4. What is the cumulative frequency after class 3?', '13', '3', '12', '9', 3,
'lc_hl_statistics', 2, 'foundation', 'lc_hl', 'Cumulative frequency = 3 + 3 + 3 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 12, 3, 11, 7, 7', '9.0', '7.0', '40', '8.0', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (12 + 3 + 11 + 7 + 7)/5 = 40/5 = 8.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 2, 11, 8, 9, 10, 2', '42', '8.0', '7.0', '6.0', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (2 + 11 + 8 + 9 + 10 + 2)/6 = 42/6 = 7.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 3, 10, 2, 12, 12', '8.8', '7.8', '39', '6.8', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (3 + 10 + 2 + 12 + 12)/5 = 39/5 = 7.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 2, 6, 14, 4', '5.5', '26', '7.5', '6.5', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (2 + 6 + 14 + 4)/4 = 26/4 = 6.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 12, 15, 6, 3, 10, 15', '10.2', '11.2', '61', '9.2', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (12 + 15 + 6 + 3 + 10 + 15)/6 = 61/6 = 10.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 13, 2, 6, 10, 3, 8', '6.0', '8.0', '42', '7.0', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (13 + 2 + 6 + 10 + 3 + 8)/6 = 42/6 = 7.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 3, 10, 3, 3', '3.8', '4.8', '19', '5.8', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (3 + 10 + 3 + 3)/4 = 19/4 = 4.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 13, 7, 8, 7', '9.8', '7.8', '8.8', '35', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (13 + 7 + 8 + 7)/4 = 35/4 = 8.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 4, 13, 10, 9, 15, 12', '63', '11.5', '10.5', '9.5', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (4 + 13 + 10 + 9 + 15 + 12)/6 = 63/6 = 10.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 12, 14, 10, 13, 2, 4', '9.2', '10.2', '55', '8.2', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = (12 + 14 + 10 + 13 + 2 + 4)/6 = 55/6 = 9.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 2, 4, 5, 6, 9, 13, 18', '7', '8.1', '6', '5', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (4th value) = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 1, 7, 14, 18, 18', '13', '14', '15', '11.6', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (3th value) = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 2, 6, 6, 9, 10, 13, 18', '9.1', '9', '10', '8', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (4th value) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 6, 13, 17, 19, 20, 20, 20', '16.4', '19', '20', '18', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (4th value) = 19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 1, 1, 1, 5, 7, 14, 20', '5', '7.0', '4', '6', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (4th value) = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 8, 18, 18, 20', '13.6', '17', '19', '18', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (3th value) = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 2, 6, 7, 10, 13, 16, 18', '11', '10.3', '9', '10', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (4th value) = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 4, 7, 9, 12, 17, 20', '9', '10', '10.4', '8', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Data is sorted. Median is the middle value (4th value) = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 7, 11, 12, 15, 18', '11.2', '11.5', '12', '11', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (11 + 12)/2 = 11.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 1, 2, 2, 4, 7, 20', '4', '3.0', '2', '6.0', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (2 + 4)/2 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 1, 6, 15, 19', '10.2', '6', '15', '10.5', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (6 + 15)/2 = 10.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 5, 7, 13, 14, 17', '10.0', '7', 'Cannot determine', '13', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (7 + 13)/2 = 10.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 8, 9, 9, 11', 'Cannot determine', '9.0', '9', '9.2', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (9 + 9)/2 = 9.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 12, 15, 16, 18', '15.5', '15.2', '16', '15', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (15 + 16)/2 = 15.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 1, 1, 4, 13, 19, 19', '8.5', '4', '9.5', '13', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (4 + 13)/2 = 8.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 4, 8, 14, 16', '11.0', '8', '14', '10.5', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Even count. Median = (8 + 14)/2 = 11.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 5, 9, 9, 9, 5, 3', '9', 'No mode', '5', '3', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 9 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 2, 5, 2, 5, 8, 5', '8', '5', 'No mode', '2', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 5 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 8, 10, 10, 5, 10, 10', 'No mode', '8', '10', '5', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 10 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 2, 7, 2, 2, 5, 2', '5', 'No mode', '2', '7', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 2 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 6, 9, 8, 9, 9, 1', '9', '6', '8', '1', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 9 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 4, 9, 4, 8, 4, 9', 'No mode', '8', '9', '4', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 4 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 9, 1, 10, 1, 9, 1', '10', '1', '9', 'No mode', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 1 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mode of: 9, 4, 9, 9, 9, 2', '9', 'No mode', '4', '2', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is the most frequent value. 9 appears most often.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 1), (2: 4), (3: 4), (4: 2), (5: 3)', '3.0', '3.14', '3.64', '2.64', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 44/14 = 3.14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 4), (2: 4), (3: 5), (4: 1), (5: 2)', '2.56', '3.0', '2.06', '3.06', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 41/16 = 2.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 3), (2: 5), (3: 2), (4: 3), (5: 4)', '2.5', 'Cannot determine', '3.0', '3.5', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 51/17 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 1), (2: 3), (3: 2), (4: 5), (5: 3)', '3.93', '3.0', '3.43', '2.93', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 48/14 = 3.43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 2), (2: 4), (3: 4), (4: 2), (5: 5)', '2.74', '3.0', '3.74', '3.24', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 55/17 = 3.24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 4), (2: 5), (3: 5), (4: 1), (5: 2)', '2.53', '2.03', '3.03', '3.0', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 43/17 = 2.53', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 3), (2: 1), (3: 2), (4: 3), (5: 2)', 'Cannot determine', '3.0', '2.5', '3.5', 1,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 33/11 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean from this frequency table (value: frequency): (1: 4), (2: 1), (3: 5), (4: 3), (5: 4)', '3.12', '3.62', '3.0', '2.62', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'Mean = Σfx/Σf = 53/17 = 3.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: Salaries in a company with one very high earner?', 'Mode', 'Mean', 'Median', 'Range', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The median is most appropriate because it''s not affected by outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: Shoe sizes sold in a shop?', 'Mean', 'Range', 'Mode', 'Median', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is most appropriate because it''s measures most common value.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: Exam scores with no outliers?', 'Mode', 'Median', 'Mean', 'Range', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mean is most appropriate because it''s uses all values when distribution is symmetric.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: House prices in an area with mansions?', 'Mode', 'Range', 'Mean', 'Median', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The median is most appropriate because it''s not affected by outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: Most popular car colour?', 'Range', 'Median', 'Mode', 'Mean', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is most appropriate because it''s measures most common value.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: Symmetrically distributed heights?', 'Mean', 'Range', 'Interquartile range', 'Mode', 0,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mean is most appropriate because it''s uses all values when distribution is symmetric.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: Salaries in a company with one very high earner?', 'Mean', 'Range', 'Median', 'Mode', 2,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The median is most appropriate because it''s not affected by outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most appropriate for: Shoe sizes sold in a shop?', 'Median', 'Range', 'Mean', 'Mode', 3,
'lc_hl_statistics', 3, 'foundation', 'lc_hl', 'The mode is most appropriate because it''s measures most common value.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 42, 42, 36, 17, 28', '42', '30', '25', '17', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 42 - 17 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 44, 34, 33, 7, 35', '37', '44', '42', '7', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 44 - 7 = 37', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 15, 5, 6, 25, 25', '5', '20', '25', 'Cannot determine', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 25 - 5 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 40, 17, 30, 38, 20', '28', '40', '17', '23', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 40 - 17 = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 15, 9, 21, 6, 46', '6', '45', '40', '46', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 46 - 6 = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 11, 37, 32, 46, 31', '40', '46', '35', '11', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 46 - 11 = 35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 5, 25, 15, 10, 12', '5', '20', '25', 'Cannot determine', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 25 - 5 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 22, 14, 26, 22, 15', '12', '26', '14', '17', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 26 - 14 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 47, 10, 48, 14, 32', '38', '10', '43', '48', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 48 - 10 = 38', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 29, 42, 8, 36, 39', '42', '39', '8', '34', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'Range = Max - Min = 42 - 8 = 34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 13, 20, 24, 25, 25, 28, 31, 44', '20', '24', '13', '22.0', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (20 + 24)/2 = 22.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 30, 32, 35, 36, 39, 39, 41, 42', '33.5', '35', '30', '32', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (32 + 35)/2 = 33.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 15, 20, 23, 26, 31, 36, 43, 50', '21.5', '15', '20', '23', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (20 + 23)/2 = 21.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 11, 16, 31, 39, 42, 48, 48, 49', '31', '11', '23.5', '16', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (16 + 31)/2 = 23.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 14, 16, 29, 38, 40, 41, 44, 45', '16', '14', '29', '22.5', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (16 + 29)/2 = 22.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 16, 17, 20, 22, 24, 29, 30, 30', '18.5', '16', '17', '20', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (17 + 20)/2 = 18.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 15, 24, 39, 42, 44, 45, 49, 50', '15', '24', '31.5', '39', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (24 + 39)/2 = 31.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q1 (lower quartile) for: 15, 23, 32, 35, 45, 46, 48, 49', '15', '32', '27.5', '23', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q1 is the average of the 2nd and 3rd values: (23 + 32)/2 = 27.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 10, 11, 22, 23, 43, 44, 47, 48', '44', '48', '45.5', '47', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (44 + 47)/2 = 45.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 17, 19, 20, 20, 22, 35, 35, 39', 'Cannot determine', '39', '35.0', '35', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (35 + 35)/2 = 35.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 13, 15, 16, 24, 29, 38, 42, 49', '38', '40.0', '42', '49', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (38 + 42)/2 = 40.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 11, 11, 17, 17, 30, 35, 38, 45', '38', '35', '36.5', '45', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (35 + 38)/2 = 36.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 10, 12, 13, 17, 23, 37, 38, 43', '37.5', '38', '43', '37', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (37 + 38)/2 = 37.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 15, 17, 20, 21, 21, 40, 48, 49', '40', '44.0', '49', '48', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (40 + 48)/2 = 44.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 12, 17, 30, 31, 35, 37, 38, 42', '42', '37.5', '38', '37', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (37 + 38)/2 = 37.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find Q3 (upper quartile) for: 16, 19, 27, 36, 38, 38, 46, 47', '47', '38', '46', '42.0', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'For n=8, Q3 is the average of the 6th and 7th values: (38 + 46)/2 = 42.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 21 and Q3 = 42, find the Interquartile Range (IQR).', '42', 'Cannot determine', '21', '63', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 42 - 21 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 26 and Q3 = 39, find the Interquartile Range (IQR).', '65', '13', '26', '39', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 39 - 26 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 20 and Q3 = 41, find the Interquartile Range (IQR).', '41', '61', '20', '21', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 41 - 20 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 30 and Q3 = 49, find the Interquartile Range (IQR).', '19', '79', '49', '30', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 49 - 30 = 19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 25 and Q3 = 47, find the Interquartile Range (IQR).', '25', '47', '22', '72', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 47 - 25 = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 28 and Q3 = 46, find the Interquartile Range (IQR).', '74', '18', '28', '46', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 46 - 28 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 33 and Q3 = 53, find the Interquartile Range (IQR).', '33', '86', '53', '20', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 53 - 33 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 29 and Q3 = 43, find the Interquartile Range (IQR).', '72', '14', '29', '43', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 43 - 29 = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 29 and Q3 = 41, find the Interquartile Range (IQR).', '70', '41', '12', '29', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 41 - 29 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If Q1 = 28 and Q3 = 44, find the Interquartile Range (IQR).', '28', '72', '44', '16', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = Q3 - Q1 = 44 - 28 = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is -7 an outlier? (Use 1.5 × IQR rule)', 'No, it is not an outlier', 'Need more data', 'Cannot determine', 'Yes, it is an outlier', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. -7 is inside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is 28 an outlier? (Use 1.5 × IQR rule)', 'No, it is not an outlier', 'Yes, it is an outlier', 'Need more data', 'Cannot determine', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. 28 is inside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is 29 an outlier? (Use 1.5 × IQR rule)', 'Need more data', 'No, it is not an outlier', 'Cannot determine', 'Yes, it is an outlier', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. 29 is inside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is 30 an outlier? (Use 1.5 × IQR rule)', 'No, it is not an outlier', 'Need more data', 'Cannot determine', 'Yes, it is an outlier', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. 30 is inside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is 34 an outlier? (Use 1.5 × IQR rule)', 'Cannot determine', 'Yes, it is an outlier', 'No, it is not an outlier', 'Need more data', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. 34 is inside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is -12 an outlier? (Use 1.5 × IQR rule)', 'Yes, it is an outlier', 'Need more data', 'Cannot determine', 'No, it is not an outlier', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. -12 is outside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is 28 an outlier? (Use 1.5 × IQR rule)', 'Need more data', 'Yes, it is an outlier', 'Cannot determine', 'No, it is not an outlier', 3,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. 28 is inside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given Q1 = 20, Q3 = 40. Is 73 an outlier? (Use 1.5 × IQR rule)', 'No, it is not an outlier', 'Yes, it is an outlier', 'Need more data', 'Cannot determine', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'IQR = 20. Fences: [-10.0, 70.0]. 73 is outside this range.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Adding a very high value affects which measure most?', 'IQR', 'Mean', 'Median', 'Mode', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'The Mean is resistant to outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which measure of spread is resistant to outliers?', 'Range', 'IQR', 'Variance', 'Standard deviation', 1,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'The IQR is resistant to outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which average is most affected by outliers?', 'Median', 'Mode', 'Mean', 'Both median and mode', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'The Mean is most affected by outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which is a better measure of spread when outliers exist?', 'Range', 'Mean deviation', 'IQR', 'Total spread', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'The IQR is resistant to outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Adding a very high value affects which measure most?', 'IQR', 'Mode', 'Mean', 'Median', 2,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'The Mean is resistant to outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which measure of spread is resistant to outliers?', 'IQR', 'Variance', 'Range', 'Standard deviation', 0,
'lc_hl_statistics', 4, 'developing', 'lc_hl', 'The IQR is resistant to outliers.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 5, 9, 10, 10 (Mean = 8.5)', '17.0', '4.25', '8.5', '2.06', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 17.0/4 = 4.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 5, 4, 10, 1 (Mean = 5.0)', '10.5', '21.0', '42.0', '3.24', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 42.0/4 = 10.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 5, 8, 7, 8 (Mean = 7.0)', '3.0', '6.0', '1.5', '1.22', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 6.0/4 = 1.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 9, 7, 8, 10 (Mean = 8.5)', '2.5', '1.12', '1.25', '5.0', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 5.0/4 = 1.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 5, 8, 6, 6 (Mean = 6.25)', '1.09', '2.38', '4.75', '1.19', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 4.75/4 = 1.19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 10, 8, 5, 3 (Mean = 6.5)', '14.5', '7.25', '2.69', '29.0', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 29.0/4 = 7.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 8, 5, 1, 7 (Mean = 5.25)', '28.75', '14.38', '7.19', '2.68', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 28.75/4 = 7.19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the population variance for: 8, 9, 5, 9 (Mean = 7.75)', '1.64', '2.69', '10.75', '5.38', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Variance = Σ(x-μ)²/n = 10.75/4 = 2.69', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 36, what is the standard deviation?', '7', '12', '36', '6', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 9, what is the standard deviation?', '6', '9', '4', '3', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √9 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 25, what is the standard deviation?', '6', '5', '10', '25', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √25 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 4, what is the standard deviation?', '2', '3', '4', 'Cannot determine', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √4 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 16, what is the standard deviation?', '16', '5', '8', '4', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √16 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 16, what is the standard deviation?', '4', '16', '8', '5', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √16 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 16, what is the standard deviation?', '16', '5', '8', '4', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √16 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the variance is 36, what is the standard deviation?', '12', '36', '6', '7', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Standard deviation = √variance = √36 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 8 and the mean of squares is 73, find the variance.', '137', '64', '73', '9', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 73 - 8² = 73 - 64 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 7 and the mean of squares is 51, find the variance.', '49', '2', '100', '51', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 51 - 7² = 51 - 49 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 7 and the mean of squares is 53, find the variance.', '49', '4', '102', '53', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 53 - 7² = 53 - 49 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 10 and the mean of squares is 109, find the variance.', '9', '109', '209', '100', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 109 - 10² = 109 - 100 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 9 and the mean of squares is 91, find the variance.', '91', '172', '10', '81', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 91 - 9² = 91 - 81 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 8 and the mean of squares is 73, find the variance.', '73', '64', '9', '137', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 73 - 8² = 73 - 64 = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 8 and the mean of squares is 68, find the variance.', '132', '64', '4', '68', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 68 - 8² = 68 - 64 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the mean is 8 and the mean of squares is 69, find the variance.', '64', '69', '133', '5', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Var = E(X²) - [E(X)]² = 69 - 8² = 69 - 64 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 7, what is the standard deviation of 4X + 5?', '12', '7', '28', '33', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(4X + 5) = |4| × σ = 4 × 7 = 28. Adding 5 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 4, what is the standard deviation of 2X + 6?', '8', '10', '14', '4', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(2X + 6) = |2| × σ = 2 × 4 = 8. Adding 6 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 4, what is the standard deviation of 2X + 3?', '8', '11', '7', '4', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(2X + 3) = |2| × σ = 2 × 4 = 8. Adding 3 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 7, what is the standard deviation of 3X + 3?', '10', '24', '21', '7', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(3X + 3) = |3| × σ = 3 × 7 = 21. Adding 3 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 6, what is the standard deviation of 4X + 1?', '7', '25', '24', '6', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(4X + 1) = |4| × σ = 4 × 6 = 24. Adding 1 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 3, what is the standard deviation of 2X + 8?', '14', '6', '11', '3', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(2X + 8) = |2| × σ = 2 × 3 = 6. Adding 8 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 6, what is the standard deviation of 3X + 1?', '18', '7', '6', '19', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(3X + 1) = |3| × σ = 3 × 6 = 18. Adding 1 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 5, what is the standard deviation of 4X + 6?', '20', '5', '11', '26', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'SD(4X + 6) = |4| × σ = 4 × 5 = 20. Adding 6 doesn''t affect spread.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 8 with Σ(x-x̄)² = 132, find the sample variance.', '18.86', '16.5', '4.34', '132', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 132/7 = 18.86', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 10 with Σ(x-x̄)² = 129, find the sample variance.', '14.33', '3.79', '129', '12.9', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 129/9 = 14.33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 8 with Σ(x-x̄)² = 155, find the sample variance.', '155', '22.14', '4.71', '19.38', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 155/7 = 22.14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 6 with Σ(x-x̄)² = 113, find the sample variance.', '18.83', '4.75', '22.6', '113', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 113/5 = 22.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 8 with Σ(x-x̄)² = 138, find the sample variance.', '138', '17.25', '19.71', '4.44', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 138/7 = 19.71', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 7 with Σ(x-x̄)² = 185, find the sample variance.', '26.43', '5.55', '185', '30.83', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 185/6 = 30.83', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 8 with Σ(x-x̄)² = 88, find the sample variance.', '88', '12.57', '3.55', '11.0', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 88/7 = 12.57', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For a sample of size 9 with Σ(x-x̄)² = 161, find the sample variance.', '20.12', '17.89', '4.49', '161', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'Sample variance uses n-1: s² = 161/8 = 20.12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two datasets have the same mean but different standard deviations. What does a larger SD indicate?', 'More data points', 'Higher mean', 'Smaller range', 'Greater spread/variability', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: Greater spread/variability', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If SD = 0, what does this tell us about the data?', 'All values are identical', 'Mean equals median', 'There are no outliers', 'Data is normally distributed', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: All values are identical', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 5. After multiplying all values by 2, the new SD is:', '7', '5', '25', '10', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Adding 10 to every value in a dataset will:', 'Increase SD by 10', 'Double the SD', 'Not change the SD', 'Decrease the SD', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: Not change the SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two datasets have the same mean but different standard deviations. What does a larger SD indicate?', 'Greater spread/variability', 'Smaller range', 'More data points', 'Higher mean', 0,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: Greater spread/variability', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If SD = 0, what does this tell us about the data?', 'Mean equals median', 'Data is normally distributed', 'All values are identical', 'There are no outliers', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: All values are identical', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A dataset has SD = 5. After multiplying all values by 2, the new SD is:', '5', '25', '10', '7', 2,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Adding 10 to every value in a dataset will:', 'Decrease the SD', 'Increase SD by 10', 'Double the SD', 'Not change the SD', 3,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: Not change the SD', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two datasets have the same mean but different standard deviations. What does a larger SD indicate?', 'Higher mean', 'Greater spread/variability', 'More data points', 'Smaller range', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: Greater spread/variability', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If SD = 0, what does this tell us about the data?', 'Data is normally distributed', 'All values are identical', 'Mean equals median', 'There are no outliers', 1,
'lc_hl_statistics', 5, 'developing', 'lc_hl', 'The answer is: All values are identical', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 10-15: 18, 15-20: 19, 20-25: 16, 25-30: 15. What is the frequency for the class 10-15?', '18', '19', '20', '68', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 10-15 is 18.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 0-10: 8, 10-20: 15, 20-30: 11, 30-40: 15. What is the frequency for the class 10-20?', '17', '49', '15', '11', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 10-20 is 15.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 0-5: 9, 5-10: 11, 10-15: 10, 15-20: 11. What is the frequency for the class 0-5?', '11', 'Cannot determine', '41', '9', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 0-5 is 9.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 0-10: 11, 10-20: 12, 20-30: 16, 30-40: 16. What is the frequency for the class 0-10?', '11', '55', '13', '12', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 0-10 is 11.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 10-20: 15, 20-30: 10, 30-40: 20, 40-50: 5. What is the frequency for the class 30-40?', '5', '50', '20', '22', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 30-40 is 20.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 20-30: 6, 30-40: 16, 40-50: 7, 50-60: 16. What is the frequency for the class 30-40?', '16', '7', '18', '45', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 30-40 is 16.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 10-15: 6, 15-20: 17, 20-25: 11, 25-30: 20. What is the frequency for the class 25-30?', '22', '6', '54', '20', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 25-30 is 20.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A histogram shows: 10-20: 14, 20-30: 11, 30-40: 19, 40-50: 14. What is the frequency for the class 30-40?', '14', '19', '58', '21', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'The frequency for class 30-40 is 19.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 13, 5, 5, 6. What is the cumulative frequency after class 2?', '13', '18', '5', '29', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 13 + 5 = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 12, 7, 11, 9. What is the cumulative frequency after class 4?', '39', '30', '9', 'Cannot determine', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 12 + 7 + 11 + 9 = 39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 12, 12, 5, 11. What is the cumulative frequency after class 3?', '40', '29', '24', '5', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 12 + 12 + 5 = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 7, 15, 11, 5. What is the cumulative frequency after class 3?', '33', '11', '22', '38', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 7 + 15 + 11 = 33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 6, 7, 15, 13. What is the cumulative frequency after class 2?', '6', '41', '13', '7', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 6 + 7 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 14, 11, 15, 8. What is the cumulative frequency after class 3?', '40', '25', '48', '15', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 14 + 11 + 15 = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 15, 13, 12, 11. What is the cumulative frequency after class 4?', '11', 'Cannot determine', '51', '40', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 15 + 13 + 12 + 11 = 51', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Frequencies are 11, 14, 11, 15. What is the cumulative frequency after class 3?', '11', '36', '25', '51', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Cumulative frequency = 11 + 14 + 11 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 80 data points. At what cumulative frequency position is the median?', '80', '40.0', '40.5', '20.0', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 80/2 = 40.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 80 data points. At what cumulative frequency position is the median?', '80', '40.5', '20.0', '40.0', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 80/2 = 40.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 50 data points. At what cumulative frequency position is the median?', '12.5', '25.5', '25.0', '50', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 50/2 = 25.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 80 data points. At what cumulative frequency position is the median?', '40.0', '20.0', '40.5', '80', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 80/2 = 40.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 60 data points. At what cumulative frequency position is the median?', '30.0', '30.5', '15.0', '60', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 60/2 = 30.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 60 data points. At what cumulative frequency position is the median?', '30.5', '15.0', '60', '30.0', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 60/2 = 30.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 40 data points. At what cumulative frequency position is the median?', '40', '10.0', '20.0', '20.5', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 40/2 = 20.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('There are 80 data points. At what cumulative frequency position is the median?', '40.0', '40.5', '20.0', '80', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Median position = n/2 = 80/2 = 40.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 80 data points, at what cumulative frequency position is Q1?', '20.0', '40.0', '60.0', 'Cannot determine', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q1 position = 1n/4 = 1×80/4 = 20.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 60 data points, at what cumulative frequency position is Q3?', '45.0', 'Cannot determine', '30.0', '15.0', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q3 position = 3n/4 = 3×60/4 = 45.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 60 data points, at what cumulative frequency position is Q1?', '30.0', 'Cannot determine', '15.0', '45.0', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q1 position = 1n/4 = 1×60/4 = 15.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 40 data points, at what cumulative frequency position is Q3?', '20.0', '30.0', '10.0', 'Cannot determine', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q3 position = 3n/4 = 3×40/4 = 30.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 40 data points, at what cumulative frequency position is Q3?', '10.0', '30.0', 'Cannot determine', '20.0', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q3 position = 3n/4 = 3×40/4 = 30.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 80 data points, at what cumulative frequency position is Q1?', '20.0', '60.0', '40.0', 'Cannot determine', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q1 position = 1n/4 = 1×80/4 = 20.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 80 data points, at what cumulative frequency position is Q1?', '40.0', '60.0', 'Cannot determine', '20.0', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q1 position = 1n/4 = 1×80/4 = 20.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 80 data points, at what cumulative frequency position is Q3?', '20.0', 'Cannot determine', '40.0', '60.0', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Q3 position = 3n/4 = 3×80/4 = 60.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 25 and width 10. What is the frequency density?', '250', '25', '10', '2.5', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 25/10 = 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 40 and width 5. What is the frequency density?', '5', '200', '40', '8.0', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 40/5 = 8.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 21 and width 10. What is the frequency density?', '10', '210', '2.1', '21', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 21/10 = 2.1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 14 and width 10. What is the frequency density?', '14', '1.4', '140', '10', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 14/10 = 1.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 35 and width 5. What is the frequency density?', '175', '5', '35', '7.0', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 35/5 = 7.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 32 and width 20. What is the frequency density?', '1.6', '20', '640', '32', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 32/20 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 38 and width 20. What is the frequency density?', '38', '1.9', '20', '760', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 38/20 = 1.9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A class has frequency 30 and width 20. What is the frequency density?', '1.5', '30', '20', '600', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', 'Frequency density = frequency/width = 30/20 = 1.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 75th percentile?', 'Cannot determine', '25', '37', '75', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '75th percentile position = 75% of 100 = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 90th percentile?', '10', '90', 'Cannot determine', '45', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '90th percentile position = 90% of 100 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 25th percentile?', '25', 'Cannot determine', '75', '12', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '25th percentile position = 25% of 100 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 75th percentile?', '37', 'Cannot determine', '25', '75', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '75th percentile position = 75% of 100 = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 25th percentile?', 'Cannot determine', '12', '75', '25', 3,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '25th percentile position = 25% of 100 = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 50th percentile?', 'Cannot determine', 'Cannot determine', '50', '25', 2,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '50th percentile position = 50% of 100 = 50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 75th percentile?', '75', 'Cannot determine', '25', '37', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '75th percentile position = 75% of 100 = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 75th percentile?', 'Cannot determine', '75', '37', '25', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '75th percentile position = 75% of 100 = 75', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 90th percentile?', '45', '90', 'Cannot determine', '10', 1,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '90th percentile position = 90% of 100 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 100 data points, at what position is the 90th percentile?', '90', '45', '10', 'Cannot determine', 0,
'lc_hl_statistics', 6, 'developing', 'lc_hl', '90th percentile position = 90% of 100 = 90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? As height increases, weight tends to increase', 'No correlation', 'Negative correlation', 'Positive correlation', 'Perfect correlation', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? As temperature increases, heating costs decrease', 'Negative correlation', 'Perfect correlation', 'Positive correlation', 'No correlation', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? Shoe size and IQ show no pattern', 'Positive correlation', 'No correlation', 'Weak correlation', 'Negative correlation', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows no correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? More study hours leads to higher exam scores', 'No correlation', 'Positive correlation', 'Negative correlation', 'Perfect correlation', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? Higher car age corresponds to lower value', 'Perfect correlation', 'Positive correlation', 'No correlation', 'Negative correlation', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? Hair colour and maths ability', 'Negative correlation', 'Weak positive correlation', 'Positive correlation', 'No correlation', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows no correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? As height increases, weight tends to increase', 'Negative correlation', 'Perfect correlation', 'No correlation', 'Positive correlation', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? As temperature increases, heating costs decrease', 'Perfect correlation', 'No correlation', 'Negative correlation', 'Positive correlation', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? Shoe size and IQ show no pattern', 'No correlation', 'Negative correlation', 'Positive correlation', 'Weak correlation', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows no correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? More study hours leads to higher exam scores', 'Positive correlation', 'Negative correlation', 'No correlation', 'Perfect correlation', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? Higher car age corresponds to lower value', 'Positive correlation', 'Perfect correlation', 'Negative correlation', 'No correlation', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What type of correlation? Hair colour and maths ability', 'Negative correlation', 'No correlation', 'Positive correlation', 'Weak positive correlation', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'This shows no correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = 0.35', 'Weak positive', 'No correlation', 'Weak negative', 'Strong positive', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = 0.35 indicates weak positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = -0.45', 'No correlation', 'Strong negative', 'Weak positive', 'Weak negative', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = -0.45 indicates weak negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = -0.98', 'No correlation', 'Strong negative', 'Weak negative', 'Strong positive', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = -0.98 indicates strong negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = 0.35', 'Strong positive', 'No correlation', 'Weak positive', 'Weak negative', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = 0.35 indicates weak positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = 0.75', 'Moderate negative', 'No correlation', 'Strong positive', 'Moderate positive', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = 0.75 indicates moderate positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = -0.45', 'No correlation', 'Weak positive', 'Weak negative', 'Strong negative', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = -0.45 indicates weak negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = -0.45', 'Weak positive', 'Weak negative', 'No correlation', 'Strong negative', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = -0.45 indicates weak negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = 0.95', 'Strong negative', 'No correlation', 'Strong positive', 'Weak positive', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = 0.95 indicates strong positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = -0.98', 'Weak negative', 'No correlation', 'Strong negative', 'Strong positive', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = -0.98 indicates strong negative correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Describe the correlation for r = 0.05', 'Very weak/none positive', 'Strong positive', 'No correlation', 'Very weak/none negative', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r = 0.05 indicates very weak/none positive correlation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The correlation coefficient r must be between:', '-∞ and ∞', '-1 and 1', '-100 and 100', '0 and 1', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: -1 and 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 1, this indicates:', 'Weak correlation', 'No correlation', 'Perfect positive correlation', 'Perfect negative correlation', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: Perfect positive correlation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = -1, this indicates:', 'No correlation', 'Perfect negative correlation', 'Perfect positive correlation', 'Strong positive correlation', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: Perfect negative correlation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0, this indicates:', 'Perfect correlation', 'Negative correlation', 'No linear correlation', 'Positive correlation', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: No linear correlation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Correlation measures:', 'The slope of the line', 'Causation', 'Strength and direction of linear relationship', 'The y-intercept', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: Strength and direction of linear relationship', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Does correlation imply causation?', 'Only for r > 0.9', 'Yes', 'Sometimes', 'No', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: No', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The correlation coefficient r must be between:', '0 and 1', '-1 and 1', '-100 and 100', '-∞ and ∞', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: -1 and 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 1, this indicates:', 'Weak correlation', 'Perfect positive correlation', 'No correlation', 'Perfect negative correlation', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'The answer is: Perfect positive correlation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.9, what percentage of variation in y is explained by x?', '81%', '40%', '90%', '19%', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.9² = 0.81, so 81% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.9, what percentage of variation in y is explained by x?', '19%', '81%', '90%', '40%', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.9² = 0.81, so 81% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.8, what percentage of variation in y is explained by x?', '36%', '64%', '80%', '32%', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.8² = 0.64, so 64% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.8, what percentage of variation in y is explained by x?', '80%', '64%', '36%', '32%', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.8² = 0.64, so 64% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = -0.8, what percentage of variation in y is explained by x?', '32%', '80%', '36%', '64%', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = -0.8² = 0.64, so 64% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.6, what percentage of variation in y is explained by x?', '60%', '64%', '36%', '18%', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.6² = 0.36, so 36% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = -0.9, what percentage of variation in y is explained by x?', '19%', '40%', '90%', '81%', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = -0.9² = 0.81, so 81% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.6, what percentage of variation in y is explained by x?', '60%', '36%', '18%', '64%', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.6² = 0.36, so 36% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.6, what percentage of variation in y is explained by x?', '64%', '36%', '18%', '60%', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.6² = 0.36, so 36% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.9, what percentage of variation in y is explained by x?', '40%', '19%', '90%', '81%', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'r² = 0.9² = 0.81, so 81% of variation is explained.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An outlier can:', 'Never affect r', 'Significantly affect r', 'Only decrease r', 'Only increase r', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Significantly affect r', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A single extreme point can:', 'Only weaken correlation', 'Only strengthen correlation', 'Have no effect', 'Make correlation appear stronger or weaker', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Make correlation appear stronger or weaker', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Before calculating correlation, you should:', 'Ignore any outliers', 'Remove all extreme values', 'Calculate mean first', 'Check for outliers in the scatter plot', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Check for outliers in the scatter plot', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An outlier can:', 'Never affect r', 'Only increase r', 'Significantly affect r', 'Only decrease r', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Significantly affect r', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A single extreme point can:', 'Only strengthen correlation', 'Make correlation appear stronger or weaker', 'Only weaken correlation', 'Have no effect', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Make correlation appear stronger or weaker', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Before calculating correlation, you should:', 'Remove all extreme values', 'Calculate mean first', 'Ignore any outliers', 'Check for outliers in the scatter plot', 3,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Check for outliers in the scatter plot', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An outlier can:', 'Significantly affect r', 'Only decrease r', 'Never affect r', 'Only increase r', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Significantly affect r', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A single extreme point can:', 'Make correlation appear stronger or weaker', 'Only weaken correlation', 'Only strengthen correlation', 'Have no effect', 0,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Make correlation appear stronger or weaker', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Before calculating correlation, you should:', 'Calculate mean first', 'Remove all extreme values', 'Check for outliers in the scatter plot', 'Ignore any outliers', 2,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Check for outliers in the scatter plot', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An outlier can:', 'Only increase r', 'Significantly affect r', 'Never affect r', 'Only decrease r', 1,
'lc_hl_statistics', 7, 'proficient', 'lc_hl', 'Significantly affect r', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for sales (€) vs advertising (€) has slope 3.0. What does this mean?', 'For each 1 unit increase in x, y increases by 3.0', 'y equals 3.0 when x is 0', 'The correlation is 3.0', 'x increases by 3.0 for each unit of y', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = 3.0 means For each 1 unit increase in x, y increases by 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for sales (€) vs advertising (€) has slope 2.5. What does this mean?', 'For each 1 unit increase in x, y increases by 2.5', 'x increases by 2.5 for each unit of y', 'y equals 2.5 when x is 0', 'The correlation is 2.5', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = 2.5 means For each 1 unit increase in x, y increases by 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for weight (kg) vs height (cm) has slope -2.0. What does this mean?', 'y equals -2.0 when x is 0', 'The correlation is -2.0', 'For each 1 unit increase in x, y decreases by 2.0', 'x increases by -2.0 for each unit of y', 2,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = -2.0 means For each 1 unit increase in x, y decreases by 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for weight (kg) vs height (cm) has slope 2.5. What does this mean?', 'The correlation is 2.5', 'For each 1 unit increase in x, y increases by 2.5', 'y equals 2.5 when x is 0', 'x increases by 2.5 for each unit of y', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = 2.5 means For each 1 unit increase in x, y increases by 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for score vs hours studied has slope 2.5. What does this mean?', 'For each 1 unit increase in x, y increases by 2.5', 'The correlation is 2.5', 'y equals 2.5 when x is 0', 'x increases by 2.5 for each unit of y', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = 2.5 means For each 1 unit increase in x, y increases by 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for score vs hours studied has slope -1.5. What does this mean?', 'y equals -1.5 when x is 0', 'x increases by -1.5 for each unit of y', 'The correlation is -1.5', 'For each 1 unit increase in x, y decreases by 1.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = -1.5 means For each 1 unit increase in x, y decreases by 1.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for weight (kg) vs height (cm) has slope -1.5. What does this mean?', 'y equals -1.5 when x is 0', 'x increases by -1.5 for each unit of y', 'The correlation is -1.5', 'For each 1 unit increase in x, y decreases by 1.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = -1.5 means For each 1 unit increase in x, y decreases by 1.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for weight (kg) vs height (cm) has slope 3.0. What does this mean?', 'y equals 3.0 when x is 0', 'The correlation is 3.0', 'x increases by 3.0 for each unit of y', 'For each 1 unit increase in x, y increases by 3.0', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = 3.0 means For each 1 unit increase in x, y increases by 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for score vs hours studied has slope 2.5. What does this mean?', 'x increases by 2.5 for each unit of y', 'The correlation is 2.5', 'y equals 2.5 when x is 0', 'For each 1 unit increase in x, y increases by 2.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = 2.5 means For each 1 unit increase in x, y increases by 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line for sales (€) vs advertising (€) has slope 1.5. What does this mean?', 'y equals 1.5 when x is 0', 'The correlation is 1.5', 'x increases by 1.5 for each unit of y', 'For each 1 unit increase in x, y increases by 1.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Slope = 1.5 means For each 1 unit increase in x, y increases by 1.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 19. What does this represent?', 'y increases by 19 per unit of x', 'The slope is 19', 'The correlation is 19', 'When x = 0, y = 19', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 19.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 41. What does this represent?', 'The correlation is 41', 'When x = 0, y = 41', 'The slope is 41', 'y increases by 41 per unit of x', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 41.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 16. What does this represent?', 'When x = 0, y = 16', 'y increases by 16 per unit of x', 'The slope is 16', 'The correlation is 16', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 16.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 15. What does this represent?', 'y increases by 15 per unit of x', 'The slope is 15', 'The correlation is 15', 'When x = 0, y = 15', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 15.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 20. What does this represent?', 'When x = 0, y = 20', 'The correlation is 20', 'The slope is 20', 'y increases by 20 per unit of x', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 20.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 31. What does this represent?', 'y increases by 31 per unit of x', 'The correlation is 31', 'When x = 0, y = 31', 'The slope is 31', 2,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 31.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 10. What does this represent?', 'y increases by 10 per unit of x', 'The slope is 10', 'The correlation is 10', 'When x = 0, y = 10', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 10.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A regression line has y-intercept 50. What does this represent?', 'y increases by 50 per unit of x', 'The slope is 50', 'The correlation is 50', 'When x = 0, y = 50', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The y-intercept is the value of y when x = 0, so y = 50.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.3x + 24. Predict y when x = 17.', 'Cannot determine', '56.1', '83.4', '80.1', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.3(17) + 24 = 56.1 + 24 = 80.1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.1x + 12. Predict y when x = 15.', '61.6', '46.5', 'Cannot determine', '58.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.1(15) + 12 = 46.5 + 12 = 58.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.6x + 18. Predict y when x = 15.', '54.0', '75.6', 'Cannot determine', '72.0', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.6(15) + 18 = 54.0 + 18 = 72.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.0x + 16. Predict y when x = 13.', '39.0', 'Cannot determine', '58.0', '55.0', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.0(13) + 16 = 39.0 + 16 = 55.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.7x + 12. Predict y when x = 5.', '34.2', 'Cannot determine', '18.5', '30.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.7(5) + 12 = 18.5 + 12 = 30.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.9x + 6. Predict y when x = 5.', '29.4', 'Cannot determine', '19.5', '25.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.9(5) + 6 = 19.5 + 6 = 25.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.1x + 25. Predict y when x = 16.', '74.6', '77.7', 'Cannot determine', '49.6', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.1(16) + 25 = 49.6 + 25 = 74.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 2.5x + 12. Predict y when x = 20.', '50.0', '62.0', 'Cannot determine', '64.5', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 2.5(20) + 12 = 50.0 + 12 = 62.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 1.9x + 7. Predict y when x = 20.', '46.9', 'Cannot determine', '38.0', '45.0', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 1.9(20) + 7 = 38.0 + 7 = 45.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line is y = 3.2x + 12. Predict y when x = 12.', 'Cannot determine', '50.4', '53.6', '38.4', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'y = 3.2(12) + 12 = 38.4 + 12 = 50.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 14 to x = 46. Predicting y for x = 24 is:', 'Extrapolation - less reliable prediction', 'Cannot make predictions', 'Interpolation - reliable prediction', 'Perfect prediction', 2,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting within the data range is interpolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 18 to x = 50. Predicting y for x = 70 is:', 'Cannot make predictions', 'Interpolation - reliable prediction', 'Perfect prediction', 'Extrapolation - less reliable prediction', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting outside the data range is extrapolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 18 to x = 48. Predicting y for x = 68 is:', 'Extrapolation - less reliable prediction', 'Cannot make predictions', 'Perfect prediction', 'Interpolation - reliable prediction', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting outside the data range is extrapolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 14 to x = 59. Predicting y for x = 24 is:', 'Cannot make predictions', 'Interpolation - reliable prediction', 'Perfect prediction', 'Extrapolation - less reliable prediction', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting within the data range is interpolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 19 to x = 55. Predicting y for x = 29 is:', 'Cannot make predictions', 'Extrapolation - less reliable prediction', 'Perfect prediction', 'Interpolation - reliable prediction', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting within the data range is interpolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 16 to x = 45. Predicting y for x = 26 is:', 'Extrapolation - less reliable prediction', 'Interpolation - reliable prediction', 'Cannot make predictions', 'Perfect prediction', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting within the data range is interpolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 13 to x = 54. Predicting y for x = 74 is:', 'Extrapolation - less reliable prediction', 'Cannot make predictions', 'Interpolation - reliable prediction', 'Perfect prediction', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting outside the data range is extrapolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Data ranges from x = 10 to x = 41. Predicting y for x = 20 is:', 'Perfect prediction', 'Cannot make predictions', 'Interpolation - reliable prediction', 'Extrapolation - less reliable prediction', 2,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Predicting within the data range is interpolation.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line always passes through:', 'The origin', '(0, 0)', '(1, 1)', '(x̄, ȳ)', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: (x̄, ȳ)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line minimises:', 'Sum of x values', 'Correlation', 'Sum of residuals', 'Sum of squared residuals', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: Sum of squared residuals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A residual is:', 'Predicted y - x', 'y-intercept', 'Slope × x', 'Actual y - Predicted y', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: Actual y - Predicted y', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If all points lie exactly on the regression line:', 'r = 0', 'r² = 1', 'Slope = 0', 'r² = 0', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: r² = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line always passes through:', '(x̄, ȳ)', '(1, 1)', 'The origin', '(0, 0)', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: (x̄, ȳ)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The regression line minimises:', 'Sum of squared residuals', 'Sum of x values', 'Sum of residuals', 'Correlation', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: Sum of squared residuals', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A residual is:', 'Predicted y - x', 'Slope × x', 'y-intercept', 'Actual y - Predicted y', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: Actual y - Predicted y', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If all points lie exactly on the regression line:', 'r = 0', 'r² = 1', 'r² = 0', 'Slope = 0', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'The answer is: r² = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given x̄ = 13, ȳ = 23, and slope = 2.4, find the regression equation.', 'y = -8.2x + 2.4', 'y = 2.4x + -8.2', 'y = 3.4x + -8.2', 'y = 2.4x + 23', 1,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Using ȳ = m·x̄ + c: 23 = 2.4×13 + c, so c = -8.2. Equation: y = 2.4x + -8.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given x̄ = 12, ȳ = 21, and slope = 1.8, find the regression equation.', 'y = 1.8x + -0.6', 'y = -0.6x + 1.8', 'y = 1.8x + 21', 'y = 2.8x + -0.6', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Using ȳ = m·x̄ + c: 21 = 1.8×12 + c, so c = -0.6. Equation: y = 1.8x + -0.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given x̄ = 5, ȳ = 31, and slope = 1.5, find the regression equation.', 'y = 1.5x + 23.5', 'y = 1.5x + 31', 'y = 23.5x + 1.5', 'y = 2.5x + 23.5', 0,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Using ȳ = m·x̄ + c: 31 = 1.5×5 + c, so c = 23.5. Equation: y = 1.5x + 23.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given x̄ = 6, ȳ = 22, and slope = 2.7, find the regression equation.', 'y = 2.7x + 22', 'y = 5.8x + 2.7', 'y = 3.7x + 5.8', 'y = 2.7x + 5.8', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Using ȳ = m·x̄ + c: 22 = 2.7×6 + c, so c = 5.8. Equation: y = 2.7x + 5.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given x̄ = 5, ȳ = 39, and slope = 2.7, find the regression equation.', 'y = 3.7x + 25.5', 'y = 2.7x + 39', 'y = 2.7x + 25.5', 'y = 25.5x + 2.7', 2,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Using ȳ = m·x̄ + c: 39 = 2.7×5 + c, so c = 25.5. Equation: y = 2.7x + 25.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Given x̄ = 15, ȳ = 25, and slope = 1.9, find the regression equation.', 'y = 2.9x + -3.5', 'y = -3.5x + 1.9', 'y = 1.9x + 25', 'y = 1.9x + -3.5', 3,
'lc_hl_statistics', 8, 'proficient', 'lc_hl', 'Using ȳ = m·x̄ + c: 25 = 1.9×15 + c, so c = -3.5. Equation: y = 1.9x + -3.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a coin is fair?', 'H₀: p ≠ 0.5', 'H₀: p = 0.5', 'H₀: p > 0.5', 'H₀: p < 0.5', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: p = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a new drug is better than standard?', 'H₀: μ₁ = μ₂', 'H₀: μ₁ > μ₂', 'H₀: μ₁ < μ₂', 'H₀: μ₁ ≠ μ₂', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: μ₁ = μ₂', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if average height differs from 170cm?', 'H₀: μ ≠ 170', 'H₀: μ = 170', 'H₀: μ > 170', 'H₀: μ < 170', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: μ = 170', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a process mean exceeds target?', 'H₀: μ ≤ target', 'H₀: μ ≠ target', 'H₀: μ = 0', 'H₀: μ > target', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: μ ≤ target', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a coin is fair?', 'H₀: p ≠ 0.5', 'H₀: p > 0.5', 'H₀: p = 0.5', 'H₀: p < 0.5', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: p = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a new drug is better than standard?', 'H₀: μ₁ < μ₂', 'H₀: μ₁ = μ₂', 'H₀: μ₁ ≠ μ₂', 'H₀: μ₁ > μ₂', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: μ₁ = μ₂', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if average height differs from 170cm?', 'H₀: μ > 170', 'H₀: μ = 170', 'H₀: μ ≠ 170', 'H₀: μ < 170', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: μ = 170', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a process mean exceeds target?', 'H₀: μ = 0', 'H₀: μ ≤ target', 'H₀: μ ≠ target', 'H₀: μ > target', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: μ ≤ target', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a coin is fair?', 'H₀: p ≠ 0.5', 'H₀: p = 0.5', 'H₀: p < 0.5', 'H₀: p > 0.5', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: p = 0.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the null hypothesis for: Testing if a new drug is better than standard?', 'H₀: μ₁ = μ₂', 'H₀: μ₁ < μ₂', 'H₀: μ₁ ≠ μ₂', 'H₀: μ₁ > μ₂', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The null hypothesis (H₀) represents no effect or no difference: H₀: μ₁ = μ₂', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rejecting H₀ when it is true', 'Power', 'Type I error', 'Type II error', 'Correct decision', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Type I error', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Failing to reject H₀ when it is false', 'Type I error', 'Type II error', 'Correct decision', 'Significance level', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Type II error', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of a Type I error is denoted by:', 'β (beta)', 'Power', 'p-value', 'α (alpha)', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: α (alpha)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of a Type II error is denoted by:', '1 - α', 'p-value', 'α (alpha)', 'β (beta)', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: β (beta)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Power of a test equals:', 'β', '1 - β', 'α', '1 - α', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: 1 - β', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A significant result means:', 'Reject H₀', 'Accept H₀', 'Inconclusive', 'Type II error', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rejecting H₀ when it is true', 'Correct decision', 'Type I error', 'Power', 'Type II error', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Type I error', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Failing to reject H₀ when it is false', 'Type I error', 'Significance level', 'Correct decision', 'Type II error', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Type II error', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of a Type I error is denoted by:', 'α (alpha)', 'β (beta)', 'p-value', 'Power', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: α (alpha)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The probability of a Type II error is denoted by:', 'p-value', 'α (alpha)', 'β (beta)', '1 - α', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: β (beta)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 5% significance level means:', '5% of data is significant', '5% chance of Type I error', '95% chance of error', '5% chance of Type II error', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: 5% chance of Type I error', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If α = 0.01, we:', 'Require stronger evidence to reject H₀', 'Have a larger Type I error rate', 'Have a 99% chance of error', 'Always reject H₀', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Require stronger evidence to reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Common significance levels are:', '0.05 and 0.01', '0.5 and 0.1', '0.95 and 0.99', '5 and 10', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: 0.05 and 0.01', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A smaller α means:', 'More likely to reject H₀', 'Larger Type I error', 'Weaker evidence needed', 'More conservative test', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: More conservative test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 5% significance level means:', '5% chance of Type I error', '5% chance of Type II error', '5% of data is significant', '95% chance of error', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: 5% chance of Type I error', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If α = 0.01, we:', 'Require stronger evidence to reject H₀', 'Have a larger Type I error rate', 'Always reject H₀', 'Have a 99% chance of error', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Require stronger evidence to reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Common significance levels are:', '0.95 and 0.99', '0.5 and 0.1', '5 and 10', '0.05 and 0.01', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: 0.05 and 0.01', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A smaller α means:', 'Larger Type I error', 'More conservative test', 'More likely to reject H₀', 'Weaker evidence needed', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: More conservative test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 5% significance level means:', '95% chance of error', '5% chance of Type II error', '5% chance of Type I error', '5% of data is significant', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: 5% chance of Type I error', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If α = 0.01, we:', 'Have a larger Type I error rate', 'Always reject H₀', 'Require stronger evidence to reject H₀', 'Have a 99% chance of error', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Require stronger evidence to reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.03 and α = 0.05, what is your conclusion?', 'Test is inconclusive', 'Fail to reject H₀', 'Accept H₁', 'Reject H₀', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.03) < α (0.05), so we reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.08 and α = 0.05, what is your conclusion?', 'Accept H₁', 'Test is inconclusive', 'Fail to reject H₀', 'Reject H₀', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.08) ≥ α (0.05), so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.04 and α = 0.05, what is your conclusion?', 'Accept H₁', 'Test is inconclusive', 'Fail to reject H₀', 'Reject H₀', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.04) < α (0.05), so we reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.06 and α = 0.05, what is your conclusion?', 'Test is inconclusive', 'Accept H₁', 'Fail to reject H₀', 'Reject H₀', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.06) ≥ α (0.05), so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.06 and α = 0.05, what is your conclusion?', 'Test is inconclusive', 'Accept H₁', 'Reject H₀', 'Fail to reject H₀', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.06) ≥ α (0.05), so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.03 and α = 0.05, what is your conclusion?', 'Reject H₀', 'Accept H₁', 'Fail to reject H₀', 'Test is inconclusive', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.03) < α (0.05), so we reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.04 and α = 0.05, what is your conclusion?', 'Fail to reject H₀', 'Reject H₀', 'Accept H₁', 'Test is inconclusive', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.04) < α (0.05), so we reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.08 and α = 0.05, what is your conclusion?', 'Reject H₀', 'Fail to reject H₀', 'Test is inconclusive', 'Accept H₁', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.08) ≥ α (0.05), so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.06 and α = 0.05, what is your conclusion?', 'Test is inconclusive', 'Accept H₁', 'Reject H₀', 'Fail to reject H₀', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.06) ≥ α (0.05), so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If p-value = 0.12 and α = 0.05, what is your conclusion?', 'Accept H₁', 'Reject H₀', 'Test is inconclusive', 'Fail to reject H₀', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'p-value (0.12) ≥ α (0.05), so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ ≠ 50', 'Z-test only', 'One-tailed test', 'Two-tailed test', 'No test needed', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Two-tailed test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ > 100', 'One-tailed test (right)', 'One-tailed test (left)', 'No test needed', 'Two-tailed test', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: One-tailed test (right)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ < 30', 'One-tailed test (right)', 'No test needed', 'Two-tailed test', 'One-tailed test (left)', 3,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: One-tailed test (left)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('H₁: p ≠ 0.5 suggests:', 'No hypothesis test', 'Two-tailed test', 'One-tailed test', 'Chi-square test', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Two-tailed test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ ≠ 50', 'No test needed', 'Two-tailed test', 'One-tailed test', 'Z-test only', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Two-tailed test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ > 100', 'Two-tailed test', 'One-tailed test (right)', 'One-tailed test (left)', 'No test needed', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: One-tailed test (right)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ < 30', 'Two-tailed test', 'One-tailed test (left)', 'One-tailed test (right)', 'No test needed', 1,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: One-tailed test (left)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('H₁: p ≠ 0.5 suggests:', 'No hypothesis test', 'One-tailed test', 'Two-tailed test', 'Chi-square test', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Two-tailed test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ ≠ 50', 'Two-tailed test', 'Z-test only', 'One-tailed test', 'No test needed', 0,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: Two-tailed test', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Testing if μ > 100', 'One-tailed test (left)', 'No test needed', 'One-tailed test (right)', 'Two-tailed test', 2,
'lc_hl_statistics', 9, 'proficient', 'lc_hl', 'The answer is: One-tailed test (right)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 99% confidence interval (54, 66) for the population mean.', 'The mean equals 60.0 with 99% certainty', 'We are 99% confident the true mean lies between 54 and 66', 'The probability the mean is between 54 and 66 is 99%', '99% of the data lies between 54 and 66', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 99% confident the true mean lies between 54 and 66. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 99% confidence interval (54, 68) for the population mean.', 'The probability the mean is between 54 and 68 is 99%', 'We are 99% confident the true mean lies between 54 and 68', '99% of the data lies between 54 and 68', 'The mean equals 61.0 with 99% certainty', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 99% confident the true mean lies between 54 and 68. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 95% confidence interval (45, 60) for the population mean.', '95% of the data lies between 45 and 60', 'We are 95% confident the true mean lies between 45 and 60', 'The probability the mean is between 45 and 60 is 95%', 'The mean equals 52.5 with 95% certainty', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 95% confident the true mean lies between 45 and 60. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 95% confidence interval (53, 68) for the population mean.', 'The mean equals 60.5 with 95% certainty', 'The probability the mean is between 53 and 68 is 95%', '95% of the data lies between 53 and 68', 'We are 95% confident the true mean lies between 53 and 68', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 95% confident the true mean lies between 53 and 68. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 90% confidence interval (54, 62) for the population mean.', '90% of the data lies between 54 and 62', 'The mean equals 58.0 with 90% certainty', 'We are 90% confident the true mean lies between 54 and 62', 'The probability the mean is between 54 and 62 is 90%', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 90% confident the true mean lies between 54 and 62. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 99% confidence interval (52, 58) for the population mean.', 'The probability the mean is between 52 and 58 is 99%', '99% of the data lies between 52 and 58', 'The mean equals 55.0 with 99% certainty', 'We are 99% confident the true mean lies between 52 and 58', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 99% confident the true mean lies between 52 and 58. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 95% confidence interval (47, 53) for the population mean.', 'The probability the mean is between 47 and 53 is 95%', 'We are 95% confident the true mean lies between 47 and 53', '95% of the data lies between 47 and 53', 'The mean equals 50.0 with 95% certainty', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 95% confident the true mean lies between 47 and 53. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 95% confidence interval (47, 60) for the population mean.', 'The mean equals 53.5 with 95% certainty', '95% of the data lies between 47 and 60', 'The probability the mean is between 47 and 60 is 95%', 'We are 95% confident the true mean lies between 47 and 60', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 95% confident the true mean lies between 47 and 60. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 90% confidence interval (50, 62) for the population mean.', 'The probability the mean is between 50 and 62 is 90%', '90% of the data lies between 50 and 62', 'We are 90% confident the true mean lies between 50 and 62', 'The mean equals 56.0 with 90% certainty', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 90% confident the true mean lies between 50 and 62. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Interpret the 90% confidence interval (54, 68) for the population mean.', 'The mean equals 61.0 with 90% certainty', 'The probability the mean is between 54 and 68 is 90%', 'We are 90% confident the true mean lies between 54 and 68', '90% of the data lies between 54 and 68', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'We are 90% confident the true mean lies between 54 and 68. This is about the procedure, not the specific interval.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 95% CI with σ = 7, n = 64, z = 1.96.', '3.42', '1.71', '13.72', '17.92', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.96 × 7/√64 = 1.71', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 90% CI with σ = 15, n = 25, z = 1.645.', '24.68', '4.94', '2.74', '9.88', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.645 × 15/√25 = 4.94', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 99% CI with σ = 8, n = 100, z = 2.576.', '20.61', '2.06', '4.12', '32.2', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 2.576 × 8/√100 = 2.06', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 90% CI with σ = 12, n = 36, z = 1.645.', '6.58', '19.74', '3.29', '4.93', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.645 × 12/√36 = 3.29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 90% CI with σ = 15, n = 49, z = 1.645.', '3.52', '7.04', '24.68', '5.37', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.645 × 15/√49 = 3.52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 90% CI with σ = 5, n = 49, z = 1.645.', '16.12', '1.18', '2.36', '8.22', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.645 × 5/√49 = 1.18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 95% CI with σ = 15, n = 64, z = 1.96.', '3.67', '29.4', '7.34', '8.36', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.96 × 15/√64 = 3.67', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 90% CI with σ = 7, n = 64, z = 1.645.', '15.04', '2.88', '11.52', '1.44', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.645 × 7/√64 = 1.44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 95% CI with σ = 12, n = 25, z = 1.96.', '4.7', '9.4', '4.08', '23.52', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.96 × 12/√25 = 4.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the margin of error for a 90% CI with σ = 8, n = 64, z = 1.645.', 'Cannot determine', '3.3', '13.16', '1.65', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'ME = z × σ/√n = 1.645 × 8/√64 = 1.65', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Increasing sample size will:', 'Widen the confidence interval', 'Narrow the confidence interval', 'Not affect the interval', 'Increase confidence level', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Narrow the confidence interval', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Doubling the sample size will:', 'Not affect width', 'Halve the width', 'Double the width', 'Decrease width by factor of √2', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Decrease width by factor of √2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To halve the margin of error, sample size must:', 'Stay the same', 'Double', 'Quadruple', 'Halve', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Quadruple', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Larger n leads to:', 'Wider interval', 'Lower confidence', 'More precise estimate', 'Larger margin of error', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: More precise estimate', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Increasing sample size will:', 'Narrow the confidence interval', 'Increase confidence level', 'Widen the confidence interval', 'Not affect the interval', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Narrow the confidence interval', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Doubling the sample size will:', 'Halve the width', 'Double the width', 'Not affect width', 'Decrease width by factor of √2', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Decrease width by factor of √2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To halve the margin of error, sample size must:', 'Double', 'Stay the same', 'Halve', 'Quadruple', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Quadruple', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Larger n leads to:', 'Lower confidence', 'More precise estimate', 'Larger margin of error', 'Wider interval', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: More precise estimate', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 99% CI compared to a 95% CI is:', 'More precise', 'The same width', 'Wider', 'Narrower', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Wider', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Higher confidence level means:', 'Lower margin of error', 'Wider interval', 'Narrower interval', 'Smaller z-value', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Wider interval', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The z-value for 95% confidence is approximately:', '2.576', '1.96', '1.645', '1.28', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: 1.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The z-value for 99% confidence is approximately:', '3.00', '2.576', '1.96', '1.645', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: 2.576', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 99% CI compared to a 95% CI is:', 'Narrower', 'More precise', 'Wider', 'The same width', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Wider', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Higher confidence level means:', 'Narrower interval', 'Wider interval', 'Lower margin of error', 'Smaller z-value', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Wider interval', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The z-value for 95% confidence is approximately:', '2.576', '1.96', '1.28', '1.645', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: 1.96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The z-value for 99% confidence is approximately:', '2.576', '1.96', '1.645', '3.00', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: 2.576', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 45 and margin of error = 4, what is the confidence interval?', '(41, 49)', '(41, 45)', '(45, 49)', '(43.0, 47.0)', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (45 - 4, 45 + 4) = (41, 49)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 48 and margin of error = 3, what is the confidence interval?', '(46.5, 49.5)', '(48, 51)', '(45, 48)', '(45, 51)', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (48 - 3, 48 + 3) = (45, 51)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 45 and margin of error = 6, what is the confidence interval?', '(45, 51)', '(39, 51)', '(42.0, 48.0)', '(39, 45)', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (45 - 6, 45 + 6) = (39, 51)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 52 and margin of error = 7, what is the confidence interval?', '(48.5, 55.5)', '(45, 59)', '(52, 59)', '(45, 52)', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (52 - 7, 52 + 7) = (45, 59)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 55 and margin of error = 6, what is the confidence interval?', '(49, 61)', '(52.0, 58.0)', '(49, 55)', '(55, 61)', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (55 - 6, 55 + 6) = (49, 61)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 46 and margin of error = 4, what is the confidence interval?', '(42, 46)', '(42, 50)', '(44.0, 48.0)', '(46, 50)', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (46 - 4, 46 + 4) = (42, 50)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 52 and margin of error = 8, what is the confidence interval?', '(48.0, 56.0)', '(44, 52)', '(52, 60)', '(44, 60)', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (52 - 8, 52 + 8) = (44, 60)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If x̄ = 49 and margin of error = 4, what is the confidence interval?', '(45, 53)', '(47.0, 51.0)', '(49, 53)', '(45, 49)', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'CI = (x̄ - ME, x̄ + ME) = (49 - 4, 49 + 4) = (45, 53)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 95% CI for μ is (52, 58), testing H₀: μ = 50 at α = 0.05:', 'Cannot determine', 'Fail to reject H₀', 'Accept H₀', 'Reject H₀', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 95% CI for μ is (48, 56), testing H₀: μ = 50 at α = 0.05:', 'Accept H₁', 'Reject H₀', 'Fail to reject H₀', 'Cannot determine', 2,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Fail to reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If H₀ value is inside the CI:', 'Need more data', 'Fail to reject H₀', 'Reject H₀', 'Test is inconclusive', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Fail to reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If H₀ value is outside the CI:', 'Need larger sample', 'Accept H₀', 'Fail to reject H₀', 'Reject H₀', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 95% CI for μ is (52, 58), testing H₀: μ = 50 at α = 0.05:', 'Accept H₀', 'Fail to reject H₀', 'Cannot determine', 'Reject H₀', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 95% CI for μ is (48, 56), testing H₀: μ = 50 at α = 0.05:', 'Reject H₀', 'Cannot determine', 'Accept H₁', 'Fail to reject H₀', 3,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Fail to reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If H₀ value is inside the CI:', 'Test is inconclusive', 'Fail to reject H₀', 'Need more data', 'Reject H₀', 1,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Fail to reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If H₀ value is outside the CI:', 'Reject H₀', 'Fail to reject H₀', 'Accept H₀', 'Need larger sample', 0,
'lc_hl_statistics', 10, 'advanced', 'lc_hl', 'The answer is: Reject H₀', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The Central Limit Theorem states that sample means:', 'Equal the population mean', 'Are always exactly normal', 'Are approximately normally distributed for large n', 'Have the same variance as the population', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Are approximately normally distributed for large n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('CLT applies when sample size is:', 'Large (typically n ≥ 30)', 'n = 100 exactly', 'Any size', 'n < 30 only', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Large (typically n ≥ 30)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The standard error of the mean equals:', 'σ', 'σ×n', 'σ/n', 'σ/√n', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: σ/√n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('As sample size increases, standard error:', 'Stays the same', 'Increases', 'Becomes zero', 'Decreases', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Decreases', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sampling distribution of x̄ has mean:', 'x̄', 'σ', 'μ (population mean)', '0', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: μ (population mean)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The Central Limit Theorem states that sample means:', 'Have the same variance as the population', 'Equal the population mean', 'Are always exactly normal', 'Are approximately normally distributed for large n', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Are approximately normally distributed for large n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('CLT applies when sample size is:', 'Large (typically n ≥ 30)', 'n < 30 only', 'n = 100 exactly', 'Any size', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Large (typically n ≥ 30)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The standard error of the mean equals:', 'σ×n', 'σ/n', 'σ/√n', 'σ', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: σ/√n', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('As sample size increases, standard error:', 'Increases', 'Becomes zero', 'Decreases', 'Stays the same', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Decreases', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The sampling distribution of x̄ has mean:', 'σ', '0', 'μ (population mean)', 'x̄', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: μ (population mean)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 12 and n = 16, what is the standard error of the mean?', '12', '48.0', '0.75', '3.0', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 12/√16 = 12/4 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 10 and n = 16, what is the standard error of the mean?', '0.62', '2.5', '40.0', '10', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 10/√16 = 10/4 = 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 20 and n = 64, what is the standard error of the mean?', '20', '160.0', '2.5', '0.31', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 20/√64 = 20/8 = 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 12 and n = 64, what is the standard error of the mean?', '12', '96.0', '1.5', '0.19', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 12/√64 = 12/8 = 1.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 10 and n = 25, what is the standard error of the mean?', '0.4', '50.0', '2.0', '10', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 10/√25 = 10/5 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 20 and n = 36, what is the standard error of the mean?', '0.56', '3.33', '20', '120.0', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 20/√36 = 20/6 = 3.33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 15 and n = 64, what is the standard error of the mean?', '15', '120.0', '1.88', '0.23', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 15/√64 = 15/8 = 1.88', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 15 and n = 64, what is the standard error of the mean?', '15', '120.0', '1.88', '0.23', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 15/√64 = 15/8 = 1.88', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 20 and n = 100, what is the standard error of the mean?', '2.0', '20', '0.2', '200.0', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 20/√100 = 20/10 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If σ = 20 and n = 64, what is the standard error of the mean?', '0.31', '160.0', '20', '2.5', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = σ/√n = 20/√64 = 20/8 = 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 49, μ₀ = 50, σ = 10, n = 36', '0.6', '-0.6', '-1.2', '-0.1', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (49 - 50)/(10/√36) = -0.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 49, μ₀ = 50, σ = 10, n = 36', '0.6', '-0.1', '-0.6', '-1.2', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (49 - 50)/(10/√36) = -0.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 51, μ₀ = 50, σ = 10, n = 64', '0.1', '-0.8', '0.8', '1.6', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (51 - 50)/(10/√64) = 0.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 48, μ₀ = 50, σ = 11, n = 36', '-0.18', '1.09', '-2.18', '-1.09', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (48 - 50)/(11/√36) = -1.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 52, μ₀ = 50, σ = 11, n = 36', '-1.09', '1.09', '0.18', '2.18', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (52 - 50)/(11/√36) = 1.09', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 48, μ₀ = 50, σ = 9, n = 36', '-0.22', '-2.66', '-1.33', '1.33', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (48 - 50)/(9/√36) = -1.33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 48, μ₀ = 50, σ = 11, n = 100', '-1.82', '-3.64', '1.82', '-0.18', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (48 - 50)/(11/√100) = -1.82', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Calculate the z-statistic: x̄ = 52, μ₀ = 50, σ = 10, n = 36', '0.2', '-1.2', '1.2', '2.4', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'z = (x̄ - μ)/(σ/√n) = (52 - 50)/(10/√36) = 1.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use t-distribution instead of z when:', 'Sample mean is known', 'Population σ is unknown', 'Population is normal', 'n is large', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Population σ is unknown', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Degrees of freedom for one-sample t-test:', 'n + 1', 'n - 1', 'n/2', 'n', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: n - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('As df increases, t-distribution:', 'Changes shape randomly', 'Becomes more spread out', 'Approaches normal distribution', 'Has larger critical values', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Approaches normal distribution', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('T-distribution compared to normal is:', 'Narrower', 'Only positive values', 'Identical', 'More spread out with heavier tails', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: More spread out with heavier tails', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use t-distribution instead of z when:', 'Sample mean is known', 'Population σ is unknown', 'Population is normal', 'n is large', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Population σ is unknown', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Degrees of freedom for one-sample t-test:', 'n + 1', 'n/2', 'n', 'n - 1', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: n - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('As df increases, t-distribution:', 'Approaches normal distribution', 'Has larger critical values', 'Becomes more spread out', 'Changes shape randomly', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Approaches normal distribution', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('T-distribution compared to normal is:', 'Identical', 'Narrower', 'Only positive values', 'More spread out with heavier tails', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: More spread out with heavier tails', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.5, n = 400', '0.025', '0.25', '0.035', 'Cannot determine', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.5×0.5/400) = 0.025', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.45, n = 400', '0.248', '0.022', '0.034', '0.025', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.45×0.55/400) = 0.025', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.45, n = 100', '0.067', '0.248', '0.045', '0.05', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.45×0.55/100) = 0.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.54, n = 100', '0.054', '0.05', '0.248', '0.073', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.54×0.46/100) = 0.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.55, n = 100', '0.05', '0.074', '0.055', '0.247', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.55×0.45/100) = 0.05', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.41, n = 200', '0.029', '0.035', '0.045', '0.242', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.41×0.59/200) = 0.035', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.6, n = 400', '0.03', '0.24', '0.024', '0.039', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.6×0.4/400) = 0.024', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find SE for a proportion: p̂ = 0.54, n = 200', '0.248', '0.035', '0.038', '0.052', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'SE = √(p̂(1-p̂)/n) = √(0.54×0.46/200) = 0.035', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To decrease margin of error by half, sample size must:', 'Halve', 'Stay the same', 'Double', 'Quadruple', 3,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Quadruple', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 95% CI with ME = 2 and σ = 10, minimum n is approximately:', '200', '50', '96', '25', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: 96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Larger desired confidence level requires:', 'Same sample size', 'Larger sample size', 'Cannot determine', 'Smaller sample size', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Larger sample size', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Smaller desired margin of error requires:', 'Larger sample size', 'Smaller sample size', 'Same sample size', 'Higher confidence', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Larger sample size', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To decrease margin of error by half, sample size must:', 'Quadruple', 'Stay the same', 'Halve', 'Double', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Quadruple', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For 95% CI with ME = 2 and σ = 10, minimum n is approximately:', '200', '50', '96', '25', 2,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: 96', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Larger desired confidence level requires:', 'Cannot determine', 'Larger sample size', 'Smaller sample size', 'Same sample size', 1,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Larger sample size', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Smaller desired margin of error requires:', 'Larger sample size', 'Higher confidence', 'Smaller sample size', 'Same sample size', 0,
'lc_hl_statistics', 11, 'advanced', 'lc_hl', 'The answer is: Larger sample size', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 101, s = 15, n = 36, z = 1.96', '(96.1, 105.9)', '(94.1, 107.9)', '(86, 116)', '(101, 105.9)', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 15/√36 = 4.9. CI = (101 ± 4.9) = (96.1, 105.9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 100, s = 12, n = 36, z = 1.96', '(100, 103.92)', '(96.08, 103.92)', '(94.08, 105.92)', '(88, 112)', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 12/√36 = 3.92. CI = (100 ± 3.92) = (96.08, 103.92)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 101, s = 11, n = 25, z = 1.96', '(101, 105.31)', '(94.69, 107.31)', '(96.69, 105.31)', '(90, 112)', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 11/√25 = 4.31. CI = (101 ± 4.31) = (96.69, 105.31)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 102, s = 18, n = 36, z = 1.96', '(96.12, 107.88)', '(84, 120)', '(94.12, 109.88)', '(102, 107.88)', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 18/√36 = 5.88. CI = (102 ± 5.88) = (96.12, 107.88)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 96, s = 15, n = 49, z = 1.96', '(89.8, 102.2)', '(91.8, 100.2)', '(96, 100.2)', '(81, 111)', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 15/√49 = 4.2. CI = (96 ± 4.2) = (91.8, 100.2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 96, s = 13, n = 49, z = 1.96', '(83, 109)', '(90.36, 101.64)', '(96, 99.64)', '(92.36, 99.64)', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 13/√49 = 3.64. CI = (96 ± 3.64) = (92.36, 99.64)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 100, s = 17, n = 25, z = 1.96', '(100, 106.66)', '(93.34, 106.66)', '(91.34, 108.66)', '(83, 117)', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 17/√25 = 6.66. CI = (100 ± 6.66) = (93.34, 106.66)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Construct a 95% CI: x̄ = 105, s = 17, n = 25, z = 1.96', '(98.34, 111.66)', '(96.34, 113.66)', '(105, 111.66)', '(88, 122)', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'ME = 1.96 × 17/√25 = 6.66. CI = (105 ± 6.66) = (98.34, 111.66)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = 1.56, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Fail to reject H₀ (not significant)', 'Accept H₁', 'Test inconclusive', 'Reject H₀ (significant result)', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|1.56| ≤ 1.96, so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = 2.54, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Accept H₁', 'Fail to reject H₀ (not significant)', 'Test inconclusive', 'Reject H₀ (significant result)', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|2.54| > 1.96, so we reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = -2.82, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Accept H₁', 'Fail to reject H₀ (not significant)', 'Test inconclusive', 'Reject H₀ (significant result)', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|-2.82| > 1.96, so we reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = -1.08, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Reject H₀ (significant result)', 'Accept H₁', 'Test inconclusive', 'Fail to reject H₀ (not significant)', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|-1.08| ≤ 1.96, so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = -2.46, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Reject H₀ (significant result)', 'Accept H₁', 'Test inconclusive', 'Fail to reject H₀ (not significant)', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|-2.46| > 1.96, so we reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = -0.46, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Fail to reject H₀ (not significant)', 'Reject H₀ (significant result)', 'Accept H₁', 'Test inconclusive', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|-0.46| ≤ 1.96, so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = -0.14, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Reject H₀ (significant result)', 'Accept H₁', 'Fail to reject H₀ (not significant)', 'Test inconclusive', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|-0.14| ≤ 1.96, so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('z = -0.71, α = 0.05 (two-tailed, critical = ±1.96). Decision?', 'Accept H₁', 'Fail to reject H₀ (not significant)', 'Reject H₀ (significant result)', 'Test inconclusive', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', '|-0.71| ≤ 1.96, so we fail to reject h₀.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 20, 21, 21, 39, 40', '22', '15', '21', '30.2', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The median = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the mean of: 15, 18, 20, 31, 39', '24.6', '21', '26.6', '19', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The mean = 24.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 11, 21, 28, 38, 49', '29', '33', '31.4', '28', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The median = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 11, 16, 21, 26, 30', '22.8', '14', '22', '21', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The median = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 12, 14, 17, 18, 36', '17', '21.4', '18', '19', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The median = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 17, 21, 43, 44, 46', '44', '36.2', '24', '29', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The range = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the range of: 12, 14, 22, 37, 39', '22', '23', '27', '26.8', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The range = 27', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the median of: 24, 40, 40, 47, 49', '40', '42.0', '41', '20', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The median = 40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.85, slope = 2.1, intercept = 12, express the regression with r².', 'y = 2.1x + 12, r² = 0.85', 'y = 12x + 2.1, r² = 0.72', 'y = 2.1x + 12, r² = 0.72', 'y = -2.1x + 12, r² = 0.72', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'r² = 0.85² = 0.72. Equation: y = 2.1x + 12, r² = 0.72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.9, slope = 2.5, intercept = 11, express the regression with r².', 'y = 11x + 2.5, r² = 0.81', 'y = 2.5x + 11, r² = 0.81', 'y = 2.5x + 11, r² = 0.9', 'y = -2.5x + 11, r² = 0.81', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'r² = 0.9² = 0.81. Equation: y = 2.5x + 11, r² = 0.81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.9, slope = 3.3, intercept = 10, express the regression with r².', 'y = 3.3x + 10, r² = 0.81', 'y = -3.3x + 10, r² = 0.81', 'y = 3.3x + 10, r² = 0.9', 'y = 10x + 3.3, r² = 0.81', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'r² = 0.9² = 0.81. Equation: y = 3.3x + 10, r² = 0.81', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = -0.8, slope = -2.6, intercept = 15, express the regression with r².', 'y = 15x + -2.6, r² = 0.64', 'y = -2.6x + 15, r² = 0.64', 'y = 2.6x + 15, r² = 0.64', 'y = -2.6x + 15, r² = 0.8', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'r² = -0.8² = 0.64. Equation: y = -2.6x + 15, r² = 0.64', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.85, slope = 3.5, intercept = 20, express the regression with r².', 'y = -3.5x + 20, r² = 0.72', 'y = 3.5x + 20, r² = 0.85', 'y = 20x + 3.5, r² = 0.72', 'y = 3.5x + 20, r² = 0.72', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'r² = 0.85² = 0.72. Equation: y = 3.5x + 20, r² = 0.72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If r = 0.85, slope = 3.1, intercept = 12, express the regression with r².', 'y = 3.1x + 12, r² = 0.72', 'y = 3.1x + 12, r² = 0.85', 'y = 12x + 3.1, r² = 0.72', 'y = -3.1x + 12, r² = 0.72', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'r² = 0.85² = 0.72. Equation: y = 3.1x + 12, r² = 0.72', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Scores ~ N(100, 15²). Calculate z for score = 115.', '1.0', '-1.0', '2.0', '15', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'z = (115 - 100)/15 = 1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Scores ~ N(100, 15²). Calculate z for score = 70.', '-30', '-2.0', '2.0', '-1.0', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'z = (70 - 100)/15 = -2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Scores ~ N(100, 15²). Calculate z for score = 70.', '2.0', '-1.0', '-30', '-2.0', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'z = (70 - 100)/15 = -2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Scores ~ N(100, 15²). Calculate z for score = 115.', '2.0', '15', '-1.0', '1.0', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'z = (115 - 100)/15 = 1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Scores ~ N(100, 15²). Calculate z for score = 115.', '15', '1.0', '-1.0', '2.0', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'z = (115 - 100)/15 = 1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Scores ~ N(100, 15²). Calculate z for score = 85.', '-1.0', '0.0', '1.0', '-15', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'z = (85 - 100)/15 = -1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Population: μ = 46, σ = 8. For samples of size 25, the sampling distribution of x̄ has:', 'Mean = 46, SE = 8', 'Mean = 46, SE = 1.6', 'Mean = 46, SE = 0.32', 'Mean = 51, SE = 1.6', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'Mean of x̄ = μ = 46. SE = σ/√n = 8/√25 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Population: μ = 48, σ = 10. For samples of size 25, the sampling distribution of x̄ has:', 'Mean = 48, SE = 2.0', 'Mean = 48, SE = 10', 'Mean = 53, SE = 2.0', 'Mean = 48, SE = 0.4', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'Mean of x̄ = μ = 48. SE = σ/√n = 10/√25 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Population: μ = 53, σ = 8. For samples of size 16, the sampling distribution of x̄ has:', 'Mean = 53, SE = 8', 'Mean = 53, SE = 0.5', 'Mean = 58, SE = 2.0', 'Mean = 53, SE = 2.0', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'Mean of x̄ = μ = 53. SE = σ/√n = 8/√16 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Population: μ = 50, σ = 12. For samples of size 16, the sampling distribution of x̄ has:', 'Mean = 50, SE = 12', 'Mean = 50, SE = 3.0', 'Mean = 55, SE = 3.0', 'Mean = 50, SE = 0.75', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'Mean of x̄ = μ = 50. SE = σ/√n = 12/√16 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Population: μ = 48, σ = 12. For samples of size 36, the sampling distribution of x̄ has:', 'Mean = 48, SE = 12', 'Mean = 48, SE = 2.0', 'Mean = 48, SE = 0.33', 'Mean = 53, SE = 2.0', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'Mean of x̄ = μ = 48. SE = σ/√n = 12/√36 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Population: μ = 54, σ = 12. For samples of size 36, the sampling distribution of x̄ has:', 'Mean = 59, SE = 2.0', 'Mean = 54, SE = 2.0', 'Mean = 54, SE = 12', 'Mean = 54, SE = 0.33', 1,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'Mean of x̄ = μ = 54. SE = σ/√n = 12/√36 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A study with n=10 finds p=0.04. Most appropriate response:', 'Results suggest significance but small sample warrants caution', 'Result is not significant', 'Definitely reject H₀', 'Increase α to 0.10', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: Results suggest significance but small sample warrants caution', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two variables correlate (r=0.9). Can we conclude causation?', 'Yes, strong correlation proves causation', 'Yes, if p < 0.05', 'No, correlation does not imply causation', 'Only if r > 0.95', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: No, correlation does not imply causation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 95% CI is (45, 55). A 99% CI would be:', 'Wider than (45, 55)', 'The same', '(45, 55) exactly', 'Narrower than (45, 55)', 0,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: Wider than (45, 55)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sample mean differs from population mean. This is due to:', 'Calculation error', 'Invalid sample', 'Sampling variability', 'Bias only', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: Sampling variability', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A study with n=10 finds p=0.04. Most appropriate response:', 'Definitely reject H₀', 'Increase α to 0.10', 'Result is not significant', 'Results suggest significance but small sample warrants caution', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: Results suggest significance but small sample warrants caution', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two variables correlate (r=0.9). Can we conclude causation?', 'Yes, if p < 0.05', 'Only if r > 0.95', 'Yes, strong correlation proves causation', 'No, correlation does not imply causation', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: No, correlation does not imply causation', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A 95% CI is (45, 55). A 99% CI would be:', '(45, 55) exactly', 'The same', 'Narrower than (45, 55)', 'Wider than (45, 55)', 3,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: Wider than (45, 55)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Sample mean differs from population mean. This is due to:', 'Invalid sample', 'Calculation error', 'Sampling variability', 'Bias only', 2,
'lc_hl_statistics', 12, 'advanced', 'lc_hl', 'The answer is: Sampling variability', 1);