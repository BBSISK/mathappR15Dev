#!/usr/bin/env python3
"""
AgentMath - Indices & Scientific Notation Generator v1
Junior Cycle Mathematics - SEC Aligned

12 Levels:
1. Understanding Index Notation - Foundation
2. Squares and Cubes - Foundation
3. Index Laws: Multiplication (a^m × a^n = a^(m+n)) - Foundation
4. Index Laws: Division (a^m ÷ a^n = a^(m-n)) - Ordinary
5. Index Laws: Power of a Power ((a^m)^n = a^(mn)) - Ordinary
6. Zero and Negative Indices - Ordinary
7. Fractional Indices (Roots) - Higher
8. Scientific Notation: Large Numbers - Higher
9. Scientific Notation: Small Numbers - Higher
10. Calculations with Scientific Notation - Mastery
11. Mixed Index Problems - Mastery
12. Problem Solving & Applications - Mastery

SEC References:
- 2022-2025 OL/HL: Index notation
- Scientific notation for large/small numbers
- Laws of indices
"""

import random
import math

TOPIC = "indices"
MODE = "jc_exam"
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12


# Visual SVG generators
def index_notation_svg(base, exponent, expanded=True):
    """Visual showing index notation with optional expansion"""
    svg = '''<svg viewBox="0 0 220 80" xmlns="http://www.w3.org/2000/svg">
    <rect width="220" height="80" fill="#fef3c7"/>
    '''
    
    # Show base^exponent
    svg += f'<text x="30" y="45" font-size="28" fill="#1e293b" font-weight="bold">{base}</text>'
    svg += f'<text x="55" y="30" font-size="18" fill="#dc2626" font-weight="bold">{exponent}</text>'
    
    if expanded and exponent > 0 and exponent <= 5:
        # Show expansion
        svg += f'<text x="80" y="45" font-size="20" fill="#64748b">=</text>'
        expansion = ' × '.join([str(base)] * exponent)
        svg += f'<text x="100" y="45" font-size="16" fill="#059669">{expansion}</text>'
    
    svg += '</svg>'
    return svg


def scientific_notation_svg(number, is_large=True):
    """Visual showing scientific notation conversion"""
    svg = '''<svg viewBox="0 0 280 90" xmlns="http://www.w3.org/2000/svg">
    <rect width="280" height="90" fill="#f0f9ff"/>
    '''
    
    if is_large:
        # Large number
        svg += f'<text x="20" y="35" font-size="14" fill="#64748b">Large number:</text>'
        svg += f'<text x="20" y="55" font-size="16" fill="#1e293b" font-weight="bold">{number:,}</text>'
        
        # Convert
        exp = len(str(int(number))) - 1
        mantissa = number / (10 ** exp)
        svg += f'<text x="20" y="80" font-size="14" fill="#059669">= {mantissa} × 10</text>'
        svg += f'<text x="120" y="70" font-size="11" fill="#dc2626" font-weight="bold">{exp}</text>'
    else:
        # Small number
        svg += f'<text x="20" y="35" font-size="14" fill="#64748b">Small number:</text>'
        svg += f'<text x="20" y="55" font-size="16" fill="#1e293b" font-weight="bold">{number}</text>'
        
        # Convert - count decimal places
        str_num = f"{number:.10f}".rstrip('0')
        if '.' in str_num:
            decimal_part = str_num.split('.')[1]
            exp = -len(decimal_part.lstrip('0')) - (1 if decimal_part[0] == '0' else 0)
            mantissa = number * (10 ** -exp)
        else:
            exp = 0
            mantissa = number
        svg += f'<text x="20" y="80" font-size="14" fill="#059669">= {mantissa:.1f} × 10</text>'
        svg += f'<text x="130" y="70" font-size="11" fill="#dc2626" font-weight="bold">{exp}</text>'
    
    svg += '</svg>'
    return svg


def index_law_svg(law_type):
    """Visual showing index law"""
    laws = {
        'multiply': ('a^m × a^n = a^(m+n)', 'Multiply: ADD powers'),
        'divide': ('a^m ÷ a^n = a^(m-n)', 'Divide: SUBTRACT powers'),
        'power': ('(a^m)^n = a^(m×n)', 'Power of power: MULTIPLY'),
        'zero': ('a^0 = 1', 'Zero power = 1 (always!)'),
        'negative': ('a^(-n) = 1/a^n', 'Negative: Flip to fraction'),
        'fractional': ('a^(1/n) = ⁿ√a', 'Fraction power = Root'),
    }
    
    formula, explanation = laws.get(law_type, ('', ''))
    
    svg = f'''<svg viewBox="0 0 240 70" xmlns="http://www.w3.org/2000/svg">
    <rect width="240" height="70" fill="#ecfdf5"/>
    <text x="120" y="30" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="bold">{formula}</text>
    <text x="120" y="55" font-size="12" fill="#059669" text-anchor="middle">{explanation}</text>
    </svg>'''
    return svg


def power_tower_svg(base, exp, result):
    """Visual showing base, exponent, and result"""
    svg = f'''<svg viewBox="0 0 180 100" xmlns="http://www.w3.org/2000/svg">
    <rect width="180" height="100" fill="#fdf4ff"/>
    
    <rect x="20" y="20" width="50" height="60" rx="8" fill="#8b5cf6" opacity="0.2"/>
    <text x="45" y="55" font-size="24" fill="#7c3aed" text-anchor="middle" font-weight="bold">{base}</text>
    <text x="65" y="35" font-size="16" fill="#dc2626" font-weight="bold">{exp}</text>
    
    <text x="90" y="55" font-size="20" fill="#64748b">=</text>
    
    <rect x="110" y="20" width="55" height="60" rx="8" fill="#22c55e" opacity="0.2"/>
    <text x="137" y="58" font-size="20" fill="#16a34a" text-anchor="middle" font-weight="bold">{result}</text>
    </svg>'''
    return svg


