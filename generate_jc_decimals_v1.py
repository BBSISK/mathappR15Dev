#!/usr/bin/env python3
"""
AgentMath - Decimals Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q1(b): Write down whole number nearest to 15.8
- 2023 OL Q1(a): Find 3.4 × 7
- 2022 OL Q2(c): 15% of €72, rounded to nearest euro
- 2024 HL Q4(b): Profit as percentage to 1 d.p.
- 2022 OL Q3(d): Convert £15.95 to euro, to nearest cent

Level Structure:
  L1-3:   Foundation (place value, reading/writing, comparing)
  L4-6:   Ordinary (operations, rounding basics)
  L7-9:   Higher (multi-step, conversions, estimation)
  L10-12: Application/Mastery (real-world, problem solving)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os
from decimal import Decimal, ROUND_HALF_UP

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'decimals'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Róisín', 'Seán', 
               'Ciara', 'Darragh', 'Éabha', 'Fionn', 'Gráinne', 'Liam', 'Meadhbh', 'Tadhg',
               'Áine', 'Cillian', 'Orlaith', 'Pádraig', 'Sinéad', 'Eoin', 'Caoimhe', 'Declan',
               'Emma', 'Jack', 'Sophie', 'Dylan', 'Katie', 'Ryan', 'Molly', 'Luke']

# Shopping items with prices
SHOP_ITEMS = [
    ('milk', 1.49), ('bread', 1.89), ('butter', 2.35), ('cheese', 3.49),
    ('apples', 2.99), ('bananas', 1.79), ('oranges', 2.49), ('grapes', 3.29),
    ('chicken', 5.99), ('beef', 7.49), ('fish', 6.29), ('eggs', 3.15),
    ('pasta', 1.29), ('rice', 2.19), ('cereal', 3.89), ('juice', 2.55),
    ('yogurt', 1.99), ('chocolate', 2.79), ('biscuits', 1.89), ('crisps', 1.65)
]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def round_val(value, decimals=2):
    """Round to specified decimal places"""
    return float(Decimal(str(value)).quantize(Decimal(f'0.{"0"*decimals}'), rounding=ROUND_HALF_UP))

def round_to_dp(value, dp):
    """Round to specified decimal places"""
    multiplier = 10 ** dp
    return round(value * multiplier) / multiplier

def get_place_value_name(position):
    """Get name for decimal place position"""
    names = {
        -1: 'tenths',
        -2: 'hundredths', 
        -3: 'thousandths',
        1: 'units',
        2: 'tens',
        3: 'hundreds'
    }
    return names.get(position, 'unknown')

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    unique_wrong = [str(w) for w in wrong_list if str(w) != correct_str]
    seen = set()
    unique_wrong = [w for w in unique_wrong if not (w in seen or seen.add(w))]
    
    options = [correct_str] + unique_wrong[:3]
    
    counter = 1
    while len(set(options)) < 4:
        new_opt = f"Option {counter}"
        if new_opt not in options:
            options.append(new_opt)
        counter += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    
    return options, correct_idx

# ============================================================
# SVG GENERATORS
# ============================================================

def generate_place_value_chart_svg(number):
    """Generate a place value chart showing decimal positions"""
    width = 280
    height = 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="5"/>'
    
    # Split number into parts
    num_str = str(number)
    if '.' in num_str:
        whole, decimal = num_str.split('.')
    else:
        whole, decimal = num_str, ''
    
    # Draw columns
    cols = ['Tens', 'Units', '.', 'Tenths', 'Hundredths']
    col_width = width / len(cols)
    
    for i, col in enumerate(cols):
        x = i * col_width
        # Header
        svg += f'<rect x="{x}" y="0" width="{col_width}" height="30" fill="#0284c7" stroke="#0284c7"/>'
        svg += f'<text x="{x + col_width/2}" y="20" text-anchor="middle" font-size="10" fill="white">{col}</text>'
        # Value cell
        svg += f'<rect x="{x}" y="30" width="{col_width}" height="40" fill="white" stroke="#0284c7"/>'
    
    # Fill in digits
    whole = whole.zfill(2)  # Ensure 2 digits
    decimal = (decimal + '00')[:2]  # Ensure 2 decimal places
    
    values = [whole[0] if whole[0] != '0' else '', whole[1], '.', decimal[0], decimal[1]]
    for i, val in enumerate(values):
        x = i * col_width + col_width/2
        svg += f'<text x="{x}" y="58" text-anchor="middle" font-size="16" fill="#1e40af" font-weight="bold">{val}</text>'
    
    svg += '</svg>'
    return svg

def generate_number_line_svg(number, min_val, max_val):
    """Generate a number line with a marked point"""
    width = 280
    height = 60
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="5"/>'
    
    # Number line
    line_y = 35
    line_start = 30
    line_end = 250
    
    svg += f'<line x1="{line_start}" y1="{line_y}" x2="{line_end}" y2="{line_y}" stroke="#1f2937" stroke-width="2"/>'
    
    # Ticks and labels
    num_ticks = 5
    for i in range(num_ticks + 1):
        x = line_start + (line_end - line_start) * i / num_ticks
        val = min_val + (max_val - min_val) * i / num_ticks
        svg += f'<line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#1f2937" stroke-width="2"/>'
        svg += f'<text x="{x}" y="{line_y + 20}" text-anchor="middle" font-size="10" fill="#374151">{round_val(val, 1)}</text>'
    
    # Mark the number
    if min_val <= number <= max_val:
        x_pos = line_start + (line_end - line_start) * (number - min_val) / (max_val - min_val)
        svg += f'<circle cx="{x_pos}" cy="{line_y}" r="6" fill="#ef4444"/>'
        svg += f'<text x="{x_pos}" y="15" text-anchor="middle" font-size="11" fill="#ef4444" font-weight="bold">?</text>'
    
    svg += '</svg>'
    return svg

def generate_money_svg(amount):
    """Generate a price tag visual"""
    width = 120
    height = 60
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    # Price tag shape
    svg += f'<path d="M10,10 L100,10 L110,30 L100,50 L10,50 Z" fill="#22c55e" stroke="#15803d" stroke-width="2"/>'
    svg += f'<circle cx="20" cy="30" r="5" fill="white"/>'
    svg += f'<text x="60" y="35" text-anchor="middle" font-size="14" fill="white" font-weight="bold">€{amount:.2f}</text>'
    svg += '</svg>'
    return svg

def generate_comparison_svg(num1, num2):
    """Generate visual comparison of two decimals"""
    width = 200
    height = 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f0fdf4" stroke="#22c55e" stroke-width="2" rx="5"/>'
    
    # Two boxes with numbers
    svg += f'<rect x="20" y="25" width="60" height="35" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2" rx="5"/>'
    svg += f'<text x="50" y="48" text-anchor="middle" font-size="14" fill="#1e40af" font-weight="bold">{num1}</text>'
    
    svg += f'<text x="100" y="48" text-anchor="middle" font-size="20" fill="#374151">?</text>'
    
    svg += f'<rect x="120" y="25" width="60" height="35" fill="#fecaca" stroke="#ef4444" stroke-width="2" rx="5"/>'
    svg += f'<text x="150" y="48" text-anchor="middle" font-size="14" fill="#b91c1c" font-weight="bold">{num2}</text>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Place Value (Foundation)
# ============================================================

def generate_level_1():
    """Understanding decimal place value"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['identify_digit', 'place_name', 'value_of_digit', 'write_decimal', 'read_decimal'])
        
        try:
            if q_type == 'identify_digit':
                whole = random.randint(1, 99)
                tenths = random.randint(1, 9)
                hundredths = random.randint(1, 9)
                number = float(f"{whole}.{tenths}{hundredths}")
                
                place = random.choice(['tenths', 'hundredths', 'units'])
                if place == 'tenths':
                    correct = str(tenths)
                elif place == 'hundredths':
                    correct = str(hundredths)
                else:
                    correct = str(whole % 10)
                
                q_text = f"In the number {number}, what digit is in the {place} place?"
                
                wrong_digits = [str(d) for d in range(10) if str(d) != correct]
                wrong = random.sample(wrong_digits, 3)
                
                visual = generate_place_value_chart_svg(number)
                explanation = f"In {number}:\\nThe {place} digit is {correct}."
                
            elif q_type == 'place_name':
                whole = random.randint(1, 9)
                tenths = random.randint(1, 9)
                hundredths = random.randint(1, 9)
                number = float(f"{whole}.{tenths}{hundredths}")
                
                digit_choice = random.choice(['tenths', 'hundredths'])
                if digit_choice == 'tenths':
                    digit = tenths
                    correct = "tenths"
                else:
                    digit = hundredths
                    correct = "hundredths"
                
                q_text = f"In {number}, the digit {digit} is in which place?"
                wrong = ["units", "tens", "thousands" if correct == "tenths" else "tenths"]
                
                visual = generate_place_value_chart_svg(number)
                explanation = f"In {number}, the digit {digit} is in the {correct} place."
                
            elif q_type == 'value_of_digit':
                whole = random.randint(1, 9)
                tenths = random.randint(1, 9)
                number = float(f"{whole}.{tenths}")
                
                choice = random.choice(['tenths', 'units'])
                if choice == 'tenths':
                    digit = tenths
                    correct = f"0.{tenths}"
                    wrong = [f"{tenths}", f"0.0{tenths}", f"{tenths}0"]
                else:
                    digit = whole
                    correct = str(whole)
                    wrong = [f"0.{whole}", f"{whole}0", f"0.0{whole}"]
                
                q_text = f"In {number}, what is the VALUE of the digit {digit}?"
                
                visual = None
                explanation = f"The digit {digit} is in the {choice} place.\\nIts value is {correct}."
                
            elif q_type == 'write_decimal':
                whole = random.randint(1, 20)
                tenths = random.randint(1, 9)
                
                q_text = f"Write '{whole} and {tenths} tenths' as a decimal."
                correct = f"{whole}.{tenths}"
                wrong = [f"{whole}{tenths}", f"{tenths}.{whole}", f"{whole}.0{tenths}"]
                
                visual = None
                explanation = f"{whole} and {tenths} tenths = {whole} + 0.{tenths} = {correct}"
                
            else:  # read_decimal
                whole = random.randint(1, 9)
                tenths = random.randint(1, 9)
                hundredths = random.randint(1, 9)
                number = float(f"{whole}.{tenths}{hundredths}")
                
                q_text = f"How do you read {number} in words?"
                correct = f"{whole} point {tenths} {hundredths}"
                wrong = [
                    f"{whole} point {tenths}{hundredths}",
                    f"{whole} and {tenths}{hundredths}",
                    f"{whole} point {hundredths} {tenths}"
                ]
                
                visual = None
                explanation = f"{number} is read as '{correct}' or '{whole} and {tenths}{hundredths} hundredths'."
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Comparing Decimals (Foundation)
# ============================================================

