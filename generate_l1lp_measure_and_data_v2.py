"""
AgentMath L1LP Question Generator
Topic: Measure and Data
Learning Outcomes: 2.22 - 2.25
Version: 2.0 - Updated for actual database schema
"""

import sqlite3
import random
import math

TOPIC = 'measure_and_data'
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
IRISH_COINS = [{'value': 1, 'name': '1 cent', 'colour': '#CD7F32'}, {'value': 2, 'name': '2 cent', 'colour': '#CD7F32'},
               {'value': 5, 'name': '5 cent', 'colour': '#CD7F32'}, {'value': 10, 'name': '10 cent', 'colour': '#FFD700'},
               {'value': 20, 'name': '20 cent', 'colour': '#FFD700'}, {'value': 50, 'name': '50 cent', 'colour': '#FFD700'},
               {'value': 100, 'name': '€1', 'colour': '#C0C0C0'}, {'value': 200, 'name': '€2', 'colour': '#C0C0C0'}]

def create_svg_wrapper(content, width=400, height=180):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def svg_circle(x, y, size, colour='#3498DB'):
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2}" fill="{colour}"/>'

def svg_tree(x, y, size='medium'):
    scales = {'small': 0.5, 'medium': 1.0, 'large': 1.5}
    s = scales.get(size, 1.0)
    tw, th, cr = int(15 * s), int(30 * s), int(25 * s)
    return f'<rect x="{x - tw//2}" y="{y - th}" width="{tw}" height="{th}" fill="#8B4513"/><circle cx="{x}" cy="{y - th - cr + 5}" r="{cr}" fill="#27AE60"/>'

def svg_glass(x, y, fill_level='full'):
    levels = {'empty': 0, 'half': 0.5, 'full': 1.0}
    level = levels.get(fill_level, 1.0)
    gh, gw = 70, 40
    wh = int(gh * level * 0.8)
    glass = f'<path d="M{x},{y} L{x + 5},{y + gh} L{x + gw - 5},{y + gh} L{x + gw},{y} Z" fill="none" stroke="#333" stroke-width="2"/>'
    water = f'<rect x="{x + 3}" y="{y + gh - wh - 5}" width="{gw - 6}" height="{wh}" fill="#3498DB" opacity="0.7"/>' if level > 0 else ''
    return glass + water

def svg_rock(x, y):
    return f'<ellipse cx="{x + 35}" cy="{y + 40}" rx="30" ry="20" fill="#7F8C8D"/><ellipse cx="{x + 30}" cy="{y + 35}" rx="8" ry="5" fill="#95A5A6"/>'

def svg_feather(x, y):
    return f'<path d="M{x + 30},{y + 5} Q{x + 15},{y + 30} {x + 30},{y + 60} Q{x + 45},{y + 30} {x + 30},{y + 5}" fill="#3498DB"/><line x1="{x + 30}" y1="{y + 5}" x2="{x + 30}" y2="{y + 65}" stroke="#8B4513" stroke-width="2"/>'

def svg_coin(x, y, coin_data):
    size = 40 if coin_data['value'] >= 100 else 35 if coin_data['value'] >= 10 else 30
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2}" fill="{coin_data["colour"]}" stroke="#333" stroke-width="1"/><text x="{x + size//2}" y="{y + size//2 + 5}" text-anchor="middle" font-size="10">{coin_data["name"]}</text>'

def svg_pictograph_row(x, y, count, colour='#F1C40F'):
    svg = ''
    for i in range(count):
        svg += f'<circle cx="{x + i * 25 + 12}" cy="{y + 12}" r="10" fill="{colour}"/>'
    return svg

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
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            big, small = random.randint(50, 70), random.randint(20, 35)
            svg_c = svg_circle(50, 60, big, COLOURS['blue']) + svg_circle(200, 80, small, COLOURS['red'])
            svg_c += '<text x="75" y="160" text-anchor="middle" font-size="14">A</text><text x="220" y="160" text-anchor="middle" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = 'Which circle is BIGGER?', 'A'
        else:
            big, small = random.randint(50, 70), random.randint(20, 35)
            svg_c = svg_circle(50, 60, big, COLOURS['blue']) + svg_circle(200, 80, small, COLOURS['red'])
            svg_c += '<text x="75" y="160" text-anchor="middle" font-size="14">A</text><text x="220" y="160" text-anchor="middle" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = 'Which circle is SMALLER?', 'B'
        options = ['A', 'B', '', '']
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 1))
    return questions

