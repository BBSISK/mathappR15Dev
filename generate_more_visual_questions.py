#!/usr/bin/env python3
"""
BOOST VISUAL QUESTIONS TO 75%
Generates additional visual questions for Fractions, Percentages, Probability
"""

import sqlite3
import random
import math
from datetime import datetime

DB_PATH = 'instance/mathquiz.db'

def get_db():
    return sqlite3.connect(DB_PATH)

# ============================================================
# SVG GENERATORS (Enhanced with more variety)
# ============================================================

def svg_pie_chart(num_shaded, total_slices, size=200):
    """Generate SVG pie chart with shaded slices"""
    cx, cy, r = size//2, size//2, size//2 - 10
    angle_per_slice = 360 / total_slices
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    for i in range(total_slices):
        start_angle = i * angle_per_slice - 90
        end_angle = (i + 1) * angle_per_slice - 90
        
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        
        large_arc = 1 if angle_per_slice > 180 else 0
        color = '#8b5cf6' if i < num_shaded else '#e5e7eb'
        
        path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large_arc},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="#374151" stroke-width="2"/>'
    
    svg += f'<circle cx="{cx}" cy="{cy}" r="4" fill="#374151"/>'
    svg += '</svg>'
    return svg


def svg_fraction_bar(num_shaded, total_parts, width=300, height=60):
    """Generate SVG fraction bar"""
    part_width = (width - 20) / total_parts
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    svg += f'<rect x="10" y="10" width="{width-20}" height="{height-20}" fill="none" stroke="#374151" stroke-width="2" rx="5"/>'
    
    for i in range(total_parts):
        x = 10 + i * part_width
        color = '#8b5cf6' if i < num_shaded else '#f3f4f6'
        svg += f'<rect x="{x}" y="10" width="{part_width}" height="{height-20}" fill="{color}" stroke="#374151" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def svg_rectangle_grid(rows, cols, shaded, cell_size=40):
    """Rectangle divided into grid cells"""
    width = cols * cell_size + 20
    height = rows * cell_size + 20
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            x = 10 + c * cell_size
            y = 10 + r * cell_size
            color = '#8b5cf6' if count < shaded else '#f3f4f6'
            svg += f'<rect x="{x}" y="{y}" width="{cell_size-2}" height="{cell_size-2}" fill="{color}" stroke="#374151" stroke-width="1"/>'
            count += 1
    
    svg += '</svg>'
    return svg


def svg_number_line(value, min_val=0, max_val=1, width=350, height=80, show_fractions=None):
    """Number line with point marked"""
    margin = 40
    line_width = width - 2 * margin
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    y = height // 2
    svg += f'<line x1="{margin}" y1="{y}" x2="{width-margin}" y2="{y}" stroke="#374151" stroke-width="3"/>'
    
    # End markers
    svg += f'<line x1="{margin}" y1="{y-10}" x2="{margin}" y2="{y+10}" stroke="#374151" stroke-width="2"/>'
    svg += f'<text x="{margin}" y="{y+25}" text-anchor="middle" font-size="14" fill="#374151">{min_val}</text>'
    
    svg += f'<line x1="{width-margin}" y1="{y-10}" x2="{width-margin}" y2="{y+10}" stroke="#374151" stroke-width="2"/>'
    svg += f'<text x="{width-margin}" y="{y+25}" text-anchor="middle" font-size="14" fill="#374151">{max_val}</text>'
    
    # Show fraction markers if specified
    if show_fractions:
        for frac_val, label in show_fractions:
            pos = margin + frac_val * line_width
            svg += f'<line x1="{pos}" y1="{y-6}" x2="{pos}" y2="{y+6}" stroke="#9ca3af" stroke-width="1"/>'
            svg += f'<text x="{pos}" y="{y+22}" text-anchor="middle" font-size="10" fill="#9ca3af">{label}</text>'
    
    # Value marker
    pos = margin + (value - min_val) / (max_val - min_val) * line_width
    svg += f'<circle cx="{pos}" cy="{y}" r="8" fill="#8b5cf6" stroke="#5b21b6" stroke-width="2"/>'
    
    svg += '</svg>'
    return svg


def svg_percentage_bar(percentage, width=300, height=50):
    """Progress bar for percentage"""
    bar_width = width - 40
    filled = bar_width * percentage / 100
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    svg += f'<rect x="20" y="15" width="{bar_width}" height="20" fill="#e5e7eb" rx="10" stroke="#9ca3af" stroke-width="1"/>'
    
    if filled > 0:
        svg += f'<rect x="20" y="15" width="{filled}" height="20" fill="#8b5cf6" rx="10"/>'
    
    svg += '</svg>'
    return svg