def generate_level_2():
    """Comparing and ordering decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['compare_two', 'largest', 'smallest', 'order', 'between'])
        
        try:
            if q_type == 'compare_two':
                num1 = round_val(random.uniform(0.1, 9.9), 1)
                num2 = round_val(random.uniform(0.1, 9.9), 1)
                while num1 == num2:
                    num2 = round_val(random.uniform(0.1, 9.9), 1)
                
                if num1 > num2:
                    correct = ">"
                else:
                    correct = "<"
                
                q_text = f"Which symbol goes in the box?\\n{num1} ☐ {num2}"
                wrong = ["<" if correct == ">" else ">", "=", "≠"]
                
                visual = generate_comparison_svg(num1, num2)
                explanation = f"{num1} is {'greater' if correct == '>' else 'less'} than {num2}, so {num1} {correct} {num2}"
                
            elif q_type == 'largest':
                base = random.randint(1, 8)
                decimals = [
                    round_val(base + random.uniform(0.01, 0.99), 2)
                    for _ in range(4)
                ]
                decimals = list(set([round_val(d, 2) for d in decimals]))
                while len(decimals) < 4:
                    decimals.append(round_val(base + random.uniform(0.01, 0.99), 2))
                decimals = decimals[:4]
                
                correct = str(max(decimals))
                wrong = [str(d) for d in decimals if str(d) != correct]
                
                q_text = f"Which is the largest?\\n{', '.join(str(d) for d in decimals)}"
                
                visual = None
                explanation = f"Comparing: {', '.join(str(d) for d in sorted(decimals))}\\nLargest is {correct}"
                
            elif q_type == 'smallest':
                base = random.randint(1, 8)
                decimals = [
                    round_val(base + random.uniform(0.01, 0.99), 2)
                    for _ in range(4)
                ]
                decimals = list(set([round_val(d, 2) for d in decimals]))
                while len(decimals) < 4:
                    decimals.append(round_val(base + random.uniform(0.01, 0.99), 2))
                decimals = decimals[:4]
                
                correct = str(min(decimals))
                wrong = [str(d) for d in decimals if str(d) != correct]
                
                q_text = f"Which is the smallest?\\n{', '.join(str(d) for d in decimals)}"
                
                visual = None
                explanation = f"Comparing: {', '.join(str(d) for d in sorted(decimals))}\\nSmallest is {correct}"
                
            elif q_type == 'order':
                base = random.randint(1, 5)
                nums = [round_val(base + random.uniform(0.1, 2.9), 1) for _ in range(3)]
                nums = list(set(nums))
                while len(nums) < 3:
                    nums.append(round_val(base + random.uniform(0.1, 2.9), 1))
                nums = nums[:3]
                
                sorted_nums = sorted(nums)
                correct = f"{sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}"
                
                wrong = [
                    f"{sorted_nums[2]}, {sorted_nums[1]}, {sorted_nums[0]}",
                    f"{sorted_nums[1]}, {sorted_nums[0]}, {sorted_nums[2]}",
                    f"{sorted_nums[0]}, {sorted_nums[2]}, {sorted_nums[1]}"
                ]
                
                q_text = f"Put in order from smallest to largest:\\n{nums[0]}, {nums[1]}, {nums[2]}"
                
                visual = None
                explanation = f"Ordering from smallest: {correct}"
                
            else:  # between
                lower = round_val(random.uniform(1, 8), 1)
                upper = round_val(lower + random.uniform(0.2, 0.8), 1)
                middle = round_val((lower + upper) / 2, 2)
                
                q_text = f"Which number is between {lower} and {upper}?"
                correct = str(middle)
                
                wrong = [
                    str(round_val(lower - 0.5, 1)),
                    str(round_val(upper + 0.5, 1)),
                    str(round_val(lower - 1, 1))
                ]
                
                visual = generate_number_line_svg(middle, lower - 0.5, upper + 0.5)
                explanation = f"{middle} is between {lower} and {upper}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Adding & Subtracting Decimals (Foundation)
# ============================================================

def generate_level_3():
    """Adding and subtracting decimals with same decimal places"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['add_simple', 'subtract_simple', 'add_money', 'subtract_money'])
        
        try:
            if q_type == 'add_simple':
                num1 = round_val(random.uniform(1, 9), 1)
                num2 = round_val(random.uniform(1, 9), 1)
                result = round_val(num1 + num2, 1)
                
                q_text = f"Calculate: {num1} + {num2}"
                correct = str(result)
                wrong = [
                    str(round_val(result + 1, 1)),
                    str(round_val(result - 1, 1)),
                    str(round_val(num1 * num2, 1))
                ]
                
                visual = None
                explanation = f"{num1} + {num2} = {result}"
                
            elif q_type == 'subtract_simple':
                num1 = round_val(random.uniform(5, 15), 1)
                num2 = round_val(random.uniform(1, num1 - 0.5), 1)
                result = round_val(num1 - num2, 1)
                
                q_text = f"Calculate: {num1} - {num2}"
                correct = str(result)
                wrong = [
                    str(round_val(result + 1, 1)),
                    str(round_val(result - 1, 1)),
                    str(round_val(num1 + num2, 1))
                ]
                
                visual = None
                explanation = f"{num1} - {num2} = {result}"
                
            elif q_type == 'add_money':
                item1, price1 = random.choice(SHOP_ITEMS)
                item2, price2 = random.choice(SHOP_ITEMS)
                while item1 == item2:
                    item2, price2 = random.choice(SHOP_ITEMS)
                
                total = round_val(price1 + price2, 2)
                
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} buys {item1} (€{price1:.2f}) and {item2} (€{price2:.2f}).\\nWhat is the total cost?"
                
                correct = f"€{total:.2f}"
                wrong = [
                    f"€{round_val(total + 1, 2):.2f}",
                    f"€{round_val(total - 0.5, 2):.2f}",
                    f"€{round_val(price1 * price2, 2):.2f}"
                ]
                
                visual = None
                explanation = f"€{price1:.2f} + €{price2:.2f} = €{total:.2f}"
                
            else:  # subtract_money
                paid = random.choice([5, 10, 20])
                item, price = random.choice([i for i in SHOP_ITEMS if i[1] < paid])
                change = round_val(paid - price, 2)
                
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} buys {item} for €{price:.2f} and pays with €{paid}.\\nHow much change?"
                
                correct = f"€{change:.2f}"
                wrong = [
                    f"€{round_val(change + 1, 2):.2f}",
                    f"€{round_val(change - 0.5, 2):.2f}",
                    f"€{round_val(paid + price, 2):.2f}"
                ]
                
                visual = generate_money_svg(price)
                explanation = f"€{paid:.2f} - €{price:.2f} = €{change:.2f}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Multiplying Decimals (Ordinary)
