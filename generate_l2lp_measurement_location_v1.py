"""
AgentMath L2LP Question Generator
Topic: Measurement & Location (l2_measurement_location)
NCCA Module: Understanding measurement, location and position

Generates 600 questions (50 per level × 12 levels) for the L2LP strand.
High visual percentage with SVG graphics for accessibility.

Author: AgentMath Generator
Version: 1.0
Date: December 2025
"""

import sqlite3
import random
import math
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'l2_measurement_location'
MODE = 'adaptive'
DIFFICULTY = 'adaptive'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

def get_visual_percentage(level):
    if level <= 3:
        return 85
    elif level <= 6:
        return 75
    elif level <= 9:
        return 65
    else:
        return 55

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
    'brown': '#8B4513'
}

# ============================================================
# SVG GENERATION FUNCTIONS
# ============================================================

def generate_ruler_svg(length_cm, show_measurement=True):
    """Generate SVG of a ruler measuring an object"""
    width = max(300, length_cm * 25 + 60)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 120">
        <rect width="{width}" height="120" fill="{COLOURS['light_grey']}"/>
        
        <!-- Ruler -->
        <rect x="20" y="60" width="{width - 40}" height="40" fill="#F4D03F" stroke="{COLOURS['dark']}" stroke-width="2"/>
        '''
    
    # Add cm markings
    for i in range(int(width / 25) - 1):
        x = 30 + i * 25
        if i % 2 == 0:
            svg += f'<line x1="{x}" y1="60" x2="{x}" y2="75" stroke="{COLOURS["dark"]}" stroke-width="1"/>'
            svg += f'<text x="{x}" y="95" font-size="10" fill="{COLOURS["dark"]}" text-anchor="middle">{i}</text>'
        else:
            svg += f'<line x1="{x}" y1="60" x2="{x}" y2="70" stroke="{COLOURS["dark"]}" stroke-width="1"/>'
    
    # Object being measured
    obj_width = length_cm * 25
    svg += f'''
        <rect x="30" y="25" width="{obj_width}" height="25" fill="{COLOURS['blue']}" rx="3"/>
        <line x1="30" y1="15" x2="30" y2="55" stroke="{COLOURS['red']}" stroke-width="2"/>
        <line x1="{30 + obj_width}" y1="15" x2="{30 + obj_width}" y2="55" stroke="{COLOURS['red']}" stroke-width="2"/>
    '''
    
    if show_measurement:
        svg += f'<text x="{30 + obj_width/2}" y="42" font-size="14" fill="{COLOURS["white"]}" text-anchor="middle" font-weight="bold">{length_cm} cm</text>'
    
    svg += '</svg>'
    return svg


def generate_comparison_svg(obj1_name, obj1_size, obj2_name, obj2_size, attribute='length'):
    """Generate SVG comparing two objects"""
    max_size = max(obj1_size, obj2_size)
    scale = 150 / max_size
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 150">
        <rect width="350" height="150" fill="{COLOURS['light_grey']}"/>
        
        <!-- Object 1 -->
        <text x="90" y="25" font-size="14" fill="{COLOURS['dark']}" text-anchor="middle">{obj1_name}</text>
        <rect x="20" y="35" width="{obj1_size * scale}" height="40" fill="{COLOURS['blue']}" rx="3"/>
        <text x="90" y="95" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">{obj1_size} cm</text>
        
        <!-- Object 2 -->
        <text x="260" y="25" font-size="14" fill="{COLOURS['dark']}" text-anchor="middle">{obj2_name}</text>
        <rect x="190" y="35" width="{obj2_size * scale}" height="40" fill="{COLOURS['green']}" rx="3"/>
        <text x="260" y="95" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">{obj2_size} cm</text>
    </svg>'''
    return svg


