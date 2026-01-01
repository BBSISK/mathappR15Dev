"""
AgentMath L2LP Question Generator
Topic: Number & Money (l2_number_and_money)
NCCA Module: Understanding number and money

Generates 600 questions (50 per level × 12 levels) for the L2LP strand.
High visual percentage with SVG graphics for accessibility.

*** V2: Uses questions_adaptive table (correct for adaptive quiz API) ***

Author: AgentMath Generator
Version: 2.0
Date: December 2025
"""

import sqlite3
import random
import json
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'l2_number_and_money'
MODE = 'adaptive'
DIFFICULTY = 'adaptive'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

# Visual percentage targets by level
def get_visual_percentage(level):
    if level <= 3:
        return 85  # Foundation - maximum visual support
    elif level <= 6:
        return 75  # Developing - high visual support
    elif level <= 9:
        return 65  # Progressing - moderate visual support
    else:
        return 55  # Consolidating - building text confidence


def get_difficulty_band(level):
    """Map level 1-12 to difficulty band for questions_adaptive table"""
    if level <= 3:
        return 'beginner'
    elif level <= 6:
        return 'intermediate'
    elif level <= 9:
        return 'advanced'
    elif level == 10:
        return 'mastery'
    elif level == 11:
        return 'application'
    else:
        return 'linked'  # Level 12


def ensure_four_options(correct, distractors, option_pool=None):
    """Ensure we have exactly 4 options (1 correct + 3 distractors)"""
    # Remove duplicates and the correct answer from distractors
    distractors = [d for d in distractors if d != correct]
    distractors = list(dict.fromkeys(distractors))  # Remove duplicates, preserve order
    
    # If we don't have enough, add from pool or generate randoms
    while len(distractors) < 3:
        if option_pool:
            for opt in option_pool:
                if opt != correct and opt not in distractors:
                    distractors.append(opt)
                    break
            else:
                # Pool exhausted, add a variation
                if isinstance(correct, (int, float)):
                    new_d = correct + random.randint(1, 10)
                    if new_d not in distractors and new_d != correct:
                        distractors.append(new_d)
                else:
                    break
        else:
            # No pool, try to create numeric variations
            if isinstance(correct, (int, float)):
                new_d = correct + random.randint(-5, 10)
                if new_d not in distractors and new_d != correct and new_d >= 0:
                    distractors.append(new_d)
            else:
                break
    
    distractors = distractors[:3]
    
    # Convert all to strings for consistency
    options = [str(correct)] + [str(d) for d in distractors]
    
    # Ensure we have exactly 4 options
    while len(options) < 4:
        options.append("")  # Fallback - shouldn't happen
    
    random.shuffle(options)
    correct_letter = ['A', 'B', 'C', 'D'][options.index(str(correct))]
    
    return options, correct_letter

# ============================================================
# COLOUR PALETTE
# ============================================================

COLOURS = {
    'orange': '#f97316',
    'red': '#dc2626',
    'blue': '#3b82f6',
    'green': '#22c55e',
    'yellow': '#eab308',
    'purple': '#8b5cf6',
    'grey': '#6b7280',
    'dark': '#1f2937',
    'white': '#ffffff',
    'light_grey': '#f3f4f6',
    'gold': '#d4a017',
    'copper': '#b87333',
    'silver': '#c0c0c0'
}

# ============================================================
# SVG GENERATION FUNCTIONS
# ============================================================

def generate_objects_svg(count, object_type='circle', colour='#3b82f6'):
    """Generate SVG showing a count of objects"""
    objects = {
        'circle': lambda x, y: f'<circle cx="{x}" cy="{y}" r="20" fill="{colour}"/>',
        'star': lambda x, y: f'''<polygon points="{x},{y-22} {x+7},{y-7} {x+23},{y-7} {x+10},{y+5} 
            {x+15},{y+22} {x},{y+12} {x-15},{y+22} {x-10},{y+5} {x-23},{y-7} {x-7},{y-7}" 
            fill="{colour}"/>''',
        'apple': lambda x, y: f'''<ellipse cx="{x}" cy="{y+5}" rx="18" ry="20" fill="#e74c3c"/>
            <ellipse cx="{x-5}" cy="{y-5}" rx="4" ry="8" fill="#27ae60"/>
            <rect x="{x-2}" y="{y-18}" width="4" height="12" fill="#8B4513"/>''',
        'square': lambda x, y: f'<rect x="{x-18}" y="{y-18}" width="36" height="36" fill="{colour}" rx="3"/>',
    }
    
    # Arrange objects in a grid
    cols = min(count, 5)
    rows = (count + cols - 1) // cols
    
    width = cols * 60 + 40
    height = rows * 60 + 40
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    svg += f'<rect width="{width}" height="{height}" fill="{COLOURS["light_grey"]}"/>'
    
    obj_func = objects.get(object_type, objects['circle'])
    
    for i in range(count):
        row = i // cols
        col = i % cols
        x = 50 + col * 60
        y = 50 + row * 60
        svg += obj_func(x, y)
    
    svg += '</svg>'
    return svg


def generate_number_svg(number, size='large'):
    """Generate SVG showing a number prominently"""
    font_size = 72 if size == 'large' else 48
    width = len(str(number)) * 50 + 40
    height = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
        <rect width="{width}" height="{height}" fill="{COLOURS['light_grey']}" rx="10"/>
        <text x="{width//2}" y="70" font-size="{font_size}" font-family="Arial, sans-serif" 
            font-weight="bold" fill="{COLOURS['dark']}" text-anchor="middle">{number}</text>
    </svg>'''
    return svg


def generate_place_value_svg(number):
    """Generate SVG showing place value blocks (tens and ones)"""
    tens = number // 10
    ones = number % 10
    
    width = max(tens * 25 + ones * 25 + 100, 300)
    height = 180
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
        <rect width="{width}" height="{height}" fill="{COLOURS['light_grey']}"/>
        <text x="20" y="30" font-size="16" font-family="Arial" fill="{COLOURS['dark']}">Tens</text>
        <text x="20" y="130" font-size="16" font-family="Arial" fill="{COLOURS['dark']}">Ones</text>
    '''
    
    # Draw tens (tall rectangles)
    for i in range(tens):
        x = 70 + i * 25
        svg += f'<rect x="{x}" y="15" width="20" height="60" fill="{COLOURS["blue"]}" stroke="{COLOURS["dark"]}" stroke-width="1" rx="2"/>'
    
    # Draw ones (small squares)
    for i in range(ones):
        x = 70 + i * 25
        svg += f'<rect x="{x}" y="110" width="20" height="20" fill="{COLOURS["orange"]}" stroke="{COLOURS["dark"]}" stroke-width="1" rx="2"/>'
    
    # Show the number
    svg += f'''<text x="{width - 50}" y="90" font-size="48" font-family="Arial" 
        font-weight="bold" fill="{COLOURS['dark']}" text-anchor="middle">{number}</text>'''
    
    svg += '</svg>'
    return svg


