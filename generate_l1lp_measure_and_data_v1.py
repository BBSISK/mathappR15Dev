"""
AgentMath L1LP Question Generator
Topic: Measure and Data
Learning Outcomes: 2.22 - 2.25
Version: 1.0

Generates 600 questions (50 per level × 12 levels) for the L1LP strand.
Focus: Big/small, long/short, heavy/light, full/empty, ordering by size, coins, shopping, temperature, pictographs.

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
TOPIC = 'measure_and_data'
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
    'brown': '#8B4513',
    'grey': '#7F8C8D'
}

# Irish coins for money activities
IRISH_COINS = [
    {'value': 1, 'name': '1 cent', 'colour': '#CD7F32'},
    {'value': 2, 'name': '2 cent', 'colour': '#CD7F32'},
    {'value': 5, 'name': '5 cent', 'colour': '#CD7F32'},
    {'value': 10, 'name': '10 cent', 'colour': '#FFD700'},
    {'value': 20, 'name': '20 cent', 'colour': '#FFD700'},
    {'value': 50, 'name': '50 cent', 'colour': '#FFD700'},
    {'value': 100, 'name': '€1', 'colour': '#C0C0C0'},
    {'value': 200, 'name': '€2', 'colour': '#C0C0C0'}
]

# =============================================================================
# SVG GENERATION FUNCTIONS
# =============================================================================

def create_svg_wrapper(content, width=400, height=180):
    """Wrap SVG content"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def svg_circle(x, y, size, colour='#3498DB'):
    """Generate a circle"""
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2}" fill="{colour}"/>'

def svg_rectangle(x, y, width, height, colour='#3498DB'):
    """Generate a rectangle"""
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{colour}" stroke="#333" stroke-width="1" rx="3"/>'

def svg_tree(x, y, size='medium'):
    """Generate a tree of different sizes"""
    sizes = {'small': 0.5, 'medium': 1.0, 'large': 1.5}
    scale = sizes.get(size, 1.0)
    
    trunk_w = int(15 * scale)
    trunk_h = int(30 * scale)
    crown_r = int(25 * scale)
    
    trunk = f'<rect x="{x - trunk_w//2}" y="{y - trunk_h}" width="{trunk_w}" height="{trunk_h}" fill="#8B4513"/>'
    crown = f'<circle cx="{x}" cy="{y - trunk_h - crown_r + 5}" r="{crown_r}" fill="#27AE60"/>'
    
    return trunk + crown

def svg_pencil(x, y, length='medium'):
    """Generate a pencil of different lengths"""
    lengths = {'short': 40, 'medium': 70, 'long': 100}
    l = lengths.get(length, 70)
    
    body = f'<rect x="{x}" y="{y}" width="{l}" height="12" fill="#F1C40F"/>'
    tip = f'<polygon points="{x + l},{y} {x + l + 15},{y + 6} {x + l},{y + 12}" fill="#F5CBA7"/>'
    eraser = f'<rect x="{x - 10}" y="{y}" width="10" height="12" fill="#FF69B4"/>'
    
    return body + tip + eraser

def svg_glass(x, y, fill_level='full'):
    """Generate a glass with different fill levels"""
    levels = {'empty': 0, 'half': 0.5, 'full': 1.0}
    level = levels.get(fill_level, 1.0)
    
    glass_h = 70
    glass_w = 40
    water_h = int(glass_h * level * 0.8)
    
    # Glass outline
    glass = f'<path d="M{x},{y} L{x + 5},{y + glass_h} L{x + glass_w - 5},{y + glass_h} L{x + glass_w},{y} Z" fill="none" stroke="#333" stroke-width="2"/>'
    
    # Water fill
    if level > 0:
        water_y = y + glass_h - water_h - 5
        water = f'<rect x="{x + 3}" y="{water_y}" width="{glass_w - 6}" height="{water_h}" fill="#3498DB" opacity="0.7"/>'
    else:
        water = ''
    
    return glass + water

