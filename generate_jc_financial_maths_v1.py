#!/usr/bin/env python3
"""
AgentMath - Financial Maths Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q2(a): Money calculations, change
- 2022 OL Q9(a-d): Profit, cost, selling price
- 2022 OL Q3(d): Currency conversion (£ to €)
- 2022 HL Q1(a): Currency conversion (€ to $)
- 2022 HL Q1(b): Income tax with tax credits
- 2023 HL Q10: USC tax bands calculation
- 2024 OL Q2(a-c): Shopping, wages, overtime, tax
- 2024 HL Q3(a-c): Wages, tax, compound interest
- 2025 OL Q2(a): Money calculations
- 2025 OL Q9(a-c): Savings, simple interest, interest rate
- 2025 OL Q12(c): Currency comparison
- 2025 HL Q1(b): Percentage discount
- 2025 HL Q3: Bills with VAT

Level Structure:
  L1-3:   Foundation (75% visual)
  L4-6:   Ordinary (75% visual)
  L7-9:   Higher (75% visual)
  L10-12: Application/Mastery (L10: 75%, L11-12: 50%)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os
from decimal import Decimal, ROUND_HALF_UP

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'applied_arithmetic'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Róisín', 'Seán', 
               'Ciara', 'Darragh', 'Éabha', 'Fionn', 'Gráinne', 'Liam', 'Meadhbh', 'Tadhg',
               'Áine', 'Cillian', 'Orlaith', 'Pádraig', 'Sinéad', 'Eoin', 'Caoimhe', 'Declan',
               'Lily', 'Noah', 'Alice', 'Tomás', 'Jane', 'Michelle', 'Mae', 'Margaret', 'John']

# Irish shops/restaurants
IRISH_SHOPS = ['Dunnes', 'Tesco', 'SuperValu', 'Aldi', 'Lidl', 'Centra', 'Spar']
IRISH_RESTAURANTS = ['Eddie Rockets', 'Supermacs', 'Apache Pizza', 'Four Star Pizza']

# Jobs for wage calculations
JOBS = ['chef', 'shop assistant', 'barista', 'waiter', 'receptionist', 'lifeguard', 
        'cinema worker', 'retail assistant', 'office worker', 'delivery driver']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def round_money(value):
    """Round to 2 decimal places for money"""
    return float(Decimal(str(value)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

def format_money(value):
    """Format as euro amount"""
    rounded = round_money(value)
    if rounded == int(rounded):
        return f"€{int(rounded)}"
    return f"€{rounded:.2f}"

def get_unique_wrong_money(correct_val, count=3):
    """Generate unique wrong money options"""
    correct_rounded = round_money(correct_val)
    wrong = set()
    
    # Try nearby values
    candidates = [
        correct_rounded + 0.10, correct_rounded - 0.10,
        correct_rounded + 1, correct_rounded - 1,
        correct_rounded + 0.50, correct_rounded - 0.50,
        correct_rounded * 1.1, correct_rounded * 0.9,
        correct_rounded + 5, correct_rounded - 5,
        correct_rounded * 2, correct_rounded / 2
    ]
    
    for c in candidates:
        c_rounded = round_money(c)
        if c_rounded > 0 and c_rounded != correct_rounded and len(wrong) < count:
            wrong.add(c_rounded)
    
    # Fill with random if needed
    while len(wrong) < count:
        w = round_money(random.uniform(max(0.50, correct_rounded * 0.5), correct_rounded * 2))
        if w > 0 and w != correct_rounded and w not in wrong:
            wrong.add(w)
    
    return [format_money(w) for w in list(wrong)[:count]]

def get_unique_wrong_numbers(correct_val, count=3, min_val=1, max_val=1000):
    """Generate unique wrong number options"""
    wrong = set()
    
    candidates = [correct_val + 1, correct_val - 1, correct_val + 5, correct_val - 5,
                  correct_val + 10, correct_val - 10, correct_val * 2, int(correct_val / 2)]
    
    for c in candidates:
        if c != correct_val and c >= min_val and c <= max_val and len(wrong) < count:
            wrong.add(c)
    
    while len(wrong) < count:
        w = random.randint(min_val, max_val)
        if w != correct_val and w not in wrong:
            wrong.add(w)
    
    return list(wrong)[:count]

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

def generate_receipt_svg(items, total):
    """Generate SVG receipt visual"""
    width = 220
    height = 40 + len(items) * 25 + 40
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fffbeb" stroke="#d97706" stroke-width="2" rx="5"/>'
    
    # Header
    svg += f'<text x="110" y="25" text-anchor="middle" font-size="14" fill="#92400e" font-weight="bold">🧾 Receipt</text>'
    svg += f'<line x1="10" y1="35" x2="210" y2="35" stroke="#d97706" stroke-width="1"/>'
    
    # Items
    y = 55
    for item, price in items:
        svg += f'<text x="15" y="{y}" font-size="11" fill="#374151">{item}</text>'
        svg += f'<text x="205" y="{y}" text-anchor="end" font-size="11" fill="#374151">{format_money(price)}</text>'
        y += 25
    
    # Total line
    svg += f'<line x1="10" y1="{y - 10}" x2="210" y2="{y - 10}" stroke="#d97706" stroke-width="1"/>'
    svg += f'<text x="15" y="{y + 10}" font-size="12" fill="#92400e" font-weight="bold">Total:</text>'
    svg += f'<text x="205" y="{y + 10}" text-anchor="end" font-size="12" fill="#92400e" font-weight="bold">{format_money(total)}</text>'
    
    svg += '</svg>'
    return svg

def generate_wage_slip_svg(name, hours, rate, gross, deductions=None, net=None):
    """Generate SVG wage slip visual"""
    width = 260
    height = 150 if deductions else 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ecfdf5" stroke="#059669" stroke-width="2" rx="5"/>'
    
    # Header
    svg += f'<text x="130" y="22" text-anchor="middle" font-size="13" fill="#065f46" font-weight="bold">💰 Pay Slip</text>'
    svg += f'<line x1="10" y1="30" x2="250" y2="30" stroke="#059669" stroke-width="1"/>'
    
    # Details
    svg += f'<text x="15" y="50" font-size="11" fill="#374151">Employee: {name}</text>'
    svg += f'<text x="15" y="68" font-size="11" fill="#374151">Hours: {hours} × {format_money(rate)}/hr</text>'
    svg += f'<text x="15" y="86" font-size="11" fill="#059669" font-weight="bold">Gross Pay: {format_money(gross)}</text>'
    
    if deductions and net:
        svg += f'<line x1="10" y1="95" x2="250" y2="95" stroke="#059669" stroke-width="1"/>'
        svg += f'<text x="15" y="112" font-size="10" fill="#dc2626">Tax: -{format_money(deductions["tax"])}</text>'
        if "credits" in deductions:
            svg += f'<text x="130" y="112" font-size="10" fill="#059669">Credits: +{format_money(deductions["credits"])}</text>'
        svg += f'<text x="15" y="135" font-size="12" fill="#065f46" font-weight="bold">Net Pay: {format_money(net)}</text>'
    
    svg += '</svg>'
    return svg

def generate_currency_svg(from_curr, to_curr, rate, amount, result):
    """Generate SVG for currency conversion"""
    width = 260
    height = 80
    
    symbols = {'EUR': '€', 'GBP': '£', 'USD': '$', 'JPY': '¥'}
    from_sym = symbols.get(from_curr, from_curr)
    to_sym = symbols.get(to_curr, to_curr)
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#eff6ff" stroke="#3b82f6" stroke-width="2" rx="8"/>'
    
    # From amount
    svg += f'<rect x="20" y="20" width="80" height="40" fill="#dbeafe" rx="5"/>'
    svg += f'<text x="60" y="45" text-anchor="middle" font-size="14" fill="#1e40af" font-weight="bold">{from_sym}{amount}</text>'
    
    # Arrow with rate
    svg += f'<text x="130" y="35" text-anchor="middle" font-size="10" fill="#6b7280">Rate: {rate}</text>'
    svg += f'<text x="130" y="52" text-anchor="middle" font-size="16" fill="#3b82f6">→</text>'
    
    # To amount
    svg += f'<rect x="160" y="20" width="80" height="40" fill="#dcfce7" rx="5"/>'
    svg += f'<text x="200" y="45" text-anchor="middle" font-size="14" fill="#166534" font-weight="bold">{to_sym}{result}</text>'
    
    svg += '</svg>'
    return svg

def generate_interest_svg(principal, rate, time, interest, final_amount):
    """Generate SVG for interest calculation"""
    width = 240
    height = 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="8"/>'
    
    # Header
    svg += f'<text x="120" y="22" text-anchor="middle" font-size="12" fill="#92400e" font-weight="bold">🏦 Savings Account</text>'
    
    # Details
    svg += f'<text x="20" y="45" font-size="11" fill="#374151">Principal: {format_money(principal)}</text>'
    svg += f'<text x="140" y="45" font-size="11" fill="#374151">Rate: {rate}%</text>'
    svg += f'<text x="20" y="65" font-size="11" fill="#374151">Time: {time} year{"s" if time > 1 else ""}</text>'
    svg += f'<text x="140" y="65" font-size="11" fill="#059669">Interest: {format_money(interest)}</text>'
    
    # Final
    svg += f'<line x1="10" y1="75" x2="230" y2="75" stroke="#d97706" stroke-width="1"/>'
    svg += f'<text x="120" y="92" text-anchor="middle" font-size="13" fill="#065f46" font-weight="bold">Total: {format_money(final_amount)}</text>'
    
    svg += '</svg>'
    return svg

def generate_profit_loss_svg(cost, selling, profit, is_profit=True):
    """Generate SVG for profit/loss calculation"""
    width = 260
    height = 90
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    color = "#059669" if is_profit else "#dc2626"
    bg_color = "#ecfdf5" if is_profit else "#fef2f2"
    
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="{bg_color}" stroke="{color}" stroke-width="2" rx="8"/>'
    
    # Cost and Selling
    svg += f'<text x="20" y="28" font-size="12" fill="#374151">Cost Price: {format_money(cost)}</text>'
    svg += f'<text x="20" y="50" font-size="12" fill="#374151">Selling Price: {format_money(selling)}</text>'
    
    # Profit/Loss
    svg += f'<line x1="10" y1="60" x2="250" y2="60" stroke="{color}" stroke-width="1"/>'
    label = "Profit" if is_profit else "Loss"
    svg += f'<text x="20" y="80" font-size="14" fill="{color}" font-weight="bold">{label}: {format_money(abs(profit))}</text>'
    
    svg += '</svg>'
    return svg

def generate_bill_svg(items, subtotal, vat_rate, vat_amount, total):
    """Generate SVG for bill with VAT"""
    width = 260
    height = 60 + len(items) * 22 + 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f8fafc" stroke="#475569" stroke-width="2" rx="5"/>'
    
    # Header
    svg += f'<text x="130" y="25" text-anchor="middle" font-size="14" fill="#1e293b" font-weight="bold">📋 Invoice</text>'
    svg += f'<line x1="10" y1="35" x2="250" y2="35" stroke="#94a3b8" stroke-width="1"/>'
    
    # Items
    y = 55
    for item, qty, price in items:
        svg += f'<text x="15" y="{y}" font-size="10" fill="#374151">{item} × {qty}</text>'
        svg += f'<text x="245" y="{y}" text-anchor="end" font-size="10" fill="#374151">{format_money(price * qty)}</text>'
        y += 22
    
    # Subtotal, VAT, Total
    svg += f'<line x1="10" y1="{y}" x2="250" y2="{y}" stroke="#94a3b8" stroke-width="1"/>'
    y += 18
    svg += f'<text x="15" y="{y}" font-size="11" fill="#374151">Subtotal:</text>'
    svg += f'<text x="245" y="{y}" text-anchor="end" font-size="11" fill="#374151">{format_money(subtotal)}</text>'
    y += 20
    svg += f'<text x="15" y="{y}" font-size="11" fill="#374151">VAT ({vat_rate}%):</text>'
    svg += f'<text x="245" y="{y}" text-anchor="end" font-size="11" fill="#374151">{format_money(vat_amount)}</text>'
    y += 22
    svg += f'<line x1="10" y1="{y - 8}" x2="250" y2="{y - 8}" stroke="#1e293b" stroke-width="2"/>'
    svg += f'<text x="15" y="{y + 8}" font-size="13" fill="#1e293b" font-weight="bold">TOTAL:</text>'
    svg += f'<text x="245" y="{y + 8}" text-anchor="end" font-size="13" fill="#1e293b" font-weight="bold">{format_money(total)}</text>'
    
    svg += '</svg>'
    return svg

def generate_tax_bands_svg(gross, bands, total_tax, credits=0, net=0):
    """Generate SVG for tax band calculation"""
    width = 280
    height = 140
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fef2f2" stroke="#dc2626" stroke-width="2" rx="8"/>'
    
    # Header
    svg += f'<text x="140" y="22" text-anchor="middle" font-size="12" fill="#991b1b" font-weight="bold">📊 Tax Calculation</text>'
    svg += f'<text x="140" y="38" font-size="10" fill="#374151">Gross Income: {format_money(gross)}</text>'
    
    # Bands
    y = 58
    for band_name, amount, rate, tax in bands:
        svg += f'<text x="15" y="{y}" font-size="9" fill="#374151">{band_name}: {format_money(amount)} @ {rate}%</text>'
        svg += f'<text x="265" y="{y}" text-anchor="end" font-size="9" fill="#dc2626">{format_money(tax)}</text>'
        y += 16
    
    # Total and Net
    svg += f'<line x1="10" y1="{y}" x2="270" y2="{y}" stroke="#dc2626" stroke-width="1"/>'
    y += 15
    svg += f'<text x="15" y="{y}" font-size="10" fill="#374151">Total Tax:</text>'
    svg += f'<text x="265" y="{y}" text-anchor="end" font-size="10" fill="#dc2626">{format_money(total_tax)}</text>'
    
    if credits > 0:
        y += 14
        svg += f'<text x="15" y="{y}" font-size="10" fill="#059669">Tax Credits:</text>'
        svg += f'<text x="265" y="{y}" text-anchor="end" font-size="10" fill="#059669">-{format_money(credits)}</text>'
    
    y += 16
    svg += f'<text x="15" y="{y}" font-size="11" fill="#065f46" font-weight="bold">Net Income:</text>'
    svg += f'<text x="265" y="{y}" text-anchor="end" font-size="11" fill="#065f46" font-weight="bold">{format_money(net)}</text>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Money Calculations - Basic (Foundation)
# ============================================================

def generate_level_1():
    """Money Calculations - Adding costs, giving change"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['total_cost', 'calculate_change', 'cost_per_item', 'compare_prices']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            if q_type == 'total_cost':
                # SEC 2024 OL Q2(a) style
                name = random.choice(IRISH_NAMES)
                shop = random.choice(IRISH_SHOPS)
                
                items = []
                item_names = random.sample(['milk', 'bread', 'cheese', 'apples', 'juice', 'pasta', 'eggs'], 3)
                for item in item_names:
                    price = round_money(random.uniform(0.99, 4.99))
                    items.append((item.capitalize(), price))
                
                total = sum(p for _, p in items)
                
                q_text = f"{name} buys the following at {shop}:\\n"
                q_text += "\\n".join([f"• {item}: {format_money(price)}" for item, price in items])
                q_text += "\\n\\nWhat is the total cost?"
                
                correct = format_money(total)
                wrong = get_unique_wrong_money(total, 3)
                
                visual = generate_receipt_svg(items, total)
                explanation = f"Total = {' + '.join([format_money(p) for _, p in items])} = {format_money(total)}"
                
            elif q_type == 'calculate_change':
                # SEC 2022 OL Q2(a)(ii) style
                name = random.choice(IRISH_NAMES)
                bill = round_money(random.uniform(15, 45))
                paid = random.choice([20, 50, 100])
                while paid < bill:
                    paid = random.choice([20, 50, 100])
                
                change = paid - bill
                
                q_text = f"{name}'s bill is {format_money(bill)}. They pay with {format_money(paid)}.\\nHow much change do they get?"
                correct = format_money(change)
                wrong = get_unique_wrong_money(change, 3)
                
                visual = None
                explanation = f"Change = {format_money(paid)} − {format_money(bill)} = {format_money(change)}"
                
            elif q_type == 'cost_per_item':
                # SEC 2025 OL Q2(a) style
                name = random.choice(IRISH_NAMES)
                item = random.choice(['chocolate bars', 'notebooks', 'pens', 'bottles of water'])
                qty = random.randint(2, 5)
                price_each = round_money(random.uniform(1.50, 4.99))
                total_paid = round_money(qty * price_each + random.uniform(5, 15))
                change = round_money(total_paid - qty * price_each)
                
                q_text = f"{name} buys {qty} {item}. They pay {format_money(total_paid)} and get {format_money(change)} change.\\nWhat is the cost of one {item.rstrip('s')}?"
                
                correct = format_money(price_each)
                wrong = get_unique_wrong_money(price_each, 3)
                
                visual = None
                total_cost = total_paid - change
                explanation = f"Total cost = {format_money(total_paid)} − {format_money(change)} = {format_money(total_cost)}\\n" \
                             f"Cost per item = {format_money(total_cost)} ÷ {qty} = {format_money(price_each)}"
                
            else:  # compare_prices
                item = random.choice(['pizza', 'coffee', 'sandwich', 'burger'])
                shop1 = random.choice(IRISH_SHOPS[:3])
                shop2 = random.choice(IRISH_SHOPS[3:])
                price1 = round_money(random.uniform(5, 12))
                price2 = round_money(price1 + random.choice([-1.50, -1, -0.50, 0.50, 1, 1.50]))
                
                cheaper = shop1 if price1 < price2 else shop2
                saving = abs(price1 - price2)
                
                q_text = f"A {item} costs {format_money(price1)} at {shop1} and {format_money(price2)} at {shop2}.\\nHow much would you save by buying from the cheaper shop?"
                
                correct = format_money(saving)
                wrong = get_unique_wrong_money(saving, 3)
                
                visual = None
                explanation = f"Saving = {format_money(max(price1, price2))} − {format_money(min(price1, price2))} = {format_money(saving)}\\n{cheaper} is cheaper."
            
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
# LEVEL 2: Profit and Loss - Basic (Foundation)
# ============================================================

