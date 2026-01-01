"""
AgentMath L1LP Question Generator
Topic: Awareness of Environment
Learning Outcomes: 2.1 - 2.7
Version: 2.0 - Updated for actual database schema

Generates 600 questions (50 per level × 12 levels) for the L1LP strand.
Focus: Exploring objects, same/different, matching, sorting, cause/effect, object permanence.

Level Structure:
- Levels 1-4 (Foundation): 90% visual, 2-3 options
- Levels 5-8 (Developing): 80% visual, 3-4 options  
- Levels 9-12 (Progressing/Consolidating): 70% visual, 4 options
"""

import sqlite3
import random
import json
import math
from datetime import datetime

# Configuration
TOPIC = 'awareness_of_environment'
MODE = 'l1lp'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

# Difficulty bands by level
DIFFICULTY_BANDS = {
    1: 'Foundation', 2: 'Foundation', 3: 'Foundation', 4: 'Foundation',
    5: 'Developing', 6: 'Developing', 7: 'Developing', 8: 'Developing',
    9: 'Progressing', 10: 'Progressing', 11: 'Consolidating', 12: 'Consolidating'
}

# Accessible colour palette
COLOURS = {
    'red': '#E74C3C',
    'blue': '#3498DB',
    'green': '#27AE60',
    'yellow': '#F1C40F',
    'orange': '#E67E22',
    'purple': '#9B59B6',
    'pink': '#FF69B4',
    'brown': '#8B4513'
}

COLOUR_NAMES = list(COLOURS.keys())

# Common objects for L1LP
OBJECTS = {
    'apple': {'colour': 'red', 'category': 'food'},
    'banana': {'colour': 'yellow', 'category': 'food'},
    'orange': {'colour': 'orange', 'category': 'food'},
    'ball': {'colour': 'red', 'category': 'toy'},
    'teddy': {'colour': 'brown', 'category': 'toy'},
    'car': {'colour': 'blue', 'category': 'toy'},
    'cup': {'colour': 'blue', 'category': 'kitchen'},
    'spoon': {'colour': 'grey', 'category': 'kitchen'},
    'plate': {'colour': 'white', 'category': 'kitchen'},
    'book': {'colour': 'red', 'category': 'school'},
    'pencil': {'colour': 'yellow', 'category': 'school'},
    'chair': {'colour': 'brown', 'category': 'furniture'},
    'table': {'colour': 'brown', 'category': 'furniture'},
    'sock': {'colour': 'blue', 'category': 'clothing'},
    'shoe': {'colour': 'brown', 'category': 'clothing'},
    'hat': {'colour': 'red', 'category': 'clothing'}
}

OBJECT_NAMES = list(OBJECTS.keys())

# =============================================================================
# SVG GENERATION FUNCTIONS
# =============================================================================

def svg_apple(x, y, size=60, colour='#E74C3C'):
    """Generate an apple SVG"""
    return f'''<g transform="translate({x},{y})">
        <ellipse cx="{size//2}" cy="{size//2 + 5}" rx="{size//2}" ry="{size//2 + 5}" fill="{colour}"/>
        <rect x="{size//2 - 3}" y="0" width="6" height="12" fill="#8B4513"/>
        <ellipse cx="{size//2 + 8}" cy="8" rx="8" ry="5" fill="#27AE60"/>
    </g>'''

def svg_banana(x, y, size=60, colour='#F1C40F'):
    """Generate a banana SVG"""
    return f'''<g transform="translate({x},{y})">
        <path d="M10,{size-10} Q{size//2},{size//4} {size-10},10" stroke="{colour}" stroke-width="18" fill="none" stroke-linecap="round"/>
    </g>'''

def svg_orange(x, y, size=60, colour='#E67E22'):
    """Generate an orange SVG"""
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//2}" cy="{size//2}" r="{size//2 - 5}" fill="{colour}"/>
        <ellipse cx="{size//2}" cy="8" rx="6" ry="4" fill="#27AE60"/>
    </g>'''

def svg_ball(x, y, size=60, colour='#E74C3C'):
    """Generate a ball SVG"""
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//2}" cy="{size//2}" r="{size//2 - 5}" fill="{colour}"/>
        <path d="M{size//4},{size//3} Q{size//2},{size//4} {size*3//4},{size//3}" stroke="white" stroke-width="3" fill="none"/>
    </g>'''

