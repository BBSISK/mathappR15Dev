"""
AgentMath L1LP Question Generator
Topic: Pattern and Sequence
Learning Outcomes: 2.8 - 2.12
Version: 1.0

Generates 600 questions (50 per level × 12 levels) for the L1LP strand.
Focus: AB/ABB/ABC patterns, what comes next, ordering, sequencing, daily routines.

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
TOPIC = 'pattern_and_sequence'
MODE = 'l1lp'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

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

COLOUR_NAMES = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# Emoji representations for text-based patterns
SHAPE_EMOJIS = {
    'circle': '🔵',
    'square': '🟥',
    'triangle': '🔺',
    'star': '⭐',
    'heart': '❤️',
    'diamond': '💎'
}

# =============================================================================
# SVG GENERATION FUNCTIONS
# =============================================================================

def svg_circle(x, y, size=40, colour='#3498DB'):
    """Generate a circle SVG"""
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2 - 2}" fill="{colour}"/>'

def svg_square(x, y, size=40, colour='#E74C3C'):
    """Generate a square SVG"""
    return f'<rect x="{x + 2}" y="{y + 2}" width="{size - 4}" height="{size - 4}" fill="{colour}"/>'

def svg_triangle(x, y, size=40, colour='#27AE60'):
    """Generate a triangle SVG"""
    return f'<polygon points="{x + size//2},{y + 2} {x + 2},{y + size - 2} {x + size - 2},{y + size - 2}" fill="{colour}"/>'

def svg_star(x, y, size=40, colour='#F1C40F'):
    """Generate a star SVG"""
    cx, cy = x + size//2, y + size//2
    points = []
    for i in range(5):
        angle_outer = (i * 72 - 90) * math.pi / 180
        angle_inner = ((i * 72) + 36 - 90) * math.pi / 180
        r_outer = size//2 - 2
        r_inner = size//4
        points.append(f"{cx + r_outer * math.cos(angle_outer)},{cy + r_outer * math.sin(angle_outer)}")
        points.append(f"{cx + r_inner * math.cos(angle_inner)},{cy + r_inner * math.sin(angle_inner)}")
    return f'<polygon points="{" ".join(points)}" fill="{colour}"/>'

def svg_heart(x, y, size=40, colour='#E74C3C'):
    """Generate a heart SVG"""
    scale = size / 40
    return f'''<g transform="translate({x},{y}) scale({scale})">
        <path d="M20,35 L5,20 C0,15 0,5 10,5 C15,5 20,10 20,15 C20,10 25,5 30,5 C40,5 40,15 35,20 Z" fill="{colour}"/>
    </g>'''

def svg_diamond(x, y, size=40, colour='#9B59B6'):
    """Generate a diamond SVG"""
    cx, cy = x + size//2, y + size//2
    return f'<polygon points="{cx},{y + 2} {x + size - 2},{cy} {cx},{y + size - 2} {x + 2},{cy}" fill="{colour}"/>'

def get_shape_svg(shape, x, y, size=40, colour=None):
    """Get SVG for a named shape"""
    default_colours = {
        'circle': '#3498DB',
        'square': '#E74C3C',
        'triangle': '#27AE60',
        'star': '#F1C40F',
        'heart': '#E74C3C',
        'diamond': '#9B59B6'
    }
    
    c = colour or default_colours.get(shape, '#3498DB')
    
    shape_funcs = {
        'circle': svg_circle,
        'square': svg_square,
        'triangle': svg_triangle,
        'star': svg_star,
        'heart': svg_heart,
        'diamond': svg_diamond
    }
    
    if shape in shape_funcs:
        return shape_funcs[shape](x, y, size, c)
    return svg_circle(x, y, size, c)

def svg_coloured_circle(x, y, size=40, colour='#3498DB'):
    """Generate a coloured circle"""
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2 - 2}" fill="{colour}" stroke="#333" stroke-width="1"/>'

def svg_question_mark(x, y, size=40):
    """Generate a question mark placeholder"""
    return f'''<g>
        <rect x="{x}" y="{y}" width="{size}" height="{size}" fill="#f0f0f0" stroke="#ccc" stroke-width="2" stroke-dasharray="5,5" rx="5"/>
        <text x="{x + size//2}" y="{y + size//2 + 8}" text-anchor="middle" font-size="{size//2}" fill="#999">?</text>
    </g>'''

def create_svg_wrapper(content, width=400, height=150):
    """Wrap SVG content in full SVG element"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def create_pattern_svg(pattern, item_size=40, show_question=True, question_pos=-1):
    """Create SVG showing a pattern of shapes or colours"""
    spacing = item_size + 10
    total_items = len(pattern) + (1 if show_question else 0)
    width = max(400, total_items * spacing + 40)
    
    svg_content = ''
    start_x = (width - total_items * spacing) // 2
    y = 55
    
    for i, item in enumerate(pattern):
        x = start_x + i * spacing
        
        if isinstance(item, dict):
            # Item has shape and colour
            svg_content += get_shape_svg(item['shape'], x, y, item_size, item.get('colour'))
        elif item in COLOURS:
            # Colour-only pattern
            svg_content += svg_coloured_circle(x, y, item_size, COLOURS[item])
        elif item in ['circle', 'square', 'triangle', 'star', 'heart', 'diamond']:
            # Shape pattern
            svg_content += get_shape_svg(item, x, y, item_size)
        else:
            # Assume it's a colour name
            svg_content += svg_coloured_circle(x, y, item_size, COLOURS.get(item, '#3498DB'))
    
    # Add question mark at the end if needed
    if show_question:
        x = start_x + len(pattern) * spacing
        svg_content += svg_question_mark(x, y, item_size)
    
    return create_svg_wrapper(svg_content, width, 150)

