-- LC Ordinary Level - Applied Measure Complete SQL
-- Generated: 2025-12-15
-- Total: 600 questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Applied Measure topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_ol_applied_measure', 'Applied Measure', id, '📐', 7, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_ol_applied_measure';

-- Insert questions
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 215 cm to metres.', '21500 m', '21.5 m', '2.15 m', '2150 m', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '215 cm ÷ 100 = 2.15 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 419 cm to metres.', '41.9 m', '4190 m', '4.19 m', '41900 m', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '419 cm ÷ 100 = 4.19 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 221 cm to metres.', '2.21 m', '22.1 m', '22100 m', '2210 m', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '221 cm ÷ 100 = 2.21 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 465 cm to metres.', '46.5 m', '4.65 m', '4650 m', '46500 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '465 cm ÷ 100 = 4.65 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 343 cm to metres.', '34300 m', '3430 m', '3.43 m', '34.3 m', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '343 cm ÷ 100 = 3.43 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 462 cm to metres.', '4620 m', '46.2 m', '4.62 m', '46200 m', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '462 cm ÷ 100 = 4.62 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 386 cm to metres.', '38600 m', '3.86 m', '3860 m', '38.6 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '386 cm ÷ 100 = 3.86 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 345 cm to metres.', '34.5 m', '3.45 m', '3450 m', '34500 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '345 cm ÷ 100 = 3.45 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 310 cm to metres.', '3100 m', '31.0 m', '31000 m', '3.1 m', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '310 cm ÷ 100 = 3.1 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 307 cm to metres.', '30700 m', '3.07 m', '3070 m', '30.7 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '307 cm ÷ 100 = 3.07 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 260 cm to metres.', '26.0 m', '26000 m', '2.6 m', '2600 m', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '260 cm ÷ 100 = 2.6 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 243 cm to metres.', '2.43 m', '24.3 m', '2430 m', '24300 m', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '243 cm ÷ 100 = 2.43 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 400 cm to metres.', '40.0 m', '4 m', '40000 m', '4000 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '400 cm ÷ 100 = 4 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 289 cm to metres.', '2.89 m', '2890 m', '28900 m', '28.9 m', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '289 cm ÷ 100 = 2.89 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 434 cm to metres.', '43400 m', '4.34 m', '43.4 m', '4340 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '434 cm ÷ 100 = 4.34 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3727 m to kilometres.', '3.727 km', '37.27 km', '3727000 km', '37270 km', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3727 m ÷ 1000 = 3.727 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2875 m to kilometres.', '28750 km', '28.75 km', '2875000 km', '2.875 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '2875 m ÷ 1000 = 2.875 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3821 m to kilometres.', '38.21 km', '3821000 km', '3.821 km', '38210 km', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3821 m ÷ 1000 = 3.821 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4313 m to kilometres.', '43130 km', '43.13 km', '4313000 km', '4.313 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '4313 m ÷ 1000 = 4.313 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 918 m to kilometres.', '918000 km', '9.18 km', '9180 km', '0.918 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '918 m ÷ 1000 = 0.918 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3478 m to kilometres.', '34780 km', '34.78 km', '3.478 km', '3478000 km', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3478 m ÷ 1000 = 3.478 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4118 m to kilometres.', '4.118 km', '4118000 km', '41180 km', '41.18 km', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '4118 m ÷ 1000 = 4.118 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 874 m to kilometres.', '8.74 km', '874000 km', '8740 km', '0.874 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '874 m ÷ 1000 = 0.874 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4644 m to kilometres.', '4.644 km', '46.44 km', '4644000 km', '46440 km', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '4644 m ÷ 1000 = 4.644 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2660 m to kilometres.', '26.6 km', '26600 km', '2660000 km', '2.66 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '2660 m ÷ 1000 = 2.66 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3808 m to kilometres.', '3.808 km', '38.08 km', '3808000 km', '38080 km', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3808 m ÷ 1000 = 3.808 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2137 m to kilometres.', '21370 km', '2137000 km', '21.37 km', '2.137 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '2137 m ÷ 1000 = 2.137 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3040 m to kilometres.', '30400 km', '3040000 km', '30.4 km', '3.04 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3040 m ÷ 1000 = 3.04 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2360 m to kilometres.', '23.6 km', '2.36 km', '23600 km', '2360000 km', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '2360 m ÷ 1000 = 2.36 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3919 m to kilometres.', '3919000 km', '39.19 km', '39190 km', '3.919 km', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3919 m ÷ 1000 = 3.919 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4.8 km to metres.', '4800 m', '48 m', '480 m', '0.0048 m', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '4.8 km × 1000 = 4800 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1.5 km to metres.', '1500 m', '15 m', '0.0015 m', '150 m', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '1.5 km × 1000 = 1500 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.5 km to metres.', '0.0035 m', '3500 m', '35 m', '350 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3.5 km × 1000 = 3500 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.5 km to metres.', '3500 m', '350 m', '35 m', '0.0035 m', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3.5 km × 1000 = 3500 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 0.5 km to metres.', '0.0005 m', '500 m', '50 m', '5 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '0.5 km × 1000 = 500 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.5 km to metres.', '250 m', '2500 m', '0.0025 m', '25 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '2.5 km × 1000 = 2500 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.5 km to metres.', '0.0035 m', '3500 m', '35 m', '350 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3.5 km × 1000 = 3500 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.2 km to metres.', '3200 m', '32 m', '0.0032 m', '320 m', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '3.2 km × 1000 = 3200 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4.8 km to metres.', '48 m', '0.0048 m', '4800 m', '480 m', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '4.8 km × 1000 = 4800 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.75 km to metres.', '27 m', '2750 m', '0.00275 m', '275 m', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '2.75 km × 1000 = 2750 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 52 mm to centimetres.', '5.2 cm', '520 cm', '52 cm', '0.52 cm', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '52 mm ÷ 10 = 5.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 40 mm to centimetres.', '0.4 cm', '40 cm', '4 cm', '400 cm', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '40 mm ÷ 10 = 4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 104 mm to centimetres.', '1040 cm', '1.04 cm', '104 cm', '10.4 cm', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '104 mm ÷ 10 = 10.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 41 mm to centimetres.', '0.41 cm', '410 cm', '4.1 cm', '41 cm', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '41 mm ÷ 10 = 4.1 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 200 mm to centimetres.', '20 cm', '200 cm', '2000 cm', '2.0 cm', 0,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '200 mm ÷ 10 = 20 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 137 mm to centimetres.', '1.37 cm', '1370 cm', '137 cm', '13.7 cm', 3,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '137 mm ÷ 10 = 13.7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 39 mm to centimetres.', '39 cm', '390 cm', '3.9 cm', '0.39 cm', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '39 mm ÷ 10 = 3.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 79 mm to centimetres.', '79 cm', '0.79 cm', '7.9 cm', '790 cm', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '79 mm ÷ 10 = 7.9 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 33 mm to centimetres.', '0.33 cm', '3.3 cm', '33 cm', '330 cm', 1,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '33 mm ÷ 10 = 3.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 163 mm to centimetres.', '1630 cm', '1.63 cm', '16.3 cm', '163 cm', 2,
'lc_ol_applied_measure', 1, 'foundation', 'lc_ol', '163 mm ÷ 10 = 16.3 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 595 g to kilograms.', '595000 kg', '595 kg', '5.95 kg', '0.595 kg', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '595 g ÷ 1000 = 0.595 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4797 g to kilograms.', '4797 kg', '4.797 kg', '4797000 kg', '47.97 kg', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '4797 g ÷ 1000 = 4.797 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1331 g to kilograms.', '1331000 kg', '1331 kg', '13.31 kg', '1.331 kg', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1331 g ÷ 1000 = 1.331 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3701 g to kilograms.', '3.701 kg', '37.01 kg', '3701000 kg', '3701 kg', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '3701 g ÷ 1000 = 3.701 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2605 g to kilograms.', '26.05 kg', '2.605 kg', '2605 kg', '2605000 kg', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2605 g ÷ 1000 = 2.605 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2520 g to kilograms.', '2.52 kg', '2520000 kg', '25.2 kg', '2520 kg', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2520 g ÷ 1000 = 2.52 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3433 g to kilograms.', '3433 kg', '3433000 kg', '3.433 kg', '34.33 kg', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '3433 g ÷ 1000 = 3.433 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1494 g to kilograms.', '1494 kg', '14.94 kg', '1494000 kg', '1.494 kg', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1494 g ÷ 1000 = 1.494 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1133 g to kilograms.', '11.33 kg', '1133 kg', '1.133 kg', '1133000 kg', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1133 g ÷ 1000 = 1.133 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2900 g to kilograms.', '2.9 kg', '29.0 kg', '2900000 kg', '2900 kg', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2900 g ÷ 1000 = 2.9 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1312 g to kilograms.', '1312000 kg', '13.12 kg', '1312 kg', '1.312 kg', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1312 g ÷ 1000 = 1.312 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1502 g to kilograms.', '1502 kg', '1502000 kg', '1.502 kg', '15.02 kg', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1502 g ÷ 1000 = 1.502 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1118 g to kilograms.', '1118000 kg', '1.118 kg', '1118 kg', '11.18 kg', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1118 g ÷ 1000 = 1.118 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4711 g to kilograms.', '4711000 kg', '4.711 kg', '4711 kg', '47.11 kg', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '4711 g ÷ 1000 = 4.711 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3124 g to kilograms.', '3.124 kg', '31.24 kg', '3124000 kg', '3124 kg', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '3124 g ÷ 1000 = 3.124 kg', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.8 kg to grams.', '0.0028 g', '2 g', '280 g', '2800 g', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.8 kg × 1000 = 2800 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.8 kg to grams.', '280 g', '2 g', '2800 g', '0.0028 g', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.8 kg × 1000 = 2800 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.25 kg to grams.', '0.00325 g', '325 g', '3 g', '3250 g', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '3.25 kg × 1000 = 3250 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4.2 kg to grams.', '0.004200000000000001 g', '420 g', '4 g', '4200 g', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '4.2 kg × 1000 = 4200 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.8 kg to grams.', '0.0028 g', '2800 g', '280 g', '2 g', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.8 kg × 1000 = 2800 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1.5 kg to grams.', '1 g', '1500 g', '150 g', '0.0015 g', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1.5 kg × 1000 = 1500 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 0.75 kg to grams.', '75 g', '0 g', '750 g', '0.00075 g', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '0.75 kg × 1000 = 750 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 0.75 kg to grams.', '0 g', '0.00075 g', '750 g', '75 g', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '0.75 kg × 1000 = 750 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.25 kg to grams.', '0.00325 g', '3250 g', '325 g', '3 g', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '3.25 kg × 1000 = 3250 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4.2 kg to grams.', '4200 g', '420 g', '0.004200000000000001 g', '4 g', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '4.2 kg × 1000 = 4200 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1057 ml to litres.', '1.057 L', '1057000 L', '10.57 L', '1057 L', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1057 ml ÷ 1000 = 1.057 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1821 ml to litres.', '1.821 L', '1821000 L', '1821 L', '18.21 L', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1821 ml ÷ 1000 = 1.821 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 707 ml to litres.', '707 L', '7.07 L', '707000 L', '0.707 L', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '707 ml ÷ 1000 = 0.707 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 562 ml to litres.', '562000 L', '562 L', '5.62 L', '0.562 L', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '562 ml ÷ 1000 = 0.562 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 695 ml to litres.', '6.95 L', '0.695 L', '695000 L', '695 L', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '695 ml ÷ 1000 = 0.695 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 576 ml to litres.', '0.576 L', '576000 L', '5.76 L', '576 L', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '576 ml ÷ 1000 = 0.576 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 372 ml to litres.', '372000 L', '0.372 L', '372 L', '3.72 L', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '372 ml ÷ 1000 = 0.372 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1790 ml to litres.', '17.9 L', '1790000 L', '1790 L', '1.79 L', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1790 ml ÷ 1000 = 1.79 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 595 ml to litres.', '595 L', '5.95 L', '595000 L', '0.595 L', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '595 ml ÷ 1000 = 0.595 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1682 ml to litres.', '16.82 L', '1682 L', '1.682 L', '1682000 L', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1682 ml ÷ 1000 = 1.682 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1649 ml to litres.', '1.649 L', '1649 L', '16.49 L', '1649000 L', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1649 ml ÷ 1000 = 1.649 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1666 ml to litres.', '1.666 L', '1666 L', '1666000 L', '16.66 L', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1666 ml ÷ 1000 = 1.666 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 699 ml to litres.', '0.699 L', '6.99 L', '699 L', '699000 L', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '699 ml ÷ 1000 = 0.699 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 648 ml to litres.', '6.48 L', '648 L', '648000 L', '0.648 L', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '648 ml ÷ 1000 = 0.648 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 500 ml to litres.', '0.5 L', '500 L', '5.0 L', '500000 L', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '500 ml ÷ 1000 = 0.5 L', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1.5 litres to millilitres.', '150 ml', '0.0015 ml', '1500 ml', '1 ml', 2,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1.5 L × 1000 = 1500 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.2 litres to millilitres.', '0.0032 ml', '3 ml', '320 ml', '3200 ml', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '3.2 L × 1000 = 3200 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3.2 litres to millilitres.', '0.0032 ml', '3 ml', '320 ml', '3200 ml', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '3.2 L × 1000 = 3200 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.25 litres to millilitres.', '2250 ml', '225 ml', '2 ml', '0.00225 ml', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.25 L × 1000 = 2250 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.5 litres to millilitres.', '2 ml', '2500 ml', '0.0025 ml', '250 ml', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.5 L × 1000 = 2500 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 0.75 litres to millilitres.', '750 ml', '0 ml', '0.00075 ml', '75 ml', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '0.75 L × 1000 = 750 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.5 litres to millilitres.', '2500 ml', '250 ml', '0.0025 ml', '2 ml', 0,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.5 L × 1000 = 2500 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1.5 litres to millilitres.', '150 ml', '1500 ml', '1 ml', '0.0015 ml', 1,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '1.5 L × 1000 = 1500 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.25 litres to millilitres.', '0.00225 ml', '225 ml', '2 ml', '2250 ml', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.25 L × 1000 = 2250 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2.25 litres to millilitres.', '2 ml', '0.00225 ml', '225 ml', '2250 ml', 3,
'lc_ol_applied_measure', 2, 'foundation', 'lc_ol', '2.25 L × 1000 = 2250 ml', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 112 minutes to hours and minutes.', '1 hr 52 min', '1 hr 12 min', '2 hr 52 min', '1 hr 112 min', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '112 ÷ 60 = 1 remainder 52, so 1 hr 52 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 82 minutes to hours and minutes.', '1 hr 82 min', '2 hr 22 min', '0 hr 82 min', '1 hr 22 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '82 ÷ 60 = 1 remainder 22, so 1 hr 22 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 188 minutes to hours and minutes.', '1 hr 88 min', '4 hr 8 min', '3 hr 188 min', '3 hr 8 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '188 ÷ 60 = 3 remainder 8, so 3 hr 8 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 139 minutes to hours and minutes.', '1 hr 39 min', '3 hr 19 min', '2 hr 19 min', '2 hr 139 min', 2,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '139 ÷ 60 = 2 remainder 19, so 2 hr 19 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 152 minutes to hours and minutes.', '1 hr 52 min', '2 hr 152 min', '3 hr 32 min', '2 hr 32 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '152 ÷ 60 = 2 remainder 32, so 2 hr 32 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 176 minutes to hours and minutes.', '2 hr 56 min', '3 hr 56 min', '1 hr 76 min', '2 hr 176 min', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '176 ÷ 60 = 2 remainder 56, so 2 hr 56 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 175 minutes to hours and minutes.', '3 hr 55 min', '2 hr 55 min', '2 hr 175 min', '1 hr 75 min', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '175 ÷ 60 = 2 remainder 55, so 2 hr 55 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 110 minutes to hours and minutes.', '1 hr 10 min', '1 hr 50 min', '2 hr 50 min', '1 hr 110 min', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '110 ÷ 60 = 1 remainder 50, so 1 hr 50 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 119 minutes to hours and minutes.', '1 hr 119 min', '1 hr 19 min', '1 hr 59 min', '2 hr 59 min', 2,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '119 ÷ 60 = 1 remainder 59, so 1 hr 59 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 175 minutes to hours and minutes.', '3 hr 55 min', '2 hr 175 min', '1 hr 75 min', '2 hr 55 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '175 ÷ 60 = 2 remainder 55, so 2 hr 55 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 77 minutes to hours and minutes.', '1 hr 77 min', '1 hr 17 min', '2 hr 17 min', '0 hr 77 min', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '77 ÷ 60 = 1 remainder 17, so 1 hr 17 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 174 minutes to hours and minutes.', '1 hr 74 min', '3 hr 54 min', '2 hr 174 min', '2 hr 54 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '174 ÷ 60 = 2 remainder 54, so 2 hr 54 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 112 minutes to hours and minutes.', '1 hr 112 min', '1 hr 52 min', '2 hr 52 min', '1 hr 12 min', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '112 ÷ 60 = 1 remainder 52, so 1 hr 52 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 104 minutes to hours and minutes.', '2 hr 44 min', '1 hr 104 min', '1 hr 4 min', '1 hr 44 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '104 ÷ 60 = 1 remainder 44, so 1 hr 44 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 130 minutes to hours and minutes.', '3 hr 10 min', '2 hr 10 min', '2 hr 130 min', '1 hr 30 min', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '130 ÷ 60 = 2 remainder 10, so 2 hr 10 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 83 minutes to hours and minutes.', '2 hr 23 min', '1 hr 83 min', '0 hr 83 min', '1 hr 23 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '83 ÷ 60 = 1 remainder 23, so 1 hr 23 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 129 minutes to hours and minutes.', '3 hr 9 min', '2 hr 129 min', '1 hr 29 min', '2 hr 9 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '129 ÷ 60 = 2 remainder 9, so 2 hr 9 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 171 minutes to hours and minutes.', '2 hr 171 min', '2 hr 51 min', '1 hr 71 min', '3 hr 51 min', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '171 ÷ 60 = 2 remainder 51, so 2 hr 51 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 99 minutes to hours and minutes.', '2 hr 39 min', '1 hr 99 min', '0 hr 99 min', '1 hr 39 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '99 ÷ 60 = 1 remainder 39, so 1 hr 39 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 192 minutes to hours and minutes.', '3 hr 192 min', '4 hr 12 min', '1 hr 92 min', '3 hr 12 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '192 ÷ 60 = 3 remainder 12, so 3 hr 12 min', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 14:30 and ends at 18:00. How long is the meeting?', '4 hr', '3 hr 30 min', '3 hr 45 min', '4 hr 30 min', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 14:30 to 18:00 = 3 hours and 30 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 11:30 and ends at 13:30. How long is the meeting?', '2 hr', 'Cannot determine', '3 hr 0 min', '2 hr 15 min', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 11:30 to 13:30 = 2 hours and 0 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 13:30 and ends at 18:00. How long is the meeting?', '5 hr 30 min', '4 hr 45 min', '5 hr', '4 hr 30 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 13:30 to 18:00 = 4 hours and 30 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 14:15 and ends at 15:15. How long is the meeting?', '1 hr 15 min', '2 hr 0 min', '1 hr', 'Cannot determine', 2,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 14:15 to 15:15 = 1 hours and 0 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 09:45 and ends at 11:30. How long is the meeting?', '1 hr 45 min', 'Cannot determine', '2 hr 45 min', '2 hr', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 09:45 to 11:30 = 1 hours and 45 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 11:30 and ends at 15:45. How long is the meeting?', '4 hr 30 min', '4 hr', '5 hr 15 min', '4 hr 15 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 11:30 to 15:45 = 4 hours and 15 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 11:30 and ends at 15:00. How long is the meeting?', '3 hr 45 min', '4 hr 30 min', '3 hr 30 min', '4 hr', 2,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 11:30 to 15:00 = 3 hours and 30 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 09:45 and ends at 13:15. How long is the meeting?', '4 hr 30 min', '3 hr 45 min', '4 hr', '3 hr 30 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 09:45 to 13:15 = 3 hours and 30 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 11:15 and ends at 15:30. How long is the meeting?', '4 hr 15 min', '5 hr 15 min', '4 hr', '4 hr 30 min', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 11:15 to 15:30 = 4 hours and 15 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 14:00 and ends at 17:15. How long is the meeting?', '4 hr 15 min', '3 hr 15 min', '3 hr 30 min', '3 hr', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 14:00 to 17:15 = 3 hours and 15 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 13:30 and ends at 15:45. How long is the meeting?', '2 hr 15 min', '2 hr 30 min', '2 hr', '3 hr 15 min', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 13:30 to 15:45 = 2 hours and 15 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 14:00 and ends at 17:30. How long is the meeting?', '3 hr 45 min', '3 hr 30 min', '4 hr 30 min', '3 hr', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 14:00 to 17:30 = 3 hours and 30 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 14:45 and ends at 15:45. How long is the meeting?', '1 hr', '2 hr 0 min', '1 hr 15 min', 'Cannot determine', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 14:45 to 15:45 = 1 hours and 0 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 13:15 and ends at 17:30. How long is the meeting?', '4 hr 30 min', '4 hr', '5 hr 15 min', '4 hr 15 min', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 13:15 to 17:30 = 4 hours and 15 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A meeting starts at 08:15 and ends at 11:45. How long is the meeting?', '3 hr 30 min', '3 hr', '3 hr 45 min', '4 hr 30 min', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', 'From 08:15 to 11:45 = 3 hours and 30 minutes', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 13:00 to 12-hour format.', '13:00 am', '1:00 pm', '1:00 am', '3:00 pm', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '13:00 = 13 - 12 = 1 pm, so 1:00 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 21:45 to 12-hour format.', '9:45 am', '21:45 am', '11:45 pm', '9:45 pm', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '21:45 = 21 - 12 = 9 pm, so 9:45 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 13:15 to 12-hour format.', '13:15 am', '1:15 am', '1:15 pm', '3:15 pm', 2,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '13:15 = 13 - 12 = 1 pm, so 1:15 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 19:00 to 12-hour format.', '19:00 am', '7:00 pm', '7:00 am', '9:00 pm', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '19:00 = 19 - 12 = 7 pm, so 7:00 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 22:15 to 12-hour format.', '10:15 am', '12:15 pm', '22:15 am', '10:15 pm', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '22:15 = 22 - 12 = 10 pm, so 10:15 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 17:00 to 12-hour format.', '5:00 am', '5:00 pm', '7:00 pm', '17:00 am', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '17:00 = 17 - 12 = 5 pm, so 5:00 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 18:15 to 12-hour format.', '8:15 pm', '6:15 am', '18:15 am', '6:15 pm', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '18:15 = 18 - 12 = 6 pm, so 6:15 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 17:00 to 12-hour format.', '17:00 am', '5:00 pm', '7:00 pm', '5:00 am', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '17:00 = 17 - 12 = 5 pm, so 5:00 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 18:15 to 12-hour format.', '8:15 pm', '6:15 pm', '18:15 am', '6:15 am', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '18:15 = 18 - 12 = 6 pm, so 6:15 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 14:30 to 12-hour format.', '4:30 pm', '2:30 am', '14:30 am', '2:30 pm', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '14:30 = 14 - 12 = 2 pm, so 2:30 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 19:15 to 12-hour format.', '9:15 pm', '7:15 am', '7:15 pm', '19:15 am', 2,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '19:15 = 19 - 12 = 7 pm, so 7:15 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 19:45 to 12-hour format.', '7:45 am', '9:45 pm', '7:45 pm', '19:45 am', 2,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '19:45 = 19 - 12 = 7 pm, so 7:45 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 15:00 to 12-hour format.', '3:00 pm', '5:00 pm', '3:00 am', '15:00 am', 0,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '15:00 = 15 - 12 = 3 pm, so 3:00 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 23:30 to 12-hour format.', '13:30 pm', '11:30 pm', '23:30 am', '11:30 am', 1,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '23:30 = 23 - 12 = 11 pm, so 11:30 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 20:30 to 12-hour format.', '8:30 am', '10:30 pm', '20:30 am', '8:30 pm', 3,
'lc_ol_applied_measure', 3, 'foundation', 'lc_ol', '20:30 = 20 - 12 = 8 pm, so 8:30 pm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 80 km/h for 1 hours. How far does it travel?', 'Cannot determine', '40 km', '160 km', '80 km', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 80 × 1 = 80 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 60 km/h for 3 hours. How far does it travel?', '240 km', '180 km', '60 km', '90 km', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 60 × 3 = 180 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 120 km/h for 3 hours. How far does it travel?', '120 km', '180 km', '360 km', '480 km', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 120 × 3 = 360 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 80 km/h for 4 hours. How far does it travel?', '80 km', '400 km', '320 km', '160 km', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 80 × 4 = 320 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 100 km/h for 3 hours. How far does it travel?', '400 km', '100 km', '150 km', '300 km', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 100 × 3 = 300 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 50 km/h for 2 hours. How far does it travel?', 'Cannot determine', '50 km', '150 km', '100 km', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 50 × 2 = 100 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 50 km/h for 2 hours. How far does it travel?', 'Cannot determine', '150 km', '100 km', '50 km', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 50 × 2 = 100 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 80 km/h for 4 hours. How far does it travel?', '80 km', '320 km', '400 km', '160 km', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 80 × 4 = 320 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 120 km/h for 1.5 hours. How far does it travel?', '300 km', '90 km', '120 km', '180 km', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 120 × 1.5 = 180.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 80 km/h for 1.5 hours. How far does it travel?', '200 km', '120 km', '60 km', '80 km', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 80 × 1.5 = 120.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 50 km/h for 4 hours. How far does it travel?', '50 km', '250 km', '200 km', '100 km', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 50 × 4 = 200 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 60 km/h for 2.5 hours. How far does it travel?', '75 km', '210 km', '150 km', '60 km', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 60 × 2.5 = 150.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 120 km/h for 3 hours. How far does it travel?', '360 km', '120 km', '180 km', '480 km', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 120 × 3 = 360 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 120 km/h for 2 hours. How far does it travel?', '240 km', '360 km', 'Cannot determine', '120 km', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 120 × 2 = 240 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 100 km/h for 2.5 hours. How far does it travel?', '250 km', '350 km', '125 km', '100 km', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 100 × 2.5 = 250.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 60 km/h for 1 hours. How far does it travel?', 'Cannot determine', '30 km', '120 km', '60 km', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 60 × 1 = 60 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 100 km/h for 2 hours. How far does it travel?', 'Cannot determine', '300 km', '200 km', '100 km', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 100 × 2 = 200 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 60 km/h for 1.5 hours. How far does it travel?', '45 km', '90 km', '150 km', '60 km', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 60 × 1.5 = 90.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 120 km/h for 2 hours. How far does it travel?', '240 km', '120 km', 'Cannot determine', '360 km', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 120 × 2 = 240 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels at 50 km/h for 4 hours. How far does it travel?', '200 km', '250 km', '50 km', '100 km', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Distance = Speed × Time = 50 × 4 = 200 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km at 50 km/h. How long does the journey take?', '1.5 hours', '3 hours', '4.0 hours', '0.3333333333333333 hours', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 150 ÷ 50 = 3.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 300 km at 80 km/h. How long does the journey take?', '3.0 hours', '0.26666666666666666 hours', '3.75 hours', '4.75 hours', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 300 ÷ 80 = 3.75 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 200 km at 80 km/h. How long does the journey take?', '0.4 hours', '3.5 hours', '2.0 hours', '2.5 hours', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 200 ÷ 80 = 2.5 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 200 km at 40 km/h. How long does the journey take?', '5 hours', '2.0 hours', '6.0 hours', '0.2 hours', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 200 ÷ 40 = 5.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 100 km at 80 km/h. How long does the journey take?', '1.0 hours', '1.25 hours', '0.8 hours', '2.25 hours', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 100 ÷ 80 = 1.25 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 100 km at 100 km/h. How long does the journey take?', '2.0 hours', 'Cannot determine', '1 hours', '1.0 hours', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 100 ÷ 100 = 1.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km at 100 km/h. How long does the journey take?', 'Cannot determine', '1.5 hours', '2.5 hours', '0.6666666666666666 hours', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 150 ÷ 100 = 1.5 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 240 km at 80 km/h. How long does the journey take?', '2.4 hours', '4.0 hours', '3 hours', '0.3333333333333333 hours', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 240 ÷ 80 = 3.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 300 km at 80 km/h. How long does the journey take?', '0.26666666666666666 hours', '4.75 hours', '3.75 hours', '3.0 hours', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 300 ÷ 80 = 3.75 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 300 km at 60 km/h. How long does the journey take?', '3.0 hours', '5 hours', '0.2 hours', '6.0 hours', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 300 ÷ 60 = 5.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 100 km at 80 km/h. How long does the journey take?', '1.0 hours', '0.8 hours', '1.25 hours', '2.25 hours', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 100 ÷ 80 = 1.25 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 240 km at 40 km/h. How long does the journey take?', '0.16666666666666666 hours', '7.0 hours', '2.4 hours', '6 hours', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 240 ÷ 40 = 6.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km at 60 km/h. How long does the journey take?', '1.5 hours', '3.5 hours', '2.5 hours', '0.4 hours', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 150 ÷ 60 = 2.5 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km at 80 km/h. How long does the journey take?', '1.875 hours', '1.5 hours', '2.875 hours', '0.5333333333333333 hours', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 150 ÷ 80 = 1.875 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 100 km at 100 km/h. How long does the journey take?', '2.0 hours', 'Cannot determine', '1 hours', '1.0 hours', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Time = Distance ÷ Speed = 100 ÷ 100 = 1.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 180 km in 2.5 hours. What is its average speed?', '92 km/h', '180 km/h', '72 km/h', '36 km/h', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 180 ÷ 2.5 = 72.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 200 km in 2.5 hours. What is its average speed?', '200 km/h', '100 km/h', '80 km/h', '40 km/h', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 200 ÷ 2.5 = 80.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 240 km in 4 hours. What is its average speed?', '240 km/h', '60 km/h', '80 km/h', '30 km/h', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 240 ÷ 4 = 60.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km in 4 hours. What is its average speed?', '18 km/h', '57 km/h', '37.5 km/h', '150 km/h', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 150 ÷ 4 = 37.5 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 300 km in 2 hours. What is its average speed?', '170 km/h', '150 km/h', '300 km/h', '75 km/h', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 300 ÷ 2 = 150.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 200 km in 4 hours. What is its average speed?', '25 km/h', '50 km/h', '200 km/h', '70 km/h', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 200 ÷ 4 = 50.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 120 km in 4 hours. What is its average speed?', '15 km/h', '30 km/h', '120 km/h', '50 km/h', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 120 ÷ 4 = 30.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 240 km in 2 hours. What is its average speed?', '60 km/h', '120 km/h', '240 km/h', '140 km/h', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 240 ÷ 2 = 120.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 180 km in 2 hours. What is its average speed?', '180 km/h', '90 km/h', '45 km/h', '110 km/h', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 180 ÷ 2 = 90.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 200 km in 2 hours. What is its average speed?', '100 km/h', '200 km/h', '120 km/h', '50 km/h', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 200 ÷ 2 = 100.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km in 4 hours. What is its average speed?', '57 km/h', '37.5 km/h', '150 km/h', '18 km/h', 1,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 150 ÷ 4 = 37.5 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km in 3 hours. What is its average speed?', '25 km/h', '70 km/h', '150 km/h', '50 km/h', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 150 ÷ 3 = 50.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 150 km in 2 hours. What is its average speed?', '75 km/h', '37 km/h', '150 km/h', '95 km/h', 0,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 150 ÷ 2 = 75.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 120 km in 3 hours. What is its average speed?', '120 km/h', '20 km/h', '60 km/h', '40 km/h', 3,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 120 ÷ 3 = 40.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 300 km in 2 hours. What is its average speed?', '75 km/h', '170 km/h', '150 km/h', '300 km/h', 2,
'lc_ol_applied_measure', 4, 'developing', 'lc_ol', 'Speed = Distance ÷ Time = 300 ÷ 2 = 150.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 80 km/h travels for 1 hours 30 minutes. Find the distance.', '2480 km', '120.0 km', '140 km', '80 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 30/60 = 1.5 hours. Distance = 80 × 1.5 = 120.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 100 km/h travels for 1 hours 30 minutes. Find the distance.', '3100 km', '100 km', '150.0 km', '170 km', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 30/60 = 1.5 hours. Distance = 100 × 1.5 = 150.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 90 km/h travels for 3 hours 45 minutes. Find the distance.', '270 km', '4320 km', '337.5 km', '358 km', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 3 + 45/60 = 3.75 hours. Distance = 90 × 3.75 = 337.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 90 km/h travels for 1 hours 15 minutes. Find the distance.', '132 km', '1440 km', '112.5 km', '90 km', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 15/60 = 1.25 hours. Distance = 90 × 1.25 = 112.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 1 hours 45 minutes. Find the distance.', '60 km', '105.0 km', '125 km', '2760 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 45/60 = 1.75 hours. Distance = 60 × 1.75 = 105.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 100 km/h travels for 1 hours 15 minutes. Find the distance.', '125.0 km', '100 km', '145 km', '1600 km', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 15/60 = 1.25 hours. Distance = 100 × 1.25 = 125.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 2 hours 45 minutes. Find the distance.', '2820 km', '165.0 km', '185 km', '120 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 2 + 45/60 = 2.75 hours. Distance = 60 × 2.75 = 165.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 120 km/h travels for 1 hours 15 minutes. Find the distance.', '120 km', '1920 km', '170 km', '150.0 km', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 15/60 = 1.25 hours. Distance = 120 × 1.25 = 150.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 2 hours 45 minutes. Find the distance.', '165.0 km', '120 km', '185 km', '2820 km', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 2 + 45/60 = 2.75 hours. Distance = 60 × 2.75 = 165.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 2 hours 15 minutes. Find the distance.', '120 km', '135.0 km', '1020 km', '155 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 2 + 15/60 = 2.25 hours. Distance = 60 × 2.25 = 135.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 3 hours 15 minutes. Find the distance.', '1080 km', '195.0 km', '215 km', '180 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 3 + 15/60 = 3.25 hours. Distance = 60 × 3.25 = 195.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 80 km/h travels for 2 hours 45 minutes. Find the distance.', '240 km', '220.0 km', '160 km', '3760 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 2 + 45/60 = 2.75 hours. Distance = 80 × 2.75 = 220.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 100 km/h travels for 1 hours 15 minutes. Find the distance.', '145 km', '1600 km', '100 km', '125.0 km', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 15/60 = 1.25 hours. Distance = 100 × 1.25 = 125.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 2 hours 15 minutes. Find the distance.', '120 km', '155 km', '135.0 km', '1020 km', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 2 + 15/60 = 2.25 hours. Distance = 60 × 2.25 = 135.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 3 hours 45 minutes. Find the distance.', '180 km', '225.0 km', '245 km', '2880 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 3 + 45/60 = 3.75 hours. Distance = 60 × 3.75 = 225.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 60 km/h travels for 2 hours 15 minutes. Find the distance.', '1020 km', '120 km', '155 km', '135.0 km', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 2 + 15/60 = 2.25 hours. Distance = 60 × 2.25 = 135.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 120 km/h travels for 3 hours 45 minutes. Find the distance.', '360 km', '450.0 km', '470 km', '5760 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 3 + 45/60 = 3.75 hours. Distance = 120 × 3.75 = 450.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 100 km/h travels for 1 hours 15 minutes. Find the distance.', '100 km', '1600 km', '125.0 km', '145 km', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 1 + 15/60 = 1.25 hours. Distance = 100 × 1.25 = 125.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 120 km/h travels for 2 hours 30 minutes. Find the distance.', '3840 km', '300.0 km', '320 km', '240 km', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 2 + 30/60 = 2.5 hours. Distance = 120 × 2.5 = 300.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car at 120 km/h travels for 3 hours 45 minutes. Find the distance.', '470 km', '5760 km', '360 km', '450.0 km', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 3 + 45/60 = 3.75 hours. Distance = 120 × 3.75 = 450.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 71 km in 2 hr, then 108 km in 1 hr. What is the average speed for the whole journey?', '35.5 km/h', '71.75 km/h', '70 km/h', '59.7 km/h', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 179/3 = 59.7 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 68 km in 2 hr, then 63 km in 2 hr. What is the average speed for the whole journey?', '43 km/h', '32.75 km/h', '34.0 km/h', '32.8 km/h', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 131/4 = 32.8 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 80 km in 1 hr, then 101 km in 1 hr. What is the average speed for the whole journey?', '90.5 km/h', 'Cannot determine', '80.0 km/h', '100 km/h', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 181/2 = 90.5 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 70 km in 1 hr, then 104 km in 1 hr. What is the average speed for the whole journey?', 'Cannot determine', '97 km/h', '70.0 km/h', '87.0 km/h', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 174/2 = 87.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 81 km in 2 hr, then 86 km in 2 hr. What is the average speed for the whole journey?', '41.8 km/h', '40.5 km/h', '52 km/h', '41.75 km/h', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 167/4 = 41.8 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 97 km in 2 hr, then 81 km in 1 hr. What is the average speed for the whole journey?', '64.75 km/h', '48.5 km/h', '69 km/h', '59.3 km/h', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 178/3 = 59.3 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 82 km in 1 hr, then 80 km in 1 hr. What is the average speed for the whole journey?', '81.0 km/h', 'Cannot determine', '91 km/h', '82.0 km/h', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 162/2 = 81.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 60 km in 2 hr, then 63 km in 2 hr. What is the average speed for the whole journey?', '30.0 km/h', '30.75 km/h', '30.8 km/h', '41 km/h', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 123/4 = 30.8 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 114 km in 1 hr, then 107 km in 2 hr. What is the average speed for the whole journey?', '83.75 km/h', '114.0 km/h', '73.7 km/h', '84 km/h', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 221/3 = 73.7 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 98 km in 1 hr, then 88 km in 1 hr. What is the average speed for the whole journey?', '93.0 km/h', 'Cannot determine', '103 km/h', '98.0 km/h', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 186/2 = 93.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 80 km in 1 hr, then 112 km in 2 hr. What is the average speed for the whole journey?', '80.0 km/h', '74 km/h', '64.0 km/h', '68.0 km/h', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 192/3 = 64.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 91 km in 1 hr, then 98 km in 1 hr. What is the average speed for the whole journey?', '94.5 km/h', 'Cannot determine', '104 km/h', '91.0 km/h', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 189/2 = 94.5 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 66 km in 2 hr, then 74 km in 1 hr. What is the average speed for the whole journey?', '53.5 km/h', '57 km/h', '33.0 km/h', '46.7 km/h', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 140/3 = 46.7 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 67 km in 1 hr, then 81 km in 2 hr. What is the average speed for the whole journey?', '67.0 km/h', '49.3 km/h', '59 km/h', '53.75 km/h', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 148/3 = 49.3 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car travels 87 km in 2 hr, then 111 km in 1 hr. What is the average speed for the whole journey?', '43.5 km/h', '66.0 km/h', '76 km/h', '77.25 km/h', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Average speed = Total distance / Total time = 198/3 = 66.0 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 11:30, travelling 120 km at 60 km/h. What time do you arrive?', '13:30', '14:30', 'Cannot determine', '13:45', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 120/60 = 2.0 hrs = 120 min. Start 11:30 + 120 min = 13:30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 14:30, travelling 180 km at 60 km/h. What time do you arrive?', 'Cannot determine', '18:30', '17:30', '17:45', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 180/60 = 3.0 hrs = 180 min. Start 14:30 + 180 min = 17:30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 09:00, travelling 120 km at 100 km/h. What time do you arrive?', '10:27', '10:12', '11:12', '10:00', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 120/100 = 1.2 hrs = 72 min. Start 09:00 + 72 min = 10:12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 09:15, travelling 150 km at 60 km/h. What time do you arrive?', '11:15', '11:45', '12:45', '11:00', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 150/60 = 2.5 hrs = 150 min. Start 09:15 + 150 min = 11:45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 11:15, travelling 120 km at 80 km/h. What time do you arrive?', '12:45', '13:45', '12:15', '12:00', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 120/80 = 1.5 hrs = 90 min. Start 11:15 + 90 min = 12:45', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 14:30, travelling 120 km at 60 km/h. What time do you arrive?', '17:30', '16:30', 'Cannot determine', '16:45', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 120/60 = 2.0 hrs = 120 min. Start 14:30 + 120 min = 16:30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 12:30, travelling 200 km at 60 km/h. What time do you arrive?', '15:30', '15:50', '16:50', '15:05', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 200/60 = 3.3333333333333335 hrs = 200 min. Start 12:30 + 200 min = 15:50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 08:00, travelling 120 km at 100 km/h. What time do you arrive?', '09:27', '09:00', '10:12', '09:12', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 120/100 = 1.2 hrs = 72 min. Start 08:00 + 72 min = 09:12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 09:00, travelling 180 km at 100 km/h. What time do you arrive?', '10:00', '10:03', '11:48', '10:48', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 180/100 = 1.8 hrs = 108 min. Start 09:00 + 108 min = 10:48', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 08:00, travelling 200 km at 60 km/h. What time do you arrive?', '11:20', '11:35', '12:20', '11:00', 0,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 200/60 = 3.3333333333333335 hrs = 200 min. Start 08:00 + 200 min = 11:20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 14:00, travelling 150 km at 80 km/h. What time do you arrive?', '16:52', '15:00', '15:52', '15:07', 2,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 150/80 = 1.875 hrs = 112 min. Start 14:00 + 112 min = 15:52', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 14:15, travelling 200 km at 60 km/h. What time do you arrive?', '17:15', '17:50', '18:35', '17:35', 3,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 200/60 = 3.3333333333333335 hrs = 200 min. Start 14:15 + 200 min = 17:35', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 08:15, travelling 150 km at 80 km/h. What time do you arrive?', '10:22', '10:07', '09:15', '11:07', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 150/80 = 1.875 hrs = 112 min. Start 08:15 + 112 min = 10:07', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 11:30, travelling 200 km at 100 km/h. What time do you arrive?', '14:30', '13:30', '13:45', 'Cannot determine', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 200/100 = 2.0 hrs = 120 min. Start 11:30 + 120 min = 13:30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Leaving at 09:15, travelling 180 km at 100 km/h. What time do you arrive?', '10:15', '11:03', '12:03', '11:18', 1,
'lc_ol_applied_measure', 5, 'developing', 'lc_ol', 'Time = 180/100 = 1.8 hrs = 108 min. Start 09:15 + 108 min = 11:03', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:100. A line is 11 cm on the drawing. What is the actual length?', '11 m', '0.11 cm', '11.0 m', '110.0 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 11 × 100 = 1100 cm = 11.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:100. A line is 8 cm on the drawing. What is the actual length?', '0.08 cm', '8 m', '8.0 m', '80.0 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 8 × 100 = 800 cm = 8.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:500. A line is 15 cm on the drawing. What is the actual length?', '15 m', '75.0 m', '750.0 cm', '0.03 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 15 × 500 = 7500 cm = 75.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:500. A line is 7 cm on the drawing. What is the actual length?', '35.0 m', '7 m', '350.0 cm', '0.014 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 7 × 500 = 3500 cm = 35.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:50. A line is 11 cm on the drawing. What is the actual length?', '5.5 m', '11 m', '0.22 cm', '55.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 11 × 50 = 550 cm = 5.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 2 cm on the drawing. What is the actual length?', '2 m', '0.01 cm', '40.0 cm', '4.0 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 2 × 200 = 400 cm = 4.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 13 cm on the drawing. What is the actual length?', '260.0 cm', '13 m', '0.065 cm', '26.0 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 13 × 200 = 2600 cm = 26.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:50. A line is 2 cm on the drawing. What is the actual length?', '0.04 cm', '2 m', '10.0 cm', '1.0 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 2 × 50 = 100 cm = 1.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:50. A line is 9 cm on the drawing. What is the actual length?', '45.0 cm', '0.18 cm', '9 m', '4.5 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 9 × 50 = 450 cm = 4.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 15 cm on the drawing. What is the actual length?', '30.0 m', '0.075 cm', '15 m', '300.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 15 × 200 = 3000 cm = 30.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:100. A line is 9 cm on the drawing. What is the actual length?', '9 m', '90.0 cm', '0.09 cm', '9.0 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 9 × 100 = 900 cm = 9.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:500. A line is 2 cm on the drawing. What is the actual length?', '10.0 m', '100.0 cm', '2 m', '0.004 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 2 × 500 = 1000 cm = 10.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 13 cm on the drawing. What is the actual length?', '13 m', '0.065 cm', '260.0 cm', '26.0 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 13 × 200 = 2600 cm = 26.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:500. A line is 11 cm on the drawing. What is the actual length?', '11 m', '0.022 cm', '550.0 cm', '55.0 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 11 × 500 = 5500 cm = 55.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 15 cm on the drawing. What is the actual length?', '30.0 m', '15 m', '0.075 cm', '300.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 15 × 200 = 3000 cm = 30.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:500. A line is 8 cm on the drawing. What is the actual length?', '40.0 m', '400.0 cm', '8 m', '0.016 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 8 × 500 = 4000 cm = 40.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:50. A line is 13 cm on the drawing. What is the actual length?', '13 m', '65.0 cm', '0.26 cm', '6.5 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 13 × 50 = 650 cm = 6.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:100. A line is 2 cm on the drawing. What is the actual length?', '2.0 m', '0.02 cm', '2 m', '20.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 2 × 100 = 200 cm = 2.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 10 cm on the drawing. What is the actual length?', '20.0 m', '0.05 cm', '200.0 cm', '10 m', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 10 × 200 = 2000 cm = 20.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 5 cm on the drawing. What is the actual length?', '0.025 cm', '10.0 m', '5 m', '100.0 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 5 × 200 = 1000 cm = 10.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:50. A line is 4 cm on the drawing. What is the actual length?', '4 m', '0.08 cm', '20.0 cm', '2.0 m', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 4 × 50 = 200 cm = 2.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:50. A line is 4 cm on the drawing. What is the actual length?', '0.08 cm', '4 m', '2.0 m', '20.0 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 4 × 50 = 200 cm = 2.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:100. A line is 11 cm on the drawing. What is the actual length?', '11.0 m', '0.11 cm', '11 m', '110.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 11 × 100 = 1100 cm = 11.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:200. A line is 10 cm on the drawing. What is the actual length?', '20.0 m', '200.0 cm', '0.05 cm', '10 m', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 10 × 200 = 2000 cm = 20.0 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A drawing uses scale 1:50. A line is 9 cm on the drawing. What is the actual length?', '4.5 m', '45.0 cm', '0.18 cm', '9 m', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Actual = Drawing × Scale = 9 × 50 = 450 cm = 4.5 m', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 6 m?', '6.0 cm', '600 cm', '6 cm', '60.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 600 ÷ 100 = 6.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:200 is used. What length on the drawing represents 7 m?', '1400 cm', '35.0 cm', '3.5 cm', '7 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 700 ÷ 200 = 3.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 6 m?', '6 cm', '6.0 cm', '60.0 cm', '600 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 600 ÷ 100 = 6.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:50 is used. What length on the drawing represents 7 m?', '140.0 cm', '14.0 cm', '7 cm', '350 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 700 ÷ 50 = 14.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 3 m?', '30.0 cm', '300 cm', '3 cm', '3.0 cm', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 300 ÷ 100 = 3.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 2 m?', '200 cm', '20.0 cm', '2.0 cm', '2 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 200 ÷ 100 = 2.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:500 is used. What length on the drawing represents 10 m?', '10 cm', '2.0 cm', '5000 cm', '20.0 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 1000 ÷ 500 = 2.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:200 is used. What length on the drawing represents 7 m?', '35.0 cm', '7 cm', '3.5 cm', '1400 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 700 ÷ 200 = 3.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 8 m?', '800 cm', '8 cm', '8.0 cm', '80.0 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 800 ÷ 100 = 8.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:200 is used. What length on the drawing represents 2 m?', '2 cm', '1.0 cm', '10.0 cm', '400 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 200 ÷ 200 = 1.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:500 is used. What length on the drawing represents 7 m?', '7 cm', '14.0 cm', '3500 cm', '1.4 cm', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 700 ÷ 500 = 1.4 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:500 is used. What length on the drawing represents 5 m?', '10.0 cm', '1.0 cm', '5 cm', '2500 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 500 ÷ 500 = 1.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 2 m?', '2 cm', '2.0 cm', '20.0 cm', '200 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 200 ÷ 100 = 2.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:50 is used. What length on the drawing represents 7 m?', '140.0 cm', '350 cm', '7 cm', '14.0 cm', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 700 ÷ 50 = 14.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:500 is used. What length on the drawing represents 8 m?', '16.0 cm', '8 cm', '4000 cm', '1.6 cm', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 800 ÷ 500 = 1.6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:200 is used. What length on the drawing represents 4 m?', '2.0 cm', '4 cm', '800 cm', '20.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 400 ÷ 200 = 2.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:50 is used. What length on the drawing represents 9 m?', '180.0 cm', '18.0 cm', '450 cm', '9 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 900 ÷ 50 = 18.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 9 m?', '9.0 cm', '9 cm', '900 cm', '90.0 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 900 ÷ 100 = 9.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:50 is used. What length on the drawing represents 3 m?', '60.0 cm', '3 cm', '6.0 cm', '150 cm', 2,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 300 ÷ 50 = 6.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:50 is used. What length on the drawing represents 2 m?', '100 cm', '4.0 cm', '40.0 cm', '2 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 200 ÷ 50 = 4.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:50 is used. What length on the drawing represents 2 m?', '4.0 cm', '100 cm', '40.0 cm', '2 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 200 ÷ 50 = 4.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:100 is used. What length on the drawing represents 7 m?', '7.0 cm', '7 cm', '70.0 cm', '700 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 700 ÷ 100 = 7.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:500 is used. What length on the drawing represents 4 m?', '0.8 cm', '8.0 cm', '2000 cm', '4 cm', 0,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 400 ÷ 500 = 0.8 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:500 is used. What length on the drawing represents 5 m?', '2500 cm', '5 cm', '10.0 cm', '1.0 cm', 3,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 500 ÷ 500 = 1.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A scale of 1:500 is used. What length on the drawing represents 6 m?', '6 cm', '1.2 cm', '3000 cm', '12.0 cm', 1,
'lc_ol_applied_measure', 6, 'developing', 'lc_ol', 'Drawing = Actual ÷ Scale = 600 ÷ 500 = 1.2 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 9 cm apart on the map. What is the actual distance?', '2250.0 km', '22.5 km', '225.0 km', '9 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 9 × 250000 = 2250000 cm = 22.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:50000. Two towns are 2 cm apart on the map. What is the actual distance?', '10.0 km', '1.0 km', '100.0 km', '2 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 2 × 50000 = 100000 cm = 1.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:25000. Two towns are 6 cm apart on the map. What is the actual distance?', '15.0 km', '6 km', '1.5 km', '150.0 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 6 × 25000 = 150000 cm = 1.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 4 cm apart on the map. What is the actual distance?', '4 km', '10.0 km', '100.0 km', '1000.0 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 4 × 250000 = 1000000 cm = 10.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:100000. Two towns are 4 cm apart on the map. What is the actual distance?', '4.0 km', '4 km', '400.0 km', '40.0 km', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 4 × 100000 = 400000 cm = 4.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 5 cm apart on the map. What is the actual distance?', '5 km', '125.0 km', '1250.0 km', '12.5 km', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 5 × 250000 = 1250000 cm = 12.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 10 cm apart on the map. What is the actual distance?', '2500.0 km', '25.0 km', '10 km', '250.0 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 10 × 250000 = 2500000 cm = 25.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:50000. Two towns are 3 cm apart on the map. What is the actual distance?', '150.0 km', '1.5 km', '15.0 km', '3 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 3 × 50000 = 150000 cm = 1.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:50000. Two towns are 7 cm apart on the map. What is the actual distance?', '35.0 km', '7 km', '3.5 km', '350.0 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 7 × 50000 = 350000 cm = 3.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 5 cm apart on the map. What is the actual distance?', '12.5 km', '5 km', '125.0 km', '1250.0 km', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 5 × 250000 = 1250000 cm = 12.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 10 cm apart on the map. What is the actual distance?', '10 km', '250.0 km', '2500.0 km', '25.0 km', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 10 × 250000 = 2500000 cm = 25.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:25000. Two towns are 6 cm apart on the map. What is the actual distance?', '150.0 km', '1.5 km', '6 km', '15.0 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 6 × 25000 = 150000 cm = 1.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 4 cm apart on the map. What is the actual distance?', '10.0 km', '100.0 km', '4 km', '1000.0 km', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 4 × 250000 = 1000000 cm = 10.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:25000. Two towns are 9 cm apart on the map. What is the actual distance?', '225.0 km', '22.5 km', '2.25 km', '9 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 9 × 25000 = 225000 cm = 2.25 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:25000. Two towns are 7 cm apart on the map. What is the actual distance?', '175.0 km', '17.5 km', '1.75 km', '7 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 7 × 25000 = 175000 cm = 1.75 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:25000. Two towns are 2 cm apart on the map. What is the actual distance?', '2 km', '5.0 km', '0.5 km', '50.0 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 2 × 25000 = 50000 cm = 0.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:50000. Two towns are 9 cm apart on the map. What is the actual distance?', '9 km', '45.0 km', '450.0 km', '4.5 km', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 9 × 50000 = 450000 cm = 4.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:100000. Two towns are 8 cm apart on the map. What is the actual distance?', '8 km', '8.0 km', '80.0 km', '800.0 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 8 × 100000 = 800000 cm = 8.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 5 cm apart on the map. What is the actual distance?', '125.0 km', '5 km', '12.5 km', '1250.0 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 5 × 250000 = 1250000 cm = 12.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:25000. Two towns are 2 cm apart on the map. What is the actual distance?', '50.0 km', '2 km', '5.0 km', '0.5 km', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 2 × 25000 = 50000 cm = 0.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:50000. Two towns are 7 cm apart on the map. What is the actual distance?', '350.0 km', '3.5 km', '7 km', '35.0 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 7 × 50000 = 350000 cm = 3.5 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:25000. Two towns are 5 cm apart on the map. What is the actual distance?', '1.25 km', '12.5 km', '125.0 km', '5 km', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 5 × 25000 = 125000 cm = 1.25 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:50000. Two towns are 10 cm apart on the map. What is the actual distance?', '10 km', '500.0 km', '5.0 km', '50.0 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 10 × 50000 = 500000 cm = 5.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:100000. Two towns are 7 cm apart on the map. What is the actual distance?', '70.0 km', '7 km', '7.0 km', '700.0 km', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 7 × 100000 = 700000 cm = 7.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map has scale 1:250000. Two towns are 4 cm apart on the map. What is the actual distance?', '1000.0 km', '10.0 km', '100.0 km', '4 km', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Actual = 4 × 250000 = 1000000 cm = 10.0 km', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:100000. How far apart on the map are two points that are 7.5 km apart?', '75.0 cm', '7.5 cm', 'Cannot determine', 'Cannot determine', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 100000 = 7.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:100000. How far apart on the map are two points that are 2.5 km apart?', '2.5 cm', 'Cannot determine', 'Cannot determine', '25.0 cm', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 2.5 km = 250000.0 cm. 250000.0 ÷ 100000 = 2.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 7.5 km apart?', '7.5 cm', '15.0 cm', '3.75 cm', '150.0 cm', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 50000 = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 7.5 km apart?', '300.0 cm', '1.875 cm', '7.5 cm', '30.0 cm', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 25000 = 30.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 2.5 km apart?', '2.5 cm', '100.0 cm', '0.625 cm', '10.0 cm', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 2.5 km = 250000.0 cm. 250000.0 ÷ 25000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:100000. How far apart on the map are two points that are 10 km apart?', '100.0 cm', '10 cm', '10.0 cm', 'Cannot determine', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 10 km = 1000000 cm. 1000000 ÷ 100000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 12.5 km apart?', '12.5 cm', '6.25 cm', '250.0 cm', '25.0 cm', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 12.5 km = 1250000.0 cm. 1250000.0 ÷ 50000 = 25.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 5 km apart?', '2.5 cm', '5 cm', '10.0 cm', '100.0 cm', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 5 km = 500000 cm. 500000 ÷ 50000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 7.5 km apart?', '15.0 cm', '7.5 cm', '150.0 cm', '3.75 cm', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 50000 = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 7.5 km apart?', '300.0 cm', '30.0 cm', '1.875 cm', '7.5 cm', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 25000 = 30.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:100000. How far apart on the map are two points that are 7.5 km apart?', 'Cannot determine', '7.5 cm', '75.0 cm', 'Cannot determine', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 100000 = 7.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 7.5 km apart?', '7.5 cm', '300.0 cm', '1.875 cm', '30.0 cm', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 25000 = 30.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 12.5 km apart?', '25.0 cm', '12.5 cm', '250.0 cm', '6.25 cm', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 12.5 km = 1250000.0 cm. 1250000.0 ÷ 50000 = 25.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 2.5 km apart?', '100.0 cm', '2.5 cm', '10.0 cm', '0.625 cm', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 2.5 km = 250000.0 cm. 250000.0 ÷ 25000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:100000. How far apart on the map are two points that are 12.5 km apart?', '125.0 cm', 'Cannot determine', '12.5 cm', 'Cannot determine', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 12.5 km = 1250000.0 cm. 1250000.0 ÷ 100000 = 12.5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 2.5 km apart?', '0.625 cm', '10.0 cm', '100.0 cm', '2.5 cm', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 2.5 km = 250000.0 cm. 250000.0 ÷ 25000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 12.5 km apart?', '3.125 cm', '50.0 cm', '12.5 cm', '500.0 cm', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 12.5 km = 1250000.0 cm. 1250000.0 ÷ 25000 = 50.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 12.5 km apart?', '50.0 cm', '500.0 cm', '3.125 cm', '12.5 cm', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 12.5 km = 1250000.0 cm. 1250000.0 ÷ 25000 = 50.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 5 km apart?', '100.0 cm', '2.5 cm', '5 cm', '10.0 cm', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 5 km = 500000 cm. 500000 ÷ 50000 = 10.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 7.5 km apart?', '1.875 cm', '7.5 cm', '300.0 cm', '30.0 cm', 3,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 25000 = 30.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 10 km apart?', '10 cm', '2.5 cm', '40.0 cm', '400.0 cm', 2,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 10 km = 1000000 cm. 1000000 ÷ 25000 = 40.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 7.5 km apart?', '15.0 cm', '150.0 cm', '3.75 cm', '7.5 cm', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 7.5 km = 750000.0 cm. 750000.0 ÷ 50000 = 15.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 10 km apart?', '20.0 cm', '5.0 cm', '200.0 cm', '10 cm', 0,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 10 km = 1000000 cm. 1000000 ÷ 50000 = 20.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:50000. How far apart on the map are two points that are 10 km apart?', '5.0 cm', '20.0 cm', '10 cm', '200.0 cm', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 10 km = 1000000 cm. 1000000 ÷ 50000 = 20.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A map scale is 1:25000. How far apart on the map are two points that are 12.5 km apart?', '12.5 cm', '50.0 cm', '3.125 cm', '500.0 cm', 1,
'lc_ol_applied_measure', 7, 'proficient', 'lc_ol', 'Map distance = 12.5 km = 1250000.0 cm. 1250000.0 ÷ 25000 = 50.0 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 litres per 100 km. How much fuel for a 600 km journey?', '75.0 litres', '4800 litres', '58.0 litres', '48.0 litres', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 8 × 600/100 = 48.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 litres per 100 km. How much fuel for a 200 km journey?', '1200 litres', '22.0 litres', '12.0 litres', '33.333333333333336 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 6 × 200/100 = 12.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 10 litres per 100 km. How much fuel for a 300 km journey?', '40.0 litres', '3000 litres', '30.0 litres', 'Cannot determine', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 10 × 300/100 = 30.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 litres per 100 km. How much fuel for a 300 km journey?', '33.333333333333336 litres', '2700 litres', '27.0 litres', '37.0 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 9 × 300/100 = 27.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 10 litres per 100 km. How much fuel for a 400 km journey?', 'Cannot determine', '40.0 litres', '50.0 litres', '4000 litres', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 10 × 400/100 = 40.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 7 litres per 100 km. How much fuel for a 200 km journey?', '14.0 litres', '1400 litres', '24.0 litres', '28.571428571428573 litres', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 7 × 200/100 = 14.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 litres per 100 km. How much fuel for a 300 km journey?', '27.0 litres', '33.333333333333336 litres', '2700 litres', '37.0 litres', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 9 × 300/100 = 27.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 10 litres per 100 km. How much fuel for a 500 km journey?', '60.0 litres', '50.0 litres', '5000 litres', 'Cannot determine', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 10 × 500/100 = 50.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 litres per 100 km. How much fuel for a 200 km journey?', '22.22222222222222 litres', '1800 litres', '18.0 litres', '28.0 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 9 × 200/100 = 18.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 litres per 100 km. How much fuel for a 200 km journey?', '22.0 litres', '1200 litres', '12.0 litres', '33.333333333333336 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 6 × 200/100 = 12.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 10 litres per 100 km. How much fuel for a 300 km journey?', '30.0 litres', '40.0 litres', '3000 litres', 'Cannot determine', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 10 × 300/100 = 30.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 7 litres per 100 km. How much fuel for a 500 km journey?', '45.0 litres', '3500 litres', '35.0 litres', '71.42857142857143 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 7 × 500/100 = 35.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 litres per 100 km. How much fuel for a 300 km journey?', '28.0 litres', '50.0 litres', '18.0 litres', '1800 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 6 × 300/100 = 18.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 litres per 100 km. How much fuel for a 300 km journey?', '1800 litres', '28.0 litres', '50.0 litres', '18.0 litres', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 6 × 300/100 = 18.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 litres per 100 km. How much fuel for a 500 km journey?', '45.0 litres', '55.0 litres', '55.55555555555556 litres', '4500 litres', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 9 × 500/100 = 45.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 litres per 100 km. How much fuel for a 200 km journey?', '28.0 litres', '1800 litres', '18.0 litres', '22.22222222222222 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 9 × 200/100 = 18.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 5 litres per 100 km. How much fuel for a 500 km journey?', '25.0 litres', '100.0 litres', '35.0 litres', '2500 litres', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 5 × 500/100 = 25.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 10 litres per 100 km. How much fuel for a 400 km journey?', '40.0 litres', '50.0 litres', '4000 litres', 'Cannot determine', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 10 × 400/100 = 40.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 litres per 100 km. How much fuel for a 200 km journey?', '26.0 litres', '1600 litres', '16.0 litres', '25.0 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 8 × 200/100 = 16.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 5 litres per 100 km. How much fuel for a 500 km journey?', '35.0 litres', '2500 litres', '25.0 litres', '100.0 litres', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Fuel = 5 × 500/100 = 25.0 litres', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 18 items cost €20, what is the cost per item?', '€1.11', '€0.9', '€20', '€1.61', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €20 ÷ 18 = €1.11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 19 items cost €25, what is the cost per item?', '€1.82', '€1.32', '€0.76', '€25', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €25 ÷ 19 = €1.32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 9 items cost €30, what is the cost per item?', '€3.33', '€3.83', '€0.3', '€30', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €30 ÷ 9 = €3.33', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 18 items cost €25, what is the cost per item?', '€1.39', '€25', '€0.72', '€1.89', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €25 ÷ 18 = €1.39', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 12 items cost €30, what is the cost per item?', '€3.0', '€0.4', '€30', '€2.5', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €30 ÷ 12 = €2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 12 items cost €20, what is the cost per item?', '€1.67', '€20', '€2.17', '€0.6', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €20 ÷ 12 = €1.67', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 18 items cost €30, what is the cost per item?', '€0.6', '€1.67', '€30', '€2.17', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €30 ÷ 18 = €1.67', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 13 items cost €50, what is the cost per item?', '€4.35', '€50', '€3.85', '€0.26', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €50 ÷ 13 = €3.85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5 items cost €40, what is the cost per item?', '€8.5', '€8.0', '€40', '€0.125', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €40 ÷ 5 = €8.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 9 items cost €50, what is the cost per item?', '€50', '€5.56', '€0.18', '€6.06', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €50 ÷ 9 = €5.56', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 9 items cost €40, what is the cost per item?', '€40', '€4.44', '€4.94', '€0.225', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €40 ÷ 9 = €4.44', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 14 items cost €50, what is the cost per item?', '€50', '€3.57', '€0.28', '€4.07', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €50 ÷ 14 = €3.57', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 20 items cost €25, what is the cost per item?', '€0.8', '€25', '€1.75', '€1.25', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €25 ÷ 20 = €1.25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 19 items cost €50, what is the cost per item?', '€0.38', '€50', '€3.13', '€2.63', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €50 ÷ 19 = €2.63', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 15 items cost €30, what is the cost per item?', '€0.5', '€30', '€2.5', '€2.0', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Cost per item = €30 ÷ 15 = €2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 4 workers take 7 hours to complete a job, how long would 6 workers take?', '4.666666666666667 hours', '10.5 hours', '7 hours', '6.666666666666667 hours', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 4 × 7 = 28 worker-hours. Time for 6 = 28/6 = 4.666666666666667 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 8 workers take 10 hours to complete a job, how long would 4 workers take?', '22.0 hours', '20.0 hours', '10 hours', '5.0 hours', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 8 × 10 = 80 worker-hours. Time for 4 = 80/4 = 20.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 3 workers take 6 hours to complete a job, how long would 6 workers take?', '5.0 hours', '12.0 hours', '3.0 hours', '6 hours', 2,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 3 × 6 = 18 worker-hours. Time for 6 = 18/6 = 3.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 7 workers take 8 hours to complete a job, how long would 4 workers take?', '14.0 hours', '8 hours', '4.571428571428571 hours', '16.0 hours', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 7 × 8 = 56 worker-hours. Time for 4 = 56/4 = 14.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 6 workers take 8 hours to complete a job, how long would 6 workers take?', '8.0 hours', 'Cannot determine', '10.0 hours', '8 hours', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 6 × 8 = 48 worker-hours. Time for 6 = 48/6 = 8.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 6 workers take 8 hours to complete a job, how long would 6 workers take?', '8 hours', '8.0 hours', 'Cannot determine', '10.0 hours', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 6 × 8 = 48 worker-hours. Time for 6 = 48/6 = 8.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 3 workers take 8 hours to complete a job, how long would 2 workers take?', '5.333333333333333 hours', '8 hours', '14.0 hours', '12.0 hours', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 3 × 8 = 24 worker-hours. Time for 2 = 24/2 = 12.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5 workers take 10 hours to complete a job, how long would 3 workers take?', '10 hours', '6.0 hours', '18.666666666666668 hours', '16.666666666666668 hours', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 5 × 10 = 50 worker-hours. Time for 3 = 50/3 = 16.666666666666668 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 3 workers take 4 hours to complete a job, how long would 3 workers take?', 'Cannot determine', '4.0 hours', '6.0 hours', '4 hours', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 3 × 4 = 12 worker-hours. Time for 3 = 12/3 = 4.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 3 workers take 10 hours to complete a job, how long would 6 workers take?', '10 hours', '7.0 hours', '20.0 hours', '5.0 hours', 3,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 3 × 10 = 30 worker-hours. Time for 6 = 30/6 = 5.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 7 workers take 8 hours to complete a job, how long would 4 workers take?', '4.571428571428571 hours', '14.0 hours', '8 hours', '16.0 hours', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 7 × 8 = 56 worker-hours. Time for 4 = 56/4 = 14.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 3 workers take 8 hours to complete a job, how long would 3 workers take?', '8 hours', '8.0 hours', '10.0 hours', 'Cannot determine', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 3 × 8 = 24 worker-hours. Time for 3 = 24/3 = 8.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 4 workers take 10 hours to complete a job, how long would 3 workers take?', '7.5 hours', '13.333333333333334 hours', '15.333333333333334 hours', '10 hours', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 4 × 10 = 40 worker-hours. Time for 3 = 40/3 = 13.333333333333334 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 5 workers take 9 hours to complete a job, how long would 5 workers take?', '9.0 hours', '11.0 hours', 'Cannot determine', '9 hours', 0,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 5 × 9 = 45 worker-hours. Time for 5 = 45/5 = 9.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If 6 workers take 6 hours to complete a job, how long would 4 workers take?', '11.0 hours', '9.0 hours', '4.0 hours', '6 hours', 1,
'lc_ol_applied_measure', 8, 'proficient', 'lc_ol', 'Total work = 6 × 6 = 36 worker-hours. Time for 4 = 36/4 = 9.0 hours', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 100 g and volume 25 cm³. Calculate its density.', '4.0 g/cm³', '2500 g/cm³', '5.0 g/cm³', '0.25 g/cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 100 ÷ 25 = 4.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 400 g and volume 40 cm³. Calculate its density.', '16000 g/cm³', '10.0 g/cm³', '0.1 g/cm³', '11.0 g/cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 400 ÷ 40 = 10.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 300 g and volume 50 cm³. Calculate its density.', '15000 g/cm³', '0.16666666666666666 g/cm³', '6.0 g/cm³', '7.0 g/cm³', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 300 ÷ 50 = 6.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 200 g and volume 25 cm³. Calculate its density.', '0.125 g/cm³', '9.0 g/cm³', '8.0 g/cm³', '5000 g/cm³', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 200 ÷ 25 = 8.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 250 g and volume 40 cm³. Calculate its density.', '6.25 g/cm³', '10000 g/cm³', '7.25 g/cm³', '0.16 g/cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 250 ÷ 40 = 6.25 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 100 g and volume 20 cm³. Calculate its density.', '2000 g/cm³', '5.0 g/cm³', '0.2 g/cm³', '6.0 g/cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 100 ÷ 20 = 5.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 400 g and volume 40 cm³. Calculate its density.', '0.1 g/cm³', '10.0 g/cm³', '11.0 g/cm³', '16000 g/cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 400 ÷ 40 = 10.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 200 g and volume 25 cm³. Calculate its density.', '8.0 g/cm³', '0.125 g/cm³', '5000 g/cm³', '9.0 g/cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 200 ÷ 25 = 8.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 400 g and volume 25 cm³. Calculate its density.', '0.0625 g/cm³', '16.0 g/cm³', '17.0 g/cm³', '10000 g/cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 400 ÷ 25 = 16.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 150 g and volume 20 cm³. Calculate its density.', '0.13333333333333333 g/cm³', '7.5 g/cm³', '8.5 g/cm³', '3000 g/cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 150 ÷ 20 = 7.5 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 200 g and volume 100 cm³. Calculate its density.', '3.0 g/cm³', '20000 g/cm³', '2.0 g/cm³', '0.5 g/cm³', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 200 ÷ 100 = 2.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 100 g and volume 20 cm³. Calculate its density.', '5.0 g/cm³', '6.0 g/cm³', '0.2 g/cm³', '2000 g/cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 100 ÷ 20 = 5.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 400 g and volume 25 cm³. Calculate its density.', '0.0625 g/cm³', '10000 g/cm³', '17.0 g/cm³', '16.0 g/cm³', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 400 ÷ 25 = 16.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 100 g and volume 50 cm³. Calculate its density.', '2.0 g/cm³', '3.0 g/cm³', '5000 g/cm³', '0.5 g/cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 100 ÷ 50 = 2.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 200 g and volume 20 cm³. Calculate its density.', '4000 g/cm³', '10.0 g/cm³', '0.1 g/cm³', '11.0 g/cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 200 ÷ 20 = 10.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 300 g and volume 20 cm³. Calculate its density.', '0.06666666666666667 g/cm³', '6000 g/cm³', '16.0 g/cm³', '15.0 g/cm³', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 300 ÷ 20 = 15.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 500 g and volume 50 cm³. Calculate its density.', '0.1 g/cm³', '11.0 g/cm³', '10.0 g/cm³', '25000 g/cm³', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 500 ÷ 50 = 10.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 200 g and volume 100 cm³. Calculate its density.', '2.0 g/cm³', '20000 g/cm³', '0.5 g/cm³', '3.0 g/cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 200 ÷ 100 = 2.0 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 100 g and volume 40 cm³. Calculate its density.', '2.5 g/cm³', '0.4 g/cm³', '4000 g/cm³', '3.5 g/cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 100 ÷ 40 = 2.5 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('An object has mass 300 g and volume 40 cm³. Calculate its density.', '8.5 g/cm³', '0.13333333333333333 g/cm³', '12000 g/cm³', '7.5 g/cm³', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Density = Mass ÷ Volume = 300 ÷ 40 = 7.5 g/cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 10 g/cm³. What is the mass of 30 cm³?', '3.0 g', '40 g', '30.0 g', '300 g', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 10 × 30 = 300 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2.5 g/cm³. What is the mass of 40 cm³?', '16.0 g', '100.0 g', '42.5 g', '10.0 g', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2.5 × 40 = 100.0 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³. What is the mass of 50 cm³?', '10.0 g', '52 g', '25.0 g', '100 g', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2 × 50 = 100 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³. What is the mass of 20 cm³?', '4.0 g', '22 g', '10.0 g', '40 g', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2 × 20 = 40 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 10 g/cm³. What is the mass of 30 cm³?', '3.0 g', '30.0 g', '300 g', '40 g', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 10 × 30 = 300 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³. What is the mass of 30 cm³?', '15.0 g', '60 g', '6.0 g', '32 g', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2 × 30 = 60 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 5 g/cm³. What is the mass of 30 cm³?', '15.0 g', '6.0 g', '35 g', '150 g', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 5 × 30 = 150 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³. What is the mass of 40 cm³?', '80 g', '42 g', '8.0 g', '20.0 g', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2 × 40 = 80 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³. What is the mass of 50 cm³?', '10.0 g', '100 g', '52 g', '25.0 g', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2 × 50 = 100 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³. What is the mass of 30 cm³?', '6.0 g', '60 g', '15.0 g', '32 g', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2 × 30 = 60 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 10 g/cm³. What is the mass of 100 cm³?', '10.0 g', '110 g', '1000 g', '100.0 g', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 10 × 100 = 1000 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 5 g/cm³. What is the mass of 100 cm³?', '105 g', '20.0 g', '500 g', '50.0 g', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 5 × 100 = 500 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³. What is the mass of 30 cm³?', '15.0 g', '60 g', '6.0 g', '32 g', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2 × 30 = 60 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 7.5 g/cm³. What is the mass of 20 cm³?', '2.6666666666666665 g', '15.0 g', '150.0 g', '27.5 g', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 7.5 × 20 = 150.0 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2.5 g/cm³. What is the mass of 50 cm³?', '12.5 g', '52.5 g', '20.0 g', '125.0 g', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Mass = Density × Volume = 2.5 × 50 = 125.0 g', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 8 g/cm³ and mass 400 g. What is its volume?', '408 cm³', '3200 cm³', '100.0 cm³', '50.0 cm³', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 400 ÷ 8 = 50.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 8 g/cm³ and mass 100 g. What is its volume?', '12.5 cm³', '108 cm³', '800 cm³', '25.0 cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 100 ÷ 8 = 12.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 10 g/cm³ and mass 500 g. What is its volume?', '100.0 cm³', '5000 cm³', '50.0 cm³', '510 cm³', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 500 ÷ 10 = 50.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 8 g/cm³ and mass 100 g. What is its volume?', '25.0 cm³', '12.5 cm³', '800 cm³', '108 cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 100 ÷ 8 = 12.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2.5 g/cm³ and mass 400 g. What is its volume?', '320.0 cm³', '402.5 cm³', '160.0 cm³', '1000.0 cm³', 2,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 400 ÷ 2.5 = 160.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 5 g/cm³ and mass 400 g. What is its volume?', '160.0 cm³', '80.0 cm³', '2000 cm³', '405 cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 400 ÷ 5 = 80.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³ and mass 400 g. What is its volume?', '200.0 cm³', '800 cm³', '402 cm³', '400.0 cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 400 ÷ 2 = 200.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 5 g/cm³ and mass 500 g. What is its volume?', '505 cm³', '200.0 cm³', '2500 cm³', '100.0 cm³', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 500 ÷ 5 = 100.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 4 g/cm³ and mass 200 g. What is its volume?', '100.0 cm³', '50.0 cm³', '204 cm³', '800 cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 200 ÷ 4 = 50.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2 g/cm³ and mass 500 g. What is its volume?', '250.0 cm³', '500.0 cm³', '1000 cm³', '502 cm³', 0,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 500 ÷ 2 = 250.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 8 g/cm³ and mass 500 g. What is its volume?', '125.0 cm³', '62.5 cm³', '508 cm³', '4000 cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 500 ÷ 8 = 62.5 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2.5 g/cm³ and mass 800 g. What is its volume?', '640.0 cm³', '320.0 cm³', '802.5 cm³', '2000.0 cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 800 ÷ 2.5 = 320.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 5 g/cm³ and mass 400 g. What is its volume?', '160.0 cm³', '80.0 cm³', '405 cm³', '2000 cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 400 ÷ 5 = 80.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 10 g/cm³ and mass 400 g. What is its volume?', '80.0 cm³', '410 cm³', '4000 cm³', '40.0 cm³', 3,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 400 ÷ 10 = 40.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A material has density 2.5 g/cm³ and mass 200 g. What is its volume?', '500.0 cm³', '80.0 cm³', '202.5 cm³', '160.0 cm³', 1,
'lc_ol_applied_measure', 9, 'proficient', 'lc_ol', 'Volume = Mass ÷ Density = 200 ÷ 2.5 = 80.0 cm³', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 9:00 in Mumbai, what time is it in Berlin?', '3:00', '5:00', '4.5:00', '9:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Berlin is -4.5 hours from Mumbai. 9:00 + -4.5 = 4.5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 20:00 in Tokyo, what time is it in Berlin?', '20:00', '11:00', '13:00', '12:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Berlin is -8 hours from Tokyo. 20:00 + -8 = 12:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 18:00 in Paris, what time is it in London?', 'Cannot determine', '16:00', '18:00', '17:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'London is -1 hours from Paris. 18:00 + -1 = 17:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 20:00 in Paris, what time is it in New York?', '15:00', '20:00', '14:00', '13:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is -6 hours from Paris. 20:00 + -6 = 14:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 19:00 in Los Angeles, what time is it in Dubai?', '8:00', '19:00', '6:00', '7:00 (next day)', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Dubai is +12 hours from Los Angeles. 19:00 + 12 = 7:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 12:00 in Dublin, what time is it in Mumbai?', '12:00', '16:00', '18:00', '17.5:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Mumbai is +5.5 hours from Dublin. 12:00 + 5.5 = 17.5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 8:00 in New York, what time is it in Los Angeles?', '6:00', '5:00', '8:00', '4:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Los Angeles is -3 hours from New York. 8:00 + -3 = 5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 13:00 in Berlin, what time is it in New York?', '7:00', '6:00', '13:00', '8:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is -6 hours from Berlin. 13:00 + -6 = 7:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 18:00 in Berlin, what time is it in Dublin?', 'Cannot determine', '16:00', '17:00', '18:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Dublin is -1 hours from Berlin. 18:00 + -1 = 17:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 15:00 in Sydney, what time is it in Dublin?', '15:00', '3:00', '4:00', '5:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Dublin is -11 hours from Sydney. 15:00 + -11 = 4:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 14:00 in Sydney, what time is it in New York?', '21:00', '22:00 (previous day)', '14:00', '23:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is -16 hours from Sydney. 14:00 + -16 = 22:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 16:00 in New York, what time is it in Berlin?', '21:00', '16:00', '23:00', '22:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Berlin is +6 hours from New York. 16:00 + 6 = 22:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 10:00 in London, what time is it in New York?', '10:00', '6:00', '5:00', '4:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is -5 hours from London. 10:00 + -5 = 5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 8:00 in London, what time is it in New York?', '8:00', '2:00', '3:00', '4:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is -5 hours from London. 8:00 + -5 = 3:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 13:00 in Los Angeles, what time is it in New York?', '13:00', '15:00', '16:00', '17:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is +3 hours from Los Angeles. 13:00 + 3 = 16:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 11:00 in Berlin, what time is it in Dubai?', '14:00', '15:00', '13:00', '11:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Dubai is +3 hours from Berlin. 11:00 + 3 = 14:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 8:00 in London, what time is it in New York?', '4:00', '3:00', '2:00', '8:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is -5 hours from London. 8:00 + -5 = 3:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 10:00 in Mumbai, what time is it in Dubai?', '9:00', '10:00', '8.5:00', '7:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Dubai is -1.5 hours from Mumbai. 10:00 + -1.5 = 8.5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 19:00 in Sydney, what time is it in Paris?', '9:00', '8:00', '19:00', '10:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Paris is -10 hours from Sydney. 19:00 + -10 = 9:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 15:00 in Dublin, what time is it in Los Angeles?', '15:00', '6:00', '7:00', '8:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Los Angeles is -8 hours from Dublin. 15:00 + -8 = 7:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 17:00 in Dubai, what time is it in Berlin?', '14:00', '15:00', '17:00', '13:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Berlin is -3 hours from Dubai. 17:00 + -3 = 14:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 16:00 in Berlin, what time is it in Mumbai?', '21:00', '19:00', '20.5:00', '16:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Mumbai is +4.5 hours from Berlin. 16:00 + 4.5 = 20.5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 10:00 in Mumbai, what time is it in Berlin?', '6:00', '5.5:00', '10:00', '4:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Berlin is -4.5 hours from Mumbai. 10:00 + -4.5 = 5.5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 14:00 in Sydney, what time is it in Paris?', '4:00', '3:00', '5:00', '14:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Paris is -10 hours from Sydney. 14:00 + -10 = 4:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('When it''s 9:00 in Mumbai, what time is it in New York?', '22.5:00 (previous day)', '21:00', '23:00', '9:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'New York is -10.5 hours from Mumbai. 9:00 + -10.5 = 22.5:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 13:00, flight time is 4 hours, destination is -3 hours different. Arrival time?', '16:00', '14:00', '13:00', '17:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 13 + 4 + -3 = 14:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 14:00, flight time is 4 hours, destination is +1 hours different. Arrival time?', 'Cannot determine', '19:00', '21:00', '18:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 14 + 4 + 1 = 19:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 12:00, flight time is 8 hours, destination is +4 hours different. Arrival time?', '2:00', '23:00', '0:00 (next day)', '20:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 12 + 8 + 4 = 0:00 (next day)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 8:00, flight time is 4 hours, destination is +6 hours different. Arrival time?', '17:00', '12:00', '20:00', '18:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 8 + 4 + 6 = 18:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 13:00, flight time is 8 hours, destination is +1 hours different. Arrival time?', 'Cannot determine', '22:00', '0:00', '21:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 13 + 8 + 1 = 22:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 13:00, flight time is 4 hours, destination is +6 hours different. Arrival time?', '17:00', '1:00', '22:00', '23:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 13 + 4 + 6 = 23:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 12:00, flight time is 5 hours, destination is -3 hours different. Arrival time?', '16:00', '14:00', '17:00', '13:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 12 + 5 + -3 = 14:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 8:00, flight time is 8 hours, destination is +4 hours different. Arrival time?', '22:00', '20:00', '16:00', '19:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 8 + 8 + 4 = 20:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 12:00, flight time is 5 hours, destination is +6 hours different. Arrival time?', '17:00', '23:00', '1:00', '22:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 12 + 5 + 6 = 23:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 9:00, flight time is 4 hours, destination is +2 hours different. Arrival time?', '17:00', '15:00', '13:00', '14:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 9 + 4 + 2 = 15:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 12:00, flight time is 4 hours, destination is +6 hours different. Arrival time?', '22:00', '0:00', '21:00', '16:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 12 + 4 + 6 = 22:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 11:00, flight time is 3 hours, destination is +4 hours different. Arrival time?', '17:00', '14:00', '20:00', '18:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 11 + 3 + 4 = 18:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 9:00, flight time is 5 hours, destination is -3 hours different. Arrival time?', '11:00', '14:00', '13:00', '10:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 9 + 5 + -3 = 11:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 12:00, flight time is 8 hours, destination is -3 hours different. Arrival time?', '19:00', '20:00', '16:00', '17:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 12 + 8 + -3 = 17:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 8:00, flight time is 6 hours, destination is +1 hours different. Arrival time?', '14:00', 'Cannot determine', '15:00', '17:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 8 + 6 + 1 = 15:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 11:00, flight time is 2 hours, destination is +2 hours different. Arrival time?', '17:00', '15:00', '13:00', '14:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 11 + 2 + 2 = 15:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 11:00, flight time is 2 hours, destination is -3 hours different. Arrival time?', '12:00', '13:00', '9:00', '10:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 11 + 2 + -3 = 10:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 11:00, flight time is 2 hours, destination is +4 hours different. Arrival time?', '19:00', '13:00', '16:00', '17:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 11 + 2 + 4 = 17:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 14:00, flight time is 3 hours, destination is +2 hours different. Arrival time?', '19:00', '18:00', '21:00', '17:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 14 + 3 + 2 = 19:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 10:00, flight time is 3 hours, destination is +6 hours different. Arrival time?', '13:00', '19:00', '21:00', '18:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 10 + 3 + 6 = 19:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 8:00, flight time is 2 hours, destination is -3 hours different. Arrival time?', '10:00', '9:00', '6:00', '7:00', 3,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 8 + 2 + -3 = 7:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 12:00, flight time is 6 hours, destination is +2 hours different. Arrival time?', '20:00', '19:00', '18:00', '22:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 12 + 6 + 2 = 20:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 12:00, flight time is 6 hours, destination is -3 hours different. Arrival time?', '18:00', '15:00', '14:00', '17:00', 1,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 12 + 6 + -3 = 15:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 10:00, flight time is 4 hours, destination is +1 hours different. Arrival time?', 'Cannot determine', '14:00', '15:00', '17:00', 2,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 10 + 4 + 1 = 15:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A flight departs at 14:00, flight time is 5 hours, destination is -3 hours different. Arrival time?', '16:00', '19:00', '18:00', '15:00', 0,
'lc_ol_applied_measure', 10, 'advanced', 'lc_ol', 'Arrive = 14 + 5 + -3 = 16:00', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 10, 7, 10, 12. Find the area.', '140.0 sq units', '195 sq units', '280.0 sq units', '145.0 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (10 + 12 + 2×17) = 140.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 5, 2, 2. Find the area.', '9 sq units', '5.5 sq units', '6.5 sq units', '11.0 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (5 + 2 + 2×2) = 5.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 2, 10, 11, 3, 11. Find the area.', '31.5 sq units', '61.0 sq units', '30.5 sq units', '37 sq units', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (2 + 11 + 2×24) = 30.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 2 and y-values: 5, 6, 8. Find the area.', '50.0 sq units', '27.0 sq units', '38 sq units', '25.0 sq units', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 2/2 × (5 + 8 + 2×6) = 25.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 15, 8, 6. Find the area.', '19.5 sq units', '29 sq units', '37.0 sq units', '18.5 sq units', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (15 + 6 + 2×8) = 18.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 10, 2, 4, 2, 3. Find the area.', '72.5 sq units', '105 sq units', '77.5 sq units', '145.0 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (10 + 3 + 2×8) = 72.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 2 and y-values: 10, 7, 10, 8, 2. Find the area.', '62.0 sq units', '74 sq units', '64.0 sq units', '124.0 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 2/2 × (10 + 2 + 2×25) = 62.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 4, 4, 15. Find the area.', '72.5 sq units', '135.0 sq units', '67.5 sq units', '115 sq units', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (4 + 15 + 2×4) = 67.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 10, 5, 10. Find the area.', '15.0 sq units', '25 sq units', '30.0 sq units', '16.0 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (10 + 10 + 2×5) = 15.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 5, 6, 15, 5. Find the area.', '130.0 sq units', '155 sq units', '135.0 sq units', '260.0 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (5 + 5 + 2×21) = 130.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 4, 9, 2. Find the area.', '24.0 sq units', '12.0 sq units', '15 sq units', '13.0 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (4 + 2 + 2×9) = 12.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 8, 13, 12, 8, 3. Find the area.', '77.0 sq units', '38.5 sq units', '39.5 sq units', '44 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (8 + 3 + 2×33) = 38.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 7, 14, 4. Find the area.', '102.5 sq units', '97.5 sq units', '125 sq units', '195.0 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (7 + 4 + 2×14) = 97.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 2 and y-values: 15, 3, 13, 4. Find the area.', '53.0 sq units', '70 sq units', '102.0 sq units', '51.0 sq units', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 2/2 × (15 + 4 + 2×16) = 51.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 2 and y-values: 15, 2, 6, 9, 10. Find the area.', '59.0 sq units', '84 sq units', '61.0 sq units', '118.0 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 2/2 × (15 + 10 + 2×17) = 59.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 8, 2, 2. Find the area.', '60 sq units', '35.0 sq units', '70.0 sq units', '40.0 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (8 + 2 + 2×2) = 35.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 10, 6, 5, 4, 2. Find the area.', '110.0 sq units', '105.0 sq units', '210.0 sq units', '135 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (10 + 2 + 2×15) = 105.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 9, 7, 6, 11. Find the area.', '33 sq units', '46.0 sq units', '23.0 sq units', '24.0 sq units', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (9 + 11 + 2×13) = 23.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 5, 7, 8, 10, 7. Find the area.', '31.0 sq units', '32.0 sq units', '62.0 sq units', '37 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (5 + 7 + 2×25) = 31.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 10, 13, 6, 14, 6. Find the area.', '205.0 sq units', '410.0 sq units', '210.0 sq units', '245 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (10 + 6 + 2×33) = 205.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 6, 9, 14. Find the area.', '38.0 sq units', '29 sq units', '20.0 sq units', '19.0 sq units', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (6 + 14 + 2×9) = 19.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 4, 11, 2, 13, 3. Find the area.', '295.0 sq units', '147.5 sq units', '165 sq units', '152.5 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (4 + 3 + 2×26) = 147.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 9, 10, 3, 6, 10. Find the area.', '28.5 sq units', '57.0 sq units', '29.5 sq units', '38 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (9 + 10 + 2×19) = 28.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 14, 6, 7, 7, 3. Find the area.', '57.0 sq units', '28.5 sq units', '37 sq units', '29.5 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (14 + 3 + 2×20) = 28.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 15, 12, 8. Find the area.', '23.5 sq units', '24.5 sq units', '47.0 sq units', '35 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (15 + 8 + 2×12) = 23.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 9, 2, 12, 3. Find the area.', '200.0 sq units', '105.0 sq units', '100.0 sq units', '130 sq units', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (9 + 3 + 2×14) = 100.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 15, 13, 15, 11, 7. Find the area.', '305 sq units', '255.0 sq units', '500.0 sq units', '250.0 sq units', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (15 + 7 + 2×39) = 250.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 5 and y-values: 8, 5, 9. Find the area.', '110 sq units', '67.5 sq units', '135.0 sq units', '72.5 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 5/2 × (8 + 9 + 2×5) = 67.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 1 and y-values: 6, 11, 15, 11. Find the area.', '35.5 sq units', '34.5 sq units', '43 sq units', '69.0 sq units', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 1/2 × (6 + 11 + 2×26) = 34.5 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Use the trapezoidal rule with h = 2 and y-values: 5, 12, 7, 3, 10. Find the area.', '59.0 sq units', '74 sq units', '118.0 sq units', '61.0 sq units', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'Area = 2/2 × (5 + 10 + 2×22) = 59.0 sq units', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [5, 9] with 2 strips, what is h?', '4', '2.0', '1.0', '4.0', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (9 - 5) / 2 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [2, 10] with 2 strips, what is h?', '2.0', '8.0', '8', '4.0', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (10 - 2) / 2 = 4.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [1, 5] with 4 strips, what is h?', '1.0', '4', '0.5', '2.0', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (5 - 1) / 4 = 1.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [2, 12] with 5 strips, what is h?', '4.0', '1.0', '2.0', '10', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (12 - 2) / 5 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [4, 14] with 2 strips, what is h?', '2.5', '5.0', '10', '10.0', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (14 - 4) / 2 = 5.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [1, 11] with 5 strips, what is h?', '10', '2.0', '4.0', '1.0', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (11 - 1) / 5 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [0, 6] with 5 strips, what is h?', '0.6', '2.4', '1.2', '6', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (6 - 0) / 5 = 1.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [2, 6] with 2 strips, what is h?', '1.0', '4.0', '2.0', '4', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (6 - 2) / 2 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [3, 9] with 5 strips, what is h?', '0.6', '1.2', '6', '2.4', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (9 - 3) / 5 = 1.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [0, 8] with 5 strips, what is h?', '0.8', '3.2', '8', '1.6', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (8 - 0) / 5 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [1, 5] with 5 strips, what is h?', '0.4', '0.8', '4', '1.6', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (5 - 1) / 5 = 0.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [4, 8] with 5 strips, what is h?', '1.6', '0.4', '0.8', '4', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (8 - 4) / 5 = 0.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [1, 7] with 2 strips, what is h?', '3.0', '1.5', '6', '6.0', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (7 - 1) / 2 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [5, 13] with 4 strips, what is h?', '8', '4.0', '1.0', '2.0', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (13 - 5) / 4 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [5, 15] with 5 strips, what is h?', '10', '1.0', '4.0', '2.0', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (15 - 5) / 5 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [0, 8] with 5 strips, what is h?', '0.8', '8', '1.6', '3.2', 2,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (8 - 0) / 5 = 1.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [4, 12] with 4 strips, what is h?', '1.0', '2.0', '4.0', '8', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (12 - 4) / 4 = 2.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [2, 12] with 2 strips, what is h?', '5.0', '10', '10.0', '2.5', 0,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (12 - 2) / 2 = 5.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [2, 12] with 4 strips, what is h?', '5.0', '2.5', '1.25', '10', 1,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (12 - 2) / 4 = 2.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For the trapezoidal rule on [1, 7] with 2 strips, what is h?', '6', '6.0', '1.5', '3.0', 3,
'lc_ol_applied_measure', 11, 'advanced', 'lc_ol', 'h = (b - a) / n = (7 - 1) / 2 = 3.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 53 km at 50 km/h, then 61 km at 80 km/h. What is the average speed?', '67.6 km/h', '65.0 km/h', '50 km/h', '62.6 km/h', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 114 km, Total time = 1.82 h. Avg speed = 62.6 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 74 km at 50 km/h, then 84 km at 120 km/h. What is the average speed?', '85.0 km/h', '50 km/h', '72.5 km/h', '77.5 km/h', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 158 km, Total time = 2.18 h. Avg speed = 72.5 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 60 km at 50 km/h, then 68 km at 80 km/h. What is the average speed?', '67.4 km/h', '62.4 km/h', '50 km/h', '65.0 km/h', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 128 km, Total time = 2.05 h. Avg speed = 62.4 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 80 km at 60 km/h, then 76 km at 120 km/h. What is the average speed?', '79.3 km/h', '90.0 km/h', '84.3 km/h', '60 km/h', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 156 km, Total time = 1.97 h. Avg speed = 79.3 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 70 km at 60 km/h, then 84 km at 80 km/h. What is the average speed?', '74.5 km/h', '70.0 km/h', '60 km/h', '69.5 km/h', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 154 km, Total time = 2.22 h. Avg speed = 69.5 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 74 km at 60 km/h, then 87 km at 100 km/h. What is the average speed?', '76.5 km/h', '80.0 km/h', '81.5 km/h', '60 km/h', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 161 km, Total time = 2.1 h. Avg speed = 76.5 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 59 km at 50 km/h, then 97 km at 100 km/h. What is the average speed?', '75.0 km/h', '72.6 km/h', '50 km/h', '77.6 km/h', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 156 km, Total time = 2.15 h. Avg speed = 72.6 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 76 km at 50 km/h, then 62 km at 120 km/h. What is the average speed?', '72.8 km/h', '50 km/h', '85.0 km/h', '67.8 km/h', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 138 km, Total time = 2.04 h. Avg speed = 67.8 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 53 km at 40 km/h, then 89 km at 80 km/h. What is the average speed?', '63.3 km/h', '58.3 km/h', '40 km/h', '60.0 km/h', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 142 km, Total time = 2.44 h. Avg speed = 58.3 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 51 km at 60 km/h, then 90 km at 100 km/h. What is the average speed?', '80.0 km/h', '85.6 km/h', '80.6 km/h', '60 km/h', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 141 km, Total time = 1.75 h. Avg speed = 80.6 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 71 km at 60 km/h, then 53 km at 80 km/h. What is the average speed?', '67.2 km/h', '72.2 km/h', '60 km/h', '70.0 km/h', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 124 km, Total time = 1.85 h. Avg speed = 67.2 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 67 km at 40 km/h, then 59 km at 100 km/h. What is the average speed?', '70.0 km/h', '40 km/h', '55.6 km/h', '60.6 km/h', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 126 km, Total time = 2.27 h. Avg speed = 55.6 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 84 km at 60 km/h, then 99 km at 80 km/h. What is the average speed?', '69.4 km/h', '74.4 km/h', '60 km/h', '70.0 km/h', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 183 km, Total time = 2.64 h. Avg speed = 69.4 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 89 km at 50 km/h, then 91 km at 100 km/h. What is the average speed?', '71.9 km/h', '50 km/h', '66.9 km/h', '75.0 km/h', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 180 km, Total time = 2.69 h. Avg speed = 66.9 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Drive 84 km at 50 km/h, then 50 km at 80 km/h. What is the average speed?', '50 km/h', '65.0 km/h', '58.1 km/h', '63.1 km/h', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Total dist = 134 km, Total time = 2.3 h. Avg speed = 58.1 km/h', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 L/100km. Fuel costs €1.9/L. What is the fuel cost for 350 km?', '€31.5', '€6.65', '€69.85', '€59.85', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 9 × 350/100 = 31.5 L. Cost = 31.5 × €1.9 = €59.85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 L/100km. Fuel costs €1.8/L. What is the fuel cost for 400 km?', '€74.8', '€36.0', '€64.8', '€7.2', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 9 × 400/100 = 36.0 L. Cost = 36.0 × €1.8 = €64.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 L/100km. Fuel costs €1.8/L. What is the fuel cost for 500 km?', '€54.0', '€9.0', '€30.0', '€64.0', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 6 × 500/100 = 30.0 L. Cost = 30.0 × €1.8 = €54.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 L/100km. Fuel costs €1.9/L. What is the fuel cost for 450 km?', '€8.55', '€36.0', '€68.4', '€78.4', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 8 × 450/100 = 36.0 L. Cost = 36.0 × €1.9 = €68.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 7 L/100km. Fuel costs €1.6/L. What is the fuel cost for 350 km?', '€49.2', '€39.2', '€5.6', '€24.5', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 7 × 350/100 = 24.5 L. Cost = 24.5 × €1.6 = €39.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 L/100km. Fuel costs €1.7/L. What is the fuel cost for 450 km?', '€71.2', '€7.65', '€36.0', '€61.2', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 8 × 450/100 = 36.0 L. Cost = 36.0 × €1.7 = €61.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 7 L/100km. Fuel costs €1.9/L. What is the fuel cost for 450 km?', '€31.5', '€59.85', '€8.55', '€69.85', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 7 × 450/100 = 31.5 L. Cost = 31.5 × €1.9 = €59.85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 L/100km. Fuel costs €1.9/L. What is the fuel cost for 450 km?', '€68.4', '€8.55', '€78.4', '€36.0', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 8 × 450/100 = 36.0 L. Cost = 36.0 × €1.9 = €68.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 L/100km. Fuel costs €1.9/L. What is the fuel cost for 450 km?', '€36.0', '€8.55', '€68.4', '€78.4', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 8 × 450/100 = 36.0 L. Cost = 36.0 × €1.9 = €68.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 L/100km. Fuel costs €1.7/L. What is the fuel cost for 500 km?', '€45.0', '€86.5', '€8.5', '€76.5', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 9 × 500/100 = 45.0 L. Cost = 45.0 × €1.7 = €76.5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 L/100km. Fuel costs €1.8/L. What is the fuel cost for 350 km?', '€66.7', '€31.5', '€6.3', '€56.7', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 9 × 350/100 = 31.5 L. Cost = 31.5 × €1.8 = €56.7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 L/100km. Fuel costs €1.9/L. What is the fuel cost for 350 km?', '€6.65', '€21.0', '€39.9', '€49.9', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 6 × 350/100 = 21.0 L. Cost = 21.0 × €1.9 = €39.9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 7 L/100km. Fuel costs €1.7/L. What is the fuel cost for 400 km?', '€28.0', '€6.8', '€57.6', '€47.6', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 7 × 400/100 = 28.0 L. Cost = 28.0 × €1.7 = €47.6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 L/100km. Fuel costs €1.6/L. What is the fuel cost for 450 km?', '€53.2', '€43.2', '€7.2', '€27.0', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 6 × 450/100 = 27.0 L. Cost = 27.0 × €1.6 = €43.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 L/100km. Fuel costs €1.6/L. What is the fuel cost for 350 km?', '€5.6', '€60.4', '€50.4', '€31.5', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 9 × 350/100 = 31.5 L. Cost = 31.5 × €1.6 = €50.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 L/100km. Fuel costs €1.8/L. What is the fuel cost for 450 km?', '€8.1', '€64.8', '€36.0', '€74.8', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 8 × 450/100 = 36.0 L. Cost = 36.0 × €1.8 = €64.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 L/100km. Fuel costs €1.6/L. What is the fuel cost for 500 km?', '€64.0', '€40.0', '€74.0', '€8.0', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 8 × 500/100 = 40.0 L. Cost = 40.0 × €1.6 = €64.0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 9 L/100km. Fuel costs €1.6/L. What is the fuel cost for 450 km?', '€64.8', '€74.8', '€40.5', '€7.2', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 9 × 450/100 = 40.5 L. Cost = 40.5 × €1.6 = €64.8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 8 L/100km. Fuel costs €1.8/L. What is the fuel cost for 350 km?', '€28.0', '€60.4', '€6.3', '€50.4', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 8 × 350/100 = 28.0 L. Cost = 28.0 × €1.8 = €50.4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A car uses 6 L/100km. Fuel costs €1.8/L. What is the fuel cost for 400 km?', '€53.2', '€24.0', '€43.2', '€7.2', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Fuel = 6 × 400/100 = 24.0 L. Cost = 24.0 × €1.8 = €43.2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 10cm × 7cm on a 1:500 drawing. What is its actual area in m²?', '1750.0 m²', '35000 m²', '17500000 m²', '175.0 m²', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 5000cm × 3500cm = 17500000cm² = 1750.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 7cm × 6cm on a 1:100 drawing. What is its actual area in m²?', '4.2 m²', '420000 m²', '42.0 m²', '4200 m²', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 700cm × 600cm = 420000cm² = 42.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 4cm × 6cm on a 1:100 drawing. What is its actual area in m²?', '240000 m²', '2.4 m²', '2400 m²', '24.0 m²', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 400cm × 600cm = 240000cm² = 24.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 9cm × 6cm on a 1:100 drawing. What is its actual area in m²?', '540000 m²', '5400 m²', '5.4 m²', '54.0 m²', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 900cm × 600cm = 540000cm² = 54.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 10cm × 5cm on a 1:100 drawing. What is its actual area in m²?', '5.0 m²', '500000 m²', '50.0 m²', '5000 m²', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 1000cm × 500cm = 500000cm² = 50.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 10cm × 3cm on a 1:100 drawing. What is its actual area in m²?', '3.0 m²', '300000 m²', '30.0 m²', '3000 m²', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 1000cm × 300cm = 300000cm² = 30.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 4cm × 5cm on a 1:200 drawing. What is its actual area in m²?', '80.0 m²', '800000 m²', '8.0 m²', '4000 m²', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 800cm × 1000cm = 800000cm² = 80.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 9cm × 7cm on a 1:100 drawing. What is its actual area in m²?', '6300 m²', '630000 m²', '6.3 m²', '63.0 m²', 3,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 900cm × 700cm = 630000cm² = 63.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 9cm × 3cm on a 1:200 drawing. What is its actual area in m²?', '10.8 m²', '108.0 m²', '5400 m²', '1080000 m²', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 1800cm × 600cm = 1080000cm² = 108.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 6cm × 6cm on a 1:500 drawing. What is its actual area in m²?', '90.0 m²', '900.0 m²', '9000000 m²', '18000 m²', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 3000cm × 3000cm = 9000000cm² = 900.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 5cm × 7cm on a 1:100 drawing. What is its actual area in m²?', '3500 m²', '35.0 m²', '350000 m²', '3.5 m²', 1,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 500cm × 700cm = 350000cm² = 35.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 5cm × 7cm on a 1:100 drawing. What is its actual area in m²?', '35.0 m²', '350000 m²', '3500 m²', '3.5 m²', 0,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 500cm × 700cm = 350000cm² = 35.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 9cm × 7cm on a 1:200 drawing. What is its actual area in m²?', '12600 m²', '2520000 m²', '252.0 m²', '25.2 m²', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 1800cm × 1400cm = 2520000cm² = 252.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 7cm × 5cm on a 1:100 drawing. What is its actual area in m²?', '3.5 m²', '3500 m²', '35.0 m²', '350000 m²', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 700cm × 500cm = 350000cm² = 35.0m²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A room is 5cm × 6cm on a 1:200 drawing. What is its actual area in m²?', '12.0 m²', '6000 m²', '120.0 m²', '1200000 m²', 2,
'lc_ol_applied_measure', 12, 'advanced', 'lc_ol', 'Actual: 1000cm × 1200cm = 1200000cm² = 120.0m²', 1);

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = 'lc_ol_applied_measure';