def svg_teddy(x, y, size=60, colour='#8B4513'):
    """Generate a teddy bear SVG"""
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//4}" cy="{size//4}" r="{size//6}" fill="{colour}"/>
        <circle cx="{size*3//4}" cy="{size//4}" r="{size//6}" fill="{colour}"/>
        <circle cx="{size//2}" cy="{size//2 + 5}" r="{size//3}" fill="{colour}"/>
        <circle cx="{size//3}" cy="{size//2}" r="4" fill="black"/>
        <circle cx="{size*2//3}" cy="{size//2}" r="4" fill="black"/>
        <ellipse cx="{size//2}" cy="{size//2 + 10}" rx="6" ry="4" fill="#5D3A1A"/>
    </g>'''

def svg_car(x, y, size=60, colour='#3498DB'):
    """Generate a car SVG"""
    return f'''<g transform="translate({x},{y})">
        <rect x="5" y="{size//3}" width="{size-10}" height="{size//3}" rx="5" fill="{colour}"/>
        <rect x="{size//4}" y="{size//6}" width="{size//2}" height="{size//4}" rx="3" fill="{colour}"/>
        <circle cx="{size//4}" cy="{size*2//3}" r="{size//8}" fill="#2C3E50"/>
        <circle cx="{size*3//4}" cy="{size*2//3}" r="{size//8}" fill="#2C3E50"/>
    </g>'''

def svg_cup(x, y, size=60, colour='#3498DB'):
    """Generate a cup SVG"""
    return f'''<g transform="translate({x},{y})">
        <path d="M{size//6},{size//6} L{size//4},{size-10} L{size*3//4},{size-10} L{size*5//6},{size//6} Z" fill="{colour}"/>
        <ellipse cx="{size//2}" cy="{size//6}" rx="{size//3}" ry="{size//10}" fill="{colour}"/>
        <path d="M{size*5//6},{size//3} Q{size+5},{size//2} {size*5//6},{size*2//3}" stroke="{colour}" stroke-width="5" fill="none"/>
    </g>'''

def svg_book(x, y, size=60, colour='#E74C3C'):
    """Generate a book SVG"""
    return f'''<g transform="translate({x},{y})">
        <rect x="5" y="5" width="{size-10}" height="{size-10}" rx="3" fill="{colour}"/>
        <rect x="10" y="10" width="{size-25}" height="{size-20}" fill="white"/>
        <line x1="15" y1="{size//3}" x2="{size-20}" y2="{size//3}" stroke="#ccc" stroke-width="2"/>
        <line x1="15" y1="{size//2}" x2="{size-20}" y2="{size//2}" stroke="#ccc" stroke-width="2"/>
    </g>'''

def svg_pencil(x, y, size=60, colour='#F1C40F'):
    """Generate a pencil SVG"""
    return f'''<g transform="translate({x},{y})">
        <rect x="{size//4}" y="5" width="{size//2}" height="{size-20}" fill="{colour}"/>
        <polygon points="{size//4},5 {size*3//4},5 {size//2},-10" fill="#F5CBA7"/>
        <rect x="{size//4}" y="{size-20}" width="{size//2}" height="10" fill="#FF69B4"/>
    </g>'''

def svg_sock(x, y, size=60, colour='#3498DB'):
    """Generate a sock SVG"""
    return f'''<g transform="translate({x},{y})">
        <path d="M{size//4},5 L{size//4},{size//2} Q{size//4},{size*3//4} {size//2},{size*3//4} L{size-10},{size*3//4} Q{size},{size*3//4} {size},{size//2} L{size*3//4},{size//2} L{size*3//4},5 Z" fill="{colour}"/>
        <rect x="{size//4}" y="5" width="{size//2}" height="10" fill="white"/>
    </g>'''

def svg_hat(x, y, size=60, colour='#E74C3C'):
    """Generate a hat SVG"""
    return f'''<g transform="translate({x},{y})">
        <ellipse cx="{size//2}" cy="{size*2//3}" rx="{size//2 - 5}" ry="{size//6}" fill="{colour}"/>
        <rect x="{size//4}" y="{size//4}" width="{size//2}" height="{size//2 - 5}" rx="5" fill="{colour}"/>
    </g>'''

def svg_star(x, y, size=60, colour='#F1C40F'):
    """Generate a star SVG"""
    cx, cy = size//2, size//2
    points = []
    for i in range(5):
        angle_outer = (i * 72 - 90) * math.pi / 180
        angle_inner = ((i * 72) + 36 - 90) * math.pi / 180
        r_outer = size//2 - 5
        r_inner = size//4
        points.append(f"{cx + r_outer * math.cos(angle_outer)},{cy + r_outer * math.sin(angle_outer)}")
        points.append(f"{cx + r_inner * math.cos(angle_inner)},{cy + r_inner * math.sin(angle_inner)}")
    return f'''<g transform="translate({x},{y})">
        <polygon points="{' '.join(points)}" fill="{colour}"/>
    </g>'''

def svg_circle_shape(x, y, size=60, colour='#3498DB'):
    """Generate a circle shape SVG"""
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//2}" cy="{size//2}" r="{size//2 - 5}" fill="{colour}"/>
    </g>'''

