#!/usr/bin/env python3
"""
LC Higher Level - Financial Maths Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level x 12 levels) for LC HL Financial Maths
"""

import random

TOPIC = 'lc_hl_financial'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Simple Interest',
    'Compound Interest',
    'Depreciation',
    'Present Value',
    'Future Value',
    'Annuities - Basics',
    'Annuities - Applications',
    'Amortisation',
    'APR & AER',
    'Investment Comparisons',
    'Loan Calculations',
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
        unique_wrong.append(f"Option {len(unique_wrong) + 2}")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def superscript(n):
    """Convert integer to superscript string"""
    sup_map = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
               '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻'}
    return ''.join(sup_map.get(c, c) for c in str(n))

def format_currency(amount):
    """Format as currency with 2 decimal places"""
    return f"€{amount:,.2f}"

def generate_level_1():
    """Level 1: Simple Interest"""
    questions = []
    
    # Type 1: Calculate simple interest (20 questions)
    for _ in range(20):
        principal = random.choice([100, 200, 500, 1000, 2000, 5000])
        rate = random.randint(2, 10)
        time = random.randint(1, 5)
        
        interest = principal * rate * time / 100
        
        correct = format_currency(interest)
        
        distractors = [
            format_currency(principal * rate / 100),
            format_currency(interest + principal),
            format_currency(interest * 2)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Simple Interest = PRT/100 = {principal} × {rate} × {time} / 100 = {format_currency(interest)}"
        
        questions.append({
            'question_text': f"Calculate the simple interest on {format_currency(principal)} at {rate}% per annum for {time} year{'s' if time > 1 else ''}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find total amount with simple interest (15 questions)
    for _ in range(15):
        principal = random.choice([500, 1000, 2000, 3000, 5000])
        rate = random.randint(3, 8)
        time = random.randint(2, 6)
        
        interest = principal * rate * time / 100
        total = principal + interest
        
        correct = format_currency(total)
        
        distractors = [
            format_currency(interest),
            format_currency(principal * (1 + rate/100)),
            format_currency(total + interest)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Interest = {principal} × {rate} × {time} / 100 = {format_currency(interest)}. Total = {format_currency(principal)} + {format_currency(interest)} = {format_currency(total)}"
        
        questions.append({
            'question_text': f"€{principal:,} is invested at {rate}% simple interest per annum for {time} years. What is the total amount at the end?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find the rate (10 questions)
    for _ in range(10):
        principal = random.choice([1000, 2000, 5000])
        rate = random.randint(3, 10)
        time = random.randint(2, 5)
        
        interest = principal * rate * time / 100
        
        correct = f"{rate}%"
        
        distractors = [
            f"{rate + 1}%",
            f"{rate - 1}%",
            f"{rate * 2}%"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Rate = (Interest × 100) / (Principal × Time) = ({interest} × 100) / ({principal} × {time}) = {rate}%"
        
        questions.append({
            'question_text': f"€{principal:,} earns {format_currency(interest)} simple interest over {time} years. What is the annual interest rate?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Find the time (5 questions)
    for _ in range(5):
        principal = random.choice([1000, 2000, 4000])
        rate = random.randint(4, 8)
        time = random.randint(2, 5)
        
        interest = principal * rate * time / 100
        
        correct = f"{time} years"
        
        distractors = [
            f"{time + 1} years",
            f"{time - 1} years" if time > 1 else "6 months",
            f"{time * 2} years"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Time = (Interest × 100) / (Principal × Rate) = ({interest} × 100) / ({principal} × {rate}) = {time} years"
        
        questions.append({
            'question_text': f"How long will it take for €{principal:,} to earn {format_currency(interest)} at {rate}% simple interest per annum?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_2():
    """Level 2: Compound Interest"""
    questions = []
    
    # Type 1: Annual compound interest (18 questions)
    for _ in range(18):
        principal = random.choice([1000, 2000, 5000, 10000])
        rate = random.randint(3, 8)
        time = random.randint(2, 4)
        
        amount = principal * (1 + rate/100) ** time
        amount = round(amount, 2)
        
        correct = format_currency(amount)
        
        # Simple interest for distractor
        simple = principal * (1 + rate * time / 100)
        
        distractors = [
            format_currency(simple),
            format_currency(amount + principal * rate / 100),
            format_currency(principal * (1 + rate/100))
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"A = P(1 + r)ⁿ = {principal}(1 + {rate/100})^{time} = {principal} × {(1 + rate/100):.4f}^{time} = {format_currency(amount)}"
        
        questions.append({
            'question_text': f"€{principal:,} is invested at {rate}% compound interest per annum. Find the value after {time} years.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find compound interest earned (15 questions)
    for _ in range(15):
        principal = random.choice([2000, 5000, 8000, 10000])
        rate = random.randint(4, 7)
        time = random.randint(2, 5)
        
        amount = principal * (1 + rate/100) ** time
        interest = round(amount - principal, 2)
        
        correct = format_currency(interest)
        
        distractors = [
            format_currency(round(amount, 2)),
            format_currency(principal * rate * time / 100),
            format_currency(interest / 2)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Amount = {principal}(1.{rate:02d})^{time} = {format_currency(round(amount, 2))}. Interest = {format_currency(round(amount, 2))} - {format_currency(principal)} = {format_currency(interest)}"
        
        questions.append({
            'question_text': f"Find the compound interest earned when €{principal:,} is invested at {rate}% per annum for {time} years.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Compare simple vs compound (10 questions)
    for _ in range(10):
        principal = random.choice([5000, 10000])
        rate = random.randint(5, 8)
        time = random.randint(3, 5)
        
        compound_amount = principal * (1 + rate/100) ** time
        simple_amount = principal * (1 + rate * time / 100)
        difference = round(compound_amount - simple_amount, 2)
        
        correct = format_currency(difference)
        
        distractors = [
            format_currency(difference * 2),
            format_currency(simple_amount - principal),
            format_currency(principal * rate / 100)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Compound: {format_currency(round(compound_amount, 2))}, Simple: {format_currency(simple_amount)}. Difference = {format_currency(difference)}"
        
        questions.append({
            'question_text': f"€{principal:,} is invested for {time} years at {rate}%. How much more is earned with compound interest than simple interest?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Compound interest formula identification (7 questions)
    formula_qs = [
        ("Which formula gives compound interest?", "A = P(1 + r)ⁿ", "The compound interest formula multiplies by (1 + r) for each period."),
        ("In A = P(1 + r)ⁿ, what does P represent?", "Principal (initial investment)", "P is the principal or starting amount."),
        ("In A = P(1 + r)ⁿ, what does r represent?", "Interest rate (as decimal)", "r is the interest rate expressed as a decimal."),
        ("In A = P(1 + r)ⁿ, what does n represent?", "Number of time periods", "n is the number of compounding periods."),
        ("What does 'compounding' mean?", "Interest earns interest", "Compound interest means interest is added to principal, then earns more interest."),
        ("If interest is compounded annually, how often is it added?", "Once per year", "Annual compounding means interest is calculated and added once per year."),
        ("What is the multiplier for 5% compound interest?", "1.05", "The multiplier is (1 + r) = 1 + 0.05 = 1.05"),
    ]
    
    for q, a, expl in formula_qs:
        correct = a
        
        if "formula" in q.lower():
            distractors = ["A = P + PRT", "A = P × r × n", "A = P/r"]
        elif "P represent" in q:
            distractors = ["Percentage", "Period", "Payment"]
        elif "r represent" in q:
            distractors = ["Number of years", "Final amount", "Principal"]
        elif "n represent" in q:
            distractors = ["Interest rate", "Number of payments", "Principal"]
        elif "compounding" in q.lower():
            distractors = ["Interest stays fixed", "Principal decreases", "Rate changes yearly"]
        elif "annually" in q:
            distractors = ["Twice per year", "Every month", "Every quarter"]
        else:
            distractors = ["0.05", "5", "1.5"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_3():
    """Level 3: Depreciation"""
    questions = []
    
    # Type 1: Calculate depreciated value (20 questions)
    for _ in range(20):
        initial = random.choice([10000, 15000, 20000, 25000, 30000])
        rate = random.randint(10, 25)
        years = random.randint(2, 5)
        
        value = initial * (1 - rate/100) ** years
        value = round(value, 2)
        
        correct = format_currency(value)
        
        distractors = [
            format_currency(initial - initial * rate * years / 100),
            format_currency(initial * (1 - rate/100)),
            format_currency(value + initial * rate / 100)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"V = P(1 - r)ⁿ = {initial}(1 - {rate/100})^{years} = {initial} × {(1 - rate/100):.2f}^{years} = {format_currency(value)}"
        
        questions.append({
            'question_text': f"A car worth {format_currency(initial)} depreciates at {rate}% per year. What is its value after {years} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Calculate total depreciation (15 questions)
    for _ in range(15):
        initial = random.choice([8000, 12000, 18000, 24000])
        rate = random.randint(12, 20)
        years = random.randint(2, 4)
        
        final_value = initial * (1 - rate/100) ** years
        depreciation = round(initial - final_value, 2)
        
        correct = format_currency(depreciation)
        
        distractors = [
            format_currency(round(final_value, 2)),
            format_currency(initial * rate * years / 100),
            format_currency(depreciation / 2)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Final value = {format_currency(round(final_value, 2))}. Depreciation = {format_currency(initial)} - {format_currency(round(final_value, 2))} = {format_currency(depreciation)}"
        
        questions.append({
            'question_text': f"Equipment worth {format_currency(initial)} depreciates at {rate}% per annum. Find the total depreciation over {years} years.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find original value (10 questions)
    for _ in range(10):
        rate = random.randint(15, 25)
        years = random.randint(2, 4)
        # Work backwards from a nice final value
        multiplier = (1 - rate/100) ** years
        final = random.choice([5000, 6000, 8000, 10000])
        initial = round(final / multiplier, 2)
        
        correct = format_currency(initial)
        
        distractors = [
            format_currency(final * (1 + rate/100) ** years),
            format_currency(final + final * rate * years / 100),
            format_currency(initial * 1.1)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"If V = P(1 - r)ⁿ, then P = V/(1 - r)ⁿ = {final}/{multiplier:.4f} = {format_currency(initial)}"
        
        questions.append({
            'question_text': f"After {years} years of {rate}% annual depreciation, machinery is worth {format_currency(final)}. What was its original value?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Depreciation concepts (5 questions)
    concept_qs = [
        ("What is the depreciation multiplier for 20% annual depreciation?", "0.80", "Multiplier = 1 - 0.20 = 0.80"),
        ("What is the depreciation multiplier for 15% annual depreciation?", "0.85", "Multiplier = 1 - 0.15 = 0.85"),
        ("If an asset depreciates by 10% each year, what fraction of its value does it retain?", "90% or 0.9", "It retains 100% - 10% = 90% of its value each year."),
        ("Which formula represents depreciation?", "V = P(1 - r)ⁿ", "Depreciation uses subtraction: (1 - r) as the multiplier."),
        ("A laptop loses half its value in 3 years. Is this likely straight-line or reducing balance depreciation?", "Reducing balance", "Reducing balance depreciation is typically used for technology assets."),
    ]
    
    for q, a, expl in concept_qs:
        correct = a
        
        if "multiplier" in q.lower() and "20%" in q:
            distractors = ["1.20", "0.20", "0.70"]
        elif "multiplier" in q.lower() and "15%" in q:
            distractors = ["1.15", "0.15", "0.75"]
        elif "fraction" in q.lower():
            distractors = ["10% or 0.1", "100% or 1.0", "110% or 1.1"]
        elif "formula" in q.lower():
            distractors = ["V = P(1 + r)ⁿ", "V = P - Prn", "V = P/rⁿ"]
        else:
            distractors = ["Straight-line", "Cannot determine", "Neither"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_4():
    """Level 4: Present Value"""
    questions = []
    
    # Type 1: Calculate present value (20 questions)
    for _ in range(20):
        future_value = random.choice([5000, 10000, 15000, 20000, 25000])
        rate = random.randint(3, 8)
        years = random.randint(3, 7)
        
        present_value = future_value / (1 + rate/100) ** years
        present_value = round(present_value, 2)
        
        correct = format_currency(present_value)
        
        distractors = [
            format_currency(future_value * (1 + rate/100) ** years),
            format_currency(future_value - future_value * rate * years / 100),
            format_currency(present_value * 0.9)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"PV = FV/(1 + r)ⁿ = {future_value}/(1.{rate:02d})^{years} = {format_currency(present_value)}"
        
        questions.append({
            'question_text': f"What is the present value of {format_currency(future_value)} due in {years} years if money can earn {rate}% per annum?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Compare present values (15 questions)
    for _ in range(15):
        amount1 = random.choice([10000, 12000, 15000])
        years1 = random.randint(2, 4)
        amount2 = amount1 + random.randint(1000, 3000)
        years2 = years1 + random.randint(2, 3)
        rate = random.randint(4, 7)
        
        pv1 = amount1 / (1 + rate/100) ** years1
        pv2 = amount2 / (1 + rate/100) ** years2
        
        if pv1 > pv2:
            correct = f"{format_currency(amount1)} in {years1} years"
            diff = round(pv1 - pv2, 2)
        else:
            correct = f"{format_currency(amount2)} in {years2} years"
            diff = round(pv2 - pv1, 2)
        
        distractors = [
            f"{format_currency(amount2)} in {years2} years" if pv1 > pv2 else f"{format_currency(amount1)} in {years1} years",
            "They have equal present value",
            "Cannot be determined"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"PV₁ = {amount1}/(1.{rate:02d})^{years1} = {format_currency(round(pv1, 2))}. PV₂ = {amount2}/(1.{rate:02d})^{years2} = {format_currency(round(pv2, 2))}. Higher PV is better."
        
        questions.append({
            'question_text': f"At {rate}% interest, which is worth more today: {format_currency(amount1)} in {years1} years or {format_currency(amount2)} in {years2} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Present value concepts (15 questions)
    pv_concepts = [
        ("Why is €1,000 today worth more than €1,000 in 5 years?", "Money today can earn interest", "The time value of money means today's money can be invested to grow."),
        ("What happens to present value when the interest rate increases?", "Present value decreases", "Higher rates mean future money is discounted more heavily."),
        ("What happens to present value when time increases?", "Present value decreases", "The longer we wait, the more the future amount is discounted."),
        ("What is the present value of €1,000 due today?", "€1,000", "If the payment is immediate, no discounting is needed."),
        ("If PV = €8,000 and FV = €10,000, what happened?", "Money grew through interest", "The difference represents interest earned over time."),
        ("What discount rate makes PV = FV?", "0%", "With 0% interest, there's no time value of money."),
        ("Present value is also called:", "Discounted value", "We 'discount' future values to find their present worth."),
        ("Which has higher PV: €5,000 in 2 years or €5,000 in 5 years (same rate)?", "€5,000 in 2 years", "Less time means less discounting, so higher present value."),
        ("The process of finding PV from FV is called:", "Discounting", "We discount future values back to the present."),
        ("In PV = FV/(1+r)ⁿ, what is (1+r)ⁿ called?", "Discount factor or compound factor", "This factor converts between present and future values."),
        ("If r = 5% and n = 2, what is the discount factor (1+r)ⁿ?", "1.1025", "(1.05)² = 1.1025"),
        ("A present value calculation assumes money can be:", "Invested at the given rate", "PV assumes the opportunity to earn the stated interest rate."),
        ("What is the relationship between PV and FV?", "PV × (1+r)ⁿ = FV", "Present value grows to future value through compounding."),
        ("Net Present Value (NPV) compares:", "Present values of cash flows", "NPV sums discounted cash inflows and outflows."),
        ("If NPV > 0, the investment is:", "Profitable at the given rate", "Positive NPV means returns exceed the discount rate."),
    ]
    
    for q, a, expl in pv_concepts:
        correct = a
        
        if "worth more" in q.lower():
            distractors = ["Inflation reduces value", "€1,000 is always €1,000", "Government regulations"]
        elif "rate increases" in q:
            distractors = ["Present value increases", "Present value stays the same", "Cannot determine"]
        elif "time increases" in q:
            distractors = ["Present value increases", "Present value stays the same", "Depends on the rate"]
        elif "due today" in q:
            distractors = ["€0", "Depends on rate", "Cannot calculate"]
        elif "grew" in q.lower():
            distractors = ["Inflation occurred", "Money was withdrawn", "Error in calculation"]
        elif "0%" in a:
            distractors = ["100%", "Any rate", "Cannot exist"]
        elif "Discounted" in a:
            distractors = ["Future value", "Accumulated value", "Nominal value"]
        elif "2 years" in a:
            distractors = ["€5,000 in 5 years", "They are equal", "Cannot compare"]
        elif "Discounting" in a:
            distractors = ["Compounding", "Amortising", "Appreciating"]
        elif "factor" in a.lower():
            distractors = ["Interest rate", "Time period", "Principal"]
        elif "1.1025" in a:
            distractors = ["1.10", "1.025", "0.9025"]
        elif "Invested" in a:
            distractors = ["Kept under a mattress", "Spent immediately", "Taxed at source"]
        elif "FV" in a:
            distractors = ["PV + FV = r", "PV - FV = n", "PV / FV = r"]
        elif "cash flows" in a.lower():
            distractors = ["Future values only", "Simple interest amounts", "Nominal rates"]
        else:
            distractors = ["Unprofitable", "Break-even", "Cannot determine"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_5():
    """Level 5: Future Value"""
    questions = []
    
    # Type 1: Calculate future value (18 questions)
    for _ in range(18):
        principal = random.choice([2000, 5000, 8000, 10000, 15000])
        rate = random.randint(3, 8)
        years = random.randint(5, 15)
        
        future_value = principal * (1 + rate/100) ** years
        future_value = round(future_value, 2)
        
        correct = format_currency(future_value)
        
        distractors = [
            format_currency(principal + principal * rate * years / 100),
            format_currency(principal * (1 + rate/100)),
            format_currency(future_value * 0.8)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"FV = P(1 + r)ⁿ = {principal}(1.{rate:02d})^{years} = {format_currency(future_value)}"
        
        questions.append({
            'question_text': f"€{principal:,} is invested at {rate}% compound interest per annum. What will it be worth in {years} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Find required principal (15 questions)
    for _ in range(15):
        target = random.choice([20000, 30000, 50000, 100000])
        rate = random.randint(4, 7)
        years = random.randint(10, 20)
        
        principal = target / (1 + rate/100) ** years
        principal = round(principal, 2)
        
        correct = format_currency(principal)
        
        distractors = [
            format_currency(target / (1 + rate * years / 100)),
            format_currency(target * (1 - rate/100) ** years),
            format_currency(principal * 1.2)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"P = FV/(1 + r)ⁿ = {target}/(1.{rate:02d})^{years} = {format_currency(principal)}"
        
        questions.append({
            'question_text': f"How much should be invested now at {rate}% per annum to have {format_currency(target)} in {years} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Doubling time approximation (Rule of 72) (10 questions)
    for _ in range(10):
        rate = random.randint(4, 12)
        approx_years = round(72 / rate)
        
        correct = f"Approximately {approx_years} years"
        
        distractors = [
            f"Approximately {approx_years + 3} years",
            f"Approximately {approx_years - 2} years" if approx_years > 3 else f"Approximately {approx_years + 5} years",
            f"Approximately {100 // rate} years"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Rule of 72: Time to double ≈ 72/rate = 72/{rate} ≈ {approx_years} years"
        
        questions.append({
            'question_text': f"Using the Rule of 72, approximately how long will it take for money to double at {rate}% per annum?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 4: Different compounding periods (7 questions)
    for _ in range(7):
        principal = random.choice([5000, 10000])
        annual_rate = random.randint(4, 8)
        years = random.randint(2, 5)
        
        # Compare annual vs semi-annual vs quarterly
        compound_type = random.choice(['semi-annual', 'quarterly', 'monthly'])
        
        if compound_type == 'semi-annual':
            n = 2
            desc = "semi-annually (twice per year)"
        elif compound_type == 'quarterly':
            n = 4
            desc = "quarterly (4 times per year)"
        else:
            n = 12
            desc = "monthly"
        
        fv = principal * (1 + annual_rate/100/n) ** (n * years)
        fv = round(fv, 2)
        
        correct = format_currency(fv)
        
        # Annual compounding for distractor
        fv_annual = principal * (1 + annual_rate/100) ** years
        
        distractors = [
            format_currency(round(fv_annual, 2)),
            format_currency(principal * (1 + annual_rate * years / 100)),
            format_currency(fv * 0.95)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"FV = P(1 + r/n)^(nt) = {principal}(1 + {annual_rate/100}/{n})^({n}×{years}) = {format_currency(fv)}"
        
        questions.append({
            'question_text': f"€{principal:,} is invested at {annual_rate}% compounded {desc} for {years} years. Find the future value.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_6():
    """Level 6: Annuities - Basics"""
    questions = []
    
    # Type 1: Future value of ordinary annuity (20 questions)
    for _ in range(20):
        payment = random.choice([100, 200, 500, 1000])
        rate = random.randint(3, 7)
        years = random.randint(5, 15)
        
        # FV = PMT × [(1+r)ⁿ - 1] / r
        r = rate / 100
        fv = payment * ((1 + r) ** years - 1) / r
        fv = round(fv, 2)
        
        correct = format_currency(fv)
        
        distractors = [
            format_currency(payment * years),
            format_currency(payment * years * (1 + r)),
            format_currency(fv * 0.8)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"FV = PMT × [(1+r)ⁿ - 1]/r = {payment} × [(1.{rate:02d})^{years} - 1]/{r} = {format_currency(fv)}"
        
        questions.append({
            'question_text': f"€{payment} is invested at the end of each year for {years} years at {rate}% per annum. Find the future value.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Present value of ordinary annuity (15 questions)
    for _ in range(15):
        payment = random.choice([500, 1000, 2000, 5000])
        rate = random.randint(4, 8)
        years = random.randint(5, 12)
        
        # PV = PMT × [1 - (1+r)⁻ⁿ] / r
        r = rate / 100
        pv = payment * (1 - (1 + r) ** (-years)) / r
        pv = round(pv, 2)
        
        correct = format_currency(pv)
        
        distractors = [
            format_currency(payment * years),
            format_currency(pv * (1 + r) ** years),
            format_currency(pv * 1.2)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"PV = PMT × [1 - (1+r)⁻ⁿ]/r = {payment} × [1 - (1.{rate:02d})^(-{years})]/{r} = {format_currency(pv)}"
        
        questions.append({
            'question_text': f"What is the present value of receiving €{payment:,} at the end of each year for {years} years, at {rate}% per annum?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Annuity concepts (15 questions)
    annuity_concepts = [
        ("What is an annuity?", "A series of equal payments at regular intervals", "An annuity involves identical payments made at fixed intervals."),
        ("In an ordinary annuity, when are payments made?", "At the end of each period", "Ordinary annuities have payments at period ends."),
        ("In an annuity due, when are payments made?", "At the beginning of each period", "Annuity due has payments at the start of each period."),
        ("Which has higher future value: ordinary annuity or annuity due (same PMT, r, n)?", "Annuity due", "Annuity due payments earn interest for one extra period."),
        ("Which has higher present value: ordinary annuity or annuity due (same PMT, r, n)?", "Annuity due", "Annuity due payments are received/paid earlier."),
        ("What is a perpetuity?", "An annuity that continues forever", "A perpetuity is an infinite stream of payments."),
        ("The present value formula for a perpetuity is:", "PV = PMT/r", "For infinite payments, PV = PMT/r."),
        ("If PMT = €1000 and r = 5%, what is the PV of a perpetuity?", "€20,000", "PV = 1000/0.05 = €20,000"),
        ("What type of annuity is a mortgage payment?", "Ordinary annuity", "Mortgage payments are typically made at period ends."),
        ("What type of annuity is rent paid in advance?", "Annuity due", "Rent paid at the start of each period is an annuity due."),
        ("The annuity factor [1 - (1+r)⁻ⁿ]/r is used for:", "Present value calculations", "This factor converts a payment stream to present value."),
        ("The annuity factor [(1+r)ⁿ - 1]/r is used for:", "Future value calculations", "This factor converts a payment stream to future value."),
        ("As the number of payments increases, the PV of an annuity:", "Increases (but at a decreasing rate)", "More payments add value, but distant payments contribute less."),
        ("As the interest rate increases, the PV of an annuity:", "Decreases", "Higher rates discount future payments more heavily."),
        ("A sinking fund is used to:", "Accumulate money for a future obligation", "Sinking funds build up to meet a future payment."),
    ]
    
    for q, a, expl in annuity_concepts:
        correct = a
        
        if "What is an annuity" in q:
            distractors = ["A single lump sum payment", "A loan from a bank", "An insurance policy"]
        elif "ordinary annuity" in q.lower() and "when" in q.lower():
            distractors = ["At the beginning", "In the middle", "Randomly"]
        elif "annuity due" in q.lower() and "when" in q.lower():
            distractors = ["At the end", "In the middle", "When convenient"]
        elif "future value" in q.lower() and "ordinary" in q.lower():
            distractors = ["Ordinary annuity", "They are equal", "Depends on rate"]
        elif "present value" in q.lower() and "ordinary" in q.lower():
            distractors = ["Ordinary annuity", "They are equal", "Depends on rate"]
        elif "perpetuity" in q.lower() and "What is" in q:
            distractors = ["An annuity for 100 years", "A type of bond", "A decreasing payment"]
        elif "formula" in q.lower() and "perpetuity" in q:
            distractors = ["PV = PMT × r", "PV = PMT × n", "PV = PMT/(1+r)"]
        elif "€20,000" in a:
            distractors = ["€5,000", "€50,000", "€1,000"]
        elif "mortgage" in q.lower():
            distractors = ["Annuity due", "Perpetuity", "Deferred annuity"]
        elif "rent" in q.lower():
            distractors = ["Ordinary annuity", "Perpetuity", "Growing annuity"]
        elif "Present value" in a:
            distractors = ["Future value calculations", "Interest rate calculations", "Payment calculations"]
        elif "Future value" in a:
            distractors = ["Present value calculations", "Interest rate calculations", "Payment calculations"]
        elif "Increases" in a:
            distractors = ["Decreases", "Stays the same", "Becomes negative"]
        elif "Decreases" in a:
            distractors = ["Increases", "Stays the same", "Doubles"]
        else:
            distractors = ["Pay off a loan early", "Avoid taxes", "Increase interest rate"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_7():
    """Level 7: Annuities - Applications"""
    questions = []
    
    # Type 1: Calculate required payment for target FV (15 questions)
    for _ in range(15):
        target = random.choice([50000, 100000, 200000, 500000])
        rate = random.randint(4, 7)
        years = random.randint(15, 30)
        
        r = rate / 100
        # PMT = FV × r / [(1+r)ⁿ - 1]
        payment = target * r / ((1 + r) ** years - 1)
        payment = round(payment, 2)
        
        correct = format_currency(payment)
        
        distractors = [
            format_currency(target / years),
            format_currency(payment * 1.5),
            format_currency(payment * 0.7)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"PMT = FV × r / [(1+r)ⁿ - 1] = {target} × {r} / [(1.{rate:02d})^{years} - 1] = {format_currency(payment)}"
        
        questions.append({
            'question_text': f"How much should be invested each year at {rate}% to accumulate {format_currency(target)} in {years} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Pension/retirement planning (15 questions)
    for _ in range(15):
        annual_income = random.choice([30000, 40000, 50000])
        rate = random.randint(3, 6)
        years = random.randint(20, 30)
        
        r = rate / 100
        # PV = PMT × [1 - (1+r)⁻ⁿ] / r
        fund_needed = annual_income * (1 - (1 + r) ** (-years)) / r
        fund_needed = round(fund_needed, 2)
        
        correct = format_currency(fund_needed)
        
        distractors = [
            format_currency(annual_income * years),
            format_currency(fund_needed * 0.6),
            format_currency(fund_needed * 1.3)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"PV = PMT × [1 - (1+r)⁻ⁿ]/r = {annual_income} × [1 - (1.{rate:02d})^(-{years})]/{r} = {format_currency(fund_needed)}"
        
        questions.append({
            'question_text': f"What pension fund is needed to provide {format_currency(annual_income)} per year for {years} years at {rate}% interest?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Annuity due calculations (10 questions)
    for _ in range(10):
        payment = random.choice([200, 500, 1000])
        rate = random.randint(4, 7)
        years = random.randint(8, 15)
        
        r = rate / 100
        # FV of annuity due = FV of ordinary × (1+r)
        fv_ordinary = payment * ((1 + r) ** years - 1) / r
        fv_due = fv_ordinary * (1 + r)
        fv_due = round(fv_due, 2)
        
        correct = format_currency(fv_due)
        
        distractors = [
            format_currency(round(fv_ordinary, 2)),
            format_currency(payment * years * (1 + r)),
            format_currency(fv_due * 0.9)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Annuity due FV = Ordinary FV × (1+r) = {format_currency(round(fv_ordinary, 2))} × 1.{rate:02d} = {format_currency(fv_due)}"
        
        questions.append({
            'question_text': f"€{payment} is invested at the START of each year for {years} years at {rate}%. Find the future value (annuity due).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Monthly vs annual payments (10 questions)
    for _ in range(10):
        annual_payment = random.choice([1200, 2400, 6000, 12000])
        monthly_payment = annual_payment / 12
        rate = random.randint(4, 8)
        years = random.randint(5, 15)
        
        # Annual payments
        r_annual = rate / 100
        fv_annual = annual_payment * ((1 + r_annual) ** years - 1) / r_annual
        
        # Monthly payments
        r_monthly = rate / 100 / 12
        n_monthly = years * 12
        fv_monthly = monthly_payment * ((1 + r_monthly) ** n_monthly - 1) / r_monthly
        
        diff = round(fv_monthly - fv_annual, 2)
        
        correct = format_currency(diff)
        
        distractors = [
            format_currency(0),
            format_currency(diff * 2),
            format_currency(fv_annual - fv_monthly) if diff < 0 else format_currency(diff / 2)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Monthly: {format_currency(round(fv_monthly, 2))}, Annual: {format_currency(round(fv_annual, 2))}. Monthly payments accumulate more due to more frequent compounding."
        
        questions.append({
            'question_text': f"Compare investing €{annual_payment:,}/year vs €{monthly_payment:,.0f}/month at {rate}% for {years} years. How much more do monthly payments yield?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_8():
    """Level 8: Amortisation"""
    questions = []
    
    # Type 1: Calculate loan payment (20 questions)
    for _ in range(20):
        principal = random.choice([100000, 150000, 200000, 250000, 300000])
        rate = random.randint(3, 6)
        years = random.choice([15, 20, 25, 30])
        
        r = rate / 100 / 12  # Monthly rate
        n = years * 12  # Number of months
        
        # PMT = P × r(1+r)ⁿ / [(1+r)ⁿ - 1]
        payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        payment = round(payment, 2)
        
        correct = format_currency(payment)
        
        distractors = [
            format_currency(principal / n),
            format_currency(payment * 1.2),
            format_currency(payment * 0.8)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Monthly payment = P × r(1+r)ⁿ / [(1+r)ⁿ - 1] where r = {rate}%/12 and n = {years}×12 = {n}. Payment = {format_currency(payment)}"
        
        questions.append({
            'question_text': f"Calculate the monthly payment on a {format_currency(principal)} mortgage at {rate}% per annum over {years} years.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Total interest paid (15 questions)
    for _ in range(15):
        principal = random.choice([150000, 200000, 250000])
        rate = random.randint(3, 5)
        years = random.choice([20, 25, 30])
        
        r = rate / 100 / 12
        n = years * 12
        
        payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        total_paid = payment * n
        total_interest = round(total_paid - principal, 2)
        
        correct = format_currency(total_interest)
        
        distractors = [
            format_currency(principal * rate * years / 100),
            format_currency(total_interest / 2),
            format_currency(total_paid)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Total paid = {format_currency(round(payment, 2))} × {n} = {format_currency(round(total_paid, 2))}. Interest = {format_currency(round(total_paid, 2))} - {format_currency(principal)} = {format_currency(total_interest)}"
        
        questions.append({
            'question_text': f"What is the total interest paid on a {format_currency(principal)} mortgage at {rate}% over {years} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: First payment breakdown (interest vs principal) (10 questions)
    for _ in range(10):
        principal = random.choice([200000, 250000, 300000])
        rate = random.randint(3, 5)
        years = random.choice([20, 25, 30])
        
        r_monthly = rate / 100 / 12
        n = years * 12
        
        payment = principal * r_monthly * (1 + r_monthly) ** n / ((1 + r_monthly) ** n - 1)
        first_interest = principal * r_monthly
        first_principal = payment - first_interest
        
        correct = f"Interest: {format_currency(round(first_interest, 2))}, Principal: {format_currency(round(first_principal, 2))}"
        
        distractors = [
            f"Interest: {format_currency(round(first_principal, 2))}, Principal: {format_currency(round(first_interest, 2))}",
            f"Interest: {format_currency(round(payment/2, 2))}, Principal: {format_currency(round(payment/2, 2))}",
            f"Interest: {format_currency(round(first_interest * 0.8, 2))}, Principal: {format_currency(round(first_principal * 1.2, 2))}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"First month interest = {format_currency(principal)} × ({rate}%/12) = {format_currency(round(first_interest, 2))}. Principal = Payment - Interest = {format_currency(round(first_principal, 2))}"
        
        questions.append({
            'question_text': f"For a {format_currency(principal)} mortgage at {rate}% over {years} years, how is the first monthly payment split?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Amortisation concepts (5 questions)
    amort_concepts = [
        ("In an amortised loan, how does the interest portion change over time?", "Decreases", "As the principal is paid down, less interest accrues each period."),
        ("In an amortised loan, how does the principal portion change over time?", "Increases", "As interest decreases, more of each payment goes to principal."),
        ("What remains constant in an amortised loan?", "The payment amount", "Amortisation calculates a fixed payment that pays off the loan."),
        ("What is the balance after all payments on an amortised loan?", "€0", "Amortisation is designed to pay off the entire loan."),
        ("Why is more interest paid in early loan years?", "The outstanding balance is highest", "Interest is calculated on the remaining balance, which is largest early on."),
    ]
    
    for q, a, expl in amort_concepts:
        correct = a
        
        if "interest portion" in q.lower():
            distractors = ["Increases", "Stays constant", "Varies randomly"]
        elif "principal portion" in q.lower():
            distractors = ["Decreases", "Stays constant", "Varies randomly"]
        elif "constant" in q.lower():
            distractors = ["Interest amount", "Principal amount", "Nothing"]
        elif "balance after" in q.lower():
            distractors = ["The original principal", "Half the original", "Depends on payments"]
        else:
            distractors = ["Interest rates are higher early", "Banks charge more initially", "It's a government rule"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_9():
    """Level 9: APR & AER"""
    questions = []
    
    # Type 1: Calculate AER from nominal rate (18 questions)
    for _ in range(18):
        nominal = random.randint(4, 12)
        comp_periods = random.choice([2, 4, 12, 365])
        
        if comp_periods == 2:
            comp_desc = "semi-annually"
        elif comp_periods == 4:
            comp_desc = "quarterly"
        elif comp_periods == 12:
            comp_desc = "monthly"
        else:
            comp_desc = "daily"
        
        # AER = (1 + r/n)ⁿ - 1
        aer = ((1 + nominal/100/comp_periods) ** comp_periods - 1) * 100
        aer = round(aer, 2)
        
        correct = f"{aer}%"
        
        distractors = [
            f"{nominal}%",
            f"{round(aer + 0.5, 2)}%",
            f"{round(nominal * comp_periods / 12, 2)}%"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"AER = (1 + {nominal}%/{comp_periods})^{comp_periods} - 1 = (1 + {nominal/100/comp_periods:.6f})^{comp_periods} - 1 = {aer}%"
        
        questions.append({
            'question_text': f"A bank offers {nominal}% compounded {comp_desc}. What is the AER (Annual Equivalent Rate)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Compare rates using AER (12 questions)
    for _ in range(12):
        rate1 = random.randint(5, 8)
        rate2 = rate1 + random.choice([0, 1])
        comp1 = random.choice([1, 4])
        comp2 = random.choice([12, 365])
        
        if comp1 == 1:
            desc1 = "annually"
        else:
            desc1 = "quarterly"
        
        if comp2 == 12:
            desc2 = "monthly"
        else:
            desc2 = "daily"
        
        aer1 = ((1 + rate1/100/comp1) ** comp1 - 1) * 100
        aer2 = ((1 + rate2/100/comp2) ** comp2 - 1) * 100
        
        if aer1 > aer2:
            correct = f"Bank A ({rate1}% {desc1})"
        elif aer2 > aer1:
            correct = f"Bank B ({rate2}% {desc2})"
        else:
            correct = "They are equal"
        
        distractors = [
            f"Bank B ({rate2}% {desc2})" if aer1 >= aer2 else f"Bank A ({rate1}% {desc1})",
            "They are equal" if aer1 != aer2 else f"Bank A ({rate1}% {desc1})",
            "Cannot compare"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"AER for A: {round(aer1, 2)}%, AER for B: {round(aer2, 2)}%. Choose higher AER for savings."
        
        questions.append({
            'question_text': f"Bank A offers {rate1}% compounded {desc1}. Bank B offers {rate2}% compounded {desc2}. Which is better for savings?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: APR concepts (20 questions)
    apr_concepts = [
        ("What does APR stand for?", "Annual Percentage Rate", "APR = Annual Percentage Rate, used for loans."),
        ("What does AER stand for?", "Annual Equivalent Rate", "AER = Annual Equivalent Rate, used for savings."),
        ("APR is primarily used for:", "Comparing loan costs", "APR helps borrowers compare the true cost of loans."),
        ("AER is primarily used for:", "Comparing savings returns", "AER helps savers compare actual returns."),
        ("If nominal rate is 6% compounded monthly, is AER higher or lower?", "Higher", "More frequent compounding increases the effective rate."),
        ("If a loan has fees, how do they affect APR?", "APR includes fees, so it's higher than the interest rate alone", "APR accounts for fees and charges over the loan term."),
        ("What's the relationship between nominal rate and AER when compounding is annual?", "They are equal", "With annual compounding, AER equals the nominal rate."),
        ("As compounding frequency increases, what happens to AER?", "AER increases", "More frequent compounding means interest earns interest sooner."),
        ("What is continuous compounding?", "Compounding infinitely often (limit as n→∞)", "The theoretical maximum compounding frequency."),
        ("The formula for continuous compounding is:", "A = Peʳᵗ", "Where e ≈ 2.71828 is the natural base."),
        ("If nominal rate is 10% compounded continuously, AER is:", "Approximately 10.52%", "AER = e^0.10 - 1 ≈ 10.52%."),
        ("Why must lenders disclose APR?", "For consumer protection and fair comparison", "Regulations require APR disclosure to help consumers compare loans."),
        ("A credit card has 1.5% monthly interest. What is the APR?", "18%", "APR = 1.5% × 12 = 18% (simple calculation for disclosure)."),
        ("The same credit card's AER would be:", "Approximately 19.56%", "AER = (1.015)¹² - 1 ≈ 19.56%."),
        ("Which rate is typically higher: nominal or AER (if compounding > annually)?", "AER", "AER captures the effect of compounding within the year."),
        ("A 0% APR offer means:", "No interest charged during the promotional period", "0% APR = interest-free for the offer period."),
        ("Representative APR must be offered to at least:", "51% of applicants", "At least 51% must qualify for the advertised rate."),
        ("What does 'nominal rate' mean?", "The stated rate before compounding effects", "Nominal = named/stated rate, not accounting for compounding."),
        ("EAR (Effective Annual Rate) is the same as:", "AER", "EAR and AER both mean the effective yearly rate."),
        ("If you want the best savings account, look for:", "Highest AER", "AER shows actual returns after compounding."),
    ]
    
    for q, a, expl in apr_concepts:
        correct = a
        
        # Generate appropriate distractors based on question type
        if "stand for" in q.lower() and "APR" in q:
            distractors = ["Average Payment Rate", "Actual Principal Returned", "Adjusted Prime Rate"]
        elif "stand for" in q.lower() and "AER" in q:
            distractors = ["Average Earning Rate", "Actual Expense Ratio", "Annual Expected Return"]
        elif "primarily used" in q.lower() and "APR" in q:
            distractors = ["Comparing savings returns", "Calculating tax", "Setting exchange rates"]
        elif "primarily used" in q.lower() and "AER" in q:
            distractors = ["Comparing loan costs", "Calculating tax", "Setting mortgages"]
        elif "higher or lower" in q.lower():
            distractors = ["Lower", "Same", "Cannot determine"]
        elif "fees" in q.lower():
            distractors = ["APR excludes fees", "Fees don't affect APR", "APR is lower with fees"]
        elif "annual" in q.lower() and "equal" in a.lower():
            distractors = ["AER is always higher", "Nominal is always higher", "They are never equal"]
        elif "frequency increases" in q.lower():
            distractors = ["AER decreases", "AER stays the same", "Cannot determine"]
        elif "continuous" in q.lower() and "what is" in q.lower():
            distractors = ["Compounding once per year", "Compounding twice per year", "No compounding"]
        elif "Peʳᵗ" in a:
            distractors = ["A = P(1+r)ⁿ", "A = P + Prt", "A = P/e^rt"]
        elif "10.52" in a:
            distractors = ["10%", "11%", "9.52%"]
        elif "consumer protection" in a.lower():
            distractors = ["To increase profits", "It's optional", "Only for mortgages"]
        elif "18%" in a:
            distractors = ["1.5%", "15%", "21%"]
        elif "19.56" in a:
            distractors = ["18%", "20%", "15%"]
        elif "AER" in a and "higher" in q.lower():
            distractors = ["Nominal", "They are always equal", "Depends on the bank"]
        elif "0%" in q.lower():
            distractors = ["The loan is free", "You pay only fees", "Interest is deferred"]
        elif "51%" in a:
            distractors = ["100% of applicants", "10% of applicants", "75% of applicants"]
        elif "nominal" in q.lower() and "mean" in q.lower():
            distractors = ["The rate after tax", "The final rate paid", "The rate including fees"]
        elif "EAR" in q:
            distractors = ["APR", "Nominal rate", "Base rate"]
        else:
            distractors = ["Lowest AER", "Highest APR", "Lowest fees only"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_10():
    """Level 10: Investment Comparisons"""
    questions = []
    
    # Type 1: NPV calculations (15 questions)
    for _ in range(15):
        initial = random.choice([10000, 20000, 50000])
        cf1 = random.randint(3000, 8000)
        cf2 = random.randint(4000, 10000)
        cf3 = random.randint(5000, 12000)
        rate = random.randint(5, 12)
        
        r = rate / 100
        npv = -initial + cf1/(1+r) + cf2/(1+r)**2 + cf3/(1+r)**3
        npv = round(npv, 2)
        
        correct = format_currency(npv)
        
        distractors = [
            format_currency(cf1 + cf2 + cf3 - initial),
            format_currency(npv * 1.5),
            format_currency(abs(npv) * -1 if npv > 0 else abs(npv))
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"NPV = -{initial} + {cf1}/1.{rate:02d} + {cf2}/1.{rate:02d}² + {cf3}/1.{rate:02d}³ = {format_currency(npv)}"
        
        questions.append({
            'question_text': f"An investment costs {format_currency(initial)} and returns {format_currency(cf1)}, {format_currency(cf2)}, {format_currency(cf3)} over 3 years. At {rate}% discount rate, what is the NPV?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Investment decision based on NPV (12 questions)
    for _ in range(12):
        initial_a = random.choice([50000, 75000, 100000])
        initial_b = initial_a + random.randint(-10000, 10000)
        rate = random.randint(6, 10)
        
        # Generate returns that give different NPVs
        cf_a = random.randint(20000, 35000)
        cf_b = random.randint(18000, 32000)
        years = 4
        
        r = rate / 100
        npv_a = -initial_a + sum(cf_a / (1+r)**i for i in range(1, years+1))
        npv_b = -initial_b + sum(cf_b / (1+r)**i for i in range(1, years+1))
        
        if npv_a > npv_b and npv_a > 0:
            correct = "Project A"
        elif npv_b > npv_a and npv_b > 0:
            correct = "Project B"
        elif npv_a > 0 or npv_b > 0:
            correct = "Project A" if npv_a > npv_b else "Project B"
        else:
            correct = "Neither (both have negative NPV)"
        
        distractors = [
            "Project B" if "A" in correct else "Project A",
            "Neither (both have negative NPV)" if "Neither" not in correct else "Project A",
            "Both are equally good"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"NPV(A) = {format_currency(round(npv_a, 2))}, NPV(B) = {format_currency(round(npv_b, 2))}. Choose highest positive NPV."
        
        questions.append({
            'question_text': f"Project A: costs {format_currency(initial_a)}, returns {format_currency(cf_a)}/year for 4 years. Project B: costs {format_currency(initial_b)}, returns {format_currency(cf_b)}/year for 4 years. At {rate}% discount rate, which is better?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Break-even analysis (13 questions)
    for _ in range(13):
        fixed_costs = random.choice([10000, 20000, 50000])
        price = random.randint(20, 100)
        variable_cost = random.randint(5, price - 5)
        
        contribution = price - variable_cost
        break_even = fixed_costs / contribution
        break_even = round(break_even, 0)
        
        correct = f"{int(break_even)} units"
        
        distractors = [
            f"{int(break_even * 0.8)} units",
            f"{int(break_even * 1.2)} units",
            f"{int(fixed_costs / price)} units"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Break-even = Fixed Costs / (Price - Variable Cost) = {fixed_costs} / ({price} - {variable_cost}) = {fixed_costs}/{contribution} = {int(break_even)} units"
        
        questions.append({
            'question_text': f"Fixed costs are {format_currency(fixed_costs)}. Each unit sells for €{price} with variable cost €{variable_cost}. What is the break-even point?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Investment comparison concepts (10 questions)
    invest_concepts = [
        ("What does a positive NPV indicate?", "The investment earns more than the discount rate", "Positive NPV means the project adds value above the required return."),
        ("What does a negative NPV indicate?", "The investment earns less than the discount rate", "Negative NPV means the project doesn't meet the required return."),
        ("IRR (Internal Rate of Return) is the rate where:", "NPV equals zero", "IRR is the discount rate that makes NPV = 0."),
        ("If IRR > required rate of return, you should:", "Accept the project", "IRR exceeding the hurdle rate indicates a good investment."),
        ("What is the payback period?", "Time to recover the initial investment", "Payback period ignores time value of money."),
        ("A limitation of payback period is:", "It ignores cash flows after payback", "Payback doesn't consider total profitability."),
        ("Which metric accounts for time value of money?", "NPV and IRR", "NPV and IRR discount future cash flows."),
        ("If two projects are mutually exclusive, choose the one with:", "Higher NPV", "For mutually exclusive projects, NPV is the best criterion."),
        ("The discount rate in NPV is also called:", "Cost of capital or hurdle rate", "It represents the minimum required return."),
        ("Profitability Index = PV of cash flows / Initial investment. If PI > 1:", "Accept the project", "PI > 1 means NPV is positive."),
    ]
    
    for q, a, expl in invest_concepts:
        correct = a
        
        if "positive NPV" in q:
            distractors = ["The investment is risk-free", "The investment loses money", "The investment breaks even"]
        elif "negative NPV" in q:
            distractors = ["The investment is profitable", "The investment should be accepted", "The investment has no risk"]
        elif "IRR" in q and "rate where" in q:
            distractors = ["NPV is maximised", "Profit is highest", "Risk is lowest"]
        elif "IRR >" in q:
            distractors = ["Reject the project", "Need more information", "The project is too risky"]
        elif "payback period" in q.lower() and "what is" in q.lower():
            distractors = ["Total profit earned", "Annual return rate", "Net present value"]
        elif "limitation" in q.lower():
            distractors = ["It's too complicated", "It considers too many factors", "It requires a discount rate"]
        elif "time value" in q.lower():
            distractors = ["Payback period only", "Simple return only", "Accounting profit only"]
        elif "mutually exclusive" in q.lower():
            distractors = ["Higher IRR", "Shorter payback", "Lower initial cost"]
        elif "discount rate" in q.lower():
            distractors = ["Tax rate", "Inflation rate", "Exchange rate"]
        else:
            distractors = ["Reject the project", "Need more analysis", "PI is irrelevant"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_11():
    """Level 11: Loan Calculations"""
    questions = []
    
    # Type 1: Outstanding balance after payments (15 questions)
    for _ in range(15):
        principal = random.choice([150000, 200000, 250000])
        rate = random.randint(3, 5)
        years = random.choice([20, 25, 30])
        years_paid = random.randint(3, 8)
        
        r = rate / 100 / 12
        n = years * 12
        n_paid = years_paid * 12
        n_remaining = n - n_paid
        
        # Calculate payment
        payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        
        # Outstanding balance = PV of remaining payments
        balance = payment * (1 - (1 + r) ** (-n_remaining)) / r
        balance = round(balance, 2)
        
        correct = format_currency(balance)
        
        distractors = [
            format_currency(principal - payment * n_paid),
            format_currency(principal * (n_remaining / n)),
            format_currency(balance * 0.9)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"After {years_paid} years ({n_paid} payments), {n_remaining} payments remain. Balance = PV of remaining payments = {format_currency(balance)}"
        
        questions.append({
            'question_text': f"A {format_currency(principal)} mortgage at {rate}% over {years} years. What is the outstanding balance after {years_paid} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Effect of extra payments (12 questions)
    for _ in range(12):
        principal = random.choice([200000, 250000])
        rate = random.randint(3, 5)
        years = 25
        extra = random.choice([100, 200, 500])
        
        r = rate / 100 / 12
        n = years * 12
        
        # Normal payment
        payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        normal_total = payment * n
        
        # With extra payment - approximate new term
        new_payment = payment + extra
        # Solve for new n: P = PMT × [1 - (1+r)^-n] / r
        # This requires iteration, so we'll estimate
        import math
        try:
            new_n = -math.log(1 - principal * r / new_payment) / math.log(1 + r)
            new_total = new_payment * new_n
            savings = round(normal_total - new_total, 2)
            years_saved = round((n - new_n) / 12, 1)
            
            correct = f"Save {format_currency(savings)}, pay off {years_saved} years early"
        except:
            correct = f"Significant savings and earlier payoff"
            savings = extra * n * 0.3  # Rough estimate
        
        distractors = [
            f"Save {format_currency(extra * n)}, same payoff time",
            f"No significant savings",
            f"Save {format_currency(savings * 0.5 if 'savings' in dir() else 10000)}, pay off 1 year early"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Extra payments reduce principal faster, saving interest and shortening the loan term significantly."
        
        questions.append({
            'question_text': f"On a {format_currency(principal)}, {years}-year mortgage at {rate}%, what's the effect of paying an extra €{extra}/month?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Loan refinancing decisions (13 questions)
    for _ in range(13):
        old_rate = random.randint(5, 7)
        new_rate = old_rate - random.randint(1, 2)
        balance = random.choice([150000, 200000, 250000])
        years_remaining = random.randint(15, 25)
        closing_costs = random.choice([2000, 3000, 5000])
        
        r_old = old_rate / 100 / 12
        r_new = new_rate / 100 / 12
        n = years_remaining * 12
        
        old_payment = balance * r_old * (1 + r_old) ** n / ((1 + r_old) ** n - 1)
        new_payment = balance * r_new * (1 + r_new) ** n / ((1 + r_new) ** n - 1)
        
        monthly_savings = round(old_payment - new_payment, 2)
        total_savings = monthly_savings * n - closing_costs
        breakeven_months = round(closing_costs / monthly_savings)
        
        correct = f"Save {format_currency(monthly_savings)}/month, break even in {breakeven_months} months"
        
        distractors = [
            f"Save {format_currency(monthly_savings * 2)}/month, break even in {breakeven_months // 2} months",
            f"Not worth refinancing",
            f"Save {format_currency(monthly_savings)}/month, never break even"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Monthly savings = {format_currency(round(old_payment, 2))} - {format_currency(round(new_payment, 2))} = {format_currency(monthly_savings)}. Break-even = {format_currency(closing_costs)} / {format_currency(monthly_savings)} = {breakeven_months} months."
        
        questions.append({
            'question_text': f"Refinance {format_currency(balance)} from {old_rate}% to {new_rate}% over {years_remaining} years with {format_currency(closing_costs)} closing costs. Is it worth it?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Loan comparison scenarios (10 questions)
    loan_scenarios = [
        ("15-year vs 30-year mortgage: which has higher monthly payment?", "15-year mortgage", "Shorter term means higher payments but less total interest."),
        ("15-year vs 30-year mortgage: which pays more total interest?", "30-year mortgage", "Longer term accumulates much more interest despite lower payments."),
        ("Fixed vs variable rate: which has predictable payments?", "Fixed rate", "Fixed rates lock in payment amounts; variable rates can change."),
        ("When might a variable rate be better than fixed?", "When rates are expected to fall", "Variable rates benefit from falling interest rates."),
        ("What is a balloon payment?", "A large final payment to clear the loan", "Balloon loans have low regular payments and a large lump sum at the end."),
        ("Interest-only loans have lower monthly payments because:", "Principal is not being repaid monthly", "Only interest is paid; principal is due at term end."),
        ("What is LTV (Loan-to-Value) ratio?", "Loan amount divided by property value", "LTV measures how much of the property value is borrowed."),
        ("Higher LTV typically means:", "Higher interest rate and may require PMI", "Lenders charge more for higher-risk, higher LTV loans."),
        ("What is PMI (Private Mortgage Insurance)?", "Insurance required when LTV is high (usually >80%)", "PMI protects the lender if the borrower defaults."),
        ("Bi-weekly payments instead of monthly result in:", "One extra monthly payment per year, faster payoff", "26 bi-weekly payments = 13 monthly equivalents per year."),
    ]
    
    for q, a, expl in loan_scenarios:
        correct = a
        
        if "higher monthly" in q.lower():
            distractors = ["30-year mortgage", "They are equal", "Depends on the rate"]
        elif "total interest" in q.lower():
            distractors = ["15-year mortgage", "They are equal", "Cannot determine"]
        elif "predictable" in q.lower():
            distractors = ["Variable rate", "Both are predictable", "Neither"]
        elif "variable rate be better" in q.lower():
            distractors = ["When rates are rising", "Never", "When you have bad credit"]
        elif "balloon" in q.lower():
            distractors = ["Extra small payments", "A type of insurance", "An early payoff penalty"]
        elif "Interest-only" in q:
            distractors = ["Interest rates are lower", "The term is longer", "There are no fees"]
        elif "LTV" in q and "what is" in q.lower():
            distractors = ["Total interest paid", "Monthly payment amount", "Years remaining"]
        elif "Higher LTV" in q:
            distractors = ["Lower interest rate", "No effect on terms", "Faster approval"]
        elif "PMI" in q and "what is" in q.lower():
            distractors = ["Tax on mortgage interest", "A type of loan", "Principal and interest combined"]
        else:
            distractors = ["No difference from monthly", "Higher total interest", "Larger final payment"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': expl,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    # Type 1: Complex time value problems (10 questions)
    for _ in range(10):
        pv1 = random.choice([5000, 10000])
        rate = random.randint(4, 8)
        years1 = random.randint(3, 6)
        years2 = years1 + random.randint(2, 4)
        
        # Find FV at years1, then use as PV for more growth
        fv1 = pv1 * (1 + rate/100) ** years1
        fv2 = fv1 * (1 + rate/100) ** (years2 - years1)
        fv2 = round(fv2, 2)
        
        # This should equal pv1 * (1 + rate/100) ** years2
        direct = pv1 * (1 + rate/100) ** years2
        
        correct = format_currency(fv2)
        
        distractors = [
            format_currency(round(fv1, 2)),
            format_currency(pv1 * (1 + rate * years2 / 100)),
            format_currency(fv2 * 1.1)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"After {years1} years: {format_currency(round(fv1, 2))}. After {years2} years total: {format_currency(fv2)}"
        
        questions.append({
            'question_text': f"{format_currency(pv1)} is invested at {rate}% compound interest. After {years1} years, how much will be in the account after another {years2 - years1} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Mixed annuity and lump sum (10 questions)
    for _ in range(10):
        lump_sum = random.choice([10000, 20000])
        annual_payment = random.choice([2000, 3000, 5000])
        rate = random.randint(4, 7)
        years = random.randint(10, 15)
        
        r = rate / 100
        
        # FV of lump sum
        fv_lump = lump_sum * (1 + r) ** years
        
        # FV of annuity
        fv_annuity = annual_payment * ((1 + r) ** years - 1) / r
        
        total_fv = round(fv_lump + fv_annuity, 2)
        
        correct = format_currency(total_fv)
        
        distractors = [
            format_currency(round(fv_lump, 2)),
            format_currency(round(fv_annuity, 2)),
            format_currency(lump_sum + annual_payment * years)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"FV of lump sum: {format_currency(round(fv_lump, 2))}. FV of annuity: {format_currency(round(fv_annuity, 2))}. Total: {format_currency(total_fv)}"
        
        questions.append({
            'question_text': f"You invest {format_currency(lump_sum)} now plus {format_currency(annual_payment)} each year for {years} years at {rate}%. What is the total future value?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Real vs nominal returns (10 questions)
    for _ in range(10):
        nominal_rate = random.randint(6, 10)
        inflation = random.randint(2, 4)
        
        # Real rate ≈ nominal - inflation (Fisher approximation)
        # Exact: (1 + nominal) / (1 + inflation) - 1
        real_rate = ((1 + nominal_rate/100) / (1 + inflation/100) - 1) * 100
        real_rate = round(real_rate, 2)
        
        correct = f"{real_rate}%"
        
        distractors = [
            f"{nominal_rate - inflation}%",
            f"{nominal_rate}%",
            f"{nominal_rate + inflation}%"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Real rate = (1 + {nominal_rate/100}) / (1 + {inflation/100}) - 1 = {real_rate}% (or approximately {nominal_rate}% - {inflation}% = {nominal_rate - inflation}%)"
        
        questions.append({
            'question_text': f"An investment returns {nominal_rate}% nominally. If inflation is {inflation}%, what is the real rate of return?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Retirement planning scenarios (10 questions)
    for _ in range(10):
        current_age = random.randint(25, 35)
        retire_age = 65
        death_age = random.randint(85, 95)
        annual_need = random.choice([40000, 50000, 60000])
        rate = random.randint(4, 6)
        
        years_saving = retire_age - current_age
        years_retirement = death_age - retire_age
        
        r = rate / 100
        
        # First find fund needed at retirement (PV of retirement annuity)
        fund_needed = annual_need * (1 - (1 + r) ** (-years_retirement)) / r
        
        # Then find annual savings needed (PMT to reach FV)
        annual_savings = fund_needed * r / ((1 + r) ** years_saving - 1)
        annual_savings = round(annual_savings, 2)
        
        correct = format_currency(annual_savings)
        
        distractors = [
            format_currency(fund_needed / years_saving),
            format_currency(annual_savings * 0.7),
            format_currency(annual_savings * 1.3)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Fund needed at {retire_age}: {format_currency(round(fund_needed, 2))}. Annual savings for {years_saving} years: {format_currency(annual_savings)}"
        
        questions.append({
            'question_text': f"Age {current_age}, planning to retire at {retire_age} and need {format_currency(annual_need)}/year until age {death_age}. At {rate}%, how much must be saved annually?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 5: Multi-part word problems (10 questions)
    word_problems = [
        {
            'q': "A business borrows €100,000 at 6% for 5 years. After 2 years, they refinance the balance at 4% for 3 more years. Compare total interest paid vs. keeping original loan.",
            'a': "Refinancing saves money",
            'e': "Original interest is higher over full term; refinancing at lower rate reduces total cost even with some early interest paid."
        },
        {
            'q': "Invest €500/month for 20 years at 7%, then stop contributing but leave invested for 10 more years. What's the final amount?",
            'a': "Approximately €521,000",
            'e': "After 20 years: ~€260,000. This grows for 10 years at 7%: €260,000 × 1.07¹⁰ ≈ €521,000"
        },
        {
            'q': "Person A invests €10,000 at age 25 and adds nothing. Person B waits until 35, then invests €10,000/year until 65. At 8%, who has more at 65?",
            'a': "Likely Person B due to larger total contributions",
            'e': "A: €10,000 × 1.08⁴⁰ ≈ €217,000. B: Annuity for 30 years ≈ €1.2 million. Contributions matter!"
        },
        {
            'q': "A €300,000 mortgage at 4% over 30 years. How much is still owed after 15 years?",
            'a': "Approximately €194,000",
            'e': "Payment ≈ €1,432/month. After 15 years, balance = PV of remaining 180 payments ≈ €194,000"
        },
        {
            'q': "Investment A: 8% compounded quarterly. Investment B: 8.1% compounded annually. Which has higher AER?",
            'a': "Investment A (AER ≈ 8.24%)",
            'e': "A: AER = (1 + 0.08/4)⁴ - 1 = 8.24%. B: AER = 8.1%. A is better despite lower nominal rate."
        },
        {
            'q': "Save €200/month at 6% for 10 years, or €400/month for 5 years. Same total contribution - which yields more?",
            'a': "€200/month for 10 years yields more",
            'e': "Longer investment period allows more compound growth despite same total deposits."
        },
        {
            'q': "A loan has APR of 12%. What is the equivalent monthly rate?",
            'a': "1% per month",
            'e': "APR / 12 = 12% / 12 = 1% per month"
        },
        {
            'q': "€50,000 depreciates at 15% per year. €30,000 depreciates at 10% per year. When are they equal in value?",
            'a': "After approximately 9.5 years",
            'e': "50,000(0.85)ⁿ = 30,000(0.90)ⁿ. Solving: n ≈ 9.5 years"
        },
        {
            'q': "A perpetuity pays €5,000/year. If sold for €100,000, what discount rate does this imply?",
            'a': "5%",
            'e': "PV = PMT/r, so r = PMT/PV = 5,000/100,000 = 5%"
        },
        {
            'q': "€100,000 is needed in 15 years. Should you invest €X now, or €Y per year? Rate is 5%.",
            'a': "Need €48,102 now OR €4,634 per year",
            'e': "Lump sum: PV = 100,000/1.05¹⁵ = €48,102. Annuity: PMT = 100,000 × 0.05/(1.05¹⁵-1) = €4,634/year"
        },
    ]
    
    for wp in word_problems:
        correct = wp['a']
        
        # Generate generic distractors
        distractors = [
            "Cannot be determined",
            "Both options are equivalent",
            "Insufficient information"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': wp['q'],
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': wp['e'],
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    return questions

def main():
    all_questions = []
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12,
    ]
    
    print(f"Generating questions for {TOPIC}...")
    print("=" * 50)
    
    for level, generator in enumerate(generators, 1):
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level} ({LEVEL_TITLES[level-1]}): {len(questions)} questions")
    
    print("=" * 50)
    print(f"Total questions generated: {len(all_questions)}")
    
    # Output SQL
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
    
    sql_file = f'/home/claude/{TOPIC}_questions.sql'
    with open(sql_file, 'w') as f:
        f.write(f"-- LC Higher Level - Financial Maths Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
