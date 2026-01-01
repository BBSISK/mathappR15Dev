"""
AgentMath L1LP Question Generator
Topic: Pattern and Sequence
Learning Outcomes: 2.8 - 2.12
Version: 2.0 - Updated for actual database schema

Generates 600 questions (50 per level × 12 levels) for the L1LP strand.
"""

import sqlite3
import random
import json
import math
from datetime import datetime

# Configuration
TOPIC = 'pattern_and_sequence'
MODE = 'l1lp'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

DIFFICULTY_BANDS = {
    1: 'Foundation', 2: 'Foundation', 3: 'Foundation', 4: 'Foundation',
    5: 'Developing', 6: 'Developing', 7: 'Developing', 8: 'Developing',
    9: 'Progressing', 10: 'Progressing', 11: 'Consolidating', 12: 'Consolidating'
}

COLOURS = {
    'red': '#E74C3C', 'blue': '#3498DB', 'green': '#27AE60',
    'yellow': '#F1C40F', 'orange': '#E67E22', 'purple': '#9B59B6'
}
COLOUR_NAMES = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

def svg_circle(x, y, size=40, colour='#3498DB'):
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2 - 2}" fill="{colour}"/>'

def svg_square(x, y, size=40, colour='#E74C3C'):
    return f'<rect x="{x + 2}" y="{y + 2}" width="{size - 4}" height="{size - 4}" fill="{colour}"/>'

def svg_triangle(x, y, size=40, colour='#27AE60'):
    return f'<polygon points="{x + size//2},{y + 2} {x + 2},{y + size - 2} {x + size - 2},{y + size - 2}" fill="{colour}"/>'

def svg_star(x, y, size=40, colour='#F1C40F'):
    cx, cy = x + size//2, y + size//2
    points = []
    for i in range(5):
        angle_outer = (i * 72 - 90) * math.pi / 180
        angle_inner = ((i * 72) + 36 - 90) * math.pi / 180
        r_outer, r_inner = size//2 - 2, size//4
        points.append(f"{cx + r_outer * math.cos(angle_outer)},{cy + r_outer * math.sin(angle_outer)}")
        points.append(f"{cx + r_inner * math.cos(angle_inner)},{cy + r_inner * math.sin(angle_inner)}")
    return f'<polygon points="{" ".join(points)}" fill="{colour}"/>'

def get_shape_svg(shape, x, y, size=40, colour=None):
    default_colours = {'circle': '#3498DB', 'square': '#E74C3C', 'triangle': '#27AE60', 'star': '#F1C40F'}
    c = colour or default_colours.get(shape, '#3498DB')
    funcs = {'circle': svg_circle, 'square': svg_square, 'triangle': svg_triangle, 'star': svg_star}
    return funcs.get(shape, svg_circle)(x, y, size, c)

def svg_coloured_circle(x, y, size=40, colour='#3498DB'):
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2 - 2}" fill="{colour}" stroke="#333" stroke-width="1"/>'

def svg_question_mark(x, y, size=40):
    return f'<g><rect x="{x}" y="{y}" width="{size}" height="{size}" fill="#f0f0f0" stroke="#ccc" stroke-width="2" stroke-dasharray="5,5" rx="5"/><text x="{x + size//2}" y="{y + size//2 + 8}" text-anchor="middle" font-size="{size//2}" fill="#999">?</text></g>'

def create_svg_wrapper(content, width=400, height=150):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def create_pattern_svg(pattern, item_size=40, show_question=True):
    spacing = item_size + 10
    total_items = len(pattern) + (1 if show_question else 0)
    width = max(400, total_items * spacing + 40)
    svg_content = ''
    start_x = (width - total_items * spacing) // 2
    y = 55
    for i, item in enumerate(pattern):
        x = start_x + i * spacing
        if item in COLOURS:
            svg_content += svg_coloured_circle(x, y, item_size, COLOURS[item])
        elif item in ['circle', 'square', 'triangle', 'star']:
            svg_content += get_shape_svg(item, x, y, item_size)
        else:
            svg_content += svg_coloured_circle(x, y, item_size, COLOURS.get(item, '#3498DB'))
    if show_question:
        x = start_x + len(pattern) * spacing
        svg_content += svg_question_mark(x, y, item_size)
    return create_svg_wrapper(svg_content, width, 150)