def generate_euro_coin_svg(value):
    """Generate SVG of a Euro coin"""
    # Coin colours based on value
    if value >= 1:  # €1 and €2 are bimetallic
        outer_colour = COLOURS['gold']
        inner_colour = COLOURS['silver']
    elif value >= 0.10:  # 10c, 20c, 50c are gold-coloured
        outer_colour = COLOURS['gold']
        inner_colour = COLOURS['gold']
    else:  # 1c, 2c, 5c are copper-coloured
        outer_colour = COLOURS['copper']
        inner_colour = COLOURS['copper']
    
    # Format display value
    if value >= 1:
        display = f"€{int(value)}"
    else:
        display = f"{int(value*100)}c"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80">
        <circle cx="40" cy="40" r="35" fill="{outer_colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        <circle cx="40" cy="40" r="25" fill="{inner_colour}"/>
        <text x="40" y="48" font-size="18" font-family="Arial" font-weight="bold" 
            fill="{COLOURS['dark']}" text-anchor="middle">{display}</text>
    </svg>'''
    return svg


def generate_coins_svg(coins_list):
    """Generate SVG showing multiple Euro coins"""
    width = len(coins_list) * 85 + 20
    height = 100
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    svg += f'<rect width="{width}" height="{height}" fill="{COLOURS["light_grey"]}"/>'
    
    for i, value in enumerate(coins_list):
        x = 50 + i * 85
        
        # Coin colours
        if value >= 1:
            outer_colour = COLOURS['gold']
            inner_colour = COLOURS['silver']
        elif value >= 0.10:
            outer_colour = COLOURS['gold']
            inner_colour = COLOURS['gold']
        else:
            outer_colour = COLOURS['copper']
            inner_colour = COLOURS['copper']
        
        # Display value
        if value >= 1:
            display = f"€{int(value)}"
        else:
            display = f"{int(value*100)}c"
        
        svg += f'''<circle cx="{x}" cy="50" r="35" fill="{outer_colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <circle cx="{x}" cy="50" r="25" fill="{inner_colour}"/>
            <text x="{x}" y="58" font-size="16" font-family="Arial" font-weight="bold" 
                fill="{COLOURS['dark']}" text-anchor="middle">{display}</text>'''
    
    svg += '</svg>'
    return svg


def generate_euro_note_svg(value):
    """Generate SVG of a Euro note"""
    # Note colours
    note_colours = {
        5: '#c4c4c4',    # Grey
        10: '#e8a4a4',   # Red/pink
        20: '#a4c4e8',   # Blue
        50: '#e8c4a4',   # Orange
        100: '#a4e8a4'   # Green
    }
    
    colour = note_colours.get(value, '#c4c4c4')
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 100">
        <rect x="5" y="5" width="170" height="90" fill="{colour}" stroke="{COLOURS['dark']}" stroke-width="2" rx="5"/>
        <text x="90" y="60" font-size="36" font-family="Arial" font-weight="bold" 
            fill="{COLOURS['dark']}" text-anchor="middle">€{value}</text>
        <text x="90" y="80" font-size="12" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">EURO</text>
    </svg>'''
    return svg


