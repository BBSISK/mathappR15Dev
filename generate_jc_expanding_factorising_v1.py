#!/usr/bin/env python3
"""
AgentMath - Expanding and Factorising Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q13(b): "Expand 4(3x - 2)"
- 2023 OL Q12(b): "Expand 3(2x - 5)"
- 2024 OL Q14(a): "Expand and simplify 2(x + 3) + 3(x - 1)"
- 2023 HL Q7(c): "Factorise x² + 5x + 6"
- 2024 HL Q8(b): "Expand and simplify (x + 3)(x - 2)"
- 2022 HL Q9(a): "Factorise fully 3x² - 12x"

Level Structure:
  L1-3:   Foundation (single brackets, subtraction, negative multipliers)
  L4-6:   Ordinary (double brackets FOIL, expand+simplify, perfect squares)
  L7-9:   Higher (common factor, quadratic factorising positive, mixed signs)
  L10-12: Mastery (difference of squares, factorise fully, SEC exam style)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
from math import gcd

TOPIC = 'expanding_factorising'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'
VARIABLES = ['x', 'y', 'a', 'b', 'n', 'm', 'p', 'k']

def make_options(correct, wrong_list):
    correct_str = str(correct).strip()
    options = [correct_str]
    for w in wrong_list:
        w_str = str(w).strip()
        if w_str != correct_str and w_str not in options:
            options.append(w_str)
        if len(options) >= 4:
            break
    fallback_idx = 1
    while len(options) < 4:
        fallback = f"Cannot simplify ({fallback_idx})"
        if fallback not in options:
            options.append(fallback)
        fallback_idx += 1
    options = options[:4]
    random.shuffle(options)
    return options, options.index(correct_str)

def generate_level_1():
    """Foundation: Expand a(bx + c) with positive numbers."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:4])
        template = random.choice([1, 2, 3])
        if template == 1:
            a, b = random.randint(2, 6), random.randint(1, 8)
            q_text = f"Expand: {a}({var} + {b})"
            correct = f"{a}{var} + {a * b}"
            wrong = [f"{a}{var} + {b}", f"{a + b}{var}", f"{var} + {a * b}"]
            exp = f"{a} × {var} = {a}{var}, {a} × {b} = {a * b}"
        elif template == 2:
            a, b, c = random.randint(2, 5), random.randint(2, 4), random.randint(1, 6)
            q_text = f"Expand: {a}({b}{var} + {c})"
            correct = f"{a * b}{var} + {a * c}"
            wrong = [f"{a + b}{var} + {c}", f"{a * b}{var} + {c}", f"{a}{var} + {a * c}"]
            exp = f"{a} × {b}{var} = {a * b}{var}, {a} × {c} = {a * c}"
        else:
            a, b = random.randint(3, 7), random.randint(2, 9)
            q_text = f"Expand: {a}({var} + {b})"
            correct = f"{a}{var} + {a * b}"
            wrong = [f"{a}{var} + {b}", f"{a + b}{var}", f"{a * b}{var}"]
            exp = f"Multiply {a} by each term inside"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 1, 'difficulty_band': 'foundation', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_2():
    """Foundation: Expand a(bx - c) with subtraction."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:4])
        template = random.choice([1, 2, 3])
        if template == 1:
            a, b = random.randint(2, 6), random.randint(1, 7)
            q_text = f"Expand: {a}({var} - {b})"
            correct = f"{a}{var} - {a * b}"
            wrong = [f"{a}{var} + {a * b}", f"{a}{var} - {b}", f"{a - b}{var}"]
            exp = f"{a} × {var} = {a}{var}, {a} × (-{b}) = -{a * b}"
        elif template == 2:
            a, b, c = random.randint(2, 5), random.randint(2, 4), random.randint(1, 5)
            q_text = f"Expand: {a}({b}{var} - {c})"
            correct = f"{a * b}{var} - {a * c}"
            wrong = [f"{a * b}{var} + {a * c}", f"{a + b}{var} - {c}", f"{a * b}{var} - {c}"]
            exp = f"{a} × {b}{var} = {a * b}{var}, {a} × (-{c}) = -{a * c}"
        else:
            a, b, c = random.randint(2, 5), random.randint(2, 6), random.randint(1, 3)
            q_text = f"Expand: {a}({b} - {c}{var})"
            correct = f"{a * b} - {a * c}{var}"
            wrong = [f"{a * b} + {a * c}{var}", f"{a * c}{var} - {a * b}", f"{a}{var} - {a * b}"]
            exp = f"{a} × {b} = {a * b}, {a} × (-{c}{var}) = -{a * c}{var}"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 2, 'difficulty_band': 'foundation', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_3():
    """Foundation: Expand -a(bx + c) with negative outside."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:4])
        template = random.choice([1, 2, 3])
        if template == 1:
            a, b = random.randint(2, 5), random.randint(1, 6)
            q_text = f"Expand: -{a}({var} + {b})"
            correct = f"-{a}{var} - {a * b}"
            wrong = [f"-{a}{var} + {a * b}", f"{a}{var} - {a * b}", f"-{a}{var} - {b}"]
            exp = f"-{a} × {var} = -{a}{var}, -{a} × {b} = -{a * b}"
        elif template == 2:
            a, b = random.randint(2, 5), random.randint(1, 6)
            q_text = f"Expand: -{a}({var} - {b})"
            correct = f"-{a}{var} + {a * b}"
            wrong = [f"-{a}{var} - {a * b}", f"{a}{var} + {a * b}", f"-{a}{var} - {b}"]
            exp = f"-{a} × {var} = -{a}{var}, -{a} × (-{b}) = +{a * b}"
        else:
            a, b, c = random.randint(2, 4), random.randint(2, 3), random.randint(1, 5)
            q_text = f"Expand: -{a}({b}{var} + {c})"
            correct = f"-{a * b}{var} - {a * c}"
            wrong = [f"-{a * b}{var} + {a * c}", f"{a * b}{var} - {a * c}", f"-{a}{var} - {c}"]
            exp = f"-{a} × {b}{var} = -{a * b}{var}, -{a} × {c} = -{a * c}"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 3, 'difficulty_band': 'foundation', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_4():
    """Ordinary: Expand (x + a)(x + b) using FOIL."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        a, b = random.randint(1, 7), random.randint(1, 7)
        q_text = f"Expand: ({var} + {a})({var} + {b})"
        middle, last = a + b, a * b
        correct = f"{var}² + {middle}{var} + {last}"
        wrong = [f"{var}² + {a}{var} + {b}{var} + {last}", f"{var}² + {last}", f"2{var} + {middle}"]
        exp = f"FOIL: {var}² + {b}{var} + {a}{var} + {last} = {var}² + {middle}{var} + {last}"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 4, 'difficulty_band': 'ordinary', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_5():
    """Ordinary: Expand and simplify - SEC 2024 style."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        template = random.choice([1, 2])
        if template == 1:
            a1, b1, a2, b2 = random.randint(2, 4), random.randint(1, 5), random.randint(2, 4), random.randint(1, 5)
            q_text = f"Expand and simplify: {a1}({var} + {b1}) + {a2}({var} + {b2})"
            coef_x, const = a1 + a2, a1 * b1 + a2 * b2
            correct = f"{coef_x}{var} + {const}"
            wrong = [f"{a1 + a2}{var} + {b1 + b2}", f"{a1}{var} + {a2}{var} + {b1} + {b2}", f"{coef_x}{var} + {a1 * b1}"]
        else:
            a1, b1, a2, b2 = random.randint(3, 5), random.randint(2, 5), random.randint(2, 3), random.randint(1, 4)
            q_text = f"Expand and simplify: {a1}({var} + {b1}) - {a2}({var} + {b2})"
            coef_x, const = a1 - a2, a1 * b1 - a2 * b2
            correct = f"{coef_x}{var} + {const}" if const >= 0 else f"{coef_x}{var} - {abs(const)}"
            if coef_x == 1: correct = f"{var} + {const}" if const >= 0 else f"{var} - {abs(const)}"
            wrong = [f"{a1 + a2}{var} + {b1 - b2}", f"{a1 - a2}{var} + {a1 * b1 + a2 * b2}", f"{coef_x}{var}"]
        exp = f"Expand each bracket then collect like terms"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 5, 'difficulty_band': 'ordinary', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_6():
    """Ordinary: Perfect squares (x ± a)²."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        template = random.choice([1, 2, 3])
        if template == 1:
            a = random.randint(2, 8)
            q_text = f"Expand: ({var} + {a})²"
            correct = f"{var}² + {2 * a}{var} + {a * a}"
            wrong = [f"{var}² + {a * a}", f"{var}² + {a}{var} + {a * a}", f"2{var} + {2 * a}"]
        elif template == 2:
            a = random.randint(2, 8)
            q_text = f"Expand: ({var} - {a})²"
            correct = f"{var}² - {2 * a}{var} + {a * a}"
            wrong = [f"{var}² + {2 * a}{var} + {a * a}", f"{var}² - {a * a}", f"{var}² - {a}{var} + {a * a}"]
        else:
            a, b = random.randint(2, 3), random.randint(1, 4)
            q_text = f"Expand: ({a}{var} + {b})²"
            correct = f"{a * a}{var}² + {2 * a * b}{var} + {b * b}"
            wrong = [f"{a}{var}² + {2 * a * b}{var} + {b * b}", f"{a * a}{var}² + {b}{var} + {b * b}", f"{a * a}{var}² + {b * b}"]
        exp = f"Use (a ± b)² = a² ± 2ab + b²"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 6, 'difficulty_band': 'ordinary', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_7():
    """Higher: Factorise common factor."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        template = random.choice([1, 2, 3, 4])
        if template == 1:
            common, a, b = random.randint(2, 6), random.randint(1, 5), random.randint(1, 6)
            t1, t2 = common * a, common * b
            q_text = f"Factorise: {t1}{var} + {t2}"
            correct = f"{common}({a}{var} + {b})" if a != 1 else f"{common}({var} + {b})"
            wrong = [f"{t1}({var} + {t2})", f"{a}({t1}{var} + {b})", f"{var}({t1} + {t2})"]
        elif template == 2:
            a = random.randint(2, 8)
            q_text = f"Factorise: {var}² + {a}{var}"
            correct = f"{var}({var} + {a})"
            wrong = [f"{a}({var}² + {var})", f"{var}²(1 + {a})", f"({var} + {a}){var}"]
        elif template == 3:
            common, a, b = random.randint(2, 4), random.randint(2, 4), random.randint(1, 4)
            t1, t2 = common * a, common * b
            q_text = f"Factorise: {t1}{var}² + {t2}{var}"
            correct = f"{common}{var}({a}{var} + {b})"
            wrong = [f"{common}({t1}{var}² + {t2}{var})", f"{var}({t1}{var} + {t2})", f"{t1}{var}({var} + {b})"]
        else:
            common, a, b = random.randint(2, 4), random.randint(2, 5), random.randint(1, 4)
            t1, t2 = common * a, common * b
            q_text = f"Factorise: {t1}{var} - {t2}"
            correct = f"{common}({a}{var} - {b})"
            wrong = [f"{common}({a}{var} + {b})", f"{t1}({var} - {b})", f"{a}({t1}{var} - {b})"]
        exp = f"Take out the HCF"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 7, 'difficulty_band': 'higher', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_8():
    """Higher: Factorise x² + bx + c (positive factors)."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        a, b = random.randint(1, 7), random.randint(1, 7)
        middle, last = a + b, a * b
        q_text = f"Factorise: {var}² + {middle}{var} + {last}"
        correct = f"({var} + {a})({var} + {b})"
        wrong = [f"({var} + {last})({var} + 1)", f"({var} + {middle})({var} + 1)", f"({var} - {a})({var} - {b})"]
        exp = f"Find two numbers that multiply to {last} and add to {middle}"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 8, 'difficulty_band': 'higher', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_9():
    """Higher: Factorise with mixed signs."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        template = random.choice([1, 2, 3])
        if template == 1:
            a, b = random.randint(1, 6), random.randint(1, 6)
            middle, last = a + b, a * b
            q_text = f"Factorise: {var}² - {middle}{var} + {last}"
            correct = f"({var} - {a})({var} - {b})"
            wrong = [f"({var} + {a})({var} + {b})", f"({var} - {a})({var} + {b})", f"({var} - {last})({var} - 1)"]
        elif template == 2:
            a = random.randint(2, 7)
            b = random.randint(1, a - 1)
            middle, last = a - b, a * b
            q_text = f"Factorise: {var}² + {middle}{var} - {last}"
            correct = f"({var} + {a})({var} - {b})"
            wrong = [f"({var} - {a})({var} + {b})", f"({var} + {a})({var} + {b})", f"({var} + {middle})({var} - 1)"]
        else:
            a = random.randint(2, 7)
            b = random.randint(1, a - 1)
            middle, last = a - b, a * b
            q_text = f"Factorise: {var}² - {middle}{var} - {last}"
            correct = f"({var} - {a})({var} + {b})"
            wrong = [f"({var} + {a})({var} - {b})", f"({var} - {a})({var} - {b})", f"({var} - {middle})({var} - 1)"]
        exp = f"Find factors that multiply to ±{last} and add to ±{middle}"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 9, 'difficulty_band': 'higher', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_10():
    """Mastery: Difference of squares."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        template = random.choice([1, 2])
        if template == 1:
            a = random.randint(2, 12)
            q_text = f"Factorise: {var}² - {a * a}"
            correct = f"({var} + {a})({var} - {a})"
            wrong = [f"({var} - {a})²", f"({var} + {a})²", f"({var} - {a * a})({var} + 1)"]
        else:
            a, b = random.randint(2, 4), random.randint(2, 5)
            q_text = f"Factorise: {a * a}{var}² - {b * b}"
            correct = f"({a}{var} + {b})({a}{var} - {b})"
            wrong = [f"({a}{var} - {b})²", f"({a * a}{var} + {b})({var} - {b})", f"{a}({var}² - {b * b})"]
        exp = f"Difference of squares: a² - b² = (a + b)(a - b)"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 10, 'difficulty_band': 'mastery', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_11():
    """Mastery: Factorise fully - SEC HL style."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        template = random.choice([1, 2, 3])
        if template == 1:
            common, a = random.randint(2, 4), random.randint(2, 5)
            q_text = f"Factorise fully: {common}{var}² - {common * a}{var}"
            correct = f"{common}{var}({var} - {a})"
            wrong = [f"{var}({common}{var} - {common * a})", f"{common}({var}² - {a}{var})", f"{common}({var}² - {a})"]
        elif template == 2:
            common, a = random.randint(2, 3), random.randint(2, 4)
            q_text = f"Factorise fully: {common}{var}² - {common * a * a}"
            correct = f"{common}({var} + {a})({var} - {a})"
            wrong = [f"{common}({var}² - {a * a})", f"({var} + {a})({var} - {a})", f"{common}{var}({var} - {a * a})"]
        else:
            a, b = random.randint(2, 5), random.randint(2, 6)
            g = gcd(a, b)
            q_text = f"Factorise fully: {a}{var}² + {b}{var}"
            correct = f"{g}{var}({a // g}{var} + {b // g})" if g > 1 else f"{var}({a}{var} + {b})"
            wrong = [f"{var}({a}{var} + {b})", f"{a}({var}² + {b}{var})", f"{a}{var}({var} + {b})"]
        exp = f"Take out all common factors completely"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 11, 'difficulty_band': 'mastery', 'topic': TOPIC, 'mode': MODE})
    return questions