def svg_grid_100(shaded_count, cell_size=20):
    """10x10 grid for percentages"""
    size = 10 * cell_size + 20
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    count = 0
    for r in range(10):
        for c in range(10):
            x = 10 + c * cell_size
            y = 10 + r * cell_size
            color = '#8b5cf6' if count < shaded_count else '#f3f4f6'
            svg += f'<rect x="{x}" y="{y}" width="{cell_size-1}" height="{cell_size-1}" fill="{color}" stroke="#d1d5db" stroke-width="0.5"/>'
            count += 1
    
    svg += '</svg>'
    return svg


def svg_dice(value, size=80):
    """Single die"""
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
    """Two dice side by side"""
    svg = '<svg width="180" height="90" viewBox="0 0 180 90">'
    
    # First die
    die1 = svg_dice(val1, 80)
    svg += f'<g transform="translate(5,5)">{die1[die1.find(">")+1:die1.rfind("<")]}</g>'
    
    # Second die  
    die2 = svg_dice(val2, 80)
    svg += f'<g transform="translate(95,5)">{die2[die2.find(">")+1:die2.rfind("<")]}</g>'
    
    svg += '</svg>'
    return svg


def svg_spinner(sections, size=180):
    """Spinner with equal sections"""
    cx, cy, r = size//2, size//2, size//2 - 15
    n = len(sections)
    angle_per = 360 / n
    colors = ['#ef4444', '#3b82f6', '#22c55e', '#f59e0b', '#8b5cf6', '#ec4899', '#14b8a6', '#f97316']
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    for i, label in enumerate(sections):
        start = i * angle_per - 90
        end = (i + 1) * angle_per - 90
        mid = (start + end) / 2
        
        x1 = cx + r * math.cos(math.radians(start))
        y1 = cy + r * math.sin(math.radians(start))
        x2 = cx + r * math.cos(math.radians(end))
        y2 = cy + r * math.sin(math.radians(end))
        
        large = 1 if angle_per > 180 else 0
        color = colors[i % len(colors)]
        
        path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="#374151" stroke-width="2"/>'
        
        # Label
        lr = r * 0.6
        lx = cx + lr * math.cos(math.radians(mid))
        ly = cy + lr * math.sin(math.radians(mid))
        svg += f'<text x="{lx}" y="{ly}" text-anchor="middle" dominant-baseline="middle" font-size="12" fill="white" font-weight="bold">{label}</text>'
    
    svg += f'<circle cx="{cx}" cy="{cy}" r="6" fill="#374151"/>'
    svg += '</svg>'
    return svg


def svg_bag_marbles(red, blue, green=0, size=150):
    """Bag with colored marbles"""
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    # Bag outline
    svg += f'<path d="M 30 40 Q 20 50 25 120 Q 30 140 75 140 Q 120 140 125 120 Q 130 50 120 40 Q 100 30 75 30 Q 50 30 30 40 Z" fill="#d4a574" stroke="#8b6914" stroke-width="3"/>'
    svg += f'<ellipse cx="75" cy="35" rx="45" ry="10" fill="#c4956a" stroke="#8b6914" stroke-width="2"/>'
    
    # Draw marbles
    marble_colors = ['#ef4444'] * red + ['#3b82f6'] * blue + ['#22c55e'] * green
    positions = [(45, 70), (75, 65), (105, 70), (55, 95), (95, 95), (75, 115), (60, 80), (90, 80)]
    
    for i, color in enumerate(marble_colors[:8]):
        if i < len(positions):
            x, y = positions[i]
            svg += f'<circle cx="{x}" cy="{y}" r="12" fill="{color}" stroke="#374151" stroke-width="1"/>'
            svg += f'<circle cx="{x-4}" cy="{y-4}" r="3" fill="white" opacity="0.6"/>'
    
    svg += '</svg>'
    return svg


def svg_cards(cards, width=200):
    """Playing cards visual"""
    card_width = 40
    height = 70
    
    svg = f'<svg width="{width}" height="{height + 20}" viewBox="0 0 {width} {height + 20}">'
    
    for i, card in enumerate(cards):
        x = 10 + i * 35
        color = '#ef4444' if card in ['♥', '♦'] else '#1f2937'
        svg += f'<rect x="{x}" y="10" width="{card_width}" height="{height}" fill="white" stroke="#374151" stroke-width="2" rx="5"/>'
        svg += f'<text x="{x + card_width//2}" y="{10 + height//2 + 8}" text-anchor="middle" font-size="24" fill="{color}">{card}</text>'
    
    svg += '</svg>'
    return svg