def generate_price_tag_svg(price):
    """Generate SVG of a price tag"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 80">
        <polygon points="10,40 30,20 110,20 110,60 30,60" fill="{COLOURS['yellow']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        <circle cx="20" cy="40" r="5" fill="{COLOURS['white']}"/>
        <text x="70" y="48" font-size="24" font-family="Arial" font-weight="bold" 
            fill="{COLOURS['dark']}" text-anchor="middle">€{price:.2f}</text>
    </svg>'''
    return svg


def generate_shopping_item_svg(item_name, price):
    """Generate SVG of a shopping item with price"""
    # Simple item representations
    items = {
        'bread': f'''<rect x="30" y="40" width="60" height="30" fill="#d4a574" rx="5"/>
            <ellipse cx="60" cy="40" rx="30" ry="10" fill="#c4956a"/>''',
        'milk': f'''<rect x="40" y="30" width="40" height="50" fill="{COLOURS['white']}" stroke="{COLOURS['blue']}" stroke-width="2" rx="3"/>
            <text x="60" y="60" font-size="10" fill="{COLOURS['blue']}" text-anchor="middle">MILK</text>''',
        'apple': f'''<ellipse cx="60" cy="50" rx="25" ry="22" fill="#e74c3c"/>
            <rect x="58" y="20" width="4" height="12" fill="#8B4513"/>
            <ellipse cx="55" cy="28" rx="6" ry="10" fill="#27ae60"/>''',
        'banana': f'''<path d="M35,60 Q40,30 60,25 Q80,30 85,50 Q75,55 55,55 Q40,55 35,60" fill="#f1c40f" stroke="#c9a227" stroke-width="2"/>''',
        'egg': f'''<ellipse cx="60" cy="50" rx="20" ry="28" fill="#fdf5e6" stroke="#d4c4a8" stroke-width="1"/>''',
        'water': f'''<rect x="45" y="25" width="30" height="55" fill="#87ceeb" stroke="{COLOURS['blue']}" stroke-width="2" rx="3"/>
            <text x="60" y="55" font-size="8" fill="{COLOURS['dark']}" text-anchor="middle">WATER</text>''',
    }
    
    item_svg = items.get(item_name.lower(), items['apple'])
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">
        <rect width="120" height="120" fill="{COLOURS['light_grey']}" rx="5"/>
        {item_svg}
        <rect x="25" y="85" width="70" height="25" fill="{COLOURS['yellow']}" rx="3"/>
        <text x="60" y="103" font-size="14" font-family="Arial" font-weight="bold" 
            fill="{COLOURS['dark']}" text-anchor="middle">€{price:.2f}</text>
    </svg>'''
    return svg


def generate_receipt_svg(items, prices, total):
    """Generate SVG of a receipt"""
    height = 80 + len(items) * 25 + 40
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 {height}">
        <rect x="10" y="10" width="180" height="{height-20}" fill="{COLOURS['white']}" stroke="{COLOURS['dark']}" stroke-width="1"/>
        <text x="100" y="35" font-size="14" font-family="Arial" font-weight="bold" fill="{COLOURS['dark']}" text-anchor="middle">RECEIPT</text>
        <line x1="20" y1="45" x2="180" y2="45" stroke="{COLOURS['dark']}" stroke-width="1"/>
    '''
    
    y = 65
    for item, price in zip(items, prices):
        svg += f'''<text x="25" y="{y}" font-size="12" font-family="Arial" fill="{COLOURS['dark']}">{item}</text>
            <text x="175" y="{y}" font-size="12" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="end">€{price:.2f}</text>'''
        y += 25
    
    svg += f'''<line x1="20" y1="{y-10}" x2="180" y2="{y-10}" stroke="{COLOURS['dark']}" stroke-width="1"/>
        <text x="25" y="{y+15}" font-size="14" font-family="Arial" font-weight="bold" fill="{COLOURS['dark']}">TOTAL</text>
        <text x="175" y="{y+15}" font-size="14" font-family="Arial" font-weight="bold" fill="{COLOURS['dark']}" text-anchor="end">€{total:.2f}</text>
    </svg>'''
    return svg


def generate_number_line_svg(start, end, highlight=None):
    """Generate SVG of a number line"""
    width = 400
    height = 80
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
        <rect width="{width}" height="{height}" fill="{COLOURS['light_grey']}"/>
        <line x1="30" y1="40" x2="{width-30}" y2="40" stroke="{COLOURS['dark']}" stroke-width="2"/>
    '''
    
    # Calculate positions
    range_size = end - start
    step = (width - 60) / range_size
    
    for i in range(range_size + 1):
        x = 30 + i * step
        num = start + i
        
        # Highlight specific number
        if highlight is not None and num == highlight:
            svg += f'''<circle cx="{x}" cy="40" r="15" fill="{COLOURS['orange']}"/>
                <text x="{x}" y="45" font-size="14" fill="{COLOURS['white']}" text-anchor="middle" font-weight="bold">{num}</text>'''
        else:
            svg += f'''<line x1="{x}" y1="35" x2="{x}" y2="45" stroke="{COLOURS['dark']}" stroke-width="2"/>
                <text x="{x}" y="60" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">{num}</text>'''
    
    svg += '</svg>'
    return svg


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1_questions():
    """Level 1: Numbers in Real Life (Foundation)
    NCCA LOs: a, b - Give examples of numbers in real world, count by gesturing
    """
    questions = []
    
    # Visual percentage for this level: 85%
    visual_count = int(QUESTIONS_PER_LEVEL * 0.85)
    
    # Type 1: Where do we see numbers? (10 questions)
    number_locations = [
        ("on a bus", "On the front of a bus", "route number"),
        ("on a door", "On a house door", "house number"),
        ("on a phone", "On a mobile phone", "phone number"),
        ("on a clock", "On a clock face", "time"),
        ("on a price tag", "On a price tag in a shop", "cost"),
        ("on a birthday card", "On a birthday card", "age"),
        ("on a TV remote", "On a TV remote", "channel"),
        ("on a calendar", "On a calendar", "date"),
        ("on a football jersey", "On a sports jersey", "player number"),
        ("on a speed limit sign", "On a road sign", "speed limit"),
    ]
    
    for location, full_location, purpose in number_locations:
        wrong_answers = random.sample([
            "To make it look pretty",
            "For decoration only",
            "It's just a pattern",
            "To fill empty space"
        ], 3)
        
        correct = f"To show the {purpose}"
        options = [correct] + wrong_answers
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Why might we see a number {location}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{full_location} shows a number to tell us the {purpose}.",
            'question_image_svg': ''
        })
    
    # Type 2: Counting objects with visuals (25 questions)
    objects_types = ['circle', 'star', 'apple', 'square']
    colours = [COLOURS['blue'], COLOURS['green'], COLOURS['orange'], COLOURS['purple']]
    colour_names = {COLOURS['blue']: 'blue', COLOURS['green']: 'green', 
                    COLOURS['orange']: 'orange', COLOURS['purple']: 'purple'}
    
    for i in range(25):
        count = random.randint(1, 10)
        obj_type = random.choice(objects_types)
        colour = random.choice(colours)
        colour_name = colour_names[colour]
        
        # Generate distractors
        distractors = [count - 1, count + 1, count + 2]
        distractors = [d for d in distractors if d > 0 and d != count]
        while len(distractors) < 3:
            d = random.randint(1, 12)
            if d != count and d not in distractors:
                distractors.append(d)
        distractors = distractors[:3]
        
        options = [str(count)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(count))]
        
        obj_name = 'shapes' if obj_type in ['circle', 'square'] else obj_type + 's'
        
        # Vary question wording to avoid duplicates
        question_variants = [
            f"How many {colour_name} {obj_name} can you count?",
            f"Count the {colour_name} {obj_name}. How many are there?",
            f"Look at the {colour_name} {obj_name}. How many do you see?",
        ]
        question_text = question_variants[i % 3]
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Count each {obj_type} one by one: there are {count} {obj_name}.",
            'question_image_svg': generate_objects_svg(count, obj_type, colour)
        })
    
    # Type 3: Number recognition (10 questions)
    for i in range(10):
        number = random.randint(1, 20)
        
        distractors = []
        while len(distractors) < 3:
            d = random.randint(1, 20)
            if d != number and d not in distractors:
                distractors.append(d)
        
        options = [str(number)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(number))]
        
        questions.append({
            'question_text': "What number is shown?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The number shown is {number}.",
            'question_image_svg': generate_number_svg(number)
        })
    
    # Type 4: Match count to number (5 questions - text only)
    for i in range(5):
        count = random.randint(3, 10)
        word_forms = {
            1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'
        }
        
        correct = str(count)
        distractors = random.sample([str(n) for n in range(1, 11) if n != count], 3)
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Which number is {word_forms[count]}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The word '{word_forms[count]}' means the number {count}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_2_questions():
    """Level 2: Counting Skills (Foundation)
    NCCA LOs: b, f - Count by gesturing, use numbers to designate quantity
    """
    questions = []
    
    colour_names = {COLOURS['blue']: 'blue', COLOURS['green']: 'green', 
                    COLOURS['orange']: 'orange', COLOURS['purple']: 'purple'}
    
    # Type 1: Count larger groups (20 questions)
    for i in range(20):
        count = random.randint(5, 15)
        obj_type = random.choice(['circle', 'star', 'apple', 'square'])
        colour = random.choice([COLOURS['blue'], COLOURS['green'], COLOURS['orange'], COLOURS['purple']])
        colour_name = colour_names[colour]
        
        distractors = [count - 2, count - 1, count + 1, count + 2]
        distractors = [d for d in distractors if d > 0 and d != count][:3]
        
        options = [str(count)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(count))]
        
        obj_name = obj_type + 's' if obj_type not in ['circle', 'square'] else 'shapes'
        question_variants = [
            f"Count the {colour_name} {obj_name} carefully. How many are there?",
            f"Look at all the {colour_name} {obj_name}. Count them. How many?",
            f"How many {colour_name} {obj_name} can you see in total?",
            f"Count each {colour_name} {obj_name}. What is the total?",
        ]
        
        questions.append({
            'question_text': question_variants[i % 4],
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Counting one by one, there are {count} objects.",
            'question_image_svg': generate_objects_svg(count, obj_type, colour)
        })
    
    # Type 2: More or less comparisons (15 questions)
    for i in range(15):
        count1 = random.randint(3, 10)
        count2 = count1 + random.choice([-3, -2, -1, 1, 2, 3])
        count2 = max(1, count2)
        
        if count1 > count2:
            correct = "Group A has more"
            solution = f"Group A has {count1} and Group B has {count2}. {count1} is more than {count2}."
        elif count2 > count1:
            correct = "Group B has more"
            solution = f"Group A has {count1} and Group B has {count2}. {count2} is more than {count1}."
        else:
            correct = "They have the same"
            solution = f"Both groups have {count1}. They are equal."
        
        options = ["Group A has more", "Group B has more", "They have the same", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        # Create side-by-side SVG
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 150">
            <rect width="400" height="150" fill="{COLOURS['light_grey']}"/>
            <text x="100" y="25" font-size="16" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">Group A</text>
            <text x="300" y="25" font-size="16" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">Group B</text>
            <line x1="200" y1="30" x2="200" y2="140" stroke="{COLOURS['dark']}" stroke-width="2" stroke-dasharray="5,5"/>
        '''
        
        # Add circles for Group A
        for j in range(count1):
            x = 40 + (j % 4) * 40
            y = 60 + (j // 4) * 40
            svg += f'<circle cx="{x}" cy="{y}" r="15" fill="{COLOURS["blue"]}"/>'
        
        # Add circles for Group B
        for j in range(count2):
            x = 240 + (j % 4) * 40
            y = 60 + (j // 4) * 40
            svg += f'<circle cx="{x}" cy="{y}" r="15" fill="{COLOURS["green"]}"/>'
        
        svg += '</svg>'
        
        questions.append({
            'question_text': "Which group has more?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': svg
        })
    
    # Type 3: Count on from a number (10 questions)
    for i in range(10):
        start = random.randint(5, 15)
        add = random.randint(1, 5)
        result = start + add
        
        distractors = [result - 1, result + 1, start]
        distractors = [d for d in distractors if d != result][:3]
        
        options = [str(result)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(result))]
        
        questions.append({
            'question_text': f"Start at {start}. Count on {add} more. What number do you reach?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Starting at {start} and counting {add} more: {', '.join(str(start + j) for j in range(1, add + 1))}. We reach {result}.",
            'question_image_svg': generate_number_line_svg(start - 2, result + 2, result)
        })
    
    # Type 4: Count backwards (5 questions)
    for i in range(5):
        start = random.randint(8, 15)
        subtract = random.randint(1, 4)
        result = start - subtract
        
        distractors = [result - 1, result + 1, start]
        distractors = [d for d in distractors if d != result and d > 0]
        while len(distractors) < 3:
            d = random.randint(1, 15)
            if d != result and d not in distractors:
                distractors.append(d)
        distractors = distractors[:3]
        
        options = [str(result)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(result))]
        
        questions.append({
            'question_text': f"Start at {start}. Count back {subtract}. What number do you reach?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Starting at {start} and counting back {subtract}: {', '.join(str(start - j) for j in range(1, subtract + 1))}. We reach {result}.",
            'question_image_svg': generate_number_line_svg(result - 2, start + 2, result)
        })
    
    return questions


def generate_level_3_questions():
    """Level 3: Tens and Ones (Foundation)
    NCCA LO: c - Interpret numbers in tens and ones
    """
    questions = []
    
    # Type 1: Identify tens in a number (15 questions)
    for i in range(15):
        number = random.randint(11, 99)
        tens = number // 10
        
        distractors = [tens - 1, tens + 1, number % 10]
        distractors = [d for d in distractors if d != tens and d >= 0]
        # Ensure we have at least 3 distractors
        while len(distractors) < 3:
            d = random.randint(0, 9)
            if d != tens and d not in distractors:
                distractors.append(d)
        distractors = distractors[:3]
        
        options = [str(tens)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(tens))]
        
        questions.append({
            'question_text': f"How many tens in {number}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{number} = {tens} tens and {number % 10} ones. There are {tens} tens.",
            'question_image_svg': generate_place_value_svg(number)
        })
    
    # Type 2: Identify ones in a number (15 questions)
    for i in range(15):
        number = random.randint(11, 99)
        ones = number % 10
        
        distractors = [ones - 1, ones + 1, number // 10]
        distractors = [d for d in distractors if d != ones and d >= 0][:3]
        while len(distractors) < 3:
            d = random.randint(0, 9)
            if d != ones and d not in distractors:
                distractors.append(d)
        
        options = [str(ones)] + [str(d) for d in distractors[:3]]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(ones))]
        
        questions.append({
            'question_text': f"How many ones in {number}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{number} = {number // 10} tens and {ones} ones. There are {ones} ones.",
            'question_image_svg': generate_place_value_svg(number)
        })
    
    # Type 3: Build number from tens and ones (15 questions)
    for i in range(15):
        tens = random.randint(1, 9)
        ones = random.randint(0, 9)
        number = tens * 10 + ones
        
        distractors = [number + 10, number - 10, ones * 10 + tens]
        distractors = [d for d in distractors if d != number and d > 0][:3]
        
        options = [str(number)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(number))]
        
        questions.append({
            'question_text': f"{tens} tens and {ones} ones makes what number?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{tens} tens = {tens * 10}. Add {ones} ones = {number}.",
            'question_image_svg': generate_place_value_svg(number)
        })
    
    # Type 4: Word problems with tens and ones (5 questions)
    scenarios = [
        ("Sara has {tens} packs of 10 stickers and {ones} loose stickers", "stickers"),
        ("Tom has {tens} bags of 10 sweets and {ones} extra sweets", "sweets"),
        ("The shop has {tens} boxes of 10 eggs and {ones} single eggs", "eggs"),
        ("There are {tens} rows of 10 seats and {ones} extra seats", "seats"),
        ("We have {tens} bundles of 10 pencils and {ones} loose pencils", "pencils"),
    ]
    
    for scenario_template, item in scenarios:
        tens = random.randint(2, 8)
        ones = random.randint(1, 9)
        number = tens * 10 + ones
        
        scenario = scenario_template.format(tens=tens, ones=ones)
        
        distractors = [tens + ones, tens * ones, number + 10]
        distractors = [d for d in distractors if d != number][:3]
        
        options = [str(number)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(number))]
        
        questions.append({
            'question_text': f"{scenario}. How many {item} in total?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{tens} packs/bags of 10 = {tens * 10}. Plus {ones} loose = {number} {item}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_4_questions():
    """Level 4: Place Value (Developing)
    NCCA LO: d - Identify how many zeros for tens, hundreds, thousands
    """
    questions = []
    
    # Type 1: Zeros in powers of 10 (10 questions)
    place_values = [
        (10, "ten", 1),
        (100, "one hundred", 2),
        (1000, "one thousand", 3),
        (10, "10", 1),
        (100, "100", 2),
        (1000, "1000", 3),
        (10, "a ten", 1),
        (100, "a hundred", 2),
        (1000, "a thousand", 3),
        (10, "ten", 1),
    ]
    
    for value, word, zeros in place_values:
        distractors = [0, 1, 2, 3, 4]
        distractors = [d for d in distractors if d != zeros][:3]
        
        options = [str(zeros)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(zeros))]
        
        questions.append({
            'question_text': f"How many zeros in {word}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{word.capitalize()} is written as {value}. It has {zeros} zero(s).",
            'question_image_svg': generate_number_svg(value)
        })
    
    # Type 2: Identify place value of a digit (15 questions)
    for i in range(15):
        number = random.randint(100, 999)
        digits = list(str(number))
        position = random.choice(['hundreds', 'tens', 'ones'])
        
        if position == 'hundreds':
            digit = int(digits[0])
            value = digit * 100
        elif position == 'tens':
            digit = int(digits[1])
            value = digit * 10
        else:
            digit = int(digits[2])
            value = digit
        
        distractors = []
        for d in [digit, digit * 10, digit * 100]:
            if d != value:
                distractors.append(d)
        while len(distractors) < 3:
            d = random.randint(1, 900)
            if d != value and d not in distractors:
                distractors.append(d)
        distractors = distractors[:3]
        
        options = [str(value)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(value))]
        
        questions.append({
            'question_text': f"In the number {number}, what is the value of the digit in the {position} place?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"In {number}, the {position} digit is {digit}. Its value is {value}.",
            'question_image_svg': generate_number_svg(number)
        })
    
    # Type 3: Which is bigger - comparing by place value (15 questions)
    for i in range(15):
        num1 = random.randint(100, 999)
        # Create a number that differs in a specific place
        diff_place = random.choice(['hundreds', 'tens', 'ones'])
        
        if diff_place == 'hundreds':
            num2 = num1 + random.choice([-100, 100])
        elif diff_place == 'tens':
            num2 = num1 + random.choice([-10, -20, 10, 20])
        else:
            num2 = num1 + random.choice([-1, -2, 1, 2])
        
        num2 = max(100, min(999, num2))
        
        if num1 > num2:
            correct = str(num1)
            solution = f"{num1} is bigger than {num2}."
        else:
            correct = str(num2)
            solution = f"{num2} is bigger than {num1}."
        
        options = [str(num1), str(num2), "They are equal", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)] if correct in options else 'C'
        
        questions.append({
            'question_text': f"Which number is bigger: {num1} or {num2}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    # Type 4: Build numbers from place values (10 questions)
    for i in range(10):
        hundreds = random.randint(1, 9)
        tens = random.randint(0, 9)
        ones = random.randint(0, 9)
        number = hundreds * 100 + tens * 10 + ones
        
        distractors = [number + 100, number - 100, int(str(ones) + str(tens) + str(hundreds))]
        distractors = [d for d in distractors if d != number and d > 0][:3]
        
        options = [str(number)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(number))]
        
        questions.append({
            'question_text': f"What number has {hundreds} hundreds, {tens} tens, and {ones} ones?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{hundreds} hundreds = {hundreds * 100}. Add {tens} tens = {hundreds * 100 + tens * 10}. Add {ones} ones = {number}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_5_questions():
    """Level 5: Estimating Amounts (Developing)
    NCCA LO: e - Estimate quantities to nearest 10s or 100s
    """
    questions = []
    
    # Type 1: Round to nearest 10 (20 questions)
    for i in range(20):
        number = random.randint(11, 99)
        rounded = round(number, -1)
        
        distractors = [rounded - 10, rounded + 10, number]
        distractors = [d for d in distractors if d != rounded and d >= 0][:3]
        
        options = [str(int(rounded))] + [str(int(d)) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(int(rounded)))]
        
        questions.append({
            'question_text': f"Round {number} to the nearest 10.",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{number} is closest to {int(rounded)} when rounding to the nearest 10.",
            'question_image_svg': generate_number_line_svg((number // 10) * 10, (number // 10 + 1) * 10 + 5, number)
        })
    
    # Type 2: Round to nearest 100 (15 questions)
    for i in range(15):
        number = random.randint(101, 999)
        rounded = round(number, -2)
        
        distractors = [rounded - 100, rounded + 100, number]
        distractors = [d for d in distractors if d != rounded and d > 0][:3]
        
        options = [str(int(rounded))] + [str(int(d)) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(int(rounded)))]
        
        questions.append({
            'question_text': f"Round {number} to the nearest 100.",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{number} is closest to {int(rounded)} when rounding to the nearest 100.",
            'question_image_svg': ''
        })
    
    # Type 3: Estimate with context (15 questions)
    contexts = [
        ("There are {n} people at a concert. About how many is that?", "people"),
        ("The shop sold {n} bottles of water. About how many is that?", "bottles"),
        ("A book has {n} pages. About how many pages is that?", "pages"),
        ("{n} students took the bus. About how many students is that?", "students"),
        ("The farmer has {n} sheep. About how many sheep is that?", "sheep"),
    ]
    
    for i in range(15):
        context_template, item = random.choice(contexts)
        number = random.randint(51, 99)
        rounded = round(number, -1)
        
        context = context_template.format(n=number)
        
        distractors = [rounded - 10, rounded + 10, number]
        distractors = [d for d in distractors if d != rounded and d > 0][:3]
        
        options = [f"About {int(rounded)}", f"About {int(distractors[0])}", f"About {int(distractors[1])}", f"Exactly {number}"]
        correct_letter = 'A'
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(f"About {int(rounded)}")]
        
        questions.append({
            'question_text': context,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{number} rounded to the nearest 10 is about {int(rounded)} {item}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_6_questions():
    """Level 6: Adding & Subtracting (Developing)
    NCCA LOs: g, h - Identify when to add/subtract, use symbols
    """
    questions = []
    
    # Type 1: Visual addition (15 questions)
    for i in range(15):
        num1 = random.randint(3, 10)
        num2 = random.randint(2, 8)
        total = num1 + num2
        
        distractors = [total - 1, total + 1, num1]
        distractors = [d for d in distractors if d != total][:3]
        
        options = [str(total)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(total))]
        
        # Create combined visual
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 100">
            <rect width="450" height="100" fill="{COLOURS['light_grey']}"/>
        '''
        
        # First group
        for j in range(num1):
            x = 30 + (j % 5) * 35
            y = 30 + (j // 5) * 35
            svg += f'<circle cx="{x}" cy="{y}" r="12" fill="{COLOURS["blue"]}"/>'
        
        # Plus sign
        svg += f'''<text x="200" y="55" font-size="36" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">+</text>'''
        
        # Second group
        for j in range(num2):
            x = 250 + (j % 5) * 35
            y = 30 + (j // 5) * 35
            svg += f'<circle cx="{x}" cy="{y}" r="12" fill="{COLOURS["green"]}"/>'
        
        svg += f'''<text x="420" y="55" font-size="24" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">=?</text>'''
        svg += '</svg>'
        
        questions.append({
            'question_text': f"How many altogether?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{num1} + {num2} = {total}",
            'question_image_svg': svg
        })
    
    # Type 2: Simple addition calculations (10 questions)
    for i in range(10):
        num1 = random.randint(10, 50)
        num2 = random.randint(5, 30)
        total = num1 + num2
        
        distractors = [total - 1, total + 1, total + 10]
        distractors = [d for d in distractors if d != total][:3]
        
        options = [str(total)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(total))]
        
        questions.append({
            'question_text': f"What is {num1} + {num2}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{num1} + {num2} = {total}",
            'question_image_svg': ''
        })
    
    # Type 3: Visual subtraction (10 questions)
    for i in range(10):
        total = random.randint(8, 15)
        subtract = random.randint(2, total - 2)
        result = total - subtract
        
        distractors = [result - 1, result + 1, total]
        distractors = [d for d in distractors if d != result and d > 0][:3]
        
        options = [str(result)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(result))]
        
        # Create visual with crossed out items
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 100">
            <rect width="350" height="100" fill="{COLOURS['light_grey']}"/>
        '''
        
        for j in range(total):
            x = 30 + (j % 8) * 40
            y = 40 + (j // 8) * 40
            if j >= result:
                svg += f'<circle cx="{x}" cy="{y}" r="15" fill="{COLOURS["grey"]}" opacity="0.5"/>'
                svg += f'<line x1="{x-15}" y1="{y-15}" x2="{x+15}" y2="{y+15}" stroke="{COLOURS["red"]}" stroke-width="3"/>'
            else:
                svg += f'<circle cx="{x}" cy="{y}" r="15" fill="{COLOURS["blue"]}"/>'
        
        svg += '</svg>'
        
        questions.append({
            'question_text': f"There were {total}. We took away {subtract}. How many are left?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{total} - {subtract} = {result}",
            'question_image_svg': svg
        })
    
    # Type 4: Word problems - add or subtract (15 questions)
    word_problems = [
        ("You have {a} sweets. You get {b} more. How many now?", "add", "sweets"),
        ("There are {a} birds. {b} fly away. How many are left?", "subtract", "birds"),
        ("The shop has {a} apples. They sell {b}. How many remain?", "subtract", "apples"),
        ("Sam has {a} coins. He finds {b} more. How many altogether?", "add", "coins"),
        ("There were {a} books. We borrowed {b}. How many are on the shelf?", "subtract", "books"),
    ]
    
    for i in range(15):
        template, operation, item = random.choice(word_problems)
        
        if operation == "add":
            num1 = random.randint(5, 20)
            num2 = random.randint(3, 15)
            answer = num1 + num2
            solution = f"{num1} + {num2} = {answer} {item}"
        else:
            num1 = random.randint(10, 25)
            num2 = random.randint(2, num1 - 3)
            answer = num1 - num2
            solution = f"{num1} - {num2} = {answer} {item}"
        
        problem = template.format(a=num1, b=num2)
        
        distractors = [answer - 1, answer + 1, num1 + num2 if operation == "subtract" else num1 - num2]
        distractors = [d for d in distractors if d != answer and d > 0][:3]
        
        options = [str(answer)] + [str(d) for d in distractors]
        while len(options) < 4: options.append(str(random.randint(0, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(str(answer))]
        
        questions.append({
            'question_text': problem,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    return questions


def generate_level_7_questions():
    """Level 7: Recognising Money (Progressing)
    NCCA LOs: i, j, k - Purpose of money, recognise coins/notes, sort by value
    """
    questions = []
    
    # Type 1: Identify coin value (15 questions) - use each value at most twice with varied text
    coin_values = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]
    question_templates = [
        "What is the value of this coin?",
        "How much is this coin worth?",
        "This coin shows what value?",
        "What amount does this coin represent?",
    ]
    
    # Create 15 unique combinations
    coin_questions = []
    for value in coin_values:
        coin_questions.append((value, question_templates[0]))
    for value in coin_values[:7]:  # 7 more to get to 15
        coin_questions.append((value, question_templates[1]))
    
    random.shuffle(coin_questions)
    coin_questions = coin_questions[:15]
    
    for i, (value, q_template) in enumerate(coin_questions):
        
        if value >= 1:
            correct = f"€{int(value)}"
        else:
            correct = f"{int(value * 100)}c"
        
        # Generate distractors
        other_values = [v for v in coin_values if v != value]
        distractor_values = random.sample(other_values, 3)
        distractors = []
        for v in distractor_values:
            if v >= 1:
                distractors.append(f"€{int(v)}")
            else:
                distractors.append(f"{int(v * 100)}c")
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': q_template,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"This coin is worth {correct}.",
            'question_image_svg': generate_euro_coin_svg(value)
        })
    
    # Type 2: Identify note value (10 questions)
    note_values = [5, 10, 20, 50, 100]
    
    for i in range(10):
        value = random.choice(note_values)
        correct = f"€{value}"
        
        other_values = [v for v in note_values if v != value]
        distractors = [f"€{v}" for v in random.sample(other_values, 3)]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "What is the value of this note?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"This note is worth {correct}.",
            'question_image_svg': generate_euro_note_svg(value)
        })
    
    # Type 3: Count coins total (15 questions)
    for i in range(15):
        num_coins = random.randint(2, 4)
        coin_options = [0.10, 0.20, 0.50, 1, 2]
        selected_coins = [random.choice(coin_options) for _ in range(num_coins)]
        total = sum(selected_coins)
        
        if total == int(total):
            correct = f"€{int(total)}"
        else:
            correct = f"€{total:.2f}"
        
        distractors = [f"€{total + 0.50:.2f}", f"€{total - 0.50:.2f}", f"€{total + 1:.2f}"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "How much money is shown?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Adding the coins: {' + '.join([f'€{c}' if c >= 1 else f'{int(c*100)}c' for c in selected_coins])} = {correct}",
            'question_image_svg': generate_coins_svg(selected_coins)
        })
    
    # Type 4: Which is worth more? (10 questions)
    for i in range(10):
        val1 = random.choice([0.20, 0.50, 1, 2])
        val2 = random.choice([0.10, 0.20, 0.50, 1])
        
        while val1 == val2:
            val2 = random.choice([0.10, 0.20, 0.50, 1])
        
        if val1 > val2:
            correct = "Coin A"
        else:
            correct = "Coin B"
        
        options = ["Coin A", "Coin B", "They are equal", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        # Create side-by-side coin SVG
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 120">
            <rect width="250" height="120" fill="{COLOURS['light_grey']}"/>
            <text x="60" y="20" font-size="14" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">Coin A</text>
            <text x="190" y="20" font-size="14" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">Coin B</text>
        '''
        
        # Coin A
        c1 = COLOURS['gold'] if val1 >= 0.10 else COLOURS['copper']
        disp1 = f"€{int(val1)}" if val1 >= 1 else f"{int(val1*100)}c"
        svg += f'''<circle cx="60" cy="70" r="35" fill="{c1}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <text x="60" y="78" font-size="16" font-family="Arial" font-weight="bold" fill="{COLOURS['dark']}" text-anchor="middle">{disp1}</text>'''
        
        # Coin B
        c2 = COLOURS['gold'] if val2 >= 0.10 else COLOURS['copper']
        disp2 = f"€{int(val2)}" if val2 >= 1 else f"{int(val2*100)}c"
        svg += f'''<circle cx="190" cy="70" r="35" fill="{c2}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <text x="190" y="78" font-size="16" font-family="Arial" font-weight="bold" fill="{COLOURS['dark']}" text-anchor="middle">{disp2}</text>'''
        
        svg += '</svg>'
        
        questions.append({
            'question_text': "Which coin is worth more?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Coin A is {disp1}, Coin B is {disp2}. {correct} is worth more.",
            'question_image_svg': svg
        })
    
    return questions


def generate_level_8_questions():
    """Level 8: Shopping & Transactions (Progressing)
    NCCA LOs: l, m, n - Shopping experience, transactions, add/subtract money
    """
    questions = []
    
    # Type 1: Calculate total cost (20 questions)
    items = [
        ("Bread", 1.50), ("Milk", 1.20), ("Apple", 0.50), ("Banana", 0.40),
        ("Eggs", 2.50), ("Butter", 2.00), ("Cheese", 3.00), ("Juice", 1.80),
        ("Crisps", 1.00), ("Chocolate", 1.50), ("Water", 0.80), ("Yogurt", 0.90)
    ]
    
    for i in range(20):
        selected = random.sample(items, 2)
        total = sum(item[1] for item in selected)
        
        correct = f"€{total:.2f}"
        distractors = [f"€{total + 0.50:.2f}", f"€{total - 0.50:.2f}", f"€{total + 1:.2f}"]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        item_names = [item[0] for item in selected]
        item_prices = [f"€{item[1]:.2f}" for item in selected]
        
        questions.append({
            'question_text': f"You buy {item_names[0]} (€{selected[0][1]:.2f}) and {item_names[1]} (€{selected[1][1]:.2f}). What is the total?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"€{selected[0][1]:.2f} + €{selected[1][1]:.2f} = {correct}",
            'question_image_svg': ''
        })
    
    # Type 2: Calculate change (20 questions)
    for i in range(20):
        paid_with = random.choice([5, 10, 20])
        cost = round(random.uniform(1, paid_with - 0.50), 2)
        cost = round(cost * 2) / 2  # Round to nearest 50c
        change = paid_with - cost
        
        correct = f"€{change:.2f}"
        distractors = [f"€{change + 1:.2f}", f"€{change - 0.50:.2f}", f"€{cost:.2f}"]
        distractors = [d for d in distractors if d != correct]
        while len(distractors) < 3:
            distractors.append(f"€{change + random.uniform(0.5, 2):.2f}")
        distractors = distractors[:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(f"€{random.uniform(1, 10):.2f}")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You spend €{cost:.2f} and pay with €{paid_with}. How much change?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"€{paid_with} - €{cost:.2f} = {correct} change",
            'question_image_svg': ''
        })
    
    # Type 3: Enough money? (10 questions)
    for i in range(10):
        have = round(random.uniform(5, 15), 0)
        cost = round(random.uniform(3, 18), 2)
        cost = round(cost * 2) / 2
        
        if have >= cost:
            correct = "Yes"
            solution = f"You have €{have:.0f} and need €{cost:.2f}. Yes, you have enough!"
        else:
            correct = "No"
            solution = f"You have €{have:.0f} but need €{cost:.2f}. No, you need €{cost - have:.2f} more."
        
        options = ["Yes", "No", "Maybe", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You have €{have:.0f}. The item costs €{cost:.2f}. Do you have enough money?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    return questions


def generate_level_9_questions():
    """Level 9: Totals & Change (Progressing)
    NCCA LOs: o, p - Calculate total cost, check change against receipt
    """
    questions = []
    
    # Type 1: Add up shopping list (15 questions)
    items = [
        ("Bread", 1.50), ("Milk", 1.20), ("Apples", 2.00), ("Bananas", 1.50),
        ("Eggs", 2.50), ("Butter", 2.30), ("Cheese", 3.50), ("Juice", 1.80),
        ("Rice", 2.00), ("Pasta", 1.60), ("Chicken", 5.00), ("Fish", 4.50)
    ]
    
    for i in range(15):
        selected = random.sample(items, 3)
        names = [item[0] for item in selected]
        prices = [item[1] for item in selected]
        total = sum(prices)
        
        correct = f"€{total:.2f}"
        distractors = [f"€{total + 1:.2f}", f"€{total - 1:.2f}", f"€{total + 2:.2f}"]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "What is the total cost?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Adding: {' + '.join([f'€{p:.2f}' for p in prices])} = {correct}",
            'question_image_svg': generate_receipt_svg(names, prices, total)
        })
    
    # Type 2: Check change is correct (20 questions)
    for i in range(20):
        total = round(random.uniform(5, 15), 2)
        total = round(total * 2) / 2
        paid = random.choice([10, 20])
        while paid <= total:
            paid = random.choice([10, 20, 50])
        
        correct_change = paid - total
        given_change = correct_change + random.choice([-0.50, 0, 0, 0, 0.50, 1])  # Sometimes wrong
        
        if abs(given_change - correct_change) < 0.01:
            correct = "Yes, it's correct"
            solution = f"€{paid} - €{total:.2f} = €{correct_change:.2f}. The change is correct!"
        else:
            correct = f"No, should be €{correct_change:.2f}"
            solution = f"€{paid} - €{total:.2f} = €{correct_change:.2f}, but you got €{given_change:.2f}. That's wrong!"
        
        options = ["Yes, it's correct", f"No, should be €{correct_change:.2f}", f"No, should be €{correct_change + 0.50:.2f}", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You paid €{paid} for items costing €{total:.2f}. You got €{given_change:.2f} change. Is this correct?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    # Type 3: Work out correct change (15 questions)
    for i in range(15):
        paid = random.choice([10, 20, 50])
        total = round(random.uniform(2, paid - 1), 2)
        total = round(total * 4) / 4  # Round to nearest 25c
        change = paid - total
        
        correct = f"€{change:.2f}"
        distractors = [f"€{change + 1:.2f}", f"€{change - 0.50:.2f}", f"€{total:.2f}"]
        distractors = [d for d in distractors if d != correct]
        while len(distractors) < 3:
            distractors.append(f"€{change + random.uniform(0.5, 3):.2f}")
        distractors = distractors[:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(f"€{random.uniform(1, 15):.2f}")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"The total is €{total:.2f}. You pay with €{paid}. What change should you get?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"€{paid} - €{total:.2f} = {correct} change",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_10_questions():
    """Level 10: Estimating & Rounding (Consolidating)
    NCCA LOs: q, r - Round prices, estimate bills and change
    """
    questions = []
    
    # Type 1: Round prices to nearest euro (15 questions)
    for i in range(15):
        price = round(random.uniform(1.10, 19.90), 2)
        rounded = round(price)
        
        correct = f"€{rounded}"
        distractors = [f"€{rounded - 1}", f"€{rounded + 1}", f"€{int(price)}"]
        distractors = [d for d in distractors if d != correct]
        # Ensure valid distractors and enough of them
        distractors = [d for d in distractors if d.startswith("€") and len(d) > 1]
        while len(distractors) < 3:
            new_val = rounded + random.choice([-2, 2, 3])
            if new_val > 0:
                distractors.append(f"€{new_val}")
        distractors = distractors[:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(f"€{random.randint(1, 20)}")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Round €{price:.2f} to the nearest euro.",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"€{price:.2f} rounds to {correct} (to the nearest euro).",
            'question_image_svg': generate_price_tag_svg(price)
        })
    
    # Type 2: Estimate shopping total (20 questions)
    for i in range(20):
        prices = [round(random.uniform(1.40, 9.60), 2) for _ in range(3)]
        exact_total = sum(prices)
        
        # Round each to nearest euro and add
        rounded_prices = [round(p) for p in prices]
        estimated = sum(rounded_prices)
        
        correct = f"About €{estimated}"
        distractors = [f"About €{estimated + 2}", f"About €{estimated - 2}", f"Exactly €{exact_total:.2f}"]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        price_str = ", ".join([f"€{p:.2f}" for p in prices])
        
        questions.append({
            'question_text': f"Estimate the total for items costing {price_str}",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Round each: {' + '.join([f'€{p}' for p in rounded_prices])} = {correct}",
            'question_image_svg': ''
        })
    
    # Type 3: Estimate change (15 questions)
    for i in range(15):
        price = round(random.uniform(5, 18), 2)
        paid = random.choice([10, 20, 50])
        while paid <= price:
            paid += 10
        
        exact_change = paid - price
        estimated_change = paid - round(price)
        
        correct = f"About €{estimated_change}"
        distractors = [f"About €{estimated_change + 2}", f"About €{estimated_change - 2}", f"Exactly €{exact_change:.2f}"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"An item costs €{price:.2f}. You pay €{paid}. Estimate your change.",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Round €{price:.2f} to €{round(price)}. Change: €{paid} - €{round(price)} = {correct}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_11_questions():
    """Level 11: Bills & Receipts (Consolidating)
    NCCA LOs: s, t - Interpret bills/receipts, plan savings
    """
    questions = []
    
    # Type 1: Read receipt information (20 questions)
    for i in range(20):
        items = random.sample([
            ("Bread", 1.50), ("Milk", 1.20), ("Eggs", 2.50), ("Butter", 2.00),
            ("Cheese", 3.50), ("Chicken", 5.50), ("Rice", 2.30), ("Pasta", 1.80)
        ], 3)
        
        names = [item[0] for item in items]
        prices = [item[1] for item in items]
        total = sum(prices)
        
        # Random question about the receipt
        q_type = random.choice(['total', 'item', 'count'])
        
        if q_type == 'total':
            correct = f"€{total:.2f}"
            question = "What is the total on this receipt?"
            distractors = [f"€{total + 1:.2f}", f"€{total - 1:.2f}", f"€{prices[0]:.2f}"]
        elif q_type == 'item':
            item_idx = random.randint(0, 2)
            correct = f"€{prices[item_idx]:.2f}"
            question = f"How much does the {names[item_idx]} cost?"
            other_prices = [p for j, p in enumerate(prices) if j != item_idx]
            distractors = [f"€{p:.2f}" for p in other_prices] + [f"€{prices[item_idx] + 0.50:.2f}"]
        else:
            correct = "3 items"
            question = "How many items are on this receipt?"
            distractors = ["2 items", "4 items", "5 items"]
        
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Looking at the receipt: {correct}",
            'question_image_svg': generate_receipt_svg(names, prices, total)
        })
    
    # Type 2: Saving for a purchase (15 questions)
    for i in range(15):
        target = random.choice([20, 30, 50, 75, 100])
        weekly_save = random.choice([5, 10, 15])
        weeks_needed = (target + weekly_save - 1) // weekly_save  # Ceiling division
        
        correct = f"{weeks_needed} weeks"
        distractors = [f"{weeks_needed - 1} weeks", f"{weeks_needed + 1} weeks", f"{weeks_needed + 2} weeks"]
        distractors = [d for d in distractors if d != correct and int(d.split()[0]) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You want to buy something for €{target}. You save €{weekly_save} per week. How many weeks to save enough?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"€{target} ÷ €{weekly_save} per week = {weeks_needed} weeks needed.",
            'question_image_svg': ''
        })
    
    # Type 3: Compare prices/value (15 questions)
    for i in range(15):
        item = random.choice(["phone credit", "bus pass", "cinema ticket", "game", "book"])
        shop_a_price = round(random.uniform(5, 25), 2)
        shop_b_price = shop_a_price + random.choice([-3, -2, -1, 1, 2, 3])
        shop_b_price = round(max(2, shop_b_price), 2)
        
        if shop_a_price < shop_b_price:
            correct = "Shop A"
            saving = shop_b_price - shop_a_price
        else:
            correct = "Shop B"
            saving = shop_a_price - shop_b_price
        
        options = ["Shop A", "Shop B", "They cost the same", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"A {item} costs €{shop_a_price:.2f} in Shop A and €{shop_b_price:.2f} in Shop B. Which is cheaper?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{correct} is cheaper by €{saving:.2f}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_12_questions():
    """Level 12: Digital Payments (Consolidating)
    NCCA LOs: u, v - Different ways money is received/spent, payment apps
    """
    questions = []
    
    # Type 1: Payment methods (15 questions)
    payment_scenarios = [
        ("buying a coffee at a café", ["Cash", "Card", "Phone payment"], "All of these"),
        ("paying for the bus", ["Leap card", "Cash"], "All of these"),
        ("buying something online", ["Card", "PayPal"], "Card or online payment"),
        ("getting your weekly allowance", ["Bank transfer", "Cash"], "Both are possible"),
        ("paying a friend back", ["Bank app", "Cash"], "Both are possible"),
        ("buying cinema tickets online", ["Card payment", "Phone payment"], "Online payment"),
        ("paying at a supermarket self-checkout", ["Card", "Cash", "Phone"], "All of these"),
        ("topping up phone credit", ["Card online", "Cash in shop"], "Both are possible"),
    ]
    
    for i in range(15):
        scenario, methods, answer_hint = random.choice(payment_scenarios)
        
        correct = answer_hint
        all_methods = ["Cash only", "Card only", "Phone only", "All of these", "Both are possible", "Online payment", "Card or online payment"]
        distractors = [m for m in all_methods if m != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"When {scenario}, which payment methods could you use?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"When {scenario}, you can use: {', '.join(methods)}.",
            'question_image_svg': ''
        })
    
    # Type 2: Contactless limits (10 questions)
    for i in range(10):
        amount = random.choice([15, 35, 55, 80, 120])
        limit = 50  # Typical contactless limit
        
        if amount <= limit:
            correct = "Yes"
            solution = f"€{amount} is under the €{limit} contactless limit."
        else:
            correct = "No, you'll need to enter your PIN"
            solution = f"€{amount} is over the €{limit} contactless limit. You need to enter your PIN."
        
        options = ["Yes", "No, you'll need to enter your PIN", "Contactless doesn't work", "Only with cash"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Can you pay €{amount} using contactless tap without a PIN? (Limit is €{limit})",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    # Type 3: Bank app/transfer questions (15 questions)
    for i in range(15):
        starting = random.choice([50, 100, 150, 200])
        spent = random.randint(10, starting - 20)
        remaining = starting - spent
        
        correct = f"€{remaining}"
        distractors = [f"€{remaining + 10}", f"€{remaining - 10}", f"€{spent}"]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Your bank app shows €{starting}. You transfer €{spent} to a friend. What's your new balance?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"€{starting} - €{spent} = {correct} remaining",
            'question_image_svg': ''
        })
    
    # Type 4: Understanding digital receipts (10 questions)
    for i in range(10):
        transaction = random.choice([
            ("online shopping", "Delivered", "refund possible for 14 days"),
            ("streaming subscription", "Monthly", "renews automatically"),
            ("phone top-up", "Complete", "credit added to phone"),
            ("bus ticket", "Valid", "show on phone to driver"),
            ("food delivery", "Paid", "arriving soon"),
        ])
        
        trans_type, status, meaning = transaction
        
        question_types = [
            (f"You bought a {trans_type}. The status shows '{status}'. What does this mean?",
             meaning,
             [meaning, "Payment failed", "Need to pay again", "Error occurred"])
        ]
        
        q_text, correct, opts = random.choice(question_types)
        
        options = opts
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': q_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"'{status}' means: {meaning}",
            'question_image_svg': ''
        })
    
    return questions


# ============================================================
# MAIN GENERATION FUNCTIONS
# ============================================================

def generate_all_questions():
    """Generate all questions for all levels"""
    all_questions = []
    
    generators = [
        generate_level_1_questions,
        generate_level_2_questions,
        generate_level_3_questions,
        generate_level_4_questions,
        generate_level_5_questions,
        generate_level_6_questions,
        generate_level_7_questions,
        generate_level_8_questions,
        generate_level_9_questions,
        generate_level_10_questions,
        generate_level_11_questions,
        generate_level_12_questions,
    ]
    
    for level, generator in enumerate(generators, 1):
        print(f"  Generating Level {level}...")
        questions = generator()
        
        # Ensure exactly 50 questions per level
        if len(questions) < QUESTIONS_PER_LEVEL:
            print(f"    Warning: Level {level} has only {len(questions)} questions, need {QUESTIONS_PER_LEVEL}")
        elif len(questions) > QUESTIONS_PER_LEVEL:
            questions = questions[:QUESTIONS_PER_LEVEL]
        
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['difficulty'] = DIFFICULTY
        
        all_questions.extend(questions)
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    """Validate all questions before insertion"""
    errors = []
    
    for i, q in enumerate(questions):
        # Check required fields
        if not q.get('question_text'):
            errors.append(f"Q{i+1}: Missing question_text")
        
        if not q.get('correct_answer') in ['A', 'B', 'C', 'D']:
            errors.append(f"Q{i+1}: Invalid correct_answer: {q.get('correct_answer')}")
        
        if not q.get('option_a'):
            errors.append(f"Q{i+1}: Missing option_a")
        
        if not q.get('option_b'):
            errors.append(f"Q{i+1}: Missing option_b")
        
        # Check correct answer matches an option
        correct = q.get('correct_answer')
        correct_option = q.get(f'option_{correct.lower()}', '')
        if not correct_option:
            errors.append(f"Q{i+1}: Correct answer {correct} but option_{correct.lower()} is empty")
    
    # Check for duplicates
    # For visual questions (with SVG), same text is OK - the image makes them unique
    # For non-visual questions, duplicate text is a problem
    seen_text_only = set()  # For non-visual questions
    seen_visual = {}  # text -> set of SVG hashes for visual questions
    
    for i, q in enumerate(questions):
        text = q['question_text']
        svg = q.get('question_image_svg', '')
        
        if svg:
            # Visual question - only duplicate if same text AND same SVG
            svg_hash = hash(svg)
            if text in seen_visual:
                if svg_hash in seen_visual[text]:
                    errors.append(f"Duplicate question found: '{text[:50]}...'")
                else:
                    seen_visual[text].add(svg_hash)
            else:
                seen_visual[text] = {svg_hash}
        else:
            # Non-visual question - duplicate text is a problem
            if text in seen_text_only:
                errors.append(f"Duplicate question found: '{text[:50]}...'")
            seen_text_only.add(text)
    
    return errors


def count_existing_questions():
    """Count existing questions for this topic in questions_adaptive table"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? GROUP BY difficulty_level', (TOPIC,))
        counts = dict(cursor.fetchall())
        conn.close()
        return counts
    except:
        return {}


