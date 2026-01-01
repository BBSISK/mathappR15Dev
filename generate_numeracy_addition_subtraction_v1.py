#!/usr/bin/env python3
"""
AgentMath - Addition & Subtraction Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Adding/Subtracting to 20, 2-digit numbers
  L4-6:   Developing - 2-digit and 3-digit operations
  L7-9:   Proficient - Word problems, mixed operations
  L10-12: Advanced - Multi-step, estimation, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'addition_subtraction'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam',
    'Emily', 'Luke', 'Sarah', 'Ryan', 'Anna', 'Ben'
]

CONTEXTS = {
    'school': ['pencils', 'books', 'crayons', 'stickers', 'rubbers'],
    'food': ['apples', 'oranges', 'sweets', 'biscuits', 'grapes'],
    'sports': ['goals', 'points', 'laps', 'medals', 'cards'],
    'toys': ['marbles', 'toy cars', 'blocks', 'balls', 'dolls'],
    'money': ['cents', 'euro', 'coins'],
    'nature': ['flowers', 'leaves', 'shells', 'stones', 'birds']
}

# ============================================================
# HELPERS
# ============================================================

def get_difficulty_band(level):
    if level <= 3:
        return 'foundation'
    elif level <= 6:
        return 'developing'
    elif level <= 9:
        return 'proficient'
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
        fallback = str(int(correct) + fallback_idx * 3) if str(correct).lstrip('-').isdigit() else f"{correct}_{fallback_idx}"
        if fallback not in options:
            options.append(fallback)
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    return options, options.index(correct_str)

def generate_number_line_svg(start, end, highlight=None, show_jumps=None):
    """Generate SVG number line for addition/subtraction visualization"""
    svg = '''<svg viewBox="0 0 400 80" xmlns="http://www.w3.org/2000/svg">
    <style>
        .line { stroke: #374151; stroke-width: 2; }
        .tick { stroke: #374151; stroke-width: 1; }
        .label { font-size: 11px; fill: #374151; text-anchor: middle; }
        .highlight { fill: #10b981; font-weight: bold; }
        .jump { stroke: #10b981; stroke-width: 2; fill: none; }
        .jump-label { font-size: 10px; fill: #10b981; text-anchor: middle; }
    </style>
    <line x1="20" y1="50" x2="380" y2="50" class="line"/>'''
    
    range_val = end - start
    if range_val == 0:
        range_val = 1
    
    # Draw ticks and labels
    step = max(1, range_val // 10)
    for i in range(start, end + 1, step):
        x = 20 + (360 * (i - start) / range_val)
        svg += f'<line x1="{x}" y1="45" x2="{x}" y2="55" class="tick"/>'
        label_class = 'highlight' if i == highlight else 'label'
        svg += f'<text x="{x}" y="70" class="{label_class}">{i}</text>'
    
    # Draw jumps if provided
    if show_jumps:
        for i, (from_val, to_val, label) in enumerate(show_jumps):
            x1 = 20 + (360 * (from_val - start) / range_val)
            x2 = 20 + (360 * (to_val - start) / range_val)
            mid_x = (x1 + x2) / 2
            svg += f'<path d="M {x1} 45 Q {mid_x} 20 {x2} 45" class="jump"/>'
            svg += f'<text x="{mid_x}" y="15" class="jump-label">{label}</text>'
    
    svg += '</svg>'
    return svg

def generate_column_addition_svg(num1, num2, show_answer=False):
    """Generate SVG showing column addition"""
    answer = num1 + num2
    num1_str = str(num1)
    num2_str = str(num2)
    ans_str = str(answer) if show_answer else '?'
    max_len = max(len(num1_str), len(num2_str), len(ans_str))
    
    svg = f'''<svg viewBox="0 0 150 120" xmlns="http://www.w3.org/2000/svg">
    <style>
        .digit {{ font-size: 20px; font-family: monospace; fill: #1f2937; }}
        .op {{ font-size: 20px; fill: #10b981; font-weight: bold; }}
        .line {{ stroke: #374151; stroke-width: 2; }}
    </style>
    <text x="20" y="35" class="digit">{num1_str.rjust(max_len)}</text>
    <text x="10" y="60" class="op">+</text>
    <text x="20" y="60" class="digit">{num2_str.rjust(max_len)}</text>
    <line x1="10" y1="70" x2="130" y2="70" class="line"/>
    <text x="20" y="95" class="digit">{ans_str.rjust(max_len)}</text>
    </svg>'''
    return svg

# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1():
    """Level 1: Adding to 20"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        if num1 + num2 > 20:
            continue
        
        answer = num1 + num2
        q_type = random.choice(['basic', 'visual', 'missing'])
        
        if q_type == 'basic':
            q_text = f"What is {num1} + {num2}?"
            image_svg = None
        elif q_type == 'visual':
            q_text = f"Add: {num1} + {num2} = ?"
            image_svg = generate_number_line_svg(0, 20, answer, [(num1, answer, f'+{num2}')])
        else:
            q_text = f"{num1} + ? = {answer}"
            answer = num2
            image_svg = None
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, answer + 2]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Count on from {num1}, add {num2} to get {num1 + num2}. ✓",
            'image_svg': image_svg,
            'difficulty': 1, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_2():
    """Level 2: Subtracting to 20"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(5, 20)
        num2 = random.randint(1, num1 - 1)
        answer = num1 - num2
        
        q_type = random.choice(['basic', 'visual', 'missing'])
        
        if q_type == 'basic':
            q_text = f"What is {num1} - {num2}?"
            image_svg = None
        elif q_type == 'visual':
            q_text = f"Subtract: {num1} - {num2} = ?"
            image_svg = generate_number_line_svg(0, 20, answer, [(num1, answer, f'-{num2}')])
        else:
            q_text = f"{num1} - ? = {answer}"
            answer = num2
            image_svg = None
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, answer + 2]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Count back from {num1}, subtract {num2} to get {answer}. ✓",
            'image_svg': image_svg,
            'difficulty': 2, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_3():
    """Level 3: Adding 2-digit numbers (no regrouping)"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        # Ensure no carrying needed
        tens1 = random.randint(1, 5)
        ones1 = random.randint(1, 4)
        tens2 = random.randint(1, 4)
        ones2 = random.randint(1, 5 - ones1)
        
        num1 = tens1 * 10 + ones1
        num2 = tens2 * 10 + ones2
        answer = num1 + num2
        
        q_text = f"What is {num1} + {num2}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, answer + 1]
        options, correct_idx = make_options(answer, wrong)
        
        image_svg = generate_column_addition_svg(num1, num2) if random.random() < 0.7 else None
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Add ones: {ones1} + {ones2} = {ones1+ones2}. Add tens: {tens1} + {tens2} = {tens1+tens2}. Answer: {answer}. ✓",
            'image_svg': image_svg,
            'difficulty': 3, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_4():
    """Level 4: Subtracting 2-digit numbers"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(30, 99)
        num2 = random.randint(10, num1 - 10)
        answer = num1 - num2
        
        q_text = f"What is {num1} - {num2}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, answer + 1, num1 + num2]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Subtract: {num1} - {num2} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 4, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_5():
    """Level 5: Adding 3-digit numbers"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(100, 500)
        num2 = random.randint(100, 400)
        answer = num1 + num2
        
        q_text = f"What is {num1} + {num2}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 100, answer - 100, answer + 10, answer - 10]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Add column by column: {num1} + {num2} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 5, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_6():
    """Level 6: Subtracting 3-digit numbers"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(300, 999)
        num2 = random.randint(100, num1 - 100)
        answer = num1 - num2
        
        q_text = f"What is {num1} - {num2}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 100, answer - 100, answer + 10, num1 + num2]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Subtract column by column: {num1} - {num2} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 6, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_7():
    """Level 7: Addition word problems"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        context = random.choice(list(CONTEXTS.keys()))
        item = random.choice(CONTEXTS[context])
        
        num1 = random.randint(20, 150)
        num2 = random.randint(20, 150)
        answer = num1 + num2
        
        templates = [
            f"{name} has {num1} {item}. They get {num2} more. How many {item} does {name} have now?",
            f"There are {num1} {item} in one box and {num2} {item} in another. How many {item} altogether?",
            f"{name} collected {num1} {item} on Monday and {num2} on Tuesday. What is the total?",
        ]
        q_text = random.choice(templates)
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, num1, num2]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Add: {num1} + {num2} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 7, 'difficulty_band': 'proficient',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_8():
    """Level 8: Subtraction word problems"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        context = random.choice(list(CONTEXTS.keys()))
        item = random.choice(CONTEXTS[context])
        
        num1 = random.randint(50, 200)
        num2 = random.randint(10, num1 - 20)
        answer = num1 - num2
        
        templates = [
            f"{name} had {num1} {item}. They gave away {num2}. How many {item} are left?",
            f"A shop had {num1} {item}. They sold {num2}. How many {item} remain?",
            f"There were {num1} {item}. {num2} were used. How many are left?",
        ]
        q_text = random.choice(templates)
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, num1 + num2, num2]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Subtract: {num1} - {num2} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 8, 'difficulty_band': 'proficient',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_9():
    """Level 9: Mixed operations"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        op_type = random.choice(['add_then_sub', 'sub_then_add', 'compare'])
        
        if op_type == 'add_then_sub':
            num1 = random.randint(50, 150)
            num2 = random.randint(20, 50)
            num3 = random.randint(10, 40)
            answer = num1 + num2 - num3
            q_text = f"What is {num1} + {num2} - {num3}?"
            explanation = f"First: {num1} + {num2} = {num1+num2}. Then: {num1+num2} - {num3} = {answer}. ✓"
            
        elif op_type == 'sub_then_add':
            num1 = random.randint(100, 200)
            num2 = random.randint(20, 50)
            num3 = random.randint(10, 40)
            answer = num1 - num2 + num3
            q_text = f"What is {num1} - {num2} + {num3}?"
            explanation = f"First: {num1} - {num2} = {num1-num2}. Then: {num1-num2} + {num3} = {answer}. ✓"
            
        else:  # compare
            num1 = random.randint(100, 500)
            num2 = random.randint(100, 500)
            answer = abs(num1 - num2)
            bigger = max(num1, num2)
            smaller = min(num1, num2)
            q_text = f"What is the difference between {bigger} and {smaller}?"
            explanation = f"Difference: {bigger} - {smaller} = {answer}. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, answer + 20, answer - 5]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': None,
            'difficulty': 9, 'difficulty_band': 'proficient',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_10():
    """Level 10: Multi-step problems"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        name2 = random.choice([n for n in IRISH_NAMES if n != name])
        
        problem_type = random.randint(1, 3)
        
        if problem_type == 1:
            # Total then split
            total = random.randint(100, 300)
            part1 = random.randint(30, total // 2)
            part2 = random.randint(20, total - part1 - 20)
            answer = total - part1 - part2
            q_text = f"{name} has {total} stickers. They give {part1} to {name2} and {part2} to a friend. How many stickers does {name} have left?"
            explanation = f"Step 1: {total} - {part1} = {total-part1}. Step 2: {total-part1} - {part2} = {answer}. ✓"
            
        elif problem_type == 2:
            # Combine then compare
            a = random.randint(50, 100)
            b = random.randint(30, 80)
            c = random.randint(100, 200)
            answer = (a + b) - c if (a + b) > c else c - (a + b)
            total_ab = a + b
            q_text = f"{name} has {a} cards and {name2} has {b} cards. Together they have how many more or fewer cards than {c}?"
            bigger = max(total_ab, c)
            smaller = min(total_ab, c)
            answer = bigger - smaller
            q_text = f"{name} has {a} cards and {name2} has {b} cards together. How many more cards do they need to have {c}?" if c > total_ab else f"{name} has {a} cards and {name2} has {b} cards together. They have how many more than {c}?"
            explanation = f"Step 1: {a} + {b} = {total_ab}. Step 2: Difference from {c} is {answer}. ✓"
            
        else:
            # Running total
            start = random.randint(50, 100)
            add1 = random.randint(20, 50)
            sub1 = random.randint(10, 30)
            add2 = random.randint(15, 40)
            answer = start + add1 - sub1 + add2
            q_text = f"A jar has {start} sweets. {add1} are added, {sub1} are eaten, then {add2} more are added. How many sweets now?"
            explanation = f"{start} + {add1} = {start+add1}, - {sub1} = {start+add1-sub1}, + {add2} = {answer}. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, answer + 20, answer - 5]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': None,
            'difficulty': 10, 'difficulty_band': 'advanced',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_11():
    """Level 11: Estimation"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        est_type = random.choice(['round_add', 'round_sub', 'closest'])
        
        if est_type == 'round_add':
            num1 = random.randint(100, 900)
            num2 = random.randint(100, 900)
            est1 = round(num1, -2)
            est2 = round(num2, -2)
            answer = int(est1 + est2)
            q_text = f"Estimate {num1} + {num2} by rounding to the nearest 100."
            explanation = f"{num1} ≈ {int(est1)}, {num2} ≈ {int(est2)}. Estimate: {answer}. ✓"
            
        elif est_type == 'round_sub':
            num1 = random.randint(500, 999)
            num2 = random.randint(100, 400)
            est1 = round(num1, -2)
            est2 = round(num2, -2)
            answer = int(est1 - est2)
            q_text = f"Estimate {num1} - {num2} by rounding to the nearest 100."
            explanation = f"{num1} ≈ {int(est1)}, {num2} ≈ {int(est2)}. Estimate: {answer}. ✓"
            
        else:
            num1 = random.randint(200, 800)
            num2 = random.randint(100, 400)
            actual = num1 + num2
            good_est = round(num1, -2) + round(num2, -2)
            answer = int(good_est)
            q_text = f"Which is the best estimate for {num1} + {num2}?"
            explanation = f"Round both numbers and add. Best estimate: {answer}. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 100, answer - 100, answer + 200, answer - 50]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': None,
            'difficulty': 11, 'difficulty_band': 'advanced',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge - Mixed"""
    questions = []
    used = set()
    
    generators = [generate_level_9, generate_level_10, generate_level_11]
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        gen = random.choice(generators)
        source = gen()
        if source:
            q = random.choice(source)
            if q['question_text'] not in used:
                used.add(q['question_text'])
                q['difficulty'] = 12
                q['difficulty_band'] = 'advanced'
                questions.append(q)
    
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
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"L{level} Q{i}: Duplicate options")
        
        if q['mode'] != 'numeracy':
            errors.append(f"L{level} Q{i}: Wrong mode")
    
    print("\n" + "="*60)
    print("VALIDATION - Addition & Subtraction")
    print("="*60)
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} {status}")
    print("="*60)
    print(f"Total: {len(questions)} | Errors: {len(errors)}")
    
    return len(errors)

def insert_questions(questions):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    print(f"Deleted {cursor.rowcount} existing questions")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (question_text, option_a, option_b, option_c, option_d,
             correct_answer, topic, difficulty_level, difficulty_band,
             mode, explanation, image_svg, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (q['question_text'], q['option_a'], q['option_b'],
              q['option_c'], q['option_d'], q['correct_idx'],
              q['topic'], q['difficulty'], q['difficulty_band'],
              q['mode'], q['explanation'], q.get('image_svg')))
    
    conn.commit()
    conn.close()
    print(f"Inserted {len(questions)} questions")

def main():
    print("="*60)
    print("Addition & Subtraction Generator (Numeracy)")
    print("="*60)
    
    all_questions = []
    generators = [
        (1, "Adding to 20", generate_level_1),
        (2, "Subtracting to 20", generate_level_2),
        (3, "Adding 2-Digit", generate_level_3),
        (4, "Subtracting 2-Digit", generate_level_4),
        (5, "Adding 3-Digit", generate_level_5),
        (6, "Subtracting 3-Digit", generate_level_6),
        (7, "Word Problems (+)", generate_level_7),
        (8, "Word Problems (−)", generate_level_8),
        (9, "Mixed Operations", generate_level_9),
        (10, "Multi-Step Problems", generate_level_10),
        (11, "Estimation", generate_level_11),
        (12, "Mastery Challenge", generate_level_12),
    ]
    
    for level, name, gen_func in generators:
        print(f"Level {level}: {name}...")
        questions = gen_func()
        print(f"  -> {len(questions)} questions")
        all_questions.extend(questions)
    
    validate_questions(all_questions)
    
    response = input("\nInsert into database? (y/n): ").strip().lower()
    if response == 'y':
        insert_questions(all_questions)
        print("✓ Done!")

if __name__ == "__main__":
    main()