def generate_level_2():
    """Profit and Loss - Cost, selling price, profit"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['find_profit', 'find_selling', 'find_cost', 'profit_word']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            item = random.choice(['chair', 'table', 'lamp', 'bookshelf', 'desk', 'painting'])
            
            if q_type == 'find_profit':
                # SEC 2022 OL Q9(a) style
                cost = random.randint(50, 200)
                selling = cost + random.randint(20, 80)
                profit = selling - cost
                
                q_text = f"{name} makes a {item}. It costs {format_money(cost)} to make and sells for {format_money(selling)}.\\nWork out the profit."
                correct = format_money(profit)
                wrong = get_unique_wrong_money(profit, 3)
                
                visual = generate_profit_loss_svg(cost, selling, profit, True)
                explanation = f"Profit = Selling Price − Cost\\n= {format_money(selling)} − {format_money(cost)}\\n= {format_money(profit)}"
                
            elif q_type == 'find_selling':
                # SEC 2022 OL Q9(b) style
                cost = random.randint(80, 180)
                profit = random.randint(30, 70)
                selling = cost + profit
                
                q_text = f"{name} makes a {item}. It costs {format_money(cost)} to make. They make a profit of {format_money(profit)}.\\nFind the selling price."
                correct = format_money(selling)
                wrong = get_unique_wrong_money(selling, 3)
                
                visual = generate_profit_loss_svg(cost, selling, profit, True)
                explanation = f"Selling Price = Cost + Profit\\n= {format_money(cost)} + {format_money(profit)}\\n= {format_money(selling)}"
                
            elif q_type == 'find_cost':
                selling = random.randint(100, 250)
                profit = random.randint(25, 60)
                cost = selling - profit
                
                q_text = f"{name} sells a {item} for {format_money(selling)}. They make a profit of {format_money(profit)}.\\nWhat did it cost to make?"
                correct = format_money(cost)
                wrong = get_unique_wrong_money(cost, 3)
                
                visual = generate_profit_loss_svg(cost, selling, profit, True)
                explanation = f"Cost = Selling Price − Profit\\n= {format_money(selling)} − {format_money(profit)}\\n= {format_money(cost)}"
                
            else:  # profit_word
                cost = random.randint(40, 120)
                selling = cost + random.randint(15, 50)
                profit = selling - cost
                
                q_text = f"A shop buys an item for {format_money(cost)} and sells it for {format_money(selling)}.\\nIs this a profit or loss, and how much?"
                correct = f"Profit of {format_money(profit)}"
                wrong = [f"Loss of {format_money(profit)}", f"Profit of {format_money(cost)}", f"Loss of {format_money(selling - cost + 10)}"]
                
                visual = generate_profit_loss_svg(cost, selling, profit, True)
                explanation = f"Since Selling Price ({format_money(selling)}) > Cost ({format_money(cost)}), it's a profit.\\nProfit = {format_money(selling)} − {format_money(cost)} = {format_money(profit)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{item}_{cost if 'cost' in dir() else selling}"
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
# LEVEL 3: Wages - Basic (Foundation)
# ============================================================

def generate_level_3():
    """Wages - Hourly rate calculations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['find_earnings', 'find_hours', 'find_rate', 'weekly_wage']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            job = random.choice(JOBS)
            
            if q_type == 'find_earnings':
                hours = random.randint(5, 12)
                rate = round_money(random.choice([12.70, 13.00, 14.00, 15.00, 16.00, 18.00]))
                earnings = hours * rate
                
                q_text = f"{name} works as a {job}. They work {hours} hours at {format_money(rate)} per hour.\\nHow much do they earn?"
                correct = format_money(earnings)
                wrong = get_unique_wrong_money(earnings, 3)
                
                visual = generate_wage_slip_svg(name, hours, rate, earnings)
                explanation = f"Earnings = Hours × Rate\\n= {hours} × {format_money(rate)}\\n= {format_money(earnings)}"
                
            elif q_type == 'find_hours':
                rate = round_money(random.choice([12.70, 14.00, 15.00, 16.00]))
                hours = random.randint(6, 10)
                earnings = hours * rate
                
                q_text = f"{name} earns {format_money(earnings)} at {format_money(rate)} per hour.\\nHow many hours did they work?"
                correct = str(hours)
                wrong = [str(w) for w in get_unique_wrong_numbers(hours, 3, 3, 15)]
                
                visual = generate_wage_slip_svg(name, "?", rate, earnings)
                explanation = f"Hours = Earnings ÷ Rate\\n= {format_money(earnings)} ÷ {format_money(rate)}\\n= {hours} hours"
                
            elif q_type == 'find_rate':
                hours = random.randint(6, 10)
                rate = round_money(random.choice([13.00, 14.00, 15.00, 16.00]))
                earnings = hours * rate
                
                q_text = f"{name} works {hours} hours and earns {format_money(earnings)}.\\nWhat is their hourly rate?"
                correct = format_money(rate)
                wrong = get_unique_wrong_money(rate, 3)
                
                visual = generate_wage_slip_svg(name, hours, "?", earnings)
                explanation = f"Hourly Rate = Earnings ÷ Hours\\n= {format_money(earnings)} ÷ {hours}\\n= {format_money(rate)} per hour"
                
            else:  # weekly_wage
                days = random.randint(4, 6)
                hours_per_day = random.randint(6, 8)
                rate = round_money(random.choice([13.00, 14.00, 15.00]))
                total_hours = days * hours_per_day
                earnings = total_hours * rate
                
                q_text = f"{name} works {days} days a week, {hours_per_day} hours each day, at {format_money(rate)}/hour.\\nWhat is their weekly wage?"
                correct = format_money(earnings)
                wrong = get_unique_wrong_money(earnings, 3)
                
                visual = generate_wage_slip_svg(name, total_hours, rate, earnings)
                explanation = f"Total hours = {days} × {hours_per_day} = {total_hours} hours\\nWeekly wage = {total_hours} × {format_money(rate)} = {format_money(earnings)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{name}_{q_text[:30]}"
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
# LEVEL 4: Overtime and Percentage Increases (Ordinary)
# ============================================================

