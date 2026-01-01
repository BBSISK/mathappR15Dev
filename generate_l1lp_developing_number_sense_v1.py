"""
AgentMath L1LP Question Generator
Topic: Developing Number Sense
Learning Outcomes: 2.13 - 2.17
Version: 1.0

Generates 600 questions (50 per level × 12 levels) for the L1LP strand.
Focus: Counting to 5/10/20, recognising numerals, matching, more/less, one more/less, combining, taking away.

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
TOPIC = 'developing_number_sense'
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
    'purple': '#9B59B6'
}

# =============================================================================
# SVG GENERATION FUNCTIONS
# =============================================================================

def svg_dot(x, y, size=30, colour='#3498DB'):
    """Generate a single dot/circle"""
    return f'<circle cx="{x}" cy="{y}" r="{size//2}" fill="{colour}"/>'

def svg_apple(x, y, size=40):
    """Generate an apple"""
    return f'''<g transform="translate({x},{y})">
        <ellipse cx="{size//2}" cy="{size//2 + 3}" rx="{size//2 - 2}" ry="{size//2}" fill="#E74C3C"/>
        <rect x="{size//2 - 2}" y="0" width="4" height="8" fill="#8B4513"/>
        <ellipse cx="{size//2 + 5}" cy="5" rx="5" ry="3" fill="#27AE60"/>
    </g>'''

def svg_star(x, y, size=40, colour='#F1C40F'):
    """Generate a star"""
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

def svg_ball(x, y, size=40, colour='#3498DB'):
    """Generate a ball"""
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//2}" cy="{size//2}" r="{size//2 - 2}" fill="{colour}"/>
        <path d="M{size//4},{size//3} Q{size//2},{size//5} {size*3//4},{size//3}" stroke="white" stroke-width="2" fill="none"/>
    </g>'''

def svg_cookie(x, y, size=40):
    """Generate a cookie"""
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//2}" cy="{size//2}" r="{size//2 - 2}" fill="#D4A574"/>
        <circle cx="{size//3}" cy="{size//3}" r="3" fill="#5D4037"/>
        <circle cx="{size*2//3}" cy="{size//3}" r="3" fill="#5D4037"/>
        <circle cx="{size//2}" cy="{size*2//3}" r="3" fill="#5D4037"/>
    </g>'''

def svg_flower(x, y, size=40):
    """Generate a flower"""
    cx, cy = x + size//2, y + size//2
    petals = ''
    for i in range(5):
        angle = i * 72 * math.pi / 180
        px = cx + (size//3) * math.cos(angle)
        py = cy + (size//3) * math.sin(angle)
        petals += f'<circle cx="{px}" cy="{py}" r="{size//5}" fill="#FF69B4"/>'
    return f'{petals}<circle cx="{cx}" cy="{cy}" r="{size//5}" fill="#F1C40F"/>'

def svg_bird(x, y, size=40):
    """Generate a simple bird"""
    return f'''<g transform="translate({x},{y})">
        <ellipse cx="{size//2}" cy="{size//2}" rx="{size//3}" ry="{size//4}" fill="#3498DB"/>
        <circle cx="{size*2//3}" cy="{size//3}" r="{size//6}" fill="#3498DB"/>
        <polygon points="{size*5//6},{size//3} {size},{size//3} {size*5//6},{size//2}" fill="#E67E22"/>
        <circle cx="{size*3//4}" cy="{size//3}" r="2" fill="black"/>
    </g>'''

def get_counting_object_svg(obj_type, x, y, size=40):
    """Get SVG for counting objects"""
    if obj_type == 'apple':
        return svg_apple(x, y, size)
    elif obj_type == 'star':
        return svg_star(x, y, size)
    elif obj_type == 'ball':
        return svg_ball(x, y, size)
    elif obj_type == 'cookie':
        return svg_cookie(x, y, size)
    elif obj_type == 'flower':
        return svg_flower(x, y, size)
    elif obj_type == 'bird':
        return svg_bird(x, y, size)
    else:
        return svg_dot(x + size//2, y + size//2, size, '#3498DB')

def create_counting_svg(count, obj_type='dot', max_per_row=5, size=35):
    """Create SVG with objects arranged for counting"""
    spacing = size + 10
    rows = (count - 1) // max_per_row + 1
    
    width = min(count, max_per_row) * spacing + 60
    height = rows * spacing + 60
    
    svg_content = ''
    for i in range(count):
        row = i // max_per_row
        col = i % max_per_row
        x = 30 + col * spacing
        y = 30 + row * spacing
        
        if obj_type == 'dot':
            colour = random.choice(list(COLOURS.values()))
            svg_content += svg_dot(x + size//2, y + size//2, size, colour)
        else:
            svg_content += get_counting_object_svg(obj_type, x, y, size)
    
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{svg_content}</svg>'

def create_numeral_svg(numeral, size=80):
    """Create SVG showing a large numeral"""
    width = 150
    height = 120
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">
        <text x="{width//2}" y="{height//2 + size//3}" text-anchor="middle" font-size="{size}" font-weight="bold" fill="#3498DB">{numeral}</text>
    </svg>'''

def create_comparison_svg(count1, count2, obj_type='dot'):
    """Create SVG showing two groups for comparison"""
    spacing = 40
    max_per_row = 5
    
    # Calculate dimensions for each group
    rows1 = (count1 - 1) // max_per_row + 1 if count1 > 0 else 1
    rows2 = (count2 - 1) // max_per_row + 1 if count2 > 0 else 1
    
    group_width = max_per_row * spacing + 20
    height = max(rows1, rows2) * spacing + 80
    width = group_width * 2 + 60
    
    svg_content = ''
    
    # Group 1 label
    svg_content += f'<text x="{group_width//2}" y="25" text-anchor="middle" font-size="14" fill="#333">Group A</text>'
    svg_content += f'<rect x="10" y="35" width="{group_width}" height="{height - 50}" fill="#f0f8ff" stroke="#3498DB" rx="5"/>'
    
    # Group 1 objects
    for i in range(count1):
        row = i // max_per_row
        col = i % max_per_row
        x = 20 + col * spacing
        y = 45 + row * spacing
        svg_content += svg_dot(x + 15, y + 15, 30, '#3498DB')
    
    # Group 2 label
    svg_content += f'<text x="{group_width + 40 + group_width//2}" y="25" text-anchor="middle" font-size="14" fill="#333">Group B</text>'
    svg_content += f'<rect x="{group_width + 40}" y="35" width="{group_width}" height="{height - 50}" fill="#fff0f5" stroke="#E74C3C" rx="5"/>'
    
    # Group 2 objects
    for i in range(count2):
        row = i // max_per_row
        col = i % max_per_row
        x = group_width + 50 + col * spacing
        y = 45 + row * spacing
        svg_content += svg_dot(x + 15, y + 15, 30, '#E74C3C')
    
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{svg_content}</svg>'

def create_addition_svg(count1, count2, obj_type='apple'):
    """Create SVG showing addition scenario"""
    total = count1 + count2
    spacing = 40
    width = max(total, 5) * spacing + 80
    height = 150
    
    svg_content = ''
    
    # First group
    svg_content += f'<text x="{(count1 * spacing)//2 + 20}" y="25" text-anchor="middle" font-size="12" fill="#333">You have {count1}</text>'
    for i in range(count1):
        svg_content += get_counting_object_svg(obj_type, 20 + i * spacing, 35, 35)
    
    # Plus sign
    plus_x = count1 * spacing + 30
    svg_content += f'<text x="{plus_x}" y="60" font-size="24" fill="#27AE60">+</text>'
    
    # Second group
    svg_content += f'<text x="{plus_x + 20 + (count2 * spacing)//2}" y="25" text-anchor="middle" font-size="12" fill="#333">{count2} more come</text>'
    for i in range(count2):
        svg_content += get_counting_object_svg(obj_type, plus_x + 20 + i * spacing, 35, 35)
    
    # Question
    svg_content += f'<text x="{width//2}" y="120" text-anchor="middle" font-size="14" fill="#333">How many altogether?</text>'
    
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{svg_content}</svg>'

def create_subtraction_svg(start_count, take_away, obj_type='cookie'):
    """Create SVG showing subtraction scenario"""
    spacing = 40
    width = max(start_count, 5) * spacing + 60
    height = 150
    
    svg_content = ''
    
    # Starting group
    svg_content += f'<text x="{width//2}" y="20" text-anchor="middle" font-size="12" fill="#333">You have {start_count}</text>'
    
    remaining = start_count - take_away
    for i in range(start_count):
        x = 20 + i * spacing
        if i < remaining:
            svg_content += get_counting_object_svg(obj_type, x, 30, 35)
        else:
            # Crossed out items
            svg_content += get_counting_object_svg(obj_type, x, 30, 35)
            svg_content += f'<line x1="{x}" y1="30" x2="{x + 35}" y2="65" stroke="#E74C3C" stroke-width="3"/>'
            svg_content += f'<line x1="{x + 35}" y1="30" x2="{x}" y2="65" stroke="#E74C3C" stroke-width="3"/>'
    
    # Explanation
    svg_content += f'<text x="{width//2}" y="90" text-anchor="middle" font-size="12" fill="#E74C3C">{take_away} go away</text>'
    svg_content += f'<text x="{width//2}" y="120" text-anchor="middle" font-size="14" fill="#333">How many left?</text>'
    
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{svg_content}</svg>'

def create_svg_wrapper(content, width=400, height=150):
    """Wrap SVG content"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

