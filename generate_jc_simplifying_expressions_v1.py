#!/usr/bin/env python3
"""
AgentMath - Simplifying Expressions Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q13(a): "Simplify 5a + 3b - 2a + 7b"
- 2023 OL Q12(b): "Expand 3(2x - 5)"
- 2024 OL Q12(a): "Simplify 4x + 7 - 2x + 3"
- 2024 HL Q8(b): "Expand and simplify (x + 3)(x - 2)"
- 2023 HL Q7(c): "Factorise x² + 5x + 6"

Level Structure:
  L1-3:   Foundation (like terms, collecting, combining)
  L4-6:   Ordinary (multiplying, single brackets, expand+simplify)
  L7-9:   Higher (double brackets, combined, mixed)
  L10-12: Mastery (factorising common, quadratics, complex)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os
from fractions import Fraction

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'simplifying_expressions'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Ciara', 'Seán', 
               'Róisín', 'Darragh', 'Caoimhe', 'Fionn', 'Éabha', 'Tadhg', 'Méabh', 
               'Cillian', 'Áine', 'Liam', 'Sinéad', 'Eoin']

VARIABLES = ['x', 'y', 'a', 'b', 'n', 'm', 'p', 'k']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_term(coef, var, first=False):
    """Format a term like 3x, -2y, etc."""
    if coef == 0:
        return ''
    if var == '':  # constant
        if first:
            return str(coef)
        elif coef > 0:
            return f" + {coef}"
        else:
            return f" - {abs(coef)}"
    else:
        if coef == 1:
            coef_str = ''
        elif coef == -1:
            coef_str = '-'
        else:
            coef_str = str(coef)
        
        if first:
            return f"{coef_str}{var}"
        elif coef > 0:
            if coef == 1:
                return f" + {var}"
            return f" + {coef}{var}"
        else:
            if coef == -1:
                return f" - {var}"
            return f" - {abs(coef)}{var}"

def format_expression(terms):
    """Format a list of (coef, var) tuples as an expression."""
    result = ''
    first = True
    for coef, var in terms:
        if coef == 0:
            continue
        term = format_term(coef, var, first)
        result += term
        if term:
            first = False
    return result if result else '0'

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included."""
    correct_str = str(correct).strip()
    options = [correct_str]
    
    for w in wrong_list:
        w_str = str(w).strip()
        if w_str != correct_str and w_str not in options:
            options.append(w_str)
        if len(options) >= 4:
            break
    
    # Ensure we have 4 unique options
    fallback_idx = 1
    while len(options) < 4:
        fallback = f"Cannot simplify ({fallback_idx})"
        if fallback not in options:
            options.append(fallback)
        fallback_idx += 1
    
    options = options[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    
    return options, correct_idx

# ============================================================
# LEVEL 1: Recognising Like Terms
# ============================================================

def generate_level_1():
    """Foundation: Identify which terms are like terms."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            template = random.choice([1, 2, 3, 4])
            
            if template == 1:
                # Which terms are like terms?
                var = random.choice(VARIABLES[:4])
                c1 = random.randint(2, 9)
                c2 = random.randint(2, 9)
                c3 = random.randint(2, 9)
                other_var = random.choice([v for v in VARIABLES[:4] if v != var])
                
                q_text = f"Which pair are like terms? {c1}{var}, {c2}{other_var}, {c3}{var}"
                correct = f"{c1}{var} and {c3}{var}"
                wrong = [
                    f"{c1}{var} and {c2}{other_var}",
                    f"{c2}{other_var} and {c3}{var}",
                    f"None are like terms"
                ]
            
            elif template == 2:
                # True/False: Are these like terms?
                var = random.choice(VARIABLES[:4])
                c1 = random.randint(2, 9)
                c2 = random.randint(2, 9)
                
                if random.choice([True, False]):
                    # Yes, they are like terms
                    q_text = f"Are {c1}{var} and {c2}{var} like terms?"
                    correct = "Yes, both have the variable " + var
                    wrong = [
                        "No, the coefficients are different",
                        "No, they cannot be combined",
                        "Only if " + var + " = 1"
                    ]
                else:
                    # No, different variables
                    other_var = random.choice([v for v in VARIABLES[:4] if v != var])
                    q_text = f"Are {c1}{var} and {c2}{other_var} like terms?"
                    correct = "No, they have different variables"
                    wrong = [
                        "Yes, both are algebraic terms",
                        "Yes, both have coefficients",
                        f"Yes, {c1} + {c2} = {c1+c2}"
                    ]
            
            elif template == 3:
                # Count like terms
                var = random.choice(VARIABLES[:4])
                other = random.choice([v for v in VARIABLES[:4] if v != var])
                terms = []
                var_count = random.randint(2, 4)
                other_count = random.randint(1, 2)
                
                for _ in range(var_count):
                    terms.append(f"{random.randint(1, 9)}{var}")
                for _ in range(other_count):
                    terms.append(f"{random.randint(1, 9)}{other}")
                
                random.shuffle(terms)
                q_text = f"How many terms contain the variable {var}? {', '.join(terms)}"
                correct = str(var_count)
                wrong = [str(other_count), str(var_count + other_count), str(var_count - 1)]
            
            else:
                # Identify the odd one out
                var = random.choice(VARIABLES[:4])
                other = random.choice([v for v in VARIABLES[:4] if v != var])
                c1, c2, c3 = random.sample(range(2, 10), 3)
                c_other = random.randint(2, 9)
                
                terms = [f"{c1}{var}", f"{c2}{var}", f"{c3}{var}", f"{c_other}{other}"]
                random.shuffle(terms)
                
                q_text = f"Which term is NOT like the others? {', '.join(terms)}"
                correct = f"{c_other}{other}"
                wrong = [f"{c1}{var}", f"{c2}{var}", f"{c3}{var}"]
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            explanation = "Like terms have the same variable part. Only like terms can be added or subtracted together."
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Collecting Like Terms (Simple)
# ============================================================

def generate_level_2():
    """Foundation: Collect like terms with one variable."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:4])
            c1 = random.randint(2, 9)
            c2 = random.randint(2, 9)
            
            template = random.choice([1, 2, 3])
            
            if template == 1:
                # Simple addition: 3x + 5x
                q_text = f"Simplify: {c1}{var} + {c2}{var}"
                answer = c1 + c2
                correct = f"{answer}{var}"
                wrong = [
                    f"{c1 * c2}{var}",
                    f"{c1}{c2}{var}",
                    f"{answer}{var}²"
                ]
                explanation = f"Step 1: Both terms have {var}\nStep 2: Add coefficients: {c1} + {c2} = {answer}\nAnswer: {answer}{var}"
            
            elif template == 2:
                # Simple subtraction: 8x - 3x
                if c1 < c2:
                    c1, c2 = c2, c1
                q_text = f"Simplify: {c1}{var} - {c2}{var}"
                answer = c1 - c2
                correct = f"{answer}{var}" if answer != 1 else var
                wrong = [
                    f"{c1 + c2}{var}",
                    f"{c1 * c2}{var}",
                    f"-{c2 - c1}{var}"
                ]
                explanation = f"Step 1: Both terms have {var}\nStep 2: Subtract coefficients: {c1} - {c2} = {answer}\nAnswer: {correct}"
            
            else:
                # Three terms: 2x + 5x + 3x
                c3 = random.randint(1, 5)
                q_text = f"Simplify: {c1}{var} + {c2}{var} + {c3}{var}"
                answer = c1 + c2 + c3
                correct = f"{answer}{var}"
                wrong = [
                    f"{c1 + c2}{var}",
                    f"{c1 * c2 * c3}{var}",
                    f"{answer}{var}³"
                ]
                explanation = f"Step 1: All terms have {var}\nStep 2: Add coefficients: {c1} + {c2} + {c3} = {answer}\nAnswer: {answer}{var}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Collecting Like Terms (Two Variables)
# ============================================================

def generate_level_3():
    """Foundation: Collect like terms with two different variables."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var1, var2 = random.sample(VARIABLES[:4], 2)
            a1 = random.randint(2, 7)
            b1 = random.randint(2, 7)
            a2 = random.randint(1, 5)
            b2 = random.randint(1, 5)
            
            template = random.choice([1, 2, 3])
            
            if template == 1:
                # 3a + 5b + 2a + 4b
                q_text = f"Simplify: {a1}{var1} + {b1}{var2} + {a2}{var1} + {b2}{var2}"
                ans_a = a1 + a2
                ans_b = b1 + b2
                correct = f"{ans_a}{var1} + {ans_b}{var2}"
                wrong = [
                    f"{a1 + a2 + b1 + b2}{var1}{var2}",
                    f"{ans_a}{var1} + {b1}{var2}",
                    f"{a1}{var1} + {ans_b}{var2}"
                ]
                explanation = f"Step 1: Group like terms: ({a1}{var1} + {a2}{var1}) + ({b1}{var2} + {b2}{var2})\nStep 2: Simplify each group: {ans_a}{var1} + {ans_b}{var2}\nAnswer: {correct}"
            
            elif template == 2:
                # 5a + 3b - 2a + 7b (SEC 2022 style)
                q_text = f"Simplify: {a1}{var1} + {b1}{var2} - {a2}{var1} + {b2}{var2}"
                ans_a = a1 - a2
                ans_b = b1 + b2
                if ans_a == 1:
                    correct = f"{var1} + {ans_b}{var2}"
                elif ans_a == 0:
                    correct = f"{ans_b}{var2}"
                else:
                    correct = f"{ans_a}{var1} + {ans_b}{var2}"
                wrong = [
                    f"{a1 + a2}{var1} + {b1 + b2}{var2}",
                    f"{a1 - a2}{var1} - {b1 + b2}{var2}",
                    f"{ans_a}{var1}{var2}"
                ]
                explanation = f"Step 1: Group {var1} terms: {a1}{var1} - {a2}{var1} = {ans_a}{var1}\nStep 2: Group {var2} terms: {b1}{var2} + {b2}{var2} = {ans_b}{var2}\nAnswer: {correct}"
            
            else:
                # With a constant: 3x + 5 + 2x + 4
                const1 = random.randint(2, 8)
                const2 = random.randint(1, 5)
                q_text = f"Simplify: {a1}{var1} + {const1} + {a2}{var1} + {const2}"
                ans_a = a1 + a2
                ans_const = const1 + const2
                correct = f"{ans_a}{var1} + {ans_const}"
                wrong = [
                    f"{ans_a + ans_const}{var1}",
                    f"{a1}{var1} + {ans_const}",
                    f"{ans_a}{var1} + {const1}"
                ]
                explanation = f"Step 1: Group {var1} terms: {a1}{var1} + {a2}{var1} = {ans_a}{var1}\nStep 2: Group constants: {const1} + {const2} = {ans_const}\nAnswer: {correct}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Multiplying Terms
# ============================================================

def generate_level_4():
    """Ordinary: Multiply algebraic terms."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:4])
            
            template = random.choice([1, 2, 3, 4])
            
            if template == 1:
                # Number × term: 3 × 4x
                c1 = random.randint(2, 6)
                c2 = random.randint(2, 6)
                q_text = f"Simplify: {c1} × {c2}{var}"
                answer = c1 * c2
                correct = f"{answer}{var}"
                wrong = [
                    f"{c1 + c2}{var}",
                    f"{c1}{c2}{var}",
                    f"{answer}"
                ]
                explanation = f"Step 1: Multiply coefficients: {c1} × {c2} = {answer}\nStep 2: Keep the variable\nAnswer: {answer}{var}"
            
            elif template == 2:
                # Term × term same variable: 2x × 3x
                c1 = random.randint(2, 5)
                c2 = random.randint(2, 5)
                q_text = f"Simplify: {c1}{var} × {c2}{var}"
                answer = c1 * c2
                correct = f"{answer}{var}²"
                wrong = [
                    f"{c1 + c2}{var}",
                    f"{answer}{var}",
                    f"{c1}{c2}{var}²"
                ]
                explanation = f"Step 1: Multiply coefficients: {c1} × {c2} = {answer}\nStep 2: Multiply variables: {var} × {var} = {var}²\nAnswer: {answer}{var}²"
            
            elif template == 3:
                # Term × term different variables: 3x × 2y
                var2 = random.choice([v for v in VARIABLES[:4] if v != var])
                c1 = random.randint(2, 5)
                c2 = random.randint(2, 5)
                q_text = f"Simplify: {c1}{var} × {c2}{var2}"
                answer = c1 * c2
                correct = f"{answer}{var}{var2}"
                wrong = [
                    f"{c1 + c2}{var}{var2}",
                    f"{answer}{var}",
                    f"{answer}{var2}"
                ]
                explanation = f"Step 1: Multiply coefficients: {c1} × {c2} = {answer}\nStep 2: Multiply variables: {var} × {var2} = {var}{var2}\nAnswer: {answer}{var}{var2}"
            
            else:
                # Square a term: (3x)²
                c1 = random.randint(2, 5)
                q_text = f"Simplify: ({c1}{var})²"
                answer = c1 * c1
                correct = f"{answer}{var}²"
                wrong = [
                    f"{c1 * 2}{var}²",
                    f"{c1}{var}²",
                    f"{answer}{var}"
                ]
                explanation = f"Step 1: ({c1}{var})² = {c1}{var} × {c1}{var}\nStep 2: {c1} × {c1} = {answer}\nStep 3: {var} × {var} = {var}²\nAnswer: {answer}{var}²"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 4,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Expanding Single Brackets
# ============================================================

def generate_level_5():
    """Ordinary: Expand single brackets - SEC 2023 style."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:4])
            
            template = random.choice([1, 2, 3, 4])
            
            if template == 1:
                # a(bx + c): 3(2x + 5)
                a = random.randint(2, 5)
                b = random.randint(1, 4)
                c = random.randint(1, 6)
                q_text = f"Expand: {a}({b}{var} + {c})"
                term1 = a * b
                term2 = a * c
                correct = f"{term1}{var} + {term2}"
                wrong = [
                    f"{a + b}{var} + {c}",
                    f"{term1}{var} + {c}",
                    f"{a}{var} + {term2}"
                ]
                explanation = f"Step 1: {a} × {b}{var} = {term1}{var}\nStep 2: {a} × {c} = {term2}\nAnswer: {term1}{var} + {term2}"
            
            elif template == 2:
                # a(bx - c): 3(4x - 2) SEC 2023 style
                a = random.randint(2, 5)
                b = random.randint(2, 4)
                c = random.randint(1, 5)
                q_text = f"Expand: {a}({b}{var} - {c})"
                term1 = a * b
                term2 = a * c
                correct = f"{term1}{var} - {term2}"
                wrong = [
                    f"{term1}{var} + {term2}",
                    f"{a + b}{var} - {c}",
                    f"{term1}{var} - {c}"
                ]
                explanation = f"Step 1: {a} × {b}{var} = {term1}{var}\nStep 2: {a} × (-{c}) = -{term2}\nAnswer: {term1}{var} - {term2}"
            
            elif template == 3:
                # x(x + a): x(x + 3)
                a = random.randint(2, 7)
                q_text = f"Expand: {var}({var} + {a})"
                correct = f"{var}² + {a}{var}"
                wrong = [
                    f"{var}² + {a}",
                    f"2{var} + {a}",
                    f"{var}² + {a}{var}²"
                ]
                explanation = f"Step 1: {var} × {var} = {var}²\nStep 2: {var} × {a} = {a}{var}\nAnswer: {var}² + {a}{var}"
            
            else:
                # Negative outside: -2(3x + 4)
                a = random.randint(2, 4)
                b = random.randint(2, 5)
                c = random.randint(1, 5)
                q_text = f"Expand: -{a}({b}{var} + {c})"
                term1 = a * b
                term2 = a * c
                correct = f"-{term1}{var} - {term2}"
                wrong = [
                    f"-{term1}{var} + {term2}",
                    f"{term1}{var} - {term2}",
                    f"-{a}{var} - {c}"
                ]
                explanation = f"Step 1: -{a} × {b}{var} = -{term1}{var}\nStep 2: -{a} × {c} = -{term2}\nAnswer: -{term1}{var} - {term2}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 5,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Expand and Simplify (Two Single Brackets)
# ============================================================

def generate_level_6():
    """Ordinary: Expand two brackets and simplify."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:4])
            
            template = random.choice([1, 2, 3])
            
            if template == 1:
                # 2(x + 3) + 3(x + 2)
                a1 = random.randint(2, 4)
                b1 = random.randint(1, 5)
                a2 = random.randint(2, 4)
                b2 = random.randint(1, 5)
                q_text = f"Expand and simplify: {a1}({var} + {b1}) + {a2}({var} + {b2})"
                coef_x = a1 + a2
                const = a1 * b1 + a2 * b2
                correct = f"{coef_x}{var} + {const}"
                wrong = [
                    f"{a1 + a2}{var} + {b1 + b2}",
                    f"{a1}{var} + {a2}{var} + {b1} + {b2}",
                    f"{coef_x}{var} + {a1 * b1}"
                ]
                explanation = f"Step 1: Expand first bracket: {a1}{var} + {a1 * b1}\nStep 2: Expand second bracket: {a2}{var} + {a2 * b2}\nStep 3: Collect like terms: ({a1} + {a2}){var} + ({a1 * b1} + {a2 * b2})\nAnswer: {coef_x}{var} + {const}"
            
            elif template == 2:
                # 3(x + 2) - 2(x + 1)
                a1 = random.randint(3, 5)
                b1 = random.randint(2, 5)
                a2 = random.randint(2, 3)
                b2 = random.randint(1, 4)
                q_text = f"Expand and simplify: {a1}({var} + {b1}) - {a2}({var} + {b2})"
                coef_x = a1 - a2
                const = a1 * b1 - a2 * b2
                if const >= 0:
                    correct = f"{coef_x}{var} + {const}" if coef_x != 1 else f"{var} + {const}"
                else:
                    correct = f"{coef_x}{var} - {abs(const)}" if coef_x != 1 else f"{var} - {abs(const)}"
                wrong = [
                    f"{a1 + a2}{var} + {b1 - b2}",
                    f"{a1 - a2}{var} + {a1 * b1 + a2 * b2}",
                    f"{coef_x}{var}"
                ]
                explanation = f"Step 1: Expand: {a1}{var} + {a1 * b1} - {a2}{var} - {a2 * b2}\nStep 2: Collect {var} terms: {a1}{var} - {a2}{var} = {coef_x}{var}\nStep 3: Collect constants: {a1 * b1} - {a2 * b2} = {const}\nAnswer: {correct}"
            
            else:
                # 4(2x - 1) + 3(x + 5)
                a1 = random.randint(2, 4)
                b1 = random.randint(2, 3)
                c1 = random.randint(1, 4)
                a2 = random.randint(2, 4)
                c2 = random.randint(2, 6)
                q_text = f"Expand and simplify: {a1}({b1}{var} - {c1}) + {a2}({var} + {c2})"
                coef_x = a1 * b1 + a2
                const = -a1 * c1 + a2 * c2
                if const >= 0:
                    correct = f"{coef_x}{var} + {const}"
                else:
                    correct = f"{coef_x}{var} - {abs(const)}"
                wrong = [
                    f"{a1 * b1}{var} + {a2}{var} - {c1} + {c2}",
                    f"{coef_x}{var} + {a1 * c1 + a2 * c2}",
                    f"{a1 + a2}{var} + {const}"
                ]
                explanation = f"Step 1: Expand first: {a1 * b1}{var} - {a1 * c1}\nStep 2: Expand second: {a2}{var} + {a2 * c2}\nStep 3: Collect like terms\nAnswer: {correct}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 6,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Expanding Double Brackets (FOIL)
# ============================================================

def generate_level_7():
    """Higher: Expand (x + a)(x + b) using FOIL."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:3])
            
            template = random.choice([1, 2, 3, 4])
            
            if template == 1:
                # (x + a)(x + b) both positive
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                q_text = f"Expand: ({var} + {a})({var} + {b})"
                middle = a + b
                last = a * b
                correct = f"{var}² + {middle}{var} + {last}"
                wrong = [
                    f"{var}² + {a}{var} + {b}{var} + {last}",
                    f"{var}² + {last}",
                    f"{var}² + {a + b}{var}"
                ]
                explanation = f"Using FOIL:\nFirst: {var} × {var} = {var}²\nOuter: {var} × {b} = {b}{var}\nInner: {a} × {var} = {a}{var}\nLast: {a} × {b} = {last}\nCombine: {var}² + {b}{var} + {a}{var} + {last} = {var}² + {middle}{var} + {last}"
            
            elif template == 2:
                # (x + a)(x - b) mixed signs
                a = random.randint(2, 6)
                b = random.randint(1, 5)
                if a == b:
                    b = a + 1
                q_text = f"Expand: ({var} + {a})({var} - {b})"
                middle = a - b
                last = -a * b
                if middle > 0:
                    correct = f"{var}² + {middle}{var} - {a * b}"
                elif middle < 0:
                    correct = f"{var}² - {abs(middle)}{var} - {a * b}"
                else:
                    correct = f"{var}² - {a * b}"
                wrong = [
                    f"{var}² + {a - b}{var} + {a * b}",
                    f"{var}² - {a + b}{var} - {a * b}",
                    f"{var}² + {a}{var} - {b}{var} - {a * b}"
                ]
                explanation = f"Using FOIL:\nFirst: {var}²\nOuter: -{b}{var}\nInner: +{a}{var}\nLast: -{a * b}\nCombine: {var}² + ({a} - {b}){var} - {a * b}"
            
            elif template == 3:
                # (x - a)(x - b) both negative
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                q_text = f"Expand: ({var} - {a})({var} - {b})"
                middle = -(a + b)
                last = a * b
                correct = f"{var}² - {a + b}{var} + {last}"
                wrong = [
                    f"{var}² + {a + b}{var} + {last}",
                    f"{var}² - {a + b}{var} - {last}",
                    f"{var}² - {a}{var} - {b}{var} + {last}"
                ]
                explanation = f"Using FOIL:\nFirst: {var}²\nOuter: -{b}{var}\nInner: -{a}{var}\nLast: +{a * b} (negative × negative = positive)\nCombine: {var}² - {a + b}{var} + {last}"
            
            else:
                # (x - a)(x + b) with a > b to get negative middle
                a = random.randint(3, 6)
                b = random.randint(1, a - 1)
                q_text = f"Expand: ({var} - {a})({var} + {b})"
                middle = b - a
                last = -a * b
                correct = f"{var}² - {abs(middle)}{var} - {a * b}"
                wrong = [
                    f"{var}² + {abs(middle)}{var} - {a * b}",
                    f"{var}² - {a}{var} + {b}{var} - {a * b}",
                    f"{var}² - {a * b}"
                ]
                explanation = f"Using FOIL:\nFirst: {var}²\nOuter: +{b}{var}\nInner: -{a}{var}\nLast: -{a * b}\nCombine: {var}² + ({b} - {a}){var} - {a * b} = {var}² - {a - b}{var} - {a * b}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 7,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Special Products
# ============================================================

def generate_level_8():
    """Higher: Perfect squares and difference of squares."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:3])
            
            template = random.choice([1, 2, 3, 4])
            
            if template == 1:
                # (x + a)² perfect square
                a = random.randint(2, 7)
                q_text = f"Expand: ({var} + {a})²"
                correct = f"{var}² + {2 * a}{var} + {a * a}"
                wrong = [
                    f"{var}² + {a * a}",
                    f"{var}² + {a}{var} + {a * a}",
                    f"2{var} + {2 * a}"
                ]
                explanation = f"({var} + {a})² = ({var} + {a})({var} + {a})\nUsing FOIL or formula (a + b)² = a² + 2ab + b²:\n{var}² + 2({a}){var} + {a}² = {var}² + {2 * a}{var} + {a * a}"
            
            elif template == 2:
                # (x - a)² perfect square
                a = random.randint(2, 7)
                q_text = f"Expand: ({var} - {a})²"
                correct = f"{var}² - {2 * a}{var} + {a * a}"
                wrong = [
                    f"{var}² + {2 * a}{var} + {a * a}",
                    f"{var}² - {a * a}",
                    f"{var}² - {a}{var} + {a * a}"
                ]
                explanation = f"({var} - {a})² = ({var} - {a})({var} - {a})\nUsing formula (a - b)² = a² - 2ab + b²:\n{var}² - 2({a}){var} + {a}² = {var}² - {2 * a}{var} + {a * a}"
            
            elif template == 3:
                # (x + a)(x - a) difference of squares
                a = random.randint(2, 8)
                q_text = f"Expand: ({var} + {a})({var} - {a})"
                correct = f"{var}² - {a * a}"
                wrong = [
                    f"{var}² + {a * a}",
                    f"{var}² - {2 * a}{var}",
                    f"2{var}"
                ]
                explanation = f"This is the difference of two squares: (a + b)(a - b) = a² - b²\n({var} + {a})({var} - {a}) = {var}² - {a}² = {var}² - {a * a}"
            
            else:
                # (ax + b)²
                a = random.randint(2, 3)
                b = random.randint(1, 4)
                q_text = f"Expand: ({a}{var} + {b})²"
                first = a * a
                middle = 2 * a * b
                last = b * b
                correct = f"{first}{var}² + {middle}{var} + {last}"
                wrong = [
                    f"{a}{var}² + {middle}{var} + {last}",
                    f"{first}{var}² + {b}{var} + {last}",
                    f"{first}{var}² + {last}"
                ]
                explanation = f"({a}{var} + {b})² = ({a}{var})² + 2({a}{var})({b}) + {b}²\n= {first}{var}² + {middle}{var} + {last}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 8,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Mixed Expanding and Simplifying
# ============================================================

def generate_level_9():
    """Higher: Complex expand and simplify."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:3])
            
            template = random.choice([1, 2, 3])
            
            if template == 1:
                # (x + a)(x + b) + c
                a = random.randint(1, 4)
                b = random.randint(1, 4)
                c = random.randint(2, 8)
                q_text = f"Expand and simplify: ({var} + {a})({var} + {b}) + {c}"
                middle = a + b
                last = a * b + c
                correct = f"{var}² + {middle}{var} + {last}"
                wrong = [
                    f"{var}² + {middle}{var} + {a * b}",
                    f"{var}² + {a + b + c}{var}",
                    f"{var}² + {c}{var} + {a * b}"
                ]
                explanation = f"Step 1: Expand ({var} + {a})({var} + {b}) = {var}² + {middle}{var} + {a * b}\nStep 2: Add {c}: {var}² + {middle}{var} + {a * b} + {c} = {var}² + {middle}{var} + {last}"
            
            elif template == 2:
                # (x + a)² - (x + b)²
                a = random.randint(2, 5)
                b = random.randint(1, a - 1)
                q_text = f"Expand and simplify: ({var} + {a})² - ({var} + {b})²"
                # (x+a)² = x² + 2ax + a²
                # (x+b)² = x² + 2bx + b²
                # Difference: 2ax - 2bx + a² - b² = 2(a-b)x + (a²-b²)
                coef = 2 * (a - b)
                const = a * a - b * b
                correct = f"{coef}{var} + {const}"
                wrong = [
                    f"{var}² + {coef}{var} + {const}",
                    f"2{var}² + {coef}{var}",
                    f"{a - b}{var} + {const}"
                ]
                explanation = f"Step 1: ({var} + {a})² = {var}² + {2 * a}{var} + {a * a}\nStep 2: ({var} + {b})² = {var}² + {2 * b}{var} + {b * b}\nStep 3: Subtract: {var}² terms cancel\n{2 * a}{var} - {2 * b}{var} = {coef}{var}\n{a * a} - {b * b} = {const}\nAnswer: {coef}{var} + {const}"
            
            else:
                # 2(x + a)(x + b)
                a = random.randint(1, 4)
                b = random.randint(1, 4)
                q_text = f"Expand and simplify: 2({var} + {a})({var} + {b})"
                middle = 2 * (a + b)
                last = 2 * a * b
                correct = f"2{var}² + {middle}{var} + {last}"
                wrong = [
                    f"2{var}² + {a + b}{var} + {a * b}",
                    f"{var}² + {middle}{var} + {last}",
                    f"2{var}² + 2{var} + {last}"
                ]
                explanation = f"Step 1: Expand ({var} + {a})({var} + {b}) = {var}² + {a + b}{var} + {a * b}\nStep 2: Multiply by 2: 2{var}² + {middle}{var} + {last}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 9,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Factorising - Common Factor
# ============================================================

def generate_level_10():
    """Mastery: Factorise by taking out common factors."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:3])
            
            template = random.choice([1, 2, 3, 4])
            
            if template == 1:
                # Number common factor: 6x + 12
                common = random.randint(2, 6)
                a = random.randint(1, 5)
                b = random.randint(1, 6)
                term1 = common * a
                term2 = common * b
                q_text = f"Factorise: {term1}{var} + {term2}"
                correct = f"{common}({a}{var} + {b})" if a != 1 else f"{common}({var} + {b})"
                wrong = [
                    f"{term1}({var} + {term2})",
                    f"{a}({term1}{var} + {b})",
                    f"{var}({term1} + {term2})"
                ]
                explanation = f"HCF of {term1} and {term2} is {common}\n{term1}{var} ÷ {common} = {a}{var}\n{term2} ÷ {common} = {b}\nAnswer: {correct}"
            
            elif template == 2:
                # Variable common factor: x² + 3x
                a = random.randint(2, 7)
                q_text = f"Factorise: {var}² + {a}{var}"
                correct = f"{var}({var} + {a})"
                wrong = [
                    f"{a}({var}² + {var})",
                    f"{var}²(1 + {a})",
                    f"({var} + {a}){var}"
                ]
                explanation = f"Common factor is {var}\n{var}² ÷ {var} = {var}\n{a}{var} ÷ {var} = {a}\nAnswer: {var}({var} + {a})"
            
            elif template == 3:
                # Both number and variable: 6x² + 9x
                common = random.randint(2, 4)
                a = random.randint(2, 4)
                b = random.randint(1, 4)
                term1 = common * a
                term2 = common * b
                q_text = f"Factorise: {term1}{var}² + {term2}{var}"
                correct = f"{common}{var}({a}{var} + {b})"
                wrong = [
                    f"{common}({term1}{var}² + {term2}{var})",
                    f"{var}({term1}{var} + {term2})",
                    f"{term1}{var}({var} + {b})"
                ]
                explanation = f"HCF of {term1}{var}² and {term2}{var} is {common}{var}\n{term1}{var}² ÷ {common}{var} = {a}{var}\n{term2}{var} ÷ {common}{var} = {b}\nAnswer: {common}{var}({a}{var} + {b})"
            
            else:
                # Subtraction: 8x - 12
                common = random.randint(2, 4)
                a = random.randint(2, 5)
                b = random.randint(1, 4)
                term1 = common * a
                term2 = common * b
                q_text = f"Factorise: {term1}{var} - {term2}"
                correct = f"{common}({a}{var} - {b})"
                wrong = [
                    f"{common}({a}{var} + {b})",
                    f"{term1}({var} - {b})",
                    f"{a}({term1}{var} - {b})"
                ]
                explanation = f"HCF of {term1} and {term2} is {common}\n{term1}{var} ÷ {common} = {a}{var}\n{term2} ÷ {common} = {b}\nAnswer: {common}({a}{var} - {b})"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 10,
                'difficulty_band': 'mastery',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 11: Factorising Quadratics (Simple)
# ============================================================

def generate_level_11():
    """Mastery: Factorise x² + bx + c - SEC 2023 HL style."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    # Pre-generate valid factor pairs for reliable question generation
    factor_pairs = []
    for a in range(1, 8):
        for b in range(1, 8):
            factor_pairs.append((a, b, a + b, a * b))  # both positive
            factor_pairs.append((-a, -b, -(a + b), a * b))  # both negative
            if a != b:
                factor_pairs.append((a, -b, a - b, -a * b))  # mixed
                factor_pairs.append((-a, b, b - a, -a * b))  # mixed other way
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:3])
            
            template = random.choice([1, 2, 3])
            
            if template == 1:
                # x² + bx + c where both factors positive
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                middle = a + b
                last = a * b
                q_text = f"Factorise: {var}² + {middle}{var} + {last}"
                correct = f"({var} + {a})({var} + {b})"
                wrong = [
                    f"({var} + {last})({var} + 1)",
                    f"({var} + {middle})({var} + 1)",
                    f"({var} - {a})({var} - {b})"
                ]
                explanation = f"Find two numbers that:\n• Multiply to give {last}\n• Add to give {middle}\nNumbers are {a} and {b}\nAnswer: ({var} + {a})({var} + {b})"
            
            elif template == 2:
                # x² - bx + c where both factors negative
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                middle = a + b
                last = a * b
                q_text = f"Factorise: {var}² - {middle}{var} + {last}"
                correct = f"({var} - {a})({var} - {b})"
                wrong = [
                    f"({var} + {a})({var} + {b})",
                    f"({var} - {a})({var} + {b})",
                    f"({var} - {last})({var} - 1)"
                ]
                explanation = f"Find two numbers that:\n• Multiply to give +{last}\n• Add to give -{middle}\nNumbers are -{a} and -{b}\nAnswer: ({var} - {a})({var} - {b})"
            
            else:
                # x² + bx - c or x² - bx - c mixed signs
                a = random.randint(2, 6)
                b = random.randint(1, a - 1)
                middle = a - b  # positive middle
                last = a * b
                q_text = f"Factorise: {var}² + {middle}{var} - {last}"
                correct = f"({var} + {a})({var} - {b})"
                wrong = [
                    f"({var} - {a})({var} + {b})",
                    f"({var} + {a})({var} + {b})",
                    f"({var} + {middle})({var} - 1)"
                ]
                explanation = f"Find two numbers that:\n• Multiply to give -{last}\n• Add to give +{middle}\nNumbers are +{a} and -{b}\nAnswer: ({var} + {a})({var} - {b})"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 11,
                'difficulty_band': 'mastery',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 12: Complex Expressions / SEC Exam Style
# ============================================================

def generate_level_12():
    """Mastery: Complex multi-step problems."""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(VARIABLES[:3])
            
            template = random.choice([1, 2, 3, 4])
            
            if template == 1:
                # Difference of squares factorising
                a = random.randint(2, 9)
                a_sq = a * a
                q_text = f"Factorise: {var}² - {a_sq}"
                correct = f"({var} + {a})({var} - {a})"
                wrong = [
                    f"({var} - {a})²",
                    f"({var} + {a})²",
                    f"({var} - {a_sq})({var} + 1)"
                ]
                explanation = f"This is the difference of two squares: a² - b² = (a + b)(a - b)\n{var}² - {a_sq} = {var}² - {a}²\n= ({var} + {a})({var} - {a})"
            
            elif template == 2:
                # Factorise completely: 2x² + 6x
                common = random.randint(2, 4)
                a = random.randint(2, 4)
                coef1 = common
                coef2 = common * a
                q_text = f"Factorise completely: {coef1}{var}² + {coef2}{var}"
                correct = f"{common}{var}({var} + {a})"
                wrong = [
                    f"{var}({coef1}{var} + {coef2})",
                    f"{coef1}({var}² + {a}{var})",
                    f"{common}({var}² + {a}{var})"
                ]
                explanation = f"HCF = {common}{var}\n{coef1}{var}² ÷ {common}{var} = {var}\n{coef2}{var} ÷ {common}{var} = {a}\nAnswer: {common}{var}({var} + {a})"
            
            elif template == 3:
                # (ax + b)² expand fully
                a = random.randint(2, 4)
                b = random.randint(2, 5)
                q_text = f"Expand fully: ({a}{var} + {b})²"
                first = a * a
                middle = 2 * a * b
                last = b * b
                correct = f"{first}{var}² + {middle}{var} + {last}"
                wrong = [
                    f"{a}{var}² + {middle}{var} + {last}",
                    f"{first}{var}² + {b}{var} + {last}",
                    f"{first}{var}² + {last}"
                ]
                explanation = f"Using (a + b)² = a² + 2ab + b²:\n({a}{var})² + 2({a}{var})({b}) + {b}²\n= {first}{var}² + {middle}{var} + {last}"
            
            else:
                # (x + a)(x + b) - (x + c)(x + d) simplify
                a = random.randint(2, 5)
                b = random.randint(1, 4)
                c = random.randint(1, 3)
                d = random.randint(1, 3)
                q_text = f"Expand and simplify: ({var} + {a})({var} + {b}) - ({var} + {c})({var} + {d})"
                # (x+a)(x+b) = x² + (a+b)x + ab
                # (x+c)(x+d) = x² + (c+d)x + cd
                coef_x = (a + b) - (c + d)
                const = a * b - c * d
                if coef_x == 0:
                    correct = str(const)
                elif coef_x == 1:
                    if const >= 0:
                        correct = f"{var} + {const}"
                    else:
                        correct = f"{var} - {abs(const)}"
                else:
                    if const >= 0:
                        correct = f"{coef_x}{var} + {const}"
                    else:
                        correct = f"{coef_x}{var} - {abs(const)}"
                wrong = [
                    f"{var}² + {coef_x}{var} + {const}",
                    f"{a - c}{var} + {b - d}",
                    f"2{var}² + {coef_x}{var}"
                ]
                explanation = f"Step 1: ({var} + {a})({var} + {b}) = {var}² + {a + b}{var} + {a * b}\nStep 2: ({var} + {c})({var} + {d}) = {var}² + {c + d}{var} + {c * d}\nStep 3: Subtract: {var}² cancels\n({a + b} - {c + d}){var} + ({a * b} - {c * d}) = {correct}"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 12,
                'difficulty_band': 'mastery',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# VALIDATION
# ============================================================

def validate_questions(questions):
    """Validate all questions before database insertion."""
    errors = []
    level_counts = {}
    
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        # Check unique options
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options in '{q['question_text'][:50]}...'")
    
    # Print summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} {status}")
    print("=" * 60)
    print(f"Total: {len(questions)} | Errors: {len(errors)}")
    
    if errors[:10]:
        print("\nFirst 10 errors:")
        for e in errors[:10]:
            print(f"  - {e}")
    
    return len(errors)

# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete existing questions for this topic/mode
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    print(f"Deleted {cursor.rowcount} existing questions")
    
    # Insert new questions
    inserted = 0
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (question_text, option_a, option_b, option_c, option_d,
                 correct_answer, topic, difficulty_level, difficulty_band,
                 mode, explanation, image_svg, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            """, (
                q['question_text'], q['option_a'], q['option_b'], 
                q['option_c'], q['option_d'], q['correct_idx'], 
                q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'], q['explanation'], q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            print(f"Insert error: {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {inserted} questions")

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("AgentMath - Simplifying Expressions Generator")
    print("SEC Junior Cycle Aligned")
    print("=" * 60)
    
    all_questions = []
    
    generators = [
        (1, generate_level_1, "Recognising Like Terms"),
        (2, generate_level_2, "Collecting Like Terms (Simple)"),
        (3, generate_level_3, "Collecting Like Terms (Two Variables)"),
        (4, generate_level_4, "Multiplying Terms"),
        (5, generate_level_5, "Expanding Single Brackets"),
        (6, generate_level_6, "Expand and Simplify"),
        (7, generate_level_7, "Expanding Double Brackets (FOIL)"),
        (8, generate_level_8, "Special Products"),
        (9, generate_level_9, "Mixed Expanding"),
        (10, generate_level_10, "Factorising - Common Factor"),
        (11, generate_level_11, "Factorising Quadratics"),
        (12, generate_level_12, "Complex Expressions"),
    ]
    
    for level, gen_func, name in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = gen_func()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    error_count = validate_questions(all_questions)
    
    print(f"\n{'=' * 60}")
    if error_count == 0:
        print("✓ All questions validated successfully!")
    else:
        print(f"⚠ {error_count} validation errors found")
    
    response = input("\nInsert into database? (y/n): ")
    if response.lower() == 'y':
        insert_questions(all_questions)
        print("\n✓ Done!")
    else:
        print("\nDatabase insertion cancelled.")

if __name__ == "__main__":
    main()
