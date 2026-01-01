"""
AgentMath L1LP Question Generator
Topic: Shape and Space
Learning Outcomes: 2.18 - 2.21
Version: 2.0 - Updated for actual database schema
"""

import sqlite3
import random
import math

TOPIC = 'shape_and_space'
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

def svg_circle(x, y, size=60, colour='#3498DB'):
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2 - 2}" fill="{colour}" stroke="#2980B9" stroke-width="2"/>'

def svg_square(x, y, size=60, colour='#E74C3C'):
    return f'<rect x="{x + 2}" y="{y + 2}" width="{size - 4}" height="{size - 4}" fill="{colour}" stroke="#C0392B" stroke-width="2"/>'

def svg_triangle(x, y, size=60, colour='#F1C40F'):
    return f'<polygon points="{x + size//2},{y + 2} {x + 2},{y + size - 2} {x + size - 2},{y + size - 2}" fill="{colour}" stroke="#D4AC0D" stroke-width="2"/>'

def svg_rectangle(x, y, w=80, h=50, colour='#27AE60'):
    return f'<rect x="{x + 2}" y="{y + 2}" width="{w - 4}" height="{h - 4}" fill="{colour}" stroke="#1E8449" stroke-width="2"/>'

def svg_sphere(x, y, size=60, colour='#3498DB'):
    return f'<g transform="translate({x},{y})"><circle cx="{size//2}" cy="{size//2}" r="{size//2 - 2}" fill="{colour}"/><ellipse cx="{size//3}" cy="{size//3}" rx="{size//6}" ry="{size//8}" fill="white" opacity="0.4"/></g>'

def svg_cube(x, y, size=60, colour='#E74C3C'):
    off = size // 4
    return f'''<g transform="translate({x},{y})">
        <rect x="0" y="{off}" width="{size - off}" height="{size - off}" fill="{colour}" stroke="#333" stroke-width="1"/>
        <polygon points="0,{off} {off},0 {size},0 {size - off},{off}" fill="{COLOURS['orange']}" stroke="#333" stroke-width="1"/>
        <polygon points="{size - off},{off} {size},0 {size},{size - off} {size - off},{size}" fill="{COLOURS['yellow']}" stroke="#333" stroke-width="1"/>
    </g>'''

def svg_cylinder(x, y, size=60, colour='#27AE60'):
    w, h = size * 0.8, size
    cx = x + size//2
    return f'''<g>
        <rect x="{x + size//10}" y="{y + size//6}" width="{w}" height="{int(h * 0.7)}" fill="{colour}" stroke="#333" stroke-width="1"/>
        <ellipse cx="{cx}" cy="{y + size//6 + int(h * 0.7)}" rx="{w//2}" ry="{size//8}" fill="{colour}" stroke="#333" stroke-width="1"/>
        <ellipse cx="{cx}" cy="{y + size//6}" rx="{w//2}" ry="{size//8}" fill="{COLOURS['green']}" stroke="#333" stroke-width="1"/>
    </g>'''

def get_2d_shape(shape, x, y, size=60, colour=None):
    defaults = {'circle': '#3498DB', 'square': '#E74C3C', 'triangle': '#F1C40F', 'rectangle': '#27AE60'}
    c = colour or defaults.get(shape, '#3498DB')
    if shape == 'circle': return svg_circle(x, y, size, c)
    elif shape == 'square': return svg_square(x, y, size, c)
    elif shape == 'triangle': return svg_triangle(x, y, size, c)
    elif shape == 'rectangle': return svg_rectangle(x, y, size + 20, size - 10, c)
    return svg_circle(x, y, size, c)

def get_3d_shape(shape, x, y, size=60, colour=None):
    defaults = {'sphere': '#3498DB', 'cube': '#E74C3C', 'cylinder': '#27AE60'}
    c = colour or defaults.get(shape, '#3498DB')
    if shape == 'sphere' or shape == 'ball': return svg_sphere(x, y, size, c)
    elif shape == 'cube' or shape == 'box': return svg_cube(x, y, size, c)
    elif shape == 'cylinder' or shape == 'can': return svg_cylinder(x, y, size, c)
    return svg_sphere(x, y, size, c)

