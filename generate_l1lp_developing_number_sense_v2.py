"""
AgentMath L1LP Question Generator
Topic: Developing Number Sense
Learning Outcomes: 2.13 - 2.17
Version: 2.0 - Updated for actual database schema
"""

import sqlite3
import random
import math

TOPIC = 'developing_number_sense'
MODE = 'l1lp'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

DIFFICULTY_BANDS = {
    1: 'Foundation', 2: 'Foundation', 3: 'Foundation', 4: 'Foundation',
    5: 'Developing', 6: 'Developing', 7: 'Developing', 8: 'Developing',
    9: 'Progressing', 10: 'Progressing', 11: 'Consolidating', 12: 'Consolidating'
}

COLOURS = {'red': '#E74C3C', 'blue': '#3498DB', 'green': '#27AE60', 'yellow': '#F1C40F', 'orange': '#E67E22', 'purple': '#9B59B6'}

def svg_dot(x, y, size=30, colour='#3498DB'):
    return f'<circle cx="{x}" cy="{y}" r="{size//2}" fill="{colour}"/>'

def svg_apple(x, y, size=40):
    return f'<g transform="translate({x},{y})"><ellipse cx="{size//2}" cy="{size//2 + 3}" rx="{size//2 - 2}" ry="{size//2}" fill="#E74C3C"/><rect x="{size//2 - 2}" y="0" width="4" height="8" fill="#8B4513"/></g>'

def svg_star(x, y, size=40, colour='#F1C40F'):
    cx, cy = x + size//2, y + size//2
    points = []
    for i in range(5):
        ao = (i * 72 - 90) * math.pi / 180
        ai = ((i * 72) + 36 - 90) * math.pi / 180
        points.append(f"{cx + (size//2-2) * math.cos(ao)},{cy + (size//2-2) * math.sin(ao)}")
        points.append(f"{cx + (size//4) * math.cos(ai)},{cy + (size//4) * math.sin(ai)}")
    return f'<polygon points="{" ".join(points)}" fill="{colour}"/>'

def svg_ball(x, y, size=40, colour='#3498DB'):
    return f'<g transform="translate({x},{y})"><circle cx="{size//2}" cy="{size//2}" r="{size//2 - 2}" fill="{colour}"/></g>'

def svg_cookie(x, y, size=40):
    return f'<g transform="translate({x},{y})"><circle cx="{size//2}" cy="{size//2}" r="{size//2 - 2}" fill="#D4A574"/><circle cx="{size//3}" cy="{size//3}" r="3" fill="#5D4037"/><circle cx="{size*2//3}" cy="{size//3}" r="3" fill="#5D4037"/></g>'

