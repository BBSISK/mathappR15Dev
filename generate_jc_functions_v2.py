#!/usr/bin/env python3
"""
AgentMath - Functions Question Generator v2
SEC Junior Cycle Aligned - JC Exam Mode

Version: 2.0
Date: 13 December 2025
Fixes Applied:
  - Function machine graphics show CORRECT operations matching the question
  - SVG visuals pose PROBLEMS, not show answers (Methodology v2.2 Mistake 10)
  - NO \n in question_text (Methodology v2.2 Mistake 9)
  - All questions use clean single-line format

Based on SEC Papers 2022-2025:
- Function notation f(x)
- Input/output tables
- Linear and quadratic functions
- Graph interpretation
- Domain and range

Level Structure:
  L1-3:   Foundation (Notation, Input/Output, Linear Functions)
  L4-6:   Ordinary (Graphing, Slope & Intercept, Interpreting)
  L7-9:   Higher (Quadratic, Parabolas, Domain & Range)
  L10-12: Mastery (Transformations, Composite, Applications)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import math

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'functions'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Siobhán', 
               'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn', 'Éabha', 'Tadhg',
               'Ciara', 'Rian', 'Méabh', 'Cillian', 'Aoibhín', 'Eoin']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    
    unique_wrong = []
    for w in wrong_list:
        w_str = str(w)
        if w_str != correct_str and w_str not in unique_wrong:
            unique_wrong.append(w_str)
    
    options = [correct_str] + unique_wrong[:3]
    
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


# ============================================================
# SVG GENERATORS - VISUALS THAT POSE PROBLEMS, NOT SHOW ANSWERS
# ============================================================

def generate_function_machine_svg(input_val, operation, op_symbol, output_val=None, show_output=False):
    """
    Generate function machine SVG.
    
    CORRECT USAGE (poses problem):
    - Show input and operation, hide output → student calculates output
    - Show input and output, hide operation → student finds operation
    - Show operation and output, hide input → student finds input
    
    WRONG USAGE (reveals answer):
    - Show all three (input, operation, output) when asking what the output is
    """
    svg = '<svg viewBox="0 0 320 100" width="320" height="100">'
    
    # Input box
    svg += '<rect x="10" y="30" width="60" height="40" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="5"/>'
    svg += f'<text x="40" y="55" text-anchor="middle" font-size="16" font-weight="bold">{input_val}</text>'
    svg += '<text x="40" y="20" text-anchor="middle" font-size="11" fill="#64748b">Input</text>'
    
    # Arrow into machine
    svg += '<line x1="70" y1="50" x2="95" y2="50" stroke="#64748b" stroke-width="2"/>'
    svg += '<polygon points="95,45 105,50 95,55" fill="#64748b"/>'
    
    # Function machine box
    svg += '<rect x="105" y="20" width="100" height="60" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="8"/>'
    svg += f'<text x="155" y="55" text-anchor="middle" font-size="18" font-weight="bold">{op_symbol}</text>'
    svg += '<text x="155" y="15" text-anchor="middle" font-size="10" fill="#64748b">Function</text>'
    
    # Arrow out of machine
    svg += '<line x1="205" y1="50" x2="230" y2="50" stroke="#64748b" stroke-width="2"/>'
    svg += '<polygon points="230,45 240,50 230,55" fill="#64748b"/>'
    
    # Output box
    svg += '<rect x="245" y="30" width="60" height="40" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>'
    if show_output and output_val is not None:
        svg += f'<text x="275" y="55" text-anchor="middle" font-size="16" font-weight="bold">{output_val}</text>'
    else:
        svg += '<text x="275" y="55" text-anchor="middle" font-size="20" font-weight="bold" fill="#16a34a">?</text>'
    svg += '<text x="275" y="20" text-anchor="middle" font-size="11" fill="#64748b">Output</text>'
    
    svg += '</svg>'
    return svg


def generate_function_machine_find_operation_svg(input_val, output_val):
    """Function machine where student must find the operation"""
    svg = '<svg viewBox="0 0 320 100" width="320" height="100">'
    
    # Input box
    svg += '<rect x="10" y="30" width="60" height="40" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="5"/>'
    svg += f'<text x="40" y="55" text-anchor="middle" font-size="16" font-weight="bold">{input_val}</text>'
    svg += '<text x="40" y="20" text-anchor="middle" font-size="11" fill="#64748b">Input</text>'
    
    # Arrow into machine
    svg += '<line x1="70" y1="50" x2="95" y2="50" stroke="#64748b" stroke-width="2"/>'
    svg += '<polygon points="95,45 105,50 95,55" fill="#64748b"/>'
    
    # Function machine box with question mark
    svg += '<rect x="105" y="20" width="100" height="60" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="8"/>'
    svg += '<text x="155" y="55" text-anchor="middle" font-size="24" font-weight="bold" fill="#f59e0b">?</text>'
    svg += '<text x="155" y="15" text-anchor="middle" font-size="10" fill="#64748b">Function</text>'
    
    # Arrow out of machine
    svg += '<line x1="205" y1="50" x2="230" y2="50" stroke="#64748b" stroke-width="2"/>'
    svg += '<polygon points="230,45 240,50 230,55" fill="#64748b"/>'
    
    # Output box
    svg += '<rect x="245" y="30" width="60" height="40" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>'
    svg += f'<text x="275" y="55" text-anchor="middle" font-size="16" font-weight="bold">{output_val}</text>'
    svg += '<text x="275" y="20" text-anchor="middle" font-size="11" fill="#64748b">Output</text>'
    
    svg += '</svg>'
    return svg


def generate_function_machine_find_input_svg(operation, op_symbol, output_val):
    """Function machine where student must find the input"""
    svg = '<svg viewBox="0 0 320 100" width="320" height="100">'
    
    # Input box with question mark
    svg += '<rect x="10" y="30" width="60" height="40" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="5"/>'
    svg += '<text x="40" y="55" text-anchor="middle" font-size="20" font-weight="bold" fill="#2563eb">?</text>'
    svg += '<text x="40" y="20" text-anchor="middle" font-size="11" fill="#64748b">Input</text>'
    
    # Arrow into machine
    svg += '<line x1="70" y1="50" x2="95" y2="50" stroke="#64748b" stroke-width="2"/>'
    svg += '<polygon points="95,45 105,50 95,55" fill="#64748b"/>'
    
    # Function machine box
    svg += '<rect x="105" y="20" width="100" height="60" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="8"/>'
    svg += f'<text x="155" y="55" text-anchor="middle" font-size="18" font-weight="bold">{op_symbol}</text>'
    svg += '<text x="155" y="15" text-anchor="middle" font-size="10" fill="#64748b">Function</text>'
    
    # Arrow out of machine
    svg += '<line x1="205" y1="50" x2="230" y2="50" stroke="#64748b" stroke-width="2"/>'
    svg += '<polygon points="230,45 240,50 230,55" fill="#64748b"/>'
    
    # Output box
    svg += '<rect x="245" y="30" width="60" height="40" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>'
    svg += f'<text x="275" y="55" text-anchor="middle" font-size="16" font-weight="bold">{output_val}</text>'
    svg += '<text x="275" y="20" text-anchor="middle" font-size="11" fill="#64748b">Output</text>'
    
    svg += '</svg>'
    return svg


def generate_input_output_table_svg(inputs, outputs, hide_index):
    """
    Generate input/output table with one value hidden.
    hide_index: which output to hide (student must find it)
    """
    svg = '<svg viewBox="0 0 280 100" width="280" height="100">'
    
    # Table header
    svg += '<rect x="10" y="10" width="60" height="30" fill="#2563eb" stroke="#1e40af"/>'
    svg += '<text x="40" y="30" text-anchor="middle" font-size="12" fill="white" font-weight="bold">Input</text>'
    
    svg += '<rect x="10" y="40" width="60" height="30" fill="#16a34a" stroke="#15803d"/>'
    svg += '<text x="40" y="60" text-anchor="middle" font-size="12" fill="white" font-weight="bold">Output</text>'
    
    # Data columns
    for i, (inp, out) in enumerate(zip(inputs, outputs)):
        x = 70 + i * 50
        svg += f'<rect x="{x}" y="10" width="50" height="30" fill="#dbeafe" stroke="#2563eb"/>'
        svg += f'<text x="{x + 25}" y="30" text-anchor="middle" font-size="14" font-weight="bold">{inp}</text>'
        
        svg += f'<rect x="{x}" y="40" width="50" height="30" fill="#dcfce7" stroke="#16a34a"/>'
        if i == hide_index:
            svg += f'<text x="{x + 25}" y="60" text-anchor="middle" font-size="18" font-weight="bold" fill="#16a34a">?</text>'
        else:
            svg += f'<text x="{x + 25}" y="60" text-anchor="middle" font-size="14" font-weight="bold">{out}</text>'
    
    svg += '</svg>'
    return svg


def generate_coordinate_grid_svg(points=None, show_line=False, slope=None, intercept=None, hide_point=None):
    """
    Generate coordinate grid for graphing questions.
    - If hide_point is set, that point shows as ? (student must find it)
    """
    svg = '<svg viewBox="0 0 200 200" width="200" height="200">'
    
    # Background
    svg += '<rect x="0" y="0" width="200" height="200" fill="#f8fafc"/>'
    
    # Grid lines
    for i in range(0, 201, 20):
        svg += f'<line x1="{i}" y1="0" x2="{i}" y2="200" stroke="#e2e8f0" stroke-width="1"/>'
        svg += f'<line x1="0" y1="{i}" x2="200" y2="{i}" stroke="#e2e8f0" stroke-width="1"/>'
    
    # Axes
    svg += '<line x1="100" y1="0" x2="100" y2="200" stroke="#64748b" stroke-width="2"/>'
    svg += '<line x1="0" y1="100" x2="200" y2="100" stroke="#64748b" stroke-width="2"/>'
    
    # Axis labels
    svg += '<text x="190" y="95" font-size="12" fill="#64748b">x</text>'
    svg += '<text x="105" y="15" font-size="12" fill="#64748b">y</text>'
    
    # Scale markers
    for i in range(-4, 5):
        if i != 0:
            x = 100 + i * 20
            svg += f'<text x="{x}" y="115" font-size="9" text-anchor="middle" fill="#64748b">{i}</text>'
            y = 100 - i * 20
            svg += f'<text x="88" y="{y + 3}" font-size="9" text-anchor="end" fill="#64748b">{i}</text>'
    
    # Draw line if specified
    if show_line and slope is not None and intercept is not None:
        # Calculate line endpoints
        x1, x2 = -5, 5
        y1 = slope * x1 + intercept
        y2 = slope * x2 + intercept
        
        # Convert to SVG coordinates
        svg_x1 = 100 + x1 * 20
        svg_y1 = 100 - y1 * 20
        svg_x2 = 100 + x2 * 20
        svg_y2 = 100 - y2 * 20
        
        svg += f'<line x1="{svg_x1}" y1="{svg_y1}" x2="{svg_x2}" y2="{svg_y2}" stroke="#2563eb" stroke-width="2"/>'
    
    # Draw points if specified
    if points:
        for i, (px, py) in enumerate(points):
            svg_x = 100 + px * 20
            svg_y = 100 - py * 20
            
            if hide_point is not None and i == hide_point:
                # Show question mark for hidden point
                svg += f'<circle cx="{svg_x}" cy="{svg_y}" r="12" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>'
                svg += f'<text x="{svg_x}" y="{svg_y + 4}" text-anchor="middle" font-size="12" font-weight="bold" fill="#f59e0b">?</text>'
            else:
                svg += f'<circle cx="{svg_x}" cy="{svg_y}" r="5" fill="#dc2626"/>'
                svg += f'<text x="{svg_x + 8}" y="{svg_y - 5}" font-size="9" fill="#dc2626">({px},{py})</text>'
    
    svg += '</svg>'
    return svg


def generate_parabola_svg(a=1, vertex_x=0, vertex_y=0, show_vertex=True, hide_vertex=False):
    """Generate parabola for quadratic function questions"""
    svg = '<svg viewBox="0 0 200 200" width="200" height="200">'
    
    # Background and grid
    svg += '<rect x="0" y="0" width="200" height="200" fill="#f8fafc"/>'
    for i in range(0, 201, 20):
        svg += f'<line x1="{i}" y1="0" x2="{i}" y2="200" stroke="#e2e8f0" stroke-width="1"/>'
        svg += f'<line x1="0" y1="{i}" x2="200" y2="{i}" stroke="#e2e8f0" stroke-width="1"/>'
    
    # Axes
    svg += '<line x1="100" y1="0" x2="100" y2="200" stroke="#64748b" stroke-width="2"/>'
    svg += '<line x1="0" y1="100" x2="200" y2="100" stroke="#64748b" stroke-width="2"/>'
    
    # Draw parabola
    points = []
    for x in range(-5, 6):
        y = a * (x - vertex_x) ** 2 + vertex_y
        svg_x = 100 + x * 20
        svg_y = 100 - y * 20
        if 0 <= svg_y <= 200:
            points.append(f"{svg_x},{svg_y}")
    
    if len(points) > 1:
        svg += f'<polyline points="{" ".join(points)}" fill="none" stroke="#7c3aed" stroke-width="2"/>'
    
    # Vertex point
    if show_vertex:
        vx = 100 + vertex_x * 20
        vy = 100 - vertex_y * 20
        if hide_vertex:
            svg += f'<circle cx="{vx}" cy="{vy}" r="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>'
            svg += f'<text x="{vx}" y="{vy + 4}" text-anchor="middle" font-size="10" font-weight="bold" fill="#f59e0b">?</text>'
        else:
            svg += f'<circle cx="{vx}" cy="{vy}" r="5" fill="#dc2626"/>'
    
    svg += '</svg>'
    return svg


# ============================================================
# LEVEL 1: Function Notation (Foundation)
# ============================================================

def generate_level_1():
    """Function Notation - Understanding f(x) notation"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['notation_meaning', 'evaluate_simple', 'identify_function', 'notation_read'])
        
        try:
            if q_type == 'notation_meaning':
                a = random.randint(2, 6)
                b = random.randint(1, 8)
                
                q_text = f"If f(x) = {a}x + {b}, what does f(x) represent?"
                correct = "The output when x is the input"
                wrong = ["The value of x", "A constant number", "The equation itself"]
                svg = None
                explanation = f"Step 1: f(x) is function notation\nStep 2: x is the input value\nStep 3: f(x) is the output after applying the rule\nAnswer: {correct}"
                
            elif q_type == 'evaluate_simple':
                a = random.randint(2, 5)
                b = random.randint(1, 6)
                x_val = random.randint(1, 5)
                result = a * x_val + b
                
                q_text = f"If f(x) = {a}x + {b}, find f({x_val})"
                correct = str(result)
                wrong = [str(a + b + x_val), str(a * x_val), str(result + 1)]
                
                # Visual shows the function machine with input, operation, output hidden
                svg = generate_function_machine_svg(x_val, f"×{a} + {b}", f"×{a} +{b}")
                explanation = f"Step 1: Substitute x = {x_val} into f(x) = {a}x + {b}\nStep 2: f({x_val}) = {a}({x_val}) + {b}\nStep 3: = {a * x_val} + {b} = {result}\nAnswer: {result}"
                
            elif q_type == 'identify_function':
                functions = [
                    ("y = 3x + 2", "f(x) = 3x + 2"),
                    ("y = 2x - 1", "f(x) = 2x - 1"),
                    ("y = 5x", "f(x) = 5x"),
                    ("y = x + 4", "f(x) = x + 4")
                ]
                eq, func = random.choice(functions)
                
                q_text = f"Write {eq} using function notation"
                correct = func
                wrong = [f"x = {eq[4:]}", f"f = {eq[4:]}", f"f(y) = {eq[4:]}"]
                svg = None
                explanation = f"Step 1: Replace y with f(x)\nStep 2: {eq} becomes {func}\nAnswer: {correct}"
                
            else:  # notation_read
                a = random.randint(2, 5)
                b = random.randint(1, 5)
                
                q_text = f"What does f({b}) mean for the function f(x) = {a}x?"
                correct = f"The value of {a}x when x = {b}"
                wrong = [f"f multiplied by {b}", f"The {b}th function", f"f plus {b}"]
                svg = None
                explanation = f"Step 1: f({b}) means evaluate f(x) when x = {b}\nStep 2: Substitute x = {b} into the rule\nAnswer: {correct}"
            
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
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 2: Input/Output (Foundation)
# ============================================================

