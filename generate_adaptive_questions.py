#!/usr/bin/env python3
"""
Generate visual questions for Adaptive Quiz BETA
Targets 75% graphical questions across all 10 levels
Topics: Fractions, Percentages, Probability
"""

import sqlite3
import random
import math
import os
from datetime import datetime

# Database path - update for PythonAnywhere
# Check multiple possible database locations
POSSIBLE_PATHS = [
    'mathapp.db',
    'instance/mathquiz.db',
    'mathquiz.db',
]

def find_db():
    """Find the database file"""
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            return path
    print("ERROR: Database not found!")
    exit(1)

DB_PATH = None  # Will be set dynamically

def get_db():
    global DB_PATH
    if DB_PATH is None:
        DB_PATH = find_db()
        print(f"Using database: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

# ============================================================
# SVG GENERATORS
# ============================================================

def svg_pie_chart(num_shaded, total_slices, size=200):
    """Generate SVG pie chart with shaded slices"""
    cx, cy, r = size//2, size//2, size//2 - 10
    angle_per_slice = 360 / total_slices
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    for i in range(total_slices):
        start_angle = i * angle_per_slice - 90
        end_angle = (i + 1) * angle_per_slice - 90
        
        # Convert to radians
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        # Calculate arc points
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        
        large_arc = 1 if angle_per_slice > 180 else 0
        color = '#8b5cf6' if i < num_shaded else '#e5e7eb'
        
        path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large_arc},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="#374151" stroke-width="2"/>'
    
    # Center dot
    svg += f'<circle cx="{cx}" cy="{cy}" r="4" fill="#374151"/>'
    svg += '</svg>'
    return svg


def svg_fraction_bar(num_shaded, total_parts, width=300, height=60):
    """Generate SVG fraction bar (rectangle divided into parts)"""
    part_width = (width - 20) / total_parts
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    svg += f'<rect x="10" y="10" width="{width-20}" height="{height-20}" fill="none" stroke="#374151" stroke-width="2" rx="5"/>'
    
    for i in range(total_parts):
        x = 10 + i * part_width
        color = '#8b5cf6' if i < num_shaded else '#f3f4f6'
        svg += f'<rect x="{x}" y="10" width="{part_width}" height="{height-20}" fill="{color}" stroke="#374151" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def svg_number_line(value, min_val=0, max_val=1, width=350, height=80):
    """Generate SVG number line showing a fraction/decimal"""
    margin = 40
    line_width = width - 2 * margin
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    # Main line
    y = height // 2
    svg += f'<line x1="{margin}" y1="{y}" x2="{width-margin}" y2="{y}" stroke="#374151" stroke-width="3"/>'
    
    # End ticks and labels
    svg += f'<line x1="{margin}" y1="{y-10}" x2="{margin}" y2="{y+10}" stroke="#374151" stroke-width="2"/>'
    svg += f'<text x="{margin}" y="{y+25}" text-anchor="middle" font-size="14" fill="#374151">{min_val}</text>'
    
    svg += f'<line x1="{width-margin}" y1="{y-10}" x2="{width-margin}" y2="{y+10}" stroke="#374151" stroke-width="2"/>'
    svg += f'<text x="{width-margin}" y="{y+25}" text-anchor="middle" font-size="14" fill="#374151">{max_val}</text>'
    
    # Value marker
    pos = margin + (value - min_val) / (max_val - min_val) * line_width
    svg += f'<circle cx="{pos}" cy="{y}" r="8" fill="#8b5cf6" stroke="#5b21b6" stroke-width="2"/>'
    svg += f'<line x1="{pos}" y1="{y-15}" x2="{pos}" y2="{y+15}" stroke="#8b5cf6" stroke-width="3"/>'
    
    svg += '</svg>'
    return svg


def svg_percentage_bar(percentage, width=300, height=50):
    """Generate SVG progress bar showing percentage"""
    bar_width = width - 40
    filled = bar_width * percentage / 100
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    # Background bar
    svg += f'<rect x="20" y="15" width="{bar_width}" height="20" fill="#e5e7eb" rx="10" stroke="#9ca3af" stroke-width="1"/>'
    
    # Filled portion
    if filled > 0:
        svg += f'<rect x="20" y="15" width="{filled}" height="20" fill="url(#grad)" rx="10"/>'
    
    # Gradient
    svg += '''<defs><linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#8b5cf6"/>
        <stop offset="100%" style="stop-color:#a78bfa"/>
    </linearGradient></defs>'''
    
    svg += '</svg>'
    return svg


