#!/usr/bin/env python3
"""
LC Higher Level - Calculus (Differentiation) Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level × 12 levels) for LC HL Calculus - Differentiation
Based on SEC Leaving Certificate exam analysis 2019-2025

Levels:
1. Power Rule (Foundation)
2. Chain Rule (Foundation)
3. Product Rule (Foundation)
4. Quotient Rule (Developing)
5. Trig Differentiation (Developing)
6. Exponential & Log (Developing)
7. Tangents & Normals (Proficient)
8. Related Rates (Proficient)
9. Max/Min Problems (Proficient)
10. First Principles (Advanced)
11. Applied Optimization (Advanced)
12. Mastery Challenge (Advanced)
"""

import random
import sqlite3
import os
from fractions import Fraction
import math

# Configuration
TOPIC = 'lc_hl_calculus_diff'
MODE = 'lc_hl'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12

# Level titles for reference
LEVEL_TITLES = [
    'Power Rule',           # 1 - Foundation
    'Chain Rule',           # 2 - Foundation
    'Product Rule',         # 3 - Foundation
    'Quotient Rule',        # 4 - Developing
    'Trig Differentiation', # 5 - Developing
    'Exponential & Log',    # 6 - Developing
    'Tangents & Normals',   # 7 - Proficient
    'Related Rates',        # 8 - Proficient
    'Max/Min Problems',     # 9 - Proficient
    'First Principles',     # 10 - Advanced
    'Applied Optimization', # 11 - Advanced
    'Mastery Challenge'     # 12 - Advanced
]

def get_difficulty_band(level):
    if level <= 3:
        return 'foundation'
    elif level <= 6:
        return 'developing'
    elif level <= 9:
        return 'proficient'
    else:
        return 'advanced'

def make_unique_options(correct, distractors):
    """Create 4 unique options with correct answer randomly placed"""
    correct_str = str(correct)
    unique_wrong = []
    for d in distractors:
        d_str = str(d)
        if d_str != correct_str and d_str not in unique_wrong:
            unique_wrong.append(d_str)
    
    while len(unique_wrong) < 3:
        fallback = f"Option {len(unique_wrong) + 2}"
        if fallback not in unique_wrong and fallback != correct_str:
            unique_wrong.append(fallback)
    
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    
    return options, correct_idx

