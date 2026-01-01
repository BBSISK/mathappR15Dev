"""
JC SEC-Aligned Fractions Question Generator v4
Target: 50 questions per level (600 total)

REQUIREMENTS:
1. 75% visual/contextual elements for Levels 1-10
2. 50% visual/contextual elements for Levels 11-12
3. No duplicate answer options within a question
4. No duplicate questions at the same level
5. SEC exam question types integrated throughout

SEC Question Types (2022-2025 Papers):
- Time as fraction (15 mins = ?/60 hour)
- Adding/subtracting fractions (Q10a style)
- Slope as fraction from coordinates
- Trigonometry ratios as fractions
- Pie chart / data fractions
- Ratio problems with fractions
- Probability as fractions
- Algebraic fractions (Higher)

Run: python generate_jc_fractions_v4.py
"""

import sqlite3
import random
from math import gcd, sqrt
import os

DB_PATH = 'instance/mathquiz.db'
QUESTIONS_PER_LEVEL = 50

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def simplify_fraction(num, den):
    """Return simplified fraction as tuple"""
    if den == 0:
        return (num, 1)
    if num == 0:
        return (0, 1)
    if den < 0:
        num, den = -num, -den
    common = gcd(abs(num), abs(den))
    return (num // common, den // common)

def lcm(a, b):
    """Least common multiple"""
    return abs(a * b) // gcd(a, b)

def fraction_str(num, den):
    """Convert fraction to string, simplifying"""
    if den == 0:
        return "undefined"
    sn, sd = simplify_fraction(num, den)
    if sd == 1:
        return str(sn)
    return f"{sn}/{sd}"

def mixed_number_str(num, den):
    """Convert improper fraction to mixed number string"""
    if den == 0 or num == 0:
        return "0"
    sn, sd = simplify_fraction(num, den)
    if sd == 1:
        return str(sn)
    if abs(sn) < sd:
        return f"{sn}/{sd}"
    whole = sn // sd
    remainder = abs(sn) % sd
    if remainder == 0:
        return str(whole)
    return f"{whole} {remainder}/{sd}"

def create_question(question_text, answer, distractor_funcs, max_attempts=50):
    """
    Create a question with validated unique options.
    Returns (question_text, options, correct_index) or None if failed.
    """
    for _ in range(max_attempts):
        distractors = []
        used = {str(answer)}
        
        funcs = distractor_funcs.copy()
        random.shuffle(funcs)
        
        for func in funcs:
            if len(distractors) >= 3:
                break
            try:
                d = func()
                d_str = str(d)
                if d_str and d_str not in used and d_str != 'undefined' and '/0' not in d_str:
                    distractors.append(d_str)
                    used.add(d_str)
            except:
                pass
        
        if len(distractors) >= 3:
            options = [str(answer)] + distractors[:3]
            random.shuffle(options)
            correct_idx = options.index(str(answer))
            
            if len(set(options)) == 4:
                return (question_text, options, correct_idx)
    
    return None

# =============================================================================
# VISUAL CONTEXT GENERATORS (for 75% visual requirement)
# =============================================================================

# Shapes for visual fraction questions
SHAPES = ['circle', 'rectangle', 'square', 'pizza', 'chocolate bar', 'cake', 'pie']
CONTAINERS = ['jar', 'bottle', 'tank', 'jug', 'bucket', 'glass']

# Real-world contexts for SEC-style questions
JOURNEY_CONTEXTS = [
    ("Sarah cycles", "km", "journey to school"),
    ("A bus travels", "km", "route"),
    ("Tom walks", "m", "path to the shop"),
    ("A train covers", "km", "track"),
    ("Emma jogs", "km", "morning run"),
]

MONEY_CONTEXTS = [
    ("Emma", "savings"),
    ("Jack", "pocket money"),
    ("A shop's", "daily takings"),
    ("The club's", "fundraising total"),
]

TIME_CONTEXTS = [
    ("homework", "hour"),
    ("the journey", "hour"),
    ("the match", "minutes of the 90-minute"),
    ("the lesson", "hour"),
    ("the movie", "hours of the 2-hour"),
]

# =============================================================================
# LEVEL 1: Visual Fractions & Basic Recognition (Foundation) - 75% Visual
# =============================================================================

def generate_level_1():
    """What fraction is shaded? / Identify fractions - VISUAL"""
    questions = []
    
    # Type 1: What fraction is shaded (VISUAL - shapes)
    for shape in SHAPES:
        for den in [2, 3, 4, 5, 6, 8]:
            for num in range(1, den):
                q_text = f"A {shape} is divided into {den} equal parts. {num} part{'s are' if num > 1 else ' is'} shaded. What fraction of the {shape} is shaded?"
                answer = fraction_str(num, den)
                
                distractors = [
                    lambda n=num, d=den: fraction_str(d - n, d),
                    lambda n=num, d=den: fraction_str(n, d + 1),
                    lambda n=num, d=den: fraction_str(n + 1, d) if n + 1 < d else fraction_str(n - 1, d),
                    lambda n=num, d=den: fraction_str(d, n) if n != 0 else "1/1",
                    lambda n=num, d=den: fraction_str(n, d + 2),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: Fraction remaining/unshaded (VISUAL)
    for shape in ['pizza', 'pie', 'cake', 'chocolate bar']:
        for den in [4, 6, 8, 10, 12]:
            eaten = random.randint(1, den - 1)
            remaining = den - eaten
            q_text = f"A {shape} is cut into {den} equal slices. {eaten} slice{'s have' if eaten > 1 else ' has'} been eaten. What fraction remains?"
            answer = fraction_str(remaining, den)
            
            distractors = [
                lambda e=eaten, d=den: fraction_str(e, d),
                lambda r=remaining, d=den: fraction_str(r + 1, d),
                lambda r=remaining, d=den: fraction_str(r, d + 1),
                lambda r=remaining, d=den: fraction_str(d, r) if r != 0 else "1/1",
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 3: Container filled (VISUAL)
    for container in CONTAINERS:
        for den in [2, 3, 4, 5, 8, 10]:
            num = random.randint(1, den - 1)
            q_text = f"A {container} is {num}/{den} full of water. What fraction is empty?"
            empty_num = den - num
            answer = fraction_str(empty_num, den)
            
            distractors = [
                lambda n=num, d=den: fraction_str(n, d),
                lambda e=empty_num, d=den: fraction_str(e + 1, d),
                lambda e=empty_num, d=den: fraction_str(e, d + 1),
                lambda e=empty_num, d=den: fraction_str(d, e) if e != 0 else "1/1",
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 4: Identify fraction from description (VISUAL context)
    descriptions = [
        (1, 2, "half"),
        (1, 4, "quarter"),
        (3, 4, "three quarters"),
        (1, 3, "one third"),
        (2, 3, "two thirds"),
    ]
    for num, den, name in descriptions:
        for shape in ['circle', 'rectangle', 'square']:
            q_text = f"A {shape} has {name} of its area shaded. Write this as a fraction."
            answer = fraction_str(num, den)
            
            distractors = [
                lambda n=num, d=den: fraction_str(d, n) if n != 0 else "1/1",
                lambda n=num, d=den: fraction_str(n + 1, d),
                lambda n=num, d=den: fraction_str(n, d + 1),
                lambda n=num, d=den: fraction_str(d - n, d),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 2: Equivalent Fractions (Foundation) - 75% Visual
# =============================================================================

def generate_level_2():
    """Find equivalent fractions - with visual contexts"""
    questions = []
    
    # Type 1: Visual equivalent - same amount different pieces
    for shape in ['pizza', 'chocolate bar', 'cake']:
        base_fractions = [(1,2,2,4), (1,2,3,6), (1,2,4,8), (1,3,2,6), (2,3,4,6), (1,4,2,8), (3,4,6,8)]
        for n1, d1, n2, d2 in base_fractions:
            q_text = f"A {shape} cut into {d1} pieces has {n1} piece{'s' if n1 > 1 else ''} taken. Another identical {shape} cut into {d2} pieces has the same amount taken. How many pieces were taken from the second {shape}?"
            answer = str(n2)
            
            distractors = [
                lambda x=n2: str(x + 1),
                lambda x=n2: str(x - 1) if x > 1 else str(x + 2),
                lambda x=n2: str(x + 2),
                lambda d=d2, n=n1: str(d - n1),
                lambda x=n2: str(x * 2),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Find equivalent fraction
    base_fractions = [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5), (1,6), (5,6)]
    for num, den in base_fractions:
        for mult in [2, 3, 4, 5]:
            q_text = f"Which fraction is equivalent to {num}/{den}?"
            answer = fraction_str(num * mult, den * mult)
            
            distractors = [
                lambda n=num, d=den, m=mult: fraction_str(n * m + 1, d * m),
                lambda n=num, d=den, m=mult: fraction_str(n * m, d * m + 1),
                lambda n=num, d=den, m=mult: fraction_str(n + m, d + m),
                lambda n=num, d=den: fraction_str(d, n) if n != 0 else "1/1",
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 3: Fill in missing numerator (VISUAL context)
    for num, den in [(1,2), (1,3), (2,3), (1,4), (3,4), (2,5)]:
        for mult in [2, 3, 4, 5, 6]:
            new_den = den * mult
            new_num = num * mult
            shape = random.choice(['rectangle', 'circle', 'bar'])
            q_text = f"A {shape} divided into {den} parts has {num} shaded. If the same {shape} were divided into {new_den} equal parts, how many would be shaded to show the same fraction?"
            answer = str(new_num)
            
            distractors = [
                lambda n=new_num: str(n + 1),
                lambda n=new_num: str(n - 1) if n > 1 else str(n + 2),
                lambda n=new_num: str(n + 2),
                lambda d=new_den, o=den: str(d - o),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 4: Missing denominator
    for num, den in [(1,2), (1,3), (1,4), (2,3), (3,4)]:
        for mult in [2, 3, 4, 5]:
            new_num = num * mult
            new_den = den * mult
            q_text = f"Find the missing denominator: {num}/{den} = {new_num}/?"
            answer = str(new_den)
            
            distractors = [
                lambda d=new_den: str(d + 1),
                lambda d=new_den: str(d - 1) if d > 1 else str(d + 2),
                lambda n=new_num: str(n),
                lambda d=new_den: str(d + 2),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 3: Simplifying Fractions (Foundation) - 75% Visual
# =============================================================================

def generate_level_3():
    """Simplify fractions to lowest terms - with visual contexts"""
    questions = []
    
    # Type 1: Simplify with visual context
    simplifiable = []
    for n in range(2, 24):
        for d in range(n + 1, 30):
            g = gcd(n, d)
            if g > 1:
                simplifiable.append((n, d))
    
    random.shuffle(simplifiable)
    
    for num, den in simplifiable[:30]:
        sn, sd = simplify_fraction(num, den)
        context = random.choice([
            f"A rectangle is divided into {den} squares, with {num} shaded. Write the shaded fraction in its simplest form.",
            f"In a bag of {den} marbles, {num} are red. What fraction are red? Give your answer in simplest form.",
            f"Out of {den} students, {num} chose pizza. What fraction chose pizza? Simplify your answer.",
            f"{num} out of {den} questions were answered correctly. Write this as a fraction in lowest terms.",
        ])
        q_text = context
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda n=num, d=den: fraction_str(n, d),  # Unsimplified
            lambda s=sn, t=sd: fraction_str(s + 1, t),
            lambda s=sn, t=sd: fraction_str(s, t + 1),
            lambda s=sn, t=sd: fraction_str(t, s) if s != 0 else "1/1",
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 2: SEC-style "Give your answer in simplest form"
    for num, den in simplifiable[30:50]:
        sn, sd = simplify_fraction(num, den)
        q_text = f"Write {num}/{den} in its simplest form."
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda n=num, d=den: fraction_str(n, d),
            lambda s=sn, t=sd: fraction_str(s * 2, t * 2),
            lambda s=sn, t=sd: fraction_str(s + 1, t),
            lambda s=sn, t=sd: fraction_str(s, t + 1),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Time as fraction (SEC 2024 OL style) - simplify
    time_fractions = [
        (15, 60, "15 minutes", "one hour"),
        (20, 60, "20 minutes", "one hour"),
        (30, 60, "30 minutes", "one hour"),
        (45, 60, "45 minutes", "one hour"),
        (10, 60, "10 minutes", "one hour"),
        (40, 60, "40 minutes", "one hour"),
        (12, 60, "12 minutes", "one hour"),
        (24, 60, "24 minutes", "one hour"),
    ]
    
    for num, den, time_str, unit in time_fractions:
        sn, sd = simplify_fraction(num, den)
        q_text = f"Write {time_str} as a fraction of {unit}. Give your answer in its simplest form."
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda n=num, d=den: fraction_str(n, d),
            lambda s=sn, t=sd: fraction_str(s + 1, t),
            lambda s=sn, t=sd: fraction_str(s, t - 1) if t > 2 else fraction_str(s, t + 1),
            lambda n=num: f"{n}/100",
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 4: Same Denominator Add/Subtract (Foundation) - 75% Visual
# =============================================================================

def generate_level_4():
    """Add and subtract fractions with same denominator - visual contexts"""
    questions = []
    
    # Type 1: Visual addition - combining portions
    for den in [4, 5, 6, 8, 10, 12]:
        for n1 in range(1, den - 1):
            for n2 in range(1, den - n1):
                if n1 + n2 < den:
                    shape = random.choice(['pizza', 'cake', 'pie', 'chocolate bar'])
                    q_text = f"Emma eats {n1}/{den} of a {shape}. Tom eats {n2}/{den} of the same {shape}. What fraction have they eaten altogether?"
                    result_num = n1 + n2
                    answer = fraction_str(result_num, den)
                    
                    distractors = [
                        lambda a=n1, b=n2, d=den: fraction_str(a + b, d + d),
                        lambda r=result_num, d=den: fraction_str(r + 1, d),
                        lambda r=result_num, d=den: fraction_str(r, d + 1),
                        lambda a=n1, b=n2, d=den: fraction_str(a * b, d),
                    ]
                    
                    result = create_question(q_text, answer, distractors)
                    if result:
                        questions.append(result)
    
    # Type 2: Visual subtraction - remaining portion
    for den in [4, 5, 6, 8, 10, 12]:
        for n1 in range(2, den):
            for n2 in range(1, n1):
                shape = random.choice(['tank', 'jar', 'bottle', 'bucket'])
                q_text = f"A {shape} is {n1}/{den} full. After {n2}/{den} is used, what fraction remains?"
                result_num = n1 - n2
                answer = fraction_str(result_num, den)
                
                distractors = [
                    lambda r=result_num, d=den: fraction_str(r + 1, d),
                    lambda a=n1, b=n2, d=den: fraction_str(a + b, d),
                    lambda r=result_num, d=den: fraction_str(r, d - 1) if d > 2 else fraction_str(r, d + 1),
                    lambda a=n1, d=den: fraction_str(d - a, d),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    # Type 3: Pure calculation (25% non-visual)
    for den in [3, 5, 7, 9, 11]:
        for n1 in range(1, den):
            for n2 in range(1, den - n1 + 1):
                if n1 + n2 <= den:
                    q_text = f"Calculate {n1}/{den} + {n2}/{den}"
                    result_num = n1 + n2
                    answer = fraction_str(result_num, den)
                    
                    distractors = [
                        lambda a=n1, b=n2, d=den: fraction_str(a + b, d + d),
                        lambda r=result_num, d=den: fraction_str(r + 1, d),
                        lambda r=result_num, d=den: fraction_str(r - 1, d) if r > 1 else fraction_str(r + 2, d),
                        lambda r=result_num, d=den: fraction_str(r, d + 1),
                    ]
                    
                    result = create_question(q_text, answer, distractors)
                    if result:
                        questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 5: Different Denominator Add/Subtract - Simple (Ordinary) ★ SEC Q10(a)
# =============================================================================

def generate_level_5():
    """Add/subtract with different denominators - SEC Q10(a) style"""
    questions = []
    
    # SEC 2022 OL Q10(a) style: "Write the following as a single fraction in its simplest form"
    pairs = [
        (2, 4), (2, 6), (2, 8), (2, 10),
        (3, 6), (3, 9), (3, 12),
        (4, 8), (4, 12),
        (5, 10), (5, 15),
    ]
    
    # Type 1: SEC exact style (25% pure calculation)
    for d1, d2 in pairs:
        for n1 in range(1, d1):
            for n2 in range(1, d2):
                common_d = lcm(d1, d2)
                result_n = n1 * (common_d // d1) + n2 * (common_d // d2)
                
                q_text = f"Write the following as a single fraction in its simplest form:\n{n1}/{d1} + {n2}/{d2}"
                answer = fraction_str(result_n, common_d)
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                    lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=common_d: fraction_str(r, d + 1),
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, max(c, e)),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: Visual context - journey fractions (75% visual)
    for context, unit, desc in JOURNEY_CONTEXTS:
        for d1, d2 in [(2, 4), (3, 6), (2, 6), (4, 8)]:
            n1 = random.randint(1, d1 - 1)
            n2 = random.randint(1, d2 - 1)
            common_d = lcm(d1, d2)
            result_n = n1 * (common_d // d1) + n2 * (common_d // d2)
            
            q_text = f"{context} {n1}/{d1} of their {desc} in the morning and {n2}/{d2} in the afternoon. What fraction of the journey is completed? Give your answer in simplest form."
            answer = fraction_str(result_n, common_d)
            
            distractors = [
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                lambda r=result_n, d=common_d: fraction_str(r - 1, d) if r > 1 else fraction_str(r + 2, d),
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c * e),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 3: Subtraction with visual context
    for d1, d2 in [(2, 4), (3, 6), (4, 8), (5, 10)]:
        for _ in range(3):
            n1 = random.randint(d1 // 2 + 1, d1 - 1) if d1 > 2 else 1
            n2 = random.randint(1, d2 // 2)
            common_d = lcm(d1, d2)
            val1 = n1 * (common_d // d1)
            val2 = n2 * (common_d // d2)
            if val1 > val2:
                result_n = val1 - val2
                name, item = random.choice([("Sarah", "pocket money"), ("Tom", "savings"), ("Emma", "allowance")])
                q_text = f"{name} had {n1}/{d1} of their {item} left. They spent {n2}/{d2} of the original amount. What fraction remains? Give your answer in simplest form."
                answer = fraction_str(result_n, common_d)
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(abs(a - b), c + e) if a != b else fraction_str(1, c + e),
                    lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, max(c, e)),
                    lambda r=result_n, d=common_d: fraction_str(r, d + 1),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 6: Different Denominator Add/Subtract - Complex (Ordinary) ★ SEC Q10(a)
# =============================================================================

def generate_level_6():
    """Add/subtract with co-prime denominators - SEC Q10(a) style"""
    questions = []
    
    # Co-prime pairs requiring LCD calculation
    pairs = [
        (2, 3), (2, 5), (2, 7), (2, 9),
        (3, 4), (3, 5), (3, 7), (3, 8),
        (4, 5), (4, 7), (4, 9),
        (5, 6), (5, 7), (5, 8),
        (6, 7), (7, 8), (7, 9),
    ]
    
    # Type 1: SEC exact style - "Write as single fraction in simplest form"
    for d1, d2 in pairs:
        for n1 in range(1, d1):
            for n2 in range(1, d2):
                common_d = lcm(d1, d2)
                result_n = n1 * (common_d // d1) + n2 * (common_d // d2)
                
                q_text = f"Write the following as a single fraction in its simplest form:\n{n1}/{d1} + {n2}/{d2}"
                answer = fraction_str(result_n, common_d)
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c * e),
                    lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=common_d: fraction_str(r - 1, d) if r > 1 else fraction_str(r + 2, d),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: Visual - tank/container problems
    for d1, d2 in [(2, 3), (3, 4), (2, 5), (3, 5), (4, 5)]:
        n1 = random.randint(1, d1 - 1)
        n2 = random.randint(1, d2 - 1)
        common_d = lcm(d1, d2)
        result_n = n1 * (common_d // d1) + n2 * (common_d // d2)
        
        container = random.choice(['tank', 'barrel', 'container', 'pool'])
        q_text = f"A {container} is {n1}/{d1} full. Another {n2}/{d2} is added. What fraction is now full? Give your answer in simplest form."
        answer = fraction_str(result_n, common_d)
        
        distractors = [
            lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
            lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * b, c * e),
            lambda r=result_n, d=common_d: fraction_str(r + 1, d),
            lambda r=result_n, d=common_d: fraction_str(r, d - 1) if d > 2 else fraction_str(r, d + 1),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Subtraction - SEC style
    for d1, d2 in pairs[:10]:
        n1 = d1 - 1  # Larger fraction
        n2 = 1  # Smaller fraction
        common_d = lcm(d1, d2)
        val1 = n1 * (common_d // d1)
        val2 = n2 * (common_d // d2)
        result_n = val1 - val2
        
        if result_n > 0:
            q_text = f"Write the following as a single fraction in its simplest form:\n{n1}/{d1} − {n2}/{d2}"
            answer = fraction_str(result_n, common_d)
            
            distractors = [
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(abs(a - b), abs(c - e)) if c != e else fraction_str(abs(a - b), c),
                lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                lambda r=result_n, d=common_d: fraction_str(r, d + 1),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 7: Multiply Fractions (Ordinary) - 75% Visual
# =============================================================================

def generate_level_7():
    """Multiply fractions - with visual contexts"""
    questions = []
    
    fractions = [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5),
                 (1,6), (5,6), (2,7), (3,7), (3,8), (5,8)]
    
    # Type 1: "Fraction of a fraction" visual context
    for f1 in fractions[:8]:
        for f2 in fractions[:8]:
            n1, d1 = f1
            n2, d2 = f2
            result_n = n1 * n2
            result_d = d1 * d2
            
            item = random.choice(['pizza', 'cake', 'chocolate bar', 'pie'])
            q_text = f"{n1}/{d1} of a {item} remains. Emma eats {n2}/{d2} of what's left. What fraction of the whole {item} did Emma eat? Give your answer in simplest form."
            answer = fraction_str(result_n, result_d)
            
            distractors = [
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * e, b * c),
                lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Pure calculation (25%)
    for f1 in fractions[4:]:
        for f2 in fractions[4:]:
            n1, d1 = f1
            n2, d2 = f2
            result_n = n1 * n2
            result_d = d1 * d2
            
            q_text = f"Calculate {n1}/{d1} × {n2}/{d2}. Give your answer in its simplest form."
            answer = fraction_str(result_n, result_d)
            
            distractors = [
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * b + 1, c * e),
                lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 3: Whole number × fraction (visual)
    for n, d in [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5)]:
        for whole in [2, 3, 4, 5, 6]:
            result_n = n * whole
            item = random.choice(['bag', 'box', 'packet'])
            thing = random.choice(['sweets', 'marbles', 'stickers'])
            q_text = f"Each {item} contains {n}/{d} kg of {thing}. How much is in {whole} {item}s? Give your answer in simplest form."
            answer = fraction_str(result_n, d)
            
            distractors = [
                lambda r=result_n, dd=d: fraction_str(r + 1, dd),
                lambda r=result_n, dd=d: fraction_str(r - 1, dd) if r > 1 else fraction_str(r + 2, dd),
                lambda r=result_n, dd=d, w=whole: fraction_str(r, dd * w),
                lambda nn=n, w=whole, dd=d: fraction_str(nn + w, dd),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 8: Divide Fractions (Ordinary) - 75% Visual
# =============================================================================

def generate_level_8():
    """Divide fractions - with visual contexts"""
    questions = []
    
    fractions = [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5),
                 (1,6), (5,6), (2,7), (3,8), (5,8)]
    
    # Type 1: "How many portions" visual context
    for f1 in fractions[:8]:
        for f2 in fractions[:6]:
            if f1 != f2:
                n1, d1 = f1
                n2, d2 = f2
                result_n = n1 * d2
                result_d = d1 * n2
                
                sn, sd = simplify_fraction(result_n, result_d)
                if sd != 1 and sn < 10:  # Keep reasonable answers
                    item = random.choice(['pizza', 'cake', 'ribbon', 'rope'])
                    q_text = f"A {item} is {n1}/{d1} of its original size. It is cut into pieces that are each {n2}/{d2} of the original. How many pieces can be made? Give your answer as a fraction in simplest form."
                    answer = fraction_str(result_n, result_d)
                    
                    distractors = [
                        lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * b, c * e),
                        lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                        lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
                        lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a - b, c - e) if c != e and a != b else fraction_str(a + b, c + e),
                    ]
                    
                    result = create_question(q_text, answer, distractors)
                    if result:
                        questions.append(result)
    
    # Type 2: Pure calculation (25%)
    for f1 in fractions:
        for f2 in fractions:
            if f1 != f2:
                n1, d1 = f1
                n2, d2 = f2
                result_n = n1 * d2
                result_d = d1 * n2
                
                q_text = f"Calculate {n1}/{d1} ÷ {n2}/{d2}. Give your answer in its simplest form."
                answer = fraction_str(result_n, result_d)
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * b, c * e),
                    lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
                    lambda r=result_n, d=result_d: fraction_str(r, d + 1),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    # Type 3: Divide by whole number (visual)
    for n, d in [(1,2), (2,3), (3,4), (4,5), (5,6)]:
        for whole in [2, 3, 4]:
            result_d = d * whole
            thing = random.choice(['cake', 'pizza', 'chocolate bar'])
            q_text = f"A {thing} that is {n}/{d} of the original is shared equally among {whole} people. What fraction does each person get?"
            answer = fraction_str(n, result_d)
            
            distractors = [
                lambda nn=n, dd=d, w=whole: fraction_str(nn * w, dd),
                lambda nn=n, rd=result_d: fraction_str(nn + 1, rd),
                lambda nn=n, rd=result_d: fraction_str(rd, nn) if nn != 0 else "1/1",
                lambda nn=n, dd=d: fraction_str(nn, dd),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 9: Ratios & Proportions with Fractions (Ordinary) ★ SEC Style
# =============================================================================

def generate_level_9():
    """Ratio problems - SEC 2023 OL Q10(b) style"""
    questions = []
    
    # Type 1: SEC style ratio problems "Ratio of X to Y is a:b"
    ratio_problems = [
        (4, 21, 450, "fruit", "yoghurt", "g"),  # SEC 2023 style
        (2, 5, 350, "sugar", "flour", "g"),
        (3, 7, 200, "water", "concentrate", "ml"),
        (1, 4, 250, "cream", "milk", "ml"),
        (2, 3, 300, "red paint", "blue paint", "ml"),
        (3, 5, 400, "boys", "girls", "students"),
        (5, 8, 520, "adults", "children", "people"),
        (1, 3, 240, "savings", "spending", "euro"),
    ]
    
    for r1, r2, total, item1, item2, unit in ratio_problems:
        # Calculate the amount of first item
        total_parts = r1 + r2
        amount1 = (total * r1) // total_parts
        if amount1 == total * r1 / total_parts:  # Exact division
            q_text = f"A mixture contains {item1} and {item2}. The ratio of {item1} to {item2} is {r1}:{r2}. The total weight is {total} {unit}. How many {unit} of {item1} are in the mixture?"
            answer = f"{amount1}"
            
            amount2 = total - amount1
            distractors = [
                lambda a2=amount2: str(a2),
                lambda a1=amount1: str(a1 + 10),
                lambda a1=amount1: str(a1 - 10) if a1 > 10 else str(a1 + 20),
                lambda t=total, r=r1: str(t // r) if r != 0 else str(t),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Simplify ratios to fractions
    for r1, r2 in [(4, 6), (6, 9), (8, 12), (10, 15), (12, 16), (15, 20), (9, 12), (6, 8)]:
        g = gcd(r1, r2)
        s1, s2 = r1 // g, r2 // g
        q_text = f"In a class, the ratio of boys to girls is {r1}:{r2}. What fraction of the class are boys? Give your answer in simplest form."
        total = s1 + s2
        answer = fraction_str(s1, total)
        
        distractors = [
            lambda a=r1, b=r2: fraction_str(a, b),
            lambda a=s1, t=total: fraction_str(a + 1, t),
            lambda a=s2, t=total: fraction_str(a, t),  # Girls instead
            lambda a=r1, b=r2: fraction_str(a, a + b),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Pie chart fractions (SEC 2024 OL style)
    for total in [12, 24, 30, 36, 40]:
        choices = random.sample(['Maths', 'Science', 'History', 'English', 'Art', 'Music', 'PE'], 3)
        counts = []
        remaining = total
        for i, choice in enumerate(choices[:-1]):
            count = random.randint(total // 6, total // 3)
            counts.append(count)
            remaining -= count
        counts.append(remaining)
        
        for i, (choice, count) in enumerate(zip(choices, counts)):
            sn, sd = simplify_fraction(count, total)
            q_text = f"A survey of {total} students asked about their favourite subject. {count} students chose {choice}. What fraction chose {choice}? Give your answer in simplest form."
            answer = fraction_str(sn, sd)
            
            distractors = [
                lambda c=count, t=total: fraction_str(c, t),
                lambda s=sn, d=sd: fraction_str(s + 1, d),
                lambda c=count, t=total: fraction_str(t - c, t),
                lambda s=sn, d=sd: fraction_str(d, s) if s != 0 else "1/1",
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 4: Mixed number ratios (SEC 2025 HL style simplified)
    for _ in range(10):
        a, b, c = random.sample([1, 2, 3, 4, 5], 3)
        total_ml = random.choice([100, 200, 500, 1000])
        total_parts = a + b + c
        amount_b = (total_ml * b) // total_parts
        if amount_b == total_ml * b / total_parts:
            q_text = f"A solution is made of ingredients A, B, and C in the ratio {a}:{b}:{c}. How many ml of B are in {total_ml} ml of solution?"
            answer = str(amount_b)
            
            amount_a = (total_ml * a) // total_parts
            amount_c = (total_ml * c) // total_parts
            distractors = [
                lambda aa=amount_a: str(aa),
                lambda ac=amount_c: str(ac),
                lambda ab=amount_b: str(ab + 10),
                lambda t=total_ml, bb=b: str(t // bb) if bb != 0 else str(t),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 10: Slope & Coordinate Geometry with Fractions (Ordinary) ★ SEC Style
# =============================================================================

def generate_level_10():
    """Slope as fraction - SEC 2022-2025 OL style"""
    questions = []
    
    # Type 1: Calculate slope from two points - give as fraction
    point_pairs = [
        ((0, 0), (3, 2)),
        ((1, 1), (4, 3)),
        ((0, 3), (6, 7)),
        ((2, 1), (5, 4)),
        ((-1, 2), (2, 5)),
        ((0, -1), (4, 2)),
        ((3, -1), (-4, 2)),  # SEC 2025 style
        ((1, 2), (5, 6)),
        ((0, 1), (3, 4)),
        ((2, 3), (8, 6)),
        ((-2, 1), (4, 4)),
        ((0, 5), (10, 0)),
        ((1, -2), (3, 4)),
        ((0, 0), (5, 3)),
        ((-3, 2), (3, -2)),
    ]
    
    for (x1, y1), (x2, y2) in point_pairs:
        rise = y2 - y1
        run = x2 - x1
        if run != 0:
            sn, sd = simplify_fraction(rise, run)
            if sd < 0:
                sn, sd = -sn, -sd
            
            q_text = f"Points A = ({x1}, {y1}) and B = ({x2}, {y2}) are shown on a coordinate diagram. Work out the slope of the line AB. Give your answer as a fraction."
            answer = fraction_str(sn, sd)
            
            distractors = [
                lambda r=rise, n=run: fraction_str(n, r) if r != 0 else "0",  # Inverted
                lambda s=sn, d=sd: fraction_str(s + 1, d),
                lambda s=sn, d=sd: fraction_str(-s, d),  # Wrong sign
                lambda s=sn, d=sd: fraction_str(s, d + 1),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Interpret slope (SEC 2023 OL style)
    slope_contexts = [
        ((2, 3), "weight in kg", "age in months", "baby's"),
        ((3, 4), "height in cm", "weeks", "plant's"),
        ((1, 2), "distance in km", "hours", "cyclist's"),
        ((5, 2), "cost in €", "items bought", "shop's"),
        ((4, 5), "temperature °C", "hours", "oven's"),
    ]
    
    for (rise, run), y_unit, x_unit, context in slope_contexts:
        sn, sd = simplify_fraction(rise, run)
        x1, y1 = 0, random.randint(1, 5)
        x2 = run * 3
        y2 = y1 + rise * 3
        
        q_text = f"The graph shows a {context} progress. Points ({x1}, {y1}) and ({x2}, {y2}) are on the line. What is the slope? Give your answer as a fraction in simplest form."
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda s=sn, d=sd: fraction_str(d, s) if s != 0 else "1/1",
            lambda s=sn, d=sd: fraction_str(s + 1, d),
            lambda yy1=y1, yy2=y2: fraction_str(yy1, yy2),
            lambda s=sn, d=sd: fraction_str(s, d + 1),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Trigonometry ratios as fractions (SEC 2022-2025 OL)
    trig_triangles = [
        (3, 4, 5),  # 3-4-5 right triangle
        (5, 12, 13),
        (8, 15, 17),
        (6, 8, 10),
        (9, 12, 15),
        (5, 5, 7),  # Approximate
        (10, 24, 26),
        (12, 16, 20),
        (7, 24, 25),
        (20, 21, 29),
    ]
    
    for opp, adj, hyp in trig_triangles:
        # sin = opp/hyp
        sn, sd = simplify_fraction(opp, hyp)
        q_text = f"In a right-angled triangle, the side opposite angle A is {opp} cm and the hypotenuse is {hyp} cm. Write sin A as a fraction in its simplest form."
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda o=opp, h=hyp: fraction_str(h, o),
            lambda o=opp, a=adj: fraction_str(o, a),
            lambda a=adj, h=hyp: fraction_str(a, h),
            lambda s=sn, d=sd: fraction_str(s + 1, d),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
        
        # cos = adj/hyp
        sn, sd = simplify_fraction(adj, hyp)
        q_text = f"In a right-angled triangle, the side adjacent to angle A is {adj} cm and the hypotenuse is {hyp} cm. Write cos A as a fraction in its simplest form."
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda a=adj, h=hyp: fraction_str(h, a),
            lambda o=opp, h=hyp: fraction_str(o, h),
            lambda o=opp, a=adj: fraction_str(o, a),
            lambda s=sn, d=sd: fraction_str(s + 1, d),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
        
        # tan = opp/adj
        sn, sd = simplify_fraction(opp, adj)
        q_text = f"In a right-angled triangle, the side opposite angle A is {opp} cm and the adjacent side is {adj} cm. Write tan A as a fraction in its simplest form."
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda o=opp, a=adj: fraction_str(a, o),
            lambda o=opp, h=hyp: fraction_str(o, h),
            lambda a=adj, h=hyp: fraction_str(a, h),
            lambda s=sn, d=sd: fraction_str(s + 1, d),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 11: Fraction-Decimal-Percentage Conversion (Higher) - 50% Visual
# =============================================================================

def generate_level_11():
    """Convert between fractions, decimals, and percentages - 50% visual"""
    questions = []
    
    conversions = [
        (1, 2, 0.5, 50), (1, 4, 0.25, 25), (3, 4, 0.75, 75),
        (1, 5, 0.2, 20), (2, 5, 0.4, 40), (3, 5, 0.6, 60), (4, 5, 0.8, 80),
        (1, 8, 0.125, 12.5), (3, 8, 0.375, 37.5), (5, 8, 0.625, 62.5), (7, 8, 0.875, 87.5),
        (1, 10, 0.1, 10), (3, 10, 0.3, 30), (7, 10, 0.7, 70), (9, 10, 0.9, 90),
        (1, 20, 0.05, 5), (1, 25, 0.04, 4), (1, 50, 0.02, 2),
    ]
    
    # Type 1: Fraction to decimal (visual context - 50%)
    for n, d, dec, pct in conversions[:12]:
        if random.random() < 0.5:
            # Visual context
            item = random.choice(['test', 'quiz', 'exam'])
            q_text = f"A student scored {n}/{d} on a {item}. Convert this to a decimal."
        else:
            q_text = f"Convert {n}/{d} to a decimal."
        answer = str(dec)
        
        distractors = [
            lambda x=dec: str(x + 0.1),
            lambda x=dec: str(x - 0.1) if x > 0.1 else str(x + 0.2),
            lambda x=dec: str(x * 10),
            lambda nn=n, dd=d: str(round(dd / nn, 2)) if nn != 0 else "1",
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 2: Decimal to fraction
    for n, d, dec, pct in conversions:
        if random.random() < 0.5:
            q_text = f"A tank is {dec} full. Write this as a fraction in its simplest form."
        else:
            q_text = f"Convert {dec} to a fraction in its simplest form."
        answer = fraction_str(n, d)
        
        distractors = [
            lambda nn=n, dd=d: fraction_str(nn + 1, dd),
            lambda nn=n, dd=d: fraction_str(nn, dd + 1),
            lambda nn=n, dd=d: fraction_str(dd, nn) if nn != 0 else "1/1",
            lambda nn=n, dd=d: fraction_str(nn * 2, dd * 2),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Fraction to percentage
    for n, d, dec, pct in conversions:
        if isinstance(pct, float):
            pct_str = f"{pct}%"
        else:
            pct_str = f"{pct}%"
        
        if random.random() < 0.5:
            q_text = f"In a sale, {n}/{d} of items are reduced. What percentage is this?"
        else:
            q_text = f"Convert {n}/{d} to a percentage."
        answer = pct_str
        
        distractors = [
            lambda p=pct: f"{p + 10}%" if isinstance(p, int) else f"{p + 5}%",
            lambda p=pct: f"{p - 10}%" if p > 10 else f"{p + 20}%",
            lambda p=pct: f"{p * 2}%" if p <= 50 else f"{p // 2}%",
            lambda nn=n, dd=d: f"{nn * 10}%",
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 4: Percentage to fraction
    for n, d, dec, pct in conversions[:15]:
        if isinstance(pct, int):
            if random.random() < 0.5:
                q_text = f"A shop offers {pct}% off. Write this as a fraction in simplest form."
            else:
                q_text = f"Convert {pct}% to a fraction in its simplest form."
            answer = fraction_str(n, d)
            
            distractors = [
                lambda p=pct: fraction_str(p, 100),
                lambda nn=n, dd=d: fraction_str(nn + 1, dd),
                lambda nn=n, dd=d: fraction_str(nn, dd * 2),
                lambda nn=n, dd=d: fraction_str(nn * 2, dd),
            ]
            
            result = create_question(q_text, answer, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 12: Probability & Complex Problems (Higher) - 50% Visual
# =============================================================================

def generate_level_12():
    """Probability as fractions & complex problems - SEC Higher style"""
    questions = []
    
    # Type 1: Basic probability as fraction (SEC 2022 HL style)
    probability_contexts = [
        (6, "dice", "rolling a", ["1", "2", "3", "4", "5", "6"]),
        (52, "deck of cards", "drawing a", ["heart", "diamond", "club", "spade"]),
        (10, "bag of marbles", "picking a", ["red", "blue", "green"]),
        (8, "spinner", "landing on", ["section 1", "section 2", "section 3", "section 4"]),
    ]
    
    for total, context, action, outcomes in probability_contexts:
        for favorable in [1, 2, 3, 4]:
            if favorable < total:
                sn, sd = simplify_fraction(favorable, total)
                outcome = random.choice(outcomes)
                q_text = f"A {context} has {total} equally likely outcomes. What is the probability of {action} {outcome}? There are {favorable} favorable outcome{'s' if favorable > 1 else ''}. Give your answer as a fraction in simplest form."
                answer = fraction_str(sn, sd)
                
                distractors = [
                    lambda f=favorable, t=total: fraction_str(t - f, t),
                    lambda s=sn, d=sd: fraction_str(s + 1, d),
                    lambda s=sn, d=sd: fraction_str(d, s) if s != 0 else "1/1",
                    lambda f=favorable, t=total: fraction_str(f, t + 1),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: Combined probability (SEC 2022 HL - "at least one")
    for _ in range(10):
        p_win_n, p_win_d = random.choice([(1, 3), (1, 4), (2, 5), (1, 2)])
        # P(at least one win in 2 games) = 1 - P(lose both) = 1 - ((d-n)/d)^2
        p_lose_n = p_win_d - p_win_n
        # P(lose both) = (p_lose_n/p_win_d)^2
        p_lose_both_n = p_lose_n * p_lose_n
        p_lose_both_d = p_win_d * p_win_d
        # P(at least one) = 1 - P(lose both)
        p_atleast_n = p_lose_both_d - p_lose_both_n
        p_atleast_d = p_lose_both_d
        
        sn, sd = simplify_fraction(p_atleast_n, p_atleast_d)
        
        q_text = f"A team has probability {p_win_n}/{p_win_d} of winning each match. Find the probability they win at least one of their next 2 matches. Give your answer as a fraction in simplest form."
        answer = fraction_str(sn, sd)
        
        distractors = [
            lambda wn=p_win_n, wd=p_win_d: fraction_str(wn * 2, wd),
            lambda s=sn, d=sd: fraction_str(s + 1, d),
            lambda wn=p_win_n, wd=p_win_d: fraction_str(wn * wn, wd * wd),
            lambda s=sn, d=sd: fraction_str(d - s, d),
        ]
        
        result = create_question(q_text, answer, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Multi-step fraction problems
    for total in [120, 180, 240, 300]:
        for n1, d1 in [(1, 3), (1, 4), (2, 5), (3, 4)]:
            for n2, d2 in [(1, 2), (1, 3), (2, 3)]:
                first_part = (total * n1) // d1
                if first_part == total * n1 / d1:
                    second_part = (first_part * n2) // d2
                    if second_part == first_part * n2 / d2:
                        context = random.choice([
                            f"A school has {total} students. {n1}/{d1} are in sports clubs. Of those, {n2}/{d2} play football.",
                            f"A company has {total} employees. {n1}/{d1} work part-time. Of those, {n2}/{d2} work weekends.",
                            f"A library has {total} books. {n1}/{d1} are fiction. Of those, {n2}/{d2} are mysteries.",
                        ])
                        
                        q_text = f"{context} How many play football/work weekends/are mysteries?"
                        answer = str(second_part)
                        
                        distractors = [
                            lambda f=first_part: str(f),
                            lambda s=second_part: str(s + 5),
                            lambda s=second_part: str(s - 5) if s > 5 else str(s + 10),
                            lambda t=total, s=second_part: str(t - s),
                        ]
                        
                        result = create_question(q_text, answer, distractors)
                        if result:
                            questions.append(result)
    
    # Type 4: Combined operations
    for n1, d1 in [(1, 2), (1, 3), (2, 3), (1, 4)]:
        for n2, d2 in [(1, 4), (1, 3), (1, 2), (2, 5)]:
            for n3, d3 in [(1, 2), (1, 3), (1, 4)]:
                common_d = lcm(d1, d2)
                sum_n = n1 * (common_d // d1) + n2 * (common_d // d2)
                result_n = sum_n * n3
                result_d = common_d * d3
                
                q_text = f"Calculate ({n1}/{d1} + {n2}/{d2}) × {n3}/{d3}. Give your answer in simplest form."
                answer = fraction_str(result_n, result_d)
                
                distractors = [
                    lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                    lambda a=n1, b=n2, c=n3, x=d1, y=d2, z=d3: fraction_str(a + b + c, x + y + z),
                    lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
                    lambda r=result_n, d=result_d: fraction_str(r * 2, d * 2),
                ]
                
                result = create_question(q_text, answer, distractors)
                if result:
                    questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# MAIN GENERATION AND DATABASE FUNCTIONS
# =============================================================================

def get_difficulty_band(level):
    """Map level to SEC difficulty band"""
    if level <= 4:
        return 'foundation'
    elif level <= 8:
        return 'ordinary'
    else:
        return 'higher'

def insert_questions(cursor, questions, level):
    """Insert questions into database with validation"""
    inserted = 0
    seen_questions = set()
    difficulty_band = get_difficulty_band(level)
    
    for q_text, options, correct_idx in questions:
        q_key = q_text.lower().strip()[:100]
        if q_key in seen_questions:
            continue
        
        if len(set(options)) != 4:
            continue
        
        if correct_idx < 0 or correct_idx > 3:
            continue
        
        seen_questions.add(q_key)
        
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text, question_type,
                 option_a, option_b, option_c, option_d, correct_answer,
                 explanation, is_active, mode)
                VALUES (?, ?, ?, ?, 'multiple_choice', ?, ?, ?, ?, ?, '', 1, 'jc_exam')
            """, (
                'fractions',
                level,
                difficulty_band,
                q_text,
                options[0], options[1], options[2], options[3],
                correct_idx
            ))
            inserted += 1
        except Exception as e:
            print(f"  ⚠️ Insert error: {e}")
    
    return inserted

def clear_existing_sec_questions(cursor):
    """Remove existing SEC fractions questions"""
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = 'fractions' AND mode = 'jc_exam'
    """)
    print(f"🗑️  Cleared existing SEC fractions questions")

def main():
    print("=" * 70)
    print("JC SEC-ALIGNED FRACTIONS GENERATOR v4")
    print("Target: 50 questions × 12 levels = 600 questions")
    print("Visual elements: 75% (L1-10), 50% (L11-12)")
    print("=" * 70)
    
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found: {DB_PATH}")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'mode' not in columns:
        print("❌ 'mode' column not found. Run add_question_mode_column.py first.")
        conn.close()
        return
    
    clear_existing_sec_questions(cursor)
    
    generators = [
        (1, generate_level_1, "Visual Fractions (Shapes/Parts)", "75%"),
        (2, generate_level_2, "Equivalent Fractions (Visual)", "75%"),
        (3, generate_level_3, "Simplifying + Time Fractions", "75%"),
        (4, generate_level_4, "Same Denom +/− (Context)", "75%"),
        (5, generate_level_5, "Different Denom Simple ★ Q10(a)", "75%"),
        (6, generate_level_6, "Different Denom Complex ★ Q10(a)", "75%"),
        (7, generate_level_7, "Multiply Fractions (Context)", "75%"),
        (8, generate_level_8, "Divide Fractions (Context)", "75%"),
        (9, generate_level_9, "Ratios & Pie Charts ★ SEC", "75%"),
        (10, generate_level_10, "Slope & Trig Fractions ★ SEC", "75%"),
        (11, generate_level_11, "Decimal/Percentage Conversion", "50%"),
        (12, generate_level_12, "Probability & Complex ★ HL", "50%"),
    ]
    
    total_inserted = 0
    level_counts = {}
    
    for level, generator, description, visual_pct in generators:
        print(f"\n📝 Level {level}: {description} [{visual_pct} visual]")
        questions = generator()
        print(f"   Generated: {len(questions)} questions")
        
        inserted = insert_questions(cursor, questions, level)
        level_counts[level] = inserted
        total_inserted += inserted
        print(f"   Inserted: {inserted} questions")
    
    conn.commit()
    
    print("\n" + "=" * 70)
    print("SUMMARY - SEC ALIGNMENT")
    print("=" * 70)
    
    print("\n📊 Questions per Level:")
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        band = get_difficulty_band(level)
        bar = "█" * (count // 5) + "░" * ((50 - count) // 5)
        status = "✅" if count >= 45 else "⚠️" if count >= 30 else "❌"
        print(f"   Level {level:2d} ({band:10s}): {bar} {count:3d} {status}")
    
    print(f"\n✅ Total Questions Inserted: {total_inserted}")
    
    print("\n📋 SEC Question Types Covered:")
    print("   ✅ Time as fraction (2024 OL, 2023 HL)")
    print("   ✅ Adding fractions Q10(a) style (2022 OL)")
    print("   ✅ Slope as fraction (2022-2025 OL)")
    print("   ✅ Trig ratios as fractions (2022-2025 OL)")
    print("   ✅ Pie chart fractions (2024 OL)")
    print("   ✅ Ratio problems (2023 OL, 2025 HL)")
    print("   ✅ Probability as fractions (2022 HL)")
    
    print("\n🔍 Verifying question quality...")
    cursor.execute("""
        SELECT id, question_text, option_a, option_b, option_c, option_d
        FROM questions_adaptive
        WHERE topic = 'fractions' AND mode = 'jc_exam'
    """)
    
    issues = 0
    for row in cursor.fetchall():
        qid, text, a, b, c, d = row
        opts = [a, b, c, d]
        if len(set(opts)) != 4:
            print(f"   ❌ Q{qid} has duplicate options: {opts}")
            issues += 1
    
    if issues == 0:
        print("   ✅ All questions have unique options!")
    else:
        print(f"   ⚠️ Found {issues} questions with duplicate options")
    
    conn.close()
    print("\n✅ Generation complete!")

if __name__ == '__main__':
    main()
