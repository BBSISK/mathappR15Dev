#!/usr/bin/env python3
"""
LC Ordinary Level - Financial Maths Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level × 12 levels) for LC OL Financial Maths
Based on SEC Paper Analysis 2019-2025 (350 marks - #2 priority Paper 1)

OL Financial Maths Focus:
- VAT calculations
- Percentage increase/decrease
- Profit, loss, margin
- Simple and compound interest
- Depreciation
- Tax (PAYE, USC bands)
- Currency exchange
- Wages and overtime

Levels:
1. Percentages Basics
2. VAT Calculations
3. Percentage Increase/Decrease
4. Profit & Loss
5. Simple Interest
6. Compound Interest
7. Depreciation
8. Tax Calculations
9. Currency Exchange
10. Wages & Overtime
11. Multi-Step Problems
12. Mastery Challenge
"""

import random

TOPIC = 'lc_ol_financial'
MODE = 'lc_ol'

LEVEL_TITLES = [
    'Percentages Basics',
    'VAT Calculations',
    'Percentage Increase/Decrease',
    'Profit & Loss',
    'Simple Interest',
    'Compound Interest',
    'Depreciation',
    'Tax Calculations',
    'Currency Exchange',
    'Wages & Overtime',
    'Multi-Step Problems',
    'Mastery Challenge'
]

def make_unique_options(correct, distractors):
    """Create 4 unique options with correct answer randomly placed"""
    correct_str = str(correct)
    unique_wrong = []
    for d in distractors:
        d_str = str(d)
        if d_str != correct_str and d_str not in unique_wrong:
            unique_wrong.append(d_str)
    while len(unique_wrong) < 3:
        unique_wrong.append("Cannot determine")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)