# =============================================================================
# PATTERN GENERATION HELPERS
# =============================================================================

def generate_ab_pattern(length=6):
    """Generate an AB pattern (two alternating elements)"""
    colours = random.sample(COLOUR_NAMES, 2)
    return [colours[i % 2] for i in range(length)]

def generate_abb_pattern(length=6):
    """Generate an ABB pattern"""
    colours = random.sample(COLOUR_NAMES, 2)
    pattern = []
    for i in range(length):
        cycle_pos = i % 3
        if cycle_pos == 0:
            pattern.append(colours[0])
        else:
            pattern.append(colours[1])
    return pattern

def generate_abc_pattern(length=6):
    """Generate an ABC pattern (three different elements)"""
    colours = random.sample(COLOUR_NAMES, 3)
    return [colours[i % 3] for i in range(length)]

def generate_aab_pattern(length=6):
    """Generate an AAB pattern"""
    colours = random.sample(COLOUR_NAMES, 2)
    pattern = []
    for i in range(length):
        cycle_pos = i % 3
        if cycle_pos < 2:
            pattern.append(colours[0])
        else:
            pattern.append(colours[1])
    return pattern

def get_next_in_pattern(pattern, pattern_type):
    """Get the next element in a pattern"""
    if pattern_type == 'ab':
        return pattern[len(pattern) % 2]
    elif pattern_type == 'abb':
        pos = len(pattern) % 3
        if pos == 0:
            # Find the first unique element
            return pattern[0]
        else:
            # Return the repeated element
            return pattern[1] if pattern[1] == pattern[2] else pattern[2]
    elif pattern_type == 'abc':
        return pattern[len(pattern) % 3]
    elif pattern_type == 'aab':
        pos = len(pattern) % 3
        return pattern[0] if pos < 2 else pattern[2]
    return pattern[0]

# =============================================================================
# QUESTION GENERATORS BY LEVEL
# =============================================================================