def create_svg_wrapper(content, width=400, height=180):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def create_position_scene(position):
    svg = f'<rect x="140" y="80" width="80" height="50" fill="#8B4513" stroke="#5D3A1A" stroke-width="2" rx="3"/>'
    svg += f'<text x="180" y="145" text-anchor="middle" font-size="12" fill="#333">box</text>'
    ball_size = 30
    if position == 'on': bx, by = 155, 50
    elif position == 'under': bx, by = 155, 135
    elif position == 'in': bx, by = 155, 85
    elif position == 'beside': bx, by = 230, 95
    else: bx, by = 155, 50
    svg += f'<circle cx="{bx + ball_size//2}" cy="{by + ball_size//2}" r="{ball_size//2}" fill="#3498DB"/>'
    svg += f'<text x="175" y="30" text-anchor="middle" font-size="14" fill="#333">The ball is {position} the box</text>'
    return create_svg_wrapper(svg, 350, 180)

def create_movement_scene(direction):
    cx, cy, alen = 175, 75, 50
    svg = ''
    if direction == 'up':
        svg = f'<line x1="{cx}" y1="{cy + alen//2}" x2="{cx}" y2="{cy - alen//2}" stroke="#27AE60" stroke-width="8"/>'
        svg += f'<polygon points="{cx},{cy - alen//2 - 10} {cx - 15},{cy - alen//2 + 10} {cx + 15},{cy - alen//2 + 10}" fill="#27AE60"/>'
    elif direction == 'down':
        svg = f'<line x1="{cx}" y1="{cy - alen//2}" x2="{cx}" y2="{cy + alen//2}" stroke="#E74C3C" stroke-width="8"/>'
        svg += f'<polygon points="{cx},{cy + alen//2 + 10} {cx - 15},{cy + alen//2 - 10} {cx + 15},{cy + alen//2 - 10}" fill="#E74C3C"/>'
    elif direction == 'left':
        svg = f'<line x1="{cx + alen//2}" y1="{cy}" x2="{cx - alen//2}" y2="{cy}" stroke="#3498DB" stroke-width="8"/>'
        svg += f'<polygon points="{cx - alen//2 - 10},{cy} {cx - alen//2 + 10},{cy - 15} {cx - alen//2 + 10},{cy + 15}" fill="#3498DB"/>'
    elif direction == 'right':
        svg = f'<line x1="{cx - alen//2}" y1="{cy}" x2="{cx + alen//2}" y2="{cy}" stroke="#9B59B6" stroke-width="8"/>'
        svg += f'<polygon points="{cx + alen//2 + 10},{cy} {cx + alen//2 - 10},{cy - 15} {cx + alen//2 - 10},{cy + 15}" fill="#9B59B6"/>'
    svg += f'<text x="{cx}" y="140" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">{direction.upper()}</text>'
    return create_svg_wrapper(svg, 350, 150)

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
    positions = ['on', 'under', 'in']
    for i in range(QUESTIONS_PER_LEVEL):
        pos = random.choice(positions)
        wrong = random.choice([p for p in positions if p != pos])
        svg = create_position_scene(pos)
        options = [pos.title(), wrong.title(), '', '']
        random.shuffle(options[:2])
        questions.append(make_question('Where is the ball?', options, pos.title(), f'The ball is {pos} the box!', svg, 1))
    return questions

def generate_level_2_questions():
    questions = []
    directions = ['up', 'down', 'left', 'right']
    for i in range(QUESTIONS_PER_LEVEL):
        d = random.choice(directions)
        wrong = [x for x in directions if x != d]
        svg = create_movement_scene(d)
        options = [d.title(), wrong[0].title(), wrong[1].title() if i % 2 == 1 else '', '']
        random.shuffle(options[:3 if i % 2 == 1 else 2])
        questions.append(make_question('Which direction is the arrow pointing?', options, d.title(), f'The arrow points {d}!', svg, 2))
    return questions