def generate_level_4():
    """Overtime - Time and a half, double time"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['time_half', 'double_time', 'mixed_week', 'percentage_rise']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            job = random.choice(JOBS)
            base_rate = round_money(random.choice([15.00, 16.00, 17.00, 18.00, 19.00]))
            
            if q_type == 'time_half':
                # SEC 2024 OL Q2(b)(ii) style - 50% extra
                hours = random.randint(4, 8)
                overtime_rate = base_rate * 1.5
                earnings = hours * overtime_rate
                
                q_text = f"{name}'s basic rate is {format_money(base_rate)}/hour. On Sundays, they get 50% extra (time and a half).\\nThey work {hours} hours on Sunday. How much do they earn?"
                correct = format_money(earnings)
                wrong = get_unique_wrong_money(earnings, 3)
                
                visual = None
                explanation = f"Overtime rate = {format_money(base_rate)} × 1.5 = {format_money(overtime_rate)}/hour\\nSunday earnings = {hours} × {format_money(overtime_rate)} = {format_money(earnings)}"
                
            elif q_type == 'double_time':
                hours = random.randint(4, 6)
                double_rate = base_rate * 2
                earnings = hours * double_rate
                
                q_text = f"{name} earns {format_money(base_rate)}/hour normally. On bank holidays, they get double time.\\nThey work {hours} hours on a bank holiday. How much do they earn?"
                correct = format_money(earnings)
                wrong = get_unique_wrong_money(earnings, 3)
                
                visual = None
                explanation = f"Double time rate = {format_money(base_rate)} × 2 = {format_money(double_rate)}/hour\\nEarnings = {hours} × {format_money(double_rate)} = {format_money(earnings)}"
                
            elif q_type == 'mixed_week':
                # SEC 2024 OL Q2(b) style - weekday + weekend
                weekday_hours = random.randint(12, 18)
                sunday_hours = random.randint(4, 8)
                overtime_rate = base_rate * 1.5
                
                weekday_pay = weekday_hours * base_rate
                sunday_pay = sunday_hours * overtime_rate
                total = weekday_pay + sunday_pay
                
                q_text = f"{name} works as a {job} at {format_money(base_rate)}/hour.\\nThis week: {weekday_hours} hours (normal rate) and {sunday_hours} hours on Sunday (time and a half).\\nFind their total earnings."
                correct = format_money(total)
                wrong = get_unique_wrong_money(total, 3)
                
                visual = None
                explanation = f"Normal pay: {weekday_hours} × {format_money(base_rate)} = {format_money(weekday_pay)}\\n" \
                             f"Sunday (×1.5): {sunday_hours} × {format_money(overtime_rate)} = {format_money(sunday_pay)}\\n" \
                             f"Total: {format_money(weekday_pay)} + {format_money(sunday_pay)} = {format_money(total)}"
                
            else:  # percentage_rise
                old_rate = round_money(random.choice([14.00, 15.00, 16.00]))
                increase_pct = random.choice([3, 4, 5, 6])
                increase = old_rate * increase_pct / 100
                new_rate = old_rate + increase
                
                q_text = f"{name} earns {format_money(old_rate)}/hour. They get a {increase_pct}% pay rise.\\nWhat is their new hourly rate?"
                correct = format_money(new_rate)
                wrong = get_unique_wrong_money(new_rate, 3)
                
                visual = None
                explanation = f"Increase = {increase_pct}% of {format_money(old_rate)}\\n= {format_money(old_rate)} × {increase_pct/100} = {format_money(increase)}\\nNew rate = {format_money(old_rate)} + {format_money(increase)} = {format_money(new_rate)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{name}_{base_rate}"
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
# LEVEL 5: Simple Interest (Ordinary)
# ============================================================

def generate_level_5():
    """Simple Interest calculations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['find_interest', 'find_total', 'find_rate', 'sec_style']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'find_interest':
                # SEC 2025 OL Q9(b)(i) style
                principal = random.choice([100, 120, 130, 150, 200, 250, 500])
                rate = random.choice([2, 2.5, 3, 3.5, 4, 5])
                interest = principal * rate / 100
                
                q_text = f"{name} puts {format_money(principal)} in a savings account at {rate}% annual interest.\\nHow much interest do they earn in one year?"
                correct = format_money(interest)
                wrong = get_unique_wrong_money(interest, 3)
                
                visual = generate_interest_svg(principal, rate, 1, interest, principal + interest)
                explanation = f"Interest = Principal × Rate\\n= {format_money(principal)} × {rate}%\\n= {format_money(principal)} × {rate/100}\\n= {format_money(interest)}"
                
            elif q_type == 'find_total':
                # SEC 2025 OL Q9(b)(ii) style
                principal = random.choice([100, 130, 150, 200, 300])
                rate = random.choice([2, 3, 4, 5])
                interest = principal * rate / 100
                total = principal + interest
                
                q_text = f"{name} invests {format_money(principal)} at {rate}% simple interest for 1 year.\\nWhat is the total amount after one year?"
                correct = format_money(total)
                wrong = get_unique_wrong_money(total, 3)
                
                visual = generate_interest_svg(principal, rate, 1, interest, total)
                explanation = f"Interest = {format_money(principal)} × {rate}% = {format_money(interest)}\\nTotal = {format_money(principal)} + {format_money(interest)} = {format_money(total)}"
                
            elif q_type == 'find_rate':
                # SEC 2025 OL Q9(c) style
                principal = random.choice([100, 120, 150, 200])
                rate = random.choice([3, 3.5, 3.8, 4, 4.5])
                interest = principal * rate / 100
                final = principal + interest
                
                q_text = f"{name} puts {format_money(principal)} in a Credit Union account. After one year, they have {format_money(final)}.\\nFind the percentage annual interest rate."
                correct = f"{rate}%"
                wrong = [f"{rate + 0.5}%", f"{rate - 0.5}%", f"{rate + 1}%"]
                
                visual = generate_interest_svg(principal, "?", 1, interest, final)
                explanation = f"Interest earned = {format_money(final)} − {format_money(principal)} = {format_money(interest)}\\n" \
                             f"Rate = ({format_money(interest)} ÷ {format_money(principal)}) × 100 = {rate}%"
                
            else:  # sec_style - multiple years
                principal = random.choice([200, 300, 400, 500])
                rate = random.choice([2, 3, 4])
                years = random.choice([2, 3])
                interest_per_year = principal * rate / 100
                total_interest = interest_per_year * years
                final = principal + total_interest
                
                q_text = f"{name} invests {format_money(principal)} at {rate}% simple interest for {years} years.\\nWhat is the total interest earned?"
                correct = format_money(total_interest)
                wrong = get_unique_wrong_money(total_interest, 3)
                
                visual = generate_interest_svg(principal, rate, years, total_interest, final)
                explanation = f"Interest per year = {format_money(principal)} × {rate}% = {format_money(interest_per_year)}\\n" \
                             f"Total interest for {years} years = {format_money(interest_per_year)} × {years} = {format_money(total_interest)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{principal}_{rate}"
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
# LEVEL 6: Currency Conversion (Ordinary)
# ============================================================

