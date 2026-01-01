"""
AgentMath L2LP Question Generator V3
Topic: Number & Money (l2_number_and_money)
NCCA Module: Understanding number and money

V3: Completely rewritten with UNIQUE question texts per level.
Each question includes specific details (numbers, colours, objects) in the text.

Generates 600 questions (50 per level × 12 levels) for the L2LP strand.

Author: AgentMath Generator
Version: 3.0
Date: December 2025
"""

import sqlite3
import random
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'l2_number_and_money'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

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
        return 'linked'

# ============================================================
# COLOUR PALETTE
# ============================================================

COLOURS = {
    'red': '#dc2626',
    'blue': '#3b82f6',
    'green': '#22c55e',
    'yellow': '#eab308',
    'purple': '#8b5cf6',
    'orange': '#f97316',
    'pink': '#ec4899'
}

COLOUR_NAMES = list(COLOURS.keys())

# ============================================================
# SVG GENERATION FUNCTIONS
# ============================================================

def generate_counting_svg(count, shape='circle', colour='blue'):
    """Generate SVG with objects to count"""
    hex_colour = COLOURS.get(colour, '#3b82f6')
    
    svg_parts = [f'<svg viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg">']
    svg_parts.append('<rect width="200" height="120" fill="#f8fafc"/>')
    
    positions = []
    for i in range(count):
        x = 20 + (i % 5) * 36
        y = 25 + (i // 5) * 35
        positions.append((x, y))
    
    for x, y in positions:
        if shape == 'circle':
            svg_parts.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{hex_colour}"/>')
        elif shape == 'square':
            svg_parts.append(f'<rect x="{x-10}" y="{y-10}" width="20" height="20" fill="{hex_colour}"/>')
        elif shape == 'star':
            svg_parts.append(f'<polygon points="{x},{y-12} {x+4},{y-4} {x+12},{y-4} {x+6},{y+2} {x+8},{y+12} {x},{y+6} {x-8},{y+12} {x-6},{y+2} {x-12},{y-4} {x-4},{y-4}" fill="{hex_colour}"/>')
        elif shape == 'triangle':
            svg_parts.append(f'<polygon points="{x},{y-12} {x+12},{y+10} {x-12},{y+10}" fill="{hex_colour}"/>')
        elif shape == 'heart':
            svg_parts.append(f'<path d="M{x},{y+8} C{x-12},{y-8} {x},{y-12} {x},{y-4} C{x},{y-12} {x+12},{y-8} {x},{y+8}Z" fill="{hex_colour}"/>')
    
    svg_parts.append('</svg>')
    return ''.join(svg_parts)


def generate_place_value_svg(number):
    """Generate place value blocks visualization"""
    tens = number // 10
    ones = number % 10
    
    svg = f'''<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="100" fill="#f8fafc"/>
    <text x="10" y="20" font-size="12" fill="#374151">Tens</text>
    <text x="120" y="20" font-size="12" fill="#374151">Ones</text>'''
    
    # Draw tens blocks (tall rectangles)
    for i in range(tens):
        x = 10 + i * 12
        svg += f'<rect x="{x}" y="25" width="10" height="50" fill="#3b82f6" stroke="#1e40af"/>'
    
    # Draw ones blocks (small squares)
    for i in range(ones):
        x = 120 + (i % 5) * 12
        y = 25 + (i // 5) * 12
        svg += f'<rect x="{x}" y="{y}" width="10" height="10" fill="#22c55e" stroke="#166534"/>'
    
    svg += '</svg>'
    return svg


def generate_money_svg(coins_cents, notes_euros=None):
    """Generate money visualization"""
    svg = '<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">'
    svg += '<rect width="200" height="100" fill="#f8fafc"/>'
    
    x_pos = 10
    
    # Draw notes
    if notes_euros:
        for note in notes_euros:
            colour = {'5': '#a3a3a3', '10': '#f97316', '20': '#3b82f6', '50': '#f59e0b'}.get(str(note), '#22c55e')
            svg += f'<rect x="{x_pos}" y="10" width="40" height="25" fill="{colour}" rx="3"/>'
            svg += f'<text x="{x_pos+20}" y="27" font-size="12" fill="white" text-anchor="middle">€{note}</text>'
            x_pos += 45
    
    # Draw coins
    y_pos = 50 if notes_euros else 30
    x_pos = 10
    for coin in coins_cents:
        if coin >= 100:
            # Euro coins
            svg += f'<circle cx="{x_pos+12}" cy="{y_pos+12}" r="12" fill="#f59e0b" stroke="#ca8a04"/>'
            svg += f'<text x="{x_pos+12}" y="{y_pos+16}" font-size="9" fill="white" text-anchor="middle">€{coin//100}</text>'
        else:
            # Cent coins
            radius = 8 if coin < 10 else 10
            svg += f'<circle cx="{x_pos+12}" cy="{y_pos+12}" r="{radius}" fill="#d97706" stroke="#b45309"/>'
            svg += f'<text x="{x_pos+12}" y="{y_pos+16}" font-size="8" fill="white" text-anchor="middle">{coin}c</text>'
        x_pos += 28
    
    svg += '</svg>'
    return svg


def generate_number_line_svg(start, end, highlight=None):
    """Generate a number line"""
    svg = '<svg viewBox="0 0 200 60" xmlns="http://www.w3.org/2000/svg">'
    svg += '<rect width="200" height="60" fill="#f8fafc"/>'
    svg += '<line x1="10" y1="30" x2="190" y2="30" stroke="#374151" stroke-width="2"/>'
    
    num_marks = min(end - start + 1, 11)
    step = (end - start) / (num_marks - 1) if num_marks > 1 else 1
    
    for i in range(num_marks):
        x = 10 + (i * 180 / (num_marks - 1)) if num_marks > 1 else 100
        num = int(start + i * step)
        svg += f'<line x1="{x}" y1="25" x2="{x}" y2="35" stroke="#374151" stroke-width="2"/>'
        
        if highlight and num == highlight:
            svg += f'<circle cx="{x}" cy="30" r="8" fill="#ef4444"/>'
            svg += f'<text x="{x}" y="50" font-size="10" fill="#ef4444" text-anchor="middle" font-weight="bold">{num}</text>'
        else:
            svg += f'<text x="{x}" y="50" font-size="10" fill="#374151" text-anchor="middle">{num}</text>'
    
    svg += '</svg>'
    return svg


def generate_price_tag_svg(price, item_name):
    """Generate a price tag visualization"""
    svg = f'''<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="100" fill="#f8fafc"/>
    <rect x="40" y="15" width="120" height="70" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="5"/>
    <circle cx="50" cy="25" r="5" fill="#f59e0b"/>
    <text x="100" y="45" font-size="12" fill="#374151" text-anchor="middle">{item_name}</text>
    <text x="100" y="70" font-size="18" fill="#dc2626" text-anchor="middle" font-weight="bold">€{price:.2f}</text>
    </svg>'''
    return svg


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1_questions():
    """Level 1: Numbers in Real Life - 50 unique questions"""
    questions = []
    
    # Template 1: Where do we see number X? (10 questions)
    locations = [
        ('on a bus', 'Bus numbers tell us which route'),
        ('on a clock', 'Clocks show us the time'),
        ('on a phone', 'Phones have number keypads'),
        ('on a door', 'Door numbers tell us the address'),
        ('on a calendar', 'Calendars show dates with numbers'),
        ('on a price tag', 'Price tags show how much things cost'),
        ('on a scoreboard', 'Scoreboards show game scores'),
        ('on a speed sign', 'Speed signs show speed limits'),
        ('on a birthday cake', 'Birthday cakes show age'),
        ('on a ruler', 'Rulers measure length with numbers')
    ]
    
    for i, (location, explanation) in enumerate(locations):
        number = random.randint(1, 50)
        questions.append({
            'question_text': f"Where might you see the number {number}? Choose the best answer.",
            'options': [location, 'in the sky', 'underwater', 'nowhere'],
            'correct_index': 0,
            'explanation': explanation
        })
    
    # Template 2: Count specific coloured shapes (25 questions)
    shapes = ['circle', 'square', 'star', 'triangle', 'heart']
    
    for i in range(25):
        count = random.randint(2, 10)
        shape = shapes[i % len(shapes)]
        colour = COLOUR_NAMES[i % len(COLOUR_NAMES)]
        
        wrong1 = count + random.randint(1, 3)
        wrong2 = max(1, count - random.randint(1, 2))
        wrong3 = count + random.randint(4, 6)
        
        options = [str(count), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(count))
        
        questions.append({
            'question_text': f"Count the {colour} {shape}s in the picture. There are exactly ___ of them.",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"There are {count} {colour} {shape}s in the picture.",
            'image_svg': generate_counting_svg(count, shape, colour)
        })
    
    # Template 3: What number comes after X? (10 questions)
    for i in range(10):
        num = random.randint(1, 20) + i  # Ensure different numbers
        correct = num + 1
        wrong1 = num - 1
        wrong2 = num + 2
        wrong3 = num
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"What number comes right after {num}? Count: {num}, ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"After {num} comes {correct}. We count {num}, {correct}."
        })
    
    # Template 4: What number comes before X? (5 questions)
    for i in range(5):
        num = random.randint(5, 25) + i * 3
        correct = num - 1
        wrong1 = num + 1
        wrong2 = num - 2
        wrong3 = num
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"What number comes just before {num}? ___, {num}",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Before {num} comes {correct}. We count {correct}, {num}."
        })
    
    return questions[:50]


