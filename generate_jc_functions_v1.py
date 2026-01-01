#!/usr/bin/env python3
"""
AgentMath - Functions Topic Generator v1
SEC Junior Cycle Mathematics - Adaptive Quiz System

Generates 600 questions (50 per level × 12 levels) for the Functions topic.
Aligned with SEC Junior Cycle Mathematics Specification.

Level Structure:
  Level 1:  Understanding Function Notation (Foundation)
  Level 2:  Evaluating Simple Functions (Foundation)
  Level 3:  Evaluating with Multiplication (Foundation)
  Level 4:  Linear Functions f(x) = ax + b (Ordinary)
  Level 5:  Finding Input from Output (Ordinary)
  Level 6:  Completing Function Tables (Ordinary)
  Level 7:  Finding Constants (Higher)
  Level 8:  Reading Function Graphs (Higher)
  Level 9:  Quadratic Functions (Higher)
  Level 10: Composite Functions (Higher)
  Level 11: Interpreting Real-World Graphs (Application)
  Level 12: Problem Solving & Applications (Mastery)

SEC Reference Questions:
  - 2022 OL Q13(b): f(x) = 2x − 1, Find f(3), Find x if f(x) = 9
  - 2023 OL Q7: Function counts letters f(cat) = 3
  - 2023 HL Q11(c): g(x) = 3x + k, g(2) = 11, find k
  - 2024 HL Q8: Complete table, draw graph, estimate f(x) = 5
  - 2025 HL Q9: Temperature function, match functions to graph sections
  - 2025 HL Q12(a): f(x) = 2/(x+2), complete table, draw graph

Author: AgentMath Generator
Version: 1.0
Date: December 2025
"""

import random
import sqlite3
import os
from datetime import datetime

# ============================================================
# SVG VISUAL GENERATORS
# ============================================================

def generate_function_machine_svg(input_val, operation, output_val, func_name='f'):
    """Generate SVG showing a function machine"""
    width = 280
    height = 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f0f9ff" rx="8"/>'
    
    # Input arrow
    svg += '<path d="M20,50 L60,50" stroke="#3b82f6" stroke-width="3" marker-end="url(#arrow)"/>'
    svg += f'<text x="15" y="35" font-size="14" font-weight="bold" fill="#1e40af">{input_val}</text>'
    
    # Function box
    svg += '<rect x="70" y="20" width="120" height="60" fill="#3b82f6" stroke="#1e40af" stroke-width="2" rx="8"/>'
    svg += f'<text x="130" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="white">{func_name}(x) = {operation}</text>'
    svg += f'<text x="130" y="65" text-anchor="middle" font-size="12" fill="#bfdbfe">Function Machine</text>'
    
    # Output arrow
    svg += '<path d="M200,50 L240,50" stroke="#22c55e" stroke-width="3" marker-end="url(#arrow2)"/>'
    svg += f'<text x="250" y="55" font-size="16" font-weight="bold" fill="#166534">{output_val}</text>'
    
    # Arrow markers
    svg += '<defs>'
    svg += '<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#3b82f6"/></marker>'
    svg += '<marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#22c55e"/></marker>'
    svg += '</defs>'
    
    svg += '</svg>'
    return svg


def generate_function_table_svg(func_expr, x_values, y_values, missing_idx=None, func_name='f'):
    """Generate SVG showing a function table"""
    n = len(x_values)
    cell_width = 50
    width = (n + 1) * cell_width + 40
    height = 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#fefce8" rx="8"/>'
    
    # Header: function expression
    svg += f'<text x="{width//2}" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">{func_name}(x) = {func_expr}</text>'
    
    # x row header
    svg += f'<rect x="20" y="28" width="{cell_width}" height="28" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>'
    svg += f'<text x="{20 + cell_width//2}" y="47" text-anchor="middle" font-size="13" font-weight="bold" fill="#713f12">x</text>'
    
    # x values
    for i, x in enumerate(x_values):
        x_pos = 20 + (i + 1) * cell_width
        svg += f'<rect x="{x_pos}" y="28" width="{cell_width}" height="28" fill="#fef9c3" stroke="#ca8a04" stroke-width="1"/>'
        svg += f'<text x="{x_pos + cell_width//2}" y="47" text-anchor="middle" font-size="13" fill="#713f12">{x}</text>'
    
    # f(x) row header
    svg += f'<rect x="20" y="56" width="{cell_width}" height="28" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>'
    svg += f'<text x="{20 + cell_width//2}" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#713f12">{func_name}(x)</text>'
    
    # y values
    for i, y in enumerate(y_values):
        x_pos = 20 + (i + 1) * cell_width
        fill = "#ffffff" if missing_idx is None or i != missing_idx else "#fef08a"
        svg += f'<rect x="{x_pos}" y="56" width="{cell_width}" height="28" fill="{fill}" stroke="#ca8a04" stroke-width="1"/>'
        display = y if (missing_idx is None or i != missing_idx) else "?"
        svg += f'<text x="{x_pos + cell_width//2}" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e293b">{display}</text>'
    
    svg += '</svg>'
    return svg