def generate_level_2():
    """Input/Output - Function machines and tables"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['find_output', 'find_input', 'find_operation', 'table_pattern'])
        
        try:
            if q_type == 'find_output':
                # Function machine: given input and operation, find output
                input_val = random.randint(2, 10)
                operations = [
                    (lambda x, n: x + n, '+', random.randint(2, 8)),
                    (lambda x, n: x * n, '×', random.randint(2, 5)),
                    (lambda x, n: x - n, '−', random.randint(1, min(5, input_val - 1))),
                ]
                op_func, op_sym, op_num = random.choice(operations)
                output_val = op_func(input_val, op_num)
                
                op_display = f"{op_sym}{op_num}"
                q_text = f"A function machine has input {input_val} and rule '{op_sym} {op_num}'. What is the output?"
                correct = str(output_val)
                wrong = [str(output_val + 1), str(output_val - 1), str(input_val)]
                
                # CORRECT: Shows input and operation, output is hidden (?)
                svg = generate_function_machine_svg(input_val, f"{op_sym}{op_num}", op_display, show_output=False)
                explanation = f"Step 1: Apply the rule {op_sym} {op_num} to the input {input_val}\nStep 2: {input_val} {op_sym} {op_num} = {output_val}\nAnswer: {output_val}"
                
            elif q_type == 'find_input':
                # Given operation and output, find input
                output_val = random.randint(10, 25)
                op_num = random.randint(2, 6)
                
                if random.choice([True, False]):
                    # Addition: input + n = output, so input = output - n
                    input_val = output_val - op_num
                    op_sym = '+'
                    op_display = f"+{op_num}"
                else:
                    # Multiplication: input × n = output
                    input_val = output_val // op_num
                    output_val = input_val * op_num  # Adjust to make it clean
                    op_sym = '×'
                    op_display = f"×{op_num}"
                
                q_text = f"A function machine has rule '{op_sym} {op_num}' and output {output_val}. What is the input?"
                correct = str(input_val)
                wrong = [str(input_val + 1), str(input_val - 1), str(output_val)]
                
                # CORRECT: Shows operation and output, input is hidden (?)
                svg = generate_function_machine_find_input_svg(f"{op_sym}{op_num}", op_display, output_val)
                explanation = f"Step 1: Work backwards from the output\nStep 2: If {op_sym} {op_num} gives {output_val}, the input must be {input_val}\nAnswer: {input_val}"
                
            elif q_type == 'find_operation':
                # Given input and output, find the operation
                input_val = random.randint(3, 8)
                op_type = random.choice(['add', 'multiply', 'subtract'])
                
                if op_type == 'add':
                    op_num = random.randint(2, 8)
                    output_val = input_val + op_num
                    correct = f"+ {op_num}"
                    wrong = [f"× {op_num}", f"− {op_num}", f"+ {op_num + 1}"]
                elif op_type == 'multiply':
                    op_num = random.randint(2, 5)
                    output_val = input_val * op_num
                    correct = f"× {op_num}"
                    wrong = [f"+ {op_num}", f"× {op_num + 1}", f"+ {output_val - input_val}"]
                else:
                    op_num = random.randint(1, input_val - 1)
                    output_val = input_val - op_num
                    correct = f"− {op_num}"
                    wrong = [f"+ {op_num}", f"− {op_num + 1}", f"× {op_num}"]
                
                q_text = f"Input: {input_val}, Output: {output_val}. What is the function rule?"
                
                # CORRECT: Shows input and output, operation is hidden (?)
                svg = generate_function_machine_find_operation_svg(input_val, output_val)
                explanation = f"Step 1: Compare input {input_val} to output {output_val}\nStep 2: Find what operation transforms {input_val} into {output_val}\nStep 3: {input_val} {correct} = {output_val}\nAnswer: {correct}"
                
            else:  # table_pattern
                # Input/output table with one missing value
                multiplier = random.randint(2, 4)
                add_const = random.randint(0, 5)
                
                inputs = [1, 2, 3, 4]
                outputs = [multiplier * x + add_const for x in inputs]
                hide_idx = random.randint(0, 3)
                
                q_text = f"Find the missing output in the table where f(x) = {multiplier}x" + (f" + {add_const}" if add_const > 0 else "")
                correct = str(outputs[hide_idx])
                wrong = [str(outputs[hide_idx] + 1), str(outputs[hide_idx] - 1), str(inputs[hide_idx] * 2)]
                
                svg = generate_input_output_table_svg(inputs, outputs, hide_idx)
                explanation = f"Step 1: Apply the rule f(x) = {multiplier}x" + (f" + {add_const}" if add_const > 0 else "") + f"\nStep 2: f({inputs[hide_idx]}) = {multiplier}({inputs[hide_idx]})" + (f" + {add_const}" if add_const > 0 else "") + f"\nStep 3: = {outputs[hide_idx]}\nAnswer: {correct}"
            
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
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions


# ============================================================
# LEVEL 3: Linear Functions (Foundation)
# ============================================================

def generate_level_3():
    """Linear Functions - Understanding y = mx + c"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['identify_linear', 'evaluate_linear', 'find_slope', 'find_intercept'])
        
        try:
            if q_type == 'identify_linear':
                linear = random.choice([
                    "y = 3x + 2", "y = 2x - 1", "y = 5x", "y = x + 4", "f(x) = 4x - 3"
                ])
                non_linear = random.choice([
                    "y = x²", "y = 2x² + 1", "y = 1/x", "y = √x"
                ])
                
                if random.choice([True, False]):
                    q_text = f"Which of these is a linear function?"
                    correct = linear
                    wrong = [non_linear, "y = x³", "y = 2ˣ"]
                else:
                    q_text = f"Which of these is NOT a linear function?"
                    correct = non_linear
                    wrong = [linear, "y = 2x", "y = -x + 5"]
                
                svg = None
                explanation = f"Step 1: Linear functions have form y = mx + c\nStep 2: No powers higher than 1, no fractions with x in denominator\nAnswer: {correct}"
                
            elif q_type == 'evaluate_linear':
                m = random.randint(2, 5)
                c = random.randint(-5, 8)
                x_val = random.randint(-3, 5)
                result = m * x_val + c
                
                if c >= 0:
                    func = f"f(x) = {m}x + {c}"
                else:
                    func = f"f(x) = {m}x - {abs(c)}"
                
                q_text = f"For {func}, find f({x_val})"
                correct = str(result)
                wrong = [str(result + 1), str(result - 1), str(m * x_val)]
                
                svg = generate_function_machine_svg(x_val, f"×{m} {'+' if c >= 0 else '-'}{abs(c)}", f"×{m}{'+' if c >= 0 else ''}{c}")
                explanation = f"Step 1: Substitute x = {x_val}\nStep 2: {m}({x_val}) + {c} = {m * x_val} + {c}\nStep 3: = {result}\nAnswer: {result}"
                
            elif q_type == 'find_slope':
                m = random.randint(1, 6)
                c = random.randint(0, 8)
                
                if c > 0:
                    func = f"y = {m}x + {c}"
                elif c < 0:
                    func = f"y = {m}x - {abs(c)}"
                else:
                    func = f"y = {m}x"
                
                q_text = f"What is the slope (gradient) of {func}?"
                correct = str(m)
                wrong = [str(c), str(m + 1), str(m - 1) if m > 1 else "0"]
                
                svg = None
                explanation = f"Step 1: In y = mx + c, m is the slope\nStep 2: Here, m = {m}\nAnswer: {m}"
                
            else:  # find_intercept
                m = random.randint(1, 5)
                c = random.randint(1, 8)
                
                func = f"y = {m}x + {c}"
                
                q_text = f"What is the y-intercept of {func}?"
                correct = str(c)
                wrong = [str(m), str(c + 1), str(m + c)]
                
                svg = None
                explanation = f"Step 1: In y = mx + c, c is the y-intercept\nStep 2: Here, c = {c}\nStep 3: The line crosses the y-axis at (0, {c})\nAnswer: {c}"
            
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
# LEVEL 4: Graphing Lines (Ordinary)
# ============================================================