def generate_level_2_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        svg_c = f'<line x1="50" y1="60" x2="250" y2="60" stroke="{COLOURS["blue"]}" stroke-width="8"/>'
        svg_c += f'<line x1="50" y1="110" x2="130" y2="110" stroke="{COLOURS["red"]}" stroke-width="8"/>'
        svg_c += '<text x="30" y="65" font-size="14">A</text><text x="30" y="115" font-size="14">B</text>'
        svg = create_svg_wrapper(svg_c)
        if i % 2 == 0:
            question, correct = 'Which line is LONGER?', 'A'
        else:
            question, correct = 'Which line is SHORTER?', 'B'
        options = ['A', 'B', '', '']
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 2))
    return questions

def generate_level_3_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        svg_c = svg_rock(80, 80) + svg_feather(250, 70)
        svg_c += '<text x="110" y="160" text-anchor="middle" font-size="12">Rock</text><text x="280" y="160" text-anchor="middle" font-size="12">Feather</text>'
        svg = create_svg_wrapper(svg_c)
        if i % 2 == 0:
            question, correct = 'Which is HEAVIER?', 'Rock'
        else:
            question, correct = 'Which is LIGHTER?', 'Feather'
        options = ['Rock', 'Feather', 'Same weight', '']
        random.shuffle(options[:3])
        questions.append(make_question(question, options, correct, f'The {correct.lower()} is correct!', svg, 3))
    return questions

def generate_level_4_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        states = [('full', 'half', 'empty'), ('half', 'empty', 'full'), ('empty', 'full', 'half')]
        s1, s2, s3 = states[i % 3]
        svg_c = svg_glass(80, 50, s1) + svg_glass(180, 50, s2) + svg_glass(280, 50, s3)
        svg_c += '<text x="100" y="150" text-anchor="middle" font-size="12">A</text>'
        svg_c += '<text x="200" y="150" text-anchor="middle" font-size="12">B</text>'
        svg_c += '<text x="300" y="150" text-anchor="middle" font-size="12">C</text>'
        svg = create_svg_wrapper(svg_c)
        target = random.choice(['full', 'empty', 'half'])
        idx = [s1, s2, s3].index(target)
        correct = ['A', 'B', 'C'][idx]
        question = f'Which glass is {target.upper()}?'
        options = ['A', 'B', 'C', '']
        questions.append(make_question(question, options, correct, f'Glass {correct} is {target}!', svg, 4))
    return questions

def generate_level_5_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        sizes = [30, 50, 70]
        random.shuffle(sizes)
        svg_c = ''
        labels = ['A', 'B', 'C']
        for j, size in enumerate(sizes):
            svg_c += svg_circle(70 + j * 110, 90 - size//2, size, COLOURS['blue'])
            svg_c += f'<text x="{70 + j*110 + size//2}" y="160" text-anchor="middle" font-size="14">{labels[j]}</text>'
        svg = create_svg_wrapper(svg_c)
        size_map = {sizes[j]: labels[j] for j in range(3)}
        target = random.choice([70, 30, 50])
        correct = size_map[target]
        target_name = 'BIGGEST' if target == 70 else 'SMALLEST' if target == 30 else 'MIDDLE'
        question = f'Which is the {target_name}?'
        options = ['A', 'B', 'C', 'All same']
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 5))
    return questions

def generate_level_6_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        coin = random.choice(IRISH_COINS)
        svg_c = svg_coin(160, 50, coin)
        svg = create_svg_wrapper(svg_c)
        wrong = [c['name'] for c in IRISH_COINS if c['name'] != coin['name']]
        options = [coin['name']] + random.sample(wrong, 3)
        random.shuffle(options)
        questions.append(make_question('What coin is this?', options, coin['name'], f'This is a {coin["name"]} coin!', svg, 6))
    return questions

def generate_level_7_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        c1, c2 = random.choice(IRISH_COINS[:6]), random.choice(IRISH_COINS[:6])
        while c1['value'] == c2['value']:
            c2 = random.choice(IRISH_COINS[:6])
        svg_c = svg_coin(100, 60, c1) + svg_coin(220, 60, c2)
        svg_c += '<text x="130" y="140" text-anchor="middle" font-size="12">A</text><text x="250" y="140" text-anchor="middle" font-size="12">B</text>'
        svg = create_svg_wrapper(svg_c)
        if i % 2 == 0:
            question = 'Which coin is worth MORE?'
            correct = 'A' if c1['value'] > c2['value'] else 'B'
        else:
            question = 'Which coin is worth LESS?'
            correct = 'A' if c1['value'] < c2['value'] else 'B'
        options = ['A', 'B', 'Same value', 'Cannot tell']
        questions.append(make_question(question, options, correct, f'Coin {correct} is the answer!', svg, 7))
    return questions

