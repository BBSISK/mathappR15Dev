"""
JC SEC-Aligned Fractions Question Generator v5
Target: 50 questions per level (600 total)

UPDATES in v5:
1. EXPLANATIONS for every question (step-by-step)
2. Fixed context matching in multi-step problems
3. 75% visual elements for Levels 1-10, 50% for Levels 11-12

SEC Question Types (2022-2025 Papers):
- Time as fraction (15 mins = ?/60 hour)
- Adding/subtracting fractions (Q10a style)
- Slope as fraction from coordinates
- Trigonometry ratios as fractions
- Pie chart / data fractions
- Ratio problems with fractions
- Probability as fractions

Run: python generate_jc_fractions_v5.py
"""

import sqlite3
import random
from math import gcd
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

def create_question_with_explanation(question_text, answer, explanation, distractor_funcs, max_attempts=50):
    """
    Create a question with validated unique options and explanation.
    Returns (question_text, options, correct_index, explanation) or None if failed.
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
                return (question_text, options, correct_idx, explanation)
    
    return None

# =============================================================================
# LEVEL 1: Visual Fractions & Basic Recognition (Foundation) - 75% Visual
# =============================================================================

def generate_level_1():
    """What fraction is shaded? / Identify fractions - VISUAL"""
    questions = []
    
    shapes = ['circle', 'rectangle', 'square', 'pizza', 'chocolate bar', 'cake', 'pie']
    
    # Type 1: What fraction is shaded
    for shape in shapes:
        for den in [2, 3, 4, 5, 6, 8]:
            for num in range(1, den):
                q_text = f"A {shape} is divided into {den} equal parts. {num} part{'s are' if num > 1 else ' is'} shaded. What fraction of the {shape} is shaded?"
                answer = fraction_str(num, den)
                explanation = f"The {shape} has {den} equal parts and {num} {'are' if num > 1 else 'is'} shaded. So the fraction shaded is {num}/{den}"
                sn, sd = simplify_fraction(num, den)
                if (sn, sd) != (num, den):
                    explanation += f" = {sn}/{sd} in simplest form."
                else:
                    explanation += "."
                
                distractors = [
                    lambda n=num, d=den: fraction_str(d - n, d),
                    lambda n=num, d=den: fraction_str(n, d + 1),
                    lambda n=num, d=den: fraction_str(n + 1, d) if n + 1 < d else fraction_str(n - 1, d),
                    lambda n=num, d=den: fraction_str(d, n) if n != 0 else "1/1",
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: Fraction remaining
    for shape in ['pizza', 'pie', 'cake', 'chocolate bar']:
        for den in [4, 6, 8, 10, 12]:
            for eaten in range(1, den - 1):
                remaining = den - eaten
                q_text = f"A {shape} is cut into {den} equal slices. {eaten} slice{'s have' if eaten > 1 else ' has'} been eaten. What fraction remains?"
                answer = fraction_str(remaining, den)
                explanation = f"Total slices = {den}. Eaten = {eaten}. Remaining = {den} - {eaten} = {remaining}. Fraction remaining = {remaining}/{den}"
                sn, sd = simplify_fraction(remaining, den)
                if (sn, sd) != (remaining, den):
                    explanation += f" = {sn}/{sd} in simplest form."
                else:
                    explanation += "."
                
                distractors = [
                    lambda e=eaten, d=den: fraction_str(e, d),
                    lambda r=remaining, d=den: fraction_str(r + 1, d),
                    lambda r=remaining, d=den: fraction_str(r, d + 1),
                    lambda r=remaining, d=den: fraction_str(d, r) if r != 0 else "1/1",
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
                if result:
                    questions.append(result)
    
    # Type 3: Container filled
    containers = ['jar', 'bottle', 'tank', 'jug', 'bucket', 'glass']
    for container in containers:
        for den in [2, 3, 4, 5, 8, 10]:
            for num in range(1, den):
                empty_num = den - num
                q_text = f"A {container} is {num}/{den} full of water. What fraction is empty?"
                answer = fraction_str(empty_num, den)
                explanation = f"If {num}/{den} is full, then the empty fraction = 1 - {num}/{den} = {den}/{den} - {num}/{den} = {empty_num}/{den}"
                sn, sd = simplify_fraction(empty_num, den)
                if (sn, sd) != (empty_num, den):
                    explanation += f" = {sn}/{sd} in simplest form."
                else:
                    explanation += "."
                
                distractors = [
                    lambda n=num, d=den: fraction_str(n, d),
                    lambda e=empty_num, d=den: fraction_str(e + 1, d),
                    lambda e=empty_num, d=den: fraction_str(e, d + 1),
                    lambda e=empty_num, d=den: fraction_str(d, e) if e != 0 else "1/1",
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
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
    
    # Type 1: Visual equivalent
    shapes = ['pizza', 'chocolate bar', 'cake', 'rectangle']
    base_fractions = [(1,2,2,4), (1,2,3,6), (1,2,4,8), (1,3,2,6), (2,3,4,6), (1,4,2,8), (3,4,6,8)]
    
    for shape in shapes:
        for n1, d1, n2, d2 in base_fractions:
            q_text = f"A {shape} cut into {d1} pieces has {n1} piece{'s' if n1 > 1 else ''} taken. Another identical {shape} cut into {d2} pieces has the same amount taken. How many pieces were taken from the second {shape}?"
            answer = str(n2)
            explanation = f"{n1}/{d1} of the first {shape} is taken. To find the equivalent with {d2} pieces: {n1}/{d1} = ?/{d2}. Multiply top and bottom by {d2 // d1}: {n1}×{d2 // d1}/{d1}×{d2 // d1} = {n2}/{d2}. So {n2} pieces."
            
            distractors = [
                lambda x=n2: str(x + 1),
                lambda x=n2: str(x - 1) if x > 1 else str(x + 2),
                lambda x=n2: str(x + 2),
                lambda d=d2, n=n1: str(d - n1),
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Find equivalent fraction
    base_fractions = [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5), (1,6), (5,6)]
    for num, den in base_fractions:
        for mult in [2, 3, 4, 5]:
            q_text = f"Which fraction is equivalent to {num}/{den}?"
            answer = fraction_str(num * mult, den * mult)
            explanation = f"To find an equivalent fraction, multiply both numerator and denominator by the same number. {num}/{den} × {mult}/{mult} = {num * mult}/{den * mult}."
            
            distractors = [
                lambda n=num, d=den, m=mult: fraction_str(n * m + 1, d * m),
                lambda n=num, d=den, m=mult: fraction_str(n * m, d * m + 1),
                lambda n=num, d=den, m=mult: fraction_str(n + m, d + m),
                lambda n=num, d=den: fraction_str(d, n) if n != 0 else "1/1",
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    # Type 3: Fill in missing numerator
    for num, den in [(1,2), (1,3), (2,3), (1,4), (3,4), (2,5)]:
        for mult in [2, 3, 4, 5, 6]:
            new_den = den * mult
            new_num = num * mult
            shape = random.choice(['rectangle', 'circle', 'bar'])
            q_text = f"A {shape} divided into {den} parts has {num} shaded. If the same {shape} were divided into {new_den} equal parts, how many would be shaded?"
            answer = str(new_num)
            explanation = f"We need {num}/{den} = ?/{new_den}. The denominator increased by ×{mult}, so the numerator also increases by ×{mult}: {num} × {mult} = {new_num}."
            
            distractors = [
                lambda n=new_num: str(n + 1),
                lambda n=new_num: str(n - 1) if n > 1 else str(n + 2),
                lambda n=new_num: str(n + 2),
                lambda d=new_den, o=den: str(d - o),
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 3: Simplifying Fractions (Foundation) - 75% Visual
# =============================================================================

def generate_level_3():
    """Simplify fractions to lowest terms"""
    questions = []
    
    # Type 1: Simplify with visual context
    simplifiable = []
    for n in range(2, 24):
        for d in range(n + 1, 30):
            g = gcd(n, d)
            if g > 1:
                simplifiable.append((n, d, g))
    
    random.shuffle(simplifiable)
    
    contexts = [
        ("A rectangle is divided into {} squares, with {} shaded. Write the shaded fraction in its simplest form.", "rectangle"),
        ("In a bag of {} marbles, {} are red. What fraction are red? Give your answer in simplest form.", "marbles"),
        ("Out of {} students, {} chose pizza. What fraction chose pizza? Simplify your answer.", "students"),
        ("{} out of {} questions were answered correctly. Write this as a fraction in lowest terms.", "questions"),
    ]
    
    for num, den, g in simplifiable[:35]:
        sn, sd = simplify_fraction(num, den)
        context_template, context_type = random.choice(contexts)
        
        if context_type == "questions":
            q_text = context_template.format(num, den)
        else:
            q_text = context_template.format(den, num)
        
        answer = fraction_str(sn, sd)
        explanation = f"To simplify {num}/{den}, find the highest common factor (HCF) of {num} and {den}. HCF = {g}. Divide both by {g}: {num}÷{g}/{den}÷{g} = {sn}/{sd}."
        
        distractors = [
            lambda n=num, d=den: fraction_str(n, d),
            lambda s=sn, t=sd: fraction_str(s + 1, t),
            lambda s=sn, t=sd: fraction_str(s, t + 1),
            lambda s=sn, t=sd: fraction_str(t, s) if s != 0 else "1/1",
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
    
    # Type 2: Time as fraction (SEC 2024 OL style)
    time_fractions = [
        (15, 60, "15 minutes", "one hour"),
        (20, 60, "20 minutes", "one hour"),
        (30, 60, "30 minutes", "one hour"),
        (45, 60, "45 minutes", "one hour"),
        (10, 60, "10 minutes", "one hour"),
        (40, 60, "40 minutes", "one hour"),
        (12, 60, "12 minutes", "one hour"),
        (24, 60, "24 minutes", "one hour"),
        (6, 60, "6 minutes", "one hour"),
        (36, 60, "36 minutes", "one hour"),
    ]
    
    for num, den, time_str, unit in time_fractions:
        sn, sd = simplify_fraction(num, den)
        g = gcd(num, den)
        q_text = f"Write {time_str} as a fraction of {unit}. Give your answer in its simplest form."
        answer = fraction_str(sn, sd)
        explanation = f"{time_str} out of 60 minutes (1 hour) = {num}/60. Simplify by dividing both by {g}: {num}÷{g}/60÷{g} = {sn}/{sd}."
        
        distractors = [
            lambda n=num, d=den: fraction_str(n, d),
            lambda s=sn, t=sd: fraction_str(s + 1, t),
            lambda s=sn, t=sd: fraction_str(s, t - 1) if t > 2 else fraction_str(s, t + 1),
            lambda n=num: f"{n}/100",
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 4: Same Denominator Add/Subtract (Foundation) - 75% Visual
# =============================================================================

def generate_level_4():
    """Add and subtract fractions with same denominator"""
    questions = []
    
    # Type 1: Visual addition
    items = [('pizza', 'of a'), ('cake', 'of a'), ('pie', 'of a'), ('chocolate bar', 'of a')]
    for item, prep in items:
        for den in [4, 5, 6, 8, 10, 12]:
            for n1 in range(1, den - 1):
                for n2 in range(1, den - n1):
                    if n1 + n2 < den:
                        result_num = n1 + n2
                        name1 = random.choice(['Emma', 'Sarah', 'Tom', 'Jack'])
                        name2 = random.choice(['Lily', 'Ben', 'Amy', 'Dan'])
                        
                        q_text = f"{name1} eats {n1}/{den} {prep} {item}. {name2} eats {n2}/{den} of the same {item}. What fraction have they eaten altogether?"
                        answer = fraction_str(result_num, den)
                        explanation = f"When denominators are the same, add the numerators: {n1}/{den} + {n2}/{den} = ({n1}+{n2})/{den} = {result_num}/{den}"
                        sn, sd = simplify_fraction(result_num, den)
                        if (sn, sd) != (result_num, den):
                            explanation += f" = {sn}/{sd} in simplest form."
                        else:
                            explanation += "."
                        
                        distractors = [
                            lambda a=n1, b=n2, d=den: fraction_str(a + b, d + d),
                            lambda r=result_num, d=den: fraction_str(r + 1, d),
                            lambda r=result_num, d=den: fraction_str(r, d + 1),
                            lambda a=n1, b=n2, d=den: fraction_str(a * b, d),
                        ]
                        
                        result = create_question_with_explanation(q_text, answer, explanation, distractors)
                        if result:
                            questions.append(result)
    
    # Type 2: Visual subtraction
    containers = ['tank', 'jar', 'bottle', 'bucket']
    for container in containers:
        for den in [4, 5, 6, 8, 10]:
            for n1 in range(3, den):
                for n2 in range(1, n1 - 1):
                    result_num = n1 - n2
                    q_text = f"A {container} is {n1}/{den} full. After {n2}/{den} is used, what fraction remains?"
                    answer = fraction_str(result_num, den)
                    explanation = f"Subtract the fractions: {n1}/{den} - {n2}/{den} = ({n1}-{n2})/{den} = {result_num}/{den}"
                    sn, sd = simplify_fraction(result_num, den)
                    if (sn, sd) != (result_num, den):
                        explanation += f" = {sn}/{sd} in simplest form."
                    else:
                        explanation += "."
                    
                    distractors = [
                        lambda r=result_num, d=den: fraction_str(r + 1, d),
                        lambda a=n1, b=n2, d=den: fraction_str(a + b, d),
                        lambda r=result_num, d=den: fraction_str(r, d - 1) if d > 2 else fraction_str(r, d + 1),
                        lambda a=n1, d=den: fraction_str(d - a, d),
                    ]
                    
                    result = create_question_with_explanation(q_text, answer, explanation, distractors)
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
    
    # Pairs where one denominator is a multiple of the other
    pairs = [
        (2, 4), (2, 6), (2, 8), (2, 10),
        (3, 6), (3, 9), (3, 12),
        (4, 8), (4, 12),
        (5, 10), (5, 15),
    ]
    
    # Type 1: SEC exact style
    for d1, d2 in pairs:
        for n1 in range(1, d1):
            for n2 in range(1, d2):
                common_d = lcm(d1, d2)
                mult1 = common_d // d1
                mult2 = common_d // d2
                new_n1 = n1 * mult1
                new_n2 = n2 * mult2
                result_n = new_n1 + new_n2
                
                q_text = f"Write the following as a single fraction in its simplest form:\n{n1}/{d1} + {n2}/{d2}"
                answer = fraction_str(result_n, common_d)
                explanation = f"Find a common denominator: LCD of {d1} and {d2} is {common_d}.\n{n1}/{d1} = {new_n1}/{common_d} and {n2}/{d2} = {new_n2}/{common_d}.\nAdd: {new_n1}/{common_d} + {new_n2}/{common_d} = {result_n}/{common_d}"
                sn, sd = simplify_fraction(result_n, common_d)
                if (sn, sd) != (result_n, common_d):
                    explanation += f" = {sn}/{sd} in simplest form."
                else:
                    explanation += "."
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                    lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=common_d: fraction_str(r, d + 1),
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, max(c, e)),
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: Visual context - journey
    journey_verbs = ['cycles', 'walks', 'runs', 'drives']
    for d1, d2 in [(2, 4), (3, 6), (2, 6), (4, 8)]:
        for n1 in range(1, d1):
            for n2 in range(1, d2):
                common_d = lcm(d1, d2)
                result_n = n1 * (common_d // d1) + n2 * (common_d // d2)
                name = random.choice(['Sarah', 'Tom', 'Emma', 'Jack'])
                verb = random.choice(journey_verbs)
                
                q_text = f"{name} {verb} {n1}/{d1} of their journey in the morning and {n2}/{d2} in the afternoon. What fraction of the journey is completed? Give your answer in simplest form."
                answer = fraction_str(result_n, common_d)
                explanation = f"Common denominator of {d1} and {d2} is {common_d}. Convert: {n1}/{d1} = {n1 * (common_d // d1)}/{common_d}, {n2}/{d2} = {n2 * (common_d // d2)}/{common_d}. Add: {n1 * (common_d // d1) + n2 * (common_d // d2)}/{common_d}"
                sn, sd = simplify_fraction(result_n, common_d)
                if (sn, sd) != (result_n, common_d):
                    explanation += f" = {sn}/{sd}."
                else:
                    explanation += "."
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                    lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=common_d: fraction_str(r - 1, d) if r > 1 else fraction_str(r + 2, d),
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c * e),
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
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
        (6, 7), (7, 8),
    ]
    
    # Type 1: SEC style - addition
    for d1, d2 in pairs:
        for n1 in range(1, d1):
            for n2 in range(1, d2):
                common_d = lcm(d1, d2)
                mult1 = common_d // d1
                mult2 = common_d // d2
                new_n1 = n1 * mult1
                new_n2 = n2 * mult2
                result_n = new_n1 + new_n2
                
                q_text = f"Write the following as a single fraction in its simplest form:\n{n1}/{d1} + {n2}/{d2}"
                answer = fraction_str(result_n, common_d)
                explanation = f"LCD of {d1} and {d2} is {common_d}.\n{n1}/{d1} × {mult1}/{mult1} = {new_n1}/{common_d}\n{n2}/{d2} × {mult2}/{mult2} = {new_n2}/{common_d}\nAdd: {new_n1} + {new_n2} = {result_n}, so answer is {result_n}/{common_d}"
                sn, sd = simplify_fraction(result_n, common_d)
                if (sn, sd) != (result_n, common_d):
                    explanation += f" = {sn}/{sd}."
                else:
                    explanation += "."
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c * e),
                    lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=common_d: fraction_str(r - 1, d) if r > 1 else fraction_str(r + 2, d),
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: SEC style - subtraction
    for d1, d2 in pairs[:10]:
        n1 = d1 - 1
        n2 = 1
        common_d = lcm(d1, d2)
        val1 = n1 * (common_d // d1)
        val2 = n2 * (common_d // d2)
        result_n = val1 - val2
        
        if result_n > 0:
            q_text = f"Write the following as a single fraction in its simplest form:\n{n1}/{d1} − {n2}/{d2}"
            answer = fraction_str(result_n, common_d)
            explanation = f"LCD of {d1} and {d2} is {common_d}. Convert both fractions, then subtract numerators: {val1}/{common_d} - {val2}/{common_d} = {result_n}/{common_d}"
            sn, sd = simplify_fraction(result_n, common_d)
            if (sn, sd) != (result_n, common_d):
                explanation += f" = {sn}/{sd}."
            else:
                explanation += "."
            
            distractors = [
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(abs(a - b), abs(c - e)) if c != e else fraction_str(abs(a - b), c),
                lambda r=result_n, d=common_d: fraction_str(r + 1, d),
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                lambda r=result_n, d=common_d: fraction_str(r, d + 1),
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 7: Multiply Fractions (Ordinary) - 75% Visual
# =============================================================================

def generate_level_7():
    """Multiply fractions"""
    questions = []
    
    fractions = [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5),
                 (1,6), (5,6), (2,7), (3,7), (3,8), (5,8)]
    
    # Type 1: "Fraction of a fraction" visual
    items = ['pizza', 'cake', 'chocolate bar', 'pie']
    for f1 in fractions[:8]:
        for f2 in fractions[:8]:
            n1, d1 = f1
            n2, d2 = f2
            result_n = n1 * n2
            result_d = d1 * d2
            
            item = random.choice(items)
            name = random.choice(['Emma', 'Tom', 'Sarah', 'Jack'])
            q_text = f"{n1}/{d1} of a {item} remains. {name} eats {n2}/{d2} of what's left. What fraction of the whole {item} did {name} eat? Give your answer in simplest form."
            answer = fraction_str(result_n, result_d)
            explanation = f"'Of' means multiply. {n2}/{d2} of {n1}/{d1} = {n2}/{d2} × {n1}/{d1} = ({n2}×{n1})/({d2}×{d1}) = {result_n}/{result_d}"
            sn, sd = simplify_fraction(result_n, result_d)
            if (sn, sd) != (result_n, result_d):
                explanation += f" = {sn}/{sd}."
            else:
                explanation += "."
            
            distractors = [
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * e, b * c),
                lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Pure calculation
    for f1 in fractions[4:]:
        for f2 in fractions[4:]:
            n1, d1 = f1
            n2, d2 = f2
            result_n = n1 * n2
            result_d = d1 * d2
            
            q_text = f"Calculate {n1}/{d1} × {n2}/{d2}. Give your answer in its simplest form."
            answer = fraction_str(result_n, result_d)
            explanation = f"Multiply numerators: {n1} × {n2} = {result_n}. Multiply denominators: {d1} × {d2} = {result_d}. Result: {result_n}/{result_d}"
            sn, sd = simplify_fraction(result_n, result_d)
            if (sn, sd) != (result_n, result_d):
                explanation += f" = {sn}/{sd}."
            else:
                explanation += "."
            
            distractors = [
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a + b, c + e),
                lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * b + 1, c * e),
                lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 8: Divide Fractions (Ordinary) - 75% Visual
# =============================================================================

def generate_level_8():
    """Divide fractions"""
    questions = []
    
    fractions = [(1,2), (1,3), (2,3), (1,4), (3,4), (1,5), (2,5), (3,5),
                 (1,6), (5,6), (2,7), (3,8), (5,8)]
    
    # Type 1: "How many fit" visual
    items = ['pizza', 'cake', 'ribbon', 'rope', 'chocolate bar']
    for f1 in fractions[:8]:
        for f2 in fractions[:6]:
            if f1 != f2:
                n1, d1 = f1
                n2, d2 = f2
                result_n = n1 * d2
                result_d = d1 * n2
                
                item = random.choice(items)
                q_text = f"A {item} is {n1}/{d1} of its original size. It is cut into pieces that are each {n2}/{d2} of the original. How many pieces can be made? Give your answer as a fraction in simplest form."
                answer = fraction_str(result_n, result_d)
                explanation = f"Divide: {n1}/{d1} ÷ {n2}/{d2} = {n1}/{d1} × {d2}/{n2} (flip and multiply) = {result_n}/{result_d}"
                sn, sd = simplify_fraction(result_n, result_d)
                if (sn, sd) != (result_n, result_d):
                    explanation += f" = {sn}/{sd}."
                else:
                    explanation += "."
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * b, c * e),
                    lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a - b, c - e) if c != e and a != b else fraction_str(a + b, c + e),
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
                if result:
                    questions.append(result)
    
    # Type 2: Pure calculation
    for f1 in fractions:
        for f2 in fractions:
            if f1 != f2:
                n1, d1 = f1
                n2, d2 = f2
                result_n = n1 * d2
                result_d = d1 * n2
                
                q_text = f"Calculate {n1}/{d1} ÷ {n2}/{d2}. Give your answer in its simplest form."
                answer = fraction_str(result_n, result_d)
                explanation = f"To divide fractions, flip the second fraction and multiply: {n1}/{d1} ÷ {n2}/{d2} = {n1}/{d1} × {d2}/{n2} = {result_n}/{result_d}"
                sn, sd = simplify_fraction(result_n, result_d)
                if (sn, sd) != (result_n, result_d):
                    explanation += f" = {sn}/{sd}."
                else:
                    explanation += "."
                
                distractors = [
                    lambda a=n1, b=n2, c=d1, e=d2: fraction_str(a * b, c * e),
                    lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                    lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
                    lambda r=result_n, d=result_d: fraction_str(r, d + 1),
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
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
    
    # Type 1: SEC style ratio problems
    ratio_problems = [
        (4, 21, 450, "fruit", "yoghurt", "g", "carton"),
        (2, 5, 350, "sugar", "flour", "g", "mixture"),
        (3, 7, 200, "water", "concentrate", "ml", "drink"),
        (1, 4, 250, "cream", "milk", "ml", "recipe"),
        (2, 3, 300, "red paint", "blue paint", "ml", "mixture"),
        (3, 5, 400, "boys", "girls", "students", "class"),
        (5, 8, 520, "adults", "children", "people", "group"),
        (1, 3, 240, "savings", "spending", "euro", "budget"),
    ]
    
    for r1, r2, total, item1, item2, unit, container in ratio_problems:
        total_parts = r1 + r2
        amount1 = (total * r1) // total_parts
        if amount1 == total * r1 / total_parts:
            q_text = f"A {container} contains {item1} and {item2}. The ratio of {item1} to {item2} is {r1}:{r2}. The total is {total} {unit}. How many {unit} of {item1} are there?"
            answer = str(amount1)
            explanation = f"Total parts = {r1} + {r2} = {total_parts}. Each part = {total} ÷ {total_parts} = {total // total_parts} {unit}. {item1.capitalize()} = {r1} parts = {r1} × {total // total_parts} = {amount1} {unit}."
            
            amount2 = total - amount1
            distractors = [
                lambda a2=amount2: str(a2),
                lambda a1=amount1: str(a1 + 10),
                lambda a1=amount1: str(a1 - 10) if a1 > 10 else str(a1 + 20),
                lambda t=total, r=r1: str(t // r) if r != 0 else str(t),
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Ratio to fraction
    for r1, r2 in [(4, 6), (6, 9), (8, 12), (10, 15), (12, 16), (15, 20), (9, 12), (6, 8)]:
        g = gcd(r1, r2)
        s1, s2 = r1 // g, r2 // g
        total = s1 + s2
        q_text = f"In a class, the ratio of boys to girls is {r1}:{r2}. What fraction of the class are boys? Give your answer in simplest form."
        answer = fraction_str(s1, total)
        explanation = f"Simplify ratio {r1}:{r2} = {s1}:{s2}. Total parts = {total}. Boys = {s1} parts out of {total} = {s1}/{total}."
        
        distractors = [
            lambda a=r1, b=r2: fraction_str(a, b),
            lambda a=s1, t=total: fraction_str(a + 1, t),
            lambda a=s2, t=total: fraction_str(a, t),
            lambda a=r1, b=r2: fraction_str(a, a + b),
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Pie chart fractions (SEC 2024 OL style)
    subjects = ['Maths', 'Science', 'History', 'English', 'Art', 'Music', 'PE', 'Geography']
    for total in [12, 24, 30, 36, 40]:
        for count in range(total // 6, total // 2):
            if gcd(count, total) > 1:
                sn, sd = simplify_fraction(count, total)
                subject = random.choice(subjects)
                q_text = f"A survey of {total} students asked about their favourite subject. {count} students chose {subject}. What fraction chose {subject}? Give your answer in simplest form."
                answer = fraction_str(sn, sd)
                g = gcd(count, total)
                explanation = f"{count} out of {total} = {count}/{total}. Simplify by dividing both by {g}: {count}÷{g}/{total}÷{g} = {sn}/{sd}."
                
                distractors = [
                    lambda c=count, t=total: fraction_str(c, t),
                    lambda s=sn, d=sd: fraction_str(s + 1, d),
                    lambda c=count, t=total: fraction_str(t - c, t),
                    lambda s=sn, d=sd: fraction_str(d, s) if s != 0 else "1/1",
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
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
    
    # Type 1: Calculate slope from two points
    point_pairs = [
        ((0, 0), (3, 2)), ((1, 1), (4, 3)), ((0, 3), (6, 7)),
        ((2, 1), (5, 4)), ((-1, 2), (2, 5)), ((0, -1), (4, 2)),
        ((3, -1), (-4, 2)), ((1, 2), (5, 6)), ((0, 1), (3, 4)),
        ((2, 3), (8, 6)), ((-2, 1), (4, 4)), ((0, 5), (10, 0)),
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
            explanation = f"Slope = rise/run = (y₂ - y₁)/(x₂ - x₁) = ({y2} - {y1})/({x2} - {x1}) = {rise}/{run}"
            if (sn, sd) != (rise, run):
                explanation += f" = {sn}/{sd}."
            else:
                explanation += "."
            
            distractors = [
                lambda r=rise, n=run: fraction_str(n, r) if r != 0 else "0",
                lambda s=sn, d=sd: fraction_str(s + 1, d),
                lambda s=sn, d=sd: fraction_str(-s, d),
                lambda s=sn, d=sd: fraction_str(s, d + 1),
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Trigonometry ratios as fractions (SEC 2022-2025 OL)
    trig_triangles = [
        (3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10),
        (9, 12, 15), (10, 24, 26), (12, 16, 20), (7, 24, 25),
    ]
    
    for opp, adj, hyp in trig_triangles:
        # sin = opp/hyp
        sn, sd = simplify_fraction(opp, hyp)
        q_text = f"In a right-angled triangle, the side opposite angle A is {opp} cm and the hypotenuse is {hyp} cm. Write sin A as a fraction in its simplest form."
        answer = fraction_str(sn, sd)
        explanation = f"sin A = opposite/hypotenuse = {opp}/{hyp}"
        if (sn, sd) != (opp, hyp):
            explanation += f" = {sn}/{sd}."
        else:
            explanation += "."
        
        distractors = [
            lambda o=opp, h=hyp: fraction_str(h, o),
            lambda o=opp, a=adj: fraction_str(o, a),
            lambda a=adj, h=hyp: fraction_str(a, h),
            lambda s=sn, d=sd: fraction_str(s + 1, d),
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
        
        # cos = adj/hyp
        sn, sd = simplify_fraction(adj, hyp)
        q_text = f"In a right-angled triangle, the side adjacent to angle A is {adj} cm and the hypotenuse is {hyp} cm. Write cos A as a fraction in its simplest form."
        answer = fraction_str(sn, sd)
        explanation = f"cos A = adjacent/hypotenuse = {adj}/{hyp}"
        if (sn, sd) != (adj, hyp):
            explanation += f" = {sn}/{sd}."
        else:
            explanation += "."
        
        distractors = [
            lambda a=adj, h=hyp: fraction_str(h, a),
            lambda o=opp, h=hyp: fraction_str(o, h),
            lambda o=opp, a=adj: fraction_str(o, a),
            lambda s=sn, d=sd: fraction_str(s + 1, d),
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
        
        # tan = opp/adj
        sn, sd = simplify_fraction(opp, adj)
        q_text = f"In a right-angled triangle, the side opposite angle A is {opp} cm and the adjacent side is {adj} cm. Write tan A as a fraction in its simplest form."
        answer = fraction_str(sn, sd)
        explanation = f"tan A = opposite/adjacent = {opp}/{adj}"
        if (sn, sd) != (opp, adj):
            explanation += f" = {sn}/{sd}."
        else:
            explanation += "."
        
        distractors = [
            lambda o=opp, a=adj: fraction_str(a, o),
            lambda o=opp, h=hyp: fraction_str(o, h),
            lambda a=adj, h=hyp: fraction_str(a, h),
            lambda s=sn, d=sd: fraction_str(s + 1, d),
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 11: Fraction-Decimal-Percentage Conversion (Higher) - 50% Visual
# =============================================================================

def generate_level_11():
    """Convert between fractions, decimals, and percentages"""
    questions = []
    
    conversions = [
        (1, 2, 0.5, 50), (1, 4, 0.25, 25), (3, 4, 0.75, 75),
        (1, 5, 0.2, 20), (2, 5, 0.4, 40), (3, 5, 0.6, 60), (4, 5, 0.8, 80),
        (1, 8, 0.125, 12.5), (3, 8, 0.375, 37.5), (5, 8, 0.625, 62.5),
        (1, 10, 0.1, 10), (3, 10, 0.3, 30), (7, 10, 0.7, 70), (9, 10, 0.9, 90),
        (1, 20, 0.05, 5), (1, 25, 0.04, 4),
    ]
    
    # Type 1: Fraction to decimal
    for n, d, dec, pct in conversions:
        q_text = f"Convert {n}/{d} to a decimal."
        answer = str(dec)
        explanation = f"{n}/{d} means {n} ÷ {d} = {dec}."
        
        distractors = [
            lambda x=dec: str(round(x + 0.1, 3)),
            lambda x=dec: str(round(x - 0.1, 3)) if x > 0.1 else str(round(x + 0.2, 3)),
            lambda x=dec: str(round(x * 10, 1)),
            lambda nn=n, dd=d: str(round(dd / nn, 2)) if nn != 0 else "1",
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
    
    # Type 2: Decimal to fraction
    for n, d, dec, pct in conversions:
        q_text = f"Convert {dec} to a fraction in its simplest form."
        answer = fraction_str(n, d)
        if dec == 0.5:
            explanation = f"{dec} = 5/10 = 1/2."
        elif dec < 1:
            mult = 10 if dec * 10 == int(dec * 10) else 100 if dec * 100 == int(dec * 100) else 1000
            explanation = f"{dec} = {int(dec * mult)}/{mult} = {n}/{d} in simplest form."
        else:
            explanation = f"{dec} = {n}/{d}."
        
        distractors = [
            lambda nn=n, dd=d: fraction_str(nn + 1, dd),
            lambda nn=n, dd=d: fraction_str(nn, dd + 1),
            lambda nn=n, dd=d: fraction_str(dd, nn) if nn != 0 else "1/1",
            lambda nn=n, dd=d: fraction_str(nn * 2, dd * 2),
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
    
    # Type 3: Fraction to percentage
    for n, d, dec, pct in conversions:
        pct_str = f"{pct}%" if isinstance(pct, int) else f"{pct}%"
        q_text = f"Convert {n}/{d} to a percentage."
        answer = pct_str
        explanation = f"{n}/{d} = {dec} = {dec} × 100% = {pct}%."
        
        distractors = [
            lambda p=pct: f"{int(p) + 10}%" if isinstance(p, int) else f"{p + 5}%",
            lambda p=pct: f"{int(p) - 10}%" if p > 10 else f"{int(p) + 20}%",
            lambda p=pct: f"{int(p) * 2}%" if p <= 50 else f"{int(p) // 2}%",
            lambda nn=n, dd=d: f"{nn * 10}%",
        ]
        
        result = create_question_with_explanation(q_text, answer, explanation, distractors)
        if result:
            questions.append(result)
    
    # Type 4: Percentage to fraction
    for n, d, dec, pct in conversions[:12]:
        if isinstance(pct, int):
            q_text = f"Convert {pct}% to a fraction in its simplest form."
            answer = fraction_str(n, d)
            explanation = f"{pct}% = {pct}/100 = {n}/{d} in simplest form."
            
            distractors = [
                lambda p=pct: fraction_str(p, 100),
                lambda nn=n, dd=d: fraction_str(nn + 1, dd),
                lambda nn=n, dd=d: fraction_str(nn, dd * 2),
                lambda nn=n, dd=d: fraction_str(nn * 2, dd),
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]

# =============================================================================
# LEVEL 12: Probability & Complex Problems (Higher) - 50% Visual
# =============================================================================

def generate_level_12():
    """Probability as fractions & complex problems"""
    questions = []
    
    # Type 1: Basic probability
    for total in [6, 8, 10, 12, 20]:
        for favorable in range(1, min(total // 2, 6)):
            sn, sd = simplify_fraction(favorable, total)
            item = random.choice(['ball', 'marble', 'counter', 'card'])
            color = random.choice(['red', 'blue', 'green', 'yellow'])
            
            q_text = f"A bag contains {total} {item}s. {favorable} are {color}. One {item} is picked at random. What is the probability of picking a {color} {item}? Give your answer as a fraction in simplest form."
            answer = fraction_str(sn, sd)
            explanation = f"Probability = favorable outcomes / total outcomes = {favorable}/{total}"
            if (sn, sd) != (favorable, total):
                explanation += f" = {sn}/{sd}."
            else:
                explanation += "."
            
            distractors = [
                lambda f=favorable, t=total: fraction_str(t - f, t),
                lambda s=sn, d=sd: fraction_str(s + 1, d),
                lambda s=sn, d=sd: fraction_str(d, s) if s != 0 else "1/1",
                lambda f=favorable, t=total: fraction_str(f, t + 1),
            ]
            
            result = create_question_with_explanation(q_text, answer, explanation, distractors)
            if result:
                questions.append(result)
    
    # Type 2: Multi-step problems (FIXED CONTEXT)
    multi_step_contexts = [
        ("A school has {total} students", "{n1}/{d1} are in sports clubs", "{n2}/{d2} play football", "How many students play football?"),
        ("A company has {total} employees", "{n1}/{d1} work part-time", "{n2}/{d2} work weekends", "How many employees work weekends?"),
        ("A library has {total} books", "{n1}/{d1} are fiction", "{n2}/{d2} are mysteries", "How many books are mysteries?"),
        ("A farm has {total} animals", "{n1}/{d1} are sheep", "{n2}/{d2} are lambs", "How many are lambs?"),
    ]
    
    for total in [120, 180, 240, 300]:
        for n1, d1 in [(1, 3), (1, 4), (2, 5), (3, 4)]:
            for n2, d2 in [(1, 2), (1, 3), (2, 3)]:
                first_part = (total * n1) // d1
                if first_part == total * n1 / d1:
                    second_part = (first_part * n2) // d2
                    if second_part == first_part * n2 / d2:
                        ctx = random.choice(multi_step_contexts)
                        part1 = ctx[0].format(total=total)
                        part2 = ctx[1].format(n1=n1, d1=d1)
                        part3 = ctx[2].format(n2=n2, d2=d2)
                        question_end = ctx[3]
                        
                        q_text = f"{part1}. {part2}. Of those, {part3}. {question_end}"
                        answer = str(second_part)
                        explanation = f"Step 1: {n1}/{d1} of {total} = {total} × {n1}/{d1} = {first_part}.\nStep 2: {n2}/{d2} of {first_part} = {first_part} × {n2}/{d2} = {second_part}."
                        
                        distractors = [
                            lambda f=first_part: str(f),
                            lambda s=second_part: str(s + 5),
                            lambda s=second_part: str(s - 5) if s > 5 else str(s + 10),
                            lambda t=total, s=second_part: str(t - s),
                        ]
                        
                        result = create_question_with_explanation(q_text, answer, explanation, distractors)
                        if result:
                            questions.append(result)
    
    # Type 3: Combined operations
    for n1, d1 in [(1, 2), (1, 3), (2, 3)]:
        for n2, d2 in [(1, 4), (1, 3), (1, 2)]:
            for n3, d3 in [(1, 2), (1, 3)]:
                common_d = lcm(d1, d2)
                sum_n = n1 * (common_d // d1) + n2 * (common_d // d2)
                result_n = sum_n * n3
                result_d = common_d * d3
                
                q_text = f"Calculate ({n1}/{d1} + {n2}/{d2}) × {n3}/{d3}. Give your answer in simplest form."
                answer = fraction_str(result_n, result_d)
                explanation = f"Step 1: {n1}/{d1} + {n2}/{d2} = {sum_n}/{common_d}.\nStep 2: {sum_n}/{common_d} × {n3}/{d3} = {result_n}/{result_d}"
                sn, sd = simplify_fraction(result_n, result_d)
                if (sn, sd) != (result_n, result_d):
                    explanation += f" = {sn}/{sd}."
                else:
                    explanation += "."
                
                distractors = [
                    lambda r=result_n, d=result_d: fraction_str(r + 1, d),
                    lambda a=n1, b=n2, c=n3, x=d1, y=d2, z=d3: fraction_str(a + b + c, x + y + z),
                    lambda r=result_n, d=result_d: fraction_str(d, r) if r != 0 else "1/1",
                    lambda r=result_n, d=result_d: fraction_str(r * 2, d * 2),
                ]
                
                result = create_question_with_explanation(q_text, answer, explanation, distractors)
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
    
    for q_text, options, correct_idx, explanation in questions:
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
                VALUES (?, ?, ?, ?, 'multiple_choice', ?, ?, ?, ?, ?, ?, 1, 'jc_exam')
            """, (
                'fractions',
                level,
                difficulty_band,
                q_text,
                options[0], options[1], options[2], options[3],
                correct_idx,
                explanation
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
    print("JC SEC-ALIGNED FRACTIONS GENERATOR v5")
    print("Target: 50 questions × 12 levels = 600 questions")
    print("NEW: Step-by-step explanations for every question!")
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
        (1, generate_level_1, "Visual Fractions (Shapes/Parts)"),
        (2, generate_level_2, "Equivalent Fractions (Visual)"),
        (3, generate_level_3, "Simplifying + Time Fractions"),
        (4, generate_level_4, "Same Denom +/− (Context)"),
        (5, generate_level_5, "Different Denom Simple ★ Q10(a)"),
        (6, generate_level_6, "Different Denom Complex ★ Q10(a)"),
        (7, generate_level_7, "Multiply Fractions (Context)"),
        (8, generate_level_8, "Divide Fractions (Context)"),
        (9, generate_level_9, "Ratios & Pie Charts ★ SEC"),
        (10, generate_level_10, "Slope & Trig Fractions ★ SEC"),
        (11, generate_level_11, "Decimal/Percentage Conversion"),
        (12, generate_level_12, "Probability & Complex ★ Higher"),
    ]
    
    total_inserted = 0
    level_counts = {}
    
    for level, generator, description in generators:
        print(f"\n📝 Level {level}: {description}")
        questions = generator()
        print(f"   Generated: {len(questions)} questions")
        
        inserted = insert_questions(cursor, questions, level)
        level_counts[level] = inserted
        total_inserted += inserted
        print(f"   Inserted: {inserted} questions")
    
    conn.commit()
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    print("\n📊 Questions per Level:")
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        band = get_difficulty_band(level)
        bar = "█" * (count // 5) + "░" * ((50 - count) // 5)
        status = "✅" if count >= 45 else "⚠️" if count >= 30 else "❌"
        print(f"   Level {level:2d} ({band:10s}): {bar} {count:3d} {status}")
    
    print(f"\n✅ Total Questions Inserted: {total_inserted}")
    print("✅ All questions include step-by-step explanations!")
    
    # Verify
    cursor.execute("""
        SELECT COUNT(*) FROM questions_adaptive
        WHERE topic = 'fractions' AND mode = 'jc_exam' AND explanation != ''
    """)
    with_explanations = cursor.fetchone()[0]
    print(f"✅ Questions with explanations: {with_explanations}/{total_inserted}")
    
    conn.close()
    print("\n✅ Generation complete!")

if __name__ == '__main__':
    main()
