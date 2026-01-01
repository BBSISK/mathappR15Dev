#!/usr/bin/env python3
"""
AgentMath - Introductory Algebra Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q9(c): Profit expression €3n cost, €5n sell
- 2022 OL Q13(a): Simplify 5a + 3b − 2a + 7b
- 2022 OL Q13(c): Expand 3(2x + 1) − 4(x − 2)
- 2022 HL Q9(a): Simplify 5xy + 3x − 2xy + 7x
- 2022 HL Q9(b): Factorise 6x² − 9xy
- 2023 OL Q12(b): Number wall with 3p, find top in terms of p
- 2023 OL Q14(a): Find 6x − 3y when x = 4, y = 3
- 2023 OL Q14(b): Expand 5(2x + 3)
- 2023 OL Q14(c): Expand 4(x + 3) + 2(3x − 5)
- 2024 OL Q12(a): Find 2a + 3b when a = 5, b = 7
- 2024 OL Q12(b): Expand 3(4x − 2)
- 2024 OL Q12(c): Expand 5(x + 4) − 2(3x − 1)
- 2024 HL Q11(a): Find 3p² − 2q when p = 4, q = 5
- 2025 OL Q7(a-b): Shape algebra (circles, triangles, hexagons)
- 2025 OL Q10(a): Find 3p + 7q when p = 2, q = 11
- 2025 OL Q10(b): Expand 2(5a − 3) − 4a + 7
- 2025 OL Q10(d): Factorise x² − 10x + 21
- 2025 HL Q11(a): Simplify 5x² − 7x + 3x² − 6x

Level Structure:
  L1-3:   Foundation (75% visual)
  L4-6:   Ordinary (75% visual)
  L7-9:   Higher (75% visual)
  L10-12: Application/Mastery (L10: 75%, L11-12: 50%)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'introductory_algebra'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Róisín', 'Seán', 
               'Ciara', 'Darragh', 'Éabha', 'Fionn', 'Gráinne', 'Liam', 'Meadhbh', 'Tadhg',
               'Áine', 'Cillian', 'Orlaith', 'Pádraig', 'Sinéad', 'Eoin', 'Caoimhe', 'Declan']

# Variables for algebra
VARIABLES = ['x', 'y', 'a', 'b', 'p', 'q', 'n', 'm', 't', 'k']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_unique_wrong_numbers(correct_val, count=3, min_val=-20, max_val=50):
    """Generate unique wrong number options"""
    wrong = set()
    
    # Try nearby values first
    candidates = [correct_val + 1, correct_val - 1, correct_val + 2, correct_val - 2,
                  correct_val * 2, correct_val + 3, correct_val - 3, correct_val + 5,
                  correct_val - 5, correct_val + 10, -correct_val]
    
    for c in candidates:
        if c != correct_val and len(wrong) < count:
            wrong.add(c)
    
    # Fill remaining with random values
    while len(wrong) < count:
        w = random.randint(min_val, max_val)
        if w != correct_val and w not in wrong:
            wrong.add(w)
    
    return list(wrong)[:count]

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    unique_wrong = [str(w) for w in wrong_list if str(w) != correct_str]
    seen = set()
    unique_wrong = [w for w in unique_wrong if not (w in seen or seen.add(w))]
    
    options = [correct_str] + unique_wrong[:3]
    
    counter = 1
    while len(set(options)) < 4:
        new_opt = f"Option {counter}"
        if new_opt not in options:
            options.append(new_opt)
        counter += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    
    return options, correct_idx

def format_term(coef, var, first=False):
    """Format an algebraic term like 3x, -2y, etc."""
    if coef == 0:
        return ""
    if var == "":
        # Constant term
        if first:
            return str(coef)
        elif coef > 0:
            return f" + {coef}"
        else:
            return f" − {abs(coef)}"
    
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
            return f" + {var}"
        return f" + {coef}{var}"
    else:
        if coef == -1:
            return f" − {var}"
        return f" − {abs(coef)}{var}"

# ============================================================
# SVG GENERATORS
# ============================================================

def generate_shape_algebra_svg(shape, value):
    """Generate SVG for shape algebra questions"""
    width = 200
    height = 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f0fdf4" rx="8"/>'
    
    if shape == 'circle':
        svg += f'<circle cx="40" cy="40" r="25" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>'
        svg += f'<text x="40" y="45" text-anchor="middle" font-size="14" fill="white" font-weight="bold">?</text>'
    elif shape == 'triangle':
        svg += f'<polygon points="40,15 65,65 15,65" fill="#22c55e" stroke="#15803d" stroke-width="2"/>'
        svg += f'<text x="40" y="52" text-anchor="middle" font-size="12" fill="white" font-weight="bold">?</text>'
    elif shape == 'square':
        svg += f'<rect x="15" y="15" width="50" height="50" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>'
        svg += f'<text x="40" y="45" text-anchor="middle" font-size="14" fill="white" font-weight="bold">?</text>'
    elif shape == 'hexagon':
        svg += f'<polygon points="40,10 65,25 65,55 40,70 15,55 15,25" fill="#8b5cf6" stroke="#7c3aed" stroke-width="2"/>'
        svg += f'<text x="40" y="45" text-anchor="middle" font-size="12" fill="white" font-weight="bold">?</text>'
    
    svg += f'<text x="100" y="45" text-anchor="start" font-size="16" fill="#374151">= {value}</text>'
    svg += '</svg>'
    return svg

def generate_equation_visual_svg(shape1, shape2, result, counts):
    """Generate SVG showing shape equation like ○ + ○ + △ = 15"""
    width = 280
    height = 60
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fef3c7" rx="8"/>'
    
    x_pos = 20
    for i, (shape, count) in enumerate([(shape1, counts[0]), (shape2, counts[1])]):
        for j in range(count):
            if shape == 'circle':
                svg += f'<circle cx="{x_pos + 15}" cy="30" r="12" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>'
            elif shape == 'triangle':
                svg += f'<polygon points="{x_pos + 15},18 {x_pos + 27},42 {x_pos + 3},42" fill="#22c55e" stroke="#15803d" stroke-width="2"/>'
            elif shape == 'square':
                svg += f'<rect x="{x_pos + 3}" y="18" width="24" height="24" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>'
            elif shape == 'hexagon':
                svg += f'<polygon points="{x_pos + 15},15 {x_pos + 25},22 {x_pos + 25},38 {x_pos + 15},45 {x_pos + 5},38 {x_pos + 5},22" fill="#8b5cf6" stroke="#7c3aed" stroke-width="2"/>'
            x_pos += 35
            if j < count - 1:
                svg += f'<text x="{x_pos - 10}" y="35" font-size="16" fill="#374151">+</text>'
        
        if i == 0 and counts[1] > 0:
            svg += f'<text x="{x_pos}" y="35" font-size="16" fill="#374151">+</text>'
            x_pos += 20
    
    svg += f'<text x="{x_pos + 5}" y="35" font-size="18" fill="#374151">= {result}</text>'
    svg += '</svg>'
    return svg

def generate_number_wall_svg(bottom_values, show_answer=False, answer=None):
    """Generate SVG for number wall (adding wall)"""
    width = 220
    height = 120
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#eff6ff" rx="8"/>'
    
    # Calculate wall values
    n = len(bottom_values)
    levels = [bottom_values]
    current = bottom_values
    while len(current) > 1:
        new_level = []
        for i in range(len(current) - 1):
            new_level.append(current[i] + current[i+1])
        levels.append(new_level)
        current = new_level
    
    # Draw wall from bottom to top
    box_w, box_h = 40, 25
    start_y = 90
    
    for level_idx, level in enumerate(levels):
        y = start_y - level_idx * 30
        level_width = len(level) * box_w + (len(level) - 1) * 5
        start_x = (width - level_width) / 2
        
        for i, val in enumerate(level):
            x = start_x + i * (box_w + 5)
            svg += f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" rx="4"/>'
            
            # Show value or ? for top
            if level_idx == len(levels) - 1 and not show_answer:
                display = "?"
            else:
                display = str(val)
            
            svg += f'<text x="{x + box_w/2}" y="{y + box_h/2 + 5}" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold">{display}</text>'
    
    svg += '</svg>'
    return svg

def generate_algebra_wall_svg(bottom_values, var='p'):
    """Generate SVG for algebraic number wall"""
    width = 240
    height = 120
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fef3c7" rx="8"/>'
    
    # Draw wall
    box_w, box_h = 50, 25
    start_y = 90
    
    # Bottom level
    level_width = len(bottom_values) * box_w + (len(bottom_values) - 1) * 5
    start_x = (width - level_width) / 2
    
    for i, val in enumerate(bottom_values):
        x = start_x + i * (box_w + 5)
        svg += f'<rect x="{x}" y="{start_y}" width="{box_w}" height="{box_h}" fill="#fef08a" stroke="#eab308" stroke-width="2" rx="4"/>'
        svg += f'<text x="{x + box_w/2}" y="{start_y + box_h/2 + 5}" text-anchor="middle" font-size="11" fill="#854d0e" font-weight="bold">{val}</text>'
    
    # Middle level (if 3 bottom)
    if len(bottom_values) == 3:
        y = start_y - 30
        level_width = 2 * box_w + 5
        start_x = (width - level_width) / 2
        for i in range(2):
            x = start_x + i * (box_w + 5)
            svg += f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" fill="#fef08a" stroke="#eab308" stroke-width="2" rx="4"/>'
            svg += f'<text x="{x + box_w/2}" y="{y + box_h/2 + 5}" text-anchor="middle" font-size="11" fill="#854d0e">?</text>'
    
    # Top level
    y = start_y - 60 if len(bottom_values) == 3 else start_y - 30
    x = (width - box_w) / 2
    svg += f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" fill="#fde047" stroke="#ca8a04" stroke-width="2" rx="4"/>'
    svg += f'<text x="{x + box_w/2}" y="{y + box_h/2 + 5}" text-anchor="middle" font-size="12" fill="#713f12" font-weight="bold">?</text>'
    
    svg += '</svg>'
    return svg

def generate_bar_model_svg(terms, simplified):
    """Generate bar model for like terms"""
    width = 280
    height = 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f0fdf4" rx="8"/>'
    
    # Title
    svg += f'<text x="140" y="20" text-anchor="middle" font-size="12" fill="#374151">Combine like terms:</text>'
    
    # Draw bars for each term type
    colors = {'x': '#3b82f6', 'y': '#22c55e', 'a': '#f59e0b', 'b': '#8b5cf6'}
    
    y_pos = 35
    x_pos = 20
    for coef, var in terms:
        color = colors.get(var, '#6b7280')
        bar_width = abs(coef) * 20
        
        if coef > 0:
            svg += f'<rect x="{x_pos}" y="{y_pos}" width="{bar_width}" height="20" fill="{color}" stroke="#374151" rx="3"/>'
            svg += f'<text x="{x_pos + bar_width/2}" y="{y_pos + 14}" text-anchor="middle" font-size="10" fill="white">{coef}{var}</text>'
        x_pos += bar_width + 10
    
    # Arrow and result
    svg += f'<text x="140" y="75" text-anchor="middle" font-size="14" fill="#374151">↓</text>'
    svg += f'<text x="140" y="92" text-anchor="middle" font-size="14" fill="#059669" font-weight="bold">{simplified}</text>'
    
    svg += '</svg>'
    return svg

def generate_substitution_visual_svg(expression, var_vals, result):
    """Generate visual for substitution"""
    width = 260
    height = 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#eff6ff" rx="8"/>'
    
    # Expression
    svg += f'<text x="130" y="25" text-anchor="middle" font-size="14" fill="#1e40af" font-weight="bold">{expression}</text>'
    
    # Variable values
    var_text = ", ".join([f"{v} = {val}" for v, val in var_vals.items()])
    svg += f'<text x="130" y="45" text-anchor="middle" font-size="12" fill="#374151">when {var_text}</text>'
    
    # Result
    svg += f'<text x="130" y="68" text-anchor="middle" font-size="16" fill="#059669" font-weight="bold">= {result}</text>'
    
    svg += '</svg>'
    return svg

def generate_expand_visual_svg(expression, expanded):
    """Generate visual for bracket expansion"""
    width = 280
    height = 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fef3c7" rx="8"/>'
    
    # Original expression
    svg += f'<text x="140" y="25" text-anchor="middle" font-size="14" fill="#92400e" font-weight="bold">{expression}</text>'
    
    # Arrow
    svg += f'<text x="140" y="45" text-anchor="middle" font-size="16" fill="#374151">↓ expand</text>'
    
    # Expanded
    svg += f'<text x="140" y="68" text-anchor="middle" font-size="14" fill="#059669" font-weight="bold">{expanded}</text>'
    
    svg += '</svg>'
    return svg

def generate_context_expression_svg(context_type, var, coef=1, const=0):
    """Generate visual for expressions in context"""
    width = 260
    height = 90
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ecfdf5" rx="8"/>'
    
    if context_type == 'cost':
        svg += f'<text x="130" y="25" text-anchor="middle" font-size="12" fill="#374151">Cost to make:</text>'
        svg += f'<text x="130" y="50" text-anchor="middle" font-size="18" fill="#059669" font-weight="bold">€{coef}{var}</text>'
    elif context_type == 'sell':
        svg += f'<text x="130" y="25" text-anchor="middle" font-size="12" fill="#374151">Selling price:</text>'
        svg += f'<text x="130" y="50" text-anchor="middle" font-size="18" fill="#3b82f6" font-weight="bold">€{coef}{var}</text>'
    elif context_type == 'perimeter':
        svg += f'<rect x="80" y="20" width="100" height="50" fill="none" stroke="#3b82f6" stroke-width="2"/>'
        svg += f'<text x="130" y="50" text-anchor="middle" font-size="12" fill="#3b82f6">{var}</text>'
        svg += f'<text x="60" y="50" text-anchor="middle" font-size="10" fill="#374151">{coef}</text>'
    
    if const != 0:
        sign = "+" if const > 0 else ""
        svg += f'<text x="130" y="75" text-anchor="middle" font-size="11" fill="#6b7280">{sign}{const}</text>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Understanding Variables (Foundation)
# ============================================================

def generate_level_1():
    """Understanding Variables - Shape algebra, what is a variable"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = [
        'shape_single',      # Find value of shape from equation
        'shape_double',      # Two shapes, find one
        'variable_meaning',  # What does x represent?
        'shape_equation',    # Shape + Shape + Shape = 21
        'match_expression',  # Match description to expression
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'shape_single':
                shape = random.choice(['circle', 'triangle', 'square'])
                value = random.randint(3, 12)
                count = random.choice([2, 3])
                total = value * count
                
                shape_name = {'circle': '○', 'triangle': '△', 'square': '□'}[shape]
                equation = f"{' + '.join([shape_name] * count)} = {total}"
                
                q_text = f"In the equation {equation}, what is the value of one {shape}?"
                correct = value
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_equation_visual_svg(shape, None, total, [count, 0])
                explanation = f"If {count} {shape}s = {total}, then one {shape} = {total} ÷ {count} = {value}"
                
            elif q_type == 'shape_double':
                # SEC 2025 OL Q7 style
                shape1, shape2 = random.sample(['circle', 'triangle', 'square'], 2)
                val1 = random.randint(4, 10)
                val2 = random.randint(2, 8)
                
                # First equation: 3 of shape1 = total1
                count1 = 3
                total1 = val1 * count1
                
                # Second equation: shape1 + shape2 + shape1 = total2
                total2 = val1 + val2 + val1
                
                shape_names = {'circle': '○', 'triangle': '△', 'square': '□'}
                
                q_text = f"Given: {shape_names[shape1]} + {shape_names[shape1]} + {shape_names[shape1]} = {total1}\\n" \
                         f"and {shape_names[shape1]} + {shape_names[shape2]} + {shape_names[shape1]} = {total2}\\n" \
                         f"What is the value of {shape_names[shape2]}?"
                
                correct = val2
                wrong = get_unique_wrong_numbers(correct, 3)
                visual = generate_shape_algebra_svg(shape2, "?")
                explanation = f"From first equation: {shape_names[shape1]} = {total1} ÷ 3 = {val1}\\n" \
                             f"Substitute into second: {val1} + {shape_names[shape2]} + {val1} = {total2}\\n" \
                             f"{shape_names[shape2]} = {total2} - {val1} - {val1} = {val2}"
                
            elif q_type == 'variable_meaning':
                contexts = [
                    ("n apples", "the number of apples", "n"),
                    ("x books", "the number of books", "x"),
                    ("t hours", "the number of hours", "t"),
                    ("p pencils", "the number of pencils", "p"),
                    ("m metres", "the distance in metres", "m"),
                ]
                context = random.choice(contexts)
                
                q_text = f"In the expression '{context[0]}', what does the letter {context[2]} represent?"
                correct = context[1]
                wrong = [f"the value {random.randint(1,10)}", 
                         f"the letter {context[2]}", 
                         "nothing specific"]
                
                visual = None
                explanation = f"In algebra, letters (variables) represent unknown numbers. Here '{context[2]}' represents {context[1]}."
                
            elif q_type == 'shape_equation':
                # Triple same shape
                shape = random.choice(['circle', 'triangle', 'square'])
                value = random.randint(5, 15)
                total = value * 3
                
                shape_name = {'circle': '○', 'triangle': '△', 'square': '□'}[shape]
                
                q_text = f"If {shape_name} + {shape_name} + {shape_name} = {total}, what is the value of {shape_name}?"
                correct = value
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_equation_visual_svg(shape, None, total, [3, 0])
                explanation = f"Three {shape}s equal {total}\\nSo one {shape} = {total} ÷ 3 = {value}"
                
            else:  # match_expression
                var = random.choice(['x', 'n', 'p'])
                coef = random.randint(2, 6)
                
                descriptions = [
                    (f"{coef} times a number {var}", f"{coef}{var}"),
                    (f"a number {var} plus {coef}", f"{var} + {coef}"),
                    (f"a number {var} minus {coef}", f"{var} - {coef}"),
                    (f"{coef} added to a number {var}", f"{var} + {coef}"),
                ]
                desc, expr = random.choice(descriptions)
                
                q_text = f"Which expression means '{desc}'?"
                correct = expr
                wrong_exprs = [f"{coef} + {var}", f"{var}{coef}", f"{coef} - {var}"]
                wrong = [w for w in wrong_exprs if w != correct][:3]
                
                visual = None
                explanation = f"'{desc}' is written as {expr} in algebra."
            
            # Create question
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:50]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Writing Simple Expressions (Foundation)
# ============================================================