def generate_linear_graph_svg(m, c, highlight_point=None, show_equation=True):
    """Generate SVG showing a linear function graph"""
    width = 220
    height = 200
    
    # Graph area
    margin = 30
    graph_width = width - 2 * margin
    graph_height = height - 2 * margin
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="8"/>'
    
    # Grid
    for i in range(7):
        x = margin + i * graph_width / 6
        svg += f'<line x1="{x}" y1="{margin}" x2="{x}" y2="{height-margin}" stroke="#e2e8f0" stroke-width="1"/>'
    for i in range(7):
        y = margin + i * graph_height / 6
        svg += f'<line x1="{margin}" y1="{y}" x2="{width-margin}" y2="{y}" stroke="#e2e8f0" stroke-width="1"/>'
    
    # Axes
    svg += f'<line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="#64748b" stroke-width="2"/>'
    svg += f'<line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height-margin}" stroke="#64748b" stroke-width="2"/>'
    
    # Axis labels
    svg += f'<text x="{width-margin+5}" y="{height-margin+5}" font-size="12" fill="#64748b">x</text>'
    svg += f'<text x="{margin-5}" y="{margin-5}" font-size="12" fill="#64748b">y</text>'
    
    # Scale: x from -1 to 5, y from -2 to 10
    def to_screen_x(x_val):
        return margin + (x_val + 1) * graph_width / 6
    
    def to_screen_y(y_val):
        return height - margin - (y_val + 2) * graph_height / 12
    
    # Draw line
    x1, x2 = -1, 5
    y1, y2 = m * x1 + c, m * x2 + c
    
    # Clip to visible area
    y1 = max(-2, min(10, y1))
    y2 = max(-2, min(10, y2))
    
    svg += f'<line x1="{to_screen_x(x1)}" y1="{to_screen_y(y1)}" x2="{to_screen_x(x2)}" y2="{to_screen_y(y2)}" stroke="#3b82f6" stroke-width="2.5"/>'
    
    # Highlight point if specified
    if highlight_point:
        px, py = highlight_point
        svg += f'<circle cx="{to_screen_x(px)}" cy="{to_screen_y(py)}" r="6" fill="#ef4444" stroke="white" stroke-width="2"/>'
        svg += f'<text x="{to_screen_x(px)+10}" y="{to_screen_y(py)-5}" font-size="11" fill="#dc2626">({px}, {py})</text>'
    
    # Equation label
    if show_equation:
        if c >= 0:
            eq = f"f(x) = {m}x + {c}" if m != 1 else f"f(x) = x + {c}"
        else:
            eq = f"f(x) = {m}x - {abs(c)}" if m != 1 else f"f(x) = x - {abs(c)}"
        if c == 0:
            eq = f"f(x) = {m}x" if m != 1 else "f(x) = x"
        svg += f'<text x="{width//2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">{eq}</text>'
    
    # X-axis numbers
    for i in range(7):
        x_val = i - 1
        svg += f'<text x="{to_screen_x(x_val)}" y="{height-margin+15}" text-anchor="middle" font-size="9" fill="#64748b">{x_val}</text>'
    
    svg += '</svg>'
    return svg


def generate_quadratic_graph_svg(a=1, b=0, c=0, highlight_point=None):
    """Generate SVG showing a quadratic function graph"""
    width = 220
    height = 200
    
    margin = 30
    graph_width = width - 2 * margin
    graph_height = height - 2 * margin
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f0fdf4" rx="8"/>'
    
    # Grid
    for i in range(7):
        x = margin + i * graph_width / 6
        svg += f'<line x1="{x}" y1="{margin}" x2="{x}" y2="{height-margin}" stroke="#dcfce7" stroke-width="1"/>'
    for i in range(7):
        y = margin + i * graph_height / 6
        svg += f'<line x1="{margin}" y1="{y}" x2="{width-margin}" y2="{y}" stroke="#dcfce7" stroke-width="1"/>'
    
    # Axes
    svg += f'<line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="#64748b" stroke-width="2"/>'
    svg += f'<line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height-margin}" stroke="#64748b" stroke-width="2"/>'
    
    # Scale: x from -3 to 3, y from -1 to 11
    def to_screen_x(x_val):
        return margin + (x_val + 3) * graph_width / 6
    
    def to_screen_y(y_val):
        return height - margin - (y_val + 1) * graph_height / 12
    
    # Draw parabola as path
    points = []
    for i in range(-30, 31):
        x_val = i / 10
        y_val = a * x_val * x_val + b * x_val + c
        if -1 <= y_val <= 11:
            points.append((to_screen_x(x_val), to_screen_y(y_val)))
    
    if points:
        path = f'M{points[0][0]},{points[0][1]} '
        for px, py in points[1:]:
            path += f'L{px},{py} '
        svg += f'<path d="{path}" stroke="#22c55e" stroke-width="2.5" fill="none"/>'
    
    # Highlight point
    if highlight_point:
        px, py = highlight_point
        svg += f'<circle cx="{to_screen_x(px)}" cy="{to_screen_y(py)}" r="6" fill="#ef4444" stroke="white" stroke-width="2"/>'
        svg += f'<text x="{to_screen_x(px)+10}" y="{to_screen_y(py)-5}" font-size="11" fill="#dc2626">({px}, {py})</text>'
    
    # Equation label
    if b == 0 and c == 0:
        eq = f"f(x) = x²" if a == 1 else f"f(x) = {a}x²"
    elif c == 0:
        eq = f"f(x) = x² + {b}x" if a == 1 else f"f(x) = {a}x² + {b}x"
    else:
        sign = '+' if c >= 0 else '-'
        eq = f"f(x) = x² {sign} {abs(c)}" if a == 1 and b == 0 else f"f(x) = {a}x² + {b}x {sign} {abs(c)}"
    
    svg += f'<text x="{width//2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">{eq}</text>'
    
    svg += '</svg>'
    return svg


