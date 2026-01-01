#!/usr/bin/env python3
r"""
AgentMath - Sets & Venn Diagrams Topic Generator v1
SEC Junior Cycle Mathematics - Adaptive Quiz System

Generates 600 questions (50 per level × 12 levels) for the Sets topic.
Aligned with SEC Junior Cycle Mathematics Specification.

Level Structure:
  Level 1:  Understanding Sets (Foundation)
  Level 2:  Set Membership (Foundation)
  Level 3:  Reading Venn Diagrams (Foundation)
  Level 4:  Completing Venn Diagrams (Ordinary)
  Level 5:  Finding Totals from Venn Diagrams (Ordinary)
  Level 6:  Set Notation - Union & Intersection (Ordinary)
  Level 7:  Set Notation - A\B (Set Difference) (Higher)
  Level 8:  Probability from Venn Diagrams (Higher)
  Level 9:  Venn Diagrams with Algebra (Higher)
  Level 10: Three-Set Venn Diagrams (Higher)
  Level 11: Word Problems with Sets (Application)
  Level 12: Complex Set Problems (Mastery)

SEC Reference Questions:
  - 2022 OL Q5: 200 people, holidays, Venn diagram
  - 2022 HL Q6: 100 students, algebra with x
  - 2023 OL Q3: Music & Sport, S\M notation
  - 2024 OL Q3: Tennis & Football
  - 2025 OL Q5: 120 students, Sport & Computer Games
  - 2025 HL Q10: 88 students, Debating & Chess, algebra

Author: AgentMath Generator
Version: 1.0
Date: December 2025
"""

import random
import sqlite3
import os
import math

# ============================================================
# SVG VISUAL GENERATORS
# ============================================================

def generate_venn_two_sets_svg(set_a_only, both, set_b_only, outside, label_a='A', label_b='B', show_values=True):
    """Generate SVG showing two-set Venn diagram"""
    svg_width = 320
    svg_height = 200
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#f0f9ff" rx="8"/>'
    
    # Universal set rectangle
    svg += f'<rect x="20" y="20" width="280" height="160" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="5"/>'
    svg += f'<text x="30" y="38" font-size="12" fill="#0369a1">U</text>'
    
    # Circle A (left)
    svg += f'<circle cx="120" cy="100" r="60" fill="#bfdbfe" fill-opacity="0.7" stroke="#3b82f6" stroke-width="2"/>'
    svg += f'<text x="85" y="55" font-size="14" font-weight="bold" fill="#1e40af">{label_a}</text>'
    
    # Circle B (right)
    svg += f'<circle cx="200" cy="100" r="60" fill="#fecaca" fill-opacity="0.7" stroke="#ef4444" stroke-width="2"/>'
    svg += f'<text x="220" y="55" font-size="14" font-weight="bold" fill="#b91c1c">{label_b}</text>'
    
    if show_values:
        # A only
        svg += f'<text x="85" y="105" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e3a8a">{set_a_only}</text>'
        # Both (intersection)
        svg += f'<text x="160" y="105" text-anchor="middle" font-size="16" font-weight="bold" fill="#7c3aed">{both}</text>'
        # B only
        svg += f'<text x="235" y="105" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">{set_b_only}</text>'
        # Outside
        svg += f'<text x="280" y="165" text-anchor="middle" font-size="14" fill="#374151">{outside}</text>'
    
    svg += '</svg>'
    return svg


def generate_venn_with_missing_svg(set_a_only, both, set_b_only, outside, missing_pos, label_a='A', label_b='B'):
    """Generate Venn diagram with one value replaced by ?"""
    svg_width = 320
    svg_height = 200
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#fef3c7" rx="8"/>'
    
    # Universal set
    svg += f'<rect x="20" y="20" width="280" height="160" fill="#fef9c3" stroke="#ca8a04" stroke-width="2" rx="5"/>'
    svg += f'<text x="30" y="38" font-size="12" fill="#ca8a04">U</text>'
    
    # Circles
    svg += f'<circle cx="120" cy="100" r="60" fill="#bbf7d0" fill-opacity="0.7" stroke="#22c55e" stroke-width="2"/>'
    svg += f'<text x="85" y="55" font-size="14" font-weight="bold" fill="#166534">{label_a}</text>'
    
    svg += f'<circle cx="200" cy="100" r="60" fill="#fecaca" fill-opacity="0.7" stroke="#ef4444" stroke-width="2"/>'
    svg += f'<text x="220" y="55" font-size="14" font-weight="bold" fill="#b91c1c">{label_b}</text>'
    
    # Values with ? for missing
    values = [set_a_only, both, set_b_only, outside]
    positions = [(85, 105), (160, 105), (235, 105), (280, 165)]
    
    for i, (val, (x, y)) in enumerate(zip(values, positions)):
        if i == missing_pos:
            svg += f'<text x="{x}" y="{y}" text-anchor="middle" font-size="18" font-weight="bold" fill="#dc2626">?</text>'
        else:
            svg += f'<text x="{x}" y="{y}" text-anchor="middle" font-size="16" font-weight="bold" fill="#374151">{val}</text>'
    
    svg += '</svg>'
    return svg