def generate_level_1_questions():
    """Level 1: Sensory Patterns - Simple repeating patterns (2 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Simple AB pattern with colours
        colours = random.sample(COLOUR_NAMES, 2)
        pattern = [colours[0], colours[1], colours[0], colours[1], colours[0]]
        next_colour = colours[1]
        
        svg = create_pattern_svg(pattern, item_size=45)
        
        options = [colours[1].title(), colours[0].title()]
        if random.random() > 0.5:
            options.reverse()
        
        questions.append({
            'question_text': 'What colour comes next?',
            'options': json.dumps(options),
            'correct_answer': next_colour.title(),
            'explanation': f'The pattern is {colours[0]}, {colours[1]}, {colours[0]}, {colours[1]}... so {next_colour} comes next!',
            'visual_data': svg
        })
    
    return questions

def generate_level_2_questions():
    """Level 2: Patterns Around Us - Identify pattern types (2 options)"""
    questions = []
    
    pattern_examples = [
        ('stripes', 'Zebra stripes', 'Yes'),
        ('stripes', 'Tiger stripes', 'Yes'),
        ('dots', 'Polka dots on a dress', 'Yes'),
        ('checkers', 'Checkerboard', 'Yes'),
        ('solid', 'Plain wall', 'No'),
        ('random', 'Messy pile of toys', 'No')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            # Create a visual pattern
            colours = random.sample(COLOUR_NAMES, 2)
            pattern = [colours[j % 2] for j in range(6)]
            svg = create_pattern_svg(pattern, item_size=40, show_question=False)
            
            questions.append({
                'question_text': 'Is this a pattern?',
                'options': json.dumps(['Yes', 'No']),
                'correct_answer': 'Yes',
                'explanation': 'Yes! The colours repeat in order - that\'s a pattern!',
                'visual_data': svg
            })
        else:
            # Create non-pattern (random)
            colours = random.sample(COLOUR_NAMES, 6)
            svg = create_pattern_svg(colours, item_size=40, show_question=False)
            
            questions.append({
                'question_text': 'Is this a pattern?',
                'options': json.dumps(['Yes', 'No']),
                'correct_answer': 'No',
                'explanation': 'No, the colours don\'t repeat in order - it\'s not a pattern.',
                'visual_data': svg
            })
    
    return questions

def generate_level_3_questions():
    """Level 3: AB Patterns - Complete simple AB patterns (3 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        colours = random.sample(COLOUR_NAMES, 3)
        pattern_colours = colours[:2]
        wrong_colour = colours[2]
        
        pattern = [pattern_colours[j % 2] for j in range(5)]
        next_colour = pattern_colours[1]  # 5 items means next is second colour
        
        svg = create_pattern_svg(pattern, item_size=45)
        
        options = [next_colour.title(), pattern_colours[0].title(), wrong_colour.title()]
        random.shuffle(options)
        
        questions.append({
            'question_text': f'{pattern_colours[0].title()}, {pattern_colours[1].title()}, {pattern_colours[0].title()}, {pattern_colours[1].title()}, {pattern_colours[0].title()}... What comes next?',
            'options': json.dumps(options),
            'correct_answer': next_colour.title(),
            'explanation': f'The pattern is {pattern_colours[0].title()}, {pattern_colours[1].title()} repeating. After {pattern_colours[0].title()} comes {next_colour.title()}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_4_questions():
    """Level 4: ABB Patterns - Complete ABB patterns (3 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        colours = random.sample(COLOUR_NAMES, 3)
        a_colour = colours[0]
        b_colour = colours[1]
        wrong_colour = colours[2]
        
        # Create ABB pattern
        pattern = [a_colour, b_colour, b_colour, a_colour, b_colour, b_colour, a_colour]
        next_colour = b_colour  # After A comes B
        
        svg = create_pattern_svg(pattern, item_size=40)
        
        options = [b_colour.title(), a_colour.title(), wrong_colour.title()]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'What comes next in this pattern?',
            'options': json.dumps(options),
            'correct_answer': next_colour.title(),
            'explanation': f'The pattern is {a_colour.title()}, {b_colour.title()}, {b_colour.title()} repeating. After {a_colour.title()} comes {b_colour.title()}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_5_questions():
    """Level 5: ABC Patterns - Complete ABC patterns (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        colours = random.sample(COLOUR_NAMES, 4)
        pattern_colours = colours[:3]
        wrong_colour = colours[3]
        
        # Create ABC pattern - 7 items, so next should be second colour (B)
        pattern = []
        for j in range(7):
            pattern.append(pattern_colours[j % 3])
        
        next_colour = pattern_colours[1]  # 7 % 3 = 1, so next is B
        
        svg = create_pattern_svg(pattern, item_size=35)
        
        options = [c.title() for c in pattern_colours] + [wrong_colour.title()]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'What comes next in this ABC pattern?',
            'options': json.dumps(options),
            'correct_answer': next_colour.title(),
            'explanation': f'The pattern is {pattern_colours[0].title()}, {pattern_colours[1].title()}, {pattern_colours[2].title()} repeating. Next is {next_colour.title()}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_6_questions():
    """Level 6: What Comes Next - Mixed pattern types (4 options)"""
    questions = []
    
    pattern_types = ['ab', 'abb', 'abc', 'aab']
    
    for i in range(QUESTIONS_PER_LEVEL):
        p_type = random.choice(pattern_types)
        colours = random.sample(COLOUR_NAMES, 4)
        
        if p_type == 'ab':
            pattern = [colours[j % 2] for j in range(5)]
            next_colour = colours[1]
            explanation = f'AB pattern: {colours[0].title()}, {colours[1].title()} repeating'
        elif p_type == 'abb':
            pattern = []
            for j in range(7):
                cycle = j % 3
                pattern.append(colours[0] if cycle == 0 else colours[1])
            next_colour = colours[1]
            explanation = f'ABB pattern: {colours[0].title()}, {colours[1].title()}, {colours[1].title()} repeating'
        elif p_type == 'abc':
            pattern = [colours[j % 3] for j in range(7)]
            next_colour = colours[1]
            explanation = f'ABC pattern: {colours[0].title()}, {colours[1].title()}, {colours[2].title()} repeating'
        else:  # aab
            pattern = []
            for j in range(7):
                cycle = j % 3
                pattern.append(colours[0] if cycle < 2 else colours[1])
            next_colour = colours[0]
            explanation = f'AAB pattern: {colours[0].title()}, {colours[0].title()}, {colours[1].title()} repeating'
        
        svg = create_pattern_svg(pattern, item_size=35)
        
        options = list(set([next_colour.title()] + [c.title() for c in colours[:3]]))
        while len(options) < 4:
            options.append(colours[3].title())
        options = options[:4]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'What comes next?',
            'options': json.dumps(options),
            'correct_answer': next_colour.title(),
            'explanation': explanation + f'. Next is {next_colour.title()}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_7_questions():
    """Level 7: Ordering & Sequencing - Put things in order (4 options)"""
    questions = []
    
    sequences = [
        {
            'items': ['wake up', 'eat breakfast', 'go to school', 'come home'],
            'question': 'What do you do first in the morning?',
            'correct': 'Wake up',
            'explanation': 'First we wake up, then eat breakfast!'
        },
        {
            'items': ['put on socks', 'put on shoes', 'tie laces', 'walk outside'],
            'question': 'What comes before putting on shoes?',
            'correct': 'Put on socks',
            'explanation': 'We put on socks first, then shoes!'
        },
        {
            'items': ['get ingredients', 'mix together', 'bake in oven', 'eat cake'],
            'question': 'What do you do first when baking a cake?',
            'correct': 'Get ingredients',
            'explanation': 'First we get the ingredients!'
        },
        {
            'items': ['feel hungry', 'get food', 'eat food', 'feel full'],
            'question': 'What happens first?',
            'correct': 'Feel hungry',
            'explanation': 'First we feel hungry, then we get food!'
        },
        {
            'items': ['seed', 'small plant', 'big plant', 'flower'],
            'question': 'What comes first when a flower grows?',
            'correct': 'Seed',
            'explanation': 'A plant starts as a seed!'
        }
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        seq = sequences[i % len(sequences)]
        
        svg_content = ''
        for j, item in enumerate(seq['items']):
            svg_content += f'<text x="{50 + j*90}" y="80" text-anchor="middle" font-size="11" fill="#333">{j+1}. {item.title()}</text>'
        svg = create_svg_wrapper(svg_content)
        
        options = [item.title() for item in seq['items']]
        random.shuffle(options)
        
        questions.append({
            'question_text': seq['question'],
            'options': json.dumps(options),
            'correct_answer': seq['correct'],
            'explanation': seq['explanation'],
            'visual_data': svg
        })
    
    return questions

def generate_level_8_questions():
    """Level 8: Daily Routines - Order daily activities (4 options)"""
    questions = []
    
    routine_sets = [
        {
            'time': 'morning',
            'activities': ['wake up', 'brush teeth', 'eat breakfast', 'go to school'],
            'question': 'Put these morning activities in order. What comes second?',
            'correct': 'Brush teeth'
        },
        {
            'time': 'evening',
            'activities': ['eat dinner', 'watch TV', 'brush teeth', 'go to bed'],
            'question': 'Put these evening activities in order. What comes last?',
            'correct': 'Go to bed'
        },
        {
            'time': 'getting dressed',
            'activities': ['underwear', 'shirt', 'jumper', 'coat'],
            'question': 'When getting dressed, what do you put on first?',
            'correct': 'Underwear'
        },
        {
            'time': 'making sandwich',
            'activities': ['get bread', 'spread butter', 'add filling', 'put top on'],
            'question': 'When making a sandwich, what do you do third?',
            'correct': 'Add filling'
        },
        {
            'time': 'washing hands',
            'activities': ['turn on tap', 'wet hands', 'use soap', 'dry hands'],
            'question': 'When washing hands, what do you do after wetting them?',
            'correct': 'Use soap'
        }
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        routine = routine_sets[i % len(routine_sets)]
        
        svg_content = f'<text x="200" y="40" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">{routine["time"].title()} Routine</text>'
        for j, act in enumerate(routine['activities']):
            svg_content += f'<text x="{60 + j*95}" y="90" text-anchor="middle" font-size="11" fill="#666">{act.title()}</text>'
            if j < len(routine['activities']) - 1:
                svg_content += f'<text x="{105 + j*95}" y="90" fill="#999">→</text>'
        svg = create_svg_wrapper(svg_content)
        
        options = [act.title() for act in routine['activities']]
        random.shuffle(options)
        
        questions.append({
            'question_text': routine['question'],
            'options': json.dumps(options),
            'correct_answer': routine['correct'],
            'explanation': f'In the {routine["time"]} routine, {routine["correct"].lower()} is the answer!',
            'visual_data': svg
        })
    
    return questions

def generate_level_9_questions():
    """Level 9: Copying Patterns - Continue the pattern correctly (4 options)"""
    questions = []
    
    shapes = ['circle', 'square', 'triangle', 'star']
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Create a shape pattern
        pattern_shapes = random.sample(shapes, 2)
        pattern = [pattern_shapes[j % 2] for j in range(5)]
        next_shape = pattern_shapes[1]  # 5 items, next is second shape
        
        # Create SVG
        svg_content = ''
        for j, shape in enumerate(pattern):
            svg_content += get_shape_svg(shape, 30 + j*60, 55, 40)
        svg_content += svg_question_mark(330, 55, 40)
        svg = create_svg_wrapper(svg_content)
        
        options = [s.title() for s in shapes]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'Copy and continue the pattern. What shape is next?',
            'options': json.dumps(options),
            'correct_answer': next_shape.title(),
            'explanation': f'The pattern is {pattern_shapes[0]}, {pattern_shapes[1]} repeating. Next is {next_shape}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_10_questions():
    """Level 10: First, Next, Last - Position in sequence (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Create a sequence of objects
        objects = random.sample(['apple', 'ball', 'cup', 'book', 'star'], 4)
        
        position = random.choice(['first', 'second', 'third', 'last'])
        pos_map = {'first': 0, 'second': 1, 'third': 2, 'last': 3}
        correct_obj = objects[pos_map[position]]
        
        # Create SVG showing sequence
        svg_content = ''
        shape_map = {
            'apple': ('circle', '#E74C3C'),
            'ball': ('circle', '#3498DB'),
            'cup': ('square', '#9B59B6'),
            'book': ('square', '#E74C3C'),
            'star': ('star', '#F1C40F')
        }
        
        for j, obj in enumerate(objects):
            shape, colour = shape_map[obj]
            svg_content += get_shape_svg(shape, 50 + j*90, 55, 45, colour)
            svg_content += f'<text x="{72 + j*90}" y="120" text-anchor="middle" font-size="10" fill="#666">{obj.title()}</text>'
        
        svg = create_svg_wrapper(svg_content)
        
        options = [obj.title() for obj in objects]
        random.shuffle(options)
        
        questions.append({
            'question_text': f'Which object is {position}?',
            'options': json.dumps(options),
            'correct_answer': correct_obj.title(),
            'explanation': f'The {correct_obj} is {position} in the sequence!',
            'visual_data': svg
        })
    
    return questions

def generate_level_11_questions():
    """Level 11: Familiar Activities - Sequence everyday tasks (4 options)"""
    questions = []
    
    activities = [
        {
            'name': 'Making Tea',
            'steps': ['Boil water', 'Put teabag in cup', 'Pour water', 'Add milk'],
            'question': 'What comes after putting in the teabag?',
            'correct': 'Pour water'
        },
        {
            'name': 'Brushing Teeth',
            'steps': ['Get toothbrush', 'Put on toothpaste', 'Brush teeth', 'Rinse mouth'],
            'question': 'What do you do before brushing?',
            'correct': 'Put on toothpaste'
        },
        {
            'name': 'Planting a Seed',
            'steps': ['Dig hole', 'Put in seed', 'Cover with soil', 'Water it'],
            'question': 'What comes after covering with soil?',
            'correct': 'Water it'
        },
        {
            'name': 'Reading a Book',
            'steps': ['Choose book', 'Open book', 'Read pages', 'Close book'],
            'question': 'What do you do first?',
            'correct': 'Choose book'
        },
        {
            'name': 'Going Swimming',
            'steps': ['Get changed', 'Shower', 'Get in pool', 'Swim'],
            'question': 'What comes before getting in the pool?',
            'correct': 'Shower'
        }
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        activity = activities[i % len(activities)]
        
        svg_content = f'<text x="200" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">{activity["name"]}</text>'
        for j, step in enumerate(activity['steps']):
            svg_content += f'<rect x="{30 + j*95}" y="55" width="80" height="40" fill="#e8f4f8" stroke="#3498DB" rx="5"/>'
            svg_content += f'<text x="{70 + j*95}" y="78" text-anchor="middle" font-size="10" fill="#333">{step}</text>'
            if j < len(activity['steps']) - 1:
                svg_content += f'<text x="{115 + j*95}" y="78" fill="#3498DB">→</text>'
        
        svg = create_svg_wrapper(svg_content)
        
        options = activity['steps'].copy()
        random.shuffle(options)
        
        questions.append({
            'question_text': activity['question'],
            'options': json.dumps(options),
            'correct_answer': activity['correct'],
            'explanation': f'In "{activity["name"]}", {activity["correct"].lower()} is the answer!',
            'visual_data': svg
        })
    
    return questions

def generate_level_12_questions():
    """Level 12: Pattern Challenge - Mixed pattern problems (4 options)"""
    questions = []
    
    challenge_types = ['colour_pattern', 'shape_pattern', 'sequence', 'routine', 'position']
    
    for i in range(QUESTIONS_PER_LEVEL):
        c_type = challenge_types[i % len(challenge_types)]
        
        if c_type == 'colour_pattern':
            # Complex colour pattern
            colours = random.sample(COLOUR_NAMES, 4)
            pattern_type = random.choice(['ab', 'abb', 'abc'])
            
            if pattern_type == 'ab':
                pattern = [colours[j % 2] for j in range(6)]
                next_c = colours[0]
            elif pattern_type == 'abb':
                pattern = []
                for j in range(7):
                    pattern.append(colours[0] if j % 3 == 0 else colours[1])
                next_c = colours[1]
            else:
                pattern = [colours[j % 3] for j in range(7)]
                next_c = colours[1]
            
            svg = create_pattern_svg(pattern, item_size=35)
            options = [c.title() for c in colours]
            random.shuffle(options)
            
            questions.append({
                'question_text': 'What colour comes next in this pattern?',
                'options': json.dumps(options),
                'correct_answer': next_c.title(),
                'explanation': f'Following the pattern, {next_c.title()} comes next!',
                'visual_data': svg
            })
            
        elif c_type == 'shape_pattern':
            shapes = random.sample(['circle', 'square', 'triangle', 'star'], 3)
            pattern = [shapes[j % 2] for j in range(5)]
            next_s = shapes[1]
            
            svg_content = ''
            for j, shape in enumerate(pattern):
                svg_content += get_shape_svg(shape, 40 + j*55, 55, 40)
            svg_content += svg_question_mark(315, 55, 40)
            svg = create_svg_wrapper(svg_content)
            
            options = [s.title() for s in ['circle', 'square', 'triangle', 'star']]
            random.shuffle(options)
            
            questions.append({
                'question_text': 'What shape comes next?',
                'options': json.dumps(options),
                'correct_answer': next_s.title(),
                'explanation': f'The pattern shows {next_s} comes next!',
                'visual_data': svg
            })
            
        elif c_type == 'sequence':
            sequences = [
                (['tiny', 'small', 'medium', 'large'], 'What size comes after medium?', 'Large'),
                (['baby', 'child', 'teen', 'adult'], 'What stage comes after child?', 'Teen'),
                (['morning', 'afternoon', 'evening', 'night'], 'What time comes after evening?', 'Night')
            ]
            seq, question, correct = random.choice(sequences)
            
            svg_content = ''
            for j, item in enumerate(seq):
                svg_content += f'<text x="{60 + j*90}" y="80" text-anchor="middle" font-size="12" fill="#333">{item.title()}</text>'
            svg = create_svg_wrapper(svg_content)
            
            options = [s.title() for s in seq]
            random.shuffle(options)
            
            questions.append({
                'question_text': question,
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'{correct} comes next in the sequence!',
                'visual_data': svg
            })
            
        elif c_type == 'routine':
            routines = [
                (['wake', 'dress', 'eat', 'leave'], 'Morning routine - what comes second?', 'Dress'),
                (['arrive', 'learn', 'lunch', 'home'], 'School day - what comes third?', 'Lunch')
            ]
            steps, question, correct = random.choice(routines)
            
            svg_content = ''
            for j, step in enumerate(steps):
                svg_content += f'<text x="{60 + j*90}" y="80" text-anchor="middle" font-size="12" fill="#333">{step.title()}</text>'
            svg = create_svg_wrapper(svg_content)
            
            options = [s.title() for s in steps]
            random.shuffle(options)
            
            questions.append({
                'question_text': question,
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'{correct} is the answer!',
                'visual_data': svg
            })
            
        else:  # position
            items = random.sample(['🍎', '⭐', '💙', '🟢'], 4)
            position = random.choice(['first', 'second', 'third', 'last'])
            pos_idx = {'first': 0, 'second': 1, 'third': 2, 'last': 3}[position]
            correct = items[pos_idx]
            
            svg_content = ''
            for j, item in enumerate(items):
                svg_content += f'<text x="{70 + j*80}" y="85" text-anchor="middle" font-size="30">{item}</text>'
            svg = create_svg_wrapper(svg_content)
            
            options = items.copy()
            random.shuffle(options)
            
            questions.append({
                'question_text': f'Which symbol is {position}?',
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'{correct} is {position} in the row!',
                'visual_data': svg
            })
    
    return questions

# =============================================================================
# MAIN GENERATION AND DATABASE FUNCTIONS
# =============================================================================

def generate_all_questions():
    """Generate all questions for all levels"""
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
        # Check required fields
        required = ['question_text', 'options', 'correct_answer', 'level', 'topic', 'mode']
        for field in required:
            if field not in q or not q[field]:
                errors.append(f"Question {i}: Missing {field}")
        
        # Check correct answer is in options
        try:
            options = json.loads(q['options'])
            if q['correct_answer'] not in options:
                errors.append(f"Question {i}: Correct answer '{q['correct_answer']}' not in options {options}")
        except:
            errors.append(f"Question {i}: Invalid options JSON")
    
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
                (topic, mode, difficulty_level, question_text, options, correct_answer, explanation, visual_data)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'],
                q['mode'],
                q['level'],
                q['question_text'],
                q['options'],
                q['correct_answer'],
                q.get('explanation', ''),
                q.get('visual_data', '')
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
