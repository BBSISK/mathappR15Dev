#!/usr/bin/env python3
"""
AgentMath - Data & Charts Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Reading pictograms, bar charts, tally charts
  L4-6:   Developing - Interpreting data, comparing, simple statistics
  L7-9:   Proficient - Mean, mode, range, word problems
  L10-12: Advanced - Complex data analysis, multi-step problems

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'data_and_charts'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam'
]

COLORS = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']
PETS = ['Dogs', 'Cats', 'Fish', 'Rabbits', 'Birds', 'Hamsters']
SPORTS = ['Football', 'Hurling', 'Swimming', 'Tennis', 'Basketball', 'Running']
FRUITS = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
SUBJECTS = ['Maths', 'English', 'Irish', 'Science', 'History', 'Art']

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

def generate_bar_chart_svg(data, title=""):
    """Generate SVG bar chart"""
    max_val = max(data.values()) if data else 10
    bar_width = 40
    gap = 15
    height = 120
    width = len(data) * (bar_width + gap) + 60
    
    svg = f'''<svg viewBox="0 0 {width} {height + 40}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .bar {{ fill: #10b981; }}
        .axis {{ stroke: #374151; stroke-width: 2; }}
        .label {{ font-size: 9px; fill: #374151; text-anchor: middle; }}
        .value {{ font-size: 8px; fill: #1f2937; text-anchor: middle; }}
        .title {{ font-size: 10px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
    </style>'''
    
    if title:
        svg += f'<text x="{width // 2}" y="12" class="title">{title}</text>'
    
    # Y-axis
    svg += f'<line x1="40" y1="20" x2="40" y2="{height}" class="axis"/>'
    # X-axis
    svg += f'<line x1="40" y1="{height}" x2="{width - 10}" y2="{height}" class="axis"/>'
    
    x = 50
    for label, value in data.items():
        bar_height = (value / max_val) * 80 if max_val > 0 else 0
        y = height - bar_height
        
        svg += f'<rect x="{x}" y="{y}" width="{bar_width}" height="{bar_height}" class="bar"/>'
        svg += f'<text x="{x + bar_width // 2}" y="{y - 3}" class="value">{value}</text>'
        svg += f'<text x="{x + bar_width // 2}" y="{height + 12}" class="label">{label[:6]}</text>'
        
        x += bar_width + gap
    
    svg += '</svg>'
    return svg

def generate_pictogram_svg(data, symbol="●", key_value=2):
    """Generate SVG pictogram"""
    max_symbols = max(v // key_value for v in data.values()) if data else 5
    height = len(data) * 25 + 40
    width = max(200, max_symbols * 20 + 100)
    
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .label {{ font-size: 10px; fill: #374151; }}
        .symbol {{ font-size: 14px; fill: #10b981; }}
        .key {{ font-size: 9px; fill: #6b7280; }}
    </style>'''
    
    y = 20
    for label, value in data.items():
        num_symbols = value // key_value
        half = (value % key_value) > 0
        
        svg += f'<text x="5" y="{y}" class="label">{label[:8]}</text>'
        
        x = 70
        for _ in range(num_symbols):
            svg += f'<text x="{x}" y="{y}" class="symbol">{symbol}</text>'
            x += 18
        if half:
            svg += f'<text x="{x}" y="{y}" class="symbol" style="opacity:0.5">{symbol}</text>'
        
        y += 22
    
    svg += f'<text x="5" y="{y + 5}" class="key">Key: {symbol} = {key_value}</text>'
    svg += '</svg>'
    return svg

def generate_tally_svg(data):
    """Generate SVG tally chart"""
    height = len(data) * 30 + 30
    
    svg = f'''<svg viewBox="0 0 250 {height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .label {{ font-size: 10px; fill: #374151; }}
        .tally {{ font-size: 14px; fill: #1f2937; font-family: monospace; }}
        .total {{ font-size: 10px; fill: #10b981; font-weight: bold; }}
        .header {{ font-size: 9px; fill: #6b7280; font-weight: bold; }}
    </style>
    <text x="5" y="15" class="header">Item</text>
    <text x="80" y="15" class="header">Tally</text>
    <text x="200" y="15" class="header">Total</text>'''
    
    y = 35
    for label, value in data.items():
        # Create tally marks
        groups = value // 5
        remainder = value % 5
        tally = "卌 " * groups + "|" * remainder
        
        svg += f'<text x="5" y="{y}" class="label">{label[:8]}</text>'
        svg += f'<text x="80" y="{y}" class="tally">{tally}</text>'
        svg += f'<text x="210" y="{y}" class="total">{value}</text>'
        y += 25
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Reading Pictograms (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Reading Simple Pictograms"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            category = random.choice(['pets', 'colors', 'fruits'])
            if category == 'pets':
                items = random.sample(PETS, 4)
            elif category == 'colors':
                items = random.sample(COLORS, 4)
            else:
                items = random.sample(FRUITS, 4)
            
            key_value = random.choice([2, 5])
            data = {item: random.randint(1, 5) * key_value for item in items}
            
            q_type = random.choice(['count_one', 'most', 'total', 'difference'])
            
            if q_type == 'count_one':
                target = random.choice(items)
                answer = data[target]
                
                q_text = f"How many children chose {target}?"
                correct = str(answer)
                wrong = [str(answer + key_value), str(answer - key_value) if answer > key_value else str(answer + key_value * 2), str(answer // 2)]
                explanation = f"Step 1: Count symbols for {target}. Step 2: Each symbol = {key_value}. Answer: {answer}. ✓"
                
            elif q_type == 'most':
                max_item = max(data, key=data.get)
                
                q_text = f"Which is the most popular?"
                correct = max_item
                wrong = [i for i in items if i != max_item]
                explanation = f"Step 1: {max_item} has the most symbols = {data[max_item]}. ✓"
                
            elif q_type == 'total':
                total = sum(data.values())
                
                q_text = f"How many children were asked in total?"
                correct = str(total)
                wrong = [str(total + key_value), str(total - key_value), str(len(data))]
                explanation = f"Step 1: Add all values: {' + '.join(str(v) for v in data.values())} = {total}. ✓"
                
            else:  # difference
                sorted_items = sorted(data.items(), key=lambda x: x[1])
                highest = sorted_items[-1]
                lowest = sorted_items[0]
                diff = highest[1] - lowest[1]
                
                q_text = f"How many more chose {highest[0]} than {lowest[0]}?"
                correct = str(diff)
                wrong = [str(diff + key_value), str(highest[1]), str(lowest[1])]
                explanation = f"Step 1: {highest[0]} = {highest[1]}, {lowest[0]} = {lowest[1]}. Step 2: {highest[1]} - {lowest[1]} = {diff}. ✓"
            
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
                'image_svg': generate_pictogram_svg(data, "●", key_value),
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Reading Bar Charts (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Reading Simple Bar Charts"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            category = random.choice(['sports', 'pets', 'subjects'])
            if category == 'sports':
                items = random.sample(SPORTS, 4)
                context = "favourite sports"
            elif category == 'pets':
                items = random.sample(PETS, 4)
                context = "pets owned"
            else:
                items = random.sample(SUBJECTS, 4)
                context = "favourite subjects"
            
            data = {item: random.randint(3, 12) for item in items}
            
            q_type = random.choice(['read_value', 'most', 'least', 'compare'])
            
            if q_type == 'read_value':
                target = random.choice(items)
                answer = data[target]
                
                q_text = f"How many chose {target}?"
                correct = str(answer)
                wrong = [str(answer + 2), str(answer - 2) if answer > 2 else str(answer + 4), str(answer + 1)]
                explanation = f"Step 1: Read the bar for {target} = {answer}. ✓"
                
            elif q_type == 'most':
                max_item = max(data, key=data.get)
                
                q_text = f"Which {context.split()[-1]} is most popular?"
                correct = max_item
                wrong = [i for i in items if i != max_item]
                explanation = f"Step 1: {max_item} has the tallest bar = {data[max_item]}. ✓"
                
            elif q_type == 'least':
                min_item = min(data, key=data.get)
                
                q_text = f"Which {context.split()[-1]} is least popular?"
                correct = min_item
                wrong = [i for i in items if i != min_item]
                explanation = f"Step 1: {min_item} has the shortest bar = {data[min_item]}. ✓"
                
            else:  # compare
                item1, item2 = random.sample(items, 2)
                val1, val2 = data[item1], data[item2]
                
                q_text = f"How many more chose {item1 if val1 > val2 else item2} than {item2 if val1 > val2 else item1}?"
                correct = str(abs(val1 - val2))
                wrong = [str(abs(val1 - val2) + 1), str(max(val1, val2)), str(min(val1, val2))]
                explanation = f"Step 1: {item1} = {val1}, {item2} = {val2}. Step 2: Difference = {abs(val1 - val2)}. ✓"
            
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
                'image_svg': generate_bar_chart_svg(data, f"Favourite {context.split()[-1].title()}"),
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Tally Charts (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Reading Tally Charts"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    # Different categories for tally charts
    categories = [
        ('colors', COLORS),
        ('pets', PETS),
        ('sports', SPORTS),
        ('fruits', FRUITS),
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            cat_name, cat_items = random.choice(categories)
            items = random.sample(cat_items, min(4, len(cat_items)))
            data = {item: random.randint(3, 18) for item in items}
            
            q_type = random.choice(['count', 'total', 'most', 'least', 'tally_meaning', 'difference', 'combined', 'compare'])
            
            if q_type == 'count':
                target = random.choice(items)
                answer = data[target]
                
                q_text = f"How many chose {target}? (Use the tally chart)"
                correct = str(answer)
                wrong = [str(answer + 2), str(answer - 2) if answer > 2 else str(answer + 4), str(answer + 5)]
                explanation = f"Step 1: Count tally marks for {target}. Step 2: 卌 = 5. Answer: {answer}. ✓"
                
            elif q_type == 'total':
                total = sum(data.values())
                
                q_text = f"How many people were surveyed in total? (Add all tallies)"
                correct = str(total)
                wrong = [str(total + 5), str(total - 5) if total > 5 else str(total + 10), str(len(data))]
                explanation = f"Step 1: Add all tallies = {total}. ✓"
                
            elif q_type == 'most':
                max_item = max(data, key=data.get)
                
                q_text = f"Which {cat_name[:-1] if cat_name.endswith('s') else cat_name} was chosen most often?"
                correct = max_item
                wrong = [i for i in items if i != max_item]
                explanation = f"Step 1: {max_item} has the most tally marks = {data[max_item]}. ✓"
                
            elif q_type == 'least':
                min_item = min(data, key=data.get)
                
                q_text = f"Which {cat_name[:-1] if cat_name.endswith('s') else cat_name} was chosen least often?"
                correct = min_item
                wrong = [i for i in items if i != min_item]
                explanation = f"Step 1: {min_item} has the fewest tally marks = {data[min_item]}. ✓"
                
            elif q_type == 'tally_meaning':
                tally_questions = [
                    ("What does 卌 represent in a tally chart?", "5", ["4", "10", "1"]),
                    ("How many does |||| (4 lines) represent?", "4", ["5", "3", "6"]),
                    ("How many does 卌 卌 || represent?", "12", ["10", "11", "7"]),
                    ("How many does 卌 ||| represent?", "8", ["5", "3", "7"]),
                    ("How many does ||| represent?", "3", ["5", "4", "2"]),
                    ("Why do we cross every 5th tally mark?", "To make counting easier", ["To show 10", "To start a new row", "To mark the end"]),
                    ("How many does 卌 卌 卌 represent?", "15", ["12", "18", "20"]),
                ]
                q_text, correct, wrong = random.choice(tally_questions)
                explanation = f"Step 1: {correct}. ✓"
                
            elif q_type == 'difference':
                sorted_items = sorted(data.items(), key=lambda x: x[1])
                highest = sorted_items[-1]
                lowest = sorted_items[0]
                diff = highest[1] - lowest[1]
                
                q_text = f"How many more chose {highest[0]} than {lowest[0]}?"
                correct = str(diff)
                wrong = [str(diff + 2), str(highest[1]), str(lowest[1])]
                explanation = f"Step 1: {highest[0]} = {highest[1]}, {lowest[0]} = {lowest[1]}. Difference = {diff}. ✓"
                
            elif q_type == 'combined':
                item1, item2 = random.sample(items, 2)
                combined = data[item1] + data[item2]
                
                q_text = f"How many chose {item1} or {item2} combined?"
                correct = str(combined)
                wrong = [str(combined + 3), str(data[item1]), str(data[item2])]
                explanation = f"Step 1: {data[item1]} + {data[item2]} = {combined}. ✓"
                
            else:  # compare
                item1, item2 = random.sample(items, 2)
                val1, val2 = data[item1], data[item2]
                
                if val1 > val2:
                    q_text = f"Did more people choose {item1} or {item2}?"
                    correct = item1
                    wrong = [item2, "Same number", "Cannot tell"]
                else:
                    q_text = f"Did more people choose {item2} or {item1}?"
                    correct = item2
                    wrong = [item1, "Same number", "Cannot tell"]
                explanation = f"Step 1: {item1} = {val1}, {item2} = {val2}. {correct} is more. ✓"
            
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
                'image_svg': generate_tally_svg(data),
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Interpreting Data (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Interpreting Data from Charts"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            items = random.sample(SPORTS, 5)
            data = {item: random.randint(5, 20) for item in items}
            
            q_type = random.choice(['combined', 'fraction', 'double', 'above_below'])
            
            if q_type == 'combined':
                item1, item2 = random.sample(items, 2)
                combined = data[item1] + data[item2]
                
                q_text = f"How many chose {item1} or {item2} combined?"
                correct = str(combined)
                wrong = [str(combined + 3), str(combined - 3) if combined > 5 else str(combined + 6), str(data[item1])]
                explanation = f"Step 1: {item1} = {data[item1]}, {item2} = {data[item2]}. Step 2: {data[item1]} + {data[item2]} = {combined}. ✓"
                
            elif q_type == 'fraction':
                total = sum(data.values())
                target = random.choice(items)
                
                q_text = f"Out of {total} students, {data[target]} chose {target}. Is this more or less than half?"
                half = total / 2
                correct = "More than half" if data[target] > half else "Less than half" if data[target] < half else "Exactly half"
                wrong = ["More than half" if data[target] <= half else "Less than half", "Exactly half" if data[target] != total / 2 else "More than half", "Cannot tell"]
                explanation = f"Step 1: Half of {total} = {half}. Step 2: {data[target]} {'>' if data[target] > half else '<'} {half}. ✓"
                
            elif q_type == 'double':
                item1 = random.choice(items)
                double_val = data[item1] * 2
                
                q_text = f"If twice as many students chose {item1}, how many would that be?"
                correct = str(double_val)
                wrong = [str(double_val + 2), str(data[item1]), str(double_val - 2) if double_val > 4 else str(double_val + 4)]
                explanation = f"Step 1: {item1} = {data[item1]}. Step 2: Double = {data[item1]} × 2 = {double_val}. ✓"
                
            else:  # above_below
                threshold = random.choice([8, 10, 12])
                above = [item for item, val in data.items() if val > threshold]
                
                q_text = f"How many sports had more than {threshold} votes?"
                correct = str(len(above))
                wrong = [str(len(above) + 1), str(len(above) - 1) if len(above) > 0 else "0", str(5 - len(above))]
                explanation = f"Step 1: Count items with value > {threshold}. Answer: {len(above)}. ✓"
            
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
                'image_svg': generate_bar_chart_svg(data, "Favourite Sports"),
                'difficulty': 4,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Comparing Data (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Comparing Data Sets"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 50
    
    # Multiple categories to increase variety
    categories = [
        ('fruits', FRUITS, "Favourite Fruits"),
        ('pets', PETS, "Pets Owned"),
        ('sports', SPORTS, "Favourite Sports"),
        ('colors', COLORS, "Favourite Colors"),
        ('subjects', SUBJECTS, "Favourite Subjects"),
    ]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            cat_name, cat_items, chart_title = random.choice(categories)
            items = random.sample(cat_items, min(4, len(cat_items)))
            data = {item: random.randint(4, 18) for item in items}
            
            q_type = random.choice(['range', 'diff_extremes', 'order', 'middle', 'compare_two', 'total', 'above_value', 'below_value'])
            
            if q_type == 'range':
                max_val = max(data.values())
                min_val = min(data.values())
                range_val = max_val - min_val
                
                q_text = f"What is the range of the data? (highest - lowest)"
                correct = str(range_val)
                wrong = [str(range_val + 2), str(max_val), str(min_val)]
                explanation = f"Step 1: Highest = {max_val}, Lowest = {min_val}. Step 2: Range = {max_val} - {min_val} = {range_val}. ✓"
                
            elif q_type == 'diff_extremes':
                sorted_items = sorted(data.items(), key=lambda x: x[1])
                lowest_item, lowest_val = sorted_items[0]
                highest_item, highest_val = sorted_items[-1]
                
                q_text = f"How many more chose {highest_item} than {lowest_item}?"
                correct = str(highest_val - lowest_val)
                wrong = [str(highest_val - lowest_val + 2), str(highest_val), str(lowest_val)]
                explanation = f"Step 1: {highest_item} = {highest_val}, {lowest_item} = {lowest_val}. Difference = {highest_val - lowest_val}. ✓"
                
            elif q_type == 'order':
                sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
                order_str = ", ".join([item[0] for item in sorted_items])
                
                q_text = f"List the {cat_name} in order from most to least popular."
                correct = order_str
                wrong_order = list(sorted_items)
                random.shuffle(wrong_order)
                wrong = [", ".join([item[0] for item in wrong_order]),
                        ", ".join([item[0] for item in sorted_items[::-1]]),
                        ", ".join([items[0], items[1], items[2], items[3]])]
                explanation = f"Step 1: Order by value: {order_str}. ✓"
                
            elif q_type == 'middle':
                sorted_vals = sorted(data.values())
                if len(sorted_vals) % 2 == 0:
                    middle = (sorted_vals[1] + sorted_vals[2]) // 2
                else:
                    middle = sorted_vals[len(sorted_vals) // 2]
                
                q_text = f"What is the middle value when the data is ordered?"
                correct = str(middle)
                wrong = [str(middle + 1), str(sum(data.values())), str(max(data.values()))]
                explanation = f"Step 1: Order values. Step 2: Find middle = {middle}. ✓"
                
            elif q_type == 'compare_two':
                item1, item2 = random.sample(items, 2)
                val1, val2 = data[item1], data[item2]
                diff = abs(val1 - val2)
                
                q_text = f"What is the difference between {item1} ({val1}) and {item2} ({val2})?"
                correct = str(diff)
                wrong = [str(diff + 2), str(val1 + val2), str(max(val1, val2))]
                explanation = f"Step 1: |{val1} - {val2}| = {diff}. ✓"
                
            elif q_type == 'total':
                total = sum(data.values())
                
                q_text = f"What is the total of all values in the chart?"
                correct = str(total)
                wrong = [str(total + 5), str(total - 3) if total > 5 else str(total + 8), str(len(data))]
                explanation = f"Step 1: Add all values = {total}. ✓"
                
            elif q_type == 'above_value':
                threshold = random.choice([6, 8, 10, 12])
                above = [item for item, val in data.items() if val > threshold]
                
                q_text = f"How many {cat_name} had more than {threshold} votes?"
                correct = str(len(above))
                wrong = [str(len(above) + 1) if len(above) < len(items) else str(len(above) - 1), 
                        str(len(items) - len(above)), str(threshold)]
                explanation = f"Step 1: Count items with value > {threshold}. Answer: {len(above)}. ✓"
                
            else:  # below_value
                threshold = random.choice([8, 10, 12, 14])
                below = [item for item, val in data.items() if val < threshold]
                
                q_text = f"How many {cat_name} had fewer than {threshold} votes?"
                correct = str(len(below))
                wrong = [str(len(below) + 1) if len(below) < len(items) else str(len(below) - 1),
                        str(len(items) - len(below)), str(threshold)]
                explanation = f"Step 1: Count items with value < {threshold}. Answer: {len(below)}. ✓"
            
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
                'image_svg': generate_bar_chart_svg(data, chart_title),
                'difficulty': 5,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Mode (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Finding the Mode"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['find_mode', 'identify_mode', 'mode_meaning', 'data_set'])
            
            if q_type == 'find_mode':
                # Create data with a clear mode
                mode_val = random.randint(3, 8)
                data_list = [mode_val] * random.randint(3, 4)
                for _ in range(random.randint(3, 5)):
                    val = random.randint(1, 10)
                    if val != mode_val:
                        data_list.append(val)
                random.shuffle(data_list)
                
                q_text = f"Find the mode of: {', '.join(map(str, data_list))}"
                correct = str(mode_val)
                wrong = [str(mode_val + 1), str(mode_val - 1) if mode_val > 1 else str(mode_val + 2), str(sum(data_list) // len(data_list))]
                explanation = f"Step 1: Mode = most common value. Step 2: {mode_val} appears most often. ✓"
                image_svg = None
                
            elif q_type == 'identify_mode':
                items = random.sample(COLORS, 4)
                # Make one item clearly the mode
                data = {}
                mode_item = random.choice(items)
                for item in items:
                    if item == mode_item:
                        data[item] = random.randint(8, 12)
                    else:
                        data[item] = random.randint(3, 6)
                
                q_text = f"Which colour is the mode (most chosen)?"
                correct = mode_item
                wrong = [i for i in items if i != mode_item]
                explanation = f"Step 1: Mode = most common. Step 2: {mode_item} = {data[mode_item]} (highest). ✓"
                image_svg = generate_bar_chart_svg(data, "Favourite Colours")
                
            elif q_type == 'mode_meaning':
                q_text = f"What does 'mode' mean in statistics?"
                correct = "The value that appears most often"
                wrong = ["The middle value", "The average", "The difference between highest and lowest"]
                explanation = f"Step 1: Mode = most frequent/common value. ✓"
                image_svg = None
                
            else:  # data_set
                # Simple number set
                numbers = [random.randint(1, 6) for _ in range(7)]
                mode_val = max(set(numbers), key=numbers.count)
                
                q_text = f"What is the mode of the dice rolls: {', '.join(map(str, numbers))}?"
                correct = str(mode_val)
                wrong = [str(mode_val + 1) if mode_val < 6 else str(mode_val - 1), str(sum(numbers) // len(numbers)), str(max(numbers) if max(numbers) != mode_val else min(numbers))]
                explanation = f"Step 1: Count each value. Step 2: {mode_val} appears most often. ✓"
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
# LEVEL 7: Mean (Average) (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Calculating the Mean"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['calculate', 'context', 'find_missing', 'meaning'])
            
            if q_type == 'calculate':
                # Create data that divides evenly
                count = random.choice([4, 5, 6])
                mean = random.randint(5, 15)
                total = mean * count
                
                # Generate numbers that sum to total
                data_list = []
                remaining = total
                for i in range(count - 1):
                    val = random.randint(max(1, mean - 5), min(remaining - (count - i - 1), mean + 5))
                    data_list.append(val)
                    remaining -= val
                data_list.append(remaining)
                random.shuffle(data_list)
                
                q_text = f"Find the mean of: {', '.join(map(str, data_list))}"
                correct = str(mean)
                wrong = [str(mean + 1), str(mean - 1) if mean > 1 else str(mean + 2), str(total)]
                explanation = f"Step 1: Sum = {total}. Step 2: Mean = {total} ÷ {count} = {mean}. ✓"
                
            elif q_type == 'context':
                name = random.choice(IRISH_NAMES)
                count = random.choice([4, 5])
                mean = random.randint(6, 10)
                total = mean * count
                
                data_list = []
                remaining = total
                for i in range(count - 1):
                    val = random.randint(max(1, mean - 3), min(remaining - (count - i - 1), mean + 3))
                    data_list.append(val)
                    remaining -= val
                data_list.append(remaining)
                
                q_text = f"{name}'s test scores are {', '.join(map(str, data_list))}. What is {name}'s average score?"
                correct = str(mean)
                wrong = [str(mean + 1), str(mean - 1), str(max(data_list))]
                explanation = f"Step 1: Total = {total}. Step 2: Average = {total} ÷ {count} = {mean}. ✓"
                
            elif q_type == 'find_missing':
                count = 4
                mean = random.randint(5, 10)
                total = mean * count
                
                known_vals = [random.randint(mean - 2, mean + 2) for _ in range(count - 1)]
                known_sum = sum(known_vals)
                missing = total - known_sum
                
                q_text = f"The mean of 4 numbers is {mean}. Three numbers are {', '.join(map(str, known_vals))}. What is the fourth?"
                correct = str(missing)
                wrong = [str(missing + 1), str(mean), str(missing - 1) if missing > 1 else str(missing + 2)]
                explanation = f"Step 1: Total must be {mean} × 4 = {total}. Step 2: {total} - {known_sum} = {missing}. ✓"
                
            else:  # meaning
                q_text = f"What does 'mean' (average) tell us about a set of numbers?"
                correct = "The typical or central value"
                wrong = ["The highest value", "The most common value", "The middle value when ordered"]
                explanation = f"Step 1: Mean = sum ÷ count = typical value of the data. ✓"
            
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
# LEVEL 8: Range (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Calculating and Using Range"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['calculate', 'context', 'meaning', 'compare_sets'])
            
            if q_type == 'calculate':
                data_list = [random.randint(2, 20) for _ in range(5)]
                max_val = max(data_list)
                min_val = min(data_list)
                range_val = max_val - min_val
                
                q_text = f"Find the range of: {', '.join(map(str, data_list))}"
                correct = str(range_val)
                wrong = [str(range_val + 2), str(max_val), str(min_val)]
                explanation = f"Step 1: Highest = {max_val}, Lowest = {min_val}. Step 2: Range = {max_val} - {min_val} = {range_val}. ✓"
                
            elif q_type == 'context':
                name = random.choice(IRISH_NAMES)
                temps = [random.randint(10, 25) for _ in range(5)]
                max_temp = max(temps)
                min_temp = min(temps)
                range_temp = max_temp - min_temp
                
                q_text = f"Temperature readings: {', '.join(map(str, temps))}°C. What is the range?"
                correct = f"{range_temp}°C"
                wrong = [f"{range_temp + 2}°C", f"{max_temp}°C", f"{min_temp}°C"]
                explanation = f"Step 1: Highest = {max_temp}°C, Lowest = {min_temp}°C. Step 2: Range = {range_temp}°C. ✓"
                
            elif q_type == 'meaning':
                q_text = f"What does 'range' tell us about a set of data?"
                correct = "How spread out the data is"
                wrong = ["The average value", "The most common value", "The total of all values"]
                explanation = f"Step 1: Range = highest - lowest = spread of data. ✓"
                
            else:  # compare_sets
                set1 = [random.randint(5, 15) for _ in range(4)]
                set2 = [random.randint(3, 20) for _ in range(4)]
                range1 = max(set1) - min(set1)
                range2 = max(set2) - min(set2)
                
                q_text = f"Set A: {', '.join(map(str, set1))}. Set B: {', '.join(map(str, set2))}. Which has the larger range?"
                if range1 > range2:
                    correct = f"Set A (range = {range1})"
                elif range2 > range1:
                    correct = f"Set B (range = {range2})"
                else:
                    correct = f"Same range ({range1})"
                wrong = [f"Set A (range = {range1})" if range1 <= range2 else f"Set B (range = {range2})",
                        f"Same range" if range1 != range2 else f"Set A",
                        f"Cannot tell"]
                explanation = f"Step 1: Range A = {range1}, Range B = {range2}. {correct}. ✓"
            
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
# LEVEL 9: Data Word Problems (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Data and Statistics Word Problems"""
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
                # Survey interpretation
                total = random.choice([30, 40, 50])
                frac = random.choice([(1, 2), (1, 4), (1, 5)])
                chosen = total * frac[0] // frac[1]
                
                q_text = f"In a survey of {total} students, {frac[0]}/{frac[1]} chose pizza as favourite food. How many chose pizza?"
                correct = str(chosen)
                wrong = [str(chosen + 5), str(total), str(chosen - 5) if chosen > 5 else str(chosen + 10)]
                explanation = f"Step 1: {frac[0]}/{frac[1]} of {total} = {total} × {frac[0]} ÷ {frac[1]} = {chosen}. ✓"
                
            elif problem_type == 2:
                # Combined statistics
                class_sizes = [random.randint(20, 30) for _ in range(3)]
                total = sum(class_sizes)
                
                q_text = f"Three classes have {class_sizes[0]}, {class_sizes[1]}, and {class_sizes[2]} students. What is the total?"
                correct = str(total)
                wrong = [str(total + 5), str(total // 3), str(max(class_sizes))]
                explanation = f"Step 1: {class_sizes[0]} + {class_sizes[1]} + {class_sizes[2]} = {total}. ✓"
                
            elif problem_type == 3:
                # Average required
                scores = [random.randint(6, 10) for _ in range(4)]
                current_avg = sum(scores) // len(scores)
                target_avg = current_avg + 1
                needed_total = target_avg * 5
                needed = needed_total - sum(scores)
                
                q_text = f"{name}'s scores are {', '.join(map(str, scores))}. What score is needed in the 5th test to average {target_avg}?"
                correct = str(needed)
                wrong = [str(target_avg), str(needed + 1), str(current_avg)]
                explanation = f"Step 1: Need total = {target_avg} × 5 = {needed_total}. Step 2: {needed_total} - {sum(scores)} = {needed}. ✓"
                
            else:
                # Percentage from data
                total = random.choice([20, 25, 40, 50])
                value = random.choice([5, 10, 20])
                while value > total:
                    value = random.choice([5, 10, 20])
                pct = (value * 100) // total
                
                q_text = f"Out of {total} students, {value} walk to school. What percentage is this?"
                correct = f"{pct}%"
                wrong = [f"{pct + 10}%", f"{value}%", f"{100 - pct}%"]
                explanation = f"Step 1: {value}/{total} × 100 = {pct}%. ✓"
            
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
# LEVEL 10: Complex Data Analysis (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Complex Data Analysis"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['all_stats', 'interpret', 'compare', 'predict'])
            
            if q_type == 'all_stats':
                # Give data, ask for specific stat
                count = 5
                mean = random.randint(6, 12)
                data_list = [mean - 2, mean - 1, mean, mean + 1, mean + 2]
                random.shuffle(data_list)
                
                stat = random.choice(['mean', 'mode', 'range'])
                if stat == 'mean':
                    answer = mean
                    explanation_text = f"Sum = {sum(data_list)}, Count = {count}. Mean = {answer}."
                elif stat == 'mode':
                    # Each value appears once, so no mode - adjust
                    mode_val = random.choice(data_list)
                    data_list.append(mode_val)
                    answer = mode_val
                    explanation_text = f"{mode_val} appears most often = mode."
                else:
                    answer = max(data_list) - min(data_list)
                    explanation_text = f"Range = {max(data_list)} - {min(data_list)} = {answer}."
                
                q_text = f"Data: {', '.join(map(str, data_list))}. What is the {stat}?"
                correct = str(answer)
                wrong = [str(answer + 1), str(answer - 1) if answer > 1 else str(answer + 2), str(sum(data_list))]
                explanation = f"Step 1: {explanation_text} ✓"
                
            elif q_type == 'interpret':
                items = random.sample(SPORTS, 4)
                data = {item: random.randint(5, 20) for item in items}
                total = sum(data.values())
                
                # Ask about a specific proportion
                target = random.choice(items)
                pct = (data[target] * 100) // total
                
                q_text = f"Total surveyed: {total}. {target} chosen by {data[target]}. What percentage?"
                correct = f"About {pct}%"
                wrong = [f"About {pct + 10}%", f"{data[target]}%", f"About {100 - pct}%"]
                explanation = f"Step 1: {data[target]}/{total} × 100 ≈ {pct}%. ✓"
                
            elif q_type == 'compare':
                # Compare two groups
                group1 = [random.randint(5, 10) for _ in range(4)]
                group2 = [random.randint(6, 12) for _ in range(4)]
                mean1 = sum(group1) // len(group1)
                mean2 = sum(group2) // len(group2)
                
                q_text = f"Class A scores: {', '.join(map(str, group1))}. Class B scores: {', '.join(map(str, group2))}. Which class has a higher average?"
                if mean1 > mean2:
                    correct = f"Class A (average {mean1})"
                elif mean2 > mean1:
                    correct = f"Class B (average {mean2})"
                else:
                    correct = f"Same average ({mean1})"
                wrong = [f"Class A (average {mean1})" if mean1 <= mean2 else f"Class B (average {mean2})",
                        "Same average" if mean1 != mean2 else "Class A",
                        f"Cannot compare"]
                explanation = f"Step 1: Mean A = {mean1}, Mean B = {mean2}. {correct}. ✓"
                
            else:  # predict
                # Simple trend
                values = [10, 15, 20, 25]
                next_val = 30
                
                q_text = f"Values are increasing: {', '.join(map(str, values))}. What is the likely next value?"
                correct = str(next_val)
                wrong = [str(next_val + 5), str(values[-1]), str(next_val - 5)]
                explanation = f"Step 1: Pattern increases by 5. Step 2: Next = {values[-1]} + 5 = {next_val}. ✓"
            
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
# LEVEL 11: Multi-Step Data Problems (Advanced)
# ============================================================

def generate_level_11():
    """Level 11: Multi-Step Data Problems"""
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
                # Combined mean
                group1 = [random.randint(5, 10) for _ in range(3)]
                group2 = [random.randint(6, 11) for _ in range(3)]
                combined = group1 + group2
                mean = sum(combined) // len(combined)
                
                q_text = f"Group A: {', '.join(map(str, group1))}. Group B: {', '.join(map(str, group2))}. What is the mean of all 6 values?"
                correct = str(mean)
                wrong = [str(mean + 1), str(sum(group1) // 3), str(sum(group2) // 3)]
                explanation = f"Step 1: Total = {sum(combined)}. Step 2: Mean = {sum(combined)} ÷ 6 = {mean}. ✓"
                
            elif problem_type == 2:
                # Effect of adding a value
                original = [random.randint(5, 10) for _ in range(4)]
                original_mean = sum(original) // len(original)
                new_val = original_mean + random.choice([3, 4, 5])
                new_mean = (sum(original) + new_val) // 5
                
                q_text = f"Data: {', '.join(map(str, original))} (mean = {original_mean}). If we add {new_val}, will the mean increase, decrease, or stay the same?"
                correct = "Increase" if new_val > original_mean else "Decrease" if new_val < original_mean else "Stay the same"
                wrong = ["Decrease" if new_val >= original_mean else "Increase", "Stay the same" if new_val != original_mean else "Increase", "Cannot tell"]
                explanation = f"Step 1: {new_val} > {original_mean}, so mean increases. ✓"
                
            elif problem_type == 3:
                # Working backwards
                count = 5
                mean = random.randint(8, 12)
                total = mean * count
                
                known_sum = random.randint(total - 15, total - 8)
                unknown = total - known_sum
                
                q_text = f"The mean of 5 numbers is {mean}. Four numbers total {known_sum}. What is the fifth number?"
                correct = str(unknown)
                wrong = [str(unknown + 2), str(mean), str(total)]
                explanation = f"Step 1: Total = {mean} × 5 = {total}. Step 2: Fifth number = {total} - {known_sum} = {unknown}. ✓"
                
            else:
                # Percentage change
                old_val = random.choice([20, 25, 40, 50])
                new_val = old_val + random.choice([5, 10, -5, -10])
                change = abs(new_val - old_val)
                pct_change = (change * 100) // old_val
                direction = "increase" if new_val > old_val else "decrease"
                
                q_text = f"Sales went from {old_val} to {new_val}. What was the percentage {direction}?"
                correct = f"{pct_change}%"
                wrong = [f"{pct_change + 10}%", f"{change}%", f"{100 - pct_change}%"]
                explanation = f"Step 1: Change = {change}. Step 2: {change}/{old_val} × 100 = {pct_change}%. ✓"
            
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
    print("VALIDATION - Data & Charts")
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
    print("AgentMath - Data & Charts Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Pictograms", generate_level_1),
        (2, "Bar Charts", generate_level_2),
        (3, "Tally Charts", generate_level_3),
        (4, "Interpreting Data", generate_level_4),
        (5, "Comparing Data", generate_level_5),
        (6, "Mode", generate_level_6),
        (7, "Mean (Average)", generate_level_7),
        (8, "Range", generate_level_8),
        (9, "Word Problems", generate_level_9),
        (10, "Complex Analysis", generate_level_10),
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