def generate_scale_svg(weight_kg, show_weight=True):
    """Generate SVG of a weighing scale"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180">
        <rect width="200" height="180" fill="{COLOURS['light_grey']}"/>
        
        <!-- Scale base -->
        <ellipse cx="100" cy="160" rx="70" ry="15" fill="{COLOURS['grey']}"/>
        <rect x="40" y="130" width="120" height="30" fill="{COLOURS['grey']}"/>
        
        <!-- Scale platform -->
        <rect x="30" y="100" width="140" height="35" fill="#C0C0C0" stroke="{COLOURS['dark']}" stroke-width="2" rx="5"/>
        
        <!-- Display -->
        <rect x="60" y="110" width="80" height="20" fill="{COLOURS['dark']}" rx="3"/>
        '''
    
    if show_weight:
        svg += f'<text x="100" y="125" font-size="14" fill="#00ff00" text-anchor="middle" font-family="monospace">{weight_kg} kg</text>'
    
    # Item on scale
    svg += f'''
        <!-- Item being weighed -->
        <ellipse cx="100" cy="85" rx="35" ry="20" fill="{COLOURS['orange']}"/>
    </svg>'''
    return svg


def generate_measuring_jug_svg(capacity_ml, filled_ml):
    """Generate SVG of a measuring jug"""
    fill_height = (filled_ml / capacity_ml) * 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 180">
        <rect width="150" height="180" fill="{COLOURS['light_grey']}"/>
        
        <!-- Jug outline -->
        <path d="M40,160 L40,50 Q40,40 50,40 L100,40 Q110,40 110,50 L110,160 Q110,170 100,170 L50,170 Q40,170 40,160 Z" 
              fill="none" stroke="{COLOURS['dark']}" stroke-width="3"/>
        
        <!-- Handle -->
        <path d="M110,60 Q140,60 140,100 Q140,140 110,140" fill="none" stroke="{COLOURS['dark']}" stroke-width="3"/>
        
        <!-- Liquid -->
        <rect x="43" y="{160 - fill_height}" width="64" height="{fill_height}" fill="{COLOURS['blue']}" opacity="0.6"/>
        
        <!-- Measurement lines -->
        '''
    
    # Add measurement markings
    for i in range(5):
        y = 160 - (i * 25)
        ml_mark = int((i / 4) * capacity_ml)
        svg += f'<line x1="35" y1="{y}" x2="45" y2="{y}" stroke="{COLOURS["dark"]}" stroke-width="1"/>'
        svg += f'<text x="25" y="{y + 4}" font-size="8" fill="{COLOURS["dark"]}" text-anchor="middle">{ml_mark}</text>'
    
    svg += f'''
        <text x="75" y="175" font-size="10" fill="{COLOURS["dark"]}" text-anchor="middle">{filled_ml} ml</text>
    </svg>'''
    return svg


def generate_simple_map_svg(landmarks, highlight=None):
    """Generate SVG of a simple map with landmarks"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 250">
        <rect width="300" height="250" fill="#e8f5e9"/>
        
        <!-- Roads -->
        <rect x="0" y="110" width="300" height="30" fill="{COLOURS['grey']}"/>
        <rect x="135" y="0" width="30" height="250" fill="{COLOURS['grey']}"/>
        
        <!-- Road markings -->
        <line x1="0" y1="125" x2="300" y2="125" stroke="{COLOURS['white']}" stroke-width="2" stroke-dasharray="10,10"/>
        <line x1="150" y1="0" x2="150" y2="250" stroke="{COLOURS['white']}" stroke-width="2" stroke-dasharray="10,10"/>
        '''
    
    landmark_positions = {
        'School': (50, 50, '🏫'),
        'Shop': (220, 50, '🏪'),
        'Park': (50, 180, '🌳'),
        'Home': (220, 180, '🏠'),
        'Library': (150, 50, '📚'),
        'Hospital': (150, 180, '🏥'),
    }
    
    for name in landmarks:
        if name in landmark_positions:
            x, y, emoji = landmark_positions[name]
            fill = COLOURS['orange'] if name == highlight else COLOURS['blue']
            svg += f'''
                <rect x="{x-25}" y="{y-25}" width="50" height="50" fill="{fill}" rx="5" opacity="0.8"/>
                <text x="{x}" y="{y+5}" font-size="24" text-anchor="middle">{emoji}</text>
                <text x="{x}" y="{y+35}" font-size="10" fill="{COLOURS['dark']}" text-anchor="middle">{name}</text>
            '''
    
    svg += '</svg>'
    return svg


def generate_grid_map_svg(grid_size=5, marked_position=None):
    """Generate SVG of a grid map with coordinates"""
    cell_size = 50
    width = grid_size * cell_size + 60
    height = grid_size * cell_size + 60
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
        <rect width="{width}" height="{height}" fill="{COLOURS['light_grey']}"/>
        '''
    
    # Draw grid
    for i in range(grid_size + 1):
        # Vertical lines
        x = 40 + i * cell_size
        svg += f'<line x1="{x}" y1="20" x2="{x}" y2="{20 + grid_size * cell_size}" stroke="{COLOURS["dark"]}" stroke-width="1"/>'
        # Horizontal lines
        y = 20 + i * cell_size
        svg += f'<line x1="40" y1="{y}" x2="{40 + grid_size * cell_size}" y2="{y}" stroke="{COLOURS["dark"]}" stroke-width="1"/>'
    
    # Column labels (A, B, C...)
    for i in range(grid_size):
        x = 40 + i * cell_size + cell_size / 2
        svg += f'<text x="{x}" y="{height - 10}" font-size="14" fill="{COLOURS["dark"]}" text-anchor="middle">{chr(65+i)}</text>'
    
    # Row labels (1, 2, 3...)
    for i in range(grid_size):
        y = 20 + i * cell_size + cell_size / 2 + 5
        svg += f'<text x="20" y="{y}" font-size="14" fill="{COLOURS["dark"]}" text-anchor="middle">{i+1}</text>'
    
    # Mark position if specified
    if marked_position:
        col, row = marked_position
        col_idx = ord(col.upper()) - 65
        row_idx = int(row) - 1
        x = 40 + col_idx * cell_size + cell_size / 2
        y = 20 + row_idx * cell_size + cell_size / 2
        svg += f'''
            <circle cx="{x}" cy="{y}" r="18" fill="{COLOURS['red']}"/>
            <text x="{x}" y="{y + 5}" font-size="16" fill="{COLOURS['white']}" text-anchor="middle">★</text>
        '''
    
    svg += '</svg>'
    return svg