def make_options(correct, wrong_set):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    wrong_list = [str(w) for w in wrong_set if str(w) != correct_str]
    random.shuffle(wrong_list)
    
    options = [correct_str] + wrong_list[:3]
    
    while len(options) < 4:
        if isinstance(correct, (int, float)):
            wrong = correct + random.choice([-2, -1, 1, 2]) * random.randint(1, 5)
        else:
            wrong = random.randint(1, 100)
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


# Level 1: Understanding Index Notation
def gen_level_1(n=50):
    """Foundation: Understand what indices mean"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['read_index', 'write_index', 'meaning', 'expand', 'count'])
        
        if qtype == 'read_index':
            base = random.randint(2, 10)
            exp = random.randint(2, 5)
            txt = f"How do you read {base}^{exp}?"
            ans = f"{base} to the power of {exp}"
            wrongs = {f"{base} times {exp}", f"{exp} to the power of {base}", 
                     f"{base} plus {exp}", f"{base} multiplied by {exp}"}
            vis = index_notation_svg(base, exp, expanded=False)
            exp_text = f"{base}^{exp} is read as '{base} to the power of {exp}'"
            
        elif qtype == 'write_index':
            base = random.randint(2, 7)
            times = random.randint(2, 5)
            expansion = ' × '.join([str(base)] * times)
            txt = f"Write {expansion} using index notation."
            ans = f"{base}^{times}"
            wrongs = {f"{base}^{times+1}", f"{base}^{times-1}", f"{times}^{base}", f"{base*times}"}
            vis = index_notation_svg(base, times)
            exp_text = f"{expansion} = {base} multiplied {times} times = {base}^{times}"
            
        elif qtype == 'meaning':
            base = random.randint(2, 6)
            exp = random.randint(2, 4)
            txt = f"What does {base}^{exp} mean?"
            ans = f"{base} multiplied by itself {exp} times"
            wrongs = {f"{base} × {exp}", f"{base} + {base} + ... ({exp} times)",
                     f"{exp} × {base}", f"{base} added {exp} times"}
            vis = index_notation_svg(base, exp)
            exp_text = f"{base}^{exp} means multiply {base} by itself {exp} times"
            
        elif qtype == 'expand':
            base = random.randint(2, 5)
            exp = random.randint(2, 4)
            expansion = ' × '.join([str(base)] * exp)
            txt = f"Expand {base}^{exp}"
            ans = expansion
            # Create wrong expansions
            wrong1 = ' × '.join([str(base)] * (exp + 1))
            wrong2 = ' × '.join([str(base)] * (exp - 1)) if exp > 2 else f"{base}"
            wrong3 = f"{base} × {exp}"
            wrongs = {wrong1, wrong2, wrong3, ' + '.join([str(base)] * exp)}
            vis = index_notation_svg(base, exp)
            exp_text = f"{base}^{exp} = {expansion}"
            
        else:  # count
            base = random.randint(2, 6)
            times = random.randint(2, 5)
            expansion = ' × '.join([str(base)] * times)
            txt = f"In {expansion}, how many times is {base} multiplied?"
            ans = str(times)
            wrongs = {str(times + 1), str(times - 1), str(base), str(times + 2)}
            vis = index_notation_svg(base, times)
            exp_text = f"Count the {base}s: there are {times} of them, so it's {base}^{times}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': vis
        })
    
    return qs


# Level 2: Squares and Cubes
def gen_level_2(n=50):
    """Foundation: Calculate squares and cubes"""
    qs = []
    used = set()
    
    for _ in range(n * 30):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['square', 'cube', 'square_root', 'cube_root', 'identify', 'fourth', 'compare'])
        
        if qtype == 'square':
            base = random.randint(1, 15)
            result = base ** 2
            txt = f"Calculate {base}²"
            ans = str(result)
            wrongs = {str(base * 2), str(result + base), str(result - 1), str(base ** 3) if base <= 5 else str(result + 10)}
            vis = power_tower_svg(base, 2, result)
            exp_text = f"{base}² = {base} × {base} = {result}"
            
        elif qtype == 'cube':
            base = random.randint(1, 7)
            result = base ** 3
            txt = f"Calculate {base}³"
            ans = str(result)
            wrongs = {str(base * 3), str(base ** 2), str(result + base), str(result - 1)}
            vis = power_tower_svg(base, 3, result)
            exp_text = f"{base}³ = {base} × {base} × {base} = {result}"
            
        elif qtype == 'square_root':
            root = random.randint(1, 12)
            square = root ** 2
            txt = f"What is √{square}?"
            ans = str(root)
            wrongs = {str(root + 1), str(root - 1) if root > 1 else "0", str(square // 2), str(root + 2)}
            vis = power_tower_svg(root, 2, square)
            exp_text = f"√{square} = {root} because {root}² = {square}"
            
        elif qtype == 'cube_root':
            root = random.randint(1, 6)
            cube = root ** 3
            txt = f"What is ³√{cube}?"
            ans = str(root)
            wrongs = {str(root + 1), str(root - 1) if root > 1 else "0", str(cube // 3), str(root * 2)}
            vis = power_tower_svg(root, 3, cube)
            exp_text = f"³√{cube} = {root} because {root}³ = {cube}"
            
        elif qtype == 'identify':
            is_square = random.choice([True, False])
            if is_square:
                root = random.randint(2, 10)
                num = root ** 2
                txt = f"Is {num} a perfect square?"
                ans = "Yes"
                exp_text = f"Yes, {num} = {root}² = {root} × {root}"
            else:
                num = random.choice([3, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20])
                txt = f"Is {num} a perfect square?"
                ans = "No"
                exp_text = f"No, {num} is not a perfect square (no whole number × itself = {num})"
            wrongs = {"Yes", "No", "Only sometimes", "Cannot determine"}
            vis = power_tower_svg(num, '?', '?')
            
        elif qtype == 'fourth':
            base = random.randint(2, 4)
            result = base ** 4
            txt = f"Calculate {base}⁴"
            ans = str(result)
            wrongs = {str(base * 4), str(base ** 3), str(base ** 2), str(result + base)}
            vis = power_tower_svg(base, 4, result)
            exp_text = f"{base}⁴ = {base} × {base} × {base} × {base} = {result}"
            
        else:  # compare
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            while a == b:
                b = random.randint(2, 5)
            txt = f"Which is larger: {a}² or {b}²?"
            if a ** 2 > b ** 2:
                ans = f"{a}²"
            else:
                ans = f"{b}²"
            wrongs = {f"{a}²", f"{b}²", "They are equal", "Cannot compare"}
            vis = power_tower_svg(max(a, b), 2, max(a, b) ** 2)
            exp_text = f"{a}² = {a**2}, {b}² = {b**2}. {ans} is larger."
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': vis
        })
    
    return qs


# Level 3: Index Laws - Multiplication
def gen_level_3(n=50):
    """Foundation: Multiply same base - add powers"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['calculate', 'simplify', 'rule', 'find_missing'])
        
        if qtype == 'calculate':
            base = random.randint(2, 5)
            exp1 = random.randint(1, 4)
            exp2 = random.randint(1, 4)
            result_exp = exp1 + exp2
            txt = f"Simplify: {base}^{exp1} × {base}^{exp2}"
            ans = f"{base}^{result_exp}"
            wrongs = {f"{base}^{exp1 * exp2}", f"{base}^{exp1 - exp2}", f"{base*2}^{result_exp}", f"{base}^{result_exp + 1}"}
            exp_text = f"When multiplying same base, ADD powers: {base}^{exp1} × {base}^{exp2} = {base}^({exp1}+{exp2}) = {base}^{result_exp}"
            
        elif qtype == 'simplify':
            base = random.choice(['a', 'x', 'y', 'm'])
            exp1 = random.randint(2, 5)
            exp2 = random.randint(2, 5)
            result_exp = exp1 + exp2
            txt = f"Simplify: {base}^{exp1} × {base}^{exp2}"
            ans = f"{base}^{result_exp}"
            wrongs = {f"{base}^{exp1 * exp2}", f"{base}^{abs(exp1 - exp2)}", f"2{base}^{exp1}", f"{base}^{result_exp - 1}"}
            exp_text = f"Add powers: {exp1} + {exp2} = {result_exp}. Answer: {base}^{result_exp}"
            
        elif qtype == 'rule':
            txt = "When multiplying powers with the same base, you should:"
            ans = "Add the powers"
            wrongs = {"Multiply the powers", "Subtract the powers", "Divide the powers", "Keep the same power"}
            exp_text = "Multiplication rule: a^m × a^n = a^(m+n) → ADD powers"
            
        else:  # find_missing
            base = random.randint(2, 5)
            exp1 = random.randint(2, 4)
            result_exp = random.randint(5, 8)
            exp2 = result_exp - exp1
            txt = f"Find ?: {base}^{exp1} × {base}^? = {base}^{result_exp}"
            ans = str(exp2)
            wrongs = {str(exp2 + 1), str(exp2 - 1), str(result_exp), str(exp1)}
            exp_text = f"{exp1} + ? = {result_exp}, so ? = {result_exp} - {exp1} = {exp2}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': index_law_svg('multiply')
        })
    
    return qs