def svg_square_shape(x, y, size=60, colour='#E74C3C'):
    """Generate a square shape SVG"""
    return f'''<g transform="translate({x},{y})">
        <rect x="5" y="5" width="{size-10}" height="{size-10}" fill="{colour}"/>
    </g>'''

def svg_triangle_shape(x, y, size=60, colour='#27AE60'):
    """Generate a triangle shape SVG"""
    return f'''<g transform="translate({x},{y})">
        <polygon points="{size//2},5 5,{size-5} {size-5},{size-5}" fill="{colour}"/>
    </g>'''

def get_object_svg(obj_name, x, y, size=60, colour=None):
    """Get SVG for a named object"""
    obj_colours = {
        'apple': '#E74C3C',
        'banana': '#F1C40F', 
        'orange': '#E67E22',
        'ball': '#E74C3C',
        'teddy': '#8B4513',
        'car': '#3498DB',
        'cup': '#3498DB',
        'book': '#E74C3C',
        'pencil': '#F1C40F',
        'sock': '#3498DB',
        'hat': '#E74C3C',
        'star': '#F1C40F',
        'circle': '#3498DB',
        'square': '#E74C3C',
        'triangle': '#27AE60'
    }
    
    c = colour or obj_colours.get(obj_name, '#3498DB')
    
    svg_funcs = {
        'apple': svg_apple,
        'banana': svg_banana,
        'orange': svg_orange,
        'ball': svg_ball,
        'teddy': svg_teddy,
        'car': svg_car,
        'cup': svg_cup,
        'book': svg_book,
        'pencil': svg_pencil,
        'sock': svg_sock,
        'hat': svg_hat,
        'star': svg_star,
        'circle': svg_circle_shape,
        'square': svg_square_shape,
        'triangle': svg_triangle_shape
    }
    
    if obj_name in svg_funcs:
        return svg_funcs[obj_name](x, y, size, c)
    return svg_circle_shape(x, y, size, c)