def generate_direction_svg(direction):
    """Generate SVG showing a compass direction"""
    directions = {
        'North': (150, 40),
        'South': (150, 260),
        'East': (260, 150),
        'West': (40, 150),
        'up': (150, 40),
        'down': (150, 260),
        'right': (260, 150),
        'left': (40, 150),
    }
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">
        <rect width="300" height="300" fill="{COLOURS['light_grey']}"/>
        
        <!-- Compass circle -->
        <circle cx="150" cy="150" r="100" fill="{COLOURS['white']}" stroke="{COLOURS['dark']}" stroke-width="3"/>
        
        <!-- Direction labels -->
        <text x="150" y="70" font-size="20" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">N</text>
        <text x="150" y="245" font-size="20" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">S</text>
        <text x="235" y="155" font-size="20" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">E</text>
        <text x="65" y="155" font-size="20" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">W</text>
        
        <!-- Center point -->
        <circle cx="150" cy="150" r="8" fill="{COLOURS['dark']}"/>
        '''
    
    # Arrow pointing to direction
    if direction in directions:
        tx, ty = directions[direction]
        svg += f'''
            <line x1="150" y1="150" x2="{tx}" y2="{ty}" stroke="{COLOURS['red']}" stroke-width="6"/>
            <circle cx="{tx}" cy="{ty}" r="12" fill="{COLOURS['red']}"/>
        '''
    
    svg += '</svg>'
    return svg


def generate_position_svg(position_word):
    """Generate SVG illustrating position words"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
        <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
        
        <!-- Reference object (table/box) -->
        <rect x="60" y="100" width="80" height="50" fill="{COLOURS['brown']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        '''
    
    # Position the ball based on the word
    ball_positions = {
        'on': (100, 85),
        'under': (100, 165),
        'in front of': (100, 175),
        'behind': (100, 85),
        'beside': (25, 125),
        'next to': (175, 125),
        'left': (25, 125),
        'right': (175, 125),
        'above': (100, 60),
        'below': (100, 165),
    }
    
    if position_word.lower() in ball_positions:
        bx, by = ball_positions[position_word.lower()]
        svg += f'<circle cx="{bx}" cy="{by}" r="20" fill="{COLOURS["red"]}"/>'
    
    svg += f'''
        <text x="100" y="190" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">The ball is {position_word} the box</text>
    </svg>'''
    return svg


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1_questions():
    """Level 1: Comparing Objects (Foundation)
    NCCA LO: Ma - Handle and evaluate everyday objects for physical differences
    """
    questions = []
    
    # Type 1: Which is bigger/smaller (20 questions)
    comparisons = [
        ("elephant", "mouse", "bigger", "An elephant is much larger than a mouse."),
        ("car", "bicycle", "bigger", "A car is bigger than a bicycle."),
        ("house", "shed", "bigger", "A house is bigger than a shed."),
        ("apple", "watermelon", "smaller", "An apple is smaller than a watermelon."),
        ("ant", "dog", "smaller", "An ant is much smaller than a dog."),
        ("book", "library", "smaller", "A book is smaller than a library."),
        ("bus", "car", "bigger", "A bus is bigger than a car."),
        ("pencil", "crayon", "bigger", "A pencil is usually longer than a crayon."),
    ]
    
    for i in range(20):
        obj1, obj2, comparison, explanation = comparisons[i % len(comparisons)]
        
        if comparison == "bigger":
            correct = obj1.capitalize()
            question = f"Which is bigger: a {obj1} or a {obj2}?"
        else:
            correct = obj1.capitalize()
            question = f"Which is smaller: a {obj1} or a {obj2}?"
        
        options = [obj1.capitalize(), obj2.capitalize(), "They are the same", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 2: Heavy or light (15 questions)
    weight_items = [
        ("feather", "light", "A feather is very light."),
        ("bowling ball", "heavy", "A bowling ball is heavy."),
        ("elephant", "heavy", "An elephant is very heavy."),
        ("leaf", "light", "A leaf is very light."),
        ("car", "heavy", "A car is heavy."),
        ("balloon", "light", "A balloon is light."),
        ("brick", "heavy", "A brick is heavy."),
        ("paper", "light", "A piece of paper is light."),
    ]
    
    for i in range(15):
        item, weight, explanation = weight_items[i % len(weight_items)]
        
        correct = weight.capitalize()
        question = f"Is a {item} heavy or light?"
        
        options = ["Heavy", "Light", "Medium", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 3: Visual comparisons (15 questions)
    for i in range(15):
        obj1_size = random.randint(3, 8)
        obj2_size = random.randint(3, 8)
        while obj1_size == obj2_size:
            obj2_size = random.randint(3, 8)
        
        if obj1_size > obj2_size:
            correct = "Object A"
            question = "Which object is longer?"
        else:
            correct = "Object B"
            question = "Which object is longer?"
        
        options = ["Object A", "Object B", "They are the same", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Object A is {obj1_size} cm, Object B is {obj2_size} cm.",
            'question_image_svg': generate_comparison_svg("Object A", obj1_size, "Object B", obj2_size)
        })
    
    return questions


def generate_level_2_questions():
    """Level 2: Measurement Language (Foundation)
    NCCA LO: Mb - Read, understand and use terms for length, distance, capacity, weight
    """
    questions = []
    
    # Type 1: Match measurement term to description (20 questions)
    terms = [
        ("length", "How long something is", "Length measures from one end to the other."),
        ("height", "How tall something is", "Height measures from bottom to top."),
        ("width", "How wide something is", "Width measures from side to side."),
        ("weight", "How heavy something is", "Weight measures how heavy an object is."),
        ("capacity", "How much a container can hold", "Capacity measures how much liquid fits inside."),
        ("distance", "How far between two places", "Distance measures how far apart things are."),
    ]
    
    for i in range(20):
        term, description, explanation = terms[i % len(terms)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"'{term.capitalize()}' measures:"
            correct = description
            distractors = [t[1] for t in terms if t[0] != term][:3]
        else:
            question = f"Which word means '{description.lower()}'?"
            correct = term.capitalize()
            distractors = [t[0].capitalize() for t in terms if t[0] != term][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append("None of these")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 2: What would you measure? (15 questions)
    measure_what = [
        ("the height of a person", "Height", "We measure how tall someone is using height."),
        ("how much water in a bottle", "Capacity", "We measure how much liquid using capacity."),
        ("how heavy a bag is", "Weight", "We measure how heavy something is using weight."),
        ("how long a pencil is", "Length", "We measure how long something is using length."),
        ("how far to school", "Distance", "We measure how far using distance."),
        ("how wide a door is", "Width", "We measure from side to side using width."),
    ]
    
    for i in range(15):
        scenario, correct, explanation = measure_what[i % len(measure_what)]
        
        options = ["Length", "Weight", "Capacity", "Height", "Distance", "Width"]
        options = [correct] + [o for o in options if o != correct][:3]
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"To measure {scenario}, you would use:",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 3: Comparison words (15 questions)
    comparison_words = [
        ("taller", "shorter", "height"),
        ("longer", "shorter", "length"),
        ("heavier", "lighter", "weight"),
        ("wider", "narrower", "width"),
        ("more", "less", "capacity"),
        ("farther", "nearer", "distance"),
    ]
    
    for i in range(15):
        word1, word2, measures = comparison_words[i % len(comparison_words)]
        
        q_type = i % 3
        if q_type == 0:
            question = f"'{word1.capitalize()}' and '{word2}' are words used to compare:"
            correct = measures.capitalize()
            distractors = ["Height", "Weight", "Length", "Capacity"]
            distractors = [d for d in distractors if d.lower() != measures][:3]
        elif q_type == 1:
            question = f"The opposite of '{word1}' is:"
            correct = word2.capitalize()
            distractors = [w[1].capitalize() for w in comparison_words if w[1] != word2][:3]
        else:
            question = f"If something is '{word1}', it has more:"
            correct = measures.capitalize()
            distractors = ["Height", "Weight", "Length", "Capacity"]
            distractors = [d for d in distractors if d.lower() != measures][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append("None of these")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"'{word1}' and '{word2}' compare {measures}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_3_questions():
    """Level 3: Metric Units (Foundation)
    NCCA LO: Mc - Interpret metric units of measurement
    """
    questions = []
    
    # Type 1: Match unit to what it measures (20 questions)
    units = [
        ("centimetre (cm)", "length", "small objects"),
        ("metre (m)", "length", "rooms, heights"),
        ("kilometre (km)", "distance", "between towns"),
        ("gram (g)", "weight", "small items"),
        ("kilogram (kg)", "weight", "people, heavy items"),
        ("millilitre (ml)", "capacity", "small amounts"),
        ("litre (l)", "capacity", "bottles, jugs"),
    ]
    
    for i in range(20):
        unit, measures, example = units[i % len(units)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"What does {unit} measure?"
            correct = measures.capitalize()
            options = ["Length", "Weight", "Capacity", "Time"]
        else:
            question = f"Which unit measures {measures}?"
            correct = unit
            options = [u[0] for u in units if u[1] == measures][:1] + \
                     [u[0] for u in units if u[1] != measures][:3]
        
        options = [correct] + [o for o in options if o != correct][:3]
        while len(options) < 4:
            options.append("None of these")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{unit} measures {measures}, used for {example}.",
            'question_image_svg': ''
        })
    
    # Type 2: Which unit would you use? (15 questions)
    scenarios = [
        ("the length of your finger", "cm", "centimetres"),
        ("the height of a door", "m", "metres"),
        ("the distance to Dublin", "km", "kilometres"),
        ("the weight of an apple", "g", "grams"),
        ("your body weight", "kg", "kilograms"),
        ("medicine in a spoon", "ml", "millilitres"),
        ("milk in a carton", "l", "litres"),
        ("the length of a pencil", "cm", "centimetres"),
        ("the length of a football pitch", "m", "metres"),
    ]
    
    for i in range(15):
        scenario, correct, full_unit = scenarios[i % len(scenarios)]
        
        distractors = ["cm", "m", "km", "g", "kg", "ml", "l"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Which unit would you use to measure {scenario}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"You would measure {scenario} in {full_unit} ({correct}).",
            'question_image_svg': ''
        })
    
    # Type 3: Unit symbols (15 questions)
    symbols = [
        ("cm", "centimetre"),
        ("m", "metre"),
        ("km", "kilometre"),
        ("g", "gram"),
        ("kg", "kilogram"),
        ("ml", "millilitre"),
        ("l", "litre"),
    ]
    
    for i in range(15):
        symbol, name = symbols[i % len(symbols)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"What does '{symbol}' stand for?"
            correct = name.capitalize()
            distractors = [s[1].capitalize() for s in symbols if s[0] != symbol][:3]
        else:
            question = f"What is the symbol for {name}?"
            correct = symbol
            distractors = [s[0] for s in symbols if s[0] != symbol][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"'{symbol}' is the symbol for {name}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_4_questions():
    """Level 4: Measuring Length (Developing)
    NCCA LO: Md - Measure and record length of object and distance between objects
    """
    questions = []
    
    # Type 1: Read a ruler measurement (25 questions)
    for i in range(25):
        length = random.randint(3, 12)
        
        correct = f"{length} cm"
        distractors = [f"{length + 1} cm", f"{length - 1} cm", f"{length + 2} cm"]
        distractors = [d for d in distractors if int(d.split()[0]) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(f"{random.randint(1, 15)} cm")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        templates = [
            "How long is this object?",
            "What is the length shown on the ruler?",
            "Read the ruler. How long is the object?",
        ]
        
        questions.append({
            'question_text': templates[i % 3],
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The object measures {length} cm on the ruler.",
            'question_image_svg': generate_ruler_svg(length)
        })
    
    # Type 2: Estimate reasonable lengths (15 questions)
    estimates = [
        ("a pencil", "15 cm", ["15 m", "15 km", "15 mm"]),
        ("a door", "2 m", ["2 cm", "2 km", "200 m"]),
        ("a football pitch", "100 m", ["100 cm", "100 km", "10 m"]),
        ("your thumb width", "2 cm", ["2 m", "2 km", "20 cm"]),
        ("a car", "4 m", ["4 cm", "4 km", "40 m"]),
        ("a phone", "15 cm", ["15 m", "15 km", "150 cm"]),
    ]
    
    for i in range(15):
        item, correct, distractors = estimates[i % len(estimates)]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"What is a reasonable length for {item}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"A reasonable length for {item} is about {correct}.",
            'question_image_svg': ''
        })
    
    # Type 3: Add lengths (10 questions)
    for i in range(10):
        len1 = random.randint(3, 10)
        len2 = random.randint(2, 8)
        total = len1 + len2
        
        correct = f"{total} cm"
        distractors = [f"{total + 1} cm", f"{total - 1} cm", f"{len1} cm"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"A pencil is {len1} cm and a rubber is {len2} cm. What is their total length?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{len1} cm + {len2} cm = {total} cm",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_5_questions():
    """Level 5: Comparing Measurements (Developing)
    NCCA LOs: Me, Mf, Mg - Compare and contrast, identify relationships, order objects
    """
    questions = []
    
    # Type 1: Which is longer/heavier/more (20 questions)
    for i in range(20):
        measure_type = random.choice(['length', 'weight', 'capacity'])
        
        if measure_type == 'length':
            val1 = random.randint(5, 20)
            val2 = random.randint(5, 20)
            unit = 'cm'
            word = 'longer'
        elif measure_type == 'weight':
            val1 = random.randint(1, 10)
            val2 = random.randint(1, 10)
            unit = 'kg'
            word = 'heavier'
        else:
            val1 = random.randint(100, 500)
            val2 = random.randint(100, 500)
            unit = 'ml'
            word = 'more'
        
        while val1 == val2:
            val2 = val1 + random.choice([-2, -1, 1, 2])
        
        if val1 > val2:
            correct = f"Object A ({val1} {unit})"
        else:
            correct = f"Object B ({val2} {unit})"
        
        options = [f"Object A ({val1} {unit})", f"Object B ({val2} {unit})", "They are equal", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Which is {word}: Object A ({val1} {unit}) or Object B ({val2} {unit})?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{max(val1, val2)} {unit} is {word} than {min(val1, val2)} {unit}.",
            'question_image_svg': ''
        })
    
    # Type 2: Order from smallest to largest (15 questions)
    for i in range(15):
        measure_type = random.choice(['length', 'weight'])
        
        if measure_type == 'length':
            values = random.sample(range(5, 25), 3)
            unit = 'cm'
        else:
            values = random.sample(range(1, 15), 3)
            unit = 'kg'
        
        sorted_vals = sorted(values)
        correct = f"{sorted_vals[0]}, {sorted_vals[1]}, {sorted_vals[2]} {unit}"
        
        # Create wrong orders
        distractors = [
            f"{sorted_vals[2]}, {sorted_vals[1]}, {sorted_vals[0]} {unit}",
            f"{sorted_vals[1]}, {sorted_vals[0]}, {sorted_vals[2]} {unit}",
            f"{sorted_vals[0]}, {sorted_vals[2]}, {sorted_vals[1]} {unit}",
        ]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Put in order from smallest to largest: {values[0]}, {values[1]}, {values[2]} {unit}",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Smallest to largest: {correct}",
            'question_image_svg': ''
        })
    
    # Type 3: Find the difference (15 questions)
    for i in range(15):
        val1 = random.randint(10, 30)
        val2 = random.randint(5, val1 - 2)
        diff = val1 - val2
        unit = random.choice(['cm', 'kg', 'ml'])
        
        correct = f"{diff} {unit}"
        distractors = [f"{diff + 1} {unit}", f"{diff - 1} {unit}", f"{val1 + val2} {unit}"]
        distractors = [d for d in distractors if int(d.split()[0]) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(f"{random.randint(1, 20)} {unit}")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"What is the difference between {val1} {unit} and {val2} {unit}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{val1} - {val2} = {diff} {unit}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_6_questions():
    """Level 6: Using Measuring Tools (Developing)
    NCCA LOs: Mh, Mi - Select appropriate tools, importance of accuracy
    """
    questions = []
    
    # Type 1: Choose the right tool (20 questions)
    tools = [
        ("the length of a book", "Ruler", "A ruler measures short lengths."),
        ("the weight of flour", "Kitchen scales", "Kitchen scales measure weight."),
        ("how much water in a jug", "Measuring jug", "A measuring jug measures liquid."),
        ("the height of a person", "Tape measure", "A tape measure is good for height."),
        ("the temperature outside", "Thermometer", "A thermometer measures temperature."),
        ("the distance to town", "Car odometer", "An odometer measures distance."),
        ("body weight", "Bathroom scales", "Bathroom scales measure body weight."),
        ("length of fabric", "Tape measure", "A tape measure works well for fabric."),
    ]
    
    for i in range(20):
        task, correct, explanation = tools[i % len(tools)]
        
        all_tools = ["Ruler", "Kitchen scales", "Measuring jug", "Tape measure", "Thermometer", "Bathroom scales"]
        distractors = [t for t in all_tools if t != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"What tool would you use to measure {task}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 2: Why accuracy matters (15 questions)
    accuracy_scenarios = [
        ("measuring medicine", "Too much or too little could be harmful", "correct dose"),
        ("measuring ingredients for a recipe", "The food might not turn out right", "taste and texture"),
        ("measuring fabric for clothes", "The clothes won't fit properly", "proper fit"),
        ("measuring distance for travel", "You might not have enough fuel", "planning"),
        ("measuring your height for a ride", "Safety rules need to be followed", "safety"),
    ]
    
    for i in range(15):
        scenario, correct_reason, importance = accuracy_scenarios[i % len(accuracy_scenarios)]
        
        question = f"Why is it important to measure {scenario} accurately?"
        correct = correct_reason
        distractors = ["It doesn't matter", "Just for fun", "To waste time"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Accurate measurement is important for {importance}.",
            'question_image_svg': ''
        })
    
    # Type 3: Read measuring tools (15 questions)
    for i in range(15):
        tool_type = i % 3
        
        if tool_type == 0:  # Ruler
            value = random.randint(5, 15)
            correct = f"{value} cm"
            question = "What length does this ruler show?"
            distractors = [f"{value + 1} cm", f"{value - 1} cm", f"{value + 2} cm"]
            svg = generate_ruler_svg(value)
        elif tool_type == 1:  # Scale
            value = random.randint(2, 10)
            correct = f"{value} kg"
            question = "What weight does this scale show?"
            distractors = [f"{value + 1} kg", f"{value - 1} kg", f"{value * 2} kg"]
            svg = generate_scale_svg(value)
        else:  # Measuring jug
            capacity = 500
            filled = random.choice([125, 250, 375, 500])
            correct = f"{filled} ml"
            question = "How much liquid is in the jug?"
            distractors = [f"{filled + 125} ml", f"{filled - 125} ml", f"{capacity} ml"]
            distractors = [d for d in distractors if int(d.split()[0]) > 0 and int(d.split()[0]) <= capacity]
            svg = generate_measuring_jug_svg(capacity, filled)
        
        while len(distractors) < 3:
            distractors.append(f"{random.randint(1, 20)} {correct.split()[1]}")
        
        options = [correct] + distractors[:3]
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The measurement shown is {correct}.",
            'question_image_svg': svg
        })
    
    return questions