# Level 4: Index Laws - Division
def gen_level_4(n=50):
    """Ordinary: Divide same base - subtract powers"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['calculate', 'simplify', 'rule', 'find_missing'])
        
        if qtype == 'calculate':
            base = random.randint(2, 5)
            exp1 = random.randint(4, 8)
            exp2 = random.randint(1, 3)
            result_exp = exp1 - exp2
            txt = f"Simplify: {base}^{exp1} ÷ {base}^{exp2}"
            ans = f"{base}^{result_exp}"
            wrongs = {f"{base}^{exp1 + exp2}", f"{base}^{exp1 * exp2}", f"{base}^{exp2 - exp1}", f"{base}^{result_exp + 1}"}
            exp_text = f"When dividing same base, SUBTRACT powers: {base}^{exp1} ÷ {base}^{exp2} = {base}^({exp1}-{exp2}) = {base}^{result_exp}"
            
        elif qtype == 'simplify':
            base = random.choice(['a', 'x', 'y', 'p'])
            exp1 = random.randint(5, 9)
            exp2 = random.randint(2, 4)
            result_exp = exp1 - exp2
            txt = f"Simplify: {base}^{exp1} ÷ {base}^{exp2}"
            ans = f"{base}^{result_exp}"
            wrongs = {f"{base}^{exp1 + exp2}", f"{base}^{exp1 * exp2}", f"{base}^{exp2}", f"{base}^{result_exp - 1}"}
            exp_text = f"Subtract powers: {exp1} - {exp2} = {result_exp}. Answer: {base}^{result_exp}"
            
        elif qtype == 'rule':
            txt = "When dividing powers with the same base, you should:"
            ans = "Subtract the powers"
            wrongs = {"Add the powers", "Multiply the powers", "Divide the powers", "Keep the larger power"}
            exp_text = "Division rule: a^m ÷ a^n = a^(m-n) → SUBTRACT powers"
            
        else:  # find_missing
            base = random.randint(2, 5)
            exp1 = random.randint(6, 10)
            result_exp = random.randint(2, 4)
            exp2 = exp1 - result_exp
            txt = f"Find ?: {base}^{exp1} ÷ {base}^? = {base}^{result_exp}"
            ans = str(exp2)
            wrongs = {str(exp2 + 1), str(exp2 - 1), str(result_exp), str(exp1)}
            exp_text = f"{exp1} - ? = {result_exp}, so ? = {exp1} - {result_exp} = {exp2}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': index_law_svg('divide')
        })
    
    return qs


# Level 5: Index Laws - Power of a Power
def gen_level_5(n=50):
    """Ordinary: (a^m)^n = a^(mn)"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['calculate', 'simplify', 'rule', 'find_missing'])
        
        if qtype == 'calculate':
            base = random.randint(2, 5)
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 3)
            result_exp = exp1 * exp2
            txt = f"Simplify: ({base}^{exp1})^{exp2}"
            ans = f"{base}^{result_exp}"
            wrongs = {f"{base}^{exp1 + exp2}", f"{base}^{exp1}", f"{base}^{exp2}", f"{base}^{result_exp + 1}"}
            exp_text = f"Power of a power: MULTIPLY. ({base}^{exp1})^{exp2} = {base}^({exp1}×{exp2}) = {base}^{result_exp}"
            
        elif qtype == 'simplify':
            base = random.choice(['a', 'x', 'y', 'n'])
            exp1 = random.randint(2, 5)
            exp2 = random.randint(2, 4)
            result_exp = exp1 * exp2
            txt = f"Simplify: ({base}^{exp1})^{exp2}"
            ans = f"{base}^{result_exp}"
            wrongs = {f"{base}^{exp1 + exp2}", f"({base}^{exp1 + exp2})", f"{base}^{exp1}", f"{base}^{result_exp - 1}"}
            exp_text = f"Multiply powers: {exp1} × {exp2} = {result_exp}. Answer: {base}^{result_exp}"
            
        elif qtype == 'rule':
            txt = "To simplify (a^m)^n, you should:"
            ans = "Multiply the powers: a^(m×n)"
            wrongs = {"Add the powers: a^(m+n)", "Subtract the powers: a^(m-n)", "Keep the inner power: a^m", "Divide the powers"}
            exp_text = "Power of a power rule: (a^m)^n = a^(m×n) → MULTIPLY powers"
            
        else:  # find_missing
            base = random.randint(2, 4)
            exp1 = random.randint(2, 4)
            result_exp = random.choice([6, 8, 10, 12])
            exp2 = result_exp // exp1
            if exp1 * exp2 != result_exp:
                continue
            txt = f"Find ?: ({base}^{exp1})^? = {base}^{result_exp}"
            ans = str(exp2)
            wrongs = {str(exp2 + 1), str(exp2 - 1), str(result_exp - exp1), str(exp1)}
            exp_text = f"{exp1} × ? = {result_exp}, so ? = {result_exp} ÷ {exp1} = {exp2}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': index_law_svg('power')
        })
    
    return qs