def generate_level_6():
    """Currency Conversion - EUR to GBP, USD"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['eur_to_gbp', 'gbp_to_eur', 'eur_to_usd', 'comparison']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'eur_to_gbp':
                # SEC 2022 HL Q1(a) style (but to GBP)
                amount = random.choice([100, 150, 200, 250, 300, 350])
                rate = round_money(random.choice([0.85, 0.87, 0.88, 0.90, 0.93]))
                result = round_money(amount * rate)
                
                q_text = f"{name} changes {format_money(amount)} to British pounds.\\nExchange rate: €1 = £{rate}\\nHow many pounds do they get?"
                correct = f"£{result:.2f}"
                wrong = [f"£{round_money(result * 1.1):.2f}", f"£{round_money(result * 0.9):.2f}", f"£{round_money(amount / rate):.2f}"]
                
                visual = generate_currency_svg('EUR', 'GBP', f"€1 = £{rate}", amount, f"{result:.2f}")
                explanation = f"Pounds = Euro × Rate\\n= {format_money(amount)} × {rate}\\n= £{result:.2f}"
                
            elif q_type == 'gbp_to_eur':
                # SEC 2022 OL Q3(d) style
                amount = round_money(random.choice([10, 15, 20, 25, 50]))
                rate = round_money(random.choice([0.85, 0.87, 0.90, 0.93]))
                result = round_money(amount / rate)
                
                q_text = f"{name} buys an item for £{amount:.2f} in London.\\nExchange rate: €1 = £{rate}\\nHow much is this in euro (to nearest cent)?"
                correct = format_money(result)
                wrong = get_unique_wrong_money(result, 3)
                
                visual = generate_currency_svg('GBP', 'EUR', f"€1 = £{rate}", f"{amount:.2f}", f"{result:.2f}")
                explanation = f"To convert £ to €, divide by rate:\\n= £{amount:.2f} ÷ {rate}\\n= {format_money(result)}"
                
            elif q_type == 'eur_to_usd':
                # SEC 2022 HL Q1(a) style
                amount = random.choice([200, 300, 350, 400, 500])
                rate = round_money(random.choice([1.08, 1.10, 1.12, 1.15, 1.20]))
                result = round_money(amount * rate)
                
                q_text = f"{name} changes {format_money(amount)} to US dollars.\\nExchange rate: €1 = ${rate}\\nHow many dollars do they get?"
                correct = f"${result:.2f}"
                wrong = [f"${round_money(result * 1.1):.2f}", f"${round_money(result * 0.9):.2f}", f"${round_money(amount / rate):.2f}"]
                
                visual = generate_currency_svg('EUR', 'USD', f"€1 = ${rate}", amount, f"{result:.2f}")
                explanation = f"Dollars = Euro × Rate\\n= {format_money(amount)} × {rate}\\n= ${result:.2f}"
                
            else:  # comparison - SEC 2025 OL Q12(c) style
                item = random.choice(['pizza', 'coffee', 'book', 't-shirt'])
                eur_price = round_money(random.uniform(8, 18))
                rate = round_money(random.choice([0.85, 0.87, 0.90, 0.93]))
                gbp_price = round_money(eur_price * rate * random.choice([0.9, 0.95, 1.05, 1.1]))
                
                eur_equiv = round_money(gbp_price / rate)
                cheaper = "Ireland" if eur_price < eur_equiv else "London"
                saving = abs(eur_price - eur_equiv)
                
                q_text = f"A {item} costs {format_money(eur_price)} in Ireland and £{gbp_price:.2f} in London.\\nExchange rate: €1 = £{rate}\\nWhich is cheaper, and by how much?"
                correct = f"{cheaper} by {format_money(saving)}"
                wrong = [
                    f"{'London' if cheaper == 'Ireland' else 'Ireland'} by {format_money(saving)}",
                    f"{cheaper} by {format_money(saving + 1)}",
                    f"Same price"
                ]
                
                visual = None
                explanation = f"Convert £{gbp_price:.2f} to euro: £{gbp_price:.2f} ÷ {rate} = {format_money(eur_equiv)}\\n" \
                             f"Ireland: {format_money(eur_price)}, London: {format_money(eur_equiv)}\\n" \
                             f"{cheaper} is cheaper by {format_money(saving)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{amount}_{rate}"
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
# LEVEL 7: Percentage Profit/Loss/Discount (Higher)
# ============================================================

def generate_level_7():
    """Percentage Profit, Loss, Discount"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['pct_profit', 'pct_discount', 'profit_as_pct_cost', 'find_original']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'pct_profit':
                # SEC 2024 HL Q4(b) style
                cost = random.choice([4, 5, 5.50, 6, 8, 10])
                revenue = round_money(cost * random.uniform(1.3, 1.8))
                profit = revenue - cost
                pct_profit = round_money((profit / cost) * 100)
                
                q_text = f"{name} buys items for {format_money(cost)} and sells them for {format_money(revenue)}.\\nWork out the profit as a percentage of the cost (to 1 d.p.)."
                correct = f"{pct_profit}%"
                wrong = [f"{round_money(pct_profit + 5)}%", f"{round_money(pct_profit - 5)}%", f"{round_money((profit/revenue)*100)}%"]
                
                visual = generate_profit_loss_svg(cost, revenue, profit, True)
                explanation = f"Profit = {format_money(revenue)} − {format_money(cost)} = {format_money(profit)}\\n" \
                             f"% Profit = (Profit ÷ Cost) × 100\\n= ({format_money(profit)} ÷ {format_money(cost)}) × 100\\n= {pct_profit}%"
                
            elif q_type == 'pct_discount':
                # SEC 2025 HL Q1(b) style
                original = random.choice([80, 100, 120, 140, 160, 200])
                sale_price = round_money(original * random.choice([0.6, 0.65, 0.67, 0.7, 0.75, 0.8]))
                discount_amt = original - sale_price
                discount_pct = round_money((discount_amt / original) * 100)
                
                q_text = f"Running shoes normally cost {format_money(original)}. In a sale, they cost {format_money(sale_price)}.\\nWork out the percentage discount."
                correct = f"{discount_pct}%"
                wrong = [f"{round_money(discount_pct + 5)}%", f"{round_money(discount_pct - 5)}%", f"{round_money((sale_price/original)*100)}%"]
                
                visual = None
                explanation = f"Discount = {format_money(original)} − {format_money(sale_price)} = {format_money(discount_amt)}\\n" \
                             f"% Discount = ({format_money(discount_amt)} ÷ {format_money(original)}) × 100 = {discount_pct}%"
                
            elif q_type == 'profit_as_pct_cost':
                # SEC 2022 OL Q9(d) style
                cost = random.choice([200, 250, 300, 320, 400])
                profit = random.choice([40, 50, 60, 75, 80, 100])
                pct = round_money((profit / cost) * 100)
                
                q_text = f"It costs {name} {format_money(cost)} to make a product. They sell it for a profit of {format_money(profit)}.\\nWrite the profit as a percentage of the cost."
                correct = f"{pct}%"
                wrong = [f"{round_money(pct + 5)}%", f"{round_money(pct - 5)}%", f"{round_money((profit/(cost+profit))*100)}%"]
                
                visual = generate_profit_loss_svg(cost, cost + profit, profit, True)
                explanation = f"% Profit = (Profit ÷ Cost) × 100\\n= ({format_money(profit)} ÷ {format_money(cost)}) × 100\\n= {pct}%"
                
            else:  # find_original
                original = random.choice([50, 60, 80, 100, 120])
                discount_pct = random.choice([10, 15, 20, 25, 30])
                sale_price = round_money(original * (1 - discount_pct/100))
                
                q_text = f"An item is reduced by {discount_pct}% in a sale. It now costs {format_money(sale_price)}.\\nWhat was the original price?"
                correct = format_money(original)
                wrong = get_unique_wrong_money(original, 3)
                
                visual = None
                explanation = f"If reduced by {discount_pct}%, the sale price is {100-discount_pct}% of original.\\n" \
                             f"Original = {format_money(sale_price)} ÷ {(100-discount_pct)/100} = {format_money(original)}"
            
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
                'difficulty': 7,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Income Tax Basics (Higher)