def svg_coin():
    """Coin visual"""
    svg = '<svg width="80" height="80" viewBox="0 0 80 80">'
    svg += '<circle cx="40" cy="40" r="35" fill="#fbbf24" stroke="#d97706" stroke-width="3"/>'
    svg += '<circle cx="40" cy="40" r="28" fill="none" stroke="#d97706" stroke-width="1"/>'
    svg += '<text x="40" y="48" text-anchor="middle" font-size="20" fill="#92400e" font-weight="bold">H</text>'
    svg += '</svg>'
    return svg


def svg_mixed_number(whole, num, denom, shape_size=50):
    """Visual representation of mixed number"""
    total_width = (whole + 1) * (shape_size + 10) + 20
    height = shape_size + 20
    
    svg = f'<svg width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">'
    
    # Whole shapes (fully shaded circles)
    for i in range(whole):
        cx = 20 + i * (shape_size + 10) + shape_size // 2
        cy = height // 2
        svg += f'<circle cx="{cx}" cy="{cy}" r="{shape_size//2}" fill="#8b5cf6" stroke="#374151" stroke-width="2"/>'
    
    # Partial shape
    if num > 0:
        cx = 20 + whole * (shape_size + 10) + shape_size // 2
        cy = height // 2
        r = shape_size // 2
        
        svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e5e7eb" stroke="#374151" stroke-width="2"/>'
        
        # Shaded portions
        angle_per = 360 / denom
        for i in range(num):
            start = i * angle_per - 90
            end = (i + 1) * angle_per - 90
            
            x1 = cx + r * math.cos(math.radians(start))
            y1 = cy + r * math.sin(math.radians(start))
            x2 = cx + r * math.cos(math.radians(end))
            y2 = cy + r * math.sin(math.radians(end))
            
            large = 1 if angle_per > 180 else 0
            path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large},1 {x2},{y2} Z'
            svg += f'<path d="{path}" fill="#8b5cf6" stroke="#374151" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


# ============================================================
# QUESTION GENERATORS - MORE VISUAL
# ============================================================