# Track question numbers for uniqueness
_question_counter = {}

def make_question(question_text, options, correct_answer, explanation, svg, level):
    global _question_counter
    key = (level, question_text)
    if key not in _question_counter:
        _question_counter[key] = 0
    _question_counter[key] += 1
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
    return {
        'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
        'option_c': options[2], 'option_d': options[3], 'correct_answer': correct_index,
        'explanation': explanation, 'image_svg': svg, 'difficulty_band': DIFFICULTY_BANDS[level],
        'question_type': 'visual' if svg else 'text'
    }

def generate_level_1_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        colours = random.sample(COLOUR_NAMES, 2)
        pattern = [colours[0], colours[1], colours[0], colours[1], colours[0]]
        next_colour = colours[1]
        svg = create_pattern_svg(pattern, item_size=45)
        options = [colours[1].title(), colours[0].title(), "", ""]
        random.shuffle(options[:2])
        questions.append(make_question('What colour comes next?', options, next_colour.title(),
            f'The pattern is {colours[0]}, {colours[1]} repeating. {next_colour.title()} comes next!', svg, 1))
    return questions

def generate_level_2_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            colours = random.sample(COLOUR_NAMES, 2)
            pattern = [colours[j % 2] for j in range(6)]
            svg = create_pattern_svg(pattern, item_size=40, show_question=False)
            questions.append(make_question('Is this a pattern?', ['Yes', 'No', '', ''], 'Yes',
                'Yes! The colours repeat in order - that\'s a pattern!', svg, 2))
        else:
            colours = random.sample(COLOUR_NAMES, 6)
            svg = create_pattern_svg(colours, item_size=40, show_question=False)
            questions.append(make_question('Is this a pattern?', ['Yes', 'No', '', ''], 'No',
                'No, the colours don\'t repeat in order - it\'s not a pattern.', svg, 2))
    return questions

def generate_level_3_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        colours = random.sample(COLOUR_NAMES, 3)
        pattern = [colours[j % 2] for j in range(5)]
        next_colour = colours[1]
        svg = create_pattern_svg(pattern, item_size=45)
        options = [next_colour.title(), colours[0].title(), colours[2].title(), '']
        random.shuffle(options[:3])
        questions.append(make_question(f'What comes next?', options, next_colour.title(),
            f'The pattern is {colours[0].title()}, {colours[1].title()} repeating. {next_colour.title()} is next!', svg, 3))
    return questions

def generate_level_4_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        colours = random.sample(COLOUR_NAMES, 3)
        pattern = [colours[0], colours[1], colours[1], colours[0], colours[1], colours[1], colours[0]]
        next_colour = colours[1]
        svg = create_pattern_svg(pattern, item_size=40)
        options = [colours[1].title(), colours[0].title(), colours[2].title(), '']
        random.shuffle(options[:3])
        questions.append(make_question('What comes next in this pattern?', options, next_colour.title(),
            f'ABB pattern: After {colours[0].title()} comes {colours[1].title()}!', svg, 4))
    return questions

def generate_level_5_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        colours = random.sample(COLOUR_NAMES, 4)
        pattern = [colours[j % 3] for j in range(7)]
        next_colour = colours[1]
        svg = create_pattern_svg(pattern, item_size=35)
        options = [c.title() for c in colours]
        random.shuffle(options)
        questions.append(make_question('What comes next in this ABC pattern?', options, next_colour.title(),
            f'ABC pattern repeating. Next is {next_colour.title()}!', svg, 5))
    return questions

def generate_level_6_questions():
    questions = []
    pattern_types = ['ab', 'abb', 'abc']
    for i in range(QUESTIONS_PER_LEVEL):
        p_type = random.choice(pattern_types)
        colours = random.sample(COLOUR_NAMES, 4)
        if p_type == 'ab':
            pattern = [colours[j % 2] for j in range(5)]
            next_colour = colours[1]
        elif p_type == 'abb':
            pattern = []
            for j in range(7):
                pattern.append(colours[0] if j % 3 == 0 else colours[1])
            next_colour = colours[1]
        else:
            pattern = [colours[j % 3] for j in range(7)]
            next_colour = colours[1]
        svg = create_pattern_svg(pattern, item_size=35)
        options = list(set([next_colour.title()] + [c.title() for c in colours[:3]]))[:4]
        random.shuffle(options)
        questions.append(make_question('What comes next?', options, next_colour.title(),
            f'Following the pattern, {next_colour.title()} comes next!', svg, 6))
    return questions