# ============================================================

def generate_level_8():
    """Income Tax - Single rate with tax credits"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['gross_tax', 'net_income', 'find_credits', 'sec_style']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'gross_tax':
                # SEC 2024 OL Q2(c)(i) style
                gross = random.choice([1500, 1800, 1900, 2000, 2200, 2500])
                tax_rate = 20
                gross_tax = gross * tax_rate / 100
                
                q_text = f"{name}'s gross income was {format_money(gross)} last month.\\nTax rate: {tax_rate}%.\\nWork out the gross tax."
                correct = format_money(gross_tax)
                wrong = get_unique_wrong_money(gross_tax, 3)
                
                visual = None
                explanation = f"Gross Tax = Gross Income × Tax Rate\\n= {format_money(gross)} × {tax_rate}%\\n= {format_money(gross)} × 0.{tax_rate}\\n= {format_money(gross_tax)}"
                
            elif q_type == 'net_income':
                # SEC 2024 OL Q2(c)(ii) style
                gross = random.choice([1800, 1900, 2000, 2200])
                tax_rate = 20
                credits = random.choice([280, 300, 312.50, 325, 350])
                gross_tax = gross * tax_rate / 100
                tax_due = max(0, gross_tax - credits)
                net = gross - tax_due
                
                q_text = f"{name}'s gross income is {format_money(gross)}. Tax rate: {tax_rate}%.\\nMonthly tax credit: {format_money(credits)}.\\nWork out their net income."
                correct = format_money(net)
                wrong = get_unique_wrong_money(net, 3)
                
                visual = generate_wage_slip_svg(name, "—", "—", gross, {"tax": gross_tax, "credits": credits}, net)
                explanation = f"Gross tax = {format_money(gross)} × {tax_rate}% = {format_money(gross_tax)}\\n" \
                             f"Tax due = {format_money(gross_tax)} − {format_money(credits)} = {format_money(tax_due)}\\n" \
                             f"Net income = {format_money(gross)} − {format_money(tax_due)} = {format_money(net)}"
                
            elif q_type == 'find_credits':
                gross = random.choice([2000, 2200, 2400])
                tax_rate = 20
                gross_tax = gross * tax_rate / 100
                net = round_money(gross * random.uniform(0.82, 0.88))
                tax_paid = gross - net
                credits = gross_tax - tax_paid
                
                q_text = f"{name} earns {format_money(gross)} gross. Tax rate: {tax_rate}%. Net pay is {format_money(net)}.\\nWhat are their monthly tax credits?"
                correct = format_money(credits)
                wrong = get_unique_wrong_money(credits, 3)
                
                visual = None
                explanation = f"Gross tax = {format_money(gross)} × {tax_rate}% = {format_money(gross_tax)}\\n" \
                             f"Tax paid = {format_money(gross)} − {format_money(net)} = {format_money(tax_paid)}\\n" \
                             f"Credits = {format_money(gross_tax)} − {format_money(tax_paid)} = {format_money(credits)}"
                
            else:  # sec_style
                gross = random.choice([1900, 2000, 2100, 2200])
                tax_rate = 20
                credits = 312.50
                gross_tax = gross * tax_rate / 100
                tax_due = gross_tax - credits
                net = gross - tax_due
                
                q_text = f"SEC-style: {name}'s monthly gross income is {format_money(gross)}.\\nTax rate: {tax_rate}%. Tax credit: {format_money(credits)}.\\nCalculate net income."
                correct = format_money(net)
                wrong = get_unique_wrong_money(net, 3)
                
                visual = generate_wage_slip_svg(name, "—", "—", gross, {"tax": gross_tax, "credits": credits}, net)
                explanation = f"Gross tax = {format_money(gross)} × 0.20 = {format_money(gross_tax)}\\n" \
                             f"Tax due = {format_money(gross_tax)} − {format_money(credits)} = {format_money(tax_due)}\\n" \
                             f"Net = {format_money(gross)} − {format_money(tax_due)} = {format_money(net)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{gross}_{name}"
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
# LEVEL 9: VAT Calculations (Higher)
# ============================================================

def generate_level_9():
    """VAT - Adding VAT, finding pre-VAT price"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    question_types = ['add_vat', 'find_vat_amount', 'pre_vat_price', 'bill_with_vat', 'vat_inclusive']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            vat_rate = random.choice([9, 13.5, 21, 23])
            
            if q_type == 'add_vat':
                pre_vat = random.choice([40, 50, 60, 75, 80, 100, 120, 150, 180, 200, 250, 400, 500])
                vat_amount = round_money(pre_vat * vat_rate / 100)
                total = pre_vat + vat_amount
                
                q_text = f"A product costs {format_money(pre_vat)} before VAT. VAT rate: {vat_rate}%.\\nWhat is the total price including VAT?"
                correct = format_money(total)
                wrong = get_unique_wrong_money(total, 3)
                
                visual = None
                explanation = f"VAT = {format_money(pre_vat)} × {vat_rate}% = {format_money(vat_amount)}\\n" \
                             f"Total = {format_money(pre_vat)} + {format_money(vat_amount)} = {format_money(total)}"
                
            elif q_type == 'find_vat_amount':
                pre_vat = random.choice([80, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600])
                vat_amount = round_money(pre_vat * vat_rate / 100)
                
                q_text = f"A bill subtotal is {format_money(pre_vat)}. VAT rate: {vat_rate}%.\\nCalculate the VAT amount."
                correct = format_money(vat_amount)
                wrong = get_unique_wrong_money(vat_amount, 3)
                
                visual = None
                explanation = f"VAT = Subtotal × Rate\\n= {format_money(pre_vat)} × {vat_rate}%\\n= {format_money(vat_amount)}"
                
            elif q_type == 'pre_vat_price':
                vat_rate = random.choice([13.5, 23])
                multiplier = 1 + vat_rate / 100
                pre_vat = random.choice([100, 150, 200, 250, 300, 400])
                total = round_money(pre_vat * multiplier)
                
                q_text = f"An item costs {format_money(total)} including {vat_rate}% VAT.\\nWhat was the price before VAT?"
                correct = format_money(pre_vat)
                wrong = get_unique_wrong_money(pre_vat, 3)
                
                visual = None
                explanation = f"Price inc. VAT = Pre-VAT price × {multiplier}\\n" \
                             f"Pre-VAT = {format_money(total)} ÷ {multiplier} = {format_money(pre_vat)}"
                
            elif q_type == 'bill_with_vat':
                # SEC 2025 HL Q3 style
                labour_hrs = random.choice([2, 2.5, 3, 3.5, 4])
                labour_rate = random.choice([80, 100, 120, 150])
                materials = random.choice([50, 75, 100, 150, 200])
                
                labour_cost = labour_hrs * labour_rate
                subtotal = labour_cost + materials
                vat_rate = 13.5
                vat_amount = round_money(subtotal * vat_rate / 100)
                total = subtotal + vat_amount
                
                items = [("Labour", labour_hrs, labour_rate), ("Materials", 1, materials)]
                
                q_text = f"Bill: Labour {labour_hrs}hrs @ {format_money(labour_rate)}/hr, Materials {format_money(materials)}.\\nVAT {vat_rate}% is added. What is the total?"
                correct = format_money(total)
                wrong = get_unique_wrong_money(total, 3)
                
                visual = generate_bill_svg(items, subtotal, vat_rate, vat_amount, total)
                explanation = f"Labour = {labour_hrs} × {format_money(labour_rate)} = {format_money(labour_cost)}\\n" \
                             f"Subtotal = {format_money(subtotal)}\\nVAT = {format_money(vat_amount)}\\nTotal = {format_money(total)}"
                
            else:  # vat_inclusive
                vat_rate = random.choice([13.5, 23])
                multiplier = 1 + vat_rate / 100
                pre_vat = random.choice([50, 80, 100, 120, 160, 200, 250])
                total = round_money(pre_vat * multiplier)
                vat_amount = total - pre_vat
                
                q_text = f"A service costs {format_money(total)} including {vat_rate}% VAT.\\nHow much of this is VAT?"
                correct = format_money(vat_amount)
                wrong = get_unique_wrong_money(vat_amount, 3)
                
                visual = None
                explanation = f"Pre-VAT price = {format_money(total)} ÷ {multiplier} = {format_money(pre_vat)}\\n" \
                             f"VAT = {format_money(total)} − {format_money(pre_vat)} = {format_money(vat_amount)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{vat_rate}_{pre_vat if 'pre_vat' in dir() else total}"
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
# LEVEL 10: Compound Interest (Application)
# ============================================================

