#!/usr/bin/env python3
"""
AgentMath - Number Patterns Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Counting patterns, adding patterns, subtracting patterns
  L4-6:   Developing - Times table patterns, finding rules, continuing patterns
  L7-9:   Proficient - Shape patterns, two-step patterns, missing numbers
  L10-12: Advanced - Complex patterns, pattern problems, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'number_patterns'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam'
]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_difficulty_band(level):
    if level <= 3:
        return 'foundation'
    elif level <= 6:
        return 'developing'
    elif level <= 9:
        return 'proficient'
    else:
        return 'advanced'

def make_options(correct, wrong_list):
    correct_str = str(correct)
    unique_wrong = []
    for w in wrong_list:
        w_str = str(w)
        if w_str != correct_str and w_str not in unique_wrong:
            unique_wrong.append(w_str)
    
    options = [correct_str] + unique_wrong[:3]
    
    fallback_idx = 1
    while len(set(options)) < 4:
        options.append(f"Option {fallback_idx}")
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    return options, correct_idx

def generate_sequence_svg(numbers, highlight_idx=None, show_blank=False):
    """Generate SVG showing a number sequence in boxes"""
    box_width = 45
    gap = 8
    height = 50
    width = len(numbers) * (box_width + gap) + 20
    
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .box {{ fill: #f0fdf4; stroke: #10b981; stroke-width: 2; rx: 5; }}
        .box-highlight {{ fill: #fef3c7; stroke: #f59e0b; stroke-width: 2; rx: 5; }}
        .box-blank {{ fill: #fee2e2; stroke: #ef4444; stroke-width: 2; rx: 5; stroke-dasharray: 4; }}
        .num {{ font-size: 16px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
        .qmark {{ font-size: 18px; fill: #ef4444; text-anchor: middle; font-weight: bold; }}
    </style>'''
    
    x = 10
    for i, num in enumerate(numbers):
        if show_blank and i == highlight_idx:
            svg += f'<rect x="{x}" y="5" width="{box_width}" height="40" class="box-blank"/>'
            svg += f'<text x="{x + box_width // 2}" y="32" class="qmark">?</text>'
        elif i == highlight_idx:
            svg += f'<rect x="{x}" y="5" width="{box_width}" height="40" class="box-highlight"/>'
            svg += f'<text x="{x + box_width // 2}" y="32" class="num">{num}</text>'
        else:
            svg += f'<rect x="{x}" y="5" width="{box_width}" height="40" class="box"/>'
            svg += f'<text x="{x + box_width // 2}" y="32" class="num">{num}</text>'
        x += box_width + gap
    
    svg += '</svg>'
    return svg

def generate_shape_pattern_svg(shapes, repeat=2):
    """Generate SVG showing shape pattern"""
    shape_width = 30
    gap = 10
    height = 50
    width = len(shapes) * repeat * (shape_width + gap) + 60
    
    colors = {'circle': '#3b82f6', 'square': '#ef4444', 'triangle': '#10b981', 
              'star': '#f59e0b', 'heart': '#ec4899', 'diamond': '#8b5cf6'}
    
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .shape {{ stroke-width: 2; }}
    </style>'''
    
    x = 15
    for _ in range(repeat):
        for shape in shapes:
            color = colors.get(shape, '#6b7280')
            cy = 25
            
            if shape == 'circle':
                svg += f'<circle cx="{x + 12}" cy="{cy}" r="12" fill="{color}" class="shape"/>'
            elif shape == 'square':
                svg += f'<rect x="{x}" y="{cy - 12}" width="24" height="24" fill="{color}" class="shape"/>'
            elif shape == 'triangle':
                svg += f'<polygon points="{x + 12},{cy - 12} {x},{cy + 12} {x + 24},{cy + 12}" fill="{color}" class="shape"/>'
            elif shape == 'star':
                svg += f'<polygon points="{x + 12},{cy - 12} {x + 15},{cy - 3} {x + 24},{cy - 3} {x + 17},{cy + 3} {x + 20},{cy + 12} {x + 12},{cy + 6} {x + 4},{cy + 12} {x + 7},{cy + 3} {x},{cy - 3} {x + 9},{cy - 3}" fill="{color}" class="shape"/>'
            elif shape == 'diamond':
                svg += f'<polygon points="{x + 12},{cy - 12} {x + 24},{cy} {x + 12},{cy + 12} {x},{cy}" fill="{color}" class="shape"/>'
            elif shape == 'heart':
                svg += f'<path d="M{x + 12},{cy + 10} C{x},{cy - 5} {x + 5},{cy - 15} {x + 12},{cy - 5} C{x + 19},{cy - 15} {x + 24},{cy - 5} {x + 12},{cy + 10}" fill="{color}" class="shape"/>'
            
            x += shape_width + gap
    
    # Add question mark box
    svg += f'<rect x="{x}" y="10" width="30" height="30" fill="#fee2e2" stroke="#ef4444" stroke-width="2" stroke-dasharray="4" rx="3"/>'
    svg += f'<text x="{x + 15}" y="32" font-size="18" fill="#ef4444" text-anchor="middle" font-weight="bold">?</text>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Counting Patterns (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Simple Counting Patterns"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['count_by_1', 'count_by_2', 'count_by_5', 'count_by_10', 'next_number'])
            
            if q_type == 'count_by_1':
                start = random.randint(1, 50)
                sequence = [start + i for i in range(5)]
                answer = start + 5
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer - 1), str(answer + 2)]
                explanation = f"Step 1: Pattern is +1 (counting up). Step 2: {sequence[-1]} + 1 = {answer}. ✓"
                image_svg = generate_sequence_svg(sequence + ['?'])
                
            elif q_type == 'count_by_2':
                start = random.choice([2, 4, 6, 8, 10])
                sequence = [start + i * 2 for i in range(4)]
                answer = sequence[-1] + 2
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer + 2), str(answer - 2)]
                explanation = f"Step 1: Pattern is +2 (counting by twos). Step 2: {sequence[-1]} + 2 = {answer}. ✓"
                image_svg = generate_sequence_svg(sequence + ['?'])
                
            elif q_type == 'count_by_5':
                start = random.choice([5, 10, 15, 20])
                sequence = [start + i * 5 for i in range(4)]
                answer = sequence[-1] + 5
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 5), str(answer - 5), str(answer + 1)]
                explanation = f"Step 1: Pattern is +5 (counting by fives). Step 2: {sequence[-1]} + 5 = {answer}. ✓"
                image_svg = generate_sequence_svg(sequence + ['?'])
                
            elif q_type == 'count_by_10':
                start = random.choice([10, 20, 30, 40, 50])
                sequence = [start + i * 10 for i in range(4)]
                answer = sequence[-1] + 10
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 10), str(answer - 10), str(answer + 1)]
                explanation = f"Step 1: Pattern is +10 (counting by tens). Step 2: {sequence[-1]} + 10 = {answer}. ✓"
                image_svg = generate_sequence_svg(sequence + ['?'])
                
            else:  # next_number
                step = random.choice([1, 2, 5, 10])
                start = random.randint(1, 30) * step // step  # align to step
                if step == 1:
                    start = random.randint(10, 50)
                elif step == 2:
                    start = random.choice([2, 4, 6, 8, 10, 12])
                elif step == 5:
                    start = random.choice([5, 10, 15, 20, 25])
                else:
                    start = random.choice([10, 20, 30, 40, 50])
                
                sequence = [start + i * step for i in range(4)]
                answer = sequence[-1] + step
                
                q_text = f"Continue the pattern: {sequence[0]}, {sequence[1]}, {sequence[2]}, {sequence[3]}, ?"
                correct = str(answer)
                wrong = [str(answer + step), str(answer - step), str(sequence[-1] + 1)]
                explanation = f"Step 1: Pattern is +{step}. Step 2: {sequence[-1]} + {step} = {answer}. ✓"
                image_svg = None
            
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
                'image_svg': image_svg,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Adding Patterns (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Patterns That Add a Fixed Number"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['add_3', 'add_4', 'add_6', 'add_7', 'identify_add'])
            
            if q_type == 'add_3':
                start = random.randint(1, 20)
                sequence = [start + i * 3 for i in range(4)]
                answer = sequence[-1] + 3
                step = 3
                
            elif q_type == 'add_4':
                start = random.randint(1, 20)
                sequence = [start + i * 4 for i in range(4)]
                answer = sequence[-1] + 4
                step = 4
                
            elif q_type == 'add_6':
                start = random.randint(1, 15)
                sequence = [start + i * 6 for i in range(4)]
                answer = sequence[-1] + 6
                step = 6
                
            elif q_type == 'add_7':
                start = random.randint(1, 15)
                sequence = [start + i * 7 for i in range(4)]
                answer = sequence[-1] + 7
                step = 7
                
            else:  # identify_add
                step = random.choice([3, 4, 5, 6, 7, 8])
                start = random.randint(2, 15)
                sequence = [start + i * step for i in range(4)]
                
                q_text = f"What is being added each time? {', '.join(map(str, sequence))}"
                correct = str(step)
                wrong = [str(step + 1), str(step - 1), str(step + 2)]
                explanation = f"Step 1: {sequence[1]} - {sequence[0]} = {step}. Step 2: Each number is +{step}. ✓"
                image_svg = generate_sequence_svg(sequence)
                
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
                    'image_svg': image_svg,
                    'difficulty': 2,
                    'difficulty_band': 'foundation',
                    'topic': TOPIC,
                    'mode': MODE
                })
                continue
            
            seq_str = ", ".join(map(str, sequence))
            q_text = f"What comes next? {seq_str}, ?"
            correct = str(answer)
            wrong = [str(answer + step), str(answer - step), str(answer + 1)]
            explanation = f"Step 1: Pattern is +{step}. Step 2: {sequence[-1]} + {step} = {answer}. ✓"
            image_svg = generate_sequence_svg(sequence + ['?'])
            
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
                'image_svg': image_svg,
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Subtracting Patterns (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Patterns That Subtract a Fixed Number"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['sub_1', 'sub_2', 'sub_3', 'sub_5', 'identify_sub'])
            
            if q_type == 'sub_1':
                start = random.randint(30, 50)
                step = 1
            elif q_type == 'sub_2':
                start = random.randint(40, 60)
                step = 2
            elif q_type == 'sub_3':
                start = random.randint(40, 60)
                step = 3
            elif q_type == 'sub_5':
                start = random.randint(50, 80)
                step = 5
            else:  # identify_sub
                step = random.choice([2, 3, 4, 5])
                start = random.randint(40, 60)
                sequence = [start - i * step for i in range(4)]
                
                q_text = f"What is being subtracted each time? {', '.join(map(str, sequence))}"
                correct = str(step)
                wrong = [str(step + 1), str(step - 1) if step > 1 else "1", str(step + 2)]
                explanation = f"Step 1: {sequence[0]} - {sequence[1]} = {step}. Step 2: Each number is -{step}. ✓"
                image_svg = generate_sequence_svg(sequence)
                
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
                    'image_svg': image_svg,
                    'difficulty': 3,
                    'difficulty_band': 'foundation',
                    'topic': TOPIC,
                    'mode': MODE
                })
                continue
            
            sequence = [start - i * step for i in range(4)]
            answer = sequence[-1] - step
            
            seq_str = ", ".join(map(str, sequence))
            q_text = f"What comes next? {seq_str}, ?"
            correct = str(answer)
            wrong = [str(answer + step), str(answer - step), str(sequence[-1] + 1)]
            explanation = f"Step 1: Pattern is -{step} (counting down). Step 2: {sequence[-1]} - {step} = {answer}. ✓"
            image_svg = generate_sequence_svg(sequence + ['?'])
            
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
                'image_svg': image_svg,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Times Table Patterns (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Patterns in Times Tables"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['times_2', 'times_3', 'times_4', 'times_5', 'times_9', 'identify_table'])
            
            if q_type == 'times_2':
                table = 2
                start_mult = random.randint(1, 6)
            elif q_type == 'times_3':
                table = 3
                start_mult = random.randint(1, 5)
            elif q_type == 'times_4':
                table = 4
                start_mult = random.randint(1, 5)
            elif q_type == 'times_5':
                table = 5
                start_mult = random.randint(1, 5)
            elif q_type == 'times_9':
                table = 9
                start_mult = random.randint(1, 4)
            else:  # identify_table
                table = random.choice([2, 3, 4, 5, 6])
                start_mult = random.randint(1, 4)
                sequence = [table * (start_mult + i) for i in range(4)]
                
                q_text = f"These numbers are from which times table? {', '.join(map(str, sequence))}"
                correct = f"{table} times table"
                wrong_tables = [t for t in [2, 3, 4, 5, 6, 7] if t != table][:3]
                wrong = [f"{t} times table" for t in wrong_tables]
                explanation = f"Step 1: All numbers divide by {table}. Step 2: This is the {table} times table. ✓"
                image_svg = generate_sequence_svg(sequence)
                
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
                    'image_svg': image_svg,
                    'difficulty': 4,
                    'difficulty_band': 'developing',
                    'topic': TOPIC,
                    'mode': MODE
                })
                continue
            
            sequence = [table * (start_mult + i) for i in range(4)]
            answer = table * (start_mult + 4)
            
            seq_str = ", ".join(map(str, sequence))
            q_text = f"These are from the {table} times table. What comes next? {seq_str}, ?"
            correct = str(answer)
            wrong = [str(answer + table), str(answer - table), str(answer + 1)]
            explanation = f"Step 1: Pattern is +{table} (the {table} times table). Step 2: {sequence[-1]} + {table} = {answer}. ✓"
            image_svg = generate_sequence_svg(sequence + ['?'])
            
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
                'image_svg': image_svg,
                'difficulty': 4,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Finding the Rule (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Identify the Pattern Rule"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['add_rule', 'sub_rule', 'mult_rule', 'describe_rule'])
            
            if q_type == 'add_rule':
                step = random.choice([3, 4, 5, 6, 7, 8, 9])
                start = random.randint(2, 15)
                sequence = [start + i * step for i in range(4)]
                
                q_text = f"What is the rule? {', '.join(map(str, sequence))}"
                correct = f"Add {step}"
                wrong = [f"Add {step + 1}", f"Add {step - 1}", f"Multiply by {step}"]
                explanation = f"Step 1: {sequence[1]} - {sequence[0]} = {step}. Step 2: Rule is add {step}. ✓"
                
            elif q_type == 'sub_rule':
                step = random.choice([2, 3, 4, 5, 6])
                start = random.randint(40, 60)
                sequence = [start - i * step for i in range(4)]
                
                q_text = f"What is the rule? {', '.join(map(str, sequence))}"
                correct = f"Subtract {step}"
                wrong = [f"Subtract {step + 1}", f"Subtract {step - 1}", f"Add {step}"]
                explanation = f"Step 1: {sequence[0]} - {sequence[1]} = {step}. Step 2: Rule is subtract {step}. ✓"
                
            elif q_type == 'mult_rule':
                mult = random.choice([2, 3])
                start = random.randint(1, 4)
                sequence = [start * (mult ** i) for i in range(4)]
                
                q_text = f"What is the rule? {', '.join(map(str, sequence))}"
                correct = f"Multiply by {mult}"
                wrong = [f"Add {sequence[1] - sequence[0]}", f"Multiply by {mult + 1}", f"Add {mult}"]
                explanation = f"Step 1: {sequence[1]} ÷ {sequence[0]} = {mult}. Step 2: Rule is multiply by {mult}. ✓"
                
            else:  # describe_rule
                variant = random.choice(['starts_at', 'goes_up', 'pattern_type'])
                step = random.choice([3, 4, 5, 6])
                start = random.randint(1, 10)
                sequence = [start + i * step for i in range(4)]
                
                if variant == 'starts_at':
                    q_text = f"The pattern {', '.join(map(str, sequence))} starts at which number?"
                    correct = str(start)
                    wrong = [str(start + step), str(start - 1), str(sequence[-1])]
                    explanation = f"Step 1: First number in pattern is {start}. ✓"
                elif variant == 'goes_up':
                    q_text = f"This pattern goes up by how much? {', '.join(map(str, sequence))}"
                    correct = str(step)
                    wrong = [str(step + 1), str(step - 1), str(step * 2)]
                    explanation = f"Step 1: {sequence[1]} - {sequence[0]} = {step}. Step 2: Goes up by {step}. ✓"
                else:
                    q_text = f"Is this pattern increasing, decreasing, or staying the same? {', '.join(map(str, sequence))}"
                    correct = "Increasing"
                    wrong = ["Decreasing", "Staying the same", "Random"]
                    explanation = f"Step 1: Numbers get bigger. Step 2: This is an increasing pattern. ✓"
            
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
                'image_svg': generate_sequence_svg(sequence),
                'difficulty': 5,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Continuing Patterns (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Find Multiple Next Terms"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['next_two', 'next_three', 'nth_term', 'fill_gap'])
            
            if q_type == 'next_two':
                step = random.choice([3, 4, 5, 6, 7])
                start = random.randint(2, 15)
                sequence = [start + i * step for i in range(3)]
                next1 = sequence[-1] + step
                next2 = next1 + step
                
                q_text = f"What are the next TWO numbers? {', '.join(map(str, sequence))}, ?, ?"
                correct = f"{next1}, {next2}"
                wrong = [f"{next1}, {next1 + 1}", f"{next1 - 1}, {next2 - 1}", f"{next2}, {next2 + step}"]
                explanation = f"Step 1: Pattern is +{step}. Step 2: {sequence[-1]} + {step} = {next1}, then {next1} + {step} = {next2}. ✓"
                
            elif q_type == 'next_three':
                step = random.choice([2, 3, 4, 5])
                start = random.randint(1, 10)
                sequence = [start + i * step for i in range(3)]
                next1 = sequence[-1] + step
                next2 = next1 + step
                next3 = next2 + step
                
                q_text = f"Find the next THREE numbers: {', '.join(map(str, sequence))}, ?, ?, ?"
                correct = f"{next1}, {next2}, {next3}"
                wrong = [f"{next1}, {next2}, {next2 + 1}", f"{next1 - 1}, {next2 - 1}, {next3 - 1}", f"{next2}, {next3}, {next3 + step}"]
                explanation = f"Step 1: Pattern is +{step}. Step 2: Continue adding {step} to get {next1}, {next2}, {next3}. ✓"
                
            elif q_type == 'nth_term':
                step = random.choice([2, 3, 4, 5])
                start = random.randint(1, 10)
                sequence = [start + i * step for i in range(4)]
                position = random.choice([5, 6, 7])
                answer = start + (position - 1) * step
                
                q_text = f"Pattern: {', '.join(map(str, sequence))}... What is the {position}th number?"
                correct = str(answer)
                wrong = [str(answer + step), str(answer - step), str(sequence[-1] + 1)]
                explanation = f"Step 1: Pattern is +{step}. Step 2: Position {position} = {start} + ({position - 1} × {step}) = {answer}. ✓"
                
            else:  # fill_gap
                step = random.choice([3, 4, 5, 6])
                start = random.randint(2, 10)
                sequence = [start + i * step for i in range(5)]
                gap_pos = random.choice([1, 2, 3])
                answer = sequence[gap_pos]
                display_seq = sequence.copy()
                display_seq[gap_pos] = "?"
                
                q_text = f"Find the missing number: {', '.join(map(str, display_seq))}"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer - 1), str(answer + step)]
                explanation = f"Step 1: Pattern is +{step}. Step 2: Missing number is {answer}. ✓"
            
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
                'image_svg': None,
                'difficulty': 6,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Shape Patterns (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Visual Shape Patterns"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    shapes = ['circle', 'square', 'triangle', 'star', 'diamond']
    shape_names = {'circle': 'Circle', 'square': 'Square', 'triangle': 'Triangle', 
                   'star': 'Star', 'diamond': 'Diamond'}
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['next_shape', 'pattern_length', 'position', 'complete'])
            
            if q_type == 'next_shape':
                pattern_len = random.choice([2, 3])
                pattern = random.sample(shapes, pattern_len)
                repeat = 2
                shown = pattern * repeat
                answer = pattern[0]
                
                q_text = f"What shape comes next in this pattern?"
                correct = shape_names[answer]
                wrong_shapes = [s for s in shapes if s != answer][:3]
                wrong = [shape_names[s] for s in wrong_shapes]
                explanation = f"Step 1: Pattern repeats every {pattern_len} shapes. Step 2: Next is {shape_names[answer]}. ✓"
                image_svg = generate_shape_pattern_svg(pattern, repeat)
                
            elif q_type == 'pattern_length':
                pattern_len = random.choice([2, 3, 4])
                pattern = random.sample(shapes, pattern_len)
                
                pattern_desc = ", ".join([shape_names[s] for s in pattern])
                q_text = f"How many shapes are in ONE repeat of this pattern? ({pattern_desc})"
                correct = str(pattern_len)
                wrong = [str(pattern_len + 1), str(pattern_len - 1) if pattern_len > 1 else "1", str(pattern_len + 2)]
                explanation = f"Step 1: Count shapes in one repeat. Step 2: There are {pattern_len} shapes. ✓"
                image_svg = generate_shape_pattern_svg(pattern, 2)
                
            elif q_type == 'position':
                pattern_len = random.choice([2, 3])
                pattern = random.sample(shapes, pattern_len)
                position = random.randint(5, 8)
                idx = (position - 1) % pattern_len
                answer = pattern[idx]
                
                q_text = f"Pattern: {', '.join([shape_names[s] for s in pattern])} (repeating). What is shape number {position}?"
                correct = shape_names[answer]
                wrong_shapes = [s for s in shapes if s != answer][:3]
                wrong = [shape_names[s] for s in wrong_shapes]
                explanation = f"Step 1: Pattern repeats every {pattern_len}. Step 2: Position {position} → shape {idx + 1} in pattern = {shape_names[answer]}. ✓"
                image_svg = generate_shape_pattern_svg(pattern, 2)
                
            else:  # complete
                pattern_len = random.choice([3, 4])
                pattern = random.sample(shapes, pattern_len)
                missing_idx = random.randint(1, pattern_len - 1)
                answer = pattern[missing_idx]
                
                display = [shape_names[s] if i != missing_idx else "?" for i, s in enumerate(pattern)]
                q_text = f"Complete the pattern: {', '.join(display)}"
                correct = shape_names[answer]
                wrong_shapes = [s for s in shapes if s != answer][:3]
                wrong = [shape_names[s] for s in wrong_shapes]
                explanation = f"Step 1: Look at the repeating pattern. Step 2: Missing shape is {shape_names[answer]}. ✓"
                image_svg = None
            
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
                'image_svg': image_svg,
                'difficulty': 7,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Two-Step Patterns (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Patterns with Two Operations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['add_then_mult', 'alternating', 'growing_step', 'two_rules'])
            
            if q_type == 'add_then_mult':
                # Pattern: ×2, ×2, ×2...
                start = random.choice([1, 2, 3])
                sequence = [start]
                for _ in range(4):
                    sequence.append(sequence[-1] * 2)
                answer = sequence[-1] * 2
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 2), str(sequence[-1] + 2), str(answer // 2)]
                explanation = f"Step 1: Pattern is ×2 (doubling). Step 2: {sequence[-1]} × 2 = {answer}. ✓"
                
            elif q_type == 'alternating':
                # Alternating add/subtract
                start = random.randint(10, 20)
                add_val = random.choice([3, 4, 5])
                sub_val = random.choice([1, 2])
                sequence = [start]
                for i in range(4):
                    if i % 2 == 0:
                        sequence.append(sequence[-1] + add_val)
                    else:
                        sequence.append(sequence[-1] - sub_val)
                # Next is add
                answer = sequence[-1] + add_val if len(sequence) % 2 == 1 else sequence[-1] - sub_val
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer - 1), str(sequence[-1] + 1)]
                explanation = f"Step 1: Pattern alternates +{add_val} then -{sub_val}. Step 2: Next is {answer}. ✓"
                
            elif q_type == 'growing_step':
                # +1, +2, +3, +4...
                start = random.randint(1, 5)
                sequence = [start]
                step = 1
                for _ in range(4):
                    sequence.append(sequence[-1] + step)
                    step += 1
                answer = sequence[-1] + step
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"The differences grow by 1 each time. What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer - 1), str(sequence[-1] + 1)]
                explanation = f"Step 1: Pattern adds +1, +2, +3, +4, +5... Step 2: {sequence[-1]} + {step} = {answer}. ✓"
                
            else:  # two_rules
                # Same rule but identify both parts
                start = random.randint(2, 8)
                step = random.choice([3, 4, 5, 6])
                sequence = [start + i * step for i in range(5)]
                
                q_text = f"This pattern starts at {start} and has a rule. What is added each time? {', '.join(map(str, sequence))}"
                correct = str(step)
                wrong = [str(step + 1), str(step - 1), str(start)]
                explanation = f"Step 1: {sequence[1]} - {sequence[0]} = {step}. Step 2: The rule is add {step}. ✓"
            
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
                'image_svg': None,
                'difficulty': 8,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Missing Numbers (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Find Missing Numbers in Patterns"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['middle_gap', 'two_gaps', 'first_missing', 'last_two'])
            
            if q_type == 'middle_gap':
                step = random.choice([4, 5, 6, 7, 8])
                start = random.randint(2, 15)
                sequence = [start + i * step for i in range(5)]
                gap_pos = random.choice([1, 2, 3])
                answer = sequence[gap_pos]
                display = sequence.copy()
                display[gap_pos] = "?"
                
                q_text = f"Find the missing number: {', '.join(map(str, display))}"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer - 1), str(answer + step)]
                explanation = f"Step 1: Pattern is +{step}. Step 2: Missing number is {answer}. ✓"
                
            elif q_type == 'two_gaps':
                step = random.choice([3, 4, 5, 6])
                start = random.randint(1, 10)
                sequence = [start + i * step for i in range(6)]
                gap1, gap2 = random.sample([1, 2, 3, 4], 2)
                answer1, answer2 = sequence[gap1], sequence[gap2]
                display = sequence.copy()
                display[gap1] = "?"
                display[gap2] = "?"
                
                q_text = f"Find BOTH missing numbers: {', '.join(map(str, display))}"
                correct = f"{min(answer1, answer2)} and {max(answer1, answer2)}"
                wrong = [f"{min(answer1, answer2) + 1} and {max(answer1, answer2) + 1}", 
                        f"{answer1} and {answer2 + step}", 
                        f"{answer1 - 1} and {answer2 - 1}"]
                explanation = f"Step 1: Pattern is +{step}. Step 2: Missing are {answer1} and {answer2}. ✓"
                
            elif q_type == 'first_missing':
                step = random.choice([4, 5, 6, 7])
                start = random.randint(3, 12)
                sequence = [start + i * step for i in range(5)]
                answer = sequence[0]
                display = ["?"] + sequence[1:]
                
                q_text = f"What is the first number? ?, {', '.join(map(str, display[1:]))}"
                correct = str(answer)
                wrong = [str(answer + step), str(answer - step), str(answer + 1)]
                explanation = f"Step 1: Pattern is +{step}. Step 2: First number is {sequence[1]} - {step} = {answer}. ✓"
                
            else:  # last_two
                step = random.choice([3, 4, 5, 6])
                start = random.randint(2, 10)
                sequence = [start + i * step for i in range(5)]
                answer1 = sequence[3]
                answer2 = sequence[4]
                
                q_text = f"Find the last two numbers: {sequence[0]}, {sequence[1]}, {sequence[2]}, ?, ?"
                correct = f"{answer1}, {answer2}"
                wrong = [f"{answer1}, {answer1 + 1}", f"{answer1 - 1}, {answer2 - 1}", f"{answer2}, {answer2 + step}"]
                explanation = f"Step 1: Pattern is +{step}. Step 2: Last two are {answer1} and {answer2}. ✓"
            
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
                'image_svg': None,
                'difficulty': 9,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Complex Patterns (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Complex Number Patterns"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['square_nums', 'triangular', 'fibonacci_like', 'prime_pattern'])
            
            if q_type == 'square_nums':
                # Square numbers: 1, 4, 9, 16, 25...
                start_n = random.randint(1, 4)
                sequence = [(start_n + i) ** 2 for i in range(4)]
                answer = (start_n + 4) ** 2
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"These are square numbers. What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(sequence[-1] + 1), str((start_n + 5) ** 2)]
                explanation = f"Step 1: Square numbers = 1², 2², 3²... Step 2: Next is {start_n + 4}² = {answer}. ✓"
                
            elif q_type == 'triangular':
                # Differences increase by 1: 1, 3, 6, 10, 15...
                sequence = [1, 3, 6, 10, 15]
                start_idx = random.randint(0, 1)
                seq_shown = sequence[start_idx:start_idx + 4]
                next_diff = 6 if start_idx == 0 else 7
                answer = seq_shown[-1] + (len(seq_shown) + start_idx + 1)
                
                seq_str = ", ".join(map(str, seq_shown))
                q_text = f"The gaps increase by 1 each time. What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer - 1), str(seq_shown[-1] + 1)]
                explanation = f"Step 1: Gaps are +2, +3, +4, +5... Step 2: Next is {seq_shown[-1]} + {len(seq_shown) + start_idx + 1} = {answer}. ✓"
                
            elif q_type == 'fibonacci_like':
                # Each number is sum of previous two
                a, b = random.choice([(1, 1), (1, 2), (2, 3), (1, 3)])
                sequence = [a, b]
                for _ in range(3):
                    sequence.append(sequence[-1] + sequence[-2])
                answer = sequence[-1] + sequence[-2]
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"Each number is the sum of the two before it. What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(sequence[-1] * 2), str(sequence[-1] + 1)]
                explanation = f"Step 1: Add last two numbers. Step 2: {sequence[-2]} + {sequence[-1]} = {answer}. ✓"
                
            else:  # prime_pattern
                # Simple pattern with primes concept
                primes = [2, 3, 5, 7, 11, 13, 17, 19]
                start_idx = random.randint(0, 3)
                sequence = primes[start_idx:start_idx + 4]
                answer = primes[start_idx + 4]
                
                seq_str = ", ".join(map(str, sequence))
                q_text = f"These are prime numbers. What comes next? {seq_str}, ?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer + 2), str(sequence[-1] + 2)]
                explanation = f"Step 1: Prime numbers only divide by 1 and themselves. Step 2: Next prime is {answer}. ✓"
            
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
                'image_svg': None,
                'difficulty': 10,
                'difficulty_band': 'advanced',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 11: Pattern Problems (Advanced)
# ============================================================

def generate_level_11():
    """Level 11: Word Problems with Patterns"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            problem_type = random.choice([1, 2, 3, 4, 5])
            
            if problem_type == 1:
                # Savings pattern
                start = random.choice([5, 10, 15, 20])
                add_weekly = random.choice([5, 10, 15])
                weeks = random.choice([5, 6, 7, 8])
                answer = start + (weeks - 1) * add_weekly
                
                sequence = [start + i * add_weekly for i in range(4)]
                q_text = f"{name} saves €{start} in week 1, then €{add_weekly} more each week. How much in week {weeks}?"
                correct = f"€{answer}"
                wrong = [f"€{answer + add_weekly}", f"€{start * weeks}", f"€{answer - add_weekly}"]
                explanation = f"Step 1: Pattern is +€{add_weekly} each week. Step 2: Week {weeks} = €{start} + {weeks - 1} × €{add_weekly} = €{answer}. ✓"
                
            elif problem_type == 2:
                # Growing pattern of objects
                start = random.choice([3, 4, 5])
                add_each = random.choice([2, 3, 4])
                step = random.choice([4, 5, 6])
                answer = start + (step - 1) * add_each
                
                q_text = f"{name} builds towers. Tower 1 has {start} blocks. Each tower has {add_each} more blocks than the last. How many in tower {step}?"
                correct = str(answer)
                wrong = [str(answer + add_each), str(start * step), str(answer - 1)]
                explanation = f"Step 1: Pattern is +{add_each} blocks each tower. Step 2: Tower {step} = {start} + {step - 1} × {add_each} = {answer}. ✓"
                
            elif problem_type == 3:
                # Time-based pattern
                start_time = random.choice([8, 9, 10])
                interval = random.choice([15, 20, 30])
                buses = random.choice([4, 5, 6])
                answer_mins = (buses - 1) * interval
                answer_time = start_time * 60 + answer_mins
                answer_hr = answer_time // 60
                answer_min = answer_time % 60
                
                q_text = f"A bus comes at {start_time}:00, then every {interval} minutes. What time is the {buses}th bus?"
                correct = f"{answer_hr}:{answer_min:02d}"
                wrong = [f"{answer_hr}:{(answer_min + interval) % 60:02d}", f"{start_time + buses}:00", f"{answer_hr}:{(answer_min - interval) % 60:02d}"]
                explanation = f"Step 1: Bus {buses} is {buses - 1} × {interval} = {answer_mins} minutes after {start_time}:00. Answer: {answer_hr}:{answer_min:02d}. ✓"
                
            elif problem_type == 4:
                # Decreasing pattern
                start = random.choice([50, 60, 70, 80])
                subtract = random.choice([5, 6, 7, 8])
                day = random.choice([5, 6, 7])
                answer = start - (day - 1) * subtract
                
                q_text = f"{name} has {start} stickers. Each day, {subtract} are given away. How many after day {day}?"
                correct = str(answer)
                wrong = [str(answer + subtract), str(start - day), str(answer - subtract)]
                explanation = f"Step 1: Pattern is -{subtract} each day. Step 2: After day {day}: {start} - {day - 1} × {subtract} = {answer}. ✓"
                
            else:
                # Find the rule from context
                start = random.choice([10, 12, 15])
                step = random.choice([3, 4, 5])
                sequence = [start + i * step for i in range(4)]
                
                q_text = f"{name}'s scores were {', '.join(map(str, sequence))}. By how much did scores increase each time?"
                correct = str(step)
                wrong = [str(step + 1), str(step - 1), str(start)]
                explanation = f"Step 1: {sequence[1]} - {sequence[0]} = {step}. Step 2: Scores increased by {step} each time. ✓"
            
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
                'image_svg': None,
                'difficulty': 11,
                'difficulty_band': 'advanced',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 12: Mastery Challenge (Advanced)