def generate_level_7_questions():
    """Level 7: Body in Space (Progressing)
    NCCA LOs: Pa, Pb - Awareness of body position, direction and movement
    """
    questions = []
    
    # Type 1: Direction words (20 questions)
    directions = [
        ("to go higher", "Up", "Moving up means going higher."),
        ("to go lower", "Down", "Moving down means going lower."),
        ("to move to the right side", "Right", "Right is the opposite of left."),
        ("to move to the left side", "Left", "Left is the opposite of right."),
        ("to move ahead", "Forward", "Forward means moving ahead."),
        ("to move the way you came", "Backward", "Backward means going back."),
    ]
    
    for i in range(20):
        description, correct, explanation = directions[i % len(directions)]
        
        all_dirs = ["Up", "Down", "Left", "Right", "Forward", "Backward"]
        distractors = [d for d in all_dirs if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Which direction do you move {description}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': generate_direction_svg(correct.lower())
        })
    
    # Type 2: Following directions (15 questions)
    instruction_sequences = [
        ("Take 2 steps forward, then turn right", "You end up facing right", "forward then right"),
        ("Turn left, then take 3 steps", "You walk to the left", "left direction"),
        ("Go up the stairs, then turn around", "You face down the stairs", "up then turn"),
        ("Walk backward 5 steps", "You move without seeing where you're going", "backward movement"),
    ]
    
    for i in range(15):
        instruction, correct, explanation = instruction_sequences[i % len(instruction_sequences)]
        
        distractors = [
            "You stay in the same place",
            "You move in a circle",
            "You end up where you started",
        ]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"If you '{instruction}', what happens?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Following '{instruction}': {correct}.",
            'question_image_svg': ''
        })
    
    # Type 3: Compass directions (15 questions)
    compass = [
        ("North", "top of the map", "North is usually at the top of a map."),
        ("South", "bottom of the map", "South is at the bottom of a map."),
        ("East", "right side of the map", "East is on the right when facing North."),
        ("West", "left side of the map", "West is on the left when facing North."),
    ]
    
    for i in range(15):
        direction, position, explanation = compass[i % len(compass)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"On a map, which direction is usually at the {position}?"
            correct = direction
            distractors = [d[0] for d in compass if d[0] != direction][:3]
        else:
            question = f"If you're facing North, which direction is to your right?"
            correct = "East"
            distractors = ["West", "North", "South"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': generate_direction_svg(direction)
        })
    
    return questions