# =============================================================================
# QUESTION GENERATORS BY LEVEL
# =============================================================================

def generate_level_1_questions():
    """Level 1: Counting to 5 - Count small groups (2 options)"""
    questions = []
    
    objects = ['apple', 'star', 'ball', 'dot']
    
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(1, 5)
        obj_type = random.choice(objects)
        
        svg = create_counting_svg(count, obj_type, max_per_row=5, size=40)
        
        # Create wrong answer (off by 1)
        wrong = count + 1 if count < 5 else count - 1
        
        options = [str(count), str(wrong)]
        random.shuffle(options)
        
        obj_word = 'dots' if obj_type == 'dot' else f'{obj_type}s' if count > 1 else obj_type
        
        questions.append({
            'question_text': f'How many {obj_word}?',
            'options': json.dumps(options),
            'correct_answer': str(count),
            'explanation': f'Count each one: 1, 2{"".join([f", {j}" for j in range(3, count+1)])}. There are {count}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_2_questions():
    """Level 2: Counting to 10 - Count larger groups (2-3 options)"""
    questions = []
    
    objects = ['apple', 'star', 'ball', 'cookie', 'dot']
    
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(5, 10)
        obj_type = random.choice(objects)
        
        svg = create_counting_svg(count, obj_type, max_per_row=5, size=35)
        
        # Create wrong answers
        wrong1 = count + 1 if count < 10 else count - 1
        wrong2 = count - 1 if count > 5 else count + 2
        
        options = [str(count), str(wrong1)]
        if i % 2 == 0:
            options.append(str(wrong2))
        random.shuffle(options)
        
        questions.append({
            'question_text': 'How many can you count?',
            'options': json.dumps(options),
            'correct_answer': str(count),
            'explanation': f'Count carefully! There are {count}.',
            'visual_data': svg
        })
    
    return questions

def generate_level_3_questions():
    """Level 3: Recognising Numerals - Match number symbols (3 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            # Show numeral, ask for name
            num = random.randint(1, 10)
            svg = create_numeral_svg(num)
            
            wrong1 = num + 1 if num < 10 else num - 2
            wrong2 = num - 1 if num > 1 else num + 2
            
            number_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                          6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
            
            correct = number_words[num]
            options = [correct, number_words[wrong1], number_words[wrong2]]
            random.shuffle(options)
            
            questions.append({
                'question_text': 'What number is this?',
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'This is the number {num} - "{correct}"!',
                'visual_data': svg
            })
        else:
            # Show word, ask for numeral
            num = random.randint(1, 10)
            number_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                          6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
            
            word = number_words[num]
            svg_content = f'<text x="200" y="80" text-anchor="middle" font-size="36" fill="#333">{word}</text>'
            svg = create_svg_wrapper(svg_content)
            
            wrong1 = num + 1 if num < 10 else num - 2
            wrong2 = num - 1 if num > 1 else num + 2
            
            options = [str(num), str(wrong1), str(wrong2)]
            random.shuffle(options)
            
            questions.append({
                'question_text': f'Which numeral shows "{word}"?',
                'options': json.dumps(options),
                'correct_answer': str(num),
                'explanation': f'"{word}" is written as {num}!',
                'visual_data': svg
            })
    
    return questions

def generate_level_4_questions():
    """Level 4: Matching Numbers - Match numerals to quantities (3 options)"""
    questions = []
    
    objects = ['apple', 'star', 'ball', 'cookie']
    
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(1, 10)
        obj_type = random.choice(objects)
        
        svg = create_counting_svg(count, obj_type, max_per_row=5, size=35)
        
        wrong1 = count + 1 if count < 10 else count - 2
        wrong2 = count - 1 if count > 1 else count + 2
        
        options = [str(count), str(wrong1), str(wrong2)]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'Which number matches?',
            'options': json.dumps(options),
            'correct_answer': str(count),
            'explanation': f'Count them: there are {count}. So the number is {count}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_5_questions():
    """Level 5: More or Less - Compare two groups (3-4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        count1 = random.randint(1, 8)
        count2 = random.randint(1, 8)
        while count1 == count2:
            count2 = random.randint(1, 8)
        
        svg = create_comparison_svg(count1, count2)
        
        if i % 2 == 0:
            # Which has more?
            correct = 'Group A' if count1 > count2 else 'Group B'
            question = 'Which group has MORE?'
            explanation = f'Group A has {count1}, Group B has {count2}. {correct} has more!'
        else:
            # Which has less?
            correct = 'Group A' if count1 < count2 else 'Group B'
            question = 'Which group has LESS?'
            explanation = f'Group A has {count1}, Group B has {count2}. {correct} has less!'
        
        options = ['Group A', 'Group B', 'Same', 'Not sure']
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_6_questions():
    """Level 6: Same Amount - Find equal groups (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        target_count = random.randint(2, 6)
        
        if i % 3 == 0:
            # Groups are the same
            count1 = target_count
            count2 = target_count
            correct = 'Yes, same amount'
        else:
            # Groups are different
            count1 = target_count
            count2 = target_count + random.choice([-2, -1, 1, 2])
            count2 = max(1, min(8, count2))
            if count2 == count1:
                count2 = count1 + 1
            correct = 'No, different amounts'
        
        svg = create_comparison_svg(count1, count2)
        
        options = ['Yes, same amount', 'No, different amounts', 'Group A has more', 'Group B has more']
        
        questions.append({
            'question_text': 'Do both groups have the SAME amount?',
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'Group A has {count1}, Group B has {count2}. {"They\'re the same!" if count1 == count2 else "They\'re different!"}',
            'visual_data': svg
        })
    
    return questions

def generate_level_7_questions():
    """Level 7: One More - Find one more than a number (4 options)"""
    questions = []
    
    objects = ['apple', 'star', 'ball', 'cookie', 'flower']
    
    for i in range(QUESTIONS_PER_LEVEL):
        start = random.randint(1, 9)
        obj_type = random.choice(objects)
        correct = start + 1
        
        svg = create_counting_svg(start, obj_type, max_per_row=5, size=35)
        
        options = [str(correct), str(start), str(start + 2), str(max(1, start - 1))]
        options = list(set(options))  # Remove duplicates
        while len(options) < 4:
            options.append(str(random.randint(1, 10)))
        options = options[:4]
        random.shuffle(options)
        
        questions.append({
            'question_text': f'There are {start}. What is ONE MORE than {start}?',
            'options': json.dumps(options),
            'correct_answer': str(correct),
            'explanation': f'{start} and one more makes {correct}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_8_questions():
    """Level 8: One Less - Find one less than a number (4 options)"""
    questions = []
    
    objects = ['apple', 'star', 'ball', 'cookie', 'flower']
    
    for i in range(QUESTIONS_PER_LEVEL):
        start = random.randint(2, 10)
        obj_type = random.choice(objects)
        correct = start - 1
        
        svg = create_counting_svg(start, obj_type, max_per_row=5, size=35)
        
        options = [str(correct), str(start), str(start + 1), str(max(1, start - 2))]
        options = list(set(options))
        while len(options) < 4:
            options.append(str(random.randint(1, 10)))
        options = options[:4]
        random.shuffle(options)
        
        questions.append({
            'question_text': f'There are {start}. What is ONE LESS than {start}?',
            'options': json.dumps(options),
            'correct_answer': str(correct),
            'explanation': f'{start} take away one is {correct}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_9_questions():
    """Level 9: Counting to 20 - Count larger groups (4 options)"""
    questions = []
    
    objects = ['dot', 'star', 'ball']
    
    for i in range(QUESTIONS_PER_LEVEL):
        count = random.randint(11, 20)
        obj_type = random.choice(objects)
        
        svg = create_counting_svg(count, obj_type, max_per_row=5, size=30)
        
        wrong1 = count + 1 if count < 20 else count - 1
        wrong2 = count - 1 if count > 11 else count + 2
        wrong3 = count + 2 if count < 19 else count - 2
        
        options = [str(count), str(wrong1), str(wrong2), str(wrong3)]
        options = list(set(options))[:4]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'Count carefully. How many are there?',
            'options': json.dumps(options),
            'correct_answer': str(count),
            'explanation': f'Count in rows: 5, 10, 15... There are {count}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_10_questions():
    """Level 10: Simple Combining - Basic addition concept (4 options)"""
    questions = []
    
    objects = ['apple', 'cookie', 'star', 'ball']
    
    for i in range(QUESTIONS_PER_LEVEL):
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        total = num1 + num2
        obj_type = random.choice(objects)
        
        svg = create_addition_svg(num1, num2, obj_type)
        
        options = [str(total), str(total + 1), str(total - 1), str(num1)]
        options = list(set(options))
        while len(options) < 4:
            options.append(str(random.randint(1, 12)))
        options = options[:4]
        random.shuffle(options)
        
        obj_word = f'{obj_type}s'
        
        questions.append({
            'question_text': f'You have {num1} {obj_word}. {num2} more come. How many altogether?',
            'options': json.dumps(options),
            'correct_answer': str(total),
            'explanation': f'{num1} and {num2} more makes {total} altogether!',
            'visual_data': svg
        })
    
    return questions

def generate_level_11_questions():
    """Level 11: Simple Taking Away - Basic subtraction concept (4 options)"""
    questions = []
    
    objects = ['cookie', 'apple', 'ball', 'star']
    scenarios = [
        ('You eat', 'How many left?'),
        ('Some fly away.', 'How many left?'),
        ('You give away', 'How many left?'),
        ('Some roll away.', 'How many left?')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        start = random.randint(3, 8)
        take_away = random.randint(1, start - 1)
        remaining = start - take_away
        obj_type = random.choice(objects)
        scenario = scenarios[i % len(scenarios)]
        
        svg = create_subtraction_svg(start, take_away, obj_type)
        
        options = [str(remaining), str(remaining + 1), str(remaining - 1) if remaining > 1 else '0', str(start)]
        options = list(set(options))
        while len(options) < 4:
            options.append(str(random.randint(0, 10)))
        options = options[:4]
        random.shuffle(options)
        
        obj_word = f'{obj_type}s'
        
        questions.append({
            'question_text': f'You have {start} {obj_word}. {take_away} go away. {scenario[1]}',
            'options': json.dumps(options),
            'correct_answer': str(remaining),
            'explanation': f'{start} take away {take_away} leaves {remaining}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_12_questions():
    """Level 12: Number Challenge - Mixed number skills (4 options)"""
    questions = []
    
    challenge_types = ['count', 'compare', 'one_more', 'one_less', 'combine', 'take_away']
    
    for i in range(QUESTIONS_PER_LEVEL):
        c_type = challenge_types[i % len(challenge_types)]
        
        if c_type == 'count':
            count = random.randint(10, 20)
            svg = create_counting_svg(count, 'dot', max_per_row=5, size=28)
            options = [str(count), str(count+1), str(count-1), str(count+2)]
            random.shuffle(options)
            
            questions.append({
                'question_text': 'How many dots?',
                'options': json.dumps(options),
                'correct_answer': str(count),
                'explanation': f'There are {count} dots!',
                'visual_data': svg
            })
            
        elif c_type == 'compare':
            c1 = random.randint(3, 8)
            c2 = random.randint(3, 8)
            while c1 == c2:
                c2 = random.randint(3, 8)
            
            svg = create_comparison_svg(c1, c2)
            correct = 'Group A' if c1 > c2 else 'Group B'
            options = ['Group A', 'Group B', 'Same', 'Cannot tell']
            
            questions.append({
                'question_text': 'Which group has MORE?',
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'A has {c1}, B has {c2}. {correct} has more!',
                'visual_data': svg
            })
            
        elif c_type == 'one_more':
            num = random.randint(5, 15)
            svg_content = f'<text x="200" y="80" text-anchor="middle" font-size="48" fill="#3498DB">{num}</text>'
            svg = create_svg_wrapper(svg_content)
            
            correct = num + 1
            options = [str(correct), str(num), str(num+2), str(num-1)]
            random.shuffle(options)
            
            questions.append({
                'question_text': f'What is ONE MORE than {num}?',
                'options': json.dumps(options),
                'correct_answer': str(correct),
                'explanation': f'{num} + 1 = {correct}!',
                'visual_data': svg
            })
            
        elif c_type == 'one_less':
            num = random.randint(5, 15)
            svg_content = f'<text x="200" y="80" text-anchor="middle" font-size="48" fill="#E74C3C">{num}</text>'
            svg = create_svg_wrapper(svg_content)
            
            correct = num - 1
            options = [str(correct), str(num), str(num+1), str(num-2)]
            random.shuffle(options)
            
            questions.append({
                'question_text': f'What is ONE LESS than {num}?',
                'options': json.dumps(options),
                'correct_answer': str(correct),
                'explanation': f'{num} - 1 = {correct}!',
                'visual_data': svg
            })
            
        elif c_type == 'combine':
            n1 = random.randint(2, 6)
            n2 = random.randint(2, 6)
            total = n1 + n2
            
            svg = create_addition_svg(n1, n2, 'star')
            options = [str(total), str(total+1), str(total-1), str(n1)]
            random.shuffle(options)
            
            questions.append({
                'question_text': f'{n1} stars and {n2} more. How many altogether?',
                'options': json.dumps(options),
                'correct_answer': str(total),
                'explanation': f'{n1} + {n2} = {total}!',
                'visual_data': svg
            })
            
        else:  # take_away
            start = random.randint(5, 10)
            away = random.randint(1, 4)
            left = start - away
            
            svg = create_subtraction_svg(start, away, 'cookie')
            options = [str(left), str(left+1), str(left-1) if left > 0 else '0', str(start)]
            random.shuffle(options)
            
            questions.append({
                'question_text': f'{start} cookies, {away} eaten. How many left?',
                'options': json.dumps(options),
                'correct_answer': str(left),
                'explanation': f'{start} - {away} = {left}!',
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
