#!/usr/bin/env python3
"""
AgentMath - Currency Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q3(d): Convert £15.95 to euro at €1 = £0.90
- 2022 HL Q1(a): Convert €350 to US dollars at €1 = $1.20
- 2025 OL Q12(c): Compare pizza prices €14 vs £12 at €1 = £0.93

Level Structure:
  L1-3:   Foundation (understanding exchange rates, simple conversions)
  L4-6:   Ordinary (€/£/$, reverse conversions, rounding)
  L7-9:   Higher (price comparisons, best value, multi-currency)
  L10-12: Application/Mastery (complex problems, commission, real-world)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os
from decimal import Decimal, ROUND_HALF_UP

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'currency'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Róisín', 'Seán', 
               'Ciara', 'Darragh', 'Éabha', 'Fionn', 'Gráinne', 'Liam', 'Meadhbh', 'Tadhg',
               'Áine', 'Cillian', 'Orlaith', 'Pádraig', 'Sinéad', 'Eoin', 'Caoimhe', 'Declan',
               'Lily', 'Noah', 'Alice', 'Tomás', 'Jane', 'Joshua', 'Emma', 'Jack']

# Cities for travel contexts
IRISH_CITIES = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford']
UK_CITIES = ['London', 'Manchester', 'Birmingham', 'Edinburgh', 'Liverpool']
US_CITIES = ['New York', 'Boston', 'Chicago', 'Los Angeles', 'Miami']
EU_CITIES = ['Paris', 'Berlin', 'Rome', 'Madrid', 'Amsterdam']

# Items for price comparisons
ITEMS = ['pizza', 'coffee', 'book', 'T-shirt', 'trainers', 'headphones', 'backpack', 
         'watch', 'sunglasses', 'jacket', 'jeans', 'phone case', 'football', 'concert ticket']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def round_money(value, decimals=2):
    """Round to specified decimal places for money"""
    return float(Decimal(str(value)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

def format_euro(value):
    """Format as euro amount"""
    rounded = round_money(value)
    if rounded == int(rounded):
        return f"€{int(rounded)}"
    return f"€{rounded:.2f}"

def format_sterling(value):
    """Format as sterling amount"""
    rounded = round_money(value)
    if rounded == int(rounded):
        return f"£{int(rounded)}"
    return f"£{rounded:.2f}"

def format_dollar(value):
    """Format as dollar amount"""
    rounded = round_money(value)
    if rounded == int(rounded):
        return f"${int(rounded)}"
    return f"${rounded:.2f}"

def format_currency(value, currency):
    """Format value with appropriate currency symbol"""
    if currency == 'EUR':
        return format_euro(value)
    elif currency == 'GBP':
        return format_sterling(value)
    elif currency == 'USD':
        return format_dollar(value)
    else:
        return f"{value:.2f} {currency}"

def get_unique_wrong_money(correct_val, count=3, currency='EUR'):
    """Generate unique wrong money options"""
    correct_rounded = round_money(correct_val)
    wrong = set()
    
    candidates = [
        correct_rounded + 0.10, correct_rounded - 0.10,
        correct_rounded + 1, correct_rounded - 1,
        correct_rounded + 0.50, correct_rounded - 0.50,
        correct_rounded * 1.1, correct_rounded * 0.9,
        correct_rounded + 5, correct_rounded - 5,
        correct_rounded * 2, correct_rounded / 2,
        correct_rounded + 2, correct_rounded - 2,
        correct_rounded * 1.05, correct_rounded * 0.95
    ]
    
    for c in candidates:
        c_rounded = round_money(c)
        if c_rounded > 0 and c_rounded != correct_rounded and len(wrong) < count:
            wrong.add(c_rounded)
    
    while len(wrong) < count:
        w = round_money(random.uniform(max(0.50, correct_rounded * 0.5), correct_rounded * 2))
        if w > 0 and w != correct_rounded and w not in wrong:
            wrong.add(w)
    
    formatted = []
    for w in list(wrong)[:count]:
        formatted.append(format_currency(w, currency))
    
    return formatted

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

def generate_exchange_board_svg(rates):
    """Generate SVG showing exchange rate board"""
    width = 240
    height = 40 + len(rates) * 30
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#1e3a5f" stroke="#0d47a1" stroke-width="2" rx="5"/>'
    
    # Header
    svg += f'<text x="120" y="25" text-anchor="middle" font-size="14" fill="#ffd700" font-weight="bold">💱 Exchange Rates</text>'
    
    # Rates
    y = 50
    for from_curr, to_curr, rate in rates:
        svg += f'<text x="20" y="{y}" font-size="12" fill="#ffffff">€1 = </text>'
        symbol = '£' if to_curr == 'GBP' else '$' if to_curr == 'USD' else to_curr
        svg += f'<text x="60" y="{y}" font-size="12" fill="#4fc3f7" font-weight="bold">{symbol}{rate}</text>'
        svg += f'<text x="130" y="{y}" font-size="10" fill="#90caf9">({to_curr})</text>'
        y += 30
    
    svg += '</svg>'
    return svg

def generate_conversion_svg(from_amount, from_curr, to_amount, to_curr, rate):
    """Generate SVG for currency conversion"""
    width = 280
    height = 90
    
    symbols = {'EUR': '€', 'GBP': '£', 'USD': '$'}
    from_sym = symbols.get(from_curr, from_curr)
    to_sym = symbols.get(to_curr, to_curr)
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#e3f2fd" stroke="#1976d2" stroke-width="2" rx="8"/>'
    
    # From amount box
    svg += f'<rect x="20" y="25" width="90" height="45" fill="#bbdefb" rx="5"/>'
    svg += f'<text x="65" y="52" text-anchor="middle" font-size="16" fill="#0d47a1" font-weight="bold">{from_sym}{from_amount}</text>'
    svg += f'<text x="65" y="65" text-anchor="middle" font-size="9" fill="#1565c0">{from_curr}</text>'
    
    # Arrow with rate
    svg += f'<text x="140" y="42" text-anchor="middle" font-size="9" fill="#616161">Rate: {rate}</text>'
    svg += f'<path d="M 115 50 L 165 50 L 155 45 M 165 50 L 155 55" stroke="#1976d2" stroke-width="2" fill="none"/>'
    
    # To amount box
    svg += f'<rect x="170" y="25" width="90" height="45" fill="#c8e6c9" rx="5"/>'
    svg += f'<text x="215" y="52" text-anchor="middle" font-size="16" fill="#2e7d32" font-weight="bold">{to_sym}{to_amount}</text>'
    svg += f'<text x="215" y="65" text-anchor="middle" font-size="9" fill="#388e3c">{to_curr}</text>'
    
    svg += '</svg>'
    return svg

def generate_price_comparison_svg(item, price1, curr1, city1, price2, curr2, city2):
    """Generate SVG for price comparison"""
    width = 280
    height = 100
    
    symbols = {'EUR': '€', 'GBP': '£', 'USD': '$'}
    sym1 = symbols.get(curr1, curr1)
    sym2 = symbols.get(curr2, curr2)
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fff3e0" stroke="#ff9800" stroke-width="2" rx="8"/>'
    
    # Header
    svg += f'<text x="140" y="22" text-anchor="middle" font-size="12" fill="#e65100" font-weight="bold">🛒 {item.title()} Price Comparison</text>'
    
    # City 1
    svg += f'<rect x="20" y="35" width="110" height="55" fill="#ffe0b2" rx="5"/>'
    svg += f'<text x="75" y="55" text-anchor="middle" font-size="11" fill="#bf360c">{city1}</text>'
    svg += f'<text x="75" y="75" text-anchor="middle" font-size="16" fill="#e65100" font-weight="bold">{sym1}{price1}</text>'
    
    # VS
    svg += f'<text x="140" y="65" text-anchor="middle" font-size="12" fill="#ff9800" font-weight="bold">VS</text>'
    
    # City 2
    svg += f'<rect x="150" y="35" width="110" height="55" fill="#ffe0b2" rx="5"/>'
    svg += f'<text x="205" y="55" text-anchor="middle" font-size="11" fill="#bf360c">{city2}</text>'
    svg += f'<text x="205" y="75" text-anchor="middle" font-size="16" fill="#e65100" font-weight="bold">{sym2}{price2}</text>'
    
    svg += '</svg>'
    return svg

def generate_travel_budget_svg(destination, items_budget):
    """Generate SVG for travel budget"""
    width = 260
    height = 50 + len(items_budget) * 25 + 30
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#e8f5e9" stroke="#4caf50" stroke-width="2" rx="5"/>'
    
    # Header
    svg += f'<text x="130" y="25" text-anchor="middle" font-size="13" fill="#2e7d32" font-weight="bold">✈️ Trip to {destination}</text>'
    svg += f'<line x1="10" y1="35" x2="250" y2="35" stroke="#4caf50" stroke-width="1"/>'
    
    # Items
    y = 55
    total = 0
    for item, amount, curr in items_budget:
        symbols = {'EUR': '€', 'GBP': '£', 'USD': '$'}
        sym = symbols.get(curr, curr)
        svg += f'<text x="20" y="{y}" font-size="11" fill="#374151">{item}</text>'
        svg += f'<text x="240" y="{y}" text-anchor="end" font-size="11" fill="#374151">{sym}{amount:.2f}</text>'
        total += amount
        y += 25
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Understanding Exchange Rates (Foundation)
# ============================================================

def generate_level_1():
    """Understanding Exchange Rates - What they mean"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['what_means', 'which_more', 'identify_symbol', 'read_board', 'basic_concept', 'currency_country', 'true_false', 'simple_meaning'])
        
        try:
            if q_type == 'what_means':
                rate = round_money(random.uniform(0.78, 0.98))
                curr = random.choice(['GBP', 'USD'])
                symbol = '£' if curr == 'GBP' else '$'
                curr_name = 'British pounds' if curr == 'GBP' else 'US dollars'
                
                q_text = f"The exchange rate is €1 = {symbol}{rate}.\\nWhat does this mean?"
                correct = f"€1 can be exchanged for {symbol}{rate}"
                wrong = [
                    f"{symbol}1 can be exchanged for €{rate}",
                    f"€{rate} can be exchanged for {symbol}1",
                    f"€1 and {symbol}{rate} are the same coin"
                ]
                
                visual = generate_exchange_board_svg([('EUR', curr, rate)])
                explanation = f"€1 = {symbol}{rate} means that 1 euro can be exchanged for {rate} {curr_name}."
                
            elif q_type == 'which_more':
                rate = round_money(random.uniform(0.80, 0.96))
                comparison = random.choice(['gbp', 'usd_high', 'usd_low'])
                
                if comparison == 'gbp':
                    q_text = f"Exchange rate: €1 = £{rate}\\nWhich is worth more, €1 or £1?"
                    correct = "€1 is worth more"
                    wrong = ["£1 is worth more", "They are equal", "Cannot tell from this information"]
                    visual = generate_exchange_board_svg([('EUR', 'GBP', rate)])
                    explanation = f"Since €1 = £{rate} (less than 1), you get fewer pounds than euros.\\nThis means €1 is worth MORE than £1."
                elif comparison == 'usd_high':
                    usd_rate = round_money(random.uniform(1.05, 1.25))
                    q_text = f"Exchange rate: €1 = ${usd_rate}\\nWhich is worth more, €1 or $1?"
                    correct = "$1 is worth less than €1"
                    wrong = ["$1 is worth more than €1", "They are equal", "Cannot tell"]
                    visual = generate_exchange_board_svg([('EUR', 'USD', usd_rate)])
                    explanation = f"Since €1 = ${usd_rate} (more than 1), you get more dollars than euros.\\nThis means €1 is worth MORE than $1."
                else:
                    q_text = f"If €1 = £0.90, how many pounds do you get for €1?"
                    correct = "£0.90"
                    wrong = ["£1.00", "£1.10", "£0.10"]
                    visual = None
                    explanation = "The rate tells us directly: €1 gives you £0.90"
                
            elif q_type == 'identify_symbol':
                currencies = [
                    ('€', 'Euro'), ('£', 'Pound Sterling'), ('$', 'US Dollar'),
                    ('€', 'Euro (EU currency)'), ('£', 'British Pound'), ('$', 'American Dollar')
                ]
                currency = random.choice(currencies)
                
                q_text = f"What currency uses the symbol {currency[0]}?"
                correct = currency[1]
                all_currencies = ['Euro', 'Pound Sterling', 'US Dollar', 'Japanese Yen', 'British Pound', 'Euro (EU currency)', 'American Dollar']
                wrong = [c for c in all_currencies if c != currency[1]][:3]
                
                visual = None
                explanation = f"The {currency[0]} symbol represents {currency[1]}."
                
            elif q_type == 'read_board':
                gbp_rate = round_money(random.uniform(0.82, 0.95))
                usd_rate = round_money(random.uniform(1.05, 1.25))
                
                ask_curr = random.choice(['GBP', 'USD'])
                ask_rate = gbp_rate if ask_curr == 'GBP' else usd_rate
                symbol = '£' if ask_curr == 'GBP' else '$'
                name = 'British pounds' if ask_curr == 'GBP' else 'US dollars'
                
                q_text = f"Look at the exchange board.\\nHow many {name} do you get for €1?"
                correct = f"{symbol}{ask_rate}"
                wrong = [
                    f"{symbol}{round_money(ask_rate + 0.05)}",
                    f"{symbol}{round_money(ask_rate - 0.05)}",
                    f"{symbol}{round_money(1/ask_rate)}"
                ]
                
                visual = generate_exchange_board_svg([('EUR', 'GBP', gbp_rate), ('EUR', 'USD', usd_rate)])
                explanation = f"Reading from the exchange board: €1 = {symbol}{ask_rate}"
                
            elif q_type == 'basic_concept':
                concepts = [
                    ("What is an exchange rate?", "The value of one currency compared to another", 
                     ["The cost of travelling abroad", "A bank fee for transfers", "The price of foreign goods"]),
                    ("Why do people exchange currency?", "To spend money in another country",
                     ["To make the money weigh less", "Because banks require it", "To get new coins"]),
                    ("Where can you exchange currency in Ireland?", "Banks, bureaux de change, post offices",
                     ["Only at Dublin Airport", "Only at banks", "Only online"]),
                    ("What currency do tourists need when visiting Ireland?", "Euro (€)",
                     ["Pound Sterling (£)", "US Dollar ($)", "Irish Punt"]),
                    ("What happens when you exchange currency?", "You give one currency and receive another",
                     ["You get free money", "Your money doubles", "You lose all your money"])
                ]
                concept = random.choice(concepts)
                
                q_text = concept[0]
                correct = concept[1]
                wrong = concept[2]
                
                visual = None
                explanation = f"{concept[0]} Answer: {concept[1]}"
                
            elif q_type == 'currency_country':
                pairs = [
                    ("Ireland", "Euro (€)"), ("France", "Euro (€)"), ("Germany", "Euro (€)"),
                    ("United Kingdom", "Pound Sterling (£)"), ("England", "Pound Sterling (£)"),
                    ("United States", "US Dollar ($)"), ("America", "US Dollar ($)"),
                    ("Spain", "Euro (€)"), ("Italy", "Euro (€)"), ("Scotland", "Pound Sterling (£)"),
                    ("Northern Ireland", "Pound Sterling (£)"), ("Wales", "Pound Sterling (£)"),
                    ("Belgium", "Euro (€)"), ("Netherlands", "Euro (€)"), ("Portugal", "Euro (€)")
                ]
                pair = random.choice(pairs)
                
                q_text = f"What currency is used in {pair[0]}?"
                correct = pair[1]
                all_curr = ["Euro (€)", "Pound Sterling (£)", "US Dollar ($)", "Japanese Yen (¥)"]
                wrong = [c for c in all_curr if c != pair[1]][:3]
                
                visual = None
                explanation = f"{pair[0]} uses {pair[1]} as its currency."
                
            elif q_type == 'true_false':
                statements = [
                    ("The euro is used in Ireland", "True", ["False", "Only in Dublin", "Only for tourists"]),
                    ("€1 = £0.90 means the euro is worth more than the pound", "True", ["False", "They are equal", "Cannot tell"]),
                    ("Exchange rates stay the same forever", "False", ["True", "Only on weekends", "Only in banks"]),
                    ("You can exchange currency at an airport", "True", ["False", "Only euros", "Only cash"]),
                    ("The symbol £ represents the US dollar", "False", ["True", "Sometimes", "In Europe only"])
                ]
                statement = random.choice(statements)
                
                q_text = f"True or False: {statement[0]}"
                correct = statement[1]
                wrong = statement[2]
                
                visual = None
                explanation = f"'{statement[0]}' is {statement[1]}."
                
            else:  # simple_meaning
                scenarios = [
                    (f"€1 = £0.{random.randint(82,95)}", "You get fewer than 1 pound for 1 euro"),
                    (f"€1 = $1.{random.randint(10,25)}", "You get more than 1 dollar for 1 euro"),
                ]
                scenario = random.choice(scenarios)
                
                q_text = f"What does the rate {scenario[0]} tell us?"
                correct = scenario[1]
                wrong = [
                    "You get exactly 1 unit of foreign currency",
                    "The currencies are worth the same",
                    "You cannot exchange this currency"
                ]
                
                visual = None
                explanation = f"{scenario[0]}: {scenario[1]}"
            
            options, correct_idx = make_options(correct, wrong)
            
            if len(set(options)) != 4:
                continue
            
            q_sig = f"{q_type}_{correct}_{q_text[:25]}"
            if q_sig in used:
                continue
            used.add(q_sig)
            
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
# LEVEL 2: Euro to Sterling - Simple (Foundation)
# ============================================================