def generate_venn_algebra_svg(expr_a_only, expr_both, expr_b_only, expr_outside, label_a='A', label_b='B'):
    """Generate Venn diagram with algebraic expressions"""
    svg_width = 320
    svg_height = 200
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#fce7f3" rx="8"/>'
    
    # Universal set
    svg += f'<rect x="20" y="20" width="280" height="160" fill="#fdf2f8" stroke="#db2777" stroke-width="2" rx="5"/>'
    svg += f'<text x="30" y="38" font-size="12" fill="#db2777">U</text>'
    
    # Circles
    svg += f'<circle cx="120" cy="100" r="60" fill="#c4b5fd" fill-opacity="0.6" stroke="#7c3aed" stroke-width="2"/>'
    svg += f'<text x="85" y="55" font-size="14" font-weight="bold" fill="#5b21b6">{label_a}</text>'
    
    svg += f'<circle cx="200" cy="100" r="60" fill="#a5f3fc" fill-opacity="0.6" stroke="#06b6d4" stroke-width="2"/>'
    svg += f'<text x="220" y="55" font-size="14" font-weight="bold" fill="#0891b2">{label_b}</text>'
    
    # Algebraic expressions
    svg += f'<text x="85" y="105" text-anchor="middle" font-size="14" font-weight="bold" fill="#5b21b6">{expr_a_only}</text>'
    svg += f'<text x="160" y="105" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">{expr_both}</text>'
    svg += f'<text x="235" y="105" text-anchor="middle" font-size="14" font-weight="bold" fill="#0891b2">{expr_b_only}</text>'
    svg += f'<text x="280" y="165" text-anchor="middle" font-size="12" fill="#374151">{expr_outside}</text>'
    
    svg += '</svg>'
    return svg


def generate_shaded_venn_svg(shade_type, label_a='A', label_b='B'):
    """Generate Venn diagram with shaded region for set notation"""
    svg_width = 320
    svg_height = 200
    
    svg = f'<svg viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{svg_width}" height="{svg_height}" fill="#f0fdf4" rx="8"/>'
    
    # Universal set
    svg += f'<rect x="20" y="20" width="280" height="160" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>'
    
    # Define clip paths for shading
    svg += '<defs>'
    svg += '<clipPath id="circleA"><circle cx="120" cy="100" r="60"/></clipPath>'
    svg += '<clipPath id="circleB"><circle cx="200" cy="100" r="60"/></clipPath>'
    svg += '</defs>'
    
    # Draw shaded region based on type
    if shade_type == 'intersection':  # A ∩ B
        # Intersection is where both circles overlap
        svg += f'<circle cx="120" cy="100" r="60" fill="#bbf7d0" stroke="#22c55e" stroke-width="2"/>'
        svg += f'<circle cx="200" cy="100" r="60" fill="#bbf7d0" stroke="#ef4444" stroke-width="2"/>'
        # Highlight intersection
        svg += f'<circle cx="200" cy="100" r="60" clip-path="url(#circleA)" fill="#fbbf24"/>'
    elif shade_type == 'union':  # A ∪ B
        svg += f'<circle cx="120" cy="100" r="60" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>'
        svg += f'<circle cx="200" cy="100" r="60" fill="#fbbf24" stroke="#ef4444" stroke-width="2"/>'
    elif shade_type == 'a_only':  # A \ B
        svg += f'<circle cx="120" cy="100" r="60" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>'
        svg += f'<circle cx="200" cy="100" r="60" fill="#dcfce7" stroke="#ef4444" stroke-width="2"/>'
    elif shade_type == 'b_only':  # B \ A
        svg += f'<circle cx="120" cy="100" r="60" fill="#dcfce7" stroke="#22c55e" stroke-width="2"/>'
        svg += f'<circle cx="200" cy="100" r="60" fill="#fbbf24" stroke="#ef4444" stroke-width="2"/>'
    else:
        svg += f'<circle cx="120" cy="100" r="60" fill="#bbf7d0" stroke="#22c55e" stroke-width="2"/>'
        svg += f'<circle cx="200" cy="100" r="60" fill="#fecaca" stroke="#ef4444" stroke-width="2"/>'
    
    # Labels
    svg += f'<text x="85" y="55" font-size="14" font-weight="bold" fill="#166534">{label_a}</text>'
    svg += f'<text x="220" y="55" font-size="14" font-weight="bold" fill="#b91c1c">{label_b}</text>'
    
    svg += '</svg>'
    return svg


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_number(n):
    """Format number"""
    if isinstance(n, float) and n == int(n):
        return str(int(n))
    return str(n)