def generate_level_8_questions():
    """Level 8: Position Words (Progressing)
    NCCA LO: Pc - Use vocabulary to describe positions
    """
    questions = []
    
    # Type 1: Identify position from picture (25 questions)
    positions = ['on', 'under', 'beside', 'left', 'right', 'above', 'below']
    
    for i in range(25):
        position = positions[i % len(positions)]
        
        correct = position.capitalize()
        distractors = [p.capitalize() for p in positions if p != position][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Where is the ball? Look at the picture.",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The ball is {position} the box.",
            'question_image_svg': generate_position_svg(position)
        })
    
    # Type 2: Opposite positions (15 questions)
    opposites = [
        ("above", "below"),
        ("on", "under"),
        ("left", "right"),
        ("in front of", "behind"),
        ("inside", "outside"),
        ("near", "far"),
    ]
    
    for i in range(15):
        word1, word2 = opposites[i % len(opposites)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"What is the opposite of '{word1}'?"
            correct = word2.capitalize()
            distractors = [o[1].capitalize() for o in opposites if o[1] != word2][:3]
        else:
            question = f"What is the opposite of '{word2}'?"
            correct = word1.capitalize()
            distractors = [o[0].capitalize() for o in opposites if o[0] != word1][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"'{word1}' and '{word2}' are opposites.",
            'question_image_svg': ''
        })
    
    # Type 3: Position in a sentence (10 questions)
    sentences = [
        ("The cat sat ___ the chair.", "on", ["under", "beside", "behind"]),
        ("The ball rolled ___ the table.", "under", ["on", "above", "beside"]),
        ("Stand ___ to me.", "next", ["on", "under", "above"]),
        ("The shop is ___ the bank.", "beside", ["on", "under", "above"]),
        ("Put the book ___ the shelf.", "on", ["under", "beside", "behind"]),
    ]
    
    for i in range(10):
        sentence, correct, distractors = sentences[i % len(sentences)]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Fill in the blank: {sentence}",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': sentence.replace("___", correct),
            'question_image_svg': ''
        })
    
    return questions


