#!/usr/bin/env python3
"""
AgentMath - Basic Decimals Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Understanding decimals, place value, reading/writing
  L4-6:   Developing - Comparing, ordering, rounding decimals
  L7-9:   Proficient - Adding/subtracting decimals, word problems
  L10-12: Advanced - Multiplying/dividing decimals, problem solving

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'basic_decimals'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam'
]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_difficulty_band(level):
    if level <= 3:
        return 'foundation'
    elif level <= 6:
        return 'developing'
    elif level <= 9:
        return 'proficient'
    else:
        return 'advanced'

def make_options(correct, wrong_list):
    correct_str = str(correct)
    unique_wrong = []
    for w in wrong_list:
        w_str = str(w)
        if w_str != correct_str and w_str not in unique_wrong:
            unique_wrong.append(w_str)
    
    options = [correct_str] + unique_wrong[:3]
    
    fallback_idx = 1
    while len(set(options)) < 4:
        options.append(f"Option {fallback_idx}")
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    return options, correct_idx

def generate_place_value_svg(decimal_num):
    """Generate SVG showing decimal place value chart"""
    parts = str(decimal_num).split('.')
    whole = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else "0"
    
    svg = f'''<svg viewBox="0 0 300 80" xmlns="http://www.w3.org/2000/svg">
    <style>
        .box {{ fill: #f3f4f6; stroke: #d1d5db; }}
        .header {{ font-size: 10px; fill: #6b7280; text-anchor: middle; }}
        .digit {{ font-size: 18px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
        .point {{ font-size: 24px; fill: #10b981; font-weight: bold; }}
    </style>'''
    
    # Tens, Units, decimal point, tenths, hundredths
    positions = [(30, "T"), (80, "U"), (130, "."), (180, "t"), (230, "h")]
    
    # Pad whole number
    whole = whole.zfill(2)
    decimal_part = decimal_part.ljust(2, '0')[:2]
    
    digits = [whole[0], whole[1], ".", decimal_part[0], decimal_part[1]]
    
    for i, (x, label) in enumerate(positions):
        if label != ".":
            svg += f'<rect x="{x - 20}" y="25" width="40" height="40" class="box"/>'
            svg += f'<text x="{x}" y="20" class="header">{label}</text>'
            svg += f'<text x="{x}" y="52" class="digit">{digits[i]}</text>'
        else:
            svg += f'<text x="{x}" y="55" class="point">.</text>'
    
    svg += '</svg>'
    return svg

def generate_number_line_decimal_svg(start, end, highlight=None):
    """Generate SVG number line for decimals"""
    svg = f'''<svg viewBox="0 0 350 70" xmlns="http://www.w3.org/2000/svg">
    <style>
        .line {{ stroke: #374151; stroke-width: 2; }}
        .tick {{ stroke: #374151; stroke-width: 1; }}
        .label {{ font-size: 10px; fill: #374151; text-anchor: middle; }}
        .highlight {{ fill: #10b981; font-weight: bold; font-size: 11px; }}
    </style>
    <line x1="20" y1="40" x2="330" y2="40" class="line"/>'''
    
    step = (end - start) / 10
    for i in range(11):
        x = 20 + i * 31
        val = start + i * step
        svg += f'<line x1="{x}" y1="35" x2="{x}" y2="45" class="tick"/>'
        
        label_class = 'highlight' if highlight and abs(val - highlight) < 0.001 else 'label'
        svg += f'<text x="{x}" y="60" class="{label_class}">{val:.1f}</text>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Understanding Decimals (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Understanding Decimals - What is a decimal?"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['read', 'write', 'meaning', 'identify'])
            
            if q_type == 'read':
                whole = random.randint(0, 9)
                tenth = random.randint(1, 9)
                decimal = f"{whole}.{tenth}"
                
                q_text = f"How do you read {decimal}?"
                correct = f"{whole} point {tenth}"
                wrong = [f"{whole} point {tenth + 1}", f"{whole}{tenth}", f"{tenth} point {whole}"]
                explanation = f"Step 1: Read the whole number, say 'point', then the decimal digit. Step 2: {decimal} = '{whole} point {tenth}'. ✓"
                image_svg = None
                
            elif q_type == 'write':
                whole = random.randint(1, 9)
                tenth = random.randint(1, 9)
                
                q_text = f"Write '{whole} point {tenth}' as a decimal number."
                correct = f"{whole}.{tenth}"
                wrong = [f"{whole}{tenth}", f"{tenth}.{whole}", f"0.{whole}{tenth}"]
                explanation = f"Step 1: Write whole number, decimal point, then tenths. Step 2: {whole}.{tenth}. ✓"
                image_svg = None
                
            elif q_type == 'meaning':
                tenth = random.randint(1, 9)
                
                q_text = f"What does the {tenth} mean in 0.{tenth}?"
                correct = f"{tenth} tenths"
                wrong = [f"{tenth} units", f"{tenth} hundredths", f"{tenth} ones"]
                explanation = f"Step 1: The digit after the decimal point shows tenths. Step 2: 0.{tenth} = {tenth} tenths. ✓"
                image_svg = None
                
            else:  # identify
                whole = random.randint(1, 5)
                tenth = random.randint(1, 9)
                decimal = f"{whole}.{tenth}"
                
                q_text = f"In {decimal}, what digit is in the tenths place?"
                correct = str(tenth)
                wrong = [str(whole), str(tenth + 1), "0"]
                explanation = f"Step 1: Tenths is the first digit after the decimal point. Step 2: In {decimal}, tenths = {tenth}. ✓"
                image_svg = generate_place_value_svg(float(decimal))
            
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
# LEVEL 2: Decimal Place Value (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Decimal Place Value - Tenths and Hundredths"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['tenths', 'hundredths', 'identify', 'value'])
            
            if q_type == 'tenths':
                tenth = random.randint(1, 9)
                
                q_text = f"What is {tenth}/10 as a decimal?"
                correct = f"0.{tenth}"
                wrong = [f"{tenth}.0", f"0.0{tenth}", f"1.{tenth}"]
                explanation = f"Step 1: {tenth}/10 = {tenth} tenths. Step 2: Write as 0.{tenth}. ✓"
                image_svg = None
                
            elif q_type == 'hundredths':
                hundredth = random.randint(1, 9)
                
                q_text = f"What is {hundredth}/100 as a decimal?"
                correct = f"0.0{hundredth}"
                wrong = [f"0.{hundredth}", f"{hundredth}.0", f"0.{hundredth}0"]
                explanation = f"Step 1: {hundredth}/100 = {hundredth} hundredths. Step 2: Write as 0.0{hundredth}. ✓"
                image_svg = None
                
            elif q_type == 'identify':
                whole = random.randint(1, 9)
                tenth = random.randint(1, 9)
                hundredth = random.randint(1, 9)
                decimal = f"{whole}.{tenth}{hundredth}"
                
                place = random.choice(['tenths', 'hundredths', 'units'])
                if place == 'tenths':
                    answer = str(tenth)
                elif place == 'hundredths':
                    answer = str(hundredth)
                else:
                    answer = str(whole)
                
                q_text = f"In {decimal}, what digit is in the {place} place?"
                correct = answer
                wrong = [str(tenth) if answer != str(tenth) else str(hundredth), 
                         str(whole) if answer != str(whole) else str(tenth),
                         str(hundredth) if answer != str(hundredth) else str(whole)]
                explanation = f"Step 1: Find the {place} place in {decimal}. Step 2: Answer = {answer}. ✓"
                image_svg = generate_place_value_svg(float(decimal))
                
            else:  # value
                whole = random.randint(1, 5)
                tenth = random.randint(1, 9)
                decimal = f"{whole}.{tenth}"
                
                q_text = f"What is the value of the {tenth} in {decimal}?"
                correct = f"{tenth}/10 or 0.{tenth}"
                wrong = [f"{tenth}", f"{tenth}/100", f"{whole}.{tenth}"]
                explanation = f"Step 1: {tenth} is in the tenths place. Step 2: Value = {tenth}/10 = 0.{tenth}. ✓"
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
# LEVEL 3: Decimals and Fractions (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Converting between Decimals and Fractions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    conversions = [
        (0.5, "1/2"), (0.25, "1/4"), (0.75, "3/4"),
        (0.1, "1/10"), (0.2, "2/10"), (0.3, "3/10"),
        (0.4, "4/10"), (0.5, "5/10"), (0.6, "6/10"),
        (0.7, "7/10"), (0.8, "8/10"), (0.9, "9/10")
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['dec_to_frac', 'frac_to_dec', 'match', 'word'])
            
            if q_type == 'dec_to_frac':
                decimal, fraction = random.choice(conversions)
                
                q_text = f"Write {decimal} as a fraction."
                correct = fraction
                other_fracs = [f[1] for f in conversions if f[1] != fraction]
                wrong = random.sample(other_fracs, 3)
                explanation = f"Step 1: {decimal} = {fraction}. ✓"
                image_svg = None
                
            elif q_type == 'frac_to_dec':
                decimal, fraction = random.choice(conversions)
                
                q_text = f"Write {fraction} as a decimal."
                correct = str(decimal)
                wrong = [str(decimal + 0.1), str(decimal - 0.1) if decimal > 0.1 else "0.05", str(1 - decimal)]
                explanation = f"Step 1: {fraction} = {decimal}. ✓"
                image_svg = None
                
            elif q_type == 'match':
                decimal, fraction = random.choice([(0.5, "1/2"), (0.25, "1/4"), (0.75, "3/4")])
                
                q_text = f"Which fraction equals {decimal}?"
                correct = fraction
                wrong = ["1/3", "2/3", "1/5"]
                explanation = f"Step 1: {decimal} = {fraction}. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                decimal, fraction = random.choice([(0.5, "half"), (0.25, "quarter"), (0.75, "three quarters")])
                
                q_text = f"{name} ate {fraction} of a pizza. What decimal is this?"
                correct = str(decimal)
                wrong = ["0.3", "0.4" if decimal != 0.5 else "0.6", "1.0"]
                explanation = f"Step 1: {fraction} = {decimal}. ✓"
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
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Comparing Decimals (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Comparing Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['bigger', 'smaller', 'symbol', 'word'])
            
            if q_type == 'bigger':
                d1 = round(random.uniform(0.1, 0.9), 1)
                d2 = round(random.uniform(0.1, 0.9), 1)
                while d1 == d2:
                    d2 = round(random.uniform(0.1, 0.9), 1)
                
                bigger = max(d1, d2)
                q_text = f"Which is bigger: {d1} or {d2}?"
                correct = str(bigger)
                wrong = [str(min(d1, d2)), "Same", str(d1 + d2)]
                explanation = f"Step 1: Compare tenths. Step 2: {bigger} is bigger. ✓"
                image_svg = None
                
            elif q_type == 'smaller':
                d1 = round(random.uniform(1.1, 5.9), 1)
                d2 = round(random.uniform(1.1, 5.9), 1)
                while d1 == d2:
                    d2 = round(random.uniform(1.1, 5.9), 1)
                
                smaller = min(d1, d2)
                q_text = f"Which is smaller: {d1} or {d2}?"
                correct = str(smaller)
                wrong = [str(max(d1, d2)), "Same", str(abs(d1 - d2))]
                explanation = f"Step 1: Compare whole numbers first, then decimals. Step 2: {smaller} is smaller. ✓"
                image_svg = None
                
            elif q_type == 'symbol':
                d1 = round(random.uniform(0.1, 2.9), 1)
                d2 = round(random.uniform(0.1, 2.9), 1)
                while d1 == d2:
                    d2 = round(random.uniform(0.1, 2.9), 1)
                
                if d1 > d2:
                    symbol = ">"
                else:
                    symbol = "<"
                
                q_text = f"Which symbol makes this true? {d1} ○ {d2}"
                correct = symbol
                wrong = [">" if symbol == "<" else "<", "=", "≠"]
                explanation = f"Step 1: {d1} is {'greater' if d1 > d2 else 'less'} than {d2}. Step 2: {d1} {symbol} {d2}. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                d1 = round(random.uniform(1.1, 3.9), 1)
                d2 = round(random.uniform(1.1, 3.9), 1)
                while d1 == d2:
                    d2 = round(random.uniform(1.1, 3.9), 1)
                
                q_text = f"{name} ran {d1} km. Their friend ran {d2} km. Who ran further?"
                correct = f"{name}" if d1 > d2 else "Friend"
                wrong = [f"{name}" if d1 < d2 else "Friend", "Same distance", "Cannot tell"]
                explanation = f"Step 1: Compare {d1} and {d2}. Step 2: {max(d1, d2)} > {min(d1, d2)}. ✓"
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
                'difficulty': 4,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Ordering Decimals (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Ordering Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['ascending', 'descending', 'insert', 'position'])
            
            if q_type == 'ascending':
                decimals = [round(random.uniform(0.1, 2.9), 1) for _ in range(3)]
                while len(set(decimals)) != 3:
                    decimals = [round(random.uniform(0.1, 2.9), 1) for _ in range(3)]
                
                sorted_dec = sorted(decimals)
                q_text = f"Put in order from smallest to biggest: {decimals[0]}, {decimals[1]}, {decimals[2]}"
                correct = f"{sorted_dec[0]}, {sorted_dec[1]}, {sorted_dec[2]}"
                wrong = [f"{sorted_dec[2]}, {sorted_dec[1]}, {sorted_dec[0]}", 
                         f"{decimals[0]}, {decimals[1]}, {decimals[2]}",
                         f"{sorted_dec[1]}, {sorted_dec[0]}, {sorted_dec[2]}"]
                explanation = f"Step 1: Compare each decimal. Step 2: Order = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'descending':
                decimals = [round(random.uniform(1.1, 4.9), 1) for _ in range(3)]
                while len(set(decimals)) != 3:
                    decimals = [round(random.uniform(1.1, 4.9), 1) for _ in range(3)]
                
                sorted_dec = sorted(decimals, reverse=True)
                q_text = f"Put in order from biggest to smallest: {decimals[0]}, {decimals[1]}, {decimals[2]}"
                correct = f"{sorted_dec[0]}, {sorted_dec[1]}, {sorted_dec[2]}"
                wrong = [f"{sorted_dec[2]}, {sorted_dec[1]}, {sorted_dec[0]}", 
                         f"{decimals[0]}, {decimals[1]}, {decimals[2]}",
                         f"{sorted_dec[1]}, {sorted_dec[2]}, {sorted_dec[0]}"]
                explanation = f"Step 1: Find biggest, then next, then smallest. Step 2: Order = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'insert':
                base = round(random.uniform(1.0, 3.0), 1)
                to_insert = round(base + random.choice([0.2, 0.3, 0.4]), 1)
                lower = round(base - 0.1, 1)
                upper = round(base + 0.6, 1)
                
                q_text = f"Where does {to_insert} go in this sequence: {lower}, ___, {upper}?"
                correct = f"Between {lower} and {upper}"
                wrong = [f"Before {lower}", f"After {upper}", "Doesn't fit"]
                explanation = f"Step 1: {lower} < {to_insert} < {upper}. Step 2: It goes in the middle. ✓"
                image_svg = generate_number_line_decimal_svg(lower, upper, to_insert)
                
            else:  # position
                decimals = [round(i * 0.1 + 1, 1) for i in range(5)]
                target = random.choice(decimals)
                position = decimals.index(target) + 1
                ordinals = ["1st", "2nd", "3rd", "4th", "5th"]
                
                q_text = f"In the list {', '.join(map(str, decimals))}, what position is {target}?"
                correct = ordinals[position - 1]
                wrong = [o for o in ordinals if o != ordinals[position - 1]][:3]
                explanation = f"Step 1: Count position from left. Step 2: {target} is in {ordinals[position - 1]} position. ✓"
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
# LEVEL 6: Rounding Decimals (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Rounding Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['to_whole', 'to_tenth', 'word', 'estimate'])
            
            if q_type == 'to_whole':
                whole = random.randint(1, 20)
                tenth = random.randint(1, 9)
                decimal = float(f"{whole}.{tenth}")
                
                rounded = round(decimal)
                q_text = f"Round {decimal} to the nearest whole number."
                correct = str(rounded)
                wrong = [str(rounded + 1), str(rounded - 1), str(whole)]
                explanation = f"Step 1: Look at tenths ({tenth}). {'≥5 so round up' if tenth >= 5 else '<5 so round down'}. Step 2: {decimal} ≈ {rounded}. ✓"
                image_svg = None
                
            elif q_type == 'to_tenth':
                whole = random.randint(1, 10)
                tenth = random.randint(0, 9)
                hundredth = random.randint(1, 9)
                decimal = float(f"{whole}.{tenth}{hundredth}")
                
                rounded = round(decimal, 1)
                q_text = f"Round {decimal} to 1 decimal place."
                correct = str(rounded)
                wrong = [str(round(rounded + 0.1, 1)), str(round(rounded - 0.1, 1)), str(whole)]
                explanation = f"Step 1: Look at hundredths ({hundredth}). {'≥5 so round up' if hundredth >= 5 else '<5 so round down'}. Step 2: {decimal} ≈ {rounded}. ✓"
                image_svg = None
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                decimal = round(random.uniform(1.1, 9.9), 1)
                rounded = round(decimal)
                
                q_text = f"{name}'s height is {decimal} metres. Rounded to the nearest metre, how tall?"
                correct = f"{rounded} metres"
                wrong = [f"{rounded + 1} metres", f"{rounded - 1} metres", f"{decimal} metres"]
                explanation = f"Step 1: {decimal} rounded = {rounded}. Step 2: {name} is about {rounded} metres tall. ✓"
                image_svg = None
                
            else:  # estimate
                d1 = round(random.uniform(2.1, 5.9), 1)
                d2 = round(random.uniform(1.1, 4.9), 1)
                estimate = round(d1) + round(d2)
                
                q_text = f"Estimate {d1} + {d2} by rounding to whole numbers first."
                correct = str(estimate)
                actual = round(d1 + d2, 1)
                wrong = [str(estimate + 1), str(estimate - 1), str(actual)]
                explanation = f"Step 1: {d1} ≈ {round(d1)}, {d2} ≈ {round(d2)}. Step 2: {round(d1)} + {round(d2)} = {estimate}. ✓"
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
# LEVEL 7: Adding Decimals (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Adding Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['one_dp', 'two_dp', 'word', 'column'])
            
            if q_type == 'one_dp':
                d1 = round(random.uniform(1.1, 9.9), 1)
                d2 = round(random.uniform(1.1, 9.9), 1)
                answer = round(d1 + d2, 1)
                
                q_text = f"What is {d1} + {d2}?"
                correct = str(answer)
                wrong = [str(round(answer + 0.1, 1)), str(round(answer - 0.1, 1)), str(round(d1 * d2, 1))]
                explanation = f"Step 1: Line up decimal points. Step 2: {d1} + {d2} = {answer}. ✓"
                image_svg = None
                
            elif q_type == 'two_dp':
                d1 = round(random.uniform(1.01, 5.99), 2)
                d2 = round(random.uniform(1.01, 5.99), 2)
                answer = round(d1 + d2, 2)
                
                q_text = f"Calculate: {d1} + {d2}"
                correct = str(answer)
                wrong = [str(round(answer + 0.01, 2)), str(round(answer - 0.01, 2)), str(round(answer + 0.1, 2))]
                explanation = f"Step 1: Line up decimal points. Step 2: Add column by column. Answer: {answer}. ✓"
                image_svg = None
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                d1 = round(random.uniform(1.1, 5.9), 1)
                d2 = round(random.uniform(1.1, 4.9), 1)
                answer = round(d1 + d2, 1)
                
                q_text = f"{name} walked {d1} km in the morning and {d2} km in the afternoon. Total distance?"
                correct = f"{answer} km"
                wrong = [f"{round(answer + 0.5, 1)} km", f"{round(answer - 0.5, 1)} km", f"{d1} km"]
                explanation = f"Step 1: {d1} + {d2} = {answer} km. ✓"
                image_svg = None
                
            else:  # column
                d1 = round(random.uniform(10.1, 30.9), 1)
                d2 = round(random.uniform(5.1, 20.9), 1)
                answer = round(d1 + d2, 1)
                
                q_text = f"Use column addition: {d1} + {d2}"
                correct = str(answer)
                wrong = [str(round(answer + 1, 1)), str(round(answer - 1, 1)), str(int(d1) + int(d2))]
                explanation = f"Step 1: Line up decimal points. Step 2: Add each column. Answer: {answer}. ✓"
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
# LEVEL 8: Subtracting Decimals (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Subtracting Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['one_dp', 'two_dp', 'word', 'column'])
            
            if q_type == 'one_dp':
                d1 = round(random.uniform(5.1, 15.9), 1)
                d2 = round(random.uniform(1.1, d1 - 0.5), 1)
                answer = round(d1 - d2, 1)
                
                q_text = f"What is {d1} - {d2}?"
                correct = str(answer)
                wrong = [str(round(answer + 0.1, 1)), str(round(answer - 0.1, 1)), str(round(d1 + d2, 1))]
                explanation = f"Step 1: Line up decimal points. Step 2: {d1} - {d2} = {answer}. ✓"
                image_svg = None
                
            elif q_type == 'two_dp':
                d1 = round(random.uniform(5.01, 10.99), 2)
                d2 = round(random.uniform(1.01, d1 - 0.5), 2)
                answer = round(d1 - d2, 2)
                
                q_text = f"Calculate: {d1} - {d2}"
                correct = str(answer)
                wrong = [str(round(answer + 0.01, 2)), str(round(answer - 0.01, 2)), str(round(answer + 0.1, 2))]
                explanation = f"Step 1: Line up decimal points. Step 2: Subtract column by column. Answer: {answer}. ✓"
                image_svg = None
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                d1 = round(random.uniform(8.1, 15.9), 1)
                d2 = round(random.uniform(2.1, d1 - 1), 1)
                answer = round(d1 - d2, 1)
                
                q_text = f"{name} had €{d1}. They spent €{d2}. How much left?"
                correct = f"€{answer}"
                wrong = [f"€{round(answer + 0.5, 1)}", f"€{round(answer - 0.5, 1)}", f"€{round(d1 + d2, 1)}"]
                explanation = f"Step 1: €{d1} - €{d2} = €{answer}. ✓"
                image_svg = None
                
            else:  # column
                d1 = round(random.uniform(20.1, 50.9), 1)
                d2 = round(random.uniform(5.1, 20.9), 1)
                answer = round(d1 - d2, 1)
                
                q_text = f"Use column subtraction: {d1} - {d2}"
                correct = str(answer)
                wrong = [str(round(answer + 1, 1)), str(round(answer - 1, 1)), str(int(d1) - int(d2))]
                explanation = f"Step 1: Line up decimal points. Step 2: Subtract each column. Answer: {answer}. ✓"
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
# LEVEL 9: Decimal Word Problems (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Decimal Word Problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            problem_type = random.randint(1, 4)
            name = random.choice(IRISH_NAMES)
            
            if problem_type == 1:
                # Shopping
                item1 = round(random.uniform(2.5, 8.99), 2)
                item2 = round(random.uniform(1.5, 5.99), 2)
                total = round(item1 + item2, 2)
                
                q_text = f"{name} bought items for €{item1} and €{item2}. What was the total cost?"
                correct = f"€{total}"
                wrong = [f"€{round(total + 0.5, 2)}", f"€{round(total - 0.5, 2)}", f"€{item1}"]
                explanation = f"Step 1: €{item1} + €{item2} = €{total}. ✓"
                
            elif problem_type == 2:
                # Change
                paid = random.choice([10.00, 20.00, 50.00])
                cost = round(random.uniform(3.5, paid - 2), 2)
                change = round(paid - cost, 2)
                
                q_text = f"{name} paid €{paid} for an item costing €{cost}. What change?"
                correct = f"€{change}"
                wrong = [f"€{round(change + 1, 2)}", f"€{round(change - 1, 2)}", f"€{cost}"]
                explanation = f"Step 1: €{paid} - €{cost} = €{change}. ✓"
                
            elif problem_type == 3:
                # Measurement
                length1 = round(random.uniform(2.1, 5.9), 1)
                length2 = round(random.uniform(1.5, 4.5), 1)
                total = round(length1 + length2, 1)
                
                q_text = f"Two pieces of ribbon are {length1} m and {length2} m long. What is the total length?"
                correct = f"{total} m"
                wrong = [f"{round(total + 0.5, 1)} m", f"{round(total - 0.5, 1)} m", f"{length1} m"]
                explanation = f"Step 1: {length1} + {length2} = {total} m. ✓"
                
            else:
                # Comparison
                weight1 = round(random.uniform(2.5, 6.9), 1)
                weight2 = round(random.uniform(1.5, 5.9), 1)
                diff = round(abs(weight1 - weight2), 1)
                
                q_text = f"One bag weighs {weight1} kg, another weighs {weight2} kg. What is the difference?"
                correct = f"{diff} kg"
                wrong = [f"{round(diff + 0.5, 1)} kg", f"{round(weight1 + weight2, 1)} kg", f"{weight1} kg"]
                explanation = f"Step 1: {max(weight1, weight2)} - {min(weight1, weight2)} = {diff} kg. ✓"
            
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
                'difficulty': 9,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Multiplying Decimals (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Multiplying Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['by_10', 'by_100', 'by_whole', 'word'])
            
            if q_type == 'by_10':
                decimal = round(random.uniform(0.1, 9.9), 1)
                answer = round(decimal * 10, 0)
                
                q_text = f"What is {decimal} × 10?"
                correct = str(int(answer))
                wrong = [str(int(answer) + 1), str(int(answer) - 1), str(decimal)]
                explanation = f"Step 1: Move decimal point 1 place right. Step 2: {decimal} × 10 = {int(answer)}. ✓"
                image_svg = None
                
            elif q_type == 'by_100':
                decimal = round(random.uniform(0.01, 0.99), 2)
                answer = round(decimal * 100, 0)
                
                q_text = f"What is {decimal} × 100?"
                correct = str(int(answer))
                wrong = [str(int(answer) + 10), str(int(answer) - 10), str(decimal * 10)]
                explanation = f"Step 1: Move decimal point 2 places right. Step 2: {decimal} × 100 = {int(answer)}. ✓"
                image_svg = None
                
            elif q_type == 'by_whole':
                decimal = round(random.uniform(0.5, 3.5), 1)
                whole = random.randint(2, 5)
                answer = round(decimal * whole, 1)
                
                q_text = f"What is {decimal} × {whole}?"
                correct = str(answer)
                wrong = [str(round(answer + 0.5, 1)), str(round(answer - 0.5, 1)), str(decimal + whole)]
                explanation = f"Step 1: {decimal} × {whole} = {answer}. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                price = round(random.uniform(1.5, 4.5), 2)
                qty = random.randint(3, 6)
                total = round(price * qty, 2)
                
                q_text = f"Apples cost €{price} each. {name} buys {qty}. Total cost?"
                correct = f"€{total}"
                wrong = [f"€{round(total + 1, 2)}", f"€{round(total - 1, 2)}", f"€{price}"]
                explanation = f"Step 1: €{price} × {qty} = €{total}. ✓"
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
# LEVEL 11: Dividing Decimals (Advanced)
# ============================================================

def generate_level_11():
    """Level 11: Dividing Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['by_10', 'by_100', 'by_whole', 'word'])
            
            if q_type == 'by_10':
                whole = random.randint(10, 100)
                answer = whole / 10
                
                q_text = f"What is {whole} ÷ 10?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer * 10), str(whole)]
                explanation = f"Step 1: Move decimal point 1 place left. Step 2: {whole} ÷ 10 = {answer}. ✓"
                image_svg = None
                
            elif q_type == 'by_100':
                whole = random.randint(100, 500)
                answer = whole / 100
                
                q_text = f"What is {whole} ÷ 100?"
                correct = str(answer)
                wrong = [str(answer + 0.1), str(answer * 10), str(whole / 10)]
                explanation = f"Step 1: Move decimal point 2 places left. Step 2: {whole} ÷ 100 = {answer}. ✓"
                image_svg = None
                
            elif q_type == 'by_whole':
                divisor = random.randint(2, 5)
                quotient = round(random.uniform(1.5, 5.5), 1)
                dividend = round(quotient * divisor, 1)
                
                q_text = f"What is {dividend} ÷ {divisor}?"
                correct = str(quotient)
                wrong = [str(round(quotient + 0.5, 1)), str(round(quotient - 0.5, 1)), str(dividend)]
                explanation = f"Step 1: {dividend} ÷ {divisor} = {quotient}. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                total = round(random.uniform(10, 25), 2)
                people = random.randint(2, 4)
                # Make it divide evenly
                total = round(people * round(total / people, 2), 2)
                each = round(total / people, 2)
                
                q_text = f"€{total} is shared equally between {people} people. How much each?"
                correct = f"€{each}"
                wrong = [f"€{round(each + 1, 2)}", f"€{round(each - 1, 2)}", f"€{total}"]
                explanation = f"Step 1: €{total} ÷ {people} = €{each}. ✓"
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
    """Level 12: Mastery Challenge"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    generators = [generate_level_9, generate_level_10, generate_level_11]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            gen = random.choice(generators)
            source_questions = gen()
            
            if source_questions:
                q = random.choice(source_questions)
                q_text = q['question_text']
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                q['difficulty'] = 12
                q['difficulty_band'] = 'advanced'
                questions.append(q)
                
        except Exception as e:
            continue
    
    return questions

# ============================================================
# VALIDATION & DATABASE
# ============================================================

def validate_questions(questions):
    errors = []
    level_counts = {}
    
    for i, q in enumerate(questions):
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if q['mode'] != 'numeracy':
            errors.append(f"Level {level} Q{i}: Wrong mode")
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level} Q{i}: Duplicate options")
    
    print("\n" + "="*60)
    print("VALIDATION - Basic Decimals")
    print("="*60)
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} {status}")
    
    print("="*60)
    print(f"Total: {len(questions)} | Errors: {len(errors)}")
    
    return len(errors)

def insert_questions(questions):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    print(f"Deleted {cursor.rowcount} existing questions")
    
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
                q['mode'], q['explanation'], q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            print(f"Insert error: {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {inserted} questions")

def main():
    print("="*60)
    print("AgentMath - Basic Decimals Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Understanding Decimals", generate_level_1),
        (2, "Decimal Place Value", generate_level_2),
        (3, "Decimals and Fractions", generate_level_3),
        (4, "Comparing Decimals", generate_level_4),
        (5, "Ordering Decimals", generate_level_5),
        (6, "Rounding Decimals", generate_level_6),
        (7, "Adding Decimals", generate_level_7),
        (8, "Subtracting Decimals", generate_level_8),
        (9, "Word Problems", generate_level_9),
        (10, "Multiplying Decimals", generate_level_10),
        (11, "Dividing Decimals", generate_level_11),
        (12, "Mastery Challenge", generate_level_12),
    ]
    
    for level, name, gen_func in generators:
        print(f"Generating Level {level}: {name}...")
        questions = gen_func()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    validate_questions(all_questions)
    
    response = input("\nInsert into database? (y/n): ").strip().lower()
    if response == 'y':
        insert_questions(all_questions)
        print("\n✓ Done!")

if __name__ == "__main__":
    main()
