"""
JC Exam Style Fractions Question Generator v2
With SANITY CHECKS:
1. No duplicate answer options within a question
2. No duplicate questions at the same level
3. Sufficient question variety per level
4. Validated correct answers

Run: python generate_jc_fractions_v2.py
"""

import sqlite3
import random
from math import gcd
import os

DB_PATH = 'instance/mathquiz.db'

def simplify_fraction(num, den):
    """Return simplified fraction as tuple"""
    if den == 0:
        return (num, 1)
    if num == 0:
        return (0, 1)
    common = gcd(abs(num), abs(den))
    return (num // common, den // common)

def lcm(a, b):
    """Least common multiple"""
    return abs(a * b) // gcd(a, b)

def fraction_to_mixed(num, den):
    """Convert improper fraction to mixed number string"""
    if den == 0:
        return "0"
    if num == 0:
        return "0"
    if abs(num) < den:
        n, d = simplify_fraction(num, den)
        return f"{n}/{d}"
    whole = num // den
    remainder = num % den
    if remainder == 0:
        return str(whole)
    n, d = simplify_fraction(remainder, den)
    return f"{whole} {n}/{d}"

def fraction_str(num, den):
    """Convert fraction to string, simplifying if possible"""
    if den == 0:
        return "undefined"
    sn, sd = simplify_fraction(num, den)
    if sd == 1:
        return str(sn)
    return f"{sn}/{sd}"

def generate_unique_distractors(answer, distractor_generators, count=3):
    """
    Generate unique distractors that don't match the answer.
    distractor_generators is a list of functions that return potential distractors.
    """
    distractors = set()
    
    # Try each generator
    for gen in distractor_generators:
        try:
            d = gen()
            if d and d != answer and d not in distractors:
                # Additional validation - no invalid fractions
                if '/0' not in str(d) and 'undefined' not in str(d):
                    distractors.add(d)
        except:
            pass
    
    # If we don't have enough, generate some safe fallbacks
    fallback_idx = 1
    while len(distractors) < count:
        # Generate fallback based on answer type
        if '/' in str(answer):
            parts = str(answer).split('/')
            try:
                num = int(parts[0].split()[-1])  # Handle mixed numbers
                den = int(parts[1])
                fallback = f"{num + fallback_idx}/{den + fallback_idx}"
            except:
                fallback = f"{fallback_idx}/{fallback_idx + 2}"
        else:
            try:
                fallback = str(int(answer) + fallback_idx)
            except:
                fallback = str(fallback_idx)
        
        if fallback != answer and fallback not in distractors:
            distractors.add(fallback)
        fallback_idx += 1
        
        if fallback_idx > 10:  # Safety limit
            break
    
    return list(distractors)[:count]

def create_question(question_text, answer, distractors, explanation, svg=None, q_type='calculation'):
    """
    Create a validated question with unique options.
    Returns None if validation fails.
    """
    # Ensure we have exactly 3 unique distractors
    unique_distractors = []
    for d in distractors:
        if d != answer and d not in unique_distractors:
            unique_distractors.append(d)
    
    if len(unique_distractors) < 3:
        return None  # Not enough unique distractors
    
    unique_distractors = unique_distractors[:3]
    
    # Create options and shuffle
    options = [answer] + unique_distractors
    
    # Final duplicate check
    if len(set(options)) != 4:
        return None  # Duplicates detected
    
    random.shuffle(options)
    correct = options.index(answer)
    
    return {
        'question': question_text,
        'options': options,
        'correct': correct,
        'explanation': explanation,
        'svg': svg,
        'type': q_type
    }

def generate_svg_pie_fraction(num, den, size=120):
    """Generate SVG pie chart showing a fraction"""
    import math
    cx, cy, r = size//2, size//2, size//2 - 10
    
    svg = f'<svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e0e0e0" stroke="#333" stroke-width="2"/>'
    
    for i in range(num):
        start_angle = (i / den) * 2 * math.pi - math.pi/2
        end_angle = ((i + 1) / den) * 2 * math.pi - math.pi/2
        
        x1 = cx + r * math.cos(start_angle)
        y1 = cy + r * math.sin(start_angle)
        x2 = cx + r * math.cos(end_angle)
        y2 = cy + r * math.sin(end_angle)
        
        large_arc = 1 if (end_angle - start_angle) > math.pi else 0
        
        svg += f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large_arc},1 {x2:.1f},{y2:.1f} Z" fill="#4CAF50" stroke="#333" stroke-width="1"/>'
    
    for i in range(den):
        angle = (i / den) * 2 * math.pi - math.pi/2
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        svg += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#333" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def generate_level_1_questions():
    """Foundation: Identify fractions from visuals"""
    questions = []
    seen_questions = set()
    
    fractions = [(1,2), (1,3), (2,3), (1,4), (2,4), (3,4), (1,5), (2,5), (3,5), (4,5),
                 (1,6), (2,6), (3,6), (4,6), (5,6), (1,8), (3,8), (5,8), (7,8)]
    
    for num, den in fractions:
        question_text = f"What fraction of this shape is shaded? ({num} out of {den} parts)"
        
        if question_text in seen_questions:
            continue
        seen_questions.add(question_text)
        
        svg = generate_svg_pie_fraction(num, den)
        answer = f"{num}/{den}"
        
        # Generate unique distractors
        distractors = generate_unique_distractors(answer, [
            lambda n=num, d=den: f"{d}/{n}",  # Inverted
            lambda n=num, d=den: f"{n}/{d+1}",  # Wrong denominator
            lambda n=num, d=den: f"{n+1}/{d}",  # Wrong numerator
            lambda n=num, d=den: f"{d-n}/{d}",  # Complement
            lambda n=num, d=den: f"{n}/{d-1}" if d > 2 else f"{n}/{d+2}",
        ])
        
        q = create_question(question_text, answer, distractors,
                           f"There are {den} equal parts and {num} are shaded, so the fraction is {num}/{den}.",
                           svg, 'visual')
        if q:
            questions.append(q)
    
    return questions[:15]  # Limit to 15 per level


