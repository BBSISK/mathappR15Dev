#!/usr/bin/env python3
"""
LC Higher Level - Algebra Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level × 12 levels) for LC HL Algebra

Levels:
1. Indices & Laws (Foundation)
2. Surds - Simplifying (Foundation)
3. Surds - Operations (Foundation)
4. Rationalising Denominators (Developing)
5. Logarithms - Basics (Developing)
6. Logarithm Laws (Developing)
7. Exponential Equations (Proficient)
8. Logarithmic Equations (Proficient)
9. Polynomial Division (Proficient)
10. Factor Theorem (Advanced)
11. Partial Fractions (Advanced)
12. Mastery Challenge (Advanced)
"""

import random

# Configuration
TOPIC = 'lc_hl_algebra'
MODE = 'lc_hl'
QUESTIONS_PER_LEVEL = 50

LEVEL_TITLES = [
    'Indices & Laws', 'Surds - Simplifying', 'Surds - Operations',
    'Rationalising Denominators', 'Logarithms - Basics', 'Logarithm Laws',
    'Exponential Equations', 'Logarithmic Equations', 'Polynomial Division',
    'Factor Theorem', 'Partial Fractions', 'Mastery Challenge'
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

# ============================================================
# LEVEL 1: Indices & Laws (Foundation)
# ============================================================
def generate_level_1():
    """Index laws and simplification"""
    questions = []
    
    # Type 1: Multiplication law a^m × a^n = a^(m+n)
    for _ in range(15):
        base = random.choice([2, 3, 5, 'x', 'a'])
        m = random.randint(2, 5)
        n = random.randint(2, 5)
        result = m + n
        
        correct = f"{base}^{result}"
        distractors = [f"{base}^{m*n}", f"{base}^{abs(m-n)}", f"{base}^{m}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Index law: a^m × a^n = a^(m+n). So {base}^{m} × {base}^{n} = {base}^{m+n} = {correct} ✓"
        
        questions.append({
            'question_text': f"Simplify {base}^{m} × {base}^{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Division law a^m ÷ a^n = a^(m-n)
    for _ in range(15):
        base = random.choice([2, 3, 5, 'x', 'a'])
        m = random.randint(5, 8)
        n = random.randint(2, 4)
        result = m - n
        
        correct = f"{base}^{result}"
        distractors = [f"{base}^{m+n}", f"{base}^{m*n}", f"{base}^{n}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Index law: a^m ÷ a^n = a^(m-n). So {base}^{m} ÷ {base}^{n} = {base}^{m-n} = {correct} ✓"
        
        questions.append({
            'question_text': f"Simplify {base}^{m} ÷ {base}^{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Power law (a^m)^n = a^(mn)
    for _ in range(10):
        base = random.choice([2, 3, 'x', 'a'])
        m = random.randint(2, 4)
        n = random.randint(2, 3)
        result = m * n
        
        correct = f"{base}^{result}"
        distractors = [f"{base}^{m+n}", f"{base}^{m}", f"{base}^{n}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Power law: (a^m)^n = a^(mn). So ({base}^{m})^{n} = {base}^(m*n) = {correct} ✓"
        
        questions.append({
            'question_text': f"Simplify ({base}^{m})^{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Negative and zero indices
    for _ in range(10):
        base = random.choice([2, 3, 5])
        n = random.randint(1, 3)
        
        q_type = random.choice(['negative', 'zero'])
        if q_type == 'negative':
            correct = f"1/{base}^{n}"
            question = f"Express {base}^(-{n}) with positive indices"
            distractors = [f"-{base}^{n}", f"{base}^{n}", f"-1/{base}^{n}"]
            explanation = f"a^(-n) = 1/a^n. So {base}^(-{n}) = 1/{base}^{n} ✓"
        else:
            correct = "1"
            question = f"What is {base}^0?"
            distractors = ["0", str(base), "-1"]
            explanation = f"Any number to the power of 0 equals 1. {base}^0 = 1 ✓"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 2: Surds - Simplifying (Foundation)
# ============================================================
def generate_level_2():
    """Simplifying surds"""
    questions = []
    
    # Type 1: √(a²b) = a√b
    perfect_squares = [(4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7)]
    
    for _ in range(25):
        sq, root = random.choice(perfect_squares)
        b = random.choice([2, 3, 5, 6, 7])
        product = sq * b
        
        correct = f"{root}√{b}"
        distractors = [f"√{product}", f"{b}√{root}", f"{root + b}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"√{product} = √({sq}×{b}) = √{sq} × √{b} = {root}√{b} ✓"
        
        questions.append({
            'question_text': f"Simplify √{product}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Already simplified check
    primes = [2, 3, 5, 7, 11, 13]
    for _ in range(15):
        p = random.choice(primes)
        correct = f"√{p}"
        distractors = [f"{p}", f"1", f"√{p*2}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"√{p} is already in simplest form ({p} is prime) ✓"
        
        questions.append({
            'question_text': f"Simplify √{p}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Perfect squares
    for _ in range(10):
        n = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        root = int(n ** 0.5)
        
        correct = str(root)
        distractors = [str(n), str(root + 1), str(root - 1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"√{n} = {root} (since {root}² = {n}) ✓"
        
        questions.append({
            'question_text': f"Evaluate √{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 3: Surds - Operations (Foundation)
# ============================================================
def generate_level_3():
    """Adding, subtracting, multiplying surds"""
    questions = []
    
    # Type 1: Adding like surds: a√n + b√n = (a+b)√n
    for _ in range(15):
        n = random.choice([2, 3, 5, 7])
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        result = a + b
        
        correct = f"{result}√{n}"
        distractors = [f"{a*b}√{n}", f"√{n*(a+b)}", f"{a+b+n}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{a}√{n} + {b}√{n} = ({a}+{b})√{n} = {result}√{n} ✓"
        
        questions.append({
            'question_text': f"Simplify {a}√{n} + {b}√{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Subtracting like surds
    for _ in range(10):
        n = random.choice([2, 3, 5, 7])
        a = random.randint(5, 8)
        b = random.randint(2, 4)
        result = a - b
        
        correct = f"{result}√{n}"
        distractors = [f"{a+b}√{n}", f"√{n*(a-b)}", f"{a-b}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{a}√{n} - {b}√{n} = ({a}-{b})√{n} = {result}√{n} ✓"
        
        questions.append({
            'question_text': f"Simplify {a}√{n} - {b}√{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Multiplying surds: √a × √b = √(ab)
    for _ in range(15):
        a = random.choice([2, 3, 5])
        b = random.choice([2, 3, 5, 6])
        product = a * b
        
        # Check if result simplifies
        simplified = None
        for sq, root in [(4, 2), (9, 3), (16, 4), (25, 5)]:
            if product % sq == 0:
                remainder = product // sq
                if remainder == 1:
                    simplified = str(root)
                else:
                    simplified = f"{root}√{remainder}"
                break
        
        if simplified:
            correct = simplified
        else:
            correct = f"√{product}"
        
        distractors = [f"√{a+b}", f"{a}√{b}", f"√{a} + √{b}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"√{a} × √{b} = √({a}×{b}) = √{product} = {correct} ✓"
        
        questions.append({
            'question_text': f"Simplify √{a} × √{b}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 4: (√a)² = a
    for _ in range(10):
        a = random.choice([2, 3, 5, 7, 11])
        correct = str(a)
        distractors = [f"√{a}", f"2√{a}", f"{a*a}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"(√{a})² = {a}. Square root squared gives the original number ✓"
        
        questions.append({
            'question_text': f"Simplify (√{a})²",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

# ============================================================
# LEVEL 4: Rationalising Denominators (Developing)
# ============================================================
def generate_level_4():
    """Rationalising surd denominators"""
    questions = []
    
    # Type 1: a/√b = a√b/b
    for _ in range(20):
        a = random.randint(1, 5)
        b = random.choice([2, 3, 5, 7])
        
        correct = f"{a}√{b}/{b}"
        if a == b:
            correct = f"√{b}"
        
        distractors = [f"{a}/√{b}", f"√{b}/{a}", f"{a*b}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{a}/√{b} = {a}/√{b} × √{b}/√{b} = {a}√{b}/{b} ✓"
        
        questions.append({
            'question_text': f"Rationalise the denominator: {a}/√{b}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: 1/(a + √b) - conjugate
    for _ in range(15):
        a = random.randint(1, 3)
        b = random.choice([2, 3, 5])
        denom = a*a - b
        
        if denom != 0:
            correct = f"({a} - √{b})/{abs(denom)}"
            if denom < 0:
                correct = f"-({a} - √{b})/{abs(denom)}"
        else:
            continue
        
        distractors = [f"({a} + √{b})/{abs(denom)}", f"1/({a} - √{b})", f"{a} - √{b}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Multiply by conjugate ({a} - √{b})/({a} - √{b}). Denominator: {a}² - (√{b})² = {a*a} - {b} = {denom} ✓"
        
        questions.append({
            'question_text': f"Rationalise: 1/({a} + √{b})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Conceptual
    for _ in range(15):
        concepts = [
            ("To rationalise a/√b, multiply by...", "√b/√b", "b/b", "1/√b", "a/a"),
            ("The conjugate of (a + √b) is...", "(a - √b)", "(a + √b)", "(-a + √b)", "(√b - a)"),
            ("(a + √b)(a - √b) equals...", "a² - b", "a² + b", "2a", "a² - 2√b"),
        ]
        q, correct, d1, d2, d3 = random.choice(concepts)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Rationalising principle: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 5: Logarithms - Basics (Developing)
# ============================================================
def generate_level_5():
    """Basic logarithm evaluation"""
    questions = []
    
    # Type 1: log_a(a^n) = n
    for _ in range(20):
        base = random.choice([2, 3, 5, 10])
        n = random.randint(1, 5)
        value = base ** n
        
        correct = str(n)
        distractors = [str(value), str(base), str(n + 1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if base == 10:
            explanation = f"log({value}) = {n} because 10^{n} = {value} ✓"
            question = f"Evaluate log({value})"
        else:
            explanation = f"log_{base}({value}) = {n} because {base}^{n} = {value} ✓"
            question = f"Evaluate log_{base}({value})"
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: log_a(1) = 0
    for _ in range(10):
        base = random.choice([2, 3, 5, 10, 'e'])
        correct = "0"
        distractors = ["1", str(base) if base != 'e' else "e", "-1"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if base == 'e':
            explanation = "ln(1) = 0 because e^0 = 1 ✓"
            question = "Evaluate ln(1)"
        elif base == 10:
            explanation = "log(1) = 0 because 10^0 = 1 ✓"
            question = "Evaluate log(1)"
        else:
            explanation = f"log_{base}(1) = 0 because {base}^0 = 1 ✓"
            question = f"Evaluate log_{base}(1)"
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: log_a(a) = 1
    for _ in range(10):
        base = random.choice([2, 3, 5, 10])
        correct = "1"
        distractors = [str(base), "0", str(base - 1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if base == 10:
            explanation = "log(10) = 1 because 10^1 = 10 ✓"
            question = "Evaluate log(10)"
        else:
            explanation = f"log_{base}({base}) = 1 because {base}^1 = {base} ✓"
            question = f"Evaluate log_{base}({base})"
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 4: Converting between log and exponential form
    for _ in range(10):
        base = random.choice([2, 3, 5])
        n = random.randint(2, 4)
        value = base ** n
        
        q_type = random.choice(['to_exp', 'to_log'])
        if q_type == 'to_exp':
            question = f"Write log_{base}({value}) = {n} in exponential form"
            correct = f"{base}^{n} = {value}"
            distractors = [f"{n}^{base} = {value}", f"{value}^{n} = {base}", f"{base}^{value} = {n}"]
        else:
            question = f"Write {base}^{n} = {value} in logarithmic form"
            correct = f"log_{base}({value}) = {n}"
            distractors = [f"log_{n}({value}) = {base}", f"log_{value}({base}) = {n}", f"log_{base}({n}) = {value}"]
        
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"log_a(b) = c ⟺ a^c = b. Answer: {correct} ✓"
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 6: Logarithm Laws (Developing)
# ============================================================
def generate_level_6():
    """Logarithm laws and simplification"""
    questions = []
    
    # Type 1: log(ab) = log(a) + log(b)
    for _ in range(15):
        a = random.choice([2, 3, 5])
        b = random.choice([2, 4, 5, 7])
        
        correct = f"log({a}) + log({b})"
        distractors = [f"log({a}) × log({b})", f"log({a+b})", f"log({a}) - log({b})"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Product rule: log(ab) = log(a) + log(b). log({a*b}) = log({a}) + log({b}) ✓"
        
        questions.append({
            'question_text': f"Express log({a*b}) as a sum of logarithms",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: log(a/b) = log(a) - log(b)
    for _ in range(10):
        a = random.choice([6, 8, 10, 12, 15])
        b = random.choice([2, 3, 5])
        
        correct = f"log({a}) - log({b})"
        distractors = [f"log({a}) + log({b})", f"log({a})/log({b})", f"log({a}) × log({b})"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Quotient rule: log(a/b) = log(a) - log(b) ✓"
        
        questions.append({
            'question_text': f"Express log({a}/{b}) as a difference of logarithms",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: log(a^n) = n·log(a)
    for _ in range(15):
        a = random.choice([2, 3, 5, 7])
        n = random.randint(2, 5)
        
        correct = f"{n}log({a})"
        distractors = [f"log({a}^{n})", f"log({a*n})", f"log({a})^{n}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Power rule: log(a^n) = n·log(a). log({a}^{n}) = {n}log({a}) ✓"
        
        questions.append({
            'question_text': f"Simplify log({a}^{n})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 4: Combining logs
    for _ in range(10):
        a = random.choice([2, 3, 4])
        b = random.choice([5, 6, 7])
        product = a * b
        
        correct = f"log({product})"
        distractors = [f"log({a+b})", f"log({a}) × log({b})", f"log({a*b*2})"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"log({a}) + log({b}) = log({a} × {b}) = log({product}) ✓"
        
        questions.append({
            'question_text': f"Simplify log({a}) + log({b}) to a single logarithm",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

# ============================================================
# LEVEL 7: Exponential Equations (Proficient)
# ============================================================
def generate_level_7():
    """Solving exponential equations"""
    questions = []
    
    # Type 1: 2^x = 2^n (same base)
    for _ in range(15):
        base = random.choice([2, 3, 5])
        n = random.randint(2, 6)
        
        correct = str(n)
        distractors = [str(base), str(n + 1), str(n * base)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"If {base}^x = {base}^{n}, then x = {n} (equal bases means equal exponents) ✓"
        
        questions.append({
            'question_text': f"Solve {base}^x = {base ** n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: a^x = a^m × a^n
    for _ in range(10):
        base = random.choice([2, 3])
        m = random.randint(2, 4)
        n = random.randint(1, 3)
        result = m + n
        
        correct = str(result)
        distractors = [str(m * n), str(m), str(n)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"{base}^x = {base}^{m} × {base}^{n} = {base}^{m+n} = {base}^{result}. So x = {result} ✓"
        
        questions.append({
            'question_text': f"Solve {base}^x = {base}^{m} × {base}^{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Convert base (4^x = 2^n)
    for _ in range(15):
        n = random.choice([4, 6, 8, 10])
        # 4^x = 2^n means (2^2)^x = 2^n, so 2x = n, x = n/2
        result = n // 2
        
        correct = str(result)
        distractors = [str(n), str(n * 2), str(result + 1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"4^x = 2^{n}. Since 4 = 2², we have (2²)^x = 2^{n}, so 2x = {n}, x = {result} ✓"
        
        questions.append({
            'question_text': f"Solve 4^x = 2^{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 4: e^x = e^a
    for _ in range(10):
        a = random.randint(2, 5)
        correct = str(a)
        distractors = [f"e^{a}", str(a + 1), "ln(" + str(a) + ")"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"If e^x = e^{a}, then x = {a} ✓"
        
        questions.append({
            'question_text': f"Solve e^x = e^{a}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 8: Logarithmic Equations (Proficient)
# ============================================================
def generate_level_8():
    """Solving logarithmic equations"""
    questions = []
    
    # Type 1: log_a(x) = n
    for _ in range(20):
        base = random.choice([2, 3, 5, 10])
        n = random.randint(1, 4)
        result = base ** n
        
        correct = str(result)
        distractors = [str(base * n), str(base + n), str(n)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        if base == 10:
            explanation = f"log(x) = {n} means 10^{n} = x, so x = {result} ✓"
            question = f"Solve log(x) = {n}"
        else:
            explanation = f"log_{base}(x) = {n} means {base}^{n} = x, so x = {result} ✓"
            question = f"Solve log_{base}(x) = {n}"
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: log(x) + log(a) = log(b) → log(ax) = log(b) → x = b/a
    for _ in range(15):
        a = random.choice([2, 3, 4, 5])
        b = a * random.randint(2, 5)
        result = b // a
        
        correct = str(result)
        distractors = [str(b - a), str(a + b), str(b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"log(x) + log({a}) = log({b}) → log({a}x) = log({b}) → {a}x = {b} → x = {result} ✓"
        
        questions.append({
            'question_text': f"Solve log(x) + log({a}) = log({b})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: ln(x) = a → x = e^a
    for _ in range(15):
        a = random.randint(1, 4)
        correct = f"e^{a}"
        distractors = [str(a), f"{a}e", f"ln({a})"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"ln(x) = {a} means x = e^{a} ✓"
        
        questions.append({
            'question_text': f"Solve ln(x) = {a}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 9: Polynomial Division (Proficient)
# ============================================================
def generate_level_9():
    """Polynomial division"""
    questions = []
    
    # Type 1: (x² + ax + b) ÷ (x + c) simple cases
    for _ in range(20):
        c = random.randint(1, 3)
        # Create (x + c)(x + d) = x² + (c+d)x + cd
        d = random.randint(1, 4)
        a = c + d
        b = c * d
        
        correct = f"x + {d}"
        distractors = [f"x + {c}", f"x + {a}", f"x - {d}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"(x² + {a}x + {b}) ÷ (x + {c}) = x + {d} ✓"
        
        questions.append({
            'question_text': f"Divide (x² + {a}x + {b}) by (x + {c})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Remainder conceptual
    for _ in range(15):
        concepts = [
            ("If (x - a) is a factor of f(x), then f(a) = ", "0", "a", "1", "-a"),
            ("When dividing f(x) by (x - 2), the remainder equals", "f(2)", "f(-2)", "f(0)", "f(x)"),
            ("If f(x) ÷ (x - 3) has remainder 0, then x = 3 is a", "root", "factor", "quotient", "coefficient"),
        ]
        q, correct, d1, d2, d3 = random.choice(concepts)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Remainder theorem: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Find remainder
    for _ in range(15):
        # f(x) = x² + ax + b, divide by (x - c), remainder = f(c)
        a = random.randint(1, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 3)
        remainder = c*c + a*c + b
        
        correct = str(remainder)
        distractors = [str(c), str(a + b), str(remainder + c)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Remainder = f({c}) = {c}² + {a}({c}) + {b} = {c*c} + {a*c} + {b} = {remainder} ✓"
        
        questions.append({
            'question_text': f"Find the remainder when x² + {a}x + {b} is divided by (x - {c})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

# ============================================================
# LEVEL 10: Factor Theorem (Advanced)
# ============================================================
def generate_level_10():
    """Factor theorem applications"""
    questions = []
    
    # Type 1: Is (x - a) a factor of f(x)?
    for _ in range(20):
        # Create polynomial with known factor
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        # (x - a)(x + b) = x² + (b-a)x - ab
        coef = b - a
        const = -a * b
        
        test_val = random.choice([a, a + 1])  # Sometimes factor, sometimes not
        result = test_val * test_val + coef * test_val + const
        
        if result == 0:
            correct = "Yes"
            explanation = f"f({test_val}) = {test_val}² + {coef}({test_val}) + ({const}) = 0, so (x - {test_val}) is a factor ✓"
        else:
            correct = "No"
            explanation = f"f({test_val}) = {test_val}² + {coef}({test_val}) + ({const}) = {result} ≠ 0, so (x - {test_val}) is not a factor ✓"
        
        distractors = ["No" if correct == "Yes" else "Yes", "Cannot determine", "Only if x > 0"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        const_str = f"+ {const}" if const >= 0 else f"- {abs(const)}"
        coef_str = f"+ {coef}x" if coef >= 0 else f"- {abs(coef)}x"
        
        questions.append({
            'question_text': f"Is (x - {test_val}) a factor of x² {coef_str} {const_str}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Find k such that (x - a) is a factor
    for _ in range(15):
        a = random.randint(1, 3)
        b = random.randint(1, 4)
        # x² + bx + k, (x - a) factor means a² + ba + k = 0, so k = -a² - ba
        k = -(a * a) - b * a
        
        correct = str(k)
        distractors = [str(-k), str(a), str(b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"For (x - {a}) to be a factor: f({a}) = 0. {a}² + {b}({a}) + k = 0. {a*a} + {b*a} + k = 0. k = {k} ✓"
        
        questions.append({
            'question_text': f"Find k if (x - {a}) is a factor of x² + {b}x + k",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Factor theorem statement
    for _ in range(15):
        statements = [
            ("The Factor Theorem states: (x - a) is a factor of f(x) if and only if...", "f(a) = 0", 
             "f(0) = a", "f(a) = 1", "f(-a) = 0"),
            ("If f(2) = 0, which is definitely a factor of f(x)?", "(x - 2)", "(x + 2)", "(x - 4)", "(2x - 1)"),
            ("To check if (x + 3) is a factor of f(x), evaluate f at x = ", "-3", "3", "0", "1/3"),
        ]
        q, correct, d1, d2, d3 = random.choice(statements)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Factor theorem: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

# ============================================================
# LEVEL 11: Partial Fractions (Advanced)
# ============================================================
def generate_level_11():
    """Partial fractions decomposition"""
    questions = []
    
    # Type 1: Setup form for partial fractions
    for _ in range(20):
        setups = [
            ("The partial fraction form of 1/[(x-1)(x+2)] is", "A/(x-1) + B/(x+2)", 
             "A/(x-1) × B/(x+2)", "(A+B)/[(x-1)(x+2)]", "A(x-1) + B(x+2)"),
            ("For 1/[(x-1)²(x+1)], the form is", "A/(x-1) + B/(x-1)² + C/(x+1)",
             "A/(x-1)² + B/(x+1)", "(A+B)/(x-1)² + C/(x+1)", "A/(x-1) + B/(x+1)"),
            ("For (2x+1)/[(x-2)(x+3)], the form is", "A/(x-2) + B/(x+3)",
             "(2x+1)/A + (2x+1)/B", "A(x-2) + B(x+3)", "(A+B)/(x-2)(x+3)"),
        ]
        q, correct, d1, d2, d3 = random.choice(setups)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Partial fraction decomposition: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Find A in simple cases
    for _ in range(15):
        # 1/[(x-a)(x-b)] = A/(x-a) + B/(x-b)
        # At x = a: 1/(a-b) = A, so A = 1/(a-b)
        a = random.randint(1, 3)
        b = a + random.randint(1, 3)
        diff = a - b
        
        # A = 1/(a-b)
        if diff == -1:
            A = "-1"
        elif diff == -2:
            A = "-1/2"
        else:
            A = f"1/{diff}"
        
        correct = A
        distractors = ["1", f"1/{b-a}", f"{a}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Set x = {a}: 1/({a}-{b}) = A. A = 1/{diff} = {A} ✓"
        
        questions.append({
            'question_text': f"In 1/[(x-{a})(x-{b})] = A/(x-{a}) + B/(x-{b}), find A",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Repeated factors
    for _ in range(15):
        concepts = [
            ("For repeated factor (x-a)², the decomposition includes", "A/(x-a) + B/(x-a)²",
             "A/(x-a)²", "(A+B)/(x-a)²", "A/(x-a) only"),
            ("How many constants are needed for 1/[(x-1)²(x+2)]?", "3", "2", "4", "1"),
            ("For (x-3)³ in denominator, we need terms with", "(x-3), (x-3)², (x-3)³",
             "(x-3)³ only", "(x-3) only", "(x-3)² only"),
        ]
        q, correct, d1, d2, d3 = random.choice(concepts)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Repeated factors: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions

# ============================================================
# LEVEL 12: Mastery Challenge (Advanced)
# ============================================================
def generate_level_12():
    """Mixed challenging algebra problems"""
    questions = []
    
    mastery_questions = [
        ("Simplify 8^(2/3)", "4", "8", "2", "16"),
        ("If log₂(x) = 5, find x", "32", "10", "25", "64"),
        ("Solve 3^(2x) = 81", "2", "4", "3", "27"),
        ("Simplify √50 + √18", "8√2", "√68", "4√17", "6√2"),
        ("Rationalise 6/(√3 - 1)", "3(√3 + 1)", "6√3 + 6", "3√3 - 3", "6/(√3 + 1)"),
        ("If log(x) + log(4) = log(20), find x", "5", "16", "80", "4"),
        ("Express log(x³y²) in terms of log x and log y", "3log x + 2log y", "5log(xy)", "log(3x) + log(2y)", "6log(xy)"),
        ("Solve 2^(x+1) = 8", "2", "3", "4", "1"),
        ("Simplify (27)^(-1/3)", "1/3", "3", "-3", "-1/3"),
        ("If 5^x = 125, find x", "3", "25", "5", "2"),
        ("Solve log₃(x) = 4", "81", "12", "64", "27"),
        ("Simplify √(72) ÷ √(8)", "3", "9", "√9", "√64"),
        ("Express 2log(3) - log(9) as a single log", "log(1)", "log(3)", "log(6)", "log(0)"),
        ("If e^x = 7, then x = ", "ln(7)", "log(7)", "7", "e^7"),
        ("Solve 4^x = 2^6", "3", "6", "2", "12"),
        ("Simplify (x^3)^(2/3)", "x²", "x^(9/2)", "x^5", "x^(5/3)"),
        ("If log(a) = 2 and log(b) = 3, find log(ab)", "5", "6", "1", "8"),
        ("Rationalise 1/(2 + √3)", "2 - √3", "(2 - √3)/1", "2 + √3", "1/(2 - √3)"),
        ("The value of log₁₀(1000) is", "3", "100", "10", "1000"),
        ("Simplify 5^0 × 5^3", "125", "0", "15", "1"),
    ]
    
    for _ in range(50):
        q, correct, d1, d2, d3 = random.choice(mastery_questions)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        
        explanation = f"Apply algebra techniques. Answer: {correct} ✓"
        
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    return questions

# ============================================================
# MAIN EXECUTION
# ============================================================
def main():
    """Generate all questions and output SQL"""
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
        f.write(f"-- LC Higher Level - Algebra Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    questions = main()