# ============================================================

def generate_level_4():
    """Multiplying decimals by whole numbers - SEC 2023 OL Q1(a) style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['decimal_times_whole', 'whole_times_decimal', 'money_multiply', 'unit_price'])
        
        try:
            if q_type == 'decimal_times_whole':
                # SEC 2023 OL Q1(a): 3.4 × 7
                decimal = round_val(random.uniform(1.1, 9.9), 1)
                whole = random.randint(2, 9)
                result = round_val(decimal * whole, 1)
                
                q_text = f"Calculate: {decimal} × {whole}"
                correct = str(result)
                wrong = [
                    str(round_val(result + whole, 1)),
                    str(round_val(result - decimal, 1)),
                    str(round_val(decimal + whole, 1))
                ]
                
                visual = None
                explanation = f"SEC 2023 OL Q1(a) style!\\n{decimal} × {whole} = {result}"
                
            elif q_type == 'whole_times_decimal':
                whole = random.randint(2, 12)
                decimal = round_val(random.uniform(0.1, 0.9), 1)
                result = round_val(whole * decimal, 1)
                
                q_text = f"Calculate: {whole} × {decimal}"
                correct = str(result)
                wrong = [
                    str(round_val(result + 1, 1)),
                    str(round_val(result * 10, 1)),
                    str(round_val(whole + decimal, 1))
                ]
                
                visual = None
                explanation = f"{whole} × {decimal} = {result}"
                
            elif q_type == 'money_multiply':
                price = round_val(random.uniform(1, 5), 2)
                quantity = random.randint(2, 6)
                total = round_val(price * quantity, 2)
                
                item = random.choice(['pencils', 'pens', 'notebooks', 'rulers', 'erasers'])
                name = random.choice(IRISH_NAMES)
                
                q_text = f"{name} buys {quantity} {item} at €{price:.2f} each.\\nWhat is the total cost?"
                correct = f"€{total:.2f}"
                wrong = [
                    f"€{round_val(total + price, 2):.2f}",
                    f"€{round_val(total - price, 2):.2f}",
                    f"€{round_val(price + quantity, 2):.2f}"
                ]
                
                visual = None
                explanation = f"{quantity} × €{price:.2f} = €{total:.2f}"
                
            else:  # unit_price
                # SEC 2023 OL Q1(b) style: milk at €1.27 per litre
                unit_price = round_val(random.uniform(1, 3), 2)
                quantity = random.randint(2, 5)
                total = round_val(unit_price * quantity, 2)
                
                item = random.choice(['litres of milk', 'kg of apples', 'metres of ribbon', 'kg of flour'])
                
                q_text = f"{quantity} {item} at €{unit_price:.2f} per unit.\\nTotal cost?"
                correct = f"€{total:.2f}"
                wrong = [
                    f"€{round_val(total + 1, 2):.2f}",
                    f"€{unit_price:.2f}",
                    f"€{round_val(unit_price + quantity, 2):.2f}"
                ]
                
                visual = None
                explanation = f"{quantity} × €{unit_price:.2f} = €{total:.2f}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 4,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Dividing Decimals (Ordinary)
# ============================================================

def generate_level_5():
    """Dividing decimals by whole numbers"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['decimal_divide_whole', 'share_money', 'find_unit_cost', 'average'])
        
        try:
            if q_type == 'decimal_divide_whole':
                divisor = random.randint(2, 5)
                result = round_val(random.uniform(1, 10), 1)
                dividend = round_val(result * divisor, 1)
                
                q_text = f"Calculate: {dividend} ÷ {divisor}"
                correct = str(result)
                wrong = [
                    str(round_val(result + 1, 1)),
                    str(round_val(result * 2, 1)),
                    str(round_val(dividend + divisor, 1))
                ]
                
                visual = None
                explanation = f"{dividend} ÷ {divisor} = {result}"
                
            elif q_type == 'share_money':
                num_people = random.randint(2, 5)
                per_person = round_val(random.uniform(5, 20), 2)
                total = round_val(per_person * num_people, 2)
                
                name = random.choice(IRISH_NAMES)
                q_text = f"€{total:.2f} is shared equally between {num_people} people.\\nHow much does each person get?"
                
                correct = f"€{per_person:.2f}"
                wrong = [
                    f"€{round_val(per_person + 2, 2):.2f}",
                    f"€{round_val(per_person - 1, 2):.2f}",
                    f"€{round_val(total / 2, 2):.2f}"
                ]
                
                visual = None
                explanation = f"€{total:.2f} ÷ {num_people} = €{per_person:.2f} each"
                
            elif q_type == 'find_unit_cost':
                quantity = random.randint(3, 6)
                unit_cost = round_val(random.uniform(1, 4), 2)
                total = round_val(unit_cost * quantity, 2)
                
                item = random.choice(['apples', 'oranges', 'bananas', 'pens', 'books'])
                
                q_text = f"{quantity} {item} cost €{total:.2f}.\\nWhat is the cost of one {item[:-1] if item.endswith('s') else item}?"
                
                correct = f"€{unit_cost:.2f}"
                wrong = [
                    f"€{round_val(unit_cost + 0.5, 2):.2f}",
                    f"€{round_val(unit_cost * 2, 2):.2f}",
                    f"€{total:.2f}"
                ]
                
                visual = None
                explanation = f"€{total:.2f} ÷ {quantity} = €{unit_cost:.2f} each"
                
            else:  # average
                num1 = round_val(random.uniform(5, 15), 1)
                num2 = round_val(random.uniform(5, 15), 1)
                average = round_val((num1 + num2) / 2, 1)
                
                q_text = f"Find the average of {num1} and {num2}."
                correct = str(average)
                wrong = [
                    str(round_val(num1 + num2, 1)),
                    str(round_val(average + 1, 1)),
                    str(round_val((num1 + num2) / 3, 1))
                ]
                
                visual = None
                explanation = f"Average = ({num1} + {num2}) ÷ 2 = {num1 + num2} ÷ 2 = {average}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 5,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Rounding Decimals (Ordinary)