def svg_grid_shaded(rows, cols, shaded_count, cell_size=30):
    """Generate SVG grid with shaded cells (for percentage)"""
    width = cols * cell_size + 20
    height = rows * cell_size + 20
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            x = 10 + c * cell_size
            y = 10 + r * cell_size
            color = '#8b5cf6' if count < shaded_count else '#f3f4f6'
            svg += f'<rect x="{x}" y="{y}" width="{cell_size-2}" height="{cell_size-2}" fill="{color}" stroke="#374151" stroke-width="1" rx="2"/>'
            count += 1
    
    svg += '</svg>'
    return svg


def svg_dice(value, size=80):
    """Generate SVG of a die showing a specific value"""
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    svg += f'<rect x="5" y="5" width="{size-10}" height="{size-10}" fill="white" stroke="#374151" stroke-width="3" rx="10"/>'
    
    dot_positions = {
        1: [(size//2, size//2)],
        2: [(size//4, size//4), (3*size//4, 3*size//4)],
        3: [(size//4, size//4), (size//2, size//2), (3*size//4, 3*size//4)],
        4: [(size//4, size//4), (3*size//4, size//4), (size//4, 3*size//4), (3*size//4, 3*size//4)],
        5: [(size//4, size//4), (3*size//4, size//4), (size//2, size//2), (size//4, 3*size//4), (3*size//4, 3*size//4)],
        6: [(size//4, size//4), (3*size//4, size//4), (size//4, size//2), (3*size//4, size//2), (size//4, 3*size//4), (3*size//4, 3*size//4)]
    }
    
    for x, y in dot_positions.get(value, []):
        svg += f'<circle cx="{x}" cy="{y}" r="6" fill="#1f2937"/>'
    
    svg += '</svg>'
    return svg


def svg_two_dice(val1, val2):
    """Generate SVG showing two dice"""
    svg = '<svg width="180" height="90" viewBox="0 0 180 90">'
    
    # First die
    svg += '<g transform="translate(5,5)">'
    svg += svg_dice(val1, 80).replace('<svg', '<svg x="0" y="0"').replace('</svg>', '')
    svg += '</g>'
    
    # Second die
    svg += '<g transform="translate(95,5)">'
    svg += svg_dice(val2, 80).replace('<svg', '<svg x="0" y="0"').replace('</svg>', '')
    svg += '</g>'
    
    svg += '</svg>'
    return svg


def svg_spinner(sections, highlighted=None, size=200):
    """Generate SVG spinner for probability"""
    cx, cy, r = size//2, size//2, size//2 - 20
    angle_per_section = 360 / len(sections)
    colors = ['#8b5cf6', '#22c55e', '#f59e0b', '#ef4444', '#3b82f6', '#ec4899', '#14b8a6', '#f97316']
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    for i, label in enumerate(sections):
        start_angle = i * angle_per_section - 90
        end_angle = (i + 1) * angle_per_section - 90
        mid_angle = (start_angle + end_angle) / 2
        
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        mid_rad = math.radians(mid_angle)
        
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        
        large_arc = 1 if angle_per_section > 180 else 0
        color = colors[i % len(colors)]
        if highlighted is not None and label == highlighted:
            color = '#fbbf24'  # Highlight color
        
        path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large_arc},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="#374151" stroke-width="2"/>'
        
        # Label
        label_r = r * 0.6
        lx = cx + label_r * math.cos(mid_rad)
        ly = cy + label_r * math.sin(mid_rad)
        svg += f'<text x="{lx}" y="{ly}" text-anchor="middle" dominant-baseline="middle" font-size="14" fill="white" font-weight="bold">{label}</text>'
    
    # Center circle and arrow
    svg += f'<circle cx="{cx}" cy="{cy}" r="8" fill="#374151"/>'
    svg += f'<polygon points="{cx},{cy-r+5} {cx-8},{cy-r+20} {cx+8},{cy-r+20}" fill="#374151"/>'
    
    svg += '</svg>'
    return svg


def svg_mixed_fraction_visual(whole, num, denom, size=250):
    """Generate SVG showing mixed fraction with whole shapes and partial"""
    shape_size = 60
    gap = 10
    total_width = (whole + 1) * (shape_size + gap) + 20
    height = shape_size + 40
    
    svg = f'<svg width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">'
    
    # Draw whole circles (fully shaded)
    for i in range(whole):
        cx = 30 + i * (shape_size + gap) + shape_size // 2
        cy = height // 2
        svg += f'<circle cx="{cx}" cy="{cy}" r="{shape_size//2}" fill="#8b5cf6" stroke="#374151" stroke-width="2"/>'
    
    # Draw partial circle (pie chart)
    if num > 0:
        cx = 30 + whole * (shape_size + gap) + shape_size // 2
        cy = height // 2
        r = shape_size // 2
        
        # Draw the full circle outline first
        svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>'
        
        # Draw shaded portions
        angle_per_slice = 360 / denom
        for i in range(num):
            start_angle = i * angle_per_slice - 90
            end_angle = (i + 1) * angle_per_slice - 90
            
            start_rad = math.radians(start_angle)
            end_rad = math.radians(end_angle)
            
            x1 = cx + r * math.cos(start_rad)
            y1 = cy + r * math.sin(start_rad)
            x2 = cx + r * math.cos(end_rad)
            y2 = cy + r * math.sin(end_rad)
            
            large_arc = 1 if angle_per_slice > 180 else 0
            path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large_arc},1 {x2},{y2} Z'
            svg += f'<path d="{path}" fill="#8b5cf6" stroke="#374151" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


# ============================================================
# QUESTION GENERATORS BY TOPIC
# ============================================================

def generate_fraction_questions():
    """Generate fraction questions across all levels"""
    questions = []
    
    # Level 1-3: Beginner - Simple unit fractions, halves, quarters
    for level in range(1, 4):
        # Pie chart questions
        for denom in [2, 3, 4]:
            for num in range(1, denom + 1):
                svg = svg_pie_chart(num, denom)
                options = generate_fraction_options(num, denom)
                questions.append({
                    'level': level,
                    'band': 'beginner',
                    'question': 'What fraction of the circle is shaded?',
                    'options': options,
                    'correct': f'{num}/{denom}',
                    'svg': svg,
                    'type': 'visual'
                })
        
        # Fraction bar questions
        for denom in [2, 4, 5]:
            for num in range(1, denom):
                svg = svg_fraction_bar(num, denom)
                options = generate_fraction_options(num, denom)
                questions.append({
                    'level': level,
                    'band': 'beginner',
                    'question': 'What fraction of the bar is shaded?',
                    'options': options,
                    'correct': f'{num}/{denom}',
                    'svg': svg,
                    'type': 'visual'
                })
        
        # Simple comparison (text)
        comparisons = [
            ('1/2', '1/4', '1/2', 'Which fraction is larger?'),
            ('1/3', '1/2', '1/2', 'Which fraction is larger?'),
            ('2/4', '1/2', 'They are equal', 'Compare these fractions:'),
        ]
        for frac1, frac2, correct, q in comparisons:
            questions.append({
                'level': level,
                'band': 'beginner',
                'question': f'{q} {frac1} or {frac2}',
                'options': [frac1, frac2, 'They are equal', 'Cannot tell'],
                'correct': correct,
                'svg': None,
                'type': 'text'
            })
    
    # Level 4-6: Intermediate - Equivalent fractions, larger denominators
    for level in range(4, 7):
        # Pie charts with more slices
        for denom in [5, 6, 8]:
            for num in range(1, denom):
                if random.random() < 0.5:  # Don't generate all
                    svg = svg_pie_chart(num, denom)
                    options = generate_fraction_options(num, denom)
                    questions.append({
                        'level': level,
                        'band': 'intermediate',
                        'question': 'What fraction of the circle is shaded?',
                        'options': options,
                        'correct': f'{num}/{denom}',
                        'svg': svg,
                        'type': 'visual'
                    })
        
        # Equivalent fraction questions
        equivalents = [
            ('2/4', '1/2', '3/4', '2/3'),
            ('3/6', '1/2', '2/3', '1/3'),
            ('4/8', '1/2', '3/8', '5/8'),
            ('2/6', '1/3', '1/2', '2/3'),
            ('6/8', '3/4', '1/2', '5/8'),
        ]
        for eq1, eq2, wrong1, wrong2 in equivalents:
            questions.append({
                'level': level,
                'band': 'intermediate',
                'question': f'Which fraction is equivalent to {eq1}?',
                'options': [eq2, wrong1, wrong2, 'None of these'],
                'correct': eq2,
                'svg': None,
                'type': 'text'
            })
        
        # Mixed to improper conversions (visual)
        mixed_conversions = [
            (1, 1, 2, '3/2'),  # 1 1/2 = 3/2
            (1, 1, 3, '4/3'),  # 1 1/3 = 4/3
            (1, 1, 4, '5/4'),  # 1 1/4 = 5/4
            (2, 1, 2, '5/2'),  # 2 1/2 = 5/2
            (1, 2, 3, '5/3'),  # 1 2/3 = 5/3
            (1, 3, 4, '7/4'),  # 1 3/4 = 7/4
            (2, 1, 3, '7/3'),  # 2 1/3 = 7/3
        ]
        for whole, num, denom, improper in mixed_conversions:
            svg = svg_mixed_fraction_visual(whole, num, denom)
            total_num = whole * denom + num
            wrong_options = generate_improper_wrong_options(total_num, denom)
            questions.append({
                'level': level,
                'band': 'intermediate',
                'question': f'The image shows {whole} {num}/{denom}. Write this as an improper fraction.',
                'options': [improper] + wrong_options[:3],
                'correct': improper,
                'svg': svg,
                'type': 'visual'
            })
    
    # Level 7-9: Advanced - Complex fractions, operations
    for level in range(7, 10):
        # Number line questions
        for denom in [4, 5, 8, 10]:
            for num in range(1, denom):
                if random.random() < 0.4:
                    value = num / denom
                    svg = svg_number_line(value)
                    options = generate_fraction_options(num, denom)
                    questions.append({
                        'level': level,
                        'band': 'advanced',
                        'question': 'What fraction is shown on the number line?',
                        'options': options,
                        'correct': f'{num}/{denom}',
                        'svg': svg,
                        'type': 'visual'
                    })
        
        # Improper to mixed conversions
        improper_to_mixed = [
            ('7/4', '1 3/4'),
            ('9/4', '2 1/4'),
            ('5/3', '1 2/3'),
            ('8/3', '2 2/3'),
            ('11/4', '2 3/4'),
            ('7/2', '3 1/2'),
            ('10/3', '3 1/3'),
            ('13/4', '3 1/4'),
            ('11/5', '2 1/5'),
        ]
        for improper, mixed in improper_to_mixed:
            wrong = generate_mixed_wrong_options(mixed)
            questions.append({
                'level': level,
                'band': 'advanced',
                'question': f'Convert {improper} to a mixed number.',
                'options': [mixed] + wrong[:3],
                'correct': mixed,
                'svg': None,
                'type': 'text'
            })
        
        # Ordering fractions
        ordering_qs = [
            (['1/4', '1/2', '3/4'], '1/4, 1/2, 3/4', 'smallest to largest'),
            (['2/3', '1/2', '3/4'], '1/2, 2/3, 3/4', 'smallest to largest'),
            (['5/6', '2/3', '1/2'], '1/2, 2/3, 5/6', 'smallest to largest'),
        ]
        for fracs, correct_order, direction in ordering_qs:
            random.shuffle(fracs)
            questions.append({
                'level': level,
                'band': 'advanced',
                'question': f'Order these fractions from {direction}: {", ".join(fracs)}',
                'options': [correct_order, ', '.join(reversed(correct_order.split(', '))), 
                           ', '.join(fracs), 'Cannot determine'],
                'correct': correct_order,
                'svg': None,
                'type': 'text'
            })
    
    # Level 10: Mastery
    # Complex visual interpretations
    for denom in [10, 12]:
        for num in range(2, denom-1, 2):
            svg = svg_pie_chart(num, denom)
            simplified = simplify_fraction(num, denom)
            options = [simplified, f'{num}/{denom}', f'{num+1}/{denom}', f'{num-1}/{denom}']
            questions.append({
                'level': 10,
                'band': 'advanced',
                'question': 'What fraction of the circle is shaded? Give your answer in simplest form.',
                'options': options,
                'correct': simplified,
                'svg': svg,
                'type': 'visual'
            })
    
    return questions


def generate_percentage_questions():
    """Generate percentage questions across all levels"""
    questions = []
    
    # Level 1-3: Beginner - Simple percentages
    for level in range(1, 4):
        # Progress bar (visual)
        for pct in [10, 20, 25, 50, 75, 100]:
            svg = svg_percentage_bar(pct)
            wrong = [pct + 10, pct - 10, pct + 25]
            wrong = [w for w in wrong if 0 <= w <= 100][:3]
            if len(wrong) < 3:
                wrong.extend([5, 15, 30][:3-len(wrong)])
            questions.append({
                'level': level,
                'band': 'beginner',
                'question': 'What percentage does this bar show?',
                'options': [f'{pct}%'] + [f'{w}%' for w in wrong],
                'correct': f'{pct}%',
                'svg': svg,
                'type': 'visual'
            })
        
        # Grid questions (10x10 = 100 squares)
        for pct in [10, 20, 25, 50]:
            svg = svg_grid_shaded(10, 10, pct)
            questions.append({
                'level': level,
                'band': 'beginner',
                'question': 'What percentage of the grid is shaded?',
                'options': [f'{pct}%', f'{pct+10}%', f'{pct-10}%' if pct > 10 else '5%', f'{100-pct}%'],
                'correct': f'{pct}%',
                'svg': svg,
                'type': 'visual'
            })
        
        # Basic conversion (text)
        conversions = [
            ('1/2', '50%'),
            ('1/4', '25%'),
            ('3/4', '75%'),
            ('1/10', '10%'),
        ]
        for frac, pct in conversions:
            questions.append({
                'level': level,
                'band': 'beginner',
                'question': f'What is {frac} as a percentage?',
                'options': [pct, '20%', '30%', '40%'],
                'correct': pct,
                'svg': None,
                'type': 'text'
            })
    
    # Level 4-6: Intermediate
    for level in range(4, 7):
        # More complex percentages
        for pct in [15, 35, 45, 60, 80]:
            svg = svg_percentage_bar(pct)
            questions.append({
                'level': level,
                'band': 'intermediate',
                'question': 'What percentage does this bar show?',
                'options': [f'{pct}%', f'{pct+5}%', f'{pct-5}%', f'{pct+15}%'],
                'correct': f'{pct}%',
                'svg': svg,
                'type': 'visual'
            })
        
        # Find percentage of amount
        percentage_of = [
            (10, 50, 5),    # 10% of 50 = 5
            (25, 80, 20),   # 25% of 80 = 20
            (50, 60, 30),   # 50% of 60 = 30
            (20, 45, 9),    # 20% of 45 = 9
            (10, 120, 12),  # 10% of 120 = 12
        ]
        for pct, total, answer in percentage_of:
            wrong = [answer + 5, answer * 2, total - answer]
            questions.append({
                'level': level,
                'band': 'intermediate',
                'question': f'What is {pct}% of {total}?',
                'options': [str(answer)] + [str(w) for w in wrong],
                'correct': str(answer),
                'svg': None,
                'type': 'text'
            })
        
        # Percentage increase/decrease (visual with before/after bars)
        changes = [
            (50, 60, 'increase', 20),   # 50 to 60 = 20% increase
            (100, 75, 'decrease', 25),  # 100 to 75 = 25% decrease
            (80, 100, 'increase', 25),  # 80 to 100 = 25% increase
        ]
        for before, after, direction, pct in changes:
            questions.append({
                'level': level,
                'band': 'intermediate',
                'question': f'A price changed from €{before} to €{after}. What is the percentage {direction}?',
                'options': [f'{pct}%', f'{pct+5}%', f'{pct-5}%', f'{pct*2}%'],
                'correct': f'{pct}%',
                'svg': None,
                'type': 'text'
            })
    
    # Level 7-9: Advanced
    for level in range(7, 10):
        # Smaller grids for harder percentages
        for rows, cols, shaded, pct in [(5, 4, 6, 30), (5, 4, 9, 45), (5, 4, 14, 70)]:
            svg = svg_grid_shaded(rows, cols, shaded)
            questions.append({
                'level': level,
                'band': 'advanced',
                'question': 'What percentage of the grid is shaded?',
                'options': [f'{pct}%', f'{pct+5}%', f'{pct-5}%', f'{100-pct}%'],
                'correct': f'{pct}%',
                'svg': svg,
                'type': 'visual'
            })
        
        # Reverse percentage problems
        reverse = [
            (20, 'is 25% of', 80),    # 20 is 25% of 80
            (15, 'is 30% of', 50),    # 15 is 30% of 50
            (24, 'is 40% of', 60),    # 24 is 40% of 60
            (18, 'is 20% of', 90),    # 18 is 20% of 90
        ]
        for part, phrase, whole in reverse:
            questions.append({
                'level': level,
                'band': 'advanced',
                'question': f'{part} {phrase} what number?',
                'options': [str(whole), str(whole + 10), str(whole - 10), str(part * 2)],
                'correct': str(whole),
                'svg': None,
                'type': 'text'
            })
        
        # Compound percentages
        compound = [
            (100, 10, 10, 121),   # 100 + 10% + 10% = 121
            (200, 20, 'then decreased by 20', 192),  # 200 + 20% - 20% = 192
        ]
        for start, pct1, action, result in compound:
            questions.append({
                'level': level,
                'band': 'advanced',
                'question': f'€{start} is increased by {pct1}%, {action}%. What is the final amount?',
                'options': [f'€{result}', f'€{result + 10}', f'€{result - 10}', f'€{start}'],
                'correct': f'€{result}',
                'svg': None,
                'type': 'text'
            })
    
    # Level 10: Mastery
    questions.append({
        'level': 10,
        'band': 'advanced',
        'question': 'A shop reduces prices by 20%, then by a further 10%. What is the total percentage reduction?',
        'options': ['28%', '30%', '25%', '32%'],
        'correct': '28%',
        'svg': None,
        'type': 'text'
    })
    
    return questions


def generate_probability_questions():
    """Generate probability questions across all levels"""
    questions = []
    
    # Level 1-3: Beginner - Basic probability with dice and spinners
    for level in range(1, 4):
        # Single die questions
        for target in range(1, 7):
            svg = svg_dice(target)
            questions.append({
                'level': level,
                'band': 'beginner',
                'question': f'A fair die is rolled. What is the probability of rolling a {target}?',
                'options': ['1/6', '1/3', '1/2', '1/4'],
                'correct': '1/6',
                'svg': svg,
                'type': 'visual'
            })
        
        # Even/odd questions
        questions.append({
            'level': level,
            'band': 'beginner',
            'question': 'What is the probability of rolling an even number on a fair die?',
            'options': ['1/2', '1/3', '1/6', '2/3'],
            'correct': '1/2',
            'svg': svg_dice(4),
            'type': 'visual'
        })
        
        # Simple spinner
        spinner_sections = ['Red', 'Blue', 'Green', 'Yellow']
        svg = svg_spinner(spinner_sections)
        questions.append({
            'level': level,
            'band': 'beginner',
            'question': 'This spinner has 4 equal sections. What is the probability of landing on Red?',
            'options': ['1/4', '1/2', '1/3', '1/6'],
            'correct': '1/4',
            'svg': svg,
            'type': 'visual'
        })
        
        # Coin flip
        questions.append({
            'level': level,
            'band': 'beginner',
            'question': 'A fair coin is flipped. What is the probability of getting heads?',
            'options': ['1/2', '1/4', '1/3', '1'],
            'correct': '1/2',
            'svg': None,
            'type': 'text'
        })
    
    # Level 4-6: Intermediate
    for level in range(4, 7):
        # Two dice sum questions
        svg = svg_two_dice(3, 4)
        questions.append({
            'level': level,
            'band': 'intermediate',
            'question': 'Two dice are rolled. How many ways can you get a sum of 7?',
            'options': ['6', '5', '4', '7'],
            'correct': '6',
            'svg': svg,
            'type': 'visual'
        })
        
        # Probability greater than
        questions.append({
            'level': level,
            'band': 'intermediate',
            'question': 'A fair die is rolled. What is the probability of rolling greater than 4?',
            'options': ['1/3', '1/2', '1/6', '2/3'],
            'correct': '1/3',
            'svg': svg_dice(5),
            'type': 'visual'
        })
        
        # Unequal spinner sections
        spinner = ['A', 'A', 'B', 'C']  # A appears twice
        svg = svg_spinner(spinner)
        questions.append({
            'level': level,
            'band': 'intermediate',
            'question': 'This spinner has 4 equal sections. Two show A. What is the probability of landing on A?',
            'options': ['1/2', '1/4', '2/3', '3/4'],
            'correct': '1/2',
            'svg': svg,
            'type': 'visual'
        })
        
        # Complementary events
        questions.append({
            'level': level,
            'band': 'intermediate',
            'question': 'The probability of rain tomorrow is 0.3. What is the probability it will NOT rain?',
            'options': ['0.7', '0.3', '0.6', '0.5'],
            'correct': '0.7',
            'svg': None,
            'type': 'text'
        })
        
        # Simple expected frequency
        questions.append({
            'level': level,
            'band': 'intermediate',
            'question': 'A coin is flipped 100 times. How many heads would you expect?',
            'options': ['50', '25', '75', '100'],
            'correct': '50',
            'svg': None,
            'type': 'text'
        })
    
    # Level 7-9: Advanced
    for level in range(7, 10):
        # Probability of sum
        sums_prob = [
            (2, '1/36'),
            (7, '1/6'),
            (12, '1/36'),
        ]
        for target_sum, prob in sums_prob:
            questions.append({
                'level': level,
                'band': 'advanced',
                'question': f'Two fair dice are rolled. What is the probability of getting a sum of {target_sum}?',
                'options': [prob, '1/12', '1/18', '1/6'],
                'correct': prob,
                'svg': svg_two_dice(1, 1),
                'type': 'visual'
            })
        
        # Conditional-style questions
        questions.append({
            'level': level,
            'band': 'advanced',
            'question': 'A bag contains 3 red and 5 blue marbles. One is picked at random. What is P(red)?',
            'options': ['3/8', '5/8', '1/2', '3/5'],
            'correct': '3/8',
            'svg': None,
            'type': 'text'
        })
        
        # Expected value
        questions.append({
            'level': level,
            'band': 'advanced',
            'question': 'A die is rolled 60 times. How many times would you expect to roll a 6?',
            'options': ['10', '6', '12', '15'],
            'correct': '10',
            'svg': svg_dice(6),
            'type': 'visual'
        })
        
        # Sample space
        questions.append({
            'level': level,
            'band': 'advanced',
            'question': 'Two coins are flipped. How many outcomes are in the sample space?',
            'options': ['4', '2', '3', '6'],
            'correct': '4',
            'svg': None,
            'type': 'text'
        })
    
    # Level 10: Mastery
    questions.append({
        'level': 10,
        'band': 'advanced',
        'question': 'Two fair dice are rolled. What is the probability that both show the same number?',
        'options': ['1/6', '1/12', '1/3', '1/36'],
        'correct': '1/6',
        'svg': svg_two_dice(4, 4),
        'type': 'visual'
    })
    
    questions.append({
        'level': 10,
        'band': 'advanced',
        'question': 'A bag has 4 red and 6 blue balls. Two are picked without replacement. What is P(both red)?',
        'options': ['2/15', '4/25', '1/6', '2/10'],
        'correct': '2/15',
        'svg': None,
        'type': 'text'
    })
    
    return questions


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def generate_fraction_options(num, denom):
    """Generate plausible wrong answers for a fraction question"""
    correct = f'{num}/{denom}'
    options = [correct]
    
    # Add wrong options
    wrongs = [
        f'{denom-num}/{denom}',  # Complement
        f'{num}/{denom+1}',      # Wrong denominator
        f'{num+1}/{denom}',      # Wrong numerator
        f'{num}/{denom-1}' if denom > 2 else f'{num}/{denom+2}',
    ]
    
    for w in wrongs:
        if w != correct and w not in options and len(options) < 4:
            options.append(w)
    
    while len(options) < 4:
        options.append(f'{random.randint(1, 5)}/{random.randint(2, 8)}')
    
    random.shuffle(options)
    return options[:4]


def generate_improper_wrong_options(numerator, denominator):
    """Generate wrong answers for improper fraction conversions"""
    wrongs = [
        f'{numerator + 1}/{denominator}',
        f'{numerator - 1}/{denominator}',
        f'{numerator}/{denominator + 1}',
        f'{denominator}/{numerator}',
    ]
    return wrongs


def generate_mixed_wrong_options(correct_mixed):
    """Generate wrong answers for mixed number conversions"""
    parts = correct_mixed.split()
    whole = int(parts[0])
    frac = parts[1]
    num, denom = map(int, frac.split('/'))
    
    wrongs = [
        f'{whole + 1} {num}/{denom}',
        f'{whole} {num + 1}/{denom}' if num + 1 < denom else f'{whole} 1/{denom}',
        f'{whole - 1} {denom - num}/{denom}' if whole > 0 else f'{whole + 2} {num}/{denom}',
    ]
    return wrongs


def simplify_fraction(num, denom):
    """Return simplified fraction string"""
    from math import gcd
    g = gcd(num, denom)
    return f'{num // g}/{denom // g}'


# ============================================================
# DATABASE OPERATIONS
# ============================================================

def insert_questions(questions, topic):
    """Insert questions into the database"""
    conn = get_db()
    cursor = conn.cursor()
    
    inserted = 0
    for q in questions:
        options = q['options']
        correct_letter = 'A'
        for i, opt in enumerate(options):
            if opt == q['correct']:
                correct_letter = ['A', 'B', 'C', 'D'][i]
                break
        
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, image_svg, is_active, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
            ''', (
                topic,
                q['question'],
                options[0] if len(options) > 0 else '',
                options[1] if len(options) > 1 else '',
                options[2] if len(options) > 2 else '',
                options[3] if len(options) > 3 else '',
                correct_letter,
                '',  # explanation
                q['level'],
                q['band'],
                q['type'],
                q['svg'],
                datetime.now().isoformat()
            ))
            inserted += 1
        except Exception as e:
            print(f"Error inserting question: {e}")
    
    conn.commit()
    conn.close()
    return inserted


def show_stats():
    """Show current question statistics"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT COUNT(*) FROM questions_adaptive")
        total = cursor.fetchone()[0]
        print(f"\n📊 Total questions in database: {total}")
        
        cursor.execute("""
            SELECT topic, difficulty_level, question_type, COUNT(*) 
            FROM questions_adaptive 
            GROUP BY topic, difficulty_level, question_type
            ORDER BY topic, difficulty_level
        """)
        
        print("\nBreakdown by topic, level, and type:")
        for row in cursor.fetchall():
            print(f"  {row[0]} | Level {row[1]} | {row[2]}: {row[3]} questions")
        
        # Visual percentage
        cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE question_type = 'visual'")
        visual = cursor.fetchone()[0]
        if total > 0:
            pct = visual / total * 100
            print(f"\n📈 Visual questions: {visual}/{total} ({pct:.1f}%)")
    except Exception as e:
        print(f"Error showing stats: {e}")
    
    conn.close()


def main():
    print("=" * 60)
    print("ADAPTIVE QUIZ QUESTION GENERATOR")
    print("=" * 60)
    
    # Generate questions for each topic
    print("\n📝 Generating Fractions questions...")
    fractions_qs = generate_fraction_questions()
    count = insert_questions(fractions_qs, 'fractions')
    print(f"   Inserted {count} questions")
    
    print("\n📝 Generating Percentages questions...")
    percentages_qs = generate_percentage_questions()
    count = insert_questions(percentages_qs, 'percentages')
    print(f"   Inserted {count} questions")
    
    print("\n📝 Generating Probability questions...")
    probability_qs = generate_probability_questions()
    count = insert_questions(probability_qs, 'probability')
    print(f"   Inserted {count} questions")
    
    # Show stats
    show_stats()
    
    print("\n✅ Done!")


if __name__ == '__main__':
    main()