def generate_level_10():
    """Compound Interest calculations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 10
    
    question_types = ['year1_interest', 'after_2_years', 'compare_simple', 'find_rate']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'year1_interest':
                # SEC 2024 HL Q3(c)(i) style
                principal = random.choice([1000, 1500, 2000, 2500, 3000])
                rate = random.choice([2.5, 3, 3.2, 3.5, 4])
                year1_interest = round_money(principal * rate / 100)
                
                q_text = f"{name} puts {format_money(principal)} in a savings account at {rate}% per year (compound interest).\\nHow much interest do they earn in the first year?"
                correct = format_money(year1_interest)
                wrong = get_unique_wrong_money(year1_interest, 3)
                
                visual = generate_interest_svg(principal, rate, 1, year1_interest, principal + year1_interest)
                explanation = f"Year 1 interest = Principal × Rate\\n= {format_money(principal)} × {rate}%\\n= {format_money(year1_interest)}"
                
            elif q_type == 'after_2_years':
                # SEC 2024 HL Q3(c)(ii) style
                principal = random.choice([2000, 2500, 3000, 4000])
                rate = random.choice([3, 3.2, 3.5, 4])
                
                year1_total = principal * (1 + rate/100)
                year2_total = round_money(year1_total * (1 + rate/100))
                
                q_text = f"{name} invests {format_money(principal)} at {rate}% per year, compounded annually.\\nWhat is the total amount after 2 years?"
                correct = format_money(year2_total)
                wrong = get_unique_wrong_money(year2_total, 3)
                
                year1_interest = principal * rate / 100
                year2_interest = year1_total * rate / 100
                visual = None
                explanation = f"After Year 1: {format_money(principal)} × 1.0{int(rate*10):02d} = {format_money(year1_total)}\\n" \
                             f"After Year 2: {format_money(year1_total)} × 1.0{int(rate*10):02d} = {format_money(year2_total)}\\n" \
                             f"Or use formula: {format_money(principal)} × (1.0{int(rate*10):02d})² = {format_money(year2_total)}"
                
            elif q_type == 'compare_simple':
                principal = random.choice([1000, 2000, 3000])
                rate = random.choice([4, 5])
                years = 2
                
                # Simple interest
                simple_total = principal + (principal * rate * years / 100)
                
                # Compound interest
                compound_total = round_money(principal * ((1 + rate/100) ** years))
                
                difference = round_money(compound_total - simple_total)
                
                q_text = f"{format_money(principal)} is invested at {rate}% for {years} years.\\nHow much more do you get with compound interest than simple interest?"
                correct = format_money(difference)
                wrong = get_unique_wrong_money(difference, 3)
                
                visual = None
                explanation = f"Simple interest total: {format_money(principal)} + ({format_money(principal)} × {rate}% × {years}) = {format_money(simple_total)}\\n" \
                             f"Compound interest total: {format_money(principal)} × (1.0{rate})² = {format_money(compound_total)}\\n" \
                             f"Difference: {format_money(compound_total)} − {format_money(simple_total)} = {format_money(difference)}"
                
            else:  # find_rate
                principal = random.choice([1000, 2000])
                rate = random.choice([3, 4, 5])
                year1_total = principal * (1 + rate/100)
                year1_interest = year1_total - principal
                
                q_text = f"{name} invests {format_money(principal)}. After 1 year with compound interest, they have {format_money(year1_total)}.\\nWhat is the annual interest rate?"
                correct = f"{rate}%"
                wrong = [f"{rate + 1}%", f"{rate - 1}%", f"{rate + 0.5}%"]
                
                visual = None
                explanation = f"Interest = {format_money(year1_total)} − {format_money(principal)} = {format_money(year1_interest)}\\n" \
                             f"Rate = ({format_money(year1_interest)} ÷ {format_money(principal)}) × 100 = {rate}%"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{principal}_{rate}"
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
# LEVEL 11: Income Tax with Bands (Application)
# ============================================================

def generate_level_11():
    """Income Tax with multiple bands"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['two_bands', 'with_credits', 'annual_income', 'sec_hl_style', 'monthly_net'])
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'two_bands':
                # SEC 2022 HL Q1(b)(i) style
                gross = random.choice([46000, 48000, 50000, 52000, 54000, 56000, 58000, 60000, 65000, 70000])
                standard_band = random.choice([40000, 42000, 44300])
                rate1, rate2 = 20, 40
                
                tax_band1 = standard_band * rate1 / 100
                higher_income = gross - standard_band
                tax_band2 = higher_income * rate2 / 100
                total_tax = tax_band1 + tax_band2
                
                q_text = f"{name}'s gross annual income is {format_money(gross)}.\\nTax: {rate1}% on first {format_money(standard_band)}, {rate2}% on the rest.\\nFind the total annual tax."
                correct = format_money(total_tax)
                wrong = get_unique_wrong_money(total_tax, 3)
                
                bands = [
                    (f"First {format_money(standard_band)}", standard_band, rate1, tax_band1),
                    (f"Balance ({format_money(higher_income)})", higher_income, rate2, tax_band2)
                ]
                visual = generate_tax_bands_svg(gross, bands, total_tax, 0, gross - total_tax)
                explanation = f"Tax on first {format_money(standard_band)} at {rate1}% = {format_money(tax_band1)}\\n" \
                             f"Tax on remaining {format_money(higher_income)} at {rate2}% = {format_money(tax_band2)}\\n" \
                             f"Total tax = {format_money(total_tax)}"
                
            elif q_type == 'with_credits':
                # SEC 2022 HL Q1(b)(ii) style
                gross = random.choice([48000, 50000, 52000, 54000, 56000, 58000, 60000, 62000])
                standard_band = 44300
                rate1, rate2 = 20, 40
                credits = random.choice([2800, 3000, 3200, 3300, 3500, 3600, 3800])
                
                tax_band1 = standard_band * rate1 / 100
                tax_band2 = (gross - standard_band) * rate2 / 100
                total_tax = tax_band1 + tax_band2
                tax_after_credits = total_tax - credits
                net = gross - tax_after_credits
                
                q_text = f"{name}'s gross annual income is {format_money(gross)}.\\nTax: 20% on first €44,300, 40% on rest.\\nAnnual tax credits: {format_money(credits)}.\\nFind annual take-home pay."
                correct = format_money(net)
                wrong = get_unique_wrong_money(net, 3)
                
                bands = [
                    (f"Standard (€44,300)", standard_band, rate1, tax_band1),
                    ("Higher rate", gross - standard_band, rate2, tax_band2)
                ]
                visual = generate_tax_bands_svg(gross, bands, total_tax, credits, net)
                explanation = f"Total tax = {format_money(tax_band1)} + {format_money(tax_band2)} = {format_money(total_tax)}\\n" \
                             f"After credits = {format_money(total_tax)} − {format_money(credits)} = {format_money(tax_after_credits)}\\n" \
                             f"Net pay = {format_money(gross)} − {format_money(tax_after_credits)} = {format_money(net)}"
                
            elif q_type == 'annual_income':
                monthly = random.choice([3200, 3500, 3800, 4000, 4200, 4500, 4800, 5000, 5500])
                annual = monthly * 12
                standard_band = 44300
                rate1, rate2 = 20, 40
                
                if annual <= standard_band:
                    total_tax = annual * rate1 / 100
                else:
                    tax_band1 = standard_band * rate1 / 100
                    tax_band2 = (annual - standard_band) * rate2 / 100
                    total_tax = tax_band1 + tax_band2
                
                q_text = f"{name} earns {format_money(monthly)} per month.\\nTax: 20% on first €44,300 annually, 40% above.\\nFind total annual tax."
                correct = format_money(total_tax)
                wrong = get_unique_wrong_money(total_tax, 3)
                
                visual = None
                explanation = f"Annual income = {format_money(monthly)} × 12 = {format_money(annual)}\\n" \
                             f"Total tax = {format_money(total_tax)}"
                
            elif q_type == 'monthly_net':
                annual_gross = random.choice([42000, 45000, 48000, 50000, 52000, 55000])
                monthly_gross = annual_gross / 12
                standard_band = 44300
                rate1, rate2 = 20, 40
                annual_credits = random.choice([3000, 3300, 3600])
                monthly_credits = annual_credits / 12
                
                if annual_gross <= standard_band:
                    annual_tax = annual_gross * rate1 / 100
                else:
                    annual_tax = (standard_band * rate1 / 100) + ((annual_gross - standard_band) * rate2 / 100)
                
                monthly_tax = annual_tax / 12
                tax_after_credits = max(0, monthly_tax - monthly_credits)
                monthly_net = round_money(monthly_gross - tax_after_credits)
                
                q_text = f"{name}'s annual salary is {format_money(annual_gross)}.\\nMonthly tax credits: {format_money(monthly_credits)}.\\nCalculate monthly net pay."
                correct = format_money(monthly_net)
                wrong = get_unique_wrong_money(monthly_net, 3)
                
                visual = None
                explanation = f"Monthly gross = {format_money(monthly_gross)}\\nMonthly tax (before credits) ≈ {format_money(monthly_tax)}\\n" \
                             f"After credits = {format_money(tax_after_credits)}\\nNet = {format_money(monthly_net)}"
                
            else:  # sec_hl_style
                gross = random.choice([50000, 52000, 54000, 56000, 58000, 60000, 62000, 64000])
                standard_band = 44300
                rate1, rate2 = 20, 40
                credits = random.choice([3000, 3300, 3500, 3600])
                
                tax_band1 = standard_band * rate1 / 100
                tax_band2 = (gross - standard_band) * rate2 / 100
                total_tax = tax_band1 + tax_band2
                tax_after_credits = total_tax - credits
                net = gross - tax_after_credits
                
                q_text = f"SEC HL Style: Annual income {format_money(gross)}.\\n20% on first €44,300, 40% above. Credits: {format_money(credits)}.\\nCalculate net annual pay."
                correct = format_money(net)
                wrong = get_unique_wrong_money(net, 3)
                
                bands = [
                    ("20% band", standard_band, rate1, tax_band1),
                    ("40% band", gross - standard_band, rate2, tax_band2)
                ]
                visual = generate_tax_bands_svg(gross, bands, total_tax, credits, net)
                explanation = f"Tax at 20% = {format_money(tax_band1)}\\nTax at 40% = {format_money(tax_band2)}\\n" \
                             f"Total = {format_money(total_tax)}\\nAfter credits = {format_money(tax_after_credits)}\\n" \
                             f"Net = {format_money(net)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{gross}_{credits if 'credits' in dir() else 0}"
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
# LEVEL 12: USC and Complex Tax (Mastery)
# ============================================================