def generate_level_12():
    """Mastery: SEC exam style mixed."""
    questions, used, attempts = [], set(), 0
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < 1000:
        attempts += 1
        var = random.choice(VARIABLES[:3])
        template = random.choice([1, 2, 3, 4])
        if template == 1:
            a, b, c = random.randint(2, 5), random.randint(1, 4), random.randint(1, 10)
            q_text = f"Expand and simplify: ({var} + {a})({var} + {b}) - {c}"
            middle, last = a + b, a * b - c
            correct = f"{var}² + {middle}{var} + {last}" if last >= 0 else f"{var}² + {middle}{var} - {abs(last)}"
            wrong = [f"{var}² + {middle}{var} + {a * b}", f"{var}² + {a + b - c}{var}", f"{var}² + {middle}{var}"]
        elif template == 2:
            a, b = random.randint(2, 5), random.randint(1, a - 1) if a > 1 else 1
            q_text = f"Expand and simplify: ({var} + {a})² - ({var} + {b})²"
            coef, const = 2 * (a - b), a * a - b * b
            correct = f"{coef}{var} + {const}"
            wrong = [f"{var}² + {coef}{var} + {const}", f"2{var}² + {coef}{var}", f"{a - b}{var} + {const}"]
        elif template == 3:
            a, p = random.randint(2, 5), random.randint(2, 5)
            q_text = f"Factorise fully: {a}{var}² - {a * p * p}"
            correct = f"{a}({var} + {p})({var} - {p})"
            wrong = [f"{a}({var}² - {p * p})", f"({var} + {p})({var} - {p})", f"{a}{var}({var} - {p * p})"]
        else:
            a = random.randint(2, 6)
            q_text = f"Expand: ({var} + {a})({var} - {a})"
            correct = f"{var}² - {a * a}"
            wrong = [f"{var}² + {a * a}", f"{var}² - {2 * a}{var}", f"({var} + {a})²"]
        exp = f"SEC exam style - use appropriate technique"
        if q_text in used: continue
        used.add(q_text)
        options, idx = make_options(correct, wrong)
        if len(set(options)) != 4: continue
        questions.append({'question_text': q_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx, 'explanation': exp,
            'image_svg': None, 'difficulty': 12, 'difficulty_band': 'mastery', 'topic': TOPIC, 'mode': MODE})
    return questions

