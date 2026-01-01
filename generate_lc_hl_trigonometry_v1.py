#!/usr/bin/env python3
"""
LC Higher Level - Trigonometry Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level x 12 levels) for LC HL Trigonometry
"""

import random
import math

TOPIC = 'lc_hl_trigonometry'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Basic Trig Ratios',
    'Special Angles',
    'Unit Circle & Quadrants',
    'Radians & Degrees',
    'Trig Identities',
    'Solving Trig Equations',
    'Graphs of Trig Functions',
    'Compound Angle Formulas',
    'Double Angle Formulas',
    'Sine & Cosine Rules',
    'Area & Applications',
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
        unique_wrong.append("None of these")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a if a != 0 else 1

def simplify_fraction(num, den):
    if den == 0:
        return "undefined"
    if num == 0:
        return "0"
    sign = -1 if (num < 0) != (den < 0) else 1
    num, den = abs(num), abs(den)
    g = gcd(num, den)
    num, den = num // g, den // g
    if sign == -1:
        num = -num
    if den == 1:
        return str(num)
    return f"{num}/{den}"

def generate_level_1():
    """Level 1: Basic Trig Ratios"""
    questions = []
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            a, b, c = random.choice(triples)
            correct = simplify_fraction(a, c)
            distractors = [simplify_fraction(b, c), simplify_fraction(a, b), simplify_fraction(c, a)]
            question = f"In a right triangle, the side opposite angle θ is {a} and the hypotenuse is {c}. Find sin θ."
            explanation = f"sin θ = opposite/hypotenuse = {a}/{c} = {correct}"
        
        elif qtype == 2:
            a, b, c = random.choice(triples)
            correct = simplify_fraction(b, c)
            distractors = [simplify_fraction(a, c), simplify_fraction(b, a), simplify_fraction(c, b)]
            question = f"In a right triangle, the side adjacent to angle θ is {b} and the hypotenuse is {c}. Find cos θ."
            explanation = f"cos θ = adjacent/hypotenuse = {b}/{c} = {correct}"
        
        elif qtype == 3:
            a, b, c = random.choice(triples)
            correct = simplify_fraction(a, b)
            distractors = [simplify_fraction(b, a), simplify_fraction(a, c), simplify_fraction(b, c)]
            question = f"In a right triangle, the side opposite angle θ is {a} and the adjacent side is {b}. Find tan θ."
            explanation = f"tan θ = opposite/adjacent = {a}/{b} = {correct}"
        
        elif qtype == 4:
            ratios = [
                ("sin θ", "opposite/hypotenuse", ["adjacent/hypotenuse", "opposite/adjacent", "hypotenuse/opposite"]),
                ("cos θ", "adjacent/hypotenuse", ["opposite/hypotenuse", "opposite/adjacent", "hypotenuse/adjacent"]),
                ("tan θ", "opposite/adjacent", ["adjacent/opposite", "opposite/hypotenuse", "adjacent/hypotenuse"]),
            ]
            ratio_name, correct, distractors = random.choice(ratios)
            question = f"In a right triangle, {ratio_name} equals:"
            explanation = f"{ratio_name} = {correct}"
        
        else:
            a, b, c = random.choice(triples)
            ratio = random.choice(['sin', 'cos', 'tan'])
            if ratio == 'sin':
                question = f"If sin θ = {a}/{c} and the hypotenuse is {c}, find the opposite side."
                correct = str(a)
                distractors = [str(b), str(c), str(a + 1)]
                explanation = f"sin θ = opp/hyp, so opp = sin θ × hyp = ({a}/{c}) × {c} = {a}"
            elif ratio == 'cos':
                question = f"If cos θ = {b}/{c} and the hypotenuse is {c}, find the adjacent side."
                correct = str(b)
                distractors = [str(a), str(c), str(b + 1)]
                explanation = f"cos θ = adj/hyp, so adj = cos θ × hyp = ({b}/{c}) × {c} = {b}"
            else:
                question = f"If tan θ = {a}/{b} and the adjacent side is {b}, find the opposite side."
                correct = str(a)
                distractors = [str(b), str(c), str(a + 1)]
                explanation = f"tan θ = opp/adj, so opp = tan θ × adj = ({a}/{b}) × {b} = {a}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    return questions