def generate_level_3_questions():
    questions = []
    shapes = ['circle', 'square']
    for i in range(QUESTIONS_PER_LEVEL):
        shape = random.choice(shapes)
        svg_c = get_2d_shape(shape, 170, 50, 80, random.choice(list(COLOURS.values())))
        svg = create_svg_wrapper(svg_c)
        options = ['Circle', 'Square', 'Triangle', '']
        random.shuffle(options[:3])
        exp = 'perfectly round' if shape == 'circle' else '4 equal sides and 4 corners'
        questions.append(make_question('What shape is this?', options, shape.title(), f'This is a {shape} - it\'s {exp}!', svg, 3))
    return questions

def generate_level_4_questions():
    questions = []
    shapes = ['triangle', 'rectangle']
    for i in range(QUESTIONS_PER_LEVEL):
        shape = random.choice(shapes)
        svg_c = get_2d_shape(shape, 160, 50, 80, random.choice(list(COLOURS.values())))
        svg = create_svg_wrapper(svg_c)
        options = ['Triangle', 'Rectangle', 'Circle', '']
        random.shuffle(options[:3])
        exp = '3 sides and 3 corners' if shape == 'triangle' else '4 sides and 4 corners'
        questions.append(make_question('What shape is this?', options, shape.title(), f'This is a {shape} - it has {exp}!', svg, 4))
    return questions

def generate_level_5_questions():
    questions = []
    real_world = [('circle', 'wheel'), ('circle', 'clock face'), ('square', 'window'), ('rectangle', 'door'), ('rectangle', 'book'), ('triangle', 'roof')]
    for i in range(QUESTIONS_PER_LEVEL):
        shape, obj = random.choice(real_world)
        svg_c = f'<text x="200" y="70" text-anchor="middle" font-size="18">What shape is a</text>'
        svg_c += f'<text x="200" y="100" text-anchor="middle" font-size="24" font-weight="bold" fill="#3498DB">{obj}</text>'
        svg_c += f'<text x="200" y="130" text-anchor="middle" font-size="18">?</text>'
        svg = create_svg_wrapper(svg_c)
        options = ['Circle', 'Square', 'Triangle', 'Rectangle']
        random.shuffle(options)
        questions.append(make_question(f'What shape is a {obj}?', options, shape.title(), f'A {obj} is shaped like a {shape}!', svg, 5))
    return questions

def generate_level_6_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            shape = random.choice(['sphere', 'cube', 'cylinder'])
            svg_c = get_3d_shape(shape, 160, 50, 70)
            svg = create_svg_wrapper(svg_c)
            options = ['Solid (3D)', 'Flat (2D)', 'Not sure', 'Neither']
            questions.append(make_question('Is this shape flat or solid?', options, 'Solid (3D)', f'This is a {shape} - it\'s solid (3D)!', svg, 6))
        else:
            shape = random.choice(['circle', 'square', 'triangle'])
            svg_c = get_2d_shape(shape, 165, 50, 70)
            svg = create_svg_wrapper(svg_c)
            options = ['Flat (2D)', 'Solid (3D)', 'Not sure', 'Neither']
            questions.append(make_question('Is this shape flat or solid?', options, 'Flat (2D)', f'This is a {shape} - it\'s flat (2D)!', svg, 6))
    return questions

def generate_level_7_questions():
    questions = []
    shape_info = [('sphere', 'Ball', 'round all over'), ('cube', 'Box', '6 square faces'), ('cylinder', 'Can', 'round with flat ends')]
    for i in range(QUESTIONS_PER_LEVEL):
        shape, name, desc = random.choice(shape_info)
        svg_c = get_3d_shape(shape, 160, 50, 70)
        svg = create_svg_wrapper(svg_c)
        options = ['Ball (Sphere)', 'Box (Cube)', 'Can (Cylinder)', 'Cone']
        random.shuffle(options)
        correct = f'{name} ({shape.title()})'
        questions.append(make_question('What 3D shape is this?', options, correct, f'This is a {shape} - like a {name.lower()}! It\'s {desc}.', svg, 7))
    return questions