def generate_level_2_questions():
    """Level 2: Counting Skills - 50 unique questions"""
    questions = []
    
    # Template 1: Count larger groups with images (20 questions)
    shapes = ['circle', 'square', 'star', 'triangle', 'heart']
    
    for i in range(20):
        count = 8 + i  # 8 to 27 - all different counts
        if count > 15:
            count = 8 + (i % 8)  # Wrap around for reasonable display
        shape = shapes[i % len(shapes)]
        colour = COLOUR_NAMES[i % len(COLOUR_NAMES)]
        
        wrong1 = count + 1
        wrong2 = count - 1
        wrong3 = count + 2
        
        options = [str(count), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(count))
        
        questions.append({
            'question_text': f"Look carefully and count every {colour} {shape}. How many {shape}s are there in total?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"If you count carefully, there are exactly {count} {colour} {shape}s.",
            'image_svg': generate_counting_svg(count, shape, colour)
        })
    
    # Template 2: More or less comparisons (15 questions)
    comparisons = [
        (7, 5, 'more', '7 is bigger than 5'),
        (3, 8, 'fewer', '3 is smaller than 8'),
        (12, 9, 'more', '12 is bigger than 9'),
        (4, 11, 'fewer', '4 is smaller than 11'),
        (15, 10, 'more', '15 is bigger than 10'),
        (6, 14, 'fewer', '6 is smaller than 14'),
        (9, 6, 'more', '9 is bigger than 6'),
        (2, 7, 'fewer', '2 is smaller than 7'),
        (13, 8, 'more', '13 is bigger than 8'),
        (5, 12, 'fewer', '5 is smaller than 12'),
        (11, 7, 'more', '11 is bigger than 7'),
        (4, 9, 'fewer', '4 is smaller than 9'),
        (8, 3, 'more', '8 is bigger than 3'),
        (6, 15, 'fewer', '6 is smaller than 15'),
        (10, 4, 'more', '10 is bigger than 4')
    ]
    
    for num1, num2, answer, explanation in comparisons:
        if answer == 'more':
            q_text = f"Emma has {num1} apples. Tom has {num2} apples. Who has MORE apples?"
            options = ['Emma', 'Tom', 'They have the same', 'Cannot tell']
            correct_idx = 0
        else:
            q_text = f"Emma has {num1} apples. Tom has {num2} apples. Who has FEWER apples?"
            options = ['Emma', 'Tom', 'They have the same', 'Cannot tell']
            correct_idx = 0
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Emma has {num1}, Tom has {num2}. {explanation}."
        })
    
    # Template 3: Count on from a number (15 questions)
    count_ons = [
        (5, 3, '8'), (7, 2, '9'), (10, 4, '14'), (8, 5, '13'), (12, 3, '15'),
        (6, 4, '10'), (9, 3, '12'), (11, 2, '13'), (4, 5, '9'), (15, 3, '18'),
        (7, 4, '11'), (8, 3, '11'), (13, 2, '15'), (6, 5, '11'), (10, 5, '15')
    ]
    
    for start, add, correct in count_ons:
        wrong1 = str(int(correct) - 1)
        wrong2 = str(int(correct) + 1)
        wrong3 = str(start)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"Start at {start} and count on {add} more. What number do you reach? {start} + {add} = ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Starting at {start} and counting {add} more: {', '.join(str(start + j) for j in range(1, add + 1))}. Answer: {correct}"
        })
    
    return questions[:50]


