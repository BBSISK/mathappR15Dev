#!/usr/bin/env python3
"""
AgentMath - Introductory Algebra Question Generator
SEC-Aligned for Irish Junior Cycle Mathematics

Version: 1.0
Date: December 2025

Generates 600 questions (50 per level × 12 levels)
- NO answer-revealing visuals (image_svg = None)
- Clean text formatting (no embedded \n characters)
- Step-by-step explanations for all questions

Level Structure:
  1: Evaluating expressions (single variable, positive)
  2: Evaluating expressions (single variable, with negatives)
  3: Evaluating expressions (two variables)
  4: Collecting like terms (basic)
  5: Collecting like terms (with negatives)
  6: Expanding single brackets: a(x + b)
  7: Expanding single brackets: a(bx + c) with negatives
  8: Expanding and simplifying: a(x + b) + cx + d
  9: Expanding double brackets: (x + a)(x + b)
  10: Expanding double brackets with negatives
  11: Factorising common factors
  12: Mixed problems and applications

SEC Question Sources:
  - Junior Cycle OL/HL Algebra strand
  - Substitution, simplification, expansion, factorisation
"""

import sqlite3
import random

# ==================== CONFIGURATION ====================
TOPIC = 'introductory_algebra'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'  # Adjust for PythonAnywhere

# Difficulty bands
BANDS = {
    1: 'beginner', 2: 'beginner', 3: 'beginner',
    4: 'intermediate', 5: 'intermediate', 6: 'intermediate',
    7: 'advanced', 8: 'advanced', 9: 'advanced',
    10: 'mastery', 11: 'application', 12: 'linked'
}

# ==================== HELPER FUNCTIONS ====================

def format_term(coef, var='x', is_first=False):
    """Format a term like 3x, -2y, x, -x properly"""
    if coef == 0:
        return ''
    if var == '':  # Constant term
        if is_first:
            return str(coef)
        elif coef > 0:
            return f' + {coef}'
        else:
            return f' - {abs(coef)}'
    else:
        if coef == 1:
            coef_str = ''
        elif coef == -1:
            coef_str = '-'
        else:
            coef_str = str(coef)
        
        if is_first:
            return f'{coef_str}{var}'
        elif coef > 0:
            if coef == 1:
                return f' + {var}'
            return f' + {coef}{var}'
        else:
            if coef == -1:
                return f' - {var}'
            return f' - {abs(coef)}{var}'

def format_expression(x_coef, const, var='x'):
    """Format an expression like 3x + 5 or 2x - 3"""
    if x_coef == 0:
        return str(const)
    
    result = format_term(x_coef, var, is_first=True)
    if const != 0:
        result += format_term(const, '', is_first=False)
    return result

def format_binomial(a, b, var='x'):
    """Format (x + a) or (x - b) style binomial"""
    if b >= 0:
        return f'({var} + {b})'
    else:
        return f'({var} - {abs(b)})'

def generate_distractors_numeric(correct, count=3, spread=5):
    """Generate numeric distractors that are plausible but wrong"""
    distractors = set()
    attempts = 0
    while len(distractors) < count and attempts < 50:
        offset = random.choice([-3, -2, -1, 1, 2, 3, -4, 4, -5, 5])
        wrong = correct + offset
        if wrong != correct:
            distractors.add(wrong)
        attempts += 1
    
    # Fill with random if needed
    while len(distractors) < count:
        wrong = correct + random.randint(-10, 10)
        if wrong != correct:
            distractors.add(wrong)
    
    return list(distractors)[:count]

def generate_distractors_expression(correct_x, correct_const, var='x'):
    """Generate expression distractors like 5x + 3 vs 5x - 3"""
    correct = format_expression(correct_x, correct_const, var)
    distractors = []
    
    # Common mistakes
    options = [
        (correct_x, -correct_const),  # Sign error on constant
        (-correct_x, correct_const),  # Sign error on x term
        (correct_x + 1, correct_const),  # Off by one on x
        (correct_x - 1, correct_const),
        (correct_x, correct_const + 1),  # Off by one on constant
        (correct_x, correct_const - 1),
        (correct_x + correct_const, 0),  # Combined wrongly
        (correct_x * 2, correct_const),  # Doubled x coefficient
    ]
    
    for x, c in options:
        expr = format_expression(x, c, var)
        if expr != correct and expr not in distractors:
            distractors.append(expr)
        if len(distractors) >= 3:
            break
    
    # Fill if needed
    while len(distractors) < 3:
        x = correct_x + random.choice([-2, -1, 1, 2])
        c = correct_const + random.choice([-2, -1, 1, 2])
        expr = format_expression(x, c, var)
        if expr != correct and expr not in distractors:
            distractors.append(expr)
    
    return distractors[:3]

