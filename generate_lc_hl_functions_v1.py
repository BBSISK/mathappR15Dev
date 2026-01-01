#!/usr/bin/env python3
"""
LC Higher Level - Functions Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level x 12 levels) for LC HL Functions
"""

import random

TOPIC = 'lc_hl_functions'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Function Notation',
    'Domain & Range',
    'Composite Functions',
    'Inverse Functions',
    'Transformations - Translations',
    'Transformations - Reflections & Stretches',
    'Graphing Functions',
    'Exponential Functions',
    'Logarithmic Functions',
    'Rational Functions',
    'Piecewise Functions',
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
        unique_wrong.append(f"Option {len(unique_wrong) + 2}")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def superscript(n):
    """Convert integer to superscript string"""
    sup_map = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
               '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻'}
    return ''.join(sup_map.get(c, c) for c in str(n))

def generate_level_1():
    """Level 1: Function Notation - Basic evaluation and notation"""
    questions = []
    
    # Type 1: Evaluate f(x) = ax + b at a point (15 questions)
    for _ in range(15):
        a = random.randint(2, 9)
        b = random.randint(-10, 10)
        x = random.randint(1, 5)
        correct = a * x + b
        
        sign = '+' if b >= 0 else '-'
        b_abs = abs(b)
        
        distractors = [correct + a, correct - b, a * x, correct + 1]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f({x}) = {a}({x}) {sign} {b_abs} = {a*x} {sign} {b_abs} = {correct}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x {sign} {b_abs}, find f({x}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Evaluate f(x) = x² + c at a point (15 questions)
    for _ in range(15):
        c = random.randint(-5, 10)
        x = random.randint(1, 6)
        correct = x**2 + c
        
        sign = '+' if c >= 0 else '-'
        c_abs = abs(c)
        
        distractors = [x**2, 2*x + c, x + c, correct + x]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if c == 0:
            explanation = f"f({x}) = ({x})² = {correct}"
            q_text = f"If f(x) = x², find f({x})."
        else:
            explanation = f"f({x}) = ({x})² {sign} {c_abs} = {x**2} {sign} {c_abs} = {correct}"
            q_text = f"If f(x) = x² {sign} {c_abs}, find f({x})."
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Evaluate at x = 0 (10 questions)
    for _ in range(10):
        a = random.randint(2, 8)
        b = random.randint(1, 15)
        correct = b
        
        distractors = [a, a + b, 0, -b]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f(0) = {a}(0) + {b} = 0 + {b} = {b}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b}, find f(0).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Evaluate at negative values (10 questions)
    for _ in range(10):
        a = random.randint(2, 6)
        b = random.randint(1, 10)
        x = random.randint(-5, -1)
        correct = a * x + b
        
        distractors = [a * (-x) + b, -a * x + b, a * x - b, correct + 2*b]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f({x}) = {a}({x}) + {b} = {a*x} + {b} = {correct}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b}, find f({x}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_2():
    """Level 2: Domain & Range - Basic concepts"""
    questions = []
    
    # Type 1: Domain of linear functions (10 questions)
    for i in range(10):
        a = random.randint(2, 10)
        b = random.randint(-10, 10)
        sign = '+' if b >= 0 else '-'
        b_abs = abs(b)
        
        correct = "All real numbers (ℝ)"
        distractors = ["x > 0", "x ≥ 0", "x ≠ 0"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "A linear function f(x) = ax + b is defined for all real values of x, so the domain is all real numbers ℝ."
        
        questions.append({
            'question_text': f"What is the domain of f(x) = {a}x {sign} {b_abs}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Domain of square root functions (12 questions)
    for _ in range(12):
        a = random.randint(1, 8)
        
        correct = f"x ≥ {-a}" if a > 0 else "x ≥ 0"
        distractors = [f"x > {-a}", f"x ≤ {-a}", "All real numbers (ℝ)"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if a > 0:
            explanation = f"For √(x + {a}) to be defined, we need x + {a} ≥ 0, so x ≥ {-a}."
            q_text = f"What is the domain of f(x) = √(x + {a})?"
        else:
            explanation = "For √x to be defined, we need x ≥ 0."
            q_text = "What is the domain of f(x) = √x?"
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Domain of 1/x type functions (10 questions)
    for _ in range(10):
        a = random.randint(1, 6)
        
        correct = f"x ≠ {a}"
        distractors = [f"x > {a}", f"x ≥ {a}", "All real numbers (ℝ)"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"For 1/(x - {a}) to be defined, we need x - {a} ≠ 0, so x ≠ {a}."
        
        questions.append({
            'question_text': f"What is the domain of f(x) = 1/(x - {a})?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Range of quadratic functions (10 questions)
    for _ in range(10):
        k = random.randint(-5, 5)
        
        correct = f"y ≥ {k}"
        distractors = [f"y > {k}", f"y ≤ {k}", "All real numbers (ℝ)"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if k == 0:
            explanation = "For f(x) = x², the minimum value is 0 (at x = 0), so the range is y ≥ 0."
            q_text = "What is the range of f(x) = x²?"
        elif k > 0:
            explanation = f"For f(x) = x² + {k}, the minimum value is {k} (at x = 0), so the range is y ≥ {k}."
            q_text = f"What is the range of f(x) = x² + {k}?"
        else:
            explanation = f"For f(x) = x² - {abs(k)}, the minimum value is {k} (at x = 0), so the range is y ≥ {k}."
            q_text = f"What is the range of f(x) = x² - {abs(k)}?"
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Range of linear functions (8 questions)
    for _ in range(8):
        a = random.randint(2, 8)
        b = random.randint(-5, 5)
        sign = '+' if b >= 0 else '-'
        
        correct = "All real numbers (ℝ)"
        distractors = ["y > 0", "y ≥ 0", f"y ≥ {b}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "A linear function f(x) = ax + b (where a ≠ 0) can produce any real output value, so the range is all real numbers ℝ."
        
        questions.append({
            'question_text': f"What is the range of f(x) = {a}x {sign} {abs(b)}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_3():
    """Level 3: Composite Functions - Basic composition"""
    questions = []
    
    # Type 1: f(g(x)) with linear functions (15 questions)
    for _ in range(15):
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        c = random.randint(2, 4)
        d = random.randint(1, 5)
        
        # f(x) = ax + b, g(x) = cx + d
        # f(g(x)) = a(cx + d) + b = acx + ad + b
        coef = a * c
        const = a * d + b
        
        sign = '+' if const >= 0 else '-'
        correct = f"{coef}x {sign} {abs(const)}"
        
        distractors = [
            f"{a + c}x + {b + d}",  # Adding instead of composing
            f"{c}x + {a*d}",  # Partial composition
            f"{a*c}x + {b}"  # Missing term
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f(g(x)) = f({c}x + {d}) = {a}({c}x + {d}) + {b} = {coef}x + {a*d} + {b} = {coef}x {sign} {abs(const)}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b} and g(x) = {c}x + {d}, find f(g(x)).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: g(f(x)) with linear functions (15 questions)
    for _ in range(15):
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        c = random.randint(2, 4)
        d = random.randint(1, 5)
        
        # f(x) = ax + b, g(x) = cx + d
        # g(f(x)) = c(ax + b) + d = acx + bc + d
        coef = a * c
        const = b * c + d
        
        sign = '+' if const >= 0 else '-'
        correct = f"{coef}x {sign} {abs(const)}"
        
        distractors = [
            f"{a + c}x + {b + d}",
            f"{a}x + {c*b}",
            f"{a*c}x + {d}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"g(f(x)) = g({a}x + {b}) = {c}({a}x + {b}) + {d} = {coef}x + {b*c} + {d} = {coef}x {sign} {abs(const)}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b} and g(x) = {c}x + {d}, find g(f(x)).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Evaluate f(g(a)) at a specific value (10 questions)
    for _ in range(10):
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        c = random.randint(2, 3)
        d = random.randint(1, 4)
        x_val = random.randint(1, 3)
        
        g_val = c * x_val + d
        correct = a * g_val + b
        
        distractors = [
            a * x_val + b + c * x_val + d,
            c * (a * x_val + b) + d,
            a * x_val + c * x_val
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"First find g({x_val}) = {c}({x_val}) + {d} = {g_val}. Then f(g({x_val})) = f({g_val}) = {a}({g_val}) + {b} = {correct}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b} and g(x) = {c}x + {d}, find f(g({x_val})).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 4: f(f(x)) - self composition (10 questions)
    for _ in range(10):
        a = random.randint(2, 3)
        b = random.randint(1, 4)
        
        # f(f(x)) = a(ax + b) + b = a²x + ab + b
        coef = a * a
        const = a * b + b
        
        correct = f"{coef}x + {const}"
        
        distractors = [
            f"{2*a}x + {2*b}",
            f"{a*a}x + {b}",
            f"{a}x + {2*b}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f(f(x)) = f({a}x + {b}) = {a}({a}x + {b}) + {b} = {coef}x + {a*b} + {b} = {coef}x + {const}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b}, find f(f(x)).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_4():
    """Level 4: Inverse Functions - Finding and verifying inverses"""
    questions = []
    
    # Type 1: Find inverse of linear function (15 questions)
    for _ in range(15):
        a = random.randint(2, 6)
        b = random.randint(1, 10)
        
        # f(x) = ax + b, inverse: f⁻¹(x) = (x - b)/a
        correct = f"(x - {b})/{a}"
        
        distractors = [
            f"(x + {b})/{a}",
            f"{a}x - {b}",
            f"x/{a} + {b}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Let y = {a}x + {b}. Swap x and y: x = {a}y + {b}. Solve for y: {a}y = x - {b}, so y = (x - {b})/{a}. Therefore f⁻¹(x) = (x - {b})/{a}."
        
        questions.append({
            'question_text': f"Find the inverse function f⁻¹(x) if f(x) = {a}x + {b}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Find inverse of f(x) = (x - a)/b (10 questions)
    for _ in range(10):
        a = random.randint(1, 8)
        b = random.randint(2, 5)
        
        # f(x) = (x - a)/b, inverse: f⁻¹(x) = bx + a
        correct = f"{b}x + {a}"
        
        distractors = [
            f"{b}x - {a}",
            f"x/{b} + {a}",
            f"(x + {a})/{b}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Let y = (x - {a})/{b}. Swap x and y: x = (y - {a})/{b}. Solve for y: {b}x = y - {a}, so y = {b}x + {a}. Therefore f⁻¹(x) = {b}x + {a}."
        
        questions.append({
            'question_text': f"Find the inverse function f⁻¹(x) if f(x) = (x - {a})/{b}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Evaluate f⁻¹ at a point (15 questions)
    for _ in range(15):
        a = random.randint(2, 5)
        b = random.randint(1, 8)
        y_val = a * random.randint(1, 4) + b  # Ensure nice answer
        
        # f(x) = ax + b, f⁻¹(y) = (y - b)/a
        correct = (y_val - b) // a
        
        distractors = [
            correct + a,
            y_val // a,
            correct - 1
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f⁻¹(x) = (x - {b})/{a}. So f⁻¹({y_val}) = ({y_val} - {b})/{a} = {y_val - b}/{a} = {correct}."
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b}, find f⁻¹({y_val}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 4: Verify inverse relationship (10 questions)
    for _ in range(10):
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        x_val = random.randint(1, 5)
        
        f_val = a * x_val + b
        correct = x_val
        
        distractors = [f_val, a * x_val, x_val + b]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"First, f({x_val}) = {a}({x_val}) + {b} = {f_val}. Then f⁻¹({f_val}) = ({f_val} - {b})/{a} = {f_val - b}/{a} = {correct}. This verifies f⁻¹(f(x)) = x."
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b}, find f⁻¹(f({x_val})).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_5():
    """Level 5: Transformations - Translations"""
    questions = []
    
    # Type 1: Horizontal translation identification (12 questions)
    for _ in range(12):
        h = random.randint(1, 8)
        direction = random.choice(['left', 'right'])
        
        if direction == 'right':
            correct = f"f(x - {h})"
            explanation = f"A horizontal translation {h} units to the right is given by f(x - {h})."
        else:
            correct = f"f(x + {h})"
            explanation = f"A horizontal translation {h} units to the left is given by f(x + {h})."
        
        distractors = [
            f"f(x) + {h}",
            f"f(x) - {h}",
            f"f(x {'+ ' + str(h) if direction == 'right' else '- ' + str(h)})"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"The graph of y = f(x) is translated {h} units to the {direction}. What is the equation of the new graph?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Vertical translation identification (12 questions)
    for _ in range(12):
        k = random.randint(1, 8)
        direction = random.choice(['up', 'down'])
        
        if direction == 'up':
            correct = f"f(x) + {k}"
            explanation = f"A vertical translation {k} units up is given by f(x) + {k}."
        else:
            correct = f"f(x) - {k}"
            explanation = f"A vertical translation {k} units down is given by f(x) - {k}."
        
        distractors = [
            f"f(x + {k})",
            f"f(x - {k})",
            f"f(x) {'- ' + str(k) if direction == 'up' else '+ ' + str(k)}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"The graph of y = f(x) is translated {k} units {direction}. What is the equation of the new graph?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Combined translations (13 questions)
    for _ in range(13):
        h = random.randint(1, 5)
        k = random.randint(1, 5)
        h_dir = random.choice(['left', 'right'])
        k_dir = random.choice(['up', 'down'])
        
        h_term = f"x + {h}" if h_dir == 'left' else f"x - {h}"
        k_term = f"+ {k}" if k_dir == 'up' else f"- {k}"
        
        correct = f"f({h_term}) {k_term}"
        
        # Create plausible wrong answers
        wrong_h = f"x - {h}" if h_dir == 'left' else f"x + {h}"
        wrong_k = f"- {k}" if k_dir == 'up' else f"+ {k}"
        
        distractors = [
            f"f({wrong_h}) {k_term}",
            f"f({h_term}) {wrong_k}",
            f"f({wrong_h}) {wrong_k}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Moving {h} units {h_dir} uses f({h_term}). Moving {k} units {k_dir} adds {k_term}. Combined: f({h_term}) {k_term}."
        
        questions.append({
            'question_text': f"The graph of y = f(x) is translated {h} units {h_dir} and {k} units {k_dir}. What is the equation of the new graph?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 4: Identify translation from equation (13 questions)
    for _ in range(13):
        h = random.randint(1, 6)
        k = random.randint(1, 6)
        h_sign = random.choice(['+', '-'])
        k_sign = random.choice(['+', '-'])
        
        h_dir = "left" if h_sign == '+' else "right"
        k_dir = "up" if k_sign == '+' else "down"
        
        correct = f"{h} units {h_dir} and {k} units {k_dir}"
        
        opposite_h = "right" if h_dir == "left" else "left"
        opposite_k = "down" if k_dir == "up" else "up"
        
        distractors = [
            f"{h} units {opposite_h} and {k} units {k_dir}",
            f"{h} units {h_dir} and {k} units {opposite_k}",
            f"{h} units {opposite_h} and {k} units {opposite_k}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"In f(x {h_sign} {h}) {k_sign} {k}: the term (x {h_sign} {h}) means {h} units {h_dir}, and {k_sign} {k} means {k} units {k_dir}."
        
        questions.append({
            'question_text': f"Describe the translation that maps y = f(x) to y = f(x {h_sign} {h}) {k_sign} {k}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_6():
    """Level 6: Transformations - Reflections & Stretches"""
    questions = []
    
    # Type 1: Reflection in x-axis (10 questions)
    for i in range(10):
        funcs = ['x²', '2x + 1', 'x³', '√x', '1/x', 'sin(x)', 'cos(x)', '|x|', 'eˣ', 'ln(x)']
        func = funcs[i % len(funcs)]
        
        correct = f"-f(x) or -{func}"
        
        distractors = [
            f"f(-x)",
            f"f(x) - 1",
            f"1/f(x)"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "Reflection in the x-axis multiplies all y-values by -1, giving -f(x)."
        
        questions.append({
            'question_text': f"If y = f(x) = {func}, what is the equation after reflecting in the x-axis?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Reflection in y-axis (10 questions)
    for i in range(10):
        funcs = ['x²', '2x + 1', 'x³', '√x', 'eˣ', 'ln(x)', 'x² + x', '2x', 'x³ - x', '3x + 2']
        func = funcs[i % len(funcs)]
        
        correct = "f(-x)"
        
        distractors = [
            "-f(x)",
            "f(x) reflected",
            "-f(-x)"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "Reflection in the y-axis replaces x with -x, giving f(-x)."
        
        questions.append({
            'question_text': f"If y = f(x) = {func}, what is the equation after reflecting in the y-axis?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Vertical stretch (10 questions)
    for _ in range(10):
        a = random.randint(2, 5)
        
        correct = f"{a}f(x)"
        
        distractors = [
            f"f({a}x)",
            f"f(x) + {a}",
            f"f(x/{a})"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"A vertical stretch by scale factor {a} multiplies all y-values by {a}, giving {a}f(x)."
        
        questions.append({
            'question_text': f"What is the equation when y = f(x) is stretched vertically by scale factor {a}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 4: Horizontal stretch (10 questions)
    for _ in range(10):
        a = random.randint(2, 4)
        
        correct = f"f(x/{a})"
        
        distractors = [
            f"{a}f(x)",
            f"f({a}x)",
            f"f(x) × {a}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"A horizontal stretch by scale factor {a} replaces x with x/{a}, giving f(x/{a})."
        
        questions.append({
            'question_text': f"What is the equation when y = f(x) is stretched horizontally by scale factor {a}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 5: Horizontal compression (10 questions)
    for _ in range(10):
        a = random.randint(2, 4)
        
        correct = f"f({a}x)"
        
        distractors = [
            f"f(x/{a})",
            f"{a}f(x)",
            f"f(x)/{a}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"A horizontal compression by scale factor 1/{a} (or stretch by factor {a} towards y-axis) replaces x with {a}x, giving f({a}x)."
        
        questions.append({
            'question_text': f"What is the equation when y = f(x) is compressed horizontally by scale factor 1/{a}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_7():
    """Level 7: Graphing Functions - Key features"""
    questions = []
    
    # Type 1: Finding y-intercept (10 questions)
    for _ in range(10):
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-8, 8)
        
        # f(x) = ax² + bx + c, y-intercept is c
        correct = f"(0, {c})"
        
        distractors = [
            f"({c}, 0)",
            f"(0, {a})",
            f"(0, {b})"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        b_sign = '+' if b >= 0 else '-'
        c_sign = '+' if c >= 0 else '-'
        
        explanation = f"The y-intercept is found by setting x = 0: f(0) = {a}(0)² {b_sign} {abs(b)}(0) {c_sign} {abs(c)} = {c}. Point: (0, {c})."
        
        questions.append({
            'question_text': f"Find the y-intercept of f(x) = {a}x² {b_sign} {abs(b)}x {c_sign} {abs(c)}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Finding x-intercepts of factored quadratic (10 questions)
    for _ in range(10):
        r1 = random.randint(-5, 5)
        r2 = random.randint(-5, 5)
        while r2 == r1:
            r2 = random.randint(-5, 5)
        
        # Sort roots for consistent display
        if r1 > r2:
            r1, r2 = r2, r1
        
        s1 = '+' if -r1 >= 0 else '-'
        s2 = '+' if -r2 >= 0 else '-'
        
        correct = f"x = {r1} and x = {r2}"
        
        distractors = [
            f"x = {-r1} and x = {-r2}",
            f"x = {r1} only",
            f"x = {r1 + r2} and x = {r1 * r2}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Setting f(x) = 0: (x {s1} {abs(r1)})(x {s2} {abs(r2)}) = 0. So x = {r1} or x = {r2}."
        
        q_text = f"Find the x-intercepts of f(x) = (x {s1} {abs(r1)})(x {s2} {abs(r2)})."
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Vertex of parabola (12 questions)
    for _ in range(12):
        h = random.randint(-5, 5)
        k = random.randint(-8, 8)
        a = random.choice([1, 2, -1, -2])
        
        correct = f"({h}, {k})"
        
        distractors = [
            f"({-h}, {k})",
            f"({h}, {-k})",
            f"({k}, {h})"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        h_sign = '-' if h >= 0 else '+'
        k_sign = '+' if k >= 0 else '-'
        
        a_str = '' if a == 1 else ('-' if a == -1 else str(a))
        
        explanation = f"In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = {h} and k = {k}, so vertex is ({h}, {k})."
        
        questions.append({
            'question_text': f"Find the vertex of f(x) = {a_str}(x {h_sign} {abs(h)})² {k_sign} {abs(k)}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Identify function type from description (10 questions)
    function_types = [
        ("passes through the origin and is symmetric about the y-axis", "y = x²", "Even polynomial (parabola)"),
        ("passes through the origin and is symmetric about the origin", "y = x³", "Odd polynomial (cubic)"),
        ("has a horizontal asymptote at y = 0 and passes through (0, 1)", "y = aˣ (a > 1)", "Exponential function"),
        ("has a vertical asymptote at x = 0 and passes through (1, 0)", "y = ln(x)", "Logarithmic function"),
        ("has vertical asymptote at x = 0 and horizontal asymptote at y = 0", "y = 1/x", "Reciprocal function"),
        ("is always positive and has minimum at x = 0", "y = x²", "Quadratic (parabola)"),
        ("has period 2π and range [-1, 1]", "y = sin(x) or y = cos(x)", "Trigonometric function"),
        ("approaches but never touches the x-axis as x → ∞", "y = aˣ (0 < a < 1)", "Exponential decay"),
        ("has a V-shape with vertex at the origin", "y = |x|", "Absolute value function"),
        ("is always increasing and passes through (0, 1)", "y = eˣ", "Natural exponential function"),
    ]
    
    for desc, answer, func_type in function_types:
        correct = answer
        
        all_answers = [ft[1] for ft in function_types]
        distractors = [a for a in all_answers if a != answer][:3]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"The description matches a {func_type}: {answer}."
        
        questions.append({
            'question_text': f"Which function {desc}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 5: Axis of symmetry (8 questions)
    for _ in range(8):
        a = random.choice([1, 2, -1, -2])
        b = random.randint(-8, 8)
        c = random.randint(-5, 5)
        
        # Axis of symmetry: x = -b/(2a)
        axis = -b / (2 * a)
        
        if axis == int(axis):
            correct = f"x = {int(axis)}"
        else:
            # Express as fraction
            from fractions import Fraction
            frac = Fraction(-b, 2*a)
            correct = f"x = {frac.numerator}/{frac.denominator}" if frac.denominator != 1 else f"x = {frac.numerator}"
        
        distractors = [
            f"x = {b}",
            f"x = {-b}",
            f"x = {c}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        b_sign = '+' if b >= 0 else '-'
        c_sign = '+' if c >= 0 else '-'
        a_str = '' if a == 1 else ('-' if a == -1 else str(a))
        
        explanation = f"For f(x) = ax² + bx + c, the axis of symmetry is x = -b/(2a) = {-b}/(2×{a}) = {-b}/{2*a}."
        
        questions.append({
            'question_text': f"Find the axis of symmetry of f(x) = {a_str}x² {b_sign} {abs(b)}x {c_sign} {abs(c)}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_8():
    """Level 8: Exponential Functions"""
    questions = []
    
    # Type 1: Evaluate exponential functions (12 questions)
    for _ in range(12):
        base = random.choice([2, 3, 5, 10])
        exp = random.randint(0, 4)
        
        correct = base ** exp
        
        distractors = [
            base * exp,
            base ** (exp + 1),
            base ** (exp - 1) if exp > 0 else base
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f({exp}) = {base}{superscript(exp)} = {correct}"
        
        questions.append({
            'question_text': f"If f(x) = {base}ˣ, find f({exp}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Identify growth vs decay (10 questions)
    for _ in range(10):
        base_type = random.choice(['growth', 'decay'])
        
        if base_type == 'growth':
            base = random.choice([2, 3, 5, 'e', 10])
            base_str = str(base) if base != 'e' else 'e'
            correct = "Exponential growth"
            explanation = f"Since the base {base_str} > 1, the function represents exponential growth."
        else:
            num = random.randint(1, 4)
            denom = random.randint(num + 1, 9)
            base_str = f"({num}/{denom})"
            correct = "Exponential decay"
            explanation = f"Since the base {num}/{denom} is between 0 and 1, the function represents exponential decay."
        
        distractors = [
            "Exponential decay" if base_type == 'growth' else "Exponential growth",
            "Linear growth",
            "Polynomial growth"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Classify the function f(x) = {base_str}ˣ.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Properties of exponential functions (10 questions)
    properties = [
        ("What is the y-intercept of f(x) = 3ˣ?", "(0, 1)", "For any f(x) = aˣ where a > 0, f(0) = a⁰ = 1. Y-intercept is (0, 1)."),
        ("What is the y-intercept of f(x) = 5ˣ?", "(0, 1)", "For any f(x) = aˣ where a > 0, f(0) = a⁰ = 1. Y-intercept is (0, 1)."),
        ("What is the horizontal asymptote of f(x) = 2ˣ?", "y = 0", "As x → -∞, 2ˣ → 0. The horizontal asymptote is y = 0."),
        ("What is the horizontal asymptote of f(x) = eˣ?", "y = 0", "As x → -∞, eˣ → 0. The horizontal asymptote is y = 0."),
        ("What is the domain of f(x) = 4ˣ?", "All real numbers (ℝ)", "Exponential functions are defined for all real x values."),
        ("What is the range of f(x) = 2ˣ?", "y > 0", "Exponential functions with base > 0 always give positive outputs."),
        ("Is f(x) = 3ˣ increasing or decreasing?", "Always increasing", "When base > 1, the exponential function is always increasing."),
        ("Is f(x) = (1/2)ˣ increasing or decreasing?", "Always decreasing", "When 0 < base < 1, the exponential function is always decreasing."),
        ("What is the y-intercept of f(x) = 2 × 3ˣ?", "(0, 2)", "f(0) = 2 × 3⁰ = 2 × 1 = 2. Y-intercept is (0, 2)."),
        ("What is the horizontal asymptote of f(x) = 2ˣ + 3?", "y = 3", "The +3 shifts the asymptote up from y = 0 to y = 3."),
    ]
    
    for q, a, expl in properties:
        correct = a
        
        if "y-intercept" in q:
            distractors = ["(1, 0)", "(0, 0)", "(0, -1)"]
        elif "asymptote" in q:
            distractors = ["y = 1", "y = -1", "x = 0"]
        elif "domain" in q:
            distractors = ["x > 0", "x ≥ 0", "x ≠ 0"]
        elif "range" in q:
            distractors = ["All real numbers", "y ≥ 0", "y ≥ 1"]
        else:
            distractors = ["Always decreasing", "Neither", "Increasing then decreasing"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Solve simple exponential equations (10 questions)
    for _ in range(10):
        base = random.choice([2, 3, 4, 5])
        exp = random.randint(1, 5)
        result = base ** exp
        
        correct = str(exp)
        
        distractors = [
            str(exp + 1),
            str(exp - 1) if exp > 1 else str(exp + 2),
            str(result // base)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"We need {base}ˣ = {result}. Since {base}{superscript(exp)} = {result}, x = {exp}."
        
        questions.append({
            'question_text': f"Solve for x: {base}ˣ = {result}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 5: Transformations of exponential functions (8 questions)
    for _ in range(8):
        h = random.randint(1, 4)
        k = random.randint(1, 4)
        base = random.choice([2, 3, 'e'])
        base_str = str(base) if base != 'e' else 'e'
        
        h_dir = random.choice(['left', 'right'])
        k_dir = random.choice(['up', 'down'])
        
        if h_dir == 'right':
            h_term = f"x - {h}"
        else:
            h_term = f"x + {h}"
        
        if k_dir == 'up':
            k_term = f"+ {k}"
            asymptote = k
        else:
            k_term = f"- {k}"
            asymptote = -k
        
        correct = f"y = {asymptote}"
        
        distractors = [
            f"y = {-asymptote}",
            f"y = 0",
            f"x = {h if h_dir == 'right' else -h}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"The transformation {k_term} shifts the horizontal asymptote from y = 0 to y = {asymptote}."
        
        questions.append({
            'question_text': f"What is the horizontal asymptote of f(x) = {base_str}⁽{h_term}⁾ {k_term}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_9():
    """Level 9: Logarithmic Functions"""
    questions = []
    
    # Type 1: Evaluate basic logarithms (12 questions)
    log_problems = [
        (2, 8, 3), (2, 16, 4), (2, 32, 5), (2, 4, 2),
        (3, 9, 2), (3, 27, 3), (3, 81, 4),
        (10, 100, 2), (10, 1000, 3), (10, 10000, 4),
        (5, 25, 2), (5, 125, 3)
    ]
    
    for base, arg, result in log_problems:
        correct = str(result)
        
        distractors = [
            str(result + 1),
            str(result - 1) if result > 1 else "0",
            str(arg // base)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if base == 10:
            explanation = f"log({arg}) = {result} because 10{superscript(result)} = {arg}."
            q_text = f"Evaluate log({arg})."
        else:
            explanation = f"log{base}({arg}) = {result} because {base}{superscript(result)} = {arg}."
            q_text = f"Evaluate log{base}({arg})."
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Properties of logarithmic functions (10 questions)
    log_props = [
        ("What is the domain of f(x) = ln(x)?", "x > 0", "Logarithms are only defined for positive arguments."),
        ("What is the domain of f(x) = log(x)?", "x > 0", "Logarithms are only defined for positive arguments."),
        ("What is the range of f(x) = ln(x)?", "All real numbers (ℝ)", "Logarithmic functions can output any real number."),
        ("What is the x-intercept of f(x) = ln(x)?", "(1, 0)", "ln(1) = 0, so the x-intercept is (1, 0)."),
        ("What is the x-intercept of f(x) = log(x)?", "(1, 0)", "log(1) = 0, so the x-intercept is (1, 0)."),
        ("What is the vertical asymptote of f(x) = ln(x)?", "x = 0", "As x → 0⁺, ln(x) → -∞. The vertical asymptote is x = 0."),
        ("Is f(x) = ln(x) increasing or decreasing for x > 0?", "Always increasing", "The natural logarithm is always increasing on its domain."),
        ("What is ln(e)?", "1", "By definition, ln(e) = 1 since e¹ = e."),
        ("What is log(10)?", "1", "By definition, log(10) = 1 since 10¹ = 10."),
        ("What is ln(1)?", "0", "ln(1) = 0 because e⁰ = 1."),
    ]
    
    for q, a, expl in log_props:
        correct = a
        
        if "domain" in q:
            distractors = ["All real numbers", "x ≥ 0", "x ≠ 0"]
        elif "range" in q:
            distractors = ["y > 0", "y ≥ 0", "y ≠ 0"]
        elif "intercept" in q:
            distractors = ["(0, 1)", "(e, 0)", "(0, 0)"]
        elif "asymptote" in q:
            distractors = ["y = 0", "x = 1", "y = 1"]
        elif "increasing" in q:
            distractors = ["Always decreasing", "Neither", "Sometimes increasing"]
        else:
            distractors = ["0", "e", "-1"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Logarithm laws (15 questions)
    log_laws = [
        ("Simplify log(a) + log(b)", "log(ab)", "Product rule: log(a) + log(b) = log(ab)"),
        ("Simplify log(a) - log(b)", "log(a/b)", "Quotient rule: log(a) - log(b) = log(a/b)"),
        ("Simplify 2log(a)", "log(a²)", "Power rule: nlog(a) = log(aⁿ)"),
        ("Simplify 3log(x)", "log(x³)", "Power rule: nlog(a) = log(aⁿ)"),
        ("Simplify log(x) + log(y) + log(z)", "log(xyz)", "Product rule extended: log(xyz)"),
        ("Simplify log(100) + log(10)", "log(1000) or 3", "log(100 × 10) = log(1000) = 3"),
        ("Simplify ln(e²)", "2", "ln(e²) = 2ln(e) = 2 × 1 = 2"),
        ("Simplify ln(e³)", "3", "ln(e³) = 3ln(e) = 3 × 1 = 3"),
        ("Simplify log₂(4) + log₂(8)", "5", "log₂(4 × 8) = log₂(32) = 5"),
        ("Simplify log₃(27) - log₃(9)", "1", "log₃(27/9) = log₃(3) = 1"),
        ("Express log(x²y) in terms of log(x) and log(y)", "2log(x) + log(y)", "log(x²y) = log(x²) + log(y) = 2log(x) + log(y)"),
        ("Express log(x/y²) in terms of log(x) and log(y)", "log(x) - 2log(y)", "log(x/y²) = log(x) - log(y²) = log(x) - 2log(y)"),
        ("Simplify log(1/x)", "-log(x)", "log(1/x) = log(1) - log(x) = 0 - log(x) = -log(x)"),
        ("Simplify ln(√x)", "½ln(x)", "ln(√x) = ln(x^½) = ½ln(x)"),
        ("Simplify log₂(2⁵)", "5", "log₂(2⁵) = 5log₂(2) = 5 × 1 = 5"),
    ]
    
    for q, a, expl in log_laws:
        correct = a
        
        # Generate plausible distractors based on question type
        if "+" in q and "log" in a:
            distractors = [a.replace("ab", "a+b"), a.replace("ab", "a-b"), "log(a) × log(b)"]
        elif "-" in q and "/" in a:
            distractors = [a.replace("/", "×"), a.replace("/", "-"), "log(a)/log(b)"]
        elif "2log" in q or "3log" in q:
            distractors = ["log(2a)", "log(a)/2", "2 × log(a)"]
        else:
            distractors = ["log(x + y)", "log(x) × log(y)", "log(x)/log(y)"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Domain of transformed logarithms (13 questions)
    for _ in range(13):
        a = random.randint(1, 6)
        sign = random.choice(['+', '-'])
        
        if sign == '+':
            correct = f"x > {-a}"
            explanation = f"For ln(x + {a}) to be defined, we need x + {a} > 0, so x > {-a}."
            q_text = f"What is the domain of f(x) = ln(x + {a})?"
        else:
            correct = f"x > {a}"
            explanation = f"For ln(x - {a}) to be defined, we need x - {a} > 0, so x > {a}."
            q_text = f"What is the domain of f(x) = ln(x - {a})?"
        
        distractors = [
            f"x ≥ {a if sign == '-' else -a}",
            "x > 0",
            "All real numbers"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_10():
    """Level 10: Rational Functions"""
    questions = []
    
    # Type 1: Vertical asymptotes (12 questions)
    for _ in range(12):
        a = random.randint(1, 8)
        sign = random.choice(['+', '-'])
        
        if sign == '+':
            asymptote = -a
            q_text = f"Find the vertical asymptote of f(x) = 1/(x + {a})."
        else:
            asymptote = a
            q_text = f"Find the vertical asymptote of f(x) = 1/(x - {a})."
        
        correct = f"x = {asymptote}"
        
        distractors = [
            f"x = {-asymptote}",
            f"y = {asymptote}",
            "x = 0"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"The vertical asymptote occurs where the denominator equals zero: x {sign} {a} = 0, so x = {asymptote}."
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Horizontal asymptotes (12 questions)
    h_asymptote_qs = [
        ("f(x) = 1/x", "y = 0", "When degree of numerator < degree of denominator, HA is y = 0."),
        ("f(x) = 3/(x + 2)", "y = 0", "When degree of numerator < degree of denominator, HA is y = 0."),
        ("f(x) = (2x + 1)/(x - 3)", "y = 2", "When degrees are equal, HA is y = (leading coef of num)/(leading coef of denom) = 2/1 = 2."),
        ("f(x) = (3x - 1)/(x + 5)", "y = 3", "When degrees are equal, HA is y = 3/1 = 3."),
        ("f(x) = (x + 2)/(2x - 1)", "y = 1/2", "When degrees are equal, HA is y = 1/2."),
        ("f(x) = (4x + 3)/(2x - 7)", "y = 2", "When degrees are equal, HA is y = 4/2 = 2."),
        ("f(x) = 5/(x² + 1)", "y = 0", "When degree of numerator < degree of denominator, HA is y = 0."),
        ("f(x) = (x² + 1)/(x² - 4)", "y = 1", "When degrees are equal, HA is y = 1/1 = 1."),
        ("f(x) = (3x² - 2)/(x² + x)", "y = 3", "When degrees are equal, HA is y = 3/1 = 3."),
        ("f(x) = 2x/(x + 1)", "y = 2", "When degrees are equal, HA is y = 2/1 = 2."),
        ("f(x) = (x - 1)/(3x + 2)", "y = 1/3", "When degrees are equal, HA is y = 1/3."),
        ("f(x) = 7/(2x - 5)", "y = 0", "When degree of numerator < degree of denominator, HA is y = 0."),
    ]
    
    for q, a, expl in h_asymptote_qs:
        correct = a
        
        distractors = ["y = 1", "y = -1", "No horizontal asymptote"]
        if a == "y = 0":
            distractors = ["y = 1", "y = 2", "No horizontal asymptote"]
        elif a == "y = 1":
            distractors = ["y = 0", "y = 2", "y = -1"]
        elif a == "y = 2":
            distractors = ["y = 0", "y = 1", "y = 4"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the horizontal asymptote of {q[5:]}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Domain of rational functions (13 questions)
    for _ in range(13):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        while r2 == r1:
            r2 = random.randint(1, 6)
        
        s1 = random.choice(['+', '-'])
        s2 = random.choice(['+', '-'])
        
        excl1 = -r1 if s1 == '+' else r1
        excl2 = -r2 if s2 == '+' else r2
        
        correct = f"x ≠ {excl1} and x ≠ {excl2}"
        
        distractors = [
            f"x ≠ {excl1}",
            f"x ≠ {excl2}",
            "All real numbers"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"The denominator (x {s1} {r1})(x {s2} {r2}) = 0 when x = {excl1} or x = {excl2}. Domain excludes these values."
        
        questions.append({
            'question_text': f"What is the domain of f(x) = x/[(x {s1} {r1})(x {s2} {r2})]?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Finding x-intercepts (13 questions)
    for _ in range(13):
        r = random.randint(-5, 5)
        a = random.randint(1, 5)
        
        s = '+' if -r >= 0 else '-'
        
        correct = f"x = {r}"
        
        distractors = [
            f"x = {-r}",
            f"x = {a}",
            "No x-intercept"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"X-intercepts occur when numerator = 0: x {s} {abs(r)} = 0, so x = {r}."
        
        questions.append({
            'question_text': f"Find the x-intercept of f(x) = (x {s} {abs(r)})/(x + {a}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_11():
    """Level 11: Piecewise Functions"""
    questions = []
    
    # Type 1: Evaluate piecewise functions (15 questions)
    for _ in range(15):
        boundary = random.randint(-3, 3)
        a1 = random.randint(1, 4)
        b1 = random.randint(-5, 5)
        a2 = random.randint(1, 4)
        b2 = random.randint(-5, 5)
        
        # Choose evaluation point
        region = random.choice(['left', 'right', 'boundary'])
        if region == 'left':
            x = boundary - random.randint(1, 4)
            correct = a1 * x + b1
            formula = f"{a1}x + {b1}" if b1 >= 0 else f"{a1}x - {abs(b1)}"
            explanation = f"Since {x} < {boundary}, we use f(x) = {formula}. f({x}) = {a1}({x}) {'+' if b1 >= 0 else '-'} {abs(b1)} = {correct}"
        elif region == 'right':
            x = boundary + random.randint(1, 4)
            correct = a2 * x + b2
            formula = f"{a2}x + {b2}" if b2 >= 0 else f"{a2}x - {abs(b2)}"
            explanation = f"Since {x} ≥ {boundary}, we use f(x) = {formula}. f({x}) = {a2}({x}) {'+' if b2 >= 0 else '-'} {abs(b2)} = {correct}"
        else:
            x = boundary
            correct = a2 * x + b2  # ≥ includes boundary
            formula = f"{a2}x + {b2}" if b2 >= 0 else f"{a2}x - {abs(b2)}"
            explanation = f"Since {x} = {boundary} (≥ {boundary}), we use f(x) = {formula}. f({x}) = {a2}({x}) {'+' if b2 >= 0 else '-'} {abs(b2)} = {correct}"
        
        distractors = [
            correct + a1,
            correct - b1,
            a1 * x + b1 if region != 'left' else a2 * x + b2
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        s1 = '+' if b1 >= 0 else '-'
        s2 = '+' if b2 >= 0 else '-'
        
        questions.append({
            'question_text': f"If f(x) = {{{a1}x {s1} {abs(b1)} if x < {boundary}, {a2}x {s2} {abs(b2)} if x ≥ {boundary}}}, find f({x}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Continuity of piecewise functions (12 questions)
    for _ in range(12):
        boundary = random.randint(-2, 2)
        a1 = random.randint(1, 3)
        a2 = random.randint(1, 3)
        
        # Make it continuous at boundary: a1*boundary + b1 = a2*boundary + b2
        # Choose b1, calculate b2 for continuity, then randomly decide if continuous
        b1 = random.randint(-3, 3)
        
        if random.choice([True, False]):
            # Make continuous
            b2 = a1 * boundary + b1 - a2 * boundary
            correct = "Yes, it is continuous"
            left_val = a1 * boundary + b1
            right_val = a2 * boundary + b2
            explanation = f"At x = {boundary}: left limit = {a1}({boundary}) + {b1} = {left_val}, right limit = {a2}({boundary}) + {b2} = {right_val}. Since they're equal, f is continuous."
        else:
            # Make discontinuous
            b2 = a1 * boundary + b1 - a2 * boundary + random.choice([-2, -1, 1, 2])
            correct = "No, it is discontinuous"
            left_val = a1 * boundary + b1
            right_val = a2 * boundary + b2
            explanation = f"At x = {boundary}: left limit = {a1}({boundary}) + {b1} = {left_val}, right limit = {a2}({boundary}) + {b2} = {right_val}. Since {left_val} ≠ {right_val}, f is discontinuous."
        
        distractors = [
            "No, it is discontinuous" if "Yes" in correct else "Yes, it is continuous",
            "Cannot be determined",
            "Only continuous from the left"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        s1 = '+' if b1 >= 0 else '-'
        s2 = '+' if b2 >= 0 else '-'
        
        questions.append({
            'question_text': f"Is f(x) = {{{a1}x {s1} {abs(b1)} if x < {boundary}, {a2}x {s2} {abs(b2)} if x ≥ {boundary}}} continuous at x = {boundary}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Find value for continuity (12 questions)
    for _ in range(12):
        boundary = random.randint(-2, 3)
        a1 = random.randint(1, 4)
        b1 = random.randint(-4, 4)
        a2 = random.randint(1, 4)
        
        # Need b2 such that a1*boundary + b1 = a2*boundary + b2
        # b2 = a1*boundary + b1 - a2*boundary
        target_b2 = a1 * boundary + b1 - a2 * boundary
        
        correct = str(target_b2)
        
        distractors = [
            str(target_b2 + 1),
            str(target_b2 - 1),
            str(a1 * boundary + b1)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        left_val = a1 * boundary + b1
        
        explanation = f"For continuity at x = {boundary}: left limit = {a1}({boundary}) + {b1} = {left_val} must equal right limit = {a2}({boundary}) + k. So {a2}({boundary}) + k = {left_val}, giving k = {target_b2}."
        
        s1 = '+' if b1 >= 0 else '-'
        
        questions.append({
            'question_text': f"Find k so that f(x) = {{{a1}x {s1} {abs(b1)} if x < {boundary}, {a2}x + k if x ≥ {boundary}}} is continuous at x = {boundary}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Domain and range of piecewise (11 questions)
    piecewise_dr = [
        ("f(x) = {x if x ≤ 0, x² if x > 0}", "Domain: all real numbers; Range: all real numbers", "Both pieces cover all x values; y can be any real number."),
        ("f(x) = {2x if x < 1, 3 if x ≥ 1}", "Domain: all real numbers; Range: y < 2 or y = 3", "Left piece gives y < 2, right piece gives y = 3."),
        ("f(x) = {-x if x ≤ 0, x if x > 0}", "Domain: all real numbers; Range: y ≥ 0", "This is |x|, which is always non-negative."),
        ("f(x) = {1/x if x > 0, x if x ≤ 0}", "Domain: all real numbers; Range: all real numbers", "Left piece: y > 0; Right piece: y ≤ 0. Combined: all reals."),
        ("f(x) = {x² if x ≤ 1, 2x - 1 if x > 1}", "Domain: all real numbers; Range: y ≥ 0", "Both pieces produce non-negative outputs for their domains."),
        ("f(x) = {3 if x < 0, x + 3 if x ≥ 0}", "Domain: all real numbers; Range: y ≥ 3", "Left piece: y = 3; Right piece: y ≥ 3."),
        ("f(x) = {√x if x ≥ 0}", "Domain: x ≥ 0; Range: y ≥ 0", "Square root requires non-negative input and produces non-negative output."),
        ("f(x) = {|x| if x ≠ 0, 1 if x = 0}", "Domain: all real numbers; Range: y > 0", "At x ≠ 0, y = |x| > 0; at x = 0, y = 1 > 0."),
        ("f(x) = {x² if x < 2, 4 if x ≥ 2}", "Domain: all real numbers; Range: y ≥ 0", "Left piece gives 0 ≤ y < 4, right piece gives y = 4."),
        ("f(x) = {-x² if x ≤ 0, -x if x > 0}", "Domain: all real numbers; Range: y ≤ 0", "Both pieces produce non-positive outputs."),
        ("f(x) = {2 if x < 0, x² if x ≥ 0}", "Domain: all real numbers; Range: y = 2 or y ≥ 0", "Left: y = 2; Right: y ≥ 0. Combined range."),
    ]
    
    for q, a, expl in piecewise_dr:
        correct = a
        
        distractors = [
            "Domain: x > 0; Range: y > 0",
            "Domain: all real numbers; Range: y > 0",
            "Domain: x ≥ 0; Range: all real numbers"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the domain and range of {q}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge - Mixed advanced problems"""
    questions = []
    
    # Type 1: Complex composition (8 questions)
    for _ in range(8):
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 3)
        
        # f(x) = ax + b, g(x) = x², find f(g(x)) and g(f(x))
        question_type = random.choice(['fg', 'gf'])
        
        if question_type == 'fg':
            # f(g(x)) = f(x²) = ax² + b
            correct = f"{a}x² + {b}"
            explanation = f"f(g(x)) = f(x²) = {a}(x²) + {b} = {a}x² + {b}"
            q_text = f"If f(x) = {a}x + {b} and g(x) = x², find f(g(x))."
        else:
            # g(f(x)) = g(ax + b) = (ax + b)²
            correct = f"({a}x + {b})² or {a*a}x² + {2*a*b}x + {b*b}"
            explanation = f"g(f(x)) = g({a}x + {b}) = ({a}x + {b})² = {a*a}x² + {2*a*b}x + {b*b}"
            q_text = f"If f(x) = {a}x + {b} and g(x) = x², find g(f(x))."
        
        distractors = [
            f"{a}x² - {b}",
            f"x² + {a}x + {b}",
            f"{a*a}x + {b}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Inverse of composite function (8 questions)
    for _ in range(8):
        a = random.randint(2, 4)
        b = random.randint(1, 6)
        
        # f(x) = ax + b, find (f⁻¹ ∘ f)(x)
        correct = "x"
        explanation = "By definition, f⁻¹(f(x)) = x for all x in the domain. The inverse undoes the original function."
        
        distractors = [
            f"{a}x + {b}",
            f"(x - {b})/{a}",
            f"{a}x"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b}, find f⁻¹(f(x)).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Combined transformations (8 questions)
    for _ in range(8):
        h = random.randint(1, 4)
        k = random.randint(1, 4)
        a = random.choice([2, 3])
        
        # y = af(x - h) + k
        correct = f"Vertical stretch by {a}, right {h}, up {k}"
        
        distractors = [
            f"Vertical stretch by {a}, left {h}, up {k}",
            f"Horizontal stretch by {a}, right {h}, down {k}",
            f"Vertical stretch by {a}, right {h}, down {k}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"In y = {a}f(x - {h}) + {k}: the {a} is a vertical stretch, (x - {h}) shifts right {h}, and +{k} shifts up {k}."
        
        questions.append({
            'question_text': f"Describe all transformations mapping y = f(x) to y = {a}f(x - {h}) + {k}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Solving equations involving functions (8 questions)
    for _ in range(8):
        a = random.randint(2, 5)
        b = random.randint(1, 8)
        target = random.randint(10, 30)
        
        # f(x) = ax + b, solve f(x) = target
        x_val = (target - b) / a
        
        if x_val == int(x_val):
            correct = str(int(x_val))
        else:
            from fractions import Fraction
            frac = Fraction(target - b, a)
            correct = f"{frac.numerator}/{frac.denominator}" if frac.denominator != 1 else str(frac.numerator)
        
        distractors = [
            str(target // a),
            str((target + b) // a),
            str(target - b)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Solve {a}x + {b} = {target}: {a}x = {target - b}, x = {target - b}/{a} = {correct}"
        
        questions.append({
            'question_text': f"If f(x) = {a}x + {b}, solve f(x) = {target}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 5: Function equations (8 questions)
    func_eqs = [
        ("If f(x) = 2ˣ and g(x) = log₂(x), what is f(g(x))?", "x", "f(g(x)) = 2^(log₂(x)) = x, since exponential and log with same base are inverses."),
        ("If f(x) = eˣ and g(x) = ln(x), what is g(f(x))?", "x", "g(f(x)) = ln(eˣ) = x, since ln and eˣ are inverse functions."),
        ("If f(x) = x² and g(x) = √x, what is f(g(x)) for x ≥ 0?", "x", "f(g(x)) = (√x)² = x for x ≥ 0."),
        ("If f(x) = 3x - 6 and g(x) = (x + 6)/3, what is g(f(x))?", "x", "g(f(x)) = (3x - 6 + 6)/3 = 3x/3 = x. They are inverses."),
        ("If f(x) = 10ˣ and g(x) = log(x), what is f(g(100))?", "100", "g(100) = log(100) = 2, then f(2) = 10² = 100."),
        ("If f(x) = x³ and g(x) = ∛x, what is g(f(x))?", "x", "g(f(x)) = ∛(x³) = x. Cube and cube root are inverses."),
        ("If f(x) = 2x and g(x) = x/2, verify that f and g are inverses by computing f(g(x)).", "x", "f(g(x)) = f(x/2) = 2(x/2) = x. ✓"),
        ("If f(x) = x + 5 and g(x) = x - 5, what is f(g(f(1)))?", "6", "f(1) = 6, g(6) = 1, f(1) = 6."),
    ]
    
    for q, a, expl in func_eqs:
        correct = a
        
        distractors = ["2x", "x²", "1"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 6: Advanced domain problems (10 questions)
    domain_probs = [
        ("f(x) = ln(x²  - 4)", "x < -2 or x > 2", "Need x² - 4 > 0, so x² > 4, meaning |x| > 2."),
        ("f(x) = √(9 - x²)", "-3 ≤ x ≤ 3", "Need 9 - x² ≥ 0, so x² ≤ 9, meaning -3 ≤ x ≤ 3."),
        ("f(x) = 1/√(x - 2)", "x > 2", "Need x - 2 > 0 (strictly, since in denominator), so x > 2."),
        ("f(x) = ln(x) + ln(4 - x)", "0 < x < 4", "Need x > 0 AND 4 - x > 0, so 0 < x < 4."),
        ("f(x) = √x + √(1 - x)", "0 ≤ x ≤ 1", "Need x ≥ 0 AND 1 - x ≥ 0, so 0 ≤ x ≤ 1."),
        ("f(x) = 1/(x² - 1)", "x ≠ 1 and x ≠ -1", "Need x² - 1 ≠ 0, so x ≠ ±1."),
        ("f(x) = √(x - 1)/√(x + 2)", "x ≥ 1", "Need x - 1 ≥ 0 AND x + 2 > 0. First gives x ≥ 1, which satisfies second."),
        ("f(x) = log(x + 3) - log(x - 1)", "x > 1", "Need x + 3 > 0 AND x - 1 > 0. Second is stricter: x > 1."),
        ("f(x) = √(x² - 9)", "x ≤ -3 or x ≥ 3", "Need x² - 9 ≥ 0, so x² ≥ 9, meaning |x| ≥ 3."),
        ("f(x) = ln((x - 1)(x + 3))", "x < -3 or x > 1", "Need (x-1)(x+3) > 0. Positive when x < -3 or x > 1."),
    ]
    
    for q, a, expl in domain_probs:
        correct = a
        
        distractors = [
            "All real numbers",
            "x > 0",
            "x ≥ 0"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the domain of {q}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 12, 'difficulty_band': 'advanced'
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
    
    # Output SQL
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
        f.write(f"-- LC Higher Level - Functions Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