def generate_level_4():
    """Graphing Lines - Plotting linear functions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['find_point', 'on_line', 'intercept_from_graph', 'missing_coordinate'])
        
        try:
            if q_type == 'find_point':
                m = random.randint(1, 3)
                c = random.randint(-2, 3)
                x_val = random.randint(1, 3)
                y_val = m * x_val + c
                
                q_text = f"For y = {m}x + {c}, what is the y-coordinate when x = {x_val}?"
                correct = str(y_val)
                wrong = [str(y_val + 1), str(y_val - 1), str(x_val)]
                
                # Show graph with the point hidden
                points = [(0, c), (x_val, y_val)]
                svg = generate_coordinate_grid_svg(points=points, show_line=True, slope=m, intercept=c, hide_point=1)
                explanation = f"Step 1: Substitute x = {x_val} into y = {m}x + {c}\nStep 2: y = {m}({x_val}) + {c} = {m * x_val} + {c} = {y_val}\nAnswer: {y_val}"
                
            elif q_type == 'on_line':
                m = random.randint(1, 3)
                c = random.randint(0, 3)
                
                # Create a point on the line
                x_on = random.randint(1, 3)
                y_on = m * x_on + c
                
                # Create a point not on the line
                x_off = random.randint(1, 3)
                y_off = m * x_off + c + random.choice([-2, -1, 1, 2])
                
                if random.choice([True, False]):
                    q_text = f"Which point lies on the line y = {m}x + {c}?"
                    correct = f"({x_on}, {y_on})"
                    wrong = [f"({x_off}, {y_off})", f"({x_on}, {y_on + 1})", f"({x_on + 1}, {y_on})"]
                else:
                    q_text = f"Does the point ({x_on}, {y_on}) lie on y = {m}x + {c}?"
                    correct = "Yes"
                    wrong = ["No", "Cannot tell", "Only if x = 0"]
                
                svg = generate_coordinate_grid_svg(show_line=True, slope=m, intercept=c)
                explanation = f"Step 1: Substitute the x-coordinate into y = {m}x + {c}\nStep 2: Check if y matches\nStep 3: {m}({x_on}) + {c} = {y_on} ✓\nAnswer: {correct}"
                
            elif q_type == 'intercept_from_graph':
                m = random.randint(1, 2)
                c = random.randint(1, 4)
                
                q_text = f"A line passes through (0, {c}) and has slope {m}. What is its equation?"
                correct = f"y = {m}x + {c}"
                wrong = [f"y = {c}x + {m}", f"y = {m}x - {c}", f"y = x + {c}"]
                
                svg = generate_coordinate_grid_svg(points=[(0, c), (2, 2*m + c)], show_line=True, slope=m, intercept=c)
                explanation = f"Step 1: y-intercept is {c}, so c = {c}\nStep 2: Slope is {m}, so m = {m}\nStep 3: y = mx + c = {m}x + {c}\nAnswer: {correct}"
                
            else:  # missing_coordinate
                m = random.randint(1, 3)
                c = random.randint(0, 3)
                x_val = random.randint(1, 3)
                y_val = m * x_val + c
                
                q_text = f"The point ({x_val}, ?) lies on y = {m}x + {c}. Find the missing coordinate."
                correct = str(y_val)
                wrong = [str(y_val + 1), str(y_val - 1), str(x_val + c)]
                
                svg = generate_coordinate_grid_svg(show_line=True, slope=m, intercept=c)
                explanation = f"Step 1: Substitute x = {x_val}\nStep 2: y = {m}({x_val}) + {c} = {y_val}\nAnswer: {y_val}"
            
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
# LEVEL 5: Slope & Intercept (Ordinary)
# ============================================================

def generate_level_5():
    """Slope & Intercept - Finding and interpreting m and c"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['slope_from_points', 'equation_from_points', 'parallel_lines', 'slope_meaning'])
        
        try:
            if q_type == 'slope_from_points':
                x1, x2 = random.randint(0, 3), random.randint(4, 7)
                m = random.randint(1, 3)
                y1 = random.randint(0, 4)
                y2 = y1 + m * (x2 - x1)
                
                q_text = f"Find the slope of the line passing through ({x1}, {y1}) and ({x2}, {y2})"
                correct = str(m)
                wrong = [str(m + 1), str(m - 1) if m > 1 else "0", str((y1 + y2) // 2)]
                
                svg = generate_coordinate_grid_svg(points=[(x1, y1), (x2, y2)], show_line=False)
                explanation = f"Step 1: Slope = (y₂ - y₁)/(x₂ - x₁)\nStep 2: = ({y2} - {y1})/({x2} - {x1})\nStep 3: = {y2 - y1}/{x2 - x1} = {m}\nAnswer: {m}"
                
            elif q_type == 'equation_from_points':
                m = random.randint(1, 2)
                c = random.randint(1, 4)
                x1, x2 = 0, 2
                y1, y2 = c, m * 2 + c
                
                q_text = f"Find the equation of the line through ({x1}, {y1}) and ({x2}, {y2})"
                correct = f"y = {m}x + {c}"
                wrong = [f"y = {c}x + {m}", f"y = {m}x - {c}", f"y = {m + 1}x + {c}"]
                
                svg = generate_coordinate_grid_svg(points=[(x1, y1), (x2, y2)], show_line=True, slope=m, intercept=c)
                explanation = f"Step 1: Find slope: ({y2}-{y1})/({x2}-{x1}) = {m}\nStep 2: y-intercept is {c} (when x=0)\nStep 3: y = {m}x + {c}\nAnswer: {correct}"
                
            elif q_type == 'parallel_lines':
                m = random.randint(2, 5)
                c1 = random.randint(1, 5)
                c2 = random.randint(6, 10)
                
                q_text = f"Lines y = {m}x + {c1} and y = {m}x + {c2} are..."
                correct = "Parallel"
                wrong = ["Perpendicular", "The same line", "Intersecting at origin"]
                
                svg = None
                explanation = f"Step 1: Compare slopes\nStep 2: Both lines have slope {m}\nStep 3: Same slope means parallel lines\nAnswer: Parallel"
                
            else:  # slope_meaning
                contexts = [
                    ("cost of a taxi ride", "€", "km", 2, 5, "cost increases by €2 per km"),
                    ("temperature during the day", "°C", "hour", 3, 10, "temperature rises 3°C per hour"),
                    ("water in a tank", "litres", "minute", -5, 100, "water decreases by 5 litres per minute")
                ]
                context, unit_y, unit_x, m, c, meaning = random.choice(contexts)
                
                if m > 0:
                    func = f"y = {m}x + {c}"
                else:
                    func = f"y = {abs(m)}x + {c}" if m > 0 else f"y = -{abs(m)}x + {c}"
                
                q_text = f"For {context}, {func} where y is in {unit_y} and x is in {unit_x}. What does the slope represent?"
                correct = meaning.capitalize()
                wrong = [f"The starting {unit_y}", f"The final {unit_y}", f"The {unit_x} taken"]
                
                svg = None
                explanation = f"Step 1: Slope shows rate of change\nStep 2: For every 1 {unit_x}, y changes by {m} {unit_y}\nAnswer: {correct}"
            
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
# LEVEL 6: Interpreting Graphs (Ordinary)
# ============================================================

def generate_level_6():
    """Interpreting Graphs - Reading and understanding function graphs"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['increasing_decreasing', 'read_value', 'intercepts', 'real_world'])
        
        try:
            if q_type == 'increasing_decreasing':
                m = random.choice([-2, -1, 1, 2, 3])
                c = random.randint(0, 3)
                
                if m > 0:
                    correct = "Increasing"
                    wrong = ["Decreasing", "Constant", "Undefined"]
                else:
                    correct = "Decreasing"
                    wrong = ["Increasing", "Constant", "Undefined"]
                
                q_text = f"Is the function y = {m}x + {c} increasing or decreasing?"
                svg = generate_coordinate_grid_svg(show_line=True, slope=m, intercept=c)
                explanation = f"Step 1: Look at the slope (m = {m})\nStep 2: Positive slope → increasing, Negative slope → decreasing\nStep 3: m = {m} is {'positive' if m > 0 else 'negative'}\nAnswer: {correct}"
                
            elif q_type == 'read_value':
                m = random.randint(1, 2)
                c = random.randint(0, 3)
                x_val = random.randint(1, 3)
                y_val = m * x_val + c
                
                q_text = f"From the graph of y = {m}x + {c}, find y when x = {x_val}"
                correct = str(y_val)
                wrong = [str(y_val + 1), str(y_val - 1), str(x_val)]
                
                svg = generate_coordinate_grid_svg(show_line=True, slope=m, intercept=c, points=[(x_val, y_val)], hide_point=0)
                explanation = f"Step 1: Go to x = {x_val} on the x-axis\nStep 2: Go up to the line\nStep 3: Read across to y-axis: y = {y_val}\nAnswer: {y_val}"
                
            elif q_type == 'intercepts':
                m = random.randint(1, 3)
                c = random.randint(2, 5)
                
                # x-intercept: when y = 0, x = -c/m
                if c % m == 0:
                    x_int = -c // m
                    q_text = f"Where does y = {m}x + {c} cross the x-axis?"
                    correct = f"({x_int}, 0)"
                    wrong = [f"(0, {c})", f"({c}, 0)", f"({-x_int}, 0)"]
                else:
                    q_text = f"Where does y = {m}x + {c} cross the y-axis?"
                    correct = f"(0, {c})"
                    wrong = [f"({c}, 0)", f"(0, {m})", f"({m}, {c})"]
                
                svg = generate_coordinate_grid_svg(show_line=True, slope=m, intercept=c)
                explanation = f"Step 1: For y-intercept, set x = 0\nStep 2: For x-intercept, set y = 0\nAnswer: {correct}"
                
            else:  # real_world
                name = random.choice(IRISH_NAMES)
                rate = random.randint(2, 5)
                start = random.randint(5, 20)
                
                scenarios = [
                    (f"{name} has €{start} and saves €{rate} per week", "weeks", "€", 
                     f"How much after 4 weeks?", str(start + rate * 4)),
                    (f"A taxi costs €{start} plus €{rate} per km", "km", "€",
                     f"What's the cost for 3 km?", str(start + rate * 3)),
                ]
                context, x_unit, y_unit, question, answer = random.choice(scenarios)
                
                q_text = f"{context}. {question}"
                correct = answer
                wrong = [str(int(answer) + rate), str(int(answer) - rate), str(start)]
                
                svg = None
                explanation = f"Step 1: Starting amount = {start}\nStep 2: Rate of change = {rate} per {x_unit}\nStep 3: Calculate the result\nAnswer: {correct}"
            
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
# LEVEL 7: Quadratic Functions (Higher)
# ============================================================

def generate_level_7():
    """Quadratic Functions - Understanding f(x) = ax² + bx + c"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['identify_quadratic', 'evaluate_quadratic', 'shape_parabola', 'find_coefficients'])
        
        try:
            if q_type == 'identify_quadratic':
                quadratics = ["y = x²", "y = 2x² + 1", "y = x² - 3x", "y = -x² + 4"]
                non_quad = ["y = 2x + 1", "y = 3x", "y = x³", "y = 1/x"]
                
                q_text = "Which of these is a quadratic function?"
                correct = random.choice(quadratics)
                wrong = random.sample(non_quad, 3)
                
                svg = None
                explanation = f"Step 1: Quadratic functions have x² as highest power\nStep 2: Form is y = ax² + bx + c where a ≠ 0\nAnswer: {correct}"
                
            elif q_type == 'evaluate_quadratic':
                a = random.choice([1, 2])
                c = random.randint(0, 5)
                x_val = random.randint(1, 4)
                result = a * x_val * x_val + c
                
                if c > 0:
                    func = f"f(x) = {a if a > 1 else ''}x² + {c}"
                else:
                    func = f"f(x) = {a if a > 1 else ''}x²"
                
                q_text = f"For {func}, find f({x_val})"
                correct = str(result)
                wrong = [str(result + 1), str(a * x_val + c), str(x_val * x_val)]
                
                svg = None
                explanation = f"Step 1: Substitute x = {x_val}\nStep 2: {a}({x_val})² + {c} = {a}({x_val * x_val}) + {c}\nStep 3: = {a * x_val * x_val} + {c} = {result}\nAnswer: {result}"
                
            elif q_type == 'shape_parabola':
                a = random.choice([-2, -1, 1, 2])
                
                if a > 0:
                    q_text = f"For y = {a if abs(a) > 1 else ''}x², does the parabola open upward or downward?"
                    correct = "Upward"
                    wrong = ["Downward", "Sideways", "It's a straight line"]
                else:
                    q_text = f"For y = {a}x², does the parabola open upward or downward?"
                    correct = "Downward"
                    wrong = ["Upward", "Sideways", "It's a straight line"]
                
                svg = generate_parabola_svg(a=a)
                explanation = f"Step 1: Look at coefficient of x² (a = {a})\nStep 2: If a > 0, parabola opens upward (∪ shape)\nStep 3: If a < 0, parabola opens downward (∩ shape)\nAnswer: {correct}"
                
            else:  # find_coefficients
                a = random.choice([1, 2])
                b = random.randint(-3, 3)
                c = random.randint(-2, 4)
                
                if b == 0 and c == 0:
                    func = f"y = {a if a > 1 else ''}x²"
                elif b == 0:
                    func = f"y = {a if a > 1 else ''}x² + {c}" if c > 0 else f"y = {a if a > 1 else ''}x² - {abs(c)}"
                elif c == 0:
                    func = f"y = {a if a > 1 else ''}x² + {b}x" if b > 0 else f"y = {a if a > 1 else ''}x² - {abs(b)}x"
                else:
                    b_str = f"+ {b}x" if b > 0 else f"- {abs(b)}x"
                    c_str = f"+ {c}" if c > 0 else f"- {abs(c)}"
                    func = f"y = {a if a > 1 else ''}x² {b_str} {c_str}"
                
                q_text = f"In {func}, what is the value of a (coefficient of x²)?"
                correct = str(a)
                wrong = [str(b), str(c), str(a + 1)]
                
                svg = None
                explanation = f"Step 1: In y = ax² + bx + c\nStep 2: a is the number multiplying x²\nStep 3: Here a = {a}\nAnswer: {a}"
            
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
# LEVEL 8: Graphing Parabolas (Higher)
# ============================================================

def generate_level_8():
    """Graphing Parabolas - Key features of quadratic graphs"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['find_vertex', 'axis_symmetry', 'roots', 'max_min'])
        
        try:
            if q_type == 'find_vertex':
                h = random.randint(-2, 2)
                k = random.randint(-2, 3)
                
                if h == 0 and k == 0:
                    func = "y = x²"
                elif h == 0:
                    func = f"y = x² + {k}" if k > 0 else f"y = x² - {abs(k)}"
                elif k == 0:
                    func = f"y = (x - {h})²" if h > 0 else f"y = (x + {abs(h)})²"
                else:
                    h_str = f"(x - {h})" if h > 0 else f"(x + {abs(h)})"
                    k_str = f"+ {k}" if k > 0 else f"- {abs(k)}"
                    func = f"y = {h_str}² {k_str}"
                
                q_text = f"Find the vertex of {func}"
                correct = f"({h}, {k})"
                wrong = [f"({k}, {h})", f"({-h}, {k})", f"({h}, {-k})"]
                
                svg = generate_parabola_svg(a=1, vertex_x=h, vertex_y=k, hide_vertex=True)
                explanation = f"Step 1: For y = (x - h)² + k, vertex is (h, k)\nStep 2: Here h = {h} and k = {k}\nAnswer: ({h}, {k})"
                
            elif q_type == 'axis_symmetry':
                h = random.randint(-3, 3)
                k = random.randint(-2, 3)
                
                q_text = f"What is the axis of symmetry for y = (x - {h})² + {k}?" if h > 0 else f"What is the axis of symmetry for y = (x + {abs(h)})² + {k}?"
                correct = f"x = {h}"
                wrong = [f"y = {k}", f"x = {-h}", f"x = {k}"]
                
                svg = generate_parabola_svg(a=1, vertex_x=h, vertex_y=k)
                explanation = f"Step 1: Axis of symmetry passes through vertex\nStep 2: It's a vertical line x = h\nStep 3: Here x = {h}\nAnswer: x = {h}"
                
            elif q_type == 'roots':
                # y = (x - r1)(x - r2) has roots at r1 and r2
                r1 = random.randint(-3, 0)
                r2 = random.randint(1, 4)
                
                # Expand: y = x² - (r1+r2)x + r1*r2
                b = -(r1 + r2)
                c = r1 * r2
                
                if b > 0 and c > 0:
                    func = f"y = x² + {b}x + {c}"
                elif b > 0 and c < 0:
                    func = f"y = x² + {b}x - {abs(c)}"
                elif b < 0 and c > 0:
                    func = f"y = x² - {abs(b)}x + {c}"
                else:
                    func = f"y = x² - {abs(b)}x - {abs(c)}"
                
                q_text = f"What are the x-intercepts (roots) of {func}?"
                correct = f"x = {r1} and x = {r2}"
                wrong = [f"x = {-r1} and x = {-r2}", f"x = {r1 + r2}", f"x = {r1 * r2}"]
                
                svg = generate_parabola_svg(a=1, vertex_x=(r1+r2)/2, vertex_y=-(r2-r1)**2/4)
                explanation = f"Step 1: Set y = 0 and solve\nStep 2: Factorise: (x - {r1})(x - {r2}) = 0\nStep 3: x = {r1} or x = {r2}\nAnswer: {correct}"
                
            else:  # max_min
                a = random.choice([-1, 1])
                k = random.randint(1, 5)
                
                if a > 0:
                    q_text = f"For y = x² + {k}, what is the minimum value of y?"
                    correct = str(k)
                    feature = "minimum"
                else:
                    q_text = f"For y = -x² + {k}, what is the maximum value of y?"
                    correct = str(k)
                    feature = "maximum"
                
                wrong = [str(k + 1), str(k - 1), "0"]
                
                svg = generate_parabola_svg(a=a, vertex_x=0, vertex_y=k)
                explanation = f"Step 1: The {feature} occurs at the vertex\nStep 2: Vertex is at (0, {k})\nStep 3: The {feature} value of y is {k}\nAnswer: {k}"
            
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
# LEVEL 9: Domain & Range (Higher)
# ============================================================

def generate_level_9():
    """Domain & Range - Understanding input and output restrictions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['domain_concept', 'range_concept', 'linear_range', 'quadratic_range',
                                'domain_restricted', 'range_negative_quad', 'domain_set', 'range_from_domain'])
        
        try:
            if q_type == 'domain_concept':
                variations = [
                    ("What is the domain of a function?", "All possible input (x) values",
                     ["All possible output (y) values", "The highest value", "The x-intercept"]),
                    ("The domain of f(x) refers to:", "The set of all valid inputs",
                     ["The set of all outputs", "The maximum value", "The slope"]),
                    ("Which describes the domain?", "All x-values where f(x) is defined",
                     ["All y-values produced", "The y-intercept only", "The gradient"])
                ]
                q_text, correct, wrong = random.choice(variations)
                svg = None
                explanation = "Step 1: Domain refers to inputs\nStep 2: It's all the x-values that can be used\nAnswer: " + correct
                
            elif q_type == 'range_concept':
                variations = [
                    ("What is the range of a function?", "All possible output (y) values",
                     ["All possible input (x) values", "The slope", "The y-intercept"]),
                    ("The range of f(x) represents:", "All values f(x) can produce",
                     ["All values x can take", "The domain", "The x-intercepts"]),
                    ("Which best describes range?", "The set of all output values",
                     ["The set of all input values", "Where the graph crosses x-axis", "The gradient"])
                ]
                q_text, correct, wrong = random.choice(variations)
                svg = None
                explanation = "Step 1: Range refers to outputs\nStep 2: It's all the y-values the function can produce\nAnswer: " + correct
                
            elif q_type == 'linear_range':
                m = random.randint(1, 4)
                c = random.randint(0, 6)
                start = random.randint(0, 3)
                domain_vals = [start, start + 1, start + 2]
                
                q_text = f"For f(x) = {m}x + {c} with domain x ∈ {{{domain_vals[0]}, {domain_vals[1]}, {domain_vals[2]}}}, find the range"
                vals = [m * x + c for x in domain_vals]
                correct = f"{{{vals[0]}, {vals[1]}, {vals[2]}}}"
                wrong = [f"{{{domain_vals[0]}, {domain_vals[1]}, {domain_vals[2]}}}", f"{{{vals[0]}, {vals[2]}}}", f"{{{c}, {m}, {m + c}}}"]
                
                svg = None
                explanation = f"Step 1: Find f({domain_vals[0]}) = {vals[0]}, f({domain_vals[1]}) = {vals[1]}, f({domain_vals[2]}) = {vals[2]}\nStep 2: Range is all output values\nAnswer: {correct}"
                
            elif q_type == 'quadratic_range':
                k = random.randint(1, 8)
                
                q_text = f"For y = x² + {k}, what is the range?"
                correct = f"y ≥ {k}"
                wrong = [f"y ≤ {k}", f"y ≥ 0", "All real numbers"]
                
                svg = generate_parabola_svg(a=1, vertex_x=0, vertex_y=k)
                explanation = f"Step 1: x² is always ≥ 0\nStep 2: So x² + {k} is always ≥ {k}\nStep 3: Range is y ≥ {k}\nAnswer: {correct}"
                
            elif q_type == 'domain_restricted':
                a = random.randint(1, 3)
                b = random.randint(1, 5)
                
                q_text = f"For f(x) = {a}x + {b} where x ≥ 0, what is the domain?"
                correct = "x ≥ 0"
                wrong = [f"y ≥ {b}", "All real numbers", f"x ≥ {b}"]
                
                svg = None
                explanation = f"Step 1: The domain is given as a restriction\nStep 2: x must be greater than or equal to 0\nAnswer: x ≥ 0"
                
            elif q_type == 'range_negative_quad':
                k = random.randint(2, 8)
                
                q_text = f"For y = -x² + {k}, what is the range?"
                correct = f"y ≤ {k}"
                wrong = [f"y ≥ {k}", f"y ≥ 0", f"y ≤ 0"]
                
                svg = generate_parabola_svg(a=-1, vertex_x=0, vertex_y=k)
                explanation = f"Step 1: -x² is always ≤ 0\nStep 2: So -x² + {k} is always ≤ {k}\nStep 3: Maximum is {k} at x = 0\nAnswer: y ≤ {k}"
                
            elif q_type == 'domain_set':
                m = random.randint(2, 5)
                c = random.randint(1, 4)
                x_vals = random.sample(range(0, 6), 3)
                x_vals.sort()
                
                q_text = f"If f(x) = {m}x + {c} has domain {{{x_vals[0]}, {x_vals[1]}, {x_vals[2]}}}, what is f({x_vals[1]})?"
                result = m * x_vals[1] + c
                correct = str(result)
                wrong = [str(result + 1), str(result - 1), str(m * x_vals[0] + c)]
                
                svg = None
                explanation = f"Step 1: f({x_vals[1]}) = {m}({x_vals[1]}) + {c}\nStep 2: = {m * x_vals[1]} + {c} = {result}\nAnswer: {result}"
                
            else:  # range_from_domain
                m = random.randint(1, 3)
                c = random.randint(0, 4)
                x_min = random.randint(0, 2)
                x_max = x_min + random.randint(2, 4)
                
                y_min = m * x_min + c
                y_max = m * x_max + c
                
                q_text = f"For f(x) = {m}x + {c} with {x_min} ≤ x ≤ {x_max}, the range is:"
                correct = f"{y_min} ≤ y ≤ {y_max}"
                wrong = [f"{x_min} ≤ y ≤ {x_max}", f"{y_min} ≤ x ≤ {y_max}", f"y ≥ {y_min}"]
                
                svg = None
                explanation = f"Step 1: Minimum y at x = {x_min}: f({x_min}) = {y_min}\nStep 2: Maximum y at x = {x_max}: f({x_max}) = {y_max}\nStep 3: Range is {y_min} ≤ y ≤ {y_max}\nAnswer: {correct}"
            
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
# LEVEL 10: Transformations (Mastery)
# ============================================================

def generate_level_10():
    """Transformations - Translations and reflections of functions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['vertical_shift', 'horizontal_shift', 'reflection', 'combined',
                                'identify_shift', 'vertex_after_shift', 'shift_direction', 'stretch'])
        
        try:
            if q_type == 'vertical_shift':
                k = random.randint(2, 9)
                direction = random.choice(['up', 'down'])
                base_func = random.choice(['x²', '2x²', 'x² + 1'])
                
                if direction == 'up':
                    q_text = f"y = {base_func} is shifted {k} units up. What is the new equation?"
                    if base_func == 'x²':
                        correct = f"y = x² + {k}"
                    elif base_func == '2x²':
                        correct = f"y = 2x² + {k}"
                    else:
                        correct = f"y = x² + {1 + k}"
                    wrong = [f"y = x² - {k}", f"y = (x + {k})²", f"y = (x - {k})²"]
                else:
                    q_text = f"y = {base_func} is shifted {k} units down. What is the new equation?"
                    if base_func == 'x²':
                        correct = f"y = x² - {k}"
                    elif base_func == '2x²':
                        correct = f"y = 2x² - {k}"
                    else:
                        correct = f"y = x² + {1 - k}" if k < 1 else f"y = x² - {k - 1}"
                    wrong = [f"y = x² + {k}", f"y = (x - {k})²", f"y = (x + {k})²"]
                
                svg = None
                explanation = f"Step 1: Vertical shift affects the constant\nStep 2: Up means +, down means -\nAnswer: {correct}"
                
            elif q_type == 'horizontal_shift':
                h = random.randint(2, 8)
                direction = random.choice(['left', 'right'])
                
                if direction == 'right':
                    q_text = f"y = x² is shifted {h} units right. What is the new equation?"
                    correct = f"y = (x - {h})²"
                    wrong = [f"y = (x + {h})²", f"y = x² + {h}", f"y = x² - {h}"]
                else:
                    q_text = f"y = x² is shifted {h} units left. What is the new equation?"
                    correct = f"y = (x + {h})²"
                    wrong = [f"y = (x - {h})²", f"y = x² - {h}", f"y = x² + {h}"]
                
                svg = None
                explanation = f"Step 1: Horizontal shift affects x inside the function\nStep 2: Right means (x - h), left means (x + h)\nAnswer: {correct}"
                
            elif q_type == 'reflection':
                variations = [
                    ("y = x² is reflected in the x-axis. What is the new equation?", "y = -x²",
                     ["y = x²", "y = (-x)²", "y = x² - 1"]),
                    ("y = 2x² is reflected in the x-axis. What is the new equation?", "y = -2x²",
                     ["y = 2x²", "y = (-2x)²", "y = 2x² - 1"]),
                    ("What happens to y = x² when multiplied by -1?", "It reflects in the x-axis",
                     ["It shifts up", "It shifts right", "It gets wider"])
                ]
                q_text, correct, wrong = random.choice(variations)
                svg = None
                explanation = "Step 1: Reflection in x-axis flips the y-values\nStep 2: Multiply the whole function by -1\nAnswer: " + correct
                
            elif q_type == 'combined':
                h = random.randint(1, 5)
                k = random.randint(1, 5)
                
                directions = [
                    (f"{h} right and {k} up", f"y = (x - {h})² + {k}"),
                    (f"{h} left and {k} up", f"y = (x + {h})² + {k}"),
                    (f"{h} right and {k} down", f"y = (x - {h})² - {k}"),
                    (f"{h} left and {k} down", f"y = (x + {h})² - {k}")
                ]
                desc, correct = random.choice(directions)
                
                q_text = f"y = x² is shifted {desc}. What is the new equation?"
                wrong = [f"y = (x + {h})² + {k}", f"y = (x - {h})² - {k}", f"y = x² + {h} + {k}"]
                
                svg = None
                explanation = f"Step 1: Apply horizontal shift to x\nStep 2: Apply vertical shift as constant\nAnswer: {correct}"
                
            elif q_type == 'identify_shift':
                h = random.randint(1, 5)
                k = random.randint(1, 5)
                
                variations = [
                    (f"y = (x - {h})² + {k}", f"{h} right and {k} up"),
                    (f"y = (x + {h})² - {k}", f"{h} left and {k} down"),
                    (f"y = (x - {h})²", f"{h} right"),
                    (f"y = x² + {k}", f"{k} up")
                ]
                func, correct = random.choice(variations)
                
                q_text = f"How has y = x² been transformed to get {func}?"
                wrong = [f"{h} left and {k} down", f"{k} right", f"{h} down"]
                
                svg = None
                explanation = f"Step 1: (x - h) means right h, (x + h) means left h\nStep 2: +k means up k, -k means down k\nAnswer: {correct}"
                
            elif q_type == 'vertex_after_shift':
                h = random.randint(1, 4)
                k = random.randint(1, 4)
                
                q_text = f"y = x² has vertex (0, 0). After shifting {h} right and {k} up, what is the new vertex?"
                correct = f"({h}, {k})"
                wrong = [f"({-h}, {k})", f"({h}, {-k})", f"({k}, {h})"]
                
                svg = generate_parabola_svg(a=1, vertex_x=h, vertex_y=k, hide_vertex=True)
                explanation = f"Step 1: Original vertex is (0, 0)\nStep 2: Right {h} changes x to {h}\nStep 3: Up {k} changes y to {k}\nAnswer: ({h}, {k})"
                
            elif q_type == 'shift_direction':
                h = random.randint(2, 6)
                
                variations = [
                    (f"y = (x - {h})² compared to y = x² is shifted:", f"{h} units right",
                     [f"{h} units left", f"{h} units up", f"{h} units down"]),
                    (f"y = (x + {h})² compared to y = x² is shifted:", f"{h} units left",
                     [f"{h} units right", f"{h} units up", f"{h} units down"]),
                    (f"To shift y = x² right by {h}, we write:", f"y = (x - {h})²",
                     [f"y = (x + {h})²", f"y = x² + {h}", f"y = x² - {h}"])
                ]
                q_text, correct, wrong = random.choice(variations)
                
                svg = None
                explanation = f"Step 1: (x - h) shifts RIGHT by h\nStep 2: (x + h) shifts LEFT by h\nAnswer: {correct}"
                
            else:  # stretch
                a = random.choice([2, 3, 4])
                
                variations = [
                    (f"y = {a}x² compared to y = x² is:", "Narrower/steeper",
                     ["Wider/flatter", "Shifted up", "Shifted right"]),
                    (f"y = x²/{a} compared to y = x² is:", "Wider/flatter",
                     ["Narrower/steeper", "Shifted down", "Reflected"]),
                    (f"What does the {a} do in y = {a}x²?", "Makes the parabola narrower",
                     ["Shifts it up {a}", "Shifts it right {a}", "Reflects it"])
                ]
                q_text, correct, wrong = random.choice(variations)
                
                svg = None
                explanation = f"Step 1: Coefficient > 1 makes parabola narrower\nStep 2: Coefficient < 1 makes it wider\nAnswer: {correct}"
            
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
# LEVEL 11: Composite Functions (Mastery)
# ============================================================

def generate_level_11():
    """Composite Functions - f(g(x)) and g(f(x))"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['fg_value', 'gf_value', 'fg_expression', 'concept'])
        
        try:
            if q_type == 'fg_value':
                # f(g(x)) at a specific value
                a, b = random.randint(2, 4), random.randint(1, 5)
                c, d = random.randint(2, 4), random.randint(1, 5)
                x_val = random.randint(1, 3)
                
                # g(x) = cx + d, f(x) = ax + b
                g_val = c * x_val + d
                fg_val = a * g_val + b
                
                q_text = f"If f(x) = {a}x + {b} and g(x) = {c}x + {d}, find f(g({x_val}))"
                correct = str(fg_val)
                wrong = [str(fg_val + 1), str(a * x_val + b), str(c * x_val + d)]
                
                svg = None
                explanation = f"Step 1: First find g({x_val}) = {c}({x_val}) + {d} = {g_val}\nStep 2: Then find f({g_val}) = {a}({g_val}) + {b} = {fg_val}\nAnswer: {fg_val}"
                
            elif q_type == 'gf_value':
                a, b = random.randint(2, 3), random.randint(1, 4)
                c, d = random.randint(2, 3), random.randint(1, 4)
                x_val = random.randint(1, 3)
                
                f_val = a * x_val + b
                gf_val = c * f_val + d
                
                q_text = f"If f(x) = {a}x + {b} and g(x) = {c}x + {d}, find g(f({x_val}))"
                correct = str(gf_val)
                wrong = [str(gf_val + 1), str(f_val), str(a * x_val + b + d)]
                
                svg = None
                explanation = f"Step 1: First find f({x_val}) = {a}({x_val}) + {b} = {f_val}\nStep 2: Then find g({f_val}) = {c}({f_val}) + {d} = {gf_val}\nAnswer: {gf_val}"
                
            elif q_type == 'fg_expression':
                a = random.randint(2, 3)
                b = random.randint(1, 4)
                
                # f(x) = ax, g(x) = x + b
                # f(g(x)) = a(x + b) = ax + ab
                result_const = a * b
                
                q_text = f"If f(x) = {a}x and g(x) = x + {b}, find f(g(x))"
                correct = f"{a}x + {result_const}"
                wrong = [f"{a}x + {b}", f"x + {result_const}", f"{a + b}x"]
                
                svg = None
                explanation = f"Step 1: g(x) = x + {b}\nStep 2: f(g(x)) = f(x + {b}) = {a}(x + {b})\nStep 3: = {a}x + {result_const}\nAnswer: {correct}"
                
            else:  # concept
                q_text = "What does f(g(x)) mean?"
                correct = "Apply g first, then apply f to the result"
                wrong = ["Apply f first, then g", "Multiply f and g", "Add f and g"]
                
                svg = None
                explanation = "Step 1: In f(g(x)), work from inside out\nStep 2: First calculate g(x)\nStep 3: Then use that result as input to f\nAnswer: Apply g first, then apply f to the result"
            
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
# LEVEL 12: Applications (Mastery)
# ============================================================

def generate_level_12():
    """Applications - Real-world problems using functions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['projectile', 'profit', 'area_function', 'physics'])
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'projectile':
                # Height of ball: h(t) = -5t² + vt + h0
                v = random.randint(15, 25)
                h0 = random.randint(1, 5)
                
                q_text = f"A ball is thrown up with h(t) = -{5}t² + {v}t + {h0} metres. What is the initial height?"
                correct = f"{h0} m"
                wrong = [f"{v} m", f"0 m", f"{v + h0} m"]
                
                svg = None
                explanation = f"Step 1: Initial height is when t = 0\nStep 2: h(0) = -5(0)² + {v}(0) + {h0}\nStep 3: = {h0}\nAnswer: {h0} m"
                
            elif q_type == 'profit':
                # Profit function P(x) = -x² + bx - c
                b = random.randint(10, 20)
                c = random.randint(5, 15)
                x_val = random.randint(2, 5)
                profit = -x_val * x_val + b * x_val - c
                
                q_text = f"A company's profit is P(x) = -x² + {b}x - {c} in thousands. Find P({x_val})."
                correct = f"€{profit},000"
                wrong = [f"€{profit + 1},000", f"€{b * x_val},000", f"€{abs(profit)},000"]
                
                svg = None
                explanation = f"Step 1: Substitute x = {x_val}\nStep 2: P({x_val}) = -({x_val})² + {b}({x_val}) - {c}\nStep 3: = -{x_val * x_val} + {b * x_val} - {c} = {profit}\nAnswer: €{profit},000"
                
            elif q_type == 'area_function':
                # Area of rectangle with constraint
                p = random.randint(16, 24)  # perimeter = 2(l + w), so l + w = p/2
                half_p = p // 2
                
                # If width = x, length = half_p - x
                # Area = x(half_p - x) = half_p*x - x²
                
                q_text = f"A rectangle has perimeter {p}m. If width = x, the area function is A(x) = x({half_p} - x). Find A(4)."
                result = 4 * (half_p - 4)
                correct = f"{result} m²"
                wrong = [f"{4 * half_p} m²", f"{half_p - 4} m²", f"{result + 4} m²"]
                
                svg = None
                explanation = f"Step 1: A(x) = x({half_p} - x)\nStep 2: A(4) = 4({half_p} - 4) = 4({half_p - 4})\nStep 3: = {result}\nAnswer: {result} m²"
                
            else:  # physics
                # Distance-time: d(t) = at² + bt
                a = random.randint(1, 3)
                b = random.randint(5, 10)
                t_val = random.randint(2, 4)
                
                distance = a * t_val * t_val + b * t_val
                
                q_text = f"{name}'s distance is d(t) = {a}t² + {b}t metres. Find the distance after {t_val} seconds."
                correct = f"{distance} m"
                wrong = [f"{a * t_val + b} m", f"{distance + t_val} m", f"{a + b} m"]
                
                svg = None
                explanation = f"Step 1: Substitute t = {t_val}\nStep 2: d({t_val}) = {a}({t_val})² + {b}({t_val})\nStep 3: = {a * t_val * t_val} + {b * t_val} = {distance}\nAnswer: {distance} m"
            
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
    visual_issues = []
    
    for i, q in enumerate(questions):
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        # Check unique options
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level} Q{i}: Duplicate options")
        
        # Check for literal \n in question text
        if '\\n' in q['question_text'] or '\n' in q['question_text']:
            newline_issues.append(f"Level {level}: Newline in '{q['question_text'][:40]}...'")
        
        # Check options for \n
        for opt in options:
            if '\\n' in str(opt) or '\n' in str(opt):
                newline_issues.append(f"Level {level}: Newline in option")
    
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
        print("\n⚠️  NEWLINE ISSUES:")
        for issue in newline_issues[:5]:
            print(f"  - {issue}")
    
    print("="*60)
    
    return len(errors) + len(newline_issues)


# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing questions for topic '{TOPIC}'")
    
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
    print("AgentMath - Functions Generator v2")
    print("="*60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Target: {QUESTIONS_PER_LEVEL * 12} questions (50 per level × 12 levels)")
    print("="*60)
    print("\nKey fixes in v2:")
    print("  ✓ Function machine graphics match the question operation")
    print("  ✓ Visuals pose problems (? for unknown), don't reveal answers")
    print("  ✓ No \\n in question text")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Function Notation", generate_level_1),
        (2, "Input/Output", generate_level_2),
        (3, "Linear Functions", generate_level_3),
        (4, "Graphing Lines", generate_level_4),
        (5, "Slope & Intercept", generate_level_5),
        (6, "Interpreting Graphs", generate_level_6),
        (7, "Quadratic Functions", generate_level_7),
        (8, "Graphing Parabolas", generate_level_8),
        (9, "Domain & Range", generate_level_9),
        (10, "Transformations", generate_level_10),
        (11, "Composite Functions", generate_level_11),
        (12, "Applications", generate_level_12),
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