def svg_elephant(x, y, size='big'):
    """Generate elephant (big animal)"""
    scale = 1.2 if size == 'big' else 0.6
    return f'''<g transform="translate({x},{y}) scale({scale})">
        <ellipse cx="30" cy="35" rx="25" ry="20" fill="#7F8C8D"/>
        <circle cx="55" cy="25" r="15" fill="#7F8C8D"/>
        <rect x="10" y="50" width="8" height="20" fill="#7F8C8D"/>
        <rect x="25" y="50" width="8" height="20" fill="#7F8C8D"/>
        <rect x="35" y="50" width="8" height="20" fill="#7F8C8D"/>
        <rect x="50" y="50" width="8" height="20" fill="#7F8C8D"/>
        <path d="M65,30 Q75,40 70,55" stroke="#7F8C8D" stroke-width="6" fill="none"/>
        <circle cx="60" cy="22" r="2" fill="black"/>
    </g>'''

def svg_mouse(x, y, size='small'):
    """Generate mouse (small animal)"""
    scale = 0.5 if size == 'small' else 1.0
    return f'''<g transform="translate({x},{y}) scale({scale})">
        <ellipse cx="25" cy="20" rx="20" ry="12" fill="#9E9E9E"/>
        <circle cx="8" cy="15" r="8" fill="#9E9E9E"/>
        <circle cx="5" cy="12" r="2" fill="black"/>
        <path d="M45,20 Q60,15 70,20" stroke="#9E9E9E" stroke-width="2" fill="none"/>
        <circle cx="0" cy="18" r="3" fill="#FFB6C1"/>
    </g>'''

def svg_feather(x, y):
    """Generate a feather (light object)"""
    return f'''<g transform="translate({x},{y})">
        <path d="M30,5 Q15,30 30,60 Q45,30 30,5" fill="#3498DB" stroke="#2980B9" stroke-width="1"/>
        <line x1="30" y1="5" x2="30" y2="65" stroke="#8B4513" stroke-width="2"/>
    </g>'''

def svg_rock(x, y):
    """Generate a rock (heavy object)"""
    return f'''<g transform="translate({x},{y})">
        <ellipse cx="35" cy="40" rx="30" ry="20" fill="#7F8C8D"/>
        <ellipse cx="30" cy="35" rx="8" ry="5" fill="#95A5A6"/>
    </g>'''

