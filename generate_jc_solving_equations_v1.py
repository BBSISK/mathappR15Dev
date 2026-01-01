#!/usr/bin/env python3
"""
AgentMath - Solving Equations Topic Generator v1
SEC Junior Cycle Mathematics - Adaptive Quiz System

Generates 600 questions (50 per level x 12 levels) for the Solving Equations topic.
Aligned with SEC Junior Cycle Mathematics Specification.

Level Structure:
  Level 1:  One-Step Equations - Addition/Subtraction (Foundation)
  Level 2:  One-Step Equations - Multiplication/Division (Foundation)
  Level 3:  Two-Step Equations (Foundation)
  Level 4:  Equations with Negatives (Ordinary)
  Level 5:  Variables on Both Sides (Ordinary)
  Level 6:  Equations with Brackets (Ordinary)
  Level 7:  Equations with Fractions (Higher)
  Level 8:  Forming Equations from Words (Higher)
  Level 9:  Simultaneous Equations - Elimination (Higher)
  Level 10: Simultaneous Equations - Substitution (Higher)
  Level 11: Quadratic Equations (Higher)
  Level 12: Problem Solving & Applications (Mastery)

SEC Reference Questions:
  - 2022 OL Q13(b): f(x) = 2x - 1, find x if f(x) = 9 (solve 2x - 1 = 9)
  - 2023 OL Q8: Solve 3x + 5 = 20
  - 2024 OL Q7: Solve 2(x + 4) = 18
  - 2024 HL Q12: Solve quadratic equation
  - 2022 HL Q8: Simultaneous equations
  - 2025 OL Q7: Form and solve equation from word problem

Author: AgentMath Generator
Version: 1.0
"""

import random
import sqlite3
import os

TOPIC = 'solving_equations'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50

IRISH_NAMES = ['Aoife', 'Ciara', 'Niamh', 'Saoirse', 'Orla', 'Siobhan', 'Aisling', 'Roisin',
               'Cian', 'Sean', 'Oisin', 'Conor', 'Liam', 'Darragh', 'Fionn', 'Eoin']

def generate_balance_svg(left_expr, right_expr):
    """Generate a balance/scales visual for equations"""
    svg = f'''<svg viewBox="0 0 280 100" width="280">
        <line x1="40" y1="60" x2="240" y2="60" stroke="#6b7280" stroke-width="3"/>
        <polygon points="140,60 130,90 150,90" fill="#6b7280"/>
        <line x1="140" y1="90" x2="140" y2="100" stroke="#6b7280" stroke-width="4"/>
        <ellipse cx="70" cy="60" rx="50" ry="8" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/>
        <text x="70" y="45" text-anchor="middle" font-size="14" fill="#1e40af" font-weight="bold">{left_expr}</text>
        <ellipse cx="210" cy="60" rx="50" ry="8" fill="#bbf7d0" stroke="#22c55e" stroke-width="2"/>
        <text x="210" y="45" text-anchor="middle" font-size="14" fill="#166534" font-weight="bold">{right_expr}</text>
        <text x="140" y="45" text-anchor="middle" font-size="16" fill="#374151">=</text>
    </svg>'''
    return svg

def generate_word_problem_svg(context, equation):
    """Generate visual for word problems"""
    svg = f'''<svg viewBox="0 0 280 70" width="280">
        <rect x="5" y="5" width="270" height="60" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
        <text x="140" y="25" text-anchor="middle" font-size="11" fill="#92400e">{context}</text>
        <text x="140" y="50" text-anchor="middle" font-size="13" fill="#1e40af" font-weight="bold">Equation: {equation}</text>
    </svg>'''
    return svg

def generate_simultaneous_svg(eq1, eq2):
    """Generate visual for simultaneous equations"""
    svg = f'''<svg viewBox="0 0 200 70" width="200">
        <text x="20" y="25" font-size="14" fill="#3b82f6" font-weight="bold">{eq1}</text>
        <text x="20" y="50" font-size="14" fill="#8b5cf6" font-weight="bold">{eq2}</text>
        <line x1="10" y1="5" x2="10" y2="60" stroke="#6b7280" stroke-width="2"/>
    </svg>'''
    return svg