# ============================================================

def generate_level_6():
    """Rounding decimals - SEC 2022 OL Q1(b) style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['round_whole', 'round_1dp', 'round_2dp', 'nearest_euro', 'nearest_cent'])
        
        try:
            if q_type == 'round_whole':
                # SEC 2022 OL Q1(b): "Write down the whole number nearest to 15.8"
                whole = random.randint(10, 50)
                decimal_part = random.randint(1, 9) / 10
                number = whole + decimal_part
                
                if decimal_part >= 0.5:
                    correct = str(whole + 1)
                else:
                    correct = str(whole)
                
                q_text = f"Write down the whole number nearest to {number}."
                wrong = [
                    str(whole if decimal_part >= 0.5 else whole + 1),
                    str(whole + 2),
                    str(whole - 1)
                ]
                
                visual = generate_number_line_svg(number, whole - 1, whole + 2)
                explanation = f"SEC 2022 OL Q1(b) style!\\n{number} rounded to nearest whole number is {correct}\\n(because .{int(decimal_part*10)} is {'≥' if decimal_part >= 0.5 else '<'} 5)"
                
            elif q_type == 'round_1dp':
                number = round_val(random.uniform(1, 20), 2)
                result = round_val(number, 1)
                
                q_text = f"Round {number} to 1 decimal place."
                correct = str(result)
                wrong = [
                    str(round_val(number, 0)),
                    str(round_val(number + 0.1, 1)),
                    str(round_val(number - 0.1, 1))
                ]
                
                visual = None
                explanation = f"{number} rounded to 1 d.p. is {result}"
                
            elif q_type == 'round_2dp':
                number = round_val(random.uniform(1, 10), 3)
                result = round_val(number, 2)
                
                q_text = f"Round {number} to 2 decimal places."
                correct = str(result)
                wrong = [
                    str(round_val(number, 1)),
                    str(round_val(number + 0.01, 2)),
                    str(round_val(number - 0.01, 2))
                ]
                
                visual = None
                explanation = f"{number} rounded to 2 d.p. is {result}"
                
            elif q_type == 'nearest_euro':
                # SEC 2022 OL Q2(c) style
                euros = random.randint(5, 50)
                cents = random.randint(1, 99)
                amount = euros + cents / 100
                
                if cents >= 50:
                    result = euros + 1
                else:
                    result = euros
                
                q_text = f"Round €{amount:.2f} to the nearest euro."
                correct = f"€{result}"
                wrong = [
                    f"€{result + 1}",
                    f"€{result - 1}",
                    f"€{euros if cents >= 50 else euros + 1}"
                ]
                
                visual = None
                explanation = f"SEC style! €{amount:.2f} → €{result} (nearest euro)"
                
            else:  # nearest_cent
                euros = random.randint(1, 20)
                cents = random.randint(10, 99)
                thousandths = random.randint(1, 9)
                amount = euros + cents / 100 + thousandths / 1000
                result = round_val(amount, 2)
                
                q_text = f"Round €{amount:.3f} to the nearest cent."
                correct = f"€{result:.2f}"
                wrong = [
                    f"€{round_val(result + 0.01, 2):.2f}",
                    f"€{round_val(result - 0.01, 2):.2f}",
                    f"€{round_val(amount, 1):.2f}"
                ]
                
                visual = None
                explanation = f"€{amount:.3f} rounded to nearest cent = €{result:.2f}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 6,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Decimal ↔ Fraction Conversion (Higher)
# ============================================================

def generate_level_7():
    """Converting between decimals and fractions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    # Common fraction-decimal pairs
    conversions = [
        (0.5, '1/2'), (0.25, '1/4'), (0.75, '3/4'),
        (0.1, '1/10'), (0.2, '1/5'), (0.4, '2/5'), (0.6, '3/5'), (0.8, '4/5'),
        (0.125, '1/8'), (0.375, '3/8'), (0.625, '5/8'), (0.875, '7/8'),
        (0.333, '1/3'), (0.667, '2/3'),
        (0.2, '2/10'), (0.3, '3/10'), (0.7, '7/10'), (0.9, '9/10')
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['decimal_to_fraction', 'fraction_to_decimal', 'simplify_decimal_fraction'])
        
        try:
            if q_type == 'decimal_to_fraction':
                decimal, fraction = random.choice(conversions)
                
                q_text = f"Write {decimal} as a fraction."
                correct = fraction
                
                # Generate wrong answers
                all_fractions = [f for d, f in conversions if f != fraction]
                wrong = random.sample(all_fractions, 3)
                
                visual = None
                explanation = f"{decimal} = {fraction}"
                
            elif q_type == 'fraction_to_decimal':
                decimal, fraction = random.choice(conversions)
                
                q_text = f"Write {fraction} as a decimal."
                correct = str(decimal)
                
                wrong = [
                    str(round_val(decimal + 0.1, 3)),
                    str(round_val(decimal * 2, 3)),
                    str(round_val(1 - decimal, 3))
                ]
                
                visual = None
                explanation = f"{fraction} = {decimal}"
                
            else:  # simplify_decimal_fraction
                # Decimals like 0.50 = 1/2
                pairs = [
                    ('0.50', '1/2'), ('0.20', '1/5'), ('0.40', '2/5'),
                    ('0.60', '3/5'), ('0.80', '4/5'), ('0.25', '1/4'),
                    ('0.75', '3/4'), ('0.10', '1/10')
                ]
                decimal_str, fraction = random.choice(pairs)
                
                q_text = f"Write {decimal_str} as a fraction in its simplest form."
                correct = fraction
                
                all_fractions = [f for d, f in pairs if f != fraction]
                wrong = random.sample(all_fractions, min(3, len(all_fractions)))
                while len(wrong) < 3:
                    wrong.append(f"{random.randint(1,9)}/{random.randint(2,10)}")
                
                visual = None
                explanation = f"{decimal_str} = {fraction} (simplified)"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 7,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Decimal ↔ Percentage Conversion (Higher)
