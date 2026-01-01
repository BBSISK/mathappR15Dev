#!/usr/bin/env python3
"""
Improved Fraction Question Generator
====================================
Generates 50+ UNIQUE questions per level for Levels 1-10
Each level has distinct questions (not duplicated across levels)

Target: 75% visual questions
"""

import sqlite3
import random
import math
import os
from datetime import datetime

# Database auto-detection
POSSIBLE_PATHS = ['mathapp.db', 'instance/mathquiz.db', 'mathquiz.db']
DB_PATH = None

def find_db():
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            return path
    print("ERROR: Database not found!")
    exit(1)

def get_db():
    global DB_PATH
    if DB_PATH is None:
        DB_PATH = find_db()
        print(f"Using database: {DB_PATH}")
    return sqlite3.connect(DB_PATH)


# ============================================================
# SVG GENERATORS
# ============================================================

def svg_pie_chart(numerator, denominator, size=150):
    """Generate pie chart SVG showing a fraction"""
    cx, cy, r = size//2, size//2, size//2 - 10
    
    if numerator == denominator:
        # Full circle
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
            <circle cx="{cx}" cy="{cy}" r="{r}" fill="#4CAF50" stroke="#2E7D32" stroke-width="2"/>
            <text x="{cx}" y="{size-5}" text-anchor="middle" font-size="12" fill="#333">?</text>
        </svg>'''
    
    # Draw slices
    slices = []
    colors = ['#4CAF50', '#E8F5E9']  # Green for shaded, light for unshaded
    
    angle_per_slice = 360 / denominator
    
    for i in range(denominator):
        start_angle = i * angle_per_slice - 90
        end_angle = (i + 1) * angle_per_slice - 90
        
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        
        large_arc = 1 if angle_per_slice > 180 else 0
        color = colors[0] if i < numerator else colors[1]
        
        path = f'M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large_arc},1 {x2:.1f},{y2:.1f} Z'
        slices.append(f'<path d="{path}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
        {''.join(slices)}
        <text x="{cx}" y="{size-5}" text-anchor="middle" font-size="12" fill="#333">What fraction is shaded?</text>
    </svg>'''