def generate_level_2():
    """Euro to Sterling - Simple whole number conversions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            rate = round_money(random.choice([0.75, 0.80, 0.85, 0.90, 0.95]) + random.uniform(-0.02, 0.02))
            euro_amount = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 100, 150, 200, 250])
            
            sterling = round_money(euro_amount * rate)
            
            uk_city = random.choice(UK_CITIES)
            contexts = [
                f"{name} is going to {uk_city}.",
                f"{name} is visiting the UK.",
                f"{name} needs British pounds for a trip.",
                f"{name} is shopping online from a UK website.",
                f"{name} is buying a gift for a friend in {uk_city}.",
                f"{name} is going to a concert in {uk_city}."
            ]
            context = random.choice(contexts)
            
            q_text = f"{context}\\nThey change {format_euro(euro_amount)} to pounds.\\nExchange rate: €1 = £{rate}\\nHow many pounds do they get?"
            
            correct = format_sterling(sterling)
            wrong = get_unique_wrong_money(sterling, 3, 'GBP')
            
            visual = generate_conversion_svg(euro_amount, 'EUR', sterling, 'GBP', f"€1 = £{rate}")
            explanation = f"Pounds = Euro × Rate\\n= {format_euro(euro_amount)} × {rate}\\n= {format_sterling(sterling)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"eur_gbp_{euro_amount}_{rate}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 3: Euro to Dollar - Simple (Foundation)
# ============================================================

def generate_level_3():
    """Euro to Dollar - Simple whole number conversions"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            rate = round_money(random.choice([1.05, 1.10, 1.12, 1.15, 1.18, 1.20, 1.22, 1.25]) + random.uniform(-0.02, 0.02))
            euro_amount = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 100, 150, 200, 250, 300])
            
            dollars = round_money(euro_amount * rate)
            
            us_city = random.choice(US_CITIES)
            contexts = [
                f"{name} is going to {us_city}.",
                f"{name} is visiting the USA.",
                f"{name} needs US dollars for a holiday.",
                f"{name} is buying from an American website.",
                f"{name} is saving for a trip to America.",
                f"{name} is going to a theme park in Florida."
            ]
            context = random.choice(contexts)
            
            q_text = f"{context}\\nThey change {format_euro(euro_amount)} to dollars.\\nExchange rate: €1 = ${rate}\\nHow many dollars do they get?"
            
            correct = format_dollar(dollars)
            wrong = get_unique_wrong_money(dollars, 3, 'USD')
            
            visual = generate_conversion_svg(euro_amount, 'EUR', dollars, 'USD', f"€1 = ${rate}")
            explanation = f"Dollars = Euro × Rate\\n= {format_euro(euro_amount)} × {rate}\\n= {format_dollar(dollars)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"eur_usd_{euro_amount}_{rate}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 4: Euro to Sterling - Decimal amounts (Ordinary)