# Level 6: Zero and Negative Indices
def gen_level_6(n=50):
    """Ordinary: a^0 = 1 and a^(-n) = 1/a^n"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['zero_power', 'negative_power', 'rule_zero', 'rule_negative', 'convert'])
        
        if qtype == 'zero_power':
            base = random.randint(2, 100)
            txt = f"What is {base}^0?"
            ans = "1"
            wrongs = {"0", str(base), str(base - 1), "undefined"}
            exp_text = f"Any number to the power of 0 equals 1. {base}^0 = 1"
            vis = index_law_svg('zero')
            
        elif qtype == 'negative_power':
            base = random.randint(2, 5)
            exp = random.randint(1, 3)
            result = base ** exp
            txt = f"Write {base}^(-{exp}) as a fraction."
            ans = f"1/{result}"
            wrongs = {f"-{result}", f"{result}", f"-1/{result}", f"1/{base}"}
            exp_text = f"{base}^(-{exp}) = 1/{base}^{exp} = 1/{result}"
            vis = index_law_svg('negative')
            
        elif qtype == 'rule_zero':
            base = random.choice(['5', '100', 'x', 'a', '(-3)'])
            txt = f"What is {base}^0?"
            ans = "1"
            wrongs = {"0", base.replace('(', '').replace(')', '').replace('-', ''), "undefined", "-1"}
            exp_text = f"Zero power rule: {base}^0 = 1 (always, except 0^0)"
            vis = index_law_svg('zero')
            
        elif qtype == 'rule_negative':
            txt = "How do you evaluate a negative index like a^(-n)?"
            ans = "Write as 1/a^n (flip to fraction)"
            wrongs = {"Multiply by -1", "It's always negative", "Cannot be calculated", "Subtract n from a"}
            exp_text = "Negative index: a^(-n) = 1/a^n. The negative flips it to a fraction."
            vis = index_law_svg('negative')
            
        else:  # convert
            base = random.randint(2, 5)
            exp = random.randint(1, 3)
            result = base ** exp
            txt = f"Write 1/{result} using a negative index (base {base})."
            ans = f"{base}^(-{exp})"
            wrongs = {f"{base}^{exp}", f"-{base}^{exp}", f"1/{base}^(-{exp})", f"(-{base})^{exp}"}
            exp_text = f"1/{result} = 1/{base}^{exp} = {base}^(-{exp})"
            vis = index_law_svg('negative')
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': vis
        })
    
    return qs


# Level 7: Fractional Indices (Roots)
def gen_level_7(n=50):
    """Higher: a^(1/n) = nth root of a"""
    qs = []
    used = set()
    
    # Perfect powers for nice answers
    squares = {4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7, 64: 8, 81: 9, 100: 10, 121: 11, 144: 12}
    cubes = {8: 2, 27: 3, 64: 4, 125: 5, 216: 6}
    
    for _ in range(n * 30):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['half_power', 'third_power', 'rule', 'convert_to_root', 'convert_to_index', 'calculate_combo', 'meaning'])
        
        if qtype == 'half_power':
            num, root = random.choice(list(squares.items()))
            txt = f"Calculate {num}^(1/2)"
            ans = str(root)
            wrongs = {str(num // 2), str(root + 1), str(root - 1) if root > 1 else "0", str(num)}
            exp_text = f"{num}^(1/2) = √{num} = {root}"
            vis = index_law_svg('fractional')
            
        elif qtype == 'third_power':
            num, root = random.choice(list(cubes.items()))
            txt = f"Calculate {num}^(1/3)"
            ans = str(root)
            wrongs = {str(num // 3), str(root + 1), str(root - 1) if root > 1 else "0", str(num)}
            exp_text = f"{num}^(1/3) = ³√{num} = {root}"
            vis = index_law_svg('fractional')
            
        elif qtype == 'rule':
            rule_variant = random.choice(['half', 'third', 'general'])
            if rule_variant == 'half':
                txt = "What does a^(1/2) mean?"
                ans = "Square root of a (√a)"
                wrongs = {"a divided by 2", "Half of a", "a squared", "a times 2"}
            elif rule_variant == 'third':
                txt = "What does a^(1/3) mean?"
                ans = "Cube root of a (³√a)"
                wrongs = {"a divided by 3", "Third of a", "a cubed", "a times 3"}
            else:
                txt = "What does a^(1/n) mean in general?"
                ans = "The nth root of a"
                wrongs = {"a divided by n", "a times (1/n)", "n divided by a", "a to the power n"}
            exp_text = f"Fractional index 1/n means nth root: a^(1/n) = ⁿ√a"
            vis = index_law_svg('fractional')
            
        elif qtype == 'convert_to_root':
            base = random.choice(['x', 'a', 'y', '25', '64', '27'])
            frac = random.choice(['1/2', '1/3', '1/4', '1/5'])
            if frac == '1/2':
                ans = f"√{base}"
            elif frac == '1/3':
                ans = f"³√{base}"
            elif frac == '1/4':
                ans = f"⁴√{base}"
            else:
                ans = f"⁵√{base}"
            txt = f"Write {base}^({frac}) as a root."
            wrongs = {f"{base}²", f"{base}/2", f"√{base}", f"³√{base}", f"⁴√{base}", f"⁵√{base}", f"{base}³"}
            exp_text = f"a^(1/n) = ⁿ√a, so {base}^({frac}) = {ans}"
            vis = index_law_svg('fractional')
            
        elif qtype == 'convert_to_index':
            num, root = random.choice(list(squares.items()))
            txt = f"Write √{num} using index notation."
            ans = f"{num}^(1/2)"
            wrongs = {f"{num}^2", f"{num}^(1/{num})", f"{root}^2", f"{num}/2"}
            exp_text = f"√{num} = {num}^(1/2) = {root}"
            vis = index_law_svg('fractional')
            
        elif qtype == 'calculate_combo':
            # Questions like 8^(2/3) = (8^(1/3))^2 = 2^2 = 4
            base = random.choice([8, 27, 64])
            if base == 8:
                root = 2
            elif base == 27:
                root = 3
            else:
                root = 4
            power = random.choice([2, 3])
            result = root ** power
            txt = f"Calculate {base}^({power}/3)"
            ans = str(result)
            wrongs = {str(base // 3 * power), str(root), str(base * power // 3), str(result + 1)}
            exp_text = f"{base}^({power}/3) = (³√{base})^{power} = {root}^{power} = {result}"
            vis = index_law_svg('fractional')
            
        else:  # meaning
            txt = "In fractional indices, the denominator tells you:"
            ans = "Which root to take"
            wrongs = {"What to multiply by", "What to divide by", "The power", "The base"}
            exp_text = "In a^(m/n): n (denominator) = which root, m (numerator) = which power"
            vis = index_law_svg('fractional')
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': vis
        })
    
    return qs


# Level 8: Scientific Notation - Large Numbers
def gen_level_8(n=50):
    """Higher: Express large numbers in scientific notation"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['convert_to_sci', 'convert_from_sci', 'identify_parts', 'compare'])
        
        if qtype == 'convert_to_sci':
            mantissa = round(random.uniform(1.1, 9.9), 1)
            exp = random.randint(3, 9)
            number = int(mantissa * (10 ** exp))
            txt = f"Write {number:,} in scientific notation."
            ans = f"{mantissa} × 10^{exp}"
            wrongs = {f"{mantissa} × 10^{exp+1}", f"{mantissa} × 10^{exp-1}", 
                     f"{mantissa*10} × 10^{exp-1}", f"{mantissa/10} × 10^{exp+1}"}
            exp_text = f"{number:,} = {mantissa} × 10^{exp}"
            vis = scientific_notation_svg(number, is_large=True)
            
        elif qtype == 'convert_from_sci':
            mantissa = round(random.uniform(1.1, 9.9), 1)
            exp = random.randint(3, 6)
            number = int(mantissa * (10 ** exp))
            txt = f"What is {mantissa} × 10^{exp} as an ordinary number?"
            ans = f"{number:,}"
            wrongs = {f"{int(number/10):,}", f"{int(number*10):,}", 
                     f"{int(mantissa * exp):,}", f"{number + 1000:,}"}
            exp_text = f"{mantissa} × 10^{exp} = {mantissa} × {'1' + '0'*exp} = {number:,}"
            vis = scientific_notation_svg(number, is_large=True)
            
        elif qtype == 'identify_parts':
            mantissa = round(random.uniform(1.1, 9.9), 1)
            exp = random.randint(4, 8)
            part = random.choice(['mantissa', 'exponent'])
            if part == 'mantissa':
                txt = f"In {mantissa} × 10^{exp}, what is the mantissa (coefficient)?"
                ans = str(mantissa)
                wrongs = {str(exp), str(10), str(mantissa * 10), str(mantissa + 1)}
            else:
                txt = f"In {mantissa} × 10^{exp}, what is the exponent (power of 10)?"
                ans = str(exp)
                wrongs = {str(mantissa), str(10), str(exp + 1), str(exp - 1)}
            exp_text = f"In a × 10^n: a is the mantissa (1-10), n is the exponent"
            vis = scientific_notation_svg(mantissa * (10 ** exp), is_large=True)
            
        else:  # compare
            m1, e1 = round(random.uniform(2, 5), 1), random.randint(5, 7)
            m2, e2 = round(random.uniform(6, 9), 1), random.randint(5, 7)
            n1 = m1 * (10 ** e1)
            n2 = m2 * (10 ** e2)
            txt = f"Which is larger: {m1} × 10^{e1} or {m2} × 10^{e2}?"
            if n1 > n2:
                ans = f"{m1} × 10^{e1}"
            else:
                ans = f"{m2} × 10^{e2}"
            wrongs = {f"{m1} × 10^{e1}", f"{m2} × 10^{e2}", "They are equal", "Cannot compare"}
            exp_text = f"{m1} × 10^{e1} = {n1:,.0f}, {m2} × 10^{e2} = {n2:,.0f}"
            vis = scientific_notation_svg(max(n1, n2), is_large=True)
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': vis
        })
    
    return qs