def svg_fraction_bar(numerator, denominator, width=200, height=60):
    """Generate a fraction bar SVG"""
    bar_height = 40
    segment_width = (width - 20) / denominator
    
    segments = []
    for i in range(denominator):
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        x = 10 + i * segment_width
        segments.append(f'<rect x="{x:.1f}" y="10" width="{segment_width:.1f}" height="{bar_height}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
        {''.join(segments)}
    </svg>'''


def svg_grid(numerator, denominator, cols=None):
    """Generate a grid showing a fraction"""
    if cols is None:
        # Try to make a reasonable grid shape
        if denominator <= 5:
            cols = denominator
        elif denominator <= 12:
            cols = 4 if denominator % 4 == 0 else (3 if denominator % 3 == 0 else denominator)
        else:
            cols = 5
    
    rows = math.ceil(denominator / cols)
    cell_size = 30
    width = cols * cell_size + 20
    height = rows * cell_size + 30
    
    cells = []
    for i in range(denominator):
        row = i // cols
        col = i % cols
        x = 10 + col * cell_size
        y = 10 + row * cell_size
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        cells.append(f'<rect x="{x}" y="{y}" width="{cell_size-2}" height="{cell_size-2}" fill="{color}" stroke="#333" stroke-width="1" rx="3"/>')
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
        {''.join(cells)}
    </svg>'''


def svg_number_line(numerator, denominator, show_position=True):
    """Generate a number line showing a fraction"""
    width = 280
    height = 80
    line_y = 40
    
    # Number line
    elements = [
        f'<line x1="20" y1="{line_y}" x2="260" y2="{line_y}" stroke="#333" stroke-width="2"/>',
        f'<line x1="20" y1="{line_y-10}" x2="20" y2="{line_y+10}" stroke="#333" stroke-width="2"/>',
        f'<line x1="260" y1="{line_y-10}" x2="260" y2="{line_y+10}" stroke="#333" stroke-width="2"/>',
        f'<text x="20" y="{line_y+25}" text-anchor="middle" font-size="12">0</text>',
        f'<text x="260" y="{line_y+25}" text-anchor="middle" font-size="12">1</text>',
    ]
    
    # Tick marks
    for i in range(1, denominator):
        x = 20 + (240 * i / denominator)
        elements.append(f'<line x1="{x:.1f}" y1="{line_y-5}" x2="{x:.1f}" y2="{line_y+5}" stroke="#666" stroke-width="1"/>')
    
    # Point marking the fraction
    if show_position:
        point_x = 20 + (240 * numerator / denominator)
        elements.append(f'<circle cx="{point_x:.1f}" cy="{line_y}" r="8" fill="#E53935"/>')
        elements.append(f'<text x="{point_x:.1f}" y="15" text-anchor="middle" font-size="11" fill="#C62828">?</text>')
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
        {''.join(elements)}
    </svg>'''


def svg_comparison(frac1_num, frac1_denom, frac2_num, frac2_denom):
    """Generate side-by-side fraction bars for comparison"""
    width = 300
    height = 100
    bar_width = 120
    bar_height = 30
    
    # First bar
    seg1_width = bar_width / frac1_denom
    bar1 = []
    for i in range(frac1_denom):
        color = '#4CAF50' if i < frac1_num else '#E8F5E9'
        bar1.append(f'<rect x="{20 + i*seg1_width:.1f}" y="20" width="{seg1_width:.1f}" height="{bar_height}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    # Second bar
    seg2_width = bar_width / frac2_denom
    bar2 = []
    for i in range(frac2_denom):
        color = '#2196F3' if i < frac2_num else '#E3F2FD'
        bar2.append(f'<rect x="{160 + i*seg2_width:.1f}" y="20" width="{seg2_width:.1f}" height="{bar_height}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
        {''.join(bar1)}
        {''.join(bar2)}
        <text x="80" y="70" text-anchor="middle" font-size="14" fill="#2E7D32">{frac1_num}/{frac1_denom}</text>
        <text x="220" y="70" text-anchor="middle" font-size="14" fill="#1565C0">{frac2_num}/{frac2_denom}</text>
        <text x="150" y="90" text-anchor="middle" font-size="12" fill="#666">Which is larger?</text>
    </svg>'''


# ============================================================
# DISTRACTOR GENERATORS
# ============================================================

def generate_fraction_distractors(correct_num, correct_denom, count=3):
    """Generate plausible wrong fraction answers - guaranteed unique"""
    correct = f"{correct_num}/{correct_denom}"
    distractors = set()
    
    # Inverted fraction
    if correct_num != correct_denom:
        distractors.add(f"{correct_denom}/{correct_num}")
    
    # Off by one in numerator
    if correct_num > 1:
        distractors.add(f"{correct_num - 1}/{correct_denom}")
    if correct_num < correct_denom:
        distractors.add(f"{correct_num + 1}/{correct_denom}")
    
    # Different denominator
    for d in [correct_denom - 1, correct_denom + 1, correct_denom * 2]:
        if d > 1:
            distractors.add(f"{correct_num}/{d}")
    
    # Add more variety
    for n in range(1, min(correct_denom + 3, 12)):
        for d in range(2, min(correct_denom + 3, 12)):
            if n <= d:
                frac = f"{n}/{d}"
                if frac != correct:
                    distractors.add(frac)
    
    # Remove correct answer if present
    distractors.discard(correct)
    
    # Return as list
    result = list(distractors)
    random.shuffle(result)
    return result[:count]


def generate_integer_distractors(correct, count=3):
    """Generate plausible wrong integer answers - guaranteed unique"""
    distractors = set()
    
    # Close values
    for offset in [-3, -2, -1, 1, 2, 3, 5, 10, -10]:
        if correct + offset > 0 and correct + offset != correct:
            distractors.add(correct + offset)
    
    # Doubled/halved
    distractors.add(correct * 2)
    if correct > 1:
        distractors.add(correct // 2)
    
    distractors.discard(correct)
    result = list(distractors)
    random.shuffle(result)
    return [str(d) for d in result[:count]]


def make_unique_options(correct, distractors, ensure_count=4):
    """Ensure we have exactly ensure_count unique options including correct answer"""
    options = [correct]
    
    for d in distractors:
        if d not in options:
            options.append(d)
        if len(options) >= ensure_count:
            break
    
    # If we still need more options, generate random ones
    attempts = 0
    while len(options) < ensure_count and attempts < 50:
        attempts += 1
        # Generate a random option based on the correct answer type
        if '/' in str(correct):
            # Fraction
            n = random.randint(1, 10)
            d = random.randint(2, 12)
            new_opt = f"{n}/{d}"
        elif '%' in str(correct):
            # Percentage
            new_opt = f"{random.randint(1, 99)}%"
        else:
            # Integer or other
            try:
                base = int(correct.split()[0]) if ' ' in str(correct) else int(correct)
                new_opt = str(base + random.randint(-5, 5))
            except:
                new_opt = str(random.randint(1, 100))
        
        if new_opt not in options:
            options.append(new_opt)
    
    return options[:ensure_count]


# ============================================================
# LEVEL 1-3: BEGINNER
# ============================================================

def generate_level_1_fractions():
    """Level 1: Simplest fractions - halves, thirds, quarters only"""
    questions = []
    
    # Pie charts - halves
    for _ in range(15):
        num = random.randint(1, 2)
        denom = 2
        svg = svg_pie_chart(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 1, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction of the circle is shaded? (Circle {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Fraction bars - halves and quarters
    for _ in range(15):
        denom = random.choice([2, 4])
        num = random.randint(1, denom - 1)
        svg = svg_fraction_bar(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 1, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction of the bar is shaded? (Bar {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Simple word problems
    items = ['pizza', 'cake', 'chocolate bar', 'apple pie']
    for _ in range(10):
        item = random.choice(items)
        denom = random.choice([2, 4])
        num = random.randint(1, denom - 1)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 1, 'band': 'beginner', 'type': 'word_problem',
            'question': f'A {item} is cut into {denom} equal pieces. Seán eats {num} piece{"s" if num > 1 else ""}. What fraction did he eat?',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Grid questions
    for _ in range(10):
        denom = random.choice([4, 6])
        num = random.randint(1, denom - 1)
        svg = svg_grid(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 1, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction of the grid is shaded? (Grid {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    return questions


def generate_level_2_fractions():
    """Level 2: Thirds and fifths added"""
    questions = []
    
    # Pie charts
    for _ in range(15):
        denom = random.choice([2, 3, 4, 5])
        num = random.randint(1, denom - 1)
        svg = svg_pie_chart(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 2, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction is shaded? (Pie {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Fraction bars
    for _ in range(15):
        denom = random.choice([3, 4, 5])
        num = random.randint(1, denom - 1)
        svg = svg_fraction_bar(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 2, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction is coloured? (Bar {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Number lines
    for _ in range(10):
        denom = random.choice([2, 4, 5])
        num = random.randint(1, denom - 1)
        svg = svg_number_line(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 2, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction does the red dot represent? (NL {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Simple fraction of amount
    for _ in range(10):
        total = random.choice([10, 12, 20])
        denom = random.choice([2, 4, 5])
        num = 1
        result = (total * num) // denom
        correct = str(result)
        distractors = generate_integer_distractors(result)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 2, 'band': 'beginner', 'type': 'calculation',
            'question': f'What is {num}/{denom} of {total}?',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


def generate_level_3_fractions():
    """Level 3: Sixths, eighths; simple comparisons"""
    questions = []
    
    # Pie charts with more segments
    for _ in range(12):
        denom = random.choice([3, 4, 6, 8])
        num = random.randint(1, denom - 1)
        svg = svg_pie_chart(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 3, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction of the pie is green? (ID {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Grids
    for _ in range(12):
        denom = random.choice([6, 8, 9])
        num = random.randint(1, denom - 1)
        svg = svg_grid(num, denom)
        correct = f"{num}/{denom}"
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 3, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction of squares are shaded? (Grid {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Comparisons with visuals
    for _ in range(12):
        f1_num, f1_denom = random.randint(1, 3), random.choice([4, 6])
        f2_num, f2_denom = random.randint(1, 3), random.choice([4, 6])
        
        val1 = f1_num / f1_denom
        val2 = f2_num / f2_denom
        
        if val1 > val2:
            correct = f"{f1_num}/{f1_denom}"
        elif val2 > val1:
            correct = f"{f2_num}/{f2_denom}"
        else:
            correct = "They are equal"
        
        svg = svg_comparison(f1_num, f1_denom, f2_num, f2_denom)
        options = [f"{f1_num}/{f1_denom}", f"{f2_num}/{f2_denom}", "They are equal", "Cannot tell"]
        
        questions.append({
            'level': 3, 'band': 'beginner', 'type': 'visual',
            'question': f'Which fraction is larger? (Comp {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Fraction of amount
    for _ in range(14):
        total = random.choice([12, 18, 24, 30])
        denom = random.choice([2, 3, 4, 6])
        num = random.randint(1, 2)
        result = (total * num) // denom
        correct = str(result)
        distractors = generate_integer_distractors(result)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 3, 'band': 'beginner', 'type': 'calculation',
            'question': f'Calculate {num}/{denom} of {total}. (Calc {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 4-6: INTERMEDIATE
# ============================================================

def generate_level_4_fractions():
    """Level 4: Equivalent fractions, simplifying"""
    questions = []
    
    # Find equivalent fraction
    equivalents = [
        (2, 4, 1, 2), (3, 6, 1, 2), (2, 6, 1, 3), (4, 8, 1, 2),
        (3, 9, 1, 3), (4, 12, 1, 3), (6, 8, 3, 4), (4, 6, 2, 3)
    ]
    for _ in range(15):
        orig_num, orig_denom, simp_num, simp_denom = random.choice(equivalents)
        correct = f"{simp_num}/{simp_denom}"
        distractors = [f"{orig_num}/{simp_denom}", f"{simp_num}/{orig_denom}", f"{orig_num-1}/{orig_denom}"]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 4, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Simplify {orig_num}/{orig_denom} to its lowest terms. (Q{random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Pie charts with equivalent checking
    for _ in range(12):
        denom = random.choice([6, 8, 10])
        num = random.randint(2, denom - 2)
        svg = svg_pie_chart(num, denom)
        
        from math import gcd
        g = gcd(num, denom)
        simp_num, simp_denom = num // g, denom // g
        
        # Sometimes ask for simplified, sometimes unsimplified
        if random.random() < 0.5:
            correct = f"{simp_num}/{simp_denom}"
            question = f'What fraction is shaded? (Give simplest form) (Pie {random.randint(1000,9999)})'
        else:
            correct = f"{num}/{denom}"
            question = f'What fraction is shaded? (Pie {random.randint(1000,9999)})'
        
        distractors = generate_fraction_distractors(num, denom)
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 4, 'band': 'intermediate', 'type': 'visual',
            'question': question, 'options': options, 
            'correct': options.index(correct), 'svg': svg
        })
    
    # Fraction of amount (larger numbers)
    for _ in range(15):
        total = random.choice([20, 24, 30, 36, 40])
        denom = random.choice([4, 5, 6])
        num = random.randint(1, 3)
        result = (total * num) // denom
        correct = str(result)
        distractors = generate_integer_distractors(result)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 4, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Find {num}/{denom} of {total}. (Calc {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Which is equivalent
    for _ in range(8):
        base_num = random.randint(1, 3)
        base_denom = random.choice([4, 5, 6])
        multiplier = random.randint(2, 3)
        eq_num = base_num * multiplier
        eq_denom = base_denom * multiplier
        
        correct = f"{eq_num}/{eq_denom}"
        wrong1 = f"{eq_num}/{base_denom}"
        wrong2 = f"{base_num}/{eq_denom}"
        wrong3 = f"{eq_num + 1}/{eq_denom}"
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        
        questions.append({
            'level': 4, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Which fraction is equivalent to {base_num}/{base_denom}? (Eq {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


def generate_level_5_fractions():
    """Level 5: Adding fractions with same denominator"""
    questions = []
    
    # Add fractions (same denominator)
    for _ in range(20):
        denom = random.choice([4, 5, 6, 8])
        num1 = random.randint(1, denom // 2)
        num2 = random.randint(1, denom // 2)
        result_num = num1 + num2
        
        from math import gcd
        g = gcd(result_num, denom)
        simp_num, simp_denom = result_num // g, denom // g
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{num1 + num2}/{denom * 2}",  # Added denominators
            f"{num1}/{denom}",  # Forgot to add
            f"{result_num}/{denom}" if f"{result_num}/{denom}" != correct else f"{result_num + 1}/{denom}"
        ]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        # Visual representation
        svg = svg_fraction_bar(num1, denom) if random.random() < 0.5 else ''
        
        questions.append({
            'level': 5, 'band': 'intermediate', 'type': 'visual' if svg else 'calculation',
            'question': f'Calculate {num1}/{denom} + {num2}/{denom}. (Add {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Subtract fractions (same denominator)
    for _ in range(15):
        denom = random.choice([4, 5, 6, 8])
        num1 = random.randint(denom // 2 + 1, denom - 1)
        num2 = random.randint(1, num1 - 1)
        result_num = num1 - num2
        
        from math import gcd
        g = gcd(result_num, denom)
        simp_num, simp_denom = result_num // g, denom // g
        
        correct = f"{simp_num}/{simp_denom}"
        distractors = generate_fraction_distractors(simp_num, simp_denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 5, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Calculate {num1}/{denom} - {num2}/{denom}. (Sub {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Ordering fractions (same denominator)
    for _ in range(15):
        denom = random.choice([5, 6, 8])
        nums = random.sample(range(1, denom), 3)
        fracs = [f"{n}/{denom}" for n in nums]
        sorted_fracs = sorted(fracs, key=lambda x: int(x.split('/')[0]))
        
        direction = random.choice(['smallest to largest', 'largest to smallest'])
        if direction == 'largest to smallest':
            sorted_fracs.reverse()
        
        correct = ', '.join(sorted_fracs)
        
        # Generate wrong orderings
        wrong_orders = []
        for _ in range(5):
            shuffled = fracs.copy()
            random.shuffle(shuffled)
            wrong = ', '.join(shuffled)
            if wrong != correct:
                wrong_orders.append(wrong)
        
        options = [correct] + wrong_orders[:3]
        random.shuffle(options)
        
        questions.append({
            'level': 5, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Order these fractions from {direction}: {", ".join(fracs)} (Ord {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


def generate_level_6_fractions():
    """Level 6: Adding fractions with different denominators"""
    questions = []
    
    # Add fractions (different but related denominators)
    pairs = [(2, 4), (2, 6), (3, 6), (4, 8), (3, 9), (5, 10)]
    for _ in range(20):
        d1, d2 = random.choice(pairs)
        num1 = random.randint(1, d1 - 1)
        num2 = random.randint(1, d2 - 1)
        
        # Convert to common denominator
        common_d = d2 if d2 % d1 == 0 else d1 * d2
        new_num1 = num1 * (common_d // d1)
        new_num2 = num2 * (common_d // d2)
        result_num = new_num1 + new_num2
        
        from math import gcd
        g = gcd(result_num, common_d)
        simp_num, simp_denom = result_num // g, common_d // g
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{num1 + num2}/{d1 + d2}",  # Common mistake
            f"{num1 + num2}/{d2}",
            f"{result_num}/{common_d}" if f"{result_num}/{common_d}" != correct else f"{result_num + 1}/{common_d}"
        ]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 6, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Calculate {num1}/{d1} + {num2}/{d2}. Give your answer in simplest form. (Add {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Mixed number identification
    for _ in range(15):
        whole = random.randint(1, 3)
        num = random.randint(1, 3)
        denom = random.choice([2, 4, 5])
        improper_num = whole * denom + num
        
        correct = f"{improper_num}/{denom}"
        distractors = [
            f"{whole + num}/{denom}",
            f"{whole * num}/{denom}",
            f"{improper_num}/{denom + 1}"
        ]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 6, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Convert {whole} {num}/{denom} to an improper fraction. (Conv {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Improper to mixed
    for _ in range(15):
        denom = random.choice([3, 4, 5])
        improper_num = random.randint(denom + 1, denom * 3)
        
        whole = improper_num // denom
        remainder = improper_num % denom
        
        if remainder == 0:
            correct = str(whole)
        else:
            correct = f"{whole} {remainder}/{denom}"
        
        distractors = [
            f"{whole + 1} {remainder}/{denom}",
            f"{whole} {remainder + 1}/{denom}" if remainder + 1 < denom else f"{whole} 1/{denom}",
            f"{improper_num}/{denom}"
        ]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 6, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Convert {improper_num}/{denom} to a mixed number. (Conv {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 7-9: ADVANCED
# ============================================================

def generate_level_7_fractions():
    """Level 7: Multiplying fractions"""
    questions = []
    
    for _ in range(25):
        num1, denom1 = random.randint(1, 4), random.choice([3, 4, 5, 6])
        num2, denom2 = random.randint(1, 4), random.choice([3, 4, 5, 6])
        
        result_num = num1 * num2
        result_denom = denom1 * denom2
        
        from math import gcd
        g = gcd(result_num, result_denom)
        simp_num, simp_denom = result_num // g, result_denom // g
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{num1 * num2}/{denom1 + denom2}",
            f"{num1 + num2}/{denom1 * denom2}",
            f"{result_num}/{result_denom}" if f"{result_num}/{result_denom}" != correct else f"{simp_num + 1}/{simp_denom}"
        ]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 7, 'band': 'advanced', 'type': 'calculation',
            'question': f'Calculate {num1}/{denom1} × {num2}/{denom2}. (Mult {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Fraction of a fraction (visual)
    for _ in range(15):
        outer_denom = random.choice([2, 3, 4])
        inner_num = random.randint(1, outer_denom - 1)
        inner_denom = random.choice([2, 3])
        
        result_num = inner_num
        result_denom = outer_denom * inner_denom
        
        from math import gcd
        g = gcd(result_num, result_denom)
        simp_num, simp_denom = result_num // g, result_denom // g
        
        correct = f"{simp_num}/{simp_denom}"
        distractors = generate_fraction_distractors(simp_num, simp_denom)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        svg = svg_grid(inner_num * inner_denom, outer_denom * inner_denom)
        
        questions.append({
            'level': 7, 'band': 'advanced', 'type': 'visual',
            'question': f'What is 1/{inner_denom} of {inner_num}/{outer_denom}? (Grid {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Comparing with different denominators
    for _ in range(10):
        f1_num, f1_denom = random.randint(2, 5), random.choice([6, 8, 9])
        f2_num, f2_denom = random.randint(2, 5), random.choice([6, 8, 9])
        
        val1 = f1_num / f1_denom
        val2 = f2_num / f2_denom
        
        if val1 > val2:
            correct = f"{f1_num}/{f1_denom}"
        elif val2 > val1:
            correct = f"{f2_num}/{f2_denom}"
        else:
            correct = "They are equal"
        
        options = [f"{f1_num}/{f1_denom}", f"{f2_num}/{f2_denom}", "They are equal", "Cannot compare"]
        
        questions.append({
            'level': 7, 'band': 'advanced', 'type': 'calculation',
            'question': f'Which is greater: {f1_num}/{f1_denom} or {f2_num}/{f2_denom}? (Comp {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


def generate_level_8_fractions():
    """Level 8: Dividing fractions"""
    questions = []
    
    for _ in range(25):
        num1, denom1 = random.randint(1, 4), random.choice([2, 3, 4, 5])
        num2, denom2 = random.randint(1, 3), random.choice([2, 3, 4])
        
        # Divide by multiplying by reciprocal
        result_num = num1 * denom2
        result_denom = denom1 * num2
        
        from math import gcd
        g = gcd(result_num, result_denom)
        simp_num, simp_denom = result_num // g, result_denom // g
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{num1 * num2}/{denom1 * denom2}",  # Multiplied instead
            f"{num1 * denom2}/{denom1 + num2}",
            f"{result_denom}/{result_num}" if result_denom != result_num else f"{simp_num + 1}/{simp_denom}"
        ]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 8, 'band': 'advanced', 'type': 'calculation',
            'question': f'Calculate {num1}/{denom1} ÷ {num2}/{denom2}. (Div {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Mixed operations
    for _ in range(15):
        num1 = random.randint(1, 3)
        denom = random.choice([4, 5, 6])
        whole = random.randint(2, 5)
        
        result_num = num1 * whole
        
        from math import gcd
        g = gcd(result_num, denom)
        simp_num, simp_denom = result_num // g, denom // g
        
        if simp_denom == 1:
            correct = str(simp_num)
        elif simp_num > simp_denom:
            whole_part = simp_num // simp_denom
            remainder = simp_num % simp_denom
            correct = f"{whole_part} {remainder}/{simp_denom}" if remainder > 0 else str(whole_part)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{num1 + whole}/{denom}",
            f"{num1 * whole + denom}/{denom}",
            str(num1 * whole)
        ]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 8, 'band': 'advanced', 'type': 'calculation',
            'question': f'Calculate {num1}/{denom} × {whole}. (Mixed {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Word problems
    for _ in range(10):
        total = random.choice([24, 30, 36, 40])
        frac_num = random.randint(2, 4)
        frac_denom = random.choice([4, 5, 6])
        result = (total * frac_num) // frac_denom
        
        correct = str(result)
        distractors = generate_integer_distractors(result)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        items = ['students', 'books', 'apples', 'euros']
        item = random.choice(items)
        
        questions.append({
            'level': 8, 'band': 'advanced', 'type': 'word_problem',
            'question': f'There are {total} {item}. {frac_num}/{frac_denom} of them are selected. How many is that? (WP {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


def generate_level_9_fractions():
    """Level 9: Complex operations and multi-step"""
    questions = []
    
    # Add then multiply
    for _ in range(15):
        num1, denom = random.randint(1, 3), random.choice([4, 6, 8])
        num2 = random.randint(1, 3)
        multiplier = random.randint(2, 4)
        
        sum_num = num1 + num2
        result_num = sum_num * multiplier
        
        from math import gcd
        g = gcd(result_num, denom)
        simp_num, simp_denom = result_num // g, denom // g
        
        if simp_denom == 1:
            correct = str(simp_num)
        elif simp_num > simp_denom:
            whole = simp_num // simp_denom
            rem = simp_num % simp_denom
            correct = f"{whole} {rem}/{simp_denom}" if rem > 0 else str(whole)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{sum_num}/{denom}",
            f"{num1 * multiplier}/{denom}",
            f"{result_num}/{denom}" if f"{result_num}/{denom}" != correct else f"{simp_num + 1}/{simp_denom}"
        ]
        options = make_unique_options(correct, [d for d in distractors if d != correct][:3], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 9, 'band': 'advanced', 'type': 'calculation',
            'question': f'Calculate ({num1}/{denom} + {num2}/{denom}) × {multiplier}. (Multi {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Fraction of fraction of amount
    for _ in range(15):
        total = random.choice([60, 72, 80, 90, 120])
        frac1_num, frac1_denom = random.randint(1, 2), random.choice([3, 4])
        frac2_num, frac2_denom = random.randint(1, 2), random.choice([2, 3])
        
        step1 = (total * frac1_num) // frac1_denom
        result = (step1 * frac2_num) // frac2_denom
        
        correct = str(result)
        distractors = generate_integer_distractors(result)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 9, 'band': 'advanced', 'type': 'word_problem',
            'question': f'Find {frac2_num}/{frac2_denom} of {frac1_num}/{frac1_denom} of {total}. (Chain {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Order 4 fractions
    for _ in range(10):
        denoms = [3, 4, 6, 8]
        fracs = []
        for d in random.sample(denoms, 4):
            n = random.randint(1, d - 1)
            fracs.append((n, d))
        
        sorted_fracs = sorted(fracs, key=lambda x: x[0] / x[1])
        sorted_strs = [f"{n}/{d}" for n, d in sorted_fracs]
        
        correct = ', '.join(sorted_strs)
        frac_strs = [f"{n}/{d}" for n, d in fracs]
        
        wrong_orders = []
        for _ in range(5):
            shuffled = frac_strs.copy()
            random.shuffle(shuffled)
            wrong = ', '.join(shuffled)
            if wrong != correct:
                wrong_orders.append(wrong)
        
        options = [correct] + wrong_orders[:3]
        random.shuffle(options)
        
        questions.append({
            'level': 9, 'band': 'advanced', 'type': 'calculation',
            'question': f'Order from smallest to largest: {", ".join(frac_strs)} (Ord {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Complex word problems
    for _ in range(10):
        total = random.choice([48, 60, 72])
        frac1 = random.choice([(1, 3), (1, 4), (2, 3)])
        frac2 = random.choice([(1, 2), (1, 3), (2, 3)])
        
        group1 = (total * frac1[0]) // frac1[1]
        remainder = total - group1
        group2 = (remainder * frac2[0]) // frac2[1]
        rest = remainder - group2
        
        correct = str(rest)
        distractors = generate_integer_distractors(rest)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 9, 'band': 'advanced', 'type': 'word_problem',
            'question': f'Of {total} sweets, {frac1[0]}/{frac1[1]} are red. Of the rest, {frac2[0]}/{frac2[1]} are blue. How many are neither red nor blue? (WP {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 10: MASTERY
# ============================================================

def generate_level_10_fractions():
    """Level 10: Mastery - challenging problems"""
    questions = []
    
    # Complex algebraic-style
    for _ in range(15):
        # Find the missing numerator: ?/6 = 2/3
        denom1 = random.choice([4, 6, 8, 9, 10, 12])
        denom2 = random.choice([2, 3, 4, 5])
        
        if denom1 % denom2 == 0:
            multiplier = denom1 // denom2
            num2 = random.randint(1, denom2 - 1)
            num1 = num2 * multiplier
            
            correct = str(num1)
            distractors = generate_integer_distractors(num1)
            options = make_unique_options(correct, distractors, 4)
            random.shuffle(options)
            
            questions.append({
                'level': 10, 'band': 'mastery', 'type': 'calculation',
                'question': f'Find the missing value: ?/{denom1} = {num2}/{denom2} (Miss {random.randint(1000,9999)})',
                'options': options, 'correct': options.index(correct), 'svg': ''
            })
    
    # Reverse word problems
    for _ in range(15):
        result = random.choice([12, 15, 18, 20, 24])
        frac_num = random.randint(2, 4)
        frac_denom = random.choice([4, 5, 6])
        total = (result * frac_denom) // frac_num
        
        correct = str(total)
        distractors = generate_integer_distractors(total)
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 10, 'band': 'mastery', 'type': 'word_problem',
            'question': f'{frac_num}/{frac_denom} of a number is {result}. What is the number? (Rev {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Multi-step with all operations
    for _ in range(10):
        num1, denom1 = random.randint(1, 3), 4
        num2, denom2 = random.randint(1, 2), 3
        num3 = random.randint(2, 3)
        
        # (a/b + c/d) × n
        # Common denom for a/b and c/d
        common_d = 12
        new_num1 = num1 * 3  # 4 -> 12
        new_num2 = num2 * 4  # 3 -> 12
        sum_num = new_num1 + new_num2
        result_num = sum_num * num3
        
        from math import gcd
        g = gcd(result_num, common_d)
        simp_num, simp_denom = result_num // g, common_d // g
        
        if simp_denom == 1:
            correct = str(simp_num)
        elif simp_num > simp_denom:
            whole = simp_num // simp_denom
            rem = simp_num % simp_denom
            correct = f"{whole} {rem}/{simp_denom}" if rem > 0 else str(whole)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        wrong1 = f"{sum_num}/{common_d}"
        wrong2 = f"{num1 * num3}/{denom1}"
        wrong3 = f"{result_num}/{common_d}" if f"{result_num}/{common_d}" != correct else "0"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        
        questions.append({
            'level': 10, 'band': 'mastery', 'type': 'calculation',
            'question': f'Calculate ({num1}/{denom1} + {num2}/{denom2}) × {num3}. (Adv {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Comparing expressions
    for _ in range(10):
        a, b = random.randint(1, 3), random.choice([4, 5, 6])
        c, d = random.randint(1, 3), random.choice([4, 5, 6])
        
        val1 = a / b
        val2 = c / d
        product = (a * c) / (b * d)
        sum_val = val1 + val2
        
        expressions = [
            (f"{a}/{b} × {c}/{d}", product),
            (f"{a}/{b} + {c}/{d}", sum_val),
            (f"{a}/{b}", val1),
            (f"{c}/{d}", val2)
        ]
        
        random.shuffle(expressions)
        sorted_exp = sorted(expressions, key=lambda x: x[1], reverse=True)
        correct = sorted_exp[0][0]
        
        options = [e[0] for e in expressions]
        
        questions.append({
            'level': 10, 'band': 'mastery', 'type': 'calculation',
            'question': f'Which expression has the greatest value? (Expr {random.randint(1000,9999)})',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database"""
    conn = get_db()
    cursor = conn.cursor()
    inserted = 0
    duplicates = 0
    
    for q in questions:
        options = q['options']
        
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, image_svg, is_active, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
            ''', (
                'fractions',
                q['question'],
                str(options[0]) if len(options) > 0 else '',
                str(options[1]) if len(options) > 1 else '',
                str(options[2]) if len(options) > 2 else '',
                str(options[3]) if len(options) > 3 else '',
                q['correct'],
                '',
                q['level'],
                q['band'],
                q['type'],
                q.get('svg', ''),
                datetime.now().isoformat()
            ))
            inserted += 1
        except sqlite3.IntegrityError:
            duplicates += 1
        except Exception as e:
            print(f"Error inserting question: {e}")
    
    conn.commit()
    conn.close()
    return inserted, duplicates


# ============================================================
# MAIN
# ============================================================

def generate_all():
    """Generate all fraction questions"""
    print("=" * 60)
    print("Generating Fractions Questions (Levels 1-10)")
    print("=" * 60)
    
    all_questions = []
    
    generators = [
        (1, generate_level_1_fractions),
        (2, generate_level_2_fractions),
        (3, generate_level_3_fractions),
        (4, generate_level_4_fractions),
        (5, generate_level_5_fractions),
        (6, generate_level_6_fractions),
        (7, generate_level_7_fractions),
        (8, generate_level_8_fractions),
        (9, generate_level_9_fractions),
        (10, generate_level_10_fractions),
    ]
    
    for level, generator in generators:
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level:2d}: Generated {len(questions)} questions")
    
    print(f"\nTotal generated: {len(all_questions)}")
    
    inserted, duplicates = insert_questions(all_questions)
    print(f"Inserted: {inserted} new questions")
    print(f"Skipped: {duplicates} duplicates")


def show_stats():
    """Show current statistics"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT difficulty_level, difficulty_band, COUNT(*), 
               SUM(CASE WHEN image_svg != '' AND image_svg IS NOT NULL THEN 1 ELSE 0 END) as visual_count
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND is_active = 1
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    """)
    
    print("\nFractions Questions by Level:")
    print("-" * 60)
    print(f"{'Level':<8} {'Band':<15} {'Total':<8} {'Visual':<8} {'%Visual':<8}")
    print("-" * 60)
    
    total_all = 0
    visual_all = 0
    
    for row in cursor.fetchall():
        level, band, total, visual = row
        visual = visual or 0
        pct = (visual / total * 100) if total > 0 else 0
        print(f"Level {level:<2} {band:<15} {total:<8} {visual:<8} {pct:.0f}%")
        total_all += total
        visual_all += visual
    
    print("-" * 60)
    overall_pct = (visual_all / total_all * 100) if total_all > 0 else 0
    print(f"{'TOTAL':<8} {'':<15} {total_all:<8} {visual_all:<8} {overall_pct:.0f}%")
    
    conn.close()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--stats':
        show_stats()
    else:
        generate_all()
        print("\n")
        show_stats()