def generate_level_3_questions():
    """Level 3: Tens and Ones - 50 unique questions"""
    questions = []
    
    # Template 1: How many tens in number X? (15 questions)
    numbers_for_tens = [14, 23, 35, 47, 52, 61, 78, 86, 94, 19, 28, 36, 45, 67, 83]
    
    for num in numbers_for_tens:
        tens = num // 10
        wrong1 = tens + 1
        wrong2 = max(0, tens - 1)
        wrong3 = num % 10
        
        options = [str(tens), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(tens))
        
        questions.append({
            'question_text': f"In the number {num}, how many TENS are there? (The first digit shows tens)",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"In {num}, the {tens} is in the tens place, so there are {tens} tens.",
            'image_svg': generate_place_value_svg(num)
        })
    
    # Template 2: How many ones in number X? (15 questions)
    numbers_for_ones = [17, 24, 38, 42, 56, 63, 71, 89, 95, 13, 26, 34, 48, 59, 82]
    
    for num in numbers_for_ones:
        ones = num % 10
        wrong1 = ones + 1 if ones < 9 else ones - 1
        wrong2 = max(0, ones - 1) if ones > 0 else ones + 2
        wrong3 = num // 10
        
        options = [str(ones), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(ones))
        
        questions.append({
            'question_text': f"In the number {num}, how many ONES are there? (The last digit shows ones)",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"In {num}, the {ones} is in the ones place, so there are {ones} ones.",
            'image_svg': generate_place_value_svg(num)
        })
    
    # Template 3: Build number from tens and ones (15 questions)
    builds = [
        (2, 5, 25), (3, 7, 37), (4, 2, 42), (5, 8, 58), (6, 1, 61),
        (7, 4, 74), (8, 3, 83), (9, 6, 96), (1, 9, 19), (2, 0, 20),
        (3, 4, 34), (4, 9, 49), (5, 5, 55), (6, 8, 68), (7, 2, 72)
    ]
    
    for tens, ones, correct in builds:
        wrong1 = correct + 10
        wrong2 = correct - 10 if correct > 10 else correct + 11
        wrong3 = int(str(ones) + str(tens)) if ones > 0 else correct + 1
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"What number has {tens} tens and {ones} ones? ({tens} × 10) + {ones} = ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{tens} tens = {tens * 10}, plus {ones} ones = {correct}.",
            'image_svg': generate_place_value_svg(correct)
        })
    
    # Template 4: Place value comparison (5 questions)
    comparisons = [
        (34, 43, 'tens', 34, "34 has 3 tens, 43 has 4 tens, so 34 has fewer tens"),
        (56, 65, 'ones', 56, "56 has 6 ones, 65 has 5 ones, so 56 has more ones"),
        (27, 72, 'tens', 72, "27 has 2 tens, 72 has 7 tens, so 72 has more tens"),
        (38, 83, 'ones', 83, "38 has 8 ones, 83 has 3 ones, so 38 has more ones"),
        (45, 54, 'tens', 54, "45 has 4 tens, 54 has 5 tens, so 54 has more tens")
    ]
    
    for num1, num2, place, answer, explanation in comparisons:
        if place == 'tens':
            q_text = f"Which number has MORE tens: {num1} or {num2}?"
        else:
            q_text = f"Which number has MORE ones: {num1} or {num2}?"
        
        options = [str(num1), str(num2), 'They are equal', 'Cannot tell']
        correct_idx = 0 if answer == num1 else 1
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_4_questions():
    """Level 4: Place Value - 50 unique questions"""
    questions = []
    
    # Template 1: Hundreds, tens, ones breakdown (15 questions)
    numbers = [123, 245, 367, 489, 512, 634, 756, 878, 901, 147, 258, 369, 471, 583, 695]
    
    for num in numbers:
        hundreds = num // 100
        tens = (num // 10) % 10
        ones = num % 10
        
        # Ask about different place values
        place = random.choice(['hundreds', 'tens', 'ones'])
        if place == 'hundreds':
            correct = hundreds
            q_text = f"In the number {num}, how many HUNDREDS are there?"
        elif place == 'tens':
            correct = tens
            q_text = f"In the number {num}, how many TENS are there?"
        else:
            correct = ones
            q_text = f"In the number {num}, how many ONES are there?"
        
        wrong1 = (correct + 1) % 10
        wrong2 = (correct + 2) % 10
        wrong3 = (correct + 5) % 10
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"In {num}: {hundreds} hundreds, {tens} tens, {ones} ones. The {place} digit is {correct}."
        })
    
    # Template 2: Value of a digit (15 questions)
    value_questions = [
        (352, 3, 300, "The 3 is in the hundreds place, so its value is 300"),
        (478, 7, 70, "The 7 is in the tens place, so its value is 70"),
        (629, 9, 9, "The 9 is in the ones place, so its value is 9"),
        (814, 8, 800, "The 8 is in the hundreds place, so its value is 800"),
        (263, 6, 60, "The 6 is in the tens place, so its value is 60"),
        (547, 4, 40, "The 4 is in the tens place, so its value is 40"),
        (195, 1, 100, "The 1 is in the hundreds place, so its value is 100"),
        (738, 3, 30, "The 3 is in the tens place, so its value is 30"),
        (426, 2, 20, "The 2 is in the tens place, so its value is 20"),
        (951, 5, 50, "The 5 is in the tens place, so its value is 50"),
        (183, 8, 80, "The 8 is in the tens place, so its value is 80"),
        (672, 6, 600, "The 6 is in the hundreds place, so its value is 600"),
        (394, 9, 90, "The 9 is in the tens place, so its value is 90"),
        (215, 5, 5, "The 5 is in the ones place, so its value is 5"),
        (847, 4, 40, "The 4 is in the tens place, so its value is 40")
    ]
    
    for num, digit, value, explanation in value_questions:
        wrong_values = [v for v in [digit, digit * 10, digit * 100] if v != value]
        wrong_values.append(value + 100 if value < 100 else value - 100)
        
        options = [str(value), str(wrong_values[0]), str(wrong_values[1]), str(abs(wrong_values[2]))]
        random.shuffle(options)
        correct_idx = options.index(str(value))
        
        questions.append({
            'question_text': f"In the number {num}, what is the VALUE of the digit {digit}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Template 3: Build number from expanded form (10 questions)
    expanded = [
        (200, 30, 5, 235), (400, 60, 2, 462), (100, 50, 8, 158),
        (300, 70, 4, 374), (500, 20, 9, 529), (600, 80, 1, 681),
        (700, 40, 6, 746), (800, 10, 3, 813), (900, 90, 7, 997),
        (200, 40, 0, 240)
    ]
    
    for h, t, o, correct in expanded:
        wrong1 = correct + 100
        wrong2 = correct - 100 if correct > 100 else correct + 111
        wrong3 = int(str(o) + str(t//10) + str(h//100)) if o > 0 else correct + 10
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"What is {h} + {t} + {o}? (Combine hundreds, tens, and ones)",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{h} + {t} + {o} = {correct}"
        })
    
    # Template 4: Compare numbers using place value (10 questions)
    compare_pairs = [
        (456, 465, '<', "456 < 465 because in the tens place, 5 < 6"),
        (723, 732, '<', "723 < 732 because in the tens place, 2 < 3"),
        (891, 819, '>', "891 > 819 because in the tens place, 9 > 1"),
        (234, 243, '<', "234 < 243 because in the tens place, 3 < 4"),
        (567, 576, '<', "567 < 576 because in the tens place, 6 < 7"),
        (389, 398, '<', "389 < 398 because in the tens place, 8 < 9"),
        (654, 645, '>', "654 > 645 because in the tens place, 5 > 4"),
        (912, 921, '<', "912 < 921 because in the tens place, 1 < 2"),
        (478, 487, '<', "478 < 487 because in the tens place, 7 < 8"),
        (836, 863, '<', "836 < 863 because in the tens place, 3 < 6")
    ]
    
    for num1, num2, sign, explanation in compare_pairs:
        q_text = f"Which symbol goes between {num1} ___ {num2}?"
        correct = sign
        
        options = ['<', '>', '=', '≠']
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_5_questions():
    """Level 5: Estimating Amounts - 50 unique questions"""
    questions = []
    
    # Template 1: Round to nearest 10 (20 questions)
    round_10 = [
        (23, 20), (27, 30), (34, 30), (38, 40), (45, 50),
        (52, 50), (56, 60), (63, 60), (67, 70), (74, 70),
        (78, 80), (81, 80), (85, 90), (92, 90), (96, 100),
        (14, 10), (19, 20), (41, 40), (55, 60), (88, 90)
    ]
    
    for num, correct in round_10:
        wrong1 = correct + 10
        wrong2 = correct - 10 if correct > 0 else correct + 20
        wrong3 = num
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"Round {num} to the nearest 10. Is {num} closer to {correct - 10 if correct > 0 else 0} or {correct}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{num} rounded to the nearest 10 is {correct}."
        })
    
    # Template 2: Estimate sums (15 questions)
    estimates = [
        (23, 18, 40, "23 ≈ 20 and 18 ≈ 20, so estimate is about 40"),
        (34, 27, 60, "34 ≈ 30 and 27 ≈ 30, so estimate is about 60"),
        (45, 36, 80, "45 ≈ 50 and 36 ≈ 40, so estimate is about 90, but 80 is closest"),
        (52, 29, 80, "52 ≈ 50 and 29 ≈ 30, so estimate is about 80"),
        (67, 24, 90, "67 ≈ 70 and 24 ≈ 20, so estimate is about 90"),
        (38, 43, 80, "38 ≈ 40 and 43 ≈ 40, so estimate is about 80"),
        (56, 35, 90, "56 ≈ 60 and 35 ≈ 40, so estimate is about 100, but 90 is closest"),
        (71, 18, 90, "71 ≈ 70 and 18 ≈ 20, so estimate is about 90"),
        (44, 47, 90, "44 ≈ 40 and 47 ≈ 50, so estimate is about 90"),
        (63, 28, 90, "63 ≈ 60 and 28 ≈ 30, so estimate is about 90"),
        (29, 32, 60, "29 ≈ 30 and 32 ≈ 30, so estimate is about 60"),
        (58, 23, 80, "58 ≈ 60 and 23 ≈ 20, so estimate is about 80"),
        (41, 49, 90, "41 ≈ 40 and 49 ≈ 50, so estimate is about 90"),
        (76, 15, 90, "76 ≈ 80 and 15 ≈ 20, so estimate is about 100, but 90 is closest"),
        (33, 38, 70, "33 ≈ 30 and 38 ≈ 40, so estimate is about 70")
    ]
    
    for num1, num2, correct, explanation in estimates:
        wrong1 = correct + 20
        wrong2 = correct - 20 if correct > 20 else correct + 30
        wrong3 = num1 + num2  # Exact answer
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"ESTIMATE: About how much is {num1} + {num2}? (Round each number first)",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Template 3: Is estimate reasonable? (15 questions)
    reasonable = [
        (47, 52, 100, 'Yes', "47 + 52 ≈ 50 + 50 = 100, so yes, 100 is reasonable"),
        (23, 31, 90, 'No', "23 + 31 ≈ 20 + 30 = 50, so no, 90 is too high"),
        (68, 24, 90, 'Yes', "68 + 24 ≈ 70 + 20 = 90, so yes, 90 is reasonable"),
        (35, 28, 100, 'No', "35 + 28 ≈ 40 + 30 = 70, so no, 100 is too high"),
        (56, 37, 90, 'Yes', "56 + 37 ≈ 60 + 40 = 100, close to 90, so yes"),
        (19, 22, 80, 'No', "19 + 22 ≈ 20 + 20 = 40, so no, 80 is too high"),
        (73, 18, 90, 'Yes', "73 + 18 ≈ 70 + 20 = 90, so yes, 90 is reasonable"),
        (44, 27, 70, 'Yes', "44 + 27 ≈ 40 + 30 = 70, so yes, 70 is reasonable"),
        (61, 33, 60, 'No', "61 + 33 ≈ 60 + 30 = 90, so no, 60 is too low"),
        (82, 15, 100, 'Yes', "82 + 15 ≈ 80 + 20 = 100, so yes, 100 is reasonable"),
        (29, 34, 100, 'No', "29 + 34 ≈ 30 + 30 = 60, so no, 100 is too high"),
        (55, 38, 90, 'Yes', "55 + 38 ≈ 60 + 40 = 100, close to 90, so yes"),
        (41, 19, 90, 'No', "41 + 19 ≈ 40 + 20 = 60, so no, 90 is too high"),
        (67, 26, 90, 'Yes', "67 + 26 ≈ 70 + 30 = 100, close to 90, so yes"),
        (38, 41, 80, 'Yes', "38 + 41 ≈ 40 + 40 = 80, so yes, 80 is reasonable")
    ]
    
    for num1, num2, estimate, answer, explanation in reasonable:
        q_text = f"Sarah estimated {num1} + {num2} ≈ {estimate}. Is this a reasonable estimate?"
        
        options = ['Yes', 'No', 'Cannot tell', 'Need more information']
        correct_idx = 0 if answer == 'Yes' else 1
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_6_questions():
    """Level 6: Adding & Subtracting - 50 unique questions"""
    questions = []
    
    # Template 1: Addition with visuals (15 questions)
    additions = [
        (12, 8, 20), (15, 7, 22), (23, 9, 32), (18, 14, 32), (25, 17, 42),
        (31, 12, 43), (27, 19, 46), (34, 18, 52), (29, 23, 52), (36, 27, 63),
        (42, 19, 61), (38, 25, 63), (45, 28, 73), (47, 36, 83), (53, 29, 82)
    ]
    
    for a, b, correct in additions:
        wrong1 = correct + random.randint(1, 5)
        wrong2 = correct - random.randint(1, 5)
        wrong3 = a - b if a > b else b - a
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"Calculate: {a} + {b} = ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{a} + {b} = {correct}"
        })
    
    # Template 2: Subtraction (15 questions)
    subtractions = [
        (20, 8, 12), (25, 9, 16), (32, 15, 17), (40, 18, 22), (35, 17, 18),
        (48, 23, 25), (52, 27, 25), (45, 19, 26), (60, 34, 26), (55, 28, 27),
        (63, 36, 27), (70, 42, 28), (58, 29, 29), (75, 48, 27), (80, 53, 27)
    ]
    
    for a, b, correct in subtractions:
        wrong1 = correct + random.randint(1, 5)
        wrong2 = correct - random.randint(1, 5) if correct > 5 else correct + random.randint(6, 10)
        wrong3 = a + b
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': f"Calculate: {a} - {b} = ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{a} - {b} = {correct}"
        })
    
    # Template 3: Word problems - addition (10 questions)
    add_word = [
        ("Tom has 15 stickers. He gets 8 more. How many stickers does Tom have now?", 15, 8, 23),
        ("A shop has 24 apples. 12 more arrive. How many apples are there now?", 24, 12, 36),
        ("Emma scored 18 points. Then she scored 14 more. What is her total?", 18, 14, 32),
        ("There are 27 birds. 15 more land. How many birds are there now?", 27, 15, 42),
        ("Dad drove 35 km in the morning and 28 km in the afternoon. How far did he drive?", 35, 28, 63),
        ("Class A has 19 students. Class B has 23. How many students in total?", 19, 23, 42),
        ("Mum baked 26 cookies. Gran baked 17. How many cookies altogether?", 26, 17, 43),
        ("I have 33 marbles. My friend gives me 19 more. How many do I have?", 33, 19, 52),
        ("The shop sold 45 drinks in the morning and 37 in the afternoon. Total sales?", 45, 37, 82),
        ("Sam collected 28 shells. Lily collected 34. How many shells in total?", 28, 34, 62)
    ]
    
    for q_text, a, b, correct in add_word:
        wrong1 = correct + random.randint(1, 5)
        wrong2 = correct - random.randint(1, 5)
        wrong3 = abs(a - b)
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{a} + {b} = {correct}"
        })
    
    # Template 4: Word problems - subtraction (10 questions)
    sub_word = [
        ("There were 30 birds. 12 flew away. How many are left?", 30, 12, 18),
        ("Tom had 45 sweets. He ate 18. How many are left?", 45, 18, 27),
        ("A bus had 52 passengers. 24 got off. How many stayed on?", 52, 24, 28),
        ("The shop had 60 toys. 35 were sold. How many are left?", 60, 35, 25),
        ("Emma had 48 stickers. She gave 19 away. How many does she have?", 48, 19, 29),
        ("There were 75 books. 38 were borrowed. How many are left?", 75, 38, 37),
        ("Dad had €50. He spent €23. How much does he have left?", 50, 23, 27),
        ("The jar had 64 sweets. 29 were eaten. How many remain?", 64, 29, 35),
        ("There were 80 balloons. 42 popped. How many are left?", 80, 42, 38),
        ("Sam had 55 cards. He lost 27. How many does he have now?", 55, 27, 28)
    ]
    
    for q_text, a, b, correct in sub_word:
        wrong1 = correct + random.randint(1, 5)
        wrong2 = correct - random.randint(1, 5) if correct > 5 else correct + random.randint(6, 10)
        wrong3 = a + b
        
        options = [str(correct), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(correct))
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{a} - {b} = {correct}"
        })
    
    return questions[:50]