def generate_fraction_visual_questions():
    """Generate LOTS of visual fraction questions"""
    questions = []
    
    # Pie charts - many variations
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        # Different denominators by level
        if level <= 3:
            denoms = [2, 3, 4]
        elif level <= 6:
            denoms = [4, 5, 6, 8]
        else:
            denoms = [6, 8, 10, 12]
        
        for denom in denoms:
            for num in range(1, denom):
                svg = svg_pie_chart(num, denom)
                correct = f'{num}/{denom}'
                
                # Generate distractors
                options = [correct]
                options.append(f'{denom-num}/{denom}')  # Complement
                options.append(f'{num}/{denom+1}' if denom < 12 else f'{num}/{denom-1}')
                options.append(f'{num+1}/{denom}' if num+1 < denom else f'{num-1}/{denom}')
                
                questions.append({
                    'level': level,
                    'band': band,
                    'question': 'What fraction of the circle is shaded?',
                    'options': options[:4],
                    'correct': correct,
                    'svg': svg,
                    'type': 'visual'
                })
    
    # Fraction bars
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        if level <= 3:
            denoms = [2, 3, 4, 5]
        elif level <= 6:
            denoms = [5, 6, 8, 10]
        else:
            denoms = [8, 10, 12]
        
        for denom in denoms:
            for num in range(1, denom):
                svg = svg_fraction_bar(num, denom)
                correct = f'{num}/{denom}'
                
                options = [correct]
                options.append(f'{denom-num}/{denom}')
                options.append(f'{num}/{denom+2}')
                options.append(f'{num+1}/{denom}' if num+1 < denom else f'1/{denom}')
                
                questions.append({
                    'level': level,
                    'band': band,
                    'question': 'What fraction of the bar is shaded?',
                    'options': options[:4],
                    'correct': correct,
                    'svg': svg,
                    'type': 'visual'
                })
    
    # Rectangle grids
    grids = [
        (2, 3, 'beginner'), (2, 4, 'beginner'), (2, 5, 'intermediate'),
        (3, 4, 'intermediate'), (3, 5, 'advanced'), (4, 5, 'advanced')
    ]
    
    for rows, cols, band in grids:
        total = rows * cols
        level = 2 if band == 'beginner' else (5 if band == 'intermediate' else 8)
        
        for shaded in range(1, total):
            svg = svg_rectangle_grid(rows, cols, shaded)
            correct = f'{shaded}/{total}'
            
            # Simplify if possible
            from math import gcd
            g = gcd(shaded, total)
            simplified = f'{shaded//g}/{total//g}'
            
            options = [correct]
            if simplified != correct:
                questions.append({
                    'level': level + 1,
                    'band': band,
                    'question': 'What fraction of the rectangle is shaded? Give your answer in simplest form.',
                    'options': [simplified, correct, f'{total-shaded}/{total}', f'{shaded+1}/{total}'],
                    'correct': simplified,
                    'svg': svg,
                    'type': 'visual'
                })
            
            questions.append({
                'level': level,
                'band': band,
                'question': 'What fraction of the rectangle is shaded?',
                'options': [correct, f'{total-shaded}/{total}', f'{shaded}/{total+1}', f'{shaded+1}/{total}'],
                'correct': correct,
                'svg': svg,
                'type': 'visual'
            })
    
    # Number line questions
    for level in range(4, 11):
        band = 'intermediate' if level <= 6 else 'advanced'
        
        for denom in [4, 5, 8, 10]:
            for num in range(1, denom):
                value = num / denom
                svg = svg_number_line(value)
                correct = f'{num}/{denom}'
                
                options = [correct, f'{denom-num}/{denom}', f'{num}/{denom+1}', f'{num+1}/{denom}']
                
                questions.append({
                    'level': level,
                    'band': band,
                    'question': 'What fraction is marked on the number line?',
                    'options': options[:4],
                    'correct': correct,
                    'svg': svg,
                    'type': 'visual'
                })
    
    # Mixed number visuals
    mixed_nums = [
        (1, 1, 2, 'intermediate'), (1, 1, 3, 'intermediate'), (1, 1, 4, 'intermediate'),
        (1, 2, 3, 'intermediate'), (1, 3, 4, 'intermediate'),
        (2, 1, 2, 'advanced'), (2, 1, 3, 'advanced'), (2, 1, 4, 'advanced'),
        (2, 2, 3, 'advanced'), (2, 3, 4, 'advanced'),
    ]
    
    for whole, num, denom, band in mixed_nums:
        level = 5 if band == 'intermediate' else 8
        svg = svg_mixed_number(whole, num, denom)
        
        correct_mixed = f'{whole} {num}/{denom}'
        improper_num = whole * denom + num
        correct_improper = f'{improper_num}/{denom}'
        
        # Mixed to improper
        questions.append({
            'level': level,
            'band': band,
            'question': f'The picture shows a mixed number. What is it as an improper fraction?',
            'options': [correct_improper, f'{improper_num+1}/{denom}', f'{improper_num-1}/{denom}', f'{improper_num}/{denom+1}'],
            'correct': correct_improper,
            'svg': svg,
            'type': 'visual'
        })
        
        # What is the mixed number
        questions.append({
            'level': level - 1,
            'band': band,
            'question': 'What mixed number does the picture show?',
            'options': [correct_mixed, f'{whole+1} {num}/{denom}', f'{whole} {num+1}/{denom}' if num+1 < denom else f'{whole} 1/{denom}', f'{whole-1} {denom-num}/{denom}' if whole > 0 else f'{whole+1} 1/{denom}'],
            'correct': correct_mixed,
            'svg': svg,
            'type': 'visual'
        })
    
    return questions