# ============================================================

def generate_level_8():
    """Converting between decimals and percentages"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['decimal_to_percent', 'percent_to_decimal', 'percent_of_decimal'])
        
        try:
            if q_type == 'decimal_to_percent':
                decimal = round_val(random.uniform(0.01, 0.99), 2)
                percent = int(decimal * 100)
                
                q_text = f"Write {decimal} as a percentage."
                correct = f"{percent}%"
                wrong = [
                    f"{percent * 10}%",
                    f"{percent // 10}%",
                    f"{100 - percent}%"
                ]
                
                visual = None
                explanation = f"{decimal} × 100 = {percent}%"
                
            elif q_type == 'percent_to_decimal':
                percent = random.randint(1, 99)
                decimal = percent / 100
                
                q_text = f"Write {percent}% as a decimal."
                correct = str(decimal)
                wrong = [
                    str(decimal * 10),
                    str(decimal / 10),
                    str(round_val(1 - decimal, 2))
                ]
                
                visual = None
                explanation = f"{percent}% = {percent} ÷ 100 = {decimal}"
                
            else:  # percent_of_decimal
                decimal = round_val(random.uniform(0.1, 0.9), 1)
                amount = random.choice([10, 20, 50, 100, 200])
                result = round_val(decimal * amount, 1)
                percent = int(decimal * 100)
                
                q_text = f"Find {percent}% of {amount}."
                correct = str(result)
                wrong = [
                    str(round_val(result + 10, 1)),
                    str(round_val(result / 2, 1)),
                    str(amount)
                ]
                
                visual = None
                explanation = f"{percent}% of {amount} = {decimal} × {amount} = {result}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 8,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Multiplying Decimals by Decimals (Higher)
# ============================================================

def generate_level_9():
    """Multiplying decimals by decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['simple_mult', 'area_problem', 'scaling'])
        
        try:
            if q_type == 'simple_mult':
                num1 = round_val(random.uniform(0.1, 5), 1)
                num2 = round_val(random.uniform(0.1, 5), 1)
                result = round_val(num1 * num2, 2)
                
                q_text = f"Calculate: {num1} × {num2}"
                correct = str(result)
                wrong = [
                    str(round_val(num1 + num2, 2)),
                    str(round_val(result * 10, 2)),
                    str(round_val(result / 10, 2))
                ]
                
                visual = None
                explanation = f"{num1} × {num2} = {result}"
                
            elif q_type == 'area_problem':
                length = round_val(random.uniform(2, 8), 1)
                width = round_val(random.uniform(2, 6), 1)
                area = round_val(length * width, 2)
                
                q_text = f"A rectangle has length {length} m and width {width} m.\\nWhat is its area?"
                correct = f"{area} m²"
                wrong = [
                    f"{round_val(length + width, 1)} m²",
                    f"{round_val(2 * (length + width), 1)} m²",
                    f"{round_val(area + 5, 2)} m²"
                ]
                
                visual = None
                explanation = f"Area = length × width\\n= {length} × {width}\\n= {area} m²"
                
            else:  # scaling
                original = round_val(random.uniform(5, 20), 1)
                scale = round_val(random.uniform(0.5, 2), 1)
                result = round_val(original * scale, 2)
                
                q_text = f"Multiply {original} by {scale}."
                correct = str(result)
                wrong = [
                    str(round_val(original + scale, 2)),
                    str(round_val(original / scale, 2)),
                    str(round_val(result + original, 2))
                ]
                
                visual = None
                explanation = f"{original} × {scale} = {result}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 9,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Dividing Decimals by Decimals (Application)