def generate_level_2():
    """Writing Simple Expressions - Number walls, words to algebra"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = [
        'number_wall',         # SEC 2023 OL Q12 style
        'words_to_expr',       # Write expression from words
        'profit_expression',   # SEC 2022 OL Q9c style
        'simple_formula',      # Simple formulas
        'expression_table',    # Complete a table of values
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'number_wall':
                # Bottom values add up
                a, b, c = random.randint(2, 8), random.randint(2, 8), random.randint(2, 8)
                mid1, mid2 = a + b, b + c
                top = mid1 + mid2
                
                q_text = f"In an adding wall, each block is the sum of the two blocks below it.\\n" \
                         f"If the bottom row is {a}, {b}, {c}, what is the value at the top?"
                correct = top
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_number_wall_svg([a, b, c], show_answer=False)
                explanation = f"Middle row: {a} + {b} = {mid1}, and {b} + {c} = {mid2}\\n" \
                             f"Top: {mid1} + {mid2} = {top}"
                
            elif q_type == 'words_to_expr':
                var = random.choice(['x', 'n', 'p', 'a'])
                num = random.randint(2, 10)
                
                word_problems = [
                    (f"five more than {var}", f"{var} + 5"),
                    (f"three less than {var}", f"{var} - 3"),
                    (f"double {var}", f"2{var}"),
                    (f"half of {var}", f"{var}/2"),
                    (f"{num} more than {var}", f"{var} + {num}"),
                    (f"{num} times {var}", f"{num}{var}"),
                ]
                words, expr = random.choice(word_problems)
                
                q_text = f"Write '{words}' as an algebraic expression."
                correct = expr
                
                # Generate wrong options
                wrong_options = []
                if "more" in words:
                    wrong_options = [f"{var} - {num}", f"{num}{var}", f"{num} - {var}"]
                elif "less" in words:
                    wrong_options = [f"{var} + 3", f"3{var}", f"3 - {var}"]
                elif "double" in words:
                    wrong_options = [f"{var} + 2", f"{var}2", f"{var}/2"]
                elif "times" in words:
                    wrong_options = [f"{var} + {num}", f"{var} - {num}", f"{var}/{num}"]
                else:
                    wrong_options = [f"{var} × 2", f"2 + {var}", f"{var} - 2"]
                
                wrong = [w for w in wrong_options if w != correct][:3]
                visual = None
                explanation = f"'{words}' translates to {expr} in algebraic notation."
                
            elif q_type == 'profit_expression':
                # SEC 2022 OL Q9c style
                var = random.choice(['n', 'x', 'p'])
                cost_coef = random.randint(2, 5)
                sell_coef = cost_coef + random.randint(1, 3)
                
                q_text = f"It costs €{cost_coef}{var} to make a product. It sells for €{sell_coef}{var}.\\n" \
                         f"Write the profit in terms of {var}."
                
                profit = sell_coef - cost_coef
                correct = f"€{profit}{var}"
                wrong = [f"€{sell_coef + cost_coef}{var}", f"€{cost_coef}{var}", f"€{sell_coef}{var}"]
                
                visual = generate_context_expression_svg('cost', var, cost_coef)
                explanation = f"Profit = Selling price - Cost\\n" \
                             f"Profit = €{sell_coef}{var} - €{cost_coef}{var} = €{profit}{var}"
                
            elif q_type == 'simple_formula':
                formulas = [
                    ("the perimeter of a square with side s", "4s", ["4 + s", "s²", "2s"]),
                    ("the perimeter of a rectangle with length l and width w", "2l + 2w", ["l + w", "lw", "2(l + w)"]),
                    ("the cost of n items at €5 each", "5n", ["n + 5", "5 + n", "n/5"]),
                    ("the total of x and y", "x + y", ["xy", "x - y", "x/y"]),
                ]
                desc, correct, wrong = random.choice(formulas)
                
                q_text = f"Write a formula for {desc}."
                visual = None
                explanation = f"The formula for {desc} is {correct}."
                
            else:  # expression_table
                var = random.choice(['x', 'n'])
                coef = random.randint(2, 4)
                const = random.randint(1, 5)
                input_val = random.randint(1, 6)
                
                expr = f"{coef}{var} + {const}"
                result = coef * input_val + const
                
                q_text = f"If {var} = {input_val}, what is the value of {expr}?"
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var: input_val}, "?")
                explanation = f"{expr} = {coef}({input_val}) + {const} = {coef * input_val} + {const} = {result}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:50]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Collecting Like Terms - Basic (Foundation)
# ============================================================

def generate_level_3():
    """Collecting Like Terms - Basic single variable"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['single_var', 'two_vars', 'identify_like', 'simplify_basic'])
            
            if q_type == 'single_var':
                # 5x + 3x
                var = random.choice(['x', 'y', 'a', 'n'])
                coef1 = random.randint(2, 8)
                coef2 = random.randint(2, 8)
                
                q_text = f"Simplify: {coef1}{var} + {coef2}{var}"
                result = coef1 + coef2
                correct = f"{result}{var}"
                wrong = [f"{coef1 * coef2}{var}", f"{coef1}{var}{coef2}", f"{result}"]
                
                visual = generate_bar_model_svg([(coef1, var), (coef2, var)], correct)
                explanation = f"{coef1}{var} + {coef2}{var} = ({coef1} + {coef2}){var} = {result}{var}\\n" \
                             f"We add the coefficients and keep the variable."
                
            elif q_type == 'two_vars':
                # SEC 2022 OL Q13(a) style: 5a + 3b − 2a + 7b
                var1, var2 = random.sample(['a', 'b', 'x', 'y'], 2)
                c1 = random.randint(3, 8)
                c2 = random.randint(2, 7)
                c3 = random.randint(1, c1-1)  # Ensure positive result
                c4 = random.randint(2, 7)
                
                q_text = f"Simplify: {c1}{var1} + {c2}{var2} − {c3}{var1} + {c4}{var2}"
                
                result_v1 = c1 - c3
                result_v2 = c2 + c4
                correct = f"{result_v1}{var1} + {result_v2}{var2}"
                
                wrong = [
                    f"{c1 + c2 - c3 + c4}{var1}{var2}",
                    f"{result_v1}{var1} − {result_v2}{var2}",
                    f"{c1 - c3}{var1} + {c2 - c4}{var2}"
                ]
                
                visual = None
                explanation = f"Collect {var1} terms: {c1}{var1} − {c3}{var1} = {result_v1}{var1}\\n" \
                             f"Collect {var2} terms: {c2}{var2} + {c4}{var2} = {result_v2}{var2}\\n" \
                             f"Answer: {correct}"
                
            elif q_type == 'identify_like':
                var = random.choice(['x', 'y', 'a'])
                terms = [f"3{var}", f"5{var}", f"2{var}²", f"7"]
                
                q_text = f"Which terms are 'like terms' that can be combined? {', '.join(terms)}"
                correct = f"3{var} and 5{var}"
                wrong = [f"3{var} and 2{var}²", f"5{var} and 7", f"All of them"]
                
                visual = None
                explanation = f"Like terms have the same variable part.\\n" \
                             f"3{var} and 5{var} both have '{var}' so they are like terms.\\n" \
                             f"2{var}² has '{var}²' which is different. 7 is a constant."
                
            else:  # simplify_basic
                var = random.choice(['x', 'y', 'p'])
                c1 = random.randint(3, 9)
                c2 = random.randint(1, c1-1)
                
                op = random.choice(['+', '−'])
                if op == '+':
                    result = c1 + c2
                    q_text = f"Simplify: {c1}{var} + {c2}{var}"
                else:
                    result = c1 - c2
                    q_text = f"Simplify: {c1}{var} − {c2}{var}"
                
                correct = f"{result}{var}"
                wrong = get_unique_wrong_numbers(result, 3)
                wrong = [f"{w}{var}" for w in wrong]
                
                visual = generate_bar_model_svg([(c1, var), (c2 if op == '+' else -c2, var)], correct)
                explanation = f"Combine like terms: {c1}{var} {op} {c2}{var} = {result}{var}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Substitution - Single Variable (Ordinary)
