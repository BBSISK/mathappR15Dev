-- LC Higher Level - Geometry - Complete SQL
-- Run: sqlite3 /home/bbsisk/mathapp/instance/mathquiz.db < lc_hl_geometry_complete.sql
-- Generated: 2025-12-15

-- Add Geometry topic to LC Higher Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT 'lc_hl_geometry', 'Geometry', id, '📐', 13, 1
FROM strands WHERE name = 'LC Higher Level';

SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = 'lc_hl_geometry';

-- Questions (600 total, 50 per level x 12 levels)


INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 139°. Find the corresponding angle.', '41', '139', '90', '149', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 139°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 101°. Find the other.', '259', '89', '101', '79', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 101° = 79°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 143°. Find the other.', '217', '37', '143', '47', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 143° = 37°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two lines intersect. One angle is 155°. Find the vertically opposite angle.', '155', '90', '165', '25', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Vertically opposite angles are equal. The angle = 155°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 96° and x°. Find x.', '94', '264', '74', '84', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 96° = 84°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 122°. Find the alternate angle.', '58', '122', '90', '137', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 122°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 77°. Find the alternate angle.', '90', '92', '77', '103', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 77°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 45°. Find the other.', '145', '45', '135', '315', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 45° = 135°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 104°. Find the other.', '256', '76', '104', '86', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 104° = 76°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 89°. Find the other.', '91', '271', '101', '89', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 89° = 91°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 97° and x°. Find x.', '83', '263', '93', '73', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 97° = 83°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 42°. Find the corresponding angle.', '90', '42', '138', '52', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 42°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 73°. Find the other.', '107', '73', '117', '287', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 73° = 107°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Four angles at a point are 42°, 85°, 106° and x°. Find x.', '117', '137', '53', '127', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles at a point sum to 360°. x = 360° - 42° - 85° - 106° = 127°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 106°. Find the corresponding angle.', '116', '90', '106', '74', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 106°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 105°. Find the other.', '75', '85', '105', '255', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 105° = 75°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 36°. Find the corresponding angle.', '144', '36', '90', '46', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 36°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Four angles at a point are 66°, 110°, 107° and x°. Find x.', '67', '87', '77', '103', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles at a point sum to 360°. x = 360° - 66° - 110° - 107° = 77°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 75° and x°. Find x.', '115', '95', '105', '285', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 75° = 105°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 45°. Find the corresponding angle.', '90', '55', '45', '135', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 149°. Find the corresponding angle.', '159', '31', '149', '90', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 149°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 64° and x°. Find x.', '296', '106', '116', '126', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 64° = 116°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 134°. Find the corresponding angle.', '144', '134', '90', '46', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 134°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 86°. Find the alternate angle.', '101', '86', '90', '94', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 86°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two lines intersect. One angle is 145°. Find the vertically opposite angle.', '35', '155', '90', '145', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Vertically opposite angles are equal. The angle = 145°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two lines intersect. One angle is 64°. Find the vertically opposite angle.', '74', '90', '64', '116', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Vertically opposite angles are equal. The angle = 64°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 138° and x°. Find x.', '52', '42', '32', '222', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 138° = 42°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 87°. Find the alternate angle.', '93', '102', '90', '87', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 87°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Four angles at a point are 68°, 59°, 53° and x°. Find x.', '170', '190', '180', '0', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles at a point sum to 360°. x = 360° - 68° - 59° - 53° = 180°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 99°. Find the alternate angle.', '90', '99', '81', '114', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 99°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 70°. Find the alternate angle.', '110', '90', '85', '70', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 70°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Four angles at a point are 46°, 68°, 109° and x°. Find x.', '43', '147', '127', '137', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles at a point sum to 360°. x = 360° - 46° - 68° - 109° = 137°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 76°. Find the other.', '114', '284', '104', '76', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 76° = 104°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 122°. Find the alternate angle.', '90', '58', '137', '122', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 122°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 89° and x°. Find x.', '91', '271', '81', '101', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 89° = 91°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 41°. Find the alternate angle.', '139', '90', '56', '41', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 41°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 71° and x°. Find x.', '109', '99', '119', '289', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 71° = 109°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two lines intersect. One angle is 117°. Find the vertically opposite angle.', '63', '117', '127', '90', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Vertically opposite angles are equal. The angle = 117°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 75° and x°. Find x.', '95', '285', '115', '105', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 75° = 105°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 96°. Find the corresponding angle.', '90', '106', '84', '96', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 96°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 127°. Find the other.', '53', '233', '127', '63', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 127° = 53°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 77°. Find the alternate angle.', '103', '92', '77', '90', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Alternate angles are equal. Angle = 77°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two lines intersect. One angle is 40°. Find the vertically opposite angle.', '90', '50', '40', '140', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Vertically opposite angles are equal. The angle = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Four angles at a point are 110°, 70°, 67° and x°. Find x.', '123', '103', '113', '67', 2,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles at a point sum to 360°. x = 360° - 110° - 70° - 67° = 113°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One co-interior angle is 74°. Find the other.', '74', '286', '116', '106', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Co-interior angles sum to 180°. Angle = 180° - 74° = 106°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 77°. Find the corresponding angle.', '77', '103', '90', '87', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 77°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Four angles at a point are 108°, 61°, 96° and x°. Find x.', 'None of these', '95', '105', '85', 1,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles at a point sum to 360°. x = 360° - 108° - 61° - 96° = 95°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 90°. Find the corresponding angle.', '90', '100', 'None of these', 'None of these', 0,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles on a straight line are 123° and x°. Find x.', '67', '47', '237', '57', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Angles on a straight line sum to 180°. x = 180° - 123° = 57°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two parallel lines cut by a transversal. One angle is 131°. Find the corresponding angle.', '90', '49', '141', '131', 3,
'lc_hl_geometry', 1, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle = 131°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 50°, 60°, 70°. What type of triangle is it?', 'acute', 'right-angled', 'obtuse', 'equilateral', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is acute.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 69° and 55°. Find the exterior angle at the third vertex.', '56', '124', '69', '55', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 69° + 55° = 124°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 3 and 4. Which could be the third side?', '1', '5', '7', '11', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 1 and 7. So 5 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 3 and 9. Which could be the third side?', '6', '9', '13', '12', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 6 and 12. So 9 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 50°, 60°, 70°. What type of triangle is it?', 'obtuse', 'right-angled', 'acute', 'equilateral', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is acute.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 44° and 61°. Find the exterior angle at the third vertex.', '105', '61', '75', '44', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 44° + 61° = 105°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 38° and angle B = 32°. Find angle C.', '100', '70', '110', '120', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 38° - 32° = 110°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 30° and 38°. Find the exterior angle at the third vertex.', '68', '38', '30', '112', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 30° + 38° = 68°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 42° and angle B = 75°. Find angle C.', '53', '117', '63', '73', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 42° - 75° = 63°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 5 and 5. Which could be the third side?', '15', '10', '2', '0', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 0 and 10. So 2 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 30°, 60°, 90°. What type of triangle is it?', 'equilateral', 'right-angled', 'obtuse', 'acute', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is right-angled.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is each angle in an equilateral triangle?', '90', '45', '120', '60', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is each angle in an equilateral triangle?', '60', '120', '45', '90', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an isosceles triangle, the two equal base angles are each 70°. Find the apex angle.', '140', '40', '70', '110', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Apex angle = 180° - 2(70°) = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 79° and angle B = 51°. Find angle C.', '130', '40', '60', '50', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 79° - 51° = 50°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 30°, 60°, 90°. What type of triangle is it?', 'obtuse', 'right-angled', 'equilateral', 'acute', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is right-angled.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 30°, 60°, 90°. What type of triangle is it?', 'equilateral', 'right-angled', 'acute', 'obtuse', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is right-angled.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 5 and 10. Which could be the third side?', '9', '5', '17', '15', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 5 and 15. So 9 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 50°, 60°, 70°. What type of triangle is it?', 'equilateral', 'right-angled', 'obtuse', 'acute', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is acute.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 30°, 40°, 110°. What type of triangle is it?', 'acute', 'equilateral', 'right-angled', 'obtuse', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is obtuse.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 37° and 48°. Find the exterior angle at the third vertex.', '85', '37', '95', '48', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 37° + 48° = 85°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 7 and 4. Which could be the third side?', '13', '11', '3', '5', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 3 and 11. So 5 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 62° and angle B = 52°. Find angle C.', '56', '76', '66', '114', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 62° - 52° = 66°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 55° and angle B = 78°. Find angle C.', '133', '47', '37', '57', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 55° - 78° = 47°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is each angle in an equilateral triangle?', '90', '60', '120', '45', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 9 and 10. Which could be the third side?', '3', '19', '22', '1', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 1 and 19. So 3 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an isosceles triangle, the two equal base angles are each 58°. Find the apex angle.', '122', '116', '64', '58', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Apex angle = 180° - 2(58°) = 64°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is each angle in an equilateral triangle?', '45', '90', '120', '60', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 35° and angle B = 47°. Find angle C.', '108', '88', '82', '98', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 35° - 47° = 98°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 50°, 60°, 70°. What type of triangle is it?', 'equilateral', 'acute', 'right-angled', 'obtuse', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is acute.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 50°, 60°, 70°. What type of triangle is it?', 'right-angled', 'obtuse', 'equilateral', 'acute', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is acute.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is each angle in an equilateral triangle?', '45', '60', '120', '90', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 40° and 39°. Find the exterior angle at the third vertex.', '79', '39', '101', '40', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 40° + 39° = 79°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 3 and 9. Which could be the third side?', '12', '6', '15', '7', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 6 and 12. So 7 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 6 and 7. Which could be the third side?', '1', '5', '14', '13', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 1 and 13. So 5 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is each angle in an equilateral triangle?', '60', '90', '120', '45', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is each angle in an equilateral triangle?', '60', '90', '120', '45', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 65° and 60°. Find the exterior angle at the third vertex.', '55', '65', '125', '60', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 65° + 60° = 125°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 74° and angle B = 46°. Find angle C.', '120', '60', '50', '70', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 74° - 46° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 9 and 9. Which could be the third side?', '18', '0', '23', '1', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 0 and 18. So 1 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 63° and 37°. Find the exterior angle at the third vertex.', '63', '80', '100', '37', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 63° + 37° = 100°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In an isosceles triangle, the two equal base angles are each 52°. Find the apex angle.', '128', '104', '52', '76', 3,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Apex angle = 180° - 2(52°) = 76°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 32° and 59°. Find the exterior angle at the third vertex.', '59', '32', '91', '89', 2,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 32° + 59° = 91°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 50°, 60°, 70°. What type of triangle is it?', 'acute', 'obtuse', 'right-angled', 'equilateral', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is acute.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a triangle, two interior angles are 47° and 60°. Find the exterior angle at the third vertex.', '73', '107', '47', '60', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Exterior angle = sum of opposite interior angles = 47° + 60° = 107°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 45° and angle B = 32°. Find angle C.', '77', '103', '113', '93', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 45° - 32° = 103°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('A triangle has angles 30°, 60°, 90°. What type of triangle is it?', 'right-angled', 'acute', 'obtuse', 'equilateral', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'The triangle is right-angled.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 6 and 3. Which could be the third side?', '7', '9', '3', '13', 0,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 3 and 9. So 7 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In triangle ABC, angle A = 67° and angle B = 35°. Find angle C.', '68', '78', '88', '102', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Angles in a triangle sum to 180°. C = 180° - 67° - 35° = 78°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two sides of a triangle are 10 and 6. Which could be the third side?', '4', '10', '16', '20', 1,
'lc_hl_geometry', 2, 'foundation', 'lc_hl', 'Third side must be between 4 and 16. So 10 is valid.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two sides and included angle equal?', 'SAS', 'SSS', 'ASA', 'AAS', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SAS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'ASA', 'Not valid', 'SAS', 'SSS', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 58°, what is angle X?', '32', '68', '58', '122', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 58°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ PQR. If AB = 6 cm, what is PQ?', '8', '4', '6', '12', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding sides are equal. PQ = 6 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: AB = PQ, angle B = angle Q, BC = QR. Which congruence condition?', 'ASA', 'SAS', 'SSS', 'AAS', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies SAS.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: angle A = angle P, AB = PQ, angle B = angle Q. Which congruence condition?', 'ASA', 'SAS', 'SSS', 'AAS', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies ASA.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two sides and included angle equal?', 'SAS', 'SSS', 'ASA', 'AAS', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SAS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'SSS', 'SAS', 'ASA', 'Not valid', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: angle A = angle P, AB = PQ, angle B = angle Q. Which congruence condition?', 'AAS', 'SSS', 'ASA', 'SAS', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies ASA.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Three sides equal?', 'ASA', 'RHS', 'SSS', 'SAS', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SSS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 33°, what is angle X?', '57', '43', '33', '147', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 33°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ PQR. If AB = 7 cm, what is PQ?', '14', '7', '5', '9', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding sides are equal. PQ = 7 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 71°, what is angle X?', '71', '109', '19', '81', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 71°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 57°, what is angle X?', '57', '123', '33', '67', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 57°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'SSS', 'SAS', 'ASA', 'Not valid', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'ASA', 'Not valid', 'SSS', 'SAS', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Right angle, hypotenuse, side?', 'ASA', 'SSS', 'SAS', 'RHS', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the RHS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'SAS', 'SSS', 'ASA', 'Not valid', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 49°, what is angle X?', '49', '59', '131', '41', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 49°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 55°, what is angle X?', '125', '65', '35', '55', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 55°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 34°, what is angle X?', '34', '44', '146', '56', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 34°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ PQR. If AB = 5 cm, what is PQ?', '10', '5', '3', '7', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding sides are equal. PQ = 5 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ PQR. If AB = 15 cm, what is PQ?', '17', '15', '30', '13', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding sides are equal. PQ = 15 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 57°, what is angle X?', '123', '67', '57', '33', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 57°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: AB = PQ, angle B = angle Q, BC = QR. Which congruence condition?', 'SSS', 'AAS', 'SAS', 'ASA', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies SAS.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 37°, what is angle X?', '143', '53', '47', '37', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 37°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 75°, what is angle X?', '105', '15', '85', '75', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 75°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Three sides equal?', 'ASA', 'SSS', 'SAS', 'RHS', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SSS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'ASA', 'Not valid', 'SSS', 'SAS', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two angles and included side equal?', 'ASA', 'RHS', 'SSS', 'SAS', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the ASA congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: AB = PQ, angle B = angle Q, BC = QR. Which congruence condition?', 'ASA', 'SAS', 'SSS', 'AAS', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies SAS.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two angles and included side equal?', 'ASA', 'RHS', 'SAS', 'SSS', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the ASA congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Right angle, hypotenuse, side?', 'SSS', 'ASA', 'RHS', 'SAS', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the RHS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two angles and included side equal?', 'SSS', 'RHS', 'ASA', 'SAS', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the ASA congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Right angle, hypotenuse, side?', 'SAS', 'SSS', 'RHS', 'ASA', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the RHS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'SSS', 'Not valid', 'ASA', 'SAS', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two sides and included angle equal?', 'AAS', 'ASA', 'SSS', 'SAS', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SAS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ PQR. If AB = 10 cm, what is PQ?', '8', '20', '10', '12', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding sides are equal. PQ = 10 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two sides and included angle equal?', 'SAS', 'ASA', 'SSS', 'AAS', 0,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SAS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'SSS', 'Not valid', 'SAS', 'ASA', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ PQR. If AB = 13 cm, what is PQ?', '11', '26', '13', '15', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding sides are equal. PQ = 13 cm', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: AB = PQ, angle B = angle Q, BC = QR. Which congruence condition?', 'SSS', 'AAS', 'ASA', 'SAS', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies SAS.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: angle A = angle P, AB = PQ, angle B = angle Q. Which congruence condition?', 'AAS', 'SAS', 'ASA', 'SSS', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies ASA.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 41°, what is angle X?', '49', '139', '51', '41', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 41°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 41°, what is angle X?', '49', '41', '51', '139', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 41°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Three sides equal?', 'ASA', 'SAS', 'SSS', 'RHS', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SSS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is AAA (three angles equal) a valid congruence condition?', 'SSS', 'Not valid', 'SAS', 'ASA', 1,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'AAA is not valid - triangles may be similar but not congruent.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which congruence condition is: Two sides and included angle equal?', 'SSS', 'ASA', 'SAS', 'AAS', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This is the SAS congruence condition.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ≅ XYZ. If angle A = 62°, what is angle X?', '72', '118', '62', '28', 2,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'Corresponding angles are equal. Angle X = 62°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC and PQR have: AB = PQ, BC = QR, AC = PR. Which congruence condition?', 'AAS', 'SAS', 'ASA', 'SSS', 3,
'lc_hl_geometry', 3, 'foundation', 'lc_hl', 'This satisfies SSS.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 3, BC = 6, PQ = 6. Find QR.', 'None of these', '12', '6', '14', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 2. QR = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ XYZ. If AB = 3 and XY = 6, find the scale factor.', '1', 'None of these', '2', '3', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 6/3 = 2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All three angles equal?', 'Need sides', 'No', 'Maybe', 'Yes', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All three angles equal?', 'Maybe', 'No', 'Yes', 'Need sides', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ XYZ. If AB = 3 and XY = 12, find the scale factor.', '9', '5', '3', '4', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 12/3 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 7, DE = 6, BC = 15. Find AB.', '13', '15', '19', '17', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ XYZ. If AB = 6 and XY = 24, find the scale factor.', '18', '5', '3', '4', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 24/6 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 6, DE = 4, BC = 9. Find AB.', '9', '13', '15', '10', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All three angles equal?', 'Maybe', 'Yes', 'Need sides', 'No', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 2. Smaller area is 21 cm². Find larger area.', 'None of these', '84', '42', '105', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 4. Larger area = 21 × 4 = 84 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 5, BC = 8, PQ = 15. Find QR.', '24', '27', '15', '23', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 3. QR = 8 × 3 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 4. Smaller area is 27 cm². Find larger area.', '459', '108', '54', '432', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 16. Larger area = 27 × 16 = 432 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 7, BC = 4, PQ = 21. Find QR.', '12', '21', '25', '15', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 3. QR = 4 × 3 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 2. Smaller area is 25 cm². Find larger area.', '125', '50', 'None of these', '100', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 4. Larger area = 25 × 4 = 100 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All sides in proportion?', 'Maybe', 'Need angles', 'No', 'Yes', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 5, BC = 10, PQ = 10. Find QR.', '20', '10', '22', 'None of these', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 2. QR = 10 × 2 = 20', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 7, DE = 5, BC = 15. Find AB.', '23', '15', '21', '12', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 3, BC = 6, PQ = 6. Find QR.', '6', '12', '14', 'None of these', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 2. QR = 6 × 2 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 4, BC = 4, PQ = 12. Find QR.', '16', 'None of these', '15', '12', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 3. QR = 4 × 3 = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All sides in proportion?', 'Maybe', 'No', 'Yes', 'Need angles', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 6, BC = 7, PQ = 18. Find QR.', '24', '18', '25', '21', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 3. QR = 7 × 3 = 21', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All sides in proportion?', 'Need angles', 'Maybe', 'Yes', 'No', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All three angles equal?', 'Yes', 'No', 'Maybe', 'Need sides', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 2. Smaller area is 23 cm². Find larger area.', '92', '46', '115', 'None of these', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 4. Larger area = 23 × 4 = 92 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 7, BC = 6, PQ = 28. Find QR.', '24', '28', 'None of these', '34', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 4. QR = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All sides in proportion?', 'No', 'Yes', 'Maybe', 'Need angles', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 8, DE = 3, BC = 11. Find AB.', '31', '29', 'None of these', '11', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 29', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All sides in proportion?', 'Need angles', 'Maybe', 'No', 'Yes', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 2. Smaller area is 25 cm². Find larger area.', '125', 'None of these', '100', '50', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 4. Larger area = 25 × 4 = 100 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 4, BC = 7, PQ = 16. Find QR.', '28', '16', '23', '32', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 4. QR = 7 × 4 = 28', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 7, DE = 6, BC = 14. Find AB.', '16', '13', '18', '14', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 7, DE = 4, BC = 13. Find AB.', '24', '11', '22', '13', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 22', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 5, BC = 6, PQ = 20. Find QR.', '26', '28', '24', '20', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 4. QR = 6 × 4 = 24', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ XYZ. If AB = 7 and XY = 35, find the scale factor.', '28', '5', '4', '6', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 35/7 = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 4, DE = 3, BC = 12. Find AB.', '7', '16', '18', '12', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All three angles equal?', 'Maybe', 'No', 'Need sides', 'Yes', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 5, DE = 3, BC = 14. Find AB.', '14', '23', '25', '8', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 23', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 8, BC = 5, PQ = 16. Find QR.', '21', '16', '12', '10', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 2. QR = 5 × 2 = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 7, DE = 5, BC = 13. Find AB.', '18', '12', '20', '13', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 7, DE = 5, BC = 13. Find AB.', '13', '18', '20', '12', 1,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 18', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 3. Smaller area is 18 cm². Find larger area.', '162', '180', '36', '54', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 9. Larger area = 18 × 9 = 162 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ XYZ. If AB = 5 and XY = 20, find the scale factor.', '15', '5', '3', '4', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 20/5 = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ PQR with AB = 3, BC = 9, PQ = 12. Find QR.', '36', '12', '21', '40', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 4. QR = 9 × 4 = 36', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 7, DE = 6, BC = 11. Find AB.', '12', '14', '11', '13', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 3. Smaller area is 15 cm². Find larger area.', '30', '45', '150', '135', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 9. Larger area = 15 × 9 = 135 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 5, DE = 6, BC = 15. Find AB.', '14', '15', '12', '11', 2,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangles ABC ~ XYZ. If AB = 3 and XY = 9, find the scale factor.', '4', '2', '6', '3', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Scale factor = 9/3 = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar triangles have scale factor 4. Smaller area is 30 cm². Find larger area.', '480', '120', '60', '510', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Area ratio = k² = 16. Larger area = 30 × 16 = 480 cm²', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In △ABC, DE ∥ BC. AD = 8, DE = 6, BC = 13. Find AB.', '19', '13', '14', '17', 3,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'By similarity: AB = AD × BC/DE = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Are triangles similar if they have: All sides in proportion?', 'Yes', 'Need angles', 'No', 'Maybe', 0,
'lc_hl_geometry', 4, 'developing', 'lc_hl', 'Yes, the triangles are similar.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 7 and 24. Find the hypotenuse.', '24', '31', '25', '26', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 7² + 24² = 625. c = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 24, hypotenuse is 25. Find the other leg.', '7', '1', '24', '8', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 25² - 24² = 49. a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is a triangle with sides 6, 8, 11 a right triangle?', 'Cannot determine', 'No', 'Yes', 'Maybe', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', '6² + 8² = 100, 11² = 121. No.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 6 × 4 × 5 box.', '24', '√77', '15', '2√13', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(6² + 4² + 5²) = √77 = √77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 5 × 5 × 3 box.', '25', '√59', '5√2', '13', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(5² + 5² + 3²) = √59 = √59', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 24, hypotenuse is 25. Find the other leg.', '24', '1', '8', '7', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 25² - 24² = 49. a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 7 and 24. Find the hypotenuse.', '24', '25', '31', '26', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 7² + 24² = 625. c = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 6 × 6 × 5 box.', '√97', '6√2', '17', '36', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(6² + 6² + 5²) = √97 = √97', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 7 and 24. Find the hypotenuse.', '24', '26', '31', '25', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 7² + 24² = 625. c = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (6, 3).', '3√5', '18', '9', '√46', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(6² + 3²) = √45 = 3√5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 6 and 8. Find the hypotenuse.', '14', '11', '9', '10', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 6² + 8² = 100. c = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 8 and 15. Find the hypotenuse.', '16', '23', '18', '17', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 8² + 15² = 289. c = 17', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (6, 3).', '√46', '18', '9', '3√5', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(6² + 3²) = √45 = 3√5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is a triangle with sides 7, 24, 25 a right triangle?', 'No', 'Cannot determine', 'Yes', 'Maybe', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', '7² + 24² = 625, 25² = 625. Yes.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 15, hypotenuse is 17. Find the other leg.', '8', '15', '9', '2', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 17² - 15² = 64. a = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 5 × 5 × 4 box.', '25', '14', '√66', '5√2', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(5² + 5² + 4²) = √66 = √66', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (6, 3).', '√46', '18', '9', '3√5', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(6² + 3²) = √45 = 3√5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 12, hypotenuse is 13. Find the other leg.', '12', '6', '5', '1', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 13² - 12² = 25. a = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 12, hypotenuse is 13. Find the other leg.', '5', '1', '12', '6', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 13² - 12² = 25. a = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 24, hypotenuse is 25. Find the other leg.', '24', '1', '7', '8', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 25² - 24² = 49. a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (4, 4).', '16', '√33', '4√2', '8', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(4² + 4²) = √32 = 4√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 5 and 12. Find the hypotenuse.', '12', '14', '17', '13', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 5² + 12² = 169. c = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 12, hypotenuse is 13. Find the other leg.', '1', '12', '5', '6', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 13² - 12² = 25. a = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 5 and 12. Find the hypotenuse.', '12', '14', '17', '13', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 5² + 12² = 169. c = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 3 and 4. Find the hypotenuse.', '4', '5', '6', '7', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 3² + 4² = 25. c = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 24, hypotenuse is 25. Find the other leg.', '24', '7', '1', '8', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 25² - 24² = 49. a = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 6 and 8. Find the hypotenuse.', '14', '11', '9', '10', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 6² + 8² = 100. c = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 8, hypotenuse is 10. Find the other leg.', '8', '7', '6', '2', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 10² - 8² = 36. a = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (5, 7).', '12', '√74', '5√3', '35', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(5² + 7²) = √74 = √74', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is a triangle with sides 6, 8, 10 a right triangle?', 'Yes', 'Cannot determine', 'Maybe', 'No', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', '6² + 8² = 100, 10² = 100. Yes.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 12, hypotenuse is 13. Find the other leg.', '6', '1', '5', '12', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 13² - 12² = 25. a = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 3 × 4 × 6 box.', '5', '13', '12', '√61', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(3² + 4² + 6²) = √61 = √61', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 7 and 24. Find the hypotenuse.', '24', '25', '26', '31', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 7² + 24² = 625. c = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is a triangle with sides 5, 12, 13 a right triangle?', 'Cannot determine', 'Yes', 'No', 'Maybe', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', '5² + 12² = 169, 13² = 169. Yes.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 3 and 4. Find the hypotenuse.', '7', '6', '5', '4', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 3² + 4² = 25. c = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 5 and 12. Find the hypotenuse.', '14', '17', '13', '12', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 5² + 12² = 169. c = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (4, 8).', '32', '12', '4√5', '9', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(4² + 8²) = √80 = 4√5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 6 and 8. Find the hypotenuse.', '14', '10', '9', '11', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 6² + 8² = 100. c = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 7 and 24. Find the hypotenuse.', '25', '24', '31', '26', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 7² + 24² = 625. c = 25', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (7, 8).', '√114', '√113', '56', '15', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(7² + 8²) = √113 = √113', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 5 × 3 × 3 box.', '15', '11', '√34', '√43', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(5² + 3² + 3²) = √43 = √43', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (7, 6).', '42', '√85', '√86', '13', 1,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(7² + 6²) = √85 = √85', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find distance between (0, 0) and (5, 6).', '30', '√62', '√61', '11', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Distance = √(5² + 6²) = √61 = √61', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 8, hypotenuse is 10. Find the other leg.', '8', '2', '6', '7', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 10² - 8² = 36. a = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a right triangle, legs are 5 and 12. Find the hypotenuse.', '13', '17', '14', '12', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'c² = 5² + 12² = 169. c = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Right triangle: one leg is 4, hypotenuse is 5. Find the other leg.', 'None of these', '1', '3', '4', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'a² = 5² - 4² = 9. a = 3', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is a triangle with sides 7, 24, 26 a right triangle?', 'Maybe', 'Cannot determine', 'No', 'Yes', 2,
'lc_hl_geometry', 5, 'developing', 'lc_hl', '7² + 24² = 625, 26² = 676. No.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Is a triangle with sides 8, 15, 17 a right triangle?', 'Yes', 'No', 'Maybe', 'Cannot determine', 0,
'lc_hl_geometry', 5, 'developing', 'lc_hl', '8² + 15² = 289, 17² = 289. Yes.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 5 × 4 × 6 box.', '20', '15', '√41', '√77', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(5² + 4² + 6²) = √77 = √77', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Find the space diagonal of a 3 × 3 × 4 box.', '10', '9', '3√2', '√34', 3,
'lc_hl_geometry', 5, 'developing', 'lc_hl', 'Diagonal = √(3² + 3² + 4²) = √34 = √34', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 56°. Find angle at centre (same arc).', '122', '124', '112', '56', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 56° = 112°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '180', '60', '45', '90', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 60°. Find angle at centre (same arc).', 'None of these', '60', '120', '130', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 60° = 120°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent meets radius at P. One angle is 51°. Find the other at P.', '39', '51', '90', '129', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangent ⟂ radius. Other angle = 90° - 51° = 39°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 27°. Find angle at centre (same arc).', '153', '64', '54', '27', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 27° = 54°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a cyclic quadrilateral, one angle is 83°. Find the opposite angle.', '83', '97', '107', '277', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Opposite angles sum to 180°. Opposite = 97°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '90', '45', '60', '180', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 61°. Find x.', '61', '71', '122', '119', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 61°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '90', '180', '45', '60', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a cyclic quadrilateral, one angle is 101°. Find the opposite angle.', '101', '259', '89', '79', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Opposite angles sum to 180°. Opposite = 79°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '180', '45', '60', '90', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a cyclic quadrilateral, one angle is 82°. Find the opposite angle.', '278', '108', '98', '82', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Opposite angles sum to 180°. Opposite = 98°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 61°. Find angle at centre (same arc).', '61', '119', '122', '132', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 61° = 122°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 63°. Find angle at centre (same arc).', '117', '136', '63', '126', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 63° = 126°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a cyclic quadrilateral, one angle is 107°. Find the opposite angle.', '83', '107', '253', '73', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Opposite angles sum to 180°. Opposite = 73°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent meets radius at P. One angle is 56°. Find the other at P.', '124', '34', '56', '90', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangent ⟂ radius. Other angle = 90° - 56° = 34°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 10. Find the other tangent length from P.', '12', '20', '8', '10', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 7. Find the other tangent length from P.', '5', '14', '7', '9', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 7', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 13. Find the other tangent length from P.', '26', '15', '11', '13', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 13', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 73°. Find angle at centre (same arc).', '107', '73', '146', '156', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 73° = 146°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '180', '90', '60', '45', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 14. Find the other tangent length from P.', '14', '16', '28', '12', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 12. Find the other tangent length from P.', '14', '10', '24', '12', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 51°. Find x.', '51', '129', '102', '61', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 51°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 36°. Find angle at centre (same arc).', '144', '36', '72', '82', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 36° = 72°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '60', '45', '180', '90', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 48°. Find x.', '48', '132', '58', '96', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 48°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 69°. Find x.', '138', '69', '111', '79', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 69°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 52°. Find x.', '62', '128', '52', '104', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 52°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 62°. Find x.', '62', '124', '72', '118', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 62°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 39°. Find x.', '49', '39', '78', '141', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 39°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 60°. Find angle at centre (same arc).', '60', '120', 'None of these', '130', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 60° = 120°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 44°. Find angle at centre (same arc).', '44', '136', '88', '98', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 44° = 88°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 54°. Find x.', '126', '108', '54', '64', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 54°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 10. Find the other tangent length from P.', '20', '10', '8', '12', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 61°. Find x.', '71', '61', '119', '122', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 61°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a cyclic quadrilateral, one angle is 114°. Find the opposite angle.', '66', '114', '246', '76', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Opposite angles sum to 180°. Opposite = 66°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 48°. Find x.', '96', '58', '48', '132', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 48°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 14. Find the other tangent length from P.', '28', '14', '12', '16', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 14', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 5. Find the other tangent length from P.', '3', '7', '5', '10', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '180', '90', '45', '60', 1,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 47°. Find x.', '94', '57', '133', '47', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 47°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a cyclic quadrilateral, one angle is 66°. Find the opposite angle.', '124', '66', '114', '294', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Opposite angles sum to 180°. Opposite = 114°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two angles in the same segment are x° and 47°. Find x.', '57', '133', '47', '94', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angles in same segment are equal. x = 47°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('From external point P, one tangent is 5. Find the other tangent length from P.', '3', '10', '5', '7', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangents from external point are equal. Length = 5', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 32°. Find angle at centre (same arc).', '64', '74', '148', '32', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 32° = 64°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('What is the angle in a semicircle?', '45', '180', '90', '60', 2,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle in a semicircle is always 90°.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a cyclic quadrilateral, one angle is 111°. Find the opposite angle.', '69', '249', '111', '79', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Opposite angles sum to 180°. Opposite = 69°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at circumference is 47°. Find angle at centre (same arc).', '94', '104', '133', '47', 0,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Angle at centre = 2 × 47° = 94°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent meets radius at P. One angle is 48°. Find the other at P.', '90', '132', '48', '42', 3,
'lc_hl_geometry', 6, 'developing', 'lc_hl', 'Tangent ⟂ radius. Other angle = 90° - 48° = 42°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '12', 'None of these', '6', '8', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '12', '6', 'None of these', '8', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 40° with chord PQ. Find angle in alternate segment.', '140', '50', '40', '80', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 40°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '8', 'None of these', '12', '6', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle between tangent and chord is 35°. Find inscribed angle on same chord.', '145', '55', '70', '35', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'By alternate segment theorem: 35°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '4', '8', '24', '10', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle between tangent and chord is 56°. Find inscribed angle on same chord.', '56', '112', '34', '124', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'By alternate segment theorem: 56°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '24', '10', '8', '4', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 44° with chord PQ. Find angle in alternate segment.', '46', '88', '44', '136', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 44°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '4', '8', '24', '10', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '8', '6', 'None of these', '12', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '8', '6', '12', 'None of these', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '8', '9', '10', '6', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 56° with chord PQ. Find angle in alternate segment.', '34', '124', '56', '112', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 56°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle between tangent and chord is 42°. Find inscribed angle on same chord.', '138', '48', '42', '84', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'By alternate segment theorem: 42°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '6', 'None of these', '12', '8', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '8', '6', '9', '10', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '12', '6', 'None of these', '8', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle between tangent and chord is 45°. Find inscribed angle on same chord.', 'None of these', '135', '45', '90', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'By alternate segment theorem: 45°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '4', '24', '10', '8', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '9', '10', '6', '8', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle between tangent and chord is 56°. Find inscribed angle on same chord.', '56', '34', '112', '124', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'By alternate segment theorem: 56°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 59° with chord PQ. Find angle in alternate segment.', '59', '121', '118', '31', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 59°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '10', '8', '24', '4', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '24', '8', '4', '10', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 37° with chord PQ. Find angle in alternate segment.', '143', '74', '53', '37', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 37°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '10', '24', '8', '4', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 53° with chord PQ. Find angle in alternate segment.', '127', '106', '37', '53', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 53°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '6', '8', '9', '10', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '12', '8', '6', 'None of these', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 31° with chord PQ. Find angle in alternate segment.', '59', '31', '149', '62', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 31°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '24', '10', '4', '8', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '24', '10', '4', '8', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 38° with chord PQ. Find angle in alternate segment.', '38', '52', '76', '142', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 38°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', 'None of these', '8', '12', '6', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '8', '9', '10', '6', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '10', '6', '8', '9', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle between tangent and chord is 35°. Find inscribed angle on same chord.', '35', '70', '145', '55', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'By alternate segment theorem: 35°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle between tangent and chord is 39°. Find inscribed angle on same chord.', '39', '78', '51', '141', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'By alternate segment theorem: 39°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '9', '10', '8', '6', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '6', '9', '10', '8', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Two secants: first 3, 5; second near = 4. Find second whole secant.', '6', '8', 'None of these', '12', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '3 × 8 = 4 × whole. Whole = 6', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '24', '10', '8', '4', 2,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent = 6, secant near segment = 4. Find whole secant.', '9', '8', '6', '10', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Tangent² = near × whole. 6² = 4 × whole. Whole = 9', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 70° with chord PQ. Find angle in alternate segment.', '70', '20', '110', '140', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 70°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 41° with chord PQ. Find angle in alternate segment.', '49', '139', '82', '41', 3,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 41°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '24', '8', '10', '4', 1,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '8', '4', '10', '24', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Tangent at P makes 58° with chord PQ. Find angle in alternate segment.', '58', '32', '116', '122', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', 'Alternate segment theorem: angle = 58°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Chords intersect: segments 4, 6 and 3, x. Find x.', '8', '4', '10', '24', 0,
'lc_hl_geometry', 7, 'proficient', 'lc_hl', '4 × 6 = 3 × x. x = 24/3 = 8', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 116°, 62°, 67°, x°. Find x.', '115', '245', '125', '65', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 116° - 62° - 67° = 115°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 55°. Find other angle on same leg.', '65', '305', '55', '125', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 125°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: All sides are...', 'perpendicular', 'equal', 'different', 'parallel', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallelogram: one angle is 58°. Find adjacent angle.', '68', '302', '122', '58', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Adjacent angles supplementary. = 180° - 58° = 122°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 89°, 70°, 61°, x°. Find x.', '140', '40', '150', '220', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 89° - 70° - 61° = 140°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: All sides are...', 'different', 'parallel', 'perpendicular', 'equal', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 82°, 76°, 93°, x°. Find x.', '251', '109', '71', '119', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 82° - 76° - 93° = 109°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 94°, 77°, 66°, x°. Find x.', '237', '123', '133', '57', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 94° - 77° - 66° = 123°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 73°. Find other angle on same leg.', '83', '287', '73', '107', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 107°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rectangle: Diagonals are...', 'unequal', 'perpendicular', 'parallel', 'equal and bisect each other', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rectangle: equal and bisect each other', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallelogram: one angle is 69°. Find adjacent angle.', '291', '111', '69', '79', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Adjacent angles supplementary. = 180° - 69° = 111°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 59°. Find other angle on same leg.', '121', '69', '301', '59', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 121°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rectangle: Diagonals are...', 'perpendicular', 'unequal', 'parallel', 'equal and bisect each other', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rectangle: equal and bisect each other', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 65°. Find other angle on same leg.', '65', '115', '75', '295', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 115°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 59°. Find other angle on same leg.', '121', '59', '69', '301', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 121°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which quadrilateral: One pair of parallel sides?', 'Trapezium', 'Rhombus', 'Parallelogram', 'Rectangle', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'A Trapezium.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: Diagonals are...', 'equal', 'perpendicular bisectors', 'parallel', 'not bisecting', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: perpendicular bisectors', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: All sides are...', 'parallel', 'equal', 'perpendicular', 'different', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallelogram: one angle is 81°. Find adjacent angle.', '81', '279', '91', '99', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Adjacent angles supplementary. = 180° - 81° = 99°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which quadrilateral: One pair of parallel sides?', 'Parallelogram', 'Rhombus', 'Trapezium', 'Rectangle', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'A Trapezium.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 55°. Find other angle on same leg.', '305', '55', '125', '65', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 125°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 91°, 102°, 93°, x°. Find x.', '74', '84', '106', '286', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 91° - 102° - 93° = 74°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which quadrilateral: 4 equal sides, 4 right angles?', 'Parallelogram', 'Rhombus', 'Square', 'Rectangle', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'A Square.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 75°. Find other angle on same leg.', '285', '75', '85', '105', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 105°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 113°, 86°, 119°, x°. Find x.', '138', '42', '52', '318', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 113° - 86° - 119° = 42°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 68°, 118°, 94°, x°. Find x.', '280', '80', '100', '90', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 68° - 118° - 94° = 80°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 70°. Find other angle on same leg.', '70', '290', '110', '80', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 110°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rectangle: All angles are...', '60°', '90°', '180°', '45°', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rectangle: 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: All sides are...', 'perpendicular', 'parallel', 'different', 'equal', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 68°. Find other angle on same leg.', '292', '112', '68', '78', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 112°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 79°. Find other angle on same leg.', '101', '89', '79', '281', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 101°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which quadrilateral: One pair of parallel sides?', 'Trapezium', 'Rhombus', 'Parallelogram', 'Rectangle', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'A Trapezium.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rectangle: All angles are...', '180°', '90°', '60°', '45°', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rectangle: 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 66°. Find other angle on same leg.', '294', '76', '114', '66', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 114°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 112°, 103°, 81°, x°. Find x.', '296', '116', '74', '64', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 112° - 103° - 81° = 64°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rectangle: All angles are...', '60°', '45°', '180°', '90°', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rectangle: 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which quadrilateral: 4 equal sides, 4 right angles?', 'Rectangle', 'Square', 'Rhombus', 'Parallelogram', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'A Square.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which quadrilateral: 4 right angles, opposite sides equal?', 'Square', 'Trapezium', 'Rhombus', 'Rectangle', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'A Rectangle.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallelogram: one angle is 58°. Find adjacent angle.', '68', '122', '58', '302', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Adjacent angles supplementary. = 180° - 58° = 122°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rectangle: All angles are...', '45°', '90°', '60°', '180°', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rectangle: 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 61°. Find other angle on same leg.', '61', '119', '71', '299', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 119°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallelogram: one angle is 120°. Find adjacent angle.', '130', '240', '60', '120', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Adjacent angles supplementary. = 180° - 120° = 60°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: Diagonals are...', 'not bisecting', 'equal', 'parallel', 'perpendicular bisectors', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: perpendicular bisectors', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: Diagonals are...', 'not bisecting', 'perpendicular bisectors', 'parallel', 'equal', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: perpendicular bisectors', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: All sides are...', 'equal', 'different', 'parallel', 'perpendicular', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Quadrilateral angles: 87°, 115°, 109°, x°. Find x.', '311', '49', '59', '131', 1,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Sum = 360°. x = 360° - 87° - 115° - 109° = 49°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Parallelogram: one angle is 111°. Find adjacent angle.', '69', '121', '249', '111', 0,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Adjacent angles supplementary. = 180° - 111° = 69°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Trapezium: angle on one leg is 70°. Find other angle on same leg.', '80', '70', '290', '110', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'Co-interior angles = 180°. Other = 110°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rhombus: All sides are...', 'perpendicular', 'parallel', 'different', 'equal', 3,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rhombus: equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('In a rectangle: All angles are...', '60°', '45°', '90°', '180°', 2,
'lc_hl_geometry', 8, 'proficient', 'lc_hl', 'In a rectangle: 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (2, -2) in the y-axis.', '(2, 2)', '(-2, 2)', '(-2, -2)', 'None of these', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-2, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (5, 5) by 90° anticlockwise about origin.', '(-5, 5)', '(5, -5)', '(-5, -5)', 'None of these', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-5, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (1, 7) in the x-axis.', '(1, -7)', '(7, 1)', '(-1, 7)', '(-1, -7)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in x-axis: (1, -7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (-4, 4) in the x-axis.', 'None of these', '(4, -4)', '(4, 4)', '(-4, -4)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in x-axis: (-4, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (8, -1) in the y-axis.', '(-8, -1)', '(8, 1)', '(-1, 8)', '(-8, 1)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-8, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (-3, 7) in the x-axis.', '(3, -7)', '(-3, -7)', '(3, 7)', '(7, -3)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in x-axis: (-3, -7)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (4, 5) by 90° anticlockwise about origin.', '(-4, -5)', '(-5, 4)', '(4, -5)', '(5, -4)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-5, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (3, 3) by scale factor 4 from origin.', '(4, 4)', '(7, 7)', '(12, 12)', '(13, 12)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (12, 12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (2, 3) by scale factor 2 from origin.', '(2, 2)', '(5, 6)', '(4, 6)', '(4, 5)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (4, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (4, -2) in the y-axis.', '(4, 2)', '(-2, 4)', '(-4, 2)', '(-4, -2)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-4, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (2, 3) in the x-axis.', '(2, -3)', '(-2, 3)', '(3, 2)', '(-2, -3)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in x-axis: (2, -3)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (5, -5) in the y-axis.', 'None of these', '(-5, 5)', '(5, 5)', '(-5, -5)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-5, -5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (4, 2) by scale factor 4 from origin.', '(17, 8)', '(16, 8)', '(8, 6)', '(4, 4)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (16, 8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(-5, 4) translated by (5, -3). Find image.', '(-8, 9)', '(1, 1)', '(-10, 7)', '(0, 1)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Image = (0, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (1, 2) by scale factor 3 from origin.', '(4, 5)', '(4, 6)', '(3, 3)', '(3, 6)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (3, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (1, 1) by 90° anticlockwise about origin.', 'None of these', '(-1, -1)', '(1, -1)', '(-1, 1)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-1, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (6, -4) in the y-axis.', '(-6, -4)', '(6, 4)', '(-6, 4)', '(-4, 6)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-6, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (1, -2) in the y-axis.', '(-2, 1)', '(-1, -2)', '(1, 2)', '(-1, 2)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-1, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (1, 2) by scale factor 3 from origin.', '(4, 6)', '(3, 3)', '(3, 6)', '(4, 5)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (3, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (2, 2) by scale factor 3 from origin.', '(6, 6)', '(5, 5)', '(3, 3)', '(7, 6)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (6, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (3, 2) by scale factor 2 from origin.', '(5, 4)', '(2, 2)', '(6, 4)', '(7, 4)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (6, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (5, 5) by 90° anticlockwise about origin.', 'None of these', '(-5, 5)', '(5, -5)', '(-5, -5)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-5, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (0, 6) in the x-axis.', '(6, 0)', '(0, 6)', '(0, -6)', 'None of these', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in x-axis: (0, -6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (5, 3) by 90° anticlockwise about origin.', '(3, -5)', '(-5, -3)', '(5, -3)', '(-3, 5)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-3, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (6, 0) in the y-axis.', '(-6, 0)', '(0, 6)', '(6, 0)', 'None of these', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-6, 0)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (4, 1) by 90° anticlockwise about origin.', '(1, -4)', '(4, -1)', '(-4, -1)', '(-1, 4)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-1, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(-4, -4) translated by (-5, -5). Find image.', '(1, 1)', 'None of these', '(-9, -9)', '(-8, -9)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Image = (-9, -9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(5, 1) translated by (1, 0). Find image.', '(4, 1)', '(7, 1)', '(5, 2)', '(6, 1)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Image = (6, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (1, 1) by scale factor 4 from origin.', 'None of these', '(5, 5)', '(4, 4)', '(5, 4)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (4, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (1, 1) by scale factor 4 from origin.', 'None of these', '(5, 4)', '(5, 5)', '(4, 4)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (4, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (3, -1) in the y-axis.', '(-3, 1)', '(-1, 3)', '(-3, -1)', '(3, 1)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-3, -1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (3, 2) in the y-axis.', '(3, -2)', '(2, 3)', '(-3, 2)', '(-3, -2)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-3, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (2, 4) by scale factor 3 from origin.', '(3, 3)', '(5, 7)', '(6, 12)', '(7, 12)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (6, 12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (8, -2) in the y-axis.', '(8, 2)', '(-2, 8)', '(-8, 2)', '(-8, -2)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-8, -2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (1, 1) in the y-axis.', '(-1, 1)', '(1, 1)', '(1, -1)', '(-1, -1)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-1, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (3, 3) by scale factor 2 from origin.', '(5, 5)', '(2, 2)', '(6, 6)', '(7, 6)', 2,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (6, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (-5, 4) in the x-axis.', '(5, -4)', '(4, -5)', '(5, 4)', '(-5, -4)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in x-axis: (-5, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (4, 4) by scale factor 2 from origin.', '(6, 6)', '(8, 8)', '(2, 2)', '(9, 8)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (8, 8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(3, -5) translated by (0, -4). Find image.', '(4, -9)', '(-1, -5)', '(3, -1)', '(3, -9)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Image = (3, -9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (3, 3) by scale factor 4 from origin.', '(13, 12)', '(4, 4)', '(7, 7)', '(12, 12)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (12, 12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (4, 1) by 90° anticlockwise about origin.', '(-1, 4)', '(4, -1)', '(1, -4)', '(-4, -1)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-1, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Reflect (8, -4) in the y-axis.', '(-4, 8)', '(-8, -4)', '(-8, 4)', '(8, 4)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Reflection in y-axis: (-8, -4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(-3, -3) translated by (4, -5). Find image.', '(2, -8)', '(-7, 2)', '(-8, 1)', '(1, -8)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Image = (1, -8)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (4, 3) by scale factor 3 from origin.', '(3, 3)', '(12, 9)', '(13, 9)', '(7, 6)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (12, 9)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (4, 4) by scale factor 3 from origin.', '(7, 7)', '(3, 3)', '(13, 12)', '(12, 12)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (12, 12)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (2, 1) by 90° anticlockwise about origin.', '(-1, 2)', '(2, -1)', '(1, -2)', '(-2, -1)', 0,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-1, 2)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (4, 3) by 90° anticlockwise about origin.', '(4, -3)', '(-3, 4)', '(3, -4)', '(-4, -3)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-3, 4)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Rotate (1, 5) by 90° anticlockwise about origin.', '(-1, -5)', '(5, -1)', '(1, -5)', '(-5, 1)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', '90° anticlockwise: (-5, 1)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(-2, 2) translated by (-5, 3). Find image.', '(-6, 5)', '(-7, 5)', '(3, -1)', '(1, -3)', 1,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Image = (-7, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Enlarge (3, 3) by scale factor 2 from origin.', '(5, 5)', '(2, 2)', '(7, 6)', '(6, 6)', 3,
'lc_hl_geometry', 9, 'proficient', 'lc_hl', 'Enlargement: (6, 6)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 6 from a fixed line?', 'Rectangle', 'Two parallel lines, each 6 units away', 'One line 6 away', 'Circle radius 6', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 6 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular bisector: draw arcs from A and B that...', 'have equal radius and intersect', 'don''t intersect', 'pass through midpoint', 'have different radii', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'have equal radius and intersect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 5 from a fixed line?', 'Two parallel lines, each 5 units away', 'One line 5 away', 'Circle radius 5', 'Rectangle', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 5 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 3 from a fixed line?', 'Two parallel lines, each 3 units away', 'Circle radius 3', 'Rectangle', 'One line 3 away', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 3 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'Line through A and B', 'Angle bisector', 'Perpendicular bisector of AB', 'A circle', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'Perpendicular bisector of AB', 'Line through A and B', 'Angle bisector', 'A circle', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'A circle', 'Line through A and B', 'Perpendicular bisector of AB', 'Angle bisector', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two intersecting lines?', 'Parallel line', 'Angle bisector of the lines', 'A circle', 'Perpendicular bisector', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The angle bisector(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 2 from a fixed line?', 'Circle radius 2', 'Rectangle', 'Two parallel lines, each 2 units away', 'One line 2 away', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 2 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 9 from point P?', 'Two parallel lines', 'Circle with radius 9', 'Square side 9', 'Line 9 units away', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 9.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 4 from point P?', 'Square side 4', 'Circle with radius 4', 'Two parallel lines', 'Line 4 units away', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'Line through A and B', 'Perpendicular bisector of AB', 'A circle', 'Angle bisector', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 6 from point P?', 'Square side 6', 'Line 6 units away', 'Circle with radius 6', 'Two parallel lines', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 6.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 3 from point P?', 'Two parallel lines', 'Square side 3', 'Line 3 units away', 'Circle with radius 3', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To bisect an angle, draw arcs from vertex that...', 'only cut one arm', 'cut both arms at equal distances', 'are different sizes', 'pass through vertex', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'cut both arms at equal distances', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'A circle', 'Angle bisector', 'Perpendicular bisector of AB', 'Line through A and B', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular bisector: draw arcs from A and B that...', 'have different radii', 'pass through midpoint', 'don''t intersect', 'have equal radius and intersect', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'have equal radius and intersect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 4 from point P?', 'Two parallel lines', 'Square side 4', 'Circle with radius 4', 'Line 4 units away', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 4.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'Angle bisector', 'A circle', 'Perpendicular bisector of AB', 'Line through A and B', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two intersecting lines?', 'Angle bisector of the lines', 'Parallel line', 'Perpendicular bisector', 'A circle', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The angle bisector(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'Line through A and B', 'A circle', 'Perpendicular bisector of AB', 'Angle bisector', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'A circle', 'Angle bisector', 'Line through A and B', 'Perpendicular bisector of AB', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To bisect an angle, draw arcs from vertex that...', 'are different sizes', 'pass through vertex', 'only cut one arm', 'cut both arms at equal distances', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'cut both arms at equal distances', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 3 from point P?', 'Square side 3', 'Circle with radius 3', 'Line 3 units away', 'Two parallel lines', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular bisector: draw arcs from A and B that...', 'have equal radius and intersect', 'pass through midpoint', 'have different radii', 'don''t intersect', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'have equal radius and intersect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 9 from point P?', 'Circle with radius 9', 'Two parallel lines', 'Square side 9', 'Line 9 units away', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 9.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 2 from a fixed line?', 'Rectangle', 'Two parallel lines, each 2 units away', 'Circle radius 2', 'One line 2 away', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 2 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 2 from a fixed line?', 'Two parallel lines, each 2 units away', 'Rectangle', 'One line 2 away', 'Circle radius 2', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 2 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular bisector: draw arcs from A and B that...', 'don''t intersect', 'have different radii', 'pass through midpoint', 'have equal radius and intersect', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'have equal radius and intersect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two intersecting lines?', 'Angle bisector of the lines', 'A circle', 'Parallel line', 'Perpendicular bisector', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The angle bisector(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 3 from a fixed line?', 'Rectangle', 'Circle radius 3', 'One line 3 away', 'Two parallel lines, each 3 units away', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 3 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'A circle', 'Angle bisector', 'Line through A and B', 'Perpendicular bisector of AB', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular bisector: draw arcs from A and B that...', 'pass through midpoint', 'don''t intersect', 'have different radii', 'have equal radius and intersect', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'have equal radius and intersect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To bisect an angle, draw arcs from vertex that...', 'only cut one arm', 'are different sizes', 'pass through vertex', 'cut both arms at equal distances', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'cut both arms at equal distances', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 7 from a fixed line?', 'Rectangle', 'One line 7 away', 'Two parallel lines, each 7 units away', 'Circle radius 7', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 7 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular bisector: draw arcs from A and B that...', 'pass through midpoint', 'have different radii', 'have equal radius and intersect', 'don''t intersect', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'have equal radius and intersect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two intersecting lines?', 'Angle bisector of the lines', 'A circle', 'Perpendicular bisector', 'Parallel line', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The angle bisector(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To bisect an angle, draw arcs from vertex that...', 'are different sizes', 'pass through vertex', 'only cut one arm', 'cut both arms at equal distances', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'cut both arms at equal distances', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To bisect an angle, draw arcs from vertex that...', 'cut both arms at equal distances', 'only cut one arm', 'pass through vertex', 'are different sizes', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'cut both arms at equal distances', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 3 from point P?', 'Line 3 units away', 'Two parallel lines', 'Square side 3', 'Circle with radius 3', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Circle centre P, radius 3.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two intersecting lines?', 'Angle bisector of the lines', 'Parallel line', 'Perpendicular bisector', 'A circle', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The angle bisector(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'Line through A and B', 'A circle', 'Angle bisector', 'Perpendicular bisector of AB', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 4 from a fixed line?', 'Circle radius 4', 'Rectangle', 'Two parallel lines, each 4 units away', 'One line 4 away', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 4 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 5 from a fixed line?', 'Two parallel lines, each 5 units away', 'Rectangle', 'One line 5 away', 'Circle radius 5', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 5 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To bisect an angle, draw arcs from vertex that...', 'cut both arms at equal distances', 'only cut one arm', 'are different sizes', 'pass through vertex', 0,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'cut both arms at equal distances', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Perpendicular bisector: draw arcs from A and B that...', 'pass through midpoint', 'have different radii', 'have equal radius and intersect', 'don''t intersect', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'have equal radius and intersect', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two intersecting lines?', 'Parallel line', 'Perpendicular bisector', 'Angle bisector of the lines', 'A circle', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The angle bisector(s).', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus equidistant from two points A and B?', 'Line through A and B', 'Angle bisector', 'A circle', 'Perpendicular bisector of AB', 3,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'The perpendicular bisector of AB.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 5 from a fixed line?', 'One line 5 away', 'Rectangle', 'Two parallel lines, each 5 units away', 'Circle radius 5', 2,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 5 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Locus at distance 2 from a fixed line?', 'Rectangle', 'Two parallel lines, each 2 units away', 'One line 2 away', 'Circle radius 2', 1,
'lc_hl_geometry', 10, 'advanced', 'lc_hl', 'Two parallel lines, 2 units from given line.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction ends when we...', 'use all info', 'draw conclusion', 'find pattern', 'reach a logical contradiction', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'reach a logical contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''Given'' in a proof refers to...', 'Assumption', 'Conclusion', 'What to prove', 'Information stated in problem', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Information stated in problem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive of ''If P then Q'':', 'If not P then not Q', 'If not Q then not P', 'P and Q', 'If Q then P', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'If not Q then not P', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For SAS congruence, we need two sides and...', 'hypotenuse', 'any angle', 'opposite angle', 'included angle equal', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'included angle equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction starts by...', 'using induction', 'drawing diagram', 'assuming opposite of what to prove', 'proving directly', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'assuming opposite of what to prove', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction ends when we...', 'reach a logical contradiction', 'use all info', 'find pattern', 'draw conclusion', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'reach a logical contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P → Q and P is true, then...', 'P is false', 'Cannot determine', 'Q is true', 'Q is false', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Q is true', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction ends when we...', 'draw conclusion', 'use all info', 'find pattern', 'reach a logical contradiction', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'reach a logical contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive of ''If P then Q'':', 'If Q then P', 'If not P then not Q', 'P and Q', 'If not Q then not P', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'If not Q then not P', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P → Q and Q is false, then...', 'P is false', 'P is true', 'Cannot determine', 'Q is true', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'P is false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove lines parallel using alternate angles...', 'show sum = 360°', 'show they differ', 'show they are equal', 'show sum = 90°', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'show they are equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For SAS congruence, we need two sides and...', 'opposite angle', 'included angle equal', 'hypotenuse', 'any angle', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'included angle equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P → Q and P is true, then...', 'Q is true', 'Q is false', 'P is false', 'Cannot determine', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Q is true', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''To Prove'' refers to...', 'First step', 'Given info', 'What we need to show', 'An axiom', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'What we need to show', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction starts by...', 'using induction', 'proving directly', 'drawing diagram', 'assuming opposite of what to prove', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'assuming opposite of what to prove', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''Given'' in a proof refers to...', 'Assumption', 'What to prove', 'Information stated in problem', 'Conclusion', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Information stated in problem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P → Q and Q is false, then...', 'Cannot determine', 'P is false', 'Q is true', 'P is true', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'P is false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Pythagoras', 'Alternate angles', 'Isosceles', 'Circle theorem', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction starts by...', 'assuming opposite of what to prove', 'drawing diagram', 'using induction', 'proving directly', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'assuming opposite of what to prove', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''To Prove'' refers to...', 'Given info', 'An axiom', 'What we need to show', 'First step', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'What we need to show', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P → Q and P is true, then...', 'Cannot determine', 'P is false', 'Q is false', 'Q is true', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Q is true', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Pythagoras', 'Circle theorem', 'Isosceles', 'Alternate angles', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove lines parallel using alternate angles...', 'show sum = 360°', 'show they differ', 'show they are equal', 'show sum = 90°', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'show they are equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove lines parallel using alternate angles...', 'show they differ', 'show sum = 360°', 'show they are equal', 'show sum = 90°', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'show they are equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For SAS congruence, we need two sides and...', 'any angle', 'opposite angle', 'hypotenuse', 'included angle equal', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'included angle equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction ends when we...', 'draw conclusion', 'reach a logical contradiction', 'find pattern', 'use all info', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'reach a logical contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''To Prove'' refers to...', 'First step', 'Given info', 'An axiom', 'What we need to show', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'What we need to show', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Circle theorem', 'Isosceles', 'Alternate angles', 'Pythagoras', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Isosceles', 'Alternate angles', 'Pythagoras', 'Circle theorem', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Two equal sides → equal opposite angles''?', 'Congruence', 'Pythagoras', 'Isosceles triangle theorem', 'Angle sum', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Isosceles triangle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction starts by...', 'assuming opposite of what to prove', 'proving directly', 'drawing diagram', 'using induction', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'assuming opposite of what to prove', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction ends when we...', 'reach a logical contradiction', 'draw conclusion', 'use all info', 'find pattern', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'reach a logical contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Pythagoras', 'Alternate angles', 'Circle theorem', 'Isosceles', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Contrapositive of ''If P then Q'':', 'If not P then not Q', 'If Q then P', 'P and Q', 'If not Q then not P', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'If not Q then not P', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''To Prove'' refers to...', 'Given info', 'What we need to show', 'First step', 'An axiom', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'What we need to show', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('For SAS congruence, we need two sides and...', 'any angle', 'included angle equal', 'hypotenuse', 'opposite angle', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'included angle equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''Given'' in a proof refers to...', 'Assumption', 'Conclusion', 'What to prove', 'Information stated in problem', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Information stated in problem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''Given'' in a proof refers to...', 'Information stated in problem', 'Assumption', 'Conclusion', 'What to prove', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Information stated in problem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Pythagoras', 'Alternate angles', 'Isosceles', 'Circle theorem', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Two equal sides → equal opposite angles''?', 'Angle sum', 'Congruence', 'Isosceles triangle theorem', 'Pythagoras', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Isosceles triangle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction ends when we...', 'find pattern', 'draw conclusion', 'use all info', 'reach a logical contradiction', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'reach a logical contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''Given'' in a proof refers to...', 'Assumption', 'Conclusion', 'Information stated in problem', 'What to prove', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'Information stated in problem', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove lines parallel using alternate angles...', 'show they are equal', 'show sum = 90°', 'show sum = 360°', 'show they differ', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'show they are equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('If P → Q and Q is false, then...', 'P is true', 'Q is true', 'Cannot determine', 'P is false', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'P is false', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''To Prove'' refers to...', 'What we need to show', 'An axiom', 'Given info', 'First step', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'What we need to show', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Alternate angles', 'Pythagoras', 'Circle theorem', 'Isosceles', 2,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('To prove lines parallel using alternate angles...', 'show they differ', 'show they are equal', 'show sum = 360°', 'show sum = 90°', 1,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'show they are equal', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Proof by contradiction ends when we...', 'use all info', 'draw conclusion', 'find pattern', 'reach a logical contradiction', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'reach a logical contradiction', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Which theorem: ''Angle at centre = 2 × angle at circumference''?', 'Alternate angles', 'Isosceles', 'Pythagoras', 'Circle theorem', 3,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'The Circle theorem.', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('''To Prove'' refers to...', 'What we need to show', 'First step', 'Given info', 'An axiom', 0,
'lc_hl_geometry', 11, 'advanced', 'lc_hl', 'What we need to show', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 13, base 10. Find height.', '13', '√145', '12', '10', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 13² - 5² = 144. h = 12', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cyclic quad ABCD: angle A = 63°. Find exterior angle at C.', '63', '73', '297', '117', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior at C = opposite interior at A = 63°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar figures have scale factor 4. What is area ratio?', '4', '5', '16', '8', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Area ratio = k² = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cyclic quad ABCD: angle A = 100°. Find exterior angle at C.', '80', '110', '260', '100', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior at C = opposite interior at A = 100°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 42°, angle B = 48°. Find exterior angle at C.', '90', '48', 'None of these', '42', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 42° + 48° = 90°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 130°. Find angle at circumference (same arc).', '75', '115', '130', '65', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 130° = 65°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 14, base 10. Find height.', '10', '14', '2√43', '3√19', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 14² - 5² = 171. h = 3√19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar figures have scale factor 4. What is area ratio?', '4', '5', '8', '16', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Area ratio = k² = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 139°. Find angle at circumference (same arc).', '111', '69', '79', '139', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 139° = 69°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(2, 3) reflected in y-axis then translated by (4, 2). Find image.', '(-2, 3)', '(1, 5)', '(6, 5)', '(2, 5)', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'After reflection: (-2, 3). After translation: (2, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(2, 3) reflected in y-axis then translated by (4, 2). Find image.', '(2, 5)', '(6, 5)', '(-2, 3)', '(1, 5)', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'After reflection: (-2, 3). After translation: (2, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 9, base 6. Find height.', '6', '6√2', '9', '√73', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 9² - 3² = 72. h = 6√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar figures have scale factor 4. What is area ratio?', '5', '16', '8', '4', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Area ratio = k² = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar figures have scale factor 4. What is area ratio?', '4', '16', '8', '5', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Area ratio = k² = 16', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 12, base 8. Find height.', '12', '√129', '8√2', '8', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 12² - 4² = 128. h = 8√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 41°, angle B = 33°. Find exterior angle at C.', '33', '41', '106', '74', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 41° + 33° = 74°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cyclic quad ABCD: angle A = 86°. Find exterior angle at C.', '274', '94', '96', '86', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior at C = opposite interior at A = 86°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 42°, angle B = 30°. Find exterior angle at C.', '72', '108', '30', '42', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 42° + 30° = 72°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 8, base 6. Find height.', '2√14', '8', '√55', '6', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 8² - 3² = 55. h = √55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(2, 3) reflected in y-axis then translated by (4, 2). Find image.', '(1, 5)', '(2, 5)', '(-2, 3)', '(6, 5)', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'After reflection: (-2, 3). After translation: (2, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 65°. Find angle at circumference (same arc).', '65', '32', '148', '42', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 65° = 32°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 14, base 12. Find height.', '√161', '4√10', '12', '14', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 14² - 6² = 160. h = 4√10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 31°, angle B = 48°. Find exterior angle at C.', '31', '101', '48', '79', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 31° + 48° = 79°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 34°, angle B = 31°. Find exterior angle at C.', '31', '115', '34', '65', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 34° + 31° = 65°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cyclic quad ABCD: angle A = 66°. Find exterior angle at C.', '294', '114', '66', '76', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior at C = opposite interior at A = 66°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 26°, angle B = 23°. Find exterior angle at C.', '23', '49', '131', '26', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 26° + 23° = 49°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(2, 3) reflected in y-axis then translated by (4, 2). Find image.', '(6, 5)', '(1, 5)', '(2, 5)', '(-2, 3)', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'After reflection: (-2, 3). After translation: (2, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 12, base 10. Find height.', '12', '10', '√119', '2√30', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 12² - 5² = 119. h = √119', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(2, 3) reflected in y-axis then translated by (4, 2). Find image.', '(2, 5)', '(1, 5)', '(-2, 3)', '(6, 5)', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'After reflection: (-2, 3). After translation: (2, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 33°, angle B = 45°. Find exterior angle at C.', '33', '102', '45', '78', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 33° + 45° = 78°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 41°, angle B = 24°. Find exterior angle at C.', '41', '24', '65', '115', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 41° + 24° = 65°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 82°. Find angle at circumference (same arc).', '41', '82', '51', '139', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 82° = 41°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 113°. Find angle at circumference (same arc).', '66', '113', '56', '124', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 113° = 56°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(2, 3) reflected in y-axis then translated by (4, 2). Find image.', '(-2, 3)', '(2, 5)', '(1, 5)', '(6, 5)', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'After reflection: (-2, 3). After translation: (2, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 107°. Find angle at circumference (same arc).', '127', '107', '53', '63', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 107° = 53°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 99°. Find angle at circumference (same arc).', '59', '99', '49', '131', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 99° = 49°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 8, base 6. Find height.', '6', '2√14', '8', '√55', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 8² - 3² = 55. h = √55', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 11, base 8. Find height.', '11', '8', '√105', '√106', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 11² - 4² = 105. h = √105', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 79°. Find angle at circumference (same arc).', '49', '79', '39', '141', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 79° = 39°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cyclic quad ABCD: angle A = 66°. Find exterior angle at C.', '114', '66', '294', '76', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior at C = opposite interior at A = 66°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 14, base 12. Find height.', '14', '12', '4√10', '√161', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 14² - 6² = 160. h = 4√10', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Cyclic quad ABCD: angle A = 96°. Find exterior angle at C.', '96', '84', '264', '106', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior at C = opposite interior at A = 96°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 14, base 10. Find height.', '10', '2√43', '3√19', '14', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 14² - 5² = 171. h = 3√19', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('(2, 3) reflected in y-axis then translated by (4, 2). Find image.', '(2, 5)', '(-2, 3)', '(1, 5)', '(6, 5)', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'After reflection: (-2, 3). After translation: (2, 5)', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 137°. Find angle at circumference (same arc).', '112', '137', '68', '78', 2,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 137° = 68°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Triangle: angle A = 40°, angle B = 22°. Find exterior angle at C.', '62', '22', '118', '40', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Exterior = 40° + 22° = 62°', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar figures have scale factor 2. What is area ratio?', '2', 'None of these', '3', '4', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Area ratio = k² = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Similar figures have scale factor 2. What is area ratio?', '3', 'None of these', '2', '4', 3,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'Area ratio = k² = 4', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Isosceles triangle: equal sides 9, base 6. Find height.', '9', '6√2', '6', '√73', 1,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', 'h² = 9² - 3² = 72. h = 6√2', 1);
INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('Angle at centre = 98°. Find angle at circumference (same arc).', '49', '131', '59', '98', 0,
'lc_hl_geometry', 12, 'advanced', 'lc_hl', '= ½ × 98° = 49°', 1);