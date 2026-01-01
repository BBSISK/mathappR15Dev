#!/usr/bin/env python3
"""
AgentMath - Money Skills Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned (Euro currency)

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Coin recognition, counting coins, simple totals
  L4-6:   Developing - Adding money, giving change, rounding
  L7-9:   Proficient - Shopping problems, discounts, budgeting
  L10-12: Advanced - Multi-step problems, best value, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'money_skills'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam'
]

# Euro coins and notes
COINS = [1, 2, 5, 10, 20, 50]  # cents
EURO_COINS = [1, 2]  # euros
NOTES = [5, 10, 20, 50]  # euros

SHOP_ITEMS = {
    'apple': (0.45, 0.75),
    'banana': (0.30, 0.50),
    'orange': (0.50, 0.80),
    'bread': (1.50, 2.50),
    'milk': (1.20, 1.80),
    'juice': (1.50, 2.50),
    'crisps': (0.80, 1.50),
    'chocolate': (0.60, 1.20),
    'pencil': (0.30, 0.60),
    'notebook': (1.50, 3.00),
    'ruler': (0.80, 1.50),
    'eraser': (0.40, 0.80),
    'comic': (2.50, 4.00),
    'magazine': (3.00, 5.00),
    'toy car': (3.00, 6.00),
    'stickers': (1.00, 2.50),
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
        options.append(f"€{fallback_idx}.00")
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    return options, correct_idx

def format_euro(cents):
    """Format cents as euro string"""
    if cents >= 100:
        euros = cents // 100
        remaining_cents = cents % 100
        if remaining_cents == 0:
            return f"€{euros}"
        else:
            return f"€{euros}.{remaining_cents:02d}"
    else:
        return f"{cents}c"

def format_euro_decimal(amount):
    """Format decimal euro amount"""
    if amount == int(amount):
        return f"€{int(amount)}"
    else:
        return f"€{amount:.2f}"

def generate_coins_svg(coins_list):
    """Generate SVG showing coins"""
    svg = f'''<svg viewBox="0 0 300 80" xmlns="http://www.w3.org/2000/svg">
    <style>
        .coin {{ stroke: #d4a356; stroke-width: 2; }}
        .cent {{ fill: #cd7f32; }}
        .euro {{ fill: #c0c0c0; }}
        .label {{ font-size: 10px; fill: #1f2937; text-anchor: middle; dominant-baseline: middle; font-weight: bold; }}
    </style>'''
    
    x = 25
    for coin in coins_list[:8]:  # Max 8 coins shown
        if coin >= 100:
            # Euro coin
            svg += f'<circle cx="{x}" cy="40" r="18" class="coin euro"/>'
            svg += f'<text x="{x}" y="40" class="label">€{coin // 100}</text>'
        else:
            # Cent coin
            radius = 12 if coin < 10 else 15
            svg += f'<circle cx="{x}" cy="40" r="{radius}" class="coin cent"/>'
            svg += f'<text x="{x}" y="40" class="label">{coin}c</text>'
        x += 35
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Recognising Coins (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: Recognising Euro Coins"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    all_coins = [(1, "1 cent"), (2, "2 cent"), (5, "5 cent"), (10, "10 cent"),
                 (20, "20 cent"), (50, "50 cent"), (100, "€1"), (200, "€2")]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['identify', 'value', 'compare', 'count'])
            
            if q_type == 'identify':
                coin_val, coin_name = random.choice(all_coins)
                
                q_text = f"What is the value of this coin?"
                correct = coin_name
                other_coins = [c[1] for c in all_coins if c[1] != coin_name]
                wrong = random.sample(other_coins, 3)
                explanation = f"Step 1: This coin is worth {coin_name}. ✓"
                image_svg = generate_coins_svg([coin_val])
                
            elif q_type == 'value':
                coin_val, coin_name = random.choice(all_coins)
                
                q_text = f"How many cent is a {coin_name} coin worth?"
                if coin_val >= 100:
                    correct = f"{coin_val} cent"
                else:
                    correct = f"{coin_val} cent"
                wrong = [f"{coin_val + 5} cent", f"{coin_val - 5} cent" if coin_val > 5 else "3 cent", f"{coin_val * 2} cent"]
                explanation = f"Step 1: A {coin_name} coin is worth {coin_val} cent. ✓"
                image_svg = None
                
            elif q_type == 'compare':
                coin1_val, coin1_name = random.choice(all_coins[:6])  # Cents only
                coin2_val, coin2_name = random.choice(all_coins[:6])
                while coin1_val == coin2_val:
                    coin2_val, coin2_name = random.choice(all_coins[:6])
                
                bigger = coin1_name if coin1_val > coin2_val else coin2_name
                q_text = f"Which is worth more: {coin1_name} or {coin2_name}?"
                correct = bigger
                wrong = [coin1_name if bigger == coin2_name else coin2_name, "Same value", "Cannot tell"]
                explanation = f"Step 1: {coin1_name} = {coin1_val}c, {coin2_name} = {coin2_val}c. Step 2: {bigger} is worth more. ✓"
                image_svg = None
                
            else:  # count
                coin_val, coin_name = random.choice(all_coins[:4])  # Smaller coins
                count = random.randint(2, 5)
                total = coin_val * count
                
                q_text = f"How much is {count} × {coin_name}?"
                correct = format_euro(total)
                wrong = [format_euro(total + coin_val), format_euro(total - coin_val), format_euro(coin_val)]
                explanation = f"Step 1: {count} × {coin_val}c = {total}c = {correct}. ✓"
                image_svg = generate_coins_svg([coin_val] * count)
            
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
# LEVEL 2: Counting Coins (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Counting Mixed Coins"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['count_mixed', 'make_amount', 'euro_cent', 'add_coins', 'word', 'total'])
            
            if q_type == 'count_mixed':
                # Mix of coins
                coins = []
                coin_options = [5, 10, 20, 50, 100, 200]
                num_coins = random.randint(3, 5)
                for _ in range(num_coins):
                    coins.append(random.choice(coin_options))
                total = sum(coins)
                
                coins_str = " + ".join([format_euro(c) for c in sorted(coins, reverse=True)])
                q_text = f"Count these coins: {coins_str}"
                correct = format_euro(total)
                wrong = [format_euro(total + 20), format_euro(total - 20) if total > 50 else format_euro(total + 50), format_euro(total + 50)]
                explanation = f"Step 1: {coins_str} = {correct}. ✓"
                image_svg = generate_coins_svg(coins)
                
            elif q_type == 'make_amount':
                target = random.choice([30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250])
                
                q_text = f"Which coins could make {format_euro(target)}?"
                if target == 30:
                    correct = "20c + 10c"
                    wrong = ["20c + 20c", "10c + 10c", "50c"]
                elif target == 40:
                    correct = "20c + 20c"
                    wrong = ["50c", "20c + 10c", "10c + 10c"]
                elif target == 50:
                    correct = "50c coin"
                    wrong = ["20c + 20c", "10c + 20c", "€1"]
                elif target == 60:
                    correct = "50c + 10c"
                    wrong = ["50c + 20c", "20c + 20c + 20c", "€1"]
                elif target == 70:
                    correct = "50c + 20c"
                    wrong = ["50c + 10c", "20c + 20c + 20c", "€1"]
                elif target == 80:
                    correct = "50c + 20c + 10c"
                    wrong = ["50c + 20c", "€1", "20c + 20c + 20c"]
                elif target == 90:
                    correct = "50c + 20c + 20c"
                    wrong = ["50c + 20c + 10c", "€1", "50c + 50c"]
                elif target == 100:
                    correct = "€1 coin"
                    wrong = ["50c + 20c", "€2", "50c"]
                elif target == 150:
                    correct = "€1 + 50c"
                    wrong = ["€1 + 20c", "€2", "50c + 50c + 50c"]
                elif target == 200:
                    correct = "€2 coin"
                    wrong = ["€1 + 50c", "50c + 50c", "€1"]
                else:  # 250
                    correct = "€2 + 50c"
                    wrong = ["€2 + 20c", "€1 + €1", "€2"]
                
                explanation = f"Step 1: {format_euro(target)} can be made with {correct}. ✓"
                image_svg = None
                
            elif q_type == 'euro_cent':
                euros = random.randint(1, 9)
                cents = random.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])
                total_cents = euros * 100 + cents
                
                q_text = f"How much is €{euros} and {cents}c altogether?"
                correct = format_euro(total_cents)
                wrong = [f"€{euros}", f"€{euros + 1}", format_euro(total_cents + 50)]
                explanation = f"Step 1: €{euros} + {cents}c = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'add_coins':
                coin1 = random.choice([50, 100, 200])
                coin2 = random.choice([10, 20, 50])
                coin3 = random.choice([5, 10, 20])
                total = coin1 + coin2 + coin3
                
                c1 = format_euro(coin1)
                c2 = format_euro(coin2)
                c3 = format_euro(coin3)
                
                q_text = f"Add: {c1} + {c2} + {c3}"
                correct = format_euro(total)
                wrong = [format_euro(total + 10), format_euro(total - 10) if total > 50 else format_euro(total + 50), format_euro(coin1 + coin2)]
                explanation = f"Step 1: {c1} + {c2} + {c3} = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                coin1 = random.choice([100, 200])
                coin2 = random.choice([20, 50])
                total = coin1 + coin2
                
                c1 = "€1" if coin1 == 100 else "€2"
                c2 = f"{coin2}c"
                
                q_text = f"{name} has a {c1} coin and a {c2} coin. How much altogether?"
                correct = format_euro(total)
                wrong = [format_euro(total + 50), format_euro(total - 20) if total > 100 else format_euro(total + 100), c1]
                explanation = f"Step 1: {c1} + {c2} = {correct}. ✓"
                image_svg = None
                
            else:  # total
                num_euro = random.randint(1, 3)
                num_50c = random.randint(0, 2)
                num_20c = random.randint(0, 3)
                total = num_euro * 100 + num_50c * 50 + num_20c * 20
                
                parts = []
                if num_euro > 0:
                    parts.append(f"{num_euro} × €1")
                if num_50c > 0:
                    parts.append(f"{num_50c} × 50c")
                if num_20c > 0:
                    parts.append(f"{num_20c} × 20c")
                
                q_text = f"Total of {', '.join(parts)}?"
                correct = format_euro(total)
                wrong = [format_euro(total + 50), format_euro(total - 20) if total > 100 else format_euro(total + 100), format_euro(num_euro * 100)]
                explanation = f"Step 1: {' + '.join(parts)} = {correct}. ✓"
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
# LEVEL 3: Simple Totals (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Simple Shopping Totals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            q_type = random.choice(['two_items', 'same_items', 'word'])
            
            if q_type == 'two_items':
                item1 = random.choice(list(SHOP_ITEMS.keys()))
                item2 = random.choice(list(SHOP_ITEMS.keys()))
                while item1 == item2:
                    item2 = random.choice(list(SHOP_ITEMS.keys()))
                
                price1 = round(random.uniform(*SHOP_ITEMS[item1]), 2)
                price2 = round(random.uniform(*SHOP_ITEMS[item2]), 2)
                total = round(price1 + price2, 2)
                
                q_text = f"An {item1} costs {format_euro_decimal(price1)} and a {item2} costs {format_euro_decimal(price2)}. What is the total?"
                correct = format_euro_decimal(total)
                wrong = [format_euro_decimal(total + 0.50), format_euro_decimal(total - 0.50), format_euro_decimal(price1)]
                explanation = f"Step 1: {format_euro_decimal(price1)} + {format_euro_decimal(price2)} = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'same_items':
                item = random.choice(list(SHOP_ITEMS.keys()))
                price = round(random.uniform(*SHOP_ITEMS[item]), 2)
                count = random.randint(2, 4)
                total = round(price * count, 2)
                
                q_text = f"{count} {item}s cost {format_euro_decimal(price)} each. What is the total?"
                correct = format_euro_decimal(total)
                wrong = [format_euro_decimal(total + price), format_euro_decimal(price), format_euro_decimal(total - price)]
                explanation = f"Step 1: {count} × {format_euro_decimal(price)} = {correct}. ✓"
                image_svg = None
                
            else:  # word
                price1 = round(random.uniform(1.00, 3.00), 2)
                price2 = round(random.uniform(0.50, 2.00), 2)
                total = round(price1 + price2, 2)
                
                q_text = f"{name} buys a snack for {format_euro_decimal(price1)} and a drink for {format_euro_decimal(price2)}. How much altogether?"
                correct = format_euro_decimal(total)
                wrong = [format_euro_decimal(total + 1), format_euro_decimal(abs(price1 - price2)), format_euro_decimal(price1)]
                explanation = f"Step 1: {format_euro_decimal(price1)} + {format_euro_decimal(price2)} = {correct}. ✓"
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
# LEVEL 4: Adding Money (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Adding Money Amounts"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            q_type = random.choice(['add_two', 'add_three', 'total'])
            
            if q_type == 'add_two':
                amount1 = round(random.uniform(2.00, 10.00), 2)
                amount2 = round(random.uniform(1.50, 8.00), 2)
                total = round(amount1 + amount2, 2)
                
                q_text = f"What is {format_euro_decimal(amount1)} + {format_euro_decimal(amount2)}?"
                correct = format_euro_decimal(total)
                wrong = [format_euro_decimal(total + 1), format_euro_decimal(total - 1), format_euro_decimal(amount1)]
                explanation = f"Step 1: {format_euro_decimal(amount1)} + {format_euro_decimal(amount2)} = {correct}. ✓"
                
            elif q_type == 'add_three':
                amounts = [round(random.uniform(1.00, 5.00), 2) for _ in range(3)]
                total = round(sum(amounts), 2)
                
                q_text = f"Add: {format_euro_decimal(amounts[0])} + {format_euro_decimal(amounts[1])} + {format_euro_decimal(amounts[2])}"
                correct = format_euro_decimal(total)
                wrong = [format_euro_decimal(total + 1), format_euro_decimal(total - 0.50), format_euro_decimal(amounts[0] + amounts[1])]
                explanation = f"Step 1: Add all amounts = {correct}. ✓"
                
            else:  # total
                items = random.sample(list(SHOP_ITEMS.keys()), 3)
                prices = [round(random.uniform(*SHOP_ITEMS[item]), 2) for item in items]
                total = round(sum(prices), 2)
                
                q_text = f"{name} buys: {items[0]} ({format_euro_decimal(prices[0])}), {items[1]} ({format_euro_decimal(prices[1])}), {items[2]} ({format_euro_decimal(prices[2])}). Total cost?"
                correct = format_euro_decimal(total)
                wrong = [format_euro_decimal(total + 1), format_euro_decimal(total - 0.50), format_euro_decimal(prices[0] + prices[1])]
                explanation = f"Step 1: Add all prices: {correct}. ✓"
            
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
# LEVEL 5: Giving Change (Developing)
# ============================================================

def generate_level_5():
    """Level 5: Calculating Change"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            q_type = random.choice(['from_note', 'from_coin', 'word'])
            
            if q_type == 'from_note':
                paid = random.choice([5, 10, 20])
                cost = round(random.uniform(1.00, paid - 0.50), 2)
                change = round(paid - cost, 2)
                
                q_text = f"{name} pays with a €{paid} note for something costing {format_euro_decimal(cost)}. What change?"
                correct = format_euro_decimal(change)
                wrong = [format_euro_decimal(change + 1), format_euro_decimal(cost), format_euro_decimal(change - 0.50)]
                explanation = f"Step 1: €{paid} - {format_euro_decimal(cost)} = {correct} change. ✓"
                
            elif q_type == 'from_coin':
                paid = random.choice([2, 5])
                cost = round(random.uniform(0.50, paid - 0.20), 2)
                change = round(paid - cost, 2)
                
                q_text = f"An item costs {format_euro_decimal(cost)}. You pay with €{paid}. How much change?"
                correct = format_euro_decimal(change)
                wrong = [format_euro_decimal(change + 0.50), format_euro_decimal(cost), format_euro_decimal(paid)]
                explanation = f"Step 1: €{paid} - {format_euro_decimal(cost)} = {correct} change. ✓"
                
            else:  # word
                paid = random.choice([10, 20])
                item = random.choice(list(SHOP_ITEMS.keys()))
                cost = round(random.uniform(3.00, paid - 2.00), 2)
                change = round(paid - cost, 2)
                
                q_text = f"{name} buys a {item} for {format_euro_decimal(cost)} and pays with €{paid}. What change should they get?"
                correct = format_euro_decimal(change)
                wrong = [format_euro_decimal(change + 2), format_euro_decimal(cost), format_euro_decimal(change - 1)]
                explanation = f"Step 1: €{paid} - {format_euro_decimal(cost)} = {correct} change. ✓"
            
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
# LEVEL 6: Rounding Money (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Rounding Money"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['round_euro', 'round_10c', 'estimate'])
            
            if q_type == 'round_euro':
                euros = random.randint(1, 20)
                cents = random.randint(1, 99)
                amount = euros + cents / 100
                
                rounded = round(amount)
                
                q_text = f"Round {format_euro_decimal(amount)} to the nearest euro."
                correct = f"€{rounded}"
                wrong = [f"€{rounded + 1}", f"€{rounded - 1}" if rounded > 1 else "€2", format_euro_decimal(amount)]
                explanation = f"Step 1: {format_euro_decimal(amount)} rounds to €{rounded}. {'(≥50c rounds up)' if cents >= 50 else '(<50c rounds down)'} ✓"
                
            elif q_type == 'round_10c':
                euros = random.randint(1, 10)
                cents = random.randint(1, 99)
                amount = euros + cents / 100
                
                # Round to nearest 10c
                rounded_cents = round(cents / 10) * 10
                if rounded_cents == 100:
                    rounded = euros + 1
                    rounded_str = f"€{rounded}"
                else:
                    rounded = euros + rounded_cents / 100
                    rounded_str = format_euro_decimal(rounded)
                
                q_text = f"Round {format_euro_decimal(amount)} to the nearest 10 cent."
                correct = rounded_str
                wrong = [f"€{euros}", format_euro_decimal(amount), f"€{euros + 1}"]
                explanation = f"Step 1: {format_euro_decimal(amount)} rounds to {rounded_str}. ✓"
                
            else:  # estimate
                prices = [round(random.uniform(2.00, 8.00), 2) for _ in range(2)]
                total = sum(prices)
                estimate = round(prices[0]) + round(prices[1])
                
                q_text = f"Estimate {format_euro_decimal(prices[0])} + {format_euro_decimal(prices[1])} by rounding to whole euros first."
                correct = f"€{estimate}"
                actual = format_euro_decimal(total)
                wrong = [actual, f"€{estimate + 2}", f"€{estimate - 2}" if estimate > 2 else "€1"]
                explanation = f"Step 1: {format_euro_decimal(prices[0])} ≈ €{round(prices[0])}, {format_euro_decimal(prices[1])} ≈ €{round(prices[1])}. Step 2: Estimate = €{estimate}. ✓"
            
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
# LEVEL 7: Shopping Problems (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Shopping Word Problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            problem_type = random.randint(1, 4)
            
            if problem_type == 1:
                # Multiple items, find total and change
                paid = random.choice([10, 20])
                items = random.sample(list(SHOP_ITEMS.keys()), 2)
                prices = [round(random.uniform(*SHOP_ITEMS[item]), 2) for item in items]
                total = round(sum(prices), 2)
                change = round(paid - total, 2)
                
                q_text = f"{name} buys a {items[0]} ({format_euro_decimal(prices[0])}) and a {items[1]} ({format_euro_decimal(prices[1])}). They pay with €{paid}. What change?"
                correct = format_euro_decimal(change)
                wrong = [format_euro_decimal(total), format_euro_decimal(change + 1), f"€{paid}"]
                explanation = f"Step 1: Total = {format_euro_decimal(total)}. Step 2: Change = €{paid} - {format_euro_decimal(total)} = {correct}. ✓"
                
            elif problem_type == 2:
                # Can they afford it?
                has = round(random.uniform(5.00, 15.00), 2)
                items = random.sample(list(SHOP_ITEMS.keys()), 3)
                prices = [round(random.uniform(*SHOP_ITEMS[item]), 2) for item in items]
                total = round(sum(prices), 2)
                
                can_afford = "Yes" if has >= total else "No"
                
                q_text = f"{name} has {format_euro_decimal(has)}. Can they buy: {items[0]} ({format_euro_decimal(prices[0])}), {items[1]} ({format_euro_decimal(prices[1])}), {items[2]} ({format_euro_decimal(prices[2])})?"
                correct = can_afford
                wrong = ["Yes" if can_afford == "No" else "No", "Maybe", "Not enough info"]
                explanation = f"Step 1: Total = {format_euro_decimal(total)}. Step 2: Has {format_euro_decimal(has)}. {can_afford}, {'enough' if can_afford == 'Yes' else 'not enough'}. ✓"
                
            elif problem_type == 3:
                # How much more needed?
                has = round(random.uniform(3.00, 8.00), 2)
                want_price = round(has + random.uniform(1.00, 5.00), 2)
                need_more = round(want_price - has, 2)
                
                item = random.choice(list(SHOP_ITEMS.keys()))
                
                q_text = f"{name} wants to buy a {item} costing {format_euro_decimal(want_price)}. They have {format_euro_decimal(has)}. How much more do they need?"
                correct = format_euro_decimal(need_more)
                wrong = [format_euro_decimal(has), format_euro_decimal(want_price), format_euro_decimal(need_more + 1)]
                explanation = f"Step 1: {format_euro_decimal(want_price)} - {format_euro_decimal(has)} = {correct} more needed. ✓"
                
            else:
                # Split bill
                total = round(random.uniform(10.00, 30.00), 2)
                people = random.choice([2, 4, 5])
                # Make it divide evenly
                total = round(round(total / people, 2) * people, 2)
                each = round(total / people, 2)
                
                q_text = f"{people} friends share a bill of {format_euro_decimal(total)} equally. How much does each pay?"
                correct = format_euro_decimal(each)
                wrong = [format_euro_decimal(total), format_euro_decimal(each + 1), format_euro_decimal(each * 2)]
                explanation = f"Step 1: {format_euro_decimal(total)} ÷ {people} = {correct} each. ✓"
            
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
# LEVEL 8: Discounts and Sales (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Discounts and Sale Prices"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            q_type = random.choice(['percent_off', 'amount_off', 'sale_price'])
            
            if q_type == 'percent_off':
                original = random.choice([10, 20, 40, 50])
                discount_pct = random.choice([10, 20, 25, 50])
                discount_amount = original * discount_pct / 100
                sale_price = original - discount_amount
                
                q_text = f"A €{original} item has {discount_pct}% off. What is the sale price?"
                correct = format_euro_decimal(sale_price)
                wrong = [format_euro_decimal(discount_amount), f"€{original}", format_euro_decimal(sale_price + 5)]
                explanation = f"Step 1: {discount_pct}% of €{original} = €{discount_amount}. Step 2: Sale price = €{original} - €{discount_amount} = {correct}. ✓"
                
            elif q_type == 'amount_off':
                original = round(random.uniform(15.00, 40.00), 2)
                discount = round(random.uniform(2.00, 8.00), 2)
                sale_price = round(original - discount, 2)
                
                q_text = f"Originally {format_euro_decimal(original)}, now {format_euro_decimal(discount)} off. New price?"
                correct = format_euro_decimal(sale_price)
                wrong = [format_euro_decimal(original), format_euro_decimal(discount), format_euro_decimal(sale_price + discount)]
                explanation = f"Step 1: {format_euro_decimal(original)} - {format_euro_decimal(discount)} = {correct}. ✓"
                
            else:  # sale_price
                original = random.choice([20, 30, 40, 50])
                sale_price = original / 2
                
                q_text = f"A €{original} item is half price in the sale. What does it cost now?"
                correct = format_euro_decimal(sale_price)
                wrong = [f"€{original}", format_euro_decimal(sale_price + 5), format_euro_decimal(original * 0.75)]
                explanation = f"Step 1: Half of €{original} = {correct}. ✓"
            
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
# LEVEL 9: Budgeting (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Budgeting and Planning"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            problem_type = random.randint(1, 4)
            
            if problem_type == 1:
                # Weekly budget
                weekly = random.choice([10, 15, 20])
                weeks = random.randint(3, 6)
                total = weekly * weeks
                
                q_text = f"{name} saves €{weekly} per week. How much after {weeks} weeks?"
                correct = f"€{total}"
                wrong = [f"€{total + weekly}", f"€{weekly}", f"€{total - weekly}"]
                explanation = f"Step 1: €{weekly} × {weeks} = €{total}. ✓"
                
            elif problem_type == 2:
                # Spending tracker
                start = random.choice([50, 100])
                expenses = [random.randint(5, 20) for _ in range(3)]
                total_spent = sum(expenses)
                remaining = start - total_spent
                
                q_text = f"{name} has €{start}. They spend €{expenses[0]}, €{expenses[1]}, and €{expenses[2]}. How much left?"
                correct = f"€{remaining}"
                wrong = [f"€{total_spent}", f"€{start}", f"€{remaining + 10}"]
                explanation = f"Step 1: Total spent = €{total_spent}. Step 2: €{start} - €{total_spent} = €{remaining} left. ✓"
                
            elif problem_type == 3:
                # Saving for goal
                goal = random.choice([50, 60, 80, 100])
                saved = random.randint(10, goal - 20)
                weekly_save = random.choice([5, 10])
                weeks_needed = (goal - saved + weekly_save - 1) // weekly_save
                
                q_text = f"{name} wants €{goal}. They have €{saved} and save €{weekly_save}/week. How many more weeks to reach the goal?"
                correct = f"{weeks_needed} weeks"
                wrong = [f"{weeks_needed + 1} weeks", f"{weeks_needed - 1} weeks" if weeks_needed > 1 else "1 week", f"{goal // weekly_save} weeks"]
                explanation = f"Step 1: Need €{goal - saved} more. Step 2: €{goal - saved} ÷ €{weekly_save} = {weeks_needed} weeks. ✓"
                
            else:
                # Comparing costs
                option1_each = round(random.uniform(2.00, 4.00), 2)
                option1_qty = 3
                option1_total = round(option1_each * option1_qty, 2)
                
                option2_total = round(option1_total - random.uniform(0.50, 1.50), 2)
                savings = round(option1_total - option2_total, 2)
                
                q_text = f"Option A: 3 items at {format_euro_decimal(option1_each)} each. Option B: Pack of 3 for {format_euro_decimal(option2_total)}. How much saved with Option B?"
                correct = format_euro_decimal(savings)
                wrong = [format_euro_decimal(option1_total), format_euro_decimal(option2_total), format_euro_decimal(savings + 1)]
                explanation = f"Step 1: Option A = {format_euro_decimal(option1_total)}. Step 2: Savings = {format_euro_decimal(option1_total)} - {format_euro_decimal(option2_total)} = {correct}. ✓"
            
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
# LEVEL 10: Multi-Step Money Problems (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Multi-Step Money Problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            problem_type = random.randint(1, 4)
            
            if problem_type == 1:
                # Buy, get change, buy more
                start = 20
                item1 = round(random.uniform(5.00, 10.00), 2)
                after1 = round(start - item1, 2)
                item2 = round(random.uniform(2.00, after1 - 1), 2)
                final = round(after1 - item2, 2)
                
                q_text = f"{name} has €{start}. Buys item for {format_euro_decimal(item1)}, then another for {format_euro_decimal(item2)}. How much left?"
                correct = format_euro_decimal(final)
                wrong = [format_euro_decimal(after1), format_euro_decimal(item1 + item2), f"€{start}"]
                explanation = f"Step 1: €{start} - {format_euro_decimal(item1)} = {format_euro_decimal(after1)}. Step 2: {format_euro_decimal(after1)} - {format_euro_decimal(item2)} = {correct}. ✓"
                
            elif problem_type == 2:
                # Earn and spend
                earned = random.choice([15, 20, 25])
                spent_pct = random.choice([20, 25, 40])
                spent = earned * spent_pct / 100
                saved = earned - spent
                
                q_text = f"{name} earns €{earned} and spends {spent_pct}%. How much do they save?"
                correct = format_euro_decimal(saved)
                wrong = [format_euro_decimal(spent), f"€{earned}", format_euro_decimal(saved + 5)]
                explanation = f"Step 1: {spent_pct}% of €{earned} = €{spent} spent. Step 2: €{earned} - €{spent} = {correct} saved. ✓"
                
            elif problem_type == 3:
                # Discount then additional purchase
                item_original = random.choice([20, 30, 40])
                discount = 25
                sale_price = item_original * (100 - discount) / 100
                extra_item = round(random.uniform(3.00, 8.00), 2)
                total = sale_price + extra_item
                
                q_text = f"A €{item_original} item is {discount}% off. {name} also buys something for {format_euro_decimal(extra_item)}. Total cost?"
                correct = format_euro_decimal(total)
                wrong = [format_euro_decimal(item_original + extra_item), format_euro_decimal(sale_price), format_euro_decimal(total + 5)]
                explanation = f"Step 1: Sale price = €{sale_price}. Step 2: Total = €{sale_price} + {format_euro_decimal(extra_item)} = {correct}. ✓"
                
            else:
                # Group purchase with leftover
                people = random.choice([3, 4, 5])
                each_contrib = random.choice([5, 10])
                total_pool = people * each_contrib
                item_cost = round(total_pool - random.uniform(2.00, 8.00), 2)
                leftover = round(total_pool - item_cost, 2)
                each_back = round(leftover / people, 2)
                
                q_text = f"{people} friends each put in €{each_contrib}. They buy a gift for {format_euro_decimal(item_cost)}. How much does each get back?"
                correct = format_euro_decimal(each_back)
                wrong = [format_euro_decimal(leftover), format_euro_decimal(each_contrib), format_euro_decimal(each_back + 1)]
                explanation = f"Step 1: Total = €{total_pool}. Leftover = €{leftover}. Step 2: Each gets back €{leftover} ÷ {people} = {correct}. ✓"
            
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
# LEVEL 11: Best Value (Advanced)
# ============================================================