def generate_level_7_questions():
    """Level 7: Recognising Money - 50 unique questions"""
    questions = []
    
    # Template 1: Identify coin values (15 questions)
    coins = [
        (1, 'cent', '1c', 'copper', 'smallest'),
        (2, 'cent', '2c', 'copper', 'small with groove'),
        (5, 'cent', '5c', 'copper', 'medium copper'),
        (10, 'cent', '10c', 'gold', 'small gold'),
        (20, 'cent', '20c', 'gold', 'medium gold'),
        (50, 'cent', '50c', 'gold', 'large gold'),
        (100, 'euro', '€1', 'silver/gold', 'two-coloured'),
        (200, 'euro', '€2', 'gold/silver', 'larger two-coloured')
    ]
    
    for i, (value, unit, display, colour, description) in enumerate(coins):
        if i >= 15:
            break
            
        if unit == 'cent':
            q_text = f"A {colour} coin worth {value} cents is shown as:"
            correct = f"{value}c"
            wrong_options = ['€1', '€2', '€5'] if value < 50 else ['1c', '2c', '5c']
        else:
            q_text = f"A {description} coin worth {value // 100} euro(s) is shown as:"
            correct = f"€{value // 100}"
            wrong_options = ['50c', '20c', '10c']
        
        options = [correct] + wrong_options[:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"This coin is worth {display}.",
            'image_svg': generate_money_svg([value])
        })
    
    # More coin questions to reach 15
    for i in range(15 - len([c for c in coins if coins.index(c) < 15])):
        coin_val = random.choice([1, 2, 5, 10, 20, 50, 100, 200])
        if coin_val < 100:
            correct = f"{coin_val}c"
            display = f"{coin_val} cent"
        else:
            correct = f"€{coin_val // 100}"
            display = f"{coin_val // 100} euro"
        
        all_options = ['1c', '2c', '5c', '10c', '20c', '50c', '€1', '€2']
        wrong_options = [o for o in all_options if o != correct][:3]
        
        options = [correct] + wrong_options
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"What is the value of this {display} coin?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"This coin is worth {correct}.",
            'image_svg': generate_money_svg([coin_val])
        })
    
    # Template 2: Count total money (20 questions)
    money_combos = [
        ([100, 50, 20], 170, '€1.70'),
        ([200, 100], 300, '€3.00'),
        ([50, 50, 20], 120, '€1.20'),
        ([100, 20, 10], 130, '€1.30'),
        ([200, 50, 10], 260, '€2.60'),
        ([100, 100, 50], 250, '€2.50'),
        ([20, 20, 20], 60, '60c'),
        ([50, 20, 5], 75, '75c'),
        ([10, 10, 5, 5], 30, '30c'),
        ([100, 50, 50], 200, '€2.00'),
        ([200, 100, 50], 350, '€3.50'),
        ([50, 20, 10, 5], 85, '85c'),
        ([100, 20, 20, 10], 150, '€1.50'),
        ([200, 200], 400, '€4.00'),
        ([100, 50, 20, 10], 180, '€1.80'),
        ([50, 50, 50], 150, '€1.50'),
        ([20, 10, 10, 5], 45, '45c'),
        ([100, 100, 100], 300, '€3.00'),
        ([200, 50, 50], 300, '€3.00'),
        ([50, 20, 20, 10], 100, '€1.00')
    ]
    
    for coins, total_cents, display in money_combos:
        if total_cents >= 100:
            correct = f"€{total_cents / 100:.2f}"
            wrong1 = f"€{(total_cents + 50) / 100:.2f}"
            wrong2 = f"€{(total_cents - 50) / 100:.2f}" if total_cents > 50 else f"€{(total_cents + 100) / 100:.2f}"
            wrong3 = f"€{(total_cents + 100) / 100:.2f}"
        else:
            correct = f"{total_cents}c"
            wrong1 = f"{total_cents + 10}c"
            wrong2 = f"{total_cents - 10}c" if total_cents > 10 else f"{total_cents + 20}c"
            wrong3 = f"{total_cents + 25}c"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        coin_text = ' + '.join([f"{c}c" if c < 100 else f"€{c//100}" for c in coins])
        
        questions.append({
            'question_text': f"Add these coins: {coin_text}. What is the total?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The total is {display}.",
            'image_svg': generate_money_svg(coins)
        })
    
    # Template 3: Notes recognition (15 questions)
    notes = [
        (5, '€5', 'grey'),
        (10, '€10', 'red/orange'),
        (20, '€20', 'blue'),
        (50, '€50', 'orange/brown')
    ]
    
    for i in range(15):
        note_val, display, colour = notes[i % len(notes)]
        
        q_text = f"A {colour} euro note worth {note_val} euros is written as:"
        correct = f"€{note_val}"
        wrong_options = [f"€{v}" for v, _, _ in notes if v != note_val]
        wrong_options.append(f"{note_val}c")
        
        options = [correct] + wrong_options[:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"This note is worth {display}.",
            'image_svg': generate_money_svg([], [note_val])
        })
    
    return questions[:50]


