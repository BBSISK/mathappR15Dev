#!/usr/bin/env python3
"""
AgentMath - Introductory Algebra Question Generator v2
SEC Junior Cycle Aligned - JC Exam Mode

Version: 2.0
Date: 13 December 2025
Fixes Applied:
  - NO \n in question_text (Methodology v2.2 Mistake 9)
  - SVG visuals pose PROBLEMS, not show answers (Methodology v2.2 Mistake 10)
  - All questions use clean single-line format

Based on SEC Papers 2022-2025:
- Algebraic expressions and simplification
- Substitution problems
- Expanding and factorising
- Problem-solving with algebra

Level Structure:
  L1-3:   Foundation (Variables, Like Terms, Simplifying)
  L4-6:   Ordinary (Substitution, Expanding, Single Brackets)
  L7-9:   Higher (Double Brackets, Factorising, Algebraic Fractions)
  L10-12: Mastery (Complex, Problem Solving, SEC Exam Style)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os
from fractions import Fraction

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'introductory_algebra'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Siobhán', 
               'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn', 'Éabha', 'Tadhg',
               'Ciara', 'Rian', 'Méabh', 'Cillian', 'Aoibhín', 'Eoin']

# Variables for algebra
VARIABLES = ['x', 'y', 'a', 'b', 'n', 'm', 'p', 'k']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    
    # Filter out duplicates and same-as-correct
    unique_wrong = []
    for w in wrong_list:
        w_str = str(w)
        if w_str != correct_str and w_str not in unique_wrong:
            unique_wrong.append(w_str)
    
    options = [correct_str] + unique_wrong[:3]
    
    # Ensure we have exactly 4 unique options
    fallback_idx = 1
    while len(set(options)) < 4:
        fallback = f"{correct_str}_{fallback_idx}"
        if fallback not in options:
            options.append(fallback)
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    
    return options, correct_idx


def format_term(coef, var, first=False):
    """Format algebraic term properly: 2x, -3y, x, -x"""
    if coef == 0:
        return ""
    if var == "":
        # Constant term
        if first:
            return str(coef)
        elif coef > 0:
            return f"+ {coef}"
        else:
            return f"- {abs(coef)}"
    else:
        # Variable term
        if coef == 1:
            coef_str = ""
        elif coef == -1:
            coef_str = "-"
        else:
            coef_str = str(coef)
        
        if first:
            return f"{coef_str}{var}"
        elif coef > 0:
            if coef == 1:
                return f"+ {var}"
            return f"+ {coef}{var}"
        else:
            if coef == -1:
                return f"- {var}"
            return f"- {abs(coef)}{var}"


def generate_shape_algebra_svg(shape1_expr, shape2_expr, total, shape1='circle', shape2='square'):
    """Generate SVG showing shape algebra puzzle - student solves for unknown"""
    colors = {'circle': '#dbeafe', 'square': '#dcfce7', 'triangle': '#fef3c7'}
    
    svg = '<svg viewBox="0 0 280 70" width="280" height="70">'
    
    # First shape
    if shape1 == 'circle':
        svg += f'<circle cx="35" cy="35" r="28" fill="{colors["circle"]}" stroke="#2563eb" stroke-width="2"/>'
    else:
        svg += f'<rect x="7" y="7" width="56" height="56" fill="{colors["square"]}" stroke="#16a34a" stroke-width="2"/>'
    svg += f'<text x="35" y="40" text-anchor="middle" font-size="14" font-weight="bold">{shape1_expr}</text>'
    
    # Plus sign
    svg += '<text x="85" y="42" text-anchor="middle" font-size="24" fill="#374151">+</text>'
    
    # Second shape  
    if shape2 == 'square':
        svg += f'<rect x="107" y="7" width="56" height="56" fill="{colors["square"]}" stroke="#16a34a" stroke-width="2"/>'
    else:
        svg += f'<circle cx="135" cy="35" r="28" fill="{colors["circle"]}" stroke="#2563eb" stroke-width="2"/>'
    svg += f'<text x="135" y="40" text-anchor="middle" font-size="14" font-weight="bold">{shape2_expr}</text>'
    
    # Equals sign
    svg += '<text x="185" y="42" text-anchor="middle" font-size="24" fill="#374151">=</text>'
    
    # Total
    svg += f'<rect x="207" y="7" width="56" height="56" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2" rx="8"/>'
    svg += f'<text x="235" y="42" text-anchor="middle" font-size="18" font-weight="bold">{total}</text>'
    
    svg += '</svg>'
    return svg


def generate_balance_svg(left_expr, right_value):
    """Generate balance/scale SVG showing equation - student finds unknown"""
    svg = '<svg viewBox="0 0 300 80" width="300" height="80">'
    
    # Left pan
    svg += '<rect x="20" y="20" width="100" height="45" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="5"/>'
    svg += f'<text x="70" y="48" text-anchor="middle" font-size="16" font-weight="bold">{left_expr}</text>'
    
    # Balance fulcrum
    svg += '<polygon points="150,70 140,80 160,80" fill="#6b7280"/>'
    svg += '<line x1="70" y1="65" x2="230" y2="65" stroke="#6b7280" stroke-width="3"/>'
    
    # Right pan
    svg += '<rect x="180" y="20" width="100" height="45" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>'
    svg += f'<text x="230" y="48" text-anchor="middle" font-size="18" font-weight="bold">{right_value}</text>'
    
    svg += '</svg>'
    return svg


def generate_perimeter_svg(length_expr, width_expr):
    """Generate rectangle with algebraic dimensions - student calculates perimeter"""
    svg = '<svg viewBox="0 0 220 140" width="220" height="140">'
    
    # Rectangle
    svg += '<rect x="30" y="30" width="160" height="80" fill="none" stroke="#6366f1" stroke-width="3"/>'
    
    # Length label (top)
    svg += f'<text x="110" y="22" text-anchor="middle" font-size="14" font-weight="bold" fill="#4f46e5">{length_expr}</text>'
    
    # Width label (right)
    svg += f'<text x="200" y="75" text-anchor="start" font-size="14" font-weight="bold" fill="#4f46e5">{width_expr}</text>'
    
    svg += '</svg>'
    return svg


def generate_expression_box_svg(expression):
    """Generate simple box with expression to simplify"""
    svg = '<svg viewBox="0 0 200 50" width="200" height="50">'
    svg += '<rect x="5" y="5" width="190" height="40" fill="#f0f9ff" stroke="#0ea5e9" stroke-width="2" rx="8"/>'
    svg += f'<text x="100" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#0369a1">{expression}</text>'
    svg += '</svg>'
    return svg


# ============================================================
# LEVEL 1: Variables & Terms (Foundation)
# ============================================================

def generate_level_1():
    """Variables & Terms - Understanding what variables represent"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'identify_variable',
        'shape_algebra',
        'term_meaning',
        'coefficient_identify',
        'variable_value'
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'identify_variable':
                # What does the variable represent?
                var = random.choice(['x', 'y', 'n'])
                contexts = [
                    (f"If {var} represents a number, what is 2{var}?", "Two times the number", 
                     ["The number plus 2", "The number minus 2", "Half the number"]),
                    (f"In the expression 5{var}, what does {var} represent?", "An unknown number",
                     ["The number 5", "The answer", "A fixed value"]),
                    (f"If {var} = 4, what type of value is {var}?", "A variable",
                     ["A constant", "An operator", "An equation"])
                ]
                context = random.choice(contexts)
                q_text = context[0]
                correct = context[1]
                wrong = context[2]
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                explanation = f"Step 1: A variable like {var} represents an unknown number\nStep 2: It can take different values\nAnswer: {correct}"
                svg = None
                
            elif q_type == 'shape_algebra':
                # Shape puzzles where shapes have values
                val1 = random.randint(2, 8)
                val2 = random.randint(2, 8)
                total = val1 + val2
                
                q_text = f"If ○ = {val1}, find the value of □ when ○ + □ = {total}"
                correct = str(val2)
                wrong = [str(total), str(val1), str(total - 1)]
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                svg = generate_shape_algebra_svg(str(val1), "?", total)
                explanation = f"Step 1: ○ + □ = {total}\nStep 2: {val1} + □ = {total}\nStep 3: □ = {total} - {val1} = {val2}\nAnswer: {val2}"
                
            elif q_type == 'term_meaning':
                # Understanding algebraic terms
                coef = random.randint(2, 9)
                var = random.choice(['x', 'y', 'n'])
                
                meanings = [
                    (f"What does {coef}{var} mean?", f"{coef} multiplied by {var}",
                     [f"{coef} added to {var}", f"{coef} divided by {var}", f"{var} to the power of {coef}"]),
                    (f"The expression {coef}{var} means:", f"{coef} times {var}",
                     [f"{coef} plus {var}", f"{var} minus {coef}", f"{var} divided by {coef}"])
                ]
                meaning = random.choice(meanings)
                q_text = meaning[0]
                correct = meaning[1]
                wrong = meaning[2]
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                svg = generate_expression_box_svg(f"{coef}{var}")
                explanation = f"Step 1: In algebra, {coef}{var} means {coef} × {var}\nStep 2: The number next to the variable is multiplied\nAnswer: {correct}"
                
            elif q_type == 'coefficient_identify':
                # Identify the coefficient
                coef = random.randint(2, 12)
                var = random.choice(['x', 'y', 'a', 'b'])
                
                q_text = f"What is the coefficient in the term {coef}{var}?"
                correct = str(coef)
                wrong = [var, str(coef + 1), str(coef - 1)]
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                svg = None
                explanation = f"Step 1: The coefficient is the number in front of the variable\nStep 2: In {coef}{var}, the coefficient is {coef}\nAnswer: {coef}"
                
            else:  # variable_value
                # Simple substitution preview
                var = random.choice(['x', 'y', 'n'])
                val = random.randint(2, 6)
                coef = random.randint(2, 5)
                result = coef * val
                
                q_text = f"If {var} = {val}, what is {coef}{var}?"
                correct = str(result)
                wrong = [str(coef + val), str(coef * val + 1), str(coef * val - 1)]
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                svg = None
                explanation = f"Step 1: {coef}{var} means {coef} × {var}\nStep 2: Substitute {var} = {val}: {coef} × {val}\nStep 3: Calculate: {coef} × {val} = {result}\nAnswer: {result}"
            
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
                'image_svg': svg,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 2: Like Terms (Foundation)