# ============================================================

def generate_level_10():
    """Dividing decimals by decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['simple_div', 'how_many_fit', 'rate_problem'])
        
        try:
            if q_type == 'simple_div':
                divisor = round_val(random.uniform(0.2, 2), 1)
                result = round_val(random.uniform(2, 10), 1)
                dividend = round_val(divisor * result, 2)
                
                q_text = f"Calculate: {dividend} ÷ {divisor}"
                correct = str(result)
                wrong = [
                    str(round_val(dividend * divisor, 2)),
                    str(round_val(result + divisor, 1)),
                    str(round_val(dividend, 1))
                ]
                
                visual = None
                explanation = f"{dividend} ÷ {divisor} = {result}"
                
            elif q_type == 'how_many_fit':
                piece = round_val(random.uniform(0.2, 0.8), 1)
                total = round_val(piece * random.randint(5, 12), 1)
                result = int(total / piece)
                
                q_text = f"How many pieces of {piece} m can be cut from {total} m of ribbon?"
                correct = str(result)
                wrong = [
                    str(result + 2),
                    str(result - 1),
                    str(int(total))
                ]
                
                visual = None
                explanation = f"{total} ÷ {piece} = {result} pieces"
                
            else:  # rate_problem
                distance = round_val(random.uniform(5, 20), 1)
                time = round_val(random.uniform(0.5, 2), 1)
                speed = round_val(distance / time, 1)
                
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} cycles {distance} km in {time} hours.\\nWhat is the average speed in km/h?"
                
                correct = f"{speed} km/h"
                wrong = [
                    f"{round_val(distance * time, 1)} km/h",
                    f"{round_val(speed + 5, 1)} km/h",
                    f"{distance} km/h"
                ]
                
                visual = None
                explanation = f"Speed = Distance ÷ Time\\n= {distance} ÷ {time}\\n= {speed} km/h"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 10,
                'difficulty_band': 'application',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 11: Estimation & Approximation (Application)
# ============================================================

def generate_level_11():
    """Estimation and checking reasonableness"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['estimate_product', 'estimate_sum', 'check_reasonable', 'approximate'])
        
        try:
            if q_type == 'estimate_product':
                num1 = round_val(random.uniform(2, 9), 1)
                num2 = round_val(random.uniform(2, 9), 1)
                exact = round_val(num1 * num2, 2)
                
                # Round to nearest whole for estimate
                est1 = round(num1)
                est2 = round(num2)
                estimate = est1 * est2
                
                q_text = f"Estimate {num1} × {num2} by rounding to whole numbers first."
                correct = str(estimate)
                wrong = [
                    str(exact),
                    str(estimate + 5),
                    str(estimate - 3)
                ]
                
                visual = None
                explanation = f"{num1} ≈ {est1}, {num2} ≈ {est2}\\nEstimate: {est1} × {est2} = {estimate}"
                
            elif q_type == 'estimate_sum':
                num1 = round_val(random.uniform(10, 50), 1)
                num2 = round_val(random.uniform(10, 50), 1)
                exact = round_val(num1 + num2, 1)
                
                est1 = round(num1)
                est2 = round(num2)
                estimate = est1 + est2
                
                q_text = f"Estimate {num1} + {num2} by rounding to whole numbers."
                correct = str(estimate)
                wrong = [
                    str(exact),
                    str(estimate + 10),
                    str(estimate - 5)
                ]
                
                visual = None
                explanation = f"{num1} ≈ {est1}, {num2} ≈ {est2}\\nEstimate: {est1} + {est2} = {estimate}"
                
            elif q_type == 'check_reasonable':
                num1 = round_val(random.uniform(3, 8), 1)
                num2 = round_val(random.uniform(3, 8), 1)
                correct_result = round_val(num1 * num2, 2)
                
                # Create wrong answers
                wrong_result = round_val(correct_result * 10, 2)
                
                q_text = f"Which is the most reasonable answer for {num1} × {num2}?"
                correct = str(correct_result)
                wrong = [
                    str(wrong_result),
                    str(round_val(correct_result / 10, 2)),
                    str(round_val(num1 + num2, 1))
                ]
                
                visual = None
                explanation = f"{num1} × {num2} ≈ {round(num1)} × {round(num2)} = {round(num1) * round(num2)}\\nSo {correct_result} is reasonable."
                
            else:  # approximate
                target = random.randint(10, 50)
                close = target + random.choice([-0.1, 0.1, -0.2, 0.2])
                
                q_text = f"Which decimal is closest to {target}?"
                correct = str(close)
                wrong = [
                    str(target + 5),
                    str(target - 3),
                    str(target + 10)
                ]
                
                visual = None
                explanation = f"{close} is closest to {target}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 11,
                'difficulty_band': 'application',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 12: Multi-Step Problems (Mastery)
