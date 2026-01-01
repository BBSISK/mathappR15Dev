#!/usr/bin/env python3
"""
LC Ordinary Level - Calculus (Differentiation) Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level × 12 levels) for LC OL Calculus
Based on SEC Paper Analysis 2019-2025 (445 marks - #1 priority topic for Paper 1)

OL Calculus Focus:
- Power rule for polynomials
- Finding derivatives
- Slopes at specific points  
- Equations of tangents
- Maximum/minimum values
- Second derivative test
- Applied optimization (profit, cost contexts)
- Reading graphs for turning points

Levels:
1. Power Rule Basics
2. Differentiating Polynomials
3. Negative Powers
4. Finding Slopes
5. Equations of Tangents
6. Rate of Change
7. Increasing/Decreasing
8. Max & Min Values
9. Second Derivative
10. Applied Max/Min
11. Optimization Problems
12. Mastery Challenge
"""

import random

TOPIC = 'lc_ol_calculus'
MODE = 'lc_ol'

LEVEL_TITLES = [
    'Power Rule Basics',
    'Differentiating Polynomials',
    'Negative Powers',
    'Finding Slopes',
    'Equations of Tangents',
    'Rate of Change',
    'Increasing/Decreasing',
    'Max & Min Values',
    'Second Derivative',
    'Applied Max/Min',
    'Optimization Problems',
    'Mastery Challenge'
]

# Superscript mappings for nice display
SUPERSCRIPTS = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
                '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', 
                '-': '⁻'}

def to_superscript(n):
    """Convert number to superscript string"""
    return ''.join(SUPERSCRIPTS.get(c, c) for c in str(n))

def format_term(coef, power, var='x'):
    """Format a term like 3x² with proper superscript"""
    if power == 0:
        return str(coef)
    elif power == 1:
        if coef == 1:
            return var
        elif coef == -1:
            return f"-{var}"
        else:
            return f"{coef}{var}"
    else:
        sup = to_superscript(power)
        if coef == 1:
            return f"{var}{sup}"
        elif coef == -1:
            return f"-{var}{sup}"
        else:
            return f"{coef}{var}{sup}"

