#!/usr/bin/env python3
"""
LC Ordinary Level - Mensuration Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level × 12 levels) for LC OL Mensuration
Based on SEC Paper Analysis 2019-2025 (350 marks - #2 priority Paper 2)

OL Mensuration Focus:
- Perimeter and circumference
- Area of 2D shapes
- Surface area of 3D shapes
- Volume of prisms, cylinders, cones, spheres
- Composite shapes
- Nets of 3D shapes

Levels:
1. Perimeter of 2D Shapes
2. Area of Rectangles & Triangles
3. Area of Circles & Sectors
4. Area of Composite Shapes
5. Surface Area - Cuboids
6. Surface Area - Cylinders
7. Surface Area - Cones & Spheres
8. Volume - Cuboids & Prisms
9. Volume - Cylinders
10. Volume - Cones & Pyramids
11. Volume - Spheres & Composite
12. Mastery Challenge
"""

import random
import math

TOPIC = 'lc_ol_mensuration'
MODE = 'lc_ol'

LEVEL_TITLES = [
    'Perimeter of 2D Shapes',
    'Area - Rectangles & Triangles',
    'Area - Circles & Sectors',
    'Area - Composite Shapes',
    'Surface Area - Cuboids',
    'Surface Area - Cylinders',
    'Surface Area - Cones & Spheres',
    'Volume - Cuboids & Prisms',
    'Volume - Cylinders',
    'Volume - Cones & Pyramids',
    'Volume - Spheres & Composite',
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
    """Level 1: Perimeter of 2D Shapes"""
    questions = []
    
    # Type 1: Rectangle perimeter (20 questions)
    for _ in range(20):
        length = random.randint(5, 20)
        width = random.randint(3, 15)
        perimeter = 2 * (length + width)
        
        question = f"Find the perimeter of a rectangle with length {length} cm and width {width} cm."
        correct = f"{perimeter} cm"
        distractors = [
            f"{length + width} cm",
            f"{length * width} cm",
            f"{perimeter + 4} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Perimeter = 2(l + w) = 2({length} + {width}) = 2 × {length + width} = {perimeter} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Square perimeter (15 questions)
    for _ in range(15):
        side = random.randint(4, 18)
        perimeter = 4 * side
        
        question = f"Find the perimeter of a square with side {side} cm."
        correct = f"{perimeter} cm"
        distractors = [
            f"{side * side} cm",
            f"{side * 2} cm",
            f"{perimeter + side} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Perimeter = 4 × side = 4 × {side} = {perimeter} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Triangle perimeter (15 questions)
    for _ in range(15):
        a = random.randint(5, 12)
        b = random.randint(5, 12)
        c = random.randint(max(abs(a-b)+1, 3), a+b-1)  # Triangle inequality
        perimeter = a + b + c
        
        question = f"Find the perimeter of a triangle with sides {a} cm, {b} cm, and {c} cm."
        correct = f"{perimeter} cm"
        distractors = [
            f"{a * b} cm",
            f"{perimeter + 3} cm",
            f"{(a + b + c) // 2} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Perimeter = {a} + {b} + {c} = {perimeter} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_2():
    """Level 2: Area of Rectangles & Triangles"""
    questions = []
    
    # Type 1: Rectangle area (20 questions)
    for _ in range(20):
        length = random.randint(5, 15)
        width = random.randint(3, 12)
        area = length * width
        
        question = f"Find the area of a rectangle with length {length} cm and width {width} cm."
        correct = f"{area} cm²"
        distractors = [
            f"{2 * (length + width)} cm²",
            f"{length + width} cm²",
            f"{area + length} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Area = length × width = {length} × {width} = {area} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Triangle area (20 questions)
    for _ in range(20):
        base = random.randint(6, 16)
        height = random.randint(4, 14)
        area = base * height / 2
        
        question = f"Find the area of a triangle with base {base} cm and height {height} cm."
        correct = f"{area} cm²" if area == int(area) else f"{area:.1f} cm²"
        distractors = [
            f"{base * height} cm²",
            f"{base + height} cm²",
            f"{area + base} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Area = ½ × base × height = ½ × {base} × {height} = {area} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Square area (10 questions)
    for _ in range(10):
        side = random.randint(5, 15)
        area = side * side
        
        question = f"Find the area of a square with side {side} cm."
        correct = f"{area} cm²"
        distractors = [
            f"{4 * side} cm²",
            f"{side * 2} cm²",
            f"{area + side} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Area = side² = {side}² = {area} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_3():
    """Level 3: Area of Circles & Sectors"""
    questions = []
    
    # Type 1: Circle area (20 questions)
    for _ in range(20):
        radius = random.randint(3, 12)
        area = math.pi * radius ** 2
        area_rounded = round(area, 2)
        
        question = f"Find the area of a circle with radius {radius} cm. (Use π = 3.14)"
        correct = f"{round(3.14 * radius ** 2, 2)} cm²"
        distractors = [
            f"{round(2 * 3.14 * radius, 2)} cm²",
            f"{round(3.14 * radius, 2)} cm²",
            f"{round(3.14 * radius ** 2 + 10, 2)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Area = πr² = 3.14 × {radius}² = 3.14 × {radius**2} = {round(3.14 * radius**2, 2)} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Circumference (15 questions)
    for _ in range(15):
        radius = random.randint(3, 10)
        circumference = 2 * 3.14 * radius
        circumference_rounded = round(circumference, 2)
        
        question = f"Find the circumference of a circle with radius {radius} cm. (Use π = 3.14)"
        correct = f"{circumference_rounded} cm"
        distractors = [
            f"{round(3.14 * radius ** 2, 2)} cm",
            f"{round(3.14 * radius, 2)} cm",
            f"{round(circumference + 5, 2)} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Circumference = 2πr = 2 × 3.14 × {radius} = {circumference_rounded} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Sector area (15 questions)
    for _ in range(15):
        radius = random.randint(4, 10)
        angle = random.choice([45, 60, 90, 120, 180])
        full_area = 3.14 * radius ** 2
        sector_area = full_area * angle / 360
        sector_rounded = round(sector_area, 2)
        
        question = f"Find the area of a sector with radius {radius} cm and angle {angle}°. (Use π = 3.14)"
        correct = f"{sector_rounded} cm²"
        distractors = [
            f"{round(full_area, 2)} cm²",
            f"{round(sector_area * 2, 2)} cm²",
            f"{round(sector_area + radius, 2)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Sector area = (θ/360) × πr² = ({angle}/360) × 3.14 × {radius}² = {sector_rounded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_4():
    """Level 4: Area of Composite Shapes"""
    questions = []
    
    # Type 1: Rectangle + triangle (20 questions)
    for _ in range(20):
        rect_l = random.randint(8, 15)
        rect_w = random.randint(5, 10)
        tri_base = rect_l
        tri_height = random.randint(3, 7)
        
        rect_area = rect_l * rect_w
        tri_area = tri_base * tri_height / 2
        total = rect_area + tri_area
        
        question = f"A shape consists of a rectangle ({rect_l}×{rect_w} cm) with a triangle (base {tri_base} cm, height {tri_height} cm) on top. Find the total area."
        correct = f"{total} cm²" if total == int(total) else f"{total:.1f} cm²"
        distractors = [
            f"{rect_area} cm²",
            f"{total + rect_w} cm²",
            f"{rect_area + tri_height} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Rectangle = {rect_area} cm². Triangle = {tri_area} cm². Total = {total} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Rectangle with semicircle (15 questions)
    for _ in range(15):
        rect_l = random.randint(10, 16)
        rect_w = random.randint(6, 10)
        radius = rect_w / 2
        
        rect_area = rect_l * rect_w
        semi_area = 3.14 * radius ** 2 / 2
        total = rect_area + semi_area
        total_rounded = round(total, 2)
        
        question = f"A rectangle ({rect_l}×{rect_w} cm) has a semicircle (diameter {rect_w} cm) attached. Find total area. (π = 3.14)"
        correct = f"{total_rounded} cm²"
        distractors = [
            f"{rect_area} cm²",
            f"{round(rect_area + 3.14 * radius ** 2, 2)} cm²",
            f"{round(total + 10, 2)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Rectangle = {rect_area}. Semicircle = ½πr² = {round(semi_area, 2)}. Total = {total_rounded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Shape with hole (15 questions)
    for _ in range(15):
        outer_side = random.randint(10, 16)
        inner_side = random.randint(3, outer_side - 4)
        
        outer_area = outer_side ** 2
        inner_area = inner_side ** 2
        shaded = outer_area - inner_area
        
        question = f"A square ({outer_side}×{outer_side} cm) has a smaller square ({inner_side}×{inner_side} cm) cut from its center. Find the remaining area."
        correct = f"{shaded} cm²"
        distractors = [
            f"{outer_area} cm²",
            f"{inner_area} cm²",
            f"{outer_area + inner_area} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Remaining = {outer_area} - {inner_area} = {shaded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_5():
    """Level 5: Surface Area - Cuboids"""
    questions = []
    
    # Type 1: Cuboid surface area (30 questions)
    for _ in range(30):
        l = random.randint(4, 12)
        w = random.randint(3, 10)
        h = random.randint(2, 8)
        
        sa = 2 * (l*w + l*h + w*h)
        
        question = f"Find the surface area of a cuboid with dimensions {l} cm × {w} cm × {h} cm."
        correct = f"{sa} cm²"
        distractors = [
            f"{l * w * h} cm²",
            f"{l*w + l*h + w*h} cm²",
            f"{sa + l*w} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"SA = 2(lw + lh + wh) = 2({l}×{w} + {l}×{h} + {w}×{h}) = 2({l*w} + {l*h} + {w*h}) = {sa} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Cube surface area (20 questions)
    for _ in range(20):
        side = random.randint(3, 12)
        sa = 6 * side ** 2
        
        question = f"Find the surface area of a cube with side {side} cm."
        correct = f"{sa} cm²"
        distractors = [
            f"{side ** 3} cm²",
            f"{side ** 2} cm²",
            f"{4 * side ** 2} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"SA = 6s² = 6 × {side}² = 6 × {side**2} = {sa} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_6():
    """Level 6: Surface Area - Cylinders"""
    questions = []
    
    # Type 1: Curved surface area (20 questions)
    for _ in range(20):
        r = random.randint(3, 8)
        h = random.randint(5, 15)
        csa = 2 * 3.14 * r * h
        csa_rounded = round(csa, 2)
        
        question = f"Find the curved surface area of a cylinder with radius {r} cm and height {h} cm. (π = 3.14)"
        correct = f"{csa_rounded} cm²"
        distractors = [
            f"{round(3.14 * r ** 2 * h, 2)} cm²",
            f"{round(3.14 * r * h, 2)} cm²",
            f"{round(csa + 50, 2)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"CSA = 2πrh = 2 × 3.14 × {r} × {h} = {csa_rounded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Total surface area (30 questions)
    for _ in range(30):
        r = random.randint(3, 7)
        h = random.randint(5, 12)
        csa = 2 * 3.14 * r * h
        circles = 2 * 3.14 * r ** 2
        total = csa + circles
        total_rounded = round(total, 2)
        
        question = f"Find the total surface area of a closed cylinder with radius {r} cm and height {h} cm. (π = 3.14)"
        correct = f"{total_rounded} cm²"
        distractors = [
            f"{round(csa, 2)} cm²",
            f"{round(circles, 2)} cm²",
            f"{round(total + 20, 2)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Total SA = 2πrh + 2πr² = {round(csa, 2)} + {round(circles, 2)} = {total_rounded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_7():
    """Level 7: Surface Area - Cones & Spheres"""
    questions = []
    
    # Type 1: Sphere surface area (25 questions)
    for _ in range(25):
        r = random.randint(3, 10)
        sa = 4 * 3.14 * r ** 2
        sa_rounded = round(sa, 2)
        
        question = f"Find the surface area of a sphere with radius {r} cm. (π = 3.14)"
        correct = f"{sa_rounded} cm²"
        distractors = [
            f"{round(3.14 * r ** 2, 2)} cm²",
            f"{round(4/3 * 3.14 * r ** 3, 2)} cm²",
            f"{round(sa + 30, 2)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"SA = 4πr² = 4 × 3.14 × {r}² = {sa_rounded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Cone curved surface area (25 questions)
    for _ in range(25):
        r = random.randint(3, 8)
        l = random.randint(r + 2, r + 10)  # slant height > radius
        csa = 3.14 * r * l
        csa_rounded = round(csa, 2)
        
        question = f"Find the curved surface area of a cone with radius {r} cm and slant height {l} cm. (π = 3.14)"
        correct = f"{csa_rounded} cm²"
        distractors = [
            f"{round(3.14 * r ** 2, 2)} cm²",
            f"{round(3.14 * r * l + 3.14 * r ** 2, 2)} cm²",
            f"{round(csa + 20, 2)} cm²"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"CSA = πrl = 3.14 × {r} × {l} = {csa_rounded} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_8():
    """Level 8: Volume - Cuboids & Prisms"""
    questions = []
    
    # Type 1: Cuboid volume (25 questions)
    for _ in range(25):
        l = random.randint(4, 12)
        w = random.randint(3, 10)
        h = random.randint(2, 8)
        volume = l * w * h
        
        question = f"Find the volume of a cuboid with dimensions {l} cm × {w} cm × {h} cm."
        correct = f"{volume} cm³"
        distractors = [
            f"{2 * (l*w + l*h + w*h)} cm³",
            f"{l + w + h} cm³",
            f"{volume + l*w} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = l × w × h = {l} × {w} × {h} = {volume} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Cube volume (15 questions)
    for _ in range(15):
        side = random.randint(3, 10)
        volume = side ** 3
        
        question = f"Find the volume of a cube with side {side} cm."
        correct = f"{volume} cm³"
        distractors = [
            f"{6 * side ** 2} cm³",
            f"{side ** 2} cm³",
            f"{4 * side ** 3} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = s³ = {side}³ = {volume} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Triangular prism (10 questions)
    for _ in range(10):
        base = random.randint(4, 10)
        height = random.randint(3, 8)
        length = random.randint(5, 12)
        tri_area = base * height / 2
        volume = tri_area * length
        
        question = f"A triangular prism has triangle base {base} cm, height {height} cm, and length {length} cm. Find the volume."
        correct = f"{volume} cm³" if volume == int(volume) else f"{volume:.1f} cm³"
        distractors = [
            f"{base * height * length} cm³",
            f"{tri_area} cm³",
            f"{volume + length} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = Area of triangle × length = (½ × {base} × {height}) × {length} = {tri_area} × {length} = {volume} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_9():
    """Level 9: Volume - Cylinders"""
    questions = []
    
    # Type 1: Cylinder volume (35 questions)
    for _ in range(35):
        r = random.randint(3, 10)
        h = random.randint(5, 15)
        volume = 3.14 * r ** 2 * h
        volume_rounded = round(volume, 2)
        
        question = f"Find the volume of a cylinder with radius {r} cm and height {h} cm. (π = 3.14)"
        correct = f"{volume_rounded} cm³"
        distractors = [
            f"{round(2 * 3.14 * r * h, 2)} cm³",
            f"{round(3.14 * r * h, 2)} cm³",
            f"{round(volume + 50, 2)} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = πr²h = 3.14 × {r}² × {h} = 3.14 × {r**2} × {h} = {volume_rounded} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Find height given volume (15 questions)
    for _ in range(15):
        r = random.randint(3, 7)
        h = random.randint(5, 12)
        volume = round(3.14 * r ** 2 * h, 2)
        
        question = f"A cylinder has radius {r} cm and volume {volume} cm³. Find its height. (π = 3.14)"
        correct = f"{h} cm"
        distractors = [
            f"{h + 2} cm",
            f"{round(volume / (3.14 * r), 1)} cm",
            f"{r} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"h = V / (πr²) = {volume} / (3.14 × {r}²) = {volume} / {round(3.14 * r**2, 2)} = {h} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_10():
    """Level 10: Volume - Cones & Pyramids"""
    questions = []
    
    # Type 1: Cone volume (25 questions)
    for _ in range(25):
        r = random.randint(3, 8)
        h = random.randint(5, 12)
        volume = (1/3) * 3.14 * r ** 2 * h
        volume_rounded = round(volume, 2)
        
        question = f"Find the volume of a cone with radius {r} cm and height {h} cm. (π = 3.14)"
        correct = f"{volume_rounded} cm³"
        distractors = [
            f"{round(3.14 * r ** 2 * h, 2)} cm³",
            f"{round(volume * 2, 2)} cm³",
            f"{round(volume + 20, 2)} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = ⅓πr²h = ⅓ × 3.14 × {r}² × {h} = {volume_rounded} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Square pyramid volume (25 questions)
    for _ in range(25):
        base = random.randint(4, 10)
        h = random.randint(5, 12)
        base_area = base ** 2
        volume = (1/3) * base_area * h
        volume_rounded = round(volume, 2) if volume != int(volume) else int(volume)
        
        question = f"Find the volume of a square-based pyramid with base side {base} cm and height {h} cm."
        correct = f"{volume_rounded} cm³"
        distractors = [
            f"{base_area * h} cm³",
            f"{round(volume * 2, 2)} cm³",
            f"{base_area} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = ⅓ × base area × height = ⅓ × {base_area} × {h} = {volume_rounded} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_11():
    """Level 11: Volume - Spheres & Composite"""
    questions = []
    
    # Type 1: Sphere volume (25 questions)
    for _ in range(25):
        r = random.randint(3, 9)
        volume = (4/3) * 3.14 * r ** 3
        volume_rounded = round(volume, 2)
        
        question = f"Find the volume of a sphere with radius {r} cm. (π = 3.14)"
        correct = f"{volume_rounded} cm³"
        distractors = [
            f"{round(4 * 3.14 * r ** 2, 2)} cm³",
            f"{round(3.14 * r ** 3, 2)} cm³",
            f"{round(volume + 50, 2)} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = (4/3)πr³ = (4/3) × 3.14 × {r}³ = {volume_rounded} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Hemisphere volume (15 questions)
    for _ in range(15):
        r = random.randint(3, 8)
        volume = (2/3) * 3.14 * r ** 3
        volume_rounded = round(volume, 2)
        
        question = f"Find the volume of a hemisphere with radius {r} cm. (π = 3.14)"
        correct = f"{volume_rounded} cm³"
        distractors = [
            f"{round((4/3) * 3.14 * r ** 3, 2)} cm³",
            f"{round(2 * 3.14 * r ** 2, 2)} cm³",
            f"{round(volume * 2, 2)} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = ½ × (4/3)πr³ = (2/3)πr³ = (2/3) × 3.14 × {r}³ = {volume_rounded} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Composite - cylinder + cone (10 questions)
    for _ in range(10):
        r = random.randint(3, 6)
        h_cyl = random.randint(6, 10)
        h_cone = random.randint(3, 6)
        
        v_cyl = 3.14 * r ** 2 * h_cyl
        v_cone = (1/3) * 3.14 * r ** 2 * h_cone
        total = v_cyl + v_cone
        total_rounded = round(total, 2)
        
        question = f"A solid has a cylinder (r={r}, h={h_cyl}) with a cone (r={r}, h={h_cone}) on top. Find total volume. (π=3.14)"
        correct = f"{total_rounded} cm³"
        distractors = [
            f"{round(v_cyl, 2)} cm³",
            f"{round(v_cyl + 3.14 * r ** 2 * h_cone, 2)} cm³",
            f"{round(total + 50, 2)} cm³"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Cylinder = {round(v_cyl, 2)} cm³. Cone = {round(v_cone, 2)} cm³. Total = {total_rounded} cm³"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    # Type 1: Find missing dimension (15 questions)
    for _ in range(15):
        l = random.randint(5, 10)
        w = random.randint(4, 8)
        h = random.randint(3, 7)
        volume = l * w * h
        
        question = f"A cuboid has volume {volume} cm³. If length = {l} cm and width = {w} cm, find the height."
        correct = f"{h} cm"
        distractors = [
            f"{h + 2} cm",
            f"{volume // (l * w) + 1} cm",
            f"{w} cm"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"h = V / (l × w) = {volume} / ({l} × {w}) = {volume} / {l * w} = {h} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Unit conversion in volume (15 questions)
    for _ in range(15):
        side_cm = random.randint(10, 30)
        volume_cm3 = side_cm ** 3
        volume_litres = volume_cm3 / 1000
        
        question = f"A cube has side {side_cm} cm. What is its volume in litres? (1 litre = 1000 cm³)"
        correct = f"{volume_litres} litres"
        distractors = [
            f"{volume_cm3} litres",
            f"{volume_litres * 10} litres",
            f"{side_cm} litres"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = {side_cm}³ = {volume_cm3} cm³ = {volume_cm3}/1000 = {volume_litres} litres"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Real-world problems (20 questions)
    for _ in range(20):
        r = random.randint(5, 10)
        h = random.randint(15, 25)
        volume = round(3.14 * r ** 2 * h, 2)
        volume_litres = round(volume / 1000, 2)
        
        question = f"A cylindrical tank has radius {r} cm and height {h} cm. How many litres of water can it hold? (π=3.14)"
        correct = f"{volume_litres} litres"
        distractors = [
            f"{volume} litres",
            f"{round(volume_litres + 1, 2)} litres",
            f"{round(3.14 * r * h / 1000, 2)} litres"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Volume = πr²h = {volume} cm³ = {volume}/1000 = {volume_litres} litres"
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
    complete_sql = f"""-- LC Ordinary Level - Mensuration Complete SQL
-- Generated: 2025-12-15
-- Total: {len(all_questions)} questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Mensuration topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT '{TOPIC}', 'Measurement', id, '📏', 5, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = '{TOPIC}';

-- Insert questions
{chr(10).join(sql_statements)}

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = '{TOPIC}';
"""
    
    with open('lc_ol_mensuration_complete.sql', 'w', encoding='utf-8') as f:
        f.write(complete_sql)
    print(f"\nSQL written to: lc_ol_mensuration_complete.sql")
    
    return all_questions


if __name__ == '__main__':
    main()
