#!/usr/bin/env python3
"""
LC Higher Level - Geometry Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level x 12 levels) for LC HL Geometry
"""

import random
import math

TOPIC = 'lc_hl_geometry'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Angle Properties',
    'Triangle Properties',
    'Congruent Triangles',
    'Similar Triangles',
    'Pythagoras Theorem',
    'Circle Theorems - Basic',
    'Circle Theorems - Advanced',
    'Quadrilaterals',
    'Transformations',
    'Constructions & Loci',
    'Geometric Proofs',
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

def simplify_sqrt(n):
    if n <= 0:
        return (0, 0)
    a, b = 1, n
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % (i * i) == 0:
            a, b = i, n // (i * i)
            break
    return (a, b)

def format_sqrt(n):
    if n == 0:
        return "0"
    a, b = simplify_sqrt(n)
    if b == 1:
        return str(a)
    elif a == 1:
        return f"√{b}"
    else:
        return f"{a}√{b}"

def generate_level_1():
    """Level 1: Angle Properties"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            a = random.randint(30, 150)
            b = 180 - a
            correct, distractors = str(b), [str(b + 10), str(b - 10), str(360 - a)]
            question = f"Two angles on a straight line are {a}° and x°. Find x."
            explanation = f"Angles on a straight line sum to 180°. x = 180° - {a}° = {b}°"
        elif qtype == 2:
            a, b, c = random.randint(40, 120), random.randint(40, 120), random.randint(40, 120)
            d = 360 - a - b - c
            correct, distractors = str(d), [str(d + 10), str(d - 10), str(180 - d)]
            question = f"Four angles at a point are {a}°, {b}°, {c}° and x°. Find x."
            explanation = f"Angles at a point sum to 360°. x = 360° - {a}° - {b}° - {c}° = {d}°"
        elif qtype == 3:
            a = random.randint(20, 160)
            correct, distractors = str(a), [str(180 - a), str(a + 10), str(90)]
            question = f"Two lines intersect. One angle is {a}°. Find the vertically opposite angle."
            explanation = f"Vertically opposite angles are equal. The angle = {a}°"
        elif qtype == 4:
            a = random.randint(30, 150)
            correct, distractors = str(a), [str(180 - a), str(a + 10), str(90)]
            question = f"Two parallel lines cut by a transversal. One angle is {a}°. Find the corresponding angle."
            explanation = f"Corresponding angles are equal. Angle = {a}°"
        elif qtype == 5:
            a = random.randint(30, 150)
            correct, distractors = str(a), [str(180 - a), str(a + 15), str(90)]
            question = f"Two parallel lines cut by a transversal. One angle is {a}°. Find the alternate angle."
            explanation = f"Alternate angles are equal. Angle = {a}°"
        else:
            a = random.randint(30, 150)
            b = 180 - a
            correct, distractors = str(b), [str(a), str(b + 10), str(360 - a)]
            question = f"Two parallel lines cut by a transversal. One co-interior angle is {a}°. Find the other."
            explanation = f"Co-interior angles sum to 180°. Angle = 180° - {a}° = {b}°"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'})
    return questions

def generate_level_2():
    """Level 2: Triangle Properties"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            a, b = random.randint(30, 80), random.randint(30, 80)
            c = 180 - a - b
            correct, distractors = str(c), [str(c + 10), str(c - 10), str(180 - c)]
            question = f"In triangle ABC, angle A = {a}° and angle B = {b}°. Find angle C."
            explanation = f"Angles in a triangle sum to 180°. C = 180° - {a}° - {b}° = {c}°"
        elif qtype == 2:
            a, b = random.randint(30, 70), random.randint(30, 70)
            ext = a + b
            correct, distractors = str(ext), [str(180 - ext), str(a), str(b)]
            question = f"In a triangle, two interior angles are {a}° and {b}°. Find the exterior angle at the third vertex."
            explanation = f"Exterior angle = sum of opposite interior angles = {a}° + {b}° = {ext}°"
        elif qtype == 3:
            base_angle = random.randint(40, 80)
            apex = 180 - 2 * base_angle
            correct, distractors = str(apex), [str(base_angle), str(180 - base_angle), str(2 * base_angle)]
            question = f"In an isosceles triangle, the two equal base angles are each {base_angle}°. Find the apex angle."
            explanation = f"Apex angle = 180° - 2({base_angle}°) = {apex}°"
        elif qtype == 4:
            correct, distractors = "60", ["45", "90", "120"]
            question = "What is each angle in an equilateral triangle?"
            explanation = "All angles in an equilateral triangle are equal: 180° ÷ 3 = 60°"
        elif qtype == 5:
            a, b = random.randint(3, 10), random.randint(3, 10)
            min_c, max_c = abs(a - b) + 1, a + b - 1
            valid_c = random.randint(min_c, max_c)
            invalid_c = a + b + random.randint(1, 5)
            correct, distractors = str(valid_c), [str(invalid_c), str(a + b), str(abs(a - b))]
            question = f"Two sides of a triangle are {a} and {b}. Which could be the third side?"
            explanation = f"Third side must be between {abs(a-b)} and {a+b}. So {valid_c} is valid."
        else:
            types = [(30, 60, 90, "right-angled", ["acute", "obtuse", "equilateral"]),
                (50, 60, 70, "acute", ["right-angled", "obtuse", "equilateral"]),
                (30, 40, 110, "obtuse", ["acute", "right-angled", "equilateral"])]
            a, b, c, correct, distractors = random.choice(types)
            question = f"A triangle has angles {a}°, {b}°, {c}°. What type of triangle is it?"
            explanation = f"The triangle is {correct}."
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'})
    return questions

