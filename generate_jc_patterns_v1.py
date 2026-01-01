#!/usr/bin/env python3
"""
AgentMath - Patterns Topic Generator v1
SEC Junior Cycle Mathematics - Adaptive Quiz System

Generates 600 questions (50 per level × 12 levels) for the Patterns topic.
Aligned with SEC Junior Cycle Mathematics Specification.

Level Structure:
  Level 1:  Reading Visual Patterns (Foundation)
  Level 2:  Extending Visual Patterns (Foundation)
  Level 3:  Finding Differences (Foundation)
  Level 4:  Linear Sequences - Counting On (Ordinary)
  Level 5:  Common Difference (Ordinary)
  Level 6:  Sequence Tables (Ordinary)
  Level 7:  Linear vs Non-Linear (Ordinary)
  Level 8:  Using nth Term Formula (Higher)
  Level 9:  Finding nth Term Formula (Higher)
  Level 10: Quadratic Sequences (Higher)
  Level 11: Geometric Sequences (Higher)
  Level 12: Problem Solving & Applications (Mastery)

SEC Reference Questions:
  - 2022 OL Q12(d): Draw Pattern 4, complete table, linear/non-linear
  - 2022 HL Q4(c): Sequence 11,8,5,2 - find 5th term, write Tₙ formula
  - 2024 HL Q12: Find nth term, is 100 a term in sequence?
  - 2025 OL Q8(c): Pattern of squares - draw, table, linear/non-linear
  - 2025 HL Q2(a): Next two terms - linear, tripling, quadratic

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

def generate_dot_pattern_svg(pattern_number, dots_per_pattern_func):
    """Generate SVG showing a dot pattern"""
    dots = dots_per_pattern_func(pattern_number)
    
    # Arrange dots in a nice pattern
    cols = min(dots, 10)
    rows = (dots + cols - 1) // cols
    
    width = max(120, cols * 25 + 20)
    height = rows * 25 + 40
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="8"/>'
    
    # Title
    svg += f'<text x="{width//2}" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">Pattern {pattern_number}</text>'
    
    # Draw dots
    dot_count = 0
    for row in range(rows):
        for col in range(cols):
            if dot_count < dots:
                cx = 20 + col * 22
                cy = 35 + row * 22
                svg += f'<circle cx="{cx}" cy="{cy}" r="8" fill="#3b82f6" stroke="#1e40af" stroke-width="1"/>'
                dot_count += 1
    
    svg += '</svg>'
    return svg


def generate_square_pattern_svg(pattern_number, squares_per_pattern_func):
    """Generate SVG showing a pattern made of squares"""
    squares = squares_per_pattern_func(pattern_number)
    
    # Arrange squares in an L-shape or staircase pattern
    size = 20
    cols = min(squares, 8)
    rows = (squares + cols - 1) // cols
    
    width = max(140, cols * (size + 4) + 30)
    height = rows * (size + 4) + 50
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f0fdf4" rx="8"/>'
    
    # Title
    svg += f'<text x="{width//2}" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">Pattern {pattern_number}</text>'
    
    # Draw squares
    square_count = 0
    for row in range(rows):
        for col in range(cols):
            if square_count < squares:
                x = 15 + col * (size + 4)
                y = 30 + row * (size + 4)
                svg += f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="#22c55e" stroke="#166534" stroke-width="2" rx="2"/>'
                square_count += 1
    
    svg += '</svg>'
    return svg


def generate_triangle_pattern_svg(pattern_number, triangles_per_pattern_func):
    """Generate SVG showing a pattern made of triangles"""
    triangles = triangles_per_pattern_func(pattern_number)
    
    size = 24
    cols = min(triangles, 8)
    rows = (triangles + cols - 1) // cols
    
    width = max(140, cols * (size + 4) + 30)
    height = rows * (size + 8) + 50
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#fef3c7" rx="8"/>'
    
    # Title
    svg += f'<text x="{width//2}" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">Pattern {pattern_number}</text>'
    
    # Draw triangles
    tri_count = 0
    for row in range(rows):
        for col in range(cols):
            if tri_count < triangles:
                x = 15 + col * (size + 4)
                y = 32 + row * (size + 6)
                # Triangle points
                points = f"{x},{y+size} {x+size//2},{y} {x+size},{y+size}"
                svg += f'<polygon points="{points}" fill="#f59e0b" stroke="#92400e" stroke-width="2"/>'
                tri_count += 1
    
    svg += '</svg>'
    return svg


def generate_matchstick_pattern_svg(pattern_number, shape_type='square'):
    """Generate SVG showing matchstick patterns (squares or triangles)"""
    if shape_type == 'square':
        # Each square shares sides with previous
        # Pattern 1: 4 matches, Pattern 2: 7 matches, Pattern 3: 10 matches
        matches = 4 + (pattern_number - 1) * 3
        width = pattern_number * 40 + 40
    else:  # triangle
        # Pattern 1: 3 matches, Pattern 2: 5 matches, Pattern 3: 7 matches
        matches = 3 + (pattern_number - 1) * 2
        width = pattern_number * 35 + 40
    
    height = 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#faf5ff" rx="8"/>'
    
    # Title
    svg += f'<text x="{width//2}" y="15" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">Pattern {pattern_number}</text>'
    
    if shape_type == 'square':
        # Draw connected squares
        for i in range(pattern_number):
            x = 20 + i * 35
            y = 25
            size = 35
            # Draw square (skip left side if not first)
            if i == 0:
                svg += f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+size}" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round"/>'
            svg += f'<line x1="{x}" y1="{y}" x2="{x+size}" y2="{y}" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round"/>'
            svg += f'<line x1="{x+size}" y1="{y}" x2="{x+size}" y2="{y+size}" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round"/>'
            svg += f'<line x1="{x}" y1="{y+size}" x2="{x+size}" y2="{y+size}" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round"/>'
    else:
        # Draw connected triangles
        for i in range(pattern_number):
            x = 20 + i * 30
            y = 60
            size = 30
            # Draw triangle (skip left side if not first)
            if i == 0:
                svg += f'<line x1="{x}" y1="{y}" x2="{x+size//2}" y2="{y-size}" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round"/>'
            svg += f'<line x1="{x+size//2}" y1="{y-size}" x2="{x+size}" y2="{y}" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round"/>'
            svg += f'<line x1="{x}" y1="{y}" x2="{x+size}" y2="{y}" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round"/>'
    
    svg += '</svg>'
    return svg, matches


def generate_staircase_pattern_svg(pattern_number):
    """Generate SVG showing a staircase pattern"""
    # Each pattern adds one more step
    # Pattern 1: 1 square, Pattern 2: 1+2=3, Pattern 3: 1+2+3=6
    total_squares = sum(range(1, pattern_number + 1))
    
    size = 18
    width = pattern_number * (size + 2) + 40
    height = pattern_number * (size + 2) + 50
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ecfeff" rx="8"/>'
    
    # Title
    svg += f'<text x="{width//2}" y="15" text-anchor="middle" font-size="11" font-weight="bold" fill="#0e7490">Pattern {pattern_number}</text>'
    
    # Draw staircase (bottom-left to top-right)
    for col in range(pattern_number):
        for row in range(col + 1):
            x = 20 + col * (size + 2)
            y = height - 25 - row * (size + 2)
            svg += f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="#06b6d4" stroke="#0e7490" stroke-width="1" rx="2"/>'
    
    svg += '</svg>'
    return svg, total_squares


def generate_sequence_visual_svg(terms, highlight_position=None):
    """Generate SVG showing a sequence of numbers"""
    n = len(terms)
    width = n * 55 + 40
    height = 70
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f1f5f9" rx="8"/>'
    
    for i, term in enumerate(terms):
        x = 30 + i * 55
        y = 35
        
        # Box color
        if highlight_position is not None and i == highlight_position:
            fill = "#fef08a"
            stroke = "#ca8a04"
        else:
            fill = "#ffffff"
            stroke = "#64748b"
        
        svg += f'<rect x="{x-20}" y="{y-18}" width="40" height="36" fill="{fill}" stroke="{stroke}" stroke-width="2" rx="4"/>'
        svg += f'<text x="{x}" y="{y+7}" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e293b">{term}</text>'
        
        # Position label
        svg += f'<text x="{x}" y="{y+32}" text-anchor="middle" font-size="10" fill="#64748b">T{i+1}</text>'
    
    svg += '</svg>'
    return svg


def generate_difference_visual_svg(terms):
    """Generate SVG showing a sequence with differences marked"""
    n = len(terms)
    width = n * 60 + 40
    height = 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f0fdf4" rx="8"/>'
    
    # Draw terms
    for i, term in enumerate(terms):
        x = 40 + i * 60
        y = 30
        svg += f'<rect x="{x-22}" y="{y-18}" width="44" height="36" fill="#ffffff" stroke="#22c55e" stroke-width="2" rx="4"/>'
        svg += f'<text x="{x}" y="{y+7}" text-anchor="middle" font-size="16" font-weight="bold" fill="#166534">{term}</text>'
    
    # Draw differences
    for i in range(len(terms) - 1):
        diff = terms[i+1] - terms[i]
        x1 = 40 + i * 60
        x2 = 40 + (i+1) * 60
        y = 55
        
        # Arrow
        svg += f'<path d="M{x1+15},{y} L{x2-15},{y}" stroke="#f97316" stroke-width="2" fill="none" marker-end="url(#arrow)"/>'
        
        # Difference value
        mid_x = (x1 + x2) / 2
        sign = "+" if diff >= 0 else ""
        svg += f'<text x="{mid_x}" y="{y+20}" text-anchor="middle" font-size="12" font-weight="bold" fill="#ea580c">{sign}{diff}</text>'
    
    # Arrow marker definition
    svg += '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">'
    svg += '<path d="M0,0 L0,6 L9,3 z" fill="#f97316"/></marker></defs>'
    
    svg += '</svg>'
    return svg


def generate_nth_term_table_svg(terms, show_formula=False, formula=""):
    """Generate SVG showing a sequence table (position, term)"""
    n = len(terms)
    cell_width = 50
    width = (n + 1) * cell_width + 40
    height = 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#fefce8" rx="8"/>'
    
    # Header row
    svg += f'<rect x="20" y="15" width="{cell_width}" height="30" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>'
    svg += f'<text x="{20 + cell_width//2}" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="#713f12">n</text>'
    
    for i in range(n):
        x = 20 + (i + 1) * cell_width
        svg += f'<rect x="{x}" y="15" width="{cell_width}" height="30" fill="#fef9c3" stroke="#ca8a04" stroke-width="1"/>'
        svg += f'<text x="{x + cell_width//2}" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="#713f12">{i+1}</text>'
    
    # Term row
    svg += f'<rect x="20" y="45" width="{cell_width}" height="30" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>'
    svg += f'<text x="{20 + cell_width//2}" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#713f12">Tₙ</text>'
    
    for i, term in enumerate(terms):
        x = 20 + (i + 1) * cell_width
        svg += f'<rect x="{x}" y="45" width="{cell_width}" height="30" fill="#ffffff" stroke="#ca8a04" stroke-width="1"/>'
        display = term if term != "?" else "?"
        svg += f'<text x="{x + cell_width//2}" y="65" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e293b">{display}</text>'
    
    if show_formula and formula:
        svg += f'<text x="{width//2}" y="90" text-anchor="middle" font-size="11" fill="#854d0e">Formula: Tₙ = {formula}</text>'
    
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
            # Generate plausible wrong answers near the correct answer
            if isinstance(correct_answer, int):
                strategies = [
                    correct_answer + random.randint(1, 5),
                    correct_answer - random.randint(1, 5),
                    correct_answer + random.randint(-10, 10),
                    correct_answer * 2,
                    correct_answer + correct_answer // 2 if correct_answer > 0 else correct_answer - 1,
                ]
                wrong = random.choice(strategies)
            else:
                wrong = correct_answer + random.randint(-5, 5)
        
        elif option_type == 'formula':
            # Wrong formula variations
            if 'n' in str(correct_answer):
                parts = str(correct_answer).replace(' ', '')
                variations = [
                    parts.replace('+', '-') if '+' in parts else parts.replace('-', '+'),
                    f"{random.randint(1,5)}n + {random.randint(0,10)}",
                    f"{random.randint(1,5)}n - {random.randint(1,10)}",
                    f"n + {random.randint(1,10)}",
                    f"{random.randint(2,6)}n",
                ]
                wrong = random.choice(variations)
            else:
                wrong = f"{random.randint(1,5)}n + {random.randint(0,10)}"
        
        elif option_type == 'sequence':
            # Wrong sequence by changing one term
            if isinstance(correct_answer, (list, tuple)):
                wrong = list(correct_answer)
                idx = random.randint(0, len(wrong) - 1)
                wrong[idx] += random.choice([-2, -1, 1, 2])
                wrong = tuple(wrong)
            else:
                wrong = correct_answer
        
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


def get_ordinal(n):
    """Get ordinal string for a number (1st, 2nd, 3rd, etc.)"""
    if 11 <= n % 100 <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"


# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1(num_questions=50):
    """
    Level 1: Reading Visual Patterns (Foundation)
    - Count shapes in a given pattern
    - Identify how many shapes in Pattern N
    """
    questions = []
    used_questions = set()
    
    shape_types = [
        ('dots', 'dot', lambda n: n + 2, generate_dot_pattern_svg),  # 3, 4, 5, 6...
        ('dots', 'dot', lambda n: 2 * n, generate_dot_pattern_svg),  # 2, 4, 6, 8...
        ('dots', 'dot', lambda n: n + 4, generate_dot_pattern_svg),  # 5, 6, 7, 8...
        ('dots', 'dot', lambda n: 3 * n, generate_dot_pattern_svg),  # 3, 6, 9, 12...
        ('squares', 'square', lambda n: n + 1, generate_square_pattern_svg),  # 2, 3, 4, 5...
        ('squares', 'square', lambda n: 2 * n + 1, generate_square_pattern_svg),  # 3, 5, 7, 9...
        ('squares', 'square', lambda n: n + 3, generate_square_pattern_svg),  # 4, 5, 6, 7...
        ('squares', 'square', lambda n: 2 * n, generate_square_pattern_svg),  # 2, 4, 6, 8...
        ('triangles', 'triangle', lambda n: n, generate_triangle_pattern_svg),  # 1, 2, 3, 4...
        ('triangles', 'triangle', lambda n: n + 3, generate_triangle_pattern_svg),  # 4, 5, 6, 7...
        ('triangles', 'triangle', lambda n: n + 5, generate_triangle_pattern_svg),  # 6, 7, 8, 9...
        ('triangles', 'triangle', lambda n: 2 * n + 2, generate_triangle_pattern_svg),  # 4, 6, 8, 10...
    ]
    
    # Question templates for variety
    templates = [
        "Look at the pattern below. How many {shape} are in Pattern {n}?",
        "Count the {shape} in the pattern shown. How many are in Pattern {n}?",
        "The pattern below shows {shape}. How many {shape} are in Pattern {n}?",
        "How many {shape} can you count in Pattern {n}?",
        "In the pattern shown, count the {shape} in Pattern {n}.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        shape_idx = random.randint(0, len(shape_types) - 1)
        shape_plural, shape_singular, count_func, svg_func = shape_types[shape_idx]
        pattern_num = random.randint(1, 8)
        template = random.choice(templates)
        correct = count_func(pattern_num)
        
        question_text = template.format(shape=shape_plural, n=pattern_num)
        
        # Check for uniqueness
        if question_text in used_questions:
            continue
        
        used_questions.add(question_text)
        
        # Generate SVG
        svg = svg_func(pattern_num, count_func)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Count the {shape_plural} in Pattern {pattern_num}.\n"
        explanation += f"There are {correct} {shape_plural if correct > 1 else shape_singular}."
        
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
    Level 2: Extending Visual Patterns (Foundation)
    - Given patterns 1, 2, 3, how many in pattern 4?
    - SEC 2022 OL Q12(d) style
    """
    questions = []
    used_questions = set()
    
    patterns = [
        # (name, formula, description)
        ('dots', lambda n: n + 1, 'adds 1 each time'),
        ('dots', lambda n: n + 2, 'adds 1 each time'),
        ('dots', lambda n: n + 3, 'starts at 4'),
        ('dots', lambda n: 2 * n, 'doubles each pattern number'),
        ('dots', lambda n: 2 * n + 1, 'odd numbers'),
        ('dots', lambda n: 2 * n + 3, 'odd numbers starting at 5'),
        ('squares', lambda n: n, 'same as pattern number'),
        ('squares', lambda n: n + 2, 'adds 1 each time'),
        ('squares', lambda n: n + 4, 'starts at 5'),
        ('squares', lambda n: 3 * n, 'triples each pattern number'),
        ('squares', lambda n: 3 * n + 1, 'starts at 4'),
        ('triangles', lambda n: n + 1, 'adds 1 each time'),
        ('triangles', lambda n: 2 * n - 1, 'odd numbers'),
        ('triangles', lambda n: 2 * n, 'even numbers'),
        ('triangles', lambda n: n + 5, 'starts at 6'),
    ]
    
    templates = [
        "A pattern of {shape} follows this sequence:\nPattern 1: {t1}, Pattern 2: {t2}, Pattern 3: {t3}\nHow many {shape} are in Pattern {ask}?",
        "Study the pattern: Pattern 1 has {t1} {shape}, Pattern 2 has {t2}, Pattern 3 has {t3}.\nHow many {shape} will Pattern {ask} have?",
        "The number of {shape} in each pattern is: {t1}, {t2}, {t3}, ...\nWhat comes next in Pattern {ask}?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        shape, formula, desc = random.choice(patterns)
        template = random.choice(templates)
        
        # Show first 3 patterns, ask about pattern 4 or 5
        shown = [formula(1), formula(2), formula(3)]
        ask_pattern = random.choice([4, 5, 6])
        correct = formula(ask_pattern)
        
        question_text = template.format(
            shape=shape, t1=shown[0], t2=shown[1], t3=shown[2], ask=ask_pattern
        )
        
        # Check for uniqueness
        if question_text in used_questions:
            continue
        
        used_questions.add(question_text)
        
        # Create visual showing the pattern
        svg = generate_sequence_visual_svg(shown + ["?"], highlight_position=3)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        diff = shown[1] - shown[0]
        explanation = f"Find the pattern: {shown[0]}, {shown[1]}, {shown[2]}\n"
        explanation += f"The difference is {'+' if diff >= 0 else ''}{diff} each time.\n"
        if ask_pattern == 4:
            explanation += f"Pattern 4 = {shown[2]} {'+' if diff >= 0 else ''} {abs(diff)} = {correct}"
        elif ask_pattern == 5:
            pattern_4 = formula(4)
            explanation += f"Pattern 4 = {shown[2]} {'+' if diff >= 0 else ''} {abs(diff)} = {pattern_4}\n"
            explanation += f"Pattern 5 = {pattern_4} {'+' if diff >= 0 else ''} {abs(diff)} = {correct}"
        else:
            pattern_4 = formula(4)
            pattern_5 = formula(5)
            explanation += f"Pattern 4 = {pattern_4}, Pattern 5 = {pattern_5}\n"
            explanation += f"Pattern 6 = {pattern_5} {'+' if diff >= 0 else ''} {abs(diff)} = {correct}"
        
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
    Level 3: Finding Differences (Foundation)
    - What is the common difference?
    - What is added each time?
    """
    questions = []
    used_questions = set()
    
    templates_positive = [
        "Look at this sequence: {seq}, ...\nWhat number is added each time?",
        "Find the common difference in: {seq}, ...",
        "What is added to get from one term to the next?\n{seq}, ...",
        "The sequence {seq} has a common difference. What is it?",
    ]
    
    templates_any = [
        "Look at this sequence: {seq}, ...\nWhat is the common difference?",
        "Find the common difference: {seq}, ...",
        "What is the difference between consecutive terms?\n{seq}",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Generate a linear sequence
        start = random.randint(1, 30)
        diff = random.randint(1, 10) * random.choice([1, -1])
        
        # Ensure no negative terms for foundation level
        if diff < 0 and start + 4 * diff < 0:
            diff = abs(diff)
        
        terms = [start + j * diff for j in range(5)]
        
        # Make sure all positive
        if min(terms) < 0:
            terms = [t - min(terms) + 1 for t in terms]
            diff = terms[1] - terms[0]
        
        correct = diff
        seq_str = ', '.join(map(str, terms[:4]))
        
        if diff > 0:
            template = random.choice(templates_positive)
        else:
            template = random.choice(templates_any)
        
        question_text = template.format(seq=seq_str)
        
        if question_text in used_questions:
            continue
        
        used_questions.add(question_text)
        
        # Visual
        svg = generate_difference_visual_svg(terms[:4])
        
        options, correct_idx = generate_unique_options(correct)
        
        explanation = f"Sequence: {', '.join(map(str, terms[:4]))}\n"
        explanation += f"Difference: {terms[1]} - {terms[0]} = {diff}\n"
        explanation += f"Check: {terms[2]} - {terms[1]} = {diff} ✓\n"
        explanation += f"The common difference is {diff}."
        
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
    Level 4: Linear Sequences - Counting On (Ordinary)
    - Find the next term(s)
    - SEC 2022 HL Q4(c) style
    """
    questions = []
    
    for i in range(num_questions):
        start = random.randint(1, 30)
        diff = random.randint(2, 10) * random.choice([1, -1])
        
        # Ensure sequence stays reasonable
        if diff < 0 and start + 5 * diff < 0:
            diff = abs(diff)
        
        terms = [start + j * diff for j in range(6)]
        
        # Ensure all positive
        if min(terms) < 0:
            terms = [t - min(terms) + 1 for t in terms]
        
        show_count = random.randint(3, 4)
        shown = terms[:show_count]
        
        # Ask for next term or next two terms
        if random.random() < 0.6:
            # Next term
            correct = terms[show_count]
            question_text = f"What is the next term in this sequence?\n{', '.join(map(str, shown))}, ..."
        else:
            # Next two terms as tuple
            next_two = (terms[show_count], terms[show_count + 1])
            correct = next_two[0] + next_two[1]  # Sum for comparison
            question_text = f"What are the next TWO terms in this sequence?\n{', '.join(map(str, shown))}, __, __"
            # For this type, we'll ask about the 5th term specifically
            correct = terms[show_count]
            question_text = f"What is the {get_ordinal(show_count + 1)} term in this sequence?\n{', '.join(map(str, shown))}, ..."
        
        svg = generate_sequence_visual_svg(shown)
        
        options, correct_idx = generate_unique_options(correct)
        
        diff_val = terms[1] - terms[0]
        explanation = f"Sequence: {', '.join(map(str, shown))}\n"
        explanation += f"Common difference: {'+' if diff_val >= 0 else ''}{diff_val}\n"
        explanation += f"Next term = {shown[-1]} {'+' if diff_val >= 0 else ''} {abs(diff_val)} = {correct}"
        
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
    Level 5: Common Difference (Ordinary)
    - Identify and use the common difference
    - Find a specific term using counting
    """
    questions = []
    
    for i in range(num_questions):
        start = random.randint(1, 20)
        diff = random.randint(2, 8)
        
        terms = [start + j * diff for j in range(10)]
        
        # Different question types
        q_type = random.choice(['find_term', 'common_diff', 'which_term'])
        
        if q_type == 'find_term':
            # Find the nth term
            n = random.randint(5, 8)
            correct = terms[n - 1]
            shown = terms[:4]
            question_text = f"In the sequence {', '.join(map(str, shown))}, ...\nWhat is the {get_ordinal(n)} term?"
            svg = generate_sequence_visual_svg(shown)
            
            explanation = f"Common difference = {terms[1]} - {terms[0]} = {diff}\n"
            explanation += f"T1 = {terms[0]}\n"
            for j in range(1, n):
                explanation += f"T{j+1} = T{j} + {diff} = {terms[j]}\n"
            explanation += f"The {get_ordinal(n)} term is {correct}."
        
        elif q_type == 'common_diff':
            # What's the common difference
            correct = diff
            shown = terms[:5]
            question_text = f"What is the common difference in this arithmetic sequence?\n{', '.join(map(str, shown))}, ..."
            svg = generate_difference_visual_svg(shown[:4])
            
            explanation = f"Common difference = second term - first term\n"
            explanation += f"= {terms[1]} - {terms[0]} = {diff}\n"
            explanation += f"Check: {terms[2]} - {terms[1]} = {diff} ✓"
        
        else:  # which_term
            # Which term is X?
            n = random.randint(5, 9)
            target = terms[n - 1]
            correct = n
            shown = terms[:4]
            question_text = f"In the sequence {', '.join(map(str, shown))}, ...\nWhich term is {target}?"
            svg = generate_sequence_visual_svg(shown)
            
            explanation = f"Common difference = {diff}\n"
            explanation += f"Count up: "
            for j in range(n):
                explanation += f"T{j+1}={terms[j]}, "
            explanation += f"\n{target} is the {get_ordinal(n)} term."
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg if 'svg' in dir() else None
        })
    
    return questions


def generate_level_6(num_questions=50):
    """
    Level 6: Sequence Tables (Ordinary)
    - Complete tables for sequences
    - SEC 2022 OL Q12(d) style - complete table
    """
    questions = []
    used_questions = set()
    
    templates = [
        "Complete the table for this sequence.\nWhat is the missing value?",
        "The table shows a sequence. Find the missing term.",
        "What value completes this sequence table?",
        "Find the missing number in the sequence table below.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        start = random.randint(2, 20)
        diff = random.randint(2, 8)
        
        terms = [start + j * diff for j in range(6)]
        
        # Create table with one missing value
        missing_pos = random.randint(2, 5)
        table_terms = terms[:6]
        display_terms = [t if j != missing_pos else "?" for j, t in enumerate(table_terms)]
        
        correct = terms[missing_pos]
        
        # Create unique identifier
        seq_id = f"{start}_{diff}_{missing_pos}"
        template = random.choice(templates)
        question_text = f"{template}\nSequence: {', '.join(str(t) for t in display_terms)}"
        
        if question_text in used_questions:
            continue
        
        used_questions.add(question_text)
        
        svg = generate_nth_term_table_svg(display_terms)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"The sequence is: {', '.join(map(str, terms[:missing_pos]))}, ?, ...\n"
        explanation += f"Common difference = {terms[1]} - {terms[0]} = {diff}\n"
        explanation += f"T{missing_pos + 1} = T{missing_pos} + {diff} = {terms[missing_pos - 1]} + {diff} = {correct}"
        
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
    Level 7: Linear vs Non-Linear (Ordinary)
    - Is the sequence linear or non-linear?
    - SEC 2022 OL Q12(d)(iii) & 2025 OL Q8(c)(iii) style
    """
    questions = []
    used_questions = set()
    
    templates = [
        "Is the following sequence linear or non-linear?\n{seq}, ...",
        "Determine if this sequence is linear or non-linear:\n{seq}, ...",
        "Look at this sequence: {seq}, ...\nIs it linear or non-linear?",
        "Classify this sequence as linear or non-linear:\n{seq}",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Generate more variety
        seq_type = random.choice(['linear', 'linear', 'quadratic', 'quadratic', 'geometric'])
        
        if seq_type == 'linear':
            a = random.randint(2, 8)
            b = random.randint(-5, 15)
            terms = [a * j + b for j in range(1, 6)]
            # Ensure positive
            if min(terms) <= 0:
                b = abs(min(terms)) + random.randint(1, 5)
                terms = [a * j + b for j in range(1, 6)]
            is_linear = True
        elif seq_type == 'quadratic':
            a = random.randint(1, 3)
            b = random.randint(-2, 3)
            c = random.randint(0, 8)
            terms = [a*n*n + b*n + c for n in range(1, 6)]
            if min(terms) <= 0:
                c = abs(min(terms)) + random.randint(1, 5)
                terms = [a*n*n + b*n + c for n in range(1, 6)]
            is_linear = False
        else:  # geometric
            start = random.randint(2, 5)
            ratio = random.choice([2, 3])
            terms = [start * (ratio ** j) for j in range(5)]
            is_linear = False
        
        seq_str = ', '.join(map(str, terms[:4]))
        template = random.choice(templates)
        question_text = template.format(seq=seq_str)
        
        if question_text in used_questions:
            continue
        
        used_questions.add(question_text)
        
        # Calculate differences
        diffs = [terms[j+1] - terms[j] for j in range(len(terms)-1)]
        
        correct = 'Linear' if is_linear else 'Non-linear'
        
        svg = generate_difference_visual_svg(terms[:4])
        
        options = ['Linear', 'Non-linear', 'Cannot tell', 'Neither']
        correct_idx = 0 if correct == 'Linear' else 1
        
        explanation = f"Sequence: {', '.join(map(str, terms[:4]))}\n"
        explanation += f"Differences: {', '.join(map(str, diffs[:3]))}\n"
        if is_linear:
            explanation += f"All differences are equal ({diffs[0]}), so the sequence is LINEAR."
        else:
            explanation += f"Differences are not constant, so the sequence is NON-LINEAR."
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_8(num_questions=50):
    """
    Level 8: Using nth Term Formula (Higher)
    - Given Tₙ = an + b, find specific terms
    - SEC HL style
    """
    questions = []
    
    for i in range(num_questions):
        a = random.randint(2, 8)
        b = random.randint(-5, 10)
        
        # Formula: Tn = an + b
        formula = f"{a}n {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else f"{a}n"
        
        n = random.randint(5, 15)
        correct = a * n + b
        
        # Different question types
        q_type = random.choice(['find_term', 'find_term', 'first_few'])
        
        if q_type == 'find_term':
            question_text = f"The nth term of a sequence is given by Tₙ = {formula}\n"
            question_text += f"Find the value of T{n} (the {get_ordinal(n)} term)."
            
            explanation = f"Tₙ = {formula}\n"
            explanation += f"T{n} = {a}({n}) {'+' if b >= 0 else '-'} {abs(b)}\n"
            explanation += f"T{n} = {a * n} {'+' if b >= 0 else '-'} {abs(b)}\n"
            explanation += f"T{n} = {correct}"
        
        else:  # first_few
            terms = [a * j + b for j in range(1, 5)]
            svg = generate_nth_term_table_svg(terms, show_formula=True, formula=formula)
            
            question_text = f"The nth term of a sequence is Tₙ = {formula}\n"
            question_text += f"What is T{n}?"
            
            explanation = f"Substitute n = {n} into Tₙ = {formula}\n"
            explanation += f"T{n} = {a} × {n} {'+' if b >= 0 else '-'} {abs(b)} = {correct}"
        
        options, correct_idx = generate_unique_options(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]),
            'option_b': format_number(options[1]),
            'option_c': format_number(options[2]),
            'option_d': format_number(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg if 'svg' in dir() else None
        })
    
    return questions


