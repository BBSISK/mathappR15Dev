#!/usr/bin/env python3
"""
AgentMath Percentages Question Generator v1
SEC-Aligned Adaptive Quiz Questions for Irish Junior Cycle

Following AgentMath Topic Generator Methodology:
- 12 levels × 50 questions = 600 total
- 75% visual/contextual for levels 1-10
- 50% visual/contextual for levels 11-12
- Step-by-step explanations for every question
- SEC exam paper alignment (2022-2025)

Level Structure:
1. Visual % (shaded grids, pie charts) - Foundation
2. % of amount (simple) - OL Q4 style
3. % of amount (multi-step, rounding) - OL Q2(c) style
4. Convert fraction ↔ % - Foundation
5. Convert decimal ↔ % - Foundation
6. % increase (simple) - OL Q4(e) style
7. % decrease/discount - HL Q1(b) style
8. % change comparison - HL Q2(e) style
9. % profit/loss - OL Q9(d), HL Q4(b) style
10. Reverse % (find original) - Higher
11. Simple interest - OL Q9(c) style
12. Compound interest, VAT - HL style

Author: AgentMath Generator
Date: December 2025
"""

import sqlite3
import random
import math
import os
import json

# Configuration
TOPIC = 'percentages'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = '/home/bbsisk/mathappR12/instance/mathquiz.db'

# Difficulty bands
DIFFICULTY_BANDS = {
    1: 'Foundation', 2: 'Foundation', 3: 'Foundation',
    4: 'Ordinary', 5: 'Ordinary', 6: 'Ordinary',
    7: 'Higher', 8: 'Higher', 9: 'Higher',
    10: 'Application', 11: 'Application', 12: 'Mastery'
}

# ============== SVG GENERATORS ==============

def generate_percentage_grid_svg(percentage, grid_size=10):
    """Generate a 10x10 grid with percentage of squares shaded"""
    shaded_count = int(percentage)
    cell_size = 25
    padding = 5
    width = grid_size * cell_size + 2 * padding
    height = grid_size * cell_size + 2 * padding
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="max-width: 250px;">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f8fafc" rx="4"/>'
    
    # Create list and shuffle for random shading
    cells_to_shade = list(range(100))
    random.shuffle(cells_to_shade)
    shaded_cells = set(cells_to_shade[:shaded_count])
    
    for i in range(100):
        row = i // grid_size
        col = i % grid_size
        x = padding + col * cell_size
        y = padding + row * cell_size
        
        fill = "#3b82f6" if i in shaded_cells else "#ffffff"
        svg += f'<rect x="{x}" y="{y}" width="{cell_size-2}" height="{cell_size-2}" fill="{fill}" stroke="#cbd5e1" stroke-width="1" rx="2"/>'
    
    svg += '</svg>'
    return svg

def generate_pie_chart_svg(percentage):
    """Generate a pie chart showing a percentage"""
    cx, cy, r = 80, 80, 60
    
    if percentage == 0:
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" style="max-width: 160px;">'
        svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>'
        svg += f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e293b">0%</text>'
        svg += '</svg>'
        return svg
    
    if percentage == 100:
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" style="max-width: 160px;">'
        svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#3b82f6" stroke="#94a3b8" stroke-width="2"/>'
        svg += f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="18" font-weight="bold" fill="#ffffff">100%</text>'
        svg += '</svg>'
        return svg
    
    angle = (percentage / 100) * 360
    end_angle_rad = math.radians(angle - 90)
    end_x = cx + r * math.cos(end_angle_rad)
    end_y = cy + r * math.sin(end_angle_rad)
    large_arc = 1 if percentage > 50 else 0
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" style="max-width: 160px;">'
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>'
    svg += f'<path d="M {cx} {cy} L {cx} {cy - r} A {r} {r} 0 {large_arc} 1 {end_x:.1f} {end_y:.1f} Z" fill="#3b82f6"/>'
    svg += f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e293b">{percentage}%</text>'
    svg += '</svg>'
    return svg

def generate_bar_comparison_svg(original, new_value, label1="Before", label2="After"):
    """Generate a bar chart comparing two values"""
    max_val = max(original, new_value, 1)
    scale = 140 / max_val
    
    bar1_height = max(5, original * scale)
    bar2_height = max(5, new_value * scale)
    
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" style="max-width: 200px;">'
    svg += '<rect x="0" y="0" width="200" height="200" fill="#f8fafc" rx="4"/>'
    
    # Bar 1
    svg += f'<rect x="30" y="{175 - bar1_height}" width="50" height="{bar1_height}" fill="#94a3b8" rx="2"/>'
    svg += f'<text x="55" y="195" text-anchor="middle" font-size="11" fill="#64748b">{label1}</text>'
    svg += f'<text x="55" y="{170 - bar1_height}" text-anchor="middle" font-size="12" font-weight="bold" fill="#374151">{original}</text>'
    
    # Bar 2
    color = "#22c55e" if new_value >= original else "#ef4444"
    svg += f'<rect x="120" y="{175 - bar2_height}" width="50" height="{bar2_height}" fill="{color}" rx="2"/>'
    svg += f'<text x="145" y="195" text-anchor="middle" font-size="11" fill="#64748b">{label2}</text>'
    svg += f'<text x="145" y="{170 - bar2_height}" text-anchor="middle" font-size="12" font-weight="bold" fill="#374151">{new_value}</text>'
    
    svg += '</svg>'
    return svg