def generate_level_8_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        sort_type = random.choice(['corners', 'sides', 'curved'])
        if sort_type == 'corners':
            svg_c = get_2d_shape('circle', 50, 60, 50) + get_2d_shape('square', 130, 60, 50)
            svg_c += get_2d_shape('triangle', 210, 60, 50) + get_2d_shape('rectangle', 280, 60, 50)
            svg = create_svg_wrapper(svg_c)
            corners = random.choice([3, 4, 0])
            if corners == 3:
                correct, question = 'Triangle', 'Which shape has 3 corners?'
            elif corners == 4:
                correct, question = random.choice(['Square', 'Rectangle']), 'Which shape has 4 corners?'
            else:
                correct, question = 'Circle', 'Which shape has NO corners?'
            options = ['Circle', 'Square', 'Triangle', 'Rectangle']
        elif sort_type == 'sides':
            svg_c = get_2d_shape('triangle', 80, 60, 55) + get_2d_shape('square', 180, 60, 55) + get_2d_shape('circle', 280, 60, 55)
            svg = create_svg_wrapper(svg_c)
            sides = random.choice([3, 4])
            correct = 'Triangle' if sides == 3 else 'Square'
            question = f'Which shape has {sides} sides?'
            options = ['Triangle', 'Square', 'Circle', 'Star']
        else:
            svg_c = get_2d_shape('circle', 80, 60, 55) + get_2d_shape('square', 280, 60, 55)
            svg = create_svg_wrapper(svg_c)
            question, correct = 'Which shape has curved edges?', 'Circle'
            options = ['Circle', 'Square', 'Both', 'Neither']
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 8))
    return questions

def generate_level_9_questions():
    questions = []
    shape_objs = {'circle': ['clock', 'wheel', 'pizza'], 'square': ['window', 'tile', 'cracker'], 'rectangle': ['door', 'book', 'phone'],
                  'sphere': ['ball', 'orange', 'globe'], 'cube': ['dice', 'box', 'ice cube'], 'cylinder': ['can', 'glass', 'candle']}
    for i in range(QUESTIONS_PER_LEVEL):
        shape = random.choice(list(shape_objs.keys()))
        obj = random.choice(shape_objs[shape])
        if shape in ['sphere', 'cube', 'cylinder']:
            svg_c = get_3d_shape(shape, 160, 50, 70)
        else:
            svg_c = get_2d_shape(shape, 165, 50, 70)
        svg = create_svg_wrapper(svg_c)
        wrong_objs = []
        for s, objs in shape_objs.items():
            if s != shape:
                wrong_objs.extend(objs)
        options = [obj.title()] + [o.title() for o in random.sample(wrong_objs, 3)]
        random.shuffle(options)
        questions.append(make_question(f'Which object is shaped like this {shape}?', options, obj.title(), f'A {obj} is shaped like a {shape}!', svg, 9))
    return questions

def generate_level_10_questions():
    questions = []
    props = {'circle': {'sides': 0, 'corners': 0}, 'triangle': {'sides': 3, 'corners': 3}, 'square': {'sides': 4, 'corners': 4}, 'rectangle': {'sides': 4, 'corners': 4}}
    for i in range(QUESTIONS_PER_LEVEL):
        shape = random.choice(['circle', 'triangle', 'square', 'rectangle'])
        prop = random.choice(['sides', 'corners'])
        correct = props[shape][prop]
        svg_c = get_2d_shape(shape, 165, 50, 70)
        svg = create_svg_wrapper(svg_c)
        if correct == 0:
            options = ['0', '1', '2', '4']
        else:
            options = list(set([str(correct), str(correct + 1), str(correct - 1), str(correct + 2)]))[:4]
        random.shuffle(options)
        questions.append(make_question(f'How many {prop} does this {shape} have?', options, str(correct), f'A {shape} has {correct} {prop}!', svg, 10))
    return questions

