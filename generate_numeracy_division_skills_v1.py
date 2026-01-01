#!/usr/bin/env python3
"""
AgentMath - Division Skills Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Sharing equally, division facts, dividing by 2/5/10
  L4-6:   Developing - Short division, remainders, dividing by 10/100
  L7-9:   Proficient - Long division, word problems, interpreting remainders
  L10-12: Advanced - Multi-step, problem solving, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'division_skills'
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
    'sharing': ['sweets', 'stickers', 'cards', 'crayons', 'marbles'],
    'groups': ['students', 'players', 'children', 'people', 'friends'],
    'containers': ['boxes', 'bags', 'packets', 'jars', 'baskets'],
    'food': ['apples', 'oranges', 'biscuits', 'grapes', 'strawberries']
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
        fallback = str(int(correct) + fallback_idx * 2) if str(correct).lstrip('-').isdigit() else f"{correct}_{fallback_idx}"
        if fallback not in options:
            options.append(fallback)
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    return options, options.index(correct_str)

def generate_sharing_svg(total, groups):
    """Generate SVG showing equal sharing"""
    per_group = total // groups
    remainder = total % groups
    
    width = groups * 80 + 20
    height = 100
    
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .group-box {{ fill: #f3f4f6; stroke: #d1d5db; rx: 8; }}
        .dot {{ fill: #10b981; }}
        .label {{ font-size: 12px; fill: #374151; text-anchor: middle; }}
    </style>'''
    
    for g in range(groups):
        x_base = 15 + g * 80
        svg += f'<rect x="{x_base}" y="10" width="70" height="60" class="group-box"/>'
        svg += f'<text x="{x_base + 35}" y="85" class="label">Group {g+1}</text>'
        
        # Draw dots for items in this group
        for i in range(min(per_group, 8)):
            row = i // 4
            col = i % 4
            svg += f'<circle cx="{x_base + 12 + col * 15}" cy="{25 + row * 20}" r="5" class="dot"/>'
    
    svg += '</svg>'
    return svg

def format_number(n):
    return f"{n:,}"

# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1():
    """Level 1: Sharing Equally"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        groups = random.randint(2, 5)
        per_group = random.randint(2, 6)
        total = groups * per_group
        answer = per_group
        
        item = random.choice(CONTEXTS['sharing'])
        name = random.choice(IRISH_NAMES)
        
        q_type = random.choice(['share', 'visual', 'each'])
        
        if q_type == 'share':
            q_text = f"{name} shares {total} {item} equally among {groups} friends. How many does each friend get?"
            image_svg = None
        elif q_type == 'visual':
            q_text = f"Share {total} dots into {groups} equal groups. How many in each group?"
            image_svg = generate_sharing_svg(total, groups)
        else:
            q_text = f"{total} {item} are shared equally into {groups} groups. How many in each group?"
            image_svg = None
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, total, groups]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{total} ÷ {groups} = {answer}. Each group gets {answer}. ✓",
            'image_svg': image_svg,
            'difficulty': 1, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_2():
    """Level 2: Division Facts"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        divisor = random.randint(2, 10)
        quotient = random.randint(2, 12)
        dividend = divisor * quotient
        answer = quotient
        
        q_type = random.choice(['basic', 'missing', 'inverse'])
        
        if q_type == 'basic':
            q_text = f"What is {dividend} ÷ {divisor}?"
        elif q_type == 'missing':
            q_text = f"{dividend} ÷ ? = {quotient}"
            answer = divisor
        else:
            q_text = f"If {divisor} × {quotient} = {dividend}, what is {dividend} ÷ {divisor}?"
            answer = quotient
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, answer + 2, divisor + quotient]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{dividend} ÷ {divisor} = {quotient}. ✓",
            'image_svg': None,
            'difficulty': 2, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_3():
    """Level 3: Dividing by 2, 5, 10"""
    questions = []
    used = set()
    
    divisors = [2, 5, 10]
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        divisor = random.choice(divisors)
        quotient = random.randint(3, 20)
        dividend = divisor * quotient
        answer = quotient
        
        q_type = random.choice(['basic', 'halving', 'pattern'])
        
        if q_type == 'basic':
            q_text = f"What is {dividend} ÷ {divisor}?"
        elif q_type == 'halving' and divisor == 2:
            q_text = f"What is half of {dividend}?"
        else:
            q_text = f"Divide {dividend} by {divisor}."
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, answer * 2, dividend]
        options, correct_idx = make_options(answer, wrong)
        
        if divisor == 2:
            tip = "Halving means dividing by 2"
        elif divisor == 5:
            tip = "Count in 5s"
        else:
            tip = "Remove the zero"
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{dividend} ÷ {divisor} = {answer}. {tip}. ✓",
            'image_svg': None,
            'difficulty': 3, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_4():
    """Level 4: Short Division (no remainder)"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        divisor = random.randint(2, 9)
        quotient = random.randint(11, 50)
        dividend = divisor * quotient
        answer = quotient
        
        q_text = f"What is {dividend} ÷ {divisor}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, answer + 10, answer - 5]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Short division: {dividend} ÷ {divisor} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 4, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_5():
    """Level 5: Division with Remainders"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        divisor = random.randint(3, 9)
        quotient = random.randint(5, 20)
        remainder = random.randint(1, divisor - 1)
        dividend = divisor * quotient + remainder
        
        q_type = random.choice(['full', 'remainder_only', 'quotient_only'])
        
        if q_type == 'full':
            q_text = f"What is {dividend} ÷ {divisor}? (Give answer with remainder)"
            answer = f"{quotient} r {remainder}"
            wrong = [f"{quotient} r {remainder+1}", f"{quotient+1} r {remainder}", f"{quotient-1} r {remainder}", str(quotient)]
        elif q_type == 'remainder_only':
            q_text = f"What is the remainder when {dividend} is divided by {divisor}?"
            answer = remainder
            wrong = [remainder + 1, remainder - 1, quotient, divisor]
        else:
            q_text = f"How many times does {divisor} go into {dividend}?"
            answer = quotient
            wrong = [quotient + 1, quotient - 1, remainder, dividend // 10]
        
        if q_text in used:
            continue
        used.add(q_text)
        
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{dividend} ÷ {divisor} = {quotient} remainder {remainder}. ✓",
            'image_svg': None,
            'difficulty': 5, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_6():
    """Level 6: Dividing by 10, 100"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        divisor = random.choice([10, 100])
        
        if divisor == 10:
            quotient = random.randint(5, 99)
        else:
            quotient = random.randint(5, 50)
        
        dividend = divisor * quotient
        answer = quotient
        
        q_text = f"What is {format_number(dividend)} ÷ {divisor}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer * 10, answer // 10 if answer >= 10 else answer + 5, answer + 10, dividend]
        options, correct_idx = make_options(answer, wrong)
        
        tip = "remove one zero" if divisor == 10 else "remove two zeros"
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"To divide by {divisor}, {tip}: {format_number(dividend)} ÷ {divisor} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 6, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_7():
    """Level 7: Long Division"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        divisor = random.randint(11, 25)
        quotient = random.randint(10, 40)
        dividend = divisor * quotient
        answer = quotient
        
        q_text = f"What is {format_number(dividend)} ÷ {divisor}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 5, answer - 5, answer + 10, answer - 2]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Long division: {format_number(dividend)} ÷ {divisor} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 7, 'difficulty_band': 'proficient',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_8():
    """Level 8: Division Word Problems"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        item = random.choice(CONTEXTS['sharing'])
        container = random.choice(CONTEXTS['containers'])
        
        divisor = random.randint(3, 12)
        quotient = random.randint(5, 20)
        total = divisor * quotient
        answer = quotient
        
        templates = [
            f"{name} has {total} {item} to share equally among {divisor} friends. How many does each friend get?",
            f"There are {total} {item} to pack into {container}. Each {container[:-1]} holds {divisor}. How many {container} are needed?",
            f"A class of {total} students is split into {divisor} equal groups. How many students in each group?",
            f"{total} {item} are arranged in rows of {divisor}. How many rows are there?",
        ]
        
        q_text = random.choice(templates)
        
        # Fix the template that has answer = total // per_container
        if "Each" in q_text and "holds" in q_text:
            per_container = divisor
            answer = total // per_container
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 2, answer - 2, total, divisor]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{total} ÷ {divisor} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 8, 'difficulty_band': 'proficient',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_9():
    """Level 9: Interpreting Remainders"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        
        problem_type = random.randint(1, 3)
        
        if problem_type == 1:
            # Round up (need extra)
            total = random.randint(25, 60)
            per_group = random.randint(4, 8)
            quotient = total // per_group
            remainder = total % per_group
            answer = quotient + 1 if remainder > 0 else quotient
            q_text = f"{name} has {total} eggs. Egg boxes hold {per_group} eggs. How many boxes does {name} need to store ALL the eggs?"
            explanation = f"{total} ÷ {per_group} = {quotient} r {remainder}. Need {answer} boxes to fit all eggs. ✓"
            
        elif problem_type == 2:
            # Round down (leftover)
            total = random.randint(30, 70)
            per_group = random.randint(5, 10)
            quotient = total // per_group
            remainder = total % per_group
            answer = quotient
            q_text = f"There are {total} sweets. {per_group} sweets fill one bag. How many FULL bags can be made?"
            explanation = f"{total} ÷ {per_group} = {quotient} full bags (with {remainder} left over). ✓"
            
        else:
            # Remainder is the answer
            total = random.randint(20, 50)
            per_group = random.randint(4, 8)
            quotient = total // per_group
            remainder = total % per_group
            if remainder == 0:
                total += random.randint(1, per_group - 1)
                remainder = total % per_group
            answer = remainder
            q_text = f"{total} children line up in rows of {per_group}. How many children are in the incomplete row?"
            explanation = f"{total} ÷ {per_group} = {quotient} r {remainder}. The incomplete row has {remainder} children. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1 if answer > 1 else answer + 2, quotient, total // 10]
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
    """Level 10: Multi-Step Division Problems"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        name2 = random.choice([n for n in IRISH_NAMES if n != name])
        
        problem_type = random.randint(1, 3)
        
        if problem_type == 1:
            # Divide then add
            total1 = random.randint(24, 60)
            divisor = random.randint(3, 6)
            share = total1 // divisor
            extra = random.randint(5, 15)
            answer = share + extra
            q_text = f"{total1} sweets are shared equally among {divisor} children. {name} gets their share plus {extra} bonus sweets. How many does {name} have?"
            explanation = f"Step 1: {total1} ÷ {divisor} = {share}. Step 2: {share} + {extra} = {answer}. ✓"
            
        elif problem_type == 2:
            # Two divisions
            total1 = random.randint(30, 60)
            divisor1 = random.randint(2, 5)
            total2 = random.randint(20, 40)
            divisor2 = random.randint(2, 4)
            share1 = total1 // divisor1
            share2 = total2 // divisor2
            answer = share1 + share2
            q_text = f"{name} divides {total1} marbles among {divisor1} friends and {total2} cards among {divisor2} friends. Each friend gets how many items total?"
            explanation = f"Marbles: {total1}÷{divisor1}={share1}. Cards: {total2}÷{divisor2}={share2}. Total: {answer}. ✓"
            
        else:
            # Multiply then divide
            groups = random.randint(3, 6)
            per_group = random.randint(8, 15)
            total = groups * per_group
            new_groups = random.randint(2, 4)
            answer = total // new_groups
            q_text = f"There are {groups} classes with {per_group} students each. All students split into {new_groups} teams. How many per team?"
            explanation = f"Step 1: {groups} × {per_group} = {total}. Step 2: {total} ÷ {new_groups} = {answer}. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 5, answer - 5, answer + 10, answer - 2]
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
    """Level 11: Problem Solving"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        
        problem_type = random.randint(1, 4)
        
        if problem_type == 1:
            # Money sharing
            total = random.randint(5, 20) * 10  # €50 to €200
            people = random.randint(2, 5)
            answer = total // people
            q_text = f"€{total} is shared equally among {people} people. How many euro does each person get?"
            explanation = f"€{total} ÷ {people} = €{answer} each. ✓"
            
        elif problem_type == 2:
            # Rate/time
            total_distance = random.randint(50, 200)
            speed = random.randint(10, 50)
            total_distance = speed * random.randint(2, 5)  # Ensure clean division
            answer = total_distance // speed
            q_text = f"A car travels {total_distance} km at {speed} km per hour. How many hours does the journey take?"
            explanation = f"{total_distance} ÷ {speed} = {answer} hours. ✓"
            
        elif problem_type == 3:
            # Average
            total = random.randint(100, 300)
            count = random.randint(4, 10)
            total = count * random.randint(15, 35)  # Ensure clean division
            answer = total // count
            q_text = f"{name} scored {total} points in {count} games. What was the average score per game?"
            explanation = f"Average = {total} ÷ {count} = {answer} points per game. ✓"
            
        else:
            # Working backwards
            quotient = random.randint(8, 25)
            divisor = random.randint(4, 12)
            dividend = quotient * divisor
            answer = dividend
            q_text = f"A number divided by {divisor} equals {quotient}. What is the number?"
            explanation = f"? ÷ {divisor} = {quotient}, so ? = {quotient} × {divisor} = {answer}. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, answer + 5, answer * 2]
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
    """Level 12: Mastery Challenge"""
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
    
    print("\n" + "="*60)
    print("VALIDATION - Division Skills")
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
    print("Division Skills Generator (Numeracy)")
    print("="*60)
    
    all_questions = []
    generators = [
        (1, "Sharing Equally", generate_level_1),
        (2, "Division Facts", generate_level_2),
        (3, "Dividing by 2,5,10", generate_level_3),
        (4, "Short Division", generate_level_4),
        (5, "Remainders", generate_level_5),
        (6, "Dividing by 10,100", generate_level_6),
        (7, "Long Division", generate_level_7),
        (8, "Word Problems", generate_level_8),
        (9, "Interpreting Remainders", generate_level_9),
        (10, "Multi-Step Problems", generate_level_10),
        (11, "Problem Solving", generate_level_11),
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