def generate_level_7_questions():
    questions = []
    sequences = [
        (['wake up', 'eat breakfast', 'go to school', 'come home'], 'What do you do first in the morning?', 'Wake up'),
        (['put on socks', 'put on shoes', 'tie laces', 'walk outside'], 'What comes before putting on shoes?', 'Put on socks'),
        (['get ingredients', 'mix together', 'bake in oven', 'eat cake'], 'What do you do first when baking?', 'Get ingredients'),
        (['seed', 'small plant', 'big plant', 'flower'], 'What comes first when a flower grows?', 'Seed'),
    ]
    for i in range(QUESTIONS_PER_LEVEL):
        items, question, correct = sequences[i % len(sequences)]
        svg_content = ''.join([f'<text x="{50 + j*90}" y="80" text-anchor="middle" font-size="11" fill="#333">{j+1}. {item.title()}</text>' for j, item in enumerate(items)])
        svg = create_svg_wrapper(svg_content)
        options = [item.title() for item in items]
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 7))
    return questions

def generate_level_8_questions():
    questions = []
    routines = [
        ('morning', ['wake up', 'brush teeth', 'eat breakfast', 'go to school'], 'What comes second?', 'Brush teeth'),
        ('evening', ['eat dinner', 'watch TV', 'brush teeth', 'go to bed'], 'What comes last?', 'Go to bed'),
        ('getting dressed', ['underwear', 'shirt', 'jumper', 'coat'], 'What do you put on first?', 'Underwear'),
    ]
    for i in range(QUESTIONS_PER_LEVEL):
        time, activities, question, correct = routines[i % len(routines)]
        svg_content = f'<text x="200" y="40" text-anchor="middle" font-size="14" font-weight="bold">{time.title()} Routine</text>'
        for j, act in enumerate(activities):
            svg_content += f'<text x="{60 + j*95}" y="90" text-anchor="middle" font-size="11">{act.title()}</text>'
        svg = create_svg_wrapper(svg_content)
        options = [act.title() for act in activities]
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is the answer!', svg, 8))
    return questions

def generate_level_9_questions():
    questions = []
    shapes = ['circle', 'square', 'triangle', 'star']
    for i in range(QUESTIONS_PER_LEVEL):
        pattern_shapes = random.sample(shapes, 2)
        pattern = [pattern_shapes[j % 2] for j in range(5)]
        next_shape = pattern_shapes[1]
        svg_content = ''.join([get_shape_svg(shape, 30 + j*60, 55, 40) for j, shape in enumerate(pattern)])
        svg_content += svg_question_mark(330, 55, 40)
        svg = create_svg_wrapper(svg_content)
        options = [s.title() for s in shapes]
        random.shuffle(options)
        questions.append(make_question('What shape is next?', options, next_shape.title(),
            f'The pattern shows {next_shape} comes next!', svg, 9))
    return questions

def generate_level_10_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        objects = random.sample(['apple', 'ball', 'cup', 'book', 'star'], 4)
        position = random.choice(['first', 'second', 'third', 'last'])
        pos_map = {'first': 0, 'second': 1, 'third': 2, 'last': 3}
        correct_obj = objects[pos_map[position]]
        svg_content = ''
        for j, obj in enumerate(objects):
            svg_content += f'<circle cx="{72 + j*90}" cy="75" r="20" fill="{list(COLOURS.values())[j]}"/>'
            svg_content += f'<text x="{72 + j*90}" y="120" text-anchor="middle" font-size="10">{obj.title()}</text>'
        svg = create_svg_wrapper(svg_content)
        options = [obj.title() for obj in objects]
        random.shuffle(options)
        questions.append(make_question(f'Which object is {position}?', options, correct_obj.title(),
            f'The {correct_obj} is {position}!', svg, 10))
    return questions

