#!/usr/bin/env python3
"""
AgentMath - Arithmetic Question Generator
SEC-Aligned for Irish Junior Cycle Mathematics

Version: 1.0
Date: December 2025
Author: Barry (ICT Coordinator, Palmerstown Community School)

Generates 600 questions (50 per level × 12 levels)
- Levels 1-10: 75% contextual
- Levels 11-12: 50% contextual
- All questions include step-by-step explanations

Level Structure:
  1: Basic Addition (2-3 digit numbers)
  2: Basic Subtraction (2-3 digit numbers)
  3: Multiplication (whole numbers, decimals × whole)
  4: Division (simple division, remainders)
  5: Rounding (to nearest whole number, 10, 100)
  6: Midpoint / Halfway (number between two values)
  7: Factors (finding all factors, factor pairs)
  8: Multiples & LCM (listing multiples, LCM of two numbers)
  9: HCF (highest common factor)
  10: Powers & Indices (squares, cubes, index notation)
  11: Square Roots & Cube Roots
  12: Mixed Operations SEC Style (BODMAS with brackets, indices, roots)

SEC Question Sources (2022-2025):
  - 2022 OL Q1(a): 243+178, 7.2×6, 24÷(9-7), 3⁴
  - 2023 OL Q1(a): 372+119, 3.4×7, 42×(8-5)
  - 2024 OL Q1(a): 634+297, 4.8×6, 32÷(7-5)²
  - 2024 OL Q1(b): Factors of 8, 12, 16; HCF
  - 2025 OL Q1(a): 456-321, 7.4×6.2, √9×(7-3)
  - 2025 OL Q8: Even numbers, LCM of 12 and 15, factors of 36
"""

import sqlite3
import random
from typing import List, Tuple, Dict, Any
import math

# ==================== CONFIGURATION ====================
TOPIC = 'arithmetic'
QUESTIONS_PER_LEVEL = 65  # Generate extra to account for potential duplicates
TARGET_PER_LEVEL = 50     # Target after deduplication
DB_PATH = 'instance/mathquiz.db'  # Adjust for PythonAnywhere if needed

# Difficulty bands matching methodology
BANDS = {
    1: 'foundation', 2: 'foundation', 3: 'foundation',
    4: 'ordinary', 5: 'ordinary', 6: 'ordinary',
    7: 'ordinary', 8: 'ordinary',
    9: 'higher', 10: 'higher', 11: 'higher', 12: 'higher'
}

# ==================== CONTEXT DATA ====================
CONTEXTS = {
    'shopping': ['books', 'apples', 'pencils', 'sandwiches', 'tickets', 'stamps'],
    'school': ['students', 'desks', 'chairs', 'books', 'markers', 'pages'],
    'sports': ['points', 'goals', 'laps', 'metres', 'minutes', 'players'],
    'money': ['euro', 'cents', 'coins', 'notes'],
    'food': ['pizzas', 'slices', 'biscuits', 'sweets', 'oranges', 'eggs'],
    'transport': ['kilometres', 'buses', 'trains', 'passengers', 'stops'],
    'animals': ['cats', 'dogs', 'birds', 'fish', 'horses', 'sheep']
}

PEOPLE_NAMES = ['Emma', 'Liam', 'Aoife', 'Cian', 'Sophie', 'Jack', 'Niamh', 'Sean', 
                'Grace', 'Conor', 'Ella', 'Dylan', 'Ava', 'Oisin', 'Mia', 'Fionn',
                'Sarah', 'James', 'Katie', 'Ryan', 'Lucy', 'Adam', 'Holly', 'Ben',
                'Noah', 'Alice', 'Paul', 'Jael', 'Martin', 'Lily', 'Joshua', 'Rachel']

# ==================== HELPER FUNCTIONS ====================