def generate_quadratic_svg(equation):
    """Generate visual for quadratic equation"""
    svg = f'''<svg viewBox="0 0 250 50" width="250">
        <rect x="5" y="5" width="240" height="40" rx="5" fill="#ede9fe" stroke="#8b5cf6" stroke-width="2"/>
        <text x="125" y="32" text-anchor="middle" font-size="14" fill="#5b21b6" font-weight="bold">{equation}</text>
    </svg>'''
    return svg

def generate_level_1(num_questions=50):
    """Level 1: One-Step Equations - Addition/Subtraction"""
    questions = []
    used_questions = set()
    
    templates = [
        ("x + {b} = {c}", "add"),
        ("x - {b} = {c}", "sub"),
        ("{b} + x = {c}", "add"),
        ("{c} = x + {b}", "add"),
        ("{c} = x - {b}", "sub"),
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        template, op_type = random.choice(templates)
        
        x = random.randint(1, 20)
        b = random.randint(2, 15)
        
        if op_type == "add":
            c = x + b
        else:
            c = x - b
            if c < 0:
                continue
        
        equation = template.format(b=b, c=c)
        question_text = f"Solve: {equation}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {x + b, abs(c - b) if c != b else c + 1, c, b}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 25)
            if wrong != x and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        if op_type == "add":
            explanation = f"To solve {equation}:\\nSubtract {b} from both sides:\\nx = {c} - {b} = {x}"
        else:
            explanation = f"To solve {equation}:\\nAdd {b} to both sides:\\nx = {c} + {b} = {x}"
        
        visual = generate_balance_svg(equation.split('=')[0].strip(), equation.split('=')[1].strip())
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_2(num_questions=50):
    """Level 2: One-Step Equations - Multiplication/Division"""
    questions = []
    used_questions = set()
    
    templates = [("{a}x = {c}", "mult"), ("x/{a} = {c}", "div"), ("{c} = {a}x", "mult")]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        template, op_type = random.choice(templates)
        
        if op_type == "mult":
            x = random.randint(2, 12)
            a = random.randint(2, 10)
            c = a * x
        else:
            a = random.randint(2, 8)
            c = random.randint(2, 10)
            x = a * c
        
        equation = template.format(a=a, c=c)
        question_text = f"Solve: {equation}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {c * a if op_type == "mult" else c, c + a, abs(c - a) if c != a else c + 2, a}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(2, 50)
            if wrong != x and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        if op_type == "mult":
            explanation = f"To solve {equation}:\\nDivide both sides by {a}:\\nx = {c} / {a} = {x}"
        else:
            explanation = f"To solve {equation}:\\nMultiply both sides by {a}:\\nx = {c} x {a} = {x}"
        
        visual = generate_balance_svg(equation.split('=')[0].strip(), equation.split('=')[1].strip())
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_3(num_questions=50):
    """Level 3: Two-Step Equations"""
    questions = []
    used_questions = set()
    templates = ["{a}x + {b} = {c}", "{a}x - {b} = {c}", "{b} + {a}x = {c}"]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        template = random.choice(templates)
        
        x = random.randint(1, 10)
        a = random.randint(2, 6)
        b = random.randint(1, 10)
        
        if '-' in template:
            c = a * x - b
            if c < 0:
                continue
        else:
            c = a * x + b
        
        equation = template.format(a=a, b=b, c=c)
        question_text = f"Solve: {equation}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {c // a if a != 0 else 1, (c + b) // a if a != 0 else 1, x + 1, x - 1 if x > 1 else x + 2}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 15)
            if wrong != x and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        explanation = f"To solve {equation}:\\nStep 1: Isolate the x term\\nStep 2: Divide to find x = {x}"
        visual = generate_balance_svg(f"{a}x", str(c))
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_4(num_questions=50):
    """Level 4: Equations with Negatives"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        x = random.randint(1, 8)
        a = random.randint(2, 5)
        b = random.randint(1, 12)
        
        eq_type = random.choice([1, 2, 3])
        if eq_type == 1:
            c = -a * x + b
            equation = f"-{a}x + {b} = {c}"
        elif eq_type == 2:
            c = -a * x
            equation = f"-{a}x = {c}"
        else:
            c = b - a * x
            equation = f"{b} - {a}x = {c}"
        
        question_text = f"Solve: {equation}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {-x, x + 1, x - 1 if x > 1 else x + 2, abs(c) // a if a != 0 else 1}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w != 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(-10, 10)
            if wrong != x and wrong != 0 and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        explanation = f"To solve {equation}:\\nRemember: negative / negative = positive\\nx = {x}"
        visual = generate_balance_svg(equation.split('=')[0].strip(), equation.split('=')[1].strip())
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_5(num_questions=50):
    """Level 5: Variables on Both Sides"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        x = random.randint(1, 10)
        a = random.randint(3, 8)
        c = random.randint(1, a - 1)
        b = random.randint(1, 15)
        d = a * x + b - c * x
        
        if d < 0:
            continue
        
        equation = f"{a}x + {b} = {c}x + {d}"
        question_text = f"Solve: {equation}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {x + 1, x - 1 if x > 1 else x + 2, (b + d) // (a + c) if (a + c) != 0 else x + 1, b - d if b != d else b + 1}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 15)
            if wrong != x and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        coeff_diff = a - c
        explanation = f"To solve {equation}:\\nCollect x terms: {coeff_diff}x = {d - b}\\nx = {x}"
        visual = generate_balance_svg(f"{a}x + {b}", f"{c}x + {d}")
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_6(num_questions=50):
    """Level 6: Equations with Brackets"""
    questions = []
    used_questions = set()
    templates = ["{a}(x + {b}) = {c}", "{a}(x - {b}) = {c}", "2(x + {b}) + {d} = {c}"]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        template = random.choice(templates)
        
        x = random.randint(1, 10)
        a = random.randint(2, 5)
        b = random.randint(1, 8)
        d = random.randint(1, 5)
        
        if template == "{a}(x + {b}) = {c}":
            c = a * (x + b)
        elif template == "{a}(x - {b}) = {c}":
            c = a * (x - b)
            if c < 0:
                continue
        else:
            c = 2 * (x + b) + d
        
        equation = template.format(a=a, b=b, c=c, d=d)
        question_text = f"Solve: {equation}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {c // a if a != 0 else 1, x + b, x + 1, x - 1 if x > 1 else x + 2}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 20)
            if wrong != x and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        explanation = f"To solve {equation}:\\nStep 1: Expand brackets\\nStep 2: Collect terms and solve\\nx = {x}"
        visual = generate_balance_svg(equation.split('=')[0].strip(), str(c))
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_7(num_questions=50):
    """Level 7: Equations with Fractions"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        
        frac_type = random.choice([1, 2, 3])
        if frac_type == 1:
            x = a * random.randint(1, 6)
            c = x // a + b
            equation = f"x/{a} + {b} = {c}"
        elif frac_type == 2:
            result = random.randint(2, 8)
            c = result
            x = a * result - b
            if x < 1:
                continue
            equation = f"(x + {b})/{a} = {c}"
        else:
            x = a * random.randint(2, 8)
            c = x // a
            equation = f"x/{a} = {c}"
        
        question_text = f"Solve: {equation}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {a * c, c - b if c > b else c + b, x + a, x - a if x > a else x + 1}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 30)
            if wrong != x and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        explanation = f"To solve {equation}:\\nMultiply both sides by {a} to clear the fraction.\\nx = {x}"
        visual = generate_balance_svg(equation.split('=')[0].strip(), str(c))
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_8(num_questions=50):
    """Level 8: Forming Equations from Words"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        problem_type = random.choice([1, 2, 3, 4])
        name = random.choice(IRISH_NAMES)
        
        if problem_type == 1:
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            x = random.randint(2, 12)
            c = a * x + b
            question_text = f"{name} thinks of a number, multiplies it by {a}, then adds {b}. The answer is {c}. What was the number?"
            equation = f"{a}x + {b} = {c}"
            answer = x
        elif problem_type == 2:
            x = random.randint(5, 30)
            total = x + (x + 1) + (x + 2)
            question_text = f"The sum of three consecutive numbers is {total}. Find the smallest number."
            equation = f"x + (x+1) + (x+2) = {total}"
            answer = x
        elif problem_type == 3:
            a = random.choice([5, 6, 7, 8, 10, 12])
            x = random.randint(2, 8)
            b = random.randint(2, 10)
            total = a * x + b
            question_text = f"{name} has {total} euro to spend. Each book costs {a} euro. After buying some books, {name} has {b} euro left. How many books?"
            equation = f"{a}x + {b} = {total}"
            answer = x
        else:
            x = random.randint(3, 15)
            a = random.randint(2, 8)
            p = 2 * (x + x + a)
            question_text = f"A rectangle has length {a} cm more than its width. The perimeter is {p} cm. Find the width."
            equation = f"2(x + x + {a}) = {p}"
            answer = x
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {answer + 1, answer - 1 if answer > 1 else answer + 2, answer + 2, answer * 2 if answer * 2 < 100 else answer + 3}
        wrong_set.discard(answer)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 50)
            if wrong != answer and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(answer)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(answer))
        
        explanation = f"Form equation: {equation}\\nSolve to find answer = {answer}"
        visual = generate_word_problem_svg("Word Problem", equation)
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_9(num_questions=50):
    """Level 9: Simultaneous Equations - Elimination"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        
        a1, b1 = random.randint(1, 4), random.randint(1, 4)
        a2, b2 = random.randint(1, 4), random.randint(1, 4)
        
        if a1 * b2 == a2 * b1:
            continue
        
        c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
        eq1, eq2 = f"{a1}x + {b1}y = {c1}", f"{a2}x + {b2}y = {c2}"
        
        question_text = f"Solve the simultaneous equations:\\n{eq1}\\n{eq2}\\nFind the value of x."
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {y, x + 1, x - 1 if x > 1 else x + 2, x + y}
        wrong_set.discard(x)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 12)
            if wrong != x and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(x)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(x))
        
        explanation = f"Using elimination method:\\nx = {x}, y = {y}"
        visual = generate_simultaneous_svg(eq1, eq2)
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_10(num_questions=50):
    """Level 10: Simultaneous Equations - Substitution"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        
        m = random.choice([1, 2, 3])
        c = y - m * x
        
        if c >= 0:
            eq1 = f"y = {m}x + {c}" if m != 1 else f"y = x + {c}"
        else:
            eq1 = f"y = {m}x - {abs(c)}" if m != 1 else f"y = x - {abs(c)}"
        
        a, b = random.randint(1, 3), random.randint(1, 3)
        d = a * x + b * y
        eq2 = f"{a}x + {b}y = {d}"
        
        question_text = f"Solve by substitution:\\n{eq1}\\n{eq2}\\nFind the value of y."
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {x, y + 1, y - 1 if y > 1 else y + 2, abs(c)}
        wrong_set.discard(y)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 15)
            if wrong != y and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(y)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(y))
        
        explanation = f"Substitution method:\\nx = {x}, y = {y}"
        visual = generate_simultaneous_svg(eq1, eq2)
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_11(num_questions=50):
    """Level 11: Quadratic Equations"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        r1 = random.randint(-8, 8)
        r2 = random.randint(-8, 8)
        if r1 == 0 and r2 == 0:
            continue
        
        b = -(r1 + r2)
        c = r1 * r2
        
        b_str = f"+ {b}x" if b > 0 else (f"- {abs(b)}x" if b < 0 else "")
        c_str = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
        equation = f"x^2 {b_str} {c_str} = 0".replace("  ", " ").strip()
        
        ask_type = random.choice(["positive", "larger", "smaller"])
        roots = sorted([r1, r2])
        
        if ask_type == "positive":
            if max(r1, r2) <= 0:
                continue
            answer = max(r1, r2)
            question_text = f"Solve: {equation}\\nGive the positive solution."
        elif ask_type == "larger":
            answer = roots[1]
            question_text = f"Solve: {equation}\\nGive the larger solution."
        else:
            answer = roots[0]
            question_text = f"Solve: {equation}\\nGive the smaller solution."
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        other_root = r2 if answer == r1 else r1
        wrong_set = {other_root, answer + 1, answer - 1, -answer if answer != 0 else 1, abs(b), abs(c)}
        wrong_set.discard(answer)
        wrong_options = list(wrong_set)[:3]
        while len(wrong_options) < 3:
            wrong = random.randint(-10, 10)
            if wrong != answer and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(answer)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(answer))
        
        explanation = f"Factorise: (x - {r1})(x - {r2}) = 0\\nSolutions: x = {r1} or x = {r2}\\nAnswer: {answer}"
        visual = generate_quadratic_svg(equation)
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_level_12(num_questions=50):
    """Level 12: Problem Solving & Applications"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 5:
        attempts += 1
        
        problem_type = random.choice([1, 2, 3, 4])
        name = random.choice(IRISH_NAMES)
        
        if problem_type == 1:
            x = random.randint(3, 10)
            extra = random.randint(2, 6)
            area = x * (x + extra)
            question_text = f"A rectangle has width x m and length (x + {extra}) m. If the area is {area} m^2, find x."
            equation = f"x(x + {extra}) = {area}"
            answer = x
        elif problem_type == 2:
            n = random.randint(3, 8)
            diff = (n + 1) ** 2 - n ** 2
            question_text = f"Two consecutive positive integers have squares that differ by {diff}. Find the smaller integer."
            equation = f"(n+1)^2 - n^2 = {diff}"
            answer = n
        elif problem_type == 3:
            speed = random.randint(40, 80)
            time = random.randint(2, 5)
            distance = speed * time
            question_text = f"A car travels {distance} km at a constant speed. If the journey takes {time} hours, find the speed in km/h."
            equation = f"speed x {time} = {distance}"
            answer = speed
        else:
            cost = random.randint(10, 50)
            num_items = random.randint(5, 15)
            profit_per_item = random.randint(2, 8)
            total_profit = num_items * profit_per_item
            selling_price = cost + profit_per_item
            question_text = f"Items bought for {cost} euro each are sold for {selling_price} euro each. If total profit is {total_profit} euro, how many items sold?"
            equation = f"{profit_per_item}x = {total_profit}"
            answer = num_items
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        wrong_set = {answer + 1, answer - 1 if answer > 1 else answer + 2, answer + 2, answer * 2 if answer * 2 < 200 else answer + 5}
        wrong_set.discard(answer)
        wrong_options = [w for w in wrong_set if w > 0][:3]
        while len(wrong_options) < 3:
            wrong = random.randint(1, 100)
            if wrong != answer and wrong not in wrong_options:
                wrong_options.append(wrong)
        
        options = [str(answer)] + [str(w) for w in wrong_options[:3]]
        random.shuffle(options)
        correct_idx = options.index(str(answer))
        
        explanation = f"Form equation: {equation}\\nSolve to find answer = {answer}"
        visual = generate_word_problem_svg("Problem Solving", equation)
        
        questions.append({
            'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'image_svg': visual
        })
    
    return questions