def generate_level_3():
    """Level 3: Congruent Triangles"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            conditions = [("Three sides equal", "SSS", ["SAS", "ASA", "RHS"]),
                ("Two sides and included angle equal", "SAS", ["SSS", "ASA", "AAS"]),
                ("Two angles and included side equal", "ASA", ["SSS", "SAS", "RHS"]),
                ("Right angle, hypotenuse, side", "RHS", ["SSS", "SAS", "ASA"])]
            desc, correct, distractors = random.choice(conditions)
            question = f"Which congruence condition is: {desc}?"
            explanation = f"This is the {correct} congruence condition."
        elif qtype == 2:
            scenarios = [("AB = PQ, BC = QR, AC = PR", "SSS", ["SAS", "ASA", "AAS"]),
                ("AB = PQ, angle B = angle Q, BC = QR", "SAS", ["SSS", "ASA", "AAS"]),
                ("angle A = angle P, AB = PQ, angle B = angle Q", "ASA", ["SSS", "SAS", "AAS"])]
            given, correct, distractors = random.choice(scenarios)
            question = f"Triangles ABC and PQR have: {given}. Which congruence condition?"
            explanation = f"This satisfies {correct}."
        elif qtype == 3:
            side = random.randint(5, 15)
            correct, distractors = str(side), [str(side + 2), str(side - 2), str(side * 2)]
            question = f"Triangles ABC ≅ PQR. If AB = {side} cm, what is PQ?"
            explanation = f"Corresponding sides are equal. PQ = {side} cm"
        elif qtype == 4:
            angle = random.randint(30, 80)
            correct, distractors = str(angle), [str(180 - angle), str(angle + 10), str(90 - angle)]
            question = f"Triangles ABC ≅ XYZ. If angle A = {angle}°, what is angle X?"
            explanation = f"Corresponding angles are equal. Angle X = {angle}°"
        else:
            correct, distractors = "Not valid", ["SSS", "SAS", "ASA"]
            question = "Is AAA (three angles equal) a valid congruence condition?"
            explanation = "AAA is not valid - triangles may be similar but not congruent."
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'})
    return questions

def generate_level_4():
    """Level 4: Similar Triangles"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            a1, b1 = random.randint(3, 8), random.randint(4, 10)
            k = random.randint(2, 4)
            a2, b2 = a1 * k, b1 * k
            correct, distractors = str(b2), [str(b2 + k), str(b1 + a2), str(a2)]
            question = f"Triangles ABC ~ PQR with AB = {a1}, BC = {b1}, PQ = {a2}. Find QR."
            explanation = f"Scale factor = {k}. QR = {b1} × {k} = {b2}"
        elif qtype == 2:
            a1, k = random.randint(3, 8), random.randint(2, 5)
            a2 = a1 * k
            correct, distractors = str(k), [str(k + 1), str(k - 1), str(a2 - a1)]
            question = f"Triangles ABC ~ XYZ. If AB = {a1} and XY = {a2}, find the scale factor."
            explanation = f"Scale factor = {a2}/{a1} = {k}"
        elif qtype == 3:
            k = random.randint(2, 4)
            area1 = random.randint(10, 30)
            area2 = area1 * k * k
            correct, distractors = str(area2), [str(area1 * k), str(area1 * 2), str(area2 + area1)]
            question = f"Similar triangles have scale factor {k}. Smaller area is {area1} cm². Find larger area."
            explanation = f"Area ratio = k² = {k*k}. Larger area = {area1} × {k*k} = {area2} cm²"
        elif qtype == 4:
            conditions = [("All three angles equal", "Yes", ["No", "Need sides", "Maybe"]),
                ("All sides in proportion", "Yes", ["No", "Need angles", "Maybe"])]
            cond, correct, distractors = random.choice(conditions)
            question = f"Are triangles similar if they have: {cond}?"
            explanation = f"{correct}, the triangles are similar."
        else:
            de, bc, ad = random.randint(3, 6), random.randint(9, 15), random.randint(4, 8)
            ab = ad * bc // de
            correct, distractors = str(ab), [str(ab + 2), str(ad + de), str(bc)]
            question = f"In △ABC, DE ∥ BC. AD = {ad}, DE = {de}, BC = {bc}. Find AB."
            explanation = f"By similarity: AB = AD × BC/DE = {ab}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'})
    return questions