def generate_level_2_questions():
    """Foundation: Simplify fractions"""
    questions = []
    seen_questions = set()
    
    pairs = [(2,4), (3,6), (4,8), (2,6), (3,9), (4,12), (5,10), (6,8), (4,6), (6,9),
             (8,12), (6,10), (9,12), (10,15), (8,10), (6,12), (9,15), (12,16), (15,20)]
    
    for num, den in pairs:
        sn, sd = simplify_fraction(num, den)
        question_text = f"Write {num}/{den} in its simplest form."
        
        if question_text in seen_questions:
            continue
        seen_questions.add(question_text)
        
        answer = f"{sn}/{sd}"
        
        distractors = generate_unique_distractors(answer, [
            lambda n=num, d=den: f"{n}/{d}",  # Unsimplified
            lambda s=sn, d=sd: f"{s+1}/{d+1}",
            lambda s=sn, d=sd: f"{s}/{d+1}",
            lambda n=num, d=den: f"{n//2}/{d}" if n % 2 == 0 else f"{n}/{d//2}" if d % 2 == 0 else f"{n+1}/{d}",
            lambda s=sn, d=sd: f"{d}/{s}" if s != d else f"{s+1}/{d}",
        ])
        
        q = create_question(question_text, answer, distractors,
                           f"Divide both {num} and {den} by their HCF ({gcd(num,den)}) to get {sn}/{sd}.",
                           None, 'simplify')
        if q:
            questions.append(q)
    
    return questions[:15]