def make_question(question_text, correct_answer, distractors, explanation, level):
    """Create a question dictionary with shuffled options"""
    options = [correct_answer] + distractors[:3]
    random.shuffle(options)
    correct_idx = options.index(correct_answer)  # Returns 0, 1, 2, or 3
    
    return {
        'topic': TOPIC,
        'question_text': question_text,
        'option_a': str(options[0]),
        'option_b': str(options[1]),
        'option_c': str(options[2]),
        'option_d': str(options[3]),
        'correct_idx': correct_idx,  # Integer 0-3 for database
        'explanation': explanation,
        'difficulty': level,
        'difficulty_band': BANDS[level],
        'mode': 'practice',
        'image_svg': None  # NO VISUALS - prevents answer reveal
    }


# ==================== LEVEL GENERATORS ====================

def generate_level_1():
    """Level 1: Evaluating expressions - single variable, positive values"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        # Generate expression type
        expr_type = random.choice(['ax', 'ax+b', 'ax-b', 'a+bx'])
        
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        x_val = random.randint(1, 10)
        
        if expr_type == 'ax':
            expr = f'{a}x'
            answer = a * x_val
            explanation = f'Substitute x = {x_val}: {a} × {x_val} = {answer}'
        elif expr_type == 'ax+b':
            expr = f'{a}x + {b}'
            answer = a * x_val + b
            explanation = f'Substitute x = {x_val}: {a} × {x_val} + {b} = {a * x_val} + {b} = {answer}'
        elif expr_type == 'ax-b':
            expr = f'{a}x - {b}'
            answer = a * x_val - b
            explanation = f'Substitute x = {x_val}: {a} × {x_val} - {b} = {a * x_val} - {b} = {answer}'
        else:  # a+bx
            expr = f'{a} + {b}x'
            answer = a + b * x_val
            explanation = f'Substitute x = {x_val}: {a} + {b} × {x_val} = {a} + {b * x_val} = {answer}'
        
        question_text = f'Find the value of {expr} when x = {x_val}'
        distractors = generate_distractors_numeric(answer)
        
        questions.append(make_question(question_text, str(answer), 
                                        [str(d) for d in distractors], explanation, 1))
    
    return questions


def generate_level_2():
    """Level 2: Evaluating expressions - with negative values"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        expr_type = random.choice(['ax', 'ax+b', 'ax-b', 'a-bx'])
        
        a = random.randint(2, 8)
        b = random.randint(1, 8)
        x_val = random.randint(-5, -1)  # Negative x values
        
        if expr_type == 'ax':
            expr = f'{a}x'
            answer = a * x_val
            explanation = f'Substitute x = {x_val}: {a} × ({x_val}) = {answer}'
        elif expr_type == 'ax+b':
            expr = f'{a}x + {b}'
            answer = a * x_val + b
            explanation = f'Substitute x = {x_val}: {a} × ({x_val}) + {b} = {a * x_val} + {b} = {answer}'
        elif expr_type == 'ax-b':
            expr = f'{a}x - {b}'
            answer = a * x_val - b
            explanation = f'Substitute x = {x_val}: {a} × ({x_val}) - {b} = {a * x_val} - {b} = {answer}'
        else:  # a-bx
            expr = f'{a} - {b}x'
            answer = a - b * x_val
            explanation = f'Substitute x = {x_val}: {a} - {b} × ({x_val}) = {a} - ({b * x_val}) = {answer}'
        
        question_text = f'Find the value of {expr} when x = {x_val}'
        distractors = generate_distractors_numeric(answer)
        
        questions.append(make_question(question_text, str(answer),
                                        [str(d) for d in distractors], explanation, 2))
    
    return questions