def generate_level_11_questions():
    questions = []
    activities = [
        ('Making Tea', ['Boil water', 'Put teabag in cup', 'Pour water', 'Add milk'], 'What comes after putting in the teabag?', 'Pour water'),
        ('Brushing Teeth', ['Get toothbrush', 'Put on toothpaste', 'Brush teeth', 'Rinse mouth'], 'What do you do before brushing?', 'Put on toothpaste'),
        ('Planting a Seed', ['Dig hole', 'Put in seed', 'Cover with soil', 'Water it'], 'What comes after covering with soil?', 'Water it'),
    ]
    for i in range(QUESTIONS_PER_LEVEL):
        name, steps, question, correct = activities[i % len(activities)]
        svg_content = f'<text x="200" y="35" text-anchor="middle" font-size="14" font-weight="bold">{name}</text>'
        for j, step in enumerate(steps):
            svg_content += f'<rect x="{30 + j*95}" y="55" width="80" height="40" fill="#e8f4f8" stroke="#3498DB" rx="5"/>'
            svg_content += f'<text x="{70 + j*95}" y="78" text-anchor="middle" font-size="10">{step}</text>'
        svg = create_svg_wrapper(svg_content)
        options = steps.copy()
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is the answer!', svg, 11))
    return questions

def generate_level_12_questions():
    questions = []
    challenge_types = ['colour_pattern', 'shape_pattern', 'sequence', 'routine', 'position']
    for i in range(QUESTIONS_PER_LEVEL):
        c_type = challenge_types[i % len(challenge_types)]
        if c_type == 'colour_pattern':
            colours = random.sample(COLOUR_NAMES, 4)
            pattern = [colours[j % 2] for j in range(6)]
            next_c = colours[0]
            svg = create_pattern_svg(pattern, item_size=35)
            options = [c.title() for c in colours]
            random.shuffle(options)
            questions.append(make_question('What colour comes next?', options, next_c.title(), f'{next_c.title()} comes next!', svg, 12))
        elif c_type == 'shape_pattern':
            shapes = random.sample(['circle', 'square', 'triangle', 'star'], 3)
            pattern = [shapes[j % 2] for j in range(5)]
            next_s = shapes[1]
            svg_content = ''.join([get_shape_svg(shape, 40 + j*55, 55, 40) for j, shape in enumerate(pattern)])
            svg_content += svg_question_mark(315, 55, 40)
            svg = create_svg_wrapper(svg_content)
            options = [s.title() for s in ['circle', 'square', 'triangle', 'star']]
            random.shuffle(options)
            questions.append(make_question('What shape comes next?', options, next_s.title(), f'{next_s.title()} comes next!', svg, 12))
        elif c_type == 'sequence':
            seqs = [(['tiny', 'small', 'medium', 'large'], 'What comes after medium?', 'Large'),
                    (['morning', 'afternoon', 'evening', 'night'], 'What comes after evening?', 'Night')]
            seq, question, correct = random.choice(seqs)
            svg_content = ''.join([f'<text x="{60 + j*90}" y="80" text-anchor="middle" font-size="12">{item.title()}</text>' for j, item in enumerate(seq)])
            svg = create_svg_wrapper(svg_content)
            options = [s.title() for s in seq]
            random.shuffle(options)
            questions.append(make_question(question, options, correct, f'{correct} comes next!', svg, 12))
        elif c_type == 'routine':
            steps, question, correct = ['wake', 'dress', 'eat', 'leave'], 'Morning routine - what comes second?', 'Dress'
            svg_content = ''.join([f'<text x="{60 + j*90}" y="80" text-anchor="middle" font-size="12">{step.title()}</text>' for j, step in enumerate(steps)])
            svg = create_svg_wrapper(svg_content)
            options = [s.title() for s in steps]
            random.shuffle(options)
            questions.append(make_question(question, options, correct, f'{correct} is the answer!', svg, 12))
        else:
            items = random.sample(['🍎', '⭐', '💙', '🟢'], 4)
            position = random.choice(['first', 'second', 'third', 'last'])
            pos_idx = {'first': 0, 'second': 1, 'third': 2, 'last': 3}[position]
            correct = items[pos_idx]
            svg_content = ''.join([f'<text x="{70 + j*80}" y="85" text-anchor="middle" font-size="30">{item}</text>' for j, item in enumerate(items)])
            svg = create_svg_wrapper(svg_content)
            options = items.copy()
            random.shuffle(options)
            questions.append(make_question(f'Which symbol is {position}?', options, correct, f'{correct} is {position}!', svg, 12))
    return questions

