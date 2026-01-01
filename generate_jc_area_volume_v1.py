#!/usr/bin/env python3
"""
AgentMath - Area, Perimeter & Volume Topic Generator v1
SEC Junior Cycle Mathematics - Adaptive Quiz System

Generates 600 questions (50 per level × 12 levels) for the Area, Perimeter & Volume topic.
Aligned with SEC Junior Cycle Mathematics Specification.

Level Structure:
  Level 1:  Counting Squares for Area (Foundation)
  Level 2:  Perimeter of Rectangles (Foundation)
  Level 3:  Area of Rectangles (Foundation)
  Level 4:  Area of Triangles (Ordinary)
  Level 5:  Area of Circles (Ordinary)
  Level 6:  Circumference of Circles (Ordinary)
  Level 7:  Composite Shapes - Area (Higher)
  Level 8:  Volume of Cuboids (Higher)
  Level 9:  Volume of Cylinders (Higher)
  Level 10: Surface Area (Higher)
  Level 11: Tiles & Slabs Problems (Application)
  Level 12: Multi-step Problems (Mastery)

SEC Reference Questions:
  - 2022 OL Q4: Rectangle 5.6m × 4.2m, tiles 0.7m × 0.7m, cost
  - 2022 HL Q3: Rectangle with semicircle - area and perimeter
  - 2023 OL Q8: Garden lawn/patio, slabs 0.5m × 0.5m
  - 2023 HL Q7: Cylinder radius 8cm, height 15cm - volume
  - 2024 OL Q6: Triangle base 12cm, height 8cm - area
  - 2025 OL Q4: Rectangle 100cm × 60cm, Circle r=21cm
  - 2025 OL Q12(b): Pizza box volume and surface area
  - 2025 HL Q7: Golf course rectangle + semicircle, cylinder

Author: AgentMath Generator
Version: 1.0
Date: December 2025
"""

import random
import sqlite3
import os
import math
from datetime import datetime

# ============================================================
# SVG VISUAL GENERATORS
# ============================================================

def generate_grid_svg(width_squares, height_squares, shaded_squares=None):
    """Generate SVG showing a grid with optional shading for counting area"""
    cell_size = 25
    svg_width = width_squares * cell_size + 40
    svg_height = height_squares * cell_size + 40
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#f0f9ff" rx="8"/>'
    
    # Draw grid
    for row in range(height_squares):
        for col in range(width_squares):
            x = 20 + col * cell_size
            y = 20 + row * cell_size
            
            if shaded_squares and (row, col) in shaded_squares:
                fill = "#93c5fd"
            else:
                fill = "#ffffff"
            
            svg += f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="{fill}" stroke="#3b82f6" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def generate_rectangle_svg(length, width, show_labels=True, unit='cm'):
    """Generate SVG showing a rectangle with dimensions"""
    scale = min(180 / max(length, 1), 120 / max(width, 1), 20)
    rect_w = length * scale
    rect_h = width * scale
    
    svg_width = rect_w + 80
    svg_height = rect_h + 70
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#fef3c7" rx="8"/>'
    
    # Rectangle
    x_offset = 40
    y_offset = 30
    svg += f'<rect x="{x_offset}" y="{y_offset}" width="{rect_w}" height="{rect_h}" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
    
    if show_labels:
        # Length label (bottom)
        svg += f'<text x="{x_offset + rect_w/2}" y="{y_offset + rect_h + 20}" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">{length} {unit}</text>'
        # Width label (right side)
        svg += f'<text x="{x_offset + rect_w + 15}" y="{y_offset + rect_h/2}" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e" transform="rotate(90,{x_offset + rect_w + 15},{y_offset + rect_h/2})">{width} {unit}</text>'
    
    svg += '</svg>'
    return svg


def generate_triangle_svg(base, height, unit='cm'):
    """Generate SVG showing a triangle with base and height"""
    scale = min(180 / max(base, 1), 140 / max(height, 1), 15)
    tri_base = base * scale
    tri_height = height * scale
    
    svg_width = tri_base + 80
    svg_height = tri_height + 60
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#dcfce7" rx="8"/>'
    
    # Triangle points
    x1, y1 = 40, tri_height + 20  # Bottom left
    x2, y2 = 40 + tri_base, tri_height + 20  # Bottom right
    x3, y3 = 40, 20  # Top
    
    svg += f'<polygon points="{x1},{y1} {x2},{y2} {x3},{y3}" fill="#86efac" stroke="#16a34a" stroke-width="2"/>'
    
    # Height line (dashed)
    svg += f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="{y3}" stroke="#16a34a" stroke-width="1" stroke-dasharray="4"/>'
    
    # Base label
    svg += f'<text x="{x1 + tri_base/2}" y="{y1 + 18}" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">base = {base} {unit}</text>'
    
    # Height label
    svg += f'<text x="{x1 - 15}" y="{(y1+y3)/2}" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534" transform="rotate(-90,{x1-15},{(y1+y3)/2})">h = {height} {unit}</text>'
    
    svg += '</svg>'
    return svg