def generate_level_8_questions():
    """Level 8: Shopping & Transactions - 50 unique questions"""
    questions = []
    
    items = [
        ('apple', 0.50), ('banana', 0.35), ('orange', 0.60), ('milk', 1.20),
        ('bread', 1.50), ('cheese', 2.30), ('juice', 1.80), ('yogurt', 0.90),
        ('biscuits', 1.40), ('crisps', 1.10), ('sandwich', 3.50), ('water', 0.80),
        ('chocolate', 1.25), ('cake', 2.80), ('ice cream', 2.50)
    ]
    
    # Template 1: Simple purchases (20 questions)
    for i in range(20):
        item1, price1 = items[i % len(items)]
        item2, price2 = items[(i + 3) % len(items)]
        
        total = price1 + price2
        correct = f"€{total:.2f}"
        wrong1 = f"€{total + 0.50:.2f}"
        wrong2 = f"€{total - 0.30:.2f}" if total > 0.30 else f"€{total + 0.70:.2f}"
        wrong3 = f"€{total + 1.00:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"You buy a {item1} (€{price1:.2f}) and a {item2} (€{price2:.2f}). What is the total cost?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"€{price1:.2f} + €{price2:.2f} = {correct}",
            'image_svg': generate_price_tag_svg(total, f"{item1} + {item2}")
        })
    
    # Template 2: Calculate change (20 questions)
    change_scenarios = [
        (5.00, 3.20, 1.80), (5.00, 2.50, 2.50), (5.00, 4.30, 0.70),
        (10.00, 6.50, 3.50), (10.00, 7.80, 2.20), (10.00, 8.40, 1.60),
        (10.00, 3.90, 6.10), (10.00, 5.25, 4.75), (20.00, 12.50, 7.50),
        (20.00, 15.80, 4.20), (20.00, 8.30, 11.70), (20.00, 17.60, 2.40),
        (5.00, 1.80, 3.20), (5.00, 3.75, 1.25), (10.00, 4.60, 5.40),
        (10.00, 9.15, 0.85), (20.00, 11.25, 8.75), (20.00, 14.90, 5.10),
        (5.00, 2.85, 2.15), (10.00, 6.95, 3.05)
    ]
    
    for paid, cost, change in change_scenarios:
        correct = f"€{change:.2f}"
        wrong1 = f"€{change + 0.50:.2f}"
        wrong2 = f"€{change - 0.50:.2f}" if change > 0.50 else f"€{change + 1.00:.2f}"
        wrong3 = f"€{paid - change:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"You pay €{paid:.2f} for something that costs €{cost:.2f}. How much change do you get?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"€{paid:.2f} - €{cost:.2f} = {correct} change"
        })
    
    # Template 3: Enough money? (10 questions)
    enough_scenarios = [
        (5.00, 4.50, 'Yes', "€5.00 is enough for €4.50"),
        (3.00, 3.80, 'No', "€3.00 is not enough for €3.80"),
        (10.00, 8.75, 'Yes', "€10.00 is enough for €8.75"),
        (2.00, 2.50, 'No', "€2.00 is not enough for €2.50"),
        (5.00, 5.00, 'Yes', "€5.00 is exactly enough for €5.00"),
        (7.50, 6.90, 'Yes', "€7.50 is enough for €6.90"),
        (4.00, 4.25, 'No', "€4.00 is not enough for €4.25"),
        (20.00, 18.50, 'Yes', "€20.00 is enough for €18.50"),
        (6.00, 6.10, 'No', "€6.00 is not enough for €6.10"),
        (15.00, 12.80, 'Yes', "€15.00 is enough for €12.80")
    ]
    
    for have, need, answer, explanation in enough_scenarios:
        q_text = f"You have €{have:.2f}. Something costs €{need:.2f}. Do you have enough money?"
        
        options = ['Yes', 'No', 'Exactly right', 'Need more information']
        if answer == 'Yes' and have == need:
            correct_idx = 2
        else:
            correct_idx = 0 if answer == 'Yes' else 1
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_9_questions():
    """Level 9: Totals & Change - 50 unique questions"""
    questions = []
    
    # Template 1: Multi-item shopping (20 questions)
    shopping_lists = [
        ([1.20, 0.80, 2.50], 4.50), ([2.30, 1.70, 0.90], 4.90),
        ([3.40, 2.60, 1.50], 7.50), ([1.80, 2.20, 1.40], 5.40),
        ([0.90, 1.10, 2.30, 0.70], 5.00), ([1.50, 2.50, 1.80], 5.80),
        ([3.20, 1.30, 2.10], 6.60), ([2.40, 1.60, 0.85], 4.85),
        ([1.75, 2.25, 1.50], 5.50), ([0.95, 1.45, 2.35], 4.75),
        ([2.80, 1.20, 1.50, 0.50], 6.00), ([3.50, 2.00, 1.25], 6.75),
        ([1.35, 2.65, 1.80], 5.80), ([2.15, 1.85, 2.50], 6.50),
        ([0.75, 1.25, 3.00], 5.00), ([1.90, 2.10, 1.40, 0.60], 6.00),
        ([2.70, 1.30, 1.50], 5.50), ([3.25, 1.75, 0.80], 5.80),
        ([1.40, 2.60, 1.20, 0.80], 6.00), ([2.50, 1.50, 2.25], 6.25)
    ]
    
    for prices, total in shopping_lists:
        correct = f"€{total:.2f}"
        wrong1 = f"€{total + 0.50:.2f}"
        wrong2 = f"€{total - 0.50:.2f}" if total > 0.50 else f"€{total + 1.00:.2f}"
        wrong3 = f"€{total + 1.00:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        price_str = ' + '.join([f"€{p:.2f}" for p in prices])
        
        questions.append({
            'question_text': f"Add up these prices: {price_str}. What is the total?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Total: {correct}"
        })
    
    # Template 2: Complex change calculations (20 questions)
    change_calcs = [
        (20.00, 13.45, 6.55), (20.00, 16.80, 3.20), (50.00, 37.25, 12.75),
        (50.00, 42.60, 7.40), (20.00, 11.35, 8.65), (10.00, 7.45, 2.55),
        (20.00, 18.90, 1.10), (50.00, 28.75, 21.25), (20.00, 14.60, 5.40),
        (10.00, 8.35, 1.65), (50.00, 33.50, 16.50), (20.00, 17.25, 2.75),
        (50.00, 46.80, 3.20), (20.00, 12.15, 7.85), (10.00, 6.70, 3.30),
        (50.00, 39.90, 10.10), (20.00, 15.55, 4.45), (50.00, 44.25, 5.75),
        (20.00, 19.30, 0.70), (10.00, 9.45, 0.55)
    ]
    
    for paid, spent, change in change_calcs:
        correct = f"€{change:.2f}"
        wrong1 = f"€{change + 0.55:.2f}"
        wrong2 = f"€{change - 0.45:.2f}" if change > 0.45 else f"€{change + 1.00:.2f}"
        wrong3 = f"€{spent:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"You pay with €{paid:.2f} for goods costing €{spent:.2f}. Calculate your change.",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"€{paid:.2f} - €{spent:.2f} = {correct}"
        })
    
    # Template 3: Best value / comparison (10 questions)
    comparisons = [
        (3, 1.50, 5, 2.00, 'B', "5 for €2.00 = 40c each, 3 for €1.50 = 50c each"),
        (2, 1.00, 4, 1.60, 'B', "4 for €1.60 = 40c each, 2 for €1.00 = 50c each"),
        (6, 3.00, 4, 2.40, 'A', "6 for €3.00 = 50c each, 4 for €2.40 = 60c each"),
        (3, 2.10, 5, 3.00, 'B', "5 for €3.00 = 60c each, 3 for €2.10 = 70c each"),
        (4, 2.00, 6, 2.40, 'B', "6 for €2.40 = 40c each, 4 for €2.00 = 50c each"),
        (2, 1.40, 3, 1.80, 'B', "3 for €1.80 = 60c each, 2 for €1.40 = 70c each"),
        (5, 2.50, 3, 1.80, 'A', "5 for €2.50 = 50c each, 3 for €1.80 = 60c each"),
        (4, 1.60, 5, 2.50, 'A', "4 for €1.60 = 40c each, 5 for €2.50 = 50c each"),
        (3, 0.90, 4, 1.00, 'B', "4 for €1.00 = 25c each, 3 for €0.90 = 30c each"),
        (6, 1.80, 4, 1.40, 'A', "6 for €1.80 = 30c each, 4 for €1.40 = 35c each")
    ]
    
    for qty_a, price_a, qty_b, price_b, answer, explanation in comparisons:
        q_text = f"Which is better value: {qty_a} items for €{price_a:.2f} (A) or {qty_b} items for €{price_b:.2f} (B)?"
        
        options = ['A', 'B', 'Same value', 'Cannot tell']
        correct_idx = 0 if answer == 'A' else 1
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_10_questions():
    """Level 10: Estimating & Rounding Money - 50 unique questions"""
    questions = []
    
    # Template 1: Round to nearest euro (15 questions)
    round_euro = [
        (2.30, 2), (3.70, 4), (5.45, 5), (6.80, 7), (8.25, 8),
        (4.50, 5), (7.49, 7), (9.51, 10), (1.85, 2), (3.15, 3),
        (6.60, 7), (8.40, 8), (2.75, 3), (5.20, 5), (7.90, 8)
    ]
    
    for amount, rounded in round_euro:
        correct = f"€{rounded}"
        wrong1 = f"€{rounded + 1}"
        wrong2 = f"€{rounded - 1}" if rounded > 1 else f"€{rounded + 2}"
        wrong3 = f"€{amount:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"Round €{amount:.2f} to the nearest euro.",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"€{amount:.2f} rounds to {correct}"
        })
    
    # Template 2: Estimate totals (20 questions)
    estimate_totals = [
        (3.20, 4.80, 8, "€3.20 ≈ €3, €4.80 ≈ €5, total ≈ €8"),
        (2.90, 5.10, 8, "€2.90 ≈ €3, €5.10 ≈ €5, total ≈ €8"),
        (6.40, 3.60, 10, "€6.40 ≈ €6, €3.60 ≈ €4, total ≈ €10"),
        (4.75, 2.25, 7, "€4.75 ≈ €5, €2.25 ≈ €2, total ≈ €7"),
        (7.30, 1.70, 9, "€7.30 ≈ €7, €1.70 ≈ €2, total ≈ €9"),
        (5.50, 4.50, 10, "€5.50 ≈ €6, €4.50 ≈ €4 or 5, total ≈ €10"),
        (8.20, 2.80, 11, "€8.20 ≈ €8, €2.80 ≈ €3, total ≈ €11"),
        (3.85, 6.15, 10, "€3.85 ≈ €4, €6.15 ≈ €6, total ≈ €10"),
        (1.90, 7.10, 9, "€1.90 ≈ €2, €7.10 ≈ €7, total ≈ €9"),
        (4.40, 5.60, 10, "€4.40 ≈ €4, €5.60 ≈ €6, total ≈ €10"),
        (2.70, 3.30, 6, "€2.70 ≈ €3, €3.30 ≈ €3, total ≈ €6"),
        (6.80, 2.20, 9, "€6.80 ≈ €7, €2.20 ≈ €2, total ≈ €9"),
        (5.25, 3.75, 9, "€5.25 ≈ €5, €3.75 ≈ €4, total ≈ €9"),
        (8.60, 1.40, 10, "€8.60 ≈ €9, €1.40 ≈ €1, total ≈ €10"),
        (4.15, 4.85, 9, "€4.15 ≈ €4, €4.85 ≈ €5, total ≈ €9"),
        (7.50, 2.50, 10, "€7.50 ≈ €8, €2.50 ≈ €2 or 3, total ≈ €10"),
        (3.45, 5.55, 9, "€3.45 ≈ €3, €5.55 ≈ €6, total ≈ €9"),
        (6.30, 3.70, 10, "€6.30 ≈ €6, €3.70 ≈ €4, total ≈ €10"),
        (2.65, 6.35, 9, "€2.65 ≈ €3, €6.35 ≈ €6, total ≈ €9"),
        (5.80, 4.20, 10, "€5.80 ≈ €6, €4.20 ≈ €4, total ≈ €10")
    ]
    
    for price1, price2, estimate, explanation in estimate_totals:
        correct = f"€{estimate}"
        wrong1 = f"€{estimate + 2}"
        wrong2 = f"€{estimate - 2}" if estimate > 2 else f"€{estimate + 3}"
        wrong3 = f"€{price1 + price2:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"ESTIMATE the total: €{price1:.2f} + €{price2:.2f} ≈ ?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Template 3: Do I have enough? (15 questions)
    enough = [
        (10, [2.80, 3.40, 2.90], 'Yes', "Estimate: €3 + €3 + €3 = €9, which is less than €10"),
        (15, [4.50, 5.80, 3.70], 'Yes', "Estimate: €5 + €6 + €4 = €15, just enough"),
        (10, [3.60, 4.80, 2.90], 'No', "Estimate: €4 + €5 + €3 = €12, more than €10"),
        (20, [6.30, 7.20, 4.50], 'Yes', "Estimate: €6 + €7 + €5 = €18, less than €20"),
        (15, [5.40, 6.70, 4.20], 'No', "Estimate: €5 + €7 + €4 = €16, more than €15"),
        (10, [2.30, 4.70, 2.10], 'Yes', "Estimate: €2 + €5 + €2 = €9, less than €10"),
        (20, [7.80, 8.40, 5.30], 'No', "Estimate: €8 + €8 + €5 = €21, more than €20"),
        (15, [4.20, 5.30, 4.60], 'Yes', "Estimate: €4 + €5 + €5 = €14, less than €15"),
        (10, [3.40, 3.80, 3.50], 'No', "Estimate: €3 + €4 + €4 = €11, more than €10"),
        (20, [5.60, 6.40, 5.90], 'Yes', "Estimate: €6 + €6 + €6 = €18, less than €20"),
        (15, [5.80, 4.60, 5.20], 'No', "Estimate: €6 + €5 + €5 = €16, more than €15"),
        (10, [2.90, 2.80, 3.20], 'Yes', "Estimate: €3 + €3 + €3 = €9, less than €10"),
        (20, [6.70, 7.50, 6.80], 'No', "Estimate: €7 + €8 + €7 = €22, more than €20"),
        (15, [3.90, 5.10, 4.80], 'Yes', "Estimate: €4 + €5 + €5 = €14, less than €15"),
        (10, [4.30, 3.60, 2.70], 'No', "Estimate: €4 + €4 + €3 = €11, more than €10")
    ]
    
    for have, prices, answer, explanation in enough:
        price_str = ', '.join([f"€{p:.2f}" for p in prices])
        q_text = f"You have €{have}. Items cost {price_str}. Is €{have} enough? (Estimate first)"
        
        options = ['Yes', 'No', 'Exactly enough', 'Cannot estimate']
        correct_idx = 0 if answer == 'Yes' else 1
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_11_questions():
    """Level 11: Bills & Receipts - 50 unique questions"""
    questions = []
    
    # Template 1: Read receipt totals (15 questions)
    receipts = [
        (['Milk €1.20', 'Bread €1.50', 'Butter €2.30'], 5.00),
        (['Apples €2.40', 'Oranges €1.80', 'Bananas €1.30'], 5.50),
        (['Cheese €3.50', 'Ham €2.80', 'Lettuce €1.20'], 7.50),
        (['Juice €1.90', 'Biscuits €2.10', 'Tea €3.50'], 7.50),
        (['Eggs €2.80', 'Bacon €3.40', 'Sausages €2.30'], 8.50),
        (['Rice €1.60', 'Pasta €1.40', 'Sauce €2.50'], 5.50),
        (['Yogurt €0.90', 'Cereal €3.20', 'Fruit €2.40'], 6.50),
        (['Chicken €4.50', 'Vegetables €2.30', 'Potatoes €1.70'], 8.50),
        (['Fish €5.20', 'Lemon €0.60', 'Herbs €1.70'], 7.50),
        (['Pizza €4.80', 'Salad €2.20', 'Drink €1.50'], 8.50),
        (['Sandwich €3.50', 'Crisps €1.30', 'Water €0.70'], 5.50),
        (['Coffee €2.80', 'Cake €3.20', 'Muffin €1.50'], 7.50),
        (['Soup €2.40', 'Bread €1.10', 'Butter €1.00'], 4.50),
        (['Steak €6.50', 'Chips €1.80', 'Sauce €0.70'], 9.00),
        (['Wine €7.50', 'Cheese €3.20', 'Crackers €1.80'], 12.50)
    ]
    
    for items, total in receipts:
        items_str = '\n'.join(items)
        correct = f"€{total:.2f}"
        wrong1 = f"€{total + 0.50:.2f}"
        wrong2 = f"€{total - 0.50:.2f}" if total > 0.50 else f"€{total + 1.00:.2f}"
        wrong3 = f"€{total + 1.00:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"Receipt shows:\n{items_str}\n\nWhat is the total?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Adding all items: Total = {correct}"
        })
    
    # Template 2: Check if receipt is correct (15 questions)
    receipt_checks = [
        ([1.20, 2.30, 1.50], 5.00, 'Correct', "1.20 + 2.30 + 1.50 = 5.00 ✓"),
        ([2.40, 1.80, 1.30], 5.00, 'Wrong', "2.40 + 1.80 + 1.30 = 5.50, not 5.00"),
        ([3.50, 2.80, 1.20], 7.50, 'Correct', "3.50 + 2.80 + 1.20 = 7.50 ✓"),
        ([1.90, 2.10, 3.50], 8.00, 'Wrong', "1.90 + 2.10 + 3.50 = 7.50, not 8.00"),
        ([2.80, 3.40, 2.30], 8.50, 'Correct', "2.80 + 3.40 + 2.30 = 8.50 ✓"),
        ([1.60, 1.40, 2.50], 6.00, 'Wrong', "1.60 + 1.40 + 2.50 = 5.50, not 6.00"),
        ([0.90, 3.20, 2.40], 6.50, 'Correct', "0.90 + 3.20 + 2.40 = 6.50 ✓"),
        ([4.50, 2.30, 1.70], 9.00, 'Wrong', "4.50 + 2.30 + 1.70 = 8.50, not 9.00"),
        ([5.20, 0.60, 1.70], 7.50, 'Correct', "5.20 + 0.60 + 1.70 = 7.50 ✓"),
        ([4.80, 2.20, 1.50], 9.00, 'Wrong', "4.80 + 2.20 + 1.50 = 8.50, not 9.00"),
        ([3.50, 1.30, 0.70], 5.50, 'Correct', "3.50 + 1.30 + 0.70 = 5.50 ✓"),
        ([2.80, 3.20, 1.50], 8.00, 'Wrong', "2.80 + 3.20 + 1.50 = 7.50, not 8.00"),
        ([2.40, 1.10, 1.00], 4.50, 'Correct', "2.40 + 1.10 + 1.00 = 4.50 ✓"),
        ([6.50, 1.80, 0.70], 8.50, 'Wrong', "6.50 + 1.80 + 0.70 = 9.00, not 8.50"),
        ([7.50, 3.20, 1.80], 12.50, 'Correct', "7.50 + 3.20 + 1.80 = 12.50 ✓")
    ]
    
    for prices, shown_total, answer, explanation in receipt_checks:
        price_str = ' + '.join([f"€{p:.2f}" for p in prices])
        q_text = f"A receipt shows: {price_str} = €{shown_total:.2f}. Is this correct?"
        
        options = ['Correct', 'Wrong - too high', 'Wrong - too low', 'Cannot tell']
        if answer == 'Correct':
            correct_idx = 0
        else:
            actual = sum(prices)
            correct_idx = 1 if shown_total > actual else 2
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Template 3: Split a bill (10 questions)
    splits = [
        (12.00, 2, 6.00), (15.00, 3, 5.00), (20.00, 4, 5.00),
        (18.00, 2, 9.00), (24.00, 3, 8.00), (16.00, 4, 4.00),
        (10.00, 2, 5.00), (21.00, 3, 7.00), (28.00, 4, 7.00),
        (14.00, 2, 7.00)
    ]
    
    for total, people, each in splits:
        correct = f"€{each:.2f}"
        wrong1 = f"€{each + 1:.2f}"
        wrong2 = f"€{each - 1:.2f}" if each > 1 else f"€{each + 2:.2f}"
        wrong3 = f"€{total:.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"A bill of €{total:.2f} is split equally between {people} people. How much does each person pay?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"€{total:.2f} ÷ {people} = {correct} each"
        })
    
    # Template 4: Bill word problems (10 questions)
    bill_problems = [
        ("Three friends ate lunch costing €24 total. If they split it equally, how much each?", 24, 3, 8.00),
        ("A family of 4 shared a €32 meal. What did each person pay?", 32, 4, 8.00),
        ("Two people split a €15 taxi fare. How much each?", 15, 2, 7.50),
        ("Five coworkers shared a €45 pizza order. Cost per person?", 45, 5, 9.00),
        ("A €36 gift was split between 4 friends. Each paid?", 36, 4, 9.00),
        ("Three siblings split a €27 present. How much each?", 27, 3, 9.00),
        ("Two friends shared a €22 meal. Each paid?", 22, 2, 11.00),
        ("Four people split a €48 hotel room. Cost per person?", 48, 4, 12.00),
        ("Six friends shared a €42 entry fee. Each paid?", 42, 6, 7.00),
        ("Three people split a €33 bill. How much each?", 33, 3, 11.00)
    ]
    
    for q_text, total, people, each in bill_problems:
        correct = f"€{each:.2f}"
        wrong1 = f"€{each + 1:.2f}"
        wrong2 = f"€{each - 1:.2f}" if each > 1 else f"€{each + 2:.2f}"
        wrong3 = f"€{total / (people + 1):.2f}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"€{total} ÷ {people} = {correct}"
        })
    
    return questions[:50]