def generate_level_8_questions():
    questions = []
    items = [{'name': 'Apple', 'price': 20}, {'name': 'Sweet', 'price': 10}, {'name': 'Biscuit', 'price': 10}, {'name': 'Juice', 'price': 50}]
    for i in range(QUESTIONS_PER_LEVEL):
        item = random.choice(items)
        if i % 3 == 0:
            # Exact money - find coin matching price
            matching_coins = [c for c in IRISH_COINS if c['value'] == item['price']]
            if matching_coins:
                have_coin = matching_coins[0]
                correct = 'Yes, exactly right'
            else:
                have_coin = next(c for c in IRISH_COINS if c['value'] > item['price'])
                correct = 'Yes, with change'
        elif i % 3 == 1:
            # More money - find coin worth more than price
            have_coin = next(c for c in IRISH_COINS if c['value'] > item['price'])
            correct = 'Yes, with change'
        else:
            # Not enough - find coin worth less than price
            smaller_coins = [c for c in IRISH_COINS if c['value'] < item['price']]
            if smaller_coins:
                have_coin = random.choice(smaller_coins)
            else:
                have_coin = IRISH_COINS[0]  # Fallback to 1 cent
            correct = 'No, not enough'
        svg_c = f'<text x="200" y="40" text-anchor="middle" font-size="14">You have:</text>'
        svg_c += svg_coin(160, 50, have_coin)
        svg_c += f'<text x="200" y="120" text-anchor="middle" font-size="14">{item["name"]} costs {item["price"]} cent</text>'
        svg = create_svg_wrapper(svg_c)
        options = ['Yes, exactly right', 'Yes, with change', 'No, not enough', 'Not sure']
        questions.append(make_question(f'Can you buy the {item["name"]}?', options, correct, f'{correct}!', svg, 8))
    return questions

def generate_level_9_questions():
    questions = []
    hot_things = ['sun', 'fire', 'hot chocolate', 'oven']
    cold_things = ['ice cream', 'snow', 'fridge', 'ice cube']
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            hot = random.choice(hot_things)
            svg_c = f'<text x="200" y="90" text-anchor="middle" font-size="18">🔥 or ❄️?</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = f'Is "{hot}" hot or cold?', 'Hot'
        else:
            cold = random.choice(cold_things)
            svg_c = f'<text x="200" y="90" text-anchor="middle" font-size="18">🔥 or ❄️?</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = f'Is "{cold}" hot or cold?', 'Cold'
        options = ['Hot', 'Cold', 'Warm', 'Freezing']
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 9))
    return questions

def generate_level_10_questions():
    questions = []
    categories = ['Apples', 'Bananas', 'Oranges']
    cols = [COLOURS['red'], COLOURS['yellow'], COLOURS['orange']]
    for i in range(QUESTIONS_PER_LEVEL):
        counts = {cat: random.randint(1, 5) for cat in categories}
        svg_c = '<text x="200" y="20" text-anchor="middle" font-size="14" font-weight="bold">Favourite Fruits</text>'
        for j, cat in enumerate(categories):
            y = 40 + j * 40
            svg_c += f'<text x="20" y="{y + 15}" font-size="12">{cat}</text>'
            svg_c += svg_pictograph_row(90, y, counts[cat], cols[j])
        svg_c += '<text x="200" y="170" text-anchor="middle" font-size="10">Each ● = 1 person</text>'
        svg = create_svg_wrapper(svg_c)
        if i % 3 == 0:
            cat = random.choice(categories)
            question, correct = f'How many people like {cat}?', str(counts[cat])
            options = list(set([str(counts[c]) for c in categories] + [str(max(counts.values()) + 1)]))[:4]
        elif i % 3 == 1:
            max_cat = max(counts, key=counts.get)
            question, correct = 'Which fruit is MOST popular?', max_cat
            options = categories + ['All the same']
        else:
            min_cat = min(counts, key=counts.get)
            question, correct = 'Which fruit is LEAST popular?', min_cat
            options = categories + ['All the same']
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 10))
    return questions