# ============================================================

def generate_level_12():
    """Level 12: Mastery Challenge - Mixed Difficult Questions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    generators = [generate_level_9, generate_level_10, generate_level_11]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            gen = random.choice(generators)
            source_questions = gen()
            
            if source_questions:
                q = random.choice(source_questions)
                q_text = q['question_text']
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                q['difficulty'] = 12
                q['difficulty_band'] = 'advanced'
                questions.append(q)
                
        except Exception as e:
            continue
    
    return questions

# ============================================================
# VALIDATION & DATABASE
# ============================================================

def validate_questions(questions):
    errors = []
    level_counts = {}
    
    for i, q in enumerate(questions):
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if q['mode'] != 'numeracy':
            errors.append(f"Level {level} Q{i}: Wrong mode")
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level} Q{i}: Duplicate options")
    
    print("\n" + "="*60)
    print("VALIDATION - Number Patterns")
    print("="*60)
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} {status}")
    
    print("="*60)
    print(f"Total: {len(questions)} | Errors: {len(errors)}")
    
    if errors:
        print("\nFirst 10 errors:")
        for err in errors[:10]:
            print(f"  - {err}")
    
    return len(errors)

def insert_questions(questions):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    print(f"Deleted {cursor.rowcount} existing questions")
    
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

def main():
    print("="*60)
    print("AgentMath - Number Patterns Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Counting Patterns", generate_level_1),
        (2, "Adding Patterns", generate_level_2),
        (3, "Subtracting Patterns", generate_level_3),
        (4, "Times Table Patterns", generate_level_4),
        (5, "Finding the Rule", generate_level_5),
        (6, "Continuing Patterns", generate_level_6),
        (7, "Shape Patterns", generate_level_7),
        (8, "Two-Step Patterns", generate_level_8),
        (9, "Missing Numbers", generate_level_9),
        (10, "Complex Patterns", generate_level_10),
        (11, "Pattern Problems", generate_level_11),
        (12, "Mastery Challenge", generate_level_12),
    ]
    
    for level, name, gen_func in generators:
        print(f"Generating Level {level}: {name}...")
        questions = gen_func()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    validate_questions(all_questions)
    
    response = input("\nInsert into database? (y/n): ").strip().lower()
    if response == 'y':
        insert_questions(all_questions)
        print("\n✓ Done!")

if __name__ == "__main__":
    main()