def generate_level_5():
    """Level 5: Pythagoras Theorem"""
    questions = []
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10)]
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            a, b, c = random.choice(triples)
            correct, distractors = str(c), [str(a + b), str(c + 1), str(c - 1)]
            question = f"In a right triangle, legs are {a} and {b}. Find the hypotenuse."
            explanation = f"c² = {a}² + {b}² = {c*c}. c = {c}"
        elif qtype == 2:
            a, b, c = random.choice(triples)
            correct, distractors = str(a), [str(c - b), str(a + 1), str(b)]
            question = f"Right triangle: one leg is {b}, hypotenuse is {c}. Find the other leg."
            explanation = f"a² = {c}² - {b}² = {a*a}. a = {a}"
        elif qtype == 3:
            a, b, c = random.choice(triples)
            is_right = random.choice([True, False])
            if not is_right:
                c = c + 1
            correct = "Yes" if a*a + b*b == c*c else "No"
            distractors = ["Yes" if correct == "No" else "No", "Cannot determine", "Maybe"]
            question = f"Is a triangle with sides {a}, {b}, {c} a right triangle?"
            explanation = f"{a}² + {b}² = {a*a + b*b}, {c}² = {c*c}. {correct}."
        elif qtype == 4:
            dx, dy = random.randint(3, 8), random.randint(3, 8)
            dist_sq = dx*dx + dy*dy
            correct, distractors = format_sqrt(dist_sq), [str(dx + dy), format_sqrt(dist_sq + 1), str(dx * dy)]
            question = f"Find distance between (0, 0) and ({dx}, {dy})."
            explanation = f"Distance = √({dx}² + {dy}²) = √{dist_sq} = {correct}"
        else:
            a, b, c = random.randint(3, 6), random.randint(3, 6), random.randint(3, 6)
            diag_sq = a*a + b*b + c*c
            correct, distractors = format_sqrt(diag_sq), [str(a + b + c), format_sqrt(a*a + b*b), str(a * b)]
            question = f"Find the space diagonal of a {a} × {b} × {c} box."
            explanation = f"Diagonal = √({a}² + {b}² + {c}²) = √{diag_sq} = {correct}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'})
    return questions

