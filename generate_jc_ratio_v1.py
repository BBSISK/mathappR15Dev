#!/usr/bin/env python3
"""
AgentMath - Ratio Topic Generator v1
SEC Junior Cycle Mathematics - Adaptive Quiz System

Generates 600 questions (50 per level × 12 levels) for the Ratio topic.
Aligned with SEC Junior Cycle Mathematics Specification.

Level Structure:
  Level 1:  Understanding Ratios (Foundation)
  Level 2:  Simplifying Ratios (Foundation)
  Level 3:  Equivalent Ratios (Foundation)
  Level 4:  Sharing in a Ratio - Two Parts (Ordinary)
  Level 5:  Sharing in a Ratio - Three Parts (Ordinary)
  Level 6:  Finding Total from One Part (Ordinary)
  Level 7:  Ratio with Quantities (Higher)
  Level 8:  Mixing Problems (Higher)
  Level 9:  Ratio with Fractions (Higher)
  Level 10: Reverse Ratio Problems (Higher)
  Level 11: Real-world Applications (Application)
  Level 12: Multi-step Ratio Problems (Mastery)

SEC Reference Questions:
  - 2023 OL Q10(b): Share €60 in ratio 3:2
  - 2024 HL Q4(a): Orange drink water:juice 7:3, 2 litres
  - 2025 OL Q2(b): Divide €13.40 in ratio 3:2
  - 2025 HL Q7(c): Ratio with fractions 1 : 3/2 : 5/3

Author: AgentMath Generator
Version: 1.0
Date: December 2025
"""

import random
import sqlite3
import os
import math
from fractions import Fraction

# ============================================================
# SVG VISUAL GENERATORS
# ============================================================

def generate_ratio_bar_svg(ratio_parts, labels=None, total=None, unit=''):
    """Generate SVG showing ratio as proportional bars"""
    colors = ['#3b82f6', '#ef4444', '#22c55e', '#f59e0b', '#8b5cf6']
    total_parts = sum(ratio_parts)
    
    bar_width = 280
    bar_height = 40
    svg_width = 320
    svg_height = 100 + (len(ratio_parts) * 25)
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#f0f9ff" rx="8"/>'
    
    # Title
    ratio_str = ':'.join(map(str, ratio_parts))
    svg += f'<text x="{svg_width/2}" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">Ratio {ratio_str}</text>'
    
    # Draw proportional bar
    x_offset = 20
    y_offset = 35
    current_x = x_offset
    
    for i, parts in enumerate(ratio_parts):
        width = (parts / total_parts) * bar_width
        color = colors[i % len(colors)]
        svg += f'<rect x="{current_x}" y="{y_offset}" width="{width}" height="{bar_height}" fill="{color}" stroke="#1e3a8a" stroke-width="1"/>'
        
        # Part label inside bar
        if width > 25:
            svg += f'<text x="{current_x + width/2}" y="{y_offset + bar_height/2 + 5}" text-anchor="middle" font-size="12" font-weight="bold" fill="white">{parts}</text>'
        
        current_x += width
    
    # Labels below
    if labels:
        y_label = y_offset + bar_height + 20
        current_x = x_offset
        for i, (parts, label) in enumerate(zip(ratio_parts, labels)):
            width = (parts / total_parts) * bar_width
            color = colors[i % len(colors)]
            svg += f'<circle cx="{current_x + 8}" cy="{y_label}" r="6" fill="{color}"/>'
            svg += f'<text x="{current_x + 20}" y="{y_label + 4}" font-size="11" fill="#1e3a8a">{label}</text>'
            current_x += width
    
    # Total if provided
    if total:
        svg += f'<text x="{svg_width/2}" y="{svg_height - 10}" text-anchor="middle" font-size="12" fill="#374151">Total: {total}{unit}</text>'
    
    svg += '</svg>'
    return svg


def generate_sharing_svg(names, amounts, unit='€'):
    """Generate SVG showing how amount is shared between people"""
    svg_width = 280
    svg_height = 60 + len(names) * 35
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#fef3c7" rx="8"/>'
    
    colors = ['#3b82f6', '#ef4444', '#22c55e', '#f59e0b']
    
    for i, (name, amount) in enumerate(zip(names, amounts)):
        y = 30 + i * 35
        color = colors[i % len(colors)]
        
        # Person icon
        svg += f'<circle cx="30" cy="{y}" r="12" fill="{color}"/>'
        svg += f'<text x="30" y="{y+4}" text-anchor="middle" font-size="10" fill="white">👤</text>'
        
        # Name and amount
        svg += f'<text x="50" y="{y+5}" font-size="13" font-weight="bold" fill="#1e3a8a">{name}:</text>'
        svg += f'<text x="130" y="{y+5}" font-size="13" fill="#047857">{unit}{amount}</text>'
    
    svg += '</svg>'
    return svg