def generate_price_tag_svg(original_price, sale_price=None, discount_percent=None):
    """Generate a price tag showing original and sale price"""
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 120" style="max-width: 180px;">'
    svg += '<rect x="5" y="5" width="170" height="110" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="8"/>'
    svg += '<circle cx="25" cy="25" r="8" fill="#ffffff" stroke="#f59e0b" stroke-width="2"/>'
    
    if sale_price is not None:
        svg += f'<text x="90" y="40" text-anchor="middle" font-size="14" fill="#9ca3af" text-decoration="line-through">€{original_price:.2f}</text>'
        svg += f'<text x="90" y="70" text-anchor="middle" font-size="22" font-weight="bold" fill="#dc2626">€{sale_price:.2f}</text>'
        if discount_percent:
            svg += f'<text x="90" y="95" text-anchor="middle" font-size="14" font-weight="bold" fill="#16a34a">{discount_percent}% OFF!</text>'
    else:
        svg += f'<text x="90" y="65" text-anchor="middle" font-size="24" font-weight="bold" fill="#1e293b">€{original_price:.2f}</text>'
    
    svg += '</svg>'
    return svg

# ============== HELPER FUNCTIONS ==============

def generate_wrong_answers(correct, candidates, count=3):
    """Generate unique wrong answers from candidates"""
    wrong = []
    for c in candidates:
        if c != correct and c not in wrong and c > 0:
            wrong.append(c)
        if len(wrong) >= count:
            break
    return wrong[:count]

def format_options(correct_answer, wrong_answers, format_str="{}"):
    """Format and shuffle options, return (options, correct_idx)"""
    formatted_correct = format_str.format(correct_answer)
    formatted_wrong = [format_str.format(w) for w in wrong_answers[:3]]
    
    # Ensure we have exactly 3 wrong answers
    while len(formatted_wrong) < 3:
        formatted_wrong.append(format_str.format(correct_answer + random.randint(1, 10)))
    
    options = [formatted_correct] + formatted_wrong[:3]
    random.shuffle(options)
    correct_idx = options.index(formatted_correct)
    
    return options, correct_idx

# ============== QUESTION GENERATORS ==============

def generate_level_1():
    """Level 1: Visual % - shaded grids and pie charts (Foundation)"""
    questions = []
    simple_percentages = [10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90]
    
    # Grid recognition (25 questions)
    for i in range(25):
        percentage = random.choice(simple_percentages)
        svg = generate_percentage_grid_svg(percentage)
        
        wrong = generate_wrong_answers(percentage, [p for p in range(5, 100, 5) if p != percentage])
        options, correct_idx = format_options(percentage, wrong, "{}%")
        
        questions.append({
            'question_text': "What percentage of this grid is shaded blue?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Count the blue squares: {percentage} out of 100 squares are shaded. {percentage} out of 100 = {percentage}%",
            'image_svg': svg
        })
    
    # Context with 100 items (15 questions)
    contexts = [
        ("garden", "flowers", "roses"), ("class", "students", "girls"),
        ("box", "chocolates", "milk chocolates"), ("car park", "spaces", "occupied"),
        ("fruit bowl", "pieces of fruit", "apples"), ("library", "books", "fiction")
    ]
    
    for i in range(15):
        percentage = random.choice(simple_percentages)
        ctx = random.choice(contexts)
        amount = percentage  # Since total is 100
        
        wrong = generate_wrong_answers(amount, [p for p in range(5, 100, 5) if p != amount])
        options, correct_idx = format_options(amount, wrong, "{}")
        
        questions.append({
            'question_text': f"In a {ctx[0]} with 100 {ctx[1]}, {percentage}% are {ctx[2]}. How many {ctx[2]} are there?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{percentage}% of 100 = {percentage}. There are {percentage} {ctx[2]}.",
            'image_svg': None
        })
    
    # Pie chart recognition (10 questions)
    for i in range(10):
        percentage = random.choice([25, 50, 75, 10, 20, 30, 40, 60, 70, 80])
        svg = generate_pie_chart_svg(percentage)
        
        wrong = generate_wrong_answers(percentage, [p for p in [10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90] if p != percentage])
        options, correct_idx = format_options(percentage, wrong, "{}%")
        
        questions.append({
            'question_text': "What percentage does the blue section of this pie chart represent?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The blue section covers {percentage}% of the circle.",
            'image_svg': svg
        })
    
    return questions

def generate_level_2():
    """Level 2: % of amount - simple calculations (OL Q4 style)"""
    questions = []
    
    contexts = [
        ("school", "students", "study French"), ("town", "people", "cycle to work"),
        ("farm", "animals", "are sheep"), ("shop", "items", "are on sale"),
        ("survey", "people", "prefer tea"), ("company", "employees", "work from home"),
        ("class", "pupils", "play sports"), ("orchard", "trees", "are apple trees"),
        ("hotel", "rooms", "are booked"), ("library", "members", "are adults")
    ]
    
    # Combinations that give whole numbers
    combinations = [
        (10, 50), (10, 80), (10, 120), (10, 200), (20, 50), (20, 75), (20, 100),
        (25, 40), (25, 80), (25, 100), (25, 200), (50, 30), (50, 60), (50, 100),
        (75, 40), (75, 80), (75, 100), (5, 100), (5, 200), (15, 100), (15, 200),
        (30, 50), (30, 100), (40, 50), (40, 100), (60, 50), (70, 100), (80, 50)
    ]
    
    for i in range(50):
        pct, amount = random.choice(combinations)
        ctx = random.choice(contexts)
        answer = int(pct * amount / 100)
        
        candidates = [answer + 5, answer - 5, answer + 10, answer * 2, amount - answer]
        wrong = generate_wrong_answers(answer, [c for c in candidates if 0 < c <= amount])
        
        while len(wrong) < 3:
            w = random.randint(1, amount)
            if w != answer and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(answer, wrong, "{}")
        
        questions.append({
            'question_text': f"A {ctx[0]} has {amount} {ctx[1]}. {pct}% of them {ctx[2]}. How many {ctx[1]} {ctx[2]}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{pct}% of {amount} = {pct}/100 × {amount} = {answer}",
            'image_svg': None
        })
    
    return questions