# ============================================================

def generate_level_12():
    """Complex multi-step decimal problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 25
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['shopping_total', 'bill_change', 'discount_problem', 'mixed_operations'])
        
        try:
            if q_type == 'shopping_total':
                # SEC 2024 OL Q2(a) style
                items = random.sample(SHOP_ITEMS, 3)
                total = sum(price for item, price in items)
                total = round_val(total, 2)
                
                name = random.choice(IRISH_NAMES)
                item_list = ', '.join([f"{item} (€{price:.2f})" for item, price in items])
                
                q_text = f"{name} buys: {item_list}.\\nWhat is the total cost?"
                correct = f"€{total:.2f}"
                wrong = [
                    f"€{round_val(total + 1, 2):.2f}",
                    f"€{round_val(total - 0.50, 2):.2f}",
                    f"€{round_val(total * 1.1, 2):.2f}"
                ]
                
                visual = None
                explanation = f"Total = €{items[0][1]:.2f} + €{items[1][1]:.2f} + €{items[2][1]:.2f} = €{total:.2f}"
                
            elif q_type == 'bill_change':
                # SEC style: pay with note, calculate change
                items = random.sample(SHOP_ITEMS, 2)
                total = sum(price for item, price in items)
                total = round_val(total, 2)
                
                payment = random.choice([10, 20, 50])
                while payment < total:
                    payment = random.choice([20, 50, 100])
                
                change = round_val(payment - total, 2)
                
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} buys {items[0][0]} (€{items[0][1]:.2f}) and {items[1][0]} (€{items[1][1]:.2f}).\\nThey pay with €{payment}. How much change?"
                
                correct = f"€{change:.2f}"
                wrong = [
                    f"€{round_val(change + 1, 2):.2f}",
                    f"€{round_val(change - 0.50, 2):.2f}",
                    f"€{total:.2f}"
                ]
                
                visual = None
                explanation = f"Total: €{items[0][1]:.2f} + €{items[1][1]:.2f} = €{total:.2f}\\nChange: €{payment} - €{total:.2f} = €{change:.2f}"
                
            elif q_type == 'discount_problem':
                original = round_val(random.uniform(20, 80), 2)
                discount_percent = random.choice([10, 15, 20, 25])
                discount_amount = round_val(original * discount_percent / 100, 2)
                sale_price = round_val(original - discount_amount, 2)
                
                item = random.choice(['jacket', 'shoes', 'bag', 'dress', 'shirt'])
                
                q_text = f"A {item} costs €{original:.2f}. There is {discount_percent}% off.\\nWhat is the sale price?"
                correct = f"€{sale_price:.2f}"
                wrong = [
                    f"€{original:.2f}",
                    f"€{discount_amount:.2f}",
                    f"€{round_val(sale_price + 5, 2):.2f}"
                ]
                
                visual = None
                explanation = f"Discount: {discount_percent}% of €{original:.2f} = €{discount_amount:.2f}\\nSale price: €{original:.2f} - €{discount_amount:.2f} = €{sale_price:.2f}"
                
            else:  # mixed_operations
                num1 = round_val(random.uniform(2, 8), 1)
                num2 = round_val(random.uniform(2, 8), 1)
                num3 = round_val(random.uniform(1, 5), 1)
                
                # (num1 + num2) × num3
                sum_val = round_val(num1 + num2, 1)
                result = round_val(sum_val * num3, 2)
                
                q_text = f"Calculate: ({num1} + {num2}) × {num3}"
                correct = str(result)
                wrong = [
                    str(round_val(num1 + num2 * num3, 2)),
                    str(round_val(num1 * num2 + num3, 2)),
                    str(round_val(result + 5, 2))
                ]
                
                visual = None
                explanation = f"({num1} + {num2}) × {num3}\\n= {sum_val} × {num3}\\n= {result}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if q_text in used or len(set(options)) != 4:
                continue
            used.add(q_text)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 12,
                'difficulty_band': 'mastery',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# VALIDATION
# ============================================================

def validate_questions(questions):
    """Validate generated questions"""
    errors = []
    level_counts = {}
    level_visuals = {}
    
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if level not in level_visuals:
            level_visuals[level] = {'total': 0, 'visual': 0}
        level_visuals[level]['total'] += 1
        if q.get('image_svg'):
            level_visuals[level]['visual'] += 1
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options")
        
        if not q.get('explanation'):
            errors.append(f"Level {level}: Missing explanation")
    
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    level_names = {
        1: "Place Value",
        2: "Comparing Decimals",
        3: "Add/Subtract",
        4: "Multiply by Whole",
        5: "Divide by Whole",
        6: "Rounding",
        7: "Decimal ↔ Fraction",
        8: "Decimal ↔ Percent",
        9: "Multiply Decimals",
        10: "Divide Decimals",
        11: "Estimation",
        12: "Multi-Step Problems"
    }
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual_pct = 0
        if level in level_visuals and level_visuals[level]['total'] > 0:
            visual_pct = (level_visuals[level]['visual'] / level_visuals[level]['total']) * 100
        
        status = "✓" if count == QUESTIONS_PER_LEVEL else "✗"
        name = level_names.get(level, "Unknown")
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} | Visual: {visual_pct:5.1f}% | {status} {name}")
    
    print("=" * 60)
    print(f"Total Questions: {len(questions)}")
    print(f"Total Errors: {len(errors)}")
    print("=" * 60)
    
    return len(errors)

# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database"""
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
    """, (TOPIC, MODE))
    
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions")
    
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
                q['question_text'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'], q['explanation'], q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {inserted} questions")
    return True

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("DECIMALS - JC EXAM QUESTION GENERATOR")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Target: {QUESTIONS_PER_LEVEL * 12} questions")
    print("=" * 60)
    
    all_questions = []
    
    generators = [
        (1, "Place Value", generate_level_1),
        (2, "Comparing Decimals", generate_level_2),
        (3, "Add/Subtract", generate_level_3),
        (4, "Multiply by Whole", generate_level_4),
        (5, "Divide by Whole", generate_level_5),
        (6, "Rounding", generate_level_6),
        (7, "Decimal ↔ Fraction", generate_level_7),
        (8, "Decimal ↔ Percent", generate_level_8),
        (9, "Multiply Decimals", generate_level_9),
        (10, "Divide Decimals", generate_level_10),
        (11, "Estimation", generate_level_11),
        (12, "Multi-Step Problems", generate_level_12),
    ]
    
    for level, name, generator in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = generator()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    validate_questions(all_questions)
    
    print("=" * 60)
    response = input("Insert into database? (y/n): ").strip().lower()
    
    if response == 'y':
        insert_questions(all_questions)
        print("\n✓ Done!")
    else:
        print("Skipped.")

if __name__ == "__main__":
    main()