def validate_questions(questions):
    errors, level_counts = [], {}
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        if len(set([q['option_a'], q['option_b'], q['option_c'], q['option_d']])) != 4:
            errors.append(f"Level {level}: Duplicate options")
    print("\n" + "=" * 60 + "\nVALIDATION SUMMARY\n" + "=" * 60)
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} {'✓' if count >= QUESTIONS_PER_LEVEL else '✗'}")
    print("=" * 60 + f"\nTotal: {len(questions)} | Errors: {len(errors)}")
    return len(errors)

def insert_questions(questions):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    print(f"Deleted {cursor.rowcount} existing questions")
    for q in questions:
        cursor.execute("""INSERT INTO questions_adaptive 
            (question_text, option_a, option_b, option_c, option_d, correct_answer, topic, 
             difficulty_level, difficulty_band, mode, explanation, image_svg, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)""",
            (q['question_text'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
             q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'], q['mode'],
             q['explanation'], q.get('image_svg')))
    conn.commit()
    conn.close()
    print(f"Inserted {len(questions)} questions")

def main():
    print("=" * 60 + "\nAgentMath - Expanding and Factorising Generator\n" + "=" * 60)
    all_questions = []
    generators = [(1, generate_level_1, "Single Brackets"), (2, generate_level_2, "Subtraction"),
        (3, generate_level_3, "Negative Multiplier"), (4, generate_level_4, "Double Brackets"),
        (5, generate_level_5, "Expand & Simplify"), (6, generate_level_6, "Perfect Squares"),
        (7, generate_level_7, "Common Factor"), (8, generate_level_8, "Quadratic (Positive)"),
        (9, generate_level_9, "Quadratic (Mixed)"), (10, generate_level_10, "Difference of Squares"),
        (11, generate_level_11, "Factorise Fully"), (12, generate_level_12, "SEC Exam Style")]
    for level, gen_func, name in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = gen_func()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    validate_questions(all_questions)
    if input("\nInsert into database? (y/n): ").lower() == 'y':
        insert_questions(all_questions)
        print("\n✓ Done!")

if __name__ == "__main__":
    main()