def generate_input_output_svg(inputs, outputs, operation_label="f"):
    """Generate SVG showing input-output mapping"""
    width = 200
    height = 40 + len(inputs) * 35
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#faf5ff" rx="8"/>'
    
    # Header
    svg += f'<text x="50" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">Input</text>'
    svg += f'<text x="100" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">{operation_label}</text>'
    svg += f'<text x="150" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">Output</text>'
    
    for i, (inp, out) in enumerate(zip(inputs, outputs)):
        y = 45 + i * 35
        
        # Input circle
        svg += f'<circle cx="50" cy="{y}" r="15" fill="#ddd6fe" stroke="#7c3aed" stroke-width="2"/>'
        svg += f'<text x="50" y="{y+5}" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">{inp}</text>'
        
        # Arrow
        svg += f'<path d="M70,{y} L130,{y}" stroke="#a78bfa" stroke-width="2" marker-end="url(#purplearrow)"/>'
        
        # Output circle
        svg += f'<circle cx="150" cy="{y}" r="15" fill="#c4b5fd" stroke="#7c3aed" stroke-width="2"/>'
        svg += f'<text x="150" y="{y+5}" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">{out}</text>'
    
    svg += '<defs><marker id="purplearrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a78bfa"/></marker></defs>'
    
    svg += '</svg>'
    return svg


def generate_composite_function_svg(f_expr, g_expr, x_val, intermediate, final):
    """Generate SVG showing composite function evaluation"""
    width = 320
    height = 90
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#fff7ed" rx="8"/>'
    
    # x value
    svg += '<circle cx="30" cy="50" r="18" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>'
    svg += f'<text x="30" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">{x_val}</text>'
    svg += '<text x="30" y="80" text-anchor="middle" font-size="10" fill="#9a3412">x</text>'
    
    # First function g
    svg += '<path d="M55,50 L85,50" stroke="#f97316" stroke-width="2" marker-end="url(#orangearrow)"/>'
    svg += '<rect x="90" y="30" width="70" height="40" fill="#fb923c" stroke="#ea580c" stroke-width="2" rx="6"/>'
    svg += f'<text x="125" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="white">g(x)={g_expr}</text>'
    
    # Intermediate value
    svg += '<path d="M165,50 L195,50" stroke="#f97316" stroke-width="2" marker-end="url(#orangearrow)"/>'
    svg += '<circle cx="215" cy="50" r="18" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>'
    svg += f'<text x="215" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">{intermediate}</text>'
    svg += '<text x="215" y="80" text-anchor="middle" font-size="10" fill="#9a3412">g(x)</text>'
    
    # Second function f
    svg += '<path d="M238,50 L258,50" stroke="#22c55e" stroke-width="2" marker-end="url(#greenarrow)"/>'
    svg += '<circle cx="290" cy="50" r="22" fill="#22c55e" stroke="#166534" stroke-width="2"/>'
    svg += f'<text x="290" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="white">{final}</text>'
    svg += '<text x="290" y="80" text-anchor="middle" font-size="10" fill="#166534">f(g(x))</text>'
    
    svg += '<defs>'
    svg += '<marker id="orangearrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#f97316"/></marker>'
    svg += '<marker id="greenarrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#22c55e"/></marker>'
    svg += '</defs>'
    
    svg += '</svg>'
    return svg


def generate_real_world_graph_svg(title, x_label, y_label, points, highlight_x=None):
    """Generate SVG showing a real-world function graph"""
    width = 260
    height = 180
    
    margin_left = 45
    margin_bottom = 35
    margin_top = 30
    margin_right = 20
    
    graph_width = width - margin_left - margin_right
    graph_height = height - margin_top - margin_bottom
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ecfeff" rx="8"/>'
    
    # Title
    svg += f'<text x="{width//2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#0e7490">{title}</text>'
    
    # Axes
    svg += f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#64748b" stroke-width="2"/>'
    svg += f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#64748b" stroke-width="2"/>'
    
    # Axis labels
    svg += f'<text x="{width//2}" y="{height-5}" text-anchor="middle" font-size="10" fill="#64748b">{x_label}</text>'
    svg += f'<text x="12" y="{height//2}" text-anchor="middle" font-size="10" fill="#64748b" transform="rotate(-90,12,{height//2})">{y_label}</text>'
    
    # Find data range
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    x_min, x_max = min(x_vals), max(x_vals)
    y_min, y_max = 0, max(y_vals) * 1.1
    
    def to_screen_x(x_val):
        return margin_left + (x_val - x_min) * graph_width / (x_max - x_min) if x_max > x_min else margin_left + graph_width/2
    
    def to_screen_y(y_val):
        return height - margin_bottom - (y_val - y_min) * graph_height / (y_max - y_min) if y_max > y_min else height - margin_bottom - graph_height/2
    
    # Grid lines
    for i in range(5):
        y = margin_top + i * graph_height / 4
        svg += f'<line x1="{margin_left}" y1="{y}" x2="{width-margin_right}" y2="{y}" stroke="#cffafe" stroke-width="1"/>'
    
    # Draw line
    if len(points) > 1:
        path = f'M{to_screen_x(points[0][0])},{to_screen_y(points[0][1])} '
        for px, py in points[1:]:
            path += f'L{to_screen_x(px)},{to_screen_y(py)} '
        svg += f'<path d="{path}" stroke="#0891b2" stroke-width="2.5" fill="none"/>'
    
    # Points
    for px, py in points:
        svg += f'<circle cx="{to_screen_x(px)}" cy="{to_screen_y(py)}" r="4" fill="#0891b2"/>'
    
    # Highlight point
    if highlight_x is not None:
        for px, py in points:
            if px == highlight_x:
                svg += f'<circle cx="{to_screen_x(px)}" cy="{to_screen_y(py)}" r="7" fill="#ef4444" stroke="white" stroke-width="2"/>'
                svg += f'<line x1="{to_screen_x(px)}" y1="{to_screen_y(py)}" x2="{to_screen_x(px)}" y2="{height-margin_bottom}" stroke="#ef4444" stroke-width="1" stroke-dasharray="4"/>'
                break
    
    svg += '</svg>'
    return svg


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_number(n):
    """Format number - remove .0 from whole numbers"""
    if isinstance(n, float) and n == int(n):
        return str(int(n))
    return str(n)


