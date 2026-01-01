#!/usr/bin/env python3
"""
AgentMath - Basic Fractions Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Understanding fractions, halves/quarters, comparing
  L4-6:   Developing - Equivalent fractions, simplifying, mixed numbers
  L7-9:   Proficient - Adding/subtracting fractions, word problems
  L10-12: Advanced - Multiplying fractions, problem solving, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import math

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'basic_fractions'
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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(num, den):
    g = gcd(num, den)
    return num // g, den // g

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

def generate_fraction_circle_svg(numerator, denominator, show_label=True):
    """Generate SVG showing a fraction as a circle divided into parts"""
    svg = f'''<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
    <style>
        .filled {{ fill: #10b981; stroke: #059669; stroke-width: 2; }}
        .empty {{ fill: #f3f4f6; stroke: #d1d5db; stroke-width: 2; }}
        .label {{ font-size: 14px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
    </style>'''
    
    cx, cy, r = 60, 55, 40
    
    for i in range(denominator):
        start_angle = (i * 360 / denominator) - 90
        end_angle = ((i + 1) * 360 / denominator) - 90
        
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        
        large_arc = 1 if (360 / denominator) > 180 else 0
        
        fill_class = 'filled' if i < numerator else 'empty'
        
        if denominator == 1:
            svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{fill_class}"/>'
        else:
            svg += f'<path d="M{cx},{cy} L{x1},{y1} A{r},{r} 0 {large_arc},1 {x2},{y2} Z" class="{fill_class}"/>'
    
    if show_label:
        svg += f'<text x="60" y="115" class="label">{numerator}/{denominator}</text>'
    
    svg += '</svg>'
    return svg

def generate_fraction_bar_svg(numerator, denominator, show_label=True):
    """Generate SVG showing a fraction as a bar divided into parts"""
    svg = f'''<svg viewBox="0 0 200 60" xmlns="http://www.w3.org/2000/svg">
    <style>
        .filled {{ fill: #10b981; stroke: #059669; stroke-width: 1; }}
        .empty {{ fill: #f3f4f6; stroke: #d1d5db; stroke-width: 1; }}
        .label {{ font-size: 12px; fill: #1f2937; text-anchor: middle; }}
    </style>'''
    
    bar_width = 180
    bar_height = 30
    part_width = bar_width / denominator
    
    for i in range(denominator):
        x = 10 + i * part_width
        fill_class = 'filled' if i < numerator else 'empty'
        svg += f'<rect x="{x}" y="10" width="{part_width}" height="{bar_height}" class="{fill_class}"/>'
    
    if show_label:
        svg += f'<text x="100" y="55" class="label">{numerator}/{denominator}</text>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Understanding Fractions (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Understanding Fractions - What is a fraction?"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['identify', 'read', 'meaning', 'visual', 'parts', 'numerator'])
            
            if q_type == 'identify':
                num = random.randint(1, 5)
                den = random.choice([2, 3, 4, 5, 6, 8])
                if num >= den:
                    num = den - 1
                
                q_text = f"What fraction is shown? {num} out of {den} parts are shaded."
                correct = f"{num}/{den}"
                wrong = [f"{den}/{num}", f"{num}/{den+1}", f"{den-num}/{den}"]
                explanation = f"Step 1: {num} parts shaded out of {den} total. Step 2: Write as {num}/{den}. ✓"
                image_svg = generate_fraction_circle_svg(num, den)
                
            elif q_type == 'read':
                num = random.randint(1, 4)
                den = random.choice([2, 3, 4, 5, 6, 8])
                if num >= den:
                    num = den - 1
                
                names = {
                    (1, 2): "one half", (1, 3): "one third", (2, 3): "two thirds",
                    (1, 4): "one quarter", (2, 4): "two quarters", (3, 4): "three quarters",
                    (1, 5): "one fifth", (2, 5): "two fifths", (3, 5): "three fifths", (4, 5): "four fifths",
                    (1, 6): "one sixth", (2, 6): "two sixths", (3, 6): "three sixths",
                    (1, 8): "one eighth", (3, 8): "three eighths", (5, 8): "five eighths"
                }
                
                name = names.get((num, den), f"{num} out of {den}")
                q_text = f"How do you write '{name}' as a fraction?"
                correct = f"{num}/{den}"
                wrong = [f"{den}/{num}", f"{num+1}/{den}", f"{num}/{den+1}"]
                explanation = f"Step 1: '{name}' means {num} parts out of {den}. Step 2: Written as {num}/{den}. ✓"
                image_svg = None
                
            elif q_type == 'meaning':
                den = random.choice([2, 3, 4, 5, 6, 8, 10])
                num = random.randint(1, den - 1)
                
                q_text = f"In the fraction {num}/{den}, what does the {den} represent?"
                correct = "Total parts"
                wrong = ["Shaded parts", "The answer", "Parts left over"]
                explanation = f"Step 1: The bottom number (denominator) shows total parts. Step 2: The top number shows how many we have. ✓"
                image_svg = generate_fraction_bar_svg(num, den)
                
            elif q_type == 'visual':
                num = random.randint(1, 4)
                den = random.choice([2, 3, 4, 5, 6, 8])
                if num >= den:
                    num = den - 1
                
                q_text = f"Look at the picture. What fraction is shaded?"
                correct = f"{num}/{den}"
                wrong = [f"{den-num}/{den}", f"{num}/{den+1}", f"{den}/{num}"]
                explanation = f"Step 1: Count shaded parts: {num}. Step 2: Count total parts: {den}. Step 3: Fraction = {num}/{den}. ✓"
                image_svg = generate_fraction_circle_svg(num, den, show_label=False)
                
            elif q_type == 'parts':
                den = random.choice([2, 3, 4, 5, 6, 8])
                num = random.randint(1, den - 1)
                
                q_text = f"A shape is divided into {den} equal parts. {num} parts are coloured. What fraction is coloured?"
                correct = f"{num}/{den}"
                wrong = [f"{den-num}/{den}", f"{num}/{den+1}", f"{den}/{num}"]
                explanation = f"Step 1: {num} coloured out of {den} total = {num}/{den}. ✓"
                image_svg = None
                
            else:  # numerator
                den = random.choice([2, 3, 4, 5, 6, 8])
                num = random.randint(1, den - 1)
                
                q_text = f"In the fraction {num}/{den}, what does the {num} represent?"
                correct = "Parts we have"
                wrong = ["Total parts", "Parts remaining", "The whole"]
                explanation = f"Step 1: The top number (numerator) shows how many parts we have. Step 2: {num} = parts we have. ✓"
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
# LEVEL 2: Halves and Quarters (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Halves and Quarters"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['half_of', 'quarter_of', 'identify', 'word'])
            
            if q_type == 'half_of':
                whole = random.choice([10, 12, 16, 18, 20, 24, 30, 40, 50, 100])
                half = whole // 2
                
                q_text = f"What is half of {whole}?"
                correct = str(half)
                wrong = [str(half + 2), str(whole), str(half - 2)]
                explanation = f"Step 1: Half means divide by 2. Step 2: {whole} ÷ 2 = {half}. ✓"
                image_svg = None
                
            elif q_type == 'quarter_of':
                whole = random.choice([8, 12, 16, 20, 24, 40, 100])
                quarter = whole // 4
                
                q_text = f"What is a quarter of {whole}?"
                correct = str(quarter)
                wrong = [str(quarter + 2), str(whole // 2), str(quarter - 1)]
                explanation = f"Step 1: Quarter means divide by 4. Step 2: {whole} ÷ 4 = {quarter}. ✓"
                image_svg = None
                
            elif q_type == 'identify':
                frac = random.choice([(1, 2), (1, 4), (2, 4), (3, 4)])
                names = {
                    (1, 2): "one half",
                    (1, 4): "one quarter",
                    (2, 4): "two quarters (or one half)",
                    (3, 4): "three quarters"
                }
                
                q_text = f"What is {frac[0]}/{frac[1]} called?"
                correct = names[frac].split(" (")[0]  # Get primary name
                wrong = ["one third", "one fifth", "two halves"]
                explanation = f"Step 1: {frac[0]}/{frac[1]} = {names[frac]}. ✓"
                image_svg = generate_fraction_circle_svg(frac[0], frac[1])
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                whole = random.choice([8, 10, 12, 16, 20])
                half = whole // 2
                quarter = whole // 4
                
                if random.choice([True, False]):
                    q_text = f"{name} has {whole} sweets and eats half. How many are left?"
                    correct = str(half)
                    wrong = [str(quarter), str(whole), str(half + 2)]
                    explanation = f"Step 1: Half of {whole} = {half}. Step 2: {whole} - {half} = {half} left. ✓"
                else:
                    q_text = f"{name} has {whole} stickers and gives away a quarter. How many given away?"
                    correct = str(quarter)
                    wrong = [str(half), str(whole), str(quarter + 2)]
                    explanation = f"Step 1: A quarter of {whole} = {whole} ÷ 4 = {quarter}. ✓"
                
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
# LEVEL 3: Comparing Fractions (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Comparing Fractions with same denominator"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['bigger', 'smaller', 'order', 'equal'])
            
            if q_type == 'bigger':
                den = random.choice([4, 5, 6, 8])
                num1 = random.randint(1, den - 2)
                num2 = random.randint(num1 + 1, den - 1)
                
                q_text = f"Which is bigger: {num1}/{den} or {num2}/{den}?"
                correct = f"{num2}/{den}"
                wrong = [f"{num1}/{den}", "They are equal", f"{den}/{num2}"]
                explanation = f"Step 1: Same denominator, compare numerators. Step 2: {num2} > {num1}, so {num2}/{den} is bigger. ✓"
                image_svg = None
                
            elif q_type == 'smaller':
                den = random.choice([4, 5, 6, 8])
                num1 = random.randint(2, den - 1)
                num2 = random.randint(1, num1 - 1)
                
                q_text = f"Which is smaller: {num1}/{den} or {num2}/{den}?"
                correct = f"{num2}/{den}"
                wrong = [f"{num1}/{den}", "They are equal", f"{den}/{num1}"]
                explanation = f"Step 1: Same denominator, compare numerators. Step 2: {num2} < {num1}, so {num2}/{den} is smaller. ✓"
                image_svg = None
                
            elif q_type == 'order':
                den = random.choice([4, 5, 6])
                nums = random.sample(range(1, den), 3)
                sorted_nums = sorted(nums)
                
                fracs = [f"{n}/{den}" for n in nums]
                sorted_fracs = [f"{n}/{den}" for n in sorted_nums]
                
                q_text = f"Put in order from smallest to biggest: {', '.join(fracs)}"
                correct = ', '.join(sorted_fracs)
                wrong = [', '.join(sorted_fracs[::-1]), ', '.join(fracs), f"{fracs[1]}, {fracs[0]}, {fracs[2]}"]
                explanation = f"Step 1: Same denominator - order by numerator. Step 2: {correct}. ✓"
                image_svg = None
                
            else:  # equal
                den = random.choice([4, 6, 8])
                num = random.randint(1, den - 1)
                
                q_text = f"True or False: {num}/{den} = {num}/{den}"
                correct = "True"
                wrong = ["False", "Cannot tell", "Only sometimes"]
                explanation = f"Step 1: {num}/{den} = {num}/{den}. Same fraction = same value. True! ✓"
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
# LEVEL 4: Equivalent Fractions (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Equivalent Fractions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['find_equiv', 'missing', 'is_equiv', 'visual'])
            
            if q_type == 'find_equiv':
                base_num = random.randint(1, 3)
                base_den = random.choice([2, 3, 4, 5])
                mult = random.randint(2, 4)
                
                equiv_num = base_num * mult
                equiv_den = base_den * mult
                
                q_text = f"Which fraction is equivalent to {base_num}/{base_den}?"
                correct = f"{equiv_num}/{equiv_den}"
                wrong = [f"{base_num + 1}/{base_den + 1}", f"{equiv_num}/{base_den}", f"{base_num}/{equiv_den}"]
                explanation = f"Step 1: Multiply top and bottom by {mult}. Step 2: {base_num}×{mult}/{base_den}×{mult} = {equiv_num}/{equiv_den}. ✓"
                image_svg = None
                
            elif q_type == 'missing':
                base_num = random.randint(1, 3)
                base_den = random.choice([2, 3, 4])
                mult = random.randint(2, 4)
                
                equiv_num = base_num * mult
                equiv_den = base_den * mult
                
                if random.choice([True, False]):
                    q_text = f"Find the missing number: {base_num}/{base_den} = ?/{equiv_den}"
                    correct = str(equiv_num)
                    wrong = [str(equiv_num + 1), str(base_num), str(equiv_den)]
                else:
                    q_text = f"Find the missing number: {base_num}/{base_den} = {equiv_num}/?"
                    correct = str(equiv_den)
                    wrong = [str(equiv_den + 1), str(base_den), str(equiv_num)]
                
                explanation = f"Step 1: {base_num}/{base_den} × {mult}/{mult} = {equiv_num}/{equiv_den}. ✓"
                image_svg = None
                
            elif q_type == 'is_equiv':
                base_num = random.randint(1, 3)
                base_den = random.choice([2, 3, 4])
                mult = random.randint(2, 3)
                
                equiv_num = base_num * mult
                equiv_den = base_den * mult
                
                # Sometimes make them not equivalent
                if random.choice([True, False]):
                    test_num, test_den = equiv_num, equiv_den
                    answer = "Yes"
                else:
                    test_num, test_den = equiv_num + 1, equiv_den
                    answer = "No"
                
                q_text = f"Is {base_num}/{base_den} equivalent to {test_num}/{test_den}?"
                correct = answer
                wrong = ["Yes" if answer == "No" else "No", "Cannot tell", "Sometimes"]
                explanation = f"Step 1: {base_num}/{base_den} = {equiv_num}/{equiv_den}. {answer}! ✓"
                image_svg = None
                
            else:  # visual
                num, den = random.choice([(1, 2), (1, 4), (2, 4)])
                mult = 2
                equiv_num, equiv_den = num * mult, den * mult
                
                q_text = f"The pictures show equivalent fractions. What is {num}/{den} equivalent to?"
                correct = f"{equiv_num}/{equiv_den}"
                wrong = [f"{num + 1}/{den + 1}", f"{num}/{equiv_den}", f"{equiv_num}/{den}"]
                explanation = f"Step 1: Same amount shaded. Step 2: {num}/{den} = {equiv_num}/{equiv_den}. ✓"
                image_svg = generate_fraction_bar_svg(num, den)
            
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
# LEVEL 5: Simplifying Fractions (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Simplifying Fractions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            # Start with a simple fraction and multiply
            simple_num = random.randint(1, 4)
            simple_den = random.choice([2, 3, 4, 5, 6])
            
            if simple_num >= simple_den:
                simple_num = simple_den - 1
            
            mult = random.randint(2, 4)
            complex_num = simple_num * mult
            complex_den = simple_den * mult
            
            q_type = random.choice(['simplify', 'lowest', 'find_hcf'])
            
            if q_type == 'simplify':
                q_text = f"Simplify {complex_num}/{complex_den}"
                correct = f"{simple_num}/{simple_den}"
                wrong = [f"{complex_num - 1}/{complex_den - 1}", f"{simple_num + 1}/{simple_den}", f"{complex_num}/{simple_den}"]
                explanation = f"Step 1: Divide top and bottom by {mult}. Step 2: {complex_num}/{complex_den} = {simple_num}/{simple_den}. ✓"
                
            elif q_type == 'lowest':
                q_text = f"Write {complex_num}/{complex_den} in its lowest terms."
                correct = f"{simple_num}/{simple_den}"
                wrong = [f"{complex_num}/{complex_den}", f"{simple_num + 1}/{simple_den + 1}", f"{mult}/{mult}"]
                explanation = f"Step 1: HCF of {complex_num} and {complex_den} is {mult}. Step 2: Divide both by {mult} = {simple_num}/{simple_den}. ✓"
                
            else:  # find_hcf
                q_text = f"What number divides both {complex_num} and {complex_den} to simplify {complex_num}/{complex_den}?"
                correct = str(mult)
                wrong = [str(mult + 1), str(simple_num), str(complex_num)]
                explanation = f"Step 1: Both {complex_num} and {complex_den} are divisible by {mult}. ✓"
            
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
# LEVEL 6: Mixed Numbers (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Mixed Numbers and Improper Fractions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['to_improper', 'to_mixed', 'identify', 'word'])
            
            if q_type == 'to_improper':
                whole = random.randint(1, 4)
                num = random.randint(1, 3)
                den = random.choice([2, 3, 4, 5])
                if num >= den:
                    num = den - 1
                
                improper_num = whole * den + num
                
                q_text = f"Convert {whole} {num}/{den} to an improper fraction."
                correct = f"{improper_num}/{den}"
                wrong = [f"{whole + num}/{den}", f"{num}/{den}", f"{improper_num}/{den + 1}"]
                explanation = f"Step 1: {whole} × {den} = {whole * den}. Step 2: {whole * den} + {num} = {improper_num}. Answer: {improper_num}/{den}. ✓"
                image_svg = None
                
            elif q_type == 'to_mixed':
                den = random.choice([2, 3, 4, 5])
                whole = random.randint(1, 4)
                remainder = random.randint(1, den - 1)
                improper_num = whole * den + remainder
                
                q_text = f"Convert {improper_num}/{den} to a mixed number."
                correct = f"{whole} {remainder}/{den}"
                wrong = [f"{whole + 1} {remainder}/{den}", f"{improper_num - den}/{den}", f"{whole} {remainder + 1}/{den}"]
                explanation = f"Step 1: {improper_num} ÷ {den} = {whole} remainder {remainder}. Answer: {whole} {remainder}/{den}. ✓"
                image_svg = None
                
            elif q_type == 'identify':
                den = random.choice([2, 3, 4])
                improper_num = random.randint(den + 1, den * 3)
                
                q_text = f"Is {improper_num}/{den} an improper fraction?"
                correct = "Yes" if improper_num > den else "No"
                wrong = ["No" if improper_num > den else "Yes", "Cannot tell", "It's a mixed number"]
                explanation = f"Step 1: {improper_num} > {den}, so numerator > denominator. Step 2: Yes, it's improper. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                whole = random.randint(2, 4)
                half = whole * 2 + 1
                
                q_text = f"{name} has {half} half pizzas. How many whole pizzas is that?"
                correct = f"{whole} 1/2"
                wrong = [f"{whole}", f"{whole + 1}", f"{half}"]
                explanation = f"Step 1: {half} halves = {half}/2. Step 2: {half}/2 = {whole} 1/2 pizzas. ✓"
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
# LEVEL 7: Adding Fractions (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Adding Fractions with same denominator"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            den = random.choice([4, 5, 6, 8, 10])
            num1 = random.randint(1, den // 2)
            num2 = random.randint(1, den // 2)
            
            result_num = num1 + num2
            simp_num, simp_den = simplify_fraction(result_num, den)
            
            q_type = random.choice(['basic', 'simplify', 'word'])
            
            if q_type == 'basic':
                q_text = f"What is {num1}/{den} + {num2}/{den}?"
                correct = f"{result_num}/{den}"
                wrong = [f"{num1 + num2 + 1}/{den}", f"{num1}/{den + den}", f"{result_num}/{den + den}"]
                explanation = f"Step 1: Same denominator - add numerators. Step 2: {num1} + {num2} = {result_num}. Answer: {result_num}/{den}. ✓"
                
            elif q_type == 'simplify':
                q_text = f"Add and simplify: {num1}/{den} + {num2}/{den}"
                if simp_num != result_num:
                    correct = f"{simp_num}/{simp_den}"
                else:
                    correct = f"{result_num}/{den}"
                wrong = [f"{result_num}/{den * 2}", f"{num1 + num2 + 1}/{den}", f"{result_num + 1}/{den}"]
                explanation = f"Step 1: {num1}/{den} + {num2}/{den} = {result_num}/{den}. Step 2: Simplified = {simp_num}/{simp_den}. ✓"
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} ate {num1}/{den} of a pizza. Their friend ate {num2}/{den}. How much pizza eaten altogether?"
                correct = f"{result_num}/{den}"
                wrong = [f"{num1 + num2 + 1}/{den}", f"{num1}/{den}", f"{result_num}/{den * 2}"]
                explanation = f"Step 1: {num1}/{den} + {num2}/{den} = {result_num}/{den} of the pizza. ✓"
            
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
# LEVEL 8: Subtracting Fractions (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Subtracting Fractions with same denominator"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            den = random.choice([4, 5, 6, 8, 10])
            num1 = random.randint(den // 2, den - 1)
            num2 = random.randint(1, num1 - 1)
            
            result_num = num1 - num2
            simp_num, simp_den = simplify_fraction(result_num, den)
            
            q_type = random.choice(['basic', 'simplify', 'word'])
            
            if q_type == 'basic':
                q_text = f"What is {num1}/{den} - {num2}/{den}?"
                correct = f"{result_num}/{den}"
                wrong = [f"{num1 - num2 + 1}/{den}", f"{num1 + num2}/{den}", f"{result_num}/{den * 2}"]
                explanation = f"Step 1: Same denominator - subtract numerators. Step 2: {num1} - {num2} = {result_num}. Answer: {result_num}/{den}. ✓"
                
            elif q_type == 'simplify':
                q_text = f"Subtract and simplify: {num1}/{den} - {num2}/{den}"
                if simp_num != result_num:
                    correct = f"{simp_num}/{simp_den}"
                else:
                    correct = f"{result_num}/{den}"
                wrong = [f"{num1 + num2}/{den}", f"{result_num + 1}/{den}", f"{num1}/{den}"]
                explanation = f"Step 1: {num1}/{den} - {num2}/{den} = {result_num}/{den}. Step 2: Simplified = {simp_num}/{simp_den}. ✓"
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} had {num1}/{den} of a cake. They ate {num2}/{den}. How much cake is left?"
                correct = f"{result_num}/{den}"
                wrong = [f"{num1 + num2}/{den}", f"{num1}/{den}", f"{result_num + 1}/{den}"]
                explanation = f"Step 1: {num1}/{den} - {num2}/{den} = {result_num}/{den} of the cake left. ✓"
            
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
# LEVEL 9: Fraction Word Problems (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Fraction Word Problems"""
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
                # Fraction of a quantity
                whole = random.choice([12, 15, 18, 20, 24, 30])
                den = random.choice([2, 3, 4, 5, 6])
                while whole % den != 0:
                    whole = random.choice([12, 15, 18, 20, 24, 30])
                num = random.randint(1, den - 1)
                answer = (whole * num) // den
                
                q_text = f"What is {num}/{den} of {whole}?"
                correct = str(answer)
                wrong = [str(answer + 2), str(whole), str(whole // den)]
                explanation = f"Step 1: {whole} ÷ {den} = {whole // den}. Step 2: {whole // den} × {num} = {answer}. ✓"
                
            elif problem_type == 2:
                # Remaining fraction
                den = random.choice([4, 5, 6, 8])
                used_num = random.randint(1, den - 2)
                remaining = den - used_num
                
                q_text = f"{name} used {used_num}/{den} of the paint. What fraction is left?"
                correct = f"{remaining}/{den}"
                wrong = [f"{used_num}/{den}", f"{remaining}/{den * 2}", f"1/{den}"]
                explanation = f"Step 1: {den}/{den} - {used_num}/{den} = {remaining}/{den}. ✓"
                
            elif problem_type == 3:
                # Comparison
                whole = random.choice([20, 24, 30, 40])
                half = whole // 2
                quarter = whole // 4
                
                q_text = f"Which is more: half of {whole} or a quarter of {whole * 2}?"
                correct = "They are equal"
                wrong = [f"Half of {whole}", f"Quarter of {whole * 2}", "Cannot tell"]
                explanation = f"Step 1: Half of {whole} = {half}. Quarter of {whole * 2} = {quarter * 2}. They are equal! ✓"
                
            else:
                # Multi-step
                total = random.choice([12, 16, 20, 24])
                half = total // 2
                quarter = total // 4
                
                q_text = f"A box has {total} chocolates. {name} eats half. Then eats a quarter of what's left. How many chocolates remain?"
                remaining_after_half = half
                ate_quarter = remaining_after_half // 4
                final = remaining_after_half - ate_quarter
                
                correct = str(final)
                wrong = [str(quarter), str(half), str(total - quarter)]
                explanation = f"Step 1: After half: {half}. Step 2: Quarter of {half} = {ate_quarter}. Step 3: {half} - {ate_quarter} = {final}. ✓"
            
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
# LEVEL 10: Multiplying Fractions (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Multiplying Fractions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['basic', 'whole', 'word', 'simplify'])
            
            if q_type == 'basic':
                num1 = random.randint(1, 3)
                den1 = random.choice([2, 3, 4])
                num2 = random.randint(1, 3)
                den2 = random.choice([2, 3, 4])
                
                result_num = num1 * num2
                result_den = den1 * den2
                simp_num, simp_den = simplify_fraction(result_num, result_den)
                
                q_text = f"What is {num1}/{den1} × {num2}/{den2}?"
                correct = f"{simp_num}/{simp_den}"
                wrong = [f"{num1 + num2}/{den1 + den2}", f"{result_num + 1}/{result_den}", f"{num1}/{den2}"]
                explanation = f"Step 1: Multiply numerators: {num1} × {num2} = {result_num}. Step 2: Multiply denominators: {den1} × {den2} = {result_den}. Answer: {simp_num}/{simp_den}. ✓"
                
            elif q_type == 'whole':
                whole = random.randint(2, 6)
                num = random.randint(1, 3)
                den = random.choice([2, 3, 4])
                
                result = (whole * num) // den if (whole * num) % den == 0 else f"{whole * num}/{den}"
                
                q_text = f"What is {num}/{den} of {whole}?"
                correct = str((whole * num) // den) if (whole * num) % den == 0 else f"{whole * num}/{den}"
                wrong = [str(whole + num), str(whole * den), str(num * den)]
                explanation = f"Step 1: {num}/{den} × {whole} = {whole * num}/{den} = {correct}. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                whole = random.choice([12, 15, 18, 20])
                
                q_text = f"{name} has {whole} sweets. They give 1/3 of them away. How many given away?"
                answer = whole // 3
                correct = str(answer)
                wrong = [str(answer + 1), str(whole), str(whole - answer)]
                explanation = f"Step 1: 1/3 of {whole} = {whole} ÷ 3 = {answer}. ✓"
                
            else:  # simplify
                num1 = random.randint(1, 2)
                den1 = random.choice([2, 3])
                num2 = random.randint(1, 2)
                den2 = random.choice([2, 3])
                
                result_num = num1 * num2
                result_den = den1 * den2
                simp_num, simp_den = simplify_fraction(result_num, result_den)
                
                q_text = f"Multiply and simplify: {num1}/{den1} × {num2}/{den2}"
                correct = f"{simp_num}/{simp_den}"
                wrong = [f"{result_num}/{result_den}" if result_num != simp_num else f"{simp_num + 1}/{simp_den}", f"{num1 + num2}/{den1 * den2}", f"{num1}/{simp_den}"]
                explanation = f"Step 1: {num1} × {num2} / {den1} × {den2} = {result_num}/{result_den}. Step 2: Simplified = {simp_num}/{simp_den}. ✓"
            
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
    """Level 11: Complex Fraction Problem Solving"""
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
                # Working backwards
                answer = random.randint(6, 15)
                multiplier = random.choice([2, 3, 4])
                whole = answer * multiplier
                
                q_text = f"1/{multiplier} of a number is {answer}. What is the number?"
                correct = str(whole)
                wrong = [str(answer * (multiplier - 1)), str(answer + multiplier), str(answer)]
                explanation = f"Step 1: If 1/{multiplier} = {answer}, then whole = {answer} × {multiplier} = {whole}. ✓"
                
            elif problem_type == 2:
                # Combined fractions
                total = random.choice([20, 24, 30, 40])
                frac1 = total // 4
                frac2 = total // 5 if total % 5 == 0 else total // 4
                
                q_text = f"{name} spent 1/4 of €{total} on books and 1/4 on food. How much money left?"
                spent = frac1 * 2
                left = total - spent
                correct = f"€{left}"
                wrong = [f"€{frac1}", f"€{total}", f"€{spent}"]
                explanation = f"Step 1: Books = €{frac1}, Food = €{frac1}. Step 2: Left = €{total} - €{spent} = €{left}. ✓"
                
            elif problem_type == 3:
                # Fraction comparison
                items = random.choice([24, 30, 36, 40])
                frac1_val = items // 3
                frac2_val = items // 4
                diff = frac1_val - frac2_val
                
                q_text = f"Is 1/3 of {items} more or less than 1/4 of {items}? By how much?"
                correct = f"More by {diff}"
                wrong = [f"Less by {diff}", "Same amount", f"More by {frac1_val}"]
                explanation = f"Step 1: 1/3 of {items} = {frac1_val}. 1/4 of {items} = {frac2_val}. Step 2: {frac1_val} - {frac2_val} = {diff} more. ✓"
                
            else:
                # Multi-step
                total = random.choice([36, 48, 60])
                third = total // 3
                remaining = total - third
                half_remaining = remaining // 2
                final = remaining - half_remaining
                
                q_text = f"A jar has {total} sweets. {name} takes 1/3. Then half of what's left is given away. How many remain?"
                correct = str(final)
                wrong = [str(half_remaining), str(third), str(remaining)]
                explanation = f"Step 1: After 1/3 taken: {remaining}. Step 2: Half given = {half_remaining}. Step 3: Remaining = {final}. ✓"
            
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
    print("VALIDATION - Basic Fractions")
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
    print("AgentMath - Basic Fractions Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Understanding Fractions", generate_level_1),
        (2, "Halves and Quarters", generate_level_2),
        (3, "Comparing Fractions", generate_level_3),
        (4, "Equivalent Fractions", generate_level_4),
        (5, "Simplifying Fractions", generate_level_5),
        (6, "Mixed Numbers", generate_level_6),
        (7, "Adding Fractions", generate_level_7),
        (8, "Subtracting Fractions", generate_level_8),
        (9, "Word Problems", generate_level_9),
        (10, "Multiplying Fractions", generate_level_10),
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