# ============================================================

def generate_level_4():
    """Euro to Sterling with decimal amounts"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            rate = random.choice([0.85, 0.87, 0.88, 0.90, 0.93])
            euro_amount = round_money(random.uniform(50, 500))
            
            sterling = round_money(euro_amount * rate)
            
            uk_city = random.choice(UK_CITIES)
            
            q_text = f"{name} changes {format_euro(euro_amount)} to British pounds for a trip to {uk_city}.\\nExchange rate: €1 = £{rate}\\nHow much sterling do they receive (to the nearest cent)?"
            
            correct = format_sterling(sterling)
            wrong = get_unique_wrong_money(sterling, 3, 'GBP')
            
            visual = generate_conversion_svg(euro_amount, 'EUR', sterling, 'GBP', f"€1 = £{rate}")
            explanation = f"Sterling = Euro × Rate\\n= {format_euro(euro_amount)} × {rate}\\n= {format_sterling(sterling)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"eur_gbp_dec_{euro_amount}_{rate}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 5: Sterling to Euro - Reverse conversion (Ordinary)
# ============================================================

def generate_level_5():
    """Sterling to Euro - Reverse conversion (divide by rate)"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            # SEC 2022 OL Q3(d) style
            rate = round_money(random.choice([0.82, 0.85, 0.87, 0.88, 0.90, 0.92, 0.93, 0.95]) + random.uniform(-0.01, 0.01))
            sterling_amount = round_money(random.choice([5, 8, 10, 12, 15, 15.95, 18, 20, 22, 25, 28, 30, 35, 40, 45, 50, 60, 75, 80, 100]))
            
            euro = round_money(sterling_amount / rate)
            
            items = ['electric pump', 'book', 'souvenir', 'gift', 'jacket', 'bag', 'toy', 
                     'video game', 't-shirt', 'hat', 'mug', 'poster', 'DVD', 'chocolate box']
            item = random.choice(items)
            
            uk_city = random.choice(UK_CITIES)
            contexts = [
                f"{name} buys a {item} in the UK for {format_sterling(sterling_amount)}.",
                f"{name} sees a {item} for {format_sterling(sterling_amount)} in {uk_city}.",
                f"{name} bought a {item} online from the UK. It cost {format_sterling(sterling_amount)}.",
                f"A {item} costs {format_sterling(sterling_amount)} in {uk_city}."
            ]
            context = random.choice(contexts)
            
            q_text = f"{context}\\nExchange rate: €1 = £{rate}\\nConvert {format_sterling(sterling_amount)} to euro (to the nearest cent)."
            
            correct = format_euro(euro)
            wrong = get_unique_wrong_money(euro, 3, 'EUR')
            
            visual = generate_conversion_svg(sterling_amount, 'GBP', euro, 'EUR', f"€1 = £{rate}")
            explanation = f"SEC 2022 OL Q3(d) style!\\nTo convert £ to €, DIVIDE by rate:\\n= {format_sterling(sterling_amount)} ÷ {rate}\\n= {format_euro(euro)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"gbp_eur_{sterling_amount}_{rate}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 6: Dollar conversions both ways (Ordinary)