def get_obj_svg(obj_type, x, y, size=40):
    if obj_type == 'apple': return svg_apple(x, y, size)
    elif obj_type == 'star': return svg_star(x, y, size)
    elif obj_type == 'ball': return svg_ball(x, y, size)
    elif obj_type == 'cookie': return svg_cookie(x, y, size)
    else: return svg_dot(x + size//2, y + size//2, size, '#3498DB')

def create_counting_svg(count, obj_type='dot', max_per_row=5, size=35):
    spacing = size + 10
    rows = (count - 1) // max_per_row + 1
    width = min(count, max_per_row) * spacing + 60
    height = rows * spacing + 60
    svg = ''
    for i in range(count):
        row, col = i // max_per_row, i % max_per_row
        x, y = 30 + col * spacing, 30 + row * spacing
        if obj_type == 'dot':
            svg += svg_dot(x + size//2, y + size//2, size, random.choice(list(COLOURS.values())))
        else:
            svg += get_obj_svg(obj_type, x, y, size)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{svg}</svg>'

def create_numeral_svg(numeral, size=80):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 120" width="150" height="120" style="background: white;"><text x="75" y="{60 + size//3}" text-anchor="middle" font-size="{size}" font-weight="bold" fill="#3498DB">{numeral}</text></svg>'

def create_comparison_svg(c1, c2):
    spacing, max_per_row = 40, 5
    r1 = (c1 - 1) // max_per_row + 1 if c1 > 0 else 1
    r2 = (c2 - 1) // max_per_row + 1 if c2 > 0 else 1
    gw = max_per_row * spacing + 20
    h = max(r1, r2) * spacing + 80
    w = gw * 2 + 60
    svg = f'<text x="{gw//2}" y="25" text-anchor="middle" font-size="14" fill="#333">Group A</text>'
    svg += f'<rect x="10" y="35" width="{gw}" height="{h - 50}" fill="#f0f8ff" stroke="#3498DB" rx="5"/>'
    for i in range(c1):
        svg += svg_dot(20 + (i % max_per_row) * spacing + 15, 45 + (i // max_per_row) * spacing + 15, 30, '#3498DB')
    svg += f'<text x="{gw + 40 + gw//2}" y="25" text-anchor="middle" font-size="14" fill="#333">Group B</text>'
    svg += f'<rect x="{gw + 40}" y="35" width="{gw}" height="{h - 50}" fill="#fff0f5" stroke="#E74C3C" rx="5"/>'
    for i in range(c2):
        svg += svg_dot(gw + 50 + (i % max_per_row) * spacing + 15, 45 + (i // max_per_row) * spacing + 15, 30, '#E74C3C')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background: white;">{svg}</svg>'

def create_addition_svg(n1, n2, obj_type='apple'):
    total = n1 + n2
    spacing = 40
    w = max(total, 5) * spacing + 80
    svg = f'<text x="{(n1 * spacing)//2 + 20}" y="25" text-anchor="middle" font-size="12">You have {n1}</text>'
    for i in range(n1):
        svg += get_obj_svg(obj_type, 20 + i * spacing, 35, 35)
    plus_x = n1 * spacing + 30
    svg += f'<text x="{plus_x}" y="60" font-size="24" fill="#27AE60">+</text>'
    svg += f'<text x="{plus_x + 20 + (n2 * spacing)//2}" y="25" text-anchor="middle" font-size="12">{n2} more</text>'
    for i in range(n2):
        svg += get_obj_svg(obj_type, plus_x + 20 + i * spacing, 35, 35)
    svg += f'<text x="{w//2}" y="120" text-anchor="middle" font-size="14">How many altogether?</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 150" width="{w}" height="150" style="background: white;">{svg}</svg>'

def create_subtraction_svg(start, away, obj_type='cookie'):
    spacing = 40
    w = max(start, 5) * spacing + 60
    svg = f'<text x="{w//2}" y="20" text-anchor="middle" font-size="12">You have {start}</text>'
    remaining = start - away
    for i in range(start):
        x = 20 + i * spacing
        svg += get_obj_svg(obj_type, x, 30, 35)
        if i >= remaining:
            svg += f'<line x1="{x}" y1="30" x2="{x + 35}" y2="65" stroke="#E74C3C" stroke-width="3"/>'
            svg += f'<line x1="{x + 35}" y1="30" x2="{x}" y2="65" stroke="#E74C3C" stroke-width="3"/>'
    svg += f'<text x="{w//2}" y="90" text-anchor="middle" font-size="12" fill="#E74C3C">{away} go away</text>'
    svg += f'<text x="{w//2}" y="120" text-anchor="middle" font-size="14">How many left?</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 150" width="{w}" height="150" style="background: white;">{svg}</svg>'

def create_svg_wrapper(content, width=400, height=150):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

# Track question numbers for uniqueness
_question_counter = {}

def make_question(question_text, options, correct_answer, explanation, svg, level):
    global _question_counter
    # Make question_text unique by adding counter
    key = (level, question_text)
    if key not in _question_counter:
        _question_counter[key] = 0
    _question_counter[key] += 1
    
    # Only add number if there are duplicates
    if _question_counter[key] > 1:
        question_text = f"{question_text} (#{_question_counter[key]})"
    
    while len(options) < 4:
        options.append("")
    options = options[:4]
    try:
        correct_index = options.index(correct_answer)
    except ValueError:
        options[0] = correct_answer
        correct_index = 0
    return {'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_answer': correct_index,
            'explanation': explanation, 'image_svg': svg, 'difficulty_band': DIFFICULTY_BANDS[level],
            'question_type': 'visual' if svg else 'text'}

def generate_level_1_questions():
    questions = []
    objects = ['apple', 'star', 'ball', 'dot']
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(1, 5)
        obj_type = random.choice(objects)
        svg = create_counting_svg(count, obj_type, max_per_row=5, size=40)
        wrong = count + 1 if count < 5 else count - 1
        options = [str(count), str(wrong), '', '']
        random.shuffle(options[:2])
        questions.append(make_question('How many can you count?', options, str(count), f'There are {count}!', svg, 1))
    return questions

def generate_level_2_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(5, 10)
        svg = create_counting_svg(count, random.choice(['apple', 'star', 'ball', 'cookie', 'dot']), max_per_row=5, size=35)
        w1 = count + 1 if count < 10 else count - 1
        w2 = count - 1 if count > 5 else count + 2
        options = [str(count), str(w1), str(w2), '']
        random.shuffle(options[:3])
        questions.append(make_question('How many can you count?', options, str(count), f'There are {count}!', svg, 2))
    return questions

def generate_level_3_questions():
    questions = []
    number_words = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten'}
    for i in range(QUESTIONS_PER_LEVEL):
        num = random.randint(1, 10)
        if i % 2 == 0:
            svg = create_numeral_svg(num)
            w1, w2 = num + 1 if num < 10 else num - 2, num - 1 if num > 1 else num + 2
            options = [number_words[num], number_words[w1], number_words[w2], '']
            random.shuffle(options[:3])
            questions.append(make_question('What number is this?', options, number_words[num], f'This is {num} - "{number_words[num]}"!', svg, 3))
        else:
            svg_c = f'<text x="200" y="80" text-anchor="middle" font-size="36" fill="#333">{number_words[num]}</text>'
            svg = create_svg_wrapper(svg_c)
            w1, w2 = num + 1 if num < 10 else num - 2, num - 1 if num > 1 else num + 2
            options = [str(num), str(w1), str(w2), '']
            random.shuffle(options[:3])
            questions.append(make_question(f'Which numeral shows "{number_words[num]}"?', options, str(num), f'"{number_words[num]}" is {num}!', svg, 3))
    return questions

def generate_level_4_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(1, 10)
        svg = create_counting_svg(count, random.choice(['apple', 'star', 'ball', 'cookie']), max_per_row=5, size=35)
        w1, w2 = count + 1 if count < 10 else count - 2, count - 1 if count > 1 else count + 2
        options = [str(count), str(w1), str(w2), '']
        random.shuffle(options[:3])
        questions.append(make_question('Which number matches?', options, str(count), f'There are {count}!', svg, 4))
    return questions

def generate_level_5_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        c1, c2 = random.randint(1, 8), random.randint(1, 8)
        while c1 == c2:
            c2 = random.randint(1, 8)
        svg = create_comparison_svg(c1, c2)
        if i % 2 == 0:
            correct = 'Group A' if c1 > c2 else 'Group B'
            question = 'Which group has MORE?'
        else:
            correct = 'Group A' if c1 < c2 else 'Group B'
            question = 'Which group has LESS?'
        options = ['Group A', 'Group B', 'Same', 'Not sure']
        questions.append(make_question(question, options, correct, f'A has {c1}, B has {c2}. {correct} is correct!', svg, 5))
    return questions

def generate_level_6_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        target = random.randint(2, 6)
        if i % 3 == 0:
            c1, c2, correct = target, target, 'Yes, same amount'
        else:
            c1 = target
            c2 = target + random.choice([-2, -1, 1, 2])
            c2 = max(1, min(8, c2))
            if c2 == c1: c2 = c1 + 1
            correct = 'No, different amounts'
        svg = create_comparison_svg(c1, c2)
        options = ['Yes, same amount', 'No, different amounts', 'Group A has more', 'Group B has more']
        questions.append(make_question('Do both groups have the SAME amount?', options, correct,
            f'A has {c1}, B has {c2}. {"Same!" if c1 == c2 else "Different!"}', svg, 6))
    return questions

def generate_level_7_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        start = random.randint(1, 9)
        correct = start + 1
        svg = create_counting_svg(start, random.choice(['apple', 'star', 'ball']), max_per_row=5, size=35)
        options = list(set([str(correct), str(start), str(start + 2), str(max(1, start - 1))]))[:4]
        random.shuffle(options)
        questions.append(make_question(f'There are {start}. What is ONE MORE than {start}?', options, str(correct),
            f'{start} + 1 = {correct}!', svg, 7))
    return questions

def generate_level_8_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        start = random.randint(2, 10)
        correct = start - 1
        svg = create_counting_svg(start, random.choice(['apple', 'star', 'ball']), max_per_row=5, size=35)
        options = list(set([str(correct), str(start), str(start + 1), str(max(1, start - 2))]))[:4]
        random.shuffle(options)
        questions.append(make_question(f'There are {start}. What is ONE LESS than {start}?', options, str(correct),
            f'{start} - 1 = {correct}!', svg, 8))
    return questions

def generate_level_9_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(11, 20)
        svg = create_counting_svg(count, random.choice(['dot', 'star', 'ball']), max_per_row=5, size=30)
        w1, w2, w3 = count + 1 if count < 20 else count - 1, count - 1 if count > 11 else count + 2, count + 2 if count < 19 else count - 2
        options = list(set([str(count), str(w1), str(w2), str(w3)]))[:4]
        random.shuffle(options)
        questions.append(make_question('Count carefully. How many?', options, str(count), f'There are {count}!', svg, 9))
    return questions

def generate_level_10_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        n1, n2 = random.randint(1, 5), random.randint(1, 5)
        total = n1 + n2
        svg = create_addition_svg(n1, n2, random.choice(['apple', 'cookie', 'star', 'ball']))
        options = list(set([str(total), str(total + 1), str(total - 1), str(n1)]))[:4]
        random.shuffle(options)
        questions.append(make_question(f'{n1} and {n2} more. How many altogether?', options, str(total),
            f'{n1} + {n2} = {total}!', svg, 10))
    return questions

def generate_level_11_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        start = random.randint(3, 8)
        away = random.randint(1, start - 1)
        remaining = start - away
        svg = create_subtraction_svg(start, away, random.choice(['cookie', 'apple', 'ball', 'star']))
        options = list(set([str(remaining), str(remaining + 1), str(remaining - 1) if remaining > 1 else '0', str(start)]))[:4]
        random.shuffle(options)
        questions.append(make_question(f'{start} items, {away} go away. How many left?', options, str(remaining),
            f'{start} - {away} = {remaining}!', svg, 11))
    return questions

def generate_level_12_questions():
    questions = []
    types = ['count', 'compare', 'one_more', 'one_less', 'combine', 'take_away']
    for i in range(QUESTIONS_PER_LEVEL):
        t = types[i % len(types)]
        if t == 'count':
            count = random.randint(10, 20)
            svg = create_counting_svg(count, 'dot', max_per_row=5, size=28)
            options = [str(count), str(count+1), str(count-1), str(count+2)]
            random.shuffle(options)
            questions.append(make_question('How many dots?', options, str(count), f'There are {count}!', svg, 12))
        elif t == 'compare':
            c1, c2 = random.randint(3, 8), random.randint(3, 8)
            while c1 == c2: c2 = random.randint(3, 8)
            svg = create_comparison_svg(c1, c2)
            correct = 'Group A' if c1 > c2 else 'Group B'
            options = ['Group A', 'Group B', 'Same', 'Cannot tell']
            questions.append(make_question('Which has MORE?', options, correct, f'A={c1}, B={c2}. {correct}!', svg, 12))
        elif t == 'one_more':
            num = random.randint(5, 15)
            svg_c = f'<text x="200" y="80" text-anchor="middle" font-size="48" fill="#3498DB">{num}</text>'
            svg = create_svg_wrapper(svg_c)
            correct = num + 1
            options = [str(correct), str(num), str(num+2), str(num-1)]
            random.shuffle(options)
            questions.append(make_question(f'What is ONE MORE than {num}?', options, str(correct), f'{num}+1={correct}!', svg, 12))
        elif t == 'one_less':
            num = random.randint(5, 15)
            svg_c = f'<text x="200" y="80" text-anchor="middle" font-size="48" fill="#E74C3C">{num}</text>'
            svg = create_svg_wrapper(svg_c)
            correct = num - 1
            options = [str(correct), str(num), str(num+1), str(num-2)]
            random.shuffle(options)
            questions.append(make_question(f'What is ONE LESS than {num}?', options, str(correct), f'{num}-1={correct}!', svg, 12))
        elif t == 'combine':
            n1, n2 = random.randint(2, 6), random.randint(2, 6)
            total = n1 + n2
            svg = create_addition_svg(n1, n2, 'star')
            options = [str(total), str(total+1), str(total-1), str(n1)]
            random.shuffle(options)
            questions.append(make_question(f'{n1} + {n2} = ?', options, str(total), f'{n1}+{n2}={total}!', svg, 12))
        else:
            start, away = random.randint(5, 10), random.randint(1, 4)
            left = start - away
            svg = create_subtraction_svg(start, away, 'cookie')
            options = [str(left), str(left+1), str(left-1) if left > 0 else '0', str(start)]
            random.shuffle(options)
            questions.append(make_question(f'{start} - {away} = ?', options, str(left), f'{start}-{away}={left}!', svg, 12))
    return questions

def generate_all_questions():
    global _question_counter
    _question_counter = {}  # Reset counter
    all_q = []
    gens = [(1, generate_level_1_questions), (2, generate_level_2_questions), (3, generate_level_3_questions),
            (4, generate_level_4_questions), (5, generate_level_5_questions), (6, generate_level_6_questions),
            (7, generate_level_7_questions), (8, generate_level_8_questions), (9, generate_level_9_questions),
            (10, generate_level_10_questions), (11, generate_level_11_questions), (12, generate_level_12_questions)]
    for level, gen in gens:
        print(f"  Generating Level {level}...")
        questions = gen()
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['mode'] = MODE
        all_q.extend(questions)
        print(f"    ✓ {len(questions)} questions generated")
    return all_q

def validate_questions(questions):
    print(f"\nValidating {len(questions)} questions...")
    errors = []
    for i, q in enumerate(questions):
        for f in ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'level', 'topic', 'mode']:
            if f not in q: errors.append(f"Q{i}: Missing {f}")
        if 'correct_answer' in q and (not isinstance(q['correct_answer'], int) or q['correct_answer'] < 0 or q['correct_answer'] > 3):
            errors.append(f"Q{i}: bad correct_answer")
    if errors:
        for e in errors[:10]: print(f"    - {e}")
        return False
    print(f"  ✓ All valid")
    return True

def insert_questions(questions):
    print(f"\nInserting {len(questions)} questions...")
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute('DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?', (TOPIC, MODE))
    print(f"  Removed {cur.rowcount} existing")
    ins = 0
    for q in questions:
        try:
            cur.execute('''INSERT INTO questions_adaptive (topic, mode, difficulty_level, difficulty_band, question_text,
                option_a, option_b, option_c, option_d, correct_answer, explanation, image_svg, question_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (q['topic'], q['mode'], q['level'], q['difficulty_band'], q['question_text'],
                 q['option_a'], q['option_b'], q['option_c'], q['option_d'], q['correct_answer'],
                 q.get('explanation', ''), q.get('image_svg', ''), q.get('question_type', 'visual')))
            ins += 1
        except Exception as e:
            print(f"  Error: {e}")
    conn.commit()
    conn.close()
    print(f"  ✓ Inserted {ins}")
    return ins

def verify_insertion():
    print(f"\nVerifying...")
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute('SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? AND mode = ? GROUP BY difficulty_level', (TOPIC, MODE))
    results = cur.fetchall()
    conn.close()
    total = sum(c for _, c in results)
    for lvl, cnt in results:
        print(f"    Level {lvl}: {cnt} {'✓' if cnt == QUESTIONS_PER_LEVEL else '✗'}")
    expected = QUESTIONS_PER_LEVEL * TOTAL_LEVELS
    print(f"\n  Total: {total} {'✓' if total == expected else '✗'}")
    return total == expected

if __name__ == '__main__':
    print("=" * 60)
    print(f"AgentMath L1LP Generator - {TOPIC}")
    print("=" * 60)
    questions = generate_all_questions()
    if not validate_questions(questions):
        exit(1)
    insert_questions(questions)
    verify_insertion()
    print("=" * 60)
    print("✓ COMPLETE!")