def generate_level_2():
    """Level 2: Special Angles (30°, 45°, 60°)"""
    questions = []
    special_values = {
        'sin': {'0°': '0', '30°': '1/2', '45°': '√2/2', '60°': '√3/2', '90°': '1'},
        'cos': {'0°': '1', '30°': '√3/2', '45°': '√2/2', '60°': '1/2', '90°': '0'},
        'tan': {'0°': '0', '30°': '√3/3', '45°': '1', '60°': '√3', '90°': 'undefined'},
    }
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            func = random.choice(['sin', 'cos', 'tan'])
            angle = random.choice(['0°', '30°', '45°', '60°', '90°'])
            if func == 'tan' and angle == '90°':
                angle = '60°'
            correct = special_values[func][angle]
            other_angles = [a for a in special_values[func].keys() if a != angle and special_values[func][a] != 'undefined']
            distractors = [special_values[func][a] for a in random.sample(other_angles, min(3, len(other_angles)))]
            question = f"What is {func} {angle}?"
            explanation = f"{func} {angle} = {correct}"
        
        elif qtype == 2:
            func = random.choice(['sin', 'cos'])
            values_map = {v: k for k, v in special_values[func].items() if v not in ['0', '1', 'undefined']}
            value = random.choice(list(values_map.keys()))
            correct = values_map[value]
            other_angles = ['30°', '45°', '60°']
            distractors = [a for a in other_angles if a != correct]
            distractors.append('90°')
            question = f"If {func} θ = {value}, find θ (where 0° ≤ θ ≤ 90°)."
            explanation = f"{func} θ = {value}, so θ = {correct}"
        
        elif qtype == 3:
            func = random.choice(['sin', 'cos'])
            angles = ['30°', '45°', '60°']
            a1, a2 = random.sample(angles, 2)
            v1 = special_values[func][a1]
            v2 = special_values[func][a2]
            val_order = {'1/2': 0.5, '√2/2': 0.707, '√3/2': 0.866}
            if val_order.get(v1, 0) > val_order.get(v2, 0):
                correct = f"{func} {a1} > {func} {a2}"
            else:
                correct = f"{func} {a1} < {func} {a2}"
            distractors = [f"{func} {a1} = {func} {a2}", 
                         f"{func} {a1} > {func} {a2}" if '<' in correct else f"{func} {a1} < {func} {a2}",
                         "Cannot be determined"]
            question = f"Which is true: {func} {a1} compared to {func} {a2}?"
            explanation = f"{func} {a1} = {v1}, {func} {a2} = {v2}. So {correct}"
        
        else:
            angle = random.choice(['30°', '45°', '60°'])
            expressions = [
                (f"sin²{angle} + cos²{angle}", "1", ["0", "2", "1/2"]),
                (f"sin {angle} / cos {angle}", special_values['tan'][angle], ["1", "√3/2", "1/2"]),
            ]
            expr, correct, distractors = random.choice(expressions)
            question = f"Evaluate: {expr}"
            explanation = f"{expr} = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    return questions