def generate_unique_options(correct_answer, num_options=4, min_val=0):
    """Generate unique answer options"""
    options = [correct_answer]
    avoid = {correct_answer}
    
    attempts = 0
    while len(options) < num_options and attempts < 100:
        attempts += 1
        
        strategies = [
            correct_answer + random.randint(1, 10),
            correct_answer - random.randint(1, min(10, max(1, correct_answer))),
            correct_answer + random.randint(-5, 5),
            int(correct_answer * 1.5) if correct_answer > 0 else random.randint(1, 10),
        ]
        wrong = random.choice(strategies)
        
        if wrong < min_val:
            wrong = min_val + random.randint(1, 5)
        
        if wrong not in avoid and wrong >= min_val:
            options.append(wrong)
            avoid.add(wrong)
    
    while len(options) < num_options:
        filler = correct_answer + len(options) * 3
        if filler not in avoid:
            options.append(filler)
    
    random.shuffle(options)
    return options, options.index(correct_answer)


# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1(num_questions=50):
    """Level 1: Understanding Sets (Foundation)"""
    questions = []
    used_questions = set()
    
    set_types = [
        ("even numbers less than {n}", lambda n: [x for x in range(2, n, 2)]),
        ("odd numbers less than {n}", lambda n: [x for x in range(1, n, 2)]),
        ("factors of {n}", lambda n: [x for x in range(1, n+1) if n % x == 0]),
        ("multiples of {m} less than {n}", lambda m, n: [x for x in range(m, n, m)]),
        ("prime numbers less than {n}", lambda n: [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5)+1))]),
    ]
    
    templates = [
        "List all {set_desc}.\nHow many elements are in the set?",
        "A = {{{set_desc}}}.\nFind #(A), the number of elements.",
        "If B = {{{set_desc}}}, how many elements does B have?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        set_idx = random.randint(0, 4)
        
        if set_idx == 0:  # even
            n = random.randint(10, 25)
            desc = f"even numbers less than {n}"
            elements = [x for x in range(2, n, 2)]
        elif set_idx == 1:  # odd
            n = random.randint(10, 25)
            desc = f"odd numbers less than {n}"
            elements = [x for x in range(1, n, 2)]
        elif set_idx == 2:  # factors
            n = random.choice([12, 18, 20, 24, 30, 36])
            desc = f"factors of {n}"
            elements = [x for x in range(1, n+1) if n % x == 0]
        elif set_idx == 3:  # multiples
            m = random.choice([3, 4, 5, 6])
            n = random.randint(20, 40)
            desc = f"multiples of {m} less than {n}"
            elements = [x for x in range(m, n, m)]
        else:  # prime
            n = random.randint(15, 30)
            desc = f"prime numbers less than {n}"
            elements = [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
        
        template = random.choice(templates)
        question_text = template.format(set_desc=desc)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        correct = len(elements)
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_venn_two_sets_svg(correct, 0, 0, 0, label_a='Set', label_b='')
        
        elements_str = ', '.join(map(str, elements[:10]))
        if len(elements) > 10:
            elements_str += '...'
        
        explanation = f"Elements: {{{elements_str}}}\n"
        explanation += f"Count: {correct} elements"
        
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


def generate_level_2(num_questions=50):
    """Level 2: Set Membership (Foundation)"""
    questions = []
    used_questions = set()
    
    templates = [
        "A = {{{elements}}}.\nIs {test_val} ∈ A (is {test_val} in set A)?",
        "Given B = {{{elements}}}.\nTrue or False: {test_val} ∈ B",
        "Set C = {{{elements}}}.\nDoes {test_val} belong to set C?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Generate a set
        set_size = random.randint(4, 7)
        elements = sorted(random.sample(range(1, 30), set_size))
        elements_str = ', '.join(map(str, elements))
        
        # Decide if we're testing an element in or out of set
        is_in_set = random.random() < 0.5
        
        if is_in_set:
            test_val = random.choice(elements)
            correct = "Yes"
        else:
            # Pick a value not in set
            test_val = random.randint(1, 30)
            while test_val in elements:
                test_val = random.randint(1, 30)
            correct = "No"
        
        template = random.choice(templates)
        question_text = template.format(elements=elements_str, test_val=test_val)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        options = ["Yes", "No", "Maybe", "Cannot tell"]
        correct_idx = 0 if correct == "Yes" else 1
        
        svg = generate_venn_two_sets_svg(set_size, 0, 0, 0, label_a='Set', label_b='')
        
        explanation = f"Set = {{{elements_str}}}\n"
        if correct == "Yes":
            explanation += f"{test_val} IS in the set, so {test_val} ∈ A"
        else:
            explanation += f"{test_val} is NOT in the set, so {test_val} ∉ A"
        
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
    """Level 3: Reading Venn Diagrams (Foundation)"""
    questions = []
    used_questions = set()
    
    contexts = [
        ('Music', 'Sport', 'M', 'S'),
        ('Tennis', 'Football', 'T', 'F'),
        ('Cats', 'Dogs', 'C', 'D'),
        ('French', 'German', 'F', 'G'),
        ('Reading', 'Gaming', 'R', 'G'),
        ('Swimming', 'Running', 'Sw', 'R'),
    ]
    
    question_types = [
        ('both', "The Venn diagram shows students who like {a} ({a_only}) and {b} ({b_only}), with {both} in both.\nHow many students like both {a} and {b}?"),
        ('a_only', "From the Venn diagram with {a}={a_total} total and {both} in both,\nhow many like {a} only (not {b})?"),
        ('b_only', "Using the diagram where {b_only} like {b} only and {both} like both,\nhow many like {b} but not {a}?"),
        ('total', "Venn diagram: {a} only={a_only}, both={both}, {b} only={b_only}, neither={outside}.\nHow many students altogether?"),
        ('neither', "The diagram shows {a_only} in {a} only, {both} in both, {b_only} in {b} only.\nIf total is {total}, how many in neither?"),
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        ctx = random.choice(contexts)
        a_name, b_name, a_label, b_label = ctx
        
        a_only = random.randint(8, 45)
        both = random.randint(5, 30)
        b_only = random.randint(8, 45)
        outside = random.randint(5, 25)
        total = a_only + both + b_only + outside
        a_total = a_only + both
        
        q_type, template = random.choice(question_types)
        question_text = template.format(
            a=a_name, b=b_name, a_only=a_only, both=both, 
            b_only=b_only, outside=outside, total=total, a_total=a_total
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine correct answer based on question type
        if q_type == 'both':
            correct = both
        elif q_type == 'a_only':
            correct = a_only
        elif q_type == 'b_only':
            correct = b_only
        elif q_type == 'total':
            correct = total
        else:  # neither
            correct = outside
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        svg = generate_venn_two_sets_svg(a_only, both, b_only, outside, a_label, b_label)
        
        explanation = f"{a_name} only: {a_only}\n"
        explanation += f"Both: {both}\n"
        explanation += f"{b_name} only: {b_only}\n"
        explanation += f"Neither: {outside}\n"
        explanation += f"Answer: {correct}"
        
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
    """Level 4: Completing Venn Diagrams (Ordinary) - SEC 2022 OL Q5, 2025 OL Q5"""
    questions = []
    used_questions = set()
    
    contexts = [
        ('Sport', 'Computer Games', 'S', 'C'),
        ('Music', 'Art', 'M', 'A'),
        ('Swimming', 'Running', 'S', 'R'),
    ]
    
    templates = [
        "{total} students were surveyed. {both} play both {a} and {b}. {b_total} play {b}.\nHow many play {a} only?",
        "{total} people surveyed. {a_total} like {a}, {both} like both.\nIf {neither} like neither, how many like {b} only?",
        "From {total} students: {a_total} do {a}, {b_total} do {b}, {both} do both.\nFind the number who do neither.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        ctx = random.choice(contexts)
        a_name, b_name, a_label, b_label = ctx
        
        # Generate valid Venn diagram values
        both = random.randint(10, 30)
        a_only = random.randint(15, 40)
        b_only = random.randint(15, 40)
        neither = random.randint(10, 30)
        
        total = a_only + both + b_only + neither
        a_total = a_only + both
        b_total = b_only + both
        
        template = random.choice(templates)
        question_text = template.format(
            total=total, both=both, a=a_name, b=b_name,
            a_total=a_total, b_total=b_total, neither=neither
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine what's being asked
        if f'{a_name} only' in question_text.lower():
            correct = a_only
            missing_pos = 0
        elif f'{b_name} only' in question_text.lower():
            correct = b_only
            missing_pos = 2
        else:  # neither
            correct = neither
            missing_pos = 3
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        svg = generate_venn_with_missing_svg(a_only, both, b_only, neither, missing_pos, a_label, b_label)
        
        explanation = f"Total = {total}\n"
        explanation += f"{a_name}: {a_total} (so {a_name} only = {a_total} - {both} = {a_only})\n"
        explanation += f"{b_name}: {b_total} (so {b_name} only = {b_total} - {both} = {b_only})\n"
        explanation += f"Neither = {total} - {a_only} - {both} - {b_only} = {neither}"
        
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


def generate_level_5(num_questions=50):
    """Level 5: Finding Totals from Venn Diagrams (Ordinary)"""
    questions = []
    used_questions = set()
    
    contexts = [
        ('History', 'Geography', 'H', 'G'),
        ('Piano', 'Guitar', 'P', 'G'),
        ('Netflix', 'Disney+', 'N', 'D'),
    ]
    
    templates = [
        "In the Venn diagram, {a_only} like {a} only, {both} like both, {b_only} like {b} only, and {neither} like neither.\nHow many people were surveyed?",
        "From the Venn diagram: #({a} only) = {a_only}, #({a} ∩ {b}) = {both}, #({b} only) = {b_only}, neither = {neither}.\nFind the total.",
        "A survey shows: {a} only = {a_only}, both = {both}, {b} only = {b_only}, neither = {neither}.\nWhat is the total number surveyed?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        ctx = random.choice(contexts)
        a_name, b_name, a_label, b_label = ctx
        
        a_only = random.randint(10, 35)
        both = random.randint(8, 25)
        b_only = random.randint(10, 35)
        neither = random.randint(5, 20)
        
        correct = a_only + both + b_only + neither
        
        template = random.choice(templates)
        question_text = template.format(
            a=a_name, b=b_name, a_only=a_only, both=both, b_only=b_only, neither=neither
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_venn_two_sets_svg(a_only, both, b_only, neither, a_label, b_label)
        
        explanation = f"Total = {a_only} + {both} + {b_only} + {neither}\n"
        explanation += f"Total = {correct}"
        
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


def generate_level_6(num_questions=50):
    """Level 6: Set Notation - Union & Intersection (Ordinary)"""
    questions = []
    used_questions = set()
    
    templates = [
        "A = {{{a_elements}}} and B = {{{b_elements}}}.\nFind #(A ∩ B), the number of elements in both sets.",
        "Given A = {{{a_elements}}} and B = {{{b_elements}}}.\nFind #(A ∪ B), the number of elements in A or B or both.",
        "A = {{{a_elements}}}, B = {{{b_elements}}}.\nWhat is #(A ∩ B)?",
        "Sets A = {{{a_elements}}} and B = {{{b_elements}}}.\nCalculate #(A ∪ B).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Generate two sets with some overlap
        base = list(range(1, 15))
        random.shuffle(base)
        
        size_a = random.randint(4, 6)
        size_b = random.randint(4, 6)
        overlap = random.randint(1, min(size_a, size_b) - 1)
        
        set_a = sorted(base[:size_a])
        set_b = sorted(base[:overlap] + base[size_a:size_a + size_b - overlap])
        
        a_elements = ', '.join(map(str, set_a))
        b_elements = ', '.join(map(str, set_b))
        
        template = random.choice(templates)
        question_text = template.format(a_elements=a_elements, b_elements=b_elements)
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        intersection = set(set_a) & set(set_b)
        union = set(set_a) | set(set_b)
        
        if '∩' in question_text and '∪' not in question_text:
            correct = len(intersection)
            symbol = '∩'
        else:
            correct = len(union)
            symbol = '∪'
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        svg = generate_shaded_venn_svg('intersection' if symbol == '∩' else 'union')
        
        explanation = f"A = {{{a_elements}}}\n"
        explanation += f"B = {{{b_elements}}}\n"
        if symbol == '∩':
            explanation += f"A ∩ B = {{{', '.join(map(str, sorted(intersection)))}}}\n"
        else:
            explanation += f"A ∪ B = {{{', '.join(map(str, sorted(union)))}}}\n"
        explanation += f"Count = {correct}"
        
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


def generate_level_7(num_questions=50):
    """Level 7: Set Notation - A\\B (Set Difference) (Higher) - SEC 2023 OL Q3, 2025 OL Q5"""
    questions = []
    used_questions = set()
    
    contexts = [
        ('Sport', 'Computer Games', 'S', 'C'),
        ('Music', 'Drama', 'M', 'D'),
        ('Debating', 'Chess', 'D', 'C'),
    ]
    
    templates = [
        "In the Venn diagram, {a_only} are in {a} only, {both} in both, {b_only} in {b} only.\nWhat is #({a_sym}\\{b_sym})? (Elements in {a} but not {b})",
        "#({a_sym}) = {a_total}, #({a_sym} ∩ {b_sym}) = {both}.\nFind #({a_sym}\\{b_sym}).",
        "If {a_sym}\\{b_sym} means '{a} but not {b}', and the Venn shows {a_only} in {a} only,\nwhat is #({a_sym}\\{b_sym})?",
        "The notation #({b_sym}\\{a_sym}) means elements in {b} but not in {a}.\nFrom the diagram, #({b_sym}\\{a_sym}) = ?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        ctx = random.choice(contexts)
        a_name, b_name, a_sym, b_sym = ctx
        
        a_only = random.randint(15, 45)
        both = random.randint(10, 30)
        b_only = random.randint(15, 45)
        
        a_total = a_only + both
        b_total = b_only + both
        
        template = random.choice(templates)
        question_text = template.format(
            a=a_name, b=b_name, a_sym=a_sym, b_sym=b_sym,
            a_only=a_only, both=both, b_only=b_only, a_total=a_total
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine which set difference is asked
        if f'{b_sym}\\{a_sym}' in question_text:
            correct = b_only
        else:
            correct = a_only
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        svg = generate_venn_two_sets_svg(a_only, both, b_only, 0, a_sym, b_sym)
        
        explanation = f"{a_sym}\\{b_sym} means in {a_name} but NOT in {b_name}\n"
        explanation += f"This is the '{a_name} only' region = {a_only}\n"
        explanation += f"{b_sym}\\{a_sym} would be '{b_name} only' = {b_only}"
        
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


def generate_level_8(num_questions=50):
    """Level 8: Probability from Venn Diagrams (Higher) - SEC 2022 OL Q5, 2024 OL Q3"""
    questions = []
    used_questions = set()
    
    contexts = [
        ('Tennis', 'Football', 'T', 'F'),
        ('Cats', 'Dogs', 'C', 'D'),
        ('Reading', 'Gaming', 'R', 'G'),
        ('Art', 'Music', 'A', 'M'),
    ]
    
    templates = [
        "{total} students surveyed. {a_only} like {a} only, {both} like both, {b_only} like {b} only.\nA student is picked at random. Find P(likes both) as a fraction.",
        "From {total} people: {a_total} like {a}, {b_total} like {b}, {both} like both, {neither} like neither.\nFind P(likes {a} or {b} but not both).",
        "In a survey of {total}: {a_only} play {a} only, {both} play both, {b_only} play {b} only.\nP(plays {a}) = ?",
        "Survey of {total} students: {a_only} in {a} only, {both} in both, {b_only} in {b} only, {neither} in neither.\nFind P(in {b}) as a simplified fraction.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        ctx = random.choice(contexts)
        a_name, b_name, a_sym, b_sym = ctx
        
        # Use nice numbers for fractions
        multiplier = random.choice([2, 4, 5, 10])
        a_only = random.randint(2, 8) * multiplier
        both = random.randint(1, 5) * multiplier
        b_only = random.randint(2, 8) * multiplier
        neither = random.randint(1, 4) * multiplier
        
        total = a_only + both + b_only + neither
        a_total = a_only + both
        b_total = b_only + both
        
        template = random.choice(templates)
        question_text = template.format(
            total=total, a=a_name, b=b_name,
            a_only=a_only, both=both, b_only=b_only,
            a_total=a_total, b_total=b_total, neither=neither
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine probability numerator
        if 'likes both' in question_text.lower() or 'play both' in question_text.lower():
            numerator = both
        elif 'but not both' in question_text.lower():
            numerator = a_only + b_only
        elif f'in {b_name.lower()})' in question_text.lower() or f'P(in {b_name})' in question_text:
            numerator = b_total
        elif f'plays {a_name.lower()}' in question_text.lower():
            numerator = a_total
        else:
            numerator = both
        
        from math import gcd
        g = gcd(numerator, total)
        frac_num = numerator // g
        frac_den = total // g
        
        correct = f"{frac_num}/{frac_den}"
        
        # Generate unique wrong fractions
        wrong_set = set()
        for offset in [-2, -1, 1, 2, 3]:
            wrong_num = frac_num + offset
            if 0 < wrong_num < frac_den:
                wrong_set.add(f"{wrong_num}/{frac_den}")
        # Also try different denominators
        wrong_set.add(f"{frac_num}/{frac_den + 1}")
        wrong_set.add(f"{frac_num + 1}/{frac_den + 2}")
        
        wrong_set.discard(correct)
        wrong_options = list(wrong_set)[:3]
        
        # Ensure we have 3 wrong options
        fallback_attempts = 0
        while len(wrong_options) < 3 and fallback_attempts < 20:
            fallback_attempts += 1
            if frac_den > 2:
                fallback = f"{random.randint(1, frac_den-1)}/{frac_den}"
            else:
                fallback = f"{random.randint(1, 5)}/{frac_den + random.randint(1, 3)}"
            if fallback != correct and fallback not in wrong_options:
                wrong_options.append(fallback)
        
        # Final fallback if still not enough options
        while len(wrong_options) < 3:
            wrong_options.append(f"{len(wrong_options) + 1}/{frac_den + len(wrong_options)}")
        
        options = [correct] + wrong_options[:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        svg = generate_venn_two_sets_svg(a_only, both, b_only, neither, a_sym, b_sym)
        
        explanation = f"Total = {total}\n"
        explanation += f"Favourable outcomes = {numerator}\n"
        explanation += f"P = {numerator}/{total} = {correct}"
        
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


def generate_level_9(num_questions=50):
    """Level 9: Venn Diagrams with Algebra (Higher) - SEC 2022 HL Q6, 2025 HL Q10"""
    questions = []
    used_questions = set()
    
    contexts = [
        ('Debating', 'Chess', 'D', 'C'),
        ('History', 'Geography', 'H', 'G'),
        ('Art', 'Music', 'A', 'M'),
    ]
    
    templates = [
        "{total} students. #({a_sym}) = {a_total}, {neither} in neither.\nIf intersection is x and {b_sym} only is {b_only_expr}, find x.",
        "In a class of {total}: {a_total} do {a}, x do both, {b_only_expr} do {b} only, {neither} do neither.\nFind x.",
        "{total} students surveyed. {a_sym} only = {a_only_expr}, both = x, {b_sym} only = {b_only}, neither = {neither}.\n#({a_sym}) = {a_total}. Find x.",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        ctx = random.choice(contexts)
        a_name, b_name, a_sym, b_sym = ctx
        
        # Set up algebra - x is the intersection
        x = random.randint(5, 15)
        a_only = random.randint(10, 25)
        b_only = random.randint(10, 25)
        neither = random.randint(10, 30)
        
        total = a_only + x + b_only + neither
        a_total = a_only + x
        
        # Express one region in terms of x
        if random.random() < 0.5:
            a_only_expr = f"{a_total} - x"
            b_only_expr = str(b_only)
        else:
            a_only_expr = str(a_only)
            b_only_expr = f"2x + {b_only - 2*x}" if b_only > 2*x else str(b_only)
        
        template = random.choice(templates)
        question_text = template.format(
            total=total, a=a_name, b=b_name, a_sym=a_sym, b_sym=b_sym,
            a_total=a_total, neither=neither, b_only_expr=b_only_expr,
            a_only_expr=a_only_expr, b_only=b_only
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        correct = x
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        svg = generate_venn_algebra_svg(a_only_expr, 'x', b_only_expr, str(neither), a_sym, b_sym)
        
        explanation = f"Set up equation using total:\n"
        explanation += f"{a_only_expr} + x + {b_only_expr} + {neither} = {total}\n"
        explanation += f"Solve for x = {x}"
        
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


def generate_level_10(num_questions=50):
    """Level 10: Three-Set Venn Diagrams (Higher)"""
    questions = []
    used_questions = set()
    
    templates = [
        "In a 3-set Venn diagram: {a_only} in A only, {b_only} in B only, {c_only} in C only.\n{ab} in A∩B only, {bc} in B∩C only, {ac} in A∩C only, {abc} in all three.\nHow many in A altogether?",
        "Three sets have: only A={a_only}, only B={b_only}, only C={c_only}, A∩B only={ab}, B∩C only={bc}, A∩C only={ac}, all three={abc}.\nFind #(A ∪ B ∪ C).",
        "From a 3-set diagram: {abc} students do all three activities.\nA only={a_only}, A∩B only={ab}, A∩C only={ac}.\nHow many do activity A?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Generate 3-set values
        a_only = random.randint(5, 15)
        b_only = random.randint(5, 15)
        c_only = random.randint(5, 15)
        ab = random.randint(3, 10)  # A∩B only (not C)
        bc = random.randint(3, 10)  # B∩C only
        ac = random.randint(3, 10)  # A∩C only
        abc = random.randint(2, 8)  # All three
        
        template = random.choice(templates)
        question_text = template.format(
            a_only=a_only, b_only=b_only, c_only=c_only,
            ab=ab, bc=bc, ac=ac, abc=abc
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Calculate answers
        a_total = a_only + ab + ac + abc
        union_total = a_only + b_only + c_only + ab + bc + ac + abc
        
        if 'A altogether' in question_text or 'do activity A' in question_text:
            correct = a_total
        else:
            correct = union_total
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        # Simple 2-set visual (3-set is complex)
        svg = generate_venn_two_sets_svg(a_only + ac, ab + abc, b_only + bc, c_only, 'A', 'B')
        
        explanation = f"A = A only + (A∩B only) + (A∩C only) + (all three)\n"
        explanation += f"A = {a_only} + {ab} + {ac} + {abc} = {a_total}\n"
        explanation += f"Union = sum of all regions = {union_total}"
        
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


def generate_level_11(num_questions=50):
    """Level 11: Word Problems with Sets (Application)"""
    questions = []
    used_questions = set()
    
    templates = [
        "A survey of {total} people found {a_total} own a car, {b_total} own a bike, and {both} own both.\nHow many own neither?",
        "In a class of {total}: {a_total} passed Maths, {b_total} passed English, {neither} passed neither.\nHow many passed both?",
        "Of {total} tourists: {a_total} visited Dublin, {b_total} visited Cork, {neither} visited neither city.\nHow many visited both cities?",
        "A club has {total} members. {a_total} play tennis, {b_total} play golf, {both} play both.\nHow many play at least one sport?",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        template = random.choice(templates)
        
        # Generate consistent values
        both = random.randint(10, 30)
        a_only = random.randint(15, 40)
        b_only = random.randint(15, 40)
        neither = random.randint(10, 25)
        
        total = a_only + both + b_only + neither
        a_total = a_only + both
        b_total = b_only + both
        at_least_one = a_only + both + b_only
        
        question_text = template.format(
            total=total, a_total=a_total, b_total=b_total,
            both=both, neither=neither
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine answer
        if 'neither' in question_text.split('?')[0].lower() and 'passed neither' not in question_text.lower():
            correct = neither
        elif 'both' in question_text.split('?')[0].lower()[-20:]:
            correct = both
        elif 'at least one' in question_text.lower():
            correct = at_least_one
        else:
            correct = both
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        svg = generate_venn_two_sets_svg(a_only, both, b_only, neither)
        
        explanation = f"Use: #(A ∪ B) = #(A) + #(B) - #(A ∩ B)\n"
        explanation += f"Or: Total = A only + Both + B only + Neither\n"
        explanation += f"Answer = {correct}"
        
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
    """Level 12: Complex Set Problems (Mastery)"""
    questions = []
    used_questions = set()
    
    templates = [
        "In a school of {total}: #(M) = {m_total}, #(S) = {s_total}, #(M ∩ S) = x, #(M ∪ S)' = {neither}.\nIf #(S\\M) = {s_only}, find x.",
        "{total} students: {m_total} study Maths, {s_total} study Science.\nThe probability a random student studies both is {prob}.\nHow many study Maths only?",
        "Sets A and B: #(A) = {a_total}, #(B) = {b_total}, #(A ∩ B) = {both}.\nFind #(A \\ B) + #(B \\ A).",
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 3:
        attempts += 1
        
        # Generate values
        both = random.randint(10, 25)
        a_only = random.randint(15, 35)
        b_only = random.randint(15, 35)
        neither = random.randint(10, 20)
        
        total = a_only + both + b_only + neither
        a_total = a_only + both
        b_total = b_only + both
        
        # For probability question
        from math import gcd
        g = gcd(both, total)
        prob_num = both // g
        prob_den = total // g
        prob = f"{prob_num}/{prob_den}"
        
        template = random.choice(templates)
        question_text = template.format(
            total=total, m_total=a_total, s_total=b_total,
            both=both, neither=neither, s_only=b_only,
            a_total=a_total, b_total=b_total, prob=prob
        )
        
        if question_text in used_questions:
            continue
        used_questions.add(question_text)
        
        # Determine answer
        if 'find x' in question_text.lower():
            correct = both
        elif 'Maths only' in question_text:
            correct = a_only
        else:  # A\B + B\A
            correct = a_only + b_only
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        
        svg = generate_venn_two_sets_svg(a_only, both, b_only, neither, 'M', 'S')
        
        explanation = f"Use set formulas:\n"
        explanation += f"#(A ∪ B) = #(A) + #(B) - #(A ∩ B)\n"
        explanation += f"Total = A only + Both + B only + Neither\n"
        explanation += f"Answer = {correct}"
        
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


# ============================================================
# VALIDATION & DATABASE
# ============================================================

def validate_questions(questions, level):
    """Validate generated questions"""
    errors = []
    
    for i, q in enumerate(questions):
        opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(opts)) != 4:
            errors.append(f"Level {level} Q{i+1}: Duplicate options")
        
        if q['correct_idx'] not in [0, 1, 2, 3]:
            errors.append(f"Level {level} Q{i+1}: Invalid correct_idx")
    
    return errors, []


def print_validation_summary(all_questions):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    total_errors = 0
    
    for level in range(1, 13):
        questions = all_questions.get(level, [])
        errors, _ = validate_questions(questions, level)
        total_errors += len(errors)
        
        visual_count = sum(1 for q in questions if q.get('image_svg'))
        visual_pct = (visual_count / len(questions) * 100) if questions else 0
        
        bar_len = 20
        filled = int(bar_len * len(questions) / 50)
        bar = "█" * filled + "░" * (bar_len - filled)
        
        status = "✓" if len(errors) == 0 else "✗"
        print(f"Level {level:2d}: [{bar}] {len(questions):2d}/50 | Visual: {visual_pct:5.1f}% | {status}")
        
        for err in errors[:2]:
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
    
    cursor.execute("SELECT COUNT(*) FROM questions_adaptive WHERE topic = 'sets'")
    existing = cursor.fetchone()[0]
    print(f"Existing sets questions: {existing}")
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = 'sets'")
    conn.commit()
    print(f"Deleted {existing} existing sets questions")
    
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
                    'sets',
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
                    print(f"Error Level {level}: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ Inserted {inserted} questions")
    if errors > 0:
        print(f"❌ {errors} errors")
    
    return errors == 0


def main():
    print("=" * 60)
    print("AgentMath - Sets & Venn Diagrams Topic Generator v1")
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
        print("\n🎉 Sets & Venn Diagrams complete!")
    else:
        print("Skipped database insertion.")


if __name__ == '__main__':
    main()
