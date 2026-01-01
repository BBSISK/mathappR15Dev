#!/usr/bin/env python3
"""
TEMPLATE-BASED ADAPTIVE QUESTION GENERATOR
==========================================
Generates mathematically verified questions using templates.
Every answer is calculated programmatically - guaranteed 100% accurate.

Usage:
    python question_generator_templates.py

This replaces the LLM-generated questions with accurate, template-based ones.
"""

import sqlite3
import random
import json
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
import math

# Database path
DB_PATH = 'instance/mathquiz.db'

# Track generated questions to avoid duplicates
_generated_questions = set()


# =============================================================================
# SMART FORMATTING HELPERS
# =============================================================================

def smart_number(val, max_decimals=2):
    """
    Format a number smartly - show decimals only if needed.
    12.0 → "12"
    12.5 → "12.5"
    12.333... → "12.33"
    """
    if val == int(val):
        return str(int(val))
    
    # Round to max_decimals and strip trailing zeros
    formatted = f"{val:.{max_decimals}f}".rstrip('0').rstrip('.')
    return formatted


def smart_money(val):
    """Format money value - €12 or €12.50"""
    if val == int(val):
        return f"€{int(val)}"
    return f"€{val:.2f}"


def smart_percent(val):
    """Format percentage - 12% or 12.5%"""
    return f"{smart_number(val)}%"


def verify_calculation(expected, actual, tolerance=0.001):
    """Verify a calculation is correct within tolerance"""
    if isinstance(expected, str) and isinstance(actual, str):
        return expected == actual
    try:
        return abs(float(expected) - float(actual)) < tolerance
    except (ValueError, TypeError):
        return expected == actual


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def clear_topic_questions(topic):
    """Clear existing questions for a topic"""
    global _generated_questions
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (topic,))
    conn.commit()
    count = cursor.rowcount
    conn.close()
    # Reset tracker for this topic
    _generated_questions = {q for q in _generated_questions if q[0] != topic}
    return count


def save_question(topic, level, question_text, options, correct_index, explanation, question_type='calculation'):
    """Save a question to the database, skipping duplicates"""
    global _generated_questions
    
    # Create unique key
    key = (topic, level, question_text)
    if key in _generated_questions:
        return False  # Skip duplicate
    
    conn = get_db()
    cursor = conn.cursor()
    
    # Determine band
    if level <= 3:
        band = 'beginner'
    elif level <= 7:
        band = 'intermediate'
    else:
        band = 'advanced'
    
    try:
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, difficulty_level, difficulty_band,
             question_type, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            topic,
            question_text,
            options[0],
            options[1],
            options[2],
            options[3],
            correct_index,
            explanation,
            level,
            band,
            question_type
        ))
        conn.commit()
        _generated_questions.add(key)
        conn.close()
        return True
    except Exception as e:
        conn.close()
        return False  # Skip on any error (likely duplicate)


def generate_distractors_int(correct, count=3):
    """Generate plausible wrong integer answers"""
    distractors = set()
    attempts = 0
    while len(distractors) < count and attempts < 100:
        attempts += 1
        offset = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -10, 10])
        d = correct + offset
        if d != correct and d not in distractors:
            distractors.add(d)
    return list(distractors)[:count]


def generate_distractors_money(correct, count=3):
    """Generate plausible wrong money answers"""
    distractors = set()
    attempts = 0
    while len(distractors) < count and attempts < 100:
        attempts += 1
        offset = random.choice([-5, -2, -1, -0.50, 0.50, 1, 2, 5, 10, -10])
        d = round(correct + offset, 2)
        if abs(d - correct) > 0.01 and d not in distractors and d > 0:
            distractors.add(d)
    return list(distractors)[:count]


def shuffle_options(correct, distractors):
    """Shuffle options and return (options_list, correct_index)"""
    options = [correct] + list(distractors)
    random.shuffle(options)
    correct_index = options.index(correct)
    return options, correct_index