def format_polynomial(terms):
    """Format polynomial from list of (coef, power) tuples, sorted by descending power"""
    if not terms:
        return "0"
    # Sort by power descending
    sorted_terms = sorted(terms, key=lambda x: x[1], reverse=True)
    result = ""
    for i, (coef, power) in enumerate(sorted_terms):
        if coef == 0:
            continue
        term_str = format_term(abs(coef), power)
        if i == 0:
            if coef < 0:
                result = f"-{term_str}"
            else:
                result = term_str
        else:
            if coef < 0:
                result += f" - {term_str}"
            else:
                result += f" + {term_str}"
    return result if result else "0"

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
    """Level 1: Power Rule Basics - y = x^n → dy/dx = nx^(n-1)"""
    questions = []
    
    # Type 1: Simple x^n (25 questions)
    for _ in range(25):
        n = random.randint(2, 6)
        question = f"If y = {format_term(1, n)}, find dy/dx."
        correct = format_term(n, n-1)
        distractors = [
            format_term(n-1, n),      # Wrong: didn't bring down power
            format_term(n, n),        # Wrong: didn't reduce power
            format_term(1, n-1)       # Wrong: forgot coefficient
        ]
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Using the power rule: dy/dx = {n}x^{n-1} = {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: ax^n with coefficient (15 questions)
    for _ in range(15):
        a = random.randint(2, 5)
        n = random.randint(2, 5)
        question = f"If y = {format_term(a, n)}, find dy/dx."
        new_coef = a * n
        correct = format_term(new_coef, n-1)
        distractors = [
            format_term(a, n-1),          # Wrong: forgot to multiply
            format_term(n, n-1),          # Wrong: dropped coefficient
            format_term(new_coef, n)      # Wrong: didn't reduce power
        ]
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Power rule: dy/dx = {a} × {n}x^{n-1} = {new_coef}x^{n-1} = {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Derivative of constant (10 questions)
    for _ in range(10):
        c = random.randint(3, 20)
        question = f"If y = {c}, find dy/dx."
        correct = "0"
        distractors = [str(c), "1", str(c-1)]
        options, idx = make_unique_options(correct, distractors)
        explanation = f"The derivative of a constant is always 0."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_2():
    """Level 2: Differentiating Polynomials - multiple terms"""
    questions = []
    
    # Type 1: Two-term polynomials (20 questions)
    for _ in range(20):
        a1 = random.randint(1, 4)
        n1 = random.randint(2, 4)
        a2 = random.choice([-1, 1]) * random.randint(1, 6)
        n2 = random.randint(0, n1-1)
        
        poly = format_polynomial([(a1, n1), (a2, n2)])
        question = f"If f(x) = {poly}, find f'(x)."
        
        # Calculate derivative
        d1_coef = a1 * n1 if n1 > 0 else 0
        d1_pow = n1 - 1 if n1 > 0 else 0
        d2_coef = a2 * n2 if n2 > 0 else 0
        d2_pow = n2 - 1 if n2 > 0 else 0
        
        deriv_terms = []
        if d1_coef != 0:
            deriv_terms.append((d1_coef, d1_pow))
        if d2_coef != 0:
            deriv_terms.append((d2_coef, d2_pow))
        
        correct = format_polynomial(deriv_terms) if deriv_terms else "0"
        
        # Generate plausible distractors
        distractors = [
            format_polynomial([(a1, n1-1), (a2, n2-1 if n2 > 0 else 0)]),
            format_polynomial([(a1*n1, n1), (a2*n2 if n2 > 0 else 0, n2)]),
            format_polynomial([(d1_coef+1, d1_pow), (d2_coef, d2_pow)])
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Differentiate term by term using the power rule: f'(x) = {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Three-term polynomials (20 questions)
    for _ in range(20):
        a1 = random.randint(1, 3)
        n1 = 3
        a2 = random.choice([-1, 1]) * random.randint(1, 4)
        n2 = 2
        a3 = random.choice([-1, 1]) * random.randint(1, 6)
        n3 = random.randint(0, 1)
        
        poly = format_polynomial([(a1, n1), (a2, n2), (a3, n3)])
        question = f"If y = {poly}, find dy/dx."
        
        d1 = a1 * 3
        d2 = a2 * 2
        d3 = a3 if n3 == 1 else 0
        
        deriv_terms = [(d1, 2), (d2, 1)]
        if d3 != 0:
            deriv_terms.append((d3, 0))
        
        correct = format_polynomial(deriv_terms)
        
        distractors = [
            format_polynomial([(a1, 2), (a2, 1), (a3, 0)]),
            format_polynomial([(d1, 3), (d2, 2)]),
            format_polynomial([(d1+1, 2), (d2-1, 1)])
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Apply the power rule to each term: dy/dx = {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Identifying f'(x) notation (10 questions)
    notations = [
        ("y = x³", "dy/dx", "3x²"),
        ("f(x) = x⁴", "f'(x)", "4x³"),
        ("y = 2x²", "dy/dx", "4x"),
        ("g(x) = 5x³", "g'(x)", "15x²"),
        ("s(t) = t²", "s'(t)", "2t"),
        ("y = x⁵", "dy/dx", "5x⁴"),
        ("h(x) = 3x⁴", "h'(x)", "12x³"),
        ("y = 4x", "dy/dx", "4"),
        ("f(x) = 6x²", "f'(x)", "12x"),
        ("P(t) = t³", "P'(t)", "3t²")
    ]
    
    for func, deriv_notation, answer in notations:
        question = f"If {func}, what is {deriv_notation}?"
        correct = answer
        # Generate wrong answers
        if "x²" in answer:
            distractors = [answer.replace("x²", "x³"), answer.replace("x²", "x"), answer[0] + "x³"]
        elif "x³" in answer:
            distractors = [answer.replace("x³", "x²"), answer.replace("x³", "x⁴"), "x³"]
        elif "x⁴" in answer:
            distractors = [answer.replace("x⁴", "x³"), answer.replace("x⁴", "x⁵"), "x⁴"]
        else:
            distractors = ["0", "x", "1"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Using the power rule: {deriv_notation} = {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_3():
    """Level 3: Negative Powers"""
    questions = []
    
    # Type 1: Rewriting with negative powers (20 questions)
    for _ in range(20):
        n = random.randint(2, 4)
        a = random.randint(1, 5)
        
        question = f"If y = {a}/x{to_superscript(n)}, rewrite as y = ax^n and find dy/dx."
        
        # y = a/x^n = ax^(-n), dy/dx = -an*x^(-n-1)
        deriv_coef = -a * n
        deriv_pow = -n - 1
        
        correct = f"{deriv_coef}x{to_superscript(deriv_pow)}"
        distractors = [
            f"{a*n}x{to_superscript(-n-1)}",      # Wrong sign
            f"{-a}x{to_superscript(-n-1)}",       # Forgot to multiply by power
            f"{deriv_coef}x{to_superscript(-n)}"  # Didn't reduce power
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Rewrite as y = {a}x^{-n}. Then dy/dx = {-n} × {a}x^{-n-1} = {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Simple 1/x^n (15 questions)
    for _ in range(15):
        n = random.randint(1, 3)
        
        if n == 1:
            question = "If y = 1/x, find dy/dx."
            correct = "-1/x²"
            distractors = ["1/x²", "-1/x", "1/x"]
        else:
            question = f"If y = 1/x{to_superscript(n)}, find dy/dx."
            correct = f"-{n}/x{to_superscript(n+1)}"
            distractors = [
                f"{n}/x{to_superscript(n+1)}",
                f"-{n}/x{to_superscript(n)}",
                f"-1/x{to_superscript(n+1)}"
            ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Write as x^{-n}, apply power rule: dy/dx = {-n}x^{-n-1} = {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Mixed positive and negative powers (15 questions)
    for _ in range(15):
        a1 = random.randint(1, 3)
        n1 = random.randint(2, 3)
        a2 = random.randint(1, 4)
        
        question = f"If y = {format_term(a1, n1)} + {a2}/x, find dy/dx."
        
        d1_coef = a1 * n1
        d1_pow = n1 - 1
        
        correct = f"{format_term(d1_coef, d1_pow)} - {a2}/x²"
        distractors = [
            f"{format_term(d1_coef, d1_pow)} + {a2}/x²",
            f"{format_term(a1, d1_pow)} - {a2}/x²",
            f"{format_term(d1_coef, n1)} - {a2}/x"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Differentiate each term: {d1_coef}x^{d1_pow} from power rule, and -({a2})x^{-2} = -{a2}/x² from 1/x"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_4():
    """Level 4: Finding Slopes at Points"""
    questions = []
    
    # Type 1: Simple polynomial, find slope at x = a (25 questions)
    for _ in range(25):
        a = random.randint(1, 3)  # coefficient
        n = random.randint(2, 3)  # power
        x_val = random.randint(1, 4)
        
        # y = ax^n, dy/dx = anx^(n-1)
        deriv_coef = a * n
        deriv_pow = n - 1
        slope = deriv_coef * (x_val ** deriv_pow)
        
        question = f"Find the slope of the tangent to y = {format_term(a, n)} at x = {x_val}."
        correct = str(slope)
        distractors = [
            str(a * (x_val ** n)),           # Evaluated original function
            str(deriv_coef * x_val),          # Wrong power in derivative
            str(slope + deriv_coef)           # Arithmetic error
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"dy/dx = {format_term(deriv_coef, deriv_pow)}. At x = {x_val}: slope = {deriv_coef}({x_val})^{deriv_pow} = {slope}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Two-term polynomial (15 questions)
    for _ in range(15):
        a1, a2 = random.randint(1, 2), random.choice([-1, 1]) * random.randint(1, 4)
        x_val = random.randint(1, 3)
        
        # y = a1*x^3 + a2*x
        # dy/dx = 3a1*x^2 + a2
        deriv_at_x = 3 * a1 * (x_val ** 2) + a2
        
        poly = format_polynomial([(a1, 3), (a2, 1)])
        question = f"Find the slope of f(x) = {poly} at x = {x_val}."
        
        correct = str(deriv_at_x)
        distractors = [
            str(3 * a1 * x_val + a2),
            str(a1 * (x_val ** 3) + a2 * x_val),
            str(deriv_at_x + a2)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"f'(x) = {3*a1}x² + {a2}. At x = {x_val}: f'({x_val}) = {3*a1}({x_val})² + {a2} = {deriv_at_x}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Given derivative, find slope (10 questions)
    for _ in range(10):
        a = random.randint(2, 5)
        b = random.choice([-1, 1]) * random.randint(1, 6)
        x_val = random.randint(1, 4)
        
        # dy/dx = ax + b
        slope = a * x_val + b
        
        question = f"If dy/dx = {a}x + {b}, find the slope of the tangent at x = {x_val}."
        correct = str(slope)
        distractors = [
            str(a * x_val),
            str(slope + a),
            str(a + b)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Substitute x = {x_val}: slope = {a}({x_val}) + {b} = {slope}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_5():
    """Level 5: Equations of Tangents"""
    questions = []
    
    # Type 1: Find tangent equation at given point (25 questions)
    for _ in range(25):
        a = random.randint(1, 2)
        n = 2
        x1 = random.randint(1, 3)
        
        # y = ax^2, y' = 2ax
        y1 = a * (x1 ** 2)
        slope = 2 * a * x1
        
        # y - y1 = m(x - x1) → y = mx - mx1 + y1
        c = -slope * x1 + y1
        
        question = f"Find the equation of the tangent to y = {format_term(a, 2)} at the point ({x1}, {y1})."
        
        if c >= 0:
            correct = f"y = {slope}x + {c}"
        else:
            correct = f"y = {slope}x - {abs(c)}"
        
        distractors = [
            f"y = {2*a}x + {y1}",
            f"y = {slope}x + {y1}",
            f"y = {slope}x - {c + 2}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"dy/dx = {2*a}x. At x = {x1}: slope = {slope}. Using y - y₁ = m(x - x₁): y - {y1} = {slope}(x - {x1}), so {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Find y-intercept of tangent (15 questions)
    for _ in range(15):
        a = random.randint(1, 2)
        x1 = random.randint(2, 4)
        
        # y = ax^2
        y1 = a * (x1 ** 2)
        slope = 2 * a * x1
        c = y1 - slope * x1  # y-intercept
        
        question = f"The tangent to y = {format_term(a, 2)} at x = {x1} has y-intercept at:"
        correct = f"(0, {c})"
        distractors = [
            f"(0, {y1})",
            f"(0, {-c})",
            f"(0, {slope})"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Slope = {slope}, point ({x1}, {y1}). Tangent: y = {slope}x + c. At ({x1}, {y1}): {y1} = {slope}({x1}) + c, so c = {c}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Match slope to point (10 questions)
    for _ in range(10):
        a = 1
        target_slope = random.randint(2, 8) * 2  # Even number for nice x value
        x_val = target_slope // 2
        
        question = f"At what point on y = x² does the tangent have slope {target_slope}?"
        y_val = x_val ** 2
        correct = f"({x_val}, {y_val})"
        distractors = [
            f"({target_slope}, {target_slope**2})",
            f"({x_val}, {target_slope})",
            f"({x_val + 1}, {(x_val+1)**2})"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"dy/dx = 2x = {target_slope}, so x = {x_val}. At x = {x_val}: y = {y_val}. Point is ({x_val}, {y_val})"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_6():
    """Level 6: Rate of Change"""
    questions = []
    
    contexts = [
        ("distance s (metres)", "time t (seconds)", "velocity", "m/s"),
        ("population P (thousands)", "time t (years)", "rate of growth", "thousand/year"),
        ("temperature T (°C)", "time t (minutes)", "rate of cooling", "°C/min"),
        ("profit P (€ thousands)", "units x sold", "marginal profit", "€ thousand/unit"),
        ("height h (metres)", "time t (seconds)", "velocity", "m/s"),
    ]
    
    # Type 1: Interpret derivative as rate of change (20 questions)
    for i in range(20):
        ctx = contexts[i % len(contexts)]
        a = random.randint(1, 3)
        b = random.choice([-1, 1]) * random.randint(1, 5)
        c = random.randint(0, 10)
        t_val = random.randint(1, 4)
        
        # Function: f(t) = at^2 + bt + c
        # Derivative: f'(t) = 2at + b
        rate = 2 * a * t_val + b
        
        poly = format_polynomial([(a, 2), (b, 1), (c, 0)]).replace('x', 't')
        question = f"The {ctx[0]} is given by {ctx[0][0]} = {poly}. Find the {ctx[2]} when t = {t_val}."
        
        correct = f"{rate} {ctx[3]}"
        distractors = [
            f"{a * (t_val**2) + b * t_val + c} {ctx[3]}",
            f"{2 * a * t_val} {ctx[3]}",
            f"{rate + b} {ctx[3]}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"d{ctx[0][0]}/dt = {2*a}t + {b}. At t = {t_val}: rate = {2*a}({t_val}) + {b} = {rate} {ctx[3]}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: When is rate zero? (15 questions)
    for _ in range(15):
        a = random.randint(1, 2)
        b = random.randint(2, 8)
        
        # f(t) = -at^2 + bt + c, f'(t) = -2at + b = 0 when t = b/(2a)
        t_zero = b / (2 * a)
        
        if t_zero == int(t_zero):
            t_zero = int(t_zero)
            poly = f"-{a}t² + {b}t + 5"
            question = f"If the height h (in metres) of a ball is h = {poly}, when is the velocity zero?"
            
            correct = f"t = {t_zero} seconds"
            distractors = [
                f"t = {b} seconds",
                f"t = {2*a} seconds",
                f"t = {t_zero + 1} seconds"
            ]
            
            options, idx = make_unique_options(correct, distractors)
            explanation = f"v = dh/dt = -{2*a}t + {b} = 0. Solving: {2*a}t = {b}, so t = {t_zero} seconds"
            questions.append({
                'question_text': question, 'option_a': options[0], 'option_b': options[1],
                'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
                'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
            })
    
    # Fill remaining with simpler rate questions
    while len(questions) < 50:
        a = random.randint(2, 5)
        t_val = random.randint(1, 4)
        
        question = f"If distance s = {a}t² metres, find the velocity when t = {t_val} seconds."
        velocity = 2 * a * t_val
        
        correct = f"{velocity} m/s"
        distractors = [f"{a * t_val**2} m/s", f"{a * t_val} m/s", f"{2 * a} m/s"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"v = ds/dt = {2*a}t. At t = {t_val}: v = {velocity} m/s"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions[:50]


def generate_level_7():
    """Level 7: Increasing/Decreasing Functions"""
    questions = []
    
    # Type 1: Determine where function is increasing (20 questions)
    count = 0
    attempts = 0
    while count < 20 and attempts < 100:
        attempts += 1
        a = random.choice([-1, 1]) * random.randint(1, 2)
        b = random.choice([-6, -4, -2, 2, 4, 6])
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            b = -b  # Ensure turning point has nice x value
        
        vertex_x = -b / (2 * a)
        
        if vertex_x == int(vertex_x) and vertex_x != 0:
            vertex_x = int(vertex_x)
            
            poly = format_polynomial([(a, 2), (b, 1)])
            question = f"For what values of x is f(x) = {poly} increasing?"
            
            if a > 0:
                correct = f"x > {vertex_x}"
                distractors = [f"x < {vertex_x}", f"x > {-vertex_x}", "all x"]
            else:
                correct = f"x < {vertex_x}"
                distractors = [f"x > {vertex_x}", f"x < {-vertex_x}", "all x"]
            
            options, idx = make_unique_options(correct, distractors)
            explanation = f"f'(x) = {2*a}x + {b}. Function increases where f'(x) > 0: {correct}"
            questions.append({
                'question_text': question, 'option_a': options[0], 'option_b': options[1],
                'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
                'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
            })
            count += 1
    
    # Type 2: Is function increasing at x = a? (20 questions)
    for _ in range(20):
        a = random.randint(1, 2)
        b = random.choice([-1, 1]) * random.randint(1, 4)
        x_val = random.randint(1, 4)
        
        # f(x) = ax^2 + bx, f'(x) = 2ax + b
        deriv_at_x = 2 * a * x_val + b
        
        poly = format_polynomial([(a, 2), (b, 1)])
        question = f"Is f(x) = {poly} increasing or decreasing at x = {x_val}?"
        
        if deriv_at_x > 0:
            correct = f"Increasing (f'({x_val}) = {deriv_at_x} > 0)"
        elif deriv_at_x < 0:
            correct = f"Decreasing (f'({x_val}) = {deriv_at_x} < 0)"
        else:
            correct = f"Neither (f'({x_val}) = 0)"
        
        distractors = [
            f"Increasing (f'({x_val}) = {abs(deriv_at_x)})",
            f"Decreasing (f'({x_val}) = {-deriv_at_x})",
            "Cannot determine"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"f'(x) = {2*a}x + {b}. At x = {x_val}: f'({x_val}) = {deriv_at_x}. Since {deriv_at_x} {'>' if deriv_at_x > 0 else '<' if deriv_at_x < 0 else '='} 0, function is {'increasing' if deriv_at_x > 0 else 'decreasing' if deriv_at_x < 0 else 'stationary'}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: From graph - identify where increasing (fill to 50)
    while len(questions) < 50:
        scenario_num = len(questions) % 5
        scenarios = [
            ("At point P where the curve is going upward (positive slope)", "f'(x) > 0", "f'(x) < 0"),
            ("At point Q where the curve is going downward (negative slope)", "f'(x) < 0", "f'(x) > 0"),
            ("At a maximum point", "f'(x) = 0", "f'(x) > 0"),
            ("At a minimum point", "f'(x) = 0", "f'(x) < 0"),
            ("Where the tangent is horizontal", "f'(x) = 0", "f'(x) = 1"),
        ]
        scenario, answer, wrong1 = scenarios[scenario_num]
        question = f"On a graph of y = f(x), what is true about the derivative {scenario}?"
        
        correct = answer
        distractors = [wrong1, "f(x) = 0", "f'(x) = f(x)"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"When curve goes up, f'(x) > 0. When down, f'(x) < 0. At turning points, f'(x) = 0."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_8():
    """Level 8: Max & Min Values"""
    questions = []
    
    # Type 1: Find turning point x-value (20 questions)
    count = 0
    attempts = 0
    while count < 20 and attempts < 100:
        attempts += 1
        a = random.choice([-1, 1]) * random.randint(1, 2)
        b = random.choice([2, 4, 6, 8, -2, -4, -6, -8])
        c = random.randint(0, 10)
        
        x_turn = -b / (2 * a)
        
        if x_turn == int(x_turn) and x_turn > 0:
            x_turn = int(x_turn)
            
            poly = format_polynomial([(a, 2), (b, 1), (c, 0)])
            turn_type = "minimum" if a > 0 else "maximum"
            
            question = f"Find the x-value where f(x) = {poly} has a {turn_type}."
            
            correct = f"x = {x_turn}"
            distractors = [f"x = {-x_turn}", f"x = {abs(b)}", f"x = {x_turn + 1}"]
            
            options, idx = make_unique_options(correct, distractors)
            explanation = f"f'(x) = {2*a}x + {b} = 0. Solving: x = -{b}/{2*a} = {x_turn}"
            questions.append({
                'question_text': question, 'option_a': options[0], 'option_b': options[1],
                'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
                'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
            })
            count += 1
    
    # Type 2: Find the maximum/minimum value (20 questions)
    for _ in range(20):
        a = random.choice([-1, 1])
        b = random.randint(2, 6) * 2  # Even for nice division
        c = random.randint(0, 10)
        
        x_turn = -b // (2 * a)
        y_turn = a * (x_turn ** 2) + b * x_turn + c
        
        poly = format_polynomial([(a, 2), (b, 1), (c, 0)])
        turn_type = "minimum" if a > 0 else "maximum"
        
        question = f"Find the {turn_type} value of f(x) = {poly}."
        
        correct = str(y_turn)
        distractors = [str(x_turn), str(y_turn + a), str(c)]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"f'(x) = {2*a}x + {b} = 0 gives x = {x_turn}. {turn_type.title()} value = f({x_turn}) = {y_turn}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Identify max or min (fill remaining to 50)
    while len(questions) < 50:
        a = random.choice([-1, 1]) * random.randint(1, 2)
        b = random.randint(2, 8)
        
        poly = format_polynomial([(a, 2), (b, 1), (5, 0)])
        
        question = f"Does f(x) = {poly} have a maximum or minimum turning point?"
        
        if a > 0:
            correct = "Minimum (coefficient of x² is positive)"
            distractors = ["Maximum (coefficient of x² is positive)", "Maximum (coefficient of x² is negative)", "Neither"]
        else:
            correct = "Maximum (coefficient of x² is negative)"
            distractors = ["Minimum (coefficient of x² is negative)", "Minimum (coefficient of x² is positive)", "Neither"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"When a {'>' if a > 0 else '<'} 0, the parabola opens {'upward (minimum)' if a > 0 else 'downward (maximum)'}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_9():
    """Level 9: Second Derivative"""
    questions = []
    
    # Type 1: Find second derivative (25 questions)
    for _ in range(25):
        a = random.randint(1, 3)
        b = random.choice([-1, 1]) * random.randint(1, 6)
        c = random.randint(1, 5)
        
        # f(x) = ax^3 + bx^2 + cx
        # f'(x) = 3ax^2 + 2bx + c
        # f''(x) = 6ax + 2b
        
        poly = format_polynomial([(a, 3), (b, 2), (c, 1)])
        question = f"If f(x) = {poly}, find f''(x)."
        
        correct = f"{6*a}x + {2*b}" if 2*b >= 0 else f"{6*a}x - {abs(2*b)}"
        distractors = [
            f"{3*a}x² + {2*b}x",
            f"{6*a}x + {b}",
            f"{a}x + {2*b}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"f'(x) = {3*a}x² + {2*b}x + {c}. f''(x) = {6*a}x + {2*b}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Second derivative test (15 questions)
    for _ in range(15):
        a = random.choice([-1, 1]) * random.randint(1, 2)
        b = random.randint(2, 8)
        x_turn = -b // (2 * a)
        
        poly = format_polynomial([(a, 2), (b, 1), (5, 0)])
        question = f"Use the second derivative test to classify the turning point of f(x) = {poly}."
        
        f_double_prime = 2 * a
        
        if f_double_prime > 0:
            correct = f"Minimum (f''(x) = {f_double_prime} > 0)"
            distractors = [f"Maximum (f''(x) = {f_double_prime})", "Point of inflection", f"Minimum (f''(x) = {-f_double_prime})"]
        else:
            correct = f"Maximum (f''(x) = {f_double_prime} < 0)"
            distractors = [f"Minimum (f''(x) = {f_double_prime})", "Point of inflection", f"Maximum (f''(x) = {-f_double_prime})"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"f''(x) = {f_double_prime}. Since f''(x) {'>' if f_double_prime > 0 else '<'} 0, turning point is a {'minimum' if f_double_prime > 0 else 'maximum'}."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Evaluate second derivative at a point (10 questions)
    for _ in range(10):
        a = random.randint(1, 2)
        b = random.choice([-1, 1]) * random.randint(1, 4)
        x_val = random.randint(1, 3)
        
        # f(x) = ax^3 + bx^2
        # f''(x) = 6ax + 2b
        f_double_prime_at_x = 6 * a * x_val + 2 * b
        
        poly = format_polynomial([(a, 3), (b, 2)])
        question = f"Find f''({x_val}) for f(x) = {poly}."
        
        correct = str(f_double_prime_at_x)
        distractors = [str(6*a*x_val), str(f_double_prime_at_x + 2*b), str(3*a*(x_val**2) + 2*b*x_val)]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"f''(x) = {6*a}x + {2*b}. At x = {x_val}: f''({x_val}) = {6*a}({x_val}) + {2*b} = {f_double_prime_at_x}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_10():
    """Level 10: Applied Max/Min - Profit, Cost, Revenue"""
    questions = []
    
    # Type 1: Profit maximization (20 questions)
    for _ in range(20):
        a = random.randint(1, 2)
        b = random.randint(10, 30)
        c = random.randint(50, 100)
        
        # P(x) = -ax^2 + bx - c
        # P'(x) = -2ax + b = 0 → x = b/(2a)
        x_max = b // (2 * a)
        max_profit = -a * (x_max ** 2) + b * x_max - c
        
        question = f"A company's profit P (in €thousands) for producing x units is P(x) = -{a}x² + {b}x - {c}. How many units maximise profit?"
        
        correct = f"{x_max} units"
        distractors = [f"{b} units", f"{x_max + a} units", f"{2*a} units"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"P'(x) = -{2*a}x + {b} = 0. Solving: x = {b}/{2*a} = {x_max} units"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Find maximum profit value (15 questions)
    for _ in range(15):
        a = 1
        b = random.randint(6, 12) * 2  # Even for nice division
        c = random.randint(10, 30)
        
        x_max = b // 2
        max_profit = -x_max**2 + b*x_max - c
        
        question = f"If profit P(x) = -x² + {b}x - {c} (€thousands), find the maximum profit."
        
        correct = f"€{max_profit},000"
        distractors = [f"€{x_max},000", f"€{max_profit + c},000", f"€{b},000"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"P'(x) = -2x + {b} = 0 gives x = {x_max}. Max profit = P({x_max}) = -{x_max}² + {b}({x_max}) - {c} = €{max_profit},000"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Cost minimization (15 questions)
    for _ in range(15):
        a = random.randint(1, 2)
        b = random.randint(8, 16)
        c = random.randint(50, 100)
        
        # C(x) = ax^2 - bx + c
        x_min = b // (2 * a)
        min_cost = a * (x_min ** 2) - b * x_min + c
        
        question = f"Production cost C(x) = {a}x² - {b}x + {c} (€). Find x for minimum cost."
        
        correct = f"x = {x_min}"
        distractors = [f"x = {b}", f"x = {x_min + 2}", f"x = {2*a}"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"C'(x) = {2*a}x - {b} = 0. Solving: x = {b}/{2*a} = {x_min}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_11():
    """Level 11: Optimization Problems - Area, Volume"""
    questions = []
    
    # Type 1: Maximize area with fixed perimeter (20 questions)
    for _ in range(20):
        perimeter = random.randint(20, 50) * 2  # Even perimeter for nice numbers
        
        # Rectangle with perimeter P: 2l + 2w = P, so w = (P-2l)/2 = P/2 - l
        # Area A = l × w = l(P/2 - l) = (P/2)l - l²
        # dA/dl = P/2 - 2l = 0 → l = P/4
        # Maximum area when l = w = P/4 (square)
        
        optimal_side = perimeter // 4
        max_area = optimal_side ** 2
        
        question = f"A rectangle has perimeter {perimeter} cm. Find the length that maximises the area."
        
        correct = f"{optimal_side} cm"
        distractors = [f"{perimeter // 2} cm", f"{optimal_side + 5} cm", f"{perimeter} cm"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Let length = l. Width = ({perimeter} - 2l)/2 = {perimeter//2} - l. Area A = l({perimeter//2} - l). dA/dl = {perimeter//2} - 2l = 0 gives l = {optimal_side} cm"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Find maximum area value (15 questions)
    for _ in range(15):
        perimeter = random.randint(10, 25) * 4  # Multiple of 4 for nice numbers
        
        optimal_side = perimeter // 4
        max_area = optimal_side ** 2
        
        question = f"A rectangle has perimeter {perimeter} cm. What is the maximum possible area?"
        
        correct = f"{max_area} cm²"
        distractors = [f"{perimeter * optimal_side} cm²", f"{max_area + optimal_side} cm²", f"{optimal_side * 2} cm²"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Maximum area is a square with side {perimeter}/4 = {optimal_side} cm. Area = {optimal_side}² = {max_area} cm²"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Simple box optimization (fill to 50)
    while len(questions) < 50:
        side = random.choice([12, 18, 24, 30])
        x_opt = side // 6
        
        question = f"A box is made from a {side}cm × {side}cm sheet by cutting squares of side x from corners. Given that the optimal x is found by solving dV/dx = 0, what is x for maximum volume?"
        
        correct = f"{x_opt} cm"
        distractors = [f"{side // 4} cm", f"{x_opt + 2} cm", f"{side // 2} cm"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"For this box problem, the optimal cut size x = {side}/6 = {x_opt} cm gives maximum volume."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_12():
    """Level 12: Mastery Challenge - Mixed Problems"""
    questions = []
    
    # Mix of all previous types at higher difficulty
    
    # Type 1: Multi-step tangent problems (10 questions)
    for _ in range(10):
        a = random.randint(1, 2)
        b = random.choice([-1, 1]) * random.randint(1, 4)
        x1 = random.randint(1, 3)
        
        # y = ax^3 + bx
        y1 = a * (x1 ** 3) + b * x1
        slope = 3 * a * (x1 ** 2) + b
        
        poly = format_polynomial([(a, 3), (b, 1)])
        question = f"Find the slope of the tangent to y = {poly} at the point where x = {x1}."
        
        correct = str(slope)
        distractors = [str(y1), str(3*a*(x1**2)), str(slope + b)]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"dy/dx = {3*a}x² + {b}. At x = {x1}: slope = {3*a}({x1})² + {b} = {slope}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Interpret derivative from context (10 questions)
    for _ in range(10):
        rate = random.randint(5, 20)
        
        contexts = [
            (f"If s'(3) = {rate}", "distance s metres at time t seconds", f"velocity is {rate} m/s at t = 3"),
            (f"If P'(100) = {rate}", "profit P euros for x items sold", f"marginal profit is €{rate} per item when 100 sold"),
            (f"If T'(5) = -{rate}", "temperature T°C at time t minutes", f"temperature decreasing at {rate}°C/min at t = 5"),
            (f"If h'(2) = 0", "height h metres at time t seconds", "velocity is 0 at t = 2 (maximum height)"),
        ]
        
        given, context, meaning = random.choice(contexts)
        
        question = f"{given}, where {context}. What does this mean?"
        correct = meaning.capitalize()
        
        distractors = [
            "Cannot determine",
            f"The {context.split()[0]} is constant",
            f"Maximum occurs at this point"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"The derivative represents rate of change. {correct}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Complete optimization (15 questions)
    for _ in range(15):
        a = random.randint(1, 2)
        b = random.randint(10, 20)
        
        x_opt = b // (2 * a)
        
        question = f"Revenue R(x) = -{a}x² + {b}x. Find both the optimal x and maximum revenue."
        
        max_rev = -a * (x_opt ** 2) + b * x_opt
        
        correct = f"x = {x_opt}, R = {max_rev}"
        distractors = [
            f"x = {b}, R = {b**2}",
            f"x = {x_opt}, R = {x_opt * b}",
            f"x = {2*a}, R = {max_rev + a}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"R'(x) = -{2*a}x + {b} = 0 gives x = {x_opt}. R({x_opt}) = -{a}({x_opt})² + {b}({x_opt}) = {max_rev}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Challenging polynomial derivatives (15 questions)
    for _ in range(15):
        a = random.randint(1, 2)
        b = random.choice([-1, 1]) * random.randint(1, 3)
        c = random.choice([-1, 1]) * random.randint(1, 5)
        d = random.randint(1, 10)
        
        poly = format_polynomial([(a, 3), (b, 2), (c, 1), (d, 0)])
        
        question = f"Find f'(x) for f(x) = {poly}."
        
        correct = format_polynomial([(3*a, 2), (2*b, 1), (c, 0)])
        distractors = [
            format_polynomial([(a, 2), (b, 1), (c, 0)]),
            format_polynomial([(3*a, 3), (2*b, 2), (c, 1)]),
            format_polynomial([(3*a, 2), (2*b, 1)])
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Apply power rule to each term: f'(x) = {correct}"
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
    
    # Create complete SQL file with strand and topic creation
    complete_sql = f"""-- LC Ordinary Level - Calculus (Differentiation) Complete SQL
-- Generated: 2025-12-15
-- Total: {len(all_questions)} questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order, is_visible)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50, 1);

-- Add Calculus topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT '{TOPIC}', 'Calculus', id, '📐', 1, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = '{TOPIC}';

-- Insert questions
{chr(10).join(sql_statements)}

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = '{TOPIC}';
"""
    
    # Write to file
    with open('lc_ol_calculus_complete.sql', 'w', encoding='utf-8') as f:
        f.write(complete_sql)
    print(f"\nSQL written to: lc_ol_calculus_complete.sql")
    
    return all_questions


if __name__ == '__main__':
    main()