def generate_all_questions():
    """Generate all questions for all levels"""
    all_questions = []
    
    generators = [
        (1, generate_level_1, "One-Step: Add/Sub"),
        (2, generate_level_2, "One-Step: Mult/Div"),
        (3, generate_level_3, "Two-Step Equations"),
        (4, generate_level_4, "Equations with Negatives"),
        (5, generate_level_5, "Variables on Both Sides"),
        (6, generate_level_6, "Equations with Brackets"),
        (7, generate_level_7, "Equations with Fractions"),
        (8, generate_level_8, "Forming Equations"),
        (9, generate_level_9, "Simultaneous - Elimination"),
        (10, generate_level_10, "Simultaneous - Substitution"),
        (11, generate_level_11, "Quadratic Equations"),
        (12, generate_level_12, "Problem Solving"),
    ]
    
    for level, generator, name in generators:
        print(f"Generating Level {level}...")
        questions = generator(QUESTIONS_PER_LEVEL)
        
        if level <= 3:
            band = "foundation"
        elif level <= 6:
            band = "ordinary"
        elif level <= 9:
            band = "higher"
        else:
            band = "mastery"
        
        for q in questions:
            q['topic'] = TOPIC
            q['difficulty'] = level
            q['difficulty_band'] = band
            q['mode'] = MODE
        
        all_questions.extend(questions)
    
    return all_questions