# ============================================================
# LEVEL 1: Power Rule (Foundation)
# ============================================================
def generate_level_1():
    """Power Rule - basic differentiation of polynomials"""
    questions = []
    
    # Type 1: Single term axⁿ
    for _ in range(20):
        a = random.choice([1, 2, 3, 4, 5, 6, -2, -3])
        n = random.randint(2, 6)
        
        derivative_coef = n * a
        derivative_power = n - 1
        
        func = f"{a}x^{n}" if a not in [1, -1] else (f"x^{n}" if a == 1 else f"-x^{n}")
        
        if derivative_power > 1:
            correct = f"{derivative_coef}x^{derivative_power}"
        elif derivative_power == 1:
            correct = f"{derivative_coef}x"
        else:
            correct = f"{derivative_coef}"
        
        distractors = [f"{a}x^{n-1}", f"{n}x^{n-1}", f"{derivative_coef}x^{n}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Power rule: d/dx(x^n) = nx^(n-1). For {func}: {n} × {a} = {derivative_coef}, power becomes {derivative_power}. Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Two-term polynomials
    for _ in range(20):
        a1, n1 = random.choice([2, 3, 4, 5]), random.randint(3, 5)
        a2, n2 = random.choice([1, 2, 3, -1, -2]), random.randint(1, 2)
        
        d1_coef, d1_pow = n1 * a1, n1 - 1
        d2_coef, d2_pow = n2 * a2, n2 - 1
        
        func = f"{a1}x^{n1} + {a2}x^{n2}" if a2 > 0 else f"{a1}x^{n1} - {abs(a2)}x^{n2}"
        
        if d2_pow == 0:
            correct = f"{d1_coef}x^{d1_pow} + {d2_coef}" if d2_coef > 0 else f"{d1_coef}x^{d1_pow} - {abs(d2_coef)}"
        else:
            correct = f"{d1_coef}x^{d1_pow} + {d2_coef}x" if d2_coef > 0 else f"{d1_coef}x^{d1_pow} - {abs(d2_coef)}x"
        
        distractors = [f"{a1}x^{n1-1} + {a2}", f"{d1_coef}x^{n1}", f"{n1}x^{d1_pow}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Differentiate each term: d/dx({a1}x^{n1}) = {d1_coef}x^{d1_pow}, d/dx({a2}x^{n2}) = {d2_coef}. Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Polynomials with constant
    for _ in range(10):
        a, n, c = random.choice([2, 3, 4, 5]), random.randint(2, 4), random.randint(1, 10)
        d_coef, d_pow = n * a, n - 1
        
        func = f"{a}x^{n} + {c}"
        correct = f"{d_coef}x^{d_pow}" if d_pow > 1 else f"{d_coef}x"
        
        distractors = [f"{d_coef}x^{d_pow} + {c}", f"{a}x^{n-1}", f"{d_coef}x^{n}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Constant {c} differentiates to 0. Only differentiate {a}x^{n} to get {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 2: Chain Rule (Foundation)
# ============================================================
def generate_level_2():
    """Chain Rule - composite functions"""
    questions = []
    
    # Type 1: (ax + b)ⁿ
    for _ in range(25):
        a, b, n = random.choice([2, 3, 4, 5]), random.choice([1, 2, 3, -1, -2]), random.randint(2, 5)
        outer_deriv, new_power = n * a, n - 1
        
        inner = f"{a}x + {b}" if b > 0 else f"{a}x - {abs(b)}"
        func = f"({inner})^{n}"
        correct = f"{outer_deriv}({inner})^{new_power}" if new_power > 1 else f"{outer_deriv}({inner})"
        
        distractors = [f"{n}({inner})^{new_power}", f"{a}({inner})^{new_power}", f"{outer_deriv}({inner})^{n}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Chain rule: outer derivative × inner derivative. {n}({inner})^{new_power} × {a} = {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: √(ax + b)
    for _ in range(15):
        a, b = random.choice([2, 3, 4]), random.choice([1, 2, 3, -1])
        inner = f"{a}x + {b}" if b > 0 else f"{a}x - {abs(b)}"
        func = f"√({inner})"
        correct = f"{a}/(2√({inner}))"
        
        distractors = [f"1/(2√({inner}))", f"{a}/√({inner})", f"{2*a}/√({inner})"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"√(u) = u^(1/2). Derivative: (1/2)u^(-1/2) × {a} = {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: (x² + a)ⁿ
    for _ in range(10):
        a, n = random.choice([1, 2, 3, 4]), random.choice([2, 3, 4])
        coef, new_power = 2 * n, n - 1
        inner = f"x² + {a}"
        func = f"({inner})^{n}"
        correct = f"{coef}x({inner})^{new_power}" if new_power > 1 else f"{coef}x({inner})"
        
        distractors = [f"{n}x({inner})^{new_power}", f"{coef}({inner})^{new_power}", f"{n}({inner})^{new_power}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Inner function x² has derivative 2x. Chain rule: {n} × 2x = {coef}x. Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 3: Product Rule (Foundation)
# ============================================================
def generate_level_3():
    """Product Rule - differentiate products of functions"""
    questions = []
    
    # Type 1: x × (ax + b)ⁿ
    for _ in range(20):
        a, b, n = random.choice([2, 3]), random.choice([1, 2, -1]), random.choice([2, 3])
        inner = f"{a}x + {b}" if b > 0 else f"{a}x - {abs(b)}"
        func = f"x({inner})^{n}"
        na, new_pow = n * a, n - 1
        
        correct = f"({inner})^{n} + {na}x({inner})^{new_pow}" if new_pow > 1 else f"({inner})^{n} + {na}x({inner})"
        distractors = [f"{na}x({inner})^{new_pow}", f"({inner})^{n}", f"{n}x({inner})^{new_pow}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Product rule: u'v + uv'. u=x, v=({inner})^{n}. Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: x² × (ax + b)
    for _ in range(15):
        a, b = random.choice([2, 3, 4]), random.choice([1, 2, 3])
        inner = f"{a}x + {b}"
        func = f"x²({inner})"
        correct = f"2x({inner}) + {a}x²"
        
        distractors = [f"2x({inner})", f"{a}x²", f"2({inner}) + {a}x²"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Product rule: u'v + uv' = 2x({inner}) + x²({a}) = {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: (x + a)(x + b)
    for _ in range(15):
        a, b = random.choice([1, 2, 3, 4]), random.choice([1, 2, 3, -1, -2])
        u_str = f"(x + {a})"
        v_str = f"(x + {b})" if b > 0 else f"(x - {abs(b)})"
        func = f"{u_str}{v_str}"
        sum_ab = a + b
        correct = f"2x + {sum_ab}" if sum_ab > 0 else (f"2x - {abs(sum_ab)}" if sum_ab < 0 else "2x")
        
        distractors = [f"x + {sum_ab}" if sum_ab != 0 else "x", f"2x + {a}", f"2x + {b}" if b > 0 else f"2x - {abs(b)}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Product rule: 1×{v_str} + {u_str}×1 = 2x + {a} + {b} = {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 4: Quotient Rule (Developing)
# ============================================================
def generate_level_4():
    """Quotient Rule - differentiate quotients"""
    questions = []
    
    # Type 1: x/(ax + b)
    for _ in range(20):
        a, b = random.choice([2, 3, 4]), random.choice([1, 2, 3])
        inner = f"{a}x + {b}"
        func = f"x/({inner})"
        correct = f"{b}/({inner})²"
        
        distractors = [f"1/({inner})²", f"{a}/({inner})²", f"-{b}/({inner})²"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Quotient rule: (u'v - uv')/v². Numerator: 1×({inner}) - x×{a} = {b}. Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: (ax + b)/(cx + d)
    for _ in range(20):
        a, b, c, d = random.choice([1, 2, 3]), random.choice([1, 2]), random.choice([1, 2]), random.choice([1, 2, 3])
        num, den = f"{a}x + {b}", f"{c}x + {d}"
        func = f"({num})/({den})"
        result_num = a * d - b * c
        correct = f"{result_num}/({den})²" if result_num != 0 else "0"
        
        distractors = [f"{a*d}/({den})²", f"{b*c}/({den})²", f"{abs(result_num + 1)}/({den})²"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Quotient rule: ({a}×({c}x+{d}) - {c}×({a}x+{b}))/({den})² = ({a*d} - {b*c})/({den})² = {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: x²/(x + a)
    for _ in range(10):
        a = random.choice([1, 2, 3])
        func = f"x²/(x + {a})"
        correct = f"x(x + {2*a})/(x + {a})²"
        
        distractors = [f"2x/(x + {a})²", f"x²/(x + {a})²", f"(x + {2*a})/(x + {a})²"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"(2x(x+{a}) - x²)/(x+{a})² = (x² + {2*a}x)/(x+{a})² = {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 5: Trig Differentiation (Developing)
# ============================================================
def generate_level_5():
    """Trigonometric differentiation"""
    questions = []
    
    # Type 1: Basic trig
    trig_basics = [
        ("sin x", "cos x", "-sin x", "sin x", "-cos x"),
        ("cos x", "-sin x", "sin x", "-cos x", "cos x"),
        ("tan x", "sec²x", "cot x", "-tan x", "sec x"),
        ("sin 2x", "2cos 2x", "cos 2x", "-2sin 2x", "2sin 2x"),
        ("cos 2x", "-2sin 2x", "2cos 2x", "-sin 2x", "sin 2x"),
    ]
    
    for _ in range(15):
        func, correct, d1, d2, d3 = random.choice(trig_basics)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"d/dx({func}) = {correct}. Key: d/dx(sin x) = cos x, d/dx(cos x) = -sin x ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: sin(ax) and cos(ax)
    for _ in range(20):
        a = random.choice([2, 3, 4, 5])
        trig_func = random.choice(['sin', 'cos'])
        func = f"{trig_func}({a}x)"
        
        if trig_func == 'sin':
            correct = f"{a}cos({a}x)"
            distractors = [f"cos({a}x)", f"-{a}sin({a}x)", f"{a}sin({a}x)"]
        else:
            correct = f"-{a}sin({a}x)"
            distractors = [f"-sin({a}x)", f"{a}cos({a}x)", f"-{a}cos({a}x)"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Chain rule with trig: derivative × inner derivative ({a}). Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: a·sin(bx) or a·cos(bx)
    for _ in range(15):
        a, b = random.choice([2, 3, 4]), random.choice([2, 3])
        trig_func = random.choice(['sin', 'cos'])
        func = f"{a}{trig_func}({b}x)"
        ab = a * b
        
        if trig_func == 'sin':
            correct = f"{ab}cos({b}x)"
            distractors = [f"{a}cos({b}x)", f"-{ab}sin({b}x)", f"{b}cos({b}x)"]
        else:
            correct = f"-{ab}sin({b}x)"
            distractors = [f"-{a}sin({b}x)", f"{ab}cos({b}x)", f"-{b}sin({b}x)"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"d/dx[{a}{trig_func}({b}x)] = {a} × {b} × derivative = {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 6: Exponential & Log (Developing)
# ============================================================
def generate_level_6():
    """Exponential and logarithmic differentiation"""
    questions = []
    
    # Type 1: e^(ax)
    for _ in range(15):
        a = random.choice([2, 3, 4, 5, -2, -3])
        func = f"e^{{{a}x}}"
        correct = f"{a}e^{{{a}x}}"
        
        distractors = [f"e^{{{a}x}}", f"{a}xe^{{{a}x}}", f"e^{{{a-1}x}}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"d/dx(e^{{kx}}) = ke^{{kx}}. With k={a}: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: ln(ax)
    for _ in range(15):
        a = random.choice([2, 3, 4, 5])
        func = f"ln({a}x)"
        correct = "1/x"
        
        distractors = [f"{a}/x", f"1/{a}x", f"{a}x"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"ln({a}x) = ln({a}) + ln(x). d/dx[ln(x)] = 1/x. Constant term vanishes. Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: ln(x^n)
    for _ in range(10):
        n = random.choice([2, 3, 4, 5])
        func = f"ln(x^{n})"
        correct = f"{n}/x"
        
        distractors = ["1/x", f"{n}x", f"x^{n}/x"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"ln(x^{n}) = {n}ln(x). d/dx[{n}ln(x)] = {n}/x ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 4: ae^(bx)
    for _ in range(10):
        a, b = random.choice([2, 3, 4]), random.choice([2, 3])
        func = f"{a}e^{{{b}x}}"
        ab = a * b
        correct = f"{ab}e^{{{b}x}}"
        
        distractors = [f"{a}e^{{{b}x}}", f"{b}e^{{{b}x}}", f"{ab}e^{{{b-1}x}}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{a} × {b}e^{{{b}x}} = {ab}e^{{{b}x}} ✓"
        
        questions.append({
            'question_text': f"Differentiate f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 7: Tangents & Normals (Proficient)
# ============================================================
def generate_level_7():
    """Find tangent and normal line equations"""
    questions = []
    
    # Type 1: Tangent to y = ax² at point
    for _ in range(20):
        a, x_val = random.choice([1, 2, 3]), random.choice([1, 2, 3])
        y_val = a * x_val ** 2
        slope = 2 * a * x_val
        c = -slope * x_val + y_val
        
        func = f"x²" if a == 1 else f"{a}x²"
        correct = f"y = {slope}x + {c}" if c > 0 else (f"y = {slope}x - {abs(c)}" if c < 0 else f"y = {slope}x")
        
        distractors = [f"y = {2*a}x + {c}", f"y = {slope}x + {y_val}", f"y = {x_val}x + {c}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f'(x) = {2*a}x. At x={x_val}: slope = {slope}, point ({x_val},{y_val}). Tangent: {correct} ✓"
        
        questions.append({
            'question_text': f"Find the equation of the tangent to y = {func} at x = {x_val}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Find slope of tangent
    for _ in range(15):
        a, b = random.choice([1, 2, 3]), random.choice([2, 4, 6, -2, -4])
        x_val = random.choice([1, 2, 3])
        slope = 2 * a * x_val + b
        
        if b > 0:
            func = f"{a}x² + {b}x" if a != 1 else f"x² + {b}x"
        else:
            func = f"{a}x² - {abs(b)}x" if a != 1 else f"x² - {abs(b)}x"
        
        correct = str(slope)
        distractors = [str(2 * a * x_val), str(2 * a + b), str(a * x_val ** 2 + b * x_val)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f'(x) = {2*a}x + {b}. At x={x_val}: f'({x_val}) = {2*a}×{x_val} + {b} = {slope} ✓"
        
        questions.append({
            'question_text': f"Find the slope of the tangent to y = {func} at x = {x_val}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Normal line slope
    for _ in range(15):
        a, x_val = random.choice([1, 2]), random.choice([1, 2])
        tangent_slope = 2 * a * x_val
        
        func = f"x²" if a == 1 else f"{a}x²"
        correct = f"-1/{tangent_slope}"
        
        distractors = [f"1/{tangent_slope}", str(tangent_slope), f"-{tangent_slope}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Tangent slope = {tangent_slope}. Normal slope = -1/{tangent_slope} (perpendicular) ✓"
        
        questions.append({
            'question_text': f"Find the slope of the normal to y = {func} at x = {x_val}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 8: Related Rates (Proficient)
# ============================================================
def generate_level_8():
    """Related rates problems"""
    questions = []
    
    # Type 1: Area of circle changing
    for _ in range(15):
        dr_dt, r_val = random.choice([1, 2, 3, 4]), random.choice([2, 3, 4, 5])
        dA_dt = 2 * r_val * dr_dt
        
        correct = f"{dA_dt}π cm²/s"
        distractors = [f"{r_val * dr_dt}π cm²/s", f"{2 * r_val}π cm²/s", f"{dA_dt} cm²/s"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"A = πr². dA/dt = 2πr × dr/dt = 2π({r_val})({dr_dt}) = {dA_dt}π cm²/s ✓"
        
        questions.append({
            'question_text': f"A circle's radius increases at {dr_dt} cm/s. Find the rate of change of area when r = {r_val} cm.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Volume of sphere changing
    for _ in range(15):
        dr_dt, r_val = random.choice([1, 2]), random.choice([2, 3, 4])
        dV_dt = 4 * r_val ** 2 * dr_dt
        
        correct = f"{dV_dt}π cm³/s"
        distractors = [f"{4 * r_val * dr_dt}π cm³/s", f"{r_val ** 2 * dr_dt}π cm³/s", f"{dV_dt} cm³/s"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"V = (4/3)πr³. dV/dt = 4πr² × dr/dt = 4π({r_val})²({dr_dt}) = {dV_dt}π cm³/s ✓"
        
        questions.append({
            'question_text': f"A sphere's radius increases at {dr_dt} cm/s. Find the rate of change of volume when r = {r_val} cm.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Square area changing
    for _ in range(10):
        ds_dt, s_val = random.choice([2, 3, 4]), random.choice([3, 4, 5, 6])
        dA_dt = 2 * s_val * ds_dt
        
        correct = f"{dA_dt} cm²/s"
        distractors = [f"{s_val * ds_dt} cm²/s", f"{2 * s_val} cm²/s", f"{s_val ** 2} cm²/s"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"A = s². dA/dt = 2s × ds/dt = 2({s_val})({ds_dt}) = {dA_dt} cm²/s ✓"
        
        questions.append({
            'question_text': f"A square's side increases at {ds_dt} cm/s. Find the rate of change of area when the side is {s_val} cm.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Cube volume changing
    for _ in range(10):
        ds_dt, s_val = random.choice([1, 2]), random.choice([2, 3, 4])
        dV_dt = 3 * s_val ** 2 * ds_dt
        
        correct = f"{dV_dt} cm³/s"
        distractors = [f"{s_val ** 2 * ds_dt} cm³/s", f"{3 * s_val * ds_dt} cm³/s", f"{s_val ** 3} cm³/s"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"V = s³. dV/dt = 3s² × ds/dt = 3({s_val})²({ds_dt}) = {dV_dt} cm³/s ✓"
        
        questions.append({
            'question_text': f"A cube's side increases at {ds_dt} cm/s. Find the rate of change of volume when the side is {s_val} cm.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 9: Max/Min Problems (Proficient)
# ============================================================
def generate_level_9():
    """Maximum and minimum value problems"""
    questions = []
    
    # Type 1: Find turning point x-coordinate
    for _ in range(20):
        a, b = random.choice([1, 2, -1, -2]), random.choice([2, 4, 6, -2, -4])
        c = random.choice([1, 2, 3])
        x_tp = -b / (2 * a)
        nature = "minimum" if a > 0 else "maximum"
        
        func = f"{a}x² + {b}x + {c}" if b > 0 else f"{a}x² - {abs(b)}x + {c}"
        if a == 1: func = func.replace("1x²", "x²")
        if a == -1: func = func.replace("-1x²", "-x²")
        
        correct = f"x = {int(x_tp) if x_tp == int(x_tp) else x_tp}"
        distractors = [f"x = {int(-x_tp) if -x_tp == int(-x_tp) else -x_tp}", f"x = {b}", f"x = {-b}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f'(x) = {2*a}x + {b} = 0. x = {-b}/{2*a} = {x_tp}. This is a {nature}. ✓"
        
        questions.append({
            'question_text': f"Find the x-coordinate of the turning point of f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Second derivative test
    for _ in range(15):
        a, x_val = random.choice([1, 2, 3, -1, -2]), random.choice([1, 2, 3])
        second_deriv = 2 * a
        correct = "Minimum" if second_deriv > 0 else "Maximum"
        
        distractors = ["Maximum" if correct == "Minimum" else "Minimum", "Inflection point", "Cannot determine"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f''({x_val}) = {second_deriv}. {'Positive' if second_deriv > 0 else 'Negative'} → {correct} ✓"
        
        questions.append({
            'question_text': f"If f''({x_val}) = {second_deriv} at a turning point, what is its nature?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Find minimum/maximum value
    for _ in range(15):
        a, p, k = random.choice([1, -1]), random.choice([1, 2, 3]), random.choice([2, 3, 4, 5])
        nature = "minimum" if a > 0 else "maximum"
        func = f"(x - {p})² + {k}" if a == 1 else f"-(x - {p})² + {k}"
        correct = str(k)
        
        distractors = [str(p), str(k + 1), str(k - 1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Vertex form: {func}. Vertex at ({p}, {k}). {nature.capitalize()} value = {k} ✓"
        
        questions.append({
            'question_text': f"Find the {nature} value of f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 10: First Principles (Advanced)
# ============================================================
def generate_level_10():
    """Differentiation from first principles"""
    questions = []
    
    # Type 1: First principles steps
    first_principles = [
        ("f(x) = x²", "f(x+h) - f(x) = ?", "2xh + h²", "2x + h", "h²", "2xh"),
        ("f(x) = x²", "[f(x+h) - f(x)]/h = ?", "2x + h", "2x", "2xh + h", "x + h"),
        ("f(x) = x²", "lim(h→0)[f(x+h) - f(x)]/h = ?", "2x", "2x + h", "x", "2"),
        ("f(x) = x³", "[f(x+h) - f(x)]/h simplified = ?", "3x² + 3xh + h²", "3x²", "x²", "3x"),
        ("f(x) = 2x", "lim(h→0)[f(x+h) - f(x)]/h = ?", "2", "2x", "0", "2h"),
    ]
    
    for _ in range(20):
        func, question, correct, d1, d2, d3 = random.choice(first_principles)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"First principles: f'(x) = lim(h→0)[f(x+h) - f(x)]/h. Answer: {correct} ✓"
        
        questions.append({
            'question_text': f"Using first principles with {func}: {question}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Complete first principles result
    functions = [("x²", "2x"), ("x³", "3x²"), ("2x²", "4x"), ("3x²", "6x"), 
                 ("x² + x", "2x + 1"), ("2x", "2"), ("5x", "5"), ("x² - 3x", "2x - 3")]
    
    for _ in range(20):
        func, correct = random.choice(functions)
        distractors = ["x", "2", "x² - 1", "x + 1"] if 'x²' in func else ["x", "1", "0", "2x"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Using first principles for f(x) = {func}: derivative is {correct} ✓"
        
        questions.append({
            'question_text': f"Using first principles, find the derivative of f(x) = {func}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Expand expressions
    for _ in range(10):
        h_terms = [("(x+h)² - x²", "2xh + h²"), ("2(x+h) - 2x", "2h"), ("3(x+h)² - 3x²", "6xh + 3h²")]
        expression, correct = random.choice(h_terms)
        distractors = ["2xh", "h²", "3x²h", "xh"]
        distractors = [d for d in distractors if d != correct][:3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Expanding {expression} gives {correct} ✓"
        
        questions.append({
            'question_text': f"Simplify: {expression}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

# ============================================================
# LEVEL 11: Applied Optimization (Advanced)
# ============================================================
def generate_level_11():
    """Applied optimization problems"""
    questions = []
    
    # Type 1: Rectangle with fixed perimeter
    for _ in range(15):
        P = random.choice([20, 24, 28, 32, 40])
        x_opt = P // 4
        max_area = x_opt * x_opt
        
        correct = str(max_area)
        distractors = [str(max_area + x_opt), str(P * P // 16 + 10), str(x_opt * 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Perimeter {P}: sides x and y with 2x+2y={P}. Area = x({P//2}-x). Max at x={x_opt}. Area = {max_area} ✓"
        
        questions.append({
            'question_text': f"A rectangle has perimeter {P} cm. What is the maximum possible area?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Box with open top - optimal cut size
    for _ in range(15):
        side = random.choice([12, 16, 20, 24])
        correct = f"{side}/6" if side % 6 != 0 else str(side // 6)
        
        distractors = [f"{side}/4", f"{side}/3", f"{side}/2"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"V = x({side}-2x)². dV/dx = 0 gives x = {side}/6 for maximum volume ✓"
        
        questions.append({
            'question_text': f"A {side}cm × {side}cm sheet has squares cut from corners for an open box. What cut size maximizes volume?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Optimal cylinder dimensions
    for _ in range(10):
        correct = "2r (diameter)"
        distractors = ["r (radius)", "πr", "4r"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = "For minimum surface area with fixed volume, optimal cylinder has h = 2r ✓"
        
        questions.append({
            'question_text': "To minimize surface area of a closed cylinder with fixed volume, the height should equal...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Speed optimization
    for _ in range(10):
        a, b = random.choice([100, 200, 400]), random.choice([1, 2])
        v_opt = int((a / b) ** 0.5)
        correct = f"{v_opt} km/h"
        
        distractors = [f"{v_opt + 10} km/h", f"{v_opt - 10} km/h", f"{v_opt * 2} km/h"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Cost C = {a}/v + {b}v. dC/dv = 0 → v = √({a}/{b}) = {v_opt} km/h ✓"
        
        questions.append({
            'question_text': f"A journey's cost is C = {a}/v + {b}v per km. Find the speed that minimizes cost.",
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
    """Mixed challenging differentiation problems"""
    questions = []
    
    # Type 1: Implicit differentiation
    for _ in range(10):
        r = random.choice([5, 10, 13])
        correct = "-x/y"
        distractors = ["x/y", "-y/x", "y/x"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"x² + y² = {r}². Differentiate: 2x + 2y(dy/dx) = 0. dy/dx = -x/y ✓"
        
        questions.append({
            'question_text': f"If x² + y² = {r}², find dy/dx",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Find where slope equals value
    for _ in range(10):
        a, target = random.choice([1, 2]), random.choice([2, 4, 6])
        x_val = target // (2 * a)
        func = f"x²" if a == 1 else f"{a}x²"
        correct = str(x_val)
        
        distractors = [str(x_val + 1), str(x_val - 1), str(target)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"f'(x) = {2*a}x = {target}. x = {target}/{2*a} = {x_val} ✓"
        
        questions.append({
            'question_text': f"At what value of x does y = {func} have slope {target}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: SEC-style mixed questions
    sec_questions = [
        ("Find f'(2) if f(x) = x³ - 3x² + 2x", "2", ["8", "0", "-2"]),
        ("Find f'(1) if f(x) = (x + 1)³", "12", ["3", "8", "27"]),
        ("If y = ln(x²), find dy/dx", "2/x", ["1/x", "2x", "1/x²"]),
        ("Find d/dx[x·eˣ] at x = 0", "1", ["0", "e", "2"]),
        ("If f(x) = sin²x, find f'(x)", "2sinx·cosx", ["cos²x", "2sinx", "-2sinx·cosx"]),
    ]
    
    for _ in range(30):
        q_text, correct, distractors = random.choice(sec_questions)
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Apply appropriate differentiation rules. Answer: {correct} ✓"
        
        questions.append({
            'question_text': q_text,
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
    
    sql_file = '/home/claude/lc_hl_calculus_diff_questions.sql'
    with open(sql_file, 'w') as f:
        f.write(f"-- LC Higher Level - Calculus (Differentiation) Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    questions = main()