def generate_mixture_svg(ingredients, amounts, unit='ml'):
    """Generate SVG showing mixture/recipe with quantities"""
    svg_width = 260
    svg_height = 80 + len(ingredients) * 30
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#ecfdf5" rx="8"/>'
    
    # Beaker/container
    svg += f'<rect x="180" y="20" width="60" height="80" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2" rx="5"/>'
    svg += f'<ellipse cx="210" cy="20" rx="30" ry="8" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/>'
    
    colors = ['#3b82f6', '#f59e0b', '#22c55e']
    
    for i, (ingredient, amount) in enumerate(zip(ingredients, amounts)):
        y = 35 + i * 30
        color = colors[i % len(colors)]
        
        svg += f'<rect x="15" y="{y-8}" width="12" height="12" fill="{color}" rx="2"/>'
        svg += f'<text x="35" y="{y+3}" font-size="12" fill="#1e3a8a">{ingredient}: {amount} {unit}</text>'
    
    total = sum(amounts)
    svg += f'<text x="{svg_width/2}" y="{svg_height - 12}" text-anchor="middle" font-size="11" font-weight="bold" fill="#374151">Total: {total} {unit}</text>'
    
    svg += '</svg>'
    return svg


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def simplify_ratio(a, b):
    """Simplify a ratio a:b to lowest terms"""
    from math import gcd
    g = gcd(a, b)
    return a // g, b // g


def simplify_ratio_three(a, b, c):
    """Simplify a ratio a:b:c to lowest terms"""
    from math import gcd
    g = gcd(gcd(a, b), c)
    return a // g, b // g, c // g


def format_number(n, decimals=None):
    """Format number - remove .0 from whole numbers"""
    if decimals is not None:
        n = round(n, decimals)
    if isinstance(n, float) and n == int(n):
        return str(int(n))
    if isinstance(n, float):
        return f"{n:.2f}".rstrip('0').rstrip('.')
    return str(n)


def generate_unique_options(correct_answer, num_options=4, min_val=None, decimal_places=None):
    """Generate unique answer options including the correct answer"""
    if decimal_places is not None:
        correct_answer = round(correct_answer, decimal_places)
    
    options = [correct_answer]
    avoid = {correct_answer}
    
    attempts = 0
    while len(options) < num_options and attempts < 100:
        attempts += 1
        
        if isinstance(correct_answer, (int, float)):
            strategies = [
                correct_answer * random.choice([0.5, 0.8, 1.2, 1.5, 2]),
                correct_answer + random.randint(-10, 10),
                correct_answer - random.randint(1, max(5, int(correct_answer * 0.3))),
            ]
            wrong = random.choice(strategies)
            
            if decimal_places is not None:
                wrong = round(wrong, decimal_places)
            elif isinstance(correct_answer, int):
                wrong = int(wrong)
        else:
            wrong = correct_answer + random.randint(-5, 5)
        
        if min_val is not None and wrong < min_val:
            wrong = min_val + random.randint(1, 5)
        
        if wrong not in avoid and wrong > 0:
            options.append(wrong)
            avoid.add(wrong)
    
    while len(options) < num_options:
        filler = correct_answer + len(options) * 3
        if filler not in avoid:
            options.append(filler)
            avoid.add(filler)
    
    random.shuffle(options)
    return options, options.index(correct_answer)


# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1(num_questions=50):
    """Level 1: Understanding Ratios (Foundation)"""
    questions = []
    used_questions = set()
    
    templates = [
        "There are {a} red balls and {b} blue balls.\nWrite this as a ratio of red to blue.",
        "A class has {a} boys and {b} girls.\nWhat is the ratio of boys to girls?",
        "In a bag there are {a} apples and {b} oranges.\nWrite the ratio of apples to oranges.",
        "A recipe uses {a} cups of flour and {b} cups of sugar.\nWhat is the ratio of flour to sugar?",
        "{a} students walk to school and {b} take the bus.\nWrite this as a ratio (walk : bus).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        a = random.randint(2, 15)
        b = random.randint(2, 15)
        while a == b:  # Ensure a != b to avoid duplicate options
            b = random.randint(2, 15)
        
        template = random.choice(templates)
        question_text = template.format(a=a, b=b)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        correct = f"{a}:{b}"
        
        # Generate wrong options - ensure all are unique
        wrong_set = set()
        wrong_set.add(f"{b}:{a}")  # Reversed
        wrong_set.add(f"{a+1}:{b}")
        wrong_set.add(f"{a}:{b+1}")
        wrong_set.add(f"{a-1}:{b}" if a > 2 else f"{a+2}:{b}")
        wrong_set.add(f"{a}:{b-1}" if b > 2 else f"{a}:{b+2}")
        wrong_set.discard(correct)  # Remove if accidentally matches
        
        wrong_options = list(wrong_set)[:3]
        
        options = [correct] + wrong_options
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        svg = generate_ratio_bar_svg([a, b])
        
        explanation = f"Count each type:\n"
        explanation += f"First type: {a}\n"
        explanation += f"Second type: {b}\n"
        explanation += f"Ratio = {a}:{b}"
        
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


def generate_level_2(num_questions=50):
    """Level 2: Simplifying Ratios (Foundation)"""
    questions = []
    used_questions = set()
    
    templates = [
        "Simplify the ratio {a}:{b} to its lowest terms.",
        "Write {a}:{b} in its simplest form.",
        "Express the ratio {a}:{b} in lowest terms.",
        "Reduce {a}:{b} to its simplest form.",
    ]
    
    # Generate ratios that can be simplified
    simplifiable = [
        (4, 6), (6, 9), (8, 12), (10, 15), (12, 16),
        (6, 8), (9, 12), (10, 20), (15, 20), (12, 18),
        (14, 21), (16, 24), (18, 27), (20, 30), (24, 36),
        (8, 10), (6, 10), (12, 8), (15, 10), (21, 14),
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        a, b = random.choice(simplifiable)
        if random.random() < 0.3:
            a, b = b, a  # Sometimes swap
        
        template = random.choice(templates)
        question_text = template.format(a=a, b=b)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        sa, sb = simplify_ratio(a, b)
        correct = f"{sa}:{sb}"
        
        wrong_options = [
            f"{sb}:{sa}",
            f"{sa+1}:{sb}",
            f"{a}:{b}",  # Not simplified
            f"{sa}:{sb+1}",
        ]
        
        options = [correct] + wrong_options[:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        svg = generate_ratio_bar_svg([sa, sb])
        
        from math import gcd
        g = gcd(a, b)
        explanation = f"Find the HCF of {a} and {b}: {g}\n"
        explanation += f"Divide both by {g}:\n"
        explanation += f"{a} ÷ {g} = {sa}\n"
        explanation += f"{b} ÷ {g} = {sb}\n"
        explanation += f"Simplified ratio = {sa}:{sb}"
        
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


def generate_level_3(num_questions=50):
    """Level 3: Equivalent Ratios (Foundation)"""
    questions = []
    used_questions = set()
    
    templates = [
        "The ratio {a}:{b} is equivalent to {c}:?\nFind the missing number.",
        "If {a}:{b} = {c}:x, what is x?",
        "Complete the equivalent ratio: {a}:{b} = {c}:?",
        "Find the missing value: {a}:{b} = {c}:□",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        multiplier = random.randint(2, 5)
        c = a * multiplier
        correct = b * multiplier
        
        template = random.choice(templates)
        question_text = template.format(a=a, b=b, c=c)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_ratio_bar_svg([a, b])
        
        explanation = f"To get from {a} to {c}, multiply by {multiplier}\n"
        explanation += f"So multiply {b} by {multiplier} too:\n"
        explanation += f"{b} × {multiplier} = {correct}"
        
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


def generate_level_4(num_questions=50):
    """Level 4: Sharing in a Ratio - Two Parts (Ordinary) - SEC 2023 OL Q10(b), 2025 OL Q2(b)"""
    questions = []
    used_questions = set()
    
    names_pairs = [
        ('Liam', 'Ciara'), ('Noah', 'Amy'), ('Sean', 'Emma'),
        ('Jack', 'Sophie'), ('Conor', 'Aoife'), ('Oisin', 'Niamh'),
    ]
    
    templates = [
        "{n1} and {n2} share €{total} in the ratio {a}:{b}.\nHow much does {n1} get?",
        "€{total} is divided between {n1} and {n2} in the ratio {a}:{b}.\nWhat does {n2} receive?",
        "{n1} and {n2} share €{total} in the ratio {a}:{b}.\nHow much does each person get? (Answer for {n1})",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        n1, n2 = random.choice(names_pairs)
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        while a == b:
            b = random.randint(2, 5)
        
        total_parts = a + b
        multiplier = random.randint(5, 20)
        total = total_parts * multiplier
        
        template = random.choice(templates)
        ask_first = 'n1' in template.split('?')[0].split('.')[-1] if '?' in template else True
        
        question_text = template.format(n1=n1, n2=n2, total=total, a=a, b=b)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        if ask_first or n1 in template.split('Answer for')[-1]:
            correct = a * multiplier
            person = n1
        else:
            correct = b * multiplier
            person = n2
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_sharing_svg([n1, n2], [a * multiplier, b * multiplier])
        
        explanation = f"Total parts = {a} + {b} = {total_parts}\n"
        explanation += f"One part = €{total} ÷ {total_parts} = €{multiplier}\n"
        explanation += f"{n1} gets {a} parts = {a} × €{multiplier} = €{a * multiplier}\n"
        explanation += f"{n2} gets {b} parts = {b} × €{multiplier} = €{b * multiplier}"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"€{int(options[0])}",
            'option_b': f"€{int(options[1])}",
            'option_c': f"€{int(options[2])}",
            'option_d': f"€{int(options[3])}",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_5(num_questions=50):
    """Level 5: Sharing in a Ratio - Three Parts (Ordinary)"""
    questions = []
    used_questions = set()
    
    names_triples = [
        ('Anna', 'Ben', 'Clara'), ('David', 'Emma', 'Finn'),
        ('Grace', 'Harry', 'Ivy'), ('Jack', 'Kate', 'Leo'),
    ]
    
    templates = [
        "{n1}, {n2} and {n3} share €{total} in the ratio {a}:{b}:{c}.\nHow much does {n2} get?",
        "€{total} is divided between {n1}, {n2} and {n3} in the ratio {a}:{b}:{c}.\nWhat does {n1} receive?",
        "Three friends share €{total} in ratio {a}:{b}:{c}.\n{n3} receives how much?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        n1, n2, n3 = random.choice(names_triples)
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 4)
        
        total_parts = a + b + c
        multiplier = random.randint(5, 15)
        total = total_parts * multiplier
        
        template = random.choice(templates)
        question_text = template.format(n1=n1, n2=n2, n3=n3, total=total, a=a, b=b, c=c)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine who we're asking about
        if n1 in template.split('?')[0].split('.')[-1]:
            correct = a * multiplier
        elif n2 in template.split('?')[0].split('.')[-1]:
            correct = b * multiplier
        else:
            correct = c * multiplier
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_sharing_svg([n1, n2, n3], [a * multiplier, b * multiplier, c * multiplier])
        
        explanation = f"Total parts = {a} + {b} + {c} = {total_parts}\n"
        explanation += f"One part = €{total} ÷ {total_parts} = €{multiplier}\n"
        explanation += f"{n1}: {a} × €{multiplier} = €{a * multiplier}\n"
        explanation += f"{n2}: {b} × €{multiplier} = €{b * multiplier}\n"
        explanation += f"{n3}: {c} × €{multiplier} = €{c * multiplier}"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"€{int(options[0])}",
            'option_b': f"€{int(options[1])}",
            'option_c': f"€{int(options[2])}",
            'option_d': f"€{int(options[3])}",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_6(num_questions=50):
    """Level 6: Finding Total from One Part (Ordinary)"""
    questions = []
    used_questions = set()
    
    templates = [
        "Two amounts are in the ratio {a}:{b}.\nThe smaller amount is €{smaller}.\nFind the total.",
        "In a ratio of {a}:{b}, the larger amount is €{larger}.\nWhat is the total amount?",
        "Money is shared in ratio {a}:{b}.\nOne person gets €{amount} ({parts} parts).\nFind the total shared.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        while a == b:
            b = random.randint(2, 5)
        
        multiplier = random.randint(10, 30)
        
        if random.random() < 0.5:
            # Give smaller amount
            smaller_parts = min(a, b)
            smaller = smaller_parts * multiplier
            template = templates[0]
            question_text = template.format(a=a, b=b, smaller=smaller)
        else:
            # Give larger amount
            larger_parts = max(a, b)
            larger = larger_parts * multiplier
            template = templates[1]
            question_text = template.format(a=a, b=b, larger=larger)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        total_parts = a + b
        correct = total_parts * multiplier
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_ratio_bar_svg([a, b], total=correct, unit='€')
        
        explanation = f"Total parts in ratio = {a} + {b} = {total_parts}\n"
        explanation += f"One part = €{multiplier}\n"
        explanation += f"Total = {total_parts} × €{multiplier} = €{correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"€{int(options[0])}",
            'option_b': f"€{int(options[1])}",
            'option_c': f"€{int(options[2])}",
            'option_d': f"€{int(options[3])}",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_7(num_questions=50):
    """Level 7: Ratio with Quantities (Higher) - SEC 2024 HL Q4(a)"""
    questions = []
    used_questions = set()
    
    mixtures = [
        ('water', 'orange juice', 'orange drink', 'ml'),
        ('flour', 'sugar', 'mixture', 'g'),
        ('red paint', 'blue paint', 'purple paint', 'ml'),
        ('sand', 'cement', 'mortar', 'kg'),
    ]
    
    templates = [
        "{person} makes {product} by mixing {ing1} and {ing2} in ratio {a}:{b}.\nShe makes {total} {unit} of the {product}.\nHow much {ing2} does she use?",
        "A {product} is made by mixing {ing1} and {ing2} in the ratio {a}:{b}.\nIf {total} {unit} of {product} is made, how much {ing1} is needed?",
    ]
    
    names = ['Ciara', 'Emma', 'Aoife', 'Sarah', 'Kate']
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        ing1, ing2, product, unit = random.choice(mixtures)
        person = random.choice(names)
        
        a = random.randint(2, 7)
        b = random.randint(2, 7)
        while a == b:
            b = random.randint(2, 7)
        
        total_parts = a + b
        multiplier = random.choice([100, 200, 250, 500])
        total = total_parts * multiplier
        
        template = random.choice(templates)
        question_text = template.format(person=person, ing1=ing1, ing2=ing2, 
                                       product=product, a=a, b=b, total=total, unit=unit)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine which ingredient is asked
        if ing2 in template.split('?')[0].split('much')[-1]:
            correct = b * multiplier
        else:
            correct = a * multiplier
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_mixture_svg([ing1, ing2], [a * multiplier, b * multiplier], unit)
        
        explanation = f"Total parts = {a} + {b} = {total_parts}\n"
        explanation += f"One part = {total} ÷ {total_parts} = {multiplier} {unit}\n"
        explanation += f"{ing1}: {a} × {multiplier} = {a * multiplier} {unit}\n"
        explanation += f"{ing2}: {b} × {multiplier} = {b * multiplier} {unit}"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{int(options[0])} {unit}",
            'option_b': f"{int(options[1])} {unit}",
            'option_c': f"{int(options[2])} {unit}",
            'option_d': f"{int(options[3])} {unit}",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_8(num_questions=50):
    """Level 8: Mixing Problems (Higher)"""
    questions = []
    used_questions = set()
    
    templates = [
        "A drink is made using {a} parts water to {b} parts cordial.\nIf you use {water_amt} ml of water, how much cordial is needed?",
        "Concrete is mixed in ratio {a}:{b} (sand:cement).\nUsing {sand_amt} kg of sand, how much cement is needed?",
        "Paint is mixed {a}:{b} (red:white).\nWith {given_amt} ml of {given_type}, how much {other_type} is needed?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        a = random.randint(2, 8)
        b = random.randint(1, 5)
        
        template_idx = random.randint(0, 2)
        
        if template_idx == 0:
            water_amt = a * random.randint(50, 150)
            cordial_amt = (water_amt // a) * b
            question_text = templates[0].format(a=a, b=b, water_amt=water_amt)
            correct = cordial_amt
            unit = 'ml'
        elif template_idx == 1:
            sand_amt = a * random.randint(10, 50)
            cement_amt = (sand_amt // a) * b
            question_text = templates[1].format(a=a, b=b, sand_amt=sand_amt)
            correct = cement_amt
            unit = 'kg'
        else:
            if random.random() < 0.5:
                given_type, other_type = 'red', 'white'
                given_amt = a * random.randint(20, 80)
                correct = (given_amt // a) * b
            else:
                given_type, other_type = 'white', 'red'
                given_amt = b * random.randint(20, 80)
                correct = (given_amt // b) * a
            question_text = templates[2].format(a=a, b=b, given_amt=given_amt, 
                                               given_type=given_type, other_type=other_type)
            unit = 'ml'
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_ratio_bar_svg([a, b])
        
        explanation = f"Ratio is {a}:{b}\n"
        explanation += f"Use proportion to find the answer:\n"
        explanation += f"Answer = {correct} {unit}"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{int(options[0])} {unit}",
            'option_b': f"{int(options[1])} {unit}",
            'option_c': f"{int(options[2])} {unit}",
            'option_d': f"{int(options[3])} {unit}",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_9(num_questions=50):
    """Level 9: Ratio with Fractions (Higher) - SEC 2025 HL Q7(c)"""
    questions = []
    used_questions = set()
    
    templates = [
        "Ingredients A, B and C are mixed in ratio 1 : {b_frac} : {c_frac}.\nHow many ml of B are in {total} ml of mixture?",
        "A fertiliser contains A, B, C in ratio 1 : {b_frac} : {c_frac}.\nIn {total} ml, how much B?",
        "Three ingredients in ratio 1 : {b_frac} : {c_frac}.\nFor {total} ml total, find amount of ingredient C.",
        "A mixture uses ingredients in ratio 1 : {b_frac} : {c_frac}.\nWith {total} ml total mixture, calculate amount of A.",
        "Paint is mixed in ratio 1 : {b_frac} : {c_frac} (white : red : blue).\nIn {total} ml of paint, how much red is used?",
    ]
    
    # More fraction ratios that work nicely
    fraction_combos = [
        ('3/2', '5/3', Fraction(3,2), Fraction(5,3)),
        ('1/2', '3/4', Fraction(1,2), Fraction(3,4)),
        ('2/3', '4/3', Fraction(2,3), Fraction(4,3)),
        ('3/4', '5/4', Fraction(3,4), Fraction(5,4)),
        ('1/2', '1/2', Fraction(1,2), Fraction(1,2)),
        ('1/3', '2/3', Fraction(1,3), Fraction(2,3)),
        ('2/5', '3/5', Fraction(2,5), Fraction(3,5)),
        ('3/4', '1/2', Fraction(3,4), Fraction(1,2)),
        ('1/4', '3/4', Fraction(1,4), Fraction(3,4)),
        ('5/4', '3/2', Fraction(5,4), Fraction(3,2)),
        ('2/3', '1/3', Fraction(2,3), Fraction(1,3)),
        ('4/3', '2/3', Fraction(4,3), Fraction(2,3)),
    ]
    
    totals = [120, 180, 240, 300, 360, 420, 480, 540, 600, 720, 840, 960, 1000, 1200]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 5:
        attempts += 1
        
        b_str, c_str, b_frac, c_frac = random.choice(fraction_combos)
        
        # Total parts = 1 + b_frac + c_frac
        total_frac = 1 + b_frac + c_frac
        
        # Choose total that divides nicely
        total = random.choice(totals)
        
        template = random.choice(templates)
        question_text = template.format(b_frac=b_str, c_frac=c_str, total=total)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Calculate answer based on which ingredient is asked
        one_part = total / float(total_frac)
        
        if 'ingredient C' in question_text or 'blue' in question_text:
            correct = int(round(one_part * float(c_frac)))
        elif 'amount of A' in question_text or 'white' in question_text:
            correct = int(round(one_part * 1))  # A is always 1 part
        else:  # B or red
            correct = int(round(one_part * float(b_frac)))
        
        if correct <= 0:
            continue
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_ratio_bar_svg([int(6), int(6*float(b_frac)), int(6*float(c_frac))], 
                                     labels=['A', 'B', 'C'])
        
        explanation = f"Ratio: 1 : {b_str} : {c_str}\n"
        explanation += f"Convert to same denominator and add for total parts\n"
        explanation += f"Total = {total} ml, so one unit = {one_part:.1f} ml\n"
        explanation += f"Answer = {correct} ml"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{int(options[0])} ml",
            'option_b': f"{int(options[1])} ml",
            'option_c': f"{int(options[2])} ml",
            'option_d': f"{int(options[3])} ml",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_10(num_questions=50):
    """Level 10: Reverse Ratio Problems (Higher)"""
    questions = []
    used_questions = set()
    
    templates = [
        "{n1} and {n2} share money in ratio {a}:{b}.\n{n1} gets €{amt1}. How much is the total?",
        "After sharing in ratio {a}:{b}, {n2} receives €{amt2}.\nWhat was the original amount?",
        "Money shared {a}:{b}. The difference between shares is €{diff}.\nFind the total amount.",
    ]
    
    names_pairs = [('Jack', 'Emma'), ('Sean', 'Aoife'), ('Conor', 'Niamh')]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        n1, n2 = random.choice(names_pairs)
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        while a == b:
            b = random.randint(2, 5)
        
        multiplier = random.randint(10, 40)
        
        template_idx = random.randint(0, 2)
        
        if template_idx == 0:
            amt1 = a * multiplier
            question_text = templates[0].format(n1=n1, n2=n2, a=a, b=b, amt1=amt1)
        elif template_idx == 1:
            amt2 = b * multiplier
            question_text = templates[1].format(n1=n1, n2=n2, a=a, b=b, amt2=amt2)
        else:
            diff = abs(a - b) * multiplier
            question_text = templates[2].format(a=a, b=b, diff=diff)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        correct = (a + b) * multiplier
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_ratio_bar_svg([a, b], total=correct, unit='€')
        
        explanation = f"Ratio {a}:{b} means {a + b} parts total\n"
        explanation += f"One part = €{multiplier}\n"
        explanation += f"Total = {a + b} × €{multiplier} = €{correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"€{int(options[0])}",
            'option_b': f"€{int(options[1])}",
            'option_c': f"€{int(options[2])}",
            'option_d': f"€{int(options[3])}",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_11(num_questions=50):
    """Level 11: Real-world Applications (Application)"""
    questions = []
    used_questions = set()
    
    contexts = [
        {
            'setup': "A map has scale 1:{scale}.\nA road is {map_cm} cm on the map.",
            'question': "What is the actual length in km?",
            'calc': lambda scale, map_cm: (map_cm * scale) / 100000
        },
        {
            'setup': "Concrete is mixed {a}:{b}:{c} (gravel:sand:cement).\n{total} kg is needed.",
            'question': "How much sand is required?",
            'calc': lambda a, b, c, total: (b / (a + b + c)) * total
        },
        {
            'setup': "A recipe for {people} people uses {amount} g of flour.\nYou're cooking for {new_people} people.",
            'question': "How much flour do you need?",
            'calc': lambda people, amount, new_people: (amount / people) * new_people
        },
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        ctx_idx = random.randint(0, 2)
        
        if ctx_idx == 0:
            scale = random.choice([50000, 100000, 200000])
            map_cm = random.randint(3, 15)
            setup = contexts[0]['setup'].format(scale=scale, map_cm=map_cm)
            question_text = setup + "\n" + contexts[0]['question']
            correct = contexts[0]['calc'](scale, map_cm)
            unit = 'km'
        elif ctx_idx == 1:
            a, b, c = random.randint(2, 4), random.randint(2, 4), 1
            total = (a + b + c) * random.randint(50, 150)
            setup = contexts[1]['setup'].format(a=a, b=b, c=c, total=total)
            question_text = setup + "\n" + contexts[1]['question']
            correct = contexts[1]['calc'](a, b, c, total)
            unit = 'kg'
        else:
            people = random.choice([4, 6, 8])
            amount = people * random.randint(50, 100)
            new_people = random.choice([2, 3, 5, 10, 12])
            setup = contexts[2]['setup'].format(people=people, amount=amount, new_people=new_people)
            question_text = setup + "\n" + contexts[2]['question']
            correct = contexts[2]['calc'](people, amount, new_people)
            unit = 'g'
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        if correct == int(correct):
            correct = int(correct)
        
        options, correct_idx = generate_unique_options(correct, min_val=1, decimal_places=1 if isinstance(correct, float) else None)
        
        svg = generate_ratio_bar_svg([3, 2])  # Generic ratio visual
        
        explanation = f"Use ratio/proportion to solve:\n"
        explanation += f"Answer = {format_number(correct)} {unit}"
        
        questions.append({
            'question_text': question_text,
            'option_a': f"{format_number(options[0])} {unit}",
            'option_b': f"{format_number(options[1])} {unit}",
            'option_c': f"{format_number(options[2])} {unit}",
            'option_d': f"{format_number(options[3])} {unit}",
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_12(num_questions=50):
    """Level 12: Multi-step Ratio Problems (Mastery)"""
    questions = []
    used_questions = set()
    
    templates = [
        "{n1}, {n2} and {n3} share €{total}.\n{n1} gets twice as much as {n2}.\n{n3} gets €{n3_amt} more than {n2}.\nHow much does {n1} get?",
        "Money is first split 2:3 between A and B.\nB's share is then split 3:2 between C and D.\nIf the total is €{total}, how much does C get?",
        "The ratio of boys to girls is {a}:{b}.\nThere are {diff} more {more_type} than {less_type}.\nHow many students altogether?",
    ]
    
    names = [('Anna', 'Ben', 'Clara'), ('David', 'Emma', 'Finn'), ('Grace', 'Harry', 'Ivy')]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template_idx = random.randint(0, 2)
        
        if template_idx == 0:
            n1, n2, n3 = random.choice(names)
            # n1 = 2*n2, n3 = n2 + extra
            n2_amt = random.randint(20, 50)
            n1_amt = 2 * n2_amt
            extra = random.randint(10, 30)
            n3_amt_diff = extra
            n3_amt = n2_amt + extra
            total = n1_amt + n2_amt + n3_amt
            
            question_text = templates[0].format(n1=n1, n2=n2, n3=n3, total=total, n3_amt=n3_amt_diff)
            correct = n1_amt
        elif template_idx == 1:
            total = random.choice([100, 150, 200, 250])
            # A:B = 2:3, so B = 3/5 of total
            b_share = (3 * total) // 5
            # B split 3:2, C gets 3/5 of B's share
            c_share = (3 * b_share) // 5
            
            question_text = templates[1].format(total=total)
            correct = c_share
        else:
            a = random.randint(3, 7)
            b = random.randint(2, 6)
            while a == b:
                b = random.randint(2, 6)
            
            diff = abs(a - b) * random.randint(5, 15)
            multiplier = diff // abs(a - b)
            
            if a > b:
                more_type, less_type = 'boys', 'girls'
            else:
                more_type, less_type = 'girls', 'boys'
            
            question_text = templates[2].format(a=a, b=b, diff=diff, 
                                               more_type=more_type, less_type=less_type)
            correct = (a + b) * multiplier
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_ratio_bar_svg([2, 3])
        
        explanation = f"Multi-step problem:\n"
        explanation += f"Work through each condition step by step.\n"
        explanation += f"Answer = {correct}"
        
        # Format based on context
        if '€' in question_text:
            opt_format = lambda x: f"€{int(x)}"
        else:
            opt_format = lambda x: str(int(x))
        
        questions.append({
            'question_text': question_text,
            'option_a': opt_format(options[0]),
            'option_b': opt_format(options[1]),
            'option_c': opt_format(options[2]),
            'option_d': opt_format(options[3]),
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


# ============================================================
# VALIDATION & DATABASE
# ============================================================

def validate_questions(questions, level):
    """Validate generated questions"""
    errors = []
    warnings = []
    
    for i, q in enumerate(questions):
        opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(opts)) != 4:
            errors.append(f"Level {level} Q{i+1}: Duplicate options: {opts}")
        
        if q['correct_idx'] not in [0, 1, 2, 3]:
            errors.append(f"Level {level} Q{i+1}: Invalid correct_idx")
        
        if not q.get('question_text') or len(q['question_text']) < 10:
            errors.append(f"Level {level} Q{i+1}: Missing question text")
    
    return errors, warnings


def print_validation_summary(all_questions):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    total_errors = 0
    
    for level in range(1, 13):
        questions = all_questions.get(level, [])
        errors, warnings = validate_questions(questions, level)
        total_errors += len(errors)
        
        visual_count = sum(1 for q in questions if q.get('image_svg'))
        visual_pct = (visual_count / len(questions) * 100) if questions else 0
        
        bar_len = 20
        filled = int(bar_len * len(questions) / 50)
        bar = "█" * filled + "░" * (bar_len - filled)
        
        status = "✓" if len(errors) == 0 else "✗"
        print(f"Level {level:2d}: [{bar}] {len(questions):2d}/50 | Visual: {visual_pct:5.1f}% | {status}")
        
        for err in errors[:3]:
            print(f"         ❌ {err}")
    
    print("=" * 60)
    print(f"Total Errors: {total_errors}")
    print("=" * 60)
    
    return total_errors == 0


def insert_questions_to_db(all_questions, db_path='instance/mathquiz.db'):
    """Insert questions into database"""
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE topic = 'ratio'")
    existing = cursor.fetchone()[0]
    print(f"Existing ratio questions: {existing}")
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = 'ratio'")
    conn.commit()
    print(f"Deleted {existing} existing ratio questions")
    
    inserted = 0
    errors = 0
    
    for level in range(1, 13):
        questions = all_questions.get(level, [])
        
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
                    'ratio',
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
                if errors <= 5:
                    print(f"Error inserting Level {level} question: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ Inserted {inserted} questions")
    if errors > 0:
        print(f"❌ {errors} errors occurred")
    
    return errors == 0


def main():
    print("=" * 60)
    print("AgentMath - Ratio Topic Generator v1")
    print("Generating 600 SEC-aligned questions")
    print("=" * 60)
    
    all_questions = {}
    
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
    
    is_valid = print_validation_summary(all_questions)
    
    if not is_valid:
        print("\n⚠️ Validation failed.")
        return
    
    print("\n" + "=" * 60)
    response = input("Insert questions into database? (y/n): ").strip().lower()
    
    if response == 'y':
        insert_questions_to_db(all_questions)
        print("\n🎉 Ratio topic generation complete!")
    else:
        print("Skipped database insertion.")


if __name__ == '__main__':
    main()
