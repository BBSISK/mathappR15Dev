#!/usr/bin/env python3
"""
AgentMath - Integers & Number Systems Generator v1
Junior Cycle Mathematics - SEC Aligned

12 Levels:
1. Understanding Integers (positive, negative, zero) - Foundation
2. Number Line & Ordering - Foundation
3. Adding Integers - Foundation
4. Subtracting Integers - Ordinary
5. Multiplying Integers - Ordinary
6. Dividing Integers - Ordinary
7. Order of Operations (BIMDAS) - Higher
8. Absolute Value - Higher
9. Factors & Multiples - Higher
10. Prime Numbers & Factorization - Mastery
11. HCF and LCM - Mastery
12. Problem Solving & Applications - Mastery

SEC References:
- 2022-2025 OL/HL: Integer operations
- Number properties, factors, multiples
- Real-world contexts with negative numbers
"""

import random
import math

TOPIC = "number_systems"
MODE = "jc_exam"
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12


# Visual SVG generators
def number_line_svg(numbers=None, highlight=None, range_start=-10, range_end=10):
    """Generate number line SVG with optional highlighted numbers"""
    width = 320
    height = 80
    margin = 30
    
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="{width}" height="{height}" fill="#f0f9ff"/>
    '''
    
    # Number line
    line_y = height // 2
    svg += f'<line x1="{margin}" y1="{line_y}" x2="{width-margin}" y2="{line_y}" stroke="#1e293b" stroke-width="2"/>'
    
    # Arrow heads
    svg += f'<polygon points="{width-margin},{line_y} {width-margin-8},{line_y-5} {width-margin-8},{line_y+5}" fill="#1e293b"/>'
    svg += f'<polygon points="{margin},{line_y} {margin+8},{line_y-5} {margin+8},{line_y+5}" fill="#1e293b"/>'
    
    # Tick marks and labels
    num_ticks = range_end - range_start + 1
    tick_spacing = (width - 2 * margin) / (num_ticks - 1)
    
    for i, num in enumerate(range(range_start, range_end + 1)):
        x = margin + i * tick_spacing
        
        # Tick mark
        svg += f'<line x1="{x}" y1="{line_y-5}" x2="{x}" y2="{line_y+5}" stroke="#1e293b" stroke-width="1.5"/>'
        
        # Label (show every other number or key numbers)
        if num % 2 == 0 or num == 0:
            color = "#dc2626" if num < 0 else "#059669" if num > 0 else "#1e293b"
            svg += f'<text x="{x}" y="{line_y+20}" font-size="11" fill="{color}" text-anchor="middle">{num}</text>'
    
    # Highlight specific numbers
    if highlight:
        for num in highlight:
            if range_start <= num <= range_end:
                i = num - range_start
                x = margin + i * tick_spacing
                svg += f'<circle cx="{x}" cy="{line_y}" r="8" fill="#3b82f6" opacity="0.8"/>'
                svg += f'<text x="{x}" y="{line_y+4}" font-size="10" fill="white" text-anchor="middle" font-weight="bold">{num}</text>'
    
    svg += '</svg>'
    return svg


def integer_operation_svg(a, b, operation, result):
    """Visual showing integer operation"""
    svg = '''<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="100" fill="#fef3c7"/>
    '''
    
    # Show the calculation
    op_symbol = {'+': '+', '-': '−', '*': '×', '/': '÷'}[operation]
    
    a_color = "#dc2626" if a < 0 else "#059669"
    b_color = "#dc2626" if b < 0 else "#059669"
    r_color = "#dc2626" if result < 0 else "#059669"
    
    svg += f'<text x="30" y="45" font-size="24" fill="{a_color}" font-weight="bold">{a}</text>'
    svg += f'<text x="70" y="45" font-size="24" fill="#1e293b">{op_symbol}</text>'
    svg += f'<text x="100" y="45" font-size="24" fill="{b_color}" font-weight="bold">{"(" + str(b) + ")" if b < 0 else str(b)}</text>'
    svg += f'<text x="140" y="45" font-size="24" fill="#1e293b">=</text>'
    svg += f'<text x="160" y="45" font-size="24" fill="{r_color}" font-weight="bold">?</text>'
    
    svg += '</svg>'
    return svg


def factor_tree_svg(number):
    """Simple factor visualization"""
    svg = '''<svg viewBox="0 0 180 120" xmlns="http://www.w3.org/2000/svg">
    <rect width="180" height="120" fill="#f0fdf4"/>
    '''
    
    # Find prime factors
    factors = []
    n = number
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    
    # Display number at top
    svg += f'<circle cx="90" cy="25" r="20" fill="#3b82f6"/>'
    svg += f'<text x="90" y="30" font-size="14" fill="white" text-anchor="middle" font-weight="bold">{number}</text>'
    
    # Display factors
    if len(factors) <= 4:
        spacing = 140 / (len(factors) + 1)
        for i, f in enumerate(factors):
            x = 20 + (i + 1) * spacing
            svg += f'<line x1="90" y1="45" x2="{x}" y2="75" stroke="#64748b" stroke-width="1.5"/>'
            svg += f'<circle cx="{x}" cy="90" r="15" fill="#22c55e"/>'
            svg += f'<text x="{x}" y="94" font-size="12" fill="white" text-anchor="middle" font-weight="bold">{f}</text>'
    
    svg += '</svg>'
    return svg


def temperature_svg(temp):
    """Thermometer showing temperature"""
    svg = '''<svg viewBox="0 0 100 160" xmlns="http://www.w3.org/2000/svg">
    <rect width="100" height="160" fill="#e0f2fe"/>
    '''
    
    # Thermometer outline
    svg += '<rect x="40" y="20" width="20" height="100" rx="10" fill="white" stroke="#64748b" stroke-width="2"/>'
    svg += '<circle cx="50" cy="130" r="15" fill="white" stroke="#64748b" stroke-width="2"/>'
    
    # Mercury level (scale: -20 to 40 degrees, mapped to 20-120 y)
    min_temp, max_temp = -20, 40
    level_height = ((temp - min_temp) / (max_temp - min_temp)) * 80
    level_y = 120 - level_height
    
    color = "#3b82f6" if temp < 0 else "#ef4444" if temp > 20 else "#f59e0b"
    svg += f'<rect x="45" y="{level_y}" width="10" height="{level_height + 25}" fill="{color}"/>'
    svg += f'<circle cx="50" cy="130" r="12" fill="{color}"/>'
    
    # Temperature label
    svg += f'<text x="50" y="155" font-size="14" fill="#1e293b" text-anchor="middle" font-weight="bold">{temp}°C</text>'
    
    # Scale markers
    for t in [-20, 0, 20, 40]:
        y = 120 - ((t - min_temp) / (max_temp - min_temp)) * 80
        svg += f'<line x1="62" y1="{y}" x2="70" y2="{y}" stroke="#64748b" stroke-width="1"/>'
        svg += f'<text x="75" y="{y+4}" font-size="8" fill="#64748b">{t}°</text>'
    
    svg += '</svg>'
    return svg


def make_options(correct, wrong_set):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    wrong_list = [str(w) for w in wrong_set if str(w) != correct_str]
    random.shuffle(wrong_list)
    
    options = [correct_str] + wrong_list[:3]
    
    while len(options) < 4:
        if isinstance(correct, int):
            wrong = correct + random.choice([-3, -2, -1, 1, 2, 3])
        else:
            wrong = random.randint(-20, 20)
        if str(wrong) not in options:
            options.append(str(wrong))
    
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    return options, correct_idx


def get_difficulty_band(level):
    """Map level to difficulty band"""
    if level <= 3:
        return 'Foundation'
    elif level <= 6:
        return 'Ordinary'
    elif level <= 9:
        return 'Higher'
    else:
        return 'Mastery'


# Level 1: Understanding Integers
def gen_level_1(n=50):
    """Foundation: Recognize and classify integers"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['classify', 'identify', 'real_world', 'which_is', 'opposite'])
        
        if qtype == 'classify':
            num = random.randint(-20, 20)
            if num > 0:
                txt = f"Is {num} a positive integer, negative integer, or zero?"
                ans = "Positive integer"
            elif num < 0:
                txt = f"Is {num} a positive integer, negative integer, or zero?"
                ans = "Negative integer"
            else:
                txt = f"Is {num} a positive integer, negative integer, or zero?"
                ans = "Zero"
            wrongs = {"Positive integer", "Negative integer", "Zero", "Not an integer"}
            vis = number_line_svg(highlight=[num], range_start=-10, range_end=10)
            exp = f"{num} is {'greater than 0' if num > 0 else 'less than 0' if num < 0 else 'neither positive nor negative'} → {ans}"
            
        elif qtype == 'identify':
            options_list = [
                ([-3, 5, -8, 0], "All are integers"),
                ([2.5, -3, 7], "Not all are integers (2.5 is not)"),
                ([-1, 0, 1, 2], "All are integers"),
            ]
            nums, explanation = random.choice(options_list)
            txt = f"Which statement is true about: {nums}?"
            if "Not all" in explanation:
                ans = "Not all are integers"
                wrongs = {"All are integers", "All are positive", "All are negative", "None are integers"}
            else:
                ans = "All are integers"
                wrongs = {"Not all are integers", "All are positive", "All are negative", "None are integers"}
            vis = number_line_svg(range_start=-10, range_end=10)
            exp = explanation
            
        elif qtype == 'real_world':
            context_type = random.choice(['temp_below', 'debt', 'profit', 'floors', 'gain'])
            
            if context_type == 'temp_below':
                val = random.randint(1, 15)
                txt = f"A temperature of {val} degrees below zero is written as:"
                ans = f"-{val}°C"
                wrongs = {f"+{val}°C", f"{val}°C", "0°C", f"-{val+1}°C"}
                exp = f"Below zero means negative: -{val}°C"
            elif context_type == 'debt':
                val = random.randint(10, 50)
                txt = f"A debt of €{val} can be represented as:"
                ans = f"-{val}"
                wrongs = {f"+{val}", f"{val}", "0", f"-{val+10}"}
                exp = f"Debt is negative: -{val}"
            elif context_type == 'profit':
                val = random.randint(10, 100)
                txt = f"A profit of €{val} is represented as:"
                ans = f"+{val}"
                wrongs = {f"-{val}", "0", f"+{val+10}", f"-{val-10}"}
                exp = f"Profit is positive: +{val}"
            elif context_type == 'floors':
                val = random.randint(1, 5)
                txt = f"{val} floors below ground level is written as:"
                ans = f"-{val}"
                wrongs = {f"+{val}", f"{val}", "0", f"-{val+1}"}
                exp = f"Below ground is negative: -{val}"
            else:  # gain
                val = random.randint(5, 20)
                txt = f"A gain of {val} points is represented as:"
                ans = f"+{val}"
                wrongs = {f"-{val}", "0", f"+{val+5}", f"-{val-5}"}
                exp = f"Gain is positive: +{val}"
            
            vis = number_line_svg(range_start=-10, range_end=10)
            
        elif qtype == 'which_is':
            num_type = random.choice(['positive', 'negative'])
            if num_type == 'positive':
                correct = random.randint(1, 10)
                txt = f"Which of these is a positive integer?"
                ans = str(correct)
                wrongs = {str(-correct), "0", str(-correct-1), str(-1)}
            else:
                correct = random.randint(-10, -1)
                txt = f"Which of these is a negative integer?"
                ans = str(correct)
                wrongs = {str(-correct), "0", str(-correct+1), "1"}
            vis = number_line_svg(highlight=[correct], range_start=-10, range_end=10)
            exp = f"{ans} is {num_type} because it is {'greater' if num_type == 'positive' else 'less'} than 0"
            
        else:  # opposite
            num = random.randint(1, 10) * random.choice([1, -1])
            txt = f"What is the opposite of {num}?"
            ans = str(-num)
            wrongs = {str(num), str(abs(num)), str(-abs(num)-1), "0"}
            vis = number_line_svg(highlight=[num, -num], range_start=-10, range_end=10)
            exp = f"The opposite of {num} is {-num} (same distance from 0, opposite side)"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 2: Number Line & Ordering
def gen_level_2(n=50):
    """Foundation: Order integers and use number line"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['order_asc', 'order_desc', 'between', 'compare', 'smallest', 'largest'])
        
        if qtype == 'order_asc':
            nums = random.sample(range(-10, 11), 4)
            sorted_nums = sorted(nums)
            txt = f"Arrange in ascending order (smallest to largest): {nums}"
            ans = str(sorted_nums)
            wrongs = {str(sorted(nums, reverse=True)), str(nums), str(sorted_nums[1:] + [sorted_nums[0]])}
            vis = number_line_svg(highlight=nums, range_start=-10, range_end=10)
            exp = f"Ascending order (left to right on number line): {sorted_nums}"
            
        elif qtype == 'order_desc':
            nums = random.sample(range(-10, 11), 4)
            sorted_nums = sorted(nums, reverse=True)
            txt = f"Arrange in descending order (largest to smallest): {nums}"
            ans = str(sorted_nums)
            wrongs = {str(sorted(nums)), str(nums), str(sorted_nums[1:] + [sorted_nums[0]])}
            vis = number_line_svg(highlight=nums, range_start=-10, range_end=10)
            exp = f"Descending order (right to left on number line): {sorted_nums}"
            
        elif qtype == 'between':
            a = random.randint(-8, 5)
            b = a + random.randint(3, 6)
            middle = (a + b) // 2
            txt = f"Which integer is between {a} and {b}?"
            ans = str(middle)
            wrongs = {str(a-1), str(b+1), str(a+b), str(a)}
            vis = number_line_svg(highlight=[a, b, middle], range_start=-10, range_end=10)
            exp = f"{middle} is between {a} and {b} on the number line"
            
        elif qtype == 'compare':
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            while a == b:
                b = random.randint(-10, 10)
            txt = f"Which symbol makes this true: {a} ___ {b}"
            if a < b:
                ans = "<"
            else:
                ans = ">"
            wrongs = {"<", ">", "=", "≠"}
            vis = number_line_svg(highlight=[a, b], range_start=-10, range_end=10)
            exp = f"{a} is {'less' if a < b else 'greater'} than {b}, so {a} {ans} {b}"
            
        elif qtype == 'smallest':
            nums = random.sample(range(-10, 11), 4)
            txt = f"Which is the smallest: {nums}?"
            ans = str(min(nums))
            wrongs = {str(max(nums)), str(sorted(nums)[1]), str(sorted(nums)[2])}
            vis = number_line_svg(highlight=nums, range_start=-10, range_end=10)
            exp = f"The smallest (furthest left on number line) is {min(nums)}"
            
        else:  # largest
            nums = random.sample(range(-10, 11), 4)
            txt = f"Which is the largest: {nums}?"
            ans = str(max(nums))
            wrongs = {str(min(nums)), str(sorted(nums)[1]), str(sorted(nums)[2])}
            vis = number_line_svg(highlight=nums, range_start=-10, range_end=10)
            exp = f"The largest (furthest right on number line) is {max(nums)}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 3: Adding Integers
def gen_level_3(n=50):
    """Foundation: Add integers including negatives"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['pos_pos', 'neg_neg', 'pos_neg', 'neg_pos', 'context'])
        
        if qtype == 'pos_pos':
            a = random.randint(1, 15)
            b = random.randint(1, 15)
            result = a + b
            txt = f"Calculate: {a} + {b}"
            exp = f"{a} + {b} = {result}"
            
        elif qtype == 'neg_neg':
            a = random.randint(-15, -1)
            b = random.randint(-15, -1)
            result = a + b
            txt = f"Calculate: ({a}) + ({b})"
            exp = f"Adding two negatives: {a} + {b} = {result}"
            
        elif qtype == 'pos_neg':
            a = random.randint(1, 15)
            b = random.randint(-15, -1)
            result = a + b
            txt = f"Calculate: {a} + ({b})"
            exp = f"Adding a negative is like subtracting: {a} + ({b}) = {a} - {abs(b)} = {result}"
            
        elif qtype == 'neg_pos':
            a = random.randint(-15, -1)
            b = random.randint(1, 15)
            result = a + b
            txt = f"Calculate: ({a}) + {b}"
            exp = f"Start at {a}, move {b} to the right: {result}"
            
        else:  # context
            contexts = [
                (f"The temperature was {random.randint(-10, -1)}°C. It rose by {random.randint(1, 15)}°C. What is the new temperature?", 
                 lambda a, b: a + b),
                (f"I owed €{random.randint(1, 20)} and then borrowed €{random.randint(1, 10)} more. What is my total debt?",
                 lambda a, b: -(a + b)),
            ]
            temp_a = random.randint(-10, -1)
            temp_b = random.randint(5, 15)
            result = temp_a + temp_b
            txt = f"The temperature was {temp_a}°C. It rose by {temp_b}°C. What is the new temperature?"
            exp = f"{temp_a} + {temp_b} = {result}°C"
        
        ans = str(result)
        wrongs = {str(result + 1), str(result - 1), str(-result), str(abs(result))}
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': integer_operation_svg(a if 'a' in dir() else temp_a, b if 'b' in dir() else temp_b, '+', result)
        })
    
    return qs


# Level 4: Subtracting Integers
def gen_level_4(n=50):
    """Ordinary: Subtract integers including negatives"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['pos_pos', 'neg_neg', 'pos_neg', 'neg_pos', 'subtract_neg'])
        
        if qtype == 'pos_pos':
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            result = a - b
            txt = f"Calculate: {a} - {b}"
            exp = f"{a} - {b} = {result}"
            
        elif qtype == 'neg_neg':
            a = random.randint(-15, -1)
            b = random.randint(-15, -1)
            result = a - b
            txt = f"Calculate: ({a}) - ({b})"
            exp = f"Subtracting a negative is adding: {a} - ({b}) = {a} + {abs(b)} = {result}"
            
        elif qtype == 'pos_neg':
            a = random.randint(1, 15)
            b = random.randint(-15, -1)
            result = a - b
            txt = f"Calculate: {a} - ({b})"
            exp = f"Subtracting negative {b} is adding {abs(b)}: {a} - ({b}) = {a} + {abs(b)} = {result}"
            
        elif qtype == 'neg_pos':
            a = random.randint(-15, -1)
            b = random.randint(1, 15)
            result = a - b
            txt = f"Calculate: ({a}) - {b}"
            exp = f"Starting at {a}, subtract {b}: {a} - {b} = {result}"
            
        else:  # subtract_neg emphasis
            a = random.randint(1, 10)
            b = random.randint(-10, -1)
            result = a - b
            txt = f"What is {a} - ({b})?"
            exp = f"Two negatives make a plus: {a} - ({b}) = {a} + {abs(b)} = {result}"
        
        ans = str(result)
        wrongs = {str(result + 2), str(result - 2), str(-result), str(a + b if 'a' in dir() else 0)}
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': integer_operation_svg(a, b, '-', result)
        })
    
    return qs


# Level 5: Multiplying Integers
def gen_level_5(n=50):
    """Ordinary: Multiply integers with sign rules"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['pos_pos', 'neg_neg', 'pos_neg', 'neg_pos', 'rule'])
        
        if qtype == 'pos_pos':
            a = random.randint(2, 12)
            b = random.randint(2, 12)
            result = a * b
            txt = f"Calculate: {a} × {b}"
            exp = f"Positive × Positive = Positive: {a} × {b} = {result}"
            
        elif qtype == 'neg_neg':
            a = random.randint(-12, -2)
            b = random.randint(-12, -2)
            result = a * b
            txt = f"Calculate: ({a}) × ({b})"
            exp = f"Negative × Negative = Positive: {a} × {b} = {result}"
            
        elif qtype == 'pos_neg':
            a = random.randint(2, 12)
            b = random.randint(-12, -2)
            result = a * b
            txt = f"Calculate: {a} × ({b})"
            exp = f"Positive × Negative = Negative: {a} × {b} = {result}"
            
        elif qtype == 'neg_pos':
            a = random.randint(-12, -2)
            b = random.randint(2, 12)
            result = a * b
            txt = f"Calculate: ({a}) × {b}"
            exp = f"Negative × Positive = Negative: {a} × {b} = {result}"
            
        else:  # rule
            rule_q = random.choice([
                ("What is the sign of: positive × negative?", "Negative"),
                ("What is the sign of: negative × negative?", "Positive"),
                ("What is the sign of: positive × positive?", "Positive"),
                ("What is the sign of: negative × positive?", "Negative"),
            ])
            txt = rule_q[0]
            ans = rule_q[1]
            wrongs = {"Positive", "Negative", "Zero", "Depends on the numbers"}
            exp = f"Rule: {txt.split(':')[1].strip()} → {ans}"
            
            opts, idx = make_options(ans, wrongs)
            qs.append({
                'question_text': txt,
                'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
                'correct_idx': idx,
                'explanation': exp,
                'image_svg': number_line_svg(range_start=-10, range_end=10)
            })
            continue
        
        ans = str(result)
        wrongs = {str(-result), str(result + a), str(a + b), str(abs(result) + 1)}
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': integer_operation_svg(a, b, '*', result)
        })
    
    return qs


# Level 6: Dividing Integers
def gen_level_6(n=50):
    """Ordinary: Divide integers with sign rules"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['pos_pos', 'neg_neg', 'pos_neg', 'neg_pos', 'rule'])
        
        # Generate division that works out evenly
        result = random.randint(2, 10) * random.choice([1, -1])
        divisor = random.randint(2, 10) * random.choice([1, -1])
        dividend = result * divisor
        
        if qtype == 'pos_pos':
            a = abs(dividend)
            b = abs(divisor)
            result = a // b
            txt = f"Calculate: {a} ÷ {b}"
            exp = f"Positive ÷ Positive = Positive: {a} ÷ {b} = {result}"
            
        elif qtype == 'neg_neg':
            a = -abs(dividend)
            b = -abs(divisor)
            result = a // b
            txt = f"Calculate: ({a}) ÷ ({b})"
            exp = f"Negative ÷ Negative = Positive: {a} ÷ {b} = {result}"
            
        elif qtype == 'pos_neg':
            a = abs(dividend)
            b = -abs(divisor)
            result = a // b
            txt = f"Calculate: {a} ÷ ({b})"
            exp = f"Positive ÷ Negative = Negative: {a} ÷ {b} = {result}"
            
        elif qtype == 'neg_pos':
            a = -abs(dividend)
            b = abs(divisor)
            result = a // b
            txt = f"Calculate: ({a}) ÷ {b}"
            exp = f"Negative ÷ Positive = Negative: {a} ÷ {b} = {result}"
            
        else:  # rule
            rule_q = random.choice([
                ("What is the sign of: positive ÷ negative?", "Negative"),
                ("What is the sign of: negative ÷ negative?", "Positive"),
                ("What is the sign of: positive ÷ positive?", "Positive"),
                ("What is the sign of: negative ÷ positive?", "Negative"),
            ])
            txt = rule_q[0]
            ans = rule_q[1]
            wrongs = {"Positive", "Negative", "Zero", "Undefined"}
            exp = f"Division sign rule: {txt.split(':')[1].strip()} → {ans}"
            
            opts, idx = make_options(ans, wrongs)
            qs.append({
                'question_text': txt,
                'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
                'correct_idx': idx,
                'explanation': exp,
                'image_svg': number_line_svg(range_start=-10, range_end=10)
            })
            continue
        
        ans = str(result)
        wrongs = {str(-result), str(result + 1), str(result - 1), str(a + b)}
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': integer_operation_svg(a, b, '/', result)
        })
    
    return qs


# Level 7: Order of Operations (BIMDAS)
def gen_level_7(n=50):
    """Higher: Apply order of operations with integers"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['two_ops', 'brackets', 'three_ops', 'compare'])
        
        if qtype == 'two_ops':
            a = random.randint(2, 8)
            b = random.randint(2, 5)
            c = random.randint(1, 10)
            ops = random.choice([('×', '+'), ('×', '-'), ('÷', '+'), ('÷', '-')])
            
            if ops == ('×', '+'):
                result = a * b + c
                txt = f"Calculate: {a} × {b} + {c}"
                exp = f"Multiply first: {a} × {b} = {a*b}, then add: {a*b} + {c} = {result}"
            elif ops == ('×', '-'):
                result = a * b - c
                txt = f"Calculate: {a} × {b} - {c}"
                exp = f"Multiply first: {a} × {b} = {a*b}, then subtract: {a*b} - {c} = {result}"
            elif ops == ('÷', '+'):
                a = b * random.randint(2, 5)  # Ensure clean division
                result = a // b + c
                txt = f"Calculate: {a} ÷ {b} + {c}"
                exp = f"Divide first: {a} ÷ {b} = {a//b}, then add: {a//b} + {c} = {result}"
            else:
                a = b * random.randint(2, 5)
                result = a // b - c
                txt = f"Calculate: {a} ÷ {b} - {c}"
                exp = f"Divide first: {a} ÷ {b} = {a//b}, then subtract: {a//b} - {c} = {result}"
                
        elif qtype == 'brackets':
            a = random.randint(2, 6)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            result = a * (b + c)
            txt = f"Calculate: {a} × ({b} + {c})"
            exp = f"Brackets first: {b} + {c} = {b+c}, then multiply: {a} × {b+c} = {result}"
            
        elif qtype == 'three_ops':
            a = random.randint(2, 5)
            b = random.randint(2, 4)
            c = random.randint(1, 5)
            d = random.randint(1, 5)
            result = a * b + c - d
            txt = f"Calculate: {a} × {b} + {c} - {d}"
            exp = f"Multiply first: {a} × {b} = {a*b}. Then left to right: {a*b} + {c} - {d} = {result}"
            
        else:  # compare
            a = random.randint(2, 5)
            b = random.randint(2, 4)
            c = random.randint(1, 5)
            val1 = a * b + c
            val2 = a * (b + c)
            txt = f"Which is larger: {a} × {b} + {c} or {a} × ({b} + {c})?"
            if val1 > val2:
                ans = f"{a} × {b} + {c}"
            elif val2 > val1:
                ans = f"{a} × ({b} + {c})"
            else:
                ans = "They are equal"
            wrongs = {f"{a} × {b} + {c}", f"{a} × ({b} + {c})", "They are equal", "Cannot determine"}
            exp = f"{a} × {b} + {c} = {val1}, {a} × ({b} + {c}) = {val2}"
            
            opts, idx = make_options(ans, wrongs)
            qs.append({
                'question_text': txt,
                'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
                'correct_idx': idx,
                'explanation': exp,
                'image_svg': number_line_svg(range_start=-10, range_end=50)
            })
            continue
        
        ans = str(result)
        wrongs = {str(result + 2), str(result - 2), str(result * 2), str(-result)}
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': number_line_svg(range_start=-10, range_end=50)
        })
    
    return qs


# Level 8: Absolute Value
def gen_level_8(n=50):
    """Higher: Understand and calculate absolute value"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['basic', 'expression', 'compare', 'equation', 'meaning'])
        
        if qtype == 'basic':
            num = random.randint(-20, 20)
            txt = f"What is |{num}|?"
            ans = str(abs(num))
            wrongs = {str(-abs(num)), str(num), str(abs(num) + 1), str(-num)}
            vis = number_line_svg(highlight=[num, abs(num)] if num != abs(num) else [num], range_start=-10, range_end=10)
            exp = f"|{num}| = {abs(num)} (distance from 0)"
            
        elif qtype == 'expression':
            a = random.randint(-10, -1)
            b = random.randint(1, 10)
            result = abs(a) + abs(b)
            txt = f"Calculate: |{a}| + |{b}|"
            ans = str(result)
            wrongs = {str(a + b), str(abs(a + b)), str(result - 1), str(-result)}
            vis = number_line_svg(highlight=[a, b], range_start=-10, range_end=10)
            exp = f"|{a}| + |{b}| = {abs(a)} + {abs(b)} = {result}"
            
        elif qtype == 'compare':
            a = random.randint(-10, -1)
            b = random.randint(1, 10)
            txt = f"Which is larger: |{a}| or |{b}|?"
            if abs(a) > abs(b):
                ans = f"|{a}|"
            elif abs(b) > abs(a):
                ans = f"|{b}|"
            else:
                ans = "They are equal"
            wrongs = {f"|{a}|", f"|{b}|", "They are equal", f"{a}"}
            vis = number_line_svg(highlight=[a, b], range_start=-10, range_end=10)
            exp = f"|{a}| = {abs(a)}, |{b}| = {abs(b)}. {ans} is larger."
            
        elif qtype == 'equation':
            val = random.randint(1, 10)
            txt = f"If |x| = {val}, what are the possible values of x?"
            ans = f"{val} or -{val}"
            wrongs = {f"Only {val}", f"Only -{val}", f"{val}", "0"}
            vis = number_line_svg(highlight=[val, -val], range_start=-10, range_end=10)
            exp = f"|x| = {val} means x = {val} or x = -{val} (both are {val} away from 0)"
            
        else:  # meaning
            txt = "What does |x| represent?"
            ans = "Distance from 0 on the number line"
            wrongs = {"The opposite of x", "x squared", "The sign of x", "Half of x"}
            vis = number_line_svg(highlight=[-5, 5], range_start=-10, range_end=10)
            exp = "Absolute value |x| is the distance from x to 0, always positive or zero"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 9: Factors & Multiples
def gen_level_9(n=50):
    """Higher: Find factors and multiples"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['factors', 'multiples', 'is_factor', 'is_multiple', 'common_factor'])
        
        if qtype == 'factors':
            num = random.choice([12, 15, 18, 20, 24, 30, 36])
            factors = [i for i in range(1, num + 1) if num % i == 0]
            txt = f"List all factors of {num}."
            ans = str(factors)
            # Generate wrong answers
            wrong1 = factors[:-1]  # Missing last
            wrong2 = factors + [num + 1]  # Extra wrong one
            wrong3 = [i for i in range(1, num) if num % i == 0]  # Missing num itself
            wrongs = {str(wrong1), str(wrong2), str(wrong3)}
            vis = factor_tree_svg(num)
            exp = f"Factors of {num} are numbers that divide {num} evenly: {factors}"
            
        elif qtype == 'multiples':
            num = random.randint(3, 9)
            multiples = [num * i for i in range(1, 6)]
            txt = f"List the first 5 multiples of {num}."
            ans = str(multiples)
            wrong1 = [num * i for i in range(0, 5)]  # Starts with 0
            wrong2 = [num * i for i in range(1, 6) if i != 3] + [num * 6]
            wrongs = {str(wrong1), str(wrong2), str([num + i for i in range(5)])}
            vis = number_line_svg(highlight=multiples[:3], range_start=0, range_end=max(multiples)+5)
            exp = f"Multiples of {num}: {num}×1, {num}×2, ... = {multiples}"
            
        elif qtype == 'is_factor':
            num = random.choice([12, 18, 24, 30, 36])
            test = random.randint(2, 10)
            is_factor = num % test == 0
            txt = f"Is {test} a factor of {num}?"
            ans = "Yes" if is_factor else "No"
            wrongs = {"Yes", "No", "Sometimes", "Cannot determine"}
            vis = factor_tree_svg(num)
            exp = f"{num} ÷ {test} = {num/test}. {'Divides evenly' if is_factor else 'Does not divide evenly'} → {ans}"
            
        elif qtype == 'is_multiple':
            base = random.randint(3, 8)
            test = base * random.randint(2, 8) + random.choice([0, 0, 1])  # Sometimes not a multiple
            is_multiple = test % base == 0
            txt = f"Is {test} a multiple of {base}?"
            ans = "Yes" if is_multiple else "No"
            wrongs = {"Yes", "No", "Sometimes", "Cannot determine"}
            vis = number_line_svg(range_start=0, range_end=test+5)
            exp = f"{test} ÷ {base} = {test/base}. {'Whole number' if is_multiple else 'Not whole'} → {ans}"
            
        else:  # common_factor
            num1 = random.choice([12, 18, 24])
            num2 = random.choice([15, 20, 30])
            common = [i for i in range(1, min(num1, num2) + 1) if num1 % i == 0 and num2 % i == 0]
            txt = f"Find a common factor of {num1} and {num2} (other than 1)."
            ans = str(common[-1] if len(common) > 1 else common[0])
            wrongs = {str(num1), str(num2), str(num1 + num2), str(max(common) + 1) if common else "2"}
            vis = factor_tree_svg(num1)
            exp = f"Common factors of {num1} and {num2}: {common}. Largest: {common[-1]}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 10: Prime Numbers & Factorization
def gen_level_10(n=50):
    """Mastery: Identify primes and find prime factorization"""
    qs = []
    used = set()
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['is_prime', 'factorize', 'product_primes', 'next_prime', 'count_primes'])
        
        if qtype == 'is_prime':
            num = random.choice(primes + composites)
            is_prime = num in primes
            txt = f"Is {num} a prime number?"
            ans = "Yes" if is_prime else "No"
            wrongs = {"Yes", "No", "Sometimes", "Cannot determine"}
            vis = factor_tree_svg(num)
            if is_prime:
                exp = f"{num} has only two factors: 1 and {num}. It is prime."
            else:
                factors = [i for i in range(2, num) if num % i == 0]
                exp = f"{num} = {factors[0]} × {num // factors[0]}. It has more than 2 factors, so not prime."
                
        elif qtype == 'factorize':
            num = random.choice([12, 18, 20, 24, 30, 36, 40, 45, 48, 50])
            # Find prime factorization
            factors = []
            temp = num
            d = 2
            while d * d <= temp:
                while temp % d == 0:
                    factors.append(d)
                    temp //= d
                d += 1
            if temp > 1:
                factors.append(temp)
            
            txt = f"Write {num} as a product of prime factors."
            ans = " × ".join(map(str, factors))
            # Generate wrong answers
            wrongs = {
                " × ".join(map(str, factors[:-1] + [factors[-1] + 1])) if factors else "2 × 2",
                " × ".join(map(str, [2] * (len(factors) + 1))),
                f"1 × {num}"
            }
            vis = factor_tree_svg(num)
            exp = f"{num} = {ans}"
            
        elif qtype == 'product_primes':
            p1 = random.choice([2, 3, 5])
            p2 = random.choice([2, 3, 5, 7])
            product = p1 * p2
            txt = f"What is {p1} × {p2}?"
            ans = str(product)
            wrongs = {str(product + 1), str(product - 1), str(p1 + p2), str(product + p1)}
            vis = factor_tree_svg(product)
            exp = f"{p1} × {p2} = {product}"
            
        elif qtype == 'next_prime':
            start = random.choice([10, 15, 20, 25, 30])
            next_p = [p for p in primes if p > start][0]
            txt = f"What is the smallest prime number greater than {start}?"
            ans = str(next_p)
            wrongs = {str(start + 1), str(start + 2), str(next_p + 2), str(start)}
            vis = number_line_svg(highlight=[next_p], range_start=start-2, range_end=start+15)
            exp = f"Checking: {start+1}... The smallest prime > {start} is {next_p}"
            
        else:  # count_primes
            limit = random.choice([10, 15, 20])
            count = len([p for p in primes if p <= limit])
            txt = f"How many prime numbers are there from 1 to {limit}?"
            ans = str(count)
            primes_list = [p for p in primes if p <= limit]
            wrongs = {str(count + 1), str(count - 1), str(limit // 2), str(count + 2)}
            vis = number_line_svg(highlight=primes_list[:5], range_start=0, range_end=limit+2)
            exp = f"Primes up to {limit}: {primes_list}. Count = {count}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 11: HCF and LCM
def gen_level_11(n=50):
    """Mastery: Calculate HCF and LCM"""
    qs = []
    used = set()
    
    hcf_pairs = [(12, 18), (15, 20), (24, 36), (18, 24), (20, 30), (14, 21), (16, 24), (8, 12),
                 (9, 12), (10, 15), (6, 9), (8, 20), (12, 16), (15, 25), (18, 27), (21, 28),
                 (24, 32), (30, 45), (12, 15), (14, 35), (16, 20), (18, 30), (20, 25), (22, 33)]
    
    lcm_pairs = [(4, 6), (3, 5), (6, 8), (4, 5), (6, 9), (8, 12), (5, 7), (3, 4),
                 (2, 7), (3, 8), (4, 9), (5, 6), (6, 7), (7, 8), (8, 9), (4, 10),
                 (5, 8), (6, 10), (3, 7), (4, 7), (5, 9), (2, 9), (3, 10), (4, 11)]
    
    for _ in range(n * 30):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['hcf', 'lcm', 'hcf_context', 'lcm_context', 'both', 'identify'])
        
        if qtype == 'hcf':
            a, b = random.choice(hcf_pairs)
            # Randomize order
            if random.random() > 0.5:
                a, b = b, a
            hcf = math.gcd(a, b)
            txt = f"Find the HCF (Highest Common Factor) of {a} and {b}."
            ans = str(hcf)
            wrongs = {str(hcf + 1), str(hcf - 1) if hcf > 1 else "0", str(a * b // hcf), str(min(a, b))}
            vis = factor_tree_svg(a)
            exp = f"Factors of {a}: {[i for i in range(1, a+1) if a % i == 0]}. Factors of {b}: {[i for i in range(1, b+1) if b % i == 0]}. HCF = {hcf}"
            
        elif qtype == 'lcm':
            a, b = random.choice(lcm_pairs)
            if random.random() > 0.5:
                a, b = b, a
            lcm = (a * b) // math.gcd(a, b)
            txt = f"Find the LCM (Lowest Common Multiple) of {a} and {b}."
            ans = str(lcm)
            wrongs = {str(a * b), str(math.gcd(a, b)), str(lcm + a), str(a + b)}
            vis = number_line_svg(highlight=[lcm] if lcm <= 50 else [], range_start=0, range_end=min(lcm+5, 50))
            exp = f"Multiples of {a}: {[a*i for i in range(1, 6)]}. Multiples of {b}: {[b*i for i in range(1, 6)]}. LCM = {lcm}"
            
        elif qtype == 'hcf_context':
            contexts = [
                (12, 18, "ribbon", "cm"),
                (15, 20, "rope", "m"),
                (24, 36, "wire", "cm"),
                (18, 24, "fabric", "cm"),
                (20, 30, "wood", "cm"),
                (16, 24, "paper", "cm"),
            ]
            a, b, material, unit = random.choice(contexts)
            hcf = math.gcd(a, b)
            txt = f"Two pieces of {material} are {a}{unit} and {b}{unit} long. What is the longest equal length they can both be cut into?"
            ans = f"{hcf} {unit}"
            wrongs = {f"{hcf + 1} {unit}", f"{min(a,b)} {unit}", f"{a + b} {unit}", f"{hcf - 1} {unit}" if hcf > 1 else f"1 {unit}"}
            vis = factor_tree_svg(a)
            exp = f"This is an HCF problem. HCF({a}, {b}) = {hcf} {unit}"
            
        elif qtype == 'lcm_context':
            contexts = [
                (4, 6, "Bus A", "Bus B"),
                (3, 5, "Train A", "Train B"),
                (6, 8, "Bell A", "Bell B"),
                (5, 7, "Light A", "Light B"),
                (3, 4, "Timer A", "Timer B"),
                (4, 5, "Alarm A", "Alarm B"),
            ]
            a, b, item1, item2 = random.choice(contexts)
            lcm = (a * b) // math.gcd(a, b)
            txt = f"{item1} comes every {a} minutes, {item2} every {b} minutes. If both leave now, when will they next leave together?"
            ans = f"{lcm} minutes"
            wrongs = {f"{a * b} minutes", f"{a + b} minutes", f"{math.gcd(a, b)} minutes", f"{lcm + a} minutes"}
            vis = number_line_svg(highlight=[lcm] if lcm <= 50 else [], range_start=0, range_end=min(lcm+5, 50))
            exp = f"This is an LCM problem. LCM({a}, {b}) = {lcm} minutes"
            
        elif qtype == 'both':
            a, b = random.choice([(6, 8), (12, 15), (10, 15), (8, 12), (9, 12), (6, 9)])
            hcf = math.gcd(a, b)
            lcm = (a * b) // hcf
            variant = random.choice(['compare', 'product', 'sum'])
            
            if variant == 'compare':
                txt = f"For {a} and {b}, which is larger: HCF or LCM?"
                ans = "LCM"
                wrongs = {"HCF", "They are equal", "Cannot determine"}
                exp = f"HCF({a}, {b}) = {hcf}, LCM({a}, {b}) = {lcm}. LCM is always ≥ HCF."
            elif variant == 'product':
                txt = f"HCF({a}, {b}) × LCM({a}, {b}) = ?"
                ans = str(a * b)
                wrongs = {str(hcf + lcm), str(hcf * 2), str(lcm * 2), str(a + b)}
                exp = f"HCF × LCM = {hcf} × {lcm} = {a * b} (always equals the product of the numbers)"
            else:
                txt = f"What is HCF({a}, {b}) + LCM({a}, {b})?"
                ans = str(hcf + lcm)
                wrongs = {str(a * b), str(hcf * lcm), str(a + b), str(hcf + lcm + 1)}
                exp = f"HCF({a}, {b}) = {hcf}, LCM({a}, {b}) = {lcm}. Sum = {hcf + lcm}"
            vis = factor_tree_svg(a)
            
        else:  # identify
            a, b = random.choice([(12, 18), (8, 12), (15, 20)])
            hcf = math.gcd(a, b)
            lcm = (a * b) // hcf
            scenarios = [
                (f"Finding the largest tile size that fits evenly into a {a}×{b} floor", "HCF"),
                (f"Finding when two events repeating every {a} and {b} days coincide", "LCM"),
                (f"Cutting {a}cm and {b}cm ribbons into equal longest pieces", "HCF"),
                (f"Two lights flashing every {a} and {b} seconds - when do they flash together?", "LCM"),
            ]
            scenario, answer = random.choice(scenarios)
            txt = f"This problem requires: {scenario}"
            ans = answer
            wrongs = {"HCF", "LCM", "Neither", "Both"}
            vis = factor_tree_svg(a)
            exp = f"Equal parts/largest common → HCF. When things coincide → LCM. Answer: {ans}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 12: Problem Solving & Applications
def gen_level_12(n=50):
    """Mastery: Complex integer problems"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['temperature', 'money', 'elevation', 'sequence', 'mixed'])
        
        if qtype == 'temperature':
            start = random.randint(-15, 10)
            changes = [random.randint(-10, 10) for _ in range(3)]
            final = start + sum(changes)
            txt = f"Temperature starts at {start}°C. It changes by {changes[0]}°C, then {changes[1]}°C, then {changes[2]}°C. Final temperature?"
            ans = f"{final}°C"
            wrongs = {f"{final + 2}°C", f"{final - 2}°C", f"{abs(final)}°C", f"{-final}°C"}
            vis = temperature_svg(final)
            exp = f"{start} + {changes[0]} + {changes[1]} + {changes[2]} = {final}°C"
            
        elif qtype == 'money':
            start = random.randint(50, 200)
            spend = random.randint(30, start - 20)
            earn = random.randint(20, 80)
            spend2 = random.randint(10, 50)
            final = start - spend + earn - spend2
            txt = f"You have €{start}. You spend €{spend}, earn €{earn}, then spend €{spend2}. How much do you have?"
            ans = f"€{final}"
            wrongs = {f"€{final + 10}", f"€{final - 10}", f"€{start - spend}", f"€{abs(final)}"}
            vis = number_line_svg(range_start=0, range_end=start + earn)
            exp = f"€{start} - €{spend} + €{earn} - €{spend2} = €{final}"
            
        elif qtype == 'elevation':
            ground = 0
            up = random.randint(5, 20)
            down = random.randint(10, 30)
            up2 = random.randint(5, 15)
            final = ground + up - down + up2
            txt = f"A lift starts at ground (0). It goes up {up} floors, down {down} floors, then up {up2} floors. Final floor?"
            ans = str(final)
            wrongs = {str(final + 2), str(final - 2), str(abs(final)), str(up + up2 - down + 5)}
            vis = number_line_svg(highlight=[final], range_start=-20, range_end=20)
            exp = f"0 + {up} - {down} + {up2} = {final}"
            
        elif qtype == 'sequence':
            start = random.randint(-5, 5)
            diff = random.choice([-3, -2, 2, 3])
            seq = [start + diff * i for i in range(5)]
            txt = f"What is the next number in the sequence: {seq[:4]}...?"
            ans = str(seq[4])
            wrongs = {str(seq[4] + diff), str(seq[4] - diff), str(seq[3] + 1), str(seq[3] * 2)}
            vis = number_line_svg(highlight=seq, range_start=min(seq)-3, range_end=max(seq)+3)
            exp = f"Pattern: add {diff} each time. Next: {seq[3]} + {diff} = {seq[4]}"
            
        else:  # mixed
            a = random.randint(-5, 5)
            b = random.randint(2, 6)
            c = random.randint(-4, 4)
            result = (a + b) * c
            txt = f"Calculate: ({a} + {b}) × {c}"
            ans = str(result)
            wrongs = {str(a + b * c), str(a * b + c), str(-result), str(abs(result))}
            vis = number_line_svg(range_start=-30, range_end=30)
            exp = f"Brackets first: {a} + {b} = {a+b}. Then: {a+b} × {c} = {result}"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Main generator
def generate_all():
    """Generate all 600 questions"""
    all_questions = []
    generators = [
        (1, gen_level_1), (2, gen_level_2), (3, gen_level_3), (4, gen_level_4),
        (5, gen_level_5), (6, gen_level_6), (7, gen_level_7), (8, gen_level_8),
        (9, gen_level_9), (10, gen_level_10), (11, gen_level_11), (12, gen_level_12)
    ]
    
    for level, gen in generators:
        print(f"Generating Level {level}...")
        qs = gen(QUESTIONS_PER_LEVEL)
        for q in qs:
            q['level'] = level
            q['topic'] = TOPIC
            q['mode'] = MODE
        all_questions.extend(qs)
    
    return all_questions


def validate(questions):
    """Validate generated questions"""
    errors = []
    level_counts = {i: 0 for i in range(1, 13)}
    visual_counts = {i: 0 for i in range(1, 13)}
    
    for q in questions:
        level = q['level']
        level_counts[level] += 1
        
        # Check required fields
        required = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 
                   'correct_idx', 'explanation', 'level', 'topic', 'mode']
        for field in required:
            if field not in q or q[field] is None:
                errors.append(f"L{level}: Missing {field}")
        
        # Check 4 unique options
        opts = [q.get('option_a'), q.get('option_b'), q.get('option_c'), q.get('option_d')]
        if len(set(opts)) != 4:
            errors.append(f"L{level}: Non-unique options: {opts}")
        
        # Check visual
        if q.get('image_svg'):
            visual_counts[level] += 1
    
    return errors, level_counts, visual_counts


def print_summary(errors, level_counts, visual_counts):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    all_pass = True
    for level in range(1, 13):
        count = level_counts[level]
        vis_pct = (visual_counts[level] / count * 100) if count > 0 else 0
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        if count < QUESTIONS_PER_LEVEL:
            all_pass = False
        bar = "█" * (count // 2) + " " * (25 - count // 2)
        print(f"Level {level:2}: [{bar}] {count}/{QUESTIONS_PER_LEVEL} | Vis: {vis_pct:.0f}% | {status}")
    
    print("=" * 60)
    print(f"Total Errors: {len(errors)}")
    if errors[:10]:
        for e in errors[:10]:
            print(f"  - {e}")
    
    return all_pass


def insert_to_db(questions):
    """Insert questions to database"""
    import sqlite3
    import os
    
    db_paths = [
        'instance/mathquiz.db',
        '../instance/mathquiz.db',
        '/home/bbsisk/mathappR12/instance/mathquiz.db'
    ]
    
    db_path = None
    for path in db_paths:
        if os.path.exists(path):
            db_path = path
            break
    
    if not db_path:
        print("Database not found. Please run from app directory.")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Delete existing
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (TOPIC,))
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions")
    conn.commit()
    
    # Insert new
    inserted = 0
    errors = 0
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text, option_a, option_b, option_c, option_d,
                 correct_answer, explanation, mode, image_svg)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'],
                q['level'],
                get_difficulty_band(q['level']),
                q['question_text'],
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_idx'],
                q['explanation'],
                q['mode'],
                q.get('image_svg', '')
            ))
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"Insert error: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"Inserted {inserted} questions, {errors} errors")
    return errors == 0


if __name__ == "__main__":
    print("=" * 60)
    print("AgentMath - Integers & Number Systems Generator v1")
    print("=" * 60)
    
    qs = generate_all()
    errors, level_counts, visual_counts = validate(qs)
    all_pass = print_summary(errors, level_counts, visual_counts)
    
    print("\n" + "=" * 60)
    response = input("Insert? (y/n): ").strip().lower()
    if response == 'y':
        if insert_to_db(qs):
            print("✓ Successfully inserted all questions!")
        else:
            print("✗ Some errors occurred during insertion")
    else:
        print("Cancelled.")
