#!/usr/bin/env python3
"""
LC Ordinary Level - Trigonometry Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level × 12 levels) for LC OL Trigonometry
Based on SEC Paper Analysis 2019-2025 (375 marks - #1 priority Paper 2)

OL Trigonometry Focus:
- Right-angled triangles (SOH-CAH-TOA)
- Sine Rule
- Cosine Rule
- Area of triangle (½absinC)
- Bearings and navigation
- Angles of elevation/depression
- Applied problems (gradient, swimming markers, etc.)

Levels:
1. Right-Angled Triangles - Sides
2. Right-Angled Triangles - Angles
3. SOH-CAH-TOA Practice
4. Sine Rule - Finding Sides
5. Sine Rule - Finding Angles
6. Cosine Rule - Finding Sides
7. Cosine Rule - Finding Angles
8. Area of Triangle
9. Bearings
10. Angles of Elevation/Depression
11. Applied Problems
12. Mastery Challenge
"""

import random
import math

TOPIC = 'lc_ol_trigonometry'
MODE = 'lc_ol'

LEVEL_TITLES = [
    'Right Triangles - Sides',
    'Right Triangles - Angles',
    'SOH-CAH-TOA Practice',
    'Sine Rule - Sides',
    'Sine Rule - Angles',
    'Cosine Rule - Sides',
    'Cosine Rule - Angles',
    'Area of Triangle',
    'Bearings',
    'Elevation & Depression',
    'Applied Problems',
    'Mastery Challenge'
]

def make_unique_options(correct, distractors):
    """Create 4 unique options with correct answer randomly placed"""
    correct_str = str(correct)
    unique_wrong = []
    for d in distractors:
        d_str = str(d)
        if d_str != correct_str and d_str not in unique_wrong:
            unique_wrong.append(d_str)
    while len(unique_wrong) < 3:
        unique_wrong.append("Cannot determine")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)