def generate_level_3():
    """Level 3: Evaluating expressions - two variables"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        expr_type = random.choice(['ax+by', 'ax-by', 'axy', 'ax+by+c'])
        
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        x_val = random.randint(1, 5)
        y_val = random.randint(1, 5)
        
        if expr_type == 'ax+by':
            expr = f'{a}x + {b}y'
            answer = a * x_val + b * y_val
            explanation = f'Substitute x = {x_val}, y = {y_val}: {a}({x_val}) + {b}({y_val}) = {a * x_val} + {b * y_val} = {answer}'
        elif expr_type == 'ax-by':
            expr = f'{a}x - {b}y'
            answer = a * x_val - b * y_val
            explanation = f'Substitute x = {x_val}, y = {y_val}: {a}({x_val}) - {b}({y_val}) = {a * x_val} - {b * y_val} = {answer}'
        elif expr_type == 'axy':
            expr = f'{a}xy'
            answer = a * x_val * y_val
            explanation = f'Substitute x = {x_val}, y = {y_val}: {a} × {x_val} × {y_val} = {answer}'
        else:  # ax+by+c
            expr = f'{a}x + {b}y + {c}'
            answer = a * x_val + b * y_val + c
            explanation = f'Substitute x = {x_val}, y = {y_val}: {a}({x_val}) + {b}({y_val}) + {c} = {a * x_val} + {b * y_val} + {c} = {answer}'
        
        question_text = f'Find the value of {expr} when x = {x_val} and y = {y_val}'
        distractors = generate_distractors_numeric(answer)
        
        questions.append(make_question(question_text, str(answer),
                                        [str(d) for d in distractors], explanation, 3))
    
    return questions


def generate_level_4():
    """Level 4: Collecting like terms - basic (positive coefficients)"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        # Generate terms to collect
        expr_type = random.choice(['x_terms', 'x_and_const', 'two_vars'])
        
        if expr_type == 'x_terms':
            a = random.randint(2, 7)
            b = random.randint(2, 7)
            expr = f'{a}x + {b}x'
            answer_x = a + b
            answer = f'{answer_x}x'
            explanation = f'Collect like terms: {a}x + {b}x = ({a} + {b})x = {answer_x}x'
            distractors = set()
            distractors.add(f'{a*b}x')
            distractors.add(f'{a + b + 1}x')
            distractors.add(f'{a + b - 1}x')
            distractors.add(f'{abs(a - b)}x')
            distractors.discard(answer)
            distractors = list(distractors)[:3]
            
        elif expr_type == 'x_and_const':
            a = random.randint(2, 6)
            b = random.randint(1, 5)
            c = random.randint(2, 6)
            d = random.randint(1, 5)
            expr = f'{a}x + {b} + {c}x + {d}'
            answer_x = a + c
            answer_const = b + d
            answer = format_expression(answer_x, answer_const)
            explanation = f'Collect like terms: ({a}x + {c}x) + ({b} + {d}) = {answer_x}x + {answer_const}'
            distractors = generate_distractors_expression(answer_x, answer_const)
            
        else:  # two_vars
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            c = random.randint(2, 5)
            d = random.randint(2, 5)
            expr = f'{a}x + {b}y + {c}x + {d}y'
            answer = f'{a+c}x + {b+d}y'
            explanation = f'Collect like terms: ({a}x + {c}x) + ({b}y + {d}y) = {a+c}x + {b+d}y'
            distractors = set()
            distractors.add(f'{a+c}x + {b+d+1}y')
            distractors.add(f'{a+c+1}x + {b+d}y')
            distractors.add(f'{a+c-1}x + {b+d}y')
            distractors.add(f'{(a+c)*(b+d)}xy')
            distractors.discard(answer)
            distractors = list(distractors)[:3]
        
        question_text = f'Simplify: {expr}'
        questions.append(make_question(question_text, answer, distractors, explanation, 4))
    
    return questions