# ============================================================

def generate_level_2():
    """Like Terms - Identifying terms that can be combined"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['identify_like', 'not_like', 'group_like', 'count_like'])
        
        try:
            if q_type == 'identify_like':
                # Which terms are like terms?
                var = random.choice(['x', 'y', 'a'])
                c1, c2, c3 = random.sample(range(2, 10), 3)
                
                scenarios = [
                    (f"Which are like terms: {c1}{var}, {c2}y, {c3}{var}?", 
                     f"{c1}{var} and {c3}{var}", 
                     [f"{c1}{var} and {c2}y", f"{c2}y and {c3}{var}", "None of them"]),
                    (f"Identify the like terms: {c1}x, {c2}x², {c3}x",
                     f"{c1}x and {c3}x",
                     [f"{c1}x and {c2}x²", f"{c2}x² and {c3}x", "All of them"])
                ]
                scenario = random.choice(scenarios)
                q_text = scenario[0]
                correct = scenario[1]
                wrong = scenario[2]
                
            elif q_type == 'not_like':
                # Which term is NOT like the others?
                var = random.choice(['x', 'y', 'n'])
                c1, c2, c3 = random.sample(range(2, 9), 3)
                odd_term = random.choice([f"{c1}y", f"{c2}", f"{c3}x²"])
                
                q_text = f"Which term is NOT like 3{var} and 5{var}?"
                options_pool = [f"2{var}", f"7{var}", odd_term, f"-{var}"]
                correct = odd_term
                wrong = [f"2{var}", f"7{var}", f"-{var}"]
                
            elif q_type == 'group_like':
                # How many groups of like terms?
                terms = ["3x", "2y", "5x", "4", "7y", "2"]
                random.shuffle(terms)
                term_str = ", ".join(terms[:4])
                
                q_text = f"How many pairs of like terms are in: {term_str}?"
                # Count pairs (x terms, y terms, constants)
                correct = "2"
                wrong = ["1", "3", "4"]
                
            else:  # count_like
                # Count like terms
                var = random.choice(['a', 'b', 'x'])
                terms_list = [f"2{var}", f"3y", f"5{var}", f"4", f"-{var}"]
                random.shuffle(terms_list)
                
                q_text = f"How many terms in '{', '.join(terms_list[:4])}' are like terms with {var}?"
                # Count terms with the chosen variable
                count = sum(1 for t in terms_list[:4] if var in t)
                correct = str(count)
                wrong = [str(count + 1), str(count - 1) if count > 1 else "0", str(4)]
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            explanation = f"Step 1: Like terms have the same variable with the same power\nStep 2: Constants (numbers only) are like terms with each other\nStep 3: Terms with different variables or powers are NOT like terms\nAnswer: {correct}"
            
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
# LEVEL 3: Simplifying (Foundation)
# ============================================================

def generate_level_3():
    """Simplifying - Collecting like terms"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['add_like', 'subtract_like', 'mixed_simple', 'two_vars'])
        
        try:
            var = random.choice(['x', 'y', 'a', 'n'])
            
            if q_type == 'add_like':
                # Simple addition of like terms: 3x + 5x
                c1 = random.randint(2, 8)
                c2 = random.randint(2, 8)
                result = c1 + c2
                
                expr = f"{c1}{var} + {c2}{var}"
                q_text = f"Simplify: {expr}"
                correct = f"{result}{var}"
                wrong = [f"{c1 * c2}{var}", f"{result}", f"{c1 + c2 + 1}{var}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Both terms have {var}, so they are like terms\nStep 2: Add the coefficients: {c1} + {c2} = {result}\nStep 3: Keep the variable: {result}{var}\nAnswer: {result}{var}"
                
            elif q_type == 'subtract_like':
                # Subtraction: 8x - 3x
                c1 = random.randint(5, 12)
                c2 = random.randint(2, c1 - 1)
                result = c1 - c2
                
                expr = f"{c1}{var} - {c2}{var}"
                q_text = f"Simplify: {expr}"
                correct = f"{result}{var}"
                wrong = [f"{c1 + c2}{var}", f"{result}", f"{c1 * c2}{var}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Both terms have {var}, so they are like terms\nStep 2: Subtract the coefficients: {c1} - {c2} = {result}\nStep 3: Keep the variable: {result}{var}\nAnswer: {result}{var}"
                
            elif q_type == 'mixed_simple':
                # Three terms: 2x + 5x + 3x
                c1 = random.randint(2, 5)
                c2 = random.randint(2, 5)
                c3 = random.randint(2, 5)
                result = c1 + c2 + c3
                
                expr = f"{c1}{var} + {c2}{var} + {c3}{var}"
                q_text = f"Simplify: {expr}"
                correct = f"{result}{var}"
                wrong = [f"{c1 * c2 * c3}{var}", f"{result}", f"{result + 1}{var}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: All terms have {var}, so they are all like terms\nStep 2: Add coefficients: {c1} + {c2} + {c3} = {result}\nStep 3: Keep the variable: {result}{var}\nAnswer: {result}{var}"
                
            else:  # two_vars
                # Two different variables: 3x + 2y + 4x
                c1 = random.randint(2, 6)
                c2 = random.randint(2, 6)
                c3 = random.randint(2, 6)
                var2 = 'y' if var == 'x' else 'x'
                result_var1 = c1 + c3
                
                expr = f"{c1}{var} + {c2}{var2} + {c3}{var}"
                q_text = f"Simplify: {expr}"
                correct = f"{result_var1}{var} + {c2}{var2}"
                wrong = [f"{c1 + c2 + c3}{var}", f"{result_var1}{var}{var2}", f"{c1}{var} + {c2 + c3}{var2}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Identify like terms: {c1}{var} and {c3}{var} are like terms\nStep 2: {c2}{var2} has a different variable\nStep 3: Combine: {c1} + {c3} = {result_var1}, so {result_var1}{var} + {c2}{var2}\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 4: Substitution (Ordinary)
# ============================================================

def generate_level_4():
    """Substitution - Replacing variables with values"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['simple_sub', 'add_sub', 'multiply_add', 'two_var_sub'])
        
        try:
            if q_type == 'simple_sub':
                # Simple: Find 3x when x = 4
                coef = random.randint(2, 8)
                val = random.randint(2, 9)
                var = random.choice(['x', 'y', 'n', 'a'])
                result = coef * val
                
                q_text = f"If {var} = {val}, find the value of {coef}{var}"
                correct = str(result)
                wrong = [str(coef + val), str(result + 1), str(result - 1)]
                
                svg = generate_expression_box_svg(f"{coef}{var} when {var} = {val}")
                explanation = f"Step 1: {coef}{var} means {coef} × {var}\nStep 2: Substitute {var} = {val}: {coef} × {val}\nStep 3: Calculate: {coef} × {val} = {result}\nAnswer: {result}"
                
            elif q_type == 'add_sub':
                # Expression with addition: 2x + 5 when x = 3
                coef = random.randint(2, 6)
                const = random.randint(2, 10)
                val = random.randint(2, 8)
                var = random.choice(['x', 'y', 'n'])
                result = coef * val + const
                
                expr = f"{coef}{var} + {const}"
                q_text = f"Find the value of {expr} when {var} = {val}"
                correct = str(result)
                wrong = [str(coef * val), str(coef + const + val), str(result + 1)]
                
                svg = generate_expression_box_svg(f"{expr}")
                explanation = f"Step 1: Substitute {var} = {val} into {expr}\nStep 2: {coef}({val}) + {const}\nStep 3: {coef * val} + {const} = {result}\nAnswer: {result}"
                
            elif q_type == 'multiply_add':
                # Expression with subtraction: 3x - 2 when x = 5
                coef = random.randint(2, 6)
                const = random.randint(2, 8)
                val = random.randint(3, 10)
                var = random.choice(['x', 'a', 'n'])
                
                if coef * val > const:
                    result = coef * val - const
                    expr = f"{coef}{var} - {const}"
                else:
                    result = coef * val + const
                    expr = f"{coef}{var} + {const}"
                
                q_text = f"Evaluate {expr} when {var} = {val}"
                correct = str(result)
                wrong = [str(result + 1), str(result - 1), str(coef + val)]
                
                svg = None
                explanation = f"Step 1: Substitute {var} = {val} into {expr}\nStep 2: Calculate {coef} × {val} = {coef * val}\nStep 3: Then add/subtract the constant\nAnswer: {result}"
                
            else:  # two_var_sub
                # Two variables: x + y when x = 3, y = 4
                val1 = random.randint(2, 8)
                val2 = random.randint(2, 8)
                result = val1 + val2
                
                q_text = f"If x = {val1} and y = {val2}, find x + y"
                correct = str(result)
                wrong = [str(val1 * val2), str(result + 1), str(result - 1)]
                
                svg = generate_balance_svg("x + y", "?")
                explanation = f"Step 1: Substitute x = {val1} and y = {val2}\nStep 2: x + y = {val1} + {val2}\nStep 3: Calculate: {val1} + {val2} = {result}\nAnswer: {result}"
            
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
                'image_svg': svg,
                'difficulty': 4,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 5: Expanding Brackets (Ordinary)
# ============================================================

def generate_level_5():
    """Expanding Brackets - Single term times bracket"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['num_bracket', 'var_bracket', 'neg_bracket'])
        
        try:
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'num_bracket':
                # Number times bracket: 2(x + 3)
                mult = random.randint(2, 6)
                coef = random.randint(1, 4)
                const = random.randint(2, 8)
                
                if coef == 1:
                    expr = f"{mult}({var} + {const})"
                    result_coef = mult
                else:
                    expr = f"{mult}({coef}{var} + {const})"
                    result_coef = mult * coef
                result_const = mult * const
                
                correct = f"{result_coef}{var} + {result_const}"
                q_text = f"Expand: {expr}"
                wrong = [f"{mult}{var} + {const}", f"{result_coef}{var} + {const}", f"{mult + coef}{var} + {result_const}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Multiply {mult} by each term in the bracket\nStep 2: {mult} × {coef if coef > 1 else ''}{var} = {result_coef}{var}\nStep 3: {mult} × {const} = {result_const}\nAnswer: {correct}"
                
            elif q_type == 'var_bracket':
                # Variable times bracket: x(x + 2)
                const = random.randint(2, 7)
                
                expr = f"{var}({var} + {const})"
                correct = f"{var}² + {const}{var}"
                q_text = f"Expand: {expr}"
                wrong = [f"2{var} + {const}", f"{var}² + {const}", f"{var} + {const}{var}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Multiply {var} by each term in the bracket\nStep 2: {var} × {var} = {var}²\nStep 3: {var} × {const} = {const}{var}\nAnswer: {correct}"
                
            else:  # neg_bracket
                # Negative: -2(x + 3) or 3(x - 2)
                mult = random.randint(2, 5)
                const = random.randint(2, 7)
                
                if random.choice([True, False]):
                    expr = f"{mult}({var} - {const})"
                    result_const = mult * const
                    correct = f"{mult}{var} - {result_const}"
                else:
                    expr = f"-{mult}({var} + {const})"
                    result_const = mult * const
                    correct = f"-{mult}{var} - {result_const}"
                
                q_text = f"Expand: {expr}"
                wrong = [f"{mult}{var} + {const}", f"-{mult}{var} + {result_const}", f"{mult}{var} - {const}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Multiply each term by the multiplier\nStep 2: Remember the sign rules\nStep 3: Write the expanded form\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 5,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 6: Single Brackets (Ordinary)
# ============================================================

def generate_level_6():
    """Single Brackets - More complex single bracket expansion"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['coef_bracket', 'combine_brackets', 'subtract_brackets'])
        
        try:
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'coef_bracket':
                # Coefficient in bracket: 3(2x + 4)
                mult = random.randint(2, 5)
                inner_coef = random.randint(2, 4)
                const = random.randint(2, 6)
                
                result_coef = mult * inner_coef
                result_const = mult * const
                
                expr = f"{mult}({inner_coef}{var} + {const})"
                q_text = f"Expand: {expr}"
                correct = f"{result_coef}{var} + {result_const}"
                wrong = [f"{mult + inner_coef}{var} + {const}", f"{result_coef}{var} + {const}", f"{inner_coef}{var} + {result_const}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: {mult} × {inner_coef}{var} = {result_coef}{var}\nStep 2: {mult} × {const} = {result_const}\nAnswer: {correct}"
                
            elif q_type == 'combine_brackets':
                # Two brackets: 2(x + 1) + 3(x + 2)
                m1, m2 = random.randint(2, 4), random.randint(2, 4)
                c1, c2 = random.randint(1, 4), random.randint(1, 4)
                
                result_coef = m1 + m2
                result_const = m1 * c1 + m2 * c2
                
                expr = f"{m1}({var} + {c1}) + {m2}({var} + {c2})"
                q_text = f"Expand and simplify: {expr}"
                correct = f"{result_coef}{var} + {result_const}"
                wrong = [f"{m1 + m2}{var} + {c1 + c2}", f"{m1 * m2}{var} + {result_const}", f"{result_coef}{var} + {c1 * c2}"]
                
                svg = None
                explanation = f"Step 1: Expand {m1}({var} + {c1}) = {m1}{var} + {m1 * c1}\nStep 2: Expand {m2}({var} + {c2}) = {m2}{var} + {m2 * c2}\nStep 3: Combine: {m1}{var} + {m2}{var} = {result_coef}{var}, {m1*c1} + {m2*c2} = {result_const}\nAnswer: {correct}"
                
            else:  # subtract_brackets
                # Subtraction: 5(x + 2) - 2(x + 1)
                m1, m2 = random.randint(4, 6), random.randint(2, 3)
                c1, c2 = random.randint(2, 5), random.randint(1, 3)
                
                result_coef = m1 - m2
                result_const = m1 * c1 - m2 * c2
                
                expr = f"{m1}({var} + {c1}) - {m2}({var} + {c2})"
                q_text = f"Expand and simplify: {expr}"
                correct = f"{result_coef}{var} + {result_const}"
                wrong = [f"{m1 + m2}{var} + {c1 - c2}", f"{result_coef}{var} + {c1 + c2}", f"{m1 - m2}{var} - {result_const}"]
                
                svg = None
                explanation = f"Step 1: Expand {m1}({var} + {c1}) = {m1}{var} + {m1 * c1}\nStep 2: Expand {m2}({var} + {c2}) = {m2}{var} + {m2 * c2}\nStep 3: Subtract: {m1}{var} - {m2}{var} = {result_coef}{var}, {m1*c1} - {m2*c2} = {result_const}\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 6,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 7: Double Brackets (Higher)
# ============================================================

def generate_level_7():
    """Double Brackets - FOIL method (x + a)(x + b)"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['foil_positive', 'foil_mixed', 'foil_negative', 'perfect_square'])
        
        try:
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'foil_positive':
                # (x + 2)(x + 3) - both positive
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                
                middle = a + b
                last = a * b
                
                expr = f"({var} + {a})({var} + {b})"
                q_text = f"Expand: {expr}"
                correct = f"{var}² + {middle}{var} + {last}"
                wrong = [f"{var}² + {a * b}{var} + {a + b}", f"2{var}² + {middle}{var} + {last}", f"{var}² + {middle}{var} - {last}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Use FOIL - First: {var} × {var} = {var}²\nStep 2: Outer + Inner: {a}{var} + {b}{var} = {middle}{var}\nStep 3: Last: {a} × {b} = {last}\nAnswer: {correct}"
                
            elif q_type == 'foil_mixed':
                # (x + 3)(x - 2) - mixed signs
                a = random.randint(2, 6)
                b = random.randint(1, a - 1)  # Ensure b < a for positive middle
                
                middle = a - b
                last = a * b
                
                expr = f"({var} + {a})({var} - {b})"
                q_text = f"Expand: {expr}"
                correct = f"{var}² + {middle}{var} - {last}"
                wrong = [f"{var}² - {middle}{var} + {last}", f"{var}² + {a - b}{var} + {last}", f"{var}² - {a + b}{var} - {last}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: First: {var} × {var} = {var}²\nStep 2: Outer: -{b}{var}, Inner: +{a}{var}, Combined: +{middle}{var}\nStep 3: Last: {a} × (-{b}) = -{last}\nAnswer: {correct}"
                
            elif q_type == 'foil_negative':
                # (x - 2)(x - 3) - both negative  
                a = random.randint(2, 5)
                b = random.randint(2, 5)
                
                middle = a + b
                last = a * b
                
                expr = f"({var} - {a})({var} - {b})"
                q_text = f"Expand: {expr}"
                correct = f"{var}² - {middle}{var} + {last}"
                wrong = [f"{var}² + {middle}{var} + {last}", f"{var}² - {middle}{var} - {last}", f"{var}² + {middle}{var} - {last}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: First: {var} × {var} = {var}²\nStep 2: Outer + Inner: -{a}{var} - {b}{var} = -{middle}{var}\nStep 3: Last: (-{a}) × (-{b}) = +{last}\nAnswer: {correct}"
                
            else:  # perfect_square
                # (x + a)² = x² + 2ax + a²
                a = random.randint(2, 6)
                middle = 2 * a
                last = a * a
                
                expr = f"({var} + {a})²"
                q_text = f"Expand: {expr}"
                correct = f"{var}² + {middle}{var} + {last}"
                wrong = [f"{var}² + {a}{var} + {last}", f"{var}² + {middle}{var} + {a}", f"2{var}² + {middle}{var} + {last}"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: ({var} + {a})² = ({var} + {a})({var} + {a})\nStep 2: First: {var}², Outer+Inner: 2×{a}{var} = {middle}{var}\nStep 3: Last: {a}² = {last}\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 7,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 8: Factorising (Higher)
# ============================================================

def generate_level_8():
    """Factorising - Common factors and simple quadratics"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['common_factor', 'factor_quad_positive', 'factor_quad_mixed', 'difference_squares'])
        
        try:
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'common_factor':
                # Take out common factor: 6x + 12 = 6(x + 2)
                factor = random.randint(2, 6)
                inner_const = random.randint(1, 5)
                
                coef = factor
                const = factor * inner_const
                
                expr = f"{coef}{var} + {const}"
                q_text = f"Factorise: {expr}"
                correct = f"{factor}({var} + {inner_const})"
                wrong = [f"{var}({coef} + {const})", f"{inner_const}({coef}{var} + 1)", f"{factor}({var} + {const})"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Find the HCF of {coef} and {const}\nStep 2: HCF = {factor}\nStep 3: {expr} = {factor}({var} + {inner_const})\nAnswer: {correct}"
                
            elif q_type == 'factor_quad_positive':
                # Factor x² + 5x + 6 = (x + 2)(x + 3)
                a = random.randint(1, 4)
                b = random.randint(1, 4)
                
                middle = a + b
                last = a * b
                
                expr = f"{var}² + {middle}{var} + {last}"
                q_text = f"Factorise: {expr}"
                correct = f"({var} + {a})({var} + {b})"
                # Also accept in reverse order
                wrong = [f"({var} + {middle})({var} + 1)", f"({var} + {last})({var} + 1)", f"({var} - {a})({var} - {b})"]
                
                svg = None
                explanation = f"Step 1: Find two numbers that multiply to {last} and add to {middle}\nStep 2: {a} × {b} = {last} and {a} + {b} = {middle} ✓\nStep 3: {expr} = ({var} + {a})({var} + {b})\nAnswer: {correct}"
                
            elif q_type == 'factor_quad_mixed':
                # Factor x² + 2x - 8 = (x + 4)(x - 2)
                a = random.randint(3, 6)
                b = random.randint(1, a - 1)
                
                middle = a - b
                last = a * b
                
                expr = f"{var}² + {middle}{var} - {last}"
                q_text = f"Factorise: {expr}"
                correct = f"({var} + {a})({var} - {b})"
                wrong = [f"({var} - {a})({var} + {b})", f"({var} + {middle})({var} - 1)", f"({var} - {a})({var} - {b})"]
                
                svg = None
                explanation = f"Step 1: Find two numbers that multiply to -{last} and add to {middle}\nStep 2: {a} × (-{b}) = -{last} and {a} + (-{b}) = {middle} ✓\nStep 3: {expr} = ({var} + {a})({var} - {b})\nAnswer: {correct}"
                
            else:  # difference_squares
                # x² - 9 = (x + 3)(x - 3)
                a = random.randint(2, 7)
                square = a * a
                
                expr = f"{var}² - {square}"
                q_text = f"Factorise: {expr}"
                correct = f"({var} + {a})({var} - {a})"
                wrong = [f"({var} - {a})²", f"({var} + {a})²", f"({var} - {square})({var} + 1)"]
                
                svg = generate_expression_box_svg(expr)
                explanation = f"Step 1: Recognise difference of two squares: {var}² - {a}²\nStep 2: Use formula: a² - b² = (a + b)(a - b)\nStep 3: {expr} = ({var} + {a})({var} - {a})\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 8,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 9: Algebraic Fractions (Higher)
# ============================================================

def generate_level_9():
    """Algebraic Fractions - Simplifying and operations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['simplify_fraction', 'add_fractions', 'multiply_fractions', 'cancel_common'])
        
        try:
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'simplify_fraction':
                # Simplify 6x/3 = 2x
                num_coef = random.randint(4, 12)
                denom = random.choice([d for d in [2, 3, 4, 6] if num_coef % d == 0])
                result_coef = num_coef // denom
                
                expr = f"{num_coef}{var}/{denom}"
                q_text = f"Simplify: {expr}"
                correct = f"{result_coef}{var}" if result_coef > 1 else var
                wrong = [f"{num_coef}{var}", f"{denom}{var}", f"{num_coef - denom}{var}"]
                
                svg = None
                explanation = f"Step 1: {num_coef}{var}/{denom}\nStep 2: Divide coefficient by {denom}: {num_coef} ÷ {denom} = {result_coef}\nAnswer: {correct}"
                
            elif q_type == 'add_fractions':
                # Add x/2 + x/2 = x
                denom = random.choice([2, 3, 4])
                
                expr = f"{var}/{denom} + {var}/{denom}"
                q_text = f"Simplify: {expr}"
                if denom == 2:
                    correct = var
                else:
                    correct = f"2{var}/{denom}"
                wrong = [f"{var}/{denom * 2}", f"2{var}", f"{var}²/{denom}"]
                
                svg = None
                explanation = f"Step 1: Same denominators, so add numerators\nStep 2: {var} + {var} = 2{var}\nStep 3: 2{var}/{denom}" + (f" = {var}" if denom == 2 else "") + f"\nAnswer: {correct}"
                
            elif q_type == 'multiply_fractions':
                # Multiply fractions: (x/2) × 4 = 2x
                denom = random.choice([2, 3, 4])
                mult = denom * random.randint(1, 3)
                result = mult // denom
                
                expr = f"({var}/{denom}) × {mult}"
                q_text = f"Simplify: {expr}"
                correct = f"{result}{var}" if result > 1 else var
                wrong = [f"{mult}{var}/{denom}", f"{var}/{mult}", f"{mult * denom}{var}"]
                
                svg = None
                explanation = f"Step 1: Multiply {var}/{denom} by {mult}\nStep 2: ({var} × {mult})/{denom} = {mult}{var}/{denom}\nStep 3: Simplify: {mult} ÷ {denom} = {result}\nAnswer: {correct}"
                
            else:  # cancel_common
                # Cancel common factor: 2x/(2x + 4) is not simplifiable
                # Instead do: 4x/2 = 2x
                factor = random.randint(2, 5)
                inner = random.randint(1, 4)
                
                num = factor * inner
                
                expr = f"{num}{var}/{factor}"
                q_text = f"Simplify: {expr}"
                correct = f"{inner}{var}" if inner > 1 else var
                wrong = [f"{num}{var}", f"{factor}{var}", f"{num + factor}{var}"]
                
                svg = None
                explanation = f"Step 1: {num}{var}/{factor}\nStep 2: {num} ÷ {factor} = {inner}\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 9,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 10: Complex Expressions (Mastery)
# ============================================================

def generate_level_10():
    """Complex Expressions - Multi-step algebraic manipulation"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['expand_simplify', 'substitute_complex', 'mixed_operations', 'nested_brackets'])
        
        try:
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'expand_simplify':
                # Expand and simplify: 3(x + 2) + 2(x - 1)
                m1, m2 = random.randint(2, 4), random.randint(2, 4)
                c1, c2 = random.randint(1, 5), random.randint(1, 5)
                
                result_coef = m1 + m2
                result_const = m1 * c1 - m2 * c2
                
                expr = f"{m1}({var} + {c1}) + {m2}({var} - {c2})"
                q_text = f"Expand and simplify: {expr}"
                
                if result_const > 0:
                    correct = f"{result_coef}{var} + {result_const}"
                elif result_const < 0:
                    correct = f"{result_coef}{var} - {abs(result_const)}"
                else:
                    correct = f"{result_coef}{var}"
                    
                wrong = [f"{m1 + m2}{var} + {c1 - c2}", f"{result_coef}{var} - {c1 + c2}", f"{m1 * m2}{var} + {result_const}"]
                
                svg = None
                explanation = f"Step 1: Expand: {m1}{var} + {m1*c1} + {m2}{var} - {m2*c2}\nStep 2: Collect like terms: ({m1} + {m2}){var} = {result_coef}{var}\nStep 3: Constants: {m1*c1} - {m2*c2} = {result_const}\nAnswer: {correct}"
                
            elif q_type == 'substitute_complex':
                # Substitute into complex expression
                a = random.randint(2, 5)
                b = random.randint(2, 5)
                val = random.randint(2, 4)
                
                result = a * val * val + b * val
                
                expr = f"{a}{var}² + {b}{var}"
                q_text = f"Find the value of {expr} when {var} = {val}"
                correct = str(result)
                wrong = [str(a * val + b * val), str(result + 1), str((a + b) * val)]
                
                svg = generate_expression_box_svg(f"{expr} when {var} = {val}")
                explanation = f"Step 1: Substitute {var} = {val}\nStep 2: {a}({val})² + {b}({val})\nStep 3: {a}({val*val}) + {b*val} = {a*val*val} + {b*val} = {result}\nAnswer: {result}"
                
            elif q_type == 'mixed_operations':
                # Simplify: 2x² + 3x + x² - x
                c1 = random.randint(2, 5)
                c2 = random.randint(2, 5)
                c3 = random.randint(1, 3)
                c4 = random.randint(1, c2)
                
                result_sq = c1 + c3
                result_lin = c2 - c4
                
                expr = f"{c1}{var}² + {c2}{var} + {c3}{var}² - {c4}{var}"
                q_text = f"Simplify: {expr}"
                
                if result_lin > 0:
                    correct = f"{result_sq}{var}² + {result_lin}{var}"
                elif result_lin == 0:
                    correct = f"{result_sq}{var}²"
                else:
                    correct = f"{result_sq}{var}² - {abs(result_lin)}{var}"
                    
                wrong = [f"{c1 + c2 + c3 - c4}{var}²", f"{result_sq}{var}² + {c2 + c4}{var}", f"{c1 * c3}{var}² + {result_lin}{var}"]
                
                svg = None
                explanation = f"Step 1: Group like terms: ({c1}{var}² + {c3}{var}²) + ({c2}{var} - {c4}{var})\nStep 2: {c1} + {c3} = {result_sq} for {var}² terms\nStep 3: {c2} - {c4} = {result_lin} for {var} terms\nAnswer: {correct}"
                
            else:  # nested_brackets
                # 2(3(x + 1) + 2)
                outer = random.randint(2, 3)
                inner = random.randint(2, 3)
                c1 = random.randint(1, 3)
                c2 = random.randint(1, 4)
                
                result_coef = outer * inner
                result_const = outer * (inner * c1 + c2)
                
                expr = f"{outer}({inner}({var} + {c1}) + {c2})"
                q_text = f"Expand fully: {expr}"
                correct = f"{result_coef}{var} + {result_const}"
                wrong = [f"{outer + inner}{var} + {c1 + c2}", f"{result_coef}{var} + {c1 * c2}", f"{outer * inner}{var} + {outer + c2}"]
                
                svg = None
                explanation = f"Step 1: Inner bracket: {inner}({var} + {c1}) = {inner}{var} + {inner*c1}\nStep 2: Add {c2}: {inner}{var} + {inner*c1 + c2}\nStep 3: Multiply by {outer}: {result_coef}{var} + {result_const}\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 10,
                'difficulty_band': 'mastery',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 11: Problem Solving (Mastery)
# ============================================================

def generate_level_11():
    """Problem Solving - Word problems requiring algebraic expressions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['perimeter_problem', 'age_problem', 'consecutive', 'cost_problem'])
        
        try:
            name = random.choice(IRISH_NAMES)
            var = 'x'
            
            if q_type == 'perimeter_problem':
                # Rectangle perimeter with algebra
                length_coef = random.randint(2, 4)
                width_add = random.randint(1, 5)
                
                # Perimeter = 2(length + width) = 2(x + length_coef*x + width_add)
                perimeter_coef = 2 * (1 + length_coef)
                perimeter_const = 2 * width_add
                
                q_text = f"A rectangle has width {var} cm and length ({length_coef}{var} + {width_add}) cm. Write an expression for the perimeter."
                correct = f"{perimeter_coef}{var} + {perimeter_const}"
                wrong = [f"{1 + length_coef}{var} + {width_add}", f"2{var} + {length_coef}{var} + {width_add}", f"{perimeter_coef}{var} + {width_add}"]
                
                svg = generate_perimeter_svg(f"{length_coef}{var} + {width_add}", var)
                explanation = f"Step 1: Perimeter = 2(length + width)\nStep 2: = 2({var} + {length_coef}{var} + {width_add})\nStep 3: = 2({1 + length_coef}{var} + {width_add}) = {perimeter_coef}{var} + {perimeter_const}\nAnswer: {correct}"
                
            elif q_type == 'age_problem':
                # Age problems
                years = random.randint(3, 8)
                mult = random.randint(2, 4)
                
                scenarios = [
                    (f"{name} is {var} years old. In {years} years, {name} will be how old?",
                     f"{var} + {years}",
                     [f"{years}{var}", f"{var} - {years}", f"{var}"]),
                    (f"{name} is {var} years old. {name}'s father is {mult} times as old. How old is the father?",
                     f"{mult}{var}",
                     [f"{var} + {mult}", f"{var} - {mult}", f"{var}/{mult}"])
                ]
                scenario = random.choice(scenarios)
                q_text = scenario[0]
                correct = scenario[1]
                wrong = scenario[2]
                
                svg = None
                explanation = f"Step 1: Identify what operation is needed\nStep 2: Apply the operation to {var}\nAnswer: {correct}"
                
            elif q_type == 'consecutive':
                # Sum of consecutive numbers
                q_text = f"Three consecutive numbers are {var}, {var} + 1, and {var} + 2. Write an expression for their sum."
                correct = f"3{var} + 3"
                wrong = [f"3{var}", f"{var} + 3", f"3{var} + 2"]
                
                svg = None
                explanation = f"Step 1: Sum = {var} + ({var} + 1) + ({var} + 2)\nStep 2: Collect {var} terms: 3{var}\nStep 3: Collect constants: 0 + 1 + 2 = 3\nAnswer: 3{var} + 3"
                
            else:  # cost_problem
                # Cost problems
                item_cost = random.randint(2, 8)
                fixed_cost = random.randint(5, 15)
                
                q_text = f"Each book costs €{item_cost}. There is a €{fixed_cost} delivery fee. Write an expression for the total cost of {var} books."
                correct = f"{item_cost}{var} + {fixed_cost}"
                wrong = [f"{item_cost + fixed_cost}{var}", f"{item_cost}{var} - {fixed_cost}", f"{item_cost} + {fixed_cost}{var}"]
                
                svg = None
                explanation = f"Step 1: Cost of {var} books = {item_cost} × {var} = {item_cost}{var}\nStep 2: Add delivery fee: {item_cost}{var} + {fixed_cost}\nAnswer: {correct}"
            
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
                'image_svg': svg,
                'difficulty': 11,
                'difficulty_band': 'mastery',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 12: SEC Exam Style (Mastery)
# ============================================================

def generate_level_12():
    """SEC Exam Style - Higher Level exam-style questions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['sec_expand', 'sec_factorise', 'sec_simplify', 'sec_evaluate', 'sec_expression'])
        
        try:
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'sec_expand':
                # SEC-style expand: (2x + 3)(x - 4)
                a = random.randint(2, 4)
                b = random.randint(2, 5)
                c = random.randint(2, 5)
                
                # (ax + b)(x - c)
                result_x2 = a
                result_x = a * (-c) + b  # -ac + b
                result_const = b * (-c)  # -bc
                
                expr = f"({a}{var} + {b})({var} - {c})"
                q_text = f"Expand and simplify: {expr}"
                
                if result_x > 0:
                    if result_const > 0:
                        correct = f"{result_x2}{var}² + {result_x}{var} + {result_const}"
                    else:
                        correct = f"{result_x2}{var}² + {result_x}{var} - {abs(result_const)}"
                else:
                    if result_const > 0:
                        correct = f"{result_x2}{var}² - {abs(result_x)}{var} + {result_const}"
                    else:
                        correct = f"{result_x2}{var}² - {abs(result_x)}{var} - {abs(result_const)}"
                
                wrong = [f"{a}{var}² + {b - c}{var} - {b * c}", f"{result_x2}{var}² - {result_x}{var} + {abs(result_const)}", f"{a + 1}{var}² + {result_x}{var} - {abs(result_const)}"]
                
                svg = None
                explanation = f"Step 1: Use FOIL method\nStep 2: First: {a}{var} × {var} = {a}{var}²\nStep 3: Outer + Inner: {a}{var}×(-{c}) + {b}×{var} = {result_x}{var}\nStep 4: Last: {b}×(-{c}) = {result_const}\nAnswer: {correct}"
                
            elif q_type == 'sec_factorise':
                # SEC-style factorise: 2x² + 7x + 3
                # (2x + 1)(x + 3) = 2x² + 6x + x + 3 = 2x² + 7x + 3
                a_vals = [(2, 1, 3), (2, 3, 1), (3, 1, 2), (2, 1, 5)]
                a, b, c = random.choice(a_vals)
                
                middle = a * c + b
                last = b * c
                
                expr = f"{a}{var}² + {middle}{var} + {last}"
                q_text = f"Factorise: {expr}"
                correct = f"({a}{var} + {b})({var} + {c})"
                wrong = [f"({a}{var} + {c})({var} + {b})", f"({var} + {b})({a}{var} + {c})", f"{a}({var} + {b})({var} + {c})"]
                
                svg = None
                explanation = f"Step 1: Find factors of {a} × {last} = {a * last} that add to {middle}\nStep 2: {a*c} × {b} = {a*last} and {a*c} + {b} = {middle}\nStep 3: Split middle term and factor by grouping\nAnswer: {correct}"
                
            elif q_type == 'sec_simplify':
                # Simplify complex expression
                m1, m2 = random.randint(2, 4), random.randint(2, 4)
                c1, c2, c3 = random.randint(1, 4), random.randint(1, 4), random.randint(1, 3)
                
                # m1(x² + c1x) - m2(x² - c2x) + c3x²
                result_x2 = m1 - m2 + c3
                result_x = m1 * c1 + m2 * c2
                
                expr = f"{m1}({var}² + {c1}{var}) - {m2}({var}² - {c2}{var}) + {c3}{var}²"
                q_text = f"Simplify: {expr}"
                correct = f"{result_x2}{var}² + {result_x}{var}"
                wrong = [f"{m1 + m2 + c3}{var}² + {c1 - c2}{var}", f"{result_x2}{var}² - {result_x}{var}", f"{m1 * m2}{var}² + {result_x}{var}"]
                
                svg = None
                explanation = f"Step 1: Expand each bracket\nStep 2: {m1}{var}² + {m1*c1}{var} - {m2}{var}² + {m2*c2}{var} + {c3}{var}²\nStep 3: Collect like terms\nAnswer: {correct}"
                
            elif q_type == 'sec_evaluate':
                # Evaluate expression with squared terms
                a = random.randint(2, 4)
                b = random.randint(3, 6)
                val = random.randint(2, 5)
                
                result = a * val * val - b * val
                
                expr = f"{a}{var}² - {b}{var}"
                q_text = f"If {var} = {val}, find the value of {expr}"
                correct = str(result)
                wrong = [str(a * val - b * val), str(result + b), str((a - b) * val)]
                
                svg = None
                explanation = f"Step 1: Substitute {var} = {val}\nStep 2: {a}({val})² - {b}({val})\nStep 3: {a}({val*val}) - {b*val} = {a*val*val} - {b*val} = {result}\nAnswer: {result}"
                
            else:  # sec_expression
                # Write expression from word problem (SEC style)
                name = random.choice(IRISH_NAMES)
                n = random.randint(2, 5)
                
                scenarios = [
                    (f"{name} has {var} euros. After spending €{n} and then tripling what remains, how much does {name} have?",
                     f"3({var} - {n})" if n > 1 else f"3{var} - 3",
                     [f"3{var} - {n}", f"3{var} + {n}", f"{var} - {3*n}"]),
                    (f"A number {var} is doubled and then {n} is added. Write an expression for the result.",
                     f"2{var} + {n}",
                     [f"2({var} + {n})", f"{var} + 2{n}", f"2 + {n}{var}"])
                ]
                scenario = random.choice(scenarios)
                q_text = scenario[0]
                correct = scenario[1]
                wrong = scenario[2]
                
                svg = None
                explanation = f"Step 1: Identify the operations in order\nStep 2: Build the expression step by step\nAnswer: {correct}"
            
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
                'image_svg': svg,
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
    """Validate all questions before database insertion"""
    errors = []
    level_counts = {}
    newline_issues = []
    
    for i, q in enumerate(questions):
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        # Check unique options
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level} Q{i}: Duplicate options")
        
        # Check for literal \n in question text (Methodology v2.2 Mistake 9)
        if '\\n' in q['question_text'] or '\n' in q['question_text']:
            newline_issues.append(f"Level {level}: Newline found in '{q['question_text'][:40]}...'")
        
        # Check options for \n
        for opt in options:
            if '\\n' in str(opt) or '\n' in str(opt):
                newline_issues.append(f"Level {level}: Newline found in option '{opt[:30]}...'")
    
    # Print summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} {status}")
    
    print("="*60)
    print(f"Total: {len(questions)} | Errors: {len(errors)} | Newline Issues: {len(newline_issues)}")
    
    if newline_issues:
        print("\n⚠️  NEWLINE ISSUES (Methodology v2.2 Mistake 9):")
        for issue in newline_issues[:5]:
            print(f"  - {issue}")
        if len(newline_issues) > 5:
            print(f"  ... and {len(newline_issues) - 5} more")
    
    print("="*60)
    
    return len(errors) + len(newline_issues)


# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete existing questions for this topic/mode
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing questions for topic '{TOPIC}'")
    
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
    return inserted


# ============================================================
# MAIN
# ============================================================

def main():
    print("="*60)
    print("AgentMath - Introductory Algebra Generator v2")
    print("="*60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Target: {QUESTIONS_PER_LEVEL * 12} questions (50 per level × 12 levels)")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Variables & Terms", generate_level_1),
        (2, "Like Terms", generate_level_2),
        (3, "Simplifying", generate_level_3),
        (4, "Substitution", generate_level_4),
        (5, "Expanding Brackets", generate_level_5),
        (6, "Single Brackets", generate_level_6),
        (7, "Double Brackets", generate_level_7),
        (8, "Factorising", generate_level_8),
        (9, "Algebraic Fractions", generate_level_9),
        (10, "Complex Expressions", generate_level_10),
        (11, "Problem Solving", generate_level_11),
        (12, "SEC Exam Style", generate_level_12),
    ]
    
    for level, name, gen_func in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = gen_func()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    error_count = validate_questions(all_questions)
    
    if error_count > 0:
        print(f"\n⚠️  {error_count} issues found. Review before inserting.")
    
    response = input("\nInsert into database? (y/n): ").strip().lower()
    if response == 'y':
        insert_questions(all_questions)
        print("\n✓ Done! Questions inserted successfully.")
    else:
        print("\nAborted. No changes made to database.")


if __name__ == "__main__":
    main()