def generate_level_3():
    """Level 3: Unit Circle & Quadrants"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            quadrant = random.randint(1, 4)
            func = random.choice(['sin', 'cos', 'tan'])
            signs = {
                1: {'sin': '+', 'cos': '+', 'tan': '+'},
                2: {'sin': '+', 'cos': '-', 'tan': '-'},
                3: {'sin': '-', 'cos': '-', 'tan': '+'},
                4: {'sin': '-', 'cos': '+', 'tan': '-'},
            }
            correct = "Positive" if signs[quadrant][func] == '+' else "Negative"
            distractors = ["Positive" if correct == "Negative" else "Negative", "Zero", "Undefined"]
            question = f"In Quadrant {quadrant}, {func} θ is:"
            explanation = f"In Q{quadrant}, {func} θ is {correct.lower()}."
        
        elif qtype == 2:
            angles = [
                (120, 60, 2), (135, 45, 2), (150, 30, 2),
                (210, 30, 3), (225, 45, 3), (240, 60, 3),
                (300, 60, 4), (315, 45, 4), (330, 30, 4),
            ]
            angle, ref_angle, quad = random.choice(angles)
            correct = f"{ref_angle}°"
            distractors = [f"{180 - ref_angle}°", f"{ref_angle + 10}°", f"{90 - ref_angle}°"]
            question = f"Find the reference angle for {angle}°."
            explanation = f"{angle}° is in Quadrant {quad}. Reference angle = {ref_angle}°"
        
        elif qtype == 3:
            conditions = [
                ("sin θ > 0 and cos θ > 0", "Quadrant 1", ["Quadrant 2", "Quadrant 3", "Quadrant 4"]),
                ("sin θ > 0 and cos θ < 0", "Quadrant 2", ["Quadrant 1", "Quadrant 3", "Quadrant 4"]),
                ("sin θ < 0 and cos θ < 0", "Quadrant 3", ["Quadrant 1", "Quadrant 2", "Quadrant 4"]),
                ("sin θ < 0 and cos θ > 0", "Quadrant 4", ["Quadrant 1", "Quadrant 2", "Quadrant 3"]),
            ]
            cond, correct, distractors = random.choice(conditions)
            question = f"If {cond}, in which quadrant does θ lie?"
            explanation = f"Given {cond}, θ is in {correct}."
        
        elif qtype == 4:
            angles_data = [
                (150, 30, 2, 'sin', '1/2'),
                (120, 60, 2, 'cos', '-1/2'),
                (225, 45, 3, 'tan', '1'),
                (330, 30, 4, 'sin', '-1/2'),
                (240, 60, 3, 'cos', '-1/2'),
                (315, 45, 4, 'cos', '√2/2'),
            ]
            angle, ref, quad, func, correct = random.choice(angles_data)
            distractors = ['1/2', '-1/2', '√3/2', '-√3/2', '√2/2', '-√2/2']
            distractors = [d for d in distractors if d != correct][:3]
            question = f"Evaluate {func} {angle}°."
            explanation = f"Reference angle is {ref}°. In Q{quad}, {func} {angle}° = {correct}"
        
        else:
            angles_coords = [
                (0, '(1, 0)'), (90, '(0, 1)'), (180, '(-1, 0)'), (270, '(0, -1)'),
                (45, '(√2/2, √2/2)'), (135, '(-√2/2, √2/2)'),
            ]
            angle, correct = random.choice(angles_coords)
            all_coords = [c for _, c in angles_coords]
            distractors = [c for c in all_coords if c != correct][:3]
            question = f"What are the coordinates of the point on the unit circle at {angle}°?"
            explanation = f"At {angle}°, the coordinates (cos θ, sin θ) = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    return questions

def generate_level_4():
    """Level 4: Radians & Degrees"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            degree_radian = [
                (30, 'π/6'), (45, 'π/4'), (60, 'π/3'), (90, 'π/2'),
                (120, '2π/3'), (135, '3π/4'), (150, '5π/6'), (180, 'π'),
                (270, '3π/2'), (360, '2π'),
            ]
            deg, correct = random.choice(degree_radian)
            all_radians = [r for _, r in degree_radian]
            distractors = [r for r in all_radians if r != correct][:3]
            question = f"Convert {deg}° to radians."
            explanation = f"{deg}° = {deg} × π/180 = {correct}"
        
        elif qtype == 2:
            radian_degree = [
                ('π/6', 30), ('π/4', 45), ('π/3', 60), ('π/2', 90),
                ('2π/3', 120), ('3π/4', 135), ('5π/6', 150), ('π', 180),
            ]
            rad, deg = random.choice(radian_degree)
            correct = f"{deg}°"
            distractors = [f"{deg + 30}°", f"{deg - 30}°" if deg > 30 else f"{deg + 60}°", f"{deg * 2}°"]
            question = f"Convert {rad} radians to degrees."
            explanation = f"{rad} = {rad} × 180/π = {deg}°"
        
        elif qtype == 3:
            r = random.randint(2, 8)
            rad_values = [('π/2', 0.5), ('π', 1), ('2π', 2)]
            rad_str, rad_val = random.choice(rad_values)
            if rad_val == 1:
                correct = f"{r}π"
            elif rad_val == 2:
                correct = f"{2*r}π"
            else:
                correct = f"{r}π/2"
            distractors = [f"{r+1}π", f"{r}π/3", f"{2*r}π"]
            distractors = [d for d in distractors if d != correct][:3]
            question = f"Find the arc length of a circle with radius {r} and central angle {rad_str}."
            explanation = f"Arc length = rθ = {r} × {rad_str} = {correct}"
        
        elif qtype == 4:
            r = random.randint(2, 6)
            rad_values = [('π/2', 0.5), ('π', 1)]
            rad_str, rad_val = random.choice(rad_values)
            area_coeff = r * r * rad_val / 2
            if area_coeff == int(area_coeff):
                correct = f"{int(area_coeff)}π"
            else:
                correct = f"{r*r}π/{int(2/rad_val)}"
            distractors = [f"{r*r}π", f"{r}π", f"{2*r*r}π"]
            distractors = [d for d in distractors if d != correct][:3]
            question = f"Find the area of a sector with radius {r} and central angle {rad_str}."
            explanation = f"Sector area = ½r²θ = ½ × {r}² × {rad_str} = {correct}"
        
        else:
            values = [
                ('sin', 'π/6', '1/2'), ('cos', 'π/3', '1/2'),
                ('sin', 'π/4', '√2/2'), ('cos', 'π/4', '√2/2'),
                ('tan', 'π/4', '1'), ('sin', 'π/2', '1'),
            ]
            func, rad, correct = random.choice(values)
            distractors = ['0', '1', '-1', '1/2', '√2/2', '√3/2']
            distractors = [d for d in distractors if d != correct][:3]
            question = f"Evaluate {func}({rad})."
            explanation = f"{func}({rad}) = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    return questions