def generate_level_6():
    """Level 6: Circle Theorems - Basic"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            angle_circ = random.randint(25, 80)
            angle_centre = 2 * angle_circ
            correct, distractors = str(angle_centre), [str(angle_circ), str(angle_centre + 10), str(180 - angle_circ)]
            question = f"Angle at circumference is {angle_circ}°. Find angle at centre (same arc)."
            explanation = f"Angle at centre = 2 × {angle_circ}° = {angle_centre}°"
        elif qtype == 2:
            correct, distractors = "90", ["45", "60", "180"]
            question = "What is the angle in a semicircle?"
            explanation = "Angle in a semicircle is always 90°."
        elif qtype == 3:
            angle = random.randint(30, 70)
            correct, distractors = str(angle), [str(180 - angle), str(angle + 10), str(2 * angle)]
            question = f"Two angles in the same segment are x° and {angle}°. Find x."
            explanation = f"Angles in same segment are equal. x = {angle}°"
        elif qtype == 4:
            angle = random.randint(60, 120)
            opp = 180 - angle
            correct, distractors = str(opp), [str(angle), str(360 - angle), str(opp + 10)]
            question = f"In a cyclic quadrilateral, one angle is {angle}°. Find the opposite angle."
            explanation = f"Opposite angles sum to 180°. Opposite = {opp}°"
        elif qtype == 5:
            angle = random.randint(20, 70)
            other = 90 - angle
            correct, distractors = str(other), [str(angle), str(180 - angle), str(90)]
            question = f"Tangent meets radius at P. One angle is {angle}°. Find the other at P."
            explanation = f"Tangent ⟂ radius. Other angle = 90° - {angle}° = {other}°"
        else:
            length = random.randint(5, 15)
            correct, distractors = str(length), [str(length + 2), str(length * 2), str(length - 2)]
            question = f"From external point P, one tangent is {length}. Find the other tangent length from P."
            explanation = f"Tangents from external point are equal. Length = {length}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'})
    return questions

def generate_level_7():
    """Level 7: Circle Theorems - Advanced"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            angle = random.randint(30, 70)
            correct, distractors = str(angle), [str(180 - angle), str(90 - angle), str(2 * angle)]
            question = f"Tangent at P makes {angle}° with chord PQ. Find angle in alternate segment."
            explanation = f"Alternate segment theorem: angle = {angle}°"
        elif qtype == 2:
            a, b, c, d = 4, 6, 3, 8
            correct, distractors = str(d), [str(a + b), str(c + 1), str(a * b)]
            question = f"Chords intersect: segments {a}, {b} and {c}, x. Find x."
            explanation = f"{a} × {b} = {c} × x. x = {a*b}/{c} = {d}"
        elif qtype == 3:
            t, a = 6, 4
            whole = 9
            correct, distractors = str(whole), [str(t), str(a * 2), str(t + a)]
            question = f"Tangent = {t}, secant near segment = {a}. Find whole secant."
            explanation = f"Tangent² = near × whole. {t}² = {a} × whole. Whole = {whole}"
        elif qtype == 4:
            a1, b1, a2, b2 = 3, 5, 4, 2
            whole2 = a2 + b2
            correct, distractors = str(whole2), [str(a1 + b1), str(whole2 + 2), str(a1 * a2)]
            question = f"Two secants: first {a1}, {b1}; second near = {a2}. Find second whole secant."
            explanation = f"{a1} × {a1+b1} = {a2} × whole. Whole = {whole2}"
        else:
            angle = random.randint(25, 65)
            correct, distractors = str(angle), [str(90 - angle), str(180 - angle), str(2 * angle)]
            question = f"Angle between tangent and chord is {angle}°. Find inscribed angle on same chord."
            explanation = f"By alternate segment theorem: {angle}°"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'})
    return questions