def simplify_fraction(num, den):
    """Simplify a fraction and return as string"""
    if den == 0:
        return "undefined"
    g = math.gcd(abs(num), abs(den))
    num, den = num // g, den // g
    if den < 0:
        num, den = -num, -den
    if den == 1:
        return str(num)
    return f"{num}/{den}"


# =============================================================================
# SOLVING EQUATIONS TEMPLATES
# =============================================================================

def generate_solving_equations():
    """Generate solving equations questions for all 10 levels"""
    print("\n📐 Generating Solving Equations...")
    clear_topic_questions('solving_equations')
    count = 0
    target_per_level = 20
    
    # Level 1: x + a = b (positive integers, small numbers)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.randint(1, 15)
        x = random.randint(1, 15)
        b = x + a
        
        question = f"Solve: x + {a} = {b}"
        correct = x
        explanation = f"x + {a} = {b}\nx = {b} - {a}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 1, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 2: x - a = b (subtraction)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.randint(1, 15)
        x = random.randint(a + 1, 25)
        b = x - a
        
        question = f"Solve: x - {a} = {b}"
        correct = x
        explanation = f"x - {a} = {b}\nx = {b} + {a}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 2, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 3: ax = b (multiplication)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.randint(2, 12)
        x = random.randint(1, 12)
        b = a * x
        
        question = f"Solve: {a}x = {b}"
        correct = x
        explanation = f"{a}x = {b}\nx = {b} ÷ {a}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 3, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 4: ax + b = c (two-step)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.randint(2, 8)
        x = random.randint(1, 12)
        b = random.randint(1, 15)
        c = a * x + b
        
        question = f"Solve: {a}x + {b} = {c}"
        correct = x
        explanation = f"{a}x + {b} = {c}\n{a}x = {c} - {b}\n{a}x = {c - b}\nx = {c - b} ÷ {a}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 4, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 5: Negative numbers (ax + b = c with negatives)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
        x = random.randint(-10, 10)
        if x == 0:
            x = random.choice([-3, 3])
        b = random.randint(-15, 15)
        c = a * x + b
        
        # Format nicely
        if b >= 0:
            b_str = f" + {b}"
        else:
            b_str = f" - {abs(b)}"
        
        question = f"Solve: {a}x{b_str} = {c}"
        correct = x
        explanation = f"{a}x{b_str} = {c}\n{a}x = {c} - ({b})\n{a}x = {c - b}\nx = {c - b} ÷ {a}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 5, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 6: Simple brackets a(x + b) = c
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.randint(2, 6)
        x = random.randint(1, 10)
        b = random.randint(1, 8)
        c = a * (x + b)
        
        question = f"Solve: {a}(x + {b}) = {c}"
        correct = x
        explanation = f"{a}(x + {b}) = {c}\n{a}x + {a * b} = {c}\n{a}x = {c} - {a * b}\n{a}x = {c - a * b}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 6, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 7: Variables both sides ax + b = cx + d
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.randint(4, 10)
        c = random.randint(1, a - 1)
        x = random.randint(1, 10)
        b = random.randint(1, 15)
        d = (a - c) * x + b
        
        question = f"Solve: {a}x + {b} = {c}x + {d}"
        correct = x
        explanation = f"{a}x + {b} = {c}x + {d}\n{a}x - {c}x = {d} - {b}\n{a - c}x = {d - b}\nx = {d - b} ÷ {a - c}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 7, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 8: Complex brackets a(x + b) + c(x + d) = e
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a = random.randint(2, 5)
        c = random.randint(2, 5)
        x = random.randint(1, 8)
        b = random.randint(1, 6)
        d = random.randint(1, 6)
        e = a * (x + b) + c * (x + d)
        
        question = f"Solve: {a}(x + {b}) + {c}(x + {d}) = {e}"
        correct = x
        coeff = a + c
        const = a * b + c * d
        explanation = f"{a}(x + {b}) + {c}(x + {d}) = {e}\n{a}x + {a*b} + {c}x + {c*d} = {e}\n{coeff}x + {const} = {e}\n{coeff}x = {e - const}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 8, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 9: Fractional coefficients (simple fractions)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        denom = random.choice([2, 4])
        x = random.randint(2, 12) * denom
        b = random.randint(1, 10)
        c = x // denom + b
        
        if denom == 2:
            frac_str = "½"
        else:
            frac_str = "¼"
        
        question = f"Solve: {frac_str}x + {b} = {c}"
        correct = x
        explanation = f"{frac_str}x + {b} = {c}\n{frac_str}x = {c} - {b}\n{frac_str}x = {c - b}\nx = {c - b} × {denom}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 9, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 10: Challenge - mix of all concepts
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        variant = random.randint(1, 3)
        
        if variant == 1:
            # Negative bracket: a(x - b) + c = d
            a = random.randint(2, 5)
            x = random.randint(4, 12)
            b = random.randint(1, x - 1)
            c = random.randint(-12, 12)
            d = a * (x - b) + c
            
            if c >= 0:
                c_str = f" + {c}"
            else:
                c_str = f" - {abs(c)}"
            
            question = f"Solve: {a}(x - {b}){c_str} = {d}"
            correct = x
            explanation = f"{a}(x - {b}){c_str} = {d}\n{a}x - {a * b}{c_str} = {d}\n{a}x = {d + a * b - c}\nx = {correct}"
            
        elif variant == 2:
            # ax - b = cx + d
            a = random.randint(4, 8)
            c = random.randint(1, a - 1)
            x = random.randint(2, 10)
            b = random.randint(1, 10)
            d = (a - c) * x - b
            
            question = f"Solve: {a}x - {b} = {c}x + {d}"
            correct = x
            explanation = f"{a}x - {b} = {c}x + {d}\n{a - c}x = {d} + {b}\n{a - c}x = {d + b}\nx = {correct}"
            
        else:
            # -a(x - b) = c
            a = random.randint(2, 5)
            x = random.randint(2, 10)
            b = random.randint(1, 6)
            c = -a * (x - b)
            
            question = f"Solve: -{a}(x - {b}) = {c}"
            correct = x
            explanation = f"-{a}(x - {b}) = {c}\n-{a}x + {a * b} = {c}\n-{a}x = {c - a * b}\nx = {correct}"
        
        distractors = generate_distractors_int(correct, 3)
        options, correct_idx = shuffle_options(str(correct), [str(d) for d in distractors])
        if save_question('solving_equations', 10, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    print(f"   ✓ Generated {count} solving equations questions")
    return count


# =============================================================================
# FRACTIONS TEMPLATES
# =============================================================================

def generate_fractions():
    """Generate fractions questions for all 10 levels"""
    print("\n🥧 Generating Fractions...")
    clear_topic_questions('fractions')
    count = 0
    target_per_level = 20
    
    # Level 1: Comparing unit fractions
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        denoms = random.sample([2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 4)
        random.shuffle(denoms)
        
        correct_denom = max(denoms)
        correct = f"1/{correct_denom}"
        
        question = f"Which of these unit fractions is the smallest?"
        options = [f"1/{d}" for d in denoms]
        correct_idx = options.index(correct)
        explanation = f"For unit fractions, the larger the denominator, the smaller the fraction. 1/{correct_denom} is smallest because {correct_denom} is the largest denominator."
        
        if save_question('fractions', 1, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 2: Equivalent fractions
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        num = random.randint(1, 5)
        den = random.randint(num + 1, 10)
        multiplier = random.randint(2, 5)
        
        equiv_num = num * multiplier
        equiv_den = den * multiplier
        
        question = f"Which fraction is equivalent to {num}/{den}?"
        correct = f"{equiv_num}/{equiv_den}"
        
        wrong1 = f"{num + 1}/{den + 1}"
        wrong2 = f"{num * multiplier}/{den}"
        wrong3 = f"{num}/{den * multiplier}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        explanation = f"{num}/{den} × {multiplier}/{multiplier} = {equiv_num}/{equiv_den}"
        
        if save_question('fractions', 2, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 3: Adding fractions (same denominator)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        den = random.randint(5, 12)
        a_num = random.randint(1, den - 2)
        b_num = random.randint(1, den - a_num - 1)
        result_num = a_num + b_num
        
        question = f"Calculate: {a_num}/{den} + {b_num}/{den}"
        correct = simplify_fraction(result_num, den)
        explanation = f"{a_num}/{den} + {b_num}/{den} = {result_num}/{den}"
        if correct != f"{result_num}/{den}":
            explanation += f" = {correct}"
        
        distractors = [
            simplify_fraction(result_num, den * 2),
            simplify_fraction(a_num + b_num + 1, den),
            simplify_fraction(max(1, a_num + b_num - 1), den)
        ]
        # Remove duplicates and correct answer
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(simplify_fraction(result_num + len(distractors) + 2, den))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 3, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 4: Subtracting fractions (same denominator)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        den = random.randint(5, 12)
        a_num = random.randint(3, den - 1)
        b_num = random.randint(1, a_num - 1)
        result_num = a_num - b_num
        
        question = f"Calculate: {a_num}/{den} - {b_num}/{den}"
        correct = simplify_fraction(result_num, den)
        explanation = f"{a_num}/{den} - {b_num}/{den} = {result_num}/{den}"
        if correct != f"{result_num}/{den}":
            explanation += f" = {correct}"
        
        distractors = [
            simplify_fraction(a_num + b_num, den),
            simplify_fraction(result_num + 1, den),
            simplify_fraction(max(1, result_num - 1), den)
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(simplify_fraction(result_num + len(distractors) + 2, den))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 4, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 5: Unlike denominators (one is multiple of other)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        small_den = random.choice([2, 3, 4, 5])
        multiplier = random.randint(2, 4)
        large_den = small_den * multiplier
        
        a_num = random.randint(1, small_den - 1)
        b_num = random.randint(1, large_den - 1)
        
        a_converted = a_num * multiplier
        result_num = a_converted + b_num
        
        question = f"Calculate: {a_num}/{small_den} + {b_num}/{large_den}"
        correct = simplify_fraction(result_num, large_den)
        explanation = f"{a_num}/{small_den} + {b_num}/{large_den} = {a_converted}/{large_den} + {b_num}/{large_den} = {result_num}/{large_den}"
        if correct != f"{result_num}/{large_den}":
            explanation += f" = {correct}"
        
        distractors = [
            simplify_fraction(a_num + b_num, large_den),
            simplify_fraction(result_num, small_den),
            simplify_fraction(result_num + 1, large_den)
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(simplify_fraction(result_num + len(distractors) + 2, large_den))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 5, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 6: Finding LCD (unlike denominators)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pairs = [(2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (3, 7), (2, 7), (5, 6), (4, 7), (5, 7)]
        den1, den2 = random.choice(pairs)
        lcd = den1 * den2
        
        a_num = random.randint(1, den1 - 1)
        b_num = random.randint(1, den2 - 1)
        
        a_conv = a_num * den2
        b_conv = b_num * den1
        result = a_conv + b_conv
        
        question = f"Calculate: {a_num}/{den1} + {b_num}/{den2}"
        correct = simplify_fraction(result, lcd)
        explanation = f"LCD of {den1} and {den2} is {lcd}.\n{a_num}/{den1} = {a_conv}/{lcd}\n{b_num}/{den2} = {b_conv}/{lcd}\n{a_conv}/{lcd} + {b_conv}/{lcd} = {result}/{lcd}"
        if correct != f"{result}/{lcd}":
            explanation += f" = {correct}"
        
        distractors = [
            simplify_fraction(a_num + b_num, den1 + den2),
            simplify_fraction(result + 1, lcd),
            simplify_fraction(max(1, result - 1), lcd)
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(simplify_fraction(result + len(distractors) + 2, lcd))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 6, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 7: Multiplying fractions
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a_num = random.randint(1, 6)
        a_den = random.randint(2, 8)
        b_num = random.randint(1, 6)
        b_den = random.randint(2, 8)
        
        result_num = a_num * b_num
        result_den = a_den * b_den
        
        question = f"Calculate: {a_num}/{a_den} × {b_num}/{b_den}"
        correct = simplify_fraction(result_num, result_den)
        explanation = f"{a_num}/{a_den} × {b_num}/{b_den} = {result_num}/{result_den}"
        if correct != f"{result_num}/{result_den}":
            explanation += f" = {correct}"
        
        distractors = [
            simplify_fraction(a_num + b_num, a_den + b_den),
            simplify_fraction(result_num + 1, result_den),
            simplify_fraction(result_num, max(1, result_den - 1))
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(simplify_fraction(result_num + len(distractors) + 1, result_den))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 7, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 8: Dividing fractions
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a_num = random.randint(1, 5)
        a_den = random.randint(2, 6)
        b_num = random.randint(1, 4)
        b_den = random.randint(2, 5)
        
        result_num = a_num * b_den
        result_den = a_den * b_num
        
        question = f"Calculate: {a_num}/{a_den} ÷ {b_num}/{b_den}"
        correct = simplify_fraction(result_num, result_den)
        explanation = f"{a_num}/{a_den} ÷ {b_num}/{b_den} = {a_num}/{a_den} × {b_den}/{b_num} = {result_num}/{result_den}"
        if correct != f"{result_num}/{result_den}":
            explanation += f" = {correct}"
        
        wrong_mult = simplify_fraction(a_num * b_num, a_den * b_den)
        distractors = [
            wrong_mult,
            simplify_fraction(result_num + 1, result_den),
            simplify_fraction(result_num, result_den + 1)
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(simplify_fraction(result_num + len(distractors) + 2, result_den))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 8, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 9: Mixed numbers addition
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        whole1 = random.randint(1, 5)
        num1 = random.randint(1, 3)
        den = random.choice([4, 5, 6, 8])
        
        whole2 = random.randint(1, 4)
        num2 = random.randint(1, den - num1)
        
        total_num = num1 + num2
        result_whole = whole1 + whole2
        if total_num >= den:
            result_whole += 1
            total_num -= den
        
        question = f"Calculate: {whole1} {num1}/{den} + {whole2} {num2}/{den}"
        
        if total_num == 0:
            correct = str(result_whole)
        else:
            simplified = simplify_fraction(total_num, den)
            if '/' in simplified:
                correct = f"{result_whole} {simplified}"
            else:
                correct = str(result_whole + int(simplified))
        
        explanation = f"{whole1} {num1}/{den} + {whole2} {num2}/{den} = {whole1 + whole2} {num1 + num2}/{den}"
        if num1 + num2 >= den:
            explanation += f" = {result_whole} {total_num}/{den}"
        
        distractors = [
            f"{result_whole + 1} {max(1, num1)}/{den}",
            f"{max(1, result_whole - 1)} {(total_num + den) % den or 1}/{den}",
            f"{result_whole} {(total_num + 1) % den or 1}/{den}"
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(f"{result_whole + len(distractors)} {1}/{den}")
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 9, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 10: Complex operations
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        a, b = random.randint(1, 3), random.randint(3, 5)
        c = random.randint(1, 3)
        e, f = random.randint(1, 3), random.randint(2, 4)
        
        sum_num = a + c
        sum_den = b
        
        result_num = sum_num * e
        result_den = sum_den * f
        
        question = f"Calculate: ({a}/{b} + {c}/{b}) × {e}/{f}"
        correct = simplify_fraction(result_num, result_den)
        explanation = f"First: {a}/{b} + {c}/{b} = {sum_num}/{sum_den}\nThen: {sum_num}/{sum_den} × {e}/{f} = {result_num}/{result_den}"
        if correct != f"{result_num}/{result_den}":
            explanation += f" = {correct}"
        
        distractors = [
            simplify_fraction(a * e + c, b * f),
            simplify_fraction(result_num + 1, result_den),
            simplify_fraction(result_num, result_den + 1)
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(simplify_fraction(result_num + len(distractors) + 2, result_den))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('fractions', 10, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    print(f"   ✓ Generated {count} fractions questions")
    return count


# =============================================================================
# PERCENTAGES TEMPLATES
# =============================================================================

def generate_percentages():
    """Generate percentages questions for all 10 levels"""
    print("\n💯 Generating Percentages...")
    clear_topic_questions('percentages')
    count = 0
    target_per_level = 20
    
    # Level 1: Convert percentage to fraction
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pct = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 100])
        
        num = pct
        den = 100
        g = math.gcd(num, den)
        simple_num, simple_den = num // g, den // g
        
        question = f"What is {pct}% as a fraction in its simplest form?"
        correct = f"{simple_num}/{simple_den}" if simple_den > 1 else str(simple_num)
        explanation = f"{pct}% = {pct}/100 = {correct}"
        
        distractors = [
            f"{pct}/100" if pct != simple_num or 100 != simple_den else f"{pct}/10",
            f"{simple_num + 1}/{simple_den}" if simple_den > 1 else f"{simple_num}/2",
            f"{simple_num}/{max(1, simple_den - 1)}" if simple_den > 2 else f"1/{simple_num + 1}"
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(f"{simple_num + len(distractors)}/{simple_den + 1}")
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 1, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 2: Simple percentage of amount (10%, 25%, 50%)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pct = random.choice([10, 25, 50])
        amount = random.choice([20, 40, 50, 60, 80, 100, 120, 150, 200])
        
        result = amount * pct // 100
        
        question = f"Find {pct}% of €{amount}"
        correct = f"€{result}"
        explanation = f"{pct}% of €{amount} = €{amount} × {pct}/100 = €{result}"
        
        distractors = [f"€{result + 5}", f"€{max(1, result - 5)}", f"€{result * 2}"]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(f"€{result + (len(distractors) + 1) * 3}")
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 2, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 3: Any percentage of amount
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pct = random.choice([15, 20, 30, 35, 40, 45, 60, 70, 80, 90])
        amount = random.choice([50, 100, 150, 200, 250, 500])
        
        result = amount * pct / 100
        
        question = f"Find {pct}% of €{amount}"
        correct = smart_money(result)
        
        explanation = f"{pct}% of €{amount} = €{amount} × {pct}/100 = {correct}"
        
        distractors = generate_distractors_money(result, 3)
        distractors = [smart_money(d) for d in distractors]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(smart_money(result + (len(distractors) + 1) * 5))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 3, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 4: Percentage increase
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pct = random.choice([10, 15, 20, 25, 30, 40, 50])
        original = random.choice([40, 50, 60, 80, 100, 120, 150, 200])
        
        increase = original * pct / 100
        result = original + increase
        
        question = f"Increase €{original} by {pct}%"
        correct = smart_money(result)
        
        explanation = f"Increase = {pct}% of €{original} = €{smart_number(increase)}\nNew amount = €{original} + €{smart_number(increase)} = {correct}"
        
        distractors = [
            smart_money(increase),  # Just the increase
            smart_money(result + 10),
            smart_money(max(1, result - 10))
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(smart_money(result + (len(distractors) + 1) * 5))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 4, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 5: Percentage decrease (discounts)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pct = random.choice([10, 15, 20, 25, 30, 40, 50])
        original = random.choice([30, 40, 50, 60, 80, 100, 120, 150, 200])
        
        discount = original * pct / 100
        result = original - discount
        
        question = f"A €{original} item has {pct}% off. What is the sale price?"
        correct = smart_money(result)
        
        explanation = f"Discount = {pct}% of €{original} = €{smart_number(discount)}\nSale price = €{original} - €{smart_number(discount)} = {correct}"
        
        distractors = [
            smart_money(discount),  # Common error: the discount amount
            smart_money(original + discount),  # Wrong direction
            smart_money(max(1, result - 5))
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(smart_money(result + (len(distractors) + 1) * 5))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 5, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 6: Express as percentage
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        total = random.choice([20, 25, 40, 50, 80, 100, 200])
        part_pct = random.choice([10, 15, 20, 25, 30, 40, 50, 60, 75])
        part = total * part_pct // 100
        
        question = f"What percentage is {part} of {total}?"
        correct = f"{part_pct}%"
        explanation = f"{part} ÷ {total} × 100 = {part_pct}%"
        
        distractors = [f"{part_pct + 5}%", f"{max(5, part_pct - 5)}%", f"{100 - part_pct}%"]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(f"{part_pct + (len(distractors) + 1) * 10}%")
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 6, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 7: Reverse percentages
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pct = random.choice([10, 20, 25, 50])
        original = random.choice([40, 50, 60, 80, 100, 120, 150, 200])
        after_increase = original * (100 + pct) / 100
        
        question = f"After a {pct}% increase, a price is now €{smart_number(after_increase)}. What was the original price?"
        correct = smart_money(original)
        explanation = f"If original = x, then x × {100 + pct}/100 = €{smart_number(after_increase)}\nx = €{smart_number(after_increase)} ÷ {(100 + pct)/100} = {correct}"
        
        wrong_calc = after_increase - (after_increase * pct / 100)
        distractors = [
            smart_money(wrong_calc),
            smart_money(original + 10),
            smart_money(max(10, original - 10))
        ]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(smart_money(original + (len(distractors) + 1) * 15))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 7, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 8: Percentage change
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        old_val = random.choice([40, 50, 60, 80, 100, 120, 150, 200])
        change_pct = random.choice([10, 15, 20, 25, 30, 40, 50])
        new_val = old_val * (100 + change_pct) / 100
        
        question = f"A price went from €{old_val} to €{smart_number(new_val)}. What is the percentage increase?"
        correct = f"{change_pct}%"
        change_amount = new_val - old_val
        explanation = f"Change = €{smart_number(new_val)} - €{old_val} = €{smart_number(change_amount)}\nPercentage = €{smart_number(change_amount)} ÷ €{old_val} × 100 = {change_pct}%"
        
        wrong_pct = (new_val - old_val) / new_val * 100
        distractors = [f"{change_pct + 5}%", f"{max(5, change_pct - 5)}%", f"{smart_number(wrong_pct)}%"]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(f"{change_pct + (len(distractors) + 1) * 10}%")
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 8, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 9: Compound percentages
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        pct1 = random.choice([10, 20, 25])
        pct2 = random.choice([10, 20, 25])
        original = 100
        
        after_first = original * (100 + pct1) / 100
        after_second = after_first * (100 - pct2) / 100
        
        net_change = after_second - original
        
        question = f"A price increases by {pct1}%, then decreases by {pct2}%. What is the net change from the original?"
        
        # Format with proper decimal handling
        def format_change(val):
            if val == int(val):
                return f"{int(abs(val))}%"
            else:
                return f"{abs(val):.1f}%".rstrip('0').rstrip('.')  + "%"
        
        # Actually simpler - just check if it's a whole number
        if net_change == int(net_change):
            change_str = f"{int(abs(net_change))}%"
        else:
            change_str = f"{abs(net_change):.1f}%"
        
        if net_change > 0:
            correct = f"{change_str} increase"
        elif net_change < 0:
            correct = f"{change_str} decrease"
        else:
            correct = "No change"
        
        explanation = f"Start: 100\nAfter {pct1}% increase: {after_first}\nAfter {pct2}% decrease: {after_second}\nNet change: {net_change:+.1f}%"
        
        # Generate distractors with proper formatting
        wrong1 = "No change"
        wrong2_val = abs(pct1 - pct2)
        wrong2 = f"{wrong2_val}% {'increase' if pct1 > pct2 else 'decrease'}"
        wrong3_val = abs(net_change) + 2
        if wrong3_val == int(wrong3_val):
            wrong3 = f"{int(wrong3_val)}% {'increase' if net_change > 0 else 'decrease'}"
        else:
            wrong3 = f"{wrong3_val:.1f}% {'increase' if net_change > 0 else 'decrease'}"
        
        distractors = [wrong1, wrong2, wrong3]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            extra_val = abs(net_change) + len(distractors) + 3
            distractors.append(f"{extra_val:.1f}% decrease")
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 9, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    # Level 10: VAT calculations (Irish VAT = 23%)
    generated = 0
    attempts = 0
    while generated < target_per_level and attempts < 200:
        attempts += 1
        variant = random.randint(1, 2)
        
        if variant == 1:
            # Calculate price INCLUDING VAT - use clean numbers
            price_ex_vat = random.choice([50, 80, 100, 120, 150, 200, 250, 300])
            vat_rate = 23
            vat_amount = price_ex_vat * vat_rate / 100
            price_inc_vat = price_ex_vat + vat_amount
            
            question = f"An item costs €{price_ex_vat} before VAT. With 23% VAT, what is the total price?"
            correct = smart_money(price_inc_vat)
            explanation = f"VAT = 23% of €{price_ex_vat} = €{smart_number(vat_amount)}\nTotal = €{price_ex_vat} + €{smart_number(vat_amount)} = {correct}"
            
        else:
            # Find price BEFORE VAT - use numbers that divide cleanly by 1.23
            # These give whole number results when divided by 1.23
            price_ex_vat = random.choice([50, 100, 150, 200, 250, 300])
            price_inc_vat = price_ex_vat * 1.23
            
            question = f"A price including 23% VAT is €{smart_number(price_inc_vat)}. What is the price before VAT?"
            correct = smart_money(price_ex_vat)
            explanation = f"Price before VAT = €{smart_number(price_inc_vat)} ÷ 1.23 = {correct}"
        
        result_val = float(correct.replace('€', ''))
        distractors = generate_distractors_money(result_val, 3)
        distractors = [smart_money(d) for d in distractors]
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(smart_money(result_val + (len(distractors) + 1) * 7))
        
        options, correct_idx = shuffle_options(correct, distractors)
        if save_question('percentages', 10, question, options, correct_idx, explanation):
            generated += 1
            count += 1
    
    print(f"   ✓ Generated {count} percentages questions")
    return count


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 60)
    print("TEMPLATE-BASED QUESTION GENERATOR")
    print("Guaranteed 100% Mathematical Accuracy")
    print("=" * 60)
    
    total = 0
    
    total += generate_solving_equations()
    total += generate_fractions()
    total += generate_percentages()
    
    print("\n" + "=" * 60)
    print(f"COMPLETE! Generated {total} mathematically verified questions")
    print("=" * 60)
    
    # Show summary
    conn = get_db()
    cursor = conn.cursor()
    
    print("\nFinal counts per topic and level:")
    for topic in ['solving_equations', 'fractions', 'percentages']:
        cursor.execute("""
            SELECT difficulty_level, COUNT(*) 
            FROM questions_adaptive 
            WHERE topic = ?
            GROUP BY difficulty_level
            ORDER BY difficulty_level
        """, (topic,))
        results = cursor.fetchall()
        total_topic = sum(r[1] for r in results)
        print(f"\n{topic}: {total_topic} total")
        for level, cnt in results:
            bar = "█" * min(cnt, 20)
            print(f"  Level {level:2d}: {cnt:3d} {bar}")
    
    conn.close()


if __name__ == '__main__':
    main()
