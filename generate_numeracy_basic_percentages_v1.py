#!/usr/bin/env python3
"""
AgentMath - Basic Percentages Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Understanding percentages, common percentages, visual
  L4-6:   Developing - Percentage of amounts, converting fractions/decimals
  L7-9:   Proficient - Percentage increase/decrease, word problems
  L10-12: Advanced - Multi-step problems, comparisons, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'basic_percentages'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam'
]

# Common percentages and their equivalents
COMMON_PERCENTAGES = {
    50: (1, 2, 0.5, "half"),
    25: (1, 4, 0.25, "quarter"),
    75: (3, 4, 0.75, "three quarters"),
    10: (1, 10, 0.1, "one tenth"),
    20: (1, 5, 0.2, "one fifth"),
    100: (1, 1, 1.0, "one whole"),
    1: (1, 100, 0.01, "one hundredth"),
}

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

def generate_percentage_bar_svg(percentage):
    """Generate SVG showing percentage as a bar"""
    svg = f'''<svg viewBox="0 0 220 50" xmlns="http://www.w3.org/2000/svg">
    <style>
        .bg {{ fill: #f3f4f6; stroke: #d1d5db; }}
        .filled {{ fill: #10b981; }}
        .label {{ font-size: 14px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
    </style>
    <rect x="10" y="10" width="200" height="25" class="bg" rx="4"/>
    <rect x="10" y="10" width="{percentage * 2}" height="25" class="filled" rx="4"/>
    <text x="110" y="50" class="label">{percentage}%</text>
    </svg>'''
    return svg

def generate_pie_percentage_svg(percentage):
    """Generate SVG showing percentage as pie chart"""
    import math
    
    angle = (percentage / 100) * 360
    rad = math.radians(angle - 90)
    
    cx, cy, r = 50, 50, 40
    x = cx + r * math.cos(rad)
    y = cy + r * math.sin(rad)
    
    large_arc = 1 if percentage > 50 else 0
    
    svg = f'''<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
    <style>
        .bg {{ fill: #f3f4f6; stroke: #d1d5db; }}
        .filled {{ fill: #10b981; stroke: #059669; }}
        .label {{ font-size: 12px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
    </style>
    <circle cx="{cx}" cy="{cy}" r="{r}" class="bg"/>'''
    
    if percentage == 100:
        svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="filled"/>'
    elif percentage > 0:
        svg += f'<path d="M{cx},{cy} L{cx},{cy - r} A{r},{r} 0 {large_arc},1 {x},{y} Z" class="filled"/>'
    
    svg += f'<text x="60" y="110" class="label">{percentage}%</text>'
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Understanding Percentages (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Understanding Percentages - What is a percentage?"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['meaning', 'symbol', 'read', 'identify', 'hundred', 'write'])
            
            if q_type == 'meaning':
                variant = random.randint(1, 3)
                if variant == 1:
                    q_text = "What does 'percent' mean?"
                    correct = "Out of 100"
                    wrong = ["Out of 10", "Out of 1000", "More than 100"]
                elif variant == 2:
                    q_text = "The word 'percent' comes from 'per centum'. What does this mean?"
                    correct = "Per hundred"
                    wrong = ["Per ten", "Per thousand", "Per one"]
                else:
                    q_text = "If something is 100%, how much is that?"
                    correct = "All of it"
                    wrong = ["Half of it", "None of it", "Double"]
                explanation = "Step 1: 'Per' means 'for each' and 'cent' means '100'. Step 2: Percent means 'out of 100'. ✓"
                image_svg = None
                
            elif q_type == 'symbol':
                variant = random.randint(1, 3)
                if variant == 1:
                    q_text = "What symbol is used to show percentage?"
                    correct = "%"
                    wrong = ["&", "#", "@"]
                elif variant == 2:
                    q_text = "Which symbol means 'percent'?"
                    correct = "%"
                    wrong = ["$", "£", "€"]
                else:
                    num = random.choice([25, 50, 75])
                    q_text = f"How do you write {num} percent using a symbol?"
                    correct = f"{num}%"
                    wrong = [f"${num}", f"{num}p", f"#{num}"]
                explanation = "Step 1: The % symbol means 'percent'. Step 2: 50% means '50 out of 100'. ✓"
                image_svg = None
                
            elif q_type == 'read':
                pct = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 100])
                
                q_text = f"How do you read {pct}%?"
                correct = f"{pct} percent"
                wrong = [f"{pct} per", f"{pct} cents", f"{pct} hundreds"]
                explanation = f"Step 1: {pct}% is read as '{pct} percent'. ✓"
                image_svg = generate_percentage_bar_svg(pct) if pct <= 100 else None
                
            elif q_type == 'identify':
                pct = random.choice([10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90])
                
                q_text = f"What percentage is shaded in the picture?"
                correct = f"{pct}%"
                wrong = [f"{100 - pct}%", f"{pct + 10}%" if pct < 90 else "5%", f"{pct - 10}%" if pct > 10 else "5%"]
                explanation = f"Step 1: Count shaded parts. Step 2: {pct}% is shaded. ✓"
                image_svg = generate_percentage_bar_svg(pct)
                
            elif q_type == 'hundred':
                num = random.randint(1, 99)
                q_text = f"What does {num}% mean?"
                correct = f"{num} out of 100"
                wrong = [f"{num} out of 10", f"{num} out of 1000", f"100 out of {num}"]
                explanation = f"Step 1: {num}% means {num} out of every 100. ✓"
                image_svg = None
                
            else:  # write
                num = random.choice([10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90])
                q_text = f"Write '{num} out of 100' as a percentage."
                correct = f"{num}%"
                wrong = [f"{100-num}%", f"{num}", f"100%"]
                explanation = f"Step 1: {num} out of 100 = {num}%. ✓"
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
# LEVEL 2: Common Percentages (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Common Percentages - 50%, 25%, 10%, 100%"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['match_frac', 'match_word', 'visual', 'simple_calc', 'reverse', 'compare'])
            
            if q_type == 'match_frac':
                pct = random.choice([50, 25, 75, 10, 20])
                num, den, dec, word = COMMON_PERCENTAGES.get(pct, (pct, 100, pct/100, f"{pct} percent"))
                
                q_text = f"What fraction equals {pct}%?"
                correct = f"{num}/{den}"
                wrong_fracs = ["1/3", "2/3", "1/8", "3/8", "2/5", "4/5"]
                wrong = [f for f in wrong_fracs if f != f"{num}/{den}"][:3]
                explanation = f"Step 1: {pct}% = {pct}/100 = {num}/{den}. ✓"
                image_svg = generate_pie_percentage_svg(pct)
                
            elif q_type == 'match_word':
                pct = random.choice([50, 25, 100, 10])
                num, den, dec, word = COMMON_PERCENTAGES.get(pct, (1, 1, 1, "one"))
                
                q_text = f"What is another way to say {pct}%?"
                correct = word.title()
                wrong = ["One third", "Two thirds", "One eighth", "Three fifths"]
                wrong = [w for w in wrong if w.lower() != word][:3]
                explanation = f"Step 1: {pct}% = {word}. ✓"
                image_svg = None
                
            elif q_type == 'visual':
                pct = random.choice([10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 100])
                
                q_text = f"The picture shows what percentage shaded?"
                correct = f"{pct}%"
                wrong = [f"{100 - pct}%", f"{pct + 25}%" if pct < 75 else "5%", f"{pct - 10}%" if pct > 10 else "5%"]
                explanation = f"Step 1: Count filled portion. Step 2: {pct}% is shaded. ✓"
                image_svg = generate_percentage_bar_svg(pct)
                
            elif q_type == 'simple_calc':
                pct = random.choice([50, 10, 100, 25])
                whole = random.choice([10, 20, 40, 50, 80, 100, 200])
                answer = (whole * pct) // 100
                
                q_text = f"What is {pct}% of {whole}?"
                correct = str(answer)
                wrong = [str(answer + 5), str(whole), str(answer - 5) if answer > 5 else str(answer + 10)]
                explanation = f"Step 1: {pct}% of {whole} = {answer}. ✓"
                image_svg = None
                
            elif q_type == 'reverse':
                pct = random.choice([50, 25, 10])
                answer = random.choice([5, 10, 20, 25])
                whole = (answer * 100) // pct
                
                q_text = f"If {pct}% of a number is {answer}, what is 100% of it?"
                correct = str(whole)
                wrong = [str(answer), str(whole + 10), str(answer * 2)]
                explanation = f"Step 1: {pct}% = {answer}, so 100% = {whole}. ✓"
                image_svg = None
                
            else:  # compare
                pct = random.choice([25, 50, 75])
                q_text = f"Which is bigger: {pct}% or {100 - pct}%?"
                if pct > 50:
                    correct = f"{pct}%"
                elif pct < 50:
                    correct = f"{100 - pct}%"
                else:
                    correct = "They are equal"
                wrong = [f"{pct}%" if pct <= 50 else f"{100-pct}%", "Cannot tell", "Neither"]
                explanation = f"Step 1: Compare {pct}% and {100-pct}%. ✓"
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
# LEVEL 3: Visual Percentages (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Visual Percentages - Reading from diagrams"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['bar', 'pie', 'grid', 'shade', 'parts', 'remaining'])
            
            if q_type == 'bar':
                pct = random.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])
                
                q_text = f"What percentage of the bar is shaded?"
                correct = f"{pct}%"
                wrong = [f"{100 - pct}%", f"{pct + 10}%" if pct < 90 else "5%", f"{pct - 10}%" if pct > 10 else "5%"]
                explanation = f"Step 1: The shaded part is {pct}% of the bar. ✓"
                image_svg = generate_percentage_bar_svg(pct)
                
            elif q_type == 'pie':
                pct = random.choice([25, 50, 75])
                
                q_text = f"What percentage of the circle is shaded?"
                correct = f"{pct}%"
                wrong = [f"{100 - pct}%", f"{pct + 25}%" if pct < 75 else "10%", "33%"]
                explanation = f"Step 1: The shaded part is {pct}% of the circle. ✓"
                image_svg = generate_pie_percentage_svg(pct)
                
            elif q_type == 'grid':
                shaded = random.choice([1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 90, 99])
                
                q_text = f"In a 100-square grid, {shaded} squares are coloured. What percentage is that?"
                correct = f"{shaded}%"
                wrong = [f"{100 - shaded}%", f"{shaded + 10}%" if shaded < 90 else "5%", f"{shaded - 5}%" if shaded > 5 else "3%"]
                explanation = f"Step 1: {shaded} out of 100 = {shaded}%. ✓"
                image_svg = None
                
            elif q_type == 'shade':
                pct = random.choice([10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90])
                remaining = 100 - pct
                
                q_text = f"If {pct}% is shaded, what percentage is NOT shaded?"
                correct = f"{remaining}%"
                wrong = [f"{pct}%", f"{remaining + 10}%" if remaining < 90 else "5%", f"{remaining - 10}%" if remaining > 10 else "5%"]
                explanation = f"Step 1: 100% - {pct}% = {remaining}%. ✓"
                image_svg = generate_percentage_bar_svg(pct)
                
            elif q_type == 'parts':
                total = random.choice([10, 20, 25, 50])
                parts = random.randint(1, total - 1)
                pct = (parts * 100) // total
                
                q_text = f"A shape is divided into {total} equal parts. {parts} parts are coloured. What percentage is coloured?"
                correct = f"{pct}%"
                wrong = [f"{100 - pct}%", f"{parts}%", f"{total}%"]
                explanation = f"Step 1: {parts} out of {total} = {pct}%. ✓"
                image_svg = None
                
            else:  # remaining
                pct = random.choice([10, 20, 25, 30, 40, 50, 60, 70, 75, 80])
                remaining = 100 - pct
                
                q_text = f"A jar is {pct}% full. What percentage is empty?"
                correct = f"{remaining}%"
                wrong = [f"{pct}%", f"{remaining + 5}%", "50%"]
                explanation = f"Step 1: 100% - {pct}% = {remaining}% empty. ✓"
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
# LEVEL 4: Percentage of Amounts (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Percentage of Amounts - 10%, 25%, 50%"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            pct = random.choice([10, 25, 50])
            
            if pct == 10:
                whole = random.choice([20, 30, 40, 50, 60, 80, 100, 200])
                method = "divide by 10"
            elif pct == 25:
                whole = random.choice([20, 40, 80, 100, 200, 400])
                method = "divide by 4"
            else:  # 50
                whole = random.choice([20, 30, 40, 50, 60, 80, 100, 200])
                method = "divide by 2 (halve)"
            
            answer = (whole * pct) // 100
            
            q_type = random.choice(['basic', 'word', 'method'])
            
            if q_type == 'basic':
                q_text = f"What is {pct}% of {whole}?"
                correct = str(answer)
                wrong = [str(answer + 5), str(whole), str(answer * 2)]
                explanation = f"Step 1: {pct}% of {whole} = {method} = {answer}. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                
                if pct == 50:
                    q_text = f"{name} saves 50% of their €{whole} pocket money. How much saved?"
                elif pct == 10:
                    q_text = f"A shop gives 10% off. An item costs €{whole}. How much is the discount?"
                else:
                    q_text = f"{name} spent 25% of €{whole}. How much was spent?"
                
                correct = f"€{answer}"
                wrong = [f"€{answer + 5}", f"€{whole}", f"€{answer * 2}"]
                explanation = f"Step 1: {pct}% of €{whole} = €{answer}. ✓"
                
            else:  # method
                q_text = f"To find {pct}% of a number, what do you do?"
                correct = f"Divide by {100 // pct}"
                wrong = ["Multiply by 2", "Add 10", "Subtract 25"]
                explanation = f"Step 1: {pct}% = {pct}/100 = 1/{100 // pct}. Step 2: So {method}. ✓"
            
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
                'difficulty': 4,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Converting Percentages (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Converting between Percentages, Fractions, Decimals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    conversions = [
        (50, "1/2", "0.5"), (25, "1/4", "0.25"), (75, "3/4", "0.75"),
        (10, "1/10", "0.1"), (20, "1/5", "0.2"), (40, "2/5", "0.4"),
        (60, "3/5", "0.6"), (80, "4/5", "0.8"), (100, "1/1", "1.0"),
        (5, "1/20", "0.05"), (30, "3/10", "0.3"), (70, "7/10", "0.7"),
        (90, "9/10", "0.9"), (33, "1/3", "0.33"), (66, "2/3", "0.66"),
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            pct, frac, dec = random.choice(conversions)
            q_type = random.choice(['pct_to_frac', 'pct_to_dec', 'frac_to_pct', 'dec_to_pct', 'match', 'compare'])
            
            if q_type == 'pct_to_frac':
                q_text = f"Write {pct}% as a fraction."
                correct = frac
                wrong = ["2/3", "1/3", "3/5", "2/5"]
                wrong = [w for w in wrong if w != frac][:3]
                explanation = f"Step 1: {pct}% = {pct}/100 = {frac}. ✓"
                
            elif q_type == 'pct_to_dec':
                q_text = f"Write {pct}% as a decimal."
                correct = dec
                wrong = [str(round(float(dec) + 0.1, 2)), str(round(float(dec) - 0.1, 2)) if float(dec) > 0.1 else "0.05", str(pct)]
                explanation = f"Step 1: {pct}% ÷ 100 = {dec}. ✓"
                
            elif q_type == 'frac_to_pct':
                q_text = f"Write {frac} as a percentage."
                correct = f"{pct}%"
                wrong = [f"{pct + 10}%", f"{pct - 10}%" if pct > 10 else "5%", f"{100 - pct}%"]
                explanation = f"Step 1: {frac} = {pct}/100 = {pct}%. ✓"
                
            elif q_type == 'dec_to_pct':
                q_text = f"Write {dec} as a percentage."
                correct = f"{pct}%"
                wrong = [f"{pct + 10}%", f"{pct - 10}%" if pct > 10 else "5%", f"{int(float(dec) * 10)}%"]
                explanation = f"Step 1: {dec} × 100 = {pct}%. ✓"
                
            elif q_type == 'match':
                q_text = f"Which equals {pct}%?"
                correct = f"{frac} or {dec}"
                wrong = ["1/3 or 0.33", "2/3 or 0.67", "1/8 or 0.125"]
                wrong = [w for w in wrong if frac not in w][:3]
                explanation = f"Step 1: {pct}% = {frac} = {dec}. ✓"
                
            else:  # compare
                pct2 = random.choice([p for p, f, d in conversions if p != pct])
                q_text = f"Which is larger: {pct}% or {pct2}%?"
                if pct > pct2:
                    correct = f"{pct}%"
                else:
                    correct = f"{pct2}%"
                wrong = [f"{pct}%" if pct < pct2 else f"{pct2}%", "They are equal", "Cannot tell"]
                explanation = f"Step 1: {max(pct, pct2)}% > {min(pct, pct2)}%. ✓"
            
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
                'difficulty': 5,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: More Percentage Calculations (Developing)
# ============================================================

def generate_level_6():
    """Level 6: More Percentage Calculations - 5%, 15%, 20%, 30%"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            pct = random.choice([5, 15, 20, 30])
            
            # Choose a whole that divides nicely
            if pct == 5:
                whole = random.choice([20, 40, 60, 100, 200])
            elif pct == 15:
                whole = random.choice([20, 40, 60, 100, 200])
            elif pct == 20:
                whole = random.choice([25, 50, 100, 200])
            else:  # 30
                whole = random.choice([10, 50, 100, 200])
            
            answer = (whole * pct) // 100
            
            q_type = random.choice(['basic', 'word', 'two_step'])
            
            if q_type == 'basic':
                q_text = f"What is {pct}% of {whole}?"
                correct = str(answer)
                wrong = [str(answer + 5), str(whole), str(answer - 5) if answer > 5 else str(answer + 10)]
                explanation = f"Step 1: {pct}% of {whole} = {answer}. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                
                if pct <= 15:
                    q_text = f"A test has {whole} questions. {name} got {pct}% wrong. How many wrong?"
                else:
                    q_text = f"{name} scored {pct}% in a test of {whole} marks. How many marks?"
                
                correct = str(answer)
                wrong = [str(answer + 5), str(whole), str(whole - answer)]
                explanation = f"Step 1: {pct}% of {whole} = {answer}. ✓"
                
            else:  # two_step
                ten_pct = whole // 10
                
                if pct == 5:
                    q_text = f"Find 5% of {whole}. (Hint: Find 10% first, then halve it)"
                    explanation = f"Step 1: 10% of {whole} = {ten_pct}. Step 2: 5% = {ten_pct} ÷ 2 = {answer}. ✓"
                elif pct == 15:
                    q_text = f"Find 15% of {whole}. (Hint: 10% + 5%)"
                    five_pct = ten_pct // 2
                    explanation = f"Step 1: 10% = {ten_pct}. 5% = {five_pct}. Step 2: 15% = {ten_pct + five_pct}. ✓"
                elif pct == 20:
                    q_text = f"Find 20% of {whole}. (Hint: 10% × 2)"
                    explanation = f"Step 1: 10% of {whole} = {ten_pct}. Step 2: 20% = {ten_pct} × 2 = {answer}. ✓"
                else:
                    q_text = f"Find 30% of {whole}. (Hint: 10% × 3)"
                    explanation = f"Step 1: 10% of {whole} = {ten_pct}. Step 2: 30% = {ten_pct} × 3 = {answer}. ✓"
                
                correct = str(answer)
                wrong = [str(answer + 5), str(ten_pct), str(answer * 2)]
            
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
                'difficulty': 6,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Percentage Increase (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Percentage Increase"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            pct = random.choice([10, 20, 25, 50])
            original = random.choice([50, 100, 200, 400])
            
            increase = (original * pct) // 100
            new_value = original + increase
            
            q_type = random.choice(['find_new', 'find_increase', 'word'])
            
            if q_type == 'find_new':
                q_text = f"Increase {original} by {pct}%. What is the new value?"
                correct = str(new_value)
                wrong = [str(increase), str(original), str(new_value + 10)]
                explanation = f"Step 1: {pct}% of {original} = {increase}. Step 2: {original} + {increase} = {new_value}. ✓"
                
            elif q_type == 'find_increase':
                q_text = f"A price of €{original} increases by {pct}%. How much is the increase?"
                correct = f"€{increase}"
                wrong = [f"€{new_value}", f"€{original}", f"€{increase + 10}"]
                explanation = f"Step 1: {pct}% of €{original} = €{increase}. ✓"
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                
                q_text = f"{name}'s pocket money of €{original} increases by {pct}%. What is the new amount?"
                correct = f"€{new_value}"
                wrong = [f"€{increase}", f"€{original}", f"€{new_value + 20}"]
                explanation = f"Step 1: Increase = {pct}% of €{original} = €{increase}. Step 2: New amount = €{original} + €{increase} = €{new_value}. ✓"
            
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
                'difficulty': 7,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Percentage Decrease (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Percentage Decrease / Discounts"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            pct = random.choice([5, 10, 15, 20, 25, 30, 40, 50])
            original = random.choice([40, 50, 60, 80, 100, 120, 150, 200, 250, 300, 400, 500])
            
            decrease = (original * pct) // 100
            new_value = original - decrease
            
            q_type = random.choice(['find_new', 'find_discount', 'word', 'sale', 'compare'])
            
            if q_type == 'find_new':
                q_text = f"Decrease {original} by {pct}%. What is the new value?"
                correct = str(new_value)
                wrong = [str(decrease), str(original), str(new_value - 10) if new_value > 10 else str(new_value + 10)]
                explanation = f"Step 1: {pct}% of {original} = {decrease}. Step 2: {original} - {decrease} = {new_value}. ✓"
                
            elif q_type == 'find_discount':
                q_text = f"A {pct}% discount on €{original}. How much do you save?"
                correct = f"€{decrease}"
                wrong = [f"€{new_value}", f"€{original}", f"€{decrease + 10}"]
                explanation = f"Step 1: {pct}% of €{original} = €{decrease} saved. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                item = random.choice(['jacket', 'bike', 'game', 'book', 'shoes'])
                
                q_text = f"A {item} costs €{original}. There's a {pct}% sale. What's the sale price?"
                correct = f"€{new_value}"
                wrong = [f"€{decrease}", f"€{original}", f"€{new_value + 20}"]
                explanation = f"Step 1: Discount = {pct}% of €{original} = €{decrease}. Step 2: Sale price = €{original} - €{decrease} = €{new_value}. ✓"
                
            elif q_type == 'sale':
                q_text = f"In a {pct}% off sale, an item marked €{original} will cost how much?"
                correct = f"€{new_value}"
                wrong = [f"€{decrease}", f"€{original}", f"€{original + decrease}"]
                explanation = f"Step 1: {pct}% off €{original} = €{decrease} discount. Step 2: Pay €{new_value}. ✓"
                
            else:  # compare
                original2 = random.choice([o for o in [50, 100, 150, 200] if o != original])
                pct2 = random.choice([p for p in [10, 20, 25, 30] if p != pct])
                new2 = original2 - (original2 * pct2) // 100
                
                q_text = f"Which is cheaper: €{original} with {pct}% off, or €{original2} with {pct2}% off?"
                if new_value < new2:
                    correct = f"€{original} with {pct}% off"
                elif new2 < new_value:
                    correct = f"€{original2} with {pct2}% off"
                else:
                    correct = "Same price"
                wrong = [f"€{original} with {pct}% off" if new_value >= new2 else f"€{original2} with {pct2}% off", "Cannot tell", f"€{min(original, original2)}"]
                explanation = f"Step 1: First = €{new_value}. Second = €{new2}. ✓"
            
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
                'difficulty': 8,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Percentage Word Problems (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Percentage Word Problems"""
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
                # Score as percentage
                correct_ans = random.choice([15, 18, 20, 24])
                total = random.choice([20, 25, 30, 40])
                while correct_ans > total:
                    correct_ans = random.choice([15, 18, 20, 24])
                
                pct = (correct_ans * 100) // total
                
                q_text = f"{name} got {correct_ans} out of {total} in a test. What percentage?"
                correct = f"{pct}%"
                wrong = [f"{100 - pct}%", f"{correct_ans}%", f"{total}%"]
                explanation = f"Step 1: {correct_ans}/{total} × 100 = {pct}%. ✓"
                
            elif problem_type == 2:
                # Finding the whole
                pct = random.choice([10, 25, 50])
                part = random.choice([5, 10, 20, 25])
                whole = (part * 100) // pct
                
                q_text = f"{pct}% of a number is {part}. What is the number?"
                correct = str(whole)
                wrong = [str(part), str(whole + 10), str(whole - 10)]
                explanation = f"Step 1: If {pct}% = {part}, then 100% = {part} × {100 // pct} = {whole}. ✓"
                
            elif problem_type == 3:
                # Comparison
                total = random.choice([50, 100, 200])
                pct1 = random.choice([20, 30, 40])
                pct2 = random.choice([25, 35, 45])
                
                val1 = (total * pct1) // 100
                val2 = (total * pct2) // 100
                diff = abs(val1 - val2)
                
                q_text = f"What is the difference between {pct1}% of {total} and {pct2}% of {total}?"
                correct = str(diff)
                wrong = [str(val1), str(val2), str(diff + 5)]
                explanation = f"Step 1: {pct1}% of {total} = {val1}. {pct2}% of {total} = {val2}. Step 2: Difference = {diff}. ✓"
                
            else:
                # Survey/data
                total_students = random.choice([20, 25, 40, 50])
                pct = random.choice([20, 25, 40, 50])
                number = (total_students * pct) // 100
                
                q_text = f"In a class of {total_students}, {pct}% like football. How many like football?"
                correct = str(number)
                wrong = [str(number + 2), str(total_students), str(100 - pct)]
                explanation = f"Step 1: {pct}% of {total_students} = {number} students. ✓"
            
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
# LEVEL 10: Multi-Step Percentage Problems (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Multi-Step Percentage Problems"""
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
                # Successive percentages
                original = random.choice([100, 200, 400])
                pct1 = 10
                pct2 = 10
                
                after_first = original + (original * pct1) // 100
                after_second = after_first + (after_first * pct2) // 100
                
                q_text = f"€{original} increases by {pct1}%, then by {pct2}% again. Final amount?"
                correct = f"€{after_second}"
                wrong = [f"€{original + 2 * (original * pct1) // 100}", f"€{after_first}", f"€{original}"]
                explanation = f"Step 1: After {pct1}%: €{after_first}. Step 2: After another {pct2}%: €{after_second}. ✓"
                
            elif problem_type == 2:
                # Combined purchase with discount
                item1 = random.choice([40, 50, 80, 100])
                item2 = random.choice([20, 30, 40, 50])
                discount_pct = random.choice([10, 20])
                
                total = item1 + item2
                discount = (total * discount_pct) // 100
                final = total - discount
                
                q_text = f"Items cost €{item1} and €{item2}. With {discount_pct}% off the total, how much to pay?"
                correct = f"€{final}"
                wrong = [f"€{total}", f"€{discount}", f"€{final + 10}"]
                explanation = f"Step 1: Total = €{total}. Step 2: {discount_pct}% off = €{discount}. Step 3: Pay €{final}. ✓"
                
            elif problem_type == 3:
                # Remaining after spending
                start = random.choice([100, 200, 400])
                spend_pct = random.choice([25, 40, 50])
                
                spent = (start * spend_pct) // 100
                remaining = start - spent
                
                q_text = f"{name} had €{start}. They spent {spend_pct}%. How much is left?"
                correct = f"€{remaining}"
                wrong = [f"€{spent}", f"€{start}", f"€{remaining + 10}"]
                explanation = f"Step 1: Spent = {spend_pct}% of €{start} = €{spent}. Step 2: Left = €{remaining}. ✓"
                
            else:
                # Finding original after percentage change
                pct = random.choice([10, 20, 25])
                new_val = random.choice([110, 120, 125, 150])
                original = (new_val * 100) // (100 + pct)
                
                q_text = f"After a {pct}% increase, a price is €{new_val}. What was the original price?"
                correct = f"€{original}"
                wrong = [f"€{new_val}", f"€{new_val - (new_val * pct) // 100}", f"€{original + 10}"]
                explanation = f"Step 1: {100 + pct}% = €{new_val}. Step 2: 100% = €{original}. ✓"
            
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
    """Level 11: Complex Percentage Problem Solving"""
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
                # Best deal comparison
                price1 = random.choice([80, 100, 120])
                disc1 = 25
                price2 = random.choice([75, 90, 110])
                disc2 = 20
                
                final1 = price1 - (price1 * disc1) // 100
                final2 = price2 - (price2 * disc2) // 100
                
                better = "Shop A" if final1 < final2 else "Shop B"
                
                q_text = f"Shop A: €{price1} with {disc1}% off. Shop B: €{price2} with {disc2}% off. Which is cheaper?"
                correct = better
                wrong = ["Shop A" if better == "Shop B" else "Shop B", "Same price", "Cannot tell"]
                explanation = f"Step 1: Shop A = €{final1}. Shop B = €{final2}. Step 2: {better} is cheaper. ✓"
                
            elif problem_type == 2:
                # Two percentage operations
                start = random.choice([200, 400, 500])
                decrease_pct = 20
                increase_pct = 25
                
                after_dec = start - (start * decrease_pct) // 100
                after_inc = after_dec + (after_dec * increase_pct) // 100
                
                q_text = f"€{start} decreases by {decrease_pct}%, then increases by {increase_pct}%. Final amount?"
                correct = f"€{after_inc}"
                wrong = [f"€{start}", f"€{after_dec}", f"€{start + (start * 5) // 100}"]
                explanation = f"Step 1: After {decrease_pct}% decrease: €{after_dec}. Step 2: After {increase_pct}% increase: €{after_inc}. ✓"
                
            elif problem_type == 3:
                # Working backwards
                final = random.choice([80, 90, 120])
                pct_paid = random.choice([80, 90])
                original = (final * 100) // pct_paid
                discount_pct = 100 - pct_paid
                
                q_text = f"{name} paid €{final} after a {discount_pct}% discount. What was the original price?"
                correct = f"€{original}"
                wrong = [f"€{final + (final * discount_pct) // 100}", f"€{final}", f"€{original + 10}"]
                explanation = f"Step 1: €{final} is {pct_paid}% of original. Step 2: Original = €{original}. ✓"
                
            else:
                # Comparing percentages of different amounts
                amount1 = random.choice([80, 100, 120])
                pct1 = 25
                amount2 = random.choice([60, 80, 100])
                pct2 = 50
                
                val1 = (amount1 * pct1) // 100
                val2 = (amount2 * pct2) // 100
                diff = abs(val1 - val2)
                bigger = f"{pct1}% of {amount1}" if val1 > val2 else f"{pct2}% of {amount2}"
                
                q_text = f"Which is bigger: {pct1}% of {amount1} or {pct2}% of {amount2}? By how much?"
                if val1 == val2:
                    correct = "Equal"
                else:
                    correct = f"{bigger} by {diff}"
                wrong = [f"{pct1}% of {amount1}" if val1 < val2 else f"{pct2}% of {amount2}", str(diff + 5), str(val1 + val2)]
                explanation = f"Step 1: {pct1}% of {amount1} = {val1}. {pct2}% of {amount2} = {val2}. Step 2: Difference = {diff}. ✓"
            
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
    print("VALIDATION - Basic Percentages")
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
    print("AgentMath - Basic Percentages Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Understanding Percentages", generate_level_1),
        (2, "Common Percentages", generate_level_2),
        (3, "Visual Percentages", generate_level_3),
        (4, "Percentage of Amounts", generate_level_4),
        (5, "Converting Percentages", generate_level_5),
        (6, "More Calculations", generate_level_6),
        (7, "Percentage Increase", generate_level_7),
        (8, "Percentage Decrease", generate_level_8),
        (9, "Word Problems", generate_level_9),
        (10, "Multi-Step Problems", generate_level_10),
        (11, "Problem Solving", generate_level_11),
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