def generate_level_9(num_questions=50):
    """
    Level 9: Finding nth Term Formula (Higher)
    - Derive Tₙ = an + b from sequence
    - SEC 2022 HL Q4(c)(ii) style
    """
    questions = []
    used_questions = set()
    
    templates = [
        "Find the formula for the nth term (Tₙ) of this sequence:\n{seq}, ...",
        "Write down the nth term formula for:\n{seq}, ...",
        "What is the formula for Tₙ in this sequence?\n{seq}",
        "Express the nth term of this sequence as a formula:\n{seq}, ...",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        a = random.randint(2, 9)
        b = random.randint(-10, 12)
        
        terms = [a * j + b for j in range(1, 6)]
        
        # Ensure all positive for easier reading
        if min(terms) <= 0:
            b = b - min(terms) + random.randint(1, 5)
            terms = [a * j + b for j in range(1, 6)]
        
        seq_str = ', '.join(map(str, terms[:4]))
        template = random.choice(templates)
        question_text = template.format(seq=seq_str)
        
        if question_text in used_questions:
            continue
        
        used_questions.add(question_text)
        
        # The formula
        if b > 0:
            correct_formula = f"{a}n + {b}"
        elif b < 0:
            correct_formula = f"{a}n - {abs(b)}"
        else:
            correct_formula = f"{a}n"
        
        svg = generate_difference_visual_svg(terms[:4])
        
        # Generate wrong formulas
        wrong_formulas = [
            f"{a}n + {b + random.randint(1, 3)}",
            f"{a}n - {abs(b) + random.randint(1, 3)}",
            f"{a + 1}n + {b}",
            f"{a - 1}n + {b + a}",
            f"{a}n" if b != 0 else f"{a}n + 1",
            f"n + {terms[0]}",
            f"{a + 2}n - {random.randint(1, 5)}",
        ]
        
        options = [correct_formula]
        for wf in wrong_formulas:
            if wf not in options and len(options) < 4:
                options.append(wf)
        
        while len(options) < 4:
            options.append(f"{random.randint(1,8)}n + {random.randint(-5, 10)}")
        
        random.shuffle(options)
        correct_idx = options.index(correct_formula)
        
        explanation = f"Sequence: {', '.join(map(str, terms[:4]))}\n"
        explanation += f"Step 1: Find common difference = {terms[1]} - {terms[0]} = {a}\n"
        explanation += f"Step 2: So the formula starts with {a}n\n"
        explanation += f"Step 3: When n=1, T₁ = {a}(1) + b = {terms[0]}\n"
        explanation += f"        So {a} + b = {terms[0]}, meaning b = {b}\n"
        explanation += f"Formula: Tₙ = {correct_formula}"
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_10(num_questions=50):
    """
    Level 10: Quadratic Sequences (Higher)
    - Second differences
    - SEC 2025 HL Q2(a)(iii) style
    """
    questions = []
    
    for i in range(num_questions):
        q_type = random.choice(['next_term', 'second_diff', 'identify'])
        
        if q_type == 'next_term':
            # Quadratic: an² + bn + c
            a = random.randint(1, 3)
            b = random.randint(-2, 4)
            c = random.randint(0, 5)
            
            terms = [a*n*n + b*n + c for n in range(1, 7)]
            
            shown = terms[:4]
            correct = terms[4]
            
            # Calculate differences
            d1 = [terms[j+1] - terms[j] for j in range(5)]
            d2 = [d1[j+1] - d1[j] for j in range(4)]
            
            svg = generate_sequence_visual_svg(shown)
            
            question_text = f"Find the next term in this quadratic sequence:\n"
            question_text += f"{', '.join(map(str, shown))}, ?"
            
            explanation = f"Sequence: {', '.join(map(str, shown))}\n"
            explanation += f"1st differences: {', '.join(map(str, d1[:4]))}\n"
            explanation += f"2nd differences: {', '.join(map(str, d2[:3]))} (constant)\n"
            explanation += f"Next 1st difference = {d1[3]} + {d2[0]} = {d1[4]}\n"
            explanation += f"Next term = {shown[-1]} + {d1[4]} = {correct}"
        
        elif q_type == 'second_diff':
            # What is the second difference?
            a = random.randint(1, 4)
            b = random.randint(-3, 5)
            c = random.randint(0, 6)
            
            terms = [a*n*n + b*n + c for n in range(1, 6)]
            d1 = [terms[j+1] - terms[j] for j in range(4)]
            d2 = [d1[j+1] - d1[j] for j in range(3)]
            
            correct = d2[0]  # The constant second difference = 2a
            
            shown = terms[:5]
            svg = generate_sequence_visual_svg(shown[:4])
            
            question_text = f"What is the second difference of this sequence?\n"
            question_text += f"{', '.join(map(str, shown))}, ..."
            
            explanation = f"Sequence: {', '.join(map(str, shown))}\n"
            explanation += f"1st differences: {d1[0]}, {d1[1]}, {d1[2]}, {d1[3]}\n"
            explanation += f"2nd differences: {d2[0]}, {d2[1]}, {d2[2]}\n"
            explanation += f"The second difference is {correct}."
        
        else:  # identify
            # Is this linear or quadratic?
            if random.random() < 0.5:
                # Linear
                a = random.randint(2, 6)
                b = random.randint(1, 10)
                terms = [a*n + b for n in range(1, 6)]
                correct = "Linear"
                reason = "The first differences are constant"
            else:
                # Quadratic
                a = random.randint(1, 3)
                b = random.randint(-2, 3)
                c = random.randint(0, 5)
                terms = [a*n*n + b*n + c for n in range(1, 6)]
                correct = "Quadratic"
                reason = "The second differences are constant"
            
            shown = terms[:5]
            svg = generate_sequence_visual_svg(shown[:4])
            
            question_text = f"Is this sequence linear or quadratic?\n"
            question_text += f"{', '.join(map(str, shown))}, ..."
            
            options = ["Linear", "Quadratic", "Neither", "Cannot tell"]
            correct_idx = options.index(correct)
            
            d1 = [terms[j+1] - terms[j] for j in range(4)]
            
            explanation = f"Sequence: {', '.join(map(str, shown))}\n"
            explanation += f"1st differences: {', '.join(map(str, d1))}\n"
            if correct == "Linear":
                explanation += f"All 1st differences are equal ({d1[0]}), so it's LINEAR."
            else:
                d2 = [d1[j+1] - d1[j] for j in range(3)]
                explanation += f"2nd differences: {', '.join(map(str, d2))}\n"
                explanation += f"2nd differences are constant ({d2[0]}), so it's QUADRATIC."
        
        if q_type != 'identify':
            options, correct_idx = generate_unique_options(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]) if isinstance(options[0], (int, float)) else options[0],
            'option_b': format_number(options[1]) if isinstance(options[1], (int, float)) else options[1],
            'option_c': format_number(options[2]) if isinstance(options[2], (int, float)) else options[2],
            'option_d': format_number(options[3]) if isinstance(options[3], (int, float)) else options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_11(num_questions=50):
    """
    Level 11: Geometric Sequences (Higher)
    - Doubling, tripling, halving
    - SEC 2025 HL Q2(a)(ii) style
    """
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        q_type = random.choice(['next_terms', 'find_ratio', 'find_term', 'identify_type'])
        
        if q_type == 'next_terms':
            # Find next two terms
            start = random.choice([2, 3, 4, 5, 6, 7, 8])
            ratio = random.choice([2, 3, 4, 5])
            
            terms = [start * (ratio ** j) for j in range(6)]
            
            shown = terms[:4]
            correct = terms[4]
            
            svg = generate_sequence_visual_svg(shown)
            
            templates = [
                f"Find the next term in this geometric sequence:\n{', '.join(map(str, shown))}, ?",
                f"What comes next? {', '.join(map(str, shown))}, ...",
                f"Continue the pattern: {', '.join(map(str, shown))}, ?",
            ]
            question_text = random.choice(templates)
            
            explanation = f"Sequence: {', '.join(map(str, shown))}\n"
            explanation += f"Each term is multiplied by {ratio}.\n"
            explanation += f"Next term = {shown[-1]} × {ratio} = {correct}"
        
        elif q_type == 'find_ratio':
            # What is the common ratio?
            start = random.choice([2, 3, 4, 5, 6, 7, 8, 10])
            ratio = random.choice([2, 3, 4, 5])
            
            terms = [start * (ratio ** j) for j in range(5)]
            
            correct = ratio
            
            svg = generate_sequence_visual_svg(terms[:4])
            
            templates = [
                f"What is the common ratio of this geometric sequence?\n{', '.join(map(str, terms[:4]))}, ...",
                f"Find the common ratio: {', '.join(map(str, terms[:4]))}",
                f"By what number is each term multiplied?\n{', '.join(map(str, terms[:4]))}",
            ]
            question_text = random.choice(templates)
            
            explanation = f"Common ratio = second term ÷ first term\n"
            explanation += f"= {terms[1]} ÷ {terms[0]} = {ratio}\n"
            explanation += f"Check: {terms[2]} ÷ {terms[1]} = {ratio} ✓"
        
        elif q_type == 'find_term':
            # Find a specific term
            start = random.choice([2, 3, 4, 5])
            ratio = random.choice([2, 3])
            n = random.randint(5, 7)
            
            terms = [start * (ratio ** j) for j in range(n)]
            correct = terms[n - 1]
            
            shown = terms[:4]
            svg = generate_sequence_visual_svg(shown)
            
            templates = [
                f"In the geometric sequence {', '.join(map(str, shown))}, ...\nWhat is T{n} (the {get_ordinal(n)} term)?",
                f"Find the {get_ordinal(n)} term of: {', '.join(map(str, shown))}, ...",
            ]
            question_text = random.choice(templates)
            
            explanation = f"First term a = {start}, common ratio r = {ratio}\n"
            explanation += f"Tₙ = a × r^(n-1)\n"
            explanation += f"T{n} = {start} × {ratio}^{n-1} = {start} × {ratio ** (n-1)} = {correct}"
        
        else:  # identify_type
            # What type of sequence is this?
            seq_type = random.choice(['arithmetic', 'geometric', 'quadratic'])
            
            if seq_type == 'arithmetic':
                start = random.randint(3, 15)
                diff = random.randint(2, 8)
                terms = [start + j * diff for j in range(5)]
                correct = "Arithmetic (linear)"
            elif seq_type == 'geometric':
                start = random.randint(2, 6)
                ratio = random.choice([2, 3, 4])
                terms = [start * (ratio ** j) for j in range(5)]
                correct = "Geometric"
            else:
                a = random.randint(1, 2)
                c = random.randint(0, 5)
                terms = [a * n * n + c for n in range(1, 6)]
                correct = "Quadratic"
            
            svg = generate_sequence_visual_svg(terms[:4])
            
            templates = [
                f"What type of sequence is this?\n{', '.join(map(str, terms[:4]))}, ...",
                f"Classify this sequence: {', '.join(map(str, terms[:4]))}",
                f"Is this arithmetic, geometric, or quadratic?\n{', '.join(map(str, terms[:4]))}",
            ]
            question_text = random.choice(templates)
            
            options = ["Arithmetic (linear)", "Geometric", "Quadratic", "None of these"]
            correct_idx = options.index(correct)
            
            explanation = f"Sequence: {', '.join(map(str, terms[:4]))}\n"
            if seq_type == 'arithmetic':
                d = terms[1] - terms[0]
                explanation += f"Differences: {d}, {d}, {d} (constant) → Arithmetic"
            elif seq_type == 'geometric':
                r = terms[1] // terms[0]
                explanation += f"Ratios: {terms[1]}/{terms[0]}={r}, {terms[2]}/{terms[1]}={r} (constant) → Geometric"
            else:
                d1 = [terms[j+1] - terms[j] for j in range(4)]
                d2 = d1[1] - d1[0]
                explanation += f"1st differences not constant, 2nd differences = {d2} → Quadratic"
        
        if question_text in used_questions:
            continue
        
        used_questions.add(question_text)
        
        if q_type not in ['identify_type']:
            options, correct_idx = generate_unique_options(correct, min_val=1)
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]) if isinstance(options[0], (int, float)) else options[0],
            'option_b': format_number(options[1]) if isinstance(options[1], (int, float)) else options[1],
            'option_c': format_number(options[2]) if isinstance(options[2], (int, float)) else options[2],
            'option_d': format_number(options[3]) if isinstance(options[3], (int, float)) else options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_12(num_questions=50):
    """
    Level 12: Problem Solving & Applications (Mastery)
    - Is X a term in the sequence?
    - Find which term equals X
    - Real-world pattern problems
    - SEC 2024 HL Q12 style
    """
    questions = []
    
    for i in range(num_questions):
        q_type = random.choice(['is_term', 'which_term', 'matchstick', 'real_world', 'backwards'])
        
        if q_type == 'is_term':
            # Is X a term in the sequence?
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            
            terms = [a * n + b for n in range(1, 20)]
            
            # Sometimes pick a term, sometimes not
            if random.random() < 0.5:
                target = random.choice(terms[5:15])
                correct = "Yes"
                n = terms.index(target) + 1
                reason = f"{target} = {a}×{n} + {b}, so it's T{n}"
            else:
                # Pick a number that's NOT a term
                target = random.choice([t + 1 for t in terms[5:10] if (t + 1) not in terms])
                correct = "No"
                reason = f"Solving {a}n + {b} = {target} gives n = {(target - b) / a}, which is not a whole number"
            
            formula = f"{a}n + {b}"
            shown = terms[:4]
            
            svg = generate_sequence_visual_svg(shown)
            
            question_text = f"The nth term of a sequence is Tₙ = {formula}\n"
            question_text += f"Is {target} a term in this sequence?"
            
            options = ["Yes", "No", "Cannot determine", "Only if n > 10"]
            correct_idx = options.index(correct)
            
            explanation = f"To check if {target} is a term:\n"
            explanation += f"Solve {a}n + {b} = {target}\n"
            explanation += f"{a}n = {target - b}\n"
            explanation += f"n = {(target - b) / a}\n"
            if correct == "Yes":
                explanation += f"n = {n} is a positive integer, so YES, {target} is T{n}."
            else:
                explanation += f"n is not a positive integer, so NO, {target} is not in the sequence."
        
        elif q_type == 'which_term':
            # Which term is equal to X?
            a = random.randint(3, 7)
            b = random.randint(0, 8)
            
            n = random.randint(8, 15)
            target = a * n + b
            correct = n
            
            formula = f"{a}n + {b}" if b > 0 else f"{a}n"
            terms = [a * j + b for j in range(1, 5)]
            
            svg = generate_sequence_visual_svg(terms)
            
            question_text = f"The nth term is Tₙ = {formula}\n"
            question_text += f"Which term is equal to {target}?"
            
            options, correct_idx = generate_unique_options(correct, min_val=1)
            
            explanation = f"Solve {formula} = {target}\n"
            explanation += f"{a}n = {target - b}\n"
            explanation += f"n = {target - b} ÷ {a} = {n}\n"
            explanation += f"So {target} is the {get_ordinal(n)} term (T{n})."
        
        elif q_type == 'matchstick':
            # Matchstick pattern problem
            shape = random.choice(['square', 'triangle'])
            
            if shape == 'square':
                # Pattern: 4, 7, 10, 13... (3n + 1)
                a, b = 3, 1
                pattern_desc = "connected squares"
            else:
                # Pattern: 3, 5, 7, 9... (2n + 1)
                a, b = 2, 1
                pattern_desc = "connected triangles"
            
            n = random.randint(8, 15)
            correct = a * n + b
            
            svg, _ = generate_matchstick_pattern_svg(3, shape)
            
            question_text = f"A pattern is made from matchsticks forming {pattern_desc}.\n"
            question_text += f"Pattern 1 uses {a + b} matchsticks, Pattern 2 uses {2*a + b} matchsticks.\n"
            question_text += f"How many matchsticks are needed for Pattern {n}?"
            
            options, correct_idx = generate_unique_options(correct, min_val=a*n)
            
            explanation = f"Each new {shape} adds {a} matchsticks.\n"
            explanation += f"Formula: Tₙ = {a}n + {b}\n"
            explanation += f"T{n} = {a}×{n} + {b} = {correct} matchsticks"
        
        elif q_type == 'real_world':
            # Real-world problem
            contexts = [
                ("seats in a theatre", 20, 4, "rows"),
                ("chairs at tables", 4, 3, "tables"),
                ("tiles in a floor pattern", 5, 2, "pattern sections"),
                ("blocks in a wall", 10, 5, "layers"),
            ]
            
            context, start, diff, unit = random.choice(contexts)
            n = random.randint(6, 12)
            
            terms = [start + j * diff for j in range(n)]
            correct = terms[n - 1]
            
            shown = terms[:4]
            svg = generate_sequence_visual_svg(shown)
            
            question_text = f"A pattern of {context} has {terms[0]} in row 1, {terms[1]} in row 2, {terms[2]} in row 3.\n"
            question_text += f"How many {context.split()[0]} are in row {n}?"
            
            options, correct_idx = generate_unique_options(correct, min_val=start)
            
            explanation = f"Sequence: {', '.join(map(str, shown))}\n"
            explanation += f"Common difference = {diff}\n"
            explanation += f"Formula: Tₙ = {diff}n + {start - diff}\n"
            explanation += f"T{n} = {diff}×{n} + {start - diff} = {correct}"
        
        else:  # backwards
            # Given T10 = X, find the first term
            a = random.randint(3, 6)
            b = random.randint(1, 10)
            
            t10 = a * 10 + b
            correct = a + b  # T1
            
            question_text = f"In an arithmetic sequence, the common difference is {a}.\n"
            question_text += f"T₁₀ = {t10}. What is T₁ (the first term)?"
            
            options, correct_idx = generate_unique_options(correct, min_val=1)
            
            explanation = f"T₁₀ = T₁ + 9d (where d = common difference)\n"
            explanation += f"{t10} = T₁ + 9×{a}\n"
            explanation += f"{t10} = T₁ + {9*a}\n"
            explanation += f"T₁ = {t10} - {9*a} = {correct}"
            
            svg = None
        
        questions.append({
            'question_text': question_text,
            'option_a': format_number(options[0]) if isinstance(options[0], (int, float)) else options[0],
            'option_b': format_number(options[1]) if isinstance(options[1], (int, float)) else options[1],
            'option_c': format_number(options[2]) if isinstance(options[2], (int, float)) else options[2],
            'option_d': format_number(options[3]) if isinstance(options[3], (int, float)) else options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg if svg else None
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
        
        # Check explanation exists and has substance
        if not q.get('explanation') or len(q['explanation']) < 20:
            warnings.append(f"Level {level} Q{i+1}: Short or missing explanation")
        
        # Check question text exists
        if not q.get('question_text') or len(q['question_text']) < 10:
            errors.append(f"Level {level} Q{i+1}: Missing or short question text")
    
    return errors, warnings


def print_validation_summary(all_questions):
    """Print validation summary with visual progress bars"""
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
    
    # Count existing patterns questions
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE topic = 'patterns'")
    existing = cursor.fetchone()[0]
    print(f"Existing patterns questions: {existing}")
    
    # Delete existing patterns questions (ONLY from questions_adaptive!)
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = 'patterns'")
    print(f"Deleted {existing} existing patterns questions from questions_adaptive")
    
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
                    'patterns',
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
    print("AgentMath - Patterns Topic Generator v1")
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
            print("\n🎉 Patterns topic generation complete!")
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
        
        with open('patterns_questions_preview.json', 'w') as f:
            json.dump(output_data, f, indent=2)
        print("Saved preview to patterns_questions_preview.json")


if __name__ == '__main__':
    main()