# ============================================================

def generate_level_6():
    """Dollar conversions - both EUR to USD and USD to EUR"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['eur_to_usd', 'usd_to_eur']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            # SEC 2022 HL Q1(a) style
            rate = random.choice([1.08, 1.10, 1.12, 1.15, 1.20])
            
            if q_type == 'eur_to_usd':
                euro_amount = random.choice([150, 200, 250, 300, 350, 400, 500])
                dollars = round_money(euro_amount * rate)
                
                us_city = random.choice(US_CITIES)
                q_text = f"{name} changes {format_euro(euro_amount)} to US dollars at rate €1 = ${rate}.\\nHow many dollars does {name} get?"
                
                correct = format_dollar(dollars)
                wrong = get_unique_wrong_money(dollars, 3, 'USD')
                
                visual = generate_conversion_svg(euro_amount, 'EUR', dollars, 'USD', f"€1 = ${rate}")
                explanation = f"SEC 2022 HL Q1(a) style!\\nDollars = Euro × Rate\\n= {format_euro(euro_amount)} × {rate}\\n= {format_dollar(dollars)}"
                
            else:  # usd_to_eur
                dollar_amount = random.choice([100, 150, 200, 250, 300])
                euro = round_money(dollar_amount / rate)
                
                q_text = f"{name} returns from America with {format_dollar(dollar_amount)}.\\nExchange rate: €1 = ${rate}\\nHow much is this in euro?"
                
                correct = format_euro(euro)
                wrong = get_unique_wrong_money(euro, 3, 'EUR')
                
                visual = generate_conversion_svg(dollar_amount, 'USD', euro, 'EUR', f"€1 = ${rate}")
                explanation = f"To convert $ to €, DIVIDE by rate:\\n= {format_dollar(dollar_amount)} ÷ {rate}\\n= {format_euro(euro)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{euro_amount if q_type == 'eur_to_usd' else dollar_amount}_{rate}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 7: Price Comparison - Which is cheaper? (Higher)
# ============================================================

def generate_level_7():
    """Price Comparison across currencies"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            # SEC 2025 OL Q12(c) style
            item = random.choice(ITEMS)
            rate = random.choice([0.85, 0.87, 0.90, 0.93])
            
            irish_city = random.choice(IRISH_CITIES)
            uk_city = random.choice(UK_CITIES)
            
            euro_price = random.randint(10, 25)
            # Make sterling price close but different
            sterling_price = round_money(euro_price * rate * random.choice([0.9, 0.95, 1.05, 1.1]))
            
            # Convert sterling to euro for comparison
            sterling_in_euro = round_money(sterling_price / rate)
            
            if euro_price < sterling_in_euro:
                cheaper = irish_city
                saving = round_money(sterling_in_euro - euro_price)
            else:
                cheaper = uk_city
                saving = round_money(euro_price - sterling_in_euro)
            
            q_text = f"A {item} costs {format_euro(euro_price)} in {irish_city} and {format_sterling(sterling_price)} in {uk_city}.\\nExchange rate: €1 = £{rate}\\nWhich city is cheaper, and by how much?"
            
            correct = f"{cheaper} by {format_euro(saving)}"
            other_city = uk_city if cheaper == irish_city else irish_city
            wrong = [
                f"{other_city} by {format_euro(saving)}",
                f"{cheaper} by {format_euro(saving + 1)}",
                f"Same price in both"
            ]
            
            visual = generate_price_comparison_svg(item, euro_price, 'EUR', irish_city, sterling_price, 'GBP', uk_city)
            explanation = f"SEC 2025 OL Q12(c) style!\\nConvert {format_sterling(sterling_price)} to euro:\\n{format_sterling(sterling_price)} ÷ {rate} = {format_euro(sterling_in_euro)}\\n\\n{irish_city}: {format_euro(euro_price)}\\n{uk_city}: {format_euro(sterling_in_euro)}\\n\\n{cheaper} is cheaper by {format_euro(saving)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"compare_{item}_{euro_price}_{sterling_price}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 8: Multi-step conversions (Higher)
