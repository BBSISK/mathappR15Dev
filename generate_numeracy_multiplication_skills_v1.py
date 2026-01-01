#!/usr/bin/env python3
"""
AgentMath - Multiplication Skills Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Times tables (2,5,10), (3,4), (6,7,8,9)
  L4-6:   Developing - Multiplying by 10/100, 2-digit × 1-digit, 2-digit × 2-digit
  L7-9:   Proficient - Word problems, multi-step, estimation
  L10-12: Advanced - 3-digit × 2-digit, problem solving, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'multiplication_skills'
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
    'food': ['apples', 'oranges', 'sweets', 'biscuits', 'eggs'],
    'sports': ['players', 'teams', 'laps', 'medals', 'points'],
    'toys': ['marbles', 'toy cars', 'blocks', 'balls', 'cards'],
    'containers': ['boxes', 'bags', 'packets', 'trays', 'baskets']
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
        fallback = str(int(correct) + fallback_idx * 7)
        if fallback not in options:
            options.append(fallback)
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    return options, options.index(correct_str)

def generate_array_svg(rows, cols, max_display=10):
    """Generate SVG showing array for multiplication"""
    display_rows = min(rows, max_display)
    display_cols = min(cols, max_display)
    
    width = display_cols * 25 + 20
    height = display_rows * 25 + 20
    
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .dot {{ fill: #10b981; }}
    </style>'''
    
    for r in range(display_rows):
        for c in range(display_cols):
            x = 15 + c * 25
            y = 15 + r * 25
            svg += f'<circle cx="{x}" cy="{y}" r="8" class="dot"/>'
    
    svg += '</svg>'
    return svg

def format_number(n):
    return f"{n:,}"

# ============================================================
# LEVEL GENERATORS
# ============================================================

def generate_level_1():
    """Level 1: Times Tables (2, 5, 10)"""
    questions = []
    used = set()
    
    tables = [2, 5, 10]
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        table = random.choice(tables)
        multiplier = random.randint(1, 12)
        answer = table * multiplier
        
        q_type = random.choice(['basic', 'reverse', 'array'])
        
        if q_type == 'basic':
            q_text = f"What is {table} × {multiplier}?"
            image_svg = None
        elif q_type == 'reverse':
            q_text = f"What is {multiplier} × {table}?"
            image_svg = None
        else:
            q_text = f"How many dots? {table} rows of {multiplier}"
            image_svg = generate_array_svg(table, multiplier) if table <= 5 and multiplier <= 8 else None
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + table, answer - table, answer + 5, table + multiplier]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{table} × {multiplier} = {answer}. ✓",
            'image_svg': image_svg,
            'difficulty': 1, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_2():
    """Level 2: Times Tables (3, 4)"""
    questions = []
    used = set()
    
    tables = [3, 4]
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        table = random.choice(tables)
        multiplier = random.randint(1, 12)
        answer = table * multiplier
        
        q_type = random.choice(['basic', 'reverse', 'missing'])
        
        if q_type == 'basic':
            q_text = f"What is {table} × {multiplier}?"
        elif q_type == 'reverse':
            q_text = f"What is {multiplier} × {table}?"
        else:
            q_text = f"{table} × ? = {answer}"
            answer = multiplier
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, answer + table, answer + 3]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{table} × {multiplier} = {table * multiplier}. ✓",
            'image_svg': None,
            'difficulty': 2, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_3():
    """Level 3: Times Tables (6, 7, 8, 9)"""
    questions = []
    used = set()
    
    tables = [6, 7, 8, 9]
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        table = random.choice(tables)
        multiplier = random.randint(1, 12)
        answer = table * multiplier
        
        q_type = random.choice(['basic', 'reverse', 'missing'])
        
        if q_type == 'basic':
            q_text = f"What is {table} × {multiplier}?"
        elif q_type == 'reverse':
            q_text = f"What is {multiplier} × {table}?"
        else:
            q_text = f"{table} × ? = {answer}"
            answer = multiplier
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 1, answer - 1, answer + table, answer - table]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{table} × {multiplier} = {table * multiplier}. ✓",
            'image_svg': None,
            'difficulty': 3, 'difficulty_band': 'foundation',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_4():
    """Level 4: Multiplying by 10, 100"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        multiplier = random.choice([10, 100])
        num = random.randint(2, 99) if multiplier == 10 else random.randint(2, 50)
        answer = num * multiplier
        
        q_type = random.choice(['basic', 'reverse', 'pattern'])
        
        if q_type == 'basic':
            q_text = f"What is {num} × {multiplier}?"
        elif q_type == 'reverse':
            q_text = f"What is {multiplier} × {num}?"
        else:
            q_text = f"Multiply {num} by {multiplier}."
        
        if q_text in used:
            continue
        used.add(q_text)
        
        if multiplier == 10:
            wrong = [answer + 10, answer - 10, num + 10, num * 100]
        else:
            wrong = [answer + 100, answer - 100, num * 10, answer + 10]
        
        options, correct_idx = make_options(answer, wrong)
        
        tip = "add one zero" if multiplier == 10 else "add two zeros"
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"To multiply by {multiplier}, {tip}: {num} × {multiplier} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 4, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_5():
    """Level 5: 2-digit × 1-digit"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(11, 49)
        num2 = random.randint(2, 9)
        answer = num1 * num2
        
        q_text = f"What is {num1} × {num2}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        # Common errors
        tens = (num1 // 10) * num2 * 10
        ones = (num1 % 10) * num2
        wrong = [answer + 10, answer - 10, tens, ones, answer + num2]
        
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{num1} × {num2}: ({num1//10}×{num2}×10) + ({num1%10}×{num2}) = {tens} + {ones} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 5, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_6():
    """Level 6: 2-digit × 2-digit"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(11, 35)
        num2 = random.randint(11, 25)
        answer = num1 * num2
        
        q_text = f"What is {num1} × {num2}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, answer + 100, num1 + num2, answer - 50]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Use long multiplication: {num1} × {num2} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 6, 'difficulty_band': 'developing',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_7():
    """Level 7: Word Problems"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        context = random.choice(list(CONTEXTS.keys()))
        item = random.choice(CONTEXTS[context])
        container = random.choice(CONTEXTS['containers'])
        
        groups = random.randint(3, 12)
        per_group = random.randint(4, 15)
        answer = groups * per_group
        
        templates = [
            f"{name} has {groups} {container} with {per_group} {item} in each. How many {item} altogether?",
            f"There are {groups} rows of {per_group} {item}. How many {item} in total?",
            f"A shop has {groups} shelves. Each shelf has {per_group} {item}. How many {item} are there?",
            f"{name} buys {groups} packs of {item}. Each pack has {per_group}. How many {item} in total?",
        ]
        q_text = random.choice(templates)
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + groups, answer - per_group, groups + per_group, answer + 10]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Multiply: {groups} × {per_group} = {answer}. ✓",
            'image_svg': None,
            'difficulty': 7, 'difficulty_band': 'proficient',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_8():
    """Level 8: Multi-step Problems"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        name = random.choice(IRISH_NAMES)
        
        problem_type = random.randint(1, 3)
        
        if problem_type == 1:
            # Multiply then add
            groups = random.randint(3, 8)
            per_group = random.randint(5, 12)
            extra = random.randint(5, 20)
            answer = groups * per_group + extra
            q_text = f"{name} has {groups} boxes with {per_group} pencils each, plus {extra} loose pencils. How many pencils in total?"
            explanation = f"Step 1: {groups} × {per_group} = {groups*per_group}. Step 2: {groups*per_group} + {extra} = {answer}. ✓"
            
        elif problem_type == 2:
            # Two multiplications
            groups1 = random.randint(2, 5)
            per1 = random.randint(4, 8)
            groups2 = random.randint(2, 5)
            per2 = random.randint(4, 8)
            answer = groups1 * per1 + groups2 * per2
            q_text = f"{name} has {groups1} bags with {per1} apples and {groups2} bags with {per2} oranges. How many fruits altogether?"
            explanation = f"Step 1: {groups1}×{per1}={groups1*per1}. Step 2: {groups2}×{per2}={groups2*per2}. Total: {answer}. ✓"
            
        else:
            # Multiply then subtract
            groups = random.randint(4, 10)
            per_group = random.randint(6, 12)
            taken = random.randint(5, 15)
            total = groups * per_group
            answer = total - taken
            q_text = f"There are {groups} packs of {per_group} biscuits. {taken} biscuits are eaten. How many are left?"
            explanation = f"Step 1: {groups} × {per_group} = {total}. Step 2: {total} - {taken} = {answer}. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 10, answer - 10, answer + 5, answer - 5]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': None,
            'difficulty': 8, 'difficulty_band': 'proficient',
            'topic': TOPIC, 'mode': MODE
        })
    
    return questions