def generate_circle_svg(radius, unit='cm', show_radius=True):
    """Generate SVG showing a circle with radius"""
    scale = min(80 / max(radius, 1), 20)
    r = radius * scale
    
    svg_width = 2 * r + 80
    svg_height = 2 * r + 60
    cx, cy = svg_width / 2, svg_height / 2
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#fce7f3" rx="8"/>'
    
    # Circle
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fbcfe8" stroke="#db2777" stroke-width="2"/>'
    
    if show_radius:
        # Radius line
        svg += f'<line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="#db2777" stroke-width="2"/>'
        # Center dot
        svg += f'<circle cx="{cx}" cy="{cy}" r="3" fill="#db2777"/>'
        # Radius label
        svg += f'<text x="{cx + r/2}" y="{cy - 8}" text-anchor="middle" font-size="11" font-weight="bold" fill="#9d174d">r = {radius} {unit}</text>'
    
    svg += '</svg>'
    return svg


def generate_composite_rect_semi_svg(rect_length, rect_width, unit='cm'):
    """Generate SVG showing rectangle with semicircle (SEC 2022 HL Q3 style)"""
    scale = min(150 / max(rect_length, 1), 100 / max(rect_width, 1), 12)
    rect_l = rect_length * scale
    rect_w = rect_width * scale
    semi_r = rect_w / 2
    
    svg_width = rect_l + semi_r + 60
    svg_height = rect_w + 60
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#e0e7ff" rx="8"/>'
    
    x_off, y_off = 30, 30
    
    # Rectangle
    svg += f'<rect x="{x_off}" y="{y_off}" width="{rect_l}" height="{rect_w}" fill="#c7d2fe" stroke="#4f46e5" stroke-width="2"/>'
    
    # Semicircle on right
    svg += f'<path d="M{x_off + rect_l},{y_off} A{semi_r},{semi_r} 0 0 1 {x_off + rect_l},{y_off + rect_w}" fill="#c7d2fe" stroke="#4f46e5" stroke-width="2"/>'
    
    # Labels
    svg += f'<text x="{x_off + rect_l/2}" y="{y_off + rect_w + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#3730a3">{rect_length} {unit}</text>'
    svg += f'<text x="{x_off - 12}" y="{y_off + rect_w/2 + 4}" text-anchor="middle" font-size="10" font-weight="bold" fill="#3730a3">{rect_width} {unit}</text>'
    
    svg += '</svg>'
    return svg


def generate_cuboid_svg(length, width, height, unit='cm'):
    """Generate SVG showing a 3D cuboid"""
    scale = min(100 / max(length, 1), 80 / max(width, 1), 60 / max(height, 1), 10)
    l = length * scale
    w = width * scale * 0.5  # Perspective
    h = height * scale
    
    svg_width = l + w + 80
    svg_height = h + w + 60
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#fef9c3" rx="8"/>'
    
    x_off, y_off = 40, 20 + w
    
    # Front face
    svg += f'<rect x="{x_off}" y="{y_off}" width="{l}" height="{h}" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
    
    # Top face (parallelogram)
    top_points = f"{x_off},{y_off} {x_off + w},{y_off - w} {x_off + l + w},{y_off - w} {x_off + l},{y_off}"
    svg += f'<polygon points="{top_points}" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>'
    
    # Right face (parallelogram)
    right_points = f"{x_off + l},{y_off} {x_off + l + w},{y_off - w} {x_off + l + w},{y_off + h - w} {x_off + l},{y_off + h}"
    svg += f'<polygon points="{right_points}" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>'
    
    # Labels
    svg += f'<text x="{x_off + l/2}" y="{y_off + h + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#854d0e">{length} {unit}</text>'
    svg += f'<text x="{x_off - 12}" y="{y_off + h/2}" text-anchor="middle" font-size="10" font-weight="bold" fill="#854d0e">{height} {unit}</text>'
    svg += f'<text x="{x_off + l + w/2 + 10}" y="{y_off - w/2}" text-anchor="middle" font-size="10" font-weight="bold" fill="#854d0e">{width} {unit}</text>'
    
    svg += '</svg>'
    return svg