# ============================================================

def generate_level_4():
    """Substitution - SEC style: Find value of expression"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['single_var', 'two_vars', 'with_subtraction', 'sec_style'])
            
            if q_type == 'single_var':
                var = random.choice(['x', 'p', 'n', 'a'])
                coef = random.randint(2, 6)
                const = random.randint(1, 10)
                val = random.randint(2, 8)
                
                result = coef * val + const
                expr = f"{coef}{var} + {const}"
                
                q_text = f"Find the value of {expr} when {var} = {val}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var: val}, "?")
                explanation = f"{expr}\\n= {coef}({val}) + {const}\\n= {coef * val} + {const}\\n= {result}"
                
            elif q_type == 'two_vars':
                # SEC 2024 OL Q12(a): Find 2a + 3b when a = 5, b = 7
                var1, var2 = random.sample(['a', 'b', 'x', 'y', 'p', 'q'], 2)
                c1 = random.randint(2, 5)
                c2 = random.randint(2, 5)
                v1 = random.randint(2, 8)
                v2 = random.randint(2, 8)
                
                result = c1 * v1 + c2 * v2
                expr = f"{c1}{var1} + {c2}{var2}"
                
                q_text = f"Find the value of {expr} when {var1} = {v1} and {var2} = {v2}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var1: v1, var2: v2}, "?")
                explanation = f"{expr}\\n= {c1}({v1}) + {c2}({v2})\\n= {c1 * v1} + {c2 * v2}\\n= {result}"
                
            elif q_type == 'with_subtraction':
                # SEC 2023 OL Q14(a): 6x − 3y when x = 4, y = 3
                var1, var2 = random.sample(['x', 'y', 'a', 'b'], 2)
                c1 = random.randint(4, 8)
                c2 = random.randint(2, 5)
                v1 = random.randint(3, 7)
                v2 = random.randint(2, 5)
                
                result = c1 * v1 - c2 * v2
                expr = f"{c1}{var1} − {c2}{var2}"
                
                q_text = f"Find the value of {expr} when {var1} = {v1} and {var2} = {v2}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var1: v1, var2: v2}, "?")
                explanation = f"{expr}\\n= {c1}({v1}) − {c2}({v2})\\n= {c1 * v1} − {c2 * v2}\\n= {result}"
                
            else:  # sec_style - SEC 2025 OL Q10(a): 3p + 7q when p = 2, q = 11
                var1, var2 = random.sample(['p', 'q', 'x', 'y'], 2)
                c1 = random.randint(2, 5)
                c2 = random.randint(5, 10)
                v1 = random.randint(2, 5)
                v2 = random.randint(8, 12)
                
                result = c1 * v1 + c2 * v2
                expr = f"{c1}{var1} + {c2}{var2}"
                
                q_text = f"Find the value of {expr}, when {var1} = {v1} and {var2} = {v2}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var1: v1, var2: v2}, "?")
                explanation = f"{expr}\\n= {c1}({v1}) + {c2}({v2})\\n= {c1 * v1} + {c2 * v2}\\n= {result}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 4,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Expanding Single Brackets (Ordinary)
# ============================================================

def generate_level_5():
    """Expanding Single Brackets - SEC style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['positive', 'negative', 'with_minus', 'sec_style'])
            
            var = random.choice(['x', 'y', 'a', 'p'])
            
            if q_type == 'positive':
                # SEC 2023 OL Q14(b): 5(2x + 3)
                outer = random.randint(2, 6)
                inner_coef = random.randint(2, 4)
                inner_const = random.randint(2, 8)
                
                expr = f"{outer}({inner_coef}{var} + {inner_const})"
                result_coef = outer * inner_coef
                result_const = outer * inner_const
                correct = f"{result_coef}{var} + {result_const}"
                
                q_text = f"Expand: {expr}"
                wrong = [
                    f"{inner_coef}{var} + {result_const}",
                    f"{result_coef}{var} + {inner_const}",
                    f"{outer + inner_coef}{var} + {inner_const}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\n= {outer} × {inner_coef}{var} + {outer} × {inner_const}\\n= {result_coef}{var} + {result_const}"
                
            elif q_type == 'negative':
                # SEC 2024 OL Q12(b): 3(4x − 2)
                outer = random.randint(2, 5)
                inner_coef = random.randint(2, 5)
                inner_const = random.randint(2, 6)
                
                expr = f"{outer}({inner_coef}{var} − {inner_const})"
                result_coef = outer * inner_coef
                result_const = outer * inner_const
                correct = f"{result_coef}{var} − {result_const}"
                
                q_text = f"Expand: {expr}"
                wrong = [
                    f"{result_coef}{var} + {result_const}",
                    f"{inner_coef}{var} − {result_const}",
                    f"{result_coef}{var} − {inner_const}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\n= {outer} × {inner_coef}{var} − {outer} × {inner_const}\\n= {result_coef}{var} − {result_const}"
                
            elif q_type == 'with_minus':
                # -2(x + 3)
                outer = random.randint(2, 4)
                inner_const = random.randint(2, 6)
                
                expr = f"−{outer}({var} + {inner_const})"
                result_const = outer * inner_const
                correct = f"−{outer}{var} − {result_const}"
                
                q_text = f"Expand: {expr}"
                wrong = [
                    f"−{outer}{var} + {result_const}",
                    f"{outer}{var} − {result_const}",
                    f"−{outer}{var} + {inner_const}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\n= −{outer} × {var} + (−{outer}) × {inner_const}\\n= −{outer}{var} − {result_const}\\n" \
                             f"Remember: negative × positive = negative"
                
            else:  # sec_style
                outer = random.randint(3, 6)
                inner_coef = random.randint(2, 4)
                inner_const = random.randint(1, 7)
                sign = random.choice(['+', '−'])
                
                if sign == '+':
                    expr = f"{outer}({inner_coef}{var} + {inner_const})"
                    result_const = outer * inner_const
                    correct = f"{outer * inner_coef}{var} + {result_const}"
                else:
                    expr = f"{outer}({inner_coef}{var} − {inner_const})"
                    result_const = outer * inner_const
                    correct = f"{outer * inner_coef}{var} − {result_const}"
                
                q_text = f"Expand: {expr}"
                wrong = [
                    f"{inner_coef}{var} + {result_const}" if sign == '+' else f"{inner_coef}{var} − {result_const}",
                    f"{outer * inner_coef}{var} {'+' if sign == '−' else '−'} {result_const}",
                    f"{outer + inner_coef}{var} + {inner_const}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\nMultiply {outer} by each term inside the bracket:\\n" \
                             f"= {outer * inner_coef}{var} {sign} {result_const}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{expr}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 5,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Expanding and Simplifying (Ordinary)
# ============================================================

def generate_level_6():
    """Expanding and Simplifying - Two brackets, SEC style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            var = random.choice(['x', 'a', 'y', 'p'])
            q_type = random.choice(['add_brackets', 'subtract_brackets', 'sec_2022', 'sec_2025'])
            
            if q_type == 'add_brackets':
                # SEC 2023 OL Q14(c): 4(x + 3) + 2(3x − 5)
                o1 = random.randint(2, 5)
                c1 = random.randint(2, 4)
                o2 = random.randint(2, 4)
                c2 = random.randint(2, 5)
                
                # First bracket: o1(x + c1)
                # Second bracket: o2(cx − c2) where c could be 2 or 3
                inner2_coef = random.randint(2, 3)
                
                expr = f"{o1}({var} + {c1}) + {o2}({inner2_coef}{var} − {c2})"
                
                # Expand: o1*x + o1*c1 + o2*inner2_coef*x - o2*c2
                x_coef = o1 + o2 * inner2_coef
                const = o1 * c1 - o2 * c2
                
                if const >= 0:
                    correct = f"{x_coef}{var} + {const}"
                else:
                    correct = f"{x_coef}{var} − {abs(const)}"
                
                q_text = f"Expand and simplify: {expr}"
                wrong = [
                    f"{o1 + o2}{var} + {c1 - c2}",
                    f"{x_coef}{var} + {o1 * c1 + o2 * c2}",
                    f"{o1 * inner2_coef}{var} − {const}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\n= {o1}{var} + {o1 * c1} + {o2 * inner2_coef}{var} − {o2 * c2}\\n" \
                             f"= ({o1} + {o2 * inner2_coef}){var} + ({o1 * c1} − {o2 * c2})\\n= {correct}"
                
            elif q_type == 'subtract_brackets':
                # SEC 2024 OL Q12(c): 5(x + 4) − 2(3x − 1)
                o1 = random.randint(3, 6)
                c1 = random.randint(2, 5)
                o2 = random.randint(2, 4)
                inner2_coef = random.randint(2, 4)
                c2 = random.randint(1, 4)
                
                expr = f"{o1}({var} + {c1}) − {o2}({inner2_coef}{var} − {c2})"
                
                # Expand: o1*x + o1*c1 - o2*inner2_coef*x + o2*c2
                x_coef = o1 - o2 * inner2_coef
                const = o1 * c1 + o2 * c2
                
                if x_coef >= 0:
                    correct = f"{x_coef}{var} + {const}"
                else:
                    correct = f"−{abs(x_coef)}{var} + {const}"
                
                q_text = f"Expand and simplify: {expr}"
                wrong = [
                    f"{o1 - o2}{var} + {c1 + c2}",
                    f"{abs(x_coef)}{var} − {const}",
                    f"{o1 + o2 * inner2_coef}{var} + {const}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\n= {o1}{var} + {o1 * c1} − {o2 * inner2_coef}{var} + {o2 * c2}\\n" \
                             f"(Note: −{o2} × −{c2} = +{o2 * c2})\\n= {correct}"
                
            elif q_type == 'sec_2022':
                # SEC 2022 OL Q13(c): 3(2x + 1) − 4(x − 2)
                o1 = random.randint(2, 4)
                inner1_coef = 2
                c1 = random.randint(1, 3)
                o2 = random.randint(2, 5)
                c2 = random.randint(1, 4)
                
                expr = f"{o1}({inner1_coef}{var} + {c1}) − {o2}({var} − {c2})"
                
                x_coef = o1 * inner1_coef - o2
                const = o1 * c1 + o2 * c2
                
                correct = f"{x_coef}{var} + {const}"
                
                q_text = f"Expand and simplify: {expr}"
                wrong = [
                    f"{o1 * inner1_coef + o2}{var} + {const}",
                    f"{x_coef}{var} − {const}",
                    f"{o1 * inner1_coef}{var} + {o1 * c1 - o2 * c2}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\n= {o1 * inner1_coef}{var} + {o1 * c1} − {o2}{var} + {o2 * c2}\\n= {correct}"
                
            else:  # sec_2025
                # SEC 2025 OL Q10(b): 2(5a − 3) − 4a + 7
                o1 = random.randint(2, 4)
                inner1_coef = random.randint(3, 6)
                c1 = random.randint(2, 5)
                loose_coef = random.randint(2, 5)
                loose_const = random.randint(3, 9)
                
                expr = f"{o1}({inner1_coef}{var} − {c1}) − {loose_coef}{var} + {loose_const}"
                
                x_coef = o1 * inner1_coef - loose_coef
                const = -o1 * c1 + loose_const
                
                if const >= 0:
                    correct = f"{x_coef}{var} + {const}"
                else:
                    correct = f"{x_coef}{var} − {abs(const)}"
                
                q_text = f"Multiply out and simplify: {expr}"
                wrong = [
                    f"{o1 * inner1_coef + loose_coef}{var} + {const}",
                    f"{x_coef}{var} − {abs(const)}" if const >= 0 else f"{x_coef}{var} + {abs(const)}",
                    f"{o1 * inner1_coef}{var} + {loose_const - c1}"
                ]
                
                visual = generate_expand_visual_svg(expr, correct)
                explanation = f"{expr}\\n= {o1 * inner1_coef}{var} − {o1 * c1} − {loose_coef}{var} + {loose_const}\\n= {correct}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{expr}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 6,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Collecting Like Terms - Multiple Variables (Higher)
# ============================================================

def generate_level_7():
    """Collecting Like Terms with xy, x², etc - SEC HL style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['xy_terms', 'mixed_xy_x', 'x_squared', 'sec_hl_style'])
            
            if q_type == 'xy_terms':
                # 3xy + 5xy
                c1 = random.randint(2, 7)
                c2 = random.randint(2, 7)
                
                q_text = f"Simplify: {c1}xy + {c2}xy"
                correct = f"{c1 + c2}xy"
                wrong = [f"{c1 * c2}xy", f"{c1}x + {c2}y", f"{c1 + c2}x{c1 + c2}y"]
                
                visual = None
                explanation = f"{c1}xy + {c2}xy = ({c1} + {c2})xy = {c1 + c2}xy"
                
            elif q_type == 'mixed_xy_x':
                # SEC 2022 HL Q9(a): 5xy + 3x − 2xy + 7x
                c_xy1 = random.randint(3, 7)
                c_x1 = random.randint(2, 6)
                c_xy2 = random.randint(1, c_xy1 - 1)
                c_x2 = random.randint(2, 7)
                
                q_text = f"Simplify: {c_xy1}xy + {c_x1}x − {c_xy2}xy + {c_x2}x"
                
                result_xy = c_xy1 - c_xy2
                result_x = c_x1 + c_x2
                correct = f"{result_xy}xy + {result_x}x"
                
                wrong = [
                    f"{c_xy1 + c_x1 - c_xy2 + c_x2}xy",
                    f"{result_x}xy + {result_xy}x",
                    f"{result_xy}x + {result_x}xy"
                ]
                
                visual = None
                explanation = f"Collect xy terms: {c_xy1}xy − {c_xy2}xy = {result_xy}xy\\n" \
                             f"Collect x terms: {c_x1}x + {c_x2}x = {result_x}x\\n" \
                             f"Answer: {correct}"
                
            elif q_type == 'x_squared':
                # 4x² + 3x − x² + 2x
                c1 = random.randint(3, 7)
                c2 = random.randint(2, 5)
                c3 = random.randint(1, c1 - 1)
                c4 = random.randint(1, 5)
                
                var = random.choice(['x', 'y', 'a'])
                
                q_text = f"Simplify: {c1}{var}² + {c2}{var} − {c3}{var}² + {c4}{var}"
                
                result_sq = c1 - c3
                result_var = c2 + c4
                correct = f"{result_sq}{var}² + {result_var}{var}"
                
                wrong = [
                    f"{c1 + c2 - c3 + c4}{var}²",
                    f"{result_sq}{var} + {result_var}{var}²",
                    f"{result_sq + result_var}{var}²"
                ]
                
                visual = None
                explanation = f"Collect {var}² terms: {c1}{var}² − {c3}{var}² = {result_sq}{var}²\\n" \
                             f"Collect {var} terms: {c2}{var} + {c4}{var} = {result_var}{var}\\n" \
                             f"Answer: {correct}"
                
            else:  # sec_hl_style
                # Mix of terms
                var1 = random.choice(['x', 'p', 'a'])
                c1 = random.randint(4, 9)
                c2 = random.randint(3, 7)
                c3 = random.randint(2, c1 - 1)
                c4 = random.randint(2, 6)
                
                q_text = f"Simplify: {c1}{var1}y + {c2}{var1} − {c3}{var1}y + {c4}{var1}"
                
                result_xy = c1 - c3
                result_x = c2 + c4
                correct = f"{result_xy}{var1}y + {result_x}{var1}"
                
                wrong = [
                    f"{result_x}{var1}y + {result_xy}{var1}",
                    f"{c1 - c3 + c2 + c4}{var1}y",
                    f"{result_xy}y + {result_x}{var1}"
                ]
                
                visual = None
                explanation = f"Group like terms:\\n" \
                             f"{var1}y terms: {c1}{var1}y − {c3}{var1}y = {result_xy}{var1}y\\n" \
                             f"{var1} terms: {c2}{var1} + {c4}{var1} = {result_x}{var1}\\n" \
                             f"Answer: {correct}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 7,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Substitution with Powers (Higher)
# ============================================================

def generate_level_8():
    """Substitution with Powers - SEC HL style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['squared', 'cubed', 'two_vars_power', 'sec_hl_style', 'mixed_powers'])
            
            if q_type == 'squared':
                var = random.choice(['x', 'p', 'a', 'n'])
                coef = random.randint(2, 5)
                val = random.randint(2, 5)
                
                result = coef * val * val
                expr = f"{coef}{var}²"
                
                q_text = f"Find the value of {expr} when {var} = {val}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var: val}, "?")
                explanation = f"{expr} = {coef} × {var}²\\n= {coef} × {val}²\\n= {coef} × {val * val}\\n= {result}"
                
            elif q_type == 'cubed':
                var = random.choice(['x', 'n', 'a'])
                val = random.randint(2, 4)
                
                result = val ** 3
                expr = f"{var}³"
                
                q_text = f"Find the value of {expr} when {var} = {val}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var: val}, "?")
                explanation = f"{expr} = {val}³ = {val} × {val} × {val} = {result}"
                
            elif q_type == 'two_vars_power':
                # SEC 2024 HL Q11(a): 3p² − 2q when p = 4, q = 5
                var1, var2 = random.sample(['p', 'q', 'x', 'y'], 2)
                c1 = random.randint(2, 4)
                c2 = random.randint(2, 4)
                v1 = random.randint(3, 5)
                v2 = random.randint(3, 8)
                
                result = c1 * v1 * v1 - c2 * v2
                expr = f"{c1}{var1}² − {c2}{var2}"
                
                q_text = f"Find the value of {expr} when {var1} = {v1} and {var2} = {v2}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var1: v1, var2: v2}, "?")
                explanation = f"{expr}\\n= {c1}({v1})² − {c2}({v2})\\n= {c1} × {v1 * v1} − {c2 * v2}\\n= {c1 * v1 * v1} − {c2 * v2}\\n= {result}"
                
            elif q_type == 'sec_hl_style':
                var1, var2 = random.sample(['a', 'b', 'x', 'y'], 2)
                c1 = random.randint(2, 4)
                c2 = random.randint(1, 3)
                v1 = random.randint(2, 4)
                v2 = random.randint(2, 5)
                
                result = c1 * v1 * v1 + c2 * v2
                expr = f"{c1}{var1}² + {c2}{var2}"
                
                q_text = f"Find the value of {expr} when {var1} = {v1} and {var2} = {v2}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var1: v1, var2: v2}, "?")
                explanation = f"{expr}\\n= {c1}({v1})² + {c2}({v2})\\n= {c1} × {v1 * v1} + {c2 * v2}\\n= {c1 * v1 * v1} + {c2 * v2}\\n= {result}"
                
            else:  # mixed_powers
                var = random.choice(['x', 'a', 'n'])
                v = random.randint(2, 4)
                c1 = random.randint(1, 3)
                c2 = random.randint(2, 5)
                
                result = c1 * v * v + c2 * v
                expr = f"{c1}{var}² + {c2}{var}"
                
                q_text = f"Find the value of {expr} when {var} = {v}."
                correct = result
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = generate_substitution_visual_svg(expr, {var: v}, "?")
                explanation = f"{expr}\\n= {c1}({v})² + {c2}({v})\\n= {c1} × {v * v} + {c2 * v}\\n= {c1 * v * v} + {c2 * v}\\n= {result}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 8,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Forming Expressions from Context (Higher)
# ============================================================

def generate_level_9():
    """Forming Expressions from Context - Word problems to algebra"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['perimeter', 'area', 'cost', 'age', 'consecutive'])
            name = random.choice(IRISH_NAMES)
            var = random.choice(['x', 'n', 'w', 'l'])
            
            if q_type == 'perimeter':
                width = random.randint(2, 5)
                
                q_text = f"A rectangle has length {var} cm and width {width} cm. Write an expression for its perimeter."
                correct = f"2{var} + {2 * width}" if width > 1 else f"2{var} + 2"
                
                wrong = [f"{var} + {width}", f"2{var} × {width}", f"{var} + {2 * width}"]
                
                visual = generate_context_expression_svg('perimeter', var, width)
                explanation = f"Perimeter = 2 × length + 2 × width\\n= 2{var} + 2({width})\\n= 2{var} + {2 * width}"
                
            elif q_type == 'area':
                width = random.randint(3, 8)
                
                q_text = f"A rectangle has length {var} cm and width {width} cm. Write an expression for its area."
                correct = f"{width}{var}"
                
                wrong = [f"2{var} + {2 * width}", f"{var} + {width}", f"{width} + {var}"]
                
                visual = None
                explanation = f"Area = length × width\\n= {var} × {width}\\n= {width}{var}"
                
            elif q_type == 'cost':
                item = random.choice(['books', 'pens', 'tickets', 'apples'])
                price = random.randint(3, 12)
                
                q_text = f"{name} buys {var} {item} at €{price} each. Write an expression for the total cost."
                correct = f"€{price}{var}"
                
                wrong = [f"€{var} + {price}", f"€{price} + {var}", f"€{price}/{var}"]
                
                visual = None
                explanation = f"Total cost = price per item × number of items\\n= €{price} × {var}\\n= €{price}{var}"
                
            elif q_type == 'age':
                years = random.randint(3, 10)
                
                q_text = f"{name} is {var} years old. Write an expression for {name}'s age in {years} years' time."
                correct = f"{var} + {years}"
                
                wrong = [f"{years}{var}", f"{var} − {years}", f"{years} − {var}"]
                
                visual = None
                explanation = f"Age in {years} years = current age + {years}\\n= {var} + {years}"
                
            else:  # consecutive
                q_text = f"Three consecutive numbers start with {var}. Write an expression for their sum."
                correct = f"3{var} + 3"
                
                wrong = [f"3{var}", f"{var} + 3", f"{var}³"]
                
                visual = None
                explanation = f"Consecutive numbers: {var}, {var}+1, {var}+2\\nSum = {var} + ({var}+1) + ({var}+2)\\n= 3{var} + 3"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:50]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 9,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Simplifying Complex Expressions (Application)
# ============================================================

def generate_level_10():
    """Simplifying Complex Expressions - SEC HL style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['mixed_squared', 'sec_2025_hl', 'three_terms', 'subtract_squared'])
            var = random.choice(['x', 'y', 'a', 'p'])
            
            if q_type == 'mixed_squared':
                # 5x² − 7x + 3x² − 6x (SEC 2025 HL Q11a)
                c1 = random.randint(3, 7)
                c2 = random.randint(4, 9)
                c3 = random.randint(2, 5)
                c4 = random.randint(3, 8)
                
                q_text = f"Simplify: {c1}{var}² − {c2}{var} + {c3}{var}² − {c4}{var}"
                
                result_sq = c1 + c3
                result_var = c2 + c4
                correct = f"{result_sq}{var}² − {result_var}{var}"
                
                wrong = [
                    f"{c1 + c3 - c2 - c4}{var}²",
                    f"{result_sq}{var}² + {result_var}{var}",
                    f"{result_sq - result_var}{var}²"
                ]
                
                visual = None
                explanation = f"Collect {var}² terms: {c1}{var}² + {c3}{var}² = {result_sq}{var}²\\n" \
                             f"Collect {var} terms: −{c2}{var} − {c4}{var} = −{result_var}{var}\\n" \
                             f"Answer: {correct}"
                
            elif q_type == 'sec_2025_hl':
                c1 = random.randint(4, 8)
                c2 = random.randint(5, 10)
                c3 = random.randint(2, 6)
                c4 = random.randint(4, 9)
                
                q_text = f"Simplify: {c1}{var}² − {c2}{var} + {c3}{var}² − {c4}{var}"
                
                result_sq = c1 + c3
                result_var = c2 + c4
                correct = f"{result_sq}{var}² − {result_var}{var}"
                
                wrong = [
                    f"{result_sq}{var} − {result_var}{var}²",
                    f"{result_sq - result_var}{var}",
                    f"{c1 - c3}{var}² − {c2 - c4}{var}"
                ]
                
                visual = None
                explanation = f"Group like terms:\\n{var}² terms: {c1}{var}² + {c3}{var}² = {result_sq}{var}²\\n" \
                             f"{var} terms: −{c2}{var} − {c4}{var} = −{result_var}{var}\\nAnswer: {correct}"
                
            elif q_type == 'three_terms':
                c1 = random.randint(3, 6)
                c2 = random.randint(2, 5)
                c3 = random.randint(2, 4)
                const1 = random.randint(3, 8)
                const2 = random.randint(2, 6)
                
                q_text = f"Simplify: {c1}{var}² + {c2}{var} − {c3}{var}² + {const1} − {const2}"
                
                result_sq = c1 - c3
                result_const = const1 - const2
                
                if result_const >= 0:
                    correct = f"{result_sq}{var}² + {c2}{var} + {result_const}"
                else:
                    correct = f"{result_sq}{var}² + {c2}{var} − {abs(result_const)}"
                
                wrong = [
                    f"{c1 + c3}{var}² + {c2}{var} + {const1 + const2}",
                    f"{result_sq}{var}² − {c2}{var} + {result_const}",
                    f"{result_sq + c2}{var}² + {result_const}"
                ]
                
                visual = None
                explanation = f"Group like terms:\\n{var}² terms: {c1}{var}² − {c3}{var}² = {result_sq}{var}²\\n" \
                             f"{var} terms: {c2}{var} (unchanged)\\nConstants: {const1} − {const2} = {result_const}\\n" \
                             f"Answer: {correct}"
                
            else:  # subtract_squared
                c1 = random.randint(5, 9)
                c2 = random.randint(3, 7)
                c3 = random.randint(2, 4)
                c4 = random.randint(2, 5)
                
                q_text = f"Simplify: {c1}{var}² + {c2}{var} − ({c3}{var}² − {c4}{var})"
                
                result_sq = c1 - c3
                result_var = c2 + c4
                correct = f"{result_sq}{var}² + {result_var}{var}"
                
                wrong = [
                    f"{c1 + c3}{var}² + {c2 - c4}{var}",
                    f"{result_sq}{var}² − {result_var}{var}",
                    f"{c1 - c3}{var}² + {c2 - c4}{var}"
                ]
                
                visual = None
                explanation = f"First remove bracket (change signs inside):\\n" \
                             f"= {c1}{var}² + {c2}{var} − {c3}{var}² + {c4}{var}\\n" \
                             f"= {result_sq}{var}² + {result_var}{var}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 10,
                'difficulty_band': 'application',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 11: Factorising - Common Factor (Application)
# ============================================================

def generate_level_11():
    """Factorising - Taking out common factor"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['number_factor', 'variable_factor', 'sec_hl_style', 'combined_factor'])
            var = random.choice(['x', 'y', 'a', 'p'])
            
            if q_type == 'number_factor':
                # 6x + 12
                factor = random.randint(2, 6)
                c1 = random.randint(1, 4)
                c2 = random.randint(2, 5)
                
                expr = f"{factor * c1}{var} + {factor * c2}"
                correct = f"{factor}({c1}{var} + {c2})" if c1 > 1 else f"{factor}({var} + {c2})"
                
                q_text = f"Factorise: {expr}"
                
                wrong = [
                    f"{c1}({factor}{var} + {c2})",
                    f"{var}({factor * c1} + {factor * c2})",
                    f"{factor * c1}({var} + {c2})"
                ]
                
                visual = None
                explanation = f"Find the HCF of {factor * c1} and {factor * c2}: it's {factor}\\n" \
                             f"Divide each term by {factor}:\\n{expr} = {correct}"
                
            elif q_type == 'variable_factor':
                # 5x² + 3x
                c1 = random.randint(2, 6)
                c2 = random.randint(2, 5)
                
                expr = f"{c1}{var}² + {c2}{var}"
                correct = f"{var}({c1}{var} + {c2})"
                
                q_text = f"Factorise: {expr}"
                
                wrong = [
                    f"{c1}({var}² + {c2})",
                    f"{var}²({c1} + {c2})",
                    f"{c1}{var}({var} + {c2})"
                ]
                
                visual = None
                explanation = f"Both terms contain {var}\\nTake {var} as common factor:\\n{expr} = {correct}"
                
            elif q_type == 'sec_hl_style':
                # SEC 2022 HL Q9(b): 6x² − 9xy
                factor = random.randint(2, 4)
                c1 = random.randint(2, 4)
                c2 = random.randint(2, 4)
                var2 = 'y' if var == 'x' else 'x'
                
                expr = f"{factor * c1}{var}² − {factor * c2}{var}{var2}"
                correct = f"{factor}{var}({c1}{var} − {c2}{var2})"
                
                q_text = f"Factorise fully: {expr}"
                
                wrong = [
                    f"{factor}({c1}{var}² − {c2}{var}{var2})",
                    f"{var}({factor * c1}{var} − {factor * c2}{var2})",
                    f"{factor * c1}{var}({var} − {c2}{var2})"
                ]
                
                visual = None
                explanation = f"HCF of {factor * c1} and {factor * c2} is {factor}\\n" \
                             f"Both terms contain {var}\\nCommon factor is {factor}{var}\\n" \
                             f"{expr} = {correct}"
                
            else:  # combined_factor
                factor = random.randint(2, 5)
                c1 = random.randint(1, 3)
                c2 = random.randint(2, 4)
                
                expr = f"{factor * c1}{var}² + {factor * c2}{var}"
                correct = f"{factor}{var}({c1}{var} + {c2})" if c1 > 1 else f"{factor}{var}({var} + {c2})"
                
                q_text = f"Factorise fully: {expr}"
                
                wrong = [
                    f"{factor}({c1}{var}² + {c2}{var})",
                    f"{var}({factor * c1}{var} + {factor * c2})",
                    f"{factor * c1}({var}² + {c2}{var})"
                ]
                
                visual = None
                explanation = f"HCF of coefficients: {factor}\\nBoth terms have {var}\\n" \
                             f"Common factor: {factor}{var}\\n{expr} = {correct}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{expr}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 11,
                'difficulty_band': 'application',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 12: Intro to Quadratic Factorising (Mastery)
# ============================================================

def generate_level_12():
    """Intro to Quadratic Factorising - SEC style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['complete_factor', 'factorise_full', 'find_missing', 'expand_check'])
            var = random.choice(['x', 'y', 'a'])
            
            if q_type == 'complete_factor':
                # SEC 2025 OL Q10(d): x² − 10x + 21 = (x − 3)(x − ?)
                # Use factors of constant term that sum to middle coefficient
                a = random.randint(2, 6)
                b = random.randint(2, 6)
                
                # x² - (a+b)x + ab = (x-a)(x-b)
                middle = a + b
                const = a * b
                
                expr = f"{var}² − {middle}{var} + {const}"
                given_factor = a
                missing_factor = b
                
                q_text = f"Factorise: {expr}\\nGiven: {expr} = ({var} − {given_factor})({var} − ?)"
                correct = str(missing_factor)
                
                wrong = get_unique_wrong_numbers(missing_factor, 3, 1, 12)
                wrong = [str(w) for w in wrong]
                
                visual = None
                explanation = f"We need two numbers that:\\n" \
                             f"• Multiply to give {const}\\n• Add to give {middle}\\n" \
                             f"These are {a} and {b}\\n{expr} = ({var} − {a})({var} − {b})"
                
            elif q_type == 'factorise_full':
                # Full factorisation
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                
                # Different cases
                case = random.choice(['both_neg', 'both_pos', 'mixed'])
                
                if case == 'both_neg':
                    # (x-a)(x-b) = x² - (a+b)x + ab
                    middle = a + b
                    const = a * b
                    expr = f"{var}² − {middle}{var} + {const}"
                    correct = f"({var} − {a})({var} − {b})"
                    
                elif case == 'both_pos':
                    # (x+a)(x+b) = x² + (a+b)x + ab
                    middle = a + b
                    const = a * b
                    expr = f"{var}² + {middle}{var} + {const}"
                    correct = f"({var} + {a})({var} + {b})"
                    
                else:  # mixed
                    # (x+a)(x-b) = x² + (a-b)x - ab
                    if a > b:
                        middle = a - b
                        const = a * b
                        expr = f"{var}² + {middle}{var} − {const}"
                        correct = f"({var} + {a})({var} − {b})"
                    else:
                        middle = b - a
                        const = a * b
                        expr = f"{var}² − {middle}{var} − {const}"
                        correct = f"({var} − {b})({var} + {a})"
                
                q_text = f"Factorise: {expr}"
                
                wrong = [
                    f"({var} + {a})({var} + {b})" if 'neg' in case else f"({var} − {a})({var} − {b})",
                    f"({var} − {const})({var} − 1)",
                    f"({var} + {a + b})({var} − {a * b})"
                ]
                wrong = [w for w in wrong if w != correct][:3]
                
                visual = None
                explanation = f"Find two numbers that multiply to give the constant " \
                             f"and add to give the middle coefficient.\\n{expr} = {correct}"
                
            elif q_type == 'find_missing':
                a = random.randint(2, 7)
                b = random.randint(2, 7)
                const = a * b
                
                q_text = f"In the factorisation ({var} − {a})({var} − {b}), " \
                         f"what is the constant term when expanded?"
                correct = const
                wrong = get_unique_wrong_numbers(correct, 3)
                
                visual = None
                explanation = f"When we expand ({var} − {a})({var} − {b}):\\n" \
                             f"The constant term = (−{a}) × (−{b}) = +{const}"
                
            else:  # expand_check
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                
                middle = a + b
                const = a * b
                expanded = f"{var}² + {middle}{var} + {const}"
                
                q_text = f"Which factorisation gives {expanded}?"
                correct = f"({var} + {a})({var} + {b})"
                
                wrong = [
                    f"({var} − {a})({var} − {b})",
                    f"({var} + {a})({var} − {b})",
                    f"({var} + {middle})({var} + {const})"
                ]
                
                visual = None
                explanation = f"({var} + {a})({var} + {b})\\n= {var}² + {b}{var} + {a}{var} + {const}\\n" \
                             f"= {var}² + {middle}{var} + {const} ✓"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:50]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,  # Level 12 is 50% visual
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
    """Validate generated questions"""
    errors = []
    level_counts = {}
    level_visuals = {}
    
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if level not in level_visuals:
            level_visuals[level] = {'total': 0, 'visual': 0}
        level_visuals[level]['total'] += 1
        if q.get('image_svg'):
            level_visuals[level]['visual'] += 1
        
        # Check for duplicate options
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options in '{q['question_text'][:50]}...'")
        
        # Check explanation exists
        if not q.get('explanation'):
            errors.append(f"Level {level}: Missing explanation for '{q['question_text'][:50]}...'")
    
    # Print summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    level_names = {
        1: "Understanding Variables",
        2: "Writing Expressions",
        3: "Collecting Like Terms (Basic)",
        4: "Substitution",
        5: "Expanding Single Brackets",
        6: "Expanding & Simplifying",
        7: "Collecting Terms (Advanced)",
        8: "Substitution with Powers",
        9: "Forming Expressions",
        10: "Complex Expressions",
        11: "Factorising (Common Factor)",
        12: "Quadratic Factorising"
    }
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual_pct = 0
        if level in level_visuals and level_visuals[level]['total'] > 0:
            visual_pct = (level_visuals[level]['visual'] / level_visuals[level]['total']) * 100
        
        status = "✓" if count == QUESTIONS_PER_LEVEL else "✗"
        name = level_names.get(level, "Unknown")
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} | Visual: {visual_pct:5.1f}% | {status} {name}")
    
    print("=" * 60)
    print(f"Total Questions: {len(questions)}")
    print(f"Total Errors: {len(errors)}")
    print("=" * 60)
    
    if errors:
        print("\nErrors found:")
        for e in errors[:10]:
            print(f"  - {e}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
    
    return len(errors)

# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database"""
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete existing questions for this topic/mode
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
    """, (TOPIC, MODE))
    
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions in {MODE} mode")
    
    # Insert new questions
    inserted = 0
    errors = 0
    
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (question_text, option_a, option_b, option_c, option_d,
                 correct_answer, topic, difficulty_level, difficulty_band,
                 mode, explanation, image_svg, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            """, (
                q['question_text'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'], q['explanation'], q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            print(f"Error inserting: {e}")
            errors += 1
    
    conn.commit()
    conn.close()
    
    print(f"Inserted {inserted} questions ({errors} errors)")
    return errors == 0

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("INTRODUCTORY ALGEBRA - JC EXAM QUESTION GENERATOR")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Questions per level: {QUESTIONS_PER_LEVEL}")
    print(f"Total target: {QUESTIONS_PER_LEVEL * 12}")
    print("=" * 60)
    
    all_questions = []
    
    generators = [
        (1, "Understanding Variables", generate_level_1),
        (2, "Writing Expressions", generate_level_2),
        (3, "Collecting Like Terms (Basic)", generate_level_3),
        (4, "Substitution", generate_level_4),
        (5, "Expanding Single Brackets", generate_level_5),
        (6, "Expanding & Simplifying", generate_level_6),
        (7, "Collecting Terms (Advanced)", generate_level_7),
        (8, "Substitution with Powers", generate_level_8),
        (9, "Forming Expressions", generate_level_9),
        (10, "Complex Expressions", generate_level_10),
        (11, "Factorising (Common Factor)", generate_level_11),
        (12, "Quadratic Factorising", generate_level_12),
    ]
    
    for level, name, generator in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = generator()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    # Validate
    error_count = validate_questions(all_questions)
    
    # Ask to insert
    print("=" * 60)
    response = input("Insert questions into database? (y/n): ").strip().lower()
    
    if response == 'y':
        success = insert_questions(all_questions)
        if success:
            print("\n✓ Questions inserted successfully!")
        else:
            print("\n✗ Some errors occurred during insertion")
    else:
        print("Skipped database insertion.")
    
    print("\nDone!")

if __name__ == "__main__":
    main()
