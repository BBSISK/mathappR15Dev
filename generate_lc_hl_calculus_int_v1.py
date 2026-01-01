#!/usr/bin/env python3
"""
LC Higher Level - Calculus (Integration) Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level × 12 levels) for LC HL Calculus - Integration

Levels:
1. Basic Integration (Foundation)
2. Power Rule Integration (Foundation)
3. Trig Integration (Foundation)
4. Exponential Integration (Developing)
5. Definite Integrals (Developing)
6. Area Under Curve (Developing)
7. Area Between Curves (Proficient)
8. Average Value (Proficient)
9. Applied Integration (Proficient)
10. Substitution Method (Advanced)
11. Complex Applications (Advanced)
12. Mastery Challenge (Advanced)
"""

import random

# Configuration
TOPIC = 'lc_hl_calculus_int'
MODE = 'lc_hl'
QUESTIONS_PER_LEVEL = 50

LEVEL_TITLES = [
    'Basic Integration', 'Power Rule Integration', 'Trig Integration',
    'Exponential Integration', 'Definite Integrals', 'Area Under Curve',
    'Area Between Curves', 'Average Value', 'Applied Integration',
    'Substitution Method', 'Complex Applications', 'Mastery Challenge'
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
        unique_wrong.append(f"Option {len(unique_wrong) + 2}")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

# ============================================================
# LEVEL 1: Basic Integration (Foundation)
# ============================================================
def generate_level_1():
    """Basic Integration - reverse of differentiation"""
    questions = []
    
    # Type 1: ∫xⁿ dx
    for _ in range(25):
        n = random.randint(1, 5)
        new_power = n + 1
        correct = f"x^{new_power}/{new_power} + C"
        
        distractors = [f"x^{n}/{n} + C", f"{new_power}x^{new_power} + C", f"x^{new_power} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫x^{n} dx = x^{n+1}/{n+1} + C = {correct} ✓"
        
        questions.append({
            'question_text': f"Find ∫x^{n} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: ∫a dx (constant)
    for _ in range(15):
        a = random.choice([2, 3, 4, 5, 7])
        correct = f"{a}x + C"
        
        distractors = [f"{a} + C", f"x + C", f"{a}x"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫{a} dx = {a}x + C. Constant integrates to constant × x ✓"
        
        questions.append({
            'question_text': f"Find ∫{a} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: ∫1 dx
    for _ in range(10):
        correct = "x + C"
        distractors = ["1 + C", "0 + C", "C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "∫1 dx = x + C. The constant 1 integrates to x ✓"
        
        questions.append({
            'question_text': "Find ∫1 dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 2: Power Rule Integration (Foundation)
# ============================================================
def generate_level_2():
    """Power Rule Integration with coefficients"""
    questions = []
    
    # Type 1: ∫axⁿ dx
    for _ in range(25):
        a = random.choice([2, 3, 4, 5, 6])
        n = random.randint(2, 5)
        new_power = n + 1
        new_coef = a  # coefficient stays, divided by new power
        
        # Simplify if possible
        from math import gcd
        g = gcd(a, new_power)
        if g > 1:
            correct = f"{a//g}x^{new_power}/{new_power//g} + C" if new_power//g > 1 else f"{a//g}x^{new_power} + C"
        else:
            correct = f"{a}x^{new_power}/{new_power} + C"
        
        distractors = [f"{a}x^{n}/{n} + C", f"x^{new_power}/{new_power} + C", f"{a*new_power}x^{new_power} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫{a}x^{n} dx = {a} × x^{new_power}/{new_power} + C = {correct} ✓"
        
        questions.append({
            'question_text': f"Find ∫{a}x^{n} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: ∫(ax + b) dx
    for _ in range(15):
        a = random.choice([2, 3, 4])
        b = random.choice([1, 2, 3, -1, -2])
        
        b_str = f"+ {b}" if b > 0 else f"- {abs(b)}"
        correct = f"{a}x²/2 {b_str}x + C"
        
        distractors = [f"{a}x {b_str} + C", f"x²/2 {b_str}x + C", f"{a}x² {b_str}x + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫({a}x {b_str}) dx = {a}x²/2 {b_str}x + C ✓"
        
        questions.append({
            'question_text': f"Find ∫({a}x {b_str}) dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: ∫x⁻ⁿ dx (negative powers)
    for _ in range(10):
        n = random.choice([2, 3])
        # ∫x⁻ⁿ dx = x⁻ⁿ⁺¹/(-n+1) + C = -1/(n-1) × x^(1-n) + C
        new_power = -n + 1
        
        if new_power == -1:
            correct = f"-1/x + C"
        else:
            correct = f"x^{new_power}/{new_power} + C"
        
        distractors = [f"-{n}x^{-n-1} + C", f"x^{-n+1} + C", f"1/x^{n} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫x^{-n} dx = x^{-n+1}/{-n+1} + C = {correct} ✓"
        
        questions.append({
            'question_text': f"Find ∫x^{-n} dx (i.e., ∫1/x^{n} dx)",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 3: Trig Integration (Foundation)
# ============================================================
def generate_level_3():
    """Trigonometric integration"""
    questions = []
    
    # Type 1: Basic trig integrals
    trig_integrals = [
        ("∫cos x dx", "sin x + C", "-sin x + C", "cos x + C", "-cos x + C"),
        ("∫sin x dx", "-cos x + C", "cos x + C", "sin x + C", "-sin x + C"),
        ("∫sec²x dx", "tan x + C", "sec x + C", "-tan x + C", "cot x + C"),
        ("∫cos 2x dx", "sin 2x/2 + C", "sin 2x + C", "2sin 2x + C", "-sin 2x/2 + C"),
        ("∫sin 2x dx", "-cos 2x/2 + C", "cos 2x/2 + C", "-cos 2x + C", "2cos 2x + C"),
    ]
    
    for _ in range(20):
        q, correct, d1, d2, d3 = random.choice(trig_integrals)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{q} = {correct}. Remember: ∫cos = sin, ∫sin = -cos ✓"
        
        questions.append({
            'question_text': f"Find {q}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: ∫cos(ax) dx
    for _ in range(15):
        a = random.choice([2, 3, 4, 5])
        correct = f"sin({a}x)/{a} + C"
        
        distractors = [f"sin({a}x) + C", f"{a}sin({a}x) + C", f"-sin({a}x)/{a} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫cos({a}x) dx = sin({a}x)/{a} + C. Divide by coefficient of x ✓"
        
        questions.append({
            'question_text': f"Find ∫cos({a}x) dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: ∫sin(ax) dx
    for _ in range(15):
        a = random.choice([2, 3, 4, 5])
        correct = f"-cos({a}x)/{a} + C"
        
        distractors = [f"cos({a}x)/{a} + C", f"-{a}cos({a}x) + C", f"-cos({a}x) + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫sin({a}x) dx = -cos({a}x)/{a} + C ✓"
        
        questions.append({
            'question_text': f"Find ∫sin({a}x) dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 4: Exponential Integration (Developing)
# ============================================================
def generate_level_4():
    """Exponential integration"""
    questions = []
    
    # Type 1: ∫eˣ dx
    for _ in range(10):
        correct = "eˣ + C"
        distractors = ["xeˣ + C", "eˣ⁻¹ + C", "eˣ/x + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "∫eˣ dx = eˣ + C. eˣ is its own integral! ✓"
        
        questions.append({
            'question_text': "Find ∫eˣ dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: ∫e^(ax) dx
    for _ in range(20):
        a = random.choice([2, 3, 4, 5, -2, -3])
        correct = f"e^{{{a}x}}/{a} + C"
        
        distractors = [f"e^{{{a}x}} + C", f"{a}e^{{{a}x}} + C", f"e^{{{a-1}x}} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫e^{{{a}x}} dx = e^{{{a}x}}/{a} + C. Divide by coefficient of x ✓"
        
        questions.append({
            'question_text': f"Find ∫e^{{{a}x}} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: ∫1/x dx
    for _ in range(10):
        correct = "ln|x| + C"
        distractors = ["1/x² + C", "x + C", "ln(x) + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "∫1/x dx = ln|x| + C. Special case - not power rule! ✓"
        
        questions.append({
            'question_text': "Find ∫1/x dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 4: ∫a/x dx
    for _ in range(10):
        a = random.choice([2, 3, 4, 5])
        correct = f"{a}ln|x| + C"
        
        distractors = [f"ln|{a}x| + C", f"{a}/x + C", f"ln|x|/{a} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫{a}/x dx = {a}∫1/x dx = {a}ln|x| + C ✓"
        
        questions.append({
            'question_text': f"Find ∫{a}/x dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 5: Definite Integrals (Developing)
# ============================================================
def generate_level_5():
    """Definite integrals with limits"""
    questions = []
    
    # Type 1: ∫[a,b] xⁿ dx
    for _ in range(20):
        n = random.choice([1, 2, 3])
        a, b = 0, random.choice([1, 2, 3])
        
        # ∫xⁿ dx = x^(n+1)/(n+1)
        new_power = n + 1
        result = (b ** new_power) / new_power - (a ** new_power) / new_power
        
        if result == int(result):
            correct = str(int(result))
        else:
            # Express as fraction
            correct = f"{b**new_power}/{new_power}"
        
        distractors = [str(b**n), str(b**(new_power)), str(new_power * b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫₀^{b} x^{n} dx = [x^{new_power}/{new_power}]₀^{b} = {b}^{new_power}/{new_power} - 0 = {correct} ✓"
        
        questions.append({
            'question_text': f"Evaluate ∫₀^{b} x^{n} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: ∫[a,b] c dx (constant)
    for _ in range(15):
        c = random.choice([2, 3, 4, 5])
        a, b = random.choice([0, 1]), random.choice([2, 3, 4, 5])
        result = c * (b - a)
        
        correct = str(result)
        distractors = [str(c * b), str(b - a), str(c + b - a)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"∫_{a}^{b} {c} dx = {c}[x]_{a}^{b} = {c}({b} - {a}) = {result} ✓"
        
        questions.append({
            'question_text': f"Evaluate ∫_{a}^{b} {c} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: ∫[0,π] sin x dx or cos x dx
    for _ in range(15):
        trig = random.choice(['sin', 'cos'])
        if trig == 'sin':
            # ∫₀^π sin x dx = [-cos x]₀^π = -cos π - (-cos 0) = -(-1) - (-1) = 1 + 1 = 2
            correct = "2"
            q = "∫₀^π sin x dx"
        else:
            # ∫₀^π cos x dx = [sin x]₀^π = sin π - sin 0 = 0 - 0 = 0
            correct = "0"
            q = "∫₀^π cos x dx"
        
        distractors = ["1", "-1", "π"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{q} = {correct}. Remember to evaluate at both limits! ✓"
        
        questions.append({
            'question_text': f"Evaluate {q}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 6: Area Under Curve (Developing)
# ============================================================
def generate_level_6():
    """Area under curve problems"""
    questions = []
    
    # Type 1: Area under y = x² from 0 to a
    for _ in range(20):
        a = random.choice([1, 2, 3])
        # Area = ∫₀^a x² dx = [x³/3]₀^a = a³/3
        result_num = a ** 3
        
        correct = f"{result_num}/3"
        if result_num % 3 == 0:
            correct = str(result_num // 3)
        
        distractors = [f"{a**2}/2", str(a**2), str(a**3)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Area = ∫₀^{a} x² dx = [x³/3]₀^{a} = {a}³/3 = {correct} ✓"
        
        questions.append({
            'question_text': f"Find the area under y = x² from x = 0 to x = {a}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Area under y = ax from 0 to b
    for _ in range(15):
        a = random.choice([2, 3, 4])
        b = random.choice([2, 3, 4])
        # Area = ∫₀^b ax dx = [ax²/2]₀^b = ab²/2
        result_num = a * b * b
        
        correct = f"{result_num}/2" if result_num % 2 != 0 else str(result_num // 2)
        
        distractors = [str(a * b), str(b * b), f"{a * b}/2"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Area = ∫₀^{b} {a}x dx = [{a}x²/2]₀^{b} = {a}×{b}²/2 = {correct} ✓"
        
        questions.append({
            'question_text': f"Find the area under y = {a}x from x = 0 to x = {b}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Area under y = c (rectangle)
    for _ in range(15):
        c = random.choice([2, 3, 4, 5])
        a, b = 0, random.choice([2, 3, 4])
        result = c * b
        
        correct = str(result)
        distractors = [str(c + b), str(c * b + b), str(b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Area = ∫₀^{b} {c} dx = {c} × {b} = {result}. It's a rectangle! ✓"
        
        questions.append({
            'question_text': f"Find the area under y = {c} from x = 0 to x = {b}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 7: Area Between Curves (Proficient)
# ============================================================
def generate_level_7():
    """Area between two curves"""
    questions = []
    
    # Type 1: Area between y = x² and y = x
    for _ in range(15):
        # Intersect at x = 0 and x = 1
        # Area = ∫₀¹ (x - x²) dx = [x²/2 - x³/3]₀¹ = 1/2 - 1/3 = 1/6
        correct = "1/6"
        distractors = ["1/3", "1/2", "1/4"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "Area = ∫₀¹ (x - x²) dx = [x²/2 - x³/3]₀¹ = 1/2 - 1/3 = 1/6 ✓"
        
        questions.append({
            'question_text': "Find the area between y = x and y = x² (from x = 0 to x = 1)",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Area between y = a and y = x² from 0 to √a
    for _ in range(15):
        a = random.choice([1, 4, 9])
        sqrt_a = int(a ** 0.5)
        # Area = ∫₀^√a (a - x²) dx = [ax - x³/3]₀^√a = a√a - (√a)³/3 = a√a - a√a/3 = 2a√a/3
        result = 2 * a * sqrt_a / 3
        
        if result == int(result):
            correct = str(int(result))
        else:
            correct = f"{2*a*sqrt_a}/3"
        
        distractors = [str(a * sqrt_a), f"{a*sqrt_a}/3", str(a)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Area between y = {a} and y = x² from 0 to {sqrt_a} = {correct} ✓"
        
        questions.append({
            'question_text': f"Find the area between y = {a} and y = x² from x = 0 to x = {sqrt_a}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Top - bottom conceptual
    for _ in range(20):
        questions_list = [
            ("To find area between curves, you integrate...", "top curve - bottom curve", 
             "bottom - top", "top + bottom", "top × bottom"),
            ("If f(x) > g(x) on [a,b], area between = ", "∫[f(x) - g(x)]dx", 
             "∫[g(x) - f(x)]dx", "∫f(x)dx - ∫g(x)dx separately", "∫[f(x) + g(x)]dx"),
        ]
        q, correct, d1, d2, d3 = random.choice(questions_list)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{correct}. Always integrate (upper - lower) curve ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 8: Average Value (Proficient)
# ============================================================
def generate_level_8():
    """Average value of a function"""
    questions = []
    
    # Type 1: Average of x² on [0, a]
    for _ in range(20):
        a = random.choice([1, 2, 3])
        # Average = (1/a)∫₀^a x² dx = (1/a)(a³/3) = a²/3
        result = a * a / 3
        
        if result == int(result):
            correct = str(int(result))
        else:
            correct = f"{a*a}/3"
        
        distractors = [f"{a}/3", str(a*a), f"{a*a}/2"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Average = (1/{a})∫₀^{a} x² dx = (1/{a}) × {a}³/3 = {a}²/3 = {correct} ✓"
        
        questions.append({
            'question_text': f"Find the average value of f(x) = x² on [0, {a}]",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Average of constant
    for _ in range(15):
        c = random.choice([2, 3, 4, 5])
        a, b = 0, random.choice([2, 3, 4])
        correct = str(c)
        
        distractors = [str(c * b), str(c + b), str(c * b / 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Average of constant {c} is just {c}. ∫{c}dx / width = {c}×width / width = {c} ✓"
        
        questions.append({
            'question_text': f"Find the average value of f(x) = {c} on [0, {b}]",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Average value formula
    for _ in range(15):
        correct = "1/(b-a) × ∫[a,b] f(x)dx"
        distractors = ["∫[a,b] f(x)dx", "(b-a) × ∫[a,b] f(x)dx", "∫[a,b] f(x)dx / f(a)"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "Average value formula: (1/(b-a)) × ∫[a,b] f(x)dx = integral ÷ interval width ✓"
        
        questions.append({
            'question_text': "The formula for average value of f(x) on [a,b] is:",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 9: Applied Integration (Proficient)
# ============================================================
def generate_level_9():
    """Applied integration problems"""
    questions = []
    
    # Type 1: Distance from velocity
    for _ in range(20):
        # v(t) = at, distance = ∫v dt = at²/2
        a = random.choice([2, 4, 6])
        t = random.choice([2, 3, 4])
        distance = a * t * t // 2
        
        correct = f"{distance} m"
        distractors = [f"{a*t} m", f"{a*t*t} m", f"{t*t} m"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Distance = ∫₀^{t} {a}t dt = [{a}t²/2]₀^{t} = {a}×{t}²/2 = {distance} m ✓"
        
        questions.append({
            'question_text': f"If velocity v(t) = {a}t m/s, find distance travelled from t=0 to t={t}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Total from rate
    for _ in range(15):
        rate = random.choice([10, 20, 50])
        t = random.choice([2, 3, 4, 5])
        total = rate * t
        
        correct = str(total)
        distractors = [str(rate), str(rate + t), str(rate * t + rate)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"If rate = {rate}/hour, total in {t} hours = ∫₀^{t} {rate} dt = {rate}×{t} = {total} ✓"
        
        questions.append({
            'question_text': f"Water flows at {rate} litres/hour. How much flows in {t} hours?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Conceptual - integration finds total
    for _ in range(15):
        concepts = [
            ("Integration of velocity gives...", "displacement", "acceleration", "speed", "velocity"),
            ("Integration of a rate gives...", "total quantity", "average rate", "maximum rate", "rate of change"),
            ("∫₀^t a dt where a is acceleration gives...", "velocity change", "position", "acceleration", "jerk"),
        ]
        q, correct, d1, d2, d3 = random.choice(concepts)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Integration finds total from rate. {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 10: Substitution Method (Advanced)
# ============================================================
def generate_level_10():
    """Integration by substitution"""
    questions = []
    
    # Type 1: ∫(ax+b)ⁿ dx
    for _ in range(20):
        a = random.choice([2, 3])
        b = random.choice([1, 2])
        n = random.choice([2, 3, 4])
        new_power = n + 1
        
        inner = f"{a}x + {b}"
        correct = f"({inner})^{new_power}/({a}×{new_power}) + C"
        
        distractors = [f"({inner})^{new_power}/{new_power} + C", 
                       f"{a}({inner})^{new_power} + C",
                       f"({inner})^{new_power}/{a} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Let u = {inner}, du = {a}dx. ∫u^{n} × (1/{a})du = u^{new_power}/({a}×{new_power}) + C ✓"
        
        questions.append({
            'question_text': f"Find ∫({inner})^{n} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: ∫x(x² + a)ⁿ dx
    for _ in range(15):
        a = random.choice([1, 2, 3])
        n = random.choice([2, 3])
        new_power = n + 1
        
        inner = f"x² + {a}"
        correct = f"({inner})^{new_power}/(2×{new_power}) + C"
        
        distractors = [f"({inner})^{new_power}/{new_power} + C",
                       f"2({inner})^{new_power} + C",
                       f"x({inner})^{new_power} + C"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Let u = {inner}, du = 2x dx. ∫(1/2)u^{n} du = u^{new_power}/(2×{new_power}) + C ✓"
        
        questions.append({
            'question_text': f"Find ∫x({inner})^{n} dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Substitution recognition
    for _ in range(15):
        recog = [
            ("For ∫f(g(x))g'(x)dx, what substitution?", "u = g(x)", "u = f(x)", "u = x", "u = f(g(x))"),
            ("For ∫x·e^(x²) dx, let u = ", "x²", "x", "e^x", "e^(x²)"),
            ("For ∫cos(3x) dx, let u = ", "3x", "cos x", "x", "sin(3x)"),
        ]
        q, correct, d1, d2, d3 = random.choice(recog)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"u = {correct}. Substitute the inner function ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

# ============================================================
# LEVEL 11: Complex Applications (Advanced)
# ============================================================
def generate_level_11():
    """Complex integration applications"""
    questions = []
    
    # Type 1: Setting up integrals
    for _ in range(15):
        setups = [
            ("Area between y = x² and y = 4 is", "∫_{-2}^{2} (4 - x²) dx", 
             "∫_{0}^{4} x² dx", "∫_{-2}^{2} x² dx", "∫_{0}^{2} (4 - x²) dx"),
            ("Volume of solid with circular cross-sections radius r(x) is", "∫ π[r(x)]² dx",
             "∫ 2πr(x) dx", "∫ r(x)² dx", "∫ πr(x) dx"),
        ]
        q, correct, d1, d2, d3 = random.choice(setups)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Correct setup: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Properties of integrals
    for _ in range(15):
        props = [
            ("∫[a,b] f(x)dx + ∫[b,c] f(x)dx = ", "∫[a,c] f(x)dx", "∫[a,b+c] f(x)dx", "0", "∫[b,b] f(x)dx"),
            ("∫[a,a] f(x)dx = ", "0", "f(a)", "2f(a)", "undefined"),
            ("∫[b,a] f(x)dx = ", "-∫[a,b] f(x)dx", "∫[a,b] f(x)dx", "0", "|∫[a,b] f(x)dx|"),
        ]
        q, correct, d1, d2, d3 = random.choice(props)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Integration property: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Multi-step calculations
    for _ in range(20):
        multi = [
            ("If ∫₀² f(x)dx = 5 and ∫₀² g(x)dx = 3, find ∫₀² [f(x) + g(x)]dx", "8", "15", "2", "5"),
            ("If ∫₀³ f(x)dx = 6, find ∫₀³ 2f(x)dx", "12", "6", "3", "8"),
            ("If ∫₁⁴ f(x)dx = 10, find ∫₄¹ f(x)dx", "-10", "10", "0", "undefined"),
        ]
        q, correct, d1, d2, d3 = random.choice(multi)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Using integral properties: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions

# ============================================================
# LEVEL 12: Mastery Challenge (Advanced)
# ============================================================
def generate_level_12():
    """Mixed challenging integration problems"""
    questions = []
    
    # SEC-style mixed questions
    sec_questions = [
        ("Evaluate ∫₀¹ (3x² + 2x) dx", "2", "1", "3", "5"),
        ("Evaluate ∫₁² 1/x dx", "ln 2", "ln 1", "1", "2"),
        ("Find ∫ (2x + 1)³ dx", "(2x+1)⁴/8 + C", "(2x+1)⁴/4 + C", "2(2x+1)⁴ + C", "(2x+1)⁴ + C"),
        ("Evaluate ∫₀^(π/2) cos x dx", "1", "0", "-1", "π/2"),
        ("If F'(x) = 3x², then F(x) = ", "x³ + C", "3x³ + C", "x² + C", "6x + C"),
        ("∫ e^(2x) dx = ", "e^(2x)/2 + C", "e^(2x) + C", "2e^(2x) + C", "e^(x) + C"),
        ("Area under y = x from 0 to 4 is", "8", "16", "4", "2"),
        ("∫ 3cos(x) dx = ", "3sin(x) + C", "-3sin(x) + C", "3cos(x) + C", "sin(3x) + C"),
        ("Evaluate ∫₀¹ e^x dx", "e - 1", "e", "1", "e + 1"),
        ("∫ (x + 1/x) dx = ", "x²/2 + ln|x| + C", "x²/2 - 1/x² + C", "x + ln|x| + C", "x²/2 + 1/x + C"),
    ]
    
    for _ in range(50):
        q, correct, d1, d2, d3 = random.choice(sec_questions)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Apply integration techniques. Answer: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    return questions

# ============================================================
# MAIN EXECUTION
# ============================================================
def main():
    """Generate all questions and output SQL"""
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
    
    # Output SQL
    sql_statements = []
    for q in all_questions:
        q_text = q['question_text'].replace("'", "''")
        opt_a = q['option_a'].replace("'", "''")
        opt_b = q['option_b'].replace("'", "''")
        opt_c = q['option_c'].replace("'", "''")
        opt_d = q['option_d'].replace("'", "''")
        expl = q['explanation'].replace("'", "''")
        
        sql = f"""INSERT INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('{q_text}', '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', {q['correct_idx']},
'{TOPIC}', {q['difficulty']}, '{q['difficulty_band']}', '{MODE}', '{expl}', 1);"""
        sql_statements.append(sql)
    
    sql_file = '/home/claude/lc_hl_calculus_int_questions.sql'
    with open(sql_file, 'w') as f:
        f.write(f"-- LC Higher Level - Calculus (Integration) Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    questions = main()