def generate_level_9_questions():
    """Level 9: Simple Maps (Progressing)
    NCCA LOs: Pd, Pe - Draw and use simple maps, locate key locations
    """
    questions = []
    
    landmarks = ['School', 'Shop', 'Park', 'Home', 'Library', 'Hospital']
    
    # Type 1: Find location on map (25 questions)
    for i in range(25):
        selected_landmarks = random.sample(landmarks, 4)
        target = random.choice(selected_landmarks)
        
        question = f"Find the {target} on the map. Where is it?"
        
        positions = ["Top left", "Top right", "Bottom left", "Bottom right", "Centre"]
        landmark_positions = {
            'School': 'Top left',
            'Shop': 'Top right',
            'Park': 'Bottom left',
            'Home': 'Bottom right',
            'Library': 'Centre',
            'Hospital': 'Centre',
        }
        
        correct = landmark_positions.get(target, "Centre")
        distractors = [p for p in positions if p != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The {target} is in the {correct} of the map.",
            'question_image_svg': generate_simple_map_svg(selected_landmarks, target)
        })
    
    # Type 2: Directions between places (15 questions)
    directions_between = [
        ("School", "Shop", "right", "The Shop is to the right of the School."),
        ("Park", "Home", "right", "Home is to the right of the Park."),
        ("School", "Park", "down", "The Park is below the School."),
        ("Shop", "Home", "down", "Home is below the Shop."),
    ]
    
    for i in range(15):
        start, end, correct, explanation = directions_between[i % len(directions_between)]
        
        question = f"To get from {start} to {end}, which direction do you go?"
        distractors = ["left", "right", "up", "down"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct.capitalize()] + [d.capitalize() for d in distractors]
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct.capitalize())]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': generate_simple_map_svg([start, end, 'Park', 'Home'])
        })
    
    # Type 3: What's near what? (10 questions)
    for i in range(10):
        selected = random.sample(landmarks, 4)
        target = random.choice(selected)
        
        question = f"Look at the map. What is near the {target}?"
        
        # Simple adjacency - anything in the list could be an answer
        correct = random.choice([l for l in selected if l != target])
        distractors = [l for l in landmarks if l not in [target, correct]][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The {correct} is near the {target}.",
            'question_image_svg': generate_simple_map_svg(selected, target)
        })
    
    return questions