def generate_level_12():
    """USC and Complex Tax calculations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 25
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['usc_bands', 'combined_tax', 'reverse_net', 'sec_hl_usc', 'prsi', 'total_deductions'])
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'usc_bands':
                # SEC 2023 HL Q10 style - USC calculation
                gross = random.choice([18000, 20000, 22000, 25000, 28000, 30000, 32000, 35000, 38000, 40000, 45000])
                
                # USC bands (simplified)
                band1 = 12012  # 0.5%
                band2 = 10908  # 2%
                band3 = max(0, gross - band1 - band2)
                
                usc1 = round_money(min(gross, band1) * 0.005)
                usc2 = round_money(min(max(0, gross - band1), band2) * 0.02)
                usc3 = round_money(band3 * 0.04)
                total_usc = usc1 + usc2 + usc3
                
                q_text = f"{name}'s gross income is {format_money(gross)}.\\nUSC: 0.5% on first €12,012, 2% on next €10,908, 4% above.\\nFind total USC."
                correct = format_money(total_usc)
                wrong = get_unique_wrong_money(total_usc, 3)
                
                visual = None
                explanation = f"USC on €12,012 at 0.5% = {format_money(usc1)}\\n" \
                             f"USC on next portion at 2% = {format_money(usc2)}\\n" \
                             f"USC on remaining at 4% = {format_money(usc3)}\\n" \
                             f"Total USC = {format_money(total_usc)}"
                
            elif q_type == 'combined_tax':
                gross = random.choice([46000, 48000, 50000, 52000, 54000, 56000, 58000])
                standard_band = 44300
                rate1, rate2 = 20, 40
                credits = random.choice([3000, 3300, 3500])
                
                # Income tax
                tax1 = standard_band * rate1 / 100
                tax2 = (gross - standard_band) * rate2 / 100
                income_tax = max(0, tax1 + tax2 - credits)
                
                # USC (simplified ~4%)
                usc = round_money(gross * 0.04)
                
                # PRSI (4%)
                prsi = gross * 0.04
                
                total_deductions = income_tax + usc + prsi
                net = gross - total_deductions
                
                q_text = f"{name} earns {format_money(gross)} annually.\\nIncome tax (after credits): {format_money(income_tax)}\\nUSC: {format_money(usc)}, PRSI: {format_money(prsi)}\\nFind net annual pay."
                correct = format_money(net)
                wrong = get_unique_wrong_money(net, 3)
                
                visual = None
                explanation = f"Total deductions = {format_money(income_tax)} + {format_money(usc)} + {format_money(prsi)} = {format_money(total_deductions)}\\n" \
                             f"Net pay = {format_money(gross)} − {format_money(total_deductions)} = {format_money(net)}"
                
            elif q_type == 'reverse_net':
                net_monthly = random.choice([2600, 2800, 3000, 3200, 3400, 3500, 3700, 3800, 4000])
                tax_rate = random.choice([0.20, 0.22, 0.25, 0.28, 0.30])
                gross = round_money(net_monthly / (1 - tax_rate))
                
                q_text = f"{name}'s net monthly pay is {format_money(net_monthly)}.\\nTheir effective tax rate is {int(tax_rate*100)}%.\\nWhat is their gross monthly pay?"
                correct = format_money(gross)
                wrong = get_unique_wrong_money(gross, 3)
                
                visual = None
                explanation = f"If {int(tax_rate*100)}% is deducted, net = {int((1-tax_rate)*100)}% of gross\\n" \
                             f"Gross = Net ÷ {1-tax_rate}\\n= {format_money(net_monthly)} ÷ {1-tax_rate}\\n= {format_money(gross)}"
                
            elif q_type == 'prsi':
                gross = random.choice([30000, 35000, 40000, 45000, 50000, 55000, 60000])
                prsi_rate = 4
                prsi = round_money(gross * prsi_rate / 100)
                
                q_text = f"{name}'s annual salary is {format_money(gross)}.\\nPRSI is charged at {prsi_rate}%.\\nHow much PRSI do they pay?"
                correct = format_money(prsi)
                wrong = get_unique_wrong_money(prsi, 3)
                
                visual = None
                explanation = f"PRSI = {format_money(gross)} × {prsi_rate}%\\n= {format_money(prsi)}"
                
            elif q_type == 'total_deductions':
                gross = random.choice([36000, 40000, 42000, 45000, 48000, 50000])
                
                # Calculate each deduction
                income_tax = round_money(gross * 0.18)  # Simplified effective rate
                usc = round_money(gross * 0.035)
                prsi = round_money(gross * 0.04)
                total = income_tax + usc + prsi
                
                q_text = f"{name}'s annual gross is {format_money(gross)}.\\nDeductions: Tax {format_money(income_tax)}, USC {format_money(usc)}, PRSI {format_money(prsi)}.\\nTotal deductions?"
                correct = format_money(total)
                wrong = get_unique_wrong_money(total, 3)
                
                visual = None
                explanation = f"Total = {format_money(income_tax)} + {format_money(usc)} + {format_money(prsi)}\\n= {format_money(total)}"
                
            else:  # sec_hl_usc - SEC 2023 HL Q10 style
                gross = random.choice([18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000])
                
                # USC bands from SEC paper
                band1_limit = 12012
                band2_limit = 5564
                rate1, rate2, rate3 = 1.5, 3.5, 7
                
                amount_band1 = min(gross, band1_limit)
                amount_band2 = min(max(0, gross - band1_limit), band2_limit)
                amount_band3 = max(0, gross - band1_limit - band2_limit)
                
                usc1 = round_money(amount_band1 * rate1 / 100)
                usc2 = round_money(amount_band2 * rate2 / 100)
                usc3 = round_money(amount_band3 * rate3 / 100)
                total_usc = usc1 + usc2 + usc3
                
                q_text = f"SEC HL: {name}'s income is {format_money(gross)}.\\nUSC: {rate1}% on first €{band1_limit}, {rate2}% on next €{band2_limit}, {rate3}% above.\\nCalculate total USC."
                correct = format_money(total_usc)
                wrong = get_unique_wrong_money(total_usc, 3)
                
                visual = None
                explanation = f"USC at {rate1}% on €{amount_band1:.0f} = {format_money(usc1)}\\n" \
                             f"USC at {rate2}% on €{amount_band2:.0f} = {format_money(usc2)}\\n" \
                             f"USC at {rate3}% on €{amount_band3:.0f} = {format_money(usc3)}\\n" \
                             f"Total = {format_money(total_usc)}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{gross}_{random.randint(1,1000)}"
            if len(set(options)) != 4:
                continue
            
            # Check for truly unique question
            q_sig = f"{q_type}_{q_text[:60]}"
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
                'image_svg': None,  # Level 12 is 50% visual
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
        1: "Money Calculations",
        2: "Profit and Loss",
        3: "Wages (Basic)",
        4: "Overtime & Increases",
        5: "Simple Interest",
        6: "Currency Conversion",
        7: "% Profit/Discount",
        8: "Income Tax (Basic)",
        9: "VAT Calculations",
        10: "Compound Interest",
        11: "Tax Bands",
        12: "USC & Complex Tax"
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
    print("FINANCIAL MATHS - JC EXAM QUESTION GENERATOR")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Questions per level: {QUESTIONS_PER_LEVEL}")
    print(f"Total target: {QUESTIONS_PER_LEVEL * 12}")
    print("=" * 60)
    
    all_questions = []
    
    generators = [
        (1, "Money Calculations", generate_level_1),
        (2, "Profit and Loss", generate_level_2),
        (3, "Wages (Basic)", generate_level_3),
        (4, "Overtime & Increases", generate_level_4),
        (5, "Simple Interest", generate_level_5),
        (6, "Currency Conversion", generate_level_6),
        (7, "% Profit/Discount", generate_level_7),
        (8, "Income Tax (Basic)", generate_level_8),
        (9, "VAT Calculations", generate_level_9),
        (10, "Compound Interest", generate_level_10),
        (11, "Tax Bands", generate_level_11),
        (12, "USC & Complex Tax", generate_level_12),
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