def validate_questions(questions):
    """Validate all generated questions"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    errors = []
    level_counts = {}
    level_visuals = {}
    
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if q.get('image_svg'):
            level_visuals[level] = level_visuals.get(level, 0) + 1
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options")
        
        if not q.get('explanation'):
            errors.append(f"Level {level}: Missing explanation")
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual_count = level_visuals.get(level, 0)
        visual_pct = (visual_count / count * 100) if count > 0 else 0
        bar = "█" * (count // 2) + "░" * ((50 - count) // 2) if count > 0 else ""
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: [{bar[:20]}] {count}/{QUESTIONS_PER_LEVEL} | Visual: {visual_pct:.1f}% | {status}")
    
    print("=" * 60)
    print(f"Total Errors: {len(errors)}")
    print("=" * 60)
    
    return len(errors) == 0

def test_single_insert(db_path):
    """
    ⚠️ MANDATORY: Test inserting ONE question before bulk insert.
    This catches column name mismatches, missing columns, etc.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    test_sql = """
        INSERT INTO questions_adaptive 
        (question_text, option_a, option_b, option_c, option_d,
         correct_answer, topic, difficulty_level, difficulty_band, 
         mode, explanation, image_svg, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
    """
    
    try:
        cursor.execute(test_sql, (
            "TEST_QUESTION_DELETE_ME", "A", "B", "C", "D",
            0, "test_topic", 1, "foundation", "jc_exam", "Test", None
        ))
        cursor.execute("DELETE FROM questions_adaptive WHERE question_text = 'TEST_QUESTION_DELETE_ME'")
        conn.commit()
        conn.close()
        print("✓ Database schema validated - test insert successful")
        return True
    except Exception as e:
        conn.close()
        print(f"✗ DATABASE SCHEMA ERROR: {e}")
        print("  Check column names match questions_adaptive table!")
        return False