def generate_cylinder_svg(radius, height, unit='cm'):
    """Generate SVG showing a cylinder"""
    scale = min(60 / max(radius, 1), 80 / max(height, 1), 8)
    r = radius * scale
    h = height * scale
    ellipse_h = r * 0.3
    
    svg_width = 2 * r + 80
    svg_height = h + 2 * ellipse_h + 60
    cx = svg_width / 2
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#f0fdfa" rx="8"/>'
    
    y_top = 30 + ellipse_h
    y_bottom = y_top + h
    
    # Side rectangle
    svg += f'<rect x="{cx - r}" y="{y_top}" width="{2*r}" height="{h}" fill="#99f6e4" stroke="#0d9488" stroke-width="2"/>'
    
    # Bottom ellipse
    svg += f'<ellipse cx="{cx}" cy="{y_bottom}" rx="{r}" ry="{ellipse_h}" fill="#5eead4" stroke="#0d9488" stroke-width="2"/>'
    
    # Top ellipse
    svg += f'<ellipse cx="{cx}" cy="{y_top}" rx="{r}" ry="{ellipse_h}" fill="#99f6e4" stroke="#0d9488" stroke-width="2"/>'
    
    # Labels
    svg += f'<line x1="{cx}" y1="{y_top}" x2="{cx + r}" y2="{y_top}" stroke="#0d9488" stroke-width="1.5" stroke-dasharray="4"/>'
    svg += f'<text x="{cx + r/2}" y="{y_top - 8}" text-anchor="middle" font-size="10" font-weight="bold" fill="#134e4a">r = {radius} {unit}</text>'
    svg += f'<text x="{cx + r + 15}" y="{y_top + h/2}" text-anchor="middle" font-size="10" font-weight="bold" fill="#134e4a">{height} {unit}</text>'
    
    svg += '</svg>'
    return svg


def generate_tiles_svg(room_length, room_width, tile_size, unit='m'):
    """Generate SVG showing room with tiles"""
    scale = 30
    room_w = room_length * scale
    room_h = room_width * scale
    tile_s = tile_size * scale
    
    svg_width = room_w + 60
    svg_height = room_h + 60
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#fff7ed" rx="8"/>'
    
    x_off, y_off = 30, 30
    
    # Room outline
    svg += f'<rect x="{x_off}" y="{y_off}" width="{room_w}" height="{room_h}" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>'
    
    # Tile grid
    num_tiles_x = int(room_length / tile_size)
    num_tiles_y = int(room_width / tile_size)
    
    for i in range(num_tiles_x):
        for j in range(num_tiles_y):
            tx = x_off + i * tile_s
            ty = y_off + j * tile_s
            fill = "#fdba74" if (i + j) % 2 == 0 else "#fb923c"
            svg += f'<rect x="{tx}" y="{ty}" width="{tile_s}" height="{tile_s}" fill="{fill}" stroke="#c2410c" stroke-width="0.5"/>'
    
    # Labels
    svg += f'<text x="{x_off + room_w/2}" y="{y_off + room_h + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#9a3412">{room_length} {unit}</text>'
    svg += f'<text x="{x_off - 12}" y="{y_off + room_h/2}" text-anchor="middle" font-size="10" font-weight="bold" fill="#9a3412">{room_width} {unit}</text>'
    
    # Tile label
    svg += f'<text x="{x_off + room_w + 5}" y="15" text-anchor="start" font-size="9" fill="#9a3412">Tile: {tile_size}×{tile_size} {unit}</text>'
    
    svg += '</svg>'
    return svg


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_number(n, decimals=None):
    """Format number - remove .0 from whole numbers, or round to decimals"""
    if decimals is not None:
        n = round(n, decimals)
    if isinstance(n, float) and n == int(n):
        return str(int(n))
    if isinstance(n, float):
        return f"{n:.2f}".rstrip('0').rstrip('.')
    return str(n)


def generate_unique_options(correct_answer, num_options=4, min_val=None, max_val=None, 
                           avoid=None, decimal_places=None):
    """Generate unique answer options including the correct answer"""
    if avoid is None:
        avoid = set()
    
    if decimal_places is not None:
        correct_answer = round(correct_answer, decimal_places)
    
    options = [correct_answer]
    avoid = set(avoid)
    avoid.add(correct_answer)
    
    attempts = 0
    max_attempts = 100
    
    while len(options) < num_options and attempts < max_attempts:
        attempts += 1
        
        # Generate plausible wrong answers
        if isinstance(correct_answer, (int, float)):
            strategies = [
                correct_answer * random.choice([0.5, 0.8, 1.2, 1.5, 2]),
                correct_answer + random.randint(-10, 10),
                correct_answer - random.randint(1, int(max(correct_answer * 0.3, 5))),
                correct_answer + random.randint(1, int(max(correct_answer * 0.3, 5))),
            ]
            wrong = random.choice(strategies)
            
            if decimal_places is not None:
                wrong = round(wrong, decimal_places)
            elif isinstance(correct_answer, int):
                wrong = int(wrong)
        else:
            wrong = correct_answer + random.randint(-5, 5)
        
        # Apply bounds
        if min_val is not None and wrong < min_val:
            wrong = min_val + random.randint(1, 5)
        if max_val is not None and wrong > max_val:
            wrong = max_val - random.randint(1, 5)
        
        if wrong not in avoid and wrong != correct_answer and wrong > 0:
            options.append(wrong)
            avoid.add(wrong)
    
    # Ensure we have enough options
    while len(options) < num_options:
        if isinstance(correct_answer, int):
            filler = correct_answer + len(options) * 3 + random.randint(1, 5)
        else:
            filler = correct_answer * (1 + len(options) * 0.15)
            if decimal_places is not None:
                filler = round(filler, decimal_places)
        if filler not in avoid and filler > 0:
            options.append(filler)
            avoid.add(filler)
    
    random.shuffle(options)
    correct_idx = options.index(correct_answer)
    
    return options, correct_idx


# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1(num_questions=50):
    """
    Level 1: Counting Squares for Area (Foundation)
    - Count shaded squares on a grid
    """
    questions = []
    used_questions = set()
    
    templates = [
        "Count the shaded squares to find the area of the {w}×{h} shaded region.\nArea = ? square units",
        "How many squares are shaded in the {w}×{h} region?\nThis gives the area in square units.",
        "The shaded area is {w} squares wide and {h} squares tall.\nHow many squares are shaded?",
        "Find the area by counting the shaded squares ({w} by {h} region).",
        "A {w}×{h} rectangular region is shaded.\nCount to find the area in square units.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        width = random.randint(3, 6)
        height = random.randint(2, 5)
        
        # Shade a rectangle within the grid
        shade_w = random.randint(2, width)
        shade_h = random.randint(2, height)
        
        correct = shade_w * shade_h
        
        template = random.choice(templates)
        question_text = template.format(w=shade_w, h=shade_h)
        
        # Check for duplicate question_text (what goes to database)
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Create shaded squares set
        shaded = set()
        for r in range(shade_h):
            for c in range(shade_w):
                shaded.add((r, c))
        
        svg = generate_grid_svg(width, height, shaded)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Count the shaded squares:\n"
        explanation += f"Width: {shade_w} squares\n"
        explanation += f"Height: {shade_h} squares\n"
        explanation += f"Area = {shade_w} × {shade_h} = {correct} square units"
        
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
    Level 2: Perimeter of Rectangles (Foundation)
    - P = 2(l + w) or P = 2l + 2w
    """
    questions = []
    used_questions = set()
    
    templates = [
        "Find the perimeter of the rectangle with length {l} cm and width {w} cm.",
        "Calculate the perimeter of a rectangle measuring {l} cm by {w} cm.",
        "A rectangle has length {l} cm and width {w} cm.\nWhat is the perimeter?",
        "Work out the perimeter of a {l} cm × {w} cm rectangle.",
        "Rectangle dimensions: {l} cm × {w} cm.\nFind the perimeter.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        length = random.randint(4, 15)
        width = random.randint(3, 12)
        if width > length:
            length, width = width, length
        
        correct = 2 * (length + width)
        
        template = random.choice(templates)
        question_text = template.format(l=length, w=width)
        
        # Check for duplicate question_text (what goes to database)
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_rectangle_svg(length, width)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Perimeter = 2 × (length + width)\n"
        explanation += f"P = 2 × ({length} + {width})\n"
        explanation += f"P = 2 × {length + width}\n"
        explanation += f"P = {correct} cm"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm",
            'option_b': f"{format_number(options[1])} cm",
            'option_c': f"{format_number(options[2])} cm",
            'option_d': f"{format_number(options[3])} cm",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_3(num_questions=50):
    """
    Level 3: Area of Rectangles (Foundation)
    - A = length × width
    - SEC 2022 OL Q4, 2025 OL Q4(a) style
    """
    questions = []
    used_questions = set()
    
    contexts = [
        ("rectangular room", "m"),
        ("rectangular flag", "cm"),
        ("rectangular garden", "m"),
        ("rectangular field", "m"),
        ("rectangular card", "cm"),
    ]
    
    templates = [
        "A {context} has length {l} {unit} and width {w} {unit}.\nFind the area.",
        "Find the area of the {context} shown.",
        "Calculate the area of this {context}.",
        "What is the area of a {context} with length {l} {unit} and width {w} {unit}?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        context, unit = random.choice(contexts)
        
        if unit == 'm':
            length = random.randint(3, 12)
            width = random.randint(2, 10)
        else:
            length = random.randint(10, 100)
            width = random.randint(8, 80)
        
        if width > length:
            length, width = width, length
        
        correct = length * width
        
        template = random.choice(templates)
        question_text = template.format(context=context, l=length, w=width, unit=unit)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_rectangle_svg(length, width, unit=unit)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Area = length × width\n"
        explanation += f"A = {length} × {width}\n"
        explanation += f"A = {correct} {unit}²"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} {unit}²",
            'option_b': f"{format_number(options[1])} {unit}²",
            'option_c': f"{format_number(options[2])} {unit}²",
            'option_d': f"{format_number(options[3])} {unit}²",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_4(num_questions=50):
    """
    Level 4: Area of Triangles (Ordinary)
    - A = ½ × base × height
    - SEC 2024 OL Q6 style
    """
    questions = []
    used_questions = set()
    
    templates = [
        "Triangle ABC has base {b} cm and height {h} cm.\nFind the area.",
        "Find the area of a triangle with base {b} cm and perpendicular height {h} cm.",
        "Calculate the area of the triangle shown.",
        "A triangle has base = {b} cm and height = {h} cm.\nWhat is its area?",
        "Work out the area of triangle with base {b} cm and height {h} cm.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Use even numbers for clean half calculations
        base = random.choice([4, 6, 8, 10, 12, 14, 16, 18, 20])
        height = random.randint(3, 15)
        
        correct = (base * height) / 2
        
        template = random.choice(templates)
        question_text = template.format(b=base, h=height)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_triangle_svg(base, height)
        
        # Common mistakes: forgetting ½, base×height
        wrong_answers = [base * height, (base + height) / 2]
        options, correct_idx = generate_unique_options(correct, min_val=1, avoid=set())
        
        explanation = f"Area of triangle = ½ × base × height\n"
        explanation += f"A = ½ × {base} × {height}\n"
        explanation += f"A = ½ × {base * height}\n"
        explanation += f"A = {format_number(correct)} cm²"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm²",
            'option_b': f"{format_number(options[1])} cm²",
            'option_c': f"{format_number(options[2])} cm²",
            'option_d': f"{format_number(options[3])} cm²",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_5(num_questions=50):
    """
    Level 5: Area of Circles (Ordinary)
    - A = πr²
    - SEC 2025 OL Q4(b) style
    """
    questions = []
    used_questions = set()
    
    templates = [
        "A circle has radius {r} cm.\nFind the area. Give your answer to the nearest cm².",
        "Calculate the area of a circle with radius {r} cm.\nRound to the nearest cm².",
        "Find the area of the circle shown.\nGive your answer to the nearest cm².",
        "What is the area of a circle with radius {r} cm?\n(Answer to nearest cm²)",
        "Work out the area of a circle with r = {r} cm.\nRound to nearest whole number.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        radius = random.randint(3, 21)
        
        correct = round(math.pi * radius * radius)
        
        template = random.choice(templates)
        question_text = template.format(r=radius)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_circle_svg(radius)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Area = πr²\n"
        explanation += f"A = π × {radius}²\n"
        explanation += f"A = π × {radius * radius}\n"
        explanation += f"A = {math.pi * radius * radius:.2f}...\n"
        explanation += f"A ≈ {correct} cm²"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm²",
            'option_b': f"{format_number(options[1])} cm²",
            'option_c': f"{format_number(options[2])} cm²",
            'option_d': f"{format_number(options[3])} cm²",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_6(num_questions=50):
    """
    Level 6: Circumference of Circles (Ordinary)
    - C = 2πr or C = πd
    """
    questions = []
    used_questions = set()
    
    templates_radius = [
        "A circle has radius {r} cm.\nFind the circumference. Give your answer to 1 decimal place.",
        "Calculate the circumference of a circle with radius {r} cm.\nRound to 1 d.p.",
        "Find the circumference of the circle with r = {r} cm.\n(1 decimal place)",
    ]
    
    templates_diameter = [
        "A circle has diameter {d} cm.\nFind the circumference. Give your answer to 1 decimal place.",
        "Calculate the circumference of a circle with diameter {d} cm.\nRound to 1 d.p.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        use_radius = random.random() < 0.6
        
        if use_radius:
            radius = random.randint(3, 20)
            correct = round(2 * math.pi * radius, 1)
            template = random.choice(templates_radius)
            question_text = template.format(r=radius)
            svg = generate_circle_svg(radius)
            explanation = f"Circumference = 2πr\n"
            explanation += f"C = 2 × π × {radius}\n"
            explanation += f"C = {2 * math.pi * radius:.4f}...\n"
            explanation += f"C ≈ {correct} cm"
        else:
            diameter = random.randint(6, 40)
            radius = diameter / 2
            correct = round(math.pi * diameter, 1)
            template = random.choice(templates_diameter)
            question_text = template.format(d=diameter)
            svg = generate_circle_svg(radius)
            explanation = f"Circumference = πd\n"
            explanation += f"C = π × {diameter}\n"
            explanation += f"C = {math.pi * diameter:.4f}...\n"
            explanation += f"C ≈ {correct} cm"
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        options, correct_idx = generate_unique_options(correct, min_val=1, decimal_places=1)
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm",
            'option_b': f"{format_number(options[1])} cm",
            'option_c': f"{format_number(options[2])} cm",
            'option_d': f"{format_number(options[3])} cm",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_7(num_questions=50):
    """
    Level 7: Composite Shapes - Area (Higher)
    - Rectangle + semicircle
    - SEC 2022 HL Q3, 2025 HL Q7(a) style
    """
    questions = []
    used_questions = set()
    
    templates = [
        "A shape consists of a rectangle ({l} cm × {w} cm) and a semicircle.\nFind the total area to the nearest cm².",
        "Find the total area of the composite shape: rectangle {l} cm × {w} cm with semicircle attached.\nGive your answer to the nearest cm².",
        "Calculate the area of the shape (rectangle {l}×{w} cm + semicircle).\nRound to nearest cm².",
        "The shape is made of a {l} cm × {w} cm rectangle with a semicircle on one end.\nFind the total area to nearest cm².",
        "Composite shape: {l} cm by {w} cm rectangle plus semicircle.\nWhat is the total area? (nearest cm²)",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        rect_length = random.randint(8, 20)
        rect_width = random.choice([4, 6, 8, 10, 12])  # Even for clean semicircle
        
        rect_area = rect_length * rect_width
        semi_radius = rect_width / 2
        semi_area = (math.pi * semi_radius * semi_radius) / 2
        correct = round(rect_area + semi_area)
        
        template = random.choice(templates)
        question_text = template.format(l=rect_length, w=rect_width)
        
        # Check for duplicate question_text (what goes to database)
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_composite_rect_semi_svg(rect_length, rect_width)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Rectangle area = {rect_length} × {rect_width} = {rect_area} cm²\n"
        explanation += f"Semicircle radius = {rect_width} ÷ 2 = {semi_radius} cm\n"
        explanation += f"Semicircle area = ½ × π × {semi_radius}² = {semi_area:.2f} cm²\n"
        explanation += f"Total = {rect_area} + {semi_area:.2f} ≈ {correct} cm²"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm²",
            'option_b': f"{format_number(options[1])} cm²",
            'option_c': f"{format_number(options[2])} cm²",
            'option_d': f"{format_number(options[3])} cm²",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_8(num_questions=50):
    """
    Level 8: Volume of Cuboids (Higher)
    - V = length × width × height
    - SEC 2025 OL Q12(b) style
    """
    questions = []
    used_questions = set()
    
    contexts = [
        "box",
        "container",
        "storage crate",
        "pizza box",
        "fish tank",
    ]
    
    templates = [
        "A {context} has dimensions {l} cm × {w} cm × {h} cm.\nFind the volume.",
        "Calculate the volume of the {context} shown.",
        "Find the volume of a {context} with length {l} cm, width {w} cm, and height {h} cm.",
        "What is the volume of this {context}?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        context = random.choice(contexts)
        length = random.randint(10, 30)
        width = random.randint(8, 25)
        height = random.randint(3, 15)
        
        correct = length * width * height
        
        template = random.choice(templates)
        question_text = template.format(context=context, l=length, w=width, h=height)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_cuboid_svg(length, width, height)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Volume = length × width × height\n"
        explanation += f"V = {length} × {width} × {height}\n"
        explanation += f"V = {correct} cm³"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm³",
            'option_b': f"{format_number(options[1])} cm³",
            'option_c': f"{format_number(options[2])} cm³",
            'option_d': f"{format_number(options[3])} cm³",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_9(num_questions=50):
    """
    Level 9: Volume of Cylinders (Higher)
    - V = πr²h
    - SEC 2023 HL Q7, 2025 HL Q7(d) style
    """
    questions = []
    used_questions = set()
    
    templates = [
        "A cylinder has radius {r} cm and height {h} cm.\nFind the volume to the nearest cm³.",
        "Calculate the volume of a cylindrical container with r = {r} cm and h = {h} cm.\nRound to nearest cm³.",
        "Find the volume of the cylinder shown.\nGive your answer to the nearest cm³.",
        "A cylindrical tank has radius {r} cm and height {h} cm.\nWhat is its volume to nearest cm³?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        radius = random.randint(3, 15)
        height = random.randint(8, 25)
        
        correct = round(math.pi * radius * radius * height)
        
        template = random.choice(templates)
        question_text = template.format(r=radius, h=height)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_cylinder_svg(radius, height)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Volume = πr²h\n"
        explanation += f"V = π × {radius}² × {height}\n"
        explanation += f"V = π × {radius * radius} × {height}\n"
        explanation += f"V = {math.pi * radius * radius * height:.2f}...\n"
        explanation += f"V ≈ {correct} cm³"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm³",
            'option_b': f"{format_number(options[1])} cm³",
            'option_c': f"{format_number(options[2])} cm³",
            'option_d': f"{format_number(options[3])} cm³",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_10(num_questions=50):
    """
    Level 10: Surface Area (Higher)
    - Surface area of cuboids
    - SEC 2025 OL Q12(b) style
    """
    questions = []
    used_questions = set()
    
    templates = [
        "A box has dimensions {l} cm × {w} cm × {h} cm.\nFind the total surface area.",
        "Calculate the surface area of a box with length {l} cm, width {w} cm, height {h} cm.",
        "Find the total surface area of the cuboid shown.",
        "What is the surface area of a box measuring {l} cm × {w} cm × {h} cm?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        length = random.randint(6, 20)
        width = random.randint(5, 15)
        height = random.randint(3, 12)
        
        # SA = 2(lw + lh + wh)
        correct = 2 * (length * width + length * height + width * height)
        
        template = random.choice(templates)
        question_text = template.format(l=length, w=width, h=height)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_cuboid_svg(length, width, height)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        lw = length * width
        lh = length * height
        wh = width * height
        
        explanation = f"Surface Area = 2(lw + lh + wh)\n"
        explanation += f"= 2({length}×{width} + {length}×{height} + {width}×{height})\n"
        explanation += f"= 2({lw} + {lh} + {wh})\n"
        explanation += f"= 2 × {lw + lh + wh}\n"
        explanation += f"= {correct} cm²"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} cm²",
            'option_b': f"{format_number(options[1])} cm²",
            'option_c': f"{format_number(options[2])} cm²",
            'option_d': f"{format_number(options[3])} cm²",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_11(num_questions=50):
    """
    Level 11: Tiles & Slabs Problems (Application)
    - How many tiles to cover an area?
    - SEC 2022 OL Q4, 2023 OL Q8, 2025 OL Q11(b) style
    """
    questions = []
    used_questions = set()
    
    contexts = [
        ("room", "tiles"),
        ("patio", "slabs"),
        ("garden", "paving stones"),
        ("floor", "tiles"),
        ("vegetable patch", "cabbages"),
    ]
    
    templates = [
        "A {context} measures {l} m by {w} m.\n{items} are {ts} m × {ts} m each.\nHow many {items} are needed?",
        "Find how many {items} ({ts}m × {ts}m) are needed to cover a {context} measuring {l}m × {w}m.",
        "A {context} is {l} m by {w} m. Each {item_single} is {ts} m × {ts} m.\nHow many are needed to cover it?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        context, items = random.choice(contexts)
        item_single = items[:-1] if items.endswith('s') else items
        
        # Use dimensions that divide evenly
        tile_size = random.choice([0.25, 0.3, 0.5, 0.7, 1.0])
        
        # Room dimensions that work with tile size
        length_tiles = random.randint(4, 12)
        width_tiles = random.randint(3, 10)
        
        length = length_tiles * tile_size
        width = width_tiles * tile_size
        
        correct = length_tiles * width_tiles
        
        template = random.choice(templates)
        question_text = template.format(
            context=context, l=length, w=width, 
            ts=tile_size, items=items, item_single=item_single
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        svg = generate_tiles_svg(length, width, tile_size)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        room_area = length * width
        tile_area = tile_size * tile_size
        
        explanation = f"Room area = {length} × {width} = {room_area} m²\n"
        explanation += f"Tile area = {tile_size} × {tile_size} = {tile_area} m²\n"
        explanation += f"Number of {items} = {room_area} ÷ {tile_area}\n"
        explanation += f"= {correct} {items}"
        
        questions.append({
            'question_text': question_text,
            'option_a': str(int(options[0])),
            'option_b': str(int(options[1])),
            'option_c': str(int(options[2])),
            'option_d': str(int(options[3])),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_12(num_questions=50):
    """
    Level 12: Multi-step Problems (Mastery)
    - Combined area/volume with costs
    - Comparing shapes
    - Real-world applications
    """
    questions = []
    used_questions = set()
    
    problem_types = [
        'tiles_cost',
        'paint_coverage',
        'volume_fill_time',
        'area_comparison',
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        problem = random.choice(problem_types)
        
        if problem == 'tiles_cost':
            length = random.randint(4, 8)
            width = random.randint(3, 6)
            tile_size = random.choice([0.5, 1.0])
            tile_cost = random.choice([5, 6, 8, 10, 12])
            
            area = length * width
            num_tiles = int(area / (tile_size * tile_size))
            correct = num_tiles * tile_cost
            
            question_text = f"A room is {length} m × {width} m.\n"
            question_text += f"Tiles are {tile_size} m × {tile_size} m and cost €{tile_cost} each.\n"
            question_text += f"Find the total cost of tiles needed."
            
            svg = generate_rectangle_svg(length, width, unit='m')
            
            explanation = f"Room area = {length} × {width} = {area} m²\n"
            explanation += f"Tile area = {tile_size}² = {tile_size * tile_size} m²\n"
            explanation += f"Number of tiles = {area} ÷ {tile_size * tile_size} = {num_tiles}\n"
            explanation += f"Total cost = {num_tiles} × €{tile_cost} = €{correct}"
            
            options, correct_idx = generate_unique_options(correct, min_val=10)
            options_formatted = [f"€{int(o)}" for o in options]
            
        elif problem == 'paint_coverage':
            length = random.randint(8, 15)
            width = random.randint(6, 12)
            coverage = random.choice([10, 12, 15])  # m² per litre
            
            area = length * width
            correct = math.ceil(area / coverage)
            
            question_text = f"A wall measures {length} m × {width} m.\n"
            question_text += f"One litre of paint covers {coverage} m².\n"
            question_text += f"How many litres are needed?"
            
            svg = generate_rectangle_svg(length, width, unit='m')
            
            explanation = f"Wall area = {length} × {width} = {area} m²\n"
            explanation += f"Litres needed = {area} ÷ {coverage} = {area/coverage:.1f}\n"
            explanation += f"Round up: {correct} litres"
            
            options, correct_idx = generate_unique_options(correct, min_val=1)
            options_formatted = [f"{int(o)} litres" for o in options]
            
        elif problem == 'volume_fill_time':
            radius = random.randint(5, 10)
            height = random.randint(15, 30)
            rate = random.choice([50, 100, 200])  # cm³ per second
            
            volume = math.pi * radius * radius * height
            time_secs = volume / rate
            correct = round(time_secs)
            
            question_text = f"A cylinder has radius {radius} cm and height {height} cm.\n"
            question_text += f"Water is poured in at {rate} cm³ per second.\n"
            question_text += f"How long to fill it? (to nearest second)"
            
            svg = generate_cylinder_svg(radius, height)
            
            explanation = f"Volume = πr²h = π × {radius}² × {height}\n"
            explanation += f"V = {volume:.1f} cm³\n"
            explanation += f"Time = {volume:.1f} ÷ {rate} = {time_secs:.1f}\n"
            explanation += f"≈ {correct} seconds"
            
            options, correct_idx = generate_unique_options(correct, min_val=1)
            options_formatted = [f"{int(o)} s" for o in options]
            
        else:  # area_comparison
            rect_l = random.randint(8, 15)
            rect_w = random.randint(6, 10)
            circle_r = random.randint(4, 8)
            
            rect_area = rect_l * rect_w
            circle_area = math.pi * circle_r * circle_r
            
            correct = round(abs(rect_area - circle_area))
            
            if rect_area > circle_area:
                question_text = f"Rectangle: {rect_l} cm × {rect_w} cm.\n"
                question_text += f"Circle: radius {circle_r} cm.\n"
                question_text += f"How much larger is the rectangle? (nearest cm²)"
            else:
                question_text = f"Rectangle: {rect_l} cm × {rect_w} cm.\n"
                question_text += f"Circle: radius {circle_r} cm.\n"
                question_text += f"How much larger is the circle? (nearest cm²)"
            
            svg = generate_rectangle_svg(rect_l, rect_w)
            
            explanation = f"Rectangle area = {rect_l} × {rect_w} = {rect_area} cm²\n"
            explanation += f"Circle area = π × {circle_r}² = {circle_area:.1f} cm²\n"
            explanation += f"Difference = |{rect_area} - {circle_area:.1f}| ≈ {correct} cm²"
            
            options, correct_idx = generate_unique_options(correct, min_val=1)
            options_formatted = [f"{int(o)} cm²" for o in options]
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        questions.append({
            'question_text': question_text,
            'option_a': options_formatted[0],
            'option_b': options_formatted[1],
            'option_c': options_formatted[2],
            'option_d': options_formatted[3],
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
    
    # Count existing area questions
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE topic = 'area_perimeter_volume'")
    existing = cursor.fetchone()[0]
    print(f"Existing area_perimeter_volume questions: {existing}")
    
    # Delete existing area questions (ONLY from questions_adaptive!)
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = 'area_perimeter_volume'")
    print(f"Deleted {existing} existing area_perimeter_volume questions from questions_adaptive")
    
    inserted = 0
    errors = 0
    
    for level in range(1, 13):
        questions = all_questions.get(level, [])
        
        # Determine difficulty band
        if level <= 3:
            band = 'Foundation'
        elif level <= 6:
            band = 'Ordinary'
        elif level <= 10:
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
                    'area_perimeter_volume',
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
    print("AgentMath - Area, Perimeter & Volume Topic Generator v1")
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
            print("\n🎉 Area, Perimeter & Volume topic generation complete!")
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
        
        with open('area_volume_questions_preview.json', 'w') as f:
            json.dump(output_data, f, indent=2)
        print("Saved preview to area_volume_questions_preview.json")


if __name__ == '__main__':
    main()