def generate_level_11_questions():
    questions = []
    descs = [('circle', 'round'), ('circle', 'no corners'), ('square', '4 equal sides'), ('square', '4 corners'),
             ('triangle', '3 sides'), ('triangle', '3 corners'), ('sphere', 'round like a ball'), ('cube', '6 square faces')]
    for i in range(QUESTIONS_PER_LEVEL):
        shape, desc = random.choice(descs)
        if shape in ['sphere', 'cube']:
            svg_c = get_3d_shape(shape, 160, 50, 70)
        else:
            svg_c = get_2d_shape(shape, 165, 50, 70)
        svg = create_svg_wrapper(svg_c)
        wrong = [d[1] for d in descs if d[0] != shape]
        options = [desc] + random.sample(wrong, 3)
        random.shuffle(options)
        questions.append(make_question(f'Which describes this {shape}?', options, desc, f'{shape.title()} is {desc}!', svg, 11))
    return questions

def generate_level_12_questions():
    questions = []
    types = ['identify_2d', 'identify_3d', 'count_property', 'real_world', 'position', 'compare']
    for i in range(QUESTIONS_PER_LEVEL):
        t = types[i % len(types)]
        if t == 'identify_2d':
            shapes = ['circle', 'square', 'triangle', 'rectangle']
            shape = random.choice(shapes)
            svg_c = get_2d_shape(shape, 165, 50, 70, random.choice(list(COLOURS.values())))
            svg = create_svg_wrapper(svg_c)
            options = [s.title() for s in shapes]
            random.shuffle(options)
            questions.append(make_question('What shape is this?', options, shape.title(), f'This is a {shape}!', svg, 12))
        elif t == 'identify_3d':
            shapes = ['sphere', 'cube', 'cylinder']
            shape = random.choice(shapes)
            svg_c = get_3d_shape(shape, 160, 50, 70)
            svg = create_svg_wrapper(svg_c)
            names = {'sphere': 'Ball', 'cube': 'Box', 'cylinder': 'Can'}
            options = [f'{names[s]} ({s.title()})' for s in shapes] + ['Cone']
            random.shuffle(options)
            correct = f'{names[shape]} ({shape.title()})'
            questions.append(make_question('What 3D shape is this?', options, correct, f'This is a {shape}!', svg, 12))
        elif t == 'count_property':
            shape = random.choice(['triangle', 'square', 'rectangle'])
            prop = random.choice(['sides', 'corners'])
            counts = {'triangle': 3, 'square': 4, 'rectangle': 4}
            correct = counts[shape]
            svg_c = get_2d_shape(shape, 165, 50, 70)
            svg = create_svg_wrapper(svg_c)
            options = [str(correct), str(correct+1), str(correct-1), '0']
            random.shuffle(options)
            questions.append(make_question(f'How many {prop}?', options, str(correct), f'{correct} {prop}!', svg, 12))
        elif t == 'real_world':
            pairs = [('circle', 'pizza'), ('square', 'window'), ('rectangle', 'door'), ('triangle', 'roof')]
            shape, obj = random.choice(pairs)
            svg_c = f'<text x="200" y="90" text-anchor="middle" font-size="20">{obj.title()}</text>'
            svg = create_svg_wrapper(svg_c)
            options = ['Circle', 'Square', 'Rectangle', 'Triangle']
            random.shuffle(options)
            questions.append(make_question(f'What shape is a {obj}?', options, shape.title(), f'A {obj} is a {shape}!', svg, 12))
        elif t == 'position':
            pos = random.choice(['on', 'under', 'beside'])
            svg = create_position_scene(pos)
            options = ['On', 'Under', 'Beside', 'In']
            random.shuffle(options)
            questions.append(make_question('Where is the ball?', options, pos.title(), f'The ball is {pos} the box!', svg, 12))
        else:
            s1, s2 = random.choice(['circle', 'square']), random.choice(['triangle', 'rectangle'])
            svg_c = get_2d_shape(s1, 100, 60, 60) + get_2d_shape(s2, 240, 60, 60)
            svg = create_svg_wrapper(svg_c)
            c1 = 0 if s1 == 'circle' else 4
            c2 = 3 if s2 == 'triangle' else 4
            question = 'Which has more corners?'
            correct = s1.title() if c1 > c2 else s2.title()
            options = [s1.title(), s2.title(), 'Same', 'Cannot tell']
            questions.append(make_question(question, options, correct, f'{correct} has more corners!', svg, 12))
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