def generate_level_11():
    """Level 11: Comparing Value and Best Deals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            problem_type = random.randint(1, 4)
            
            if problem_type == 1:
                # Unit price comparison
                qty1 = random.choice([3, 4, 5])
                price1 = round(random.uniform(2.00, 5.00), 2)
                unit1 = round(price1 / qty1, 2)
                
                qty2 = random.choice([6, 8, 10])
                unit2 = round(unit1 - random.uniform(0.05, 0.15), 2)
                price2 = round(unit2 * qty2, 2)
                
                better = "Pack B" if unit2 < unit1 else "Pack A"
                
                q_text = f"Pack A: {qty1} for {format_euro_decimal(price1)}. Pack B: {qty2} for {format_euro_decimal(price2)}. Which is better value?"
                correct = better
                wrong = ["Pack A" if better == "Pack B" else "Pack B", "Same value", "Cannot tell"]
                explanation = f"Step 1: Pack A = {format_euro_decimal(unit1)}/item. Pack B = {format_euro_decimal(unit2)}/item. Step 2: {better} is better value. ✓"
                
            elif problem_type == 2:
                # Multi-buy offer
                single_price = round(random.uniform(1.50, 3.00), 2)
                multi_qty = 3
                multi_price = round(single_price * multi_qty * 0.8, 2)
                savings = round(single_price * multi_qty - multi_price, 2)
                
                q_text = f"Single item: {format_euro_decimal(single_price)}. Or buy {multi_qty} for {format_euro_decimal(multi_price)}. How much saved with the multi-buy?"
                correct = format_euro_decimal(savings)
                wrong = [format_euro_decimal(multi_price), format_euro_decimal(single_price), format_euro_decimal(savings + 0.50)]
                explanation = f"Step 1: {multi_qty} singles = {format_euro_decimal(single_price * multi_qty)}. Step 2: Savings = {format_euro_decimal(single_price * multi_qty)} - {format_euro_decimal(multi_price)} = {correct}. ✓"
                
            elif problem_type == 3:
                # Percentage vs fixed discount
                original = random.choice([40, 50, 60])
                pct_discount = 20
                fixed_discount = original * 0.15  # 15% equivalent
                
                pct_price = original * (100 - pct_discount) / 100
                fixed_price = original - fixed_discount
                
                better = f"{pct_discount}% off" if pct_price < fixed_price else f"€{fixed_discount} off"
                
                q_text = f"€{original} item: {pct_discount}% off OR €{fixed_discount} off. Which gives lower price?"
                correct = better
                wrong = [f"{pct_discount}% off" if better != f"{pct_discount}% off" else f"€{fixed_discount} off", "Same price", "Cannot tell"]
                explanation = f"Step 1: {pct_discount}% off = €{pct_price}. €{fixed_discount} off = €{fixed_price}. Step 2: {better} is cheaper. ✓"
                
            else:
                # Total cost comparison
                shop_a_items = [round(random.uniform(2.00, 5.00), 2) for _ in range(3)]
                shop_a_total = round(sum(shop_a_items), 2)
                shop_b_total = round(shop_a_total + random.choice([-1.50, -0.50, 0.50, 1.50]), 2)
                
                better = "Shop A" if shop_a_total < shop_b_total else "Shop B"
                diff = round(abs(shop_a_total - shop_b_total), 2)
                
                q_text = f"Shop A total: {format_euro_decimal(shop_a_total)}. Shop B total: {format_euro_decimal(shop_b_total)}. Which is cheaper and by how much?"
                correct = f"{better} by {format_euro_decimal(diff)}"
                wrong = [f"{'Shop B' if better == 'Shop A' else 'Shop A'} by {format_euro_decimal(diff)}", f"Same price", f"{better} by {format_euro_decimal(diff + 1)}"]
                explanation = f"Step 1: Difference = {format_euro_decimal(diff)}. Step 2: {better} is {format_euro_decimal(diff)} cheaper. ✓"
            
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
    print("VALIDATION - Money Skills")
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
    print("AgentMath - Money Skills Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "Recognising Coins", generate_level_1),
        (2, "Counting Coins", generate_level_2),
        (3, "Simple Totals", generate_level_3),
        (4, "Adding Money", generate_level_4),
        (5, "Giving Change", generate_level_5),
        (6, "Rounding Money", generate_level_6),
        (7, "Shopping Problems", generate_level_7),
        (8, "Discounts and Sales", generate_level_8),
        (9, "Budgeting", generate_level_9),
        (10, "Multi-Step Problems", generate_level_10),
        (11, "Best Value", generate_level_11),
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