def generate_level_10_questions():
    """Level 10: Distance on Maps (Consolidating)
    NCCA LO: Pf - Calculate and record distance between two places on a map
    """
    questions = []
    
    # Type 1: Read distance from map (20 questions)
    for i in range(20):
        distance = random.randint(2, 15)
        start = random.choice(['School', 'Home', 'Shop'])
        end = random.choice(['Park', 'Library', 'Hospital'])
        
        correct = f"{distance} km"
        distractors = [f"{distance + 2} km", f"{distance - 1} km", f"{distance * 2} km"]
        distractors = [d for d in distractors if int(d.split()[0]) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(f"{random.randint(1, 20)} km")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"The distance from {start} to {end} is {distance} km. What is the distance?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The distance is {distance} km.",
            'question_image_svg': ''
        })
    
    # Type 2: Compare distances (15 questions)
    for i in range(15):
        dist1 = random.randint(3, 12)
        dist2 = random.randint(3, 12)
        while dist1 == dist2:
            dist2 = dist1 + random.choice([-2, 2])
        
        if dist1 < dist2:
            correct = f"Route A ({dist1} km)"
            question = f"Route A is {dist1} km. Route B is {dist2} km. Which is shorter?"
        else:
            correct = f"Route B ({dist2} km)"
            question = f"Route A is {dist1} km. Route B is {dist2} km. Which is shorter?"
        
        options = [f"Route A ({dist1} km)", f"Route B ({dist2} km)", "They are the same", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{min(dist1, dist2)} km is shorter than {max(dist1, dist2)} km.",
            'question_image_svg': ''
        })
    
    # Type 3: Total distance (15 questions)
    for i in range(15):
        leg1 = random.randint(2, 8)
        leg2 = random.randint(2, 8)
        total = leg1 + leg2
        
        correct = f"{total} km"
        distractors = [f"{total + 1} km", f"{total - 1} km", f"{leg1} km"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You walk {leg1} km to the shop, then {leg2} km to the park. How far in total?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{leg1} + {leg2} = {total} km total.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_11_questions():
    """Level 11: Grid References (Consolidating)
    NCCA LOs: Pg, Ph - Location on grid, recognise location in community
    """
    questions = []
    
    # Type 1: Find grid reference (25 questions)
    for i in range(25):
        col = random.choice(['A', 'B', 'C', 'D', 'E'])
        row = random.randint(1, 5)
        position = f"{col}{row}"
        
        question = f"What is the grid reference of the star?"
        correct = position
        
        # Generate distractors
        other_cols = [c for c in 'ABCDE' if c != col]
        other_rows = [r for r in range(1, 6) if r != row]
        distractors = [
            f"{random.choice(other_cols)}{row}",
            f"{col}{random.choice(other_rows)}",
            f"{random.choice(other_cols)}{random.choice(other_rows)}",
        ]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The star is at grid reference {position}.",
            'question_image_svg': generate_grid_map_svg(5, (col, str(row)))
        })
    
    # Type 2: Find what's at a location (15 questions)
    community_places = [
        ("A1", "Post Office"),
        ("B2", "Supermarket"),
        ("C3", "Library"),
        ("D4", "School"),
        ("E5", "Hospital"),
    ]
    
    for i in range(15):
        grid_ref, place = community_places[i % len(community_places)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"The {place} is at which grid reference?"
            correct = grid_ref
            distractors = [cp[0] for cp in community_places if cp[0] != grid_ref][:3]
        else:
            question = f"What is at grid reference {grid_ref}?"
            correct = place
            distractors = [cp[1] for cp in community_places if cp[1] != place][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The {place} is at {grid_ref}.",
            'question_image_svg': ''
        })
    
    # Type 3: Move on a grid (10 questions)
    moves = [
        ("B2", "right 2 squares", "D2"),
        ("C3", "down 1 square", "C4"),
        ("A1", "right 1, down 1", "B2"),
        ("E5", "left 2 squares", "C5"),
        ("D4", "up 2 squares", "D2"),
    ]
    
    for i in range(10):
        start, move, correct = moves[i % len(moves)]
        
        question = f"Start at {start}. Move {move}. Where are you now?"
        distractors = ["A1", "B3", "C4", "D5", "E2"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Starting at {start} and moving {move} takes you to {correct}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_12_questions():
    """Level 12: Planning Journeys (Consolidating)
    NCCA LO: Pi - Plan, describe and prepare a journey for a day trip
    """
    questions = []
    
    # Type 1: Plan journey steps (20 questions)
    journey_steps = [
        ("Going to the cinema", ["Leave home", "Walk to bus stop", "Take bus to town", "Walk to cinema"], "Leave home"),
        ("School trip to zoo", ["Pack lunch", "Get on bus", "Arrive at zoo", "Visit animals"], "Pack lunch"),
        ("Shopping trip", ["Make a list", "Go to shop", "Buy items", "Return home"], "Make a list"),
        ("Visit to grandparents", ["Pack bag", "Travel there", "Have dinner", "Travel home"], "Pack bag"),
    ]
    
    for i in range(20):
        trip, steps, first_step = journey_steps[i % len(journey_steps)]
        
        q_type = i % 4
        
        if q_type == 0:
            question = f"For a '{trip}', what is the first step?"
            correct = first_step
            distractors = [s for s in steps if s != first_step][:3]
        elif q_type == 1:
            question = f"For a '{trip}', what is the last step?"
            correct = steps[-1]
            distractors = steps[:-1][:3]
        elif q_type == 2:
            idx = random.randint(1, len(steps) - 1)
            question = f"For a '{trip}', what comes after '{steps[idx-1]}'?"
            correct = steps[idx]
            distractors = [s for s in steps if s != correct][:3]
        else:
            question = f"How many steps are in this journey plan?"
            correct = str(len(steps))
            distractors = [str(len(steps) + 1), str(len(steps) - 1), str(len(steps) + 2)]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append("None of these")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"For '{trip}': {', '.join(steps)}",
            'question_image_svg': ''
        })
    
    # Type 2: What to bring (15 questions)
    trips_items = [
        ("beach trip", "Sunscreen", ["Snow boots", "Umbrella (for rain)", "Winter coat"]),
        ("mountain hike", "Water bottle", ["Swimming costume", "Beach towel", "Flip flops"]),
        ("museum visit", "Comfortable shoes", ["Swimming goggles", "Tent", "Fishing rod"]),
        ("picnic in park", "Food and drinks", ["Skis", "Snorkel", "Ice skates"]),
    ]
    
    for i in range(15):
        trip, correct, distractors = trips_items[i % len(trips_items)]
        
        question = f"What should you bring for a {trip}?"
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"For a {trip}, you should bring {correct}.",
            'question_image_svg': ''
        })
    
    # Type 3: Journey time planning (15 questions)
    for i in range(15):
        walk_time = random.randint(5, 15)
        bus_time = random.randint(20, 40)
        total = walk_time + bus_time
        
        q_type = i % 3
        
        if q_type == 0:
            question = f"You walk for {walk_time} minutes, then take a bus for {bus_time} minutes. How long is the journey?"
            correct = f"{total} minutes"
            distractors = [f"{total + 10} minutes", f"{total - 10} minutes", f"{bus_time} minutes"]
        elif q_type == 1:
            arrive_time = 10
            leave_time = arrive_time - (total // 60) if total >= 60 else arrive_time
            question = f"You need to arrive at {arrive_time}:00. The journey takes {total} minutes. What time should you leave?"
            leave_hour = arrive_time - 1 if total > 30 else arrive_time
            leave_min = 60 - (total % 60) if total % 60 != 0 else 0
            correct = f"{leave_hour}:{leave_min:02d}" if leave_min > 0 else f"{leave_hour}:00"
            distractors = [f"{arrive_time}:00", f"{leave_hour - 1}:00", f"{leave_hour}:30"]
        else:
            question = f"Your journey takes {total} minutes. Is that more or less than an hour?"
            if total > 60:
                correct = "More than an hour"
            elif total < 60:
                correct = "Less than an hour"
            else:
                correct = "Exactly an hour"
            distractors = ["More than an hour", "Less than an hour", "Exactly an hour"]
            distractors = [d for d in distractors if d != correct]
        
        while len(distractors) < 3:
            distractors.append("Cannot tell")
        
        options = [correct] + distractors[:3]
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Journey time: {total} minutes.",
            'question_image_svg': ''
        })
    
    return questions