def generate_percentage_visual_questions():
    """Generate LOTS of visual percentage questions"""
    questions = []
    
    # 100-grid for percentages
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        if level <= 3:
            percentages = [10, 20, 25, 50, 75]
        elif level <= 6:
            percentages = [5, 15, 30, 35, 40, 45, 55, 60, 65, 70, 80, 85, 90, 95]
        else:
            percentages = [12, 18, 22, 28, 32, 38, 42, 48, 52, 58, 62, 68, 72, 78, 82, 88]
        
        for pct in percentages:
            svg = svg_grid_100(pct)
            correct = f'{pct}%'
            
            wrongs = [f'{pct+5}%', f'{pct-5}%' if pct >= 5 else f'{pct+10}%', f'{100-pct}%']
            
            questions.append({
                'level': level,
                'band': band,
                'question': 'What percentage of the grid is shaded?',
                'options': [correct] + wrongs[:3],
                'correct': correct,
                'svg': svg,
                'type': 'visual'
            })
    
    # Progress bars
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        if level <= 3:
            percentages = [10, 20, 25, 50, 75, 100]
        elif level <= 6:
            percentages = [15, 30, 35, 40, 45, 55, 60, 65, 70, 80, 85, 90]
        else:
            percentages = [5, 12, 18, 22, 28, 33, 37, 42, 48, 52, 58, 63, 67, 72, 78, 83, 87, 92]
        
        for pct in percentages:
            svg = svg_percentage_bar(pct)
            correct = f'{pct}%'
            
            wrongs = [f'{pct+10}%', f'{pct-10}%' if pct >= 10 else f'{pct+15}%', f'{pct+5}%']
            
            questions.append({
                'level': level,
                'band': band,
                'question': 'What percentage is shown on this bar?',
                'options': [correct] + wrongs[:3],
                'correct': correct,
                'svg': svg,
                'type': 'visual'
            })
    
    # Smaller grids for harder percentages
    smaller_grids = [
        (5, 4, 20, 'intermediate'),  # 5x4 = 20 squares
        (4, 5, 20, 'intermediate'),
        (5, 5, 25, 'advanced'),
    ]
    
    for rows, cols, total, band in smaller_grids:
        level = 5 if band == 'intermediate' else 8
        
        for shaded in range(1, total):
            pct = int(shaded / total * 100)
            svg = svg_rectangle_grid(rows, cols, shaded, 35)
            correct = f'{pct}%'
            
            questions.append({
                'level': level,
                'band': band,
                'question': 'What percentage of this grid is shaded?',
                'options': [correct, f'{pct+5}%', f'{pct-5}%' if pct >= 5 else f'{pct+10}%', f'{100-pct}%'],
                'correct': correct,
                'svg': svg,
                'type': 'visual'
            })
    
    return questions


def generate_probability_visual_questions():
    """Generate LOTS of visual probability questions"""
    questions = []
    
    # Dice questions - comprehensive
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        # Rolling specific numbers
        for target in range(1, 7):
            svg = svg_dice(target)
            questions.append({
                'level': level,
                'band': band,
                'question': f'A fair die is rolled. What is the probability of rolling a {target}?',
                'options': ['1/6', '1/3', '1/2', '1/4'],
                'correct': '1/6',
                'svg': svg,
                'type': 'visual'
            })
        
        # Rolling less than / greater than
        for threshold in [3, 4, 5]:
            svg = svg_dice(threshold)
            
            less_than = threshold - 1
            greater_than = 6 - threshold
            
            questions.append({
                'level': level,
                'band': band,
                'question': f'What is the probability of rolling less than {threshold}?',
                'options': [f'{less_than}/6', f'{threshold}/6', '1/2', '1/6'],
                'correct': f'{less_than}/6',
                'svg': svg,
                'type': 'visual'
            })
    
    # Two dice questions
    for level in range(4, 11):
        band = 'intermediate' if level <= 6 else 'advanced'
        
        # Various sums
        sum_probs = [
            (2, '1/36'), (3, '2/36'), (4, '3/36'), (5, '4/36'), (6, '5/36'),
            (7, '6/36'), (8, '5/36'), (9, '4/36'), (10, '3/36'), (11, '2/36'), (12, '1/36')
        ]
        
        for target_sum, prob in sum_probs:
            # Find a dice combination that makes this sum
            d1 = min(6, max(1, target_sum - 3))
            d2 = target_sum - d1
            if 1 <= d2 <= 6:
                svg = svg_two_dice(d1, d2)
                
                questions.append({
                    'level': level,
                    'band': band,
                    'question': f'Two fair dice are rolled. What is the probability of getting a sum of {target_sum}?',
                    'options': [prob, '1/12', '1/6', '1/36'],
                    'correct': prob,
                    'svg': svg,
                    'type': 'visual'
                })
    
    # Spinner questions
    spinner_configs = [
        (['R', 'B', 'G', 'Y'], '1/4', 'beginner'),
        (['R', 'R', 'B', 'B'], '1/2', 'beginner'),
        (['1', '2', '3', '4', '5', '6'], '1/6', 'intermediate'),
        (['R', 'R', 'R', 'B', 'G', 'Y'], '1/2', 'intermediate'),
        (['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'], '3/8', 'advanced'),
    ]
    
    for sections, prob, band in spinner_configs:
        level = 2 if band == 'beginner' else (5 if band == 'intermediate' else 8)
        svg = svg_spinner(sections)
        target = sections[0]
        
        questions.append({
            'level': level,
            'band': band,
            'question': f'The spinner has {len(sections)} equal sections. What is the probability of landing on {target}?',
            'options': [prob, '1/4', '1/2', '1/6'],
            'correct': prob,
            'svg': svg,
            'type': 'visual'
        })
    
    # Marble bag questions
    marble_configs = [
        (3, 1, 0, '3/4', 'beginner'),
        (2, 2, 0, '1/2', 'beginner'),
        (3, 5, 0, '3/8', 'intermediate'),
        (4, 2, 2, '1/2', 'intermediate'),
        (2, 3, 5, '1/5', 'advanced'),
    ]
    
    for red, blue, green, prob, band in marble_configs:
        level = 2 if band == 'beginner' else (5 if band == 'intermediate' else 8)
        svg = svg_bag_marbles(red, blue, green)
        total = red + blue + green
        
        questions.append({
            'level': level,
            'band': band,
            'question': f'A bag contains {red} red, {blue} blue{", and " + str(green) + " green" if green else ""} marbles. What is the probability of picking a red marble?',
            'options': [prob, f'{blue}/{total}', '1/2', f'{red+1}/{total}'],
            'correct': prob,
            'svg': svg,
            'type': 'visual'
        })
    
    # Card questions
    for level in range(3, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        svg = svg_cards(['♠', '♥', '♦', '♣'])
        
        questions.append({
            'level': level,
            'band': band,
            'question': 'A card is picked at random from these 4 cards. What is the probability of picking a red card (♥ or ♦)?',
            'options': ['1/2', '1/4', '2/3', '3/4'],
            'correct': '1/2',
            'svg': svg,
            'type': 'visual'
        })
    
    # Coin questions
    for level in range(1, 4):
        svg = svg_coin()
        
        questions.append({
            'level': level,
            'band': 'beginner',
            'question': 'A fair coin is flipped. What is the probability of getting heads?',
            'options': ['1/2', '1/4', '1/3', '1'],
            'correct': '1/2',
            'svg': svg,
            'type': 'visual'
        })
    
    return questions


# ============================================================
# DATABASE OPERATIONS
# ============================================================

def insert_questions(questions, topic):
    """Insert questions into database"""
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
                '',
                q['level'],
                q['band'],
                q['type'],
                q['svg'],
                datetime.now().isoformat()
            ))
            inserted += 1
        except Exception as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    return inserted