def generate_level_9():
    """Level 9: Estimation"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        est_type = random.choice(['round_mult', 'closest', 'reasonable'])
        
        if est_type == 'round_mult':
            num1 = random.randint(15, 85)
            num2 = random.randint(3, 9)
            est1 = round(num1, -1)
            answer = int(est1 * num2)
            q_text = f"Estimate {num1} × {num2} by rounding {num1} to the nearest 10."
            explanation = f"{num1} ≈ {int(est1)}. {int(est1)} × {num2} = {answer}. ✓"
            
        elif est_type == 'closest':
            num1 = random.randint(20, 60)
            num2 = random.randint(4, 9)
            actual = num1 * num2
            good_est = round(num1, -1) * num2
            answer = int(good_est)
            q_text = f"Which is the best estimate for {num1} × {num2}?"
            explanation = f"Round {num1} to {round(num1, -1)}, then multiply: {answer}. ✓"
            
        else:
            num1 = random.randint(18, 52)
            num2 = random.randint(3, 8)
            actual = num1 * num2
            answer = int(round(num1, -1) * num2)
            q_text = f"Is {answer} a good estimate for {num1} × {num2}?"
            # Change to multiple choice about estimate
            q_text = f"Estimate: {num1} × {num2} ≈ ?"
            explanation = f"Round and multiply: approximately {answer}. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 20, answer - 20, answer + 50, answer - 10]
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
    """Level 10: 3-digit × 2-digit"""
    questions = []
    used = set()
    
    while len(questions) < QUESTIONS_PER_LEVEL:
        num1 = random.randint(100, 350)
        num2 = random.randint(11, 25)
        answer = num1 * num2
        
        q_text = f"What is {num1} × {num2}?"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 100, answer - 100, answer + 500, answer - 50]
        options, correct_idx = make_options(answer, wrong)
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Long multiplication: {num1} × {num2} = {format_number(answer)}. ✓",
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
            # Cost calculation
            items = random.randint(12, 25)
            price = random.randint(3, 15)
            answer = items * price
            q_text = f"{name} buys {items} items at €{price} each. What is the total cost in euro?"
            explanation = f"{items} × {price} = €{answer}. ✓"
            
        elif problem_type == 2:
            # Area
            length = random.randint(8, 20)
            width = random.randint(5, 15)
            answer = length * width
            q_text = f"A rectangle is {length}m long and {width}m wide. What is its area in square metres?"
            explanation = f"Area = {length} × {width} = {answer} m². ✓"
            
        elif problem_type == 3:
            # Scaling
            original = random.randint(15, 50)
            multiplier = random.randint(3, 8)
            answer = original * multiplier
            q_text = f"A recipe for 1 cake needs {original}g of flour. How much flour for {multiplier} cakes?"
            explanation = f"{original} × {multiplier} = {answer}g. ✓"
            
        else:
            # Time calculation
            weeks = random.randint(3, 12)
            per_week = random.randint(5, 15)
            answer = weeks * per_week * 7
            q_text = f"{name} reads {per_week} pages every day. How many pages in {weeks} weeks?"
            explanation = f"{per_week} × 7 × {weeks} = {per_week} × {weeks * 7} = {answer} pages. ✓"
        
        if q_text in used:
            continue
        used.add(q_text)
        
        wrong = [answer + 20, answer - 20, answer + 50, answer - 10]
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
    print("VALIDATION - Multiplication Skills")
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
    print("Multiplication Skills Generator (Numeracy)")
    print("="*60)
    
    all_questions = []
    generators = [
        (1, "Times Tables (2,5,10)", generate_level_1),
        (2, "Times Tables (3,4)", generate_level_2),
        (3, "Times Tables (6,7,8,9)", generate_level_3),
        (4, "Multiplying by 10,100", generate_level_4),
        (5, "2-Digit × 1-Digit", generate_level_5),
        (6, "2-Digit × 2-Digit", generate_level_6),
        (7, "Word Problems", generate_level_7),
        (8, "Multi-Step Problems", generate_level_8),
        (9, "Estimation", generate_level_9),
        (10, "3-Digit × 2-Digit", generate_level_10),
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