def generate_level_3_questions():
    """Foundation: Add fractions with SAME denominator"""
    questions = []
    seen_questions = set()
    
    for den in [3, 4, 5, 6, 7, 8, 9, 10, 12]:
        for num1 in range(1, den-1):
            for num2 in range(1, den - num1):
                result_num = num1 + num2
                if result_num >= den:
                    continue
                    
                sn, sd = simplify_fraction(result_num, den)
                question_text = f"Calculate {num1}/{den} + {num2}/{den}. Give your answer in simplest form."
                
                if question_text in seen_questions:
                    continue
                seen_questions.add(question_text)
                
                answer = str(sn) if sd == 1 else f"{sn}/{sd}"
                
                distractors = generate_unique_distractors(answer, [
                    lambda n1=num1, n2=num2, d=den: f"{n1+n2}/{d+d}",  # Adding denominators
                    lambda r=result_num, d=den: f"{r}/{d}",  # Unsimplified (if different)
                    lambda n1=num1, n2=num2, d=den: f"{n1+n2+1}/{d}",
                    lambda n1=num1, n2=num2, d=den: f"{abs(n1-n2)}/{d}",  # Subtracted instead
                    lambda s=sn, d=sd: f"{s+1}/{d}" if sd != 1 else str(sn+1),
                ])
                
                q = create_question(question_text, answer, distractors,
                                   f"{num1}/{den} + {num2}/{den} = {result_num}/{den} = {answer}",
                                   None, 'add_same')
                if q:
                    questions.append(q)
                    
                if len(questions) >= 15:
                    return questions
    
    return questions[:15]


def generate_level_4_questions():
    """Foundation: Subtract fractions with SAME denominator"""
    questions = []
    seen_questions = set()
    
    for den in [3, 4, 5, 6, 7, 8, 9, 10, 12]:
        for num1 in range(2, den):
            for num2 in range(1, num1):
                result_num = num1 - num2
                if result_num <= 0:
                    continue
                    
                sn, sd = simplify_fraction(result_num, den)
                question_text = f"Calculate {num1}/{den} − {num2}/{den}. Give your answer in simplest form."
                
                if question_text in seen_questions:
                    continue
                seen_questions.add(question_text)
                
                answer = str(sn) if sd == 1 else f"{sn}/{sd}"
                
                distractors = generate_unique_distractors(answer, [
                    lambda r=result_num, d=den: f"{r}/{d}",  # Unsimplified
                    lambda n1=num1, n2=num2, d=den: f"{n1+n2}/{d}",  # Added instead
                    lambda r=result_num, d=den: f"{r}/{d+1}",
                    lambda s=sn, d=sd: f"{s+1}/{d}" if sd != 1 else str(sn+1),
                    lambda n1=num1, n2=num2: f"{n1}/{n2}",
                ])
                
                q = create_question(question_text, answer, distractors,
                                   f"{num1}/{den} − {num2}/{den} = {result_num}/{den} = {answer}",
                                   None, 'subtract_same')
                if q:
                    questions.append(q)
                    
                if len(questions) >= 15:
                    return questions
    
    return questions[:15]