def show_stats():
    """Show statistics"""
    conn = get_db()
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("VISUAL QUESTION STATISTICS")
    print("="*60)
    
    # By topic
    cursor.execute("""
        SELECT topic,
               COUNT(*) as total,
               SUM(CASE WHEN question_type = 'visual' THEN 1 ELSE 0 END) as visual
        FROM questions_adaptive
        WHERE is_active = 1 AND topic IN ('fractions', 'percentages', 'probability')
        GROUP BY topic
    """)
    
    grand_total = 0
    grand_visual = 0
    
    for topic, total, visual in cursor.fetchall():
        pct = (visual / total * 100) if total > 0 else 0
        status = "✅" if pct >= 75 else "⚠️"
        print(f"\n{topic}:")
        print(f"  Total: {total}, Visual: {visual} ({pct:.1f}%) {status}")
        grand_total += total
        grand_visual += visual
    
    if grand_total > 0:
        overall_pct = grand_visual / grand_total * 100
        print(f"\n{'='*40}")
        print(f"OVERALL (3 BETA topics): {grand_visual}/{grand_total} = {overall_pct:.1f}% visual")
        if overall_pct >= 75:
            print("✅ TARGET MET!")
        else:
            needed = int(grand_total * 0.75) - grand_visual
            print(f"⚠️  Need {needed} more visual questions to reach 75%")
    
    conn.close()


def main():
    print("="*60)
    print("BOOSTING VISUAL QUESTIONS TO 75%")
    print("="*60)
    
    print("\n📊 Generating visual Fractions questions...")
    fractions = generate_fraction_visual_questions()
    count = insert_questions(fractions, 'fractions')
    print(f"   Added {count} visual fraction questions")
    
    print("\n📊 Generating visual Percentages questions...")
    percentages = generate_percentage_visual_questions()
    count = insert_questions(percentages, 'percentages')
    print(f"   Added {count} visual percentage questions")
    
    print("\n📊 Generating visual Probability questions...")
    probability = generate_probability_visual_questions()
    count = insert_questions(probability, 'probability')
    print(f"   Added {count} visual probability questions")
    
    show_stats()
    print("\n✅ Done!")


if __name__ == '__main__':
    main()