def generate_level_8():
    """Level 8: Quadrilaterals"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            a, b, c = random.randint(60, 120), random.randint(60, 120), random.randint(60, 120)
            d = 360 - a - b - c
            correct, distractors = str(d), [str(d + 10), str(180 - d), str(360 - d)]
            question = f"Quadrilateral angles: {a}°, {b}°, {c}°, x°. Find x."
            explanation = f"Sum = 360°. x = 360° - {a}° - {b}° - {c}° = {d}°"
        elif qtype == 2:
            angle = random.randint(50, 130)
            adjacent = 180 - angle
            correct, distractors = str(adjacent), [str(angle), str(360 - angle), str(angle + 10)]
            question = f"Parallelogram: one angle is {angle}°. Find adjacent angle."
            explanation = f"Adjacent angles supplementary. = 180° - {angle}° = {adjacent}°"
        elif qtype == 3:
            props = [("All angles are...", "90°", ["60°", "180°", "45°"]),
                ("Diagonals are...", "equal and bisect each other", ["perpendicular", "unequal", "parallel"])]
            q_part, correct, distractors = random.choice(props)
            question = f"In a rectangle: {q_part}"
            explanation = f"In a rectangle: {correct}"
        elif qtype == 4:
            props = [("All sides are...", "equal", ["parallel", "perpendicular", "different"]),
                ("Diagonals are...", "perpendicular bisectors", ["equal", "parallel", "not bisecting"])]
            q_part, correct, distractors = random.choice(props)
            question = f"In a rhombus: {q_part}"
            explanation = f"In a rhombus: {correct}"
        elif qtype == 5:
            angle1 = random.randint(50, 80)
            angle2 = 180 - angle1
            correct, distractors = str(angle2), [str(angle1), str(360 - angle1), str(angle1 + 10)]
            question = f"Trapezium: angle on one leg is {angle1}°. Find other angle on same leg."
            explanation = f"Co-interior angles = 180°. Other = {angle2}°"
        else:
            quads = [("4 equal sides, 4 right angles", "Square", ["Rectangle", "Rhombus", "Parallelogram"]),
                ("4 right angles, opposite sides equal", "Rectangle", ["Square", "Rhombus", "Trapezium"]),
                ("One pair of parallel sides", "Trapezium", ["Parallelogram", "Rectangle", "Rhombus"])]
            desc, correct, distractors = random.choice(quads)
            question = f"Which quadrilateral: {desc}?"
            explanation = f"A {correct}."
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'})
    return questions

def generate_level_9():
    """Level 9: Transformations"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            dx, dy = random.randint(-5, 5), random.randint(-5, 5)
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            x2, y2 = x1 + dx, y1 + dy
            correct, distractors = f"({x2}, {y2})", [f"({x1 + dy}, {y1 + dx})", f"({x1 - dx}, {y1 - dy})", f"({x2 + 1}, {y2})"]
            question = f"({x1}, {y1}) translated by ({dx}, {dy}). Find image."
            explanation = f"Image = ({x2}, {y2})"
        elif qtype == 2:
            x, y = random.randint(-5, 5), random.randint(1, 8)
            correct, distractors = f"({x}, {-y})", [f"({-x}, {y})", f"({-x}, {-y})", f"({y}, {x})"]
            question = f"Reflect ({x}, {y}) in the x-axis."
            explanation = f"Reflection in x-axis: ({x}, {-y})"
        elif qtype == 3:
            x, y = random.randint(1, 8), random.randint(-5, 5)
            correct, distractors = f"({-x}, {y})", [f"({x}, {-y})", f"({-x}, {-y})", f"({y}, {x})"]
            question = f"Reflect ({x}, {y}) in the y-axis."
            explanation = f"Reflection in y-axis: ({-x}, {y})"
        elif qtype == 4:
            x, y = random.randint(1, 5), random.randint(1, 5)
            correct, distractors = f"({-y}, {x})", [f"({y}, {-x})", f"({-x}, {-y})", f"({x}, {-y})"]
            question = f"Rotate ({x}, {y}) by 90° anticlockwise about origin."
            explanation = f"90° anticlockwise: ({-y}, {x})"
        else:
            x, y = random.randint(1, 4), random.randint(1, 4)
            k = random.randint(2, 4)
            x2, y2 = k * x, k * y
            correct, distractors = f"({x2}, {y2})", [f"({x + k}, {y + k})", f"({x2 + 1}, {y2})", f"({k}, {k})"]
            question = f"Enlarge ({x}, {y}) by scale factor {k} from origin."
            explanation = f"Enlargement: ({x2}, {y2})"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'})
    return questions