# Level 9: Scientific Notation - Small Numbers
def gen_level_9(n=50):
    """Higher: Express small numbers in scientific notation"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['convert_to_sci', 'convert_from_sci', 'meaning', 'compare'])
        
        if qtype == 'convert_to_sci':
            mantissa = round(random.uniform(1.1, 9.9), 1)
            exp = random.randint(-6, -2)
            number = mantissa * (10 ** exp)
            # Format the small number
            num_str = f"{number:.{-exp+1}f}".rstrip('0')
            txt = f"Write {num_str} in scientific notation."
            ans = f"{mantissa} × 10^{exp}"
            wrongs = {f"{mantissa} × 10^{-exp}", f"{mantissa} × 10^{exp-1}", 
                     f"{mantissa} × 10^{exp+1}", f"{mantissa/10} × 10^{exp+1}"}
            exp_text = f"{num_str} = {mantissa} × 10^{exp} (negative exponent for small numbers)"
            vis = scientific_notation_svg(number, is_large=False)
            
        elif qtype == 'convert_from_sci':
            mantissa = round(random.uniform(1.1, 9.9), 1)
            exp = random.randint(-5, -2)
            number = mantissa * (10 ** exp)
            num_str = f"{number:.{-exp+1}f}".rstrip('0')
            txt = f"What is {mantissa} × 10^{exp} as a decimal?"
            ans = num_str
            wrongs = {f"{mantissa * (10 ** (exp-1)):.{-exp+2}f}".rstrip('0'),
                     f"{mantissa * (10 ** (exp+1)):.{-exp}f}".rstrip('0'),
                     str(mantissa), f"0.{int(mantissa)}"}
            exp_text = f"{mantissa} × 10^{exp} = {num_str}"
            vis = scientific_notation_svg(number, is_large=False)
            
        elif qtype == 'meaning':
            exp = random.randint(-5, -2)
            txt = f"A negative exponent like 10^{exp} means the number is:"
            ans = "Very small (less than 1)"
            wrongs = {"Very large", "Negative", "Equal to zero", "Between 1 and 10"}
            exp_text = f"Negative exponent = small number. 10^{exp} = {'0.' + '0'*(-exp-1) + '1'}"
            vis = scientific_notation_svg(10 ** exp, is_large=False)
            
        else:  # compare
            m1, e1 = round(random.uniform(2, 5), 1), random.randint(-5, -3)
            m2, e2 = round(random.uniform(6, 9), 1), random.randint(-5, -3)
            n1 = m1 * (10 ** e1)
            n2 = m2 * (10 ** e2)
            txt = f"Which is larger: {m1} × 10^{e1} or {m2} × 10^{e2}?"
            if n1 > n2:
                ans = f"{m1} × 10^{e1}"
            else:
                ans = f"{m2} × 10^{e2}"
            wrongs = {f"{m1} × 10^{e1}", f"{m2} × 10^{e2}", "They are equal", "Cannot compare"}
            exp_text = f"Compare exponents first (larger = bigger), then mantissa if same exponent"
            vis = scientific_notation_svg(max(n1, n2), is_large=False)
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': vis
        })
    
    return qs


# Level 10: Calculations with Scientific Notation
def gen_level_10(n=50):
    """Mastery: Multiply and divide in scientific notation"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['multiply', 'divide', 'add_exp', 'real_world'])
        
        if qtype == 'multiply':
            m1 = random.randint(2, 5)
            m2 = random.randint(2, 4)
            e1 = random.randint(3, 6)
            e2 = random.randint(2, 5)
            result_m = m1 * m2
            result_e = e1 + e2
            # Adjust if mantissa >= 10
            if result_m >= 10:
                result_m = result_m / 10
                result_e += 1
            txt = f"Calculate: ({m1} × 10^{e1}) × ({m2} × 10^{e2})"
            ans = f"{result_m} × 10^{result_e}"
            wrongs = {f"{m1*m2} × 10^{e1*e2}", f"{m1+m2} × 10^{e1+e2}", 
                     f"{result_m} × 10^{result_e-1}", f"{result_m} × 10^{result_e+1}"}
            exp_text = f"Multiply mantissas: {m1}×{m2}={m1*m2}. Add exponents: {e1}+{e2}={e1+e2}. Answer: {result_m} × 10^{result_e}"
            
        elif qtype == 'divide':
            m1 = random.choice([4, 6, 8, 9])
            m2 = random.choice([2, 3])
            e1 = random.randint(6, 9)
            e2 = random.randint(2, 4)
            result_m = m1 / m2
            result_e = e1 - e2
            txt = f"Calculate: ({m1} × 10^{e1}) ÷ ({m2} × 10^{e2})"
            ans = f"{result_m:.0f} × 10^{result_e}" if result_m == int(result_m) else f"{result_m} × 10^{result_e}"
            wrongs = {f"{m1/m2:.1f} × 10^{e1+e2}", f"{m1*m2} × 10^{e1-e2}", 
                     f"{result_m:.0f} × 10^{result_e+1}", f"{result_m:.0f} × 10^{result_e-1}"}
            exp_text = f"Divide mantissas: {m1}÷{m2}={result_m:.0f}. Subtract exponents: {e1}-{e2}={result_e}"
            
        elif qtype == 'add_exp':
            m = random.randint(2, 5)
            e1 = random.randint(3, 6)
            e2 = random.randint(3, 6)
            txt = f"Simplify: 10^{e1} × 10^{e2}"
            ans = f"10^{e1+e2}"
            wrongs = {f"10^{e1*e2}", f"10^{e1-e2}", f"20^{e1+e2}", f"10^{e1}"}
            exp_text = f"Same base (10), add exponents: 10^{e1} × 10^{e2} = 10^{e1+e2}"
            
        else:  # real_world
            contexts = [
                ("The Earth is about 1.5 × 10^8 km from the Sun. Light travels at 3 × 10^5 km/s. Time for light to reach Earth?", 
                 "5 × 10^2 seconds", "Divide: (1.5 × 10^8) ÷ (3 × 10^5) = 0.5 × 10^3 = 5 × 10^2 s"),
                ("A cell is 2 × 10^(-5) m wide. How wide are 1000 cells in a row?",
                 "2 × 10^(-2) m", "Multiply: (2 × 10^(-5)) × (10^3) = 2 × 10^(-2) m"),
            ]
            ctx, answer, explanation = random.choice(contexts)
            txt = ctx
            ans = answer
            wrongs = {"5 × 10^3 seconds", "5 × 10^1 seconds", "2 × 10^(-2) m", "2 × 10^(-8) m", 
                     "1.5 × 10^3 seconds", "2 × 10^(-5) m"}
            exp_text = explanation
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': index_law_svg('multiply')
        })
    
    return qs