def generate_level_1():
    """Level 1: Percentages Basics"""
    questions = []
    
    # Type 1: Find percentage of amount (20 questions)
    for _ in range(20):
        percent = random.choice([10, 15, 20, 25, 30, 40, 50, 75])
        amount = random.choice([50, 80, 100, 120, 150, 200, 250, 400, 500])
        answer = amount * percent / 100
        
        question = f"What is {percent}% of €{amount}?"
        correct = f"€{answer:.2f}" if answer != int(answer) else f"€{int(answer)}"
        distractors = [
            f"€{amount * (percent + 10) / 100:.2f}",
            f"€{amount * percent / 10:.2f}",
            f"€{amount - percent:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"{percent}% of €{amount} = {percent}/100 × {amount} = €{answer:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Express as percentage (15 questions)
    for _ in range(15):
        part = random.randint(1, 9) * 5
        whole = random.choice([50, 100, 200, 250, 500])
        if part >= whole:
            part = whole // 2
        percent = (part / whole) * 100
        
        question = f"Express {part} as a percentage of {whole}."
        correct = f"{percent:.0f}%" if percent == int(percent) else f"{percent:.1f}%"
        distractors = [
            f"{percent + 10:.0f}%",
            f"{whole / part:.0f}%" if part != 0 else "10%",
            f"{percent / 2:.0f}%"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"{part}/{whole} × 100 = {percent}%"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find the whole given percentage (15 questions)
    for _ in range(15):
        percent = random.choice([10, 20, 25, 50])
        part = random.choice([10, 15, 20, 25, 30, 40, 50])
        whole = part * 100 / percent
        
        question = f"If {percent}% of a number is {part}, what is the number?"
        correct = str(int(whole))
        distractors = [
            str(int(part * percent / 100)),
            str(int(whole + part)),
            str(int(whole / 2))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"If {percent}% = {part}, then 100% = {part} × 100/{percent} = {int(whole)}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_2():
    """Level 2: VAT Calculations"""
    questions = []
    
    # Type 1: Add VAT to price (20 questions)
    for _ in range(20):
        price = random.randint(10, 100) * 5
        vat_rate = random.choice([13.5, 23])
        vat_amount = price * vat_rate / 100
        total = price + vat_amount
        
        question = f"A product costs €{price} before VAT. If VAT is {vat_rate}%, find the price including VAT."
        correct = f"€{total:.2f}"
        distractors = [
            f"€{price * vat_rate / 100:.2f}",
            f"€{price + vat_rate:.2f}",
            f"€{total + 10:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"VAT = {vat_rate}% of €{price} = €{vat_amount:.2f}. Total = €{price} + €{vat_amount:.2f} = €{total:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find VAT amount (15 questions)
    for _ in range(15):
        price = random.randint(20, 200) * 5
        vat_rate = 23
        vat_amount = price * vat_rate / 100
        
        question = f"Calculate the VAT (at 23%) on an item priced at €{price} excluding VAT."
        correct = f"€{vat_amount:.2f}"
        distractors = [
            f"€{price + vat_amount:.2f}",
            f"€{vat_amount + 23:.2f}",
            f"€{price * 0.13:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"VAT = 23% of €{price} = 0.23 × {price} = €{vat_amount:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find price before VAT (15 questions)
    for _ in range(15):
        total = random.randint(50, 250) * 2
        vat_rate = 23
        # total = price × 1.23, so price = total / 1.23
        price_ex_vat = total / 1.23
        
        question = f"An item costs €{total} including VAT at 23%. Find the price before VAT."
        correct = f"€{price_ex_vat:.2f}"
        distractors = [
            f"€{total - 23:.2f}",
            f"€{total * 0.77:.2f}",
            f"€{total - total * 0.23:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Price before VAT = €{total} ÷ 1.23 = €{price_ex_vat:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_3():
    """Level 3: Percentage Increase/Decrease"""
    questions = []
    
    # Type 1: Calculate percentage increase (20 questions)
    for _ in range(20):
        original = random.randint(50, 200) * 2
        percent = random.choice([5, 10, 15, 20, 25, 30])
        increase = original * percent / 100
        new_val = original + increase
        
        question = f"A price of €{original} is increased by {percent}%. What is the new price?"
        correct = f"€{new_val:.2f}" if new_val != int(new_val) else f"€{int(new_val)}"
        distractors = [
            f"€{original + percent:.2f}",
            f"€{increase:.2f}",
            f"€{new_val + increase:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Increase = {percent}% of €{original} = €{increase}. New price = €{original} + €{increase} = €{new_val}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Calculate percentage decrease (15 questions)
    for _ in range(15):
        original = random.randint(100, 500) * 2
        percent = random.choice([10, 15, 20, 25, 30, 40])
        decrease = original * percent / 100
        new_val = original - decrease
        
        question = f"A €{original} item is reduced by {percent}%. What is the sale price?"
        correct = f"€{new_val:.2f}" if new_val != int(new_val) else f"€{int(new_val)}"
        distractors = [
            f"€{decrease:.2f}",
            f"€{original - percent:.2f}",
            f"€{original * percent / 10:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Decrease = {percent}% of €{original} = €{decrease}. Sale price = €{original} - €{decrease} = €{new_val}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find percentage change (15 questions)
    for _ in range(15):
        original = random.randint(20, 100) * 5
        percent = random.choice([10, 20, 25, 40, 50])
        new_val = original * (100 + percent) / 100
        
        question = f"A value changed from €{original} to €{int(new_val)}. What is the percentage increase?"
        correct = f"{percent}%"
        distractors = [
            f"{percent + 10}%",
            f"{int(new_val - original)}%",
            f"{percent * 2}%"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Change = €{int(new_val)} - €{original} = €{int(new_val - original)}. Percentage = ({int(new_val - original)}/{original}) × 100 = {percent}%"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_4():
    """Level 4: Profit & Loss"""
    questions = []
    
    # Type 1: Calculate profit (20 questions)
    for _ in range(20):
        cost = random.randint(20, 100) * 5
        profit_percent = random.choice([10, 15, 20, 25, 30, 40, 50])
        profit = cost * profit_percent / 100
        selling = cost + profit
        
        question = f"A shopkeeper buys goods for €{cost} and sells them at {profit_percent}% profit. Find the selling price."
        correct = f"€{selling:.2f}" if selling != int(selling) else f"€{int(selling)}"
        distractors = [
            f"€{profit:.2f}",
            f"€{cost + profit_percent:.2f}",
            f"€{selling + cost:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Profit = {profit_percent}% of €{cost} = €{profit}. Selling price = €{cost} + €{profit} = €{selling}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Calculate loss (15 questions)
    for _ in range(15):
        cost = random.randint(50, 200) * 5
        loss_percent = random.choice([5, 10, 15, 20, 25])
        loss = cost * loss_percent / 100
        selling = cost - loss
        
        question = f"An item bought for €{cost} is sold at a {loss_percent}% loss. What is the selling price?"
        correct = f"€{selling:.2f}" if selling != int(selling) else f"€{int(selling)}"
        distractors = [
            f"€{loss:.2f}",
            f"€{cost - loss_percent:.2f}",
            f"€{cost + loss:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Loss = {loss_percent}% of €{cost} = €{loss}. Selling price = €{cost} - €{loss} = €{selling}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Find profit percentage (15 questions)
    for _ in range(15):
        cost = random.randint(20, 100) * 4
        profit_percent = random.choice([10, 20, 25, 50])
        selling = cost * (100 + profit_percent) / 100
        
        question = f"An item is bought for €{cost} and sold for €{int(selling)}. What is the percentage profit?"
        correct = f"{profit_percent}%"
        distractors = [
            f"{int(selling - cost)}%",
            f"{profit_percent + 10}%",
            f"{profit_percent * 2}%"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Profit = €{int(selling)} - €{cost} = €{int(selling - cost)}. Percentage = ({int(selling - cost)}/{cost}) × 100 = {profit_percent}%"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_5():
    """Level 5: Simple Interest"""
    questions = []
    
    # Type 1: Calculate simple interest (25 questions)
    for _ in range(25):
        principal = random.choice([500, 1000, 1500, 2000, 2500, 3000, 4000, 5000])
        rate = random.choice([2, 3, 4, 5, 6])
        time = random.choice([1, 2, 3, 4, 5])
        interest = principal * rate * time / 100
        
        question = f"Find the simple interest on €{principal} at {rate}% per annum for {time} year{'s' if time > 1 else ''}."
        correct = f"€{interest:.2f}" if interest != int(interest) else f"€{int(interest)}"
        distractors = [
            f"€{principal * rate / 100:.2f}",
            f"€{interest + principal:.2f}",
            f"€{interest * 2:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"I = PRT/100 = ({principal} × {rate} × {time})/100 = €{interest}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Find total amount (15 questions)
    for _ in range(15):
        principal = random.choice([1000, 2000, 3000, 4000, 5000])
        rate = random.choice([3, 4, 5, 6])
        time = random.choice([2, 3, 4])
        interest = principal * rate * time / 100
        total = principal + interest
        
        question = f"€{principal} is invested at {rate}% simple interest for {time} years. Find the total amount after {time} years."
        correct = f"€{total:.2f}" if total != int(total) else f"€{int(total)}"
        distractors = [
            f"€{interest:.2f}",
            f"€{principal + rate * time:.2f}",
            f"€{total + interest:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Interest = ({principal} × {rate} × {time})/100 = €{interest}. Total = €{principal} + €{interest} = €{total}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Find rate or time (10 questions)
    for _ in range(10):
        principal = random.choice([1000, 2000, 4000, 5000])
        rate = random.choice([4, 5, 8, 10])
        time = 2
        interest = principal * rate * time / 100
        
        question = f"€{principal} earns €{int(interest)} simple interest in {time} years. What is the annual interest rate?"
        correct = f"{rate}%"
        distractors = [
            f"{rate + 2}%",
            f"{int(interest / principal * 100)}%",
            f"{rate * 2}%"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"R = (I × 100)/(P × T) = ({int(interest)} × 100)/({principal} × {time}) = {rate}%"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_6():
    """Level 6: Compound Interest"""
    questions = []
    
    # Type 1: Calculate compound amount (25 questions)
    for _ in range(25):
        principal = random.choice([1000, 2000, 3000, 4000, 5000])
        rate = random.choice([2, 3, 4, 5, 6])
        years = random.choice([1, 2, 3])
        
        amount = principal * ((1 + rate/100) ** years)
        
        question = f"€{principal} is invested at {rate}% compound interest per annum. Find the value after {years} year{'s' if years > 1 else ''}."
        correct = f"€{amount:.2f}"
        distractors = [
            f"€{principal + principal * rate * years / 100:.2f}",
            f"€{principal * (1 + rate/100):.2f}",
            f"€{amount + 100:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"A = P(1 + r)ⁿ = {principal}(1 + {rate/100})^{years} = {principal} × {(1 + rate/100)**years:.4f} = €{amount:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Find compound interest earned (15 questions)
    for _ in range(15):
        principal = random.choice([2000, 3000, 4000, 5000, 6000])
        rate = random.choice([3, 4, 5])
        years = random.choice([2, 3])
        
        amount = principal * ((1 + rate/100) ** years)
        interest = amount - principal
        
        question = f"Find the compound interest earned on €{principal} at {rate}% per annum for {years} years."
        correct = f"€{interest:.2f}"
        distractors = [
            f"€{principal * rate * years / 100:.2f}",
            f"€{amount:.2f}",
            f"€{interest + principal * rate / 100:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Amount = {principal}(1.{rate:02d})^{years} = €{amount:.2f}. Interest = €{amount:.2f} - €{principal} = €{interest:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Compare simple and compound (10 questions)
    for _ in range(10):
        principal = random.choice([2000, 4000, 5000])
        rate = 5
        years = 2
        
        simple = principal * rate * years / 100
        amount_compound = principal * ((1 + rate/100) ** years)
        compound = amount_compound - principal
        diff = compound - simple
        
        question = f"€{principal} invested for {years} years at {rate}%. How much MORE is earned with compound interest than simple interest?"
        correct = f"€{diff:.2f}"
        distractors = [
            f"€{simple:.2f}",
            f"€{compound:.2f}",
            f"€{diff * 2:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Simple interest = €{simple}. Compound interest = €{compound:.2f}. Difference = €{diff:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_7():
    """Level 7: Depreciation"""
    questions = []
    
    # Type 1: Calculate depreciated value (25 questions)
    for _ in range(25):
        original = random.choice([10000, 15000, 20000, 25000, 30000])
        rate = random.choice([10, 15, 20, 25])
        years = random.choice([1, 2, 3])
        
        value = original * ((1 - rate/100) ** years)
        
        question = f"A car worth €{original} depreciates by {rate}% per year. Find its value after {years} year{'s' if years > 1 else ''}."
        correct = f"€{value:.2f}"
        distractors = [
            f"€{original - original * rate / 100 * years:.2f}",
            f"€{original * (1 - rate/100):.2f}",
            f"€{value + 1000:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Value = {original} × (1 - {rate/100})^{years} = {original} × {(1 - rate/100)**years:.4f} = €{value:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Find depreciation amount (15 questions)
    for _ in range(15):
        original = random.choice([12000, 18000, 24000, 30000])
        rate = random.choice([10, 15, 20])
        years = 2
        
        value = original * ((1 - rate/100) ** years)
        depreciation = original - value
        
        question = f"Equipment worth €{original} depreciates at {rate}% per year. Find the total depreciation after {years} years."
        correct = f"€{depreciation:.2f}"
        distractors = [
            f"€{original * rate / 100 * years:.2f}",
            f"€{value:.2f}",
            f"€{depreciation / 2:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Value after {years} years = €{value:.2f}. Depreciation = €{original} - €{value:.2f} = €{depreciation:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Find original value (10 questions)
    for _ in range(10):
        rate = 20
        years = 1
        current = random.choice([8000, 12000, 16000, 20000])
        # current = original × 0.8, so original = current / 0.8
        original = current / (1 - rate/100)
        
        question = f"After {years} year of {rate}% depreciation, a machine is worth €{current}. What was its original value?"
        correct = f"€{original:.2f}"
        distractors = [
            f"€{current + current * rate / 100:.2f}",
            f"€{current * 1.25:.2f}",
            f"€{original + 1000:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Original = Current ÷ (1 - {rate/100}) = €{current} ÷ 0.8 = €{original:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_8():
    """Level 8: Tax Calculations"""
    questions = []
    
    # Type 1: Calculate tax at single rate (20 questions)
    for _ in range(20):
        income = random.choice([25000, 30000, 35000, 40000])
        rate = 20
        tax = income * rate / 100
        
        question = f"Calculate the income tax on €{income} at a rate of {rate}%."
        correct = f"€{tax:.2f}" if tax != int(tax) else f"€{int(tax)}"
        distractors = [
            f"€{income - tax:.2f}",
            f"€{tax / 2:.2f}",
            f"€{tax + income * 0.05:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Tax = {rate}% of €{income} = €{tax}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Net pay after tax (15 questions)
    for _ in range(15):
        gross = random.choice([35000, 40000, 45000, 50000])
        rate = 20
        tax = gross * rate / 100
        net = gross - tax
        
        question = f"A worker earns €{gross} gross. After {rate}% tax, what is the net pay?"
        correct = f"€{net:.2f}" if net != int(net) else f"€{int(net)}"
        distractors = [
            f"€{tax:.2f}",
            f"€{gross + tax:.2f}",
            f"€{net - 1000:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Tax = €{tax}. Net pay = €{gross} - €{tax} = €{net}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Two-rate tax (USC style) (15 questions)
    for _ in range(15):
        income = random.choice([18000, 22000, 25000, 30000])
        # First €12,012 at 0.5%, remainder at 2%
        threshold = 12012
        rate1 = 0.5
        rate2 = 2
        
        tax1 = threshold * rate1 / 100
        tax2 = (income - threshold) * rate2 / 100
        total_tax = tax1 + tax2
        
        question = f"USC is charged at {rate1}% on the first €{threshold} and {rate2}% on the balance. Calculate USC on €{income}."
        correct = f"€{total_tax:.2f}"
        distractors = [
            f"€{income * rate2 / 100:.2f}",
            f"€{tax1:.2f}",
            f"€{total_tax + 50:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"USC = ({rate1}% of €{threshold}) + ({rate2}% of €{income - threshold}) = €{tax1:.2f} + €{tax2:.2f} = €{total_tax:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_9():
    """Level 9: Currency Exchange"""
    questions = []
    
    currencies = [
        ("USD", "US Dollars", 1.08, 1.12),
        ("GBP", "British Pounds", 0.85, 0.88),
        ("JPY", "Japanese Yen", 155, 162),
        ("CHF", "Swiss Francs", 0.95, 0.98),
        ("AUD", "Australian Dollars", 1.62, 1.68)
    ]
    
    # Type 1: Convert EUR to foreign (20 questions)
    for _ in range(20):
        code, name, buy_rate, sell_rate = random.choice(currencies)
        euros = random.choice([100, 200, 250, 300, 400, 500])
        rate = round(random.uniform(buy_rate, sell_rate), 2)
        foreign = euros * rate
        
        question = f"Convert €{euros} to {name} at a rate of €1 = {rate} {code}."
        correct = f"{foreign:.2f} {code}"
        distractors = [
            f"{euros / rate:.2f} {code}",
            f"{foreign + euros:.2f} {code}",
            f"{rate * 100:.2f} {code}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"€{euros} × {rate} = {foreign:.2f} {code}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Convert foreign to EUR (20 questions)
    for _ in range(20):
        code, name, buy_rate, sell_rate = random.choice(currencies)
        rate = round(random.uniform(buy_rate, sell_rate), 2)
        if code == "JPY":
            foreign = random.choice([10000, 15000, 20000, 25000])
        else:
            foreign = random.choice([100, 150, 200, 250, 300])
        euros = foreign / rate
        
        question = f"Convert {foreign} {code} to Euro at a rate of €1 = {rate} {code}."
        correct = f"€{euros:.2f}"
        distractors = [
            f"€{foreign * rate:.2f}",
            f"€{euros + 50:.2f}",
            f"€{foreign:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"{foreign} {code} ÷ {rate} = €{euros:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Exchange with commission (10 questions)
    for _ in range(10):
        euros = random.choice([200, 300, 400, 500])
        rate = 1.10
        commission_rate = random.choice([2, 3, 5])
        
        commission = euros * commission_rate / 100
        amount_to_convert = euros - commission
        usd = amount_to_convert * rate
        
        question = f"A bureau charges {commission_rate}% commission. How many USD do you get for €{euros} at €1 = ${rate}?"
        correct = f"${usd:.2f}"
        distractors = [
            f"${euros * rate:.2f}",
            f"${usd + commission * rate:.2f}",
            f"${amount_to_convert:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Commission = €{commission}. Amount = €{amount_to_convert}. USD = {amount_to_convert} × {rate} = ${usd:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_10():
    """Level 10: Wages & Overtime"""
    questions = []
    
    # Type 1: Calculate basic weekly wage (15 questions)
    for _ in range(15):
        hourly = random.choice([12, 13, 14, 15, 16, 18, 20])
        hours = random.choice([35, 37.5, 38, 39, 40])
        wage = hourly * hours
        
        question = f"A worker earns €{hourly} per hour for a {hours}-hour week. Calculate their weekly wage."
        correct = f"€{wage:.2f}" if wage != int(wage) else f"€{int(wage)}"
        distractors = [
            f"€{hourly + hours:.2f}",
            f"€{wage + hourly:.2f}",
            f"€{wage - hourly * 5:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Weekly wage = {hourly} × {hours} = €{wage}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Time and a half overtime (20 questions)
    for _ in range(20):
        hourly = random.choice([14, 15, 16, 18, 20])
        basic_hours = 40
        overtime_hours = random.choice([4, 5, 6, 8, 10])
        
        basic = hourly * basic_hours
        overtime_rate = hourly * 1.5
        overtime_pay = overtime_rate * overtime_hours
        total = basic + overtime_pay
        
        question = f"A worker earns €{hourly}/hour for 40 hours, plus time-and-a-half for {overtime_hours} hours overtime. Find total pay."
        correct = f"€{total:.2f}" if total != int(total) else f"€{int(total)}"
        distractors = [
            f"€{basic + hourly * overtime_hours:.2f}",
            f"€{basic:.2f}",
            f"€{total + overtime_pay:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Basic = €{basic}. Overtime = {overtime_hours} × €{overtime_rate} = €{overtime_pay}. Total = €{total}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Find overtime hours (15 questions)
    for _ in range(15):
        hourly = 20
        basic_hours = 40
        basic = hourly * basic_hours
        overtime_rate = hourly * 1.5  # 30
        total = random.choice([920, 950, 980, 1010, 1040])
        overtime_pay = total - basic
        overtime_hours = overtime_pay / overtime_rate
        
        if overtime_hours == int(overtime_hours):
            overtime_hours = int(overtime_hours)
            
            question = f"A worker earns €{hourly}/hour for {basic_hours} hours, time-and-a-half for overtime. Total pay is €{total}. How many overtime hours?"
            correct = f"{overtime_hours} hours"
            distractors = [
                f"{overtime_hours + 2} hours",
                f"{int(overtime_pay / hourly)} hours",
                f"{overtime_hours * 2} hours"
            ]
            
            options, idx = make_unique_options(correct, distractors)
            explanation = f"Basic = €{basic}. Overtime pay = €{total} - €{basic} = €{overtime_pay}. Hours = {overtime_pay} ÷ {overtime_rate} = {overtime_hours}"
            questions.append({
                'question_text': question, 'option_a': options[0], 'option_b': options[1],
                'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
                'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
            })
    
    # Fill to 50 if needed
    while len(questions) < 50:
        hourly = random.choice([15, 16, 18])
        hours = 40
        bonus = random.choice([50, 75, 100, 150])
        total = hourly * hours + bonus
        
        question = f"A worker earns €{hourly}/hour for {hours} hours plus a €{bonus} bonus. Find total earnings."
        correct = f"€{total}"
        distractors = [f"€{hourly * hours}", f"€{total + bonus}", f"€{total - hourly}"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Basic = €{hourly * hours}. Total = €{hourly * hours} + €{bonus} = €{total}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions[:50]


def generate_level_11():
    """Level 11: Multi-Step Problems"""
    questions = []
    
    # Type 1: Discount then VAT (20 questions)
    for _ in range(20):
        original = random.choice([100, 150, 200, 250, 300])
        discount = random.choice([10, 15, 20, 25])
        vat = 23
        
        sale_price = original * (1 - discount/100)
        final = sale_price * (1 + vat/100)
        
        question = f"An item costs €{original}. After a {discount}% discount, {vat}% VAT is added. Find the final price."
        correct = f"€{final:.2f}"
        distractors = [
            f"€{original * (1 + vat/100) * (1 - discount/100):.2f}",
            f"€{sale_price:.2f}",
            f"€{original * (1 - discount/100 + vat/100):.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"After {discount}% off: €{sale_price:.2f}. After VAT: €{sale_price:.2f} × 1.23 = €{final:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Successive percentage changes (15 questions)
    for _ in range(15):
        original = random.choice([500, 600, 800, 1000])
        increase = random.choice([10, 20, 25])
        decrease = random.choice([10, 20])
        
        after_increase = original * (1 + increase/100)
        final = after_increase * (1 - decrease/100)
        
        question = f"A price of €{original} increases by {increase}%, then decreases by {decrease}%. Find the final price."
        correct = f"€{final:.2f}"
        distractors = [
            f"€{original:.2f}",
            f"€{original * (1 + (increase - decrease)/100):.2f}",
            f"€{after_increase:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"After +{increase}%: €{after_increase:.2f}. After -{decrease}%: €{final:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Profit after costs (15 questions)
    for _ in range(15):
        cost = random.choice([500, 800, 1000, 1200])
        markup = random.choice([30, 40, 50])
        expenses = random.choice([50, 80, 100])
        
        selling = cost * (1 + markup/100)
        profit = selling - cost - expenses
        
        question = f"An item bought for €{cost} is sold at {markup}% markup. If expenses are €{expenses}, what is the net profit?"
        correct = f"€{profit:.2f}" if profit != int(profit) else f"€{int(profit)}"
        distractors = [
            f"€{selling - cost:.2f}",
            f"€{profit + expenses:.2f}",
            f"€{selling:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Selling price = €{selling:.2f}. Net profit = €{selling:.2f} - €{cost} - €{expenses} = €{profit:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    # Type 1: Investment comparison (15 questions)
    for _ in range(15):
        principal = random.choice([5000, 8000, 10000])
        rate1 = 4
        rate2 = 5
        years = 3
        
        simple = principal + (principal * rate1 * years / 100)
        compound = principal * ((1 + rate2/100) ** years)
        
        better = "compound" if compound > simple else "simple"
        diff = abs(compound - simple)
        
        question = f"€{principal} for {years} years: Option A is {rate1}% simple interest, Option B is {rate2}% compound. Which gives more and by how much?"
        correct = f"Compound by €{diff:.2f}"
        distractors = [
            f"Simple by €{diff:.2f}",
            f"Compound by €{compound - principal:.2f}",
            f"Simple by €{simple - principal:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Simple: €{simple:.2f}. Compound: €{compound:.2f}. Compound better by €{diff:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Real-world tax scenario (15 questions)
    for _ in range(15):
        gross = random.choice([36000, 42000, 48000])
        tax_rate = 20
        prsi = 4
        
        income_tax = gross * tax_rate / 100
        prsi_amount = gross * prsi / 100
        net = gross - income_tax - prsi_amount
        
        question = f"Annual salary €{gross}. Income tax {tax_rate}%, PRSI {prsi}%. Calculate annual net pay."
        correct = f"€{net:.2f}" if net != int(net) else f"€{int(net)}"
        distractors = [
            f"€{gross - income_tax:.2f}",
            f"€{income_tax + prsi_amount:.2f}",
            f"€{net + 1000:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Tax = €{income_tax}. PRSI = €{prsi_amount}. Net = €{gross} - €{income_tax} - €{prsi_amount} = €{net}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Currency and shopping (10 questions)
    for _ in range(10):
        euros = random.choice([300, 400, 500])
        rate = 1.10
        item_usd = random.choice([150, 200, 250])
        
        usd_available = euros * rate
        change_usd = usd_available - item_usd
        change_eur = change_usd / rate
        
        question = f"You exchange €{euros} at €1 = ${rate}. After buying an item for ${item_usd}, how many euros is your change worth?"
        correct = f"€{change_eur:.2f}"
        distractors = [
            f"€{change_usd:.2f}",
            f"€{euros - item_usd:.2f}",
            f"€{change_eur + 20:.2f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"USD = €{euros} × {rate} = ${usd_available}. Change = ${change_usd}. In EUR: ${change_usd} ÷ {rate} = €{change_eur:.2f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Depreciation with sale (10 questions)
    for _ in range(10):
        original = random.choice([20000, 25000, 30000])
        dep_rate = 15
        years = 2
        
        value = original * ((1 - dep_rate/100) ** years)
        sale_price = value + random.choice([500, 1000, 1500])
        profit_loss = sale_price - value
        
        question = f"A car costing €{original} depreciates {dep_rate}% annually. After {years} years it sells for €{sale_price:.0f}. Profit or loss on book value?"
        correct = f"Profit €{profit_loss:.0f}"
        distractors = [
            f"Loss €{profit_loss:.0f}",
            f"Profit €{original - sale_price:.0f}",
            f"Loss €{original - value:.0f}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Book value = €{value:.2f}. Sold for €{sale_price:.0f}. Profit = €{profit_loss:.0f}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    return questions


def main():
    """Generate all questions and output SQL"""
    all_questions = []
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12,
    ]
    
    print(f"Generating questions for {TOPIC}...")
    print("=" * 60)
    
    for level, generator in enumerate(generators, 1):
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level:2d} ({LEVEL_TITLES[level-1]:25s}): {len(questions)} questions")
    
    print("=" * 60)
    print(f"Total questions generated: {len(all_questions)}")
    
    # Generate SQL statements
    sql_statements = []
    for q in all_questions:
        q_text = q['question_text'].replace("'", "''")
        opt_a = q['option_a'].replace("'", "''")
        opt_b = q['option_b'].replace("'", "''")
        opt_c = q['option_c'].replace("'", "''")
        opt_d = q['option_d'].replace("'", "''")
        expl = q['explanation'].replace("'", "''")
        
        sql = f"""INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('{q_text}', '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', {q['correct_idx']},
'{TOPIC}', {q['difficulty']}, '{q['difficulty_band']}', '{MODE}', '{expl}', 1);"""
        sql_statements.append(sql)
    
    # Create complete SQL file
    complete_sql = f"""-- LC Ordinary Level - Financial Maths Complete SQL
-- Generated: 2025-12-15
-- Total: {len(all_questions)} questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Financial Maths topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT '{TOPIC}', 'Financial Maths', id, '💰', 2, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = '{TOPIC}';

-- Insert questions
{chr(10).join(sql_statements)}

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = '{TOPIC}';
"""
    
    with open('lc_ol_financial_complete.sql', 'w', encoding='utf-8') as f:
        f.write(complete_sql)
    print(f"\nSQL written to: lc_ol_financial_complete.sql")
    
    return all_questions


if __name__ == '__main__':
    main()