def generate_level_12_questions():
    """Level 12: Digital Payments & Financial Literacy - 50 unique questions"""
    questions = []
    
    # Template 1: Payment method questions (15 questions)
    payment_qs = [
        ("What is contactless payment?", "Tap your card without entering a PIN",
         ["Tap your card without entering a PIN", "Always need PIN", "Only for large amounts", "Only online"]),
        ("What does a PIN protect?", "Your bank card from unauthorized use",
         ["Your bank card from unauthorized use", "Your phone", "Your email", "Your name"]),
        ("What is an ATM used for?", "Withdrawing cash from your bank account",
         ["Withdrawing cash from your bank account", "Buying groceries", "Making phone calls", "Sending emails"]),
        ("Why keep your PIN secret?", "To prevent theft from your account",
         ["To prevent theft from your account", "It's not important", "For fun", "To remember it better"]),
        ("What is a bank statement?", "A record of money in and out of your account",
         ["A record of money in and out of your account", "A shopping list", "A receipt", "A bill"]),
        ("What is a debit card?", "A card that takes money directly from your bank",
         ["A card that takes money directly from your bank", "Free money card", "Gift card", "Loyalty card"]),
        ("What is online banking?", "Managing your bank account on the internet",
         ["Managing your bank account on the internet", "Playing games", "Social media", "Email"]),
        ("What is a transaction?", "Money going into or out of an account",
         ["Money going into or out of an account", "A type of card", "A bank name", "An ATM"]),
        ("Why check your bank balance?", "To know how much money you have",
         ["To know how much money you have", "For fun", "It's required daily", "To get more money"]),
        ("What is a savings account?", "An account where you keep money to save",
         ["An account where you keep money to save", "A spending account", "A game", "A credit card"]),
        ("What does 'insufficient funds' mean?", "Not enough money in your account",
         ["Not enough money in your account", "Too much money", "Account is full", "Card is new"]),
        ("What is a receipt?", "Proof of a purchase you made",
         ["Proof of a purchase you made", "A type of money", "A bank card", "A password"]),
        ("Why save receipts?", "To track spending and for returns",
         ["To track spending and for returns", "They look nice", "Required by law", "No reason"]),
        ("What is budgeting?", "Planning how to spend your money",
         ["Planning how to spend your money", "Spending all your money", "Getting a loan", "A type of account"]),
        ("What is interest on savings?", "Extra money the bank adds to your savings",
         ["Extra money the bank adds to your savings", "Money you lose", "A fee", "A penalty"])
    ]
    
    for q_text, correct, options in payment_qs:
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The correct answer is: {correct}"
        })
    
    # Template 2: Safe banking practices (15 questions)
    safety_qs = [
        ("Should you share your PIN with friends?", "No", "Never share your PIN with anyone"),
        ("Is it safe to use ATMs in dark, hidden places?", "No", "Use ATMs in well-lit, busy areas"),
        ("Should you check your bank balance regularly?", "Yes", "Regular checking helps spot problems"),
        ("Is it okay to write your PIN on your card?", "No", "Never write your PIN anywhere visible"),
        ("Should you cover the keypad when entering your PIN?", "Yes", "This prevents others from seeing it"),
        ("Is it safe to click links in emails about your bank?", "No", "Banks don't ask for details via email links"),
        ("Should you keep your receipts?", "Yes", "Receipts help track spending and spot errors"),
        ("Is it safe to leave your card in a shop?", "No", "Always take your card with you"),
        ("Should you tell the bank if you lose your card?", "Yes", "Report lost cards immediately"),
        ("Is it okay to use the same PIN as your birthday?", "No", "Use PINs that aren't easy to guess"),
        ("Should you check receipts match your statement?", "Yes", "This helps find mistakes or fraud"),
        ("Is contactless payment safe?", "Yes", "It has security limits built in"),
        ("Should you log out of online banking on shared computers?", "Yes", "Always log out on shared devices"),
        ("Is it safe to save card details on any website?", "No", "Only save on trusted, secure sites"),
        ("Should you use strong passwords for online banking?", "Yes", "Strong passwords protect your account")
    ]
    
    for q_text, answer, explanation in safety_qs:
        options = ['Yes', 'No', 'Sometimes', 'Depends']
        correct_idx = 0 if answer == 'Yes' else 1
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Template 3: Real-world money scenarios (20 questions)
    scenarios = [
        ("You have €50 saved and earn €10 weekly. After 4 weeks you'll have:", "€90", "€50 + (€10 × 4) = €90"),
        ("A game costs €25. You have €18. How much more do you need?", "€7", "€25 - €18 = €7"),
        ("You save €5 per week. How long to save €30?", "6 weeks", "€30 ÷ €5 = 6 weeks"),
        ("Bus fare is €2.50 each way. Daily travel costs:", "€5.00", "€2.50 × 2 = €5.00"),
        ("Cinema ticket: €8. Popcorn: €4.50. Total?", "€12.50", "€8 + €4.50 = €12.50"),
        ("You have €20. Spend €7.50. What's left?", "€12.50", "€20 - €7.50 = €12.50"),
        ("Weekly pocket money is €10. Monthly (4 weeks)?", "€40", "€10 × 4 = €40"),
        ("A book costs €15. You have €20. Change?", "€5", "€20 - €15 = €5"),
        ("Save €8 weekly. After 5 weeks?", "€40", "€8 × 5 = €40"),
        ("Lunch costs €6.50 daily. Weekly (5 days)?", "€32.50", "€6.50 × 5 = €32.50"),
        ("You earn €15 and spend €9. Savings?", "€6", "€15 - €9 = €6"),
        ("A gift costs €35. Three friends share equally. Each pays?", "€11.67", "€35 ÷ 3 ≈ €11.67"),
        ("Bus pass: €25/week or €2/trip. If you take 15 trips, which is cheaper?", "Weekly pass", "15 trips × €2 = €30, but pass is €25"),
        ("You have €100. Spend 30%. How much left?", "€70", "€100 - €30 = €70"),
        ("Movie + popcorn deal €10 vs separate €8 + €5. Save?", "€3", "€8 + €5 = €13, deal saves €3"),
        ("Earn €12, save half. Savings?", "€6", "€12 ÷ 2 = €6"),
        ("Item was €40, now 25% off. New price?", "€30", "25% of €40 = €10, so €40 - €10 = €30"),
        ("Three snacks at €2.50 each. Total?", "€7.50", "€2.50 × 3 = €7.50"),
        ("€50 gift card, spent €37. Balance?", "€13", "€50 - €37 = €13"),
        ("Save €20/month. After 6 months?", "€120", "€20 × 6 = €120")
    ]
    
    for q_text, correct, explanation in scenarios:
        # Generate wrong answers based on the correct one
        if '€' in correct:
            val = float(correct.replace('€', ''))
            wrong1 = f"€{val + 5:.2f}".replace('.00', '')
            wrong2 = f"€{max(0, val - 3):.2f}".replace('.00', '')
            wrong3 = f"€{val + 10:.2f}".replace('.00', '')
        elif 'weeks' in correct:
            val = int(correct.split()[0])
            wrong1 = f"{val + 2} weeks"
            wrong2 = f"{val - 1} weeks" if val > 1 else f"{val + 3} weeks"
            wrong3 = f"{val + 4} weeks"
        elif 'pass' in correct.lower():
            wrong1 = "Individual trips"
            wrong2 = "Same cost"
            wrong3 = "Cannot tell"
            options = [correct, wrong1, wrong2, wrong3]
            random.shuffle(options)
            correct_idx = options.index(correct)
            questions.append({
                'question_text': q_text,
                'options': options,
                'correct_index': correct_idx,
                'explanation': explanation
            })
            continue
        else:
            wrong1 = correct + " extra"
            wrong2 = "Half that"
            wrong3 = "Double that"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