# ============================================================

def generate_level_8():
    """Multi-step problems - convert then calculate"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['convert_and_add', 'convert_and_subtract', 'budget_check']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            rate = random.choice([0.85, 0.87, 0.90, 0.93])
            
            if q_type == 'convert_and_add':
                euro1 = random.randint(50, 150)
                sterling = random.randint(30, 80)
                
                sterling_in_euro = round_money(sterling / rate)
                total = round_money(euro1 + sterling_in_euro)
                
                q_text = f"{name} has {format_euro(euro1)} and {format_sterling(sterling)}.\\nExchange rate: €1 = £{rate}\\nWhat is the total value in euro?"
                
                correct = format_euro(total)
                wrong = get_unique_wrong_money(total, 3, 'EUR')
                
                visual = None
                explanation = f"Convert £ to €: {format_sterling(sterling)} ÷ {rate} = {format_euro(sterling_in_euro)}\\nTotal: {format_euro(euro1)} + {format_euro(sterling_in_euro)} = {format_euro(total)}"
                
            elif q_type == 'convert_and_subtract':
                budget_euro = random.randint(200, 400)
                spent_sterling = random.randint(50, 150)
                
                spent_euro = round_money(spent_sterling / rate)
                remaining = round_money(budget_euro - spent_euro)
                
                q_text = f"{name} takes {format_euro(budget_euro)} to the UK and spends {format_sterling(spent_sterling)}.\\nExchange rate: €1 = £{rate}\\nHow much of their budget (in euro) is left?"
                
                correct = format_euro(remaining)
                wrong = get_unique_wrong_money(remaining, 3, 'EUR')
                
                visual = None
                explanation = f"Spent in euro: {format_sterling(spent_sterling)} ÷ {rate} = {format_euro(spent_euro)}\\nRemaining: {format_euro(budget_euro)} - {format_euro(spent_euro)} = {format_euro(remaining)}"
                
            else:  # budget_check
                budget = random.randint(150, 300)
                item_price_sterling = random.randint(80, 200)
                
                item_euro = round_money(item_price_sterling / rate)
                can_afford = budget >= item_euro
                
                q_text = f"{name} has {format_euro(budget)} to spend. They see a jacket for {format_sterling(item_price_sterling)} in London.\\nExchange rate: €1 = £{rate}\\nCan they afford it? If not, how much more do they need?"
                
                if can_afford:
                    change = round_money(budget - item_euro)
                    correct = f"Yes, with {format_euro(change)} to spare"
                    wrong = [
                        f"No, need {format_euro(10)} more",
                        f"Yes, exact amount",
                        f"No, need {format_euro(20)} more"
                    ]
                else:
                    shortfall = round_money(item_euro - budget)
                    correct = f"No, need {format_euro(shortfall)} more"
                    wrong = [
                        f"Yes, with {format_euro(10)} to spare",
                        f"No, need {format_euro(shortfall + 5)} more",
                        f"Yes, exact amount"
                    ]
                
                visual = None
                explanation = f"Jacket in euro: {format_sterling(item_price_sterling)} ÷ {rate} = {format_euro(item_euro)}\\nBudget: {format_euro(budget)}\\n{'Can afford!' if can_afford else f'Short by {format_euro(item_euro - budget)}'}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:40]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 9: Best Exchange Rate (Higher)
# ============================================================

def generate_level_9():
    """Compare exchange rates to find best deal"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['best_rate_gbp', 'best_rate_usd', 'rate_difference']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'best_rate_gbp':
                rate1 = random.choice([0.85, 0.86, 0.87])
                rate2 = round_money(rate1 + random.choice([0.02, 0.03, 0.04]))
                
                bureaux = ['Airport Bureau', 'Bank', 'Post Office', 'Online Exchange']
                bureau1, bureau2 = random.sample(bureaux, 2)
                
                euro_amount = random.choice([200, 300, 500])
                sterling1 = round_money(euro_amount * rate1)
                sterling2 = round_money(euro_amount * rate2)
                
                better = bureau2  # Higher rate is better for EUR to GBP
                difference = round_money(sterling2 - sterling1)
                
                q_text = f"{name} wants to change {format_euro(euro_amount)} to pounds.\\n{bureau1}: €1 = £{rate1}\\n{bureau2}: €1 = £{rate2}\\nWhich gives more pounds, and how much more?"
                
                correct = f"{better}, {format_sterling(difference)} more"
                wrong = [
                    f"{bureau1}, {format_sterling(difference)} more",
                    f"{better}, {format_sterling(difference + 2)} more",
                    f"Same amount at both"
                ]
                
                visual = generate_exchange_board_svg([('EUR', 'GBP', rate1), ('EUR', 'GBP', rate2)])
                explanation = f"{bureau1}: {format_euro(euro_amount)} × {rate1} = {format_sterling(sterling1)}\\n{bureau2}: {format_euro(euro_amount)} × {rate2} = {format_sterling(sterling2)}\\n{better} gives {format_sterling(difference)} more"
                
            elif q_type == 'best_rate_usd':
                rate1 = random.choice([1.08, 1.10, 1.12])
                rate2 = round_money(rate1 + random.choice([0.03, 0.05, 0.08]))
                
                euro_amount = random.choice([300, 400, 500])
                dollars1 = round_money(euro_amount * rate1)
                dollars2 = round_money(euro_amount * rate2)
                
                difference = round_money(dollars2 - dollars1)
                
                q_text = f"{name} is changing {format_euro(euro_amount)} to dollars.\\nBank A offers €1 = ${rate1}\\nBank B offers €1 = ${rate2}\\nHow much more would Bank B give?"
                
                correct = format_dollar(difference)
                wrong = get_unique_wrong_money(difference, 3, 'USD')
                
                visual = None
                explanation = f"Bank A: {format_euro(euro_amount)} × {rate1} = {format_dollar(dollars1)}\\nBank B: {format_euro(euro_amount)} × {rate2} = {format_dollar(dollars2)}\\nDifference: {format_dollar(difference)}"
                
            else:  # rate_difference
                rate = random.choice([0.87, 0.90, 0.93])
                euro_amounts = [100, 200, 500]
                
                euro = random.choice(euro_amounts)
                sterling = round_money(euro * rate)
                
                # If rate changed by 0.05
                new_rate = round_money(rate - 0.05)
                new_sterling = round_money(euro * new_rate)
                difference = round_money(sterling - new_sterling)
                
                q_text = f"The exchange rate drops from €1 = £{rate} to €1 = £{new_rate}.\\nIf you're changing {format_euro(euro)}, how much less sterling would you get?"
                
                correct = format_sterling(difference)
                wrong = get_unique_wrong_money(difference, 3, 'GBP')
                
                visual = None
                explanation = f"Old rate: {format_euro(euro)} × {rate} = {format_sterling(sterling)}\\nNew rate: {format_euro(euro)} × {new_rate} = {format_sterling(new_sterling)}\\nDifference: {format_sterling(difference)} less"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:40]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 10: Commission and Fees (Application)