def generate_level_5():
    """Level 5: Collecting like terms - with negatives"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        expr_type = random.choice(['subtract_x', 'mixed_signs', 'three_terms'])
        
        if expr_type == 'subtract_x':
            a = random.randint(5, 10)
            b = random.randint(2, 4)
            expr = f'{a}x - {b}x'
            answer_x = a - b
            answer = f'{answer_x}x'
            explanation = f'Collect like terms: {a}x - {b}x = ({a} - {b})x = {answer_x}x'
            distractors = [f'{a + b}x', f'{a - b + 1}x', f'{a - b - 1}x']
            
        elif expr_type == 'mixed_signs':
            a = random.randint(3, 8)
            b = random.randint(1, 5)
            c = random.randint(2, 6)
            d = random.randint(1, 4)
            expr = f'{a}x - {b} + {c}x - {d}'
            answer_x = a + c
            answer_const = -(b + d)
            answer = format_expression(answer_x, answer_const)
            explanation = f'Collect like terms: ({a}x + {c}x) + (-{b} - {d}) = {answer_x}x - {b + d}'
            distractors = generate_distractors_expression(answer_x, answer_const)
            
        else:  # three_terms
            a = random.randint(4, 8)
            b = random.randint(2, 5)
            c = random.randint(1, 3)
            expr = f'{a}x - {b}x + {c}x'
            answer_x = a - b + c
            answer = f'{answer_x}x'
            explanation = f'Collect like terms: {a}x - {b}x + {c}x = ({a} - {b} + {c})x = {answer_x}x'
            distractors = [f'{a + b + c}x', f'{a - b - c}x', f'{answer_x + 1}x']
        
        question_text = f'Simplify: {expr}'
        questions.append(make_question(question_text, answer, distractors, explanation, 5))
    
    return questions


def generate_level_6():
    """Level 6: Expanding single brackets - a(x + b)"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        sign = random.choice(['+', '-'])
        
        if sign == '+':
            expr = f'{a}(x + {b})'
            answer_x = a
            answer_const = a * b
        else:
            expr = f'{a}(x - {b})'
            answer_x = a
            answer_const = -a * b
        
        answer = format_expression(answer_x, answer_const)
        
        if sign == '+':
            explanation = f'Multiply each term by {a}: {a} × x + {a} × {b} = {a}x + {a * b}'
        else:
            explanation = f'Multiply each term by {a}: {a} × x - {a} × {b} = {a}x - {a * b}'
        
        distractors = generate_distractors_expression(answer_x, answer_const)
        question_text = f'Expand: {expr}'
        
        questions.append(make_question(question_text, answer, distractors, explanation, 6))
    
    return questions


def generate_level_7():
    """Level 7: Expanding single brackets - a(bx + c) with coefficient on x"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        c = random.randint(1, 6)
        sign = random.choice(['+', '-'])
        
        if sign == '+':
            expr = f'{a}({b}x + {c})'
            answer_x = a * b
            answer_const = a * c
        else:
            expr = f'{a}({b}x - {c})'
            answer_x = a * b
            answer_const = -a * c
        
        answer = format_expression(answer_x, answer_const)
        
        if sign == '+':
            explanation = f'Multiply each term by {a}: {a} × {b}x + {a} × {c} = {a*b}x + {a*c}'
        else:
            explanation = f'Multiply each term by {a}: {a} × {b}x - {a} × {c} = {a*b}x - {a*c}'
        
        distractors = generate_distractors_expression(answer_x, answer_const)
        question_text = f'Expand: {expr}'
        
        questions.append(make_question(question_text, answer, distractors, explanation, 7))
    
    return questions


def generate_level_8():
    """Level 8: Expand and simplify - a(x + b) + cx + d"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 6)
        
        # Decide on signs
        b_sign = random.choice(['+', '-'])
        c_sign = random.choice(['+', '-'])
        d_sign = random.choice(['+', '-'])
        
        # Build expression
        b_val = b if b_sign == '+' else -b
        c_val = c if c_sign == '+' else -c
        d_val = d if d_sign == '+' else -d
        
        # Format the expression nicely
        bracket_part = f'(x {b_sign} {b})' if b_sign == '+' else f'(x - {b})'
        c_part = f'+ {c}x' if c_sign == '+' else f'- {c}x'
        d_part = f'+ {d}' if d_sign == '+' else f'- {d}'
        
        expr = f'{a}{bracket_part} {c_part} {d_part}'
        
        # Calculate answer
        # a(x + b_val) + c_val*x + d_val = ax + a*b_val + c_val*x + d_val
        answer_x = a + c_val
        answer_const = a * b_val + d_val
        answer = format_expression(answer_x, answer_const)
        
        step1 = f'{a}x {("+" if a*b_val >= 0 else "-")} {abs(a*b_val)}'
        explanation = f'Expand bracket: {a}(x {b_sign} {b}) = {step1}. Then collect: ({a} {("+" if c_val >= 0 else "-")} {abs(c_val)})x + ({a*b_val} {("+" if d_val >= 0 else "-")} {abs(d_val)}) = {answer}'
        
        distractors = generate_distractors_expression(answer_x, answer_const)
        question_text = f'Expand and simplify: {expr}'
        
        questions.append(make_question(question_text, answer, distractors, explanation, 8))
    
    return questions