def generate_level_11_questions():
    questions = []
    scenarios = [
        ('Sort by Colour', [('🍎', 'Red'), ('🍌', 'Yellow'), ('🍊', 'Orange'), ('🫐', 'Blue')], 'Which fruit is RED?', '🍎'),
        ('Sort by Size', [('Elephant', 'Big'), ('Mouse', 'Small'), ('Dog', 'Medium'), ('Ant', 'Tiny')], 'Which animal is BIGGEST?', 'Elephant'),
        ('Sort by Type', [('Apple', 'Fruit'), ('Carrot', 'Vegetable'), ('Banana', 'Fruit'), ('Broccoli', 'Vegetable')], 'Which is a VEGETABLE?', 'Carrot')
    ]
    for i in range(QUESTIONS_PER_LEVEL):
        title, items, question, correct = scenarios[i % len(scenarios)]
        svg_c = f'<text x="200" y="30" text-anchor="middle" font-size="14" font-weight="bold">{title}</text>'
        for j, (item, cat) in enumerate(items):
            x, y = 50 + (j % 2) * 180, 60 + (j // 2) * 50
            svg_c += f'<text x="{x}" y="{y}" font-size="14">{item} - {cat}</text>'
        svg = create_svg_wrapper(svg_c)
        options = [item for item, _ in items]
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is the answer!', svg, 11))
    return questions

def generate_level_12_questions():
    questions = []
    types = ['size', 'length', 'weight', 'capacity', 'money', 'data']
    for i in range(QUESTIONS_PER_LEVEL):
        t = types[i % len(types)]
        if t == 'size':
            sizes = [30, 50, 70]
            random.shuffle(sizes)
            svg_c = ''
            for j, size in enumerate(sizes):
                svg_c += svg_circle(60 + j*110, 90 - size//2, size, COLOURS['blue'])
                svg_c += f'<text x="{60 + j*110 + size//2}" y="150" text-anchor="middle" font-size="12">{["A", "B", "C"][j]}</text>'
            svg = create_svg_wrapper(svg_c)
            size_map = {sizes[j]: ["A", "B", "C"][j] for j in range(3)}
            correct = size_map[70]
            options = ['A', 'B', 'C', 'All same']
            questions.append(make_question('Which is BIGGEST?', options, correct, f'{correct} is biggest!', svg, 12))
        elif t == 'length':
            svg_c = f'<line x1="50" y1="70" x2="200" y2="70" stroke="{COLOURS["blue"]}" stroke-width="6"/>'
            svg_c += f'<line x1="50" y1="110" x2="120" y2="110" stroke="{COLOURS["red"]}" stroke-width="6"/>'
            svg_c += '<text x="30" y="75" font-size="12">A</text><text x="30" y="115" font-size="12">B</text>'
            svg = create_svg_wrapper(svg_c)
            options = ['A', 'B', 'Same length', 'Cannot tell']
            questions.append(make_question('Which line is LONGER?', options, 'A', 'A is longer!', svg, 12))
        elif t == 'weight':
            svg_c = svg_rock(100, 80) + svg_feather(260, 70)
            svg = create_svg_wrapper(svg_c)
            options = ['Rock', 'Feather', 'Same weight', 'Cannot tell']
            questions.append(make_question('Which is HEAVIER?', options, 'Rock', 'The rock is heavier!', svg, 12))
        elif t == 'capacity':
            svg_c = svg_glass(100, 50, 'full') + svg_glass(220, 50, 'empty')
            svg_c += '<text x="120" y="150" text-anchor="middle" font-size="12">A</text><text x="240" y="150" text-anchor="middle" font-size="12">B</text>'
            svg = create_svg_wrapper(svg_c)
            options = ['A', 'B', 'Both', 'Neither']
            questions.append(make_question('Which glass is FULL?', options, 'A', 'A is full!', svg, 12))
        elif t == 'money':
            c1, c2 = IRISH_COINS[4], IRISH_COINS[2]
            svg_c = svg_coin(100, 60, c1) + svg_coin(220, 60, c2)
            svg_c += '<text x="130" y="130" text-anchor="middle" font-size="12">A</text><text x="250" y="130" text-anchor="middle" font-size="12">B</text>'
            svg = create_svg_wrapper(svg_c)
            options = ['A', 'B', 'Same value', 'Cannot tell']
            questions.append(make_question('Which coin is worth MORE?', options, 'A', '20 cent > 5 cent!', svg, 12))
        else:
            counts = {'Red': random.randint(2, 5), 'Blue': random.randint(2, 5), 'Green': random.randint(2, 5)}
            svg_c = '<text x="200" y="25" text-anchor="middle" font-size="12" font-weight="bold">Favourite Colours</text>'
            cols = [COLOURS['red'], COLOURS['blue'], COLOURS['green']]
            for j, (colour, count) in enumerate(counts.items()):
                y = 45 + j * 35
                svg_c += f'<text x="30" y="{y + 12}" font-size="11">{colour}</text>'
                svg_c += svg_pictograph_row(80, y, count, cols[j])
            svg = create_svg_wrapper(svg_c)
            max_colour = max(counts, key=counts.get)
            options = list(counts.keys()) + ['All same']
            questions.append(make_question('Which colour is MOST popular?', options, max_colour, f'{max_colour} is most popular!', svg, 12))
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
