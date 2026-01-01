-- LC Higher Level - Coordinate Geometry - Complete SQL
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_coord_geom_complete.sql
-- Generated: 2025-12-15

-- Add Coordinate Geometry topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_coord_geom', 'Coordinate Geometry', id, '📐', 11, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_coord_geom';

-- Questions (600 total, 50 per level x 12 levels)

INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (9, -9) and (9, -4).', '6', '4', '10', '5', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |-4 - -9| = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-2, -1) and (4, -9).', '14', '9', '11', '10', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(4--2)² + (-9--1)²] = √[6² + 8²] = √100 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-4, 0) and (1, -2).', '√30', '7', '√29', '2√7', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[5² + 2²] = √29 = √29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (2, -3) and (5, -3).', '2', '3', '4', '6', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |5 - 2| = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (0, -4) and (0, 3).', '8', '14', '7', '6', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |3 - -4| = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (2, 0) and (6, -5).', '2√10', '9', '√41', '√42', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[4² + 5²] = √41 = √41', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-5, 2) and (-2, 6).', '4', '5', '7', '6', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(-2--5)² + (6-2)²] = √[3² + 4²] = √25 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-3, -1) and (2, 11).', '17', '13', '14', '12', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(2--3)² + (11--1)²] = √[5² + 12²] = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (4, 10) and (15, 10).', '12', '11', '22', '10', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |15 - 4| = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (4, -2) and (0, -4).', '6', '√19', '2√5', '√21', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[4² + 2²] = √20 = 2√5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (5, 3) and (2, -1).', '7', '6', '4', '5', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(2-5)² + (-1-3)²] = √[3² + 4²] = √25 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (4, 2) and (4, 10).', '8', '16', '9', '7', 0,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |10 - 2| = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-6, 3) and (-6, 10).', '8', '14', '7', '6', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |10 - 3| = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (3, 4) and (-2, -8).', '12', '17', '13', '14', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(-2-3)² + (-8-4)²] = √[5² + 12²] = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-3, 2) and (-5, -3).', '√30', '7', '2√7', '√29', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[2² + 5²] = √29 = √29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-2, 5) and (4, -3).', '11', '10', '9', '14', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(4--2)² + (-3-5)²] = √[6² + 8²] = √100 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-2, 0) and (-3, -5).', '3√3', '5', '6', '√26', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[1² + 5²] = √26 = √26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-4, -7) and (-4, -3).', '8', '5', '3', '4', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |-3 - -7| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-4, -8) and (-4, 1).', '18', '10', '9', '8', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |1 - -8| = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (3, -1) and (12, -13).', '14', '16', '21', '15', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(12-3)² + (-13--1)²] = √[9² + 12²] = √225 = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (5, 10) and (16, 10).', '10', '11', '12', '22', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |16 - 5| = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-5, 9) and (1, 9).', '5', '12', '6', '7', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |1 - -5| = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (2, -4) and (7, -16).', '14', '13', '12', '17', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(7-2)² + (-16--4)²] = √[5² + 12²] = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-3, 2) and (0, 4).', '2√3', '√14', '√13', '5', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[3² + 2²] = √13 = √13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-4, -5) and (0, -5).', '4', '8', '5', '3', 0,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |0 - -4| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-3, -8) and (7, -8).', '9', '10', '20', '11', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |7 - -3| = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-10, -1) and (1, -1).', '22', '10', '12', '11', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |1 - -10| = 11', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (4, -5) and (7, -5).', '2', '4', '6', '3', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |7 - 4| = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (3, -1) and (7, -5).', '4√2', '√31', '8', '√33', 0,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[4² + 4²] = √32 = 4√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-2, -9) and (5, -9).', '6', '8', '14', '7', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |5 - -2| = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-5, 0) and (-2, 0).', '2', '4', '6', '3', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |-2 - -5| = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-1, -1) and (11, -1).', '11', '12', '13', '24', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |11 - -1| = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (0, -7) and (12, -7).', '11', '13', '24', '12', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |12 - 0| = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (1, 1) and (6, 13).', '12', '14', '17', '13', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(6-1)² + (13-1)²] = √[5² + 12²] = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-3, 4) and (0, 0).', '4', '5', '6', '7', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(0--3)² + (0-4)²] = √[3² + 4²] = √25 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-3, -5) and (2, -2).', '√34', '8', '√33', '√35', 0,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[5² + 3²] = √34 = √34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (4, 2) and (1, 3).', '√10', '4', '3', '√11', 0,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[3² + 1²] = √10 = √10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (7, -5) and (7, 7).', '24', '11', '13', '12', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |7 - -5| = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (10, 5) and (10, 13).', '16', '9', '8', '7', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |13 - 5| = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-4, -2) and (0, -6).', '√33', '4√2', '8', '√31', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[4² + 4²] = √32 = 4√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-3, -3) and (0, -6).', '6', '3√2', '√19', '√17', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[3² + 3²] = √18 = 3√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-1, -3) and (-5, 1).', '√33', '√31', '4√2', '8', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[4² + 4²] = √32 = 4√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-3, 3) and (-3, 13).', '11', '9', '10', '20', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |13 - 3| = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-3, -3) and (-4, -8).', '6', '3√3', '5', '√26', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[1² + 5²] = √26 = √26', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-5, -2) and (-10, 10).', '14', '17', '13', '12', 2,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(-10--5)² + (10--2)²] = √[5² + 12²] = √169 = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-8, -7) and (-8, 0).', '14', '6', '8', '7', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a vertical line (same x). Distance = |y₂ - y₁| = |0 - -7| = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-5, 6) and (3, 6).', '16', '7', '9', '8', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |3 - -5| = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between (-1, -2) and (3, 2).', '√31', '4√2', '√33', '8', 1,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[4² + 4²] = √32 = 4√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-2, 4) and (6, -2).', '10', '11', '14', '9', 0,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(6--2)² + (-2-4)²] = √[8² + 6²] = √100 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the distance between the points (-1, 0) and (-9, -6).', '14', '9', '11', '10', 3,
'lc_hl_coord_geom', 1, 'foundation', 'lc_hl', 'Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[(-9--1)² + (-6-0)²] = √[8² + 6²] = √100 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (0, -2) and (-6, -3).', '(-6, -5)', '(-6, -1)', '(-3, -5/2)', '(-2, -3)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((0+-6)/2, (-2+-3)/2) = (-3, -5/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (4, 1) and (-8, -1) lies on which axis?', 'Both axes', 'Neither axis', 'y-axis', 'x-axis', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint y-coordinate = (1+-1)/2 = 0/2 = 0. Since y = 0, the midpoint lies on the x-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (4, 8) and (-8, -8) lies on which axis?', 'Neither axis', 'y-axis', 'x-axis', 'Both axes', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint y-coordinate = (8+-8)/2 = 0/2 = 0. Since y = 0, the midpoint lies on the x-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (-5, -2) is the midpoint of the segment from (-5, 8) to point B, find B.', '(-5, -12)', '(-3, -12)', '(-5, -10)', '(0, -10)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So -5 = (-5+x₂)/2 → x₂ = 2(-5)--5 = -5. Similarly y₂ = -12. B = (-5, -12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (6, 10) and (-16, 12).', '(-4, 11)', '(-11, 1)', '(-5, 11)', '(-5, 12)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((6+-16)/2, (10+12)/2) = (-5, 11)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-8, 9) and (-7, -2).', '(-15, 7)', '(-15/2, 7/2)', '(1, -11)', '(-7, 3)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-8+-7)/2, (9+-2)/2) = (-15/2, 7/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-1, 8) and (1, 4).', '(0, 6)', '(0, 12)', '(1, 6)', '(2, -4)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-1+1)/2, (8+4)/2) = (0, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (4, -10) and (0, 4).', '(4, -6)', '(-4, 14)', '(3, -3)', '(2, -3)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((4+0)/2, (-10+4)/2) = (2, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (2, 12) and (-8, -2).', '(-2, 5)', '(-3, 6)', '(-5, -7)', '(-3, 5)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((2+-8)/2, (12+-2)/2) = (-3, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (8, 8) and (-8, -4) lies on which axis?', 'x-axis', 'Both axes', 'y-axis', 'Neither axis', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint x-coordinate = (8+-8)/2 = 0/2 = 0. Since x = 0, the midpoint lies on the y-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (1, 1) and (6, -1) lies on which axis?', 'Both axes', 'Neither axis', 'x-axis', 'y-axis', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint y-coordinate = (1+-1)/2 = 0/2 = 0. Since y = 0, the midpoint lies on the x-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-1, 0) and (1, -9).', '(0, -9/2)', '(0, -9)', '(1, -5)', '(2, -9)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-1+1)/2, (0+-9)/2) = (0, -9/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (3, 6) and (-2, 10).', '(-5, 4)', '(1, 8)', '(1/2, 8)', '(1, 16)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((3+-2)/2, (6+10)/2) = (1/2, 8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (3, -9) and (-2, 2).', '(1, -7)', '(1, -4)', '(1/2, -7/2)', '(-5, 11)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((3+-2)/2, (-9+2)/2) = (1/2, -7/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-2, 16) and (14, -16).', '(6, 0)', '(8, -16)', '(7, 0)', '(6, 1)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-2+14)/2, (16+-16)/2) = (6, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (5, 3) is the midpoint of the segment from (-2, -7) to point B, find B.', '(12, 15)', '(7, 10)', '(14, 13)', '(12, 13)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So 5 = (-2+x₂)/2 → x₂ = 2(5)--2 = 12. Similarly y₂ = 13. B = (12, 13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-7, 6) and (-8, -8).', '(-15/2, -1)', '(-7, -1)', '(-1, -14)', '(-15, -2)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-7+-8)/2, (6+-8)/2) = (-15/2, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (18, -20) and (8, 8).', '(13, -6)', '(-5, 14)', '(13, -5)', '(14, -6)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((18+8)/2, (-20+8)/2) = (13, -6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (8, -4) and (0, -1).', '(5, -3)', '(4, -5/2)', '(8, -5)', '(-8, 3)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((8+0)/2, (-4+-1)/2) = (4, -5/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-4, 12) and (4, 2).', '(0, 7)', '(1, 7)', '(0, 8)', '(4, -5)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-4+4)/2, (12+2)/2) = (0, 7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (20, -2) and (4, -10).', '(12, -5)', '(13, -6)', '(12, -6)', '(-8, -4)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((20+4)/2, (-2+-10)/2) = (12, -6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (3, -8) and (-3, 8) lies on which axis?', 'Both axes', 'x-axis', 'y-axis', 'Neither axis', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint x-coordinate = (3+-3)/2 = 0/2 = 0. Since x = 0, the midpoint lies on the y-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (-3, -3) is the midpoint of the segment from (-1, 6) to point B, find B.', '(-2, -9)', '(-5, -12)', '(-3, -12)', '(-5, -10)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So -3 = (-1+x₂)/2 → x₂ = 2(-3)--1 = -5. Similarly y₂ = -12. B = (-5, -12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (8, 10) and (0, -10) lies on which axis?', 'y-axis', 'x-axis', 'Neither axis', 'Both axes', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint y-coordinate = (10+-10)/2 = 0/2 = 0. Since y = 0, the midpoint lies on the x-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (4, -6) and (14, -8).', '(9, -6)', '(10, -7)', '(9, -7)', '(5, -1)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((4+14)/2, (-6+-8)/2) = (9, -7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (1, -9) and (-1, -4) lies on which axis?', 'y-axis', 'Both axes', 'x-axis', 'Neither axis', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint x-coordinate = (1+-1)/2 = 0/2 = 0. Since x = 0, the midpoint lies on the y-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (-1, 3) and (2, -3) lies on which axis?', 'y-axis', 'Both axes', 'x-axis', 'Neither axis', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint y-coordinate = (3+-3)/2 = 0/2 = 0. Since y = 0, the midpoint lies on the x-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (-7, 6) and (-2, -6) lies on which axis?', 'Both axes', 'x-axis', 'y-axis', 'Neither axis', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint y-coordinate = (6+-6)/2 = 0/2 = 0. Since y = 0, the midpoint lies on the x-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (3, -1) is the midpoint of the segment from (-1, -9) to point B, find B.', '(7, 9)', '(4, 8)', '(7, 7)', '(9, 7)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So 3 = (-1+x₂)/2 → x₂ = 2(3)--1 = 7. Similarly y₂ = 7. B = (7, 7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (-2, 1) is the midpoint of the segment from (-4, -3) to point B, find B.', '(0, 7)', '(2, 5)', '(0, 5)', '(2, 4)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So -2 = (-4+x₂)/2 → x₂ = 2(-2)--4 = 0. Similarly y₂ = 5. B = (0, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (2, 0) is the midpoint of the segment from (8, 7) to point B, find B.', '(-2, -7)', '(-4, -7)', '(-6, -7)', '(-4, -5)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So 2 = (8+x₂)/2 → x₂ = 2(2)-8 = -4. Similarly y₂ = -7. B = (-4, -7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (2, -4) and (6, 10).', '(8, 6)', '(4, 14)', '(5, 3)', '(4, 3)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((2+6)/2, (-4+10)/2) = (4, 3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (4, -2) is the midpoint of the segment from (-6, 8) to point B, find B.', '(14, -12)', '(16, -12)', '(14, -10)', '(10, -10)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So 4 = (-6+x₂)/2 → x₂ = 2(4)--6 = 14. Similarly y₂ = -12. B = (14, -12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (9, 2) and (10, -10).', '(10, -4)', '(19, -8)', '(1, -12)', '(19/2, -4)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((9+10)/2, (2+-10)/2) = (19/2, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-6, 4) and (-20, 0).', '(-13, 3)', '(-13, 2)', '(-12, 2)', '(-7, -2)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-6+-20)/2, (4+0)/2) = (-13, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (0, 1) is the midpoint of the segment from (1, 4) to point B, find B.', '(-1, 0)', '(-1, -3)', '(1, -2)', '(-1, -2)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So 0 = (1+x₂)/2 → x₂ = 2(0)-1 = -1. Similarly y₂ = -2. B = (-1, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-7, 10) and (4, -8).', '(11, -18)', '(-3/2, 1)', '(-3, 2)', '(-1, 1)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-7+4)/2, (10+-8)/2) = (-3/2, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (-1, -3) is the midpoint of the segment from (-2, 4) to point B, find B.', '(1, -7)', '(2, -10)', '(0, -8)', '(0, -10)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So -1 = (-2+x₂)/2 → x₂ = 2(-1)--2 = 0. Similarly y₂ = -10. B = (0, -10)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (10, 0) and (16, -4).', '(13, -2)', '(14, -2)', '(13, -1)', '(3, -2)', 0,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((10+16)/2, (0+-4)/2) = (13, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (3, 4) is the midpoint of the segment from (-2, 8) to point B, find B.', '(8, 2)', '(8, 0)', '(5, -4)', '(10, 0)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So 3 = (-2+x₂)/2 → x₂ = 2(3)--2 = 8. Similarly y₂ = 0. B = (8, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (1, 2) is the midpoint of the segment from (0, -5) to point B, find B.', '(4, 9)', '(1, 7)', '(2, 9)', '(2, 11)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So 1 = (0+x₂)/2 → x₂ = 2(1)-0 = 2. Similarly y₂ = 9. B = (2, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-4, -8) and (-7, -9).', '(-11, -17)', '(-11/2, -17/2)', '(-3, -1)', '(-5, -9)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-4+-7)/2, (-8+-9)/2) = (-11/2, -17/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-5, -7) and (7, 3).', '(2, -4)', '(1, -2)', '(12, 10)', '(2, -2)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-5+7)/2, (-7+3)/2) = (1, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (3, 5) and (-3, -10) lies on which axis?', 'x-axis', 'Neither axis', 'Both axes', 'y-axis', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint x-coordinate = (3+-3)/2 = 0/2 = 0. Since x = 0, the midpoint lies on the y-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (10, 4) and (-5, -4) lies on which axis?', 'y-axis', 'x-axis', 'Both axes', 'Neither axis', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint y-coordinate = (4+-4)/2 = 0/2 = 0. Since y = 0, the midpoint lies on the x-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If (-1, 0) is the midpoint of the segment from (-8, -2) to point B, find B.', '(7, 2)', '(6, 4)', '(8, 2)', '(6, 2)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So -1 = (-8+x₂)/2 → x₂ = 2(-1)--8 = 6. Similarly y₂ = 2. B = (6, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (10, -4) and (-1, -1).', '(5, -3)', '(9, -5)', '(-11, 3)', '(9/2, -5/2)', 3,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((10+-1)/2, (-4+-1)/2) = (9/2, -5/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (8, -12) and (-20, 14).', '(-6, 2)', '(-6, 1)', '(-5, 1)', '(-14, 13)', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((8+-20)/2, (-12+14)/2) = (-6, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The midpoint of (1, -6) and (-1, 9) lies on which axis?', 'Both axes', 'y-axis', 'x-axis', 'Neither axis', 1,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint x-coordinate = (1+-1)/2 = 0/2 = 0. Since x = 0, the midpoint lies on the y-axis.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the midpoint of the line segment joining (-4, 14) and (-6, -20).', '(-4, -3)', '(-5, -2)', '(-5, -3)', '(-1, -17)', 2,
'lc_hl_coord_geom', 2, 'foundation', 'lc_hl', 'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = ((-4+-6)/2, (14+-20)/2) = (-5, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-2, -3) and (3, -8).', '0', '1', '-2', '-1', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-8--3)/(3--2) = -5/5 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-10, 5) and (-8, 5).', '1', 'undefined', '0', '2', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = 5. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line is vertical''. What type of slope does it have?', 'negative', 'undefined', 'zero', 'positive', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line is vertical, so the slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line falls from left to right''. What type of slope does it have?', 'undefined', 'positive', 'zero', 'negative', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line falls from left to right, so the slope is negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (4, -3) and (7, -9).', '-2', '2', '-3', '-1', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-9--3)/(7-4) = -6/3 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line is vertical''. What type of slope does it have?', 'negative', 'zero', 'undefined', 'positive', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line is vertical, so the slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (4, -2) and (5, -4).', '2', '-3', '-2', '-1', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-4--2)/(5-4) = -2/1 = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (3, 7) and (10, 7).', '0', 'undefined', '7', '1', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = 7. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-6, 8) and (-3, 8).', 'undefined', '0', '1', '3', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = 8. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (4, -2) and (7, -2).', '1', '0', 'undefined', '3', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = -2. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (1, -2) and (4, 13).', '4', '6', '5', '-5', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (13--2)/(4-1) = 15/3 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (4, -3) and (6, -1).', '1', '0', '2', '-1', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-1--3)/(6-4) = 2/2 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-8, -9) and (-3, -9).', 'undefined', '0', '1', '5', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = -9. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (2, 3) and (6, 23).', '6', '5', '-5', '4', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (23-3)/(6-2) = 20/4 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-4, -3) and (-2, 7).', '6', '5', '-5', '4', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (7--3)/(-2--4) = 10/2 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-4, -1) and (-1, -16).', '-6', '-4', '5', '-5', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-16--1)/(-1--4) = -15/3 = -5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line rises from left to right''. What type of slope does it have?', 'positive', 'negative', 'undefined', 'zero', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line rises from left to right, so the slope is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-1, -1) and (3, -13).', '3', '-3', '-4', '-2', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-13--1)/(3--1) = -12/4 = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-4, -10) and (-4, -6).', '0', '1', 'undefined', 'infinity', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = -4. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-10, -1) and (-5, -1).', 'undefined', '0', '1', '5', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = -1. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (6, 5) and (6, 13).', 'undefined', '1', 'infinity', '0', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = 6. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-4, 3) and (-3, 4).', '0', '1', '2', '-1', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (4-3)/(-3--4) = 1/1 = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-1, -3) and (2, -4).', '-3', '-1/3', '0', '1/3', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-4--3)/(2--1) = -1/3 = -1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-4, 3) and (2, 6).', '2/3', '1/2', '-1/2', '2', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (6-3)/(2--4) = 3/6 = 1/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (2, 5) and (5, 6).', '1/3', '2/3', '3', '-1/3', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (6-5)/(5-2) = 1/3 = 1/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line rises from left to right''. What type of slope does it have?', 'undefined', 'positive', 'zero', 'negative', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line rises from left to right, so the slope is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-5, 3) and (0, -12).', '3', '-4', '-2', '-3', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-12-3)/(0--5) = -15/5 = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (3, 1) and (3, 5).', '1', '0', 'infinity', 'undefined', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = 3. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-2, 1) and (1, -3).', '-4/3', '4/3', '-1', '-3/4', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-3-1)/(1--2) = -4/3 = -4/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (0, 1) and (5, 3).', '2/5', '3/5', '5/2', '-2/5', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (3-1)/(5-0) = 2/5 = 2/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line falls from left to right''. What type of slope does it have?', 'undefined', 'zero', 'positive', 'negative', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line falls from left to right, so the slope is negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (3, -4) and (3, 1).', 'undefined', '1', '0', 'infinity', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = 3. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-10, -10) and (-10, -3).', 'infinity', '1', '0', 'undefined', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = -10. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (5, 5) and (9, 0).', '5/4', '-4/5', '-1', '-5/4', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (0-5)/(9-5) = -5/4 = -5/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (4, 4) and (7, -8).', '-4', '-5', '4', '-3', 0,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-8-4)/(7-4) = -12/3 = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-1, -5) and (5, -5).', '6', 'undefined', '0', '1', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = -5. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-5, 9) and (0, 9).', '5', '1', '0', 'undefined', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = 9. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line falls from left to right''. What type of slope does it have?', 'positive', 'zero', 'undefined', 'negative', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line falls from left to right, so the slope is negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (0, 0) and (5, 1).', '2/5', '-1/5', '1/5', '5', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (1-0)/(5-0) = 1/5 = 1/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (3, 1) and (6, 6).', '-5/3', '3/5', '5/3', '2', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (6-1)/(6-3) = 5/3 = 5/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line falls from left to right''. What type of slope does it have?', 'zero', 'negative', 'positive', 'undefined', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line falls from left to right, so the slope is negative.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-1, -8) and (-1, -6).', '1', 'infinity', 'undefined', '0', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = -1. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (3, -4) and (9, -4).', '6', '0', '1', 'undefined', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = -4. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (5, -4) and (5, -1).', '1', 'infinity', 'undefined', '0', 2,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = 5. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-1, -1) and (2, -1).', '3', '0', 'undefined', '1', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = -1. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-2, -10) and (-2, -7).', '1', 'undefined', 'infinity', '0', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have x = -2. This is a vertical line. Slope is undefined.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (3, 8) and (5, 8).', '2', 'undefined', '1', '0', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Both points have y = 8. This is a horizontal line. Slope = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (2, -3) and (5, -6).', '-2', '0', '1', '-1', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-6--3)/(5-2) = -3/3 = -1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A line has the property: ''The line rises from left to right''. What type of slope does it have?', 'zero', 'positive', 'undefined', 'negative', 1,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'The line rises from left to right, so the slope is positive.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the line through (-4, 0) and (2, -5).', '-2/3', '5/6', '-6/5', '-5/6', 3,
'lc_hl_coord_geom', 3, 'foundation', 'lc_hl', 'Slope m = (y₂-y₁)/(x₂-x₁) = (-5-0)/(2--4) = -5/6 = -5/6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-5, -5) with slope -2.', 'y = 2x + -15', 'y = -2x - 15', 'y = -2x + 15', 'y = -2x + -5', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y - y₁ = m(x - x₁): y - -5 = -2(x - -5). Simplifying: y = -2x - 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (2, -5) and (5, -14).', 'y = -3x + 1', 'y = -3x + 2', 'y = 3x + 1', 'y = -2x + 1', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (-14--5)/(5-2) = -9/3 = -3. Using point-slope form: y = -3x + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope 0 and y-intercept 0.', 'y = 0', 'None of these', 'y = 0x - 0', 'y = 0x + 0', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = 0 and c = 0: y = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3x + 4y = -14 to slope-intercept form.', 'y = 3/4x + -7/2', 'None of these', 'y = -3/4x + 7/2', 'y = -3/4x - 7/2', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: 4y = -3x + -14, so y = (-3/4)x + (-14/4) = y = -3/4x - 7/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4x + -4y = -9 to slope-intercept form.', 'y = 1x + -9/4', 'None of these', 'y = -1x + 9/4', 'y = 1x + 9/4', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -4y = -4x + -9, so y = (-4/-4)x + (-9/-4) = y = 1x + 9/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the slope of the line y = 3x + 2?', '2', '3', '-3', '4', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the slope m = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope 2 and y-intercept 6.', 'y = 6x + 2', 'y = 2x + 6', 'y = -2x + 6', 'y = 2x - 6', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = 2 and c = 6: y = 2x + 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2x + -1y = -4 to slope-intercept form.', 'y = -2x + 4', 'None of these', 'y = 2x + 4', 'y = 2x + -4', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -1y = -2x + -4, so y = (-2/-1)x + (-4/-1) = y = 2x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3x + -3y = -10 to slope-intercept form.', 'y = 1x + 10/3', 'None of these', 'y = -1x + 10/3', 'y = 1x + -10/3', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -3y = -3x + -10, so y = (-3/-3)x + (-10/-3) = y = 1x + 10/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope 0 and y-intercept 3.', 'y = 0x + 3', 'y = 0x - 3', 'y = 3', 'y = 3x + 0', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = 0 and c = 3: y = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-4, 4) and (-2, -2).', 'y = 3x + -8', 'y = -3x - 8', 'y = -3x - 7', 'y = -2x + -8', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (-2-4)/(-2--4) = -6/2 = -3. Using point-slope form: y = -3x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of the line y = -3x + 2?', '-2', '2', '-3', '3', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the y-intercept c = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (4, -2) and (7, 7).', 'y = 3x - 14', 'y = 4x + -14', 'y = -3x + -14', 'y = 3x - 13', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (7--2)/(7-4) = 9/3 = 3. Using point-slope form: y = 3x - 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of the line y = -1x + 0?', 'None of these', '1', '-1', '0', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the y-intercept c = 0', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3x + -2y = 5 to slope-intercept form.', 'None of these', 'y = 3/2x - 5/2', 'y = 3/2x + 5/2', 'y = -3/2x + -5/2', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -2y = -3x + 5, so y = (-3/-2)x + (5/-2) = y = 3/2x - 5/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3x + 5y = 4 to slope-intercept form.', 'y = -3/5x + -4/5', 'y = -3/5x + 4/5', 'y = 3/5x + 4/5', 'None of these', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: 5y = -3x + 4, so y = (-3/5)x + (4/5) = y = -3/5x + 4/5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of the line y = 0x + 6?', '6', '-6', '0', '7', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the y-intercept c = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-5, -3) with slope -1.', 'y = 1x + -8', 'y = -1x + 8', 'y = -1x + -3', 'y = -x - 8', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y - y₁ = m(x - x₁): y - -3 = -1(x - -5). Simplifying: y = -x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (0, 2) and (3, 2).', 'y = 0x + 3', 'y = 2', 'y = 1x + 2', 'y = 0x + 2', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (2-2)/(3-0) = 0/3 = 0. Using point-slope form: y = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the slope of the line y = 5x - 2?', '-5', '6', '-2', '5', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the slope m = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-3, -2) and (-1, 4).', 'y = 3x + 8', 'y = 4x + 7', 'y = 3x + 7', 'y = -3x + 7', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (4--2)/(-1--3) = 6/2 = 3. Using point-slope form: y = 3x + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 5x + -4y = 5 to slope-intercept form.', 'y = -5/4x + -5/4', 'y = 5/4x - 5/4', 'y = 5/4x + 5/4', 'None of these', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -4y = -5x + 5, so y = (-5/-4)x + (5/-4) = y = 5/4x - 5/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-2, 3) with slope -3.', 'y = -3x - 3', 'y = 3x + -3', 'y = -3x + 3', 'None of these', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y - y₁ = m(x - x₁): y - 3 = -3(x - -2). Simplifying: y = -3x - 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-5, -3) and (-2, -3).', 'y = 0x + -3', 'y = 0x - 2', 'y = 1x + -3', 'y = -3', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (-3--3)/(-2--5) = 0/3 = 0. Using point-slope form: y = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of the line y = 1x + 9?', '9', '1', '-9', '10', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the y-intercept c = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (1, 5) and (4, -1).', 'y = -2x + 7', 'y = -1x + 7', 'y = -2x + 8', 'y = 2x + 7', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (-1-5)/(4-1) = -6/3 = -2. Using point-slope form: y = -2x + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (0, 5) with slope 4.', 'y = -4x + 5', 'None of these', 'y = 4x + 5', 'y = 4x - 5', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y - y₁ = m(x - x₁): y - 5 = 4(x - 0). Simplifying: y = 4x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope 1 and y-intercept 5.', 'y = 1x - 5', 'y = -1x + 5', 'y = x + 5', 'y = 5x + 1', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = 1 and c = 5: y = x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1x + -4y = 6 to slope-intercept form.', 'y = -1/4x + -3/2', 'y = 1/4x + 3/2', 'y = 1/4x - 3/2', 'None of these', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -4y = -1x + 6, so y = (-1/-4)x + (6/-4) = y = 1/4x - 3/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope 1 and y-intercept -1.', 'y = x - 1', 'y = -1x + -1', 'y = -1x + 1', 'y = 1x + 1', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = 1 and c = -1: y = x - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope 3 and y-intercept -10.', 'y = 3x + 10', 'y = -10x + 3', 'y = -3x + -10', 'y = 3x - 10', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = 3 and c = -10: y = 3x - 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the slope of the line y = -2x + 3?', '-1', '3', '2', '-2', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the slope m = -2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (0, 4) with slope 2.', 'y = 2x - 4', 'None of these', 'y = -2x + 4', 'y = 2x + 4', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y - y₁ = m(x - x₁): y - 4 = 2(x - 0). Simplifying: y = 2x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope 4 and y-intercept 9.', 'y = -4x + 9', 'y = 4x - 9', 'y = 9x + 4', 'y = 4x + 9', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = 4 and c = 9: y = 4x + 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-4, -4) with slope 0.', 'y = -4', 'y = 0x + 4', 'y = 0x + -4', 'None of these', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y - y₁ = m(x - x₁): y - -4 = 0(x - -4). Simplifying: y = -4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope -5 and y-intercept 9.', 'y = 9x + -5', 'y = -5x + 9', 'y = 5x + 9', 'y = -5x - 9', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = -5 and c = 9: y = -5x + 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 4x + -3y = -5 to slope-intercept form.', 'y = 4/3x + -5/3', 'None of these', 'y = 4/3x + 5/3', 'y = -4/3x + 5/3', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -3y = -4x + -5, so y = (-4/-3)x + (-5/-3) = y = 4/3x + 5/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (1, -3) with slope 0.', 'y = -3', 'y = 0x + 3', 'None of these', 'y = 0x + -3', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y - y₁ = m(x - x₁): y - -3 = 0(x - 1). Simplifying: y = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-2, 2) and (2, 10).', 'y = 2x + 7', 'y = 2x + 6', 'y = 3x + 6', 'y = -2x + 6', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (10-2)/(2--2) = 8/4 = 2. Using point-slope form: y = 2x + 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (2, 3) and (3, 4).', 'y = 2x + 1', 'y = -1x + 1', 'y = x + 1', 'y = 1x + 2', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (4-3)/(3-2) = 1/1 = 1. Using point-slope form: y = x + 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 2x + 1y = -1 to slope-intercept form.', 'y = -2x + 1', 'y = 2x + -1', 'None of these', 'y = -2x - 1', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: 1y = -2x + -1, so y = (-2/1)x + (-1/1) = y = -2x - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 1x + -1y = 5 to slope-intercept form.', 'y = 1x - 5', 'y = 1x + 5', 'None of these', 'y = -1x + -5', 0,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: -1y = -1x + 5, so y = (-1/-1)x + (5/-1) = y = 1x - 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope -3 and y-intercept -8.', 'y = -8x + -3', 'y = -3x + 8', 'y = -3x - 8', 'y = 3x + -8', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = -3 and c = -8: y = -3x - 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line with slope -1 and y-intercept -4.', 'y = -4x + -1', 'y = -1x + 4', 'y = -x - 4', 'y = 1x + -4', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Using y = mx + c with m = -1 and c = -4: y = -x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (2, -1) and (5, -7).', 'y = 2x + 3', 'y = -2x + 3', 'y = -1x + 3', 'y = -2x + 4', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (-7--1)/(5-2) = -6/3 = -2. Using point-slope form: y = -2x + 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-3, 0) and (-1, -2).', 'y = 1x + -3', 'y = -1x - 2', 'y = 0x + -3', 'y = -x - 3', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (-2-0)/(-1--3) = -2/2 = -1. Using point-slope form: y = -x - 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the y-intercept of the line y = 2x - 3?', '3', '-3', '2', '-2', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'In y = mx + c form, the y-intercept c = -3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (0, -1) and (4, -5).', 'y = -1x + 0', 'y = 1x + -1', 'y = -x - 1', 'y = 0x + -1', 2,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (-5--1)/(4-0) = -4/4 = -1. Using point-slope form: y = -x - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Convert 3x + 1y = -5 to slope-intercept form.', 'y = 3x + -5', 'y = -3x + 5', 'None of these', 'y = -3x - 5', 3,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Solving for y: 1y = -3x + -5, so y = (-3/1)x + (-5/1) = y = -3x - 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line through (-3, 3) and (-1, 7).', 'y = 2x + 10', 'y = 2x + 9', 'y = 3x + 9', 'y = -2x + 9', 1,
'lc_hl_coord_geom', 4, 'developing', 'lc_hl', 'Slope m = (7-3)/(-1--3) = 4/2 = 2. Using point-slope form: y = 2x + 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = -3x - 3 passing through (0, -4).', 'y = -1/3x + -4', 'y = -3x + -4', 'y = 1/3x - 4', 'y = 1/3x + -4', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/-3 = 1/3. Using point (0, -4): y = 1/3x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = -5x - 4 and y = -5x - 9 parallel, perpendicular, or neither?', 'Neither', 'Perpendicular', 'Parallel', 'Coincident', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope -5. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 2x + 4 and y = -1/2x + 3 parallel, perpendicular, or neither?', 'Neither', 'Parallel', 'Coincident', 'Perpendicular', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 2. Slope of line 2 = -1/2. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line parallel to y = 2x - 5 passing through (-2, 0).', 'y = 3x + 4', 'y = 2x + -5', 'y = -2x + 4', 'y = 2x + 4', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Parallel lines have same slope. m = 2. Using point (-2, 0): c = 0 - 2(-2) = 4. Line: y = 2x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 5x - 4 and y = -1/5x - 5 parallel, perpendicular, or neither?', 'Perpendicular', 'Neither', 'Coincident', 'Parallel', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 5. Slope of line 2 = -1/5. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 5x - 2 and y = 5x - 5 parallel, perpendicular, or neither?', 'Neither', 'Perpendicular', 'Coincident', 'Parallel', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 5. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 1x + 3 and y = -1x - 2 parallel, perpendicular, or neither?', 'Coincident', 'Neither', 'Perpendicular', 'Parallel', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 1. Slope of line 2 = -1. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular lines have slopes that...', 'are equal', 'add to 0', 'multiply to 1', 'multiply to -1', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is multiply to -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallel lines have...', 'slopes that multiply to -1', 'zero slopes', 'equal slopes', 'opposite slopes', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is equal slopes.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = 4x + 1 passing through (4, 4).', 'y = -1/4x + 5', 'y = -1/4x + 4', 'y = 4x + 5', 'y = 1/4x + 5', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/4 = -1/4. Using point (4, 4): y = -1/4x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 3x + 0 and y = -1/3x + 0 parallel, perpendicular, or neither?', 'Parallel', 'Coincident', 'Perpendicular', 'Neither', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 3. Slope of line 2 = -1/3. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line parallel to y = 1x + 0 passing through (-4, 3).', 'y = 1x + 7', 'y = 2x + 7', 'y = -1x + 7', 'y = 1x + 0', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Parallel lines have same slope. m = 1. Using point (-4, 3): c = 3 - 1(-4) = 7. Line: y = 1x + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = 3x + 2 passing through (-4, 5).', 'y = -1/3x + 5', 'y = 1/3x + 11/3', 'y = 3x + 11/3', 'y = -1/3x + 11/3', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/3 = -1/3. Using point (-4, 5): y = -1/3x + 11/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = -1x - 1 and y = -1x + 4 parallel, perpendicular, or neither?', 'Coincident', 'Perpendicular', 'Parallel', 'Neither', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope -1. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular lines have slopes that...', 'multiply to -1', 'multiply to 1', 'add to 0', 'are equal', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is multiply to -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 3x + 5 and y = -1/3x - 1 parallel, perpendicular, or neither?', 'Parallel', 'Perpendicular', 'Neither', 'Coincident', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 3. Slope of line 2 = -1/3. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The slope of a line perpendicular to y = 3x + 1 is...', '-1/3', '-3', '1/3', '3', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is -1/3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The slope of a line parallel to y = -2x + 5 is...', '2', '1/2', '-1/2', '-2', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is -2.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The slope of a line perpendicular to y = 3x + 1 is...', '-3', '1/3', '-1/3', '3', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is -1/3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = -2x - 8 and y = -2x - 9 parallel, perpendicular, or neither?', 'Coincident', 'Perpendicular', 'Parallel', 'Neither', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope -2. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = -1x + 3 passing through (0, -3).', 'None of these', 'y = 1x + -3', 'y = 1x - 3', 'y = -1x + -3', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/-1 = 1. Using point (0, -3): y = 1x - 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = 1x - 4 passing through (4, 3).', 'y = -1x + 7', 'y = 1x + 7', 'y = -1x + 3', 'None of these', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/1 = -1. Using point (4, 3): y = -1x + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line parallel to y = 2x + 0 passing through (-1, -3).', 'y = -2x - 1', 'y = 3x + -1', 'y = 2x - 1', 'y = 2x + 0', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Parallel lines have same slope. m = 2. Using point (-1, -3): c = -3 - 2(-1) = -1. Line: y = 2x - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The slope of a line perpendicular to y = 3x + 1 is...', '1/3', '3', '-1/3', '-3', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is -1/3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line parallel to y = -2x + 4 passing through (0, 2).', 'y = -2x + 2', 'y = -1x + 2', 'y = -2x + 4', 'y = 2x + 2', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Parallel lines have same slope. m = -2. Using point (0, 2): c = 2 - -2(0) = 2. Line: y = -2x + 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallel lines have...', 'equal slopes', 'slopes that multiply to -1', 'zero slopes', 'opposite slopes', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is equal slopes.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = 1x + 0 passing through (0, 5).', 'y = 1x + 5', 'None of these', 'None of these', 'y = -1x + 5', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/1 = -1. Using point (0, 5): y = -1x + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = -1x + 4 passing through (-4, 0).', 'y = 1x + 0', 'None of these', 'y = 1x + 4', 'y = -1x + 4', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/-1 = 1. Using point (-4, 0): y = 1x + 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 1x + 0 and y = -1x - 5 parallel, perpendicular, or neither?', 'Perpendicular', 'Coincident', 'Neither', 'Parallel', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 1. Slope of line 2 = -1. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 4x + 0 and y = -1/4x + 0 parallel, perpendicular, or neither?', 'Parallel', 'Perpendicular', 'Coincident', 'Neither', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 4. Slope of line 2 = -1/4. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = -1x - 8 and y = -1x - 9 parallel, perpendicular, or neither?', 'Neither', 'Parallel', 'Perpendicular', 'Coincident', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope -1. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 4x + 9 and y = 4x + 6 parallel, perpendicular, or neither?', 'Parallel', 'Perpendicular', 'Neither', 'Coincident', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 4. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 1x - 8 and y = 1x - 10 parallel, perpendicular, or neither?', 'Neither', 'Parallel', 'Perpendicular', 'Coincident', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 1. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallel lines have...', 'slopes that multiply to -1', 'equal slopes', 'zero slopes', 'opposite slopes', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is equal slopes.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line parallel to y = -1x + 1 passing through (0, -4).', 'y = -1x - 4', 'y = 0x + -4', 'y = 1x - 4', 'y = -1x + 1', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Parallel lines have same slope. m = -1. Using point (0, -4): c = -4 - -1(0) = -4. Line: y = -1x - 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 4x - 5 and y = -1/4x - 2 parallel, perpendicular, or neither?', 'Parallel', 'Neither', 'Perpendicular', 'Coincident', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 4. Slope of line 2 = -1/4. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular lines have slopes that...', 'add to 0', 'are equal', 'multiply to -1', 'multiply to 1', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is multiply to -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular lines have slopes that...', 'add to 0', 'multiply to -1', 'are equal', 'multiply to 1', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'The answer is multiply to -1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = -4x + 5 passing through (3, -4).', 'y = -4x + -19/4', 'y = 1/4x + -4', 'y = 1/4x - 19/4', 'y = -1/4x + -19/4', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/-4 = 1/4. Using point (3, -4): y = 1/4x - 19/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = -3x - 1 passing through (4, 3).', 'y = -1/3x + 5/3', 'y = 1/3x + 5/3', 'y = 1/3x + 3', 'y = -3x + 5/3', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/-3 = 1/3. Using point (4, 3): y = 1/3x + 5/3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 5x + 4 and y = -1/5x - 4 parallel, perpendicular, or neither?', 'Parallel', 'Coincident', 'Perpendicular', 'Neither', 2,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 5. Slope of line 2 = -1/5. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 2x + 9 and y = 2x + 8 parallel, perpendicular, or neither?', 'Parallel', 'Perpendicular', 'Neither', 'Coincident', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 2. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 1x + 9 and y = 1x + 5 parallel, perpendicular, or neither?', 'Parallel', 'Neither', 'Perpendicular', 'Coincident', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 1. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = -4x - 2 and y = -4x - 7 parallel, perpendicular, or neither?', 'Parallel', 'Coincident', 'Perpendicular', 'Neither', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope -4. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 4x + 4 and y = 4x + 2 parallel, perpendicular, or neither?', 'Perpendicular', 'Parallel', 'Neither', 'Coincident', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 4. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 1x + 4 and y = 1x + 9 parallel, perpendicular, or neither?', 'Perpendicular', 'Parallel', 'Coincident', 'Neither', 1,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 1. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line perpendicular to y = -1x + 0 passing through (-5, 5).', 'y = 1x + 10', 'y = 1x + 5', 'None of these', 'y = -1x + 10', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Perpendicular slope = -1/-1 = 1. Using point (-5, 5): y = 1x + 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 4x - 10 and y = 4x - 14 parallel, perpendicular, or neither?', 'Coincident', 'Perpendicular', 'Neither', 'Parallel', 3,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Both lines have slope 4. Since slopes are equal but y-intercepts differ, they are parallel.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the line parallel to y = 2x + 1 passing through (-1, -3).', 'y = 2x - 1', 'y = 3x + -1', 'y = -2x - 1', 'y = 2x + 1', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Parallel lines have same slope. m = 2. Using point (-1, -3): c = -3 - 2(-1) = -1. Line: y = 2x - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the lines y = 5x - 2 and y = -1/5x - 3 parallel, perpendicular, or neither?', 'Perpendicular', 'Parallel', 'Neither', 'Coincident', 0,
'lc_hl_coord_geom', 5, 'developing', 'lc_hl', 'Slope of line 1 = 5. Slope of line 2 = -1/5. Product = -1. Lines are perpendicular.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (12, 7) divides the segment from (4, -3) to (24, 22) in what ratio?', '2:4', '2:3', '3:3', '3:2', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 2:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(6, 3) to B(15, 9) that is closer to B.', '(12, 5)', '(9, 7)', '(10, 6)', '(12, 7)', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to B divides in ratio 2:1. P = (12, 7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (2, 4) to (3, 0) externally in the ratio 4:2.', '(4, -5)', '(4, -4)', '(8/3, 4/3)', '(5, -4)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (4, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(5, -3) to B(14, 3) that is closer to A.', '(8, 1)', '(11, -1)', '(9, 0)', '(8, -1)', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (8, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (2, 6) to (-3, 6) in the ratio 2:4.', '(-4/3, 6)', '(4/3, 6)', '(1/3, 7)', '(1/3, 6)', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (1/3, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(5, -3) to B(14, 3) that is closer to B.', '(11, 1)', '(9, 0)', '(11, -1)', '(8, 1)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to B divides in ratio 2:1. P = (11, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(-3, -4) to B(6, 2) that is closer to B.', '(0, 0)', '(3, -2)', '(1, -1)', '(3, 0)', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to B divides in ratio 2:1. P = (3, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (3, -6) to (-4, -2) in the ratio 2:4.', '(5/3, -14/3)', '(2/3, -14/3)', '(-5/3, -10/3)', '(2/3, -11/3)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (2/3, -14/3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (-1, 6) to (-4, 2) in the ratio 1:4.', '(-17/5, 14/5)', '(-3/5, 26/5)', '(-8/5, 26/5)', '(-8/5, 31/5)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (-8/5, 26/5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (2, -2) to (-1, -2) externally in the ratio 2:1.', '(0, -2)', '(-4, -2)', '(-4, -3)', '(-3, -2)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-4, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(5, 3) to B(14, 9) that is closer to A.', '(8, 5)', '(11, 5)', '(8, 7)', '(9, 6)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (8, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (1, 1) to (0, -3) in the ratio 2:2.', '(3/2, -1)', 'None of these', '(1/2, -1)', '(1/2, 0)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (1/2, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (-1, 9) divides the segment from (-3, 5) to (3, 17) in what ratio?', '1:3', '2:2', '1:2', '2:1', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 1:2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (13, 15) divides the segment from (-2, 0) to (23, 25) in what ratio?', '3:2', '4:2', '2:3', '3:3', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 3:2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (7, 9) divides the segment from (-3, 3) to (22, 18) in what ratio?', '2:4', '2:3', '3:3', '3:2', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 2:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (4, 0) to (4, -4) externally in the ratio 4:3.', '(4, -16)', '(5, -16)', '(4, -16/7)', '(4, -17)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (4, -16)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (6, -6) to (6, 3) in the ratio 2:2.', '(6, -3/2)', 'None of these', '(7, -3/2)', '(6, -1/2)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (6, -3/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (14, 16) divides the segment from (2, -4) to (23, 31) in what ratio?', '5:3', '4:3', '3:4', '4:4', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 4:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (0, -1) to (-1, -3) externally in the ratio 4:3.', '(-4, -9)', '(-4/7, -15/7)', '(-3, -9)', '(-4, -10)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-4, -9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (4, 3) to (-4, 4) externally in the ratio 3:1.', '(-8, 9/2)', '(-7, 9/2)', '(-8, 7/2)', '(-2, 15/4)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-8, 9/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(-1, -3) to B(8, 3) that is closer to A.', '(3, 0)', '(2, 1)', '(2, -1)', '(5, -1)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (2, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(-3, -3) to B(6, 3) that is closer to A.', '(0, -1)', '(1, 0)', '(3, -1)', '(0, 1)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (0, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (16, 16) divides the segment from (4, -4) to (19, 21) in what ratio?', '4:2', '4:1', '1:4', '5:1', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 4:1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (14, 15) divides the segment from (-2, 3) to (26, 24) in what ratio?', '4:4', '4:3', '3:4', '5:3', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 4:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (10, 13) divides the segment from (2, 5) to (16, 19) in what ratio?', '4:4', '3:4', '4:3', '5:3', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 4:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (-2, -4) to (-2, 1) externally in the ratio 2:1.', '(-2, 6)', '(-2, -2/3)', '(-1, 6)', '(-2, 5)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-2, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (2, 4) to (1, 4) externally in the ratio 3:1.', '(3/2, 4)', '(5/4, 4)', '(1/2, 4)', '(1/2, 3)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (1/2, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(5, 1) to B(14, 7) that is closer to A.', '(8, 3)', '(9, 4)', '(8, 5)', '(11, 3)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (8, 3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (2, 5) to (5, 6) in the ratio 1:3.', '(11/4, 25/4)', '(11/4, 21/4)', '(17/4, 23/4)', '(15/4, 21/4)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (11/4, 21/4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (1, -2) to (-4, -4) externally in the ratio 3:2.', '(-13, -8)', '(-2, -16/5)', '(-14, -9)', '(-14, -8)', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-14, -8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (-1, -2) divides the segment from (-4, -4) to (8, 4) in what ratio?', '1:3', '2:3', '1:4', '3:1', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 1:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (1, 4) divides the segment from (-5, -4) to (4, 8) in what ratio?', '2:1', '1:2', '2:2', '3:1', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 2:1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(6, 5) to B(15, 11) that is closer to B.', '(10, 8)', '(12, 7)', '(12, 9)', '(9, 9)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to B divides in ratio 2:1. P = (12, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (4, -2) to (-2, -4) externally in the ratio 2:1.', '(-8, -6)', '(-7, -6)', '(-8, -7)', '(0, -10/3)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-8, -6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(2, 0) to B(11, 6) that is closer to A.', '(8, 2)', '(5, 2)', '(5, 4)', '(6, 3)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (5, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(-2, -6) to B(7, 0) that is closer to A.', '(2, -3)', '(1, -4)', '(4, -4)', '(1, -2)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (1, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(4, -2) to B(13, 4) that is closer to B.', '(8, 1)', '(7, 2)', '(10, 2)', '(10, 0)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to B divides in ratio 2:1. P = (10, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (10, 19) divides the segment from (4, 4) to (14, 29) in what ratio?', '4:2', '3:3', '3:2', '2:3', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 3:2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(-2, -4) to B(7, 2) that is closer to A.', '(4, -2)', '(2, -1)', '(1, -2)', '(1, 0)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (1, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (1, 2) to (-1, -3) in the ratio 4:1.', '(2/5, -2)', '(-3/5, -2)', '(-3/5, -1)', '(3/5, 1)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (-3/5, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (0, 2) to (-3, 3) externally in the ratio 3:1.', '(-9/2, 5/2)', '(-7/2, 7/2)', '(-9/4, 11/4)', '(-9/2, 7/2)', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-9/2, 7/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (-4, -3) to (-4, 3) externally in the ratio 2:1.', '(-3, 9)', '(-4, 9)', '(-4, 8)', '(-4, 1)', 1,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-4, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (1, 5) divides the segment from (-5, -3) to (10, 17) in what ratio?', '3:2', '2:4', '3:3', '2:3', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 2:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (7, 20) divides the segment from (-1, 4) to (13, 32) in what ratio?', '4:4', '3:4', '5:3', '4:3', 3,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 4:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(4, -6) to B(13, 0) that is closer to B.', '(8, -3)', '(7, -2)', '(10, -2)', '(10, -4)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to B divides in ratio 2:1. P = (10, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (0, -2) to (4, -5) in the ratio 3:3.', '(3, -7/2)', '(2, -5/2)', '(2, -7/2)', 'None of these', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = (2, -7/2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the point that divides the segment from (0, -3) to (-3, 1) externally in the ratio 4:3.', '(-12/7, -5/7)', '(-12, 12)', '(-12, 13)', '(-11, 13)', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = (-12, 13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (11, 8) divides the segment from (1, 4) to (26, 14) in what ratio?', '3:3', '2:4', '2:3', '3:2', 2,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 2:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the trisection point of segment from A(5, -5) to B(14, 1) that is closer to A.', '(8, -3)', '(11, -3)', '(8, -1)', '(9, -2)', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Trisection point closer to A divides in ratio 1:2. P = (8, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Point (3, 9) divides the segment from (-1, 3) to (9, 18) in what ratio?', '2:3', '3:3', '3:2', '2:4', 0,
'lc_hl_coord_geom', 6, 'developing', 'lc_hl', 'Using the section formula backwards, the ratio is 2:3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-2, 1), B(0, -2), and C(0, 0).', '4', '1', '3', '2', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|4| = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(4, 7), and Q(-5, 8).', '67/2', '35', 'None of these', '67', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|67| = 67/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (3, 0), (5, 5), (0, 4) in order.', '34', '15', '17', '19', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 17 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(3, -5), B(6, -11), and C(10, -16) collinear?', 'No, they are not collinear', 'Cannot be determined', 'Yes, they are collinear', 'Only two are collinear', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'The area of the triangle is non-zero, so the points are not collinear.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (6, 0), (6, 6), (0, 3) in order.', '29', '25', '27', '54', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 27 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(0, -5), B(1, 2), and C(-5, 2).', '20', '42', '21', '22', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|42| = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (5, 0), (3, 5), (0, 3) in order.', '34', '17', '19', '15', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 17 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-3, 3), B(-5, 0), and C(3, 0).', '12', '13', '24', '11', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|24| = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(3, 8), and Q(-1, 5).', '15', '13', '23/2', '23', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|23| = 23/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-1, -4), B(5, -5), and C(-3, 2).', '17', '34', '16', '18', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|34| = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-5, 4), B(0, 1), and C(-4, 5).', '8', '5', '4', '3', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|8| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(5, 4), and Q(-6, 5).', '49', '49/2', '26', 'None of these', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|49| = 49/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (3, 0), (3, 4), (0, 5) in order.', '15', '13', '26', '11', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 13 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(2, 5), B(3, -1), and C(0, 2).', '17/2', '9', '15', '15/2', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|15| = 15/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(8, 1), and Q(-5, 5).', '17', '45', '45/2', '24', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|45| = 45/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(3, 4), B(0, -4), and C(-3, -4).', '24', '13', '12', '11', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|24| = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (4, 0), (5, 5), (0, 4) in order.', '18', '20', '22', '40', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 20 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(1, 2), B(5, 6), and C(8, 9) collinear?', 'Yes, they are collinear', 'Only two are collinear', 'Cannot be determined', 'No, they are not collinear', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = 0 when points are collinear. All three points lie on line with slope 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(2, 2), B(-5, 0), and C(0, -2).', '11', '24', '12', '13', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|24| = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(5, 1), and Q(-4, 5).', '29', '13', '16', '29/2', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|29| = 29/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(6, 7), and Q(-6, 7).', '42', '43', '84', '44', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|84| = 42', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(6, 1), and Q(-8, 1).', '14', '7', '8', '9', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|14| = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(2, 3), and Q(-4, 8).', '14', '28', '16', '20', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|28| = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (4, 0), (3, 6), (0, 6) in order.', '19', '42', '23', '21', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 21 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (3, 0), (4, 4), (0, 4) in order.', '16', '28', '14', '12', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 14 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(0, -5), B(-3, -4), and C(0, 0).', '15', '17/2', '15/2', '9', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|15| = 15/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(1, 3), B(5, 15), and C(6, 20) collinear?', 'Cannot be determined', 'Yes, they are collinear', 'Only two are collinear', 'No, they are not collinear', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'The area of the triangle is non-zero, so the points are not collinear.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(5, 2), and Q(-3, 5).', '31/2', '31', '17', '13', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|31| = 31/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (5, 0), (3, 5), (0, 3) in order.', '19', '17', '15', '34', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 17 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(3, 5), B(-3, -1), and C(0, -3).', '16', '30', '14', '15', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|30| = 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(8, 4), and Q(-3, 6).', '32', '26', '30', '60', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|60| = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (3, 0), (6, 6), (0, 5) in order.', '26', '22', '48', '24', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 24 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (3, 0), (6, 3), (0, 3) in order.', '26', '11', '13', '15', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 13 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-2, -1), B(4, -3), and C(3, -1).', '4', '5', '10', '6', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|10| = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(0, -1), B(5, -4), and C(5, -1).', '9', '17/2', '15', '15/2', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|15| = 15/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-3, 3), B(4, -1), and C(5, 5).', '24', '46', '23', '22', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|46| = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(-2, 0), B(2, 0), and C(3, 1) collinear?', 'No, they are not collinear', 'Cannot be determined', 'Only two are collinear', 'Yes, they are collinear', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'The area of the triangle is non-zero, so the points are not collinear.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (5, 0), (6, 3), (0, 5) in order.', '24', '44', '20', '22', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 22 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(1, 5), B(2, 7), and C(5, 15) collinear?', 'Yes, they are collinear', 'Cannot be determined', 'No, they are not collinear', 'Only two are collinear', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'The area of the triangle is non-zero, so the points are not collinear.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(4, 8), and Q(-4, 7).', '60', '30', '31', '32', 1,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|60| = 30', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (3, 0), (3, 5), (0, 4) in order.', '13', '26', '15', '11', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 13 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(-3, 3), B(-1, 5), and C(3, 9) collinear?', 'Only two are collinear', 'No, they are not collinear', 'Yes, they are collinear', 'Cannot be determined', 2,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = 0 when points are collinear. All three points lie on line with slope 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(3, 4), B(-2, -1), and C(5, 5).', '5/2', '4', '7/2', '5', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|5| = 5/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(-2, 0), B(2, 4), and C(5, 7) collinear?', 'Yes, they are collinear', 'No, they are not collinear', 'Only two are collinear', 'Cannot be determined', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = 0 when points are collinear. All three points lie on line with slope 1.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the quadrilateral with vertices (0, 0), (3, 0), (4, 6), (0, 3) in order.', '15', '17', '30', '13', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Using the shoelace formula for the quadrilateral, Area = 15 square units.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-3, -4), B(-2, -4), and C(2, 4).', '4', '5', '3', '8', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|8| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are the points A(-5, -2), B(-1, -10), and C(3, -15) collinear?', 'No, they are not collinear', 'Yes, they are collinear', 'Only two are collinear', 'Cannot be determined', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'The area of the triangle is non-zero, so the points are not collinear.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(1, -4), B(-5, 3), and C(4, 5).', '77/2', '75', '39', '75/2', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|75| = 75/2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices O(0, 0), P(8, 4), and Q(-1, 2).', '10', '18', '20', '12', 0,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|20| = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the area of the triangle with vertices A(-3, 0), B(3, 2), and C(-1, 2).', '3', '8', '5', '4', 3,
'lc_hl_coord_geom', 7, 'proficient', 'lc_hl', 'Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|8| = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (2, 3) and passes through the origin. What is r²?', '26', '14', '12', '13', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(2² + 3²) = √13. So r² = 13.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre of the circle (x + 2)² + (y + 1)² = 36.', '(-2, -1)', '(-2, 1)', '(2, 1)', '(2, -1)', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², the centre is (h, k) = (-2, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is the point (2, 3) inside, on, or outside the circle with centre (-1, 3) and radius 6?', 'Cannot determine', 'Outside', 'On', 'Inside', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance² from point to centre = (2--1)² + (3-3)² = 9. r² = 36. Point is inside.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (0, 4) and radius 2.', '(x + 0)² + (y + 4)² = 4', 'x² + (y - 4)² = 4', 'x² + y² = 20', 'x² + y² = 2', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (0, 4) and r = 2: x² + (y - 4)² = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (-1, -1) and radius 6.', 'None of these', '(x + -1)² + (y + -1)² = 36', 'x² + y² = 38', 'x² + y² = 6', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (-1, -1) and r = 6: (x + -1)² + (y + -1)² = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (3, -5) and passes through the origin. What is r²?', '35', '34', '68', '33', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(3² + -5²) = √34. So r² = 34.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (2, 2) and passes through the origin. What is r²?', '16', '7', '9', '8', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(2² + 2²) = √8. So r² = 8.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (-4, -3) and passes through the origin. What is r²?', '50', '24', '26', '25', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(-4² + -3²) = √25. So r² = 25.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre of the circle (x - 2)² + (y - 1)² = 9.', '(2, -1)', '(-2, 1)', '(-2, -1)', '(2, 1)', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², the centre is (h, k) = (2, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 2x - 6y + 6 = 0.', 'Centre (1, -3), radius 2', 'Centre (-1, 3), radius 4', 'Centre (-1, 3), radius 2', 'Centre (2, -6), radius 2', 2,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (-1, 3), r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (-1, -3) and passes through the origin. What is r²?', '9', '10', '11', '20', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(-1² + -3²) = √10. So r² = 10.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is the point (9, 3) inside, on, or outside the circle with centre (0, 2) and radius 6?', 'Cannot determine', 'Inside', 'Outside', 'On', 2,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance² from point to centre = (9-0)² + (3-2)² = 82. r² = 36. Point is outside.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the radius of the circle (x - 4)² + (y + 1)² = 16.', '4', '16', '5', '3', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², r² = 16, so r = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre of the circle x² + (y + 3)² = 49.', 'None of these', 'None of these', '(0, -3)', '(0, 3)', 2,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², the centre is (h, k) = (0, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² - 6x - 8y + 9 = 0.', 'Centre (-6, -8), radius 4', 'Centre (-3, -4), radius 4', 'Centre (3, 4), radius 4', 'Centre (3, 4), radius 16', 2,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (3, 4), r = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (-1, -5) and passes through the origin. What is r²?', '52', '26', '27', '25', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(-1² + -5²) = √26. So r² = 26.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the radius of the circle (x - 5)² + (y - 3)² = 4.', '3', '2', '4', '1', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², r² = 4, so r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the radius of the circle (x + 2)² + (y + 2)² = 25.', '4', '6', '25', '5', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², r² = 25, so r = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (4, -5) and radius 6.', '(x - 4)² + (y + -5)² = 36', 'x² + y² = 77', '(x + 4)² + (y + -5)² = 36', 'x² + y² = 6', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (4, -5) and r = 6: (x - 4)² + (y + -5)² = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (1, -3) and radius 7.', 'x² + y² = 59', '(x + 1)² + (y + -3)² = 49', 'x² + y² = 7', '(x - 1)² + (y + -3)² = 49', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (1, -3) and r = 7: (x - 1)² + (y + -3)² = 49', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is the point (-2, -2) inside, on, or outside the circle with centre (-2, -2) and radius 5?', 'On', 'Inside', 'Cannot determine', 'Outside', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance² from point to centre = (-2--2)² + (-2--2)² = 0. r² = 25. Point is inside.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre of the circle (x - 2)² + (y + 5)² = 49.', '(2, 5)', '(-2, -5)', '(-2, 5)', '(2, -5)', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², the centre is (h, k) = (2, -5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre of the circle (x + 1)² + (y + 3)² = 25.', '(-1, -3)', '(-1, 3)', '(1, 3)', '(1, -3)', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², the centre is (h, k) = (-1, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (0, -4) and radius 1.', 'x² + (y + -4)² = 1', 'x² + y² = 17', 'x² + y² = 1', '(x + 0)² + (y + -4)² = 1', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (0, -4) and r = 1: x² + (y + -4)² = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (4, -2) and passes through the origin. What is r²?', '21', '40', '19', '20', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(4² + -2²) = √20. So r² = 20.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (0, 1) and radius 1.', '(x + 0)² + (y + 1)² = 1', 'x² + y² = 1', 'x² + (y - 1)² = 1', 'x² + y² = 2', 2,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (0, 1) and r = 1: x² + (y - 1)² = 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is the point (5, -3) inside, on, or outside the circle with centre (1, -3) and radius 4?', 'Cannot determine', 'Outside', 'On', 'Inside', 2,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance² from point to centre = (5-1)² + (-3--3)² = 16. r² = 16. Point is on.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (4, -4) and passes through the origin. What is r²?', '32', '64', '31', '33', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(4² + -4²) = √32. So r² = 32.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre of the circle (x + 1)² + (y - 4)² = 9.', '(-1, 4)', '(1, 4)', '(1, -4)', '(-1, -4)', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², the centre is (h, k) = (-1, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is the point (5, -2) inside, on, or outside the circle with centre (2, -2) and radius 3?', 'Inside', 'Outside', 'Cannot determine', 'On', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance² from point to centre = (5-2)² + (-2--2)² = 9. r² = 9. Point is on.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the radius of the circle (x - 5)² + (y + 3)² = 16.', '5', '4', '3', '16', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², r² = 16, so r = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 6x - 4y - 3 = 0.', 'Centre (6, -4), radius 4', 'Centre (-3, 2), radius 4', 'Centre (-3, 2), radius 16', 'Centre (3, -2), radius 4', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (-3, 2), r = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 8x  = 0.', 'Centre (8, 0), radius 4', 'Centre (4, 0), radius 4', 'Centre (-4, 0), radius 4', 'Centre (-4, 0), radius 16', 2,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (-4, 0), r = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (-1, 3) and passes through the origin. What is r²?', '10', '9', '20', '11', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(-1² + 3²) = √10. So r² = 10.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the radius of the circle x² + (y + 3)² = 9.', '2', '9', '4', '3', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², r² = 9, so r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 4x - 2y - 11 = 0.', 'Centre (-2, 1), radius 4', 'Centre (-2, 1), radius 16', 'Centre (2, -1), radius 4', 'Centre (4, -2), radius 4', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (-2, 1), r = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre of the circle (x + 3)² + (y + 2)² = 36.', '(3, -2)', '(-3, -2)', '(-3, 2)', '(3, 2)', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'From (x-h)² + (y-k)² = r², the centre is (h, k) = (-3, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² - 8y + 7 = 0.', 'Centre (0, 4), radius 3', 'Centre (0, 4), radius 9', 'Centre (0, -4), radius 3', 'Centre (0, -8), radius 3', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (0, 4), r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 4x - 8y + 16 = 0.', 'Centre (-2, 4), radius 2', 'Centre (-2, 4), radius 4', 'Centre (2, -4), radius 2', 'Centre (4, -8), radius 2', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (-2, 4), r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² - 8x + 2y + 8 = 0.', 'Centre (4, -1), radius 3', 'Centre (4, -1), radius 9', 'Centre (-8, 2), radius 3', 'Centre (-4, 1), radius 3', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (4, -1), r = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (-5, -4) and radius 4.', '(x + -5)² + (y + -4)² = 16', 'x² + y² = 57', 'None of these', 'x² + y² = 4', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (-5, -4) and r = 4: (x + -5)² + (y + -4)² = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (2, 2) and radius 5.', 'x² + y² = 33', '(x - 2)² + (y - 2)² = 25', '(x + 2)² + (y + 2)² = 25', 'x² + y² = 5', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (2, 2) and r = 5: (x - 2)² + (y - 2)² = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² - 4x + 4y + 4 = 0.', 'Centre (-2, 2), radius 2', 'Centre (2, -2), radius 2', 'Centre (2, -2), radius 4', 'Centre (-4, 4), radius 2', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (2, -2), r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is the point (7, 0) inside, on, or outside the circle with centre (-1, -1) and radius 5?', 'Outside', 'Cannot determine', 'On', 'Inside', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance² from point to centre = (7--1)² + (0--1)² = 65. r² = 25. Point is outside.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 4y - 12 = 0.', 'Centre (0, -2), radius 4', 'Centre (0, -2), radius 16', 'Centre (0, 2), radius 4', 'Centre (0, 4), radius 4', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (0, -2), r = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (-5, 5) and passes through the origin. What is r²?', '49', '50', '51', '100', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(-5² + 5²) = √50. So r² = 50.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A circle has centre (4, 1) and passes through the origin. What is r²?', '18', '34', '16', '17', 3,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Distance from centre to origin = √(4² + 1²) = √17. So r² = 17.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 4y = 0.', 'Centre (0, -2), radius 2', 'Centre (0, 2), radius 2', 'Centre (0, -2), radius 4', 'Centre (0, 4), radius 2', 0,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (0, -2), r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the circle with centre (-4, 0) and radius 3.', '(x + -4)² + (y + 0)² = 9', '(x + -4)² + y² = 9', 'x² + y² = 3', 'x² + y² = 25', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Circle equation: (x-h)² + (y-k)² = r². With centre (-4, 0) and r = 3: (x + -4)² + y² = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centre and radius of the circle x² + y² + 2x + 6y + 6 = 0.', 'Centre (1, 3), radius 2', 'Centre (-1, -3), radius 2', 'Centre (-1, -3), radius 4', 'Centre (2, 6), radius 2', 1,
'lc_hl_coord_geom', 8, 'proficient', 'lc_hl', 'Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = (-1, -3), r = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the length of the tangent from point (6, 0) to the circle x² + y² = 16.', '2√5', '2', '10', '2√13', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Distance from point to centre = 6. Tangent length = √(d² - r²) = √(6² - 4²) = √20 = 2√5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = -1x + c tangent to the circle x² + y² = 16?', 'c = ±4', 'c = ±16', 'c = ±√17', 'c = ±√32', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 16(1 + 1) = 32. So c = ±√32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 0x + c tangent to the circle x² + y² = 9?', 'None of these', 'c = ±9', 'c = ±√9', 'c = ±3', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 9(1 + 0) = 9. So c = ±3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 100 at the point (8, 6).', '8x + 6y = 100', '8x - 6y = 100', '8x + 6y = 10', '6x + 8y = 100', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (8, 6) on x² + y² = 100 is: 8x + 6y = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 0x + c tangent to the circle x² + y² = 9?', 'None of these', 'c = ±√9', 'c = ±3', 'c = ±9', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 9(1 + 0) = 9. So c = ±3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the length of the tangent from point (7, 0) to the circle x² + y² = 9.', '4', '√58', '10', '2√10', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Distance from point to centre = 7. Tangent length = √(d² - r²) = √(7² - 3²) = √40 = 2√10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 3x + c tangent to the circle x² + y² = 25?', 'c = ±25', 'c = ±√250', 'c = ±√34', 'c = ±5', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 25(1 + 9) = 250. So c = ±√250', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 0x + c tangent to the circle x² + y² = 16?', 'c = ±16', 'c = ±4', 'c = ±√16', 'None of these', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 16(1 + 0) = 16. So c = ±4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the length of the tangent from point (8, 0) to the circle x² + y² = 36.', '10', '2√7', '14', '2', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Distance from point to centre = 8. Tangent length = √(d² - r²) = √(8² - 6²) = √28 = 2√7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = -1x + c tangent to the circle x² + y² = 16?', 'c = ±16', 'c = ±√32', 'c = ±√17', 'c = ±4', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 16(1 + 1) = 32. So c = ±√32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 25 at the point (5, 0).', '5x - 0y = 25', '0x + 5y = 25', 'x = 5', '5x + 0y = 5', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'At point (5, 0) on circle x² + y² = 25, tangent is vertical: x = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 25 at the point (3, 4).', '3x + 4y = 25', '3x + 4y = 5', '3x - 4y = 25', '4x + 3y = 25', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (3, 4) on x² + y² = 25 is: 3x + 4y = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 2x + c tangent to the circle x² + y² = 16?', 'c = ±√80', 'c = ±4', 'c = ±16', 'c = ±√20', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 16(1 + 4) = 80. So c = ±√80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = -1x + c tangent to the circle x² + y² = 16?', 'c = ±√17', 'c = ±√32', 'c = ±16', 'c = ±4', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 16(1 + 1) = 32. So c = ±√32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the length of the tangent from point (9, 0) to the circle x² + y² = 25.', '4', '14', '√106', '2√14', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Distance from point to centre = 9. Tangent length = √(d² - r²) = √(9² - 5²) = √56 = 2√14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 25 at the point (3, 4).', '3x + 4y = 5', '3x - 4y = 25', '3x + 4y = 25', '4x + 3y = 25', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (3, 4) on x² + y² = 25 is: 3x + 4y = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the length of the tangent from point (10, 0) to the circle x² + y² = 36.', '2√34', '8', '16', '4', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Distance from point to centre = 10. Tangent length = √(d² - r²) = √(10² - 6²) = √64 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to the circle with centre (0, -2) at the point (3, 2).', '3/4', '-4/3', '-3/4', '4/3', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Radius slope = (2--2)/(3-0) = 4/3. Tangent is perpendicular, so slope = -3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 1x + c tangent to the circle x² + y² = 25?', 'c = ±√50', 'c = ±√26', 'c = ±25', 'c = ±5', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 25(1 + 1) = 50. So c = ±√50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to the circle with centre (-1, 3) at the point (2, 7).', '-4/3', '4/3', '-3/4', '3/4', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Radius slope = (7-3)/(2--1) = 4/3. Tangent is perpendicular, so slope = -3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 3x + c tangent to the circle x² + y² = 25?', 'c = ±√34', 'c = ±5', 'c = ±25', 'c = ±√250', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 25(1 + 9) = 250. So c = ±√250', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 25 at the point (4, 3).', '4x - 3y = 25', '3x + 4y = 25', '4x + 3y = 5', '4x + 3y = 25', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (4, 3) on x² + y² = 25 is: 4x + 3y = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 25 at the point (5, 0).', '0x + 5y = 25', 'x = 5', '5x - 0y = 25', '5x + 0y = 5', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'At point (5, 0) on circle x² + y² = 25, tangent is vertical: x = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = -1x + c tangent to the circle x² + y² = 9?', 'c = ±√18', 'c = ±√10', 'c = ±9', 'c = ±3', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 9(1 + 1) = 18. So c = ±√18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 2x + c tangent to the circle x² + y² = 25?', 'c = ±5', 'c = ±√125', 'c = ±25', 'c = ±√29', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 25(1 + 4) = 125. So c = ±√125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 169 at the point (13, 0).', '13x + 0y = 13', '13x - 0y = 169', 'x = 13', '0x + 13y = 169', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'At point (13, 0) on circle x² + y² = 169, tangent is vertical: x = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 25 at the point (5, 0).', '5x + 0y = 5', '5x - 0y = 25', 'x = 5', '0x + 5y = 25', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'At point (5, 0) on circle x² + y² = 25, tangent is vertical: x = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the length of the tangent from point (5, 0) to the circle x² + y² = 9.', '4', '2', '√34', '8', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Distance from point to centre = 5. Tangent length = √(d² - r²) = √(5² - 3²) = √16 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = -2x + c tangent to the circle x² + y² = 16?', 'c = ±√80', 'c = ±√20', 'c = ±16', 'c = ±4', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 16(1 + 4) = 80. So c = ±√80', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 169 at the point (12, 5).', '12x + 5y = 13', '12x + 5y = 169', '5x + 12y = 169', '12x - 5y = 169', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (12, 5) on x² + y² = 169 is: 12x + 5y = 169', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 25 at the point (4, 3).', '4x + 3y = 5', '4x - 3y = 25', '3x + 4y = 25', '4x + 3y = 25', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (4, 3) on x² + y² = 25 is: 4x + 3y = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to the circle with centre (-3, -2) at the point (0, 2).', '-3/4', '3/4', '4/3', '-4/3', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Radius slope = (2--2)/(0--3) = 4/3. Tangent is perpendicular, so slope = -3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 3x + c tangent to the circle x² + y² = 4?', 'c = ±√13', 'c = ±4', 'c = ±√40', 'c = ±2', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 4(1 + 9) = 40. So c = ±√40', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 100 at the point (8, 6).', '8x + 6y = 10', '6x + 8y = 100', '8x - 6y = 100', '8x + 6y = 100', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (8, 6) on x² + y² = 100 is: 8x + 6y = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 3x + c tangent to the circle x² + y² = 16?', 'c = ±4', 'c = ±16', 'c = ±√25', 'c = ±√160', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 16(1 + 9) = 160. So c = ±√160', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 169 at the point (5, 12).', '5x + 12y = 13', '12x + 5y = 169', '5x - 12y = 169', '5x + 12y = 169', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (5, 12) on x² + y² = 169 is: 5x + 12y = 169', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 2x + c tangent to the circle x² + y² = 4?', 'c = ±√8', 'c = ±4', 'c = ±2', 'c = ±√20', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 4(1 + 4) = 20. So c = ±√20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 169 at the point (12, 5).', '12x + 5y = 169', '5x + 12y = 169', '12x + 5y = 13', '12x - 5y = 169', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (12, 5) on x² + y² = 169 is: 12x + 5y = 169', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 169 at the point (5, 12).', '5x - 12y = 169', '5x + 12y = 169', '12x + 5y = 169', '5x + 12y = 13', 1,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (5, 12) on x² + y² = 169 is: 5x + 12y = 169', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = 2x + c tangent to the circle x² + y² = 25?', 'c = ±5', 'c = ±√29', 'c = ±√125', 'c = ±25', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 25(1 + 4) = 125. So c = ±√125', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to the circle with centre (-3, 1) at the point (0, 5).', '-3/4', '4/3', '-4/3', '3/4', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Radius slope = (5-1)/(0--3) = 4/3. Tangent is perpendicular, so slope = -3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the length of the tangent from point (6, 0) to the circle x² + y² = 9.', '3√3', '3', '3√5', '9', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Distance from point to centre = 6. Tangent length = √(d² - r²) = √(6² - 3²) = √27 = 3√3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to the circle with centre (3, 0) at the point (6, 4).', '4/3', '3/4', '-3/4', '-4/3', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Radius slope = (4-0)/(6-3) = 4/3. Tangent is perpendicular, so slope = -3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 100 at the point (8, 6).', '6x + 8y = 100', '8x - 6y = 100', '8x + 6y = 10', '8x + 6y = 100', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (8, 6) on x² + y² = 100 is: 8x + 6y = 100', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to the circle with centre (-1, -3) at the point (2, 1).', '-3/4', '3/4', '4/3', '-4/3', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Radius slope = (1--3)/(2--1) = 4/3. Tangent is perpendicular, so slope = -3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 169 at the point (5, 12).', '5x + 12y = 169', '12x + 5y = 169', '5x + 12y = 13', '5x - 12y = 169', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (5, 12) on x² + y² = 169 is: 5x + 12y = 169', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the slope of the tangent to the circle with centre (2, 0) at the point (5, 4).', '-3/4', '3/4', '4/3', '-4/3', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Radius slope = (4-0)/(5-2) = 4/3. Tangent is perpendicular, so slope = -3/4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the equation of the tangent to the circle x² + y² = 169 at the point (12, 5).', '12x + 5y = 169', '5x + 12y = 169', '12x - 5y = 169', '12x + 5y = 13', 0,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'Tangent at (12, 5) on x² + y² = 169 is: 12x + 5y = 169', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = -3x + c tangent to the circle x² + y² = 9?', 'c = ±√18', 'c = ±9', 'c = ±3', 'c = ±√90', 3,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 9(1 + 9) = 90. So c = ±√90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what value(s) of c is the line y = -3x + c tangent to the circle x² + y² = 9?', 'c = ±√18', 'c = ±9', 'c = ±√90', 'c = ±3', 2,
'lc_hl_coord_geom', 9, 'proficient', 'lc_hl', 'For tangency: c² = r²(1 + m²) = 9(1 + 9) = 90. So c = ±√90', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = -x + 3 and the circle x² + y² = 16?', '1 point', '0 points', '3 points', '2 points', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line intersects circle at 2 points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = -2x + 11 and the circle x² + y² = 36?', '1 point', '0 points', '3 points', '2 points', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line intersects circle at 2 points (secant)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = 5 and the circle x² + y² = 16?', '2 points', '3 points', '0 points', '1 point', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line does not intersect circle', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 4 from the centre. Find the chord length.', '2√41', '10', '6', '√36', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 4²) = 2√9 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 16?', 'k = ±16', 'k = ±8', 'k = ±4√2', 'k = ±4', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 4. So k = ±4√2 = ±√32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = 2x + 9 and the circle x² + y² = 16?', '1 point', '2 points', '3 points', '0 points', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line does not intersect circle', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = 2x + 13 and the circle x² + y² = 25?', '1 point', '2 points', '3 points', '0 points', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line does not intersect circle', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 2 from the centre. Find the chord length.', '2√21', '2√29', '√84', '10', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 2²) = 2√21 = 2√21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = -2x + 5 and the circle x² + y² = 36?', '2 points', '3 points', '1 point', '0 points', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line intersects circle at 2 points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 4?', 'k = ±4', 'None of these', 'k = ±2√2', 'k = ±2', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 2. So k = ±2√2 = ±√8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = 2x + 3 and the circle x² + y² = 25?', '3 points', '1 point', '0 points', '2 points', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line intersects circle at 2 points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 25?', 'k = ±10', 'k = ±5√2', 'k = ±25', 'k = ±5', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 5. So k = ±5√2 = ±√50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = 2x + 4 and the circle x² + y² = 16?', '0 points', '3 points', '2 points', '1 point', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line intersects circle at 2 points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = x - 4 and the circle x² + y² = 16?', '3 points', '2 points', '0 points', '1 point', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line intersects circle at 2 points (secant)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '10', '√96', '4√6', '2√26', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(5, 0) only', '(5, 5) and (-5, -5)', '(5, 0) and (-5, 0)', '(0, 5) and (0, -5)', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '4√6', '2√26', '√96', '10', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = x + 6 and the circle x² + y² = 16?', '2 points', '0 points', '1 point', '3 points', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line does not intersect circle', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '10', '4√6', '√96', '2√26', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 25?', 'k = ±25', 'k = ±10', 'k = ±5', 'k = ±5√2', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 5. So k = ±5√2 = ±√50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '4√6', '2√26', '√96', '10', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '10', '4√6', '2√26', '√96', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(5, 5) and (-5, -5)', '(5, 0) only', '(0, 5) and (0, -5)', '(5, 0) and (-5, 0)', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 3 from the centre. Find the chord length.', '√64', '8', '10', '2√34', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 3²) = 2√16 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 4 from the centre. Find the chord length.', '√36', '2√41', '10', '6', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 4²) = 2√9 = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(5, 0) only', '(0, 5) and (0, -5)', '(5, 0) and (-5, 0)', '(5, 5) and (-5, -5)', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(0, 5) and (0, -5)', '(5, 0) and (-5, 0)', '(5, 0) only', '(5, 5) and (-5, -5)', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 25?', 'k = ±10', 'k = ±5', 'k = ±5√2', 'k = ±25', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 5. So k = ±5√2 = ±√50', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '10', '√96', '4√6', '2√26', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 16?', 'k = ±4√2', 'k = ±4', 'k = ±16', 'k = ±8', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 4. So k = ±4√2 = ±√32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(0, 5) and (0, -5)', '(5, 0) only', '(5, 0) and (-5, 0)', '(5, 5) and (-5, -5)', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '√96', '4√6', '2√26', '10', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = x + 8 and the circle x² + y² = 25?', '0 points', '2 points', '1 point', '3 points', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line does not intersect circle', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(5, 0) only', '(5, 5) and (-5, -5)', '(5, 0) and (-5, 0)', '(0, 5) and (0, -5)', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '4√6', '10', '√96', '2√26', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 3 from the centre. Find the chord length.', '10', '8', '√64', '2√34', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 3²) = 2√16 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(5, 0) only', '(0, 5) and (0, -5)', '(5, 0) and (-5, 0)', '(5, 5) and (-5, -5)', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = 6 and the circle x² + y² = 36?', '1 point', '2 points', '3 points', '0 points', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line is tangent to circle (1 point)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 3 from the centre. Find the chord length.', '8', '2√34', '√64', '10', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 3²) = 2√16 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = -x + 11 and the circle x² + y² = 36?', '3 points', '1 point', '2 points', '0 points', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line does not intersect circle', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(0, 5) and (0, -5)', '(5, 0) and (-5, 0)', '(5, 5) and (-5, -5)', '(5, 0) only', 1,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(5, 0) and (-5, 0)', '(5, 5) and (-5, -5)', '(5, 0) only', '(0, 5) and (0, -5)', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('How many points of intersection are there between the line y = -x + 0 and the circle x² + y² = 9?', '2 points', '1 point', '3 points', '0 points', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Line intersects circle at 2 points (secant)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 4?', 'k = ±4', 'None of these', 'k = ±2', 'k = ±2√2', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 2. So k = ±2√2 = ±√8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 1 from the centre. Find the chord length.', '√96', '2√26', '4√6', '10', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 1²) = 2√24 = 4√6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 3 from the centre. Find the chord length.', '8', '2√34', '√64', '10', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 3²) = 2√16 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the points of intersection of the line y = 0 and the circle x² + y² = 25.', '(5, 0) and (-5, 0)', '(5, 5) and (-5, -5)', '(5, 0) only', '(0, 5) and (0, -5)', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Substituting y = 0: x² = 25, so x = ±5. Points: (5, 0) and (-5, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 16?', 'k = ±16', 'k = ±8', 'k = ±4√2', 'k = ±4', 2,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 4. So k = ±4√2 = ±√32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A chord of a circle with radius 5 is at distance 2 from the centre. Find the chord length.', '2√21', '10', '2√29', '√84', 0,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Chord length = 2√(r² - d²) = 2√(5² - 2²) = 2√21 = 2√21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For what values of k is the line y = x + k tangent to the circle x² + y² = 4?', 'None of these', 'k = ±4', 'k = ±2', 'k = ±2√2', 3,
'lc_hl_coord_geom', 10, 'advanced', 'lc_hl', 'Distance from origin to line = |k|/√2 = 2. So k = ±2√2 = ±√8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-4, 1), what are the new coordinates of the point (7, -7)?', '(11, -8)', '(-11, 8)', '(12, -8)', '(3, -6)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (7 - -4, -7 - 1) = (11, -8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (3, 0). If a point has new coordinates (6, -1), find its original coordinates.', '(9, -1)', '(10, -1)', '(-3, 1)', '(3, -1)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (6 + 3, -1 + 0) = (9, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-4, 4), what are the new coordinates of the point (4, -1)?', '(9, -5)', '(0, 3)', '(8, -5)', '(-8, 5)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (4 - -4, -1 - 4) = (8, -5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² - 6x + 2y + 4 = 0?', '(-6, 2)', '(-3, 1)', '(3, -1)', '(6, -2)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (3, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (0, -3). If a point has new coordinates (-5, -1), find its original coordinates.', '(-4, -4)', '(5, -2)', '(-5, 2)', '(-5, -4)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (-5 + 0, -1 + -3) = (-5, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (2, 0). If a point has new coordinates (4, 6), find its original coordinates.', '(6, 6)', '(7, 6)', '(2, 6)', '(-2, -6)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (4 + 2, 6 + 0) = (6, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (4, -2). If a point has new coordinates (4, -6), find its original coordinates.', '(8, -8)', '(0, -4)', '(9, -8)', '(0, 4)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (4 + 4, -6 + -2) = (8, -8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (2, -4), what are the new coordinates of the point (-6, 8)?', '(8, -12)', '(-7, 12)', '(-8, 12)', '(-4, 4)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (-6 - 2, 8 - -4) = (-8, 12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (4, 4), transform the equation y = x² to the new coordinates.', 'Y = X² + 8X + 20', 'Y = X² + 8X + 12', 'Y = X² - 8X + 12', 'Y = (X - 4)² + 4', 1,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 4, y = Y + 4: Y + 4 = (X + 4)². Expanding: Y = X² + 8X + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (1, 2), transform the equation y = x² to the new coordinates.', 'Y = X² - 2X - 1', 'Y = (X - 1)² + 2', 'Y = X² + 2X - 1', 'Y = X² + 2X + 3', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 1, y = Y + 2: Y + 2 = (X + 1)². Expanding: Y = X² + 2X - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² - 6x + 2y - 5 = 0?', '(-3, 1)', '(-6, 2)', '(6, -2)', '(3, -1)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (3, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (4, 5), what are the new coordinates of the point (5, 7)?', '(9, 12)', '(1, 2)', '(2, 2)', '(-1, -2)', 1,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (5 - 4, 7 - 5) = (1, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 8x + 2y + 1 = 0?', '(-4, -1)', '(8, 2)', '(-8, -2)', '(4, 1)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-4, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 6x + 4y - 4 = 0?', '(6, 4)', '(-3, -2)', '(3, 2)', '(-6, -4)', 1,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-3, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (1, 2), transform the equation y = x² to the new coordinates.', 'Y = X² - 2X - 1', 'Y = (X - 1)² + 2', 'Y = X² + 2X + 3', 'Y = X² + 2X - 1', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 1, y = Y + 2: Y + 2 = (X + 1)². Expanding: Y = X² + 2X - 1', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 6x - 2y + 2 = 0?', '(6, -2)', '(3, -1)', '(-6, 2)', '(-3, 1)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-3, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (4, 4), transform the equation y = x² to the new coordinates.', 'Y = X² - 8X + 12', 'Y = X² + 8X + 20', 'Y = X² + 8X + 12', 'Y = (X - 4)² + 4', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 4, y = Y + 4: Y + 4 = (X + 4)². Expanding: Y = X² + 8X + 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (3, 4), transform the equation y = x² to the new coordinates.', 'Y = X² + 6X + 5', 'Y = X² - 6X + 5', 'Y = (X - 3)² + 4', 'Y = X² + 6X + 13', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 3, y = Y + 4: Y + 4 = (X + 3)². Expanding: Y = X² + 6X + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 6x + 9 = 0?', '(-3, 0)', '(6, 0)', '(-6, 0)', '(3, 0)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-3, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (4, 2), transform the equation y = x² to the new coordinates.', 'Y = X² + 8X + 18', 'Y = X² - 8X + 14', 'Y = (X - 4)² + 2', 'Y = X² + 8X + 14', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 4, y = Y + 2: Y + 2 = (X + 4)². Expanding: Y = X² + 8X + 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (4, -1), what are the new coordinates of the point (3, 0)?', '(-1, 1)', '(7, -1)', '(1, -1)', '(0, 1)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (3 - 4, 0 - -1) = (-1, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 4x + 4y + 3 = 0?', '(4, 4)', '(2, 2)', '(-4, -4)', '(-2, -2)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-2, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-2, 5), what are the new coordinates of the point (4, -6)?', '(-6, 11)', '(7, -11)', '(2, -1)', '(6, -11)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (4 - -2, -6 - 5) = (6, -11)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (2, 5), what are the new coordinates of the point (1, 3)?', '(1, 2)', '(-1, -2)', '(3, 8)', '(0, -2)', 1,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (1 - 2, 3 - 5) = (-1, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (3, 2), transform the equation y = x² to the new coordinates.', 'Y = X² + 6X + 7', 'Y = X² - 6X + 7', 'Y = X² + 6X + 11', 'Y = (X - 3)² + 2', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 3, y = Y + 2: Y + 2 = (X + 3)². Expanding: Y = X² + 6X + 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² - 6y - 10 = 0?', '(0, 6)', '(0, -3)', '(0, -6)', '(0, 3)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (0, 3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-1, -1), what are the new coordinates of the point (5, 7)?', '(-6, -8)', '(7, 8)', '(4, 6)', '(6, 8)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (5 - -1, 7 - -1) = (6, 8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² - 2x - 2y - 5 = 0?', '(2, 2)', '(-2, -2)', '(1, 1)', '(-1, -1)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (1, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (1, 4), transform the equation y = x² to the new coordinates.', 'Y = X² + 2X - 3', 'Y = X² - 2X - 3', 'Y = X² + 2X + 5', 'Y = (X - 1)² + 4', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 1, y = Y + 4: Y + 4 = (X + 1)². Expanding: Y = X² + 2X - 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (3, 3), what are the new coordinates of the point (-3, -4)?', '(-5, -7)', '(0, -1)', '(6, 7)', '(-6, -7)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (-3 - 3, -4 - 3) = (-6, -7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (-4, 4). If a point has new coordinates (1, 5), find its original coordinates.', '(5, 1)', '(-3, 9)', '(-2, 9)', '(-5, -1)', 1,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (1 + -4, 5 + 4) = (-3, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-4, 0), what are the new coordinates of the point (-2, 7)?', '(2, 7)', '(-6, 7)', '(3, 7)', '(-2, -7)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (-2 - -4, 7 - 0) = (2, 7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-4, 2), what are the new coordinates of the point (4, 2)?', '(8, 0)', '(-8, 0)', '(9, 0)', '(0, 4)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (4 - -4, 2 - 2) = (8, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (2, 3). If a point has new coordinates (6, -4), find its original coordinates.', '(4, -7)', '(9, -1)', '(-4, 7)', '(8, -1)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (6 + 2, -4 + 3) = (8, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 6x - 2y - 9 = 0?', '(3, -1)', '(6, -2)', '(-3, 1)', '(-6, 2)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-3, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (3, 4), transform the equation y = x² to the new coordinates.', 'Y = X² + 6X + 13', 'Y = (X - 3)² + 4', 'Y = X² - 6X + 5', 'Y = X² + 6X + 5', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 3, y = Y + 4: Y + 4 = (X + 3)². Expanding: Y = X² + 6X + 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-5, -4), what are the new coordinates of the point (-3, 5)?', '(-8, 1)', '(3, 9)', '(-2, -9)', '(2, 9)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (-3 - -5, 5 - -4) = (2, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (4, 1), transform the equation y = x² to the new coordinates.', 'Y = X² + 8X + 15', 'Y = X² + 8X + 17', 'Y = X² - 8X + 15', 'Y = (X - 4)² + 1', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 4, y = Y + 1: Y + 1 = (X + 4)². Expanding: Y = X² + 8X + 15', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 4x + 4y + 8 = 0?', '(-4, -4)', '(-2, -2)', '(4, 4)', '(2, 2)', 1,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-2, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (3, -1). If a point has new coordinates (0, -5), find its original coordinates.', '(3, -6)', '(-3, -4)', '(4, -6)', '(3, 4)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (0 + 3, -5 + -1) = (3, -6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² + 6x + 6y + 10 = 0?', '(-3, -3)', '(-6, -6)', '(3, 3)', '(6, 6)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (-3, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (-1, 5), what are the new coordinates of the point (1, -8)?', '(-2, 13)', '(3, -13)', '(0, -3)', '(2, -13)', 3,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (1 - -1, -8 - 5) = (2, -13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² - 6x + 6y - 3 = 0?', '(3, -3)', '(6, -6)', '(-3, 3)', '(-6, 6)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (3, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (1, -4), what are the new coordinates of the point (-7, 5)?', '(-8, 9)', '(-6, 1)', '(-7, 9)', '(8, -9)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (-7 - 1, 5 - -4) = (-8, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is translated to (4, -5), what are the new coordinates of the point (0, 6)?', '(4, 1)', '(-3, 11)', '(-4, 11)', '(4, -11)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'New coordinates: (X, Y) = (x - h, y - k) = (0 - 4, 6 - -5) = (-4, 11)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (2, 4), transform the equation y = x² to the new coordinates.', 'Y = X² + 4X', 'Y = (X - 2)² + 4', 'Y = X² - 4X ', 'Y = X² + 4X + 8', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 2, y = Y + 4: Y + 4 = (X + 2)². Expanding: Y = X² + 4X', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If the origin is shifted to (1, 4), transform the equation y = x² to the new coordinates.', 'Y = X² + 2X - 3', 'Y = X² + 2X + 5', 'Y = (X - 1)² + 4', 'Y = X² - 2X - 3', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Substituting x = X + 1, y = Y + 4: Y + 4 = (X + 1)². Expanding: Y = X² + 2X - 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (-4, -2). If a point has new coordinates (3, -6), find its original coordinates.', '(-7, 4)', '(7, -4)', '(-1, -8)', '(0, -8)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (3 + -4, -6 + -2) = (-1, -8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To what point should the origin be translated to remove the first-degree terms from x² + y² - 2x - 4y - 5 = 0?', '(-2, -4)', '(-1, -2)', '(1, 2)', '(2, 4)', 2,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = (1, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('The origin is translated to (-1, -4). If a point has new coordinates (-1, -2), find its original coordinates.', '(-2, -6)', '(0, -2)', '(0, 2)', '(-1, -6)', 0,
'lc_hl_coord_geom', 11, 'advanced', 'lc_hl', 'Original coordinates: (x, y) = (X + h, Y + k) = (-1 + -1, -2 + -4) = (-2, -6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (6, -1), (-2, -4), (2, 8).', '(3, 1)', '(2, 1)', '(2, 2)', '(2, -3)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (2, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (4, 0), (0, 5), (-10, -11).', '(-2, -1)', '(2, 2)', '(-2, -2)', '(-1, -2)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (-2, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Circle 1: centre (0, 0), radius 5. Circle 2: centre (6, 0), radius 3. Describe their intersection.', '2 intersection points', 'External tangency (1 point)', 'No intersection (external)', 'Internal tangency (1 point)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance between centres = 6. Sum of radii = 8. |Difference| = 2. 2 intersection points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Circle 1: centre (0, 0), radius 5. Circle 2: centre (7, 0), radius 5. Describe their intersection.', 'No intersection (external)', 'Internal tangency (1 point)', 'External tangency (1 point)', '2 intersection points', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance between centres = 7. Sum of radii = 10. |Difference| = 0. 2 intersection points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumcentre of the triangle with vertices A(0, 0), B(6, 0), C(0, 8).', '(3, 4)', '(3, 3)', '(2, 4)', '(2, 2)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'For a right triangle, the circumcentre is the midpoint of the hypotenuse. Circumcentre = (3, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (-1, 1), (5, 6), (5, -4).', '(3, 1)', '(3, 2)', '(4, 1)', '(2, 3)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (3, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (1, -2) to the line 3x + 3y = 5.', '9/√18', '8/√18', '8', '8/√19', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |3(1) + 3(-2) - 5| / √(3² + 3²) = 8/√18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumcentre of the triangle with vertices A(0, 0), B(6, 0), C(0, 8).', '(2, 4)', '(3, 4)', '(2, 2)', '(3, 3)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'For a right triangle, the circumcentre is the midpoint of the hypotenuse. Circumcentre = (3, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Circle 1: centre (0, 0), radius 5. Circle 2: centre (10, 0), radius 5. Describe their intersection.', 'External tangency (1 point)', 'No intersection (external)', 'Internal tangency (1 point)', '2 intersection points', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance between centres = 10. Sum of radii = 10. |Difference| = 0. External tangency (1 point)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (-6, -5), (-1, 5), (-2, -6).', '(-2, -2)', '(-4, 0)', '(-3, -2)', '(-3, -1)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (-3, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (5, -3) to the line 4x + 2y = 11.', '4/√20', '3', '3/√20', '3/√21', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |4(5) + 2(-3) - 11| / √(4² + 2²) = 3/√20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reflection of the point (2, 4) in the line y = x.', '(4, 2)', '(-4, -2)', '(-2, -4)', '(2, -4)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Reflection in y = x swaps the coordinates. (2, 4) → (4, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are points with AB = 10. If A = (5, 0) and the midpoint M = (8, 4), find B.', '(15, 0)', 'None of these', '(11, 8)', '(12, 8)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'B = (2mx - x1, 2my - y1) = (2·8 - 5, 2·4 - 0) = (11, 8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reflection of the point (4, -4) in the line y = x.', 'None of these', '(4, -4)', '(4, 4)', '(-4, 4)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Reflection in y = x swaps the coordinates. (4, -4) → (-4, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are points with AB = 10. If A = (0, 5) and the midpoint M = (3, 9), find B.', 'None of these', '(7, 13)', '(10, 5)', '(6, 13)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'B = (2mx - x1, 2my - y1) = (2·3 - 0, 2·9 - 5) = (6, 13)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reflection of the point (4, -5) in the line y = x.', '(4, 5)', '(5, -4)', '(-4, 5)', '(-5, 4)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Reflection in y = x swaps the coordinates. (4, -5) → (-5, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (2, 1), (1, 4), (0, -2).', '(2, 1)', 'None of these', '(1, 2)', '(1, 1)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (1, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (-4, -2), (-5, -6), (3, 2).', '(-2, -2)', '(-2, -1)', '(-1, -2)', '(-5, -4)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (-2, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are points with AB = 10. If A = (5, -3) and the midpoint M = (8, 1), find B.', '(15, -3)', '(11, 5)', 'None of these', '(12, 5)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'B = (2mx - x1, 2my - y1) = (2·8 - 5, 2·1 - -3) = (11, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (2, 2) to the line 2x + 4y = 5.', '7', '8/√20', '7/√20', '7/√21', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |2(2) + 4(2) - 5| / √(2² + 4²) = 7/√20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reflection of the point (4, 1) in the line y = x.', '(-1, -4)', '(4, -1)', '(-4, -1)', '(1, 4)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Reflection in y = x swaps the coordinates. (4, 1) → (1, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are points with AB = 10. If A = (-4, -4) and the midpoint M = (-1, 0), find B.', '(2, 4)', '(3, 4)', '(6, -4)', 'None of these', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'B = (2mx - x1, 2my - y1) = (2·-1 - -4, 2·0 - -4) = (2, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (-3, 5) to the line 2x + 4y = 13.', '2/√20', '1/√20', '1', '1/√21', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |2(-3) + 4(5) - 13| / √(2² + 4²) = 1/√20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Circle 1: centre (0, 0), radius 5. Circle 2: centre (9, 0), radius 3. Describe their intersection.', 'No intersection (external)', '2 intersection points', 'Internal tangency (1 point)', 'External tangency (1 point)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance between centres = 9. Sum of radii = 8. |Difference| = 2. No intersection (external)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (-4, 5), (-2, 2), (12, 2).', '(2, 3)', '(3, 3)', '(-3, 3)', '(2, 4)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (2, 3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (2, 3), (6, -4), (1, 10).', '(4, 3)', '(3, 4)', '(4, -1)', '(3, 3)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (3, 3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumcentre of the triangle with vertices A(0, 0), B(6, 0), C(0, 8).', '(2, 4)', '(3, 3)', '(3, 4)', '(2, 2)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'For a right triangle, the circumcentre is the midpoint of the hypotenuse. Circumcentre = (3, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumcentre of the triangle with vertices A(0, 0), B(6, 0), C(0, 8).', '(2, 4)', '(3, 4)', '(3, 3)', '(2, 2)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'For a right triangle, the circumcentre is the midpoint of the hypotenuse. Circumcentre = (3, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (-1, -5) to the line 4x + 1y = 8.', '17/√17', '17', '17/√18', '18/√17', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |4(-1) + 1(-5) - 8| / √(4² + 1²) = 17/√17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (0, 0), (-1, -1), (-8, -2).', '(-3, -1)', '(-1, -1)', '(-3, 0)', '(-2, -1)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (-3, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumcentre of the triangle with vertices A(0, 0), B(6, 0), C(0, 8).', '(3, 3)', '(2, 4)', '(2, 2)', '(3, 4)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'For a right triangle, the circumcentre is the midpoint of the hypotenuse. Circumcentre = (3, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (4, -3), (4, -4), (-8, 13).', '(1, 2)', '(0, 3)', '(0, 2)', '(4, -4)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (0, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (4, -3) to the line 4x + 4y = 9.', '5/√32', '5', '5/√33', '6/√32', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |4(4) + 4(-3) - 9| / √(4² + 4²) = 5/√32', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (-3, 4), (-2, -5), (-1, -5).', '(-2, -1)', '(-3, -1)', '(-1, -2)', '(-2, -2)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (-2, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (-3, -2) to the line 1x + 3y = 6.', '16/√10', '15/√10', '15/√11', '15', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |1(-3) + 3(-2) - 6| / √(1² + 3²) = 15/√10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (-3, -4), (2, -3), (7, 7).', '(2, 1)', '(2, 0)', '(3, 0)', '(-1, -4)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (2, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Circle 1: centre (0, 0), radius 5. Circle 2: centre (6, 0), radius 2. Describe their intersection.', 'External tangency (1 point)', '2 intersection points', 'Internal tangency (1 point)', 'No intersection (external)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance between centres = 6. Sum of radii = 7. |Difference| = 3. 2 intersection points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (3, 6), (6, 6), (-12, -21).', '(-1, -3)', '(-1, -2)', '(4, 6)', '(0, -3)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (-1, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (0, 3) to the line 1x + 3y = 9.', '0', '0/√10', '1/√10', '0/√11', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |1(0) + 3(3) - 9| / √(1² + 3²) = 0/√10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (-5, -3), (5, 5), (9, -8).', '(3, -1)', '(3, -2)', '(0, 1)', '(4, -2)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (3, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the centroid of the triangle with vertices (0, 6), (3, 4), (-6, -13).', '(1, 5)', '(-1, 0)', '(-1, -1)', '(0, -1)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = (-1, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A and B are points with AB = 10. If A = (-1, -2) and the midpoint M = (2, 2), find B.', '(9, -2)', '(5, 6)', 'None of these', '(6, 6)', 1,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'B = (2mx - x1, 2my - y1) = (2·2 - -1, 2·2 - -2) = (5, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reflection of the point (-2, 0) in the line y = x.', '(0, -2)', '(2, 0)', '(0, 2)', '(-2, 0)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Reflection in y = x swaps the coordinates. (-2, 0) → (0, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the reflection of the point (-5, 1) in the line y = x.', '(-1, 5)', '(-5, -1)', '(1, -5)', '(5, -1)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Reflection in y = x swaps the coordinates. (-5, 1) → (1, -5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Circle 1: centre (0, 0), radius 5. Circle 2: centre (12, 0), radius 3. Describe their intersection.', 'No intersection (external)', 'Internal tangency (1 point)', '2 intersection points', 'External tangency (1 point)', 0,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance between centres = 12. Sum of radii = 8. |Difference| = 2. No intersection (external)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the circumcentre of the triangle with vertices A(0, 0), B(6, 0), C(0, 8).', '(3, 3)', '(2, 2)', '(2, 4)', '(3, 4)', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'For a right triangle, the circumcentre is the midpoint of the hypotenuse. Circumcentre = (3, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Circle 1: centre (0, 0), radius 5. Circle 2: centre (6, 0), radius 4. Describe their intersection.', 'Internal tangency (1 point)', 'No intersection (external)', '2 intersection points', 'External tangency (1 point)', 2,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance between centres = 6. Sum of radii = 9. |Difference| = 1. 2 intersection points', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (2, 0) to the line 3x + 1y = 13.', '7/√11', '8/√10', '7', '7/√10', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |3(2) + 1(0) - 13| / √(3² + 1²) = 7/√10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (4, -4) to the line 1x + 2y = 13.', '18/√5', '17/√6', '17', '17/√5', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |1(4) + 2(-4) - 13| / √(1² + 2²) = 17/√5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the perpendicular distance from point (-1, 1) to the line 2x + 3y = 11.', '11/√13', '10/√14', '10', '10/√13', 3,
'lc_hl_coord_geom', 12, 'advanced', 'lc_hl', 'Distance = |2(-1) + 3(1) - 11| / √(2² + 3²) = 10/√13', 1);