def insert_into_database(questions):
    """Insert questions into the database"""
    db_path = 'instance/mathquiz.db'
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return False
    
    # ⚠️ MANDATORY: Test single insert first to catch schema errors
    if not test_single_insert(db_path):
        print("ABORTING: Fix schema errors before bulk insert!")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    print(f"Deleted existing {TOPIC} questions")
    
    inserted = 0
    errors = 0
    
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (question_text, option_a, option_b, option_c, option_d,
                 correct_answer, topic, difficulty_level, difficulty_band,
                 mode, explanation, image_svg, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['question_text'],
                q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'], q['explanation'], q.get('image_svg', ''), 1
            ))
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"\nInserted {inserted} questions, {errors} errors")
    return errors == 0

if __name__ == "__main__":
    print("=" * 60)
    print("AgentMath - Solving Equations Topic Generator v1")
    print("Generating 600 SEC-aligned questions")
    print("=" * 60)
    
    questions = generate_all_questions()
    validate_questions(questions)
    
    print("\n" + "=" * 60)
    response = input("Insert questions into database? (y/n): ")
    
    if response.lower() == 'y':
        success = insert_into_database(questions)
        if success:
            print("\n✓ All questions inserted successfully!")
        else:
            print("\n⚠ Some questions failed to insert")
    else:
        print("Skipped database insertion.")