# ============================================================

def generate_level_10():
    """Currency exchange with commission/fees"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['flat_fee', 'percentage_commission', 'combined']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            rate = random.choice([0.87, 0.90, 0.93])
            
            if q_type == 'flat_fee':
                euro_amount = random.choice([200, 300, 400, 500])
                fee = random.choice([3, 5, 7.50, 10])
                
                amount_after_fee = euro_amount - fee
                sterling = round_money(amount_after_fee * rate)
                
                q_text = f"{name} changes {format_euro(euro_amount)} at a bureau that charges a {format_euro(fee)} flat fee.\\nExchange rate: €1 = £{rate}\\nHow much sterling do they receive?"
                
                correct = format_sterling(sterling)
                wrong = get_unique_wrong_money(sterling, 3, 'GBP')
                
                visual = None
                explanation = f"After fee: {format_euro(euro_amount)} - {format_euro(fee)} = {format_euro(amount_after_fee)}\\nSterling: {format_euro(amount_after_fee)} × {rate} = {format_sterling(sterling)}"
                
            elif q_type == 'percentage_commission':
                euro_amount = random.choice([300, 400, 500, 600])
                commission_pct = random.choice([1, 1.5, 2, 2.5, 3])
                
                commission = round_money(euro_amount * commission_pct / 100)
                amount_after = euro_amount - commission
                sterling = round_money(amount_after * rate)
                
                q_text = f"A bank charges {commission_pct}% commission on currency exchange.\\n{name} changes {format_euro(euro_amount)} at rate €1 = £{rate}.\\nHow much sterling do they get after commission?"
                
                correct = format_sterling(sterling)
                wrong = get_unique_wrong_money(sterling, 3, 'GBP')
                
                visual = None
                explanation = f"Commission: {commission_pct}% of {format_euro(euro_amount)} = {format_euro(commission)}\\nAfter commission: {format_euro(amount_after)}\\nSterling: {format_euro(amount_after)} × {rate} = {format_sterling(sterling)}"
                
            else:  # combined - compare with and without fee
                euro_amount = random.choice([250, 300, 400])
                
                # Option 1: Better rate, with fee
                rate1 = 0.92
                fee = 5
                result1 = round_money((euro_amount - fee) * rate1)
                
                # Option 2: Worse rate, no fee
                rate2 = 0.88
                result2 = round_money(euro_amount * rate2)
                
                better = "Bureau A" if result1 > result2 else "Bureau B"
                difference = abs(result1 - result2)
                
                q_text = f"{name} wants to change {format_euro(euro_amount)}.\\nBureau A: €1 = £{rate1}, {format_euro(fee)} fee\\nBureau B: €1 = £{rate2}, no fee\\nWhich gives more sterling?"
                
                correct = f"{better} by {format_sterling(difference)}"
                other = "Bureau B" if better == "Bureau A" else "Bureau A"
                wrong = [
                    f"{other} by {format_sterling(difference)}",
                    f"{better} by {format_sterling(difference + 2)}",
                    "Same amount"
                ]
                
                visual = None
                explanation = f"Bureau A: ({format_euro(euro_amount)} - {format_euro(fee)}) × {rate1} = {format_sterling(result1)}\\nBureau B: {format_euro(euro_amount)} × {rate2} = {format_sterling(result2)}\\n{better} is better by {format_sterling(difference)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:40]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 11: Travel Budget Problems (Application)
# ============================================================

def generate_level_11():
    """Complex travel budget calculations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['daily_budget', 'return_conversion', 'split_currencies']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'daily_budget':
                gbp_rate = random.choice([0.87, 0.90, 0.93])
                days = random.randint(4, 7)
                daily_sterling = random.randint(50, 80)
                
                total_sterling = daily_sterling * days
                euro_needed = round_money(total_sterling / gbp_rate)
                
                uk_city = random.choice(UK_CITIES)
                q_text = f"{name} is going to {uk_city} for {days} days.\\nThey budget {format_sterling(daily_sterling)} per day.\\nExchange rate: €1 = £{gbp_rate}\\nHow much euro should they bring?"
                
                correct = format_euro(euro_needed)
                wrong = get_unique_wrong_money(euro_needed, 3, 'EUR')
                
                visual = None
                explanation = f"Total needed: {days} × {format_sterling(daily_sterling)} = {format_sterling(total_sterling)}\\nIn euro: {format_sterling(total_sterling)} ÷ {gbp_rate} = {format_euro(euro_needed)}"
                
            elif q_type == 'return_conversion':
                rate_out = random.choice([0.87, 0.90])
                rate_back = round_money(rate_out + random.choice([-0.03, 0.03]))
                
                euro_changed = random.choice([300, 400, 500])
                sterling_received = round_money(euro_changed * rate_out)
                sterling_spent = random.randint(int(sterling_received * 0.6), int(sterling_received * 0.8))
                sterling_left = round_money(sterling_received - sterling_spent)
                euro_back = round_money(sterling_left / rate_back)
                
                q_text = f"{name} changed {format_euro(euro_changed)} at €1 = £{rate_out}.\\nThey spent {format_sterling(sterling_spent)} and changed the rest back at €1 = £{rate_back}.\\nHow much euro did they get back?"
                
                correct = format_euro(euro_back)
                wrong = get_unique_wrong_money(euro_back, 3, 'EUR')
                
                visual = None
                explanation = f"Received: {format_euro(euro_changed)} × {rate_out} = {format_sterling(sterling_received)}\\nLeft over: {format_sterling(sterling_received)} - {format_sterling(sterling_spent)} = {format_sterling(sterling_left)}\\nBack to euro: {format_sterling(sterling_left)} ÷ {rate_back} = {format_euro(euro_back)}"
                
            else:  # split_currencies
                gbp_rate = 0.90
                usd_rate = 1.15
                
                total_euro = random.choice([600, 800, 1000])
                gbp_portion = random.choice([0.4, 0.5, 0.6])
                
                euro_to_gbp = round_money(total_euro * gbp_portion)
                euro_to_usd = total_euro - euro_to_gbp
                
                sterling = round_money(euro_to_gbp * gbp_rate)
                dollars = round_money(euro_to_usd * usd_rate)
                
                q_text = f"{name} changes {format_euro(total_euro)}.\\nThey convert {format_euro(euro_to_gbp)} to sterling (€1 = £{gbp_rate})\\nand {format_euro(euro_to_usd)} to dollars (€1 = ${usd_rate}).\\nHow much sterling do they receive?"
                
                correct = format_sterling(sterling)
                wrong = get_unique_wrong_money(sterling, 3, 'GBP')
                
                visual = None
                explanation = f"Sterling: {format_euro(euro_to_gbp)} × {gbp_rate} = {format_sterling(sterling)}\\n(Dollars would be: {format_euro(euro_to_usd)} × {usd_rate} = {format_dollar(dollars)})"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:40]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
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
# LEVEL 12: Complex Multi-Currency (Mastery)
# ============================================================