def generate_level_5():
    """Level 5: Trig Identities"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            identities = [
                ("sin²θ + cos²θ", "1", ["0", "2", "sin θ cos θ"]),
                ("1 + tan²θ", "sec²θ", ["csc²θ", "cot²θ", "1"]),
                ("1 + cot²θ", "csc²θ", ["sec²θ", "tan²θ", "1"]),
            ]
            expr, correct, distractors = random.choice(identities)
            question = f"Simplify: {expr}"
            explanation = f"Using Pythagorean identity: {expr} = {correct}"
        
        elif qtype == 2:
            identities = [
                ("1/sin θ", "csc θ", ["sec θ", "cot θ", "tan θ"]),
                ("1/cos θ", "sec θ", ["csc θ", "tan θ", "cot θ"]),
                ("sin θ/cos θ", "tan θ", ["cot θ", "sec θ", "csc θ"]),
            ]
            expr, correct, distractors = random.choice(identities)
            question = f"Simplify: {expr}"
            explanation = f"Using reciprocal/quotient identity: {expr} = {correct}"
        
        elif qtype == 3:
            sin_vals = [('3/5', '4/5'), ('5/13', '12/13'), ('8/17', '15/17')]
            sin_v, cos_v = random.choice(sin_vals)
            given = random.choice(['sin', 'cos'])
            find = 'cos' if given == 'sin' else 'sin'
            if given == 'sin':
                correct = cos_v
                question = f"If sin θ = {sin_v} and θ is in Quadrant 1, find cos θ."
            else:
                correct = sin_v
                question = f"If cos θ = {cos_v} and θ is in Quadrant 1, find sin θ."
            distractors = [sin_v if correct == cos_v else cos_v, '1/2', '3/4']
            explanation = f"Using sin²θ + cos²θ = 1: {find} θ = {correct}"
        
        elif qtype == 4:
            expressions = [
                ("sin θ csc θ", "1", ["sin²θ", "0", "cos θ"]),
                ("cos θ sec θ", "1", ["cos²θ", "0", "sin θ"]),
                ("tan θ cot θ", "1", ["tan²θ", "0", "sin θ cos θ"]),
            ]
            expr, correct, distractors = random.choice(expressions)
            question = f"Simplify: {expr}"
            explanation = f"{expr} = {correct}"
        
        else:
            true_identities = ["sin(-θ) = -sin θ", "cos(-θ) = cos θ", "tan(-θ) = -tan θ"]
            false_statements = ["sin(-θ) = sin θ", "cos(-θ) = -cos θ", "tan(-θ) = tan θ"]
            is_true = random.choice([True, False])
            if is_true:
                statement = random.choice(true_identities)
                correct = "True"
            else:
                statement = random.choice(false_statements)
                correct = "False"
            distractors = ["True" if correct == "False" else "False", "Only for acute angles", "Sometimes true"]
            question = f"Is this identity correct? {statement}"
            explanation = f"The statement '{statement}' is {correct}."
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    return questions

def generate_level_6():
    """Level 6: Solving Trig Equations"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            equations = [
                ("sin θ = 1/2", "30° and 150°", ["30° and 210°", "60° and 120°", "45° and 135°"]),
                ("sin θ = √2/2", "45° and 135°", ["45° and 225°", "30° and 150°", "60° and 120°"]),
                ("sin θ = √3/2", "60° and 120°", ["30° and 150°", "45° and 135°", "60° and 240°"]),
            ]
            eq, correct, distractors = random.choice(equations)
            question = f"Solve {eq} for 0° ≤ θ < 360°."
            explanation = f"The solutions are θ = {correct}"
        
        elif qtype == 2:
            equations = [
                ("cos θ = 1/2", "60° and 300°", ["60° and 120°", "30° and 330°", "45° and 315°"]),
                ("cos θ = √2/2", "45° and 315°", ["45° and 135°", "30° and 330°", "60° and 300°"]),
                ("cos θ = √3/2", "30° and 330°", ["60° and 300°", "45° and 315°", "30° and 150°"]),
            ]
            eq, correct, distractors = random.choice(equations)
            question = f"Solve {eq} for 0° ≤ θ < 360°."
            explanation = f"The solutions are θ = {correct}"
        
        elif qtype == 3:
            equations = [
                ("tan θ = 1", "45° and 225°", ["45° and 135°", "45° and 315°", "30° and 210°"]),
                ("tan θ = √3", "60° and 240°", ["30° and 210°", "60° and 120°", "45° and 225°"]),
                ("tan θ = -1", "135° and 315°", ["45° and 225°", "45° and 315°", "135° and 225°"]),
            ]
            eq, correct, distractors = random.choice(equations)
            question = f"Solve {eq} for 0° ≤ θ < 360°."
            explanation = f"The solutions are θ = {correct}"
        
        elif qtype == 4:
            equations = [
                ("sin θ = 0.5 for 0° ≤ θ < 360°", "2", ["1", "3", "4"]),
                ("cos θ = 0 for 0° ≤ θ < 360°", "2", ["1", "3", "4"]),
                ("sin θ = 1 for 0° ≤ θ < 360°", "1", ["2", "0", "4"]),
                ("cos θ = 2 for 0° ≤ θ < 360°", "0", ["1", "2", "4"]),
            ]
            eq, correct, distractors = random.choice(equations)
            question = f"How many solutions does {eq} have?"
            explanation = f"The equation has {correct} solution(s)."
        
        else:
            equations = [
                ("sin θ = 1/2 for 0 ≤ θ < 2π", "π/6 and 5π/6", ["π/6 and 7π/6", "π/3 and 2π/3", "π/4 and 3π/4"]),
                ("cos θ = 1/2 for 0 ≤ θ < 2π", "π/3 and 5π/3", ["π/3 and 2π/3", "π/6 and 11π/6", "π/4 and 7π/4"]),
                ("tan θ = 1 for 0 ≤ θ < 2π", "π/4 and 5π/4", ["π/4 and 3π/4", "π/4 and 7π/4", "π/3 and 4π/3"]),
            ]
            eq, correct, distractors = random.choice(equations)
            question = f"Solve {eq}."
            explanation = f"The solutions are θ = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    return questions