def svg_coin(x, y, coin_data):
    """Generate a coin"""
    size = 40 if coin_data['value'] >= 100 else 35 if coin_data['value'] >= 10 else 30
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//2}" cy="{size//2}" r="{size//2}" fill="{coin_data['colour']}" stroke="#333" stroke-width="1"/>
        <text x="{size//2}" y="{size//2 + 5}" text-anchor="middle" font-size="10" fill="#333">{coin_data['name']}</text>
    </g>'''

def svg_thermometer(x, y, temp='warm'):
    """Generate a thermometer showing temperature"""
    temps = {'cold': 0.2, 'cool': 0.4, 'warm': 0.7, 'hot': 0.95}
    level = temps.get(temp, 0.5)
    
    colours = {'cold': '#3498DB', 'cool': '#27AE60', 'warm': '#E67E22', 'hot': '#E74C3C'}
    colour = colours.get(temp, '#E67E22')
    
    # Thermometer body
    body = f'<rect x="{x}" y="{y}" width="20" height="80" fill="white" stroke="#333" stroke-width="2" rx="10"/>'
    # Bulb
    bulb = f'<circle cx="{x + 10}" cy="{y + 90}" r="15" fill="{colour}"/>'
    # Mercury level
    mercury_h = int(70 * level)
    mercury = f'<rect x="{x + 5}" y="{y + 80 - mercury_h}" width="10" height="{mercury_h}" fill="{colour}"/>'
    
    return body + mercury + bulb

def svg_pictograph_row(x, y, count, symbol='star', colour='#F1C40F'):
    """Generate a row of symbols for pictograph"""
    svg = ''
    for i in range(count):
        if symbol == 'star':
            cx = x + i * 25 + 12
            cy = y + 12
            points = []
            for j in range(5):
                angle_outer = (j * 72 - 90) * math.pi / 180
                angle_inner = ((j * 72) + 36 - 90) * math.pi / 180
                points.append(f"{cx + 10 * math.cos(angle_outer)},{cy + 10 * math.sin(angle_outer)}")
                points.append(f"{cx + 5 * math.cos(angle_inner)},{cy + 5 * math.sin(angle_inner)}")
            svg += f'<polygon points="{" ".join(points)}" fill="{colour}"/>'
        elif symbol == 'circle':
            svg += f'<circle cx="{x + i * 25 + 12}" cy="{y + 12}" r="10" fill="{colour}"/>'
        elif symbol == 'square':
            svg += f'<rect x="{x + i * 25 + 2}" y="{y + 2}" width="20" height="20" fill="{colour}"/>'
    return svg

# =============================================================================
# QUESTION GENERATORS BY LEVEL
# =============================================================================

def generate_level_1_questions():
    """Level 1: Big and Small - Compare sizes (2 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        comparison_type = random.choice(['circles', 'trees', 'animals'])
        
        if comparison_type == 'circles':
            # Two circles of different sizes
            big_size = random.randint(50, 70)
            small_size = random.randint(20, 35)
            
            svg_content = svg_circle(50, 60, big_size, COLOURS['blue'])
            svg_content += svg_circle(200, 80, small_size, COLOURS['red'])
            svg_content += f'<text x="75" y="160" text-anchor="middle" font-size="14">A</text>'
            svg_content += f'<text x="220" y="160" text-anchor="middle" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            if i % 2 == 0:
                question = 'Which circle is BIGGER?'
                correct = 'A'
            else:
                question = 'Which circle is SMALLER?'
                correct = 'B'
                
        elif comparison_type == 'trees':
            svg_content = svg_tree(80, 140, 'large')
            svg_content += svg_tree(250, 140, 'small')
            svg_content += f'<text x="80" y="160" text-anchor="middle" font-size="14">A</text>'
            svg_content += f'<text x="250" y="160" text-anchor="middle" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            if i % 2 == 0:
                question = 'Which tree is BIGGER?'
                correct = 'A'
            else:
                question = 'Which tree is SMALLER?'
                correct = 'B'
                
        else:  # animals
            svg_content = svg_elephant(30, 70, 'big')
            svg_content += svg_mouse(250, 100, 'small')
            svg_content += f'<text x="80" y="160" text-anchor="middle" font-size="14">A</text>'
            svg_content += f'<text x="280" y="160" text-anchor="middle" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            if i % 2 == 0:
                question = 'Which animal is BIGGER?'
                correct = 'A'
            else:
                question = 'Which animal is SMALLER?'
                correct = 'B'
        
        options = ['A', 'B']
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is correct!',
            'visual_data': svg
        })
    
    return questions

def generate_level_2_questions():
    """Level 2: Long and Short - Compare lengths (2 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        comparison_type = random.choice(['pencils', 'lines', 'snakes'])
        
        if comparison_type == 'pencils':
            svg_content = svg_pencil(50, 50, 'long')
            svg_content += svg_pencil(50, 100, 'short')
            svg_content += f'<text x="30" y="60" font-size="14">A</text>'
            svg_content += f'<text x="30" y="110" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            if i % 2 == 0:
                question = 'Which pencil is LONGER?'
                correct = 'A'
            else:
                question = 'Which pencil is SHORTER?'
                correct = 'B'
                
        elif comparison_type == 'lines':
            svg_content = f'<line x1="50" y1="60" x2="250" y2="60" stroke="{COLOURS["blue"]}" stroke-width="8"/>'
            svg_content += f'<line x1="50" y1="110" x2="130" y2="110" stroke="{COLOURS["red"]}" stroke-width="8"/>'
            svg_content += f'<text x="30" y="65" font-size="14">A</text>'
            svg_content += f'<text x="30" y="115" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            if i % 2 == 0:
                question = 'Which line is LONGER?'
                correct = 'A'
            else:
                question = 'Which line is SHORTER?'
                correct = 'B'
                
        else:  # snakes (wavy lines)
            svg_content = f'<path d="M50,60 Q100,40 150,60 Q200,80 250,60 Q300,40 350,60" stroke="{COLOURS["green"]}" stroke-width="8" fill="none"/>'
            svg_content += f'<path d="M50,110 Q80,90 110,110" stroke="{COLOURS["orange"]}" stroke-width="8" fill="none"/>'
            svg_content += f'<text x="30" y="65" font-size="14">A</text>'
            svg_content += f'<text x="30" y="115" font-size="14">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            if i % 2 == 0:
                question = 'Which snake is LONGER?'
                correct = 'A'
            else:
                question = 'Which snake is SHORTER?'
                correct = 'B'
        
        options = ['A', 'B']
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is correct!',
            'visual_data': svg
        })
    
    return questions

def generate_level_3_questions():
    """Level 3: Heavy and Light - Compare weights (3 options)"""
    questions = []
    
    heavy_items = [('rock', 'Rock'), ('elephant', 'Elephant'), ('brick', 'Brick')]
    light_items = [('feather', 'Feather'), ('balloon', 'Balloon'), ('leaf', 'Leaf')]
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            # Show heavy vs light
            svg_content = svg_rock(80, 80)
            svg_content += svg_feather(250, 70)
            svg_content += f'<text x="110" y="160" text-anchor="middle" font-size="12">Rock</text>'
            svg_content += f'<text x="280" y="160" text-anchor="middle" font-size="12">Feather</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'Which is HEAVIER?'
            correct = 'Rock'
            options = ['Rock', 'Feather', 'Same weight']
        else:
            svg_content = svg_feather(80, 70)
            svg_content += svg_rock(230, 80)
            svg_content += f'<text x="110" y="160" text-anchor="middle" font-size="12">Feather</text>'
            svg_content += f'<text x="270" y="160" text-anchor="middle" font-size="12">Rock</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'Which is LIGHTER?'
            correct = 'Feather'
            options = ['Feather', 'Rock', 'Same weight']
        
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'The {correct.lower()} is {"heavier" if "HEAVIER" in question else "lighter"}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_4_questions():
    """Level 4: Full and Empty - Compare container states (3 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        states = ['full', 'half', 'empty']
        
        if i % 3 == 0:
            # Which is full?
            svg_content = svg_glass(80, 50, 'full')
            svg_content += svg_glass(180, 50, 'half')
            svg_content += svg_glass(280, 50, 'empty')
            svg_content += f'<text x="100" y="150" text-anchor="middle" font-size="12">A</text>'
            svg_content += f'<text x="200" y="150" text-anchor="middle" font-size="12">B</text>'
            svg_content += f'<text x="300" y="150" text-anchor="middle" font-size="12">C</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'Which glass is FULL?'
            correct = 'A'
            options = ['A', 'B', 'C']
            
        elif i % 3 == 1:
            # Which is empty?
            svg_content = svg_glass(80, 50, 'half')
            svg_content += svg_glass(180, 50, 'empty')
            svg_content += svg_glass(280, 50, 'full')
            svg_content += f'<text x="100" y="150" text-anchor="middle" font-size="12">A</text>'
            svg_content += f'<text x="200" y="150" text-anchor="middle" font-size="12">B</text>'
            svg_content += f'<text x="300" y="150" text-anchor="middle" font-size="12">C</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'Which glass is EMPTY?'
            correct = 'B'
            options = ['A', 'B', 'C']
            
        else:
            # Which is half full?
            svg_content = svg_glass(80, 50, 'empty')
            svg_content += svg_glass(180, 50, 'full')
            svg_content += svg_glass(280, 50, 'half')
            svg_content += f'<text x="100" y="150" text-anchor="middle" font-size="12">A</text>'
            svg_content += f'<text x="200" y="150" text-anchor="middle" font-size="12">B</text>'
            svg_content += f'<text x="300" y="150" text-anchor="middle" font-size="12">C</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'Which glass is HALF full?'
            correct = 'C'
            options = ['A', 'B', 'C']
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'Glass {correct} is the answer!',
            'visual_data': svg
        })
    
    return questions

def generate_level_5_questions():
    """Level 5: Ordering by Size - Put in order (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Show 3 circles of different sizes
        sizes = [30, 50, 70]
        random.shuffle(sizes)
        
        svg_content = ''
        labels = ['A', 'B', 'C']
        for j, size in enumerate(sizes):
            x = 70 + j * 110
            svg_content += svg_circle(x, 90 - size//2, size, COLOURS['blue'])
            svg_content += f'<text x="{x + size//2}" y="160" text-anchor="middle" font-size="14">{labels[j]}</text>'
        
        svg = create_svg_wrapper(svg_content)
        
        # Find which label has which size
        size_to_label = {sizes[j]: labels[j] for j in range(3)}
        
        if i % 3 == 0:
            question = 'Which is the BIGGEST?'
            correct = size_to_label[70]
        elif i % 3 == 1:
            question = 'Which is the SMALLEST?'
            correct = size_to_label[30]
        else:
            question = 'Which is in the MIDDLE (not biggest, not smallest)?'
            correct = size_to_label[50]
        
        options = ['A', 'B', 'C', 'All same size']
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is correct!',
            'visual_data': svg
        })
    
    return questions

def generate_level_6_questions():
    """Level 6: Recognising Coins - Irish Euro coins (4 options)"""
    questions = []
    
    simple_coins = [c for c in IRISH_COINS if c['value'] <= 50]
    
    for i in range(QUESTIONS_PER_LEVEL):
        coin = random.choice(simple_coins)
        
        svg_content = svg_coin(160, 50, coin)
        svg = create_svg_wrapper(svg_content)
        
        # Get wrong answers
        wrong_coins = [c['name'] for c in simple_coins if c['name'] != coin['name']]
        wrong_options = random.sample(wrong_coins, 3)
        
        options = [coin['name']] + wrong_options
        random.shuffle(options)
        
        questions.append({
            'question_text': 'What coin is this?',
            'options': json.dumps(options),
            'correct_answer': coin['name'],
            'explanation': f'This is a {coin["name"]} coin!',
            'visual_data': svg
        })
    
    return questions

def generate_level_7_questions():
    """Level 7: Which Costs More - Compare coin values (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Pick two coins
        coin1 = random.choice(IRISH_COINS[:6])  # Up to 50 cent
        coin2 = random.choice([c for c in IRISH_COINS[:6] if c['value'] != coin1['value']])
        
        svg_content = svg_coin(100, 60, coin1)
        svg_content += svg_coin(220, 60, coin2)
        svg_content += f'<text x="130" y="140" text-anchor="middle" font-size="12">A</text>'
        svg_content += f'<text x="250" y="140" text-anchor="middle" font-size="12">B</text>'
        svg = create_svg_wrapper(svg_content)
        
        if i % 2 == 0:
            question = 'Which coin is worth MORE?'
            correct = 'A' if coin1['value'] > coin2['value'] else 'B'
        else:
            question = 'Which coin is worth LESS?'
            correct = 'A' if coin1['value'] < coin2['value'] else 'B'
        
        options = ['A', 'B', 'Same value', 'Cannot tell']
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'Coin {correct} ({coin1["name"] if correct == "A" else coin2["name"]}) is {"worth more" if "MORE" in question else "worth less"}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_8_questions():
    """Level 8: Simple Shopping - Can you buy it? (4 options)"""
    questions = []
    
    items = [
        {'name': 'Apple', 'price': 20, 'emoji': '🍎'},
        {'name': 'Banana', 'price': 15, 'emoji': '🍌'},
        {'name': 'Sweet', 'price': 5, 'emoji': '🍬'},
        {'name': 'Biscuit', 'price': 10, 'emoji': '🍪'},
        {'name': 'Juice', 'price': 50, 'emoji': '🧃'}
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        item = random.choice(items)
        
        # Give them a coin
        if i % 3 == 0:
            # Exact money
            have_coin = next(c for c in IRISH_COINS if c['value'] == item['price'])
            can_buy = 'Yes, exactly right'
        elif i % 3 == 1:
            # More money
            have_coin = next(c for c in IRISH_COINS if c['value'] > item['price'])
            can_buy = 'Yes, with change'
        else:
            # Not enough
            have_coin = next((c for c in IRISH_COINS if c['value'] < item['price']), IRISH_COINS[0])
            can_buy = 'No, not enough'
        
        svg_content = f'<text x="200" y="40" text-anchor="middle" font-size="14">You have:</text>'
        svg_content += svg_coin(160, 50, have_coin)
        svg_content += f'<text x="200" y="120" text-anchor="middle" font-size="14">{item["emoji"]} {item["name"]} costs {item["price"]} cent</text>'
        svg = create_svg_wrapper(svg_content)
        
        options = ['Yes, exactly right', 'Yes, with change', 'No, not enough', 'Not sure']
        
        questions.append({
            'question_text': f'Can you buy the {item["name"]}?',
            'options': json.dumps(options),
            'correct_answer': can_buy,
            'explanation': f'You have {have_coin["name"]}, the {item["name"]} costs {item["price"]} cent. {can_buy}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_9_questions():
    """Level 9: Hot and Cold - Temperature concepts (4 options)"""
    questions = []
    
    hot_things = ['sun', 'fire', 'hot chocolate', 'oven', 'summer day']
    cold_things = ['ice cream', 'snow', 'fridge', 'winter', 'ice cube']
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 3 == 0:
            # Show thermometer
            temp = random.choice(['cold', 'warm', 'hot'])
            svg_content = svg_thermometer(180, 30, temp)
            svg_content += f'<text x="250" y="100" font-size="14">?</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'What temperature does this show?'
            correct = temp.title()
            options = ['Cold', 'Warm', 'Hot', 'Freezing']
            random.shuffle(options)
            
        elif i % 3 == 1:
            # What is hot?
            hot = random.choice(hot_things)
            cold = random.choice(cold_things)
            
            svg_content = f'<text x="200" y="90" text-anchor="middle" font-size="18">🔥 or ❄️?</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = f'Is "{hot}" hot or cold?'
            correct = 'Hot'
            options = ['Hot', 'Cold', 'Warm', 'Freezing']
            
        else:
            # What is cold?
            cold = random.choice(cold_things)
            
            svg_content = f'<text x="200" y="90" text-anchor="middle" font-size="18">🔥 or ❄️?</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = f'Is "{cold}" hot or cold?'
            correct = 'Cold'
            options = ['Cold', 'Hot', 'Warm', 'Boiling']
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is the answer!',
            'visual_data': svg
        })
    
    return questions

def generate_level_10_questions():
    """Level 10: Reading Pictographs - Simple data displays (4 options)"""
    questions = []
    
    categories = ['Apples', 'Bananas', 'Oranges']
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Generate random counts
        counts = {cat: random.randint(1, 5) for cat in categories}
        
        svg_content = f'<text x="200" y="20" text-anchor="middle" font-size="14" font-weight="bold">Favourite Fruits</text>'
        
        colours = [COLOURS['red'], COLOURS['yellow'], COLOURS['orange']]
        for j, cat in enumerate(categories):
            y = 40 + j * 40
            svg_content += f'<text x="20" y="{y + 15}" font-size="12">{cat}</text>'
            svg_content += svg_pictograph_row(90, y, counts[cat], 'circle', colours[j])
        
        svg_content += f'<text x="200" y="170" text-anchor="middle" font-size="10">Each ● = 1 person</text>'
        svg = create_svg_wrapper(svg_content)
        
        if i % 3 == 0:
            # How many liked X?
            cat = random.choice(categories)
            question = f'How many people like {cat}?'
            correct = str(counts[cat])
            options = [str(counts[c]) for c in categories] + [str(max(counts.values()) + 1)]
            options = list(set(options))[:4]
        elif i % 3 == 1:
            # Which is most popular?
            max_cat = max(counts, key=counts.get)
            question = 'Which fruit is MOST popular?'
            correct = max_cat
            options = categories + ['All the same']
        else:
            # Which is least popular?
            min_cat = min(counts, key=counts.get)
            question = 'Which fruit is LEAST popular?'
            correct = min_cat
            options = categories + ['All the same']
        
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'The answer is {correct}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_11_questions():
    """Level 11: Sorting Data - Organise by category (4 options)"""
    questions = []
    
    sorting_scenarios = [
        {
            'title': 'Sort by Colour',
            'items': [('🍎', 'Red'), ('🍌', 'Yellow'), ('🍊', 'Orange'), ('🫐', 'Blue')],
            'question': 'Which fruit is RED?',
            'correct': '🍎'
        },
        {
            'title': 'Sort by Size',
            'items': [('Elephant', 'Big'), ('Mouse', 'Small'), ('Dog', 'Medium'), ('Ant', 'Tiny')],
            'question': 'Which animal is BIGGEST?',
            'correct': 'Elephant'
        },
        {
            'title': 'Sort by Type',
            'items': [('Apple', 'Fruit'), ('Carrot', 'Vegetable'), ('Banana', 'Fruit'), ('Broccoli', 'Vegetable')],
            'question': 'Which is a VEGETABLE?',
            'correct': 'Carrot'
        }
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        scenario = sorting_scenarios[i % len(sorting_scenarios)]
        
        svg_content = f'<text x="200" y="30" text-anchor="middle" font-size="14" font-weight="bold">{scenario["title"]}</text>'
        
        for j, (item, cat) in enumerate(scenario['items']):
            x = 50 + (j % 2) * 180
            y = 60 + (j // 2) * 50
            svg_content += f'<text x="{x}" y="{y}" font-size="14">{item} - {cat}</text>'
        
        svg = create_svg_wrapper(svg_content)
        
        options = [item for item, _ in scenario['items']]
        random.shuffle(options)
        
        questions.append({
            'question_text': scenario['question'],
            'options': json.dumps(options),
            'correct_answer': scenario['correct'],
            'explanation': f'{scenario["correct"]} is the answer!',
            'visual_data': svg
        })
    
    return questions

def generate_level_12_questions():
    """Level 12: Measure Challenge - Mixed measurement problems (4 options)"""
    questions = []
    
    challenge_types = ['size', 'length', 'weight', 'capacity', 'money', 'data']
    
    for i in range(QUESTIONS_PER_LEVEL):
        c_type = challenge_types[i % len(challenge_types)]
        
        if c_type == 'size':
            sizes = [30, 50, 70]
            random.shuffle(sizes)
            
            svg_content = ''
            for j, size in enumerate(sizes):
                svg_content += svg_circle(60 + j*110, 90 - size//2, size, COLOURS['blue'])
                svg_content += f'<text x="{60 + j*110 + size//2}" y="150" text-anchor="middle" font-size="12">{["A", "B", "C"][j]}</text>'
            svg = create_svg_wrapper(svg_content)
            
            size_to_label = {sizes[j]: ["A", "B", "C"][j] for j in range(3)}
            correct = size_to_label[70]
            
            questions.append({
                'question_text': 'Which is BIGGEST?',
                'options': json.dumps(['A', 'B', 'C', 'All same']),
                'correct_answer': correct,
                'explanation': f'{correct} is the biggest!',
                'visual_data': svg
            })
            
        elif c_type == 'length':
            svg_content = f'<line x1="50" y1="70" x2="200" y2="70" stroke="{COLOURS["blue"]}" stroke-width="6"/>'
            svg_content += f'<line x1="50" y1="110" x2="120" y2="110" stroke="{COLOURS["red"]}" stroke-width="6"/>'
            svg_content += f'<text x="30" y="75" font-size="12">A</text>'
            svg_content += f'<text x="30" y="115" font-size="12">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            questions.append({
                'question_text': 'Which line is LONGER?',
                'options': json.dumps(['A', 'B', 'Same length', 'Cannot tell']),
                'correct_answer': 'A',
                'explanation': 'Line A is longer!',
                'visual_data': svg
            })
            
        elif c_type == 'weight':
            svg_content = svg_rock(100, 80)
            svg_content += svg_feather(260, 70)
            svg = create_svg_wrapper(svg_content)
            
            questions.append({
                'question_text': 'Which is HEAVIER?',
                'options': json.dumps(['Rock', 'Feather', 'Same weight', 'Cannot tell']),
                'correct_answer': 'Rock',
                'explanation': 'The rock is heavier!',
                'visual_data': svg
            })
            
        elif c_type == 'capacity':
            svg_content = svg_glass(100, 50, 'full')
            svg_content += svg_glass(220, 50, 'empty')
            svg_content += f'<text x="120" y="150" text-anchor="middle" font-size="12">A</text>'
            svg_content += f'<text x="240" y="150" text-anchor="middle" font-size="12">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            questions.append({
                'question_text': 'Which glass is FULL?',
                'options': json.dumps(['A', 'B', 'Both', 'Neither']),
                'correct_answer': 'A',
                'explanation': 'Glass A is full!',
                'visual_data': svg
            })
            
        elif c_type == 'money':
            coin1 = IRISH_COINS[4]  # 20 cent
            coin2 = IRISH_COINS[2]  # 5 cent
            
            svg_content = svg_coin(100, 60, coin1)
            svg_content += svg_coin(220, 60, coin2)
            svg_content += f'<text x="130" y="130" text-anchor="middle" font-size="12">A</text>'
            svg_content += f'<text x="250" y="130" text-anchor="middle" font-size="12">B</text>'
            svg = create_svg_wrapper(svg_content)
            
            questions.append({
                'question_text': 'Which coin is worth MORE?',
                'options': json.dumps(['A', 'B', 'Same value', 'Cannot tell']),
                'correct_answer': 'A',
                'explanation': '20 cent is worth more than 5 cent!',
                'visual_data': svg
            })
            
        else:  # data
            counts = {'Red': random.randint(2, 5), 'Blue': random.randint(2, 5), 'Green': random.randint(2, 5)}
            
            svg_content = f'<text x="200" y="25" text-anchor="middle" font-size="12" font-weight="bold">Favourite Colours</text>'
            for j, (colour, count) in enumerate(counts.items()):
                y = 45 + j * 35
                svg_content += f'<text x="30" y="{y + 12}" font-size="11">{colour}</text>'
                svg_content += svg_pictograph_row(80, y, count, 'square', COLOURS[colour.lower()])
            svg = create_svg_wrapper(svg_content)
            
            max_colour = max(counts, key=counts.get)
            
            questions.append({
                'question_text': 'Which colour is MOST popular?',
                'options': json.dumps(list(counts.keys()) + ['All same']),
                'correct_answer': max_colour,
                'explanation': f'{max_colour} is most popular!',
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
        required = ['question_text', 'options', 'correct_answer', 'level', 'topic', 'mode']
        for field in required:
            if field not in q or not q[field]:
                errors.append(f"Question {i}: Missing {field}")
        
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
    
    cursor.execute('''
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
    ''', (TOPIC, MODE))
    deleted = cursor.rowcount
    print(f"  Removed {deleted} existing questions")
    
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
    
    print(f"\nGenerating questions...")
    questions = generate_all_questions()
    
    if not validate_questions(questions):
        print("\n✗ Validation failed. Aborting.")
        exit(1)
    
    insert_questions(questions)
    success = verify_insertion()
    
    print("\n" + "=" * 60)
    if success:
        print("✓ COMPLETE! All questions generated successfully.")
    else:
        print("✗ INCOMPLETE. Please check errors above.")
    print("=" * 60)