def generate_level_12():
    """Complex multi-currency and cross-rate problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    question_types = ['cross_rate', 'percentage_change', 'best_route', 'profit_loss']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'cross_rate':
                # Given EUR/GBP and EUR/USD, find GBP/USD
                eur_gbp = random.choice([0.85, 0.87, 0.90])
                eur_usd = random.choice([1.10, 1.15, 1.20])
                
                # £1 in $ = (€1/£rate) × $/€rate = $/€ ÷ £/€
                gbp_usd = round_money(eur_usd / eur_gbp)
                
                q_text = f"Exchange rates: €1 = £{eur_gbp} and €1 = ${eur_usd}\\nUsing these rates, how many US dollars equal £1?\\n(Calculate £1 in $)"
                
                correct = f"${gbp_usd}"
                wrong = [f"${round_money(gbp_usd * 1.1)}", f"${round_money(gbp_usd * 0.9)}", f"${round_money(eur_gbp * eur_usd)}"]
                
                visual = None
                explanation = f"£1 = €{round_money(1/eur_gbp)} (since €1 = £{eur_gbp})\\n€{round_money(1/eur_gbp)} = ${round_money((1/eur_gbp) * eur_usd)}\\nSo £1 = ${gbp_usd}"
                
            elif q_type == 'percentage_change':
                old_rate = random.choice([0.85, 0.90, 0.95])
                change_pct = random.choice([3, 5, 8, 10])
                
                direction = random.choice(['strengthens', 'weakens'])
                if direction == 'strengthens':
                    new_rate = round_money(old_rate * (1 - change_pct/100))
                else:
                    new_rate = round_money(old_rate * (1 + change_pct/100))
                
                euro_amount = 500
                old_sterling = round_money(euro_amount * old_rate)
                new_sterling = round_money(euro_amount * new_rate)
                difference = abs(old_sterling - new_sterling)
                
                q_text = f"The euro {direction} by {change_pct}% against sterling.\\nOld rate: €1 = £{old_rate}\\nNew rate: €1 = £{new_rate}\\nIf you exchange {format_euro(euro_amount)}, how much {'less' if direction == 'strengthens' else 'more'} sterling do you get?"
                
                correct = format_sterling(difference)
                wrong = get_unique_wrong_money(difference, 3, 'GBP')
                
                visual = None
                explanation = f"Old: {format_euro(euro_amount)} × {old_rate} = {format_sterling(old_sterling)}\\nNew: {format_euro(euro_amount)} × {new_rate} = {format_sterling(new_sterling)}\\nDifference: {format_sterling(difference)}"
                
            elif q_type == 'best_route':
                # Direct vs through another currency
                direct_rate = 0.88
                eur_usd = 1.15
                usd_gbp = 0.78
                
                euro_amount = 400
                direct_sterling = round_money(euro_amount * direct_rate)
                
                # Via USD
                dollars = round_money(euro_amount * eur_usd)
                via_sterling = round_money(dollars * usd_gbp)
                
                better = "Direct" if direct_sterling >= via_sterling else "Via USD"
                difference = abs(direct_sterling - via_sterling)
                
                q_text = f"{name} wants to convert {format_euro(euro_amount)} to sterling.\\nDirect: €1 = £{direct_rate}\\nOr via USD: €1 = ${eur_usd}, then $1 = £{usd_gbp}\\nWhich route gives more sterling?"
                
                correct = f"{better} by {format_sterling(difference)}"
                other = "Via USD" if better == "Direct" else "Direct"
                wrong = [
                    f"{other} by {format_sterling(difference)}",
                    f"{better} by {format_sterling(difference + 3)}",
                    "Same either way"
                ]
                
                visual = None
                explanation = f"Direct: {format_euro(euro_amount)} × {direct_rate} = {format_sterling(direct_sterling)}\\nVia USD: {format_euro(euro_amount)} × {eur_usd} = {format_dollar(dollars)}\\n{format_dollar(dollars)} × {usd_gbp} = {format_sterling(via_sterling)}\\n{better} is better by {format_sterling(difference)}"
                
            else:  # profit_loss
                buy_rate = random.choice([0.85, 0.87, 0.90])
                sell_rate = round_money(buy_rate + random.choice([-0.03, 0.02, 0.05]))
                
                euro_amount = random.choice([500, 1000])
                sterling_bought = round_money(euro_amount * buy_rate)
                euro_sold = round_money(sterling_bought / sell_rate)
                
                if euro_sold > euro_amount:
                    result = f"Profit of {format_euro(round_money(euro_sold - euro_amount))}"
                else:
                    result = f"Loss of {format_euro(round_money(euro_amount - euro_sold))}"
                
                q_text = f"{name} changes {format_euro(euro_amount)} to sterling at €1 = £{buy_rate}.\\nLater, they change it all back at €1 = £{sell_rate}.\\nDid they make a profit or loss, and how much?"
                
                correct = result
                wrong = [
                    result.replace("Profit", "Loss") if "Profit" in result else result.replace("Loss", "Profit"),
                    f"{'Profit' if 'Profit' in result else 'Loss'} of {format_euro(abs(euro_sold - euro_amount) + 5)}",
                    "Broke even"
                ]
                
                visual = None
                explanation = f"Bought: {format_euro(euro_amount)} × {buy_rate} = {format_sterling(sterling_bought)}\\nSold: {format_sterling(sterling_bought)} ÷ {sell_rate} = {format_euro(euro_sold)}\\n{result}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:50]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
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
        
        # Check for duplicate options
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options in '{q['question_text'][:50]}...'")
        
        # Check explanation exists
        if not q.get('explanation'):
            errors.append(f"Level {level}: Missing explanation")
    
    # Print summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    level_names = {
        1: "Understanding Rates",
        2: "EUR to GBP (Simple)",
        3: "EUR to USD (Simple)",
        4: "EUR to GBP (Decimal)",
        5: "GBP to EUR (Reverse)",
        6: "USD Both Ways",
        7: "Price Comparison",
        8: "Multi-step Problems",
        9: "Best Exchange Rate",
        10: "Commission & Fees",
        11: "Travel Budget",
        12: "Complex Multi-Currency"
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
    
    if errors:
        print("\nErrors found:")
        for e in errors[:10]:
            print(f"  - {e}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
    
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
    
    # Delete existing questions for this topic/mode
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
    """, (TOPIC, MODE))
    
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions in {MODE} mode")
    
    # Insert new questions
    inserted = 0
    errors = 0
    
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
            print(f"Error inserting: {e}")
            errors += 1
    
    conn.commit()
    conn.close()
    
    print(f"Inserted {inserted} questions ({errors} errors)")
    return errors == 0

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("CURRENCY - JC EXAM QUESTION GENERATOR")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Questions per level: {QUESTIONS_PER_LEVEL}")
    print(f"Total target: {QUESTIONS_PER_LEVEL * 12}")
    print("=" * 60)
    
    all_questions = []
    
    generators = [
        (1, "Understanding Rates", generate_level_1),
        (2, "EUR to GBP (Simple)", generate_level_2),
        (3, "EUR to USD (Simple)", generate_level_3),
        (4, "EUR to GBP (Decimal)", generate_level_4),
        (5, "GBP to EUR (Reverse)", generate_level_5),
        (6, "USD Both Ways", generate_level_6),
        (7, "Price Comparison", generate_level_7),
        (8, "Multi-step Problems", generate_level_8),
        (9, "Best Exchange Rate", generate_level_9),
        (10, "Commission & Fees", generate_level_10),
        (11, "Travel Budget", generate_level_11),
        (12, "Complex Multi-Currency", generate_level_12),
    ]
    
    for level, name, generator in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = generator()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    # Validate
    error_count = validate_questions(all_questions)
    
    # Ask to insert
    print("=" * 60)
    response = input("Insert questions into database? (y/n): ").strip().lower()
    
    if response == 'y':
        success = insert_questions(all_questions)
        if success:
            print("\n✓ Questions inserted successfully!")
        else:
            print("\n✗ Some errors occurred during insertion")
    else:
        print("Skipped database insertion.")
    
    print("\nDone!")

if __name__ == "__main__":
    main()