def generate_level_1():
    """Level 1: Right-Angled Triangles - Finding Sides"""
    questions = []
    
    # Common Pythagorean triples and variations
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15), (12, 16, 20)]
    
    # Type 1: Find hypotenuse using Pythagoras (20 questions)
    for _ in range(20):
        a, b, c = random.choice(triples)
        scale = random.choice([1, 2])
        a, b, c = a * scale, b * scale, c * scale
        
        question = f"In a right-angled triangle, the two shorter sides are {a} cm and {b} cm. Find the hypotenuse."
        correct = f"{c} cm"
        distractors = [
            f"{a + b} cm",
            f"{c + 1} cm",
            f"{int(math.sqrt(a*a + b*b) + 2)} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"c² = a² + b² = {a}² + {b}² = {a*a} + {b*b} = {c*c}. So c = {c} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find a shorter side (20 questions)
    for _ in range(20):
        a, b, c = random.choice(triples)
        scale = random.choice([1, 2])
        a, b, c = a * scale, b * scale, c * scale
        
        question = f"In a right-angled triangle, the hypotenuse is {c} cm and one side is {a} cm. Find the other side."
        correct = f"{b} cm"
        distractors = [
            f"{c - a} cm",
            f"{b + 1} cm",
            f"{c + a} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"b² = c² - a² = {c}² - {a}² = {c*c} - {a*a} = {b*b}. So b = {b} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Identify the hypotenuse (10 questions)
    for _ in range(10):
        a, b, c = random.choice(triples)
        sides = [a, b, c]
        random.shuffle(sides)
        
        question = f"Three sides of a triangle are {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm. If this is a right-angled triangle, which is the hypotenuse?"
        correct = f"{c} cm"
        distractors = [f"{a} cm", f"{b} cm", f"{a + b} cm"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"The hypotenuse is the longest side = {c} cm. Check: {a}² + {b}² = {a*a + b*b} = {c}² ✓"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_2():
    """Level 2: Right-Angled Triangles - Finding Angles"""
    questions = []
    
    # Type 1: Find angle using tan (20 questions)
    for _ in range(20):
        opposite = random.choice([3, 4, 5, 6, 8, 10, 12])
        adjacent = random.choice([3, 4, 5, 6, 8, 10, 12])
        angle = math.degrees(math.atan(opposite / adjacent))
        angle_rounded = round(angle, 1)
        
        question = f"In a right-angled triangle, opposite = {opposite} cm and adjacent = {adjacent} cm. Find angle θ."
        correct = f"{angle_rounded}°"
        distractors = [
            f"{round(90 - angle, 1)}°",
            f"{round(angle + 10, 1)}°",
            f"{round(math.degrees(math.atan(adjacent / opposite)), 1)}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"tan θ = opp/adj = {opposite}/{adjacent} = {opposite/adjacent:.3f}. θ = tan⁻¹({opposite/adjacent:.3f}) = {angle_rounded}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find angle using sin (15 questions)
    for _ in range(15):
        opposite = random.choice([3, 4, 5, 6, 7, 8])
        hypotenuse = random.choice([10, 12, 13, 15, 17])
        if opposite >= hypotenuse:
            opposite = hypotenuse - 3
        
        angle = math.degrees(math.asin(opposite / hypotenuse))
        angle_rounded = round(angle, 1)
        
        question = f"In a right-angled triangle, opposite = {opposite} cm and hypotenuse = {hypotenuse} cm. Find angle θ."
        correct = f"{angle_rounded}°"
        distractors = [
            f"{round(90 - angle, 1)}°",
            f"{round(angle + 15, 1)}°",
            f"{round(opposite / hypotenuse * 100, 1)}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"sin θ = opp/hyp = {opposite}/{hypotenuse} = {opposite/hypotenuse:.3f}. θ = sin⁻¹({opposite/hypotenuse:.3f}) = {angle_rounded}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find the third angle (15 questions)
    for _ in range(15):
        angle1 = random.choice([30, 35, 40, 45, 50, 55, 60])
        angle2 = 90
        angle3 = 180 - 90 - angle1
        
        question = f"A right-angled triangle has angles of 90° and {angle1}°. Find the third angle."
        correct = f"{angle3}°"
        distractors = [
            f"{180 - angle1}°",
            f"{angle1}°",
            f"{90 - angle3}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Angles in a triangle sum to 180°. Third angle = 180° - 90° - {angle1}° = {angle3}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_3():
    """Level 3: SOH-CAH-TOA Practice"""
    questions = []
    
    # Type 1: Find side using sin (17 questions)
    for _ in range(17):
        angle = random.choice([30, 35, 40, 45, 50, 55, 60])
        hypotenuse = random.choice([10, 12, 15, 20])
        opposite = hypotenuse * math.sin(math.radians(angle))
        opposite_rounded = round(opposite, 2)
        
        question = f"In a right-angled triangle, angle θ = {angle}° and hypotenuse = {hypotenuse} cm. Find the opposite side."
        correct = f"{opposite_rounded} cm"
        distractors = [
            f"{round(hypotenuse * math.cos(math.radians(angle)), 2)} cm",
            f"{round(opposite + 2, 2)} cm",
            f"{hypotenuse} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"sin {angle}° = opp/hyp. opp = {hypotenuse} × sin {angle}° = {hypotenuse} × {math.sin(math.radians(angle)):.4f} = {opposite_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find side using cos (17 questions)
    for _ in range(17):
        angle = random.choice([30, 35, 40, 45, 50, 55, 60])
        hypotenuse = random.choice([10, 12, 15, 20])
        adjacent = hypotenuse * math.cos(math.radians(angle))
        adjacent_rounded = round(adjacent, 2)
        
        question = f"In a right-angled triangle, angle θ = {angle}° and hypotenuse = {hypotenuse} cm. Find the adjacent side."
        correct = f"{adjacent_rounded} cm"
        distractors = [
            f"{round(hypotenuse * math.sin(math.radians(angle)), 2)} cm",
            f"{round(adjacent + 3, 2)} cm",
            f"{hypotenuse} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"cos {angle}° = adj/hyp. adj = {hypotenuse} × cos {angle}° = {hypotenuse} × {math.cos(math.radians(angle)):.4f} = {adjacent_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find side using tan (16 questions)
    for _ in range(16):
        angle = random.choice([30, 35, 40, 45, 50, 55, 60])
        adjacent = random.choice([8, 10, 12, 15])
        opposite = adjacent * math.tan(math.radians(angle))
        opposite_rounded = round(opposite, 2)
        
        question = f"In a right-angled triangle, angle θ = {angle}° and adjacent = {adjacent} cm. Find the opposite side."
        correct = f"{opposite_rounded} cm"
        distractors = [
            f"{round(adjacent / math.tan(math.radians(angle)), 2)} cm",
            f"{round(opposite + 2, 2)} cm",
            f"{adjacent} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"tan {angle}° = opp/adj. opp = {adjacent} × tan {angle}° = {adjacent} × {math.tan(math.radians(angle)):.4f} = {opposite_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_4():
    """Level 4: Sine Rule - Finding Sides"""
    questions = []
    
    # Sine Rule: a/sinA = b/sinB = c/sinC
    
    for _ in range(50):
        angle_A = random.choice([40, 45, 50, 55, 60, 65, 70])
        angle_B = random.choice([40, 45, 50, 55, 60, 65])
        if angle_A + angle_B >= 170:
            angle_B = 180 - angle_A - 30
        angle_C = 180 - angle_A - angle_B
        
        side_a = random.choice([8, 10, 12, 14, 15, 16, 18, 20])
        
        # Find side b using sine rule: b/sinB = a/sinA
        side_b = side_a * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_A))
        side_b_rounded = round(side_b, 1)
        
        question = f"In triangle ABC: angle A = {angle_A}°, angle B = {angle_B}°, and side a = {side_a} cm. Find side b."
        correct = f"{side_b_rounded} cm"
        distractors = [
            f"{round(side_b + 2, 1)} cm",
            f"{round(side_a * angle_B / angle_A, 1)} cm",
            f"{round(side_b * 1.2, 1)} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Sine Rule: b/sin B = a/sin A. b = {side_a} × sin {angle_B}° / sin {angle_A}° = {side_b_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_5():
    """Level 5: Sine Rule - Finding Angles"""
    questions = []
    
    for _ in range(50):
        angle_A = random.choice([40, 45, 50, 55, 60, 65, 70])
        side_a = random.choice([10, 12, 14, 15, 16, 18])
        side_b = random.choice([8, 9, 10, 11, 12, 13])
        
        # Ensure valid triangle
        if side_b >= side_a:
            side_b = side_a - 2
        
        # Find angle B using sine rule: sinB/b = sinA/a
        sin_B = side_b * math.sin(math.radians(angle_A)) / side_a
        if sin_B > 1:
            sin_B = 0.8
        angle_B = math.degrees(math.asin(sin_B))
        angle_B_rounded = round(angle_B, 1)
        
        question = f"In triangle ABC: angle A = {angle_A}°, side a = {side_a} cm, side b = {side_b} cm. Find angle B."
        correct = f"{angle_B_rounded}°"
        distractors = [
            f"{round(180 - angle_A - angle_B, 1)}°",
            f"{round(angle_B + 10, 1)}°",
            f"{round(angle_A * side_b / side_a, 1)}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Sine Rule: sin B/b = sin A/a. sin B = {side_b} × sin {angle_A}° / {side_a} = {sin_B:.4f}. B = {angle_B_rounded}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_6():
    """Level 6: Cosine Rule - Finding Sides"""
    questions = []
    
    # Cosine Rule: a² = b² + c² - 2bc·cos A
    
    for _ in range(50):
        side_b = random.choice([8, 10, 12, 14, 15])
        side_c = random.choice([8, 10, 12, 14, 15])
        angle_A = random.choice([40, 50, 60, 70, 80, 100, 110, 120])
        
        # Calculate side a
        a_squared = side_b**2 + side_c**2 - 2*side_b*side_c*math.cos(math.radians(angle_A))
        side_a = math.sqrt(a_squared)
        side_a_rounded = round(side_a, 1)
        
        question = f"In triangle ABC: b = {side_b} cm, c = {side_c} cm, angle A = {angle_A}°. Find side a."
        correct = f"{side_a_rounded} cm"
        distractors = [
            f"{round(side_a + 2, 1)} cm",
            f"{round(math.sqrt(side_b**2 + side_c**2), 1)} cm",
            f"{round(side_a * 1.15, 1)} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Cosine Rule: a² = b² + c² - 2bc·cos A = {side_b}² + {side_c}² - 2({side_b})({side_c})cos {angle_A}° = {a_squared:.1f}. a = {side_a_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_7():
    """Level 7: Cosine Rule - Finding Angles"""
    questions = []
    
    # Cosine Rule rearranged: cos A = (b² + c² - a²) / 2bc
    
    for _ in range(50):
        # Use valid triangle sides
        side_a = random.choice([7, 8, 9, 10, 11, 12])
        side_b = random.choice([8, 9, 10, 11, 12, 13])
        side_c = random.choice([6, 7, 8, 9, 10, 11])
        
        # Check triangle inequality
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            side_c = (side_a + side_b) // 2
        
        # Calculate angle A
        cos_A = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
        if cos_A > 1:
            cos_A = 0.9
        if cos_A < -1:
            cos_A = -0.9
        angle_A = math.degrees(math.acos(cos_A))
        angle_A_rounded = round(angle_A, 1)
        
        question = f"In triangle ABC: a = {side_a} cm, b = {side_b} cm, c = {side_c} cm. Find angle A."
        correct = f"{angle_A_rounded}°"
        distractors = [
            f"{round(180 - angle_A, 1)}°",
            f"{round(angle_A + 15, 1)}°",
            f"{round(angle_A - 10, 1)}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"cos A = (b² + c² - a²)/(2bc) = ({side_b}² + {side_c}² - {side_a}²)/(2×{side_b}×{side_c}) = {cos_A:.4f}. A = {angle_A_rounded}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_8():
    """Level 8: Area of Triangle"""
    questions = []
    
    # Area = ½ab·sin C
    
    # Type 1: Calculate area given two sides and included angle (35 questions)
    for _ in range(35):
        side_a = random.choice([6, 8, 10, 12, 14, 15])
        side_b = random.choice([6, 8, 10, 12, 14, 15])
        angle_C = random.choice([30, 45, 50, 60, 70, 80, 90, 100, 110, 120])
        
        area = 0.5 * side_a * side_b * math.sin(math.radians(angle_C))
        area_rounded = round(area, 1)
        
        question = f"Find the area of triangle ABC where a = {side_a} cm, b = {side_b} cm, and angle C = {angle_C}°."
        correct = f"{area_rounded} cm²"
        distractors = [
            f"{round(0.5 * side_a * side_b, 1)} cm²",
            f"{round(area + 5, 1)} cm²",
            f"{round(side_a * side_b, 1)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Area = ½ab·sin C = ½ × {side_a} × {side_b} × sin {angle_C}° = {area_rounded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Find side given area (15 questions)
    for _ in range(15):
        side_a = random.choice([8, 10, 12, 14])
        angle_C = random.choice([30, 45, 60, 90])
        area = random.choice([20, 24, 30, 36, 40, 48])
        
        # area = ½ × a × b × sin C, so b = 2×area / (a × sin C)
        side_b = (2 * area) / (side_a * math.sin(math.radians(angle_C)))
        side_b_rounded = round(side_b, 1)
        
        question = f"Triangle ABC has area {area} cm², side a = {side_a} cm, angle C = {angle_C}°. Find side b."
        correct = f"{side_b_rounded} cm"
        distractors = [
            f"{round(side_b + 3, 1)} cm",
            f"{round(2 * area / side_a, 1)} cm",
            f"{round(area / side_a, 1)} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Area = ½ab·sin C. {area} = ½ × {side_a} × b × sin {angle_C}°. b = {side_b_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_9():
    """Level 9: Bearings"""
    questions = []
    
    # Type 1: Simple bearing questions (25 questions)
    bearings_info = [
        ("North", 0), ("East", 90), ("South", 180), ("West", 270),
        ("North-East", 45), ("South-East", 135), ("South-West", 225), ("North-West", 315)
    ]
    
    for _ in range(25):
        direction, bearing = random.choice(bearings_info)
        
        question = f"What is the bearing of {direction}?"
        correct = f"{bearing:03d}°"
        distractors = [
            f"{(bearing + 90) % 360:03d}°",
            f"{(bearing + 180) % 360:03d}°",
            f"{(bearing + 45) % 360:03d}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Bearings are measured clockwise from North. {direction} = {bearing:03d}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Back bearing (15 questions)
    for _ in range(15):
        bearing = random.choice([30, 45, 60, 75, 90, 120, 135, 150, 210, 240, 270, 300, 330])
        back_bearing = (bearing + 180) % 360
        
        question = f"A ship sails on a bearing of {bearing:03d}°. What is the back bearing?"
        correct = f"{back_bearing:03d}°"
        distractors = [
            f"{(bearing + 90) % 360:03d}°",
            f"{360 - bearing:03d}°",
            f"{bearing:03d}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Back bearing = original ± 180°. {bearing}° + 180° = {back_bearing}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Bearing with distance (10 questions)
    for _ in range(10):
        bearing = random.choice([30, 45, 60, 90, 120, 135])
        distance = random.choice([5, 8, 10, 12, 15])
        
        # Find how far East (or North)
        east = distance * math.sin(math.radians(bearing))
        north = distance * math.cos(math.radians(bearing))
        east_rounded = round(east, 1)
        
        question = f"A boat travels {distance} km on a bearing of {bearing:03d}°. How far East has it travelled?"
        correct = f"{east_rounded} km"
        distractors = [
            f"{round(north, 1)} km",
            f"{distance} km",
            f"{round(east + 2, 1)} km"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"East = {distance} × sin {bearing}° = {east_rounded} km"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_10():
    """Level 10: Angles of Elevation and Depression"""
    questions = []
    
    # Type 1: Angle of elevation - find height (20 questions)
    for _ in range(20):
        distance = random.choice([20, 25, 30, 40, 50, 60, 80, 100])
        angle = random.choice([25, 30, 35, 40, 45, 50, 55, 60])
        
        height = distance * math.tan(math.radians(angle))
        height_rounded = round(height, 1)
        
        question = f"From {distance} m away, the angle of elevation to the top of a building is {angle}°. Find the height."
        correct = f"{height_rounded} m"
        distractors = [
            f"{round(height + 10, 1)} m",
            f"{round(distance * math.sin(math.radians(angle)), 1)} m",
            f"{distance} m"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"tan {angle}° = height/{distance}. Height = {distance} × tan {angle}° = {height_rounded} m"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Angle of depression - find distance (15 questions)
    for _ in range(15):
        height = random.choice([15, 20, 25, 30, 40, 50])
        angle = random.choice([20, 25, 30, 35, 40, 45])
        
        distance = height / math.tan(math.radians(angle))
        distance_rounded = round(distance, 1)
        
        question = f"From a cliff {height} m high, the angle of depression to a boat is {angle}°. How far is the boat from the base?"
        correct = f"{distance_rounded} m"
        distractors = [
            f"{round(height * math.tan(math.radians(angle)), 1)} m",
            f"{height} m",
            f"{round(distance + 15, 1)} m"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"tan {angle}° = {height}/distance. Distance = {height}/tan {angle}° = {distance_rounded} m"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Find the angle (15 questions)
    for _ in range(15):
        height = random.choice([10, 15, 20, 25, 30])
        distance = random.choice([15, 20, 25, 30, 40, 50])
        
        angle = math.degrees(math.atan(height / distance))
        angle_rounded = round(angle, 1)
        
        question = f"A tree is {height} m tall. From {distance} m away, what is the angle of elevation to the top?"
        correct = f"{angle_rounded}°"
        distractors = [
            f"{round(90 - angle, 1)}°",
            f"{round(angle + 10, 1)}°",
            f"{round(height / distance * 10, 1)}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"tan θ = {height}/{distance} = {height/distance:.3f}. θ = tan⁻¹({height/distance:.3f}) = {angle_rounded}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_11():
    """Level 11: Applied Problems"""
    questions = []
    
    # Type 1: Gradient as percentage (15 questions)
    for _ in range(15):
        rise = random.choice([5, 8, 10, 12, 15])
        run = random.choice([50, 80, 100, 120, 150])
        
        gradient_percent = (rise / run) * 100
        gradient_rounded = round(gradient_percent, 1)
        
        question = f"A road rises {rise} m over a horizontal distance of {run} m. What is the gradient as a percentage?"
        correct = f"{gradient_rounded}%"
        distractors = [
            f"{round(run / rise, 1)}%",
            f"{rise}%",
            f"{round(gradient_percent + 2, 1)}%"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Gradient = (rise/run) × 100 = ({rise}/{run}) × 100 = {gradient_rounded}%"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Distance across a lake (15 questions)
    for _ in range(15):
        side_a = random.choice([80, 100, 120, 150])
        side_b = random.choice([60, 80, 100, 120])
        angle = random.choice([40, 50, 60, 70, 80])
        
        # Using cosine rule to find distance across
        c_squared = side_a**2 + side_b**2 - 2*side_a*side_b*math.cos(math.radians(angle))
        distance = math.sqrt(c_squared)
        distance_rounded = round(distance, 1)
        
        question = f"Points A and B are on opposite sides of a lake. From C, CA = {side_a} m, CB = {side_b} m, angle ACB = {angle}°. Find AB."
        correct = f"{distance_rounded} m"
        distractors = [
            f"{round(distance + 20, 1)} m",
            f"{side_a + side_b} m",
            f"{round(math.sqrt(side_a**2 + side_b**2), 1)} m"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Cosine Rule: AB² = {side_a}² + {side_b}² - 2({side_a})({side_b})cos {angle}°. AB = {distance_rounded} m"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Navigation/sailing problems (20 questions)
    for _ in range(20):
        leg1 = random.choice([5, 8, 10, 12])
        bearing1 = random.choice([30, 45, 60])
        leg2 = random.choice([6, 8, 10])
        
        # Calculate displacement East and North
        east1 = leg1 * math.sin(math.radians(bearing1))
        north1 = leg1 * math.cos(math.radians(bearing1))
        
        total_east = round(east1, 1)
        total_north = round(north1, 1)
        
        question = f"A boat sails {leg1} km on bearing {bearing1:03d}°. How far North has it travelled?"
        correct = f"{total_north} km"
        distractors = [
            f"{total_east} km",
            f"{leg1} km",
            f"{round(total_north + 2, 1)} km"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"North = {leg1} × cos {bearing1}° = {total_north} km"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    # Type 1: Combined sine and cosine rule (15 questions)
    for _ in range(15):
        angle_A = random.choice([50, 55, 60, 65, 70])
        angle_B = random.choice([40, 45, 50, 55])
        side_c = random.choice([10, 12, 14, 15])
        
        angle_C = 180 - angle_A - angle_B
        
        # Find side a using sine rule
        side_a = side_c * math.sin(math.radians(angle_A)) / math.sin(math.radians(angle_C))
        side_a_rounded = round(side_a, 1)
        
        question = f"In triangle ABC: A = {angle_A}°, B = {angle_B}°, c = {side_c} cm. Find side a."
        correct = f"{side_a_rounded} cm"
        distractors = [
            f"{round(side_a + 2, 1)} cm",
            f"{side_c} cm",
            f"{round(side_c * angle_A / angle_C, 1)} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"C = 180° - {angle_A}° - {angle_B}° = {angle_C}°. Sine rule: a = {side_c} × sin {angle_A}°/sin {angle_C}° = {side_a_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Area and perimeter combined (15 questions)
    for _ in range(15):
        side_a = random.choice([8, 10, 12])
        side_b = random.choice([10, 12, 14])
        angle_C = random.choice([45, 60, 90, 120])
        
        area = 0.5 * side_a * side_b * math.sin(math.radians(angle_C))
        
        # Find side c using cosine rule
        c_squared = side_a**2 + side_b**2 - 2*side_a*side_b*math.cos(math.radians(angle_C))
        side_c = math.sqrt(c_squared)
        
        perimeter = side_a + side_b + side_c
        perimeter_rounded = round(perimeter, 1)
        
        question = f"Triangle ABC: a = {side_a} cm, b = {side_b} cm, C = {angle_C}°. Find the perimeter."
        correct = f"{perimeter_rounded} cm"
        distractors = [
            f"{side_a + side_b + round(area, 1)} cm",
            f"{round(perimeter + 3, 1)} cm",
            f"{side_a + side_b} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"c = √({side_a}² + {side_b}² - 2({side_a})({side_b})cos {angle_C}°) = {round(side_c, 1)} cm. Perimeter = {perimeter_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Real-world multi-step (20 questions)
    for _ in range(20):
        height = random.choice([50, 60, 80, 100])
        angle1 = random.choice([30, 35, 40])
        angle2 = random.choice([50, 55, 60])
        
        # Distance at first observation
        dist1 = height / math.tan(math.radians(angle1))
        # Distance at second observation
        dist2 = height / math.tan(math.radians(angle2))
        
        walked = dist1 - dist2
        walked_rounded = round(walked, 1)
        
        question = f"From point A, angle of elevation to a {height} m tower is {angle1}°. Walking towards, it becomes {angle2}°. How far walked?"
        correct = f"{walked_rounded} m"
        distractors = [
            f"{round(dist1, 1)} m",
            f"{round(dist2, 1)} m",
            f"{round(walked + 10, 1)} m"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Dist 1 = {height}/tan {angle1}° = {round(dist1, 1)} m. Dist 2 = {height}/tan {angle2}° = {round(dist2, 1)} m. Walked = {walked_rounded} m"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    return questions


def main():
    """Generate all questions and output SQL"""
    all_questions = []
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12,
    ]
    
    print(f"Generating questions for {TOPIC}...")
    print("=" * 60)
    
    for level, generator in enumerate(generators, 1):
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level:2d} ({LEVEL_TITLES[level-1]:25s}): {len(questions)} questions")
    
    print("=" * 60)
    print(f"Total questions generated: {len(all_questions)}")
    
    # Generate SQL statements
    sql_statements = []
    for q in all_questions:
        q_text = q['question_text'].replace("'", "''")
        opt_a = q['option_a'].replace("'", "''")
        opt_b = q['option_b'].replace("'", "''")
        opt_c = q['option_c'].replace("'", "''")
        opt_d = q['option_d'].replace("'", "''")
        expl = q['explanation'].replace("'", "''")
        
        sql = f"""INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('{q_text}', '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', {q['correct_idx']},
'{TOPIC}', {q['difficulty']}, '{q['difficulty_band']}', '{MODE}', '{expl}', 1);"""
        sql_statements.append(sql)
    
    # Create complete SQL file
    complete_sql = f"""-- LC Ordinary Level - Trigonometry Complete SQL
-- Generated: 2025-12-15
-- Total: {len(all_questions)} questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Trigonometry topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT '{TOPIC}', 'Trigonometry', id, '📐', 3, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = '{TOPIC}';

-- Insert questions
{chr(10).join(sql_statements)}

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = '{TOPIC}';
"""
    
    with open('lc_ol_trigonometry_complete.sql', 'w', encoding='utf-8') as f:
        f.write(complete_sql)
    print(f"\nSQL written to: lc_ol_trigonometry_complete.sql")
    
    return all_questions


if __name__ == '__main__':
    main()