def generate_level_3():
    """Level 3: % of amount with money and rounding (SEC OL Q2(c) style)"""
    questions = []
    
    money_contexts = [
        ("meal costs", "tip", 15), ("bill comes to", "service charge", 12),
        ("jacket is priced at", "discount", 20), ("phone costs", "deposit", 25),
        ("rent is", "increase", 5), ("salary is", "bonus", 10),
        ("holiday costs", "deposit required is", 30), ("laptop costs", "student discount", 10)
    ]
    
    amounts = [45, 68, 72, 85, 95, 120, 145, 180, 225, 350, 450, 580, 720, 850]
    
    for i in range(30):
        ctx = random.choice(money_contexts)
        amount = random.choice(amounts)
        pct = ctx[2]
        
        exact = amount * pct / 100
        rounded = round(exact)
        
        candidates = [rounded + 1, rounded - 1, rounded + 2, int(exact) if int(exact) != rounded else rounded + 3]
        wrong = generate_wrong_answers(rounded, candidates)
        
        while len(wrong) < 3:
            w = rounded + random.randint(-5, 5)
            if w != rounded and w > 0 and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(rounded, wrong, "€{}")
        
        questions.append({
            'question_text': f"A {ctx[0]} €{amount}. Calculate {pct}% for the {ctx[1]}, rounded to the nearest euro.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{pct}% of €{amount} = {pct}/100 × {amount} = €{exact:.2f}. Rounded to nearest euro = €{rounded}",
            'image_svg': None
        })
    
    # Multi-step (20 questions)
    for i in range(20):
        total = random.choice([200, 300, 400, 500, 600, 800, 1000])
        pct1 = random.choice([20, 25, 30, 40, 50])
        first_amount = int(total * pct1 / 100)
        remaining = total - first_amount
        pct2 = random.choice([10, 20, 25, 50])
        answer = int(remaining * pct2 / 100)
        
        candidates = [answer + 10, answer - 10, first_amount, int(total * pct2 / 100)]
        wrong = generate_wrong_answers(answer, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = answer + random.randint(-20, 20)
            if w != answer and w > 0 and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(answer, wrong, "{}")
        
        questions.append({
            'question_text': f"A company has {total} employees. {pct1}% work in sales. Of the remaining employees, {pct2}% work in IT. How many work in IT?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Sales: {pct1}% of {total} = {first_amount}. Remaining: {total} - {first_amount} = {remaining}. IT: {pct2}% of {remaining} = {answer}",
            'image_svg': None
        })
    
    return questions

def generate_level_4():
    """Level 4: Convert fraction ↔ percentage (Foundation)"""
    questions = []
    
    fraction_pct_pairs = [
        (1, 2, 50), (1, 4, 25), (3, 4, 75), (1, 5, 20), (2, 5, 40),
        (3, 5, 60), (4, 5, 80), (1, 10, 10), (3, 10, 30), (7, 10, 70),
        (9, 10, 90), (1, 20, 5), (3, 20, 15), (1, 25, 4), (1, 50, 2)
    ]
    
    # Fraction to percentage (25 questions)
    for i in range(25):
        num, den, pct = random.choice(fraction_pct_pairs)
        
        candidates = [pct + 10, pct - 10, pct + 25, 100 - pct, pct * 2 if pct < 50 else pct // 2]
        wrong = generate_wrong_answers(pct, [c for c in candidates if 0 < c <= 100])
        
        while len(wrong) < 3:
            w = random.randint(5, 95)
            if w != pct and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(pct, wrong, "{}%")
        
        questions.append({
            'question_text': f"Convert {num}/{den} to a percentage.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{num}/{den} = {num} ÷ {den} = {num/den:.4f}. Multiply by 100 to get {pct}%",
            'image_svg': None
        })
    
    # Percentage to fraction (25 questions)
    for i in range(25):
        num, den, pct = random.choice(fraction_pct_pairs)
        answer = f"{num}/{den}"
        
        wrong_fracs = []
        candidates = [(num + 1, den), (num, den + 1), (num, den * 2), (den, num) if num != den else (1, den + 1)]
        for n, d in candidates:
            if n > 0 and d > 0:
                frac = f"{n}/{d}"
                if frac != answer and frac not in wrong_fracs:
                    wrong_fracs.append(frac)
        
        while len(wrong_fracs) < 3:
            n, d = random.randint(1, 9), random.randint(2, 10)
            frac = f"{n}/{d}"
            if frac != answer and frac not in wrong_fracs:
                wrong_fracs.append(frac)
        
        options = [answer] + wrong_fracs[:3]
        random.shuffle(options)
        correct_idx = options.index(answer)
        
        questions.append({
            'question_text': f"Convert {pct}% to a fraction in its simplest form.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{pct}% = {pct}/100. Simplify: {pct}/100 = {num}/{den}",
            'image_svg': None
        })
    
    return questions

def generate_level_5():
    """Level 5: Convert decimal ↔ percentage (Foundation)"""
    questions = []
    
    decimal_pct_pairs = [
        (0.1, 10), (0.2, 20), (0.25, 25), (0.3, 30), (0.4, 40),
        (0.5, 50), (0.6, 60), (0.7, 70), (0.75, 75), (0.8, 80),
        (0.9, 90), (0.15, 15), (0.35, 35), (0.45, 45), (0.05, 5),
        (0.55, 55), (0.65, 65), (0.85, 85), (0.95, 95), (0.01, 1)
    ]
    
    # Decimal to percentage (25 questions)
    for i in range(25):
        dec, pct = random.choice(decimal_pct_pairs)
        
        candidates = [pct + 10, pct - 10, int(pct * 10), int(pct / 10) if pct >= 10 else pct + 5, 100 - pct]
        wrong = generate_wrong_answers(pct, [c for c in candidates if 0 < c <= 100])
        
        while len(wrong) < 3:
            w = random.randint(1, 99)
            if w != pct and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(pct, wrong, "{}%")
        
        questions.append({
            'question_text': f"Convert {dec} to a percentage.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"To convert a decimal to a percentage, multiply by 100. {dec} × 100 = {pct}%",
            'image_svg': None
        })
    
    # Percentage to decimal (25 questions)
    for i in range(25):
        dec, pct = random.choice(decimal_pct_pairs)
        
        candidates = [dec * 10, dec / 10 if dec >= 0.1 else dec + 0.1, dec + 0.1, 1 - dec, dec + 0.05, dec - 0.05]
        wrong_decs = []
        for c in candidates:
            rounded_c = round(c, 2)
            if 0 < rounded_c < 1 and rounded_c != dec and rounded_c not in wrong_decs:
                wrong_decs.append(rounded_c)
        
        # Ensure we have 3 unique wrong answers
        attempts = 0
        while len(wrong_decs) < 3 and attempts < 20:
            w = round(random.uniform(0.01, 0.99), 2)
            if w != dec and w not in wrong_decs:
                wrong_decs.append(w)
            attempts += 1
        
        options = [str(dec)] + [str(w) for w in wrong_decs[:3]]
        # Ensure all options are unique
        while len(set(options)) < 4:
            new_w = round(random.uniform(0.01, 0.99), 2)
            if str(new_w) not in options:
                options[-1] = str(new_w)
        
        random.shuffle(options)
        correct_idx = options.index(str(dec))
        
        questions.append({
            'question_text': f"Convert {pct}% to a decimal.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"To convert a percentage to a decimal, divide by 100. {pct}% ÷ 100 = {dec}",
            'image_svg': None
        })
    
    return questions

def generate_level_6():
    """Level 6: Percentage increase - simple (SEC OL Q4(e) style)"""
    questions = []
    
    contexts = [
        ("price of a ticket", "increased from", "to"),
        ("number of members", "grew from", "to"),
        ("population", "rose from", "to"),
        ("temperature", "increased from", "to"),
        ("attendance", "grew from", "to"),
        ("share price", "rose from", "to")
    ]
    
    # Combinations giving nice percentage increases
    increase_combos = [
        (80, 90, 12.5), (100, 120, 20), (50, 60, 20), (40, 50, 25),
        (80, 100, 25), (60, 75, 25), (100, 150, 50), (200, 250, 25),
        (80, 88, 10), (150, 180, 20), (120, 150, 25), (200, 300, 50),
        (75, 90, 20), (160, 200, 25), (90, 99, 10), (250, 300, 20)
    ]
    
    for i in range(50):
        original, new, pct_increase = random.choice(increase_combos)
        ctx = random.choice(contexts)
        
        is_money = "price" in ctx[0]
        prefix = "€" if is_money else ""
        
        svg = generate_bar_comparison_svg(original, new, "Before", "After")
        
        # Common mistake: dividing by new instead of original
        common_mistake = round((new - original) / new * 100, 1)
        candidates = [pct_increase + 5, pct_increase - 5, common_mistake, pct_increase * 2]
        wrong = generate_wrong_answers(pct_increase, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = random.randint(5, 60)
            if w != pct_increase and w not in wrong:
                wrong.append(w)
        
        answer_str = f"{int(pct_increase)}%" if pct_increase == int(pct_increase) else f"{pct_increase}%"
        wrong_strs = [f"{int(w)}%" if w == int(w) else f"{w}%" for w in wrong[:3]]
        
        options = [answer_str] + wrong_strs
        random.shuffle(options)
        correct_idx = options.index(answer_str)
        
        questions.append({
            'question_text': f"The {ctx[0]} {ctx[1]} {prefix}{original} {ctx[2]} {prefix}{new}. Calculate the percentage increase.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Increase = {new} - {original} = {new - original}. Percentage increase = ({new - original} ÷ {original}) × 100 = {pct_increase}%",
            'image_svg': svg
        })
    
    return questions

def generate_level_7():
    """Level 7: Percentage decrease/discount (SEC HL Q1(b) style)"""
    questions = []
    
    discount_contexts = [
        ("jacket", "reduced from", "to"), ("laptop", "discounted from", "to"),
        ("holiday package", "reduced from", "to"), ("TV", "on sale from", "to"),
        ("bike", "reduced from", "to"), ("phone", "discounted from", "to")
    ]
    
    decrease_combos = [
        (100, 80, 20), (100, 75, 25), (100, 90, 10), (100, 70, 30),
        (200, 150, 25), (200, 160, 20), (150, 120, 20), (80, 60, 25),
        (140, 98, 30), (120, 90, 25), (250, 200, 20), (500, 400, 20)
    ]
    
    for i in range(35):
        original, sale, pct_decrease = random.choice(decrease_combos)
        ctx = random.choice(discount_contexts)
        
        svg = generate_price_tag_svg(original, sale, pct_decrease)
        
        common_mistake = round((original - sale) / sale * 100, 1)
        candidates = [pct_decrease + 5, pct_decrease - 5, common_mistake, 100 - pct_decrease]
        wrong = generate_wrong_answers(pct_decrease, [c for c in candidates if 0 < c < 100])
        
        while len(wrong) < 3:
            w = random.randint(5, 50)
            if w != pct_decrease and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(pct_decrease, wrong, "{}%")
        
        questions.append({
            'question_text': f"A {ctx[0]} is {ctx[1]} €{original:.2f} {ctx[2]} €{sale:.2f}. Calculate the percentage discount.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Discount = €{original:.2f} - €{sale:.2f} = €{original - sale:.2f}. Percentage discount = ({original - sale:.2f} ÷ {original:.2f}) × 100 = {pct_decrease}%",
            'image_svg': svg
        })
    
    # Calculate sale price (15 questions)
    for i in range(15):
        original = random.choice([50, 80, 100, 120, 150, 200, 250, 300])
        discount_pct = random.choice([10, 15, 20, 25, 30, 40])
        sale_price = original * (100 - discount_pct) / 100
        
        candidates = [original - discount_pct, original * discount_pct / 100, sale_price + 10, original]
        wrong = generate_wrong_answers(sale_price, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = sale_price + random.randint(-20, 20)
            if w > 0 and w != sale_price and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(sale_price, wrong, "€{:.2f}")
        
        questions.append({
            'question_text': f"A coat originally costs €{original:.2f}. It is reduced by {discount_pct}%. What is the sale price?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Discount amount = {discount_pct}% of €{original:.2f} = €{original * discount_pct / 100:.2f}. Sale price = €{original:.2f} - €{original * discount_pct / 100:.2f} = €{sale_price:.2f}",
            'image_svg': None
        })
    
    return questions

def generate_level_8():
    """Level 8: Percentage change comparison (SEC HL Q2(e) style)"""
    questions = []
    
    scenarios = [("Shop A", "Shop B"), ("Company X", "Company Y"), ("Month 1", "Month 2"), ("Team A", "Team B")]
    
    for i in range(30):
        scenario = random.choice(scenarios)
        
        change1_orig = random.choice([100, 150, 200, 250])
        change1_pct = random.choice([10, 15, 20, 25, 30])
        change1_new = int(change1_orig * (100 + change1_pct) / 100)
        
        change2_orig = random.choice([80, 120, 160, 200])
        change2_pct = random.choice([12, 18, 22, 28, 35])
        change2_new = int(change2_orig * (100 + change2_pct) / 100)
        
        while change2_pct == change1_pct:
            change2_pct = random.choice([12, 18, 22, 28, 35])
            change2_new = int(change2_orig * (100 + change2_pct) / 100)
        
        greater = scenario[0] if change1_pct > change2_pct else scenario[1]
        other = scenario[1] if greater == scenario[0] else scenario[0]
        
        options = [greater, other, "Both equal", "Cannot determine"]
        random.shuffle(options)
        correct_idx = options.index(greater)
        
        questions.append({
            'question_text': f"{scenario[0]} sales went from {change1_orig} to {change1_new}. {scenario[1]} sales went from {change2_orig} to {change2_new}. Which had the greater percentage increase?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{scenario[0]}: ({change1_new} - {change1_orig}) ÷ {change1_orig} × 100 = {change1_pct}%. {scenario[1]}: ({change2_new} - {change2_orig}) ÷ {change2_orig} × 100 = {change2_pct}%. {greater} had the greater increase.",
            'image_svg': None
        })
    
    # Difference in percentage changes (20 questions)
    for i in range(20):
        orig1, new1 = random.choice([(100, 125), (200, 250), (80, 100), (150, 180)])
        orig2, new2 = random.choice([(100, 115), (200, 230), (80, 92), (150, 165)])
        
        pct1 = round((new1 - orig1) / orig1 * 100)
        pct2 = round((new2 - orig2) / orig2 * 100)
        diff = abs(pct1 - pct2)
        
        candidates = [pct1, pct2, diff + 5, diff + 10]
        wrong = generate_wrong_answers(diff, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = diff + random.randint(-5, 10)
            if w > 0 and w != diff and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(diff, wrong, "{}%")
        
        questions.append({
            'question_text': f"Product A increased from {orig1} to {new1}. Product B increased from {orig2} to {new2}. What is the difference between their percentage increases?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"A: ({new1}-{orig1})/{orig1} × 100 = {pct1}%. B: ({new2}-{orig2})/{orig2} × 100 = {pct2}%. Difference = |{pct1}% - {pct2}%| = {diff}%",
            'image_svg': None
        })
    
    return questions

def generate_level_9():
    """Level 9: Profit and loss percentage (SEC OL Q9(d), HL Q4(b) style)"""
    questions = []
    
    profit_combos = [
        (100, 120, 20), (100, 125, 25), (80, 100, 25), (200, 250, 25),
        (150, 180, 20), (320, 400, 25), (250, 300, 20), (400, 500, 25)
    ]
    
    # Profit scenarios (25 questions)
    for i in range(25):
        cost, sell, profit_pct = random.choice(profit_combos)
        profit = sell - cost
        
        common_mistake = round(profit / sell * 100)
        candidates = [profit_pct + 5, profit_pct - 5, common_mistake, profit]
        wrong = generate_wrong_answers(profit_pct, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = random.randint(10, 40)
            if w != profit_pct and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(profit_pct, wrong, "{}%")
        
        questions.append({
            'question_text': f"A trader bought an item for €{cost} and sold it for €{sell}. Calculate the profit as a percentage of the cost price.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Profit = €{sell} - €{cost} = €{profit}. Profit % = (€{profit} ÷ €{cost}) × 100 = {profit_pct}%",
            'image_svg': None
        })
    
    # Loss scenarios (25 questions)
    loss_combos = [
        (100, 80, 20), (100, 75, 25), (120, 96, 20), (150, 120, 20),
        (200, 160, 20), (250, 200, 20), (300, 240, 20), (400, 320, 20)
    ]
    
    for i in range(25):
        cost, sell, loss_pct = random.choice(loss_combos)
        loss = cost - sell
        
        common_mistake = round(loss / sell * 100)
        candidates = [loss_pct + 5, loss_pct - 5, common_mistake, loss]
        wrong = generate_wrong_answers(loss_pct, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = random.randint(10, 40)
            if w != loss_pct and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(loss_pct, wrong, "{}%")
        
        questions.append({
            'question_text': f"An item was bought for €{cost} and sold for €{sell}. Calculate the loss as a percentage of the cost price.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Loss = €{cost} - €{sell} = €{loss}. Loss % = (€{loss} ÷ €{cost}) × 100 = {loss_pct}%",
            'image_svg': None
        })
    
    return questions

def generate_level_10():
    """Level 10: Reverse percentage - find original (Higher)"""
    questions = []
    
    # Find original after increase (25 questions)
    combos = [
        (10, 110, 100), (20, 120, 100), (25, 125, 100), (50, 150, 100),
        (10, 132, 120), (20, 144, 120), (25, 150, 120), (20, 180, 150),
        (10, 220, 200), (25, 250, 200), (15, 230, 200), (20, 240, 200)
    ]
    
    for i in range(25):
        pct, final, original = random.choice(combos)
        
        # Common mistake: final - pct% of final
        common_mistake = int(final - (final * pct / 100))
        candidates = [common_mistake, final - pct, original + 10, original - 10]
        wrong = generate_wrong_answers(original, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = original + random.randint(-20, 20)
            if w > 0 and w != original and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(original, wrong, "€{}")
        
        questions.append({
            'question_text': f"The price after a {pct}% increase is €{final}. What was the original price?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Let original = x. After {pct}% increase: x × {1 + pct/100} = {final}. So x = {final} ÷ {1 + pct/100} = €{original}",
            'image_svg': None
        })
    
    # Find original after decrease (25 questions)
    dec_combos = [
        (10, 90, 100), (20, 80, 100), (25, 75, 100), (50, 50, 100),
        (10, 108, 120), (20, 96, 120), (25, 90, 120), (20, 120, 150),
        (10, 180, 200), (25, 150, 200), (15, 170, 200), (20, 160, 200)
    ]
    
    for i in range(25):
        pct, final, original = random.choice(dec_combos)
        
        common_mistake = int(final + (final * pct / 100))
        candidates = [common_mistake, final + pct, original + 10, original - 10]
        wrong = generate_wrong_answers(original, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = original + random.randint(-20, 20)
            if w > 0 and w != original and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(original, wrong, "€{}")
        
        questions.append({
            'question_text': f"The price after a {pct}% discount is €{final}. What was the original price?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Let original = x. After {pct}% decrease: x × {1 - pct/100} = {final}. So x = {final} ÷ {1 - pct/100} = €{original}",
            'image_svg': None
        })
    
    return questions

def generate_level_11():
    """Level 11: Simple interest (SEC OL Q9(c) style)"""
    questions = []
    
    # Find interest earned (20 questions)
    for i in range(20):
        principal = random.choice([100, 200, 500, 1000, 1500, 2000, 3000, 5000])
        rate = random.choice([2, 3, 4, 5, 6, 8])
        time = random.choice([1, 2, 3, 4, 5])
        
        interest = principal * rate * time / 100
        
        candidates = [principal * rate / 100, interest + principal, interest * 2, rate * time]
        wrong = generate_wrong_answers(interest, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = interest + random.randint(-50, 50)
            if w > 0 and w != interest and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(interest, wrong, "€{:.2f}")
        
        questions.append({
            'question_text': f"€{principal} is invested at {rate}% simple interest per year for {time} year{'s' if time > 1 else ''}. How much interest is earned?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Simple Interest = P × r × t = €{principal} × {rate}/100 × {time} = €{interest:.2f}",
            'image_svg': None
        })
    
    # Find rate (15 questions) - SEC style
    for i in range(15):
        principal = random.choice([100, 120, 150, 200, 500, 1000])
        rate = random.choice([2, 3, 3.5, 4, 4.5, 5])
        time = 1
        
        final = principal + (principal * rate * time / 100)
        
        candidates = [rate + 1, rate - 0.5, rate + 0.5, rate * 2]
        wrong = generate_wrong_answers(rate, [round(c, 1) for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = round(rate + random.uniform(-2, 2), 1)
            if w > 0 and w != rate and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(rate, wrong, "{}%")
        
        questions.append({
            'question_text': f"€{principal:.2f} was invested for {time} year and grew to €{final:.2f}. What was the annual interest rate?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Interest earned = €{final:.2f} - €{principal:.2f} = €{final - principal:.2f}. Rate = (Interest ÷ Principal) × 100 = ({final - principal:.2f} ÷ {principal:.2f}) × 100 = {rate}%",
            'image_svg': None
        })
    
    # Find total amount (15 questions)
    for i in range(15):
        principal = random.choice([500, 1000, 1500, 2000, 3000, 5000])
        rate = random.choice([3, 4, 5, 6, 8])
        time = random.choice([2, 3, 4, 5])
        
        interest = principal * rate * time / 100
        total = principal + interest
        
        candidates = [principal + (principal * rate / 100), interest, total + 100]
        wrong = generate_wrong_answers(total, [c for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = total + random.randint(-200, 200)
            if w > 0 and w != total and w not in wrong:
                wrong.append(w)
        
        options, correct_idx = format_options(total, wrong, "€{:.2f}")
        
        questions.append({
            'question_text': f"€{principal} is invested at {rate}% simple interest per year for {time} years. What is the total amount at the end?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Interest = €{principal} × {rate}% × {time} = €{interest:.2f}. Total = €{principal} + €{interest:.2f} = €{total:.2f}",
            'image_svg': None
        })
    
    return questions

def generate_level_12():
    """Level 12: Compound interest and VAT (SEC HL style - Mastery)"""
    questions = []
    
    # Compound interest (25 questions)
    for i in range(25):
        principal = random.choice([1000, 2000, 5000, 10000])
        rate = random.choice([5, 6, 8, 10])
        years = random.choice([2, 3])
        
        amount = principal * ((1 + rate/100) ** years)
        amount = round(amount, 2)
        
        # Simple interest for comparison (common wrong answer)
        simple = principal + (principal * rate * years / 100)
        
        candidates = [simple, principal * (1 + rate/100), amount + 100, amount - 50]
        wrong = generate_wrong_answers(amount, [round(c, 2) for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = amount + random.randint(-200, 200)
            if w > 0 and round(w, 2) != amount and w not in wrong:
                wrong.append(round(w, 2))
        
        options, correct_idx = format_options(amount, wrong, "€{:.2f}")
        
        questions.append({
            'question_text': f"€{principal} is invested at {rate}% compound interest per year for {years} years. What is the total amount?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"A = P(1 + r)^n = €{principal} × (1 + {rate}/100)^{years} = €{principal} × {(1 + rate/100):.2f}^{years} = €{amount:.2f}",
            'image_svg': None
        })
    
    # VAT calculations (25 questions)
    vat_rate = 23
    
    for i in range(15):
        net_price = random.choice([50, 75, 100, 150, 200, 250, 300, 400, 500])
        gross_price = round(net_price * (1 + vat_rate/100), 2)
        
        candidates = [net_price + vat_rate, net_price * vat_rate / 100, gross_price + 10]
        wrong = generate_wrong_answers(gross_price, [round(c, 2) for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = gross_price + random.randint(-30, 30)
            if w > 0 and round(w, 2) != gross_price and w not in wrong:
                wrong.append(round(w, 2))
        
        options, correct_idx = format_options(gross_price, wrong, "€{:.2f}")
        
        questions.append({
            'question_text': f"An item costs €{net_price:.2f} before VAT. Calculate the price including {vat_rate}% VAT.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Price with VAT = €{net_price:.2f} × (1 + {vat_rate}/100) = €{net_price:.2f} × 1.{vat_rate} = €{gross_price:.2f}",
            'image_svg': None
        })
    
    # Find original price before VAT (10 questions)
    for i in range(10):
        gross = random.choice([61.50, 73.80, 98.40, 123, 147.60, 184.50, 221.40, 307.50, 369, 492])
        net = round(gross / 1.23, 2)
        
        candidates = [gross - vat_rate, gross * 0.77, gross - (gross * 0.23)]
        wrong = generate_wrong_answers(net, [round(c, 2) for c in candidates if c > 0])
        
        while len(wrong) < 3:
            w = net + random.randint(-20, 20)
            if w > 0 and round(w, 2) != net and w not in wrong:
                wrong.append(round(w, 2))
        
        options, correct_idx = format_options(net, wrong, "€{:.2f}")
        
        questions.append({
            'question_text': f"An item costs €{gross:.2f} including {vat_rate}% VAT. What is the price before VAT?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Price before VAT = €{gross:.2f} ÷ 1.{vat_rate} = €{net:.2f}",
            'image_svg': None
        })
    
    return questions

# ============== VALIDATION ==============

def validate_questions(questions, level):
    """Validate questions meet requirements"""
    errors = []
    
    for i, q in enumerate(questions):
        required = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_idx', 'explanation']
        for field in required:
            if field not in q or q[field] is None:
                errors.append(f"Level {level}, Q{i+1}: Missing {field}")
        
        if q.get('correct_idx') not in [0, 1, 2, 3]:
            errors.append(f"Level {level}, Q{i+1}: Invalid correct_idx {q.get('correct_idx')}")
        
        options = [q.get('option_a'), q.get('option_b'), q.get('option_c'), q.get('option_d')]
        if len(set(options)) != 4:
            errors.append(f"Level {level}, Q{i+1}: Duplicate options: {options}")
        
        if not q.get('explanation') or len(q.get('explanation', '')) < 10:
            errors.append(f"Level {level}, Q{i+1}: Explanation too short")
    
    return errors

# ============== MAIN ==============

def main():
    print("=" * 60)
    print("AgentMath Percentages Question Generator v1")
    print("=" * 60)
    
    generators = {
        1: generate_level_1, 2: generate_level_2, 3: generate_level_3,
        4: generate_level_4, 5: generate_level_5, 6: generate_level_6,
        7: generate_level_7, 8: generate_level_8, 9: generate_level_9,
        10: generate_level_10, 11: generate_level_11, 12: generate_level_12
    }
    
    all_questions = []
    all_errors = []
    
    for level in range(1, 13):
        print(f"\nGenerating Level {level} ({DIFFICULTY_BANDS[level]})...")
        
        questions = generators[level]()
        
        if len(questions) < QUESTIONS_PER_LEVEL:
            print(f"  Warning: Only {len(questions)} questions, padding...")
            while len(questions) < QUESTIONS_PER_LEVEL:
                questions.append(questions[len(questions) % len(questions)].copy())
        elif len(questions) > QUESTIONS_PER_LEVEL:
            questions = questions[:QUESTIONS_PER_LEVEL]
        
        errors = validate_questions(questions, level)
        if errors:
            all_errors.extend(errors)
            print(f"  ⚠️  {len(errors)} validation errors")
        
        for q in questions:
            q['topic'] = TOPIC
            q['difficulty'] = level
            q['difficulty_band'] = DIFFICULTY_BANDS[level]
            q['mode'] = MODE
        
        all_questions.extend(questions)
        print(f"  ✓ {len(questions)} questions generated")
    
    if all_errors:
        print(f"\n⚠️  Total validation errors: {len(all_errors)}")
        for error in all_errors[:10]:
            print(f"  - {error}")
    
    print(f"\n📊 Total questions generated: {len(all_questions)}")
    
    # Deduplicate questions (by topic + level + question_text)
    seen = set()
    unique_questions = []
    duplicates_removed = 0
    for q in all_questions:
        key = (q['topic'], q['difficulty'], q['question_text'])
        if key not in seen:
            seen.add(key)
            unique_questions.append(q)
        else:
            duplicates_removed += 1
    
    if duplicates_removed > 0:
        print(f"⚠️  Removed {duplicates_removed} duplicate questions")
        all_questions = unique_questions
        print(f"📊 Unique questions: {len(all_questions)}")
    
    # Save to JSON for transfer
    with open('percentages_questions.json', 'w') as f:
        json.dump(all_questions, f, indent=2)
    print("✓ Saved to percentages_questions.json")
    
    # Try database if available
    if os.path.exists(DB_PATH):
        print(f"\n📁 Database found: {DB_PATH}")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Debug: Check what topics exist
        cursor.execute("SELECT topic, COUNT(*) FROM questions_adaptive GROUP BY topic")
        existing = cursor.fetchall()
        if existing:
            print("  Existing topics in DB:", [(r[0], r[1]) for r in existing])
        
        # Delete ALL existing questions for this topic (regardless of mode)
        # This avoids UNIQUE constraint issues if questions exist with different mode
        cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (TOPIC,))
        conn.commit()  # Commit the delete before inserting
        print(f"  Deleted {cursor.rowcount} existing questions for topic '{TOPIC}'")
        
        # Column names must match the actual database schema:
        # correct_answer (not correct_idx), difficulty_level (not difficulty)
        insert_sql = """
            INSERT INTO questions_adaptive 
            (question_text, option_a, option_b, option_c, option_d, correct_answer, 
             topic, difficulty_level, difficulty_band, mode, explanation, image_svg, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """
        
        inserted = 0
        errors = 0
        for q in all_questions:
            try:
                cursor.execute(insert_sql, (
                    q['question_text'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                    q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'],
                    q['mode'], q.get('explanation', ''), q.get('image_svg')
                ))
                inserted += 1
            except Exception as e:
                errors += 1
                if errors <= 3:  # Show first 3 errors
                    print(f"  ⚠️ Error inserting L{q['difficulty']}: {str(e)[:80]}")
                    print(f"     Question: {q['question_text'][:60]}...")
        
        conn.commit()
        print(f"\n  ✓ Inserted {inserted} questions, {errors} errors")
        
        cursor.execute("""
            SELECT difficulty_level, COUNT(*) FROM questions_adaptive 
            WHERE topic = ? AND mode = ? GROUP BY difficulty_level ORDER BY difficulty_level
        """, (TOPIC, MODE))
        
        print("\n📊 Database verification:")
        for row in cursor.fetchall():
            print(f"  Level {row[0]}: {row[1]} questions")
        
        conn.close()
    
    print("\n✅ Percentages questions generated successfully!")

if __name__ == "__main__":
    main()