# ============================================================
# MAIN FUNCTIONS
# ============================================================

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
        (12, generate_level_12_questions)
    ]
    
    for level, generator in generators:
        print(f"  Generating Level {level}...")
        questions = generator()
        
        for q in questions:
            # Convert to database format
            options = q['options']
            while len(options) < 4:
                options.append('')
            
            all_questions.append({
                'topic': TOPIC,
                'level': level,
                'question_text': q['question_text'],
                'option_a': str(options[0]),
                'option_b': str(options[1]),
                'option_c': str(options[2]),
                'option_d': str(options[3]),
                'correct_answer': ['A', 'B', 'C', 'D'][q['correct_index']],
                'solution': q.get('explanation', ''),
                'question_image_svg': q.get('image_svg', '')
            })
        
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    """Validate questions for issues"""
    errors = []
    seen = set()
    
    for i, q in enumerate(questions):
        # Check for required fields
        if not q.get('question_text'):
            errors.append(f"Q{i}: Missing question_text")
        if not q.get('option_a'):
            errors.append(f"Q{i}: Missing option_a")
        if not q.get('correct_answer'):
            errors.append(f"Q{i}: Missing correct_answer")
        
        # Check for duplicates at same level
        key = (q['level'], q['question_text'][:100])
        if key in seen:
            errors.append(f"Q{i} L{q['level']}: Duplicate text: {q['question_text'][:50]}...")
        seen.add(key)
    
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
    skipped = 0
    
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
                q.get('solution', ''),
                level,
                band,
                'multiple_choice',
                1,
                q.get('question_image_svg', ''),
                datetime.now(),
                datetime.now()
            ))
            
            if cursor.rowcount > 0:
                inserted += 1
            else:
                skipped += 1
                
        except sqlite3.Error as e:
            print(f"Error: {e}")
            skipped += 1
    
    conn.commit()
    conn.close()
    
    if skipped > 0:
        print(f"   Skipped {skipped} duplicate questions")
    
    return inserted