# Level 11: Mixed Index Problems
def gen_level_11(n=50):
    """Mastery: Combine multiple index laws"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['mult_div', 'power_mult', 'negative_frac', 'simplify_complex'])
        
        if qtype == 'mult_div':
            base = random.choice(['a', 'x', 'y'])
            e1, e2, e3 = random.randint(3, 6), random.randint(2, 4), random.randint(1, 3)
            result = e1 + e2 - e3
            txt = f"Simplify: {base}^{e1} × {base}^{e2} ÷ {base}^{e3}"
            ans = f"{base}^{result}"
            wrongs = {f"{base}^{e1+e2+e3}", f"{base}^{e1*e2-e3}", f"{base}^{e1-e2+e3}", f"{base}^{result+1}"}
            exp_text = f"Work left to right: {e1}+{e2}={e1+e2}, then {e1+e2}-{e3}={result}. Answer: {base}^{result}"
            
        elif qtype == 'power_mult':
            base = random.choice(['a', 'x', 'm'])
            e1, e2, e3 = random.randint(2, 3), random.randint(2, 3), random.randint(2, 4)
            result = e1 * e2 + e3
            txt = f"Simplify: ({base}^{e1})^{e2} × {base}^{e3}"
            ans = f"{base}^{result}"
            wrongs = {f"{base}^{e1+e2+e3}", f"{base}^{e1*e2*e3}", f"{base}^{e1*e2-e3}", f"{base}^{result-1}"}
            exp_text = f"Power of power: {e1}×{e2}={e1*e2}. Then add: {e1*e2}+{e3}={result}"
            
        elif qtype == 'negative_frac':
            base = random.randint(2, 4)
            txt = f"Calculate: {base}^(-2) × {base}^4"
            result_exp = -2 + 4
            result = base ** result_exp
            ans = str(result)
            wrongs = {str(base ** 6), str(base ** 2 * -1), f"1/{result}", str(result + base)}
            exp_text = f"Add exponents: -2 + 4 = 2. {base}^2 = {result}"
            
        else:  # simplify_complex
            base = random.choice(['x', 'y', 'a'])
            e1, e2 = random.randint(4, 8), random.randint(2, 4)
            txt = f"Simplify: ({base}^{e1}) / ({base}^{e2})^2"
            result = e1 - (e2 * 2)
            if result > 0:
                ans = f"{base}^{result}"
            elif result == 0:
                ans = "1"
            else:
                ans = f"1/{base}^{-result}"
            wrongs = {f"{base}^{e1-e2}", f"{base}^{e1+e2*2}", f"{base}^{e1*e2}", f"{base}^{abs(result)+1}"}
            exp_text = f"Bottom: ({base}^{e2})^2 = {base}^{e2*2}. Then {e1}-{e2*2}={result}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': index_law_svg('multiply')
        })
    
    return qs


# Level 12: Problem Solving & Applications
def gen_level_12(n=50):
    """Mastery: Real-world applications"""
    qs = []
    used = set()
    
    for _ in range(n * 30):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['population', 'computing', 'science', 'money', 'area', 'volume', 'decay'])
        
        if qtype == 'population':
            initial = random.choice([100, 500, 1000, 2000, 5000])
            doubles = random.randint(2, 5)
            final = initial * (2 ** doubles)
            txt = f"A bacteria population of {initial:,} doubles {doubles} times. What is the final population?"
            ans = f"{final:,}"
            wrongs = {f"{initial * doubles:,}", f"{initial * 2 * doubles:,}", 
                     f"{final + initial:,}", f"{final // 2:,}"}
            exp_text = f"{initial} × 2^{doubles} = {initial} × {2**doubles} = {final:,}"
            
        elif qtype == 'computing':
            power = random.randint(6, 14)
            value = 2 ** power
            unit = random.choice(['bytes', 'bits', 'KB'])
            txt = f"A device has 2^{power} {unit} of memory. How many {unit} is this?"
            ans = f"{value:,}"
            wrongs = {f"{2 * power:,}", f"{value // 2:,}", f"{value * 2:,}", f"{power ** 2:,}"}
            exp_text = f"2^{power} = {value:,} {unit}"
            
        elif qtype == 'science':
            mantissa = random.choice([1, 2, 3, 5, 6, 7, 8, 9])
            exp = random.randint(6, 12)
            txt = f"A distance is {mantissa} × 10^{exp} metres. How many zeros follow the {mantissa} in standard form?"
            ans = str(exp)
            wrongs = {str(exp - 1), str(exp + 1), str(mantissa), str(exp * 2)}
            exp_text = f"The exponent tells us the number of zeros: 10^{exp} has {exp} zeros"
            
        elif qtype == 'money':
            principal = random.choice([100, 200, 500, 1000])
            rate = 2  # Doubling
            years = random.randint(1, 5)
            final = principal * (rate ** years)
            txt = f"€{principal} doubles every year. After {years} years, how much will there be?"
            ans = f"€{final:,}"
            wrongs = {f"€{principal * 2 * years:,}", f"€{principal + (principal * years):,}", 
                     f"€{final // 2:,}", f"€{final + principal:,}"}
            exp_text = f"€{principal} × 2^{years} = €{principal} × {2**years} = €{final:,}"
            
        elif qtype == 'area':
            side = random.randint(2, 12)
            area = side ** 2
            txt = f"A square has side length {side} cm. What is its area?"
            ans = f"{area} cm²"
            wrongs = {f"{side * 4} cm²", f"{side * 2} cm²", f"{area + side} cm²", f"{side} cm²"}
            exp_text = f"Area = side² = {side}² = {area} cm²"
            
        elif qtype == 'volume':
            side = random.randint(2, 6)
            volume = side ** 3
            txt = f"A cube has side length {side} cm. What is its volume?"
            ans = f"{volume} cm³"
            wrongs = {f"{side * 6} cm³", f"{side ** 2} cm³", f"{side * 3} cm³", f"{volume + side} cm³"}
            exp_text = f"Volume = side³ = {side}³ = {volume} cm³"
            
        else:  # decay
            initial = random.choice([64, 128, 256, 512, 1024])
            halves = random.randint(2, 4)
            final = initial // (2 ** halves)
            txt = f"A substance starts at {initial}g and halves {halves} times. What mass remains?"
            ans = f"{final}g"
            wrongs = {f"{initial // halves}g", f"{initial - halves * 2}g", 
                     f"{final * 2}g", f"{final // 2}g"}
            exp_text = f"{initial} ÷ 2^{halves} = {initial} ÷ {2**halves} = {final}g"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp_text,
            'image_svg': index_law_svg('power')
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
    print("AgentMath - Indices & Scientific Notation Generator v1")
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