def generate_level_9():
    """Level 9: Expanding double brackets - (x + a)(x + b) positive values"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        
        expr = f'(x + {a})(x + {b})'
        
        # (x + a)(x + b) = x² + bx + ax + ab = x² + (a+b)x + ab
        middle_coef = a + b
        const = a * b
        
        answer = f'x² + {middle_coef}x + {const}'
        
        explanation = f'Use FOIL: First: x·x = x². Outer: x·{b} = {b}x. Inner: {a}·x = {a}x. Last: {a}·{b} = {a*b}. Combine: x² + {b}x + {a}x + {a*b} = x² + {a+b}x + {a*b}'
        
        # Generate unique distractors
        distractors = set()
        distractors.add(f'x² + {middle_coef + 1}x + {const}')
        distractors.add(f'x² + {middle_coef - 1}x + {const}')
        distractors.add(f'x² + {middle_coef}x + {const + 1}')
        distractors.add(f'x² + {middle_coef}x + {const - 1}')
        distractors.add(f'x² + {a * b}x + {a + b}')  # Swapped
        distractors.add(f'x² + {middle_coef + 2}x + {const}')
        
        # Remove answer if accidentally added
        distractors.discard(answer)
        distractors = list(distractors)[:3]
        
        question_text = f'Expand: {expr}'
        questions.append(make_question(question_text, answer, distractors, explanation, 9))
    
    return questions


def generate_level_10():
    """Level 10: Expanding double brackets with negatives"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        
        # Ensure a != b to avoid some duplicate issues
        while b == a:
            b = random.randint(1, 6)
        
        # Choose pattern
        pattern = random.choice(['+-', '-+', '--'])
        
        if pattern == '+-':
            expr = f'(x + {a})(x - {b})'
            middle_coef = a - b
            const = -a * b
        elif pattern == '-+':
            expr = f'(x - {a})(x + {b})'
            middle_coef = b - a
            const = -a * b
        else:  # --
            expr = f'(x - {a})(x - {b})'
            middle_coef = -(a + b)
            const = a * b
        
        # Format answer
        if middle_coef > 0:
            middle_part = f'+ {middle_coef}x'
        elif middle_coef < 0:
            middle_part = f'- {abs(middle_coef)}x'
        else:
            middle_part = ''
        
        if const > 0:
            const_part = f'+ {const}'
        else:
            const_part = f'- {abs(const)}'
        
        if middle_part:
            answer = f'x² {middle_part} {const_part}'
        else:
            answer = f'x² {const_part}'
        
        explanation = f'Use FOIL to expand {expr}. Multiply First, Outer, Inner, Last terms and combine like terms to get {answer}'
        
        # Generate unique distractors
        distractors = set()
        
        # Sign errors on middle
        if middle_coef != 0:
            wrong_mid = -middle_coef
            if wrong_mid > 0:
                distractors.add(f'x² + {wrong_mid}x {const_part}')
            else:
                distractors.add(f'x² - {abs(wrong_mid)}x {const_part}')
        
        # Sign errors on constant
        wrong_const = -const
        if wrong_const > 0:
            if middle_part:
                distractors.add(f'x² {middle_part} + {wrong_const}')
            else:
                distractors.add(f'x² + {wrong_const}')
        else:
            if middle_part:
                distractors.add(f'x² {middle_part} - {abs(wrong_const)}')
            else:
                distractors.add(f'x² - {abs(wrong_const)}')
        
        # Wrong calculation
        distractors.add(f'x² + {a + b}x + {a * b}')
        distractors.add(f'x² - {a + b}x + {a * b}')
        distractors.add(f'x² + {abs(a - b)}x - {a * b}')
        
        # Remove answer if present
        distractors.discard(answer)
        distractors = list(distractors)[:3]
        
        # Fill if needed
        while len(distractors) < 3:
            rand_mid = random.randint(-10, 10)
            rand_const = random.randint(-20, 20)
            if rand_mid > 0:
                mid_str = f'+ {rand_mid}x'
            elif rand_mid < 0:
                mid_str = f'- {abs(rand_mid)}x'
            else:
                mid_str = ''
            if rand_const > 0:
                const_str = f'+ {rand_const}'
            else:
                const_str = f'- {abs(rand_const)}'
            
            new_dist = f'x² {mid_str} {const_str}'.strip()
            if new_dist != answer and new_dist not in distractors:
                distractors.append(new_dist)
        
        question_text = f'Expand: {expr}'
        questions.append(make_question(question_text, answer, distractors, explanation, 10))
    
    return questions


