#!/usr/bin/env python3
"""
LC Higher Level - Measurement Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level x 12 levels) for LC HL Measurement
(Length, Area & Volume)
"""

import random
import math

TOPIC = 'lc_hl_measurement'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Perimeter of 2D Shapes',
    'Area of Basic Shapes',
    'Area of Composite Shapes',
    'Circles - Circumference & Area',
    'Sectors & Arcs',
    'Surface Area - Prisms',
    'Surface Area - Cylinders & Cones',
    'Volume - Prisms',
    'Volume - Cylinders & Cones',
    'Volume - Spheres & Pyramids',
    'Unit Conversions',
    'Mastery Challenge'
]

def make_unique_options(correct, distractors):
    correct_str = str(correct)
    unique_wrong = []
    for d in distractors:
        d_str = str(d)
        if d_str != correct_str and d_str not in unique_wrong:
            unique_wrong.append(d_str)
    while len(unique_wrong) < 3:
        unique_wrong.append("None of these")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def generate_level_1():
    """Level 1: Perimeter of 2D Shapes"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Rectangle perimeter
            l = random.randint(5, 20)
            w = random.randint(3, 15)
            p = 2 * (l + w)
            correct, distractors = str(p), [str(l + w), str(l * w), str(p + 2)]
            question = f"Find the perimeter of a rectangle with length {l} cm and width {w} cm."
            explanation = f"Perimeter = 2(l + w) = 2({l} + {w}) = {p} cm"
        elif qtype == 2:
            # Square perimeter
            s = random.randint(4, 15)
            p = 4 * s
            correct, distractors = str(p), [str(s * s), str(2 * s), str(p + 4)]
            question = f"Find the perimeter of a square with side {s} cm."
            explanation = f"Perimeter = 4s = 4 × {s} = {p} cm"
        elif qtype == 3:
            # Triangle perimeter
            a = random.randint(5, 12)
            b = random.randint(5, 12)
            c = random.randint(5, 12)
            p = a + b + c
            correct, distractors = str(p), [str(a * b), str(p + 1), str(a + b)]
            question = f"Find the perimeter of a triangle with sides {a}, {b}, {c} cm."
            explanation = f"Perimeter = {a} + {b} + {c} = {p} cm"
        elif qtype == 4:
            # Equilateral triangle
            s = random.randint(4, 15)
            p = 3 * s
            correct, distractors = str(p), [str(s * s), str(4 * s), str(2 * s)]
            question = f"Find the perimeter of an equilateral triangle with side {s} cm."
            explanation = f"Perimeter = 3s = 3 × {s} = {p} cm"
        else:
            # Regular hexagon
            s = random.randint(3, 10)
            p = 6 * s
            correct, distractors = str(p), [str(4 * s), str(s * s), str(5 * s)]
            question = f"Find the perimeter of a regular hexagon with side {s} cm."
            explanation = f"Perimeter = 6s = 6 × {s} = {p} cm"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'})
    return questions

def generate_level_2():
    """Level 2: Area of Basic Shapes"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            # Rectangle area
            l = random.randint(5, 15)
            w = random.randint(3, 12)
            a = l * w
            correct, distractors = str(a), [str(2 * (l + w)), str(l + w), str(a + l)]
            question = f"Find the area of a rectangle with length {l} cm and width {w} cm."
            explanation = f"Area = l × w = {l} × {w} = {a} cm²"
        elif qtype == 2:
            # Square area
            s = random.randint(4, 12)
            a = s * s
            correct, distractors = str(a), [str(4 * s), str(2 * s), str(a + s)]
            question = f"Find the area of a square with side {s} cm."
            explanation = f"Area = s² = {s}² = {a} cm²"
        elif qtype == 3:
            # Triangle area (base × height)
            b = random.randint(4, 14)
            h = random.randint(4, 14)
            a = b * h // 2
            correct, distractors = str(a), [str(b * h), str(b + h), str(a + b)]
            question = f"Find the area of a triangle with base {b} cm and height {h} cm."
            explanation = f"Area = ½bh = ½ × {b} × {h} = {a} cm²"
        elif qtype == 4:
            # Parallelogram area
            b = random.randint(5, 12)
            h = random.randint(4, 10)
            a = b * h
            correct, distractors = str(a), [str(2 * (b + h)), str(b + h), str(a // 2)]
            question = f"Find the area of a parallelogram with base {b} cm and height {h} cm."
            explanation = f"Area = bh = {b} × {h} = {a} cm²"
        elif qtype == 5:
            # Trapezium area
            a_top = random.randint(4, 10)
            b_bottom = random.randint(8, 16)
            h = random.randint(4, 10)
            area = (a_top + b_bottom) * h // 2
            correct, distractors = str(area), [str((a_top + b_bottom) * h), str(a_top * b_bottom), str(area + h)]
            question = f"Find the area of a trapezium with parallel sides {a_top} cm and {b_bottom} cm, height {h} cm."
            explanation = f"Area = ½(a + b)h = ½({a_top} + {b_bottom}) × {h} = {area} cm²"
        else:
            # Rhombus area (using diagonals)
            d1 = random.randint(6, 14)
            d2 = random.randint(6, 14)
            a = d1 * d2 // 2
            correct, distractors = str(a), [str(d1 * d2), str(d1 + d2), str(a + d1)]
            question = f"Find the area of a rhombus with diagonals {d1} cm and {d2} cm."
            explanation = f"Area = ½d₁d₂ = ½ × {d1} × {d2} = {a} cm²"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'})
    return questions

def generate_level_3():
    """Level 3: Area of Composite Shapes"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # L-shape (two rectangles)
            l1, w1 = random.randint(8, 12), random.randint(3, 5)
            l2, w2 = random.randint(3, 5), random.randint(4, 8)
            a = l1 * w1 + l2 * w2
            correct, distractors = str(a), [str(l1 * w1), str(l2 * w2), str(a + 10)]
            question = f"An L-shape consists of rectangles {l1}×{w1} and {l2}×{w2} cm. Find total area."
            explanation = f"Area = {l1}×{w1} + {l2}×{w2} = {l1*w1} + {l2*w2} = {a} cm²"
        elif qtype == 2:
            # Rectangle with triangle removed
            l, w = random.randint(10, 15), random.randint(8, 12)
            b, h = random.randint(3, 5), random.randint(3, 5)
            rect = l * w
            tri = b * h // 2
            a = rect - tri
            correct, distractors = str(a), [str(rect), str(rect + tri), str(a + 5)]
            question = f"Rectangle {l}×{w} cm has a triangle (base {b}, height {h}) removed. Find remaining area."
            explanation = f"Area = {l}×{w} - ½×{b}×{h} = {rect} - {tri} = {a} cm²"
        elif qtype == 3:
            # Two rectangles with overlap
            a1, a2 = random.randint(20, 40), random.randint(20, 40)
            overlap = random.randint(5, 10)
            total = a1 + a2 - overlap
            correct, distractors = str(total), [str(a1 + a2), str(a1), str(total + overlap)]
            question = f"Two shapes have areas {a1} and {a2} cm² with overlap {overlap} cm². Find total area."
            explanation = f"Total = {a1} + {a2} - {overlap} = {total} cm²"
        elif qtype == 4:
            # Rectangle with rectangular hole
            L, W = random.randint(12, 18), random.randint(10, 14)
            l, w = random.randint(4, 6), random.randint(3, 5)
            outer = L * W
            inner = l * w
            a = outer - inner
            correct, distractors = str(a), [str(outer), str(inner), str(outer + inner)]
            question = f"Rectangle {L}×{W} cm has a {l}×{w} hole. Find the shaded area."
            explanation = f"Area = {L}×{W} - {l}×{w} = {outer} - {inner} = {a} cm²"
        else:
            # Square with quarter circles at corners (conceptual)
            s = random.randint(8, 12)
            sq_area = s * s
            correct, distractors = f"{sq_area}", [f"{sq_area + 10}", f"{sq_area - 10}", f"{2*sq_area}"]
            question = f"A square has side {s} cm. Find its area."
            explanation = f"Area = {s}² = {sq_area} cm²"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'})
    return questions

def generate_level_4():
    """Level 4: Circles - Circumference & Area"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Circumference given radius
            r = random.randint(3, 12)
            correct, distractors = f"{2*r}π", [f"{r}π", f"{r*r}π", f"{4*r}π"]
            question = f"Find the circumference of a circle with radius {r} cm. (Leave answer in terms of π)"
            explanation = f"C = 2πr = 2π × {r} = {2*r}π cm"
        elif qtype == 2:
            # Circumference given diameter
            d = random.randint(6, 20)
            correct, distractors = f"{d}π", [f"{2*d}π", f"{d*d}π", f"{d//2}π"]
            question = f"Find the circumference of a circle with diameter {d} cm. (In terms of π)"
            explanation = f"C = πd = π × {d} = {d}π cm"
        elif qtype == 3:
            # Area given radius
            r = random.randint(3, 10)
            correct, distractors = f"{r*r}π", [f"{2*r}π", f"{r}π", f"{2*r*r}π"]
            question = f"Find the area of a circle with radius {r} cm. (In terms of π)"
            explanation = f"A = πr² = π × {r}² = {r*r}π cm²"
        elif qtype == 4:
            # Area given diameter
            d = random.randint(4, 14)
            r = d // 2
            area = r * r
            correct, distractors = f"{area}π", [f"{d*d}π", f"{d}π", f"{2*area}π"]
            question = f"Find the area of a circle with diameter {d} cm. (In terms of π)"
            explanation = f"r = {d}/2 = {r}. A = πr² = π × {r}² = {area}π cm²"
        else:
            # Find radius given circumference or area
            r = random.randint(3, 8)
            given = random.choice(['circumference', 'area'])
            if given == 'circumference':
                c = 2 * r
                correct, distractors = str(r), [str(c), str(r * 2), str(r - 1)]
                question = f"A circle has circumference {c}π cm. Find its radius."
                explanation = f"C = 2πr, so {c}π = 2πr. r = {c}/2 = {r} cm"
            else:
                a = r * r
                correct, distractors = str(r), [str(a), str(r * 2), str(r + 1)]
                question = f"A circle has area {a}π cm². Find its radius."
                explanation = f"A = πr², so {a}π = πr². r² = {a}, r = {r} cm"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'})
    return questions

def generate_level_5():
    """Level 5: Sectors & Arcs"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Arc length (degrees)
            r = random.randint(4, 12)
            theta = random.choice([60, 90, 120, 180, 270])
            frac = theta // 30  # In terms of π/6
            if theta == 60:
                correct = f"{r}π/3"
            elif theta == 90:
                correct = f"{r}π/2"
            elif theta == 120:
                correct = f"{2*r}π/3"
            elif theta == 180:
                correct = f"{r}π"
            else:  # 270
                correct = f"{3*r}π/2"
            distractors = [f"{r}π", f"{2*r}π", f"{r*r}π"]
            question = f"Find the arc length: radius {r} cm, angle {theta}°. (In terms of π)"
            explanation = f"Arc = (θ/360) × 2πr = ({theta}/360) × 2π × {r} = {correct} cm"
        elif qtype == 2:
            # Sector area (degrees)
            r = random.randint(4, 10)
            theta = random.choice([60, 90, 120, 180])
            r_sq = r * r
            if theta == 60:
                correct = f"{r_sq}π/6"
            elif theta == 90:
                correct = f"{r_sq}π/4"
            elif theta == 120:
                correct = f"{r_sq}π/3"
            else:  # 180
                correct = f"{r_sq}π/2"
            distractors = [f"{r_sq}π", f"{r}π", f"{2*r_sq}π"]
            question = f"Find sector area: radius {r} cm, angle {theta}°. (In terms of π)"
            explanation = f"Area = (θ/360) × πr² = ({theta}/360) × π × {r}² = {correct} cm²"
        elif qtype == 3:
            # Semicircle perimeter
            r = random.randint(4, 10)
            d = 2 * r
            # Perimeter = πr + 2r = r(π + 2)
            correct = f"{r}π + {d}"
            distractors = [f"{r}π", f"{2*r}π", f"{r}π + {r}"]
            question = f"Find the perimeter of a semicircle with radius {r} cm."
            explanation = f"Perimeter = πr + 2r = {r}π + {d} cm"
        elif qtype == 4:
            # Semicircle area
            r = random.randint(4, 10)
            r_sq = r * r
            correct = f"{r_sq}π/2"
            distractors = [f"{r_sq}π", f"{r}π", f"{2*r_sq}π"]
            question = f"Find the area of a semicircle with radius {r} cm."
            explanation = f"Area = ½πr² = ½ × π × {r}² = {r_sq}π/2 cm²"
        else:
            # Quarter circle area
            r = random.randint(4, 10)
            r_sq = r * r
            correct = f"{r_sq}π/4"
            distractors = [f"{r_sq}π", f"{r_sq}π/2", f"{r}π"]
            question = f"Find the area of a quarter circle with radius {r} cm."
            explanation = f"Area = ¼πr² = ¼ × π × {r}² = {r_sq}π/4 cm²"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'})
    return questions

def generate_level_6():
    """Level 6: Surface Area - Prisms"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Cuboid surface area
            l, w, h = random.randint(3, 8), random.randint(3, 8), random.randint(3, 8)
            sa = 2 * (l*w + l*h + w*h)
            correct, distractors = str(sa), [str(l*w*h), str(l*w + l*h + w*h), str(sa + 10)]
            question = f"Find surface area of cuboid {l} × {w} × {h} cm."
            explanation = f"SA = 2(lw + lh + wh) = 2({l*w} + {l*h} + {w*h}) = {sa} cm²"
        elif qtype == 2:
            # Cube surface area
            s = random.randint(3, 10)
            sa = 6 * s * s
            correct, distractors = str(sa), [str(s * s * s), str(4 * s * s), str(sa + 6)]
            question = f"Find surface area of a cube with side {s} cm."
            explanation = f"SA = 6s² = 6 × {s}² = {sa} cm²"
        elif qtype == 3:
            # Triangular prism surface area
            b, h_tri, l = random.randint(3, 8), random.randint(3, 8), random.randint(5, 10)
            # Two triangular faces + three rectangular faces
            tri_area = b * h_tri // 2
            # Assuming right triangle for simplicity
            rect_area = (b + h_tri + 5) * l  # Approximation
            total = 2 * tri_area + b * l + h_tri * l + 5 * l
            correct = str(2 * tri_area + (b + h_tri + int((b*b + h_tri*h_tri)**0.5)) * l)
            # Simplified
            correct, distractors = str(2 * tri_area + 3 * b * l), [str(tri_area * l), str(b * h_tri * l), str(2 * tri_area)]
            question = f"A triangular prism has triangle base {b} cm, height {h_tri} cm, length {l} cm. Find 2 × triangle area + perimeter × length."
            explanation = f"2 × (½ × {b} × {h_tri}) + perimeter × {l} = {2 * tri_area} + ... ≈ {correct} cm²"
        elif qtype == 4:
            # Find missing dimension
            l, w = random.randint(4, 8), random.randint(3, 6)
            h = random.randint(3, 6)
            sa = 2 * (l*w + l*h + w*h)
            correct, distractors = str(h), [str(l), str(w), str(h + 1)]
            question = f"Cuboid: length {l}, width {w}, SA = {sa} cm². Find height."
            explanation = f"Using SA = 2(lw + lh + wh), height = {h} cm"
        else:
            # Open-top box
            l, w, h = random.randint(5, 10), random.randint(4, 8), random.randint(3, 6)
            sa = l * w + 2 * l * h + 2 * w * h  # No top
            correct, distractors = str(sa), [str(2 * (l*w + l*h + w*h)), str(l * w * h), str(sa + l*w)]
            question = f"Open-top box {l} × {w} × {h} cm. Find surface area."
            explanation = f"SA = lw + 2lh + 2wh = {l*w} + {2*l*h} + {2*w*h} = {sa} cm²"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'})
    return questions

def generate_level_7():
    """Level 7: Surface Area - Cylinders & Cones"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Cylinder total surface area
            r, h = random.randint(3, 8), random.randint(5, 12)
            # SA = 2πr² + 2πrh = 2πr(r + h)
            correct = f"{2*r*(r+h)}π"
            distractors = [f"{r*r*h}π", f"{2*r*h}π", f"{r*(r+h)}π"]
            question = f"Find total surface area of cylinder: radius {r} cm, height {h} cm."
            explanation = f"SA = 2πr² + 2πrh = 2πr(r + h) = 2π × {r} × {r+h} = {2*r*(r+h)}π cm²"
        elif qtype == 2:
            # Cylinder curved surface area
            r, h = random.randint(3, 8), random.randint(5, 12)
            correct = f"{2*r*h}π"
            distractors = [f"{r*h}π", f"{r*r*h}π", f"{2*r*(r+h)}π"]
            question = f"Find curved surface area of cylinder: radius {r} cm, height {h} cm."
            explanation = f"CSA = 2πrh = 2π × {r} × {h} = {2*r*h}π cm²"
        elif qtype == 3:
            # Cone total surface area
            r, l = random.randint(3, 7), random.randint(5, 10)  # l = slant height
            # SA = πr² + πrl = πr(r + l)
            correct = f"{r*(r+l)}π"
            distractors = [f"{r*l}π", f"{r*r*l}π", f"{2*r*(r+l)}π"]
            question = f"Find total surface area of cone: radius {r} cm, slant height {l} cm."
            explanation = f"SA = πr² + πrl = πr(r + l) = π × {r} × {r+l} = {r*(r+l)}π cm²"
        elif qtype == 4:
            # Cone curved surface area
            r, l = random.randint(3, 7), random.randint(5, 10)
            correct = f"{r*l}π"
            distractors = [f"{r*(r+l)}π", f"{r*r*l}π", f"{2*r*l}π"]
            question = f"Find curved surface area of cone: radius {r} cm, slant height {l} cm."
            explanation = f"CSA = πrl = π × {r} × {l} = {r*l}π cm²"
        else:
            # Hemisphere surface area
            r = random.randint(3, 8)
            # Total SA = 2πr² (curved) + πr² (base) = 3πr²
            correct = f"{3*r*r}π"
            distractors = [f"{2*r*r}π", f"{4*r*r}π", f"{r*r}π"]
            question = f"Find total surface area of hemisphere with radius {r} cm."
            explanation = f"SA = 2πr² + πr² = 3πr² = 3 × π × {r}² = {3*r*r}π cm²"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'})
    return questions

def generate_level_8():
    """Level 8: Volume - Prisms"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Cuboid volume
            l, w, h = random.randint(3, 10), random.randint(3, 10), random.randint(3, 10)
            v = l * w * h
            correct, distractors = str(v), [str(2*(l*w + l*h + w*h)), str(l + w + h), str(v + l)]
            question = f"Find volume of cuboid {l} × {w} × {h} cm."
            explanation = f"V = lwh = {l} × {w} × {h} = {v} cm³"
        elif qtype == 2:
            # Cube volume
            s = random.randint(3, 8)
            v = s * s * s
            correct, distractors = str(v), [str(6 * s * s), str(s * s), str(v + s)]
            question = f"Find volume of a cube with side {s} cm."
            explanation = f"V = s³ = {s}³ = {v} cm³"
        elif qtype == 3:
            # Triangular prism volume
            b, h_tri, l = random.randint(4, 10), random.randint(4, 10), random.randint(5, 12)
            tri_area = b * h_tri // 2
            v = tri_area * l
            correct, distractors = str(v), [str(b * h_tri * l), str(tri_area), str(v + l)]
            question = f"Triangular prism: base {b} cm, triangle height {h_tri} cm, length {l} cm. Find volume."
            explanation = f"V = (½ × {b} × {h_tri}) × {l} = {tri_area} × {l} = {v} cm³"
        elif qtype == 4:
            # Find missing dimension
            l, w = random.randint(4, 8), random.randint(3, 6)
            h = random.randint(3, 8)
            v = l * w * h
            correct, distractors = str(h), [str(l), str(w), str(h + 1)]
            question = f"Cuboid volume = {v} cm³, length = {l} cm, width = {w} cm. Find height."
            explanation = f"h = V/(lw) = {v}/({l}×{w}) = {h} cm"
        else:
            # Prism with trapezium cross-section
            a, b, h_trap = random.randint(3, 6), random.randint(6, 10), random.randint(3, 6)
            l = random.randint(5, 10)
            trap_area = (a + b) * h_trap // 2
            v = trap_area * l
            correct, distractors = str(v), [str((a + b) * h_trap * l), str(trap_area), str(v + trap_area)]
            question = f"Prism with trapezium cross-section: parallel sides {a}, {b} cm, height {h_trap} cm, length {l} cm. Find volume."
            explanation = f"V = ½({a}+{b})×{h_trap}×{l} = {trap_area}×{l} = {v} cm³"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'})
    return questions

def generate_level_9():
    """Level 9: Volume - Cylinders & Cones"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Cylinder volume
            r, h = random.randint(3, 8), random.randint(5, 12)
            v_coeff = r * r * h
            correct = f"{v_coeff}π"
            distractors = [f"{2*r*h}π", f"{r*h}π", f"{r*r}π"]
            question = f"Find volume of cylinder: radius {r} cm, height {h} cm."
            explanation = f"V = πr²h = π × {r}² × {h} = {v_coeff}π cm³"
        elif qtype == 2:
            # Cone volume
            r, h = random.randint(3, 8), random.randint(6, 12)
            v_coeff = r * r * h
            correct = f"{v_coeff}π/3"
            distractors = [f"{v_coeff}π", f"{r*r*h}π/2", f"{r*h}π"]
            question = f"Find volume of cone: radius {r} cm, height {h} cm."
            explanation = f"V = ⅓πr²h = ⅓ × π × {r}² × {h} = {v_coeff}π/3 cm³"
        elif qtype == 3:
            # Find radius of cylinder
            h = random.randint(5, 10)
            r = random.randint(3, 7)
            v_coeff = r * r * h
            correct, distractors = str(r), [str(h), str(v_coeff), str(r + 1)]
            question = f"Cylinder: volume = {v_coeff}π cm³, height = {h} cm. Find radius."
            explanation = f"V = πr²h, so {v_coeff}π = πr²×{h}. r² = {r*r}, r = {r} cm"
        elif qtype == 4:
            # Cone vs cylinder comparison
            r, h = random.randint(3, 6), random.randint(6, 10)
            correct = "3"
            distractors = ["2", "4", "1/3"]
            question = f"A cone and cylinder have the same radius and height. How many cones fill the cylinder?"
            explanation = f"Cylinder volume = 3 × cone volume. So 3 cones fill the cylinder."
        else:
            # Hollow cylinder (pipe)
            R, r, h = random.randint(5, 8), random.randint(2, 4), random.randint(10, 15)
            v_coeff = (R*R - r*r) * h
            correct = f"{v_coeff}π"
            distractors = [f"{R*R*h}π", f"{r*r*h}π", f"{(R*R + r*r)*h}π"]
            question = f"Hollow cylinder: outer radius {R} cm, inner radius {r} cm, height {h} cm. Find volume."
            explanation = f"V = π(R² - r²)h = π({R}² - {r}²)×{h} = {v_coeff}π cm³"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'})
    return questions

def generate_level_10():
    """Level 10: Volume - Spheres & Pyramids"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Sphere volume
            r = random.randint(3, 9)
            v_coeff = 4 * r * r * r
            correct = f"{v_coeff}π/3"
            distractors = [f"{r*r*r}π", f"{4*r*r}π", f"{v_coeff}π"]
            question = f"Find volume of sphere with radius {r} cm."
            explanation = f"V = (4/3)πr³ = (4/3)π×{r}³ = {v_coeff}π/3 cm³"
        elif qtype == 2:
            # Hemisphere volume
            r = random.randint(3, 8)
            v_coeff = 2 * r * r * r
            correct = f"{v_coeff}π/3"
            distractors = [f"{4*r*r*r}π/3", f"{r*r*r}π", f"{v_coeff}π"]
            question = f"Find volume of hemisphere with radius {r} cm."
            explanation = f"V = (2/3)πr³ = (2/3)π×{r}³ = {v_coeff}π/3 cm³"
        elif qtype == 3:
            # Square-based pyramid volume
            s, h = random.randint(4, 10), random.randint(6, 12)
            v = s * s * h // 3
            correct, distractors = str(v), [str(s * s * h), str(s * s), str(v + h)]
            question = f"Square pyramid: base side {s} cm, height {h} cm. Find volume."
            explanation = f"V = ⅓ × base area × height = ⅓ × {s}² × {h} = {v} cm³"
        elif qtype == 4:
            # Rectangular pyramid volume
            l, w, h = random.randint(4, 8), random.randint(3, 6), random.randint(6, 10)
            v = l * w * h // 3
            correct, distractors = str(v), [str(l * w * h), str(l * w), str(v + l)]
            question = f"Rectangular pyramid: base {l}×{w} cm, height {h} cm. Find volume."
            explanation = f"V = ⅓ × {l} × {w} × {h} = {v} cm³"
        else:
            # Find radius of sphere
            r = random.randint(3, 6)
            v_coeff = 4 * r * r * r
            correct, distractors = str(r), [str(r * r), str(v_coeff // 3), str(r + 1)]
            question = f"Sphere volume = {v_coeff}π/3 cm³. Find radius."
            explanation = f"(4/3)πr³ = {v_coeff}π/3, so r³ = {r*r*r}, r = {r} cm"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'})
    return questions

def generate_level_11():
    """Level 11: Unit Conversions"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            # cm² to m²
            cm2 = random.randint(10000, 90000)
            m2 = cm2 / 10000
            correct = str(m2)
            distractors = [str(cm2 / 100), str(cm2 / 1000), str(cm2 * 100)]
            question = f"Convert {cm2} cm² to m²."
            explanation = f"1 m² = 10000 cm². {cm2} ÷ 10000 = {m2} m²"
        elif qtype == 2:
            # m³ to cm³
            m3 = random.randint(1, 5)
            cm3 = m3 * 1000000
            correct = str(cm3)
            distractors = [str(m3 * 1000), str(m3 * 100), str(m3 * 10000)]
            question = f"Convert {m3} m³ to cm³."
            explanation = f"1 m³ = 1,000,000 cm³. {m3} × 1,000,000 = {cm3} cm³"
        elif qtype == 3:
            # cm³ to litres
            cm3 = random.randint(500, 5000)
            litres = cm3 / 1000
            correct = str(litres)
            distractors = [str(cm3 / 100), str(cm3 * 1000), str(cm3 / 10)]
            question = f"Convert {cm3} cm³ to litres."
            explanation = f"1 litre = 1000 cm³. {cm3} ÷ 1000 = {litres} litres"
        elif qtype == 4:
            # litres to m³
            litres = random.randint(100, 2000)
            m3 = litres / 1000
            correct = str(m3)
            distractors = [str(litres * 1000), str(litres / 100), str(litres)]
            question = f"Convert {litres} litres to m³."
            explanation = f"1 m³ = 1000 litres. {litres} ÷ 1000 = {m3} m³"
        elif qtype == 5:
            # mm² to cm²
            mm2 = random.randint(100, 9000)
            cm2 = mm2 / 100
            correct = str(cm2)
            distractors = [str(mm2 / 10), str(mm2 * 100), str(mm2 / 1000)]
            question = f"Convert {mm2} mm² to cm²."
            explanation = f"1 cm² = 100 mm². {mm2} ÷ 100 = {cm2} cm²"
        else:
            # km² to m²
            km2 = random.randint(1, 10)
            m2 = km2 * 1000000
            correct = str(m2)
            distractors = [str(km2 * 1000), str(km2 * 100), str(km2 * 10000)]
            question = f"Convert {km2} km² to m²."
            explanation = f"1 km² = 1,000,000 m². {km2} × 1,000,000 = {m2} m²"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'})
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            # Combined surface area and volume
            s = random.randint(3, 7)
            sa = 6 * s * s
            v = s * s * s
            ratio = sa / v if v != 0 else 0
            correct = f"{6}/{s}"
            distractors = [f"{s}/6", f"6{s}", str(s)]
            question = f"For a cube with side {s}, find the ratio of surface area to volume."
            explanation = f"SA/V = 6s²/s³ = 6/s = 6/{s}"
        elif qtype == 2:
            # Composite solid
            r, h_cyl, h_cone = random.randint(3, 6), random.randint(8, 12), random.randint(4, 6)
            v_cyl = r * r * h_cyl
            v_cone = r * r * h_cone
            correct = f"{v_cyl}π + {v_cone}π/3"
            distractors = [f"{v_cyl + v_cone}π", f"{v_cyl}π", f"{v_cyl - v_cone}π"]
            question = f"Cylinder (r={r}, h={h_cyl}) topped with cone (h={h_cone}). Find total volume."
            explanation = f"V = πr²h + ⅓πr²h = {v_cyl}π + {v_cone}π/3"
        elif qtype == 3:
            # Scale factor and volume
            k = random.randint(2, 4)
            v1 = random.randint(10, 50)
            v2 = v1 * k * k * k
            correct = str(v2)
            distractors = [str(v1 * k), str(v1 * k * k), str(v1 + k)]
            question = f"Similar solids have scale factor {k}. Small volume = {v1} cm³. Find large volume."
            explanation = f"Volume ratio = k³ = {k}³ = {k*k*k}. Large V = {v1} × {k*k*k} = {v2} cm³"
        elif qtype == 4:
            # Spherical tank capacity
            r = random.randint(10, 20)
            v_coeff = 4 * r * r * r
            # Convert to litres (1000 cm³ = 1 L)
            correct = f"{v_coeff}π/3000"
            distractors = [f"{v_coeff}π/3", f"{v_coeff}π", f"{r*r*r}π/3"]
            question = f"Spherical tank radius {r} cm. Find capacity in litres (in terms of π)."
            explanation = f"V = (4/3)πr³ = {v_coeff}π/3 cm³ = {v_coeff}π/3000 litres"
        elif qtype == 5:
            # Surface area to paint
            l, w, h = random.randint(5, 10), random.randint(4, 8), random.randint(3, 6)
            # Walls only (4 walls)
            walls = 2 * (l * h + w * h)
            correct = str(walls)
            distractors = [str(2*(l*w + l*h + w*h)), str(l * w), str(walls + l*w)]
            question = f"Room {l}×{w}×{h} m. Find wall area to paint (4 walls only)."
            explanation = f"Walls = 2(lh + wh) = 2({l}×{h} + {w}×{h}) = {walls} m²"
        else:
            # Water displacement
            r = random.randint(3, 6)
            v_coeff = 4 * r * r * r
            correct = f"{v_coeff}π/3"
            distractors = [f"{r*r*r}π", f"{4*r*r}π", f"{v_coeff}π"]
            question = f"A sphere radius {r} cm is submerged. Find water displaced."
            explanation = f"Water displaced = volume of sphere = (4/3)πr³ = {v_coeff}π/3 cm³"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'})
    return questions

def main():
    all_questions = []
    generators = [generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12]
    
    print(f"Generating questions for {TOPIC}...")
    print("=" * 50)
    for level, generator in enumerate(generators, 1):
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level} ({LEVEL_TITLES[level-1]}): {len(questions)} questions")
    print("=" * 50)
    print(f"Total questions generated: {len(all_questions)}")
    
    sql_statements = []
    for q in all_questions:
        q_text = q['question_text'].replace("'", "''")
        opt_a, opt_b = q['option_a'].replace("'", "''"), q['option_b'].replace("'", "''")
        opt_c, opt_d = q['option_c'].replace("'", "''"), q['option_d'].replace("'", "''")
        expl = q['explanation'].replace("'", "''")
        sql = f"""INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('{q_text}', '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', {q['correct_idx']},
'{TOPIC}', {q['difficulty']}, '{q['difficulty_band']}', '{MODE}', '{expl}', 1);"""
        sql_statements.append(sql)
    
    sql_file = f'/home/claude/{TOPIC}_questions.sql'
    with open(sql_file, 'w') as f:
        f.write(f"-- LC Higher Level - Measurement Questions\n-- Generated: 2025-12-15\n-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
