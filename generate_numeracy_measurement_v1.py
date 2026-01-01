#!/usr/bin/env python3
"""
AgentMath - Measurement Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Units of length, mass, capacity; reading scales
  L4-6:   Developing - Converting units, comparing measurements
  L7-9:   Proficient - Word problems, perimeter, area basics
  L10-12: Advanced - Complex conversions, multi-step problems

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'measurement'
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

def generate_ruler_svg(length_cm, max_cm=15):
    """Generate SVG of a ruler showing measurement"""
    width = max_cm * 20 + 40
    svg = f'''<svg viewBox="0 0 {width} 60" xmlns="http://www.w3.org/2000/svg">
    <style>
        .ruler {{ fill: #fef3c7; stroke: #d97706; stroke-width: 2; }}
        .tick {{ stroke: #1f2937; }}
        .num {{ font-size: 8px; fill: #1f2937; text-anchor: middle; }}
        .measure {{ fill: #10b981; opacity: 0.5; }}
        .arrow {{ stroke: #dc2626; stroke-width: 2; fill: none; }}
    </style>
    <rect x="20" y="15" width="{max_cm * 20}" height="25" class="ruler" rx="2"/>'''
    
    # Tick marks
    for i in range(max_cm + 1):
        x = 20 + i * 20
        tick_height = 15 if i % 5 == 0 else (10 if i % 1 == 0 else 5)
        svg += f'<line x1="{x}" y1="15" x2="{x}" y2="{15 + tick_height}" class="tick"/>'
        if i % 1 == 0:
            svg += f'<text x="{x}" y="52" class="num">{i}</text>'
    
    # Highlight measurement
    svg += f'<rect x="20" y="15" width="{length_cm * 20}" height="25" class="measure"/>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Units of Length (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Understanding Units of Length"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    # Expanded items list
    length_items = [
        ("length of a pencil", "cm"), ("height of a person", "cm"), ("distance to Dublin", "km"),
        ("width of a book", "cm"), ("length of a football pitch", "m"), ("thickness of a coin", "mm"),
        ("height of a door", "m"), ("width of a fingernail", "mm"), ("length of a car", "m"),
        ("distance run in a marathon", "km"), ("length of an ant", "mm"), ("height of a table", "cm"),
        ("width of a road", "m"), ("length of Ireland", "km"), ("thickness of paper", "mm"),
        ("height of a classroom", "m"), ("width of a phone", "cm"), ("length of a bus", "m"),
        ("distance to Cork", "km"), ("length of your thumb", "cm"), ("height of a tree", "m"),
        ("width of a hair", "mm"), ("length of a ruler", "cm"), ("distance walked in an hour", "km"),
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['unit_match', 'abbreviation', 'choose_unit', 'compare', 'read_ruler', 'estimate', 'convert_simple', 'order'])
            
            if q_type == 'unit_match':
                units = [
                    ("millimetre", "mm", "very small lengths like thickness of a coin"),
                    ("millimetre", "mm", "tiny things like width of a staple"),
                    ("centimetre", "cm", "small lengths like width of a finger"),
                    ("centimetre", "cm", "medium small things like length of a key"),
                    ("metre", "m", "medium lengths like height of a door"),
                    ("metre", "m", "room-sized things like width of a classroom"),
                    ("kilometre", "km", "long distances like between towns"),
                    ("kilometre", "km", "travel distances like a car journey")
                ]
                unit_name, abbrev, description = random.choice(units)
                
                q_text = f"What unit would you use to measure {description}?"
                correct = unit_name
                wrong = ["millimetre", "centimetre", "metre", "kilometre"]
                wrong = [w for w in wrong if w != unit_name][:3]
                explanation = f"Step 1: {description.capitalize()} → use {unit_name} ({abbrev}). ✓"
                image_svg = None
                
            elif q_type == 'abbreviation':
                units = [("millimetre", "mm"), ("centimetre", "cm"), ("metre", "m"), ("kilometre", "km")]
                unit_name, abbrev = random.choice(units)
                variant = random.choice(['abbrev', 'full'])
                
                if variant == 'abbrev':
                    q_text = f"What is the abbreviation for {unit_name}?"
                    correct = abbrev
                    wrong = [u[1] for u in units if u[1] != abbrev]
                else:
                    q_text = f"What does '{abbrev}' stand for?"
                    correct = unit_name
                    wrong = [u[0] for u in units if u[0] != unit_name]
                explanation = f"Step 1: {unit_name} is abbreviated as {abbrev}. ✓"
                image_svg = None
                
            elif q_type == 'choose_unit':
                item, correct_unit = random.choice(length_items)
                all_units = ["mm", "cm", "m", "km"]
                wrong_units = [u for u in all_units if u != correct_unit]
                
                q_text = f"What unit is best to measure the {item}?"
                correct = correct_unit
                wrong = wrong_units
                explanation = f"Step 1: {item.capitalize()} → measure in {correct_unit}. ✓"
                image_svg = None
                
            elif q_type == 'compare':
                comparisons = [
                    ("1 metre", "100 centimetres", "equal"),
                    ("1 kilometre", "100 metres", "greater"),
                    ("1 centimetre", "1 metre", "smaller"),
                    ("50 cm", "half a metre", "equal"),
                    ("1 km", "1000 m", "equal"),
                    ("10 mm", "1 cm", "equal"),
                    ("500 m", "1 km", "smaller"),
                    ("2 m", "200 cm", "equal"),
                    ("150 cm", "1 m", "greater"),
                    ("5 km", "5000 m", "equal"),
                ]
                val1, val2, relation = random.choice(comparisons)
                
                q_text = f"Is {val1} greater than, smaller than, or equal to {val2}?"
                correct = relation.capitalize()
                wrong = ["Greater" if relation != "greater" else "Smaller", 
                        "Smaller" if relation != "smaller" else "Equal",
                        "Equal" if relation != "equal" else "Greater"]
                explanation = f"Step 1: {val1} is {relation} to {val2}. ✓"
                image_svg = None
                
            elif q_type == 'read_ruler':
                length = random.randint(1, 14)
                
                q_text = f"The ruler shows a line ending at {length}. How long is it?"
                correct = f"{length} cm"
                wrong = [f"{length + 1} cm", f"{length - 1} cm" if length > 1 else "0.5 cm", f"{length * 10} mm"]
                explanation = f"Step 1: Read from 0 to {length} = {length} cm. ✓"
                image_svg = generate_ruler_svg(length)
                
            elif q_type == 'estimate':
                estimates = [
                    ("a door handle height from the floor", "1 m", ["10 cm", "10 m", "1 km"]),
                    ("length of a new pencil", "15 cm", ["15 mm", "15 m", "1.5 m"]),
                    ("width of a classroom", "8 m", ["8 cm", "80 m", "8 km"]),
                    ("thickness of your little finger", "1 cm", ["1 mm", "1 m", "10 cm"]),
                    ("height of a basketball hoop", "3 m", ["30 cm", "30 m", "3 cm"]),
                    ("length of a shoelace", "80 cm", ["8 cm", "8 m", "80 mm"]),
                ]
                item, correct_est, wrong_ests = random.choice(estimates)
                
                q_text = f"Estimate: What is the approximate {item}?"
                correct = correct_est
                wrong = wrong_ests
                explanation = f"Step 1: {item.capitalize()} ≈ {correct_est}. ✓"
                image_svg = None
                
            elif q_type == 'convert_simple':
                conversions = [
                    ("1 m", "100 cm"), ("1 km", "1000 m"), ("1 cm", "10 mm"),
                    ("2 m", "200 cm"), ("3 km", "3000 m"), ("5 cm", "50 mm"),
                ]
                from_val, to_val = random.choice(conversions)
                
                q_text = f"How many {to_val.split()[1]} are in {from_val}?"
                correct = to_val.split()[0]
                num = int(to_val.split()[0])
                wrong = [str(num // 10), str(num * 10), str(num + 100)]
                explanation = f"Step 1: {from_val} = {to_val}. ✓"
                image_svg = None
                
            else:  # order
                units_order = ["mm", "cm", "m", "km"]
                q_text = f"Put these units in order from smallest to largest: km, mm, cm, m"
                correct = "mm, cm, m, km"
                wrong = ["km, m, cm, mm", "cm, mm, m, km", "m, km, cm, mm"]
                explanation = f"Step 1: Smallest to largest: mm < cm < m < km. ✓"
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
# LEVEL 2: Units of Mass (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Understanding Units of Mass"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    # Expanded mass items list
    mass_items = [
        ("a bag of apples", "kg"), ("a feather", "g"), ("a lorry", "tonnes"),
        ("a person", "kg"), ("a slice of bread", "g"), ("a tablet (medicine)", "mg"),
        ("a bag of sugar", "kg"), ("a paperclip", "g"), ("an elephant", "tonnes"),
        ("a laptop", "kg"), ("a grain of rice", "mg"), ("a bicycle", "kg"),
        ("a pen", "g"), ("a ship", "tonnes"), ("a coin", "g"),
        ("a baby", "kg"), ("a leaf", "g"), ("a bus", "tonnes"),
        ("a textbook", "kg"), ("a stamp", "g"), ("an aeroplane", "tonnes"),
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['unit_match', 'abbreviation', 'choose_unit', 'compare', 'estimate', 'convert_simple', 'order', 'word'])
            
            if q_type == 'unit_match':
                units = [
                    ("gram", "g", "light things like a paperclip"),
                    ("gram", "g", "small items like a coin"),
                    ("kilogram", "kg", "heavier things like a bag of sugar"),
                    ("kilogram", "kg", "medium things like a laptop"),
                    ("tonne", "t", "very heavy things like a car"),
                    ("tonne", "t", "huge things like an elephant"),
                    ("milligram", "mg", "tiny amounts like medicine dose"),
                ]
                unit_name, abbrev, description = random.choice(units)
                
                q_text = f"What unit would you use to measure {description}?"
                correct = unit_name
                wrong = ["gram", "kilogram", "tonne", "milligram"]
                wrong = [w for w in wrong if w != unit_name][:3]
                explanation = f"Step 1: {description.capitalize()} → use {unit_name} ({abbrev}). ✓"
                image_svg = None
                
            elif q_type == 'abbreviation':
                units = [("gram", "g"), ("kilogram", "kg"), ("milligram", "mg"), ("tonne", "t")]
                unit_name, abbrev = random.choice(units)
                variant = random.choice(['abbrev', 'full'])
                
                if variant == 'abbrev':
                    q_text = f"What is the abbreviation for {unit_name}?"
                    correct = abbrev
                    wrong = [u[1] for u in units if u[1] != abbrev]
                else:
                    q_text = f"What does '{abbrev}' stand for in mass?"
                    correct = unit_name
                    wrong = [u[0] for u in units if u[0] != unit_name]
                explanation = f"Step 1: {unit_name} is abbreviated as {abbrev}. ✓"
                image_svg = None
                
            elif q_type == 'choose_unit':
                item, correct_unit = random.choice(mass_items)
                all_units = ["mg", "g", "kg", "tonnes"]
                wrong_units = [u for u in all_units if u != correct_unit]
                
                q_text = f"What unit is best to measure the mass of {item}?"
                correct = correct_unit
                wrong = wrong_units
                explanation = f"Step 1: {item.capitalize()} → measure in {correct_unit}. ✓"
                image_svg = None
                
            elif q_type == 'compare':
                comparisons = [
                    ("1 kilogram", "1000 grams", "equal"),
                    ("500 g", "half a kilogram", "equal"),
                    ("1 kg", "500 g", "greater"),
                    ("100 g", "1 kg", "smaller"),
                    ("2 kg", "2000 g", "equal"),
                    ("1 tonne", "1000 kg", "equal"),
                    ("750 g", "1 kg", "smaller"),
                    ("1500 g", "1 kg", "greater"),
                    ("250 g", "quarter of a kg", "equal"),
                    ("3 kg", "3000 g", "equal"),
                ]
                val1, val2, relation = random.choice(comparisons)
                
                q_text = f"Is {val1} greater than, smaller than, or equal to {val2}?"
                correct = relation.capitalize()
                wrong = ["Greater" if relation != "greater" else "Smaller", 
                        "Smaller" if relation != "smaller" else "Equal",
                        "Equal" if relation != "equal" else "Greater"]
                explanation = f"Step 1: {val1} is {relation} to {val2}. ✓"
                image_svg = None
                
            elif q_type == 'estimate':
                items = [
                    ("an apple", "150 g", ["15 g", "1.5 kg", "15 kg"]),
                    ("a bag of flour", "1 kg", ["100 g", "10 kg", "1 g"]),
                    ("a car", "1 tonne", ["100 kg", "10 kg", "10 tonnes"]),
                    ("a phone", "200 g", ["20 g", "2 kg", "20 kg"]),
                    ("a loaf of bread", "500 g", ["50 g", "5 kg", "5 g"]),
                    ("a newborn baby", "3 kg", ["300 g", "30 kg", "30 g"]),
                    ("a tennis ball", "60 g", ["6 g", "600 g", "6 kg"]),
                    ("a watermelon", "5 kg", ["500 g", "50 kg", "50 g"]),
                ]
                item, correct_mass, wrong_masses = random.choice(items)
                
                q_text = f"About how much does {item} weigh?"
                correct = correct_mass
                wrong = wrong_masses
                explanation = f"Step 1: {item.capitalize()} weighs about {correct_mass}. ✓"
                image_svg = None
                
            elif q_type == 'convert_simple':
                conversions = [
                    ("1 kg", "1000 g"), ("2 kg", "2000 g"), ("half a kg", "500 g"),
                    ("1 tonne", "1000 kg"), ("3 kg", "3000 g"), ("1.5 kg", "1500 g"),
                ]
                from_val, to_val = random.choice(conversions)
                
                q_text = f"How many grams are in {from_val}?"
                correct = to_val.split()[0] + " g"
                num = int(to_val.split()[0])
                wrong = [f"{num // 10} g", f"{num * 10} g", f"{num + 500} g"]
                explanation = f"Step 1: {from_val} = {to_val}. ✓"
                image_svg = None
                
            elif q_type == 'order':
                q_text = f"Put these masses in order from lightest to heaviest: 1 kg, 500 g, 2 kg, 100 g"
                correct = "100 g, 500 g, 1 kg, 2 kg"
                wrong = ["2 kg, 1 kg, 500 g, 100 g", "500 g, 100 g, 1 kg, 2 kg", "1 kg, 2 kg, 100 g, 500 g"]
                explanation = f"Step 1: Lightest to heaviest: 100 g < 500 g < 1 kg < 2 kg. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                item_weight = random.choice([(200, "g"), (500, "g"), (1, "kg"), (2, "kg")])
                
                q_text = f"{name} has a bag weighing {item_weight[0]} {item_weight[1]}. What is the mass?"
                correct = f"{item_weight[0]} {item_weight[1]}"
                wrong = [f"{item_weight[0] * 10} {item_weight[1]}", f"{item_weight[0] // 2} {item_weight[1]}", f"{item_weight[0]} {'kg' if item_weight[1] == 'g' else 'g'}"]
                explanation = f"Step 1: The bag weighs {correct}. ✓"
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
# LEVEL 3: Units of Capacity (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Understanding Units of Capacity"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    # Expanded capacity items list
    capacity_items = [
        ("a swimming pool", "litres"), ("a teaspoon of medicine", "ml"), ("a carton of milk", "litres"),
        ("a drop of water", "ml"), ("petrol in a car", "litres"), ("a cup of tea", "ml"),
        ("a bucket", "litres"), ("a spoonful of syrup", "ml"), ("a fish tank", "litres"),
        ("a water bottle", "ml"), ("a bathtub", "litres"), ("a syringe", "ml"),
        ("a watering can", "litres"), ("a perfume bottle", "ml"), ("a paddling pool", "litres"),
        ("an eyedropper", "ml"), ("a washing machine drum", "litres"), ("a juice box", "ml"),
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['unit_match', 'abbreviation', 'choose_unit', 'compare', 'estimate', 'convert_simple', 'order', 'word'])
            
            if q_type == 'unit_match':
                units = [
                    ("millilitre", "ml", "small amounts like medicine"),
                    ("millilitre", "ml", "tiny amounts like eye drops"),
                    ("millilitre", "ml", "small drinks like a juice box"),
                    ("litre", "l", "larger amounts like a bottle of water"),
                    ("litre", "l", "big containers like a bucket"),
                    ("litre", "l", "household amounts like milk"),
                ]
                unit_name, abbrev, description = random.choice(units)
                
                q_text = f"What unit would you use to measure {description}?"
                correct = unit_name
                wrong = ["litre" if unit_name == "millilitre" else "millilitre", "gram", "centimetre"]
                explanation = f"Step 1: {description.capitalize()} → use {unit_name} ({abbrev}). ✓"
                image_svg = None
                
            elif q_type == 'abbreviation':
                units = [("millilitre", "ml"), ("litre", "l")]
                unit_name, abbrev = random.choice(units)
                variant = random.choice(['abbrev', 'full'])
                
                if variant == 'abbrev':
                    q_text = f"What is the abbreviation for {unit_name}?"
                    correct = abbrev
                    wrong = ["l" if abbrev == "ml" else "ml", "m", "g"]
                else:
                    q_text = f"What does '{abbrev}' stand for in capacity?"
                    correct = unit_name
                    wrong = ["litre" if unit_name == "millilitre" else "millilitre", "metre", "gram"]
                explanation = f"Step 1: {unit_name} is abbreviated as {abbrev}. ✓"
                image_svg = None
                
            elif q_type == 'choose_unit':
                item, correct_unit = random.choice(capacity_items)
                wrong_units = ["ml" if correct_unit == "litres" else "litres", "kg", "cm"]
                
                q_text = f"What unit is best to measure the capacity of {item}?"
                correct = correct_unit
                wrong = wrong_units
                explanation = f"Step 1: {item.capitalize()} → measure in {correct_unit}. ✓"
                image_svg = None
                
            elif q_type == 'compare':
                comparisons = [
                    ("1 litre", "1000 ml", "equal"),
                    ("500 ml", "half a litre", "equal"),
                    ("1 l", "500 ml", "greater"),
                    ("250 ml", "1 l", "smaller"),
                    ("2 litres", "2000 ml", "equal"),
                    ("750 ml", "1 litre", "smaller"),
                    ("1500 ml", "1 litre", "greater"),
                    ("quarter of a litre", "250 ml", "equal"),
                    ("3 litres", "3000 ml", "equal"),
                    ("100 ml", "1 litre", "smaller"),
                ]
                val1, val2, relation = random.choice(comparisons)
                
                q_text = f"Is {val1} greater than, smaller than, or equal to {val2}?"
                correct = relation.capitalize()
                wrong = ["Greater" if relation != "greater" else "Smaller", 
                        "Smaller" if relation != "smaller" else "Equal",
                        "Equal" if relation != "equal" else "Greater"]
                explanation = f"Step 1: {val1} is {relation} to {val2}. ✓"
                image_svg = None
                
            elif q_type == 'estimate':
                items = [
                    ("a glass of water", "250 ml", ["25 ml", "2.5 l", "25 l"]),
                    ("a bath", "80 litres", ["8 l", "800 ml", "8000 l"]),
                    ("a kettle", "1.5 litres", ["150 ml", "15 l", "0.15 l"]),
                    ("a can of fizzy drink", "330 ml", ["33 ml", "3.3 l", "33 l"]),
                    ("a large water bottle", "2 litres", ["200 ml", "20 l", "20 ml"]),
                    ("a mug of coffee", "300 ml", ["30 ml", "3 l", "30 l"]),
                    ("a small carton of juice", "200 ml", ["20 ml", "2 l", "20 l"]),
                    ("a bucket", "10 litres", ["1 l", "100 l", "100 ml"]),
                ]
                item, correct_cap, wrong_caps = random.choice(items)
                
                q_text = f"About how much does {item} hold?"
                correct = correct_cap
                wrong = wrong_caps
                explanation = f"Step 1: {item.capitalize()} holds about {correct_cap}. ✓"
                image_svg = None
                
            elif q_type == 'convert_simple':
                conversions = [
                    ("1 litre", "1000 ml"), ("2 litres", "2000 ml"), ("half a litre", "500 ml"),
                    ("3 litres", "3000 ml"), ("1.5 litres", "1500 ml"), ("quarter of a litre", "250 ml"),
                ]
                from_val, to_val = random.choice(conversions)
                
                q_text = f"How many ml are in {from_val}?"
                correct = to_val.split()[0] + " ml"
                num = int(to_val.split()[0])
                wrong = [f"{num // 10} ml", f"{num * 10} ml", f"{num + 500} ml"]
                explanation = f"Step 1: {from_val} = {to_val}. ✓"
                image_svg = None
                
            elif q_type == 'order':
                q_text = f"Put these capacities in order from smallest to largest: 1 l, 500 ml, 2 l, 250 ml"
                correct = "250 ml, 500 ml, 1 l, 2 l"
                wrong = ["2 l, 1 l, 500 ml, 250 ml", "500 ml, 250 ml, 1 l, 2 l", "1 l, 2 l, 250 ml, 500 ml"]
                explanation = f"Step 1: Smallest to largest: 250 ml < 500 ml < 1 l < 2 l. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                amount = random.choice([(250, "ml"), (500, "ml"), (1, "litre"), (2, "litres")])
                
                q_text = f"{name} drinks {amount[0]} {amount[1]} of water. How much is that?"
                correct = f"{amount[0]} {amount[1]}"
                wrong = [f"{amount[0] * 10} {amount[1]}", f"{amount[0] // 2} {amount[1]}" if amount[0] > 1 else f"{amount[0] * 2} {amount[1]}", f"{amount[0]} {'litres' if amount[1] == 'ml' else 'ml'}"]
                explanation = f"Step 1: {name} drinks {correct} of water. ✓"
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
# LEVEL 4: Converting Length (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Converting Length Units"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['cm_to_m', 'm_to_cm', 'mm_to_cm', 'cm_to_mm', 'km_to_m', 'm_to_km', 'word', 'mixed'])
            
            if q_type == 'cm_to_m':
                cm = random.choice([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 750, 800, 900, 1000])
                m = cm / 100
                
                q_text = f"Convert {cm} cm to metres."
                correct = f"{m} m"
                wrong = [f"{cm} m", f"{m * 10} m", f"{cm / 10} m"]
                explanation = f"Step 1: {cm} cm ÷ 100 = {m} m. ✓"
                
            elif q_type == 'm_to_cm':
                m = random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10])
                cm = int(m * 100)
                
                q_text = f"Convert {m} m to centimetres."
                correct = f"{cm} cm"
                wrong = [f"{m} cm", f"{cm // 10} cm", f"{cm * 10} cm"]
                explanation = f"Step 1: {m} m × 100 = {cm} cm. ✓"
                
            elif q_type == 'mm_to_cm':
                mm = random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150, 200, 250])
                cm = mm / 10
                
                q_text = f"Convert {mm} mm to centimetres."
                correct = f"{cm} cm"
                wrong = [f"{mm} cm", f"{cm * 10} cm", f"{mm * 10} cm"]
                explanation = f"Step 1: {mm} mm ÷ 10 = {cm} cm. ✓"
                
            elif q_type == 'cm_to_mm':
                cm = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30])
                mm = cm * 10
                
                q_text = f"Convert {cm} cm to millimetres."
                correct = f"{mm} mm"
                wrong = [f"{cm} mm", f"{mm // 10} mm", f"{mm * 10} mm"]
                explanation = f"Step 1: {cm} cm × 10 = {mm} mm. ✓"
                
            elif q_type == 'km_to_m':
                km = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20])
                m = km * 1000
                
                q_text = f"Convert {km} km to metres."
                correct = f"{m} m"
                wrong = [f"{km * 100} m", f"{km} m", f"{m * 10} m"]
                explanation = f"Step 1: {km} km × 1000 = {m} m. ✓"
                
            elif q_type == 'm_to_km':
                m = random.choice([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 6000, 7500, 8000, 10000])
                km = m / 1000
                
                q_text = f"Convert {m} m to kilometres."
                correct = f"{km} km"
                wrong = [f"{m} km", f"{km * 10} km", f"{m / 100} km"]
                explanation = f"Step 1: {m} m ÷ 1000 = {km} km. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                scenarios = [
                    (f"{name}'s desk is 120 cm long. How many metres is that?", "1.2 m", ["12 m", "0.12 m", "120 m"]),
                    (f"A path is 2.5 km long. How many metres?", "2500 m", ["250 m", "25 m", "25000 m"]),
                    (f"A pencil is 180 mm long. How many cm?", "18 cm", ["1.8 cm", "180 cm", "1800 cm"]),
                    (f"A room is 4 m wide. How many cm?", "400 cm", ["40 cm", "4000 cm", "4 cm"]),
                    (f"A nail is 50 mm long. How many cm?", "5 cm", ["50 cm", "0.5 cm", "500 cm"]),
                    (f"The garden is 3000 m long. How many km?", "3 km", ["30 km", "300 km", "0.3 km"]),
                ]
                q_text, correct, wrong = random.choice(scenarios)
                explanation = f"Step 1: Convert using the correct factor. Answer: {correct}. ✓"
                
            else:  # mixed
                conversions = [
                    ("How many cm in 2.5 m?", "250 cm", ["25 cm", "2500 cm", "2.5 cm"]),
                    ("How many mm in 7 cm?", "70 mm", ["7 mm", "700 mm", "0.7 mm"]),
                    ("How many m in 450 cm?", "4.5 m", ["45 m", "0.45 m", "450 m"]),
                    ("How many km in 6000 m?", "6 km", ["60 km", "0.6 km", "600 km"]),
                    ("How many cm in 35 mm?", "3.5 cm", ["35 cm", "0.35 cm", "350 cm"]),
                    ("How many m in 8 km?", "8000 m", ["800 m", "80 m", "80000 m"]),
                ]
                q_text, correct, wrong = random.choice(conversions)
                explanation = f"Step 1: {correct}. ✓"
            
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
# LEVEL 5: Converting Mass (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Converting Mass Units"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['g_to_kg', 'kg_to_g', 'mixed', 'word'])
            
            if q_type == 'g_to_kg':
                g = random.choice([500, 1000, 1500, 2000, 2500, 3000, 4000, 5000])
                kg = g / 1000
                
                q_text = f"Convert {g} g to kilograms."
                correct = f"{kg} kg"
                wrong = [f"{g} kg", f"{kg * 10} kg", f"{g / 100} kg"]
                explanation = f"Step 1: {g} g ÷ 1000 = {kg} kg. ✓"
                
            elif q_type == 'kg_to_g':
                kg = random.choice([1, 1.5, 2, 2.5, 3, 4, 5])
                g = int(kg * 1000)
                
                q_text = f"Convert {kg} kg to grams."
                correct = f"{g} g"
                wrong = [f"{kg} g", f"{g // 10} g", f"{g * 10} g"]
                explanation = f"Step 1: {kg} kg × 1000 = {g} g. ✓"
                
            elif q_type == 'mixed':
                kg = random.randint(1, 5)
                g = random.choice([200, 250, 300, 500, 750])
                total_g = kg * 1000 + g
                
                q_text = f"How many grams is {kg} kg {g} g?"
                correct = f"{total_g} g"
                wrong = [f"{kg * 100 + g} g", f"{total_g + 500} g", f"{kg}{g} g"]
                explanation = f"Step 1: {kg} kg = {kg * 1000} g. Step 2: {kg * 1000} + {g} = {total_g} g. ✓"
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                kg = random.choice([2, 3, 5])
                g = kg * 1000
                
                scenarios = [
                    (f"{name} buys {kg} kg of apples. How many grams is that?", f"{g} g"),
                    (f"A recipe needs {g} g of flour. How many kg is that?", f"{kg} kg"),
                ]
                q_text, correct = random.choice(scenarios)
                wrong = [f"{kg} g" if "kg" in correct else f"{g} kg", f"{g // 10} g", f"{kg * 100} g"]
                explanation = f"Step 1: {kg} kg = {g} g. ✓"
            
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
# LEVEL 6: Converting Capacity (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Converting Capacity Units"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['ml_to_l', 'l_to_ml', 'mixed', 'word'])
            
            if q_type == 'ml_to_l':
                ml = random.choice([500, 1000, 1500, 2000, 2500, 3000, 4000, 5000])
                l = ml / 1000
                
                q_text = f"Convert {ml} ml to litres."
                correct = f"{l} l"
                wrong = [f"{ml} l", f"{l * 10} l", f"{ml / 100} l"]
                explanation = f"Step 1: {ml} ml ÷ 1000 = {l} l. ✓"
                
            elif q_type == 'l_to_ml':
                l = random.choice([1, 1.5, 2, 2.5, 3, 4, 5])
                ml = int(l * 1000)
                
                q_text = f"Convert {l} l to millilitres."
                correct = f"{ml} ml"
                wrong = [f"{l} ml", f"{ml // 10} ml", f"{ml * 10} ml"]
                explanation = f"Step 1: {l} l × 1000 = {ml} ml. ✓"
                
            elif q_type == 'mixed':
                l = random.randint(1, 4)
                ml = random.choice([200, 250, 300, 500, 750])
                total_ml = l * 1000 + ml
                
                q_text = f"How many ml is {l} l and {ml} ml?"
                correct = f"{total_ml} ml"
                wrong = [f"{l * 100 + ml} ml", f"{total_ml + 500} ml", f"{l}{ml} ml"]
                explanation = f"Step 1: {l} l = {l * 1000} ml. Step 2: {l * 1000} + {ml} = {total_ml} ml. ✓"
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                l = random.choice([2, 3, 5])
                ml = l * 1000
                
                scenarios = [
                    (f"{name} has {l} litres of juice. How many ml is that?", f"{ml} ml"),
                    (f"A container holds {ml} ml. How many litres is that?", f"{l} l"),
                ]
                q_text, correct = random.choice(scenarios)
                wrong = [f"{l} ml" if "ml" in correct else f"{ml} l", f"{ml // 10} ml", f"{l * 100} ml"]
                explanation = f"Step 1: {l} l = {ml} ml. ✓"
            
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
# LEVEL 7: Perimeter (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Calculating Perimeter"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['square', 'rectangle', 'triangle', 'word'])
            
            if q_type == 'square':
                side = random.randint(3, 15)
                perimeter = 4 * side
                
                q_text = f"Find the perimeter of a square with sides of {side} cm."
                correct = f"{perimeter} cm"
                wrong = [f"{side * side} cm", f"{side * 2} cm", f"{perimeter + side} cm"]
                explanation = f"Step 1: Perimeter = 4 × side = 4 × {side} = {perimeter} cm. ✓"
                
            elif q_type == 'rectangle':
                length = random.randint(5, 15)
                width = random.randint(3, length - 1)
                perimeter = 2 * (length + width)
                
                q_text = f"Find the perimeter of a rectangle with length {length} cm and width {width} cm."
                correct = f"{perimeter} cm"
                wrong = [f"{length * width} cm", f"{length + width} cm", f"{perimeter + length} cm"]
                explanation = f"Step 1: P = 2 × (l + w) = 2 × ({length} + {width}) = {perimeter} cm. ✓"
                
            elif q_type == 'triangle':
                a = random.randint(4, 10)
                b = random.randint(4, 10)
                c = random.randint(4, 10)
                perimeter = a + b + c
                
                q_text = f"Find the perimeter of a triangle with sides {a} cm, {b} cm, and {c} cm."
                correct = f"{perimeter} cm"
                wrong = [f"{a * b} cm", f"{a + b} cm", f"{perimeter + a} cm"]
                explanation = f"Step 1: P = {a} + {b} + {c} = {perimeter} cm. ✓"
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                length = random.randint(8, 20)
                width = random.randint(5, length - 2)
                perimeter = 2 * (length + width)
                
                q_text = f"{name}'s garden is {length} m long and {width} m wide. How much fencing is needed to go around it?"
                correct = f"{perimeter} m"
                wrong = [f"{length * width} m", f"{length + width} m", f"{perimeter * 2} m"]
                explanation = f"Step 1: Perimeter = 2 × ({length} + {width}) = {perimeter} m. ✓"
            
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
# LEVEL 8: Area (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Calculating Area"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['square', 'rectangle', 'word', 'units'])
            
            if q_type == 'square':
                side = random.randint(3, 12)
                area = side * side
                
                q_text = f"Find the area of a square with sides of {side} cm."
                correct = f"{area} cm²"
                wrong = [f"{side * 4} cm²", f"{side * 2} cm²", f"{area + side} cm²"]
                explanation = f"Step 1: Area = side² = {side}² = {area} cm². ✓"
                
            elif q_type == 'rectangle':
                length = random.randint(5, 15)
                width = random.randint(3, 10)
                area = length * width
                
                q_text = f"Find the area of a rectangle with length {length} cm and width {width} cm."
                correct = f"{area} cm²"
                wrong = [f"{2 * (length + width)} cm²", f"{length + width} cm²", f"{area + length} cm²"]
                explanation = f"Step 1: Area = l × w = {length} × {width} = {area} cm². ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                length = random.randint(5, 12)
                width = random.randint(4, 10)
                area = length * width
                
                q_text = f"{name}'s bedroom floor is {length} m by {width} m. What is the area?"
                correct = f"{area} m²"
                wrong = [f"{2 * (length + width)} m²", f"{length + width} m²", f"{area * 2} m²"]
                explanation = f"Step 1: Area = {length} × {width} = {area} m². ✓"
                
            else:  # units
                side = random.randint(5, 10)
                area = side * side
                
                q_text = f"A square has area {area} cm². What unit is used for area?"
                correct = "cm² (square centimetres)"
                wrong = ["cm (centimetres)", "cm³ (cubic centimetres)", "m (metres)"]
                explanation = f"Step 1: Area is measured in square units, so cm². ✓"
            
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
# LEVEL 9: Measurement Word Problems (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Measurement Word Problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            problem_type = random.randint(1, 4)
            name = random.choice(IRISH_NAMES)
            
            if problem_type == 1:
                # Length problem
                total = random.randint(100, 200)
                used_amount = random.randint(30, total - 20)
                remaining = total - used_amount
                
                q_text = f"{name} has {total} cm of ribbon. {used_amount} cm is used. How much is left?"
                correct = f"{remaining} cm"
                wrong = [f"{total} cm", f"{used_amount} cm", f"{remaining + 10} cm"]
                explanation = f"Step 1: {total} - {used_amount} = {remaining} cm left. ✓"
                
            elif problem_type == 2:
                # Mass problem
                each = random.choice([200, 250, 500])
                count = random.randint(3, 6)
                total = each * count
                
                q_text = f"Each apple weighs {each} g. How much do {count} apples weigh?"
                correct = f"{total} g"
                wrong = [f"{each} g", f"{total + each} g", f"{total // 2} g"]
                explanation = f"Step 1: {count} × {each} = {total} g. ✓"
                
            elif problem_type == 3:
                # Capacity problem
                bottle = random.choice([500, 750, 1000])
                cups = random.randint(3, 6)
                cup_size = bottle // cups
                
                q_text = f"A {bottle} ml bottle fills {cups} equal cups. How much in each cup?"
                correct = f"{cup_size} ml"
                wrong = [f"{bottle} ml", f"{cup_size * 2} ml", f"{cup_size + 50} ml"]
                explanation = f"Step 1: {bottle} ÷ {cups} = {cup_size} ml each. ✓"
                
            else:
                # Mixed conversion problem
                km = random.choice([2, 3, 5])
                extra_m = random.choice([200, 500, 800])
                total_m = km * 1000 + extra_m
                
                q_text = f"A walk is {km} km and {extra_m} m. What is the total in metres?"
                correct = f"{total_m} m"
                wrong = [f"{km + extra_m} m", f"{km * 100 + extra_m} m", f"{total_m + 1000} m"]
                explanation = f"Step 1: {km} km = {km * 1000} m. Step 2: {km * 1000} + {extra_m} = {total_m} m. ✓"
            
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
# LEVEL 10: Complex Conversions (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Complex Measurement Conversions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['multi_step', 'compare', 'add_mixed', 'subtract_mixed'])
            
            if q_type == 'multi_step':
                cm = random.choice([250, 350, 450, 550])
                m = cm / 100
                mm = cm * 10
                
                direction = random.choice(['to_mm', 'to_m'])
                if direction == 'to_mm':
                    q_text = f"Convert {cm} cm to mm."
                    correct = f"{mm} mm"
                    wrong = [f"{cm} mm", f"{mm // 10} mm", f"{mm + 100} mm"]
                else:
                    q_text = f"Convert {cm} cm to metres."
                    correct = f"{m} m"
                    wrong = [f"{cm} m", f"{m * 10} m", f"{cm / 10} m"]
                explanation = f"Step 1: {cm} cm = {correct}. ✓"
                
            elif q_type == 'compare':
                val1 = random.choice([1500, 2000, 2500])
                val2 = random.choice([1.2, 1.8, 2.3, 2.8])
                
                # Compare g to kg or ml to l
                unit_type = random.choice(['mass', 'capacity'])
                if unit_type == 'mass':
                    q_text = f"Which is heavier: {val1} g or {val2} kg?"
                    val2_g = val2 * 1000
                    correct = f"{val1} g" if val1 > val2_g else f"{val2} kg"
                    wrong = [f"{val1} g" if val1 <= val2_g else f"{val2} kg", "Same weight", "Cannot compare"]
                else:
                    q_text = f"Which holds more: {val1} ml or {val2} l?"
                    val2_ml = val2 * 1000
                    correct = f"{val1} ml" if val1 > val2_ml else f"{val2} l"
                    wrong = [f"{val1} ml" if val1 <= val2_ml else f"{val2} l", "Same capacity", "Cannot compare"]
                explanation = f"Step 1: Convert to same units. {correct} is more. ✓"
                
            elif q_type == 'add_mixed':
                unit_type = random.choice(['length', 'mass', 'capacity'])
                if unit_type == 'length':
                    m1 = random.randint(1, 3)
                    cm1 = random.choice([25, 50, 75])
                    m2 = random.randint(1, 3)
                    cm2 = random.choice([25, 50, 75])
                    total_cm = m1 * 100 + cm1 + m2 * 100 + cm2
                    total_m = total_cm // 100
                    rem_cm = total_cm % 100
                    
                    q_text = f"Add: {m1} m {cm1} cm + {m2} m {cm2} cm"
                    correct = f"{total_m} m {rem_cm} cm"
                    wrong = [f"{m1 + m2} m {cm1 + cm2} cm", f"{total_cm} cm", f"{total_m + 1} m"]
                elif unit_type == 'mass':
                    kg1 = random.randint(1, 3)
                    g1 = random.choice([250, 500, 750])
                    kg2 = random.randint(1, 3)
                    g2 = random.choice([250, 500, 750])
                    total_g = kg1 * 1000 + g1 + kg2 * 1000 + g2
                    total_kg = total_g // 1000
                    rem_g = total_g % 1000
                    
                    q_text = f"Add: {kg1} kg {g1} g + {kg2} kg {g2} g"
                    correct = f"{total_kg} kg {rem_g} g"
                    wrong = [f"{kg1 + kg2} kg {g1 + g2} g", f"{total_g} g", f"{total_kg + 1} kg"]
                else:
                    l1 = random.randint(1, 3)
                    ml1 = random.choice([250, 500, 750])
                    l2 = random.randint(1, 3)
                    ml2 = random.choice([250, 500, 750])
                    total_ml = l1 * 1000 + ml1 + l2 * 1000 + ml2
                    total_l = total_ml // 1000
                    rem_ml = total_ml % 1000
                    
                    q_text = f"Add: {l1} l {ml1} ml + {l2} l {ml2} ml"
                    correct = f"{total_l} l {rem_ml} ml"
                    wrong = [f"{l1 + l2} l {ml1 + ml2} ml", f"{total_ml} ml", f"{total_l + 1} l"]
                explanation = f"Step 1: Add and convert. Answer: {correct}. ✓"
                
            else:  # subtract_mixed
                m1 = random.randint(3, 6)
                cm1 = random.choice([50, 75])
                m2 = random.randint(1, 2)
                cm2 = random.choice([25, 30])
                
                total1 = m1 * 100 + cm1
                total2 = m2 * 100 + cm2
                diff = total1 - total2
                result_m = diff // 100
                result_cm = diff % 100
                
                q_text = f"Subtract: {m1} m {cm1} cm - {m2} m {cm2} cm"
                correct = f"{result_m} m {result_cm} cm"
                wrong = [f"{m1 - m2} m {cm1 - cm2} cm", f"{diff} cm", f"{result_m - 1} m {result_cm + 100} cm"]
                explanation = f"Step 1: Convert, subtract. Answer: {correct}. ✓"
            
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
# LEVEL 11: Multi-Step Problems (Advanced)
# ============================================================

def generate_level_11():
    """Level 11: Complex Multi-Step Measurement Problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            problem_type = random.randint(1, 4)
            name = random.choice(IRISH_NAMES)
            
            if problem_type == 1:
                # Area with conversion
                length_m = random.randint(4, 8)
                width_m = random.randint(3, 6)
                area = length_m * width_m
                
                q_text = f"A room is {length_m} m by {width_m} m. How many 1 m² tiles are needed to cover the floor?"
                correct = f"{area} tiles"
                wrong = [f"{2 * (length_m + width_m)} tiles", f"{length_m + width_m} tiles", f"{area * 2} tiles"]
                explanation = f"Step 1: Area = {length_m} × {width_m} = {area} m². Step 2: Need {area} tiles. ✓"
                
            elif problem_type == 2:
                # Total and parts
                total_l = random.choice([3, 4, 5])
                glasses = random.choice([6, 8, 10])
                ml_each = (total_l * 1000) // glasses
                
                q_text = f"{name} has {total_l} litres of juice. It fills {glasses} glasses equally. How much in each glass?"
                correct = f"{ml_each} ml"
                wrong = [f"{total_l * 1000} ml", f"{ml_each // 10} ml", f"{ml_each * 2} ml"]
                explanation = f"Step 1: {total_l} l = {total_l * 1000} ml. Step 2: {total_l * 1000} ÷ {glasses} = {ml_each} ml. ✓"
                
            elif problem_type == 3:
                # Perimeter with cost
                length = random.randint(8, 15)
                width = random.randint(5, 10)
                perimeter = 2 * (length + width)
                cost_per_m = random.choice([5, 8, 10])
                total_cost = perimeter * cost_per_m
                
                q_text = f"A {length} m × {width} m garden needs fencing at €{cost_per_m}/m. Total cost?"
                correct = f"€{total_cost}"
                wrong = [f"€{length * width * cost_per_m}", f"€{perimeter}", f"€{total_cost + cost_per_m}"]
                explanation = f"Step 1: P = 2 × ({length} + {width}) = {perimeter} m. Step 2: {perimeter} × €{cost_per_m} = €{total_cost}. ✓"
                
            else:
                # Journey with mixed units
                km = random.randint(2, 5)
                m = random.choice([200, 500, 800])
                total_m = km * 1000 + m
                
                q_text = f"{name} cycles {km} km {m} m to school and back. Total distance in metres?"
                total_both = total_m * 2
                correct = f"{total_both} m"
                wrong = [f"{total_m} m", f"{km * 2} km", f"{total_both + 1000} m"]
                explanation = f"Step 1: One way = {total_m} m. Step 2: Return = {total_m} × 2 = {total_both} m. ✓"
            
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
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
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
    print("VALIDATION - Measurement")
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
    print("AgentMath - Measurement Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Units of Length", generate_level_1),
        (2, "Units of Mass", generate_level_2),
        (3, "Units of Capacity", generate_level_3),
        (4, "Converting Length", generate_level_4),
        (5, "Converting Mass", generate_level_5),
        (6, "Converting Capacity", generate_level_6),
        (7, "Perimeter", generate_level_7),
        (8, "Area", generate_level_8),
        (9, "Word Problems", generate_level_9),
        (10, "Complex Conversions", generate_level_10),
        (11, "Multi-Step Problems", generate_level_11),
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