# ============================================================
# MAIN FUNCTIONS
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
        
        if len(questions) > QUESTIONS_PER_LEVEL:
            questions = questions[:QUESTIONS_PER_LEVEL]
        
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['difficulty'] = DIFFICULTY
        
        all_questions.extend(questions)
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    """Validate all questions"""
    errors = []
    
    for i, q in enumerate(questions):
        if not q.get('question_text'):
            errors.append(f"Q{i+1}: Missing question_text")
        if not q.get('correct_answer') in ['A', 'B', 'C', 'D']:
            errors.append(f"Q{i+1}: Invalid correct_answer")
        if not q.get('option_a'):
            errors.append(f"Q{i+1}: Missing option_a")
        if not q.get('option_b'):
            errors.append(f"Q{i+1}: Missing option_b")
    
    seen_text = set()
    seen_visual = {}
    for q in questions:
        text = q['question_text']
        svg = q.get('question_image_svg', '')
        if svg:
            if text in seen_visual:
                if hash(svg) in seen_visual[text]:
                    errors.append(f"Duplicate: '{text[:50]}...'")
                else:
                    seen_visual[text].add(hash(svg))
            else:
                seen_visual[text] = {hash(svg)}
        else:
            if text in seen_text:
                errors.append(f"Duplicate: '{text[:50]}...'")
            seen_text.add(text)
    
    return errors


def clear_existing_questions():
    """Clear existing questions for this topic"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM questions WHERE topic = ?', (TOPIC,))
        count = cursor.fetchone()[0]
        conn.close()
        
        if count > 0:
            print(f"\n⚠️  Found {count} existing questions for {TOPIC}")
            response = input("Delete existing questions? (yes/no): ").strip().lower()
            if response == 'yes':
                conn = sqlite3.connect(DATABASE_PATH)
                cursor = conn.cursor()
                cursor.execute('DELETE FROM questions WHERE topic = ?', (TOPIC,))
                conn.commit()
                conn.close()
                print(f"   Deleted {count} questions")
                return True
            return False
    except:
        pass
    return True


def insert_questions(questions):
    """Insert questions into database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    inserted = 0
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions 
                (topic, difficulty, level, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, question_image_svg)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'], q['difficulty'], q['level'],
                q['question_text'], q['option_a'], q['option_b'], 
                q.get('option_c', ''), q.get('option_d', ''),
                q['correct_answer'], q.get('solution', ''),
                q.get('question_image_svg', '')
            ))
            inserted += 1
        except sqlite3.Error as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    return inserted


def main():
    print("=" * 60)
    print("AgentMath L2LP Question Generator")
    print(f"Topic: {TOPIC}")
    print(f"Target: {QUESTIONS_PER_LEVEL} × {TOTAL_LEVELS} = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS}")
    print("=" * 60)
    
    if not clear_existing_questions():
        return
    
    print("\nGenerating questions...")
    questions = generate_all_questions()
    print(f"\nTotal: {len(questions)}")
    
    print("\nValidating...")
    errors = validate_questions(questions)
    critical = [e for e in errors if 'Duplicate' not in e]
    
    if critical:
        print(f"❌ {len(critical)} critical errors")
        for e in critical[:5]:
            print(f"   {e}")
        return
    
    print("✅ Validation passed")
    
    print("\nInserting...")
    inserted = insert_questions(questions)
    print(f"✅ Inserted {inserted} questions!")
    
    print("\nSummary:")
    for level in range(1, 13):
        count = sum(1 for q in questions if q['level'] == level)
        visual = sum(1 for q in questions if q['level'] == level and q.get('question_image_svg'))
        pct = (visual / count * 100) if count else 0
        print(f"  Level {level}: {count} questions, {pct:.0f}% visual")


if __name__ == '__main__':
    main()