def create_svg_wrapper(content, width=400, height=200):
    """Wrap SVG content in full SVG element"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

# =============================================================================
# HELPER FUNCTION FOR QUESTION FORMAT
# =============================================================================

# Track question numbers for uniqueness
_question_counter = {}

def make_question(question_text, options, correct_answer, explanation, svg, level):
    """Create a question dict matching the database schema"""
    global _question_counter
    # Make question_text unique by adding counter
    key = (level, question_text)
    if key not in _question_counter:
        _question_counter[key] = 0
    _question_counter[key] += 1
    if _question_counter[key] > 1:
        question_text = f"{question_text} (#{_question_counter[key]})"
    
    # Ensure we have exactly 4 options
    while len(options) < 4:
        options.append("")
    options = options[:4]
    
    # Find correct answer index
    try:
        correct_index = options.index(correct_answer)
    except ValueError:
        # If correct answer not in options, add it
        options[0] = correct_answer
        correct_index = 0
    
    return {
        'question_text': question_text,
        'option_a': options[0],
        'option_b': options[1],
        'option_c': options[2],
        'option_d': options[3],
        'correct_answer': correct_index,
        'explanation': explanation,
        'image_svg': svg,
        'difficulty_band': DIFFICULTY_BANDS[level],
        'question_type': 'visual' if svg else 'text'
    }

# =============================================================================
# QUESTION GENERATORS BY LEVEL
# =============================================================================

def generate_level_1_questions():
    """Level 1: Exploring Objects - Identify single objects (2 options)"""
    questions = []
    objects_to_use = ['apple', 'ball', 'cup', 'book', 'teddy', 'car', 'banana', 'sock']
    
    for i in range(QUESTIONS_PER_LEVEL):
        obj = random.choice(objects_to_use)
        wrong = random.choice([o for o in objects_to_use if o != obj])
        
        svg_content = get_object_svg(obj, 170, 70, 60)
        svg = create_svg_wrapper(svg_content)
        
        options = [obj.title(), wrong.title(), "", ""]
        random.shuffle(options[:2])
        
        questions.append(make_question(
            'What is this?',
            options,
            obj.title(),
            f'This is a {obj}!',
            svg,
            1
        ))
    
    return questions

def generate_level_2_questions():
    """Level 2: Objects in Motion - Which can roll/slide (2 options)"""
    questions = []
    
    rolling_objects = ['ball', 'orange', 'apple']
    non_rolling = ['book', 'cup', 'pencil', 'sock']
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            obj = random.choice(rolling_objects)
            wrong = random.choice(non_rolling)
            question = 'Which one can roll?'
            correct = obj
        else:
            obj = random.choice(non_rolling)
            wrong = random.choice(rolling_objects)
            question = 'Which one cannot roll?'
            correct = obj
        
        svg_content = get_object_svg(obj, 80, 70, 60)
        svg_content += get_object_svg(wrong, 260, 70, 60)
        svg = create_svg_wrapper(svg_content)
        
        options = [obj.title(), wrong.title(), "", ""]
        random.shuffle(options[:2])
        
        questions.append(make_question(
            question,
            options,
            correct.title(),
            f'{correct.title()} {"can" if correct in rolling_objects else "cannot"} roll because it is {"round" if correct in rolling_objects else "not round"}!',
            svg,
            2
        ))
    
    return questions

def generate_level_3_questions():
    """Level 3: Showing Preferences - Pick your favourite (3 options)"""
    questions = []
    
    categories = {
        'food': ['apple', 'banana', 'orange'],
        'toy': ['ball', 'teddy', 'car'],
        'colour': ['red', 'blue', 'green']
    }
    
    for i in range(QUESTIONS_PER_LEVEL):
        cat = random.choice(list(categories.keys()))
        items = categories[cat]
        
        if cat == 'colour':
            svg_content = ''
            for j, colour in enumerate(items):
                svg_content += svg_circle_shape(50 + j*120, 70, 60, COLOURS[colour])
            svg = create_svg_wrapper(svg_content)
            
            options = [c.title() for c in items] + [""]
            correct = random.choice(items).title()
            question = 'Which colour do you like best?'
            explanation = f'You picked {correct}! All choices are good - it\'s YOUR favourite!'
        else:
            svg_content = ''
            for j, item in enumerate(items):
                svg_content += get_object_svg(item, 50 + j*120, 70, 60)
            svg = create_svg_wrapper(svg_content)
            
            options = [item.title() for item in items] + [""]
            correct = random.choice(items).title()
            question = f'Which {cat} would you pick?'
            explanation = f'You picked {correct}! All choices are good - it\'s YOUR favourite!'
        
        questions.append(make_question(question, options, correct, explanation, svg, 3))
    
    return questions

def generate_level_4_questions():
    """Level 4: Same or Different - Compare two objects (3 options)"""
    questions = []
    
    simple_objects = ['apple', 'ball', 'cup', 'book', 'star', 'teddy']
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            obj = random.choice(simple_objects)
            obj1, obj2 = obj, obj
            correct = 'Same'
            explanation = f'They are the same! Both are {obj}s.'
        else:
            obj1 = random.choice(simple_objects)
            obj2 = random.choice([o for o in simple_objects if o != obj1])
            correct = 'Different'
            explanation = f'They are different! One is a {obj1} and one is a {obj2}.'
        
        svg_content = get_object_svg(obj1, 100, 70, 60)
        svg_content += get_object_svg(obj2, 240, 70, 60)
        svg = create_svg_wrapper(svg_content)
        
        options = ['Same', 'Different', 'Not sure', '']
        
        questions.append(make_question(
            'Are these the same or different?',
            options,
            correct,
            explanation,
            svg,
            4
        ))
    
    return questions

def generate_level_5_questions():
    """Level 5: Matching Objects - Find the matching pair (3-4 options)"""
    questions = []
    
    objects = ['apple', 'ball', 'cup', 'book', 'teddy', 'car', 'sock', 'hat']
    
    for i in range(QUESTIONS_PER_LEVEL):
        target = random.choice(objects)
        distractors = random.sample([o for o in objects if o != target], 2)
        
        svg_content = get_object_svg(target, 50, 70, 60)
        svg_content += f'<text x="130" y="100" font-size="24" fill="#333">→</text>'
        
        all_options = [target] + distractors
        random.shuffle(all_options)
        
        for j, opt in enumerate(all_options):
            svg_content += get_object_svg(opt, 170 + j*80, 70, 50)
        
        svg = create_svg_wrapper(svg_content)
        
        options = [o.title() for o in all_options] + [""]
        
        questions.append(make_question(
            f'Find the matching {target}!',
            options,
            target.title(),
            f'The {target} matches the {target}! They are the same.',
            svg,
            5
        ))
    
    return questions

def generate_level_6_questions():
    """Level 6: Sorting by One Thing - Sort by colour or type (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            target_colour = random.choice(['red', 'blue', 'green', 'yellow'])
            
            red_obj = random.choice(['apple', 'ball', 'book'])
            blue_obj = random.choice(['cup', 'car', 'sock'])
            green_obj = 'triangle'
            yellow_obj = random.choice(['banana', 'star', 'pencil'])
            
            svg_content = get_object_svg(red_obj, 50, 70, 50, COLOURS['red'])
            svg_content += get_object_svg(blue_obj, 130, 70, 50, COLOURS['blue'])
            svg_content += get_object_svg(green_obj, 210, 70, 50, COLOURS['green'])
            svg_content += get_object_svg(yellow_obj, 290, 70, 50, COLOURS['yellow'])
            svg = create_svg_wrapper(svg_content)
            
            colour_map = {'red': red_obj, 'blue': blue_obj, 'green': green_obj, 'yellow': yellow_obj}
            correct = colour_map[target_colour].title()
            
            options = [red_obj.title(), blue_obj.title(), green_obj.title(), yellow_obj.title()]
            
            questions.append(make_question(
                f'Which one is {target_colour}?',
                options,
                correct,
                f'The {correct.lower()} is {target_colour}!',
                svg,
                6
            ))
        else:
            categories = {
                'food': ['apple', 'banana', 'orange'],
                'toy': ['ball', 'teddy', 'car']
            }
            target_cat = random.choice(list(categories.keys()))
            correct_obj = random.choice(categories[target_cat])
            wrong_cat = 'toy' if target_cat == 'food' else 'food'
            wrong_objs = random.sample(categories[wrong_cat], 3)
            
            all_objs = [correct_obj] + wrong_objs
            random.shuffle(all_objs)
            
            svg_content = ''
            for j, obj in enumerate(all_objs):
                svg_content += get_object_svg(obj, 50 + j*90, 70, 50)
            svg = create_svg_wrapper(svg_content)
            
            options = [o.title() for o in all_objs]
            
            questions.append(make_question(
                f'Which one is {target_cat}?',
                options,
                correct_obj.title(),
                f'{correct_obj.title()} is {target_cat}!',
                svg,
                6
            ))
    
    return questions

def generate_level_7_questions():
    """Level 7: Cause and Effect - What happens when... (4 options)"""
    questions = []
    
    scenarios = [
        {
            'setup': 'You push the ball',
            'question': 'What happens when you push the ball?',
            'correct': 'It rolls',
            'options': ['It rolls', 'It flies', 'It disappears', 'It grows'],
            'explanation': 'When you push a ball, it rolls!'
        },
        {
            'setup': 'You drop a cup',
            'question': 'What happens when you drop a cup?',
            'correct': 'It falls down',
            'options': ['It falls down', 'It floats up', 'It stays still', 'It runs away'],
            'explanation': 'When you drop something, it falls down!'
        },
        {
            'setup': 'You turn on the light',
            'question': 'What happens when you turn on the light?',
            'correct': 'It gets bright',
            'options': ['It gets bright', 'It gets dark', 'Nothing happens', 'It rains'],
            'explanation': 'When you turn on the light, it gets bright!'
        },
        {
            'setup': 'You open an umbrella in the rain',
            'question': 'What happens when you open an umbrella?',
            'correct': 'You stay dry',
            'options': ['You stay dry', 'You get wet', 'It snows', 'You fly'],
            'explanation': 'An umbrella keeps you dry in the rain!'
        },
        {
            'setup': 'You press the button',
            'question': 'What usually happens when you press a button?',
            'correct': 'Something turns on',
            'options': ['Something turns on', 'Nothing at all', 'It breaks', 'It sings'],
            'explanation': 'Pressing buttons usually makes something happen - like turning on!'
        }
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        scenario = scenarios[i % len(scenarios)]
        
        svg_content = f'<text x="200" y="100" text-anchor="middle" font-size="16" fill="#333">{scenario["setup"]}</text>'
        svg = create_svg_wrapper(svg_content)
        
        options = scenario['options'].copy()
        random.shuffle(options)
        
        questions.append(make_question(
            scenario['question'],
            options,
            scenario['correct'],
            scenario['explanation'],
            svg,
            7
        ))
    
    return questions

def generate_level_8_questions():
    """Level 8: What Happens Next - Predict sequences (4 options)"""
    questions = []
    
    sequences = [
        {
            'scene': 'Ball rolling toward pins',
            'question': 'The ball is rolling toward the pins. What happens next?',
            'correct': 'Pins fall down',
            'options': ['Pins fall down', 'Pins fly away', 'Ball stops', 'Pins grow bigger'],
            'explanation': 'When a ball hits pins, they fall down!'
        },
        {
            'scene': 'Ice cream in the sun',
            'question': 'Ice cream is in the hot sun. What happens next?',
            'correct': 'It melts',
            'options': ['It melts', 'It freezes more', 'It gets bigger', 'It sings'],
            'explanation': 'Ice cream melts in the hot sun!'
        },
        {
            'scene': 'Pouring water into a glass',
            'question': 'You keep pouring water into the glass. What happens next?',
            'correct': 'It overflows',
            'options': ['It overflows', 'It disappears', 'Glass gets smaller', 'Water flies up'],
            'explanation': 'If you keep pouring, the glass overflows!'
        },
        {
            'scene': 'Balloon getting bigger',
            'question': 'You keep blowing up the balloon. What might happen?',
            'correct': 'It pops',
            'options': ['It pops', 'It shrinks', 'It turns blue', 'It sings'],
            'explanation': 'If you blow too much, the balloon pops!'
        },
        {
            'scene': 'Candle burning',
            'question': 'The candle keeps burning. What happens to the candle?',
            'correct': 'It gets smaller',
            'options': ['It gets smaller', 'It gets bigger', 'It floats', 'It turns green'],
            'explanation': 'As a candle burns, it gets smaller!'
        }
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        seq = sequences[i % len(sequences)]
        
        svg_content = f'<text x="200" y="90" text-anchor="middle" font-size="14" fill="#333">{seq["scene"]}</text>'
        svg_content += f'<text x="200" y="120" text-anchor="middle" font-size="20" fill="#666">❓</text>'
        svg = create_svg_wrapper(svg_content)
        
        options = seq['options'].copy()
        random.shuffle(options)
        
        questions.append(make_question(
            seq['question'],
            options,
            seq['correct'],
            seq['explanation'],
            svg,
            8
        ))
    
    return questions

def generate_level_9_questions():
    """Level 9: Object Permanence - Is it still there? (4 options)"""
    questions = []
    
    hiding_spots = ['under the blanket', 'behind the box', 'inside the cup', 'under the hat']
    objects = ['ball', 'teddy', 'apple', 'car', 'sock']
    
    for i in range(QUESTIONS_PER_LEVEL):
        obj = random.choice(objects)
        spot = random.choice(hiding_spots)
        
        svg_content = f'<rect x="150" y="60" width="100" height="80" fill="#8B4513" rx="5"/>'
        svg_content += f'<text x="200" y="170" text-anchor="middle" font-size="12" fill="#333">The {obj} is {spot}</text>'
        svg = create_svg_wrapper(svg_content)
        
        options = ['Yes, it\'s still there', 'No, it disappeared', 'It flew away', 'Not sure']
        
        questions.append(make_question(
            f'A {obj} goes {spot}. Is it still there?',
            options,
            'Yes, it\'s still there',
            f'Yes! The {obj} is still there - it\'s just hidden {spot}!',
            svg,
            9
        ))
    
    return questions

def generate_level_10_questions():
    """Level 10: Hidden Objects - Track where things went (4 options)"""
    questions = []
    
    containers = ['red cup', 'blue box', 'green basket', 'yellow hat']
    objects = ['ball', 'teddy', 'apple', 'star']
    
    for i in range(QUESTIONS_PER_LEVEL):
        obj = random.choice(objects)
        correct_container = random.choice(containers)
        wrong_containers = [c for c in containers if c != correct_container][:3]
        
        svg_content = ''
        all_containers = [correct_container] + wrong_containers
        random.shuffle(all_containers)
        
        colours = {'red': '#E74C3C', 'blue': '#3498DB', 'green': '#27AE60', 'yellow': '#F1C40F'}
        for j, cont in enumerate(all_containers):
            colour_name = cont.split()[0]
            svg_content += f'<rect x="{50 + j*90}" y="80" width="60" height="50" fill="{colours[colour_name]}" rx="5"/>'
            svg_content += f'<text x="{80 + j*90}" y="150" text-anchor="middle" font-size="10" fill="#333">{cont.split()[1]}</text>'
        
        svg = create_svg_wrapper(svg_content)
        
        options = all_containers
        
        questions.append(make_question(
            f'The {obj} went into the {correct_container}. Where is it?',
            options,
            correct_container,
            f'The {obj} is in the {correct_container}! That\'s where it went.',
            svg,
            10
        ))
    
    return questions

def generate_level_11_questions():
    """Level 11: Multi-Attribute Sort - Sort by two things (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        sizes = ['big', 'small']
        colours = ['red', 'blue']
        
        target_size = random.choice(sizes)
        target_colour = random.choice(colours)
        
        combos = []
        for s in sizes:
            for c in colours:
                combos.append((s, c))
        
        random.shuffle(combos)
        
        svg_content = ''
        for j, (s, c) in enumerate(combos):
            size_px = 50 if s == 'big' else 30
            y_offset = 80 if s == 'big' else 90
            svg_content += svg_circle_shape(60 + j*90, y_offset, size_px, COLOURS[c])
        
        svg = create_svg_wrapper(svg_content)
        
        options = [f'{s.title()} {c}' for s, c in combos]
        correct = f'{target_size.title()} {target_colour}'
        
        questions.append(make_question(
            f'Find the {target_size} {target_colour} circle!',
            options,
            correct,
            f'The {correct.lower()} circle is the one that is both {target_size} AND {target_colour}!',
            svg,
            11
        ))
    
    return questions

def generate_level_12_questions():
    """Level 12: Environment Challenge - Mixed skills (4 options)"""
    questions = []
    
    challenge_types = ['identify', 'match', 'sort', 'predict', 'find']
    
    for i in range(QUESTIONS_PER_LEVEL):
        c_type = challenge_types[i % len(challenge_types)]
        
        if c_type == 'identify':
            objects = ['apple', 'ball', 'teddy', 'car']
            obj = random.choice(objects)
            svg_content = get_object_svg(obj, 170, 70, 60)
            svg = create_svg_wrapper(svg_content)
            options = [o.title() for o in objects]
            
            questions.append(make_question(
                'What object is this?',
                options,
                obj.title(),
                f'This is a {obj}!',
                svg,
                12
            ))
            
        elif c_type == 'match':
            objects = ['apple', 'ball', 'cup', 'book']
            target = random.choice(objects)
            others = [o for o in objects if o != target]
            
            svg_content = get_object_svg(target, 50, 70, 50)
            svg_content += f'<text x="120" y="100" font-size="20">→</text>'
            
            all_opts = [target] + others
            random.shuffle(all_opts)
            for j, opt in enumerate(all_opts):
                svg_content += get_object_svg(opt, 150 + j*70, 70, 40)
            
            svg = create_svg_wrapper(svg_content)
            options = [o.title() for o in all_opts]
            
            questions.append(make_question(
                f'Which one matches the {target}?',
                options,
                target.title(),
                f'{target.title()} matches {target}!',
                svg,
                12
            ))
            
        elif c_type == 'sort':
            colours = ['red', 'blue', 'green', 'yellow']
            target = random.choice(colours)
            
            svg_content = ''
            for j, c in enumerate(colours):
                svg_content += svg_circle_shape(60 + j*90, 80, 40, COLOURS[c])
            svg = create_svg_wrapper(svg_content)
            
            options = [c.title() for c in colours]
            
            questions.append(make_question(
                f'Which circle is {target}?',
                options,
                target.title(),
                f'The {target} circle is {target}!',
                svg,
                12
            ))
            
        elif c_type == 'predict':
            scenarios = [
                ('You drop a ball', 'It falls', ['It falls', 'It floats', 'It flies', 'It grows']),
                ('You push a car', 'It moves', ['It moves', 'It stops', 'It jumps', 'It shrinks'])
            ]
            scene, correct, opts = random.choice(scenarios)
            
            svg_content = f'<text x="200" y="100" text-anchor="middle" font-size="16">{scene}</text>'
            svg = create_svg_wrapper(svg_content)
            
            random.shuffle(opts)
            
            questions.append(make_question(
                f'{scene}. What happens?',
                opts,
                correct,
                f'When you do that, {correct.lower()}!',
                svg,
                12
            ))
            
        else:  # find
            obj = random.choice(['ball', 'teddy', 'apple'])
            spots = ['Under the box', 'Behind the cup', 'In the basket', 'On the table']
            correct_spot = random.choice(spots)
            
            svg_content = f'<text x="200" y="80" text-anchor="middle" font-size="14">The {obj} is hiding!</text>'
            svg_content += f'<text x="200" y="110" text-anchor="middle" font-size="12" fill="#666">It went {correct_spot.lower()}</text>'
            svg = create_svg_wrapper(svg_content)
            
            questions.append(make_question(
                f'Where is the {obj}?',
                spots,
                correct_spot,
                f'The {obj} is {correct_spot.lower()}!',
                svg,
                12
            ))
    
    return questions

# =============================================================================
# MAIN GENERATION AND DATABASE FUNCTIONS
# =============================================================================

def generate_all_questions():
    """Generate all questions for all levels"""
    global _question_counter
    _question_counter = {}  # Reset counter
    all_questions = []
    
    generators = [
        (1, generate_level_1_questions),
        (2, generate_level_2_questions),
        (3, generate_level_3_questions),
        (4, generate_level_4_questions),
        (5, generate_level_5_questions),
        (6, generate_level_6_questions),
        (7, generate_level_7_questions),
        (8, generate_level_8_questions),
        (9, generate_level_9_questions),
        (10, generate_level_10_questions),
        (11, generate_level_11_questions),
        (12, generate_level_12_questions),
    ]
    
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
    """Validate all questions before insertion"""
    print(f"\nValidating {len(questions)} questions...")
    
    errors = []
    for i, q in enumerate(questions):
        required = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 
                    'correct_answer', 'level', 'topic', 'mode', 'difficulty_band']
        for field in required:
            if field not in q:
                errors.append(f"Question {i}: Missing {field}")
        
        # Check correct_answer is valid index
        if 'correct_answer' in q:
            if not isinstance(q['correct_answer'], int) or q['correct_answer'] < 0 or q['correct_answer'] > 3:
                errors.append(f"Question {i}: correct_answer must be 0-3, got {q['correct_answer']}")
    
    if errors:
        print(f"  ✗ Found {len(errors)} errors:")
        for e in errors[:10]:
            print(f"    - {e}")
        if len(errors) > 10:
            print(f"    ... and {len(errors) - 10} more")
        return False
    
    print(f"  ✓ All questions valid")
    return True

def insert_questions(questions):
    """Insert questions into database"""
    print(f"\nInserting {len(questions)} questions into database...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # First, remove existing questions for this topic/mode
    cursor.execute('''
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
    ''', (TOPIC, MODE))
    deleted = cursor.rowcount
    print(f"  Removed {deleted} existing questions")
    
    # Insert new questions
    inserted = 0
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (topic, mode, difficulty_level, difficulty_band, question_text, 
                 option_a, option_b, option_c, option_d, correct_answer, 
                 explanation, image_svg, question_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'],
                q['mode'],
                q['level'],
                q['difficulty_band'],
                q['question_text'],
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_answer'],
                q.get('explanation', ''),
                q.get('image_svg', ''),
                q.get('question_type', 'visual')
            ))
            inserted += 1
        except Exception as e:
            print(f"  Error inserting question: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"  ✓ Inserted {inserted} questions")
    return inserted

def verify_insertion():
    """Verify questions were inserted correctly"""
    print(f"\nVerifying insertion...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT difficulty_level, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    ''', (TOPIC, MODE))
    
    results = cursor.fetchall()
    conn.close()
    
    print(f"\n  Questions per level:")
    total = 0
    for level, count in results:
        status = "✓" if count == QUESTIONS_PER_LEVEL else "✗"
        print(f"    Level {level}: {count} {status}")
        total += count
    
    print(f"\n  Total: {total} questions")
    expected = QUESTIONS_PER_LEVEL * TOTAL_LEVELS
    if total == expected:
        print(f"  ✓ Perfect! Expected {expected}, got {total}")
    else:
        print(f"  ✗ Mismatch! Expected {expected}, got {total}")
    
    return total == expected

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print(f"AgentMath L1LP Question Generator")
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print("=" * 60)
    
    # Generate questions
    print(f"\nGenerating questions...")
    questions = generate_all_questions()
    
    # Validate
    if not validate_questions(questions):
        print("\n✗ Validation failed. Aborting.")
        exit(1)
    
    # Insert
    insert_questions(questions)
    
    # Verify
    success = verify_insertion()
    
    print("\n" + "=" * 60)
    if success:
        print("✓ COMPLETE! All questions generated successfully.")
    else:
        print("✗ INCOMPLETE. Please check errors above.")
    print("=" * 60)
