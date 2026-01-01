#!/usr/bin/env python3
"""
AgentMath - Whole Numbers Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy
Visual Requirements: 85%/75%/65%/55% by band

Level Structure:
  L1-3:   Foundation (85% visual) - Reading, Place Value, Comparing
  L4-6:   Developing (75% visual) - Ordering, Rounding
  L7-9:   Proficient (65% visual) - Large Numbers, Estimation
  L10-12: Advanced (55% visual) - Properties, Problem Solving, Mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'whole_numbers'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems (child-friendly mix)
IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam',
    'Emily', 'Luke', 'Sarah', 'Ryan', 'Anna', 'Ben'
]

# Child-friendly contexts
CONTEXTS = {
    'school': ['pencils', 'books', 'crayons', 'stickers', 'students', 'desks'],
    'food': ['apples', 'oranges', 'sweets', 'cookies', 'sandwiches'],
    'sports': ['goals', 'points', 'medals', 'laps', 'players'],
    'animals': ['dogs', 'cats', 'birds', 'fish', 'rabbits'],
    'toys': ['marbles', 'cards', 'toy cars', 'balls', 'blocks'],
    'nature': ['flowers', 'trees', 'leaves', 'stones', 'shells']
}

# ============================================================
# DIFFICULTY BANDS
# ============================================================

def get_difficulty_band(level):
    """Return difficulty band for numeracy strand"""
    if level <= 3:
        return 'foundation'
    elif level <= 6:
        return 'developing'
    elif level <= 9:
        return 'proficient'
    else:
        return 'advanced'

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    
    unique_wrong = []
    for w in wrong_list:
        w_str = str(w)
        if w_str != correct_str and w_str not in unique_wrong:
            unique_wrong.append(w_str)
    
    options = [correct_str] + unique_wrong[:3]
    
    # Ensure exactly 4 unique options
    fallback_idx = 1
    while len(set(options)) < 4:
        if isinstance(correct, int):
            fallback = str(correct + fallback_idx * 7)
        else:
            fallback = str(int(correct.replace(',', '')) + fallback_idx * 7)
        if fallback not in options:
            options.append(fallback)
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    
    return options, correct_idx

def format_number(n):
    """Format number with commas for display"""
    return f"{n:,}"

def number_to_words(n):
    """Convert number to words (up to millions)"""
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
            'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if n < 20:
        return ones[n]
    elif n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        return tens[n // 10] + '-' + ones[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + ' hundred'
        return ones[n // 100] + ' hundred and ' + number_to_words(n % 100)
    elif n < 10000:
        if n % 1000 == 0:
            return ones[n // 1000] + ' thousand'
        return ones[n // 1000] + ' thousand, ' + number_to_words(n % 1000)
    elif n < 100000:
        thousands = n // 1000
        remainder = n % 1000
        if remainder == 0:
            return number_to_words(thousands) + ' thousand'
        return number_to_words(thousands) + ' thousand, ' + number_to_words(remainder)
    elif n < 1000000:
        thousands = n // 1000
        remainder = n % 1000
        if remainder == 0:
            return number_to_words(thousands) + ' thousand'
        return number_to_words(thousands) + ' thousand, ' + number_to_words(remainder)
    else:
        millions = n // 1000000
        remainder = n % 1000000
        if remainder == 0:
            return number_to_words(millions) + ' million'
        return number_to_words(millions) + ' million, ' + number_to_words(remainder)

def generate_place_value_chart_svg(number, highlight_place=None):
    """Generate SVG showing place value chart"""
    digits = str(number).replace(',', '')
    places = ['Millions', 'Hundred Thousands', 'Ten Thousands', 'Thousands', 'Hundreds', 'Tens', 'Ones']
    
    # Pad to 7 digits
    digits = digits.zfill(7)
    
    # Only show relevant places (skip leading zeros)
    start_idx = 0
    for i, d in enumerate(digits):
        if d != '0':
            start_idx = i
            break
    
    # Always show at least 4 places
    start_idx = min(start_idx, 3)
    
    relevant_digits = digits[start_idx:]
    relevant_places = places[start_idx:]
    
    width = len(relevant_digits) * 70 + 20
    
    svg = f'''<svg viewBox="0 0 {width} 100" xmlns="http://www.w3.org/2000/svg">
    <style>
        .place-label {{ font-size: 8px; fill: #6b7280; text-anchor: middle; }}
        .digit {{ font-size: 24px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
        .highlight {{ fill: #fef3c7; }}
        .highlight-digit {{ fill: #d97706; }}
    </style>'''
    
    for i, (digit, place) in enumerate(zip(relevant_digits, relevant_places)):
        x = 45 + i * 70
        is_highlight = highlight_place and place.lower().startswith(highlight_place.lower())
        
        # Background box
        fill = '#fef3c7' if is_highlight else '#f3f4f6'
        svg += f'<rect x="{x-30}" y="25" width="60" height="50" fill="{fill}" stroke="#d1d5db" rx="4"/>'
        
        # Place label
        short_place = place.replace(' ', '\\n').split('\\n')[0][:3]
        svg += f'<text x="{x}" y="18" class="place-label">{short_place}</text>'
        
        # Digit
        digit_class = 'highlight-digit' if is_highlight else 'digit'
        svg += f'<text x="{x}" y="60" class="{digit_class}">{digit}</text>'
    
    svg += '</svg>'
    return svg

def generate_number_line_svg(numbers, highlight=None, show_question=False):
    """Generate SVG number line"""
    min_n = min(numbers)
    max_n = max(numbers)
    range_n = max_n - min_n
    
    svg = '''<svg viewBox="0 0 400 80" xmlns="http://www.w3.org/2000/svg">
    <style>
        .line {{ stroke: #374151; stroke-width: 2; }}
        .tick {{ stroke: #374151; stroke-width: 1; }}
        .label {{ font-size: 11px; fill: #374151; text-anchor: middle; }}
        .highlight {{ fill: #10b981; font-weight: bold; }}
        .question {{ fill: #ef4444; font-weight: bold; font-size: 14px; }}
    </style>
    <line x1="20" y1="40" x2="380" y2="40" class="line"/>'''
    
    for i, n in enumerate(numbers):
        x = 20 + (360 * (n - min_n) / range_n) if range_n > 0 else 200
        svg += f'<line x1="{x}" y1="35" x2="{x}" y2="45" class="tick"/>'
        
        if show_question and n == highlight:
            svg += f'<text x="{x}" y="65" class="question">?</text>'
        else:
            label_class = 'highlight' if n == highlight else 'label'
            svg += f'<text x="{x}" y="65" class="{label_class}">{format_number(n)}</text>'
    
    svg += '</svg>'
    return svg

def generate_comparison_svg(num1, num2, symbol=None):
    """Generate SVG showing two numbers to compare"""
    svg = f'''<svg viewBox="0 0 300 60" xmlns="http://www.w3.org/2000/svg">
    <style>
        .number {{ font-size: 24px; fill: #1f2937; font-weight: bold; }}
        .symbol {{ font-size: 28px; fill: #10b981; font-weight: bold; }}
        .box {{ fill: #f3f4f6; stroke: #d1d5db; rx: 8; }}
    </style>
    <rect x="10" y="10" width="100" height="40" class="box"/>
    <text x="60" y="40" text-anchor="middle" class="number">{format_number(num1)}</text>
    <text x="150" y="42" text-anchor="middle" class="symbol">{symbol if symbol else '?'}</text>
    <rect x="190" y="10" width="100" height="40" class="box"/>
    <text x="240" y="40" text-anchor="middle" class="number">{format_number(num2)}</text>
    </svg>'''
    return svg

# ============================================================
# LEVEL 1: Reading Numbers (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Reading Numbers - Read and recognise numbers to 10,000"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'read_number',
        'write_from_words',
        'identify_number',
        'match_words'
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'read_number':
                # What is this number?
                number = random.randint(100, 9999)
                q_text = f"What is {format_number(number)} in words?"
                correct = number_to_words(number)
                
                # Generate plausible wrong answers
                wrong = []
                wrong.append(number_to_words(number + 10))
                wrong.append(number_to_words(number - 10))
                wrong.append(number_to_words(number + 100))
                
                explanation = f"Step 1: Break the number into parts. Step 2: {format_number(number)} = {correct}. The answer is {correct}! ✓"
                image_svg = generate_place_value_chart_svg(number)
                
            elif q_type == 'write_from_words':
                # Write the number from words
                number = random.randint(100, 9999)
                words = number_to_words(number)
                q_text = f"Write this number using digits: {words}"
                correct = format_number(number)
                
                wrong = [
                    format_number(number + 10),
                    format_number(number - 10),
                    format_number(number + 100)
                ]
                
                explanation = f"Step 1: Read the words carefully: {words}. Step 2: Write as digits: {correct}. The answer is {correct}! ✓"
                image_svg = None
                
            elif q_type == 'identify_number':
                # Which number is shown?
                number = random.randint(1000, 9999)
                q_text = f"Look at the place value chart. What number is shown?"
                correct = format_number(number)
                
                wrong = [
                    format_number(number + 100),
                    format_number(number - 100),
                    format_number(number + 1000)
                ]
                
                explanation = f"Step 1: Read each digit from left to right. Step 2: The number is {correct}. The answer is {correct}! ✓"
                image_svg = generate_place_value_chart_svg(number)
                
            else:  # match_words
                # Match number to words
                number = random.randint(100, 5000)
                q_text = f"Which of these equals {format_number(number)}?"
                correct = number_to_words(number)
                
                wrong = [
                    number_to_words(number + 100),
                    number_to_words(number - 100),
                    number_to_words(number + 10)
                ]
                
                explanation = f"Step 1: Read {format_number(number)} carefully. Step 2: It equals {correct}. The answer is {correct}! ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Place Value (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Place Value - Identify place value of digits"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'value_of_digit',
        'which_place',
        'digit_in_place',
        'total_value'
    ]
    
    places = {
        'ones': 1,
        'tens': 10,
        'hundreds': 100,
        'thousands': 1000
    }
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'value_of_digit':
                # What is the value of the digit X in this number?
                number = random.randint(1000, 9999)
                digits = str(number)
                pos = random.randint(0, 3)
                digit = int(digits[pos])
                
                place_names = ['thousands', 'hundreds', 'tens', 'ones']
                place_name = place_names[pos]
                place_value = [1000, 100, 10, 1][pos]
                
                value = digit * place_value
                
                q_text = f"In {format_number(number)}, what is the value of the digit {digit}?"
                correct = format_number(value)
                
                wrong = [
                    str(digit),  # Just the digit
                    format_number(digit * 10),
                    format_number(digit * 100)
                ]
                
                explanation = f"Step 1: The digit {digit} is in the {place_name} place. Step 2: {digit} × {place_value} = {value}. The answer is {correct}! ✓"
                image_svg = generate_place_value_chart_svg(number, place_name)
                
            elif q_type == 'which_place':
                # Which place is the digit X in?
                number = random.randint(1000, 9999)
                digits = str(number)
                pos = random.randint(0, 3)
                digit = int(digits[pos])
                
                place_names = ['thousands', 'hundreds', 'tens', 'ones']
                correct = place_names[pos]
                
                q_text = f"In {format_number(number)}, what place is the digit {digit} in?"
                
                wrong = [p for p in place_names if p != correct]
                
                explanation = f"Step 1: Find the digit {digit} in {format_number(number)}. Step 2: Count from the right: ones, tens, hundreds, thousands. The {digit} is in the {correct} place! ✓"
                image_svg = generate_place_value_chart_svg(number, correct)
                
            elif q_type == 'digit_in_place':
                # What digit is in the X place?
                number = random.randint(1000, 9999)
                digits = str(number)
                pos = random.randint(0, 3)
                
                place_names = ['thousands', 'hundreds', 'tens', 'ones']
                place_name = place_names[pos]
                correct = digits[pos]
                
                q_text = f"In {format_number(number)}, what digit is in the {place_name} place?"
                
                wrong = [d for d in digits if d != correct]
                while len(wrong) < 3:
                    wrong.append(str(random.randint(0, 9)))
                
                explanation = f"Step 1: Find the {place_name} place (position {4-pos} from the right). Step 2: The digit there is {correct}. The answer is {correct}! ✓"
                image_svg = generate_place_value_chart_svg(number, place_name)
                
            else:  # total_value
                # What is X thousands + Y hundreds + Z tens + W ones?
                th = random.randint(1, 9)
                hu = random.randint(0, 9)
                te = random.randint(0, 9)
                on = random.randint(0, 9)
                
                total = th * 1000 + hu * 100 + te * 10 + on
                
                q_text = f"What number is: {th} thousands + {hu} hundreds + {te} tens + {on} ones?"
                correct = format_number(total)
                
                wrong = [
                    format_number(total + 100),
                    format_number(total - 100),
                    format_number(total + 10)
                ]
                
                explanation = f"Step 1: {th}×1000 = {th*1000}. Step 2: {hu}×100 = {hu*100}. Step 3: {te}×10 = {te*10}. Step 4: Add {on}. Total = {correct}! ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Comparing Numbers (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Comparing Numbers - Use <, >, = to compare"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'which_symbol',
        'which_bigger',
        'which_smaller',
        'true_false'
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'which_symbol':
                # What symbol goes between?
                num1 = random.randint(100, 9999)
                diff = random.choice([-100, -10, -1, 0, 1, 10, 100])
                num2 = num1 + diff
                
                if num1 > num2:
                    correct = '>'
                elif num1 < num2:
                    correct = '<'
                else:
                    correct = '='
                
                q_text = f"What symbol goes in the box? {format_number(num1)} □ {format_number(num2)}"
                wrong = ['<', '>', '=']
                wrong.remove(correct)
                wrong.append('≠')
                
                explanation = f"Step 1: Compare {format_number(num1)} and {format_number(num2)}. Step 2: {format_number(num1)} is {'greater than' if correct == '>' else 'less than' if correct == '<' else 'equal to'} {format_number(num2)}. The answer is {correct}! ✓"
                image_svg = generate_comparison_svg(num1, num2)
                
            elif q_type == 'which_bigger':
                # Which number is bigger?
                num1 = random.randint(100, 9999)
                num2 = num1 + random.randint(1, 500)
                
                # Shuffle which is first
                if random.choice([True, False]):
                    num1, num2 = num2, num1
                
                bigger = max(num1, num2)
                q_text = f"Which number is bigger: {format_number(num1)} or {format_number(num2)}?"
                correct = format_number(bigger)
                
                smaller = min(num1, num2)
                wrong = [
                    format_number(smaller),
                    format_number(bigger + 10),
                    format_number(smaller - 10)
                ]
                
                explanation = f"Step 1: Compare from left to right. Step 2: {format_number(bigger)} has more in the higher places. The answer is {correct}! ✓"
                image_svg = generate_comparison_svg(num1, num2)
                
            elif q_type == 'which_smaller':
                # Which is smaller?
                num1 = random.randint(100, 9999)
                num2 = num1 + random.randint(1, 500)
                
                if random.choice([True, False]):
                    num1, num2 = num2, num1
                
                smaller = min(num1, num2)
                q_text = f"Which number is smaller: {format_number(num1)} or {format_number(num2)}?"
                correct = format_number(smaller)
                
                bigger = max(num1, num2)
                wrong = [
                    format_number(bigger),
                    format_number(smaller + 10),
                    format_number(bigger - 10)
                ]
                
                explanation = f"Step 1: Compare from left to right. Step 2: {format_number(smaller)} has less in the higher places. The answer is {correct}! ✓"
                image_svg = generate_comparison_svg(num1, num2)
                
            else:  # true_false
                # Is this statement true?
                num1 = random.randint(100, 9999)
                num2 = num1 + random.randint(-100, 100)
                
                symbol = random.choice(['<', '>', '='])
                
                if symbol == '<':
                    is_true = num1 < num2
                elif symbol == '>':
                    is_true = num1 > num2
                else:
                    is_true = num1 == num2
                
                q_text = f"Is this true? {format_number(num1)} {symbol} {format_number(num2)}"
                correct = "True" if is_true else "False"
                
                wrong = ["False" if is_true else "True", "Cannot tell", "Maybe"]
                
                explanation = f"Step 1: {format_number(num1)} {'is' if is_true else 'is not'} {symbol} {format_number(num2)}. The statement is {correct}! ✓"
                image_svg = generate_comparison_svg(num1, num2, symbol)
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Ordering Numbers (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Ordering Numbers - Arrange in ascending/descending order"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            # Generate 3-4 numbers to order
            count = random.choice([3, 4])
            base = random.randint(100, 5000)
            numbers = [base + random.randint(-500, 500) for _ in range(count)]
            numbers = list(set(numbers))  # Remove duplicates
            
            if len(numbers) < 3:
                continue
            
            ascending = random.choice([True, False])
            order_word = "smallest to largest" if ascending else "largest to smallest"
            
            sorted_nums = sorted(numbers, reverse=not ascending)
            
            numbers_str = ', '.join(format_number(n) for n in numbers)
            q_text = f"Put these numbers in order from {order_word}: {numbers_str}"
            
            correct = ', '.join(format_number(n) for n in sorted_nums)
            
            # Wrong answers: different orderings
            wrong = []
            wrong.append(', '.join(format_number(n) for n in sorted(numbers, reverse=ascending)))  # Opposite order
            random.shuffle(numbers)
            wrong.append(', '.join(format_number(n) for n in numbers))
            random.shuffle(numbers)
            wrong.append(', '.join(format_number(n) for n in numbers))
            
            explanation = f"Step 1: Compare the numbers. Step 2: Order from {order_word}. The answer is {correct}! ✓"
            
            # Visual: number line
            image_svg = generate_number_line_svg(sorted_nums)
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 4,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Rounding to 10s and 100s (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Rounding (10s, 100s) - Round to nearest 10 and 100"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            round_to = random.choice([10, 100])
            
            if round_to == 10:
                number = random.randint(10, 999)
                rounded = round(number, -1)
                look_at = "ones"
            else:
                number = random.randint(100, 9999)
                rounded = round(number, -2)
                look_at = "tens"
            
            q_text = f"Round {format_number(number)} to the nearest {round_to}."
            correct = format_number(int(rounded))
            
            # Wrong answers
            wrong = []
            if round_to == 10:
                wrong.append(format_number(int(rounded) + 10))
                wrong.append(format_number(int(rounded) - 10))
                wrong.append(format_number(round(number, -2)))
            else:
                wrong.append(format_number(int(rounded) + 100))
                wrong.append(format_number(int(rounded) - 100))
                wrong.append(format_number(round(number, -1)))
            
            digit = str(number)[-1] if round_to == 10 else str(number)[-2] if len(str(number)) > 1 else '0'
            direction = "up" if int(digit) >= 5 else "down"
            
            explanation = f"Step 1: Look at the {look_at} digit: {digit}. Step 2: {digit} is {'5 or more' if int(digit) >= 5 else 'less than 5'}, so round {direction}. The answer is {correct}! ✓"
            
            # Visual for some questions
            if random.random() < 0.75:
                # Show on number line
                lower = (number // round_to) * round_to
                upper = lower + round_to
                image_svg = generate_number_line_svg([lower, number, upper], number)
            else:
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 5,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Rounding to 1000s (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Rounding (1000s) - Round to nearest 1,000"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            number = random.randint(1000, 99999)
            rounded = round(number, -3)
            
            q_text = f"Round {format_number(number)} to the nearest 1,000."
            correct = format_number(int(rounded))
            
            # Wrong answers
            wrong = [
                format_number(int(rounded) + 1000),
                format_number(int(rounded) - 1000),
                format_number(round(number, -2))
            ]
            
            hundreds_digit = (number // 100) % 10
            direction = "up" if hundreds_digit >= 5 else "down"
            
            explanation = f"Step 1: Look at the hundreds digit: {hundreds_digit}. Step 2: {hundreds_digit} is {'5 or more' if hundreds_digit >= 5 else 'less than 5'}, so round {direction}. The answer is {correct}! ✓"
            
            # Visual for some questions
            if random.random() < 0.75:
                lower = (number // 1000) * 1000
                upper = lower + 1000
                image_svg = generate_number_line_svg([lower, number, upper], number)
            else:
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 6,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Large Numbers (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Large Numbers - Numbers to 100,000"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'read_large',
        'place_value_large',
        'compare_large',
        'order_large'
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'read_large':
                number = random.randint(10000, 99999)
                q_text = f"What is {format_number(number)} in words?"
                correct = number_to_words(number)
                
                wrong = [
                    number_to_words(number + 1000),
                    number_to_words(number - 1000),
                    number_to_words(number + 10000)
                ]
                
                explanation = f"Step 1: Break into parts: {number//1000} thousand and {number%1000}. Step 2: {correct}. ✓"
                image_svg = generate_place_value_chart_svg(number)
                
            elif q_type == 'place_value_large':
                number = random.randint(10000, 99999)
                digits = str(number)
                pos = random.randint(0, 4)
                digit = int(digits[pos])
                
                place_names = ['ten thousands', 'thousands', 'hundreds', 'tens', 'ones']
                place_values = [10000, 1000, 100, 10, 1]
                place_name = place_names[pos]
                value = digit * place_values[pos]
                
                q_text = f"In {format_number(number)}, what is the value of the digit {digit}?"
                correct = format_number(value)
                
                wrong = [str(digit), format_number(digit * 10), format_number(digit * 100)]
                
                explanation = f"Step 1: The {digit} is in the {place_name} place. Step 2: {digit} × {place_values[pos]} = {value}. The answer is {correct}! ✓"
                image_svg = generate_place_value_chart_svg(number)
                
            elif q_type == 'compare_large':
                num1 = random.randint(10000, 99999)
                num2 = num1 + random.randint(-5000, 5000)
                
                if num1 > num2:
                    correct = format_number(num1)
                    other = format_number(num2)
                else:
                    correct = format_number(num2)
                    other = format_number(num1)
                
                q_text = f"Which is larger: {format_number(num1)} or {format_number(num2)}?"
                
                wrong = [other, format_number(max(num1, num2) + 1000), format_number(min(num1, num2) - 1000)]
                
                explanation = f"Step 1: Compare from the left. Step 2: {correct} is larger. ✓"
                image_svg = generate_comparison_svg(num1, num2)
                
            else:  # order_large
                numbers = [random.randint(10000, 99999) for _ in range(3)]
                numbers = list(set(numbers))
                if len(numbers) < 3:
                    continue
                
                ascending = random.choice([True, False])
                order_word = "smallest to largest" if ascending else "largest to smallest"
                sorted_nums = sorted(numbers, reverse=not ascending)
                
                q_text = f"Order from {order_word}: {', '.join(format_number(n) for n in numbers)}"
                correct = ', '.join(format_number(n) for n in sorted_nums)
                
                wrong = [
                    ', '.join(format_number(n) for n in sorted(numbers, reverse=ascending)),
                ]
                random.shuffle(numbers)
                wrong.append(', '.join(format_number(n) for n in numbers))
                random.shuffle(numbers)
                wrong.append(', '.join(format_number(n) for n in numbers))
                
                explanation = f"Step 1: Compare the numbers. Step 2: {correct}. ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 7,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Millions (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Millions - Numbers to 1,000,000+"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'read_millions',
        'write_millions',
        'place_value_millions',
        'compare_millions'
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'read_millions':
                number = random.randint(1000000, 9999999)
                q_text = f"How do you read {format_number(number)}?"
                
                millions = number // 1000000
                remainder = number % 1000000
                
                if remainder == 0:
                    correct = f"{millions} million"
                else:
                    thousands = remainder // 1000
                    ones = remainder % 1000
                    if ones == 0:
                        correct = f"{millions} million, {thousands} thousand"
                    else:
                        correct = f"{millions} million, {format_number(remainder)}"
                
                wrong = [
                    f"{millions + 1} million",
                    f"{millions} thousand",
                    f"{millions * 10} million"
                ]
                
                explanation = f"Step 1: {millions} million. Step 2: Plus {format_number(remainder)} more. The answer is {correct}! ✓"
                image_svg = generate_place_value_chart_svg(number)
                
            elif q_type == 'write_millions':
                millions = random.randint(1, 9)
                thousands = random.randint(0, 999)
                number = millions * 1000000 + thousands * 1000
                
                q_text = f"Write {millions} million, {thousands} thousand in digits."
                correct = format_number(number)
                
                wrong = [
                    format_number(number + 1000000),
                    format_number(number - 1000000),
                    format_number(millions * 100000 + thousands)
                ]
                
                explanation = f"Step 1: {millions} million = {millions},000,000. Step 2: Add {thousands} thousand. The answer is {correct}! ✓"
                image_svg = None
                
            elif q_type == 'place_value_millions':
                number = random.randint(1000000, 9999999)
                millions_digit = number // 1000000
                
                q_text = f"In {format_number(number)}, what is the value of the digit in the millions place?"
                correct = format_number(millions_digit * 1000000)
                
                wrong = [
                    str(millions_digit),
                    format_number(millions_digit * 100000),
                    format_number(millions_digit * 10000000)
                ]
                
                explanation = f"Step 1: The millions digit is {millions_digit}. Step 2: Value = {millions_digit} × 1,000,000 = {correct}. ✓"
                image_svg = generate_place_value_chart_svg(number, 'millions')
                
            else:  # compare_millions
                num1 = random.randint(1000000, 9999999)
                num2 = num1 + random.randint(-500000, 500000)
                
                bigger = max(num1, num2)
                q_text = f"Which is bigger: {format_number(num1)} or {format_number(num2)}?"
                correct = format_number(bigger)
                
                wrong = [
                    format_number(min(num1, num2)),
                    format_number(bigger + 1000000),
                    format_number(bigger - 1000000)
                ]
                
                explanation = f"Step 1: Compare from the left (millions first). Step 2: {correct} is bigger. ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 8,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Estimation (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Estimation - Estimate calculations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'estimate_sum',
        'estimate_difference',
        'closest_estimate',
        'reasonable_answer'
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'estimate_sum':
                num1 = random.randint(100, 999)
                num2 = random.randint(100, 999)
                
                # Round to nearest 100
                est1 = round(num1, -2)
                est2 = round(num2, -2)
                estimate = int(est1 + est2)
                
                q_text = f"Estimate {num1} + {num2} by rounding to the nearest 100."
                correct = format_number(estimate)
                
                wrong = [
                    format_number(estimate + 100),
                    format_number(estimate - 100),
                    format_number(num1 + num2)  # Exact answer
                ]
                
                explanation = f"Step 1: Round {num1} → {int(est1)}. Step 2: Round {num2} → {int(est2)}. Step 3: {int(est1)} + {int(est2)} = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'estimate_difference':
                num1 = random.randint(500, 999)
                num2 = random.randint(100, 400)
                
                est1 = round(num1, -2)
                est2 = round(num2, -2)
                estimate = int(est1 - est2)
                
                q_text = f"Estimate {num1} - {num2} by rounding to the nearest 100."
                correct = format_number(estimate)
                
                wrong = [
                    format_number(estimate + 100),
                    format_number(estimate - 100),
                    format_number(num1 - num2)
                ]
                
                explanation = f"Step 1: Round {num1} → {int(est1)}. Step 2: Round {num2} → {int(est2)}. Step 3: {int(est1)} - {int(est2)} = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'closest_estimate':
                num1 = random.randint(100, 999)
                num2 = random.randint(100, 999)
                actual = num1 + num2
                
                # Create estimate options
                good_est = round(num1, -2) + round(num2, -2)
                
                q_text = f"Which is the best estimate for {num1} + {num2}?"
                correct = format_number(int(good_est))
                
                wrong = [
                    format_number(int(good_est) + 500),
                    format_number(int(good_est) - 500),
                    format_number(int(good_est) + 200)
                ]
                
                explanation = f"Step 1: Round both numbers. Step 2: {correct} is closest to the actual sum of {actual}. ✓"
                image_svg = None
                
            else:  # reasonable_answer
                num1 = random.randint(200, 800)
                num2 = random.randint(100, 500)
                actual = num1 + num2
                
                reasonable = round(actual, -2)
                unreasonable = [actual * 2, actual // 2, actual + 1000]
                
                q_text = f"Is {format_number(random.choice([reasonable] + unreasonable))} a reasonable answer for {num1} + {num2}?"
                
                # Actually let's ask which IS reasonable
                q_text = f"Which answer is reasonable for {num1} + {num2}?"
                correct = format_number(int(round(actual, -2)))
                
                wrong = [
                    format_number(actual * 2),
                    format_number(actual // 2),
                    format_number(actual + 500)
                ]
                
                explanation = f"Step 1: Estimate {num1} + {num2}. Step 2: {correct} is close to {actual}. ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 9,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Number Properties (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Number Properties - Odd, even, factors, multiples"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = [
        'odd_even',
        'factors',
        'multiples',
        'divisibility'
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'odd_even':
                number = random.randint(100, 9999)
                is_even = number % 2 == 0
                
                q_text = f"Is {format_number(number)} odd or even?"
                correct = "Even" if is_even else "Odd"
                
                wrong = ["Odd" if is_even else "Even", "Neither", "Both"]
                
                last_digit = number % 10
                explanation = f"Step 1: Look at the last digit: {last_digit}. Step 2: {last_digit} is {'even' if is_even else 'odd'}. The number is {correct}! ✓"
                image_svg = None
                
            elif q_type == 'factors':
                number = random.choice([12, 18, 20, 24, 30, 36])
                
                # Find all factors
                factors = [i for i in range(1, number + 1) if number % i == 0]
                
                q_text = f"How many factors does {number} have?"
                correct = str(len(factors))
                
                wrong = [str(len(factors) + 1), str(len(factors) - 1), str(len(factors) + 2)]
                
                explanation = f"Step 1: Factors of {number}: {', '.join(map(str, factors))}. Step 2: Count them: {correct} factors. ✓"
                image_svg = None
                
            elif q_type == 'multiples':
                base = random.choice([3, 4, 5, 6, 7, 8, 9])
                position = random.randint(5, 12)
                multiple = base * position
                
                q_text = f"What is the {position}th multiple of {base}?"
                correct = str(multiple)
                
                wrong = [
                    str(base * (position + 1)),
                    str(base * (position - 1)),
                    str(base * position + base)
                ]
                
                explanation = f"Step 1: The {position}th multiple means {base} × {position}. Step 2: {base} × {position} = {correct}. ✓"
                image_svg = None
                
            else:  # divisibility
                divisor = random.choice([2, 3, 5, 10])
                
                if divisor == 2:
                    number = random.randint(10, 100) * 2 + random.choice([0, 1])
                elif divisor == 5:
                    number = random.randint(10, 100) * 5 + random.choice([0, 3])
                elif divisor == 10:
                    number = random.randint(10, 100) * 10 + random.choice([0, 7])
                else:  # 3
                    number = random.randint(100, 999)
                
                is_divisible = number % divisor == 0
                
                q_text = f"Is {number} divisible by {divisor}?"
                correct = "Yes" if is_divisible else "No"
                
                wrong = ["No" if is_divisible else "Yes", "Sometimes", "Cannot tell"]
                
                if divisor == 2:
                    rule = f"ends in {number % 10}, which is {'even' if is_divisible else 'odd'}"
                elif divisor == 5:
                    rule = f"ends in {number % 10}"
                elif divisor == 10:
                    rule = f"ends in {number % 10}"
                else:
                    digit_sum = sum(int(d) for d in str(number))
                    rule = f"digit sum is {digit_sum}"
                
                explanation = f"Step 1: Check the divisibility rule. {number} {rule}. Step 2: {'It divides evenly' if is_divisible else 'It does not divide evenly'}. {correct}! ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 10,
                'difficulty_band': 'advanced',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 11: Problem Solving (Advanced)
# ============================================================

def generate_level_11():
    """Level 11: Problem Solving - Multi-step word problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            context = random.choice(list(CONTEXTS.keys()))
            item = random.choice(CONTEXTS[context])
            
            problem_type = random.randint(1, 5)
            
            if problem_type == 1:
                # Total and part given, find other part
                total = random.randint(500, 2000)
                part1 = random.randint(100, total - 100)
                part2 = total - part1
                
                q_text = f"A school has {format_number(total)} {item}. {format_number(part1)} are in the library. How many are in the classrooms?"
                correct = format_number(part2)
                
                wrong = [
                    format_number(part2 + 100),
                    format_number(part2 - 100),
                    format_number(total)
                ]
                
                explanation = f"Step 1: Total - library = classrooms. Step 2: {format_number(total)} - {format_number(part1)} = {correct}. ✓"
                
            elif problem_type == 2:
                # Population/attendance comparison
                num1 = random.randint(1000, 9000)
                num2 = random.randint(1000, 9000)
                diff = abs(num1 - num2)
                
                q_text = f"Town A has {format_number(num1)} people. Town B has {format_number(num2)} people. How many more people are in the {'larger' if num1 > num2 else 'smaller'} town?"
                
                if num1 > num2:
                    q_text = f"Town A has {format_number(num1)} people. Town B has {format_number(num2)} people. How many more people are in Town A?"
                else:
                    q_text = f"Town A has {format_number(num1)} people. Town B has {format_number(num2)} people. How many more people are in Town B?"
                
                correct = format_number(diff)
                
                wrong = [
                    format_number(diff + 100),
                    format_number(num1 + num2),
                    format_number(diff - 100)
                ]
                
                explanation = f"Step 1: Find the difference. Step 2: {format_number(max(num1, num2))} - {format_number(min(num1, num2))} = {correct}. ✓"
                
            elif problem_type == 3:
                # Rounding in context
                exact = random.randint(2345, 8765)
                rounded = round(exact, -3)
                
                q_text = f"A stadium holds {format_number(exact)} people. Rounded to the nearest thousand, about how many is that?"
                correct = format_number(int(rounded))
                
                wrong = [
                    format_number(int(rounded) + 1000),
                    format_number(int(rounded) - 1000),
                    format_number(exact)
                ]
                
                explanation = f"Step 1: Look at hundreds digit. Step 2: Round {format_number(exact)} → {correct}. ✓"
                
            elif problem_type == 4:
                # Place value in context
                number = random.randint(10000, 99999)
                thousands = (number // 1000) % 10
                
                q_text = f"{name} saved {format_number(number)} points. How many thousands does this represent?"
                correct = str(number // 1000)
                
                wrong = [
                    str(thousands),
                    str(number // 100),
                    str(number // 10000)
                ]
                
                explanation = f"Step 1: {format_number(number)} ÷ 1,000 = {correct} thousands. ✓"
                
            else:
                # Compare and order in context
                heights = [random.randint(1000, 5000) for _ in range(3)]
                mountains = ["Ben Bulben", "Croagh Patrick", "Carrauntoohil"]
                
                max_height = max(heights)
                tallest_idx = heights.index(max_height)
                
                heights_text = ', '.join(f"{m}: {h}m" for m, h in zip(mountains, heights))
                
                q_text = f"Mountain heights: {heights_text}. Which is tallest?"
                correct = mountains[tallest_idx]
                
                wrong = [m for m in mountains if m != correct]
                wrong.append("They are equal")
                
                explanation = f"Step 1: Compare heights. Step 2: {max_height}m is highest. {correct} is tallest! ✓"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 11,
                'difficulty_band': 'advanced',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 12: Mastery Challenge (Advanced)
# ============================================================

def generate_level_12():
    """Level 12: Mastery Challenge - Mixed challenging questions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    # Mix of all skills
    generators = [
        generate_level_7,  # Large numbers
        generate_level_8,  # Millions
        generate_level_9,  # Estimation
        generate_level_10, # Number properties
        generate_level_11  # Problem solving
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            # Get a question from a random higher level
            gen = random.choice(generators)
            source_questions = gen()
            
            if source_questions:
                q = random.choice(source_questions)
                q_text = q['question_text']
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                # Update to level 12
                q['difficulty'] = 12
                q['difficulty_band'] = 'advanced'
                
                questions.append(q)
                
        except Exception as e:
            continue
    
    return questions

# ============================================================
# VALIDATION
# ============================================================

def validate_questions(questions):
    """Validate questions with numeracy-specific checks"""
    errors = []
    level_counts = {}
    newline_issues = []
    mode_issues = []
    
    for i, q in enumerate(questions):
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        # Check mode is correct
        if q['mode'] != 'numeracy':
            mode_issues.append(f"Level {level} Q{i}: Wrong mode '{q['mode']}'")
        
        # Check unique options
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level} Q{i}: Duplicate options: {options}")
        
        # Check for \n in question text
        if '\\n' in q['question_text'] or '\n' in q['question_text']:
            newline_issues.append(f"Level {level}: Newline in question")
    
    # Print summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY - Whole Numbers (Numeracy Strand)")
    print("="*60)
    
    all_good = True
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        if count < QUESTIONS_PER_LEVEL:
            all_good = False
        band = get_difficulty_band(level)
        print(f"Level {level:2} ({band:12}): {count:2}/{QUESTIONS_PER_LEVEL} {status}")
    
    print("="*60)
    print(f"Total: {len(questions)} questions")
    print(f"Errors: {len(errors)}")
    print(f"Newline Issues: {len(newline_issues)}")
    print(f"Mode Issues: {len(mode_issues)}")
    print("="*60)
    
    if errors:
        print("\nErrors found:")
        for e in errors[:10]:
            print(f"  - {e}")
    
    if mode_issues:
        print("\nMode issues found:")
        for e in mode_issues[:5]:
            print(f"  - {e}")
    
    return len(errors) + len(newline_issues) + len(mode_issues)

# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions with mode='numeracy'"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete existing questions for this topic/mode
    cursor.execute(
        "DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?",
        (TOPIC, MODE)
    )
    print(f"Deleted {cursor.rowcount} existing questions for {TOPIC}/{MODE}")
    
    inserted = 0
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (question_text, option_a, option_b, option_c, option_d,
                 correct_answer, topic, difficulty_level, difficulty_band,
                 mode, explanation, image_svg, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            """, (
                q['question_text'], q['option_a'], q['option_b'],
                q['option_c'], q['option_d'], q['correct_idx'],
                q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'],
                q['explanation'], q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            print(f"Insert error: {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {inserted} questions for {TOPIC} ({MODE} mode)")

# ============================================================
# MAIN
# ============================================================

def main():
    print("="*60)
    print("AgentMath - Whole Numbers Generator")
    print("Strand: Numeracy")
    print("Target: 600 questions (50 per level)")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Reading Numbers", generate_level_1),
        (2, "Place Value", generate_level_2),
        (3, "Comparing Numbers", generate_level_3),
        (4, "Ordering Numbers", generate_level_4),
        (5, "Rounding (10s, 100s)", generate_level_5),
        (6, "Rounding (1000s)", generate_level_6),
        (7, "Large Numbers", generate_level_7),
        (8, "Millions", generate_level_8),
        (9, "Estimation", generate_level_9),
        (10, "Number Properties", generate_level_10),
        (11, "Problem Solving", generate_level_11),
        (12, "Mastery Challenge", generate_level_12),
    ]
    
    for level, name, gen_func in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = gen_func()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    error_count = validate_questions(all_questions)
    
    if error_count == 0:
        print("\n✓ All validations passed!")
    else:
        print(f"\n⚠ Found {error_count} issues - review above")
    
    response = input("\nInsert into database? (y/n): ").strip().lower()
    if response == 'y':
        insert_questions(all_questions)
        print("\n✓ Done! Whole Numbers topic is ready.")
    else:
        print("\nSkipped database insertion.")

if __name__ == "__main__":
    main()