def generate_level_7():
    """Level 7: Graphs of Trig Functions"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            a = random.randint(2, 6)
            func = random.choice(['sin', 'cos'])
            correct = str(a)
            distractors = [str(a + 1), str(a - 1), str(2 * a)]
            question = f"What is the amplitude of y = {a}{func} x?"
            explanation = f"For y = a·{func} x, the amplitude is |a| = {a}"
        
        elif qtype == 2:
            b_values = [(1, '2π'), (2, 'π'), (3, '2π/3'), (4, 'π/2')]
            b, period = random.choice(b_values)
            func = random.choice(['sin', 'cos'])
            correct = period
            all_periods = ['2π', 'π', '2π/3', 'π/2', '4π']
            distractors = [p for p in all_periods if p != correct][:3]
            question = f"What is the period of y = {func}({b}x)?"
            explanation = f"For y = {func}(bx), period = 2π/b = 2π/{b} = {period}"
        
        elif qtype == 3:
            shifts = [
                ("sin(x - π/4)", "π/4 right", ["π/4 left", "π/2 right", "No shift"]),
                ("sin(x + π/3)", "π/3 left", ["π/3 right", "π/6 left", "No shift"]),
                ("cos(x - π/2)", "π/2 right", ["π/2 left", "π right", "No shift"]),
            ]
            func, correct, distractors = random.choice(shifts)
            question = f"What is the phase shift of y = {func}?"
            explanation = f"For y = {func}, the phase shift is {correct}"
        
        elif qtype == 4:
            k = random.randint(1, 5) * random.choice([1, -1])
            func = random.choice(['sin', 'cos'])
            if k > 0:
                correct = f"{k} units up"
            else:
                correct = f"{abs(k)} units down"
            distractors = [f"{abs(k)} units {'down' if k > 0 else 'up'}", f"{abs(k) + 1} units {'up' if k > 0 else 'down'}", "No vertical shift"]
            eq = f"y = {func} x + {k}" if k > 0 else f"y = {func} x - {abs(k)}"
            question = f"What is the vertical shift of {eq}?"
            explanation = f"The graph is shifted {correct}"
        
        else:
            a = random.randint(1, 4)
            k = random.randint(-3, 3)
            func = random.choice(['sin', 'cos'])
            min_val = -a + k
            max_val = a + k
            correct = f"[{min_val}, {max_val}]"
            distractors = [f"[{min_val - 1}, {max_val + 1}]", f"[-{a}, {a}]", f"[{k - 1}, {k + 1}]"]
            if k >= 0:
                eq = f"y = {a}{func} x + {k}" if a > 1 else f"y = {func} x + {k}"
            else:
                eq = f"y = {a}{func} x - {abs(k)}" if a > 1 else f"y = {func} x - {abs(k)}"
            question = f"What is the range of {eq}?"
            explanation = f"Range = [-a + k, a + k] = [{min_val}, {max_val}]"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    return questions

def generate_level_8():
    """Level 8: Compound Angle Formulas"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            formulas = [
                ("sin(A + B)", "sin A cos B + cos A sin B", ["sin A sin B + cos A cos B", "sin A cos B - cos A sin B", "cos A cos B - sin A sin B"]),
                ("sin(A - B)", "sin A cos B - cos A sin B", ["sin A cos B + cos A sin B", "sin A sin B - cos A cos B", "cos A cos B + sin A sin B"]),
                ("cos(A + B)", "cos A cos B - sin A sin B", ["cos A cos B + sin A sin B", "sin A cos B + cos A sin B", "sin A sin B - cos A cos B"]),
                ("cos(A - B)", "cos A cos B + sin A sin B", ["cos A cos B - sin A sin B", "sin A cos B - cos A sin B", "sin A sin B + cos A cos B"]),
            ]
            lhs, correct, distractors = random.choice(formulas)
            question = f"The expansion of {lhs} is:"
            explanation = f"{lhs} = {correct}"
        
        elif qtype == 2:
            calculations = [
                ("sin 75°", "sin(45° + 30°)", "(√6 + √2)/4", ["(√6 - √2)/4", "√3/2", "(√2 + 1)/2"]),
                ("cos 75°", "cos(45° + 30°)", "(√6 - √2)/4", ["(√6 + √2)/4", "√2/2", "(√3 - 1)/2"]),
                ("sin 15°", "sin(45° - 30°)", "(√6 - √2)/4", ["(√6 + √2)/4", "√3/4", "(√2 - 1)/2"]),
            ]
            expr, expansion, correct, distractors = random.choice(calculations)
            question = f"Evaluate {expr} using compound angle formulas."
            explanation = f"{expr} = {expansion} = {correct}"
        
        elif qtype == 3:
            formulas = [
                ("tan(A + B)", "(tan A + tan B)/(1 - tan A tan B)", ["(tan A - tan B)/(1 + tan A tan B)", "tan A + tan B", "tan A tan B"]),
                ("tan(A - B)", "(tan A - tan B)/(1 + tan A tan B)", ["(tan A + tan B)/(1 - tan A tan B)", "tan A - tan B", "tan A / tan B"]),
            ]
            lhs, correct, distractors = random.choice(formulas)
            question = f"The formula for {lhs} is:"
            explanation = f"{lhs} = {correct}"
        
        elif qtype == 4:
            expressions = [
                ("sin 50° cos 40° + cos 50° sin 40°", "sin 90°", "1", ["0", "√2/2", "√3/2"]),
                ("cos 70° cos 20° + sin 70° sin 20°", "cos 50°", "cos 50°", ["sin 50°", "1", "0"]),
                ("sin 80° cos 20° - cos 80° sin 20°", "sin 60°", "√3/2", ["1/2", "√2/2", "1"]),
            ]
            expr, simplified, correct, distractors = random.choice(expressions)
            question = f"Simplify: {expr}"
            explanation = f"{expr} = {simplified} = {correct}"
        
        else:
            scenarios = [
                ("If sin A = 3/5 and cos B = 12/13 (A, B in Q1), find sin(A + B)", 
                 "sin A cos B + cos A sin B = (3/5)(12/13) + (4/5)(5/13) = 56/65", 
                 "56/65", ["16/65", "36/65", "20/65"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    return questions

def generate_level_9():
    """Level 9: Double Angle Formulas"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            formulas = [
                ("sin 2A", "2 sin A cos A", ["sin²A + cos²A", "2 sin A + 2 cos A", "sin²A - cos²A"]),
                ("cos 2A (first form)", "cos²A - sin²A", ["sin²A - cos²A", "2 cos²A", "2 sin²A"]),
                ("cos 2A (second form)", "2cos²A - 1", ["1 - 2cos²A", "cos²A - 1", "2cos²A + 1"]),
                ("tan 2A", "2tan A/(1 - tan²A)", ["2tan A/(1 + tan²A)", "tan²A - 1", "2tan A"]),
            ]
            lhs, correct, distractors = random.choice(formulas)
            question = f"Express {lhs} in terms of single angles:"
            explanation = f"{lhs} = {correct}"
        
        elif qtype == 2:
            calculations = [
                ("2 sin 30° cos 30°", "sin 60°", "√3/2", ["1/2", "√2/2", "1"]),
                ("cos²45° - sin²45°", "cos 90°", "0", ["1", "√2/2", "1/2"]),
                ("2cos²30° - 1", "cos 60°", "1/2", ["√3/2", "0", "√2/2"]),
            ]
            expr, equals, correct, distractors = random.choice(calculations)
            question = f"Evaluate: {expr}"
            explanation = f"{expr} = {equals} = {correct}"
        
        elif qtype == 3:
            values = [
                ("sin A = 3/5 (A in Q1)", "sin 2A = 2 sin A cos A = 2(3/5)(4/5)", "24/25", ["12/25", "7/25", "18/25"]),
                ("sin A = 3/5 (A in Q1)", "cos 2A = 1 - 2sin²A = 1 - 2(9/25)", "7/25", ["24/25", "-7/25", "18/25"]),
            ]
            given, calc, correct, distractors = random.choice(values)
            find = "sin 2A" if "sin 2A" in calc else "cos 2A"
            question = f"If {given}, find {find}."
            explanation = f"{calc} = {correct}"
        
        elif qtype == 4:
            expressions = [
                ("sin 4x", "2 sin 2x cos 2x", ["sin²2x + cos²2x", "4 sin x cos x", "sin 2x + cos 2x"]),
                ("(sin x + cos x)²", "1 + sin 2x", ["1 - sin 2x", "sin 2x", "cos 2x"]),
            ]
            expr, correct, distractors = random.choice(expressions)
            question = f"Simplify: {expr}"
            explanation = f"{expr} = {correct}"
        
        else:
            expressions = [
                ("If cos 2A = 7/25, find cos²A (A in Q1)", "(1 + cos 2A)/2 = (1 + 7/25)/2", "16/25", ["9/25", "7/25", "18/25"]),
                ("If cos 2A = 7/25, find sin²A (A in Q1)", "(1 - cos 2A)/2 = (1 - 7/25)/2", "9/25", ["16/25", "7/25", "18/25"]),
            ]
            q_text, calc, correct, distractors = random.choice(expressions)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    return questions

def generate_level_10():
    """Level 10: Sine & Cosine Rules"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            rules = [
                ("Sine Rule", "a/sin A = b/sin B = c/sin C", ["a sin A = b sin B", "a/cos A = b/cos B", "a² = b² + c²"]),
                ("Cosine Rule (find side)", "a² = b² + c² - 2bc cos A", ["a² = b² + c² + 2bc cos A", "a = b + c - 2bc cos A", "a² = b² - c² + 2bc cos A"]),
            ]
            name, correct, distractors = random.choice(rules)
            question = f"State the {name}:"
            explanation = f"The {name} states: {correct}"
        
        elif qtype == 2:
            scenarios = [
                ("In triangle ABC, a = 10, A = 30°, B = 45°. Find b using sine rule.", 
                 "b = a sin B / sin A = 10 × sin 45° / sin 30°", "10√2", ["10", "5√2", "20"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        elif qtype == 3:
            scenarios = [
                ("In triangle ABC, a = 10, b = 10, A = 60°. Find B.",
                 "Since a = b, the triangle is isosceles, so B = A", "60°", ["30°", "45°", "90°"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        elif qtype == 4:
            scenarios = [
                ("In triangle ABC, b = 5, c = 8, A = 60°. Find a.",
                 "a² = b² + c² - 2bc cos A = 25 + 64 - 80(1/2) = 49", "7", ["8", "6", "9"]),
                ("In triangle ABC, b = 3, c = 4, A = 90°. Find a.",
                 "a² = b² + c² - 2bc cos 90° = 9 + 16 - 0 = 25", "5", ["6", "7", "4"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc}, so a = {correct}"
        
        else:
            scenarios = [
                ("In triangle ABC, a = 7, b = 5, c = 8. Find cos A.",
                 "cos A = (b² + c² - a²)/(2bc) = (25 + 64 - 49)/(80) = 40/80", "1/2", ["1/4", "3/4", "√3/2"]),
                ("In triangle ABC, a = 5, b = 4, c = 3. Find cos A.",
                 "cos A = (b² + c² - a²)/(2bc) = (16 + 9 - 25)/(24) = 0/24", "0", ["1/2", "1/4", "√3/2"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    return questions

def generate_level_11():
    """Level 11: Area & Applications"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            a = random.randint(4, 10)
            b = random.randint(4, 10)
            angle = random.choice([30, 45, 60, 90])
            if angle == 30:
                area = f"{a*b}/4" if a*b % 4 != 0 else str(a*b//4)
            elif angle == 45:
                area = f"{a*b}√2/4"
            elif angle == 60:
                area = f"{a*b}√3/4"
            else:
                area = str(a*b//2)
            correct = area
            distractors = [str(a*b), str(a*b//2), f"{a*b}/2"]
            distractors = [d for d in distractors if d != correct][:3]
            question = f"Find the area of triangle with sides {a} and {b} and included angle {angle}°."
            explanation = f"Area = ½ab sin C = ½ × {a} × {b} × sin {angle}° = {correct}"
        
        elif qtype == 2:
            a, b, c = 3, 4, 5
            correct = "6"
            distractors = ["7", "8", "12"]
            question = f"Find the area of a triangle with sides {a}, {b}, {c}."
            explanation = f"Using Heron's formula: Area = √(6×3×2×1) = √36 = {correct}"
        
        elif qtype == 3:
            scenarios = [
                ("A flagpole casts a shadow 20m long when the angle of elevation of the sun is 60°. Find the height.",
                 "tan 60° = h/20, so h = 20 × tan 60° = 20√3", "20√3 m", ["20 m", "40 m", "10√3 m"]),
                ("From 50m away, the angle of elevation to a tower top is 45°. Find the tower height.",
                 "tan 45° = h/50, so h = 50", "50 m", ["25 m", "100 m", "50√2 m"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        elif qtype == 4:
            scenarios = [
                ("A ship sails 10km on bearing 060° then 10km on bearing 150°. Find distance from start.",
                 "The angle between paths is 90°. Using Pythagoras: d = √(100 + 100)", "10√2 km", ["10 km", "20 km", "15 km"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        else:
            scenarios = [
                ("A cube has side 4. Find the length of a space diagonal.",
                 "Space diagonal = √(4² + 4² + 4²) = √48", "4√3", ["4√2", "8", "12"]),
                ("A rectangular box has dimensions 3×4×12. Find the space diagonal.",
                 "Diagonal = √(9 + 16 + 144) = √169", "13", ["12", "15", "17"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc} = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 6)
        
        if qtype == 1:
            expressions = [
                ("sin 3A in terms of sin A", "3 sin A - 4 sin³A", ["3 sin A + 4 sin³A", "sin³A - 3 sin A", "4 sin³A - 3 sin A"]),
                ("cos 3A in terms of cos A", "4 cos³A - 3 cos A", ["3 cos A - 4 cos³A", "4 cos³A + 3 cos A", "cos³A - 3 cos A"]),
            ]
            expr, correct, distractors = random.choice(expressions)
            question = f"Express {expr}:"
            explanation = f"{expr} = {correct}"
        
        elif qtype == 2:
            equations = [
                ("2sin²x + sinx - 1 = 0 for 0° ≤ x < 360°", 
                 "(2sinx - 1)(sinx + 1) = 0, so sinx = 1/2 or sinx = -1",
                 "30°, 150°, 270°", ["30°, 150°", "60°, 300°", "45°, 135°, 225°, 315°"]),
                ("2cos²x - cosx - 1 = 0 for 0° ≤ x < 360°",
                 "(2cosx + 1)(cosx - 1) = 0",
                 "0°, 120°, 240°", ["60°, 300°", "0°, 180°", "90°, 270°"]),
            ]
            eq, working, correct, distractors = random.choice(equations)
            question = f"Solve: {eq}"
            explanation = f"{working}. Solutions: {correct}"
        
        elif qtype == 3:
            proofs = [
                ("To prove tan A + cot A = sec A csc A, the key step is:",
                 "(sin A/cos A) + (cos A/sin A) = (sin²A + cos²A)/(sin A cos A)",
                 ["sin A + cos A = 1", "tan A = sin A / cos A only", "cot A = 1"]),
            ]
            q_text, correct, distractors = random.choice(proofs)
            question = q_text
            explanation = f"The key step: {correct}"
        
        elif qtype == 4:
            calculations = [
                ("tan 22.5°", "Using tan 45° = 2tan22.5°/(1-tan²22.5°)", "√2 - 1", ["√2 + 1", "1/√2", "2 - √2"]),
            ]
            expr, method, correct, distractors = random.choice(calculations)
            question = f"Find the exact value of {expr}."
            explanation = f"{method}: {expr} = {correct}"
        
        elif qtype == 5:
            scenarios = [
                ("From point A, a tower has angle of elevation 30°. From B, 100m closer, it's 60°. Find tower height.",
                 "Using tan relationships", "50√3 m", ["100 m", "50 m", "100√3 m"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc}. Answer = {correct}"
        
        else:
            scenarios = [
                ("Find the maximum value of 3sin x + 4cos x",
                 "R sin(x + α) form where R = √(9+16) = 5",
                 "5", ["3", "4", "7"]),
                ("Find the minimum value of 5 - 3cos x",
                 "cos x has max 1, so minimum is 5 - 3(1) = 2",
                 "2", ["5", "8", "-3"]),
                ("Find the range of 2 + 3sin x",
                 "-1 ≤ sin x ≤ 1, so -1 ≤ 2 + 3sin x ≤ 5",
                 "[-1, 5]", ["[-3, 3]", "[2, 5]", "[-1, 3]"]),
            ]
            q_text, calc, correct, distractors = random.choice(scenarios)
            question = q_text
            explanation = f"{calc}. Answer = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    return questions

def main():
    all_questions = []
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12,
    ]
    
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
    
    sql_file = f'/home/claude/{TOPIC}_questions.sql'
    with open(sql_file, 'w') as f:
        f.write(f"-- LC Higher Level - Trigonometry Questions\n")
        f.write(f"-- Generated: 2025-12-15\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