def generate_level_11():
    """Level 11: Factorising - taking out common factors"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        factor_type = random.choice(['numeric', 'variable', 'both'])
        
        if factor_type == 'numeric':
            common = random.randint(2, 6)
            a = random.randint(2, 6)  # Ensure a >= 2 to avoid 1x issues
            b = random.randint(1, 5)
            expr = f'{common * a}x + {common * b}'
            answer = f'{common}({a}x + {b})'
            explanation = f'Find HCF of {common * a} and {common * b}, which is {common}. Factor out: {common}({a}x + {b})'
            distractors = set()
            distractors.add(f'{common}({a}x + {b + 1})')
            distractors.add(f'{common}({a}x + {b - 1})' if b > 1 else f'{common}({a}x + {b + 2})')
            distractors.add(f'{common + 1}({a}x + {b})')
            distractors.add(f'{common - 1}({a}x + {b})' if common > 2 else f'{common + 2}({a}x + {b})')
            distractors.discard(answer)
            distractors = list(distractors)[:3]
            
        elif factor_type == 'variable':
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            expr = f'{a}x² + {b}x'
            answer = f'x({a}x + {b})'
            explanation = f'Both terms have x as a factor. Factor out x: x({a}x + {b})'
            distractors = set()
            distractors.add(f'x({a}x + {b + 1})')
            distractors.add(f'x({a}x + {b - 1})' if b > 2 else f'x({a}x + {b + 2})')
            distractors.add(f'{a}x(x + {b})')
            distractors.add(f'x²({a} + {b})')
            distractors.discard(answer)
            distractors = list(distractors)[:3]
            
        else:  # both
            common = random.randint(2, 4)
            a = random.randint(2, 5)
            b = random.randint(1, 4)
            expr = f'{common * a}x² + {common * b}x'
            answer = f'{common}x({a}x + {b})'
            explanation = f'HCF is {common}x. Factor out: {common}x({a}x + {b})'
            distractors = set()
            distractors.add(f'{common}({a}x² + {b}x)')
            distractors.add(f'x({common * a}x + {common * b})')
            distractors.add(f'{common}x({a}x + {b + 1})')
            distractors.add(f'{common}x({a + 1}x + {b})')
            distractors.discard(answer)
            distractors = list(distractors)[:3]
        
        question_text = f'Factorise: {expr}'
        questions.append(make_question(question_text, answer, distractors, explanation, 11))
    
    return questions


def generate_level_12():
    """Level 12: Mixed problems and multi-step"""
    questions = []
    
    for _ in range(QUESTIONS_PER_LEVEL):
        problem_type = random.choice(['expand_simplify', 'factorise_solve', 'expression_equals', 'area_algebra'])
        
        if problem_type == 'expand_simplify':
            a = random.randint(2, 4)
            b = random.randint(1, 4)
            c = random.randint(2, 4)
            d = random.randint(1, 4)
            expr = f'{a}(x + {b}) + {c}(x - {d})'
            
            answer_x = a + c
            answer_const = a * b - c * d
            answer = format_expression(answer_x, answer_const)
            
            explanation = f'Expand each bracket: {a}x + {a*b} + {c}x - {c*d}. Collect: {answer_x}x + {a*b - c*d}'
            distractors = generate_distractors_expression(answer_x, answer_const)
            question_text = f'Expand and simplify: {expr}'
            
        elif problem_type == 'factorise_solve':
            a = random.randint(2, 5)
            b = random.randint(1, 6)
            # Ensure a != b to avoid (x+a)(x+a) type answers
            while b == a:
                b = random.randint(1, 6)
            
            product = a * b
            sum_val = a + b
            expr = f'x² + {sum_val}x + {product}'
            
            # Ensure consistent ordering (smaller first)
            if a > b:
                a, b = b, a
            
            answer = f'(x + {a})(x + {b})'
            explanation = f'Find two numbers that multiply to {product} and add to {sum_val}. These are {a} and {b}. So: (x + {a})(x + {b})'
            
            distractors = set()
            distractors.add(f'(x + {a})(x + {b + 1})')
            distractors.add(f'(x + {a + 1})(x + {b})')
            distractors.add(f'(x + {a - 1})(x + {b})' if a > 1 else f'(x + {a})(x + {b - 1})')
            distractors.add(f'(x + {product})(x + 1)')
            distractors.discard(answer)
            distractors = list(distractors)[:3]
            question_text = f'Factorise: {expr}'
            
        elif problem_type == 'expression_equals':
            a = random.randint(2, 5)
            b = random.randint(1, 6)
            c = random.randint(2, 5)
            x_val = random.randint(2, 8)
            result = a * x_val + b
            
            question_text = f'If {a}x + {b} = {result}, find the value of {c}x'
            answer = c * x_val
            explanation = f'Solve for x: {a}x = {result} - {b} = {result - b}, so x = {x_val}. Then {c}x = {c} × {x_val} = {answer}'
            distractors = generate_distractors_numeric(answer)
            distractors = [str(d) for d in distractors]
            answer = str(answer)
            
        else:  # area_algebra
            length = random.randint(2, 5)
            width_expr = random.randint(2, 5)  # Ensure >= 2 to get different distractors
            
            question_text = f'A rectangle has length (x + {length}) and width {width_expr}. Write an expression for its area.'
            answer = f'{width_expr}x + {width_expr * length}'
            explanation = f'Area = length × width = {width_expr}(x + {length}) = {width_expr}x + {width_expr * length}'
            
            distractors = set()
            distractors.add(f'{width_expr}x + {length}')
            distractors.add(f'{width_expr + length}x')
            distractors.add(f'x + {width_expr * length}')
            distractors.add(f'{width_expr}x + {width_expr * length + 1}')
            distractors.discard(answer)
            distractors = list(distractors)[:3]
        
        questions.append(make_question(question_text, answer, distractors, explanation, 12))
    
    return questions


# ==================== VALIDATION ====================

def validate_questions(questions):
    """Validate all questions for common issues"""
    issues = []
    
    for i, q in enumerate(questions):
        qtext = q['question_text']
        
        # Check for \n in text
        if '\\n' in qtext or '\n' in qtext:
            issues.append(f"Q{i+1} L{q['difficulty']}: Contains newline in question text")
        
        # Check options for \n
        for opt in ['option_a', 'option_b', 'option_c', 'option_d']:
            if '\\n' in q[opt] or '\n' in q[opt]:
                issues.append(f"Q{i+1} L{q['difficulty']}: Contains newline in {opt}")
        
        # Check explanation
        if '\\n' in q['explanation']:
            issues.append(f"Q{i+1} L{q['difficulty']}: Contains \\n in explanation")
        
        # Check for empty options
        for opt in ['option_a', 'option_b', 'option_c', 'option_d']:
            if not q[opt] or q[opt].strip() == '':
                issues.append(f"Q{i+1} L{q['difficulty']}: Empty {opt}")
        
        # Check for duplicate options
        opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(opts) != len(set(opts)):
            issues.append(f"Q{i+1} L{q['difficulty']}: Duplicate options")
    
    return issues


def print_validation_summary(questions):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("📋 VALIDATION SUMMARY")
    print("=" * 60)
    
    # Count by level
    level_counts = {}
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    print(f"Total questions: {len(questions)}")
    print("\nBy level:")
    for level in sorted(level_counts.keys()):
        status = "✓" if level_counts[level] >= QUESTIONS_PER_LEVEL else "✗"
        print(f"  Level {level}: {level_counts[level]} questions {status}")
    
    # Run validation
    issues = validate_questions(questions)
    
    if issues:
        print(f"\n⚠️ Found {len(issues)} issues:")
        for issue in issues[:10]:
            print(f"  - {issue}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
        return False
    else:
        print("\n✅ All questions passed validation!")
        return True


# ==================== DATABASE ====================

def insert_questions(questions, db_path):
    """Insert questions into database"""
    print(f"\n📥 Inserting {len(questions)} questions...")
    
    # Remove duplicates
    seen = set()
    unique_questions = []
    for q in questions:
        key = (q['topic'], q['difficulty'], q['question_text'][:100])
        if key not in seen:
            seen.add(key)
            unique_questions.append(q)
    
    if len(unique_questions) < len(questions):
        print(f"⚠️ Removed {len(questions) - len(unique_questions)} duplicate questions")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check existing
    cursor.execute("SELECT topic, COUNT(*) FROM questions_adaptive GROUP BY topic")
    existing = cursor.fetchall()
    if existing:
        print(f"📁 Existing topics: {[(r[0], r[1]) for r in existing]}")
    
    # Delete existing for this topic
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (TOPIC,))
    deleted = cursor.rowcount
    conn.commit()
    print(f"🗑️ Deleted {deleted} existing questions for '{TOPIC}'")
    
    # Insert new questions
    insert_sql = """
        INSERT INTO questions_adaptive 
        (question_text, option_a, option_b, option_c, option_d,
         correct_answer, topic, difficulty_level, difficulty_band, mode,
         explanation, image_svg, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
    """
    
    inserted = 0
    errors = 0
    for q in unique_questions:
        try:
            cursor.execute(insert_sql, (
                q['question_text'],
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_idx'],
                q['topic'],
                q['difficulty'],
                q['difficulty_band'],
                q['mode'],
                q['explanation'],
                q.get('image_svg')  # Will be None - no visuals!
            ))
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"   ⚠️ Error L{q['difficulty']}: {str(e)[:60]}")
    
    conn.commit()
    conn.close()
    
    print(f"✅ Inserted {inserted} questions, {errors} errors")
    return inserted, errors


# ==================== MAIN ====================

def main():
    """Main function to generate and insert questions"""
    print("=" * 60)
    print("🎓 AgentMath - Introductory Algebra Generator")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Target: {QUESTIONS_PER_LEVEL} questions × 12 levels = 600 total")
    print(f"Visuals: NONE (preventing answer reveal)")
    print()
    
    all_questions = []
    
    # Generate questions for each level
    generators = [
        generate_level_1,
        generate_level_2,
        generate_level_3,
        generate_level_4,
        generate_level_5,
        generate_level_6,
        generate_level_7,
        generate_level_8,
        generate_level_9,
        generate_level_10,
        generate_level_11,
        generate_level_12,
    ]
    
    for level, generator in enumerate(generators, 1):
        print(f"Generating Level {level}...", end=" ")
        try:
            questions = generator()
            all_questions.extend(questions)
            print(f"✓ {len(questions)} questions")
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()
    
    # Validate
    is_valid = print_validation_summary(all_questions)
    
    if not is_valid:
        print("\n⚠️ Validation failed. Fix errors before inserting.")
        response = input("Continue anyway? (y/N): ").strip().lower()
        if response != 'y':
            print("Aborted.")
            return
    
    # Insert into database
    print("\n" + "=" * 60)
    print("💾 DATABASE INSERTION")
    print("=" * 60)
    print(f"Database: {DB_PATH}")
    
    response = input("Insert questions into database? (y/N): ").strip().lower()
    if response == 'y':
        try:
            inserted, errors = insert_questions(all_questions, DB_PATH)
            print(f"\n🎉 Complete! {inserted} questions added to database.")
        except Exception as e:
            print(f"\n❌ Database error: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("Skipped database insertion.")
    
    # Verification query
    print("\n📋 Verification SQL:")
    print(f"""
    SELECT difficulty_level, COUNT(*) as count
    FROM questions_adaptive 
    WHERE topic = '{TOPIC}'
    GROUP BY difficulty_level
    ORDER BY difficulty_level;
    """)


if __name__ == "__main__":
    main()