def generate_unique_options(correct_answer, num_options=4, option_type='integer', 
                           min_val=None, max_val=None, avoid=None):
    """Generate unique answer options including the correct answer"""
    if avoid is None:
        avoid = set()
    
    options = [correct_answer]
    avoid = set(avoid)
    avoid.add(correct_answer)
    
    attempts = 0
    max_attempts = 100
    
    while len(options) < num_options and attempts < max_attempts:
        attempts += 1
        
        if option_type == 'integer':
            if isinstance(correct_answer, int):
                strategies = [
                    correct_answer + random.randint(1, 5),
                    correct_answer - random.randint(1, 5),
                    correct_answer + random.randint(-10, 10),
                    correct_answer * 2 if correct_answer != 0 else random.randint(1, 10),
                    abs(correct_answer) + random.randint(1, 8),
                ]
                wrong = random.choice(strategies)
            else:
                wrong = correct_answer + random.randint(-5, 5)
        else:
            wrong = correct_answer + random.randint(-5, 5)
        
        # Apply bounds
        if min_val is not None and isinstance(wrong, (int, float)) and wrong < min_val:
            wrong = min_val + random.randint(0, 3)
        if max_val is not None and isinstance(wrong, (int, float)) and wrong > max_val:
            wrong = max_val - random.randint(0, 3)
        
        if wrong not in avoid and wrong != correct_answer:
            options.append(wrong)
            avoid.add(wrong)
    
    # Ensure we have enough options
    while len(options) < num_options:
        if isinstance(correct_answer, int):
            filler = correct_answer + len(options) * 2 + random.randint(1, 3)
        else:
            filler = random.randint(1, 20)
        if filler not in avoid:
            options.append(filler)
            avoid.add(filler)
    
    random.shuffle(options)
    correct_idx = options.index(correct_answer)
    
    return options, correct_idx


def format_linear_function(a, b, var='x'):
    """Format a linear function expression"""
    if a == 1:
        a_part = var
    elif a == -1:
        a_part = f"-{var}"
    else:
        a_part = f"{a}{var}"
    
    if b == 0:
        return a_part
    elif b > 0:
        return f"{a_part} + {b}"
    else:
        return f"{a_part} - {abs(b)}"


# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1(num_questions=50):
    """
    Level 1: Understanding Function Notation (Foundation)
    - What does f(x) mean?
    - Input → Output concept
    """
    questions = []
    used_questions = set()
    
    templates = [
        ("The function f takes a number and adds {b}.\nWhat is f({x})?", lambda x, b: x + b),
        ("The function g takes a number and subtracts {b}.\nWhat is g({x})?", lambda x, b: x - b),
        ("Function h adds {b} to any number.\nFind h({x}).", lambda x, b: x + b),
        ("If f means 'add {b}', what is f({x})?", lambda x, b: x + b),
        ("The function f takes {x} and adds {b}.\nWhat is the output?", lambda x, b: x + b),
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template, func = random.choice(templates)
        x = random.randint(1, 15)
        b = random.randint(1, 10)
        correct = func(x, b)
        
        question_text = template.format(x=x, b=b)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_function_machine_svg(x, f"+{b}", correct)
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        explanation = f"The function adds {b} to the input.\n"
        explanation += f"Input: {x}\n"
        explanation += f"Output: {x} + {b} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_2(num_questions=50):
    """
    Level 2: Evaluating Simple Functions (Foundation)
    - f(x) = x + 3, find f(2)
    - Simple addition/subtraction
    """
    questions = []
    used_questions = set()
    
    templates = [
        "If f(x) = x + {b}, find f({x}).",
        "Given f(x) = x + {b}, what is f({x})?",
        "The function f(x) = x + {b}.\nCalculate f({x}).",
        "f(x) = x + {b}\nFind the value of f({x}).",
        "For the function f(x) = x + {b}, evaluate f({x}).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        x = random.randint(1, 20)
        b = random.randint(1, 15)
        correct = x + b
        
        question_text = template.format(x=x, b=b)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_function_machine_svg(x, f"x + {b}", correct)
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        explanation = f"f(x) = x + {b}\n"
        explanation += f"f({x}) = {x} + {b}\n"
        explanation += f"f({x}) = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_3(num_questions=50):
    """
    Level 3: Evaluating with Multiplication (Foundation)
    - f(x) = 2x, find f(5)
    - f(x) = 3x + 1, find f(4)
    """
    questions = []
    used_questions = set()
    
    templates = [
        "If f(x) = {a}x, find f({x}).",
        "Given f(x) = {a}x, what is f({x})?",
        "The function f(x) = {a}x.\nCalculate f({x}).",
        "f(x) = {a}x\nFind the value of f({x}).",
        "For f(x) = {a}x, evaluate f({x}).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        a = random.randint(2, 8)
        x = random.randint(1, 12)
        correct = a * x
        
        question_text = template.format(a=a, x=x)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_function_machine_svg(x, f"{a}x", correct)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"f(x) = {a}x\n"
        explanation += f"f({x}) = {a} × {x}\n"
        explanation += f"f({x}) = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_4(num_questions=50):
    """
    Level 4: Linear Functions f(x) = ax + b (Ordinary)
    - SEC 2022 OL Q13(b) style: f(x) = 2x - 1, find f(3)
    """
    questions = []
    used_questions = set()
    
    templates = [
        "The function f is defined as f(x) = {expr}.\nFind f({x}).",
        "If f(x) = {expr}, what is the value of f({x})?",
        "Given f(x) = {expr}, calculate f({x}).",
        "f(x) = {expr}\nEvaluate f({x}).",
        "For the function f(x) = {expr}, find f({x}).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        a = random.randint(2, 6)
        b = random.randint(-8, 8)
        x = random.randint(1, 10)
        correct = a * x + b
        
        expr = format_linear_function(a, b)
        question_text = template.format(expr=expr, x=x)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_function_machine_svg(x, expr, correct)
        
        options, correct_idx = generate_unique_options(correct)
        
        explanation = f"f(x) = {expr}\n"
        explanation += f"f({x}) = {a}({x}) {'+' if b >= 0 else '-'} {abs(b)}\n"
        explanation += f"f({x}) = {a * x} {'+' if b >= 0 else '-'} {abs(b)}\n"
        explanation += f"f({x}) = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_5(num_questions=50):
    """
    Level 5: Finding Input from Output (Ordinary)
    - SEC 2022 OL Q13(b)(ii) style: f(x) = 9, find x
    """
    questions = []
    used_questions = set()
    
    templates = [
        "If f(x) = {expr} and f(x) = {output}, find the value of x.",
        "The function f(x) = {expr}.\nIf f(x) = {output}, what is x?",
        "Given f(x) = {expr}, find x when f(x) = {output}.",
        "f(x) = {expr}\nSolve for x if f(x) = {output}.",
        "For f(x) = {expr}, find x such that f(x) = {output}.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        a = random.randint(2, 6)
        b = random.randint(-5, 8)
        x = random.randint(1, 12)  # The answer we want
        output = a * x + b
        
        expr = format_linear_function(a, b)
        question_text = template.format(expr=expr, output=output)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        correct = x
        
        # Visual showing the reverse process
        svg = generate_input_output_svg(["?", "x"], [output, "→ solve"], "f")
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        explanation = f"f(x) = {expr}\n"
        explanation += f"We need f(x) = {output}\n"
        explanation += f"So: {a}x {'+' if b >= 0 else '-'} {abs(b)} = {output}\n"
        explanation += f"{a}x = {output - b}\n"
        explanation += f"x = {output - b} ÷ {a} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_6(num_questions=50):
    """
    Level 6: Completing Function Tables (Ordinary)
    - SEC 2024 HL Q8 style: complete table of values
    """
    questions = []
    used_questions = set()
    
    templates = [
        "Complete the table for f(x) = {expr}.\nWhat is the missing value?",
        "The table shows values for f(x) = {expr}.\nFind the missing output.",
        "f(x) = {expr}\nComplete the table to find the missing value.",
        "For the function f(x) = {expr}, find the missing value in the table.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        a = random.randint(2, 5)
        b = random.randint(-4, 6)
        
        x_values = list(range(1, 6))
        y_values = [a * x + b for x in x_values]
        
        missing_idx = random.randint(1, 4)
        correct = y_values[missing_idx]
        
        expr = format_linear_function(a, b)
        question_text = template.format(expr=expr)
        
        # Include the missing position in the question for uniqueness
        q_key = f"{question_text}_{missing_idx}_{a}_{b}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        # Generate table SVG with missing value
        display_y = y_values.copy()
        svg = generate_function_table_svg(expr, x_values, display_y, missing_idx)
        
        options, correct_idx = generate_unique_options(correct)
        
        x_val = x_values[missing_idx]
        explanation = f"f(x) = {expr}\n"
        explanation += f"We need f({x_val}).\n"
        explanation += f"f({x_val}) = {a}({x_val}) {'+' if b >= 0 else '-'} {abs(b)}\n"
        explanation += f"f({x_val}) = {a * x_val} {'+' if b >= 0 else '-'} {abs(b)} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_7(num_questions=50):
    """
    Level 7: Finding Constants (Higher)
    - SEC 2023 HL Q11(c) style: g(x) = 3x + k, g(2) = 11, find k
    """
    questions = []
    used_questions = set()
    
    templates = [
        "The function g(x) = {a}x + k.\nGiven that g({x}) = {output}, find the value of k.",
        "If g(x) = {a}x + k and g({x}) = {output}, what is k?",
        "g(x) = {a}x + k\nFind k if g({x}) = {output}.",
        "For the function g(x) = {a}x + k, given g({x}) = {output}, calculate k.",
        "The function is g(x) = {a}x + k.\nWhen x = {x}, g(x) = {output}. Find k.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        a = random.randint(2, 6)
        x = random.randint(2, 8)
        k = random.randint(-5, 10)  # The answer
        output = a * x + k
        
        question_text = template.format(a=a, x=x, output=output)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        correct = k
        
        svg = generate_function_machine_svg(x, f"{a}x + k", output, 'g')
        
        options, correct_idx = generate_unique_options(correct)
        
        explanation = f"g(x) = {a}x + k\n"
        explanation += f"g({x}) = {output}\n"
        explanation += f"So: {a}({x}) + k = {output}\n"
        explanation += f"{a * x} + k = {output}\n"
        explanation += f"k = {output} - {a * x} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_8(num_questions=50):
    """
    Level 8: Reading Function Graphs (Higher)
    - Find f(3) from graph
    - Find x when f(x) = 5
    """
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        q_type = random.choice(['find_y', 'find_x', 'find_y', 'find_x'])
        
        m = random.randint(1, 3)
        c = random.randint(-2, 4)
        
        if q_type == 'find_y':
            x = random.randint(1, 4)
            correct = m * x + c
            
            templates = [
                f"The graph shows f(x) = {format_linear_function(m, c)}.\nFrom the graph, what is f({x})?",
                f"Use the graph to find f({x}) when f(x) = {format_linear_function(m, c)}.",
                f"From the graph of f(x) = {format_linear_function(m, c)}, find f({x}).",
            ]
            question_text = random.choice(templates)
            highlight = (x, correct)
        else:
            y = random.randint(2, 8)
            # Make sure x comes out as integer
            if (y - c) % m != 0:
                y = m * 2 + c  # Guarantee clean division
            correct = (y - c) // m
            
            templates = [
                f"The graph shows f(x) = {format_linear_function(m, c)}.\nFrom the graph, find x when f(x) = {y}.",
                f"Use the graph to find x if f(x) = {y}, where f(x) = {format_linear_function(m, c)}.",
                f"From the graph of f(x) = {format_linear_function(m, c)}, find x when f(x) = {y}.",
            ]
            question_text = random.choice(templates)
            highlight = (correct, y)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_linear_graph_svg(m, c, highlight_point=highlight)
        
        options, correct_idx = generate_unique_options(correct, min_val=-2)
        
        if q_type == 'find_y':
            explanation = f"From the graph, when x = {x}:\n"
            explanation += f"f({x}) = {m}({x}) {'+' if c >= 0 else '-'} {abs(c)} = {correct}"
        else:
            explanation = f"From the graph, when f(x) = {y}:\n"
            explanation += f"{format_linear_function(m, c)} = {y}\n"
            explanation += f"x = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_9(num_questions=50):
    """
    Level 9: Quadratic Functions (Higher)
    - f(x) = x², find f(3)
    - f(x) = x² + 1, find f(4)
    """
    questions = []
    used_questions = set()
    
    templates = [
        "If f(x) = x² {op} {c}, find f({x}).",
        "Given f(x) = x² {op} {c}, what is f({x})?",
        "The function f(x) = x² {op} {c}.\nCalculate f({x}).",
        "f(x) = x² {op} {c}\nEvaluate f({x}).",
        "For f(x) = x² {op} {c}, find the value of f({x}).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        x = random.randint(-4, 5)
        c = random.randint(0, 8)
        
        if c == 0:
            correct = x * x
            op = "+"
            c_display = 0
            expr = "x²"
        else:
            sign = random.choice(['+', '-'])
            if sign == '+':
                correct = x * x + c
                op = "+"
            else:
                correct = x * x - c
                op = "-"
            c_display = c
            expr = f"x² {op} {c}"
        
        if c == 0:
            question_text = f"If f(x) = x², find f({x})."
        else:
            question_text = template.format(op=op, c=c_display, x=x)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_quadratic_graph_svg(1, 0, c if op == '+' else -c, highlight_point=(x, correct))
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        explanation = f"f(x) = {expr}\n"
        explanation += f"f({x}) = ({x})²"
        if c != 0:
            explanation += f" {op} {c}"
        explanation += f"\nf({x}) = {x*x}"
        if c != 0:
            explanation += f" {op} {c} = {correct}"
        else:
            explanation += f" = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_10(num_questions=50):
    """
    Level 10: Composite Functions (Higher)
    - f(g(x)) = ?
    - g(f(2)) = ?
    """
    questions = []
    used_questions = set()
    
    templates = [
        "f(x) = {f_expr} and g(x) = {g_expr}.\nFind f(g({x})).",
        "Given f(x) = {f_expr} and g(x) = {g_expr}, calculate f(g({x})).",
        "If f(x) = {f_expr} and g(x) = {g_expr}, what is g(f({x}))?",
        "For f(x) = {f_expr} and g(x) = {g_expr}, find g(f({x})).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Simple linear functions for composition
        f_a = random.randint(2, 4)
        f_b = random.randint(0, 5)
        g_a = random.randint(2, 3)
        g_b = random.randint(1, 4)
        
        x = random.randint(1, 5)
        
        # Decide f(g(x)) or g(f(x))
        if random.random() < 0.5:
            # f(g(x)): first apply g, then f
            g_x = g_a * x + g_b
            correct = f_a * g_x + f_b
            composition = "f(g"
            template = random.choice(templates[:2])
        else:
            # g(f(x)): first apply f, then g
            f_x = f_a * x + f_b
            correct = g_a * f_x + g_b
            composition = "g(f"
            template = random.choice(templates[2:])
        
        f_expr = format_linear_function(f_a, f_b)
        g_expr = format_linear_function(g_a, g_b)
        
        question_text = template.format(f_expr=f_expr, g_expr=g_expr, x=x)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        if "f(g" in question_text:
            intermediate = g_a * x + g_b
            svg = generate_composite_function_svg(f_expr, g_expr, x, intermediate, correct)
            explanation = f"f(x) = {f_expr}, g(x) = {g_expr}\n"
            explanation += f"Step 1: Find g({x}) = {g_a}({x}) + {g_b} = {intermediate}\n"
            explanation += f"Step 2: Find f({intermediate}) = {f_a}({intermediate}) + {f_b} = {correct}\n"
            explanation += f"So f(g({x})) = {correct}"
        else:
            intermediate = f_a * x + f_b
            svg = generate_composite_function_svg(g_expr, f_expr, x, intermediate, correct)
            explanation = f"f(x) = {f_expr}, g(x) = {g_expr}\n"
            explanation += f"Step 1: Find f({x}) = {f_a}({x}) + {f_b} = {intermediate}\n"
            explanation += f"Step 2: Find g({intermediate}) = {g_a}({intermediate}) + {g_b} = {correct}\n"
            explanation += f"So g(f({x})) = {correct}"
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_11(num_questions=50):
    """
    Level 11: Interpreting Real-World Graphs (Application)
    - SEC 2025 HL Q9 style: temperature, distance functions
    - Rate of change from graphs
    """
    questions = []
    used_questions = set()
    
    contexts = [
        ("Temperature", "Time (hours)", "Temp (°C)", lambda t: 15 + 2*t),
        ("Distance", "Time (hours)", "Distance (km)", lambda t: 10*t),
        ("Water Level", "Time (minutes)", "Level (cm)", lambda t: 50 - 5*t),
        ("Cost", "Items", "Cost (€)", lambda n: 5 + 3*n),
        ("Height", "Time (seconds)", "Height (m)", lambda t: 20 + 4*t),
    ]
    
    templates = [
        "The graph shows {context} over time.\nWhat is the {y_label} when {x_label} = {x}?",
        "From the {context} graph, find the value when {x_label} is {x}.",
        "The function shows {context}.\nAt {x_label} = {x}, what is the {y_label}?",
        "Using the graph of {context}, find the value at {x_label} = {x}.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        context_name, x_label, y_label, func = random.choice(contexts)
        template = random.choice(templates)
        
        # Generate points for graph
        x_vals = list(range(0, 6))
        points = [(x, func(x)) for x in x_vals]
        
        # Pick a point to ask about
        ask_x = random.randint(1, 4)
        correct = func(ask_x)
        
        question_text = template.format(
            context=context_name, 
            x_label=x_label.split()[0].lower(), 
            y_label=y_label.split()[0].lower(),
            x=ask_x
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_real_world_graph_svg(context_name, x_label, y_label, points, highlight_x=ask_x)
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        explanation = f"From the graph, when {x_label.split()[0].lower()} = {ask_x}:\n"
        explanation += f"The {y_label.split()[0].lower()} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_12(num_questions=50):
    """
    Level 12: Problem Solving & Applications (Mastery)
    - Real-world function problems
    - SEC 2025 HL Q9 style
    """
    questions = []
    used_questions = set()
    
    problem_types = [
        {
            'context': 'taxi fare',
            'setup': 'A taxi charges €{base} plus €{rate} per km.',
            'func': 'C(d) = {base} + {rate}d',
            'templates': [
                "What is the cost for a {d} km journey?",
                "Calculate the fare for travelling {d} km.",
                "How much would a {d} km trip cost?",
            ]
        },
        {
            'context': 'mobile phone',
            'setup': 'A phone plan costs €{base} per month plus €{rate} per GB of data.',
            'func': 'C(g) = {base} + {rate}g',
            'templates': [
                "What is the monthly cost if {d} GB is used?",
                "Calculate the bill for {d} GB of data.",
                "How much for a month using {d} GB?",
            ]
        },
        {
            'context': 'temperature conversion',
            'setup': 'To convert Celsius to Fahrenheit: F(C) = 1.8C + 32.',
            'func': 'F(C) = 1.8C + 32',
            'templates': [
                "Convert {d}°C to Fahrenheit.",
                "What is {d}°C in Fahrenheit?",
                "Find the Fahrenheit equivalent of {d}°C.",
            ]
        },
        {
            'context': 'savings account',
            'setup': 'Emma has €{base} in savings and adds €{rate} each week.',
            'func': 'S(w) = {base} + {rate}w',
            'templates': [
                "How much will she have after {d} weeks?",
                "Calculate her savings after {d} weeks.",
                "What is her balance after {d} weeks?",
            ]
        },
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        problem = random.choice(problem_types)
        
        if problem['context'] == 'temperature conversion':
            d = random.randint(10, 35)
            correct = int(1.8 * d + 32)
            base = 0
            rate = 1.8
            setup = problem['setup']
        else:
            base = random.randint(5, 20)
            rate = random.randint(2, 8)
            d = random.randint(3, 12)
            correct = base + rate * d
            setup = problem['setup'].format(base=base, rate=rate)
        
        template = random.choice(problem['templates'])
        question_part = template.format(d=d)
        
        question_text = f"{setup}\n{question_part}"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Generate appropriate visual
        if problem['context'] == 'temperature conversion':
            svg = generate_function_machine_svg(d, "1.8C + 32", correct, 'F')
        else:
            svg = generate_function_machine_svg(d, f"{base} + {rate}x", correct, 'C')
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        if problem['context'] == 'temperature conversion':
            explanation = f"F(C) = 1.8C + 32\n"
            explanation += f"F({d}) = 1.8({d}) + 32\n"
            explanation += f"F({d}) = {1.8 * d} + 32 = {correct}°F"
        else:
            func_expr = problem['func'].format(base=base, rate=rate)
            explanation = f"Using {func_expr}:\n"
            explanation += f"When d = {d}:\n"
            explanation += f"= {base} + {rate}({d})\n"
            explanation += f"= {base} + {rate * d} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


# ============================================================
# VALIDATION
# ============================================================

def validate_questions(questions, level):
    """Validate generated questions for quality"""
    errors = []
    warnings = []
    
    for i, q in enumerate(questions):
        # Check unique options
        opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(opts)) != 4:
            errors.append(f"Level {level} Q{i+1}: Duplicate options found: {opts}")
        
        # Check correct_idx is valid
        if q['correct_idx'] not in [0, 1, 2, 3]:
            errors.append(f"Level {level} Q{i+1}: Invalid correct_idx: {q['correct_idx']}")
        
        # Check explanation exists
        if not q.get('explanation') or len(q['explanation']) < 20:
            warnings.append(f"Level {level} Q{i+1}: Short or missing explanation")
        
        # Check question text exists
        if not q.get('question_text') or len(q['question_text']) < 10:
            errors.append(f"Level {level} Q{i+1}: Missing or short question text")
    
    return errors, warnings


def print_validation_summary(all_questions):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    total_errors = 0
    total_warnings = 0
    
    for level in range(1, 13):
        questions = all_questions.get(level, [])
        errors, warnings = validate_questions(questions, level)
        
        total_errors += len(errors)
        total_warnings += len(warnings)
        
        # Visual count
        visual_count = sum(1 for q in questions if q.get('image_svg'))
        visual_pct = (visual_count / len(questions) * 100) if questions else 0
        
        # Progress bar
        bar_len = 20
        filled = int(bar_len * len(questions) / 50)
        bar = "█" * filled + "░" * (bar_len - filled)
        
        status = "✓" if len(errors) == 0 else "✗"
        print(f"Level {level:2d}: [{bar}] {len(questions):2d}/50 | Visual: {visual_pct:5.1f}% | {status}")
        
        for err in errors:
            print(f"         ❌ {err}")
    
    print("=" * 60)
    print(f"Total Errors: {total_errors} | Total Warnings: {total_warnings}")
    print("=" * 60)
    
    return total_errors == 0


# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions_to_db(all_questions, db_path='instance/mathquiz.db'):
    """Insert questions into the database"""
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Count existing functions questions
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE topic = 'functions'")
    existing = cursor.fetchone()[0]
    print(f"Existing functions questions: {existing}")
    
    # Delete existing functions questions (ONLY from questions_adaptive!)
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = 'functions'")
    print(f"Deleted {existing} existing functions questions from questions_adaptive")
    
    inserted = 0
    errors = 0
    
    for level in range(1, 13):
        questions = all_questions.get(level, [])
        
        # Determine difficulty band
        if level <= 3:
            band = 'Foundation'
        elif level <= 6:
            band = 'Ordinary'
        elif level <= 9:
            band = 'Higher'
        elif level <= 11:
            band = 'Application'
        else:
            band = 'Mastery'
        
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
                    q['option_a'],
                    q['option_b'],
                    q['option_c'],
                    q['option_d'],
                    q['correct_idx'],
                    'functions',
                    level,
                    band,
                    'jc_exam',
                    q['explanation'],
                    q.get('image_svg'),
                    1
                ))
                inserted += 1
            except Exception as e:
                errors += 1
                print(f"Error inserting Level {level} question: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ Inserted {inserted} questions")
    if errors > 0:
        print(f"❌ {errors} errors occurred")
    
    return errors == 0


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("AgentMath - Functions Topic Generator v1")
    print("Generating 600 SEC-aligned questions (50 per level)")
    print("=" * 60)
    
    all_questions = {}
    
    # Generate questions for each level
    generators = {
        1: generate_level_1,
        2: generate_level_2,
        3: generate_level_3,
        4: generate_level_4,
        5: generate_level_5,
        6: generate_level_6,
        7: generate_level_7,
        8: generate_level_8,
        9: generate_level_9,
        10: generate_level_10,
        11: generate_level_11,
        12: generate_level_12,
    }
    
    for level, generator in generators.items():
        print(f"Generating Level {level}...")
        all_questions[level] = generator(50)
    
    # Validate
    is_valid = print_validation_summary(all_questions)
    
    if not is_valid:
        print("\n⚠️ Validation failed. Fix errors before inserting to database.")
        return
    
    # Ask about database insertion
    print("\n" + "=" * 60)
    response = input("Insert questions into database? (y/n): ").strip().lower()
    
    if response == 'y':
        success = insert_questions_to_db(all_questions)
        if success:
            print("\n🎉 Functions topic generation complete!")
        else:
            print("\n⚠️ Some errors occurred during insertion.")
    else:
        print("Skipped database insertion.")
        
        # Save to JSON for review
        import json
        output_data = {
            level: [
                {k: v for k, v in q.items() if k != 'image_svg'}
                for q in questions
            ]
            for level, questions in all_questions.items()
        }
        
        with open('functions_questions_preview.json', 'w') as f:
            json.dump(output_data, f, indent=2)
        print("Saved preview to functions_questions_preview.json")


if __name__ == '__main__':
    main()