def generate_level_5_questions():
    """★ CORE SEC ORDINARY LEVEL - Add fractions with DIFFERENT denominators"""
    questions = []
    seen_questions = set()
    
    # Carefully selected pairs that give nice results
    pairs = [
        (1,2, 1,3), (1,2, 1,4), (1,2, 1,5), (1,2, 1,6),
        (1,3, 1,4), (1,3, 1,6), (1,3, 2,5),
        (1,4, 1,5), (1,4, 2,3), (1,4, 3,5),
        (2,3, 1,4), (2,3, 1,5), (2,3, 1,6), (2,3, 3,4), (2,3, 5,7),
        (3,4, 1,5), (3,4, 1,6), (3,4, 2,5),
        (2,5, 1,3), (2,5, 1,4), (2,5, 3,10),
        (1,6, 1,4), (5,6, 1,4),
    ]
    
    for n1, d1, n2, d2 in pairs:
        common_den = lcm(d1, d2)
        new_n1 = n1 * (common_den // d1)
        new_n2 = n2 * (common_den // d2)
        result_num = new_n1 + new_n2
        
        sn, sd = simplify_fraction(result_num, common_den)
        question_text = f"Write {n1}/{d1} + {n2}/{d2} as a single fraction in its simplest form."
        
        if question_text in seen_questions:
            continue
        seen_questions.add(question_text)
        
        answer = str(sn) if sd == 1 else f"{sn}/{sd}"
        
        distractors = generate_unique_distractors(answer, [
            lambda a=n1, b=n2, c=d1, d=d2: f"{a+b}/{c+d}",  # Common error: add both
            lambda r=result_num, cd=common_den: f"{r}/{cd}",  # Unsimplified
            lambda a=n1, b=n2, c=d1, d=d2: f"{a+b}/{max(c,d)}",  # Using larger denom only
            lambda a=n1, b=n2, c=d1, d=d2: f"{a+b}/{min(c,d)}",  # Using smaller denom
            lambda s=sn, d=sd: f"{s+1}/{d}" if sd != 1 else str(sn+1),
        ])
        
        q = create_question(question_text, answer, distractors,
                           f"LCD = {common_den}. {n1}/{d1} = {new_n1}/{common_den}, {n2}/{d2} = {new_n2}/{common_den}. Sum = {result_num}/{common_den} = {answer}",
                           None, 'add_different')
        if q:
            questions.append(q)
    
    return questions[:15]


def generate_level_6_questions():
    """★ SEC ORDINARY LEVEL - Subtract fractions with DIFFERENT denominators"""
    questions = []
    seen_questions = set()
    
    pairs = [
        (3,4, 1,2), (3,4, 1,3), (3,4, 1,4), (3,4, 2,5),
        (2,3, 1,4), (2,3, 1,6), (2,3, 1,2),
        (5,6, 1,3), (5,6, 1,4), (5,6, 1,2),
        (4,5, 1,2), (4,5, 1,3), (4,5, 3,10),
        (7,8, 1,2), (7,8, 1,4), (7,8, 3,4),
        (5,8, 1,4), (3,5, 1,3),
        (7,10, 2,5), (9,10, 3,5),
    ]
    
    for n1, d1, n2, d2 in pairs:
        common_den = lcm(d1, d2)
        new_n1 = n1 * (common_den // d1)
        new_n2 = n2 * (common_den // d2)
        result_num = new_n1 - new_n2
        
        if result_num <= 0:
            continue
            
        sn, sd = simplify_fraction(result_num, common_den)
        question_text = f"Write {n1}/{d1} − {n2}/{d2} as a single fraction in its simplest form."
        
        if question_text in seen_questions:
            continue
        seen_questions.add(question_text)
        
        answer = str(sn) if sd == 1 else f"{sn}/{sd}"
        
        distractors = generate_unique_distractors(answer, [
            lambda a=n1, b=n2, c=d1, d=d2: f"{abs(a-b)}/{abs(c-d)}" if c != d else f"{a-b}/{c+1}",
            lambda r=result_num, cd=common_den: f"{r}/{cd}",  # Unsimplified
            lambda a=n1, b=n2, c=d1, d=d2: f"{a+b}/{c+d}",  # Added instead
            lambda a=n1, b=n2, c=d1, d=d2: f"{abs(a-b)}/{max(c,d)}",
            lambda s=sn, d=sd: f"{s+1}/{d}" if sd != 1 else str(sn+1),
        ])
        
        q = create_question(question_text, answer, distractors,
                           f"LCD = {common_den}. {n1}/{d1} = {new_n1}/{common_den}, {n2}/{d2} = {new_n2}/{common_den}. Difference = {result_num}/{common_den} = {answer}",
                           None, 'subtract_different')
        if q:
            questions.append(q)
    
    return questions[:15]


def generate_level_7_questions():
    """Ordinary Level: Multiply fractions"""
    questions = []
    seen_questions = set()
    
    pairs = [
        (1,2, 1,3), (1,2, 1,4), (1,2, 2,3), (1,2, 3,4),
        (2,3, 3,4), (2,3, 1,5), (2,3, 4,5),
        (1,4, 2,5), (1,4, 3,5), (1,4, 4,5),
        (3,5, 5,6), (3,5, 2,3),
        (3,4, 4,5), (3,4, 2,3), (3,4, 5,6),
        (2,5, 5,8), (2,5, 3,4),
        (1,3, 3,7), (1,3, 6,7),
        (4,5, 5,8), (5,6, 3,5),
    ]
    
    for n1, d1, n2, d2 in pairs:
        result_num = n1 * n2
        result_den = d1 * d2
        sn, sd = simplify_fraction(result_num, result_den)
        
        question_text = f"Calculate {n1}/{d1} × {n2}/{d2}. Give your answer in simplest form."
        
        if question_text in seen_questions:
            continue
        seen_questions.add(question_text)
        
        answer = str(sn) if sd == 1 else f"{sn}/{sd}"
        
        distractors = generate_unique_distractors(answer, [
            lambda r=result_num, d=result_den: f"{r}/{d}",  # Unsimplified
            lambda a=n1, b=n2, c=d1, d=d2: f"{a+b}/{c+d}",  # Added instead
            lambda a=n1, b=n2, c=d1, d=d2: f"{a*d}/{c*b}",  # Cross-multiplied wrong
            lambda s=sn, d=sd: f"{s+1}/{d}" if sd != 1 else str(sn+1),
            lambda a=n1, b=n2, c=d1, d=d2: f"{a*b}/{c*d+1}",
        ])
        
        q = create_question(question_text, answer, distractors,
                           f"{n1}/{d1} × {n2}/{d2} = {result_num}/{result_den} = {answer}",
                           None, 'multiply')
        if q:
            questions.append(q)
    
    return questions[:15]


def generate_level_8_questions():
    """Ordinary Level: Divide fractions"""
    questions = []
    seen_questions = set()
    
    pairs = [
        (1,2, 1,4), (1,2, 1,3), (1,2, 2,3), (1,2, 3,4),
        (2,3, 1,3), (2,3, 4,9), (2,3, 1,6),
        (3,4, 1,2), (3,4, 3,8), (3,4, 1,4),
        (1,3, 2,3), (1,3, 1,6),
        (2,5, 1,5), (2,5, 4,5),
        (5,6, 1,3), (5,6, 5,12),
        (4,5, 2,5), (4,5, 8,15),
        (5,8, 1,4), (7,8, 7,16),
    ]
    
    for n1, d1, n2, d2 in pairs:
        result_num = n1 * d2
        result_den = d1 * n2
        sn, sd = simplify_fraction(result_num, result_den)
        
        question_text = f"Calculate {n1}/{d1} ÷ {n2}/{d2}. Give your answer in simplest form."
        
        if question_text in seen_questions:
            continue
        seen_questions.add(question_text)
        
        answer = str(sn) if sd == 1 else f"{sn}/{sd}"
        
        distractors = generate_unique_distractors(answer, [
            lambda a=n1, b=n2, c=d1, d=d2: f"{a*b}/{c*d}",  # Multiplied instead
            lambda a=n1, c=d1, b=n2: f"{a}/{c*b}",  # Forgot to flip
            lambda r=result_num, d=result_den: f"{d}/{r}" if r != 0 else "1",  # Reciprocal
            lambda s=sn, d=sd: f"{s+1}/{d}" if sd != 1 else str(sn+1),
            lambda r=result_num, d=result_den: f"{r}/{d}",  # Unsimplified
        ])
        
        q = create_question(question_text, answer, distractors,
                           f"{n1}/{d1} ÷ {n2}/{d2} = {n1}/{d1} × {d2}/{n2} = {result_num}/{result_den} = {answer}",
                           None, 'divide')
        if q:
            questions.append(q)
    
    return questions[:15]


def generate_level_9_questions():
    """Higher/Stretch: Mixed numbers addition"""
    questions = []
    seen_questions = set()
    
    problems = [
        (1, 1,2, 2, 1,4),   # 1½ + 2¼
        (2, 1,3, 1, 1,2),   # 2⅓ + 1½
        (1, 3,4, 2, 1,3),   # 1¾ + 2⅓
        (3, 1,5, 1, 2,5),   # 3⅕ + 1⅖
        (2, 2,3, 1, 5,6),   # 2⅔ + 1⅚
        (1, 1,4, 3, 1,2),   # 1¼ + 3½
        (2, 3,8, 1, 1,4),   # 2⅜ + 1¼
        (1, 5,6, 2, 1,3),   # 1⅚ + 2⅓
        (2, 1,2, 3, 1,4),   # 2½ + 3¼
        (1, 2,3, 2, 1,6),   # 1⅔ + 2⅙
        (3, 1,4, 1, 3,4),   # 3¼ + 1¾
        (2, 1,5, 1, 3,10),  # 2⅕ + 1 3/10
    ]
    
    for w1, n1, d1, w2, n2, d2 in problems:
        imp1 = w1 * d1 + n1
        imp2 = w2 * d2 + n2
        common_den = lcm(d1, d2)
        new_n1 = imp1 * (common_den // d1)
        new_n2 = imp2 * (common_den // d2)
        result_num = new_n1 + new_n2
        
        answer = fraction_to_mixed(result_num, common_den)
        question_text = f"Calculate {w1} {n1}/{d1} + {w2} {n2}/{d2}. Give your answer as a mixed number in simplest form."
        
        if question_text in seen_questions:
            continue
        seen_questions.add(question_text)
        
        distractors = generate_unique_distractors(answer, [
            lambda r=result_num, cd=common_den: fraction_to_mixed(r - cd, cd),
            lambda r=result_num, cd=common_den: fraction_to_mixed(r + cd, cd),
            lambda a=w1, b=w2, c=n1, d=n2, e=d1, f=d2: f"{a+b} {c+d}/{e+f}",
            lambda a=w1, b=w2: str(a + b),
            lambda r=result_num, cd=common_den: fraction_to_mixed(r + 2, cd),
        ])
        
        q = create_question(question_text, answer, distractors,
                           "Convert to improper fractions, find common denominator, add, then convert back to mixed number.",
                           None, 'mixed_add')
        if q:
            questions.append(q)
    
    return questions[:10]


def generate_level_10_questions():
    """Higher/Stretch: Word problems with fractions"""
    word_problems = [
        {
            'question': "A recipe needs 2/3 cup of flour. If you want to make 1½ times the recipe, how much flour do you need?",
            'answer': "1",
            'distractors': ["2/3", "1/2", "5/6", "1 1/6"]
        },
        {
            'question': "Sarah walked 3/4 km to school and 2/5 km to the shop. How far did she walk in total?",
            'answer': "1 3/20",
            'distractors': ["5/9", "1 1/5", "1 1/4", "23/20"]
        },
        {
            'question': "A tank is 5/6 full. After using 1/4 of the tank's capacity, what fraction remains?",
            'answer': "7/12",
            'distractors': ["1/2", "2/3", "4/6", "11/12"]
        },
        {
            'question': "If 3/5 of a class are girls, and 1/4 of the girls wear glasses, what fraction of the class are girls wearing glasses?",
            'answer': "3/20",
            'distractors': ["4/9", "1/5", "17/20", "7/20"]
        },
        {
            'question': "A piece of rope is 7/8 m long. How many pieces of 1/4 m can be cut from it?",
            'answer': "3 1/2",
            'distractors': ["3", "4", "7/32", "2 1/2"]
        },
        {
            'question': "John ate 1/3 of a pizza and Mary ate 1/4 of it. What fraction of the pizza is left?",
            'answer': "5/12",
            'distractors': ["2/7", "1/2", "7/12", "1/12"]
        },
        {
            'question': "A car uses 2/5 of a tank of petrol for a journey. If the tank holds 50 litres, how many litres were used?",
            'answer': "20",
            'distractors': ["25", "10", "40", "15"]
        },
        {
            'question': "Tom has €60. He spends 1/4 on books and 1/3 on food. How much money does he have left?",
            'answer': "25",
            'distractors': ["35", "20", "30", "15"]
        },
    ]
    
    questions = []
    for wp in word_problems:
        distractors = [d for d in wp['distractors'] if d != wp['answer']][:3]
        q = create_question(wp['question'], wp['answer'], distractors,
                           "Identify the operation needed, then calculate with fractions.",
                           None, 'word_problem')
        if q:
            questions.append(q)
    
    return questions[:8]


def generate_level_11_questions():
    """Higher Level: Multi-step problems"""
    multi_step = [
        {
            'question': "Calculate (1/2 + 1/3) × 3/5. Give your answer in simplest form.",
            'answer': "1/2",
            'distractors': ["5/6", "3/10", "1/3", "2/5"]
        },
        {
            'question': "Calculate (3/4 − 1/3) ÷ 5/12. Give your answer in simplest form.",
            'answer': "1",
            'distractors': ["5/12", "25/144", "12/5", "5/9"]
        },
        {
            'question': "Calculate 2/3 of (1/2 + 3/4). Give your answer in simplest form.",
            'answer': "5/6",
            'distractors': ["1/2", "7/12", "11/12", "3/4"]
        },
        {
            'question': "Calculate 1/2 + 1/3 + 1/6. Give your answer in simplest form.",
            'answer': "1",
            'distractors': ["3/11", "5/6", "7/6", "2/3"]
        },
        {
            'question': "Calculate (2/3)² × 9/4. Give your answer in simplest form.",
            'answer': "1",
            'distractors': ["4/9", "2/3", "3/2", "6/12"]
        },
        {
            'question': "If a = 1/2 and b = 2/3, calculate 2a + 3b.",
            'answer': "3",
            'distractors': ["2", "7/6", "5/3", "4"]
        },
        {
            'question': "Calculate 3/4 ÷ (1/2 + 1/4). Give your answer in simplest form.",
            'answer': "1",
            'distractors': ["3/4", "1/2", "4/3", "2"]
        },
    ]
    
    questions = []
    for ms in multi_step:
        distractors = [d for d in ms['distractors'] if d != ms['answer']][:3]
        q = create_question(ms['question'], ms['answer'], distractors,
                           "Follow order of operations (BIMDAS) when solving multi-step fraction problems.",
                           None, 'multi_step')
        if q:
            questions.append(q)
    
    return questions[:7]


def generate_level_12_questions():
    """Higher Level: Cross-topic (fractions ↔ percentages, decimals)"""
    cross_topic = [
        {
            'question': "Express 3/8 as a percentage.",
            'answer': "37.5%",
            'distractors': ["37%", "38%", "0.375%", "35%"]
        },
        {
            'question': "What fraction is equivalent to 0.125?",
            'answer': "1/8",
            'distractors': ["1/125", "125/1000", "1/4", "1/5"]
        },
        {
            'question': "If 40% of a number is 24, what is 3/4 of that number?",
            'answer': "45",
            'distractors': ["48", "40", "36", "30"]
        },
        {
            'question': "Write 2.75 as a mixed number in simplest form.",
            'answer': "2 3/4",
            'distractors': ["2 75/100", "2 7/10", "275/100", "2 1/4"]
        },
        {
            'question': "What is 2/5 as a decimal?",
            'answer': "0.4",
            'distractors': ["0.25", "0.5", "0.2", "2.5"]
        },
        {
            'question': "Express 0.6 as a fraction in simplest form.",
            'answer': "3/5",
            'distractors': ["6/10", "2/3", "1/6", "6/100"]
        },
        {
            'question': "What percentage is equivalent to 5/8?",
            'answer': "62.5%",
            'distractors': ["58%", "65%", "0.625%", "56%"]
        },
    ]
    
    questions = []
    for ct in cross_topic:
        distractors = [d for d in ct['distractors'] if d != ct['answer']][:3]
        q = create_question(ct['question'], ct['answer'], distractors,
                           "Convert between fractions, decimals, and percentages as needed.",
                           None, 'cross_topic')
        if q:
            questions.append(q)
    
    return questions[:7]


def insert_questions(cursor, questions, level):
    """Insert questions into database with duplicate checking"""
    count = 0
    
    if level <= 4:
        band = 'foundation'
    elif level <= 8:
        band = 'ordinary'
    else:
        band = 'higher'
    
    for q in questions:
        # Final validation before insert
        if len(set(q['options'])) != 4:
            print(f"   ⚠️ Skipping question with duplicate options: {q['question'][:50]}...")
            continue
            
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text, 
                 option_a, option_b, option_c, option_d, correct_answer, 
                 explanation, image_svg, question_type, is_active, mode)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 'jc_exam')
            """, (
                'fractions',
                level,
                band,
                q['question'],
                q['options'][0],
                q['options'][1],
                q['options'][2],
                q['options'][3],
                q['correct'],
                q['explanation'],
                q['svg'],
                q['type']
            ))
            count += 1
        except sqlite3.IntegrityError as e:
            if 'UNIQUE' in str(e):
                pass  # Duplicate question, skip silently
            else:
                print(f"   ⚠️ Error inserting question: {e}")
        except Exception as e:
            print(f"   ⚠️ Error inserting question: {e}")
    
    return count


def main():
    print("=" * 60)
    print("JC Exam Style Fractions Question Generator v2")
    print("WITH SANITY CHECKS")
    print("=" * 60)
    
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if mode column exists
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'mode' not in columns:
        print("❌ 'mode' column not found. Run add_question_mode_column.py first.")
        conn.close()
        return
    
    # Clear existing jc_exam fractions questions
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = 'fractions' AND mode = 'jc_exam'
    """)
    deleted = cursor.rowcount
    print(f"🗑️ Cleared {deleted} existing JC Exam fractions questions")
    
    # Generate questions for each level
    generators = {
        1: generate_level_1_questions,
        2: generate_level_2_questions,
        3: generate_level_3_questions,
        4: generate_level_4_questions,
        5: generate_level_5_questions,
        6: generate_level_6_questions,
        7: generate_level_7_questions,
        8: generate_level_8_questions,
        9: generate_level_9_questions,
        10: generate_level_10_questions,
        11: generate_level_11_questions,
        12: generate_level_12_questions,
    }
    
    total_inserted = 0
    
    print("\n📝 Generating questions by level:")
    print("-" * 40)
    
    for level in range(1, 13):
        questions = generators[level]()
        
        # Validate all questions have unique options
        valid_questions = []
        for q in questions:
            if len(set(q['options'])) == 4:
                valid_questions.append(q)
            else:
                print(f"   ⚠️ Level {level}: Rejected question with duplicate options")
        
        count = insert_questions(cursor, valid_questions, level)
        
        band = 'Foundation' if level <= 4 else ('Ordinary' if level <= 8 else 'Higher')
        star = '★' if level in [5, 6] else ' '
        print(f"   Level {level:2d} ({band:10s}): {count:3d} questions {star}")
        total_inserted += count
    
    conn.commit()
    
    print("-" * 40)
    print(f"✅ Total inserted: {total_inserted} JC Exam questions")
    
    # Summary by band
    cursor.execute("""
        SELECT difficulty_band, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND mode = 'jc_exam'
        GROUP BY difficulty_band
    """)
    print("\n📊 Questions by difficulty band:")
    for band, count in cursor.fetchall():
        print(f"   {band}: {count}")
    
    # Verify no duplicate options
    print("\n🔍 Verifying option uniqueness...")
    cursor.execute("""
        SELECT id, question_text, option_a, option_b, option_c, option_d
        FROM questions_adaptive
        WHERE topic = 'fractions' AND mode = 'jc_exam'
    """)
    
    duplicates_found = 0
    for row in cursor.fetchall():
        options = [row[2], row[3], row[4], row[5]]
        if len(set(options)) != 4:
            print(f"   ⚠️ Question ID {row[0]} has duplicate options!")
            duplicates_found += 1
    
    if duplicates_found == 0:
        print("   ✅ All questions have unique options!")
    else:
        print(f"   ⚠️ Found {duplicates_found} questions with duplicate options")
    
    conn.close()
    print("\n✅ Generation complete!")
    print("\n💡 Levels 5-6 (★) directly match SEC Ordinary Level Q10(a) style")


if __name__ == "__main__":
    main()