def generate_all_questions():
    global _question_counter
    _question_counter = {}  # Reset counter
    all_questions = []
    generators = [(1, generate_level_1_questions), (2, generate_level_2_questions), (3, generate_level_3_questions),
                  (4, generate_level_4_questions), (5, generate_level_5_questions), (6, generate_level_6_questions),
                  (7, generate_level_7_questions), (8, generate_level_8_questions), (9, generate_level_9_questions),
                  (10, generate_level_10_questions), (11, generate_level_11_questions), (12, generate_level_12_questions)]
    for level, generator in generators:
        print(f"  Generating Level {level}...")
        questions = generator()
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['mode'] = MODE
        all_questions.extend(questions)
        print(f"    ✓ {len(questions)} questions generated")
    return all_questions

def validate_questions(questions):
    print(f"\nValidating {len(questions)} questions...")
    errors = []
    for i, q in enumerate(questions):
        for field in ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'level', 'topic', 'mode', 'difficulty_band']:
            if field not in q:
                errors.append(f"Question {i}: Missing {field}")
        if 'correct_answer' in q and (not isinstance(q['correct_answer'], int) or q['correct_answer'] < 0 or q['correct_answer'] > 3):
            errors.append(f"Question {i}: correct_answer must be 0-3")
    if errors:
        print(f"  ✗ Found {len(errors)} errors:")
        for e in errors[:10]:
            print(f"    - {e}")
        return False
    print(f"  ✓ All questions valid")
    return True

def insert_questions(questions):
    print(f"\nInserting {len(questions)} questions into database...")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?', (TOPIC, MODE))
    print(f"  Removed {cursor.rowcount} existing questions")
    inserted = 0
    for q in questions:
        try:
            cursor.execute('''INSERT INTO questions_adaptive (topic, mode, difficulty_level, difficulty_band, question_text, 
                option_a, option_b, option_c, option_d, correct_answer, explanation, image_svg, question_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (q['topic'], q['mode'], q['level'], q['difficulty_band'], q['question_text'],
                 q['option_a'], q['option_b'], q['option_c'], q['option_d'], q['correct_answer'],
                 q.get('explanation', ''), q.get('image_svg', ''), q.get('question_type', 'visual')))
            inserted += 1
        except Exception as e:
            print(f"  Error inserting question: {e}")
    conn.commit()
    conn.close()
    print(f"  ✓ Inserted {inserted} questions")
    return inserted

def verify_insertion():
    print(f"\nVerifying insertion...")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? AND mode = ? GROUP BY difficulty_level ORDER BY difficulty_level', (TOPIC, MODE))
    results = cursor.fetchall()
    conn.close()
    print(f"\n  Questions per level:")
    total = 0
    for level, count in results:
        status = "✓" if count == QUESTIONS_PER_LEVEL else "✗"
        print(f"    Level {level}: {count} {status}")
        total += count
    expected = QUESTIONS_PER_LEVEL * TOTAL_LEVELS
    print(f"\n  Total: {total} questions")
    if total == expected:
        print(f"  ✓ Perfect! Expected {expected}, got {total}")
    else:
        print(f"  ✗ Mismatch! Expected {expected}, got {total}")
    return total == expected

if __name__ == '__main__':
    print("=" * 60)
    print(f"AgentMath L1LP Question Generator - {TOPIC}")
    print("=" * 60)
    questions = generate_all_questions()
    if not validate_questions(questions):
        print("\n✗ Validation failed. Aborting.")
        exit(1)
    insert_questions(questions)
    success = verify_insertion()
    print("\n" + "=" * 60)
    print("✓ COMPLETE!" if success else "✗ INCOMPLETE.")
    print("=" * 60)