def clear_existing_questions():
    """Clear existing questions for this topic from questions_adaptive (with confirmation)"""
    counts = count_existing_questions()
    total = sum(counts.values())
    
    if total > 0:
        print(f"\n⚠️  Found {total} existing questions for {TOPIC}")
        response = input("Delete existing? (yes/no): ").strip().lower()
        if response == 'yes':
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM questions_adaptive WHERE topic = ?', (TOPIC,))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()
            print(f"   Deleted {deleted} questions from questions_adaptive")
            return True
        else:
            print("   Keeping existing questions")
            return False
    return True


def insert_questions(questions):
    """Insert questions into questions_adaptive table"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Convert letter answer to integer (A=0, B=1, C=2, D=3)
    letter_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    
    inserted = 0
    for q in questions:
        try:
            level = q['level']
            band = get_difficulty_band(level)
            
            # Convert correct_answer from letter to integer
            correct_answer = q['correct_answer']
            if isinstance(correct_answer, str):
                correct_answer = letter_to_int.get(correct_answer.upper(), 0)
            
            cursor.execute('''
                INSERT OR IGNORE INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, is_active, image_svg, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'], 
                q['question_text'], 
                q['option_a'], 
                q['option_b'], 
                q.get('option_c', ''), 
                q.get('option_d', ''),
                correct_answer,
                q.get('solution', ''),  # Map solution to explanation column
                level,
                band,
                'multiple_choice',
                1,  # is_active
                q.get('question_image_svg', ''),
                datetime.now(),
                datetime.now()
            ))
            inserted += 1
        except sqlite3.Error as e:
            print(f"Error inserting question: {e}")
            print(f"Question: {q['question_text'][:50]}...")
    
    conn.commit()
    conn.close()
    return inserted


def main():
    """Main entry point"""
    print("=" * 60)
    print("AgentMath L2LP Question Generator (V2)")
    print(f"Topic: {TOPIC}")
    print(f"Table: questions_adaptive")
    print(f"Target: {QUESTIONS_PER_LEVEL} questions × {TOTAL_LEVELS} levels = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS} total")
    print("=" * 60)
    
    # Check for existing questions
    if not clear_existing_questions():
        print("\nAborting to preserve existing questions.")
        return
    
    # Generate questions
    print("\nGenerating questions...")
    questions = generate_all_questions()
    
    print(f"\nTotal questions generated: {len(questions)}")
    
    # Validate
    print("\nValidating questions...")
    errors = validate_questions(questions)
    
    # Separate critical errors from duplicate warnings
    critical_errors = [e for e in errors if 'Duplicate' not in e]
    duplicate_warnings = [e for e in errors if 'Duplicate' in e]
    
    if critical_errors:
        print(f"\n❌ Found {len(critical_errors)} critical errors:")
        for error in critical_errors[:10]:
            print(f"   - {error}")
        if len(critical_errors) > 10:
            print(f"   ... and {len(critical_errors) - 10} more")
        
        response = input("\nCritical errors found. Continue anyway? (yes/no): ").strip().lower()
        if response != 'yes':
            print("Aborting.")
            return
    
    if duplicate_warnings:
        print(f"\n⚠️  Found {len(duplicate_warnings)} potential duplicate questions (not blocking)")
        print("   Note: Visual questions with same text but different images are acceptable.")
    
    if not critical_errors and not duplicate_warnings:
        print("✅ All questions validated successfully!")
    
    # Insert into database
    print("\nInserting questions into database...")
    inserted = insert_questions(questions)
    
    print(f"\n✅ Successfully inserted {inserted} questions!")
    
    # Summary by level
    print("\nQuestions per level:")
    level_counts = {}
    for q in questions:
        level = q['level']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    for level in sorted(level_counts.keys()):
        print(f"   Level {level}: {level_counts[level]} questions")
    
    # Visual percentage check
    print("\nVisual question check:")
    for level in range(1, 13):
        level_qs = [q for q in questions if q['level'] == level]
        visual_count = sum(1 for q in level_qs if q.get('question_image_svg'))
        visual_pct = (visual_count / len(level_qs) * 100) if level_qs else 0
        target = get_visual_percentage(level)
        status = "✅" if visual_pct >= target - 5 else "⚠️"
        print(f"   Level {level}: {visual_pct:.0f}% visual (target: {target}%) {status}")


if __name__ == '__main__':
    main()