def generate_level_10():
    """Level 10: Constructions & Loci"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            correct = "Perpendicular bisector of AB"
            distractors = ["A circle", "Line through A and B", "Angle bisector"]
            question = "Locus equidistant from two points A and B?"
            explanation = "The perpendicular bisector of AB."
        elif qtype == 2:
            correct = "Angle bisector of the lines"
            distractors = ["A circle", "Perpendicular bisector", "Parallel line"]
            question = "Locus equidistant from two intersecting lines?"
            explanation = "The angle bisector(s)."
        elif qtype == 3:
            r = random.randint(3, 10)
            correct = f"Circle with radius {r}"
            distractors = [f"Line {r} units away", f"Square side {r}", "Two parallel lines"]
            question = f"Locus at distance {r} from point P?"
            explanation = f"Circle centre P, radius {r}."
        elif qtype == 4:
            d = random.randint(2, 8)
            correct = f"Two parallel lines, each {d} units away"
            distractors = [f"Circle radius {d}", f"One line {d} away", "Rectangle"]
            question = f"Locus at distance {d} from a fixed line?"
            explanation = f"Two parallel lines, {d} units from given line."
        else:
            constructions = [("To bisect an angle, draw arcs from vertex that...", 
                "cut both arms at equal distances", ["are different sizes", "only cut one arm", "pass through vertex"]),
                ("Perpendicular bisector: draw arcs from A and B that...", 
                "have equal radius and intersect", ["have different radii", "don't intersect", "pass through midpoint"])]
            q_text, correct, distractors = random.choice(constructions)
            question = q_text
            explanation = correct
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'})
    return questions

def generate_level_11():
    """Level 11: Geometric Proofs"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            steps = [("'Given' in a proof refers to...", "Information stated in problem", ["What to prove", "Conclusion", "Assumption"]),
                ("'To Prove' refers to...", "What we need to show", ["Given info", "First step", "An axiom"])]
            q_text, correct, distractors = random.choice(steps)
            question = q_text
            explanation = correct
        elif qtype == 2:
            theorems = [("Two equal sides → equal opposite angles", "Isosceles triangle theorem", ["Pythagoras", "Angle sum", "Congruence"]),
                ("Angle at centre = 2 × angle at circumference", "Circle theorem", ["Pythagoras", "Alternate angles", "Isosceles"])]
            statement, correct, distractors = random.choice(theorems)
            question = f"Which theorem: '{statement}'?"
            explanation = f"The {correct}."
        elif qtype == 3:
            logic = [("If P → Q and P is true, then...", "Q is true", ["Q is false", "P is false", "Cannot determine"]),
                ("If P → Q and Q is false, then...", "P is false", ["P is true", "Q is true", "Cannot determine"]),
                ("Contrapositive of 'If P then Q':", "If not Q then not P", ["If Q then P", "If not P then not Q", "P and Q"])]
            q_text, correct, distractors = random.choice(logic)
            question = q_text
            explanation = correct
        elif qtype == 4:
            proofs = [("For SAS congruence, we need two sides and...", "included angle equal", ["any angle", "opposite angle", "hypotenuse"]),
                ("To prove lines parallel using alternate angles...", "show they are equal", ["show they differ", "show sum = 90°", "show sum = 360°"])]
            q_text, correct, distractors = random.choice(proofs)
            question = q_text
            explanation = correct
        else:
            scenarios = [("Proof by contradiction starts by...", "assuming opposite of what to prove", ["proving directly", "using induction", "drawing diagram"]),
                ("Proof by contradiction ends when we...", "reach a logical contradiction", ["find pattern", "use all info", "draw conclusion"])]
            q_text, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = correct
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
            a, b = random.randint(20, 50), random.randint(20, 50)
            ext = a + b
            correct, distractors = str(ext), [str(180 - ext), str(a), str(b)]
            question = f"Triangle: angle A = {a}°, angle B = {b}°. Find exterior angle at C."
            explanation = f"Exterior = {a}° + {b}° = {ext}°"
        elif qtype == 2:
            angle_centre = random.randint(60, 140)
            angle_circ = angle_centre // 2
            correct, distractors = str(angle_circ), [str(angle_centre), str(180 - angle_circ), str(angle_circ + 10)]
            question = f"Angle at centre = {angle_centre}°. Find angle at circumference (same arc)."
            explanation = f"= ½ × {angle_centre}° = {angle_circ}°"
        elif qtype == 3:
            k = random.randint(2, 4)
            correct, distractors = str(k * k), [str(k), str(k + 1), str(2 * k)]
            question = f"Similar figures have scale factor {k}. What is area ratio?"
            explanation = f"Area ratio = k² = {k*k}"
        elif qtype == 4:
            x, y = 2, 3
            x2, y2 = -x + 4, y + 2
            correct, distractors = f"({x2}, {y2})", [f"({-x}, {y})", f"({x + 4}, {y + 2})", f"({x2 - 1}, {y2})"]
            question = f"({x}, {y}) reflected in y-axis then translated by (4, 2). Find image."
            explanation = f"After reflection: ({-x}, {y}). After translation: ({x2}, {y2})"
        elif qtype == 5:
            angle = random.randint(60, 100)
            correct, distractors = str(angle), [str(180 - angle), str(angle + 10), str(360 - angle)]
            question = f"Cyclic quad ABCD: angle A = {angle}°. Find exterior angle at C."
            explanation = f"Exterior at C = opposite interior at A = {angle}°"
        else:
            base = random.choice([6, 8, 10, 12])
            side = base + random.randint(2, 4)
            half_base = base // 2
            h_sq = side * side - half_base * half_base
            h = format_sqrt(h_sq)
            correct, distractors = h, [str(side), str(base), format_sqrt(h_sq + 1)]
            question = f"Isosceles triangle: equal sides {side}, base {base}. Find height."
            explanation = f"h² = {side}² - {half_base}² = {h_sq}. h = {h}"
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
        f.write(f"-- LC Higher Level - Geometry Questions\n-- Generated: 2025-12-15\n-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