def get_factors(n: int) -> List[int]:
    """Get all factors of n in ascending order"""
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def get_hcf(a: int, b: int) -> int:
    """Get highest common factor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def get_lcm(a: int, b: int) -> int:
    """Get lowest common multiple"""
    return abs(a * b) // get_hcf(a, b)

def generate_distractors(correct: int, count: int = 3, 
                          min_diff: int = 1, max_diff: int = 10) -> List[int]:
    """Generate plausible wrong answers"""
    distractors = set()
    attempts = 0
    
    while len(distractors) < count and attempts < 100:
        attempts += 1
        # Common error types
        error_type = random.choice(['add', 'subtract', 'near', 'off_by_10'])
        
        if error_type == 'add':
            d = correct + random.randint(min_diff, max_diff)
        elif error_type == 'subtract':
            d = correct - random.randint(min_diff, max_diff)
        elif error_type == 'near':
            d = correct + random.choice([-2, -1, 1, 2, 3])
        else:  # off_by_10
            d = correct + random.choice([-10, 10, -100, 100])
        
        if d > 0 and d != correct and d not in distractors:
            distractors.add(d)
    
    # Fill remaining with simple offsets if needed
    offset = 1
    while len(distractors) < count:
        d = correct + offset
        if d > 0 and d != correct and d not in distractors:
            distractors.add(d)
        offset = -offset if offset > 0 else -offset + 1
    
    return list(distractors)[:count]

def generate_decimal_distractors(correct: float, count: int = 3) -> List[float]:
    """Generate plausible wrong decimal answers"""
    distractors = set()
    
    # Common decimal errors
    errors = [0.1, -0.1, 0.2, -0.2, 1, -1, 0.5, -0.5, 0.01, -0.01]
    random.shuffle(errors)
    
    for err in errors:
        d = round(correct + err, 2)
        if d > 0 and d != correct and d not in distractors:
            distractors.add(d)
        if len(distractors) >= count:
            break
    
    return list(distractors)[:count]

def format_options(correct: Any, distractors: List[Any]) -> Tuple[List[str], int]:
    """Shuffle options and return (options_list, correct_index)"""
    options = [correct] + distractors
    random.shuffle(options)
    correct_idx = options.index(correct)
    return [str(opt) for opt in options], correct_idx

# ==================== LEVEL GENERATORS ====================

def generate_level_1() -> List[Dict]:
    """Level 1: Basic Addition (2-3 digit numbers)"""
    questions = []
    used = set()
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Generate unique problem
        attempts = 0
        while attempts < 100:
            attempts += 1
            a = random.randint(100, 999)
            b = random.randint(100, 999)
            key = (min(a, b), max(a, b))
            if key not in used:
                used.add(key)
                break
        
        correct = a + b
        distractors = generate_distractors(correct, 3, 1, 20)
        options, correct_idx = format_options(correct, distractors)
        
        # Contextual vs pure (75% contextual)
        if random.random() < 0.75:
            context = random.choice(list(CONTEXTS.keys()))
            item = random.choice(CONTEXTS[context])
            name1, name2 = random.sample(PEOPLE_NAMES, 2)
            
            question_text = f"{name1} has {a} {item} and {name2} has {b} {item}. How many {item} do they have altogether?"
            explanation = f"Add the two amounts:\n{a} + {b} = {correct}\nThey have {correct} {item} altogether."
        else:
            question_text = f"Find the value of: {a} + {b}"
            explanation = f"Add the numbers:\n{a} + {b} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_2() -> List[Dict]:
    """Level 2: Basic Subtraction (2-3 digit numbers)"""
    questions = []
    used = set()
    
    for i in range(QUESTIONS_PER_LEVEL):
        attempts = 0
        while attempts < 100:
            attempts += 1
            a = random.randint(200, 999)
            b = random.randint(100, a - 50)  # Ensure positive result
            key = (a, b)
            if key not in used:
                used.add(key)
                break
        
        correct = a - b
        distractors = generate_distractors(correct, 3, 1, 20)
        options, correct_idx = format_options(correct, distractors)
        
        if random.random() < 0.75:
            context = random.choice(list(CONTEXTS.keys()))
            item = random.choice(CONTEXTS[context])
            name = random.choice(PEOPLE_NAMES)
            
            question_text = f"{name} had {a} {item} and used {b} of them. How many {item} are left?"
            explanation = f"Subtract to find what's left:\n{a} - {b} = {correct}\n{name} has {correct} {item} left."
        else:
            question_text = f"Find the value of: {a} − {b}"
            explanation = f"Subtract the numbers:\n{a} - {b} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_3() -> List[Dict]:
    """Level 3: Multiplication (whole numbers, decimal × whole)"""
    questions = []
    used = set()
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Mix of whole number and decimal multiplication
        is_decimal = random.random() < 0.4
        
        attempts = 0
        while attempts < 100:
            attempts += 1
            if is_decimal:
                # SEC style: 7.2 × 6, 3.4 × 7, 4.8 × 6, 7.4 × 6.2
                a = round(random.uniform(2.0, 9.9), 1)
                b = random.randint(2, 9)
                key = (a, b)
            else:
                a = random.randint(10, 50)
                b = random.randint(2, 12)
                key = (min(a, b), max(a, b))
            
            if key not in used:
                used.add(key)
                break
        
        correct = round(a * b, 2) if is_decimal else a * b
        
        if is_decimal:
            distractors = generate_decimal_distractors(correct, 3)
            options, correct_idx = format_options(correct, distractors)
        else:
            distractors = generate_distractors(correct, 3, 1, 15)
            options, correct_idx = format_options(correct, distractors)
        
        if random.random() < 0.75:
            if is_decimal:
                item = random.choice(['litres of milk', 'kg of flour', 'metres of ribbon', 'litres of juice'])
                price = a
                qty = b
                question_text = f"A {item.split(' of ')[1] if ' of ' in item else item} costs €{price:.2f}. Find the cost of {qty} {item}."
                correct_str = f"€{correct:.2f}"
                explanation = f"Multiply price by quantity:\n€{price:.2f} × {qty} = €{correct:.2f}"
                options = [f"€{float(opt):.2f}" for opt in options]
            else:
                context = random.choice(['sports', 'school', 'food'])
                item = random.choice(CONTEXTS[context])
                question_text = f"There are {a} {item} in each group. How many {item} are there in {b} groups?"
                correct_str = str(correct)
                explanation = f"Multiply to find the total:\n{a} × {b} = {correct}"
        else:
            if is_decimal:
                question_text = f"Find the value of: {a} × {b}"
            else:
                question_text = f"Find the value of: {a} × {b}"
            explanation = f"Multiply the numbers:\n{a} × {b} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_4() -> List[Dict]:
    """Level 4: Division (simple division)"""
    questions = []
    used = set()
    
    for i in range(QUESTIONS_PER_LEVEL):
        attempts = 0
        while attempts < 100:
            attempts += 1
            # Ensure clean division
            b = random.randint(2, 12)
            result = random.randint(5, 50)
            a = b * result
            key = (a, b)
            if key not in used:
                used.add(key)
                break
        
        correct = a // b
        distractors = generate_distractors(correct, 3, 1, 10)
        options, correct_idx = format_options(correct, distractors)
        
        if random.random() < 0.75:
            context = random.choice(list(CONTEXTS.keys()))
            item = random.choice(CONTEXTS[context])
            name = random.choice(PEOPLE_NAMES)
            
            question_text = f"{name} shares {a} {item} equally among {b} people. How many {item} does each person get?"
            explanation = f"Divide the total by the number of people:\n{a} ÷ {b} = {correct}\nEach person gets {correct} {item}."
        else:
            question_text = f"Find the value of: {a} ÷ {b}"
            explanation = f"Divide:\n{a} ÷ {b} = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_5() -> List[Dict]:
    """Level 5: Rounding (to nearest whole number, 10, 100)"""
    questions = []
    used = set()
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Mix of rounding types
        rounding_type = random.choice(['whole', 'ten', 'hundred'])
        
        attempts = 0
        while attempts < 100:
            attempts += 1
            if rounding_type == 'whole':
                # SEC style: "Write down the whole number nearest to 15.8"
                decimal = round(random.uniform(10, 99) + random.choice([0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]), 1)
                correct = round(decimal)
                key = ('whole', decimal)
            elif rounding_type == 'ten':
                num = random.randint(11, 99)
                correct = round(num, -1)
                key = ('ten', num)
            else:  # hundred
                num = random.randint(101, 999)
                correct = round(num, -2)
                key = ('hundred', num)
            
            if key not in used:
                used.add(key)
                break
        
        distractors = generate_distractors(correct, 3, 1, 15)
        options, correct_idx = format_options(correct, distractors)
        
        if rounding_type == 'whole':
            question_text = f"Write down the whole number that is nearest to {decimal}."
            explanation = f"Look at the decimal part: {decimal}\nSince {str(decimal).split('.')[1]} is {'5 or more' if decimal % 1 >= 0.5 else 'less than 5'}, round {'up' if decimal % 1 >= 0.5 else 'down'}.\nThe nearest whole number is {correct}."
        elif rounding_type == 'ten':
            question_text = f"Round {num} to the nearest 10."
            ones_digit = num % 10
            explanation = f"Look at the ones digit: {ones_digit}\nSince {ones_digit} is {'5 or more' if ones_digit >= 5 else 'less than 5'}, round {'up' if ones_digit >= 5 else 'down'}.\n{num} rounded to the nearest 10 is {correct}."
        else:
            question_text = f"Round {num} to the nearest 100."
            tens_digit = (num % 100) // 10
            explanation = f"Look at the tens digit: {tens_digit}\nSince the tens digit is {'5 or more' if (num % 100) >= 50 else 'less than 5'}, round {'up' if (num % 100) >= 50 else 'down'}.\n{num} rounded to the nearest 100 is {correct}."
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_6() -> List[Dict]:
    """Level 6: Midpoint / Halfway (SEC style: 'halfway between')"""
    questions = []
    used = set()
    
    for i in range(QUESTIONS_PER_LEVEL):
        attempts = 0
        while attempts < 100:
            attempts += 1
            # Generate two even numbers for clean midpoint, or allow odd result
            a = random.randint(5, 100)
            b = random.randint(a + 4, a + 50)
            # Ensure clean midpoint (both even or both odd)
            if (a + b) % 2 != 0:
                b += 1
            key = (a, b)
            if key not in used:
                used.add(key)
                break
        
        correct = (a + b) // 2
        distractors = generate_distractors(correct, 3, 1, 10)
        options, correct_idx = format_options(correct, distractors)
        
        # SEC exact wording style
        if random.random() < 0.75:
            name = random.choice(PEOPLE_NAMES)
            context_type = random.choice(['age', 'score', 'money'])
            
            if context_type == 'age':
                question_text = f"{name}'s age is halfway between {a} and {b}. How old is {name}?"
                explanation = f"To find the number halfway between {a} and {b}:\nAdd them: {a} + {b} = {a+b}\nDivide by 2: {a+b} ÷ 2 = {correct}\n{name} is {correct} years old."
            elif context_type == 'score':
                question_text = f"A score halfway between {a} and {b} is needed to pass. What score is needed?"
                explanation = f"To find the number halfway between {a} and {b}:\nAdd them: {a} + {b} = {a+b}\nDivide by 2: {a+b} ÷ 2 = {correct}"
            else:
                question_text = f"The price is halfway between €{a} and €{b}. What is the price?"
                explanation = f"To find the number halfway between {a} and {b}:\nAdd them: {a} + {b} = {a+b}\nDivide by 2: {a+b} ÷ 2 = {correct}\nThe price is €{correct}."
        else:
            question_text = f"What number is halfway between {a} and {b}?"
            explanation = f"To find the number halfway between {a} and {b}:\nAdd them: {a} + {b} = {a+b}\nDivide by 2: {a+b} ÷ 2 = {correct}"
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_7() -> List[Dict]:
    """Level 7: Factors (finding all factors, counting factors)"""
    questions = []
    used = set()
    
    # Good numbers for factor questions
    good_numbers = [12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 42, 45, 48, 50, 54, 56, 60, 64, 72, 80, 90, 100]
    
    for i in range(QUESTIONS_PER_LEVEL):
        question_type = random.choice(['count', 'missing', 'identify'])
        
        attempts = 0
        while attempts < 100:
            attempts += 1
            n = random.choice(good_numbers)
            key = (question_type, n)
            if key not in used:
                used.add(key)
                break
        
        factors = get_factors(n)
        
        if question_type == 'count':
            correct = len(factors)
            distractors = generate_distractors(correct, 3, 1, 3)
            options, correct_idx = format_options(correct, distractors)
            question_text = f"How many factors does {n} have?"
            explanation = f"The factors of {n} are: {', '.join(map(str, factors))}\nCount them: {n} has {correct} factors."
        
        elif question_type == 'missing':
            # SEC style: "The number 36 has nine factors. Four are given. Fill in the remaining five."
            shown = random.sample(factors, min(4, len(factors) - 1))
            hidden = [f for f in factors if f not in shown]
            correct = random.choice(hidden)
            wrong_options = [f for f in range(1, n+1) if f not in factors][:10]
            distractors = random.sample(wrong_options, min(3, len(wrong_options)))
            while len(distractors) < 3:
                d = random.randint(1, n)
                if d not in factors and d not in distractors:
                    distractors.append(d)
            options, correct_idx = format_options(correct, distractors[:3])
            
            shown_str = ', '.join(map(str, sorted(shown)))
            question_text = f"The number {n} has {len(factors)} factors. Some factors are: {shown_str}. Which of the following is also a factor of {n}?"
            explanation = f"The factors of {n} are: {', '.join(map(str, factors))}\n{correct} divides evenly into {n} ({n} ÷ {correct} = {n//correct}), so {correct} is a factor."
        
        else:  # identify
            # Is X a factor of Y?
            test_num = random.choice([random.choice(factors), random.randint(2, n)])
            is_factor = test_num in factors
            correct = "Yes" if is_factor else "No"
            options = ["Yes", "No", f"Only if {n} is even", f"Only if {n} is odd"]
            random.shuffle(options)
            correct_idx = options.index(correct)
            question_text = f"Is {test_num} a factor of {n}?"
            if is_factor:
                explanation = f"Check: {n} ÷ {test_num} = {n//test_num}\nSince {n} divides evenly by {test_num}, yes, {test_num} IS a factor of {n}."
            else:
                explanation = f"Check: {n} ÷ {test_num} = {n/test_num:.2f}\nSince {n} doesn't divide evenly by {test_num}, no, {test_num} is NOT a factor of {n}."
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_8() -> List[Dict]:
    """Level 8: Multiples & LCM"""
    questions = []
    used_texts = set()  # Track actual question texts
    
    for i in range(QUESTIONS_PER_LEVEL):
        question_type = random.choice([
            'lcm_basic', 'lcm_word', 'multiple_identify', 'common_multiple',
            'first_common', 'lcm_context_buses', 'lcm_context_lights'
        ])
        
        attempts = 0
        while attempts < 200:
            attempts += 1
            a = random.randint(2, 20)
            b = random.randint(2, 20)
            if a == b:
                b += 1
            
            if question_type == 'lcm_basic':
                correct = get_lcm(a, b)
                question_text = f"Find the LCM (Lowest Common Multiple) of {a} and {b}."
                multiples_a = [a * i for i in range(1, 8)]
                multiples_b = [b * i for i in range(1, 8)]
                explanation = f"Multiples of {a}: {', '.join(map(str, multiples_a))}...\nMultiples of {b}: {', '.join(map(str, multiples_b))}...\nThe smallest number in both lists is {correct}.\nLCM of {a} and {b} = {correct}"
                
            elif question_type == 'lcm_word':
                correct = get_lcm(a, b)
                question_text = f"What is the lowest common multiple of {a} and {b}?"
                explanation = f"Find multiples of both numbers until you find a match.\nLCM({a}, {b}) = {correct}"
                
            elif question_type == 'multiple_identify':
                n = random.randint(3, 15)
                multiplier = random.randint(2, 12)
                correct = n * multiplier
                question_text = f"Which of the following is a multiple of {n}?"
                explanation = f"{correct} ÷ {n} = {multiplier} (exact)\nSo {correct} is a multiple of {n}."
                
            elif question_type == 'common_multiple':
                correct = get_lcm(a, b) * random.randint(1, 3)
                question_text = f"Which of the following is a common multiple of {a} and {b}?"
                explanation = f"A common multiple must be divisible by both {a} and {b}.\n{correct} ÷ {a} = {correct // a} ✓\n{correct} ÷ {b} = {correct // b} ✓"
                
            elif question_type == 'first_common':
                correct = get_lcm(a, b)
                question_text = f"What is the first (smallest) common multiple of {a} and {b}?"
                explanation = f"The smallest common multiple is the LCM.\nLCM({a}, {b}) = {correct}"
                
            elif question_type == 'lcm_context_buses':
                # Bus schedule problem
                a = random.choice([10, 12, 15, 20, 30])
                b = random.choice([8, 12, 15, 18, 20, 24])
                if a == b:
                    b = random.choice([6, 9, 14, 16])
                correct = get_lcm(a, b)
                question_text = f"Bus A arrives every {a} minutes and Bus B arrives every {b} minutes. If both arrive at 9:00 AM, after how many minutes will they next arrive together?"
                explanation = f"Find when both schedules align = LCM({a}, {b}) = {correct} minutes"
                
            else:  # lcm_context_lights
                a = random.choice([3, 4, 5, 6])
                b = random.choice([4, 5, 6, 7, 8])
                if a == b:
                    b += 1
                correct = get_lcm(a, b)
                question_text = f"One light flashes every {a} seconds, another every {b} seconds. If they flash together now, in how many seconds will they next flash together?"
                explanation = f"Find when both flash = LCM({a}, {b}) = {correct} seconds"
            
            if question_text not in used_texts:
                used_texts.add(question_text)
                break
        
        # Generate appropriate distractors
        if question_type == 'multiple_identify':
            wrong = []
            while len(wrong) < 3:
                w = random.randint(10, 100)
                if w % n != 0 and w not in wrong and w != correct:
                    wrong.append(w)
            options, correct_idx = format_options(correct, wrong)
        elif question_type == 'common_multiple':
            wrong = []
            while len(wrong) < 3:
                w = random.randint(max(a, b), correct * 2)
                if (w % a != 0 or w % b != 0) and w not in wrong and w != correct:
                    wrong.append(w)
            options, correct_idx = format_options(correct, wrong)
        else:
            distractors = [a * b, get_hcf(a, b), correct + a, correct - b]
            distractors = [d for d in distractors if d != correct and d > 0]
            while len(distractors) < 3:
                d = random.randint(max(a, b), correct + 20)
                if d != correct and d not in distractors:
                    distractors.append(d)
            options, correct_idx = format_options(correct, distractors[:3])
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_9() -> List[Dict]:
    """Level 9: HCF (Highest Common Factor)"""
    questions = []
    used = set()
    
    # Pairs with interesting HCFs
    good_pairs = [(8, 12), (12, 16), (12, 18), (15, 20), (18, 24), (20, 30), 
                  (24, 36), (16, 24), (14, 21), (18, 27), (21, 28), (24, 32),
                  (30, 45), (36, 48), (40, 60), (42, 56), (48, 64), (54, 72)]
    
    for i in range(QUESTIONS_PER_LEVEL):
        question_type = random.choice(['find_hcf', 'three_numbers', 'context'])
        
        attempts = 0
        while attempts < 100:
            attempts += 1
            if question_type == 'three_numbers':
                a, b = random.choice(good_pairs)
                c = get_hcf(a, b) * random.randint(2, 4)
                key = (question_type, tuple(sorted([a, b, c])))
            else:
                a, b = random.choice(good_pairs)
                key = (question_type, min(a, b), max(a, b))
            
            if key not in used:
                used.add(key)
                break
        
        if question_type == 'find_hcf':
            correct = get_hcf(a, b)
            # Common wrong answers: LCM, product, one of the numbers
            distractors = [get_lcm(a, b), min(a, b), max(a, b)]
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                d = random.randint(1, min(a, b))
                if d != correct and d not in distractors:
                    distractors.append(d)
            options, correct_idx = format_options(correct, distractors[:3])
            
            question_text = f"Find the HCF (Highest Common Factor) of {a} and {b}."
            factors_a = get_factors(a)
            factors_b = get_factors(b)
            common = sorted(set(factors_a) & set(factors_b))
            explanation = f"Factors of {a}: {', '.join(map(str, factors_a))}\nFactors of {b}: {', '.join(map(str, factors_b))}\nCommon factors: {', '.join(map(str, common))}\nThe highest common factor is {correct}."
        
        elif question_type == 'three_numbers':
            # SEC style: "HCF of 8, 12, and 16"
            correct = get_hcf(get_hcf(a, b), c)
            distractors = [get_lcm(a, get_lcm(b, c)), min(a, b, c), 1]
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                d = random.randint(1, min(a, b, c))
                if d != correct and d not in distractors:
                    distractors.append(d)
            options, correct_idx = format_options(correct, distractors[:3])
            
            nums = sorted([a, b, c])
            question_text = f"What is the highest common factor of {nums[0]}, {nums[1]}, and {nums[2]}?"
            explanation = f"Find factors common to all three numbers.\nThe factors that divide evenly into {nums[0]}, {nums[1]}, and {nums[2]} are limited.\nThe highest common factor is {correct}."
        
        else:  # context
            correct = get_hcf(a, b)
            distractors = generate_distractors(correct, 3, 1, 5)
            options, correct_idx = format_options(correct, distractors)
            
            name = random.choice(PEOPLE_NAMES)
            question_text = f"{name} has {a} red beads and {b} blue beads. She wants to make identical bags with the same number of each colour in each bag (no beads left over). What is the maximum number of bags she can make?"
            explanation = f"We need the HCF of {a} and {b} to find how many equal groups.\nHCF({a}, {b}) = {correct}\n{name} can make {correct} bags, each with {a//correct} red and {b//correct} blue beads."
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_10() -> List[Dict]:
    """Level 10: Powers & Indices (squares, cubes, index notation)"""
    questions = []
    used_texts = set()  # Track actual question texts
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Many question types for variety
        question_type = random.choice([
            'evaluate_power', 'square', 'cube', 'identify_square',
            'identify_cube', 'fourth_power', 'fifth_power',
            'square_add', 'square_subtract', 'square_diff',
            'power_mult', 'square_word_area', 'cube_word_volume'
        ])
        
        attempts = 0
        while attempts < 300:
            attempts += 1
            
            if question_type == 'evaluate_power':
                base = random.randint(2, 7)
                exp = random.randint(2, 5)
                correct = base ** exp
                superscript = ''.join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(d)] for d in str(exp)])
                question_text = f"Find the value of {base}{superscript}"
                explanation = f"{base}{superscript} means {base} multiplied by itself {exp} times\n= {' × '.join([str(base)] * exp)}\n= {correct}"
                
            elif question_type == 'square':
                base = random.randint(2, 25)
                correct = base ** 2
                question_text = f"Find the value of {base}²"
                explanation = f"{base}² means {base} × {base}\n= {correct}"
                
            elif question_type == 'cube':
                base = random.randint(2, 10)
                correct = base ** 3
                question_text = f"Find the value of {base}³"
                explanation = f"{base}³ means {base} × {base} × {base}\n= {base * base} × {base}\n= {correct}"
                
            elif question_type == 'identify_square':
                base = random.randint(2, 20)
                correct = base ** 2
                question_text = f"What is {base} squared?"
                explanation = f"{base} squared = {base}² = {base} × {base} = {correct}"
                
            elif question_type == 'identify_cube':
                base = random.randint(2, 9)
                correct = base ** 3
                question_text = f"What is {base} cubed?"
                explanation = f"{base} cubed = {base}³ = {base} × {base} × {base} = {correct}"
                
            elif question_type == 'fourth_power':
                base = random.randint(2, 5)
                correct = base ** 4
                question_text = f"Calculate {base}⁴"
                explanation = f"{base}⁴ = {base} × {base} × {base} × {base}\n= {base**2} × {base**2}\n= {correct}"
                
            elif question_type == 'fifth_power':
                base = random.randint(2, 4)
                correct = base ** 5
                question_text = f"Calculate {base}⁵"
                explanation = f"{base}⁵ = {base} × {base} × {base} × {base} × {base} = {correct}"
                
            elif question_type == 'square_add':
                a = random.randint(2, 12)
                b = random.randint(2, 12)
                correct = a**2 + b**2
                question_text = f"Calculate: {a}² + {b}²"
                explanation = f"{a}² + {b}² = {a**2} + {b**2} = {correct}"
                
            elif question_type == 'square_subtract':
                a = random.randint(5, 18)
                b = random.randint(2, a-1)
                correct = a**2 - b**2
                question_text = f"Calculate: {a}² − {b}²"
                explanation = f"{a}² − {b}² = {a**2} − {b**2} = {correct}"
                
            elif question_type == 'square_diff':
                a = random.randint(6, 20)
                b = random.randint(2, a-2)
                correct = a**2 - b**2
                question_text = f"Find the value of: {a}² − {b}²"
                explanation = f"{a}² = {a**2}\n{b}² = {b**2}\n{a**2} − {b**2} = {correct}"
                
            elif question_type == 'power_mult':
                base = random.randint(2, 6)
                mult = random.randint(2, 8)
                correct = base**2 * mult
                question_text = f"Calculate: {mult} × {base}²"
                explanation = f"{mult} × {base}² = {mult} × {base**2} = {correct}"
                
            elif question_type == 'square_word_area':
                side = random.randint(3, 25)
                correct = side ** 2
                question_text = f"A square has sides of {side} cm. What is its area in cm²?"
                explanation = f"Area = side² = {side}² = {side} × {side} = {correct} cm²"
                
            else:  # cube_word_volume
                side = random.randint(2, 10)
                correct = side ** 3
                question_text = f"A cube has edges of {side} cm. What is its volume in cm³?"
                explanation = f"Volume = side³ = {side}³ = {side} × {side} × {side} = {correct} cm³"
            
            if question_text not in used_texts:
                used_texts.add(question_text)
                break
        
        distractors = [correct + random.randint(1, 15), correct - random.randint(1, max(1, min(10, correct-1))), 
                      correct + random.randint(16, 40)]
        distractors = [d for d in distractors if d > 0 and d != correct]
        while len(distractors) < 3:
            d = correct + random.choice([-5, 5, 10, -10, 15, 20, -15])
            if d > 0 and d != correct and d not in distractors:
                distractors.append(d)
        
        options, correct_idx = format_options(correct, distractors[:3])
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_11() -> List[Dict]:
    """Level 11: Square Roots & Cube Roots"""
    questions = []
    used_texts = set()  # Track actual question texts
    
    # More perfect squares and cubes
    perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
    perfect_cubes = [8, 27, 64, 125, 216]
    
    for i in range(QUESTIONS_PER_LEVEL):
        question_type = random.choice([
            'sqrt_basic', 'sqrt_word', 'cbrt_basic', 'sqrt_mult', 
            'sqrt_add', 'sqrt_context_area', 'sqrt_context_tiles', 'sqrt_reverse'
        ])
        
        attempts = 0
        while attempts < 200:
            attempts += 1
            
            if question_type == 'sqrt_basic':
                n = random.choice(perfect_squares)
                correct = int(math.sqrt(n))
                question_text = f"Find the value of √{n}"
                explanation = f"√{n} means 'what number multiplied by itself gives {n}?'\n{correct} × {correct} = {n}\nSo √{n} = {correct}"
                
            elif question_type == 'sqrt_word':
                n = random.choice(perfect_squares)
                correct = int(math.sqrt(n))
                question_text = f"What is the square root of {n}?"
                explanation = f"The square root of {n} = √{n} = {correct}\nBecause {correct} × {correct} = {n}"
                
            elif question_type == 'cbrt_basic':
                n = random.choice(perfect_cubes)
                correct = int(round(n ** (1/3)))
                question_text = f"Find the cube root of {n}"
                explanation = f"∛{n} means 'what number × itself × itself = {n}?'\n{correct} × {correct} × {correct} = {n}\nSo ∛{n} = {correct}"
                
            elif question_type == 'sqrt_mult':
                n = random.choice([4, 9, 16, 25, 36])
                mult = random.randint(2, 12)
                sqrt_val = int(math.sqrt(n))
                correct = sqrt_val * mult
                question_text = f"Find the value of: √{n} × {mult}"
                explanation = f"First find √{n} = {sqrt_val}\nThen multiply: {sqrt_val} × {mult} = {correct}"
                
            elif question_type == 'sqrt_add':
                n1 = random.choice([4, 9, 16, 25])
                n2 = random.choice([4, 9, 16, 25])
                if n1 == n2:
                    n2 = random.choice([36, 49])
                sqrt1 = int(math.sqrt(n1))
                sqrt2 = int(math.sqrt(n2))
                correct = sqrt1 + sqrt2
                question_text = f"Calculate: √{n1} + √{n2}"
                explanation = f"√{n1} = {sqrt1}\n√{n2} = {sqrt2}\n{sqrt1} + {sqrt2} = {correct}"
                
            elif question_type == 'sqrt_context_area':
                n = random.choice(perfect_squares)
                correct = int(math.sqrt(n))
                contexts = [
                    f"A square has an area of {n} cm². What is the length of one side?",
                    f"A square painting has an area of {n} m². How long is each edge?",
                    f"A square field has an area of {n} m². Find the length of one side.",
                    f"The area of a square is {n} cm². What is the side length?"
                ]
                question_text = random.choice(contexts)
                explanation = f"Area of square = side²\nIf area = {n}, then side = √{n} = {correct}"
                
            elif question_type == 'sqrt_context_tiles':
                # How many tiles per side?
                total_tiles = random.choice([16, 25, 36, 49, 64, 81, 100])
                correct = int(math.sqrt(total_tiles))
                name = random.choice(PEOPLE_NAMES)
                question_text = f"{name} arranges {total_tiles} tiles in a square pattern. How many tiles are along each side?"
                explanation = f"If {total_tiles} tiles form a square, each side has √{total_tiles} = {correct} tiles\nCheck: {correct} × {correct} = {total_tiles} ✓"
                
            else:  # sqrt_reverse - given the root, find the square
                root = random.randint(2, 15)
                correct = root ** 2
                question_text = f"If √x = {root}, what is x?"
                explanation = f"If √x = {root}, then x = {root}² = {root} × {root} = {correct}"
            
            if question_text not in used_texts:
                used_texts.add(question_text)
                break
        
        distractors = generate_distractors(correct, 3, 1, 8)
        options, correct_idx = format_options(correct, distractors)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


def generate_level_12() -> List[Dict]:
    """Level 12: Mixed Operations SEC Style (BODMAS with brackets, indices, roots)"""
    questions = []
    used = set()
    
    for i in range(QUESTIONS_PER_LEVEL):
        # Various SEC Q1(a) style questions
        question_style = random.choice([
            'div_brackets',      # 24 ÷ (9 - 7)
            'mult_brackets',     # 42 × (8 - 5)
            'div_brackets_sq',   # 32 ÷ (7 - 5)²
            'sqrt_brackets',     # √9 × (7 - 3)
            'power_simple',      # 3⁴
            'complex_bodmas'     # Mixed operations
        ])
        
        attempts = 0
        while attempts < 100:
            attempts += 1
            
            if question_style == 'div_brackets':
                # 24 ÷ (9 - 7) = 24 ÷ 2 = 12
                bracket_result = random.randint(2, 6)
                a = random.randint(bracket_result + 2, 15)
                b = a - bracket_result
                dividend = bracket_result * random.randint(3, 12)
                correct = dividend // bracket_result
                key = (question_style, dividend, a, b)
                if key not in used and dividend % bracket_result == 0:
                    used.add(key)
                    question_text = f"Find the value of: {dividend} ÷ ({a} − {b})"
                    explanation = f"BODMAS: Brackets first\n({a} − {b}) = {bracket_result}\nThen divide: {dividend} ÷ {bracket_result} = {correct}"
                    break
            
            elif question_style == 'mult_brackets':
                # 42 × (8 - 5) = 42 × 3 = 126
                bracket_result = random.randint(2, 6)
                a = random.randint(bracket_result + 2, 12)
                b = a - bracket_result
                multiplier = random.randint(10, 50)
                correct = multiplier * bracket_result
                key = (question_style, multiplier, a, b)
                if key not in used:
                    used.add(key)
                    question_text = f"Find the value of: {multiplier} × ({a} − {b})"
                    explanation = f"BODMAS: Brackets first\n({a} − {b}) = {bracket_result}\nThen multiply: {multiplier} × {bracket_result} = {correct}"
                    break
            
            elif question_style == 'div_brackets_sq':
                # 32 ÷ (7 - 5)² = 32 ÷ 4 = 8
                inner_diff = random.randint(2, 4)
                a = random.randint(inner_diff + 3, 12)
                b = a - inner_diff
                bracket_squared = inner_diff ** 2
                dividend = bracket_squared * random.randint(2, 10)
                correct = dividend // bracket_squared
                key = (question_style, dividend, a, b)
                if key not in used and dividend % bracket_squared == 0:
                    used.add(key)
                    question_text = f"Find the value of: {dividend} ÷ ({a} − {b})²"
                    explanation = f"BODMAS: Brackets first, then Indices\n({a} − {b}) = {inner_diff}\n{inner_diff}² = {bracket_squared}\nThen divide: {dividend} ÷ {bracket_squared} = {correct}"
                    break
            
            elif question_style == 'sqrt_brackets':
                # √9 × (7 - 3) = 3 × 4 = 12
                sqrt_n = random.choice([4, 9, 16, 25])
                sqrt_val = int(math.sqrt(sqrt_n))
                bracket_result = random.randint(2, 8)
                a = random.randint(bracket_result + 2, 15)
                b = a - bracket_result
                correct = sqrt_val * bracket_result
                key = (question_style, sqrt_n, a, b)
                if key not in used:
                    used.add(key)
                    question_text = f"Calculate the value of: √{sqrt_n} × ({a} − {b})"
                    explanation = f"BODMAS: Roots and Brackets first\n√{sqrt_n} = {sqrt_val}\n({a} − {b}) = {bracket_result}\nThen multiply: {sqrt_val} × {bracket_result} = {correct}"
                    break
            
            elif question_style == 'power_simple':
                # 3⁴ = 81
                base = random.randint(2, 5)
                exp = random.randint(3, 4)
                correct = base ** exp
                key = (question_style, base, exp)
                if key not in used:
                    used.add(key)
                    superscript = ''.join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(d)] for d in str(exp)])
                    question_text = f"Find the value of: {base}{superscript}"
                    explanation = f"{base}{superscript} = {' × '.join([str(base)] * exp)} = {correct}"
                    break
            
            else:  # complex_bodmas
                # Something like 5 + 3 × 4 or 20 - 12 ÷ 4
                op = random.choice(['mult_add', 'div_sub'])
                if op == 'mult_add':
                    a = random.randint(2, 10)
                    b = random.randint(2, 8)
                    c = random.randint(2, 8)
                    correct = a + b * c
                    key = ('complex', a, b, c, 'mult_add')
                    if key not in used:
                        used.add(key)
                        question_text = f"Find the value of: {a} + {b} × {c}"
                        explanation = f"BODMAS: Multiplication before Addition\n{b} × {c} = {b*c}\nThen add: {a} + {b*c} = {correct}"
                        break
                else:
                    divisor = random.randint(2, 6)
                    quotient = random.randint(2, 8)
                    c = divisor * quotient
                    a = random.randint(quotient + 5, 50)
                    correct = a - quotient
                    key = ('complex', a, c, divisor, 'div_sub')
                    if key not in used:
                        used.add(key)
                        question_text = f"Find the value of: {a} − {c} ÷ {divisor}"
                        explanation = f"BODMAS: Division before Subtraction\n{c} ÷ {divisor} = {quotient}\nThen subtract: {a} − {quotient} = {correct}"
                        break
        
        distractors = generate_distractors(correct, 3, 1, 20)
        options, correct_idx = format_options(correct, distractors)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation
        })
    
    return questions


# ==================== MAIN EXECUTION ====================

def generate_all_questions() -> List[Dict]:
    """Generate all 600 questions"""
    all_questions = []
    
    generators = {
        1: generate_level_1,
        2: generate_level_2,
        3: generate_level_3,
        4: generate_level_4,
        5: generate_level_5,
        6: generate_level_6,
        7: generate_level_7,
        8: generate_level_8,
        9: generate_level_9,
        10: generate_level_10,
        11: generate_level_11,
        12: generate_level_12
    }
    
    for level, generator in generators.items():
        print(f"Generating Level {level}...")
        questions = generator()
        
        for q in questions:
            q['level'] = level
            q['band'] = BANDS[level]
            q['topic'] = TOPIC
            q['mode'] = 'jc_exam'
        
        all_questions.extend(questions)
        print(f"  Generated {len(questions)} questions")
    
    return all_questions


def insert_questions(questions: List[Dict], db_path: str = DB_PATH):
    """Insert questions into database, skipping duplicates"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Clear existing questions for this topic/mode
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = 'jc_exam'
    """, (TOPIC,))
    
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing questions")
    
    # Track inserted to avoid duplicates
    inserted = 0
    skipped = 0
    seen_texts = set()
    
    # Insert new questions
    for q in questions:
        # Create unique key for this question
        key = (q['level'], q['question_text'])
        if key in seen_texts:
            skipped += 1
            continue
        seen_texts.add(key)
        
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, mode, question_text, 
                 option_a, option_b, option_c, option_d, correct_answer, explanation, image_svg)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                q['topic'],
                q['level'],
                q['band'],
                q['mode'],
                q['question_text'],
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_idx'],
                q['explanation'],
                q.get('image_svg')
            ))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"  Skipped duplicate: {q['question_text'][:50]}...")
    
    conn.commit()
    
    if skipped > 0:
        print(f"Skipped {skipped} duplicate questions")
    
    # Verify counts
    cursor.execute("""
        SELECT difficulty_level, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = ? AND mode = 'jc_exam'
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    """, (TOPIC,))
    
    print("\nVerification - Questions per level:")
    total = 0
    for level, count in cursor.fetchall():
        status = "✓" if count >= 45 else "⚠️" if count >= 40 else "✗"
        print(f"  Level {level}: {count} {status}")
        total += count
    
    print(f"\nTotal questions inserted: {total}")
    
    conn.close()
    return total


def main():
    print("=" * 60)
    print("AgentMath - Arithmetic Question Generator")
    print("SEC-Aligned for Irish Junior Cycle Mathematics")
    print("=" * 60)
    print()
    
    questions = generate_all_questions()
    print(f"\nGenerated {len(questions)} total questions")
    
    # Insert into database
    print("\nInserting into database...")
    total = insert_questions(questions)
    
    print("\n" + "=" * 60)
    print("Generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