def main():
    """Main entry point"""
    print("=" * 60)
    print("AgentMath L2LP Question Generator V3")
    print(f"Topic: {TOPIC}")
    print(f"Table: questions_adaptive")
    print(f"Target: {QUESTIONS_PER_LEVEL} × {TOTAL_LEVELS} = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS}")
    print("=" * 60)
    
    if not clear_existing_questions():
        return
    
    print("\nGenerating questions...")
    questions = generate_all_questions()
    print(f"\nTotal: {len(questions)}")
    
    print("\nValidating...")
    errors = validate_questions(questions)
    duplicates = [e for e in errors if 'Duplicate' in e]
    critical = [e for e in errors if 'Duplicate' not in e]
    
    if duplicates:
        print(f"⚠️  {len(duplicates)} duplicate warnings (will be skipped)")
    
    if critical:
        print(f"❌ {len(critical)} critical errors:")
        for e in critical[:10]:
            print(f"   {e}")
        return
    
    print("✅ Validation passed")
    
    print("\nInserting...")
    inserted = insert_questions(questions)
    
    print(f"\n{'=' * 60}")
    print(f"✅ Complete! Inserted {inserted} questions for {TOPIC}")
    
    # Show breakdown by level
    counts = count_existing_questions()
    print("\nQuestions per level:")
    for level in range(1, 13):
        count = counts.get(level, 0)
        status = "✓" if count >= 40 else "⚠️" if count >= 20 else "❌"
        print(f"   Level {level}: {count} {status}")
    
    print("=" * 60)


if __name__ == '__main__':
    main()
