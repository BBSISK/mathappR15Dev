#!/usr/bin/env python3
"""
LC Higher Level - Sequences & Series Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level x 12 levels) for LC HL Sequences & Series
"""

import random

TOPIC = 'lc_hl_sequences'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Arithmetic Sequences - Basics', 'Arithmetic Sequences - nth Term', 'Arithmetic Series - Sum',
    'Geometric Sequences - Basics', 'Geometric Sequences - nth Term', 'Geometric Series - Finite Sum',
    'Geometric Series - Infinite Sum', 'Sigma Notation', 'Series Applications',
    'Recurrence Relations', 'Mixed Sequences', 'Mastery Challenge'
]

def make_unique_options(correct, distractors):
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

def generate_level_1():
    """Arithmetic Sequences - Basics"""
    questions = []
    
    for _ in range(20):
        a = random.randint(1, 10)
        d = random.randint(2, 8)
        seq = [a + i*d for i in range(4)]
        correct = str(d)
        distractors = [str(d + 1), str(d - 1), str(a)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Common difference d = {seq[1]} - {seq[0]} = {d}"
        questions.append({
            'question_text': f"Find the common difference: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    for _ in range(15):
        a = random.randint(2, 15)
        d = random.randint(2, 7)
        seq = [a + i*d for i in range(4)]
        next_term = a + 4*d
        correct = str(next_term)
        distractors = [str(next_term + d), str(next_term - d), str(seq[3] + seq[2])]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"d = {d}, next term = {seq[3]} + {d} = {next_term}"
        questions.append({
            'question_text': f"Find the next term: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    for _ in range(15):
        is_arith = random.choice([True, False])
        if is_arith:
            a = random.randint(1, 10)
            d = random.randint(2, 5)
            seq = [a + i*d for i in range(4)]
            correct = "Yes"
            explanation = f"Constant difference of {d} between terms"
        else:
            a = random.randint(2, 4)
            r = random.randint(2, 3)
            seq = [a * (r**i) for i in range(4)]
            correct = "No"
            explanation = f"Differences not constant: {seq[1]-seq[0]}, {seq[2]-seq[1]}, {seq[3]-seq[2]}"
        distractors = ["No" if correct == "Yes" else "Yes", "Cannot tell", "Sometimes"]
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': f"Is this an arithmetic sequence? {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    return questions

def generate_level_2():
    """Arithmetic Sequences - nth Term"""
    questions = []
    
    for _ in range(25):
        a = random.randint(1, 10)
        d = random.randint(2, 6)
        n = random.randint(5, 12)
        term = a + (n - 1) * d
        correct = str(term)
        distractors = [str(term + d), str(term - d), str(a + n * d)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"T_n = a + (n-1)d = {a} + ({n}-1) x {d} = {term}"
        questions.append({
            'question_text': f"Find T_{n} for a = {a}, d = {d}, n = {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    for _ in range(15):
        a = random.randint(1, 5)
        d = random.randint(2, 4)
        coef = d
        const = a - d
        if const >= 0:
            correct = f"{coef}n + {const}"
        else:
            correct = f"{coef}n - {abs(const)}"
        distractors = [f"{coef}n + {a}", f"{a}n + {d}", f"{coef+1}n + {const}"]
        options, correct_idx = make_unique_options(correct, distractors)
        seq = [a + i*d for i in range(3)]
        explanation = f"a = {a}, d = {d}. T_n = {a} + (n-1) x {d} = {correct}"
        questions.append({
            'question_text': f"Find T_n for: {seq[0]}, {seq[1]}, {seq[2]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    for _ in range(10):
        a = random.randint(2, 5)
        d = random.randint(3, 6)
        n = random.randint(8, 15)
        term = a + (n - 1) * d
        correct = str(n)
        distractors = [str(n + 1), str(n - 1), str(term // d)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"{term} = {a} + (n-1) x {d}, solving gives n = {n}"
        questions.append({
            'question_text': f"In an AP with a = {a}, d = {d}, which term equals {term}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    return questions

def generate_level_3():
    """Arithmetic Series - Sum"""
    questions = []
    
    for _ in range(20):
        a = random.randint(1, 5)
        d = random.randint(2, 4)
        n = random.randint(5, 10)
        total = n * (2 * a + (n - 1) * d) // 2
        correct = str(total)
        distractors = [str(total + n), str(total - a), str(n * a)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"S_n = n/2(2a + (n-1)d) = {n}/2(2 x {a} + {n-1} x {d}) = {total}"
        questions.append({
            'question_text': f"Find S_{n} for a = {a}, d = {d}, n = {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    for _ in range(15):
        a = random.randint(1, 10)
        n = random.randint(5, 10)
        d = random.randint(4, 8)
        l = a + (n - 1) * d
        total = n * (a + l) // 2
        correct = str(total)
        distractors = [str(n * l), str(a + l), str(total + n)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"S_n = n/2(a + l) = {n}/2({a} + {l}) = {total}"
        questions.append({
            'question_text': f"Find sum of AP with first term {a}, last term {l}, and {n} terms",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    for _ in range(15):
        n = random.randint(10, 50)
        total = n * (n + 1) // 2
        correct = str(total)
        distractors = [str(n * n), str(total + n), str(n * (n - 1) // 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Sum 1 to {n} = n(n+1)/2 = {n} x {n+1}/2 = {total}"
        questions.append({
            'question_text': f"Find 1 + 2 + 3 + ... + {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    return questions

def generate_level_4():
    """Geometric Sequences - Basics"""
    questions = []
    
    for _ in range(20):
        a = random.randint(1, 5)
        r = random.randint(2, 4)
        seq = [a * (r**i) for i in range(4)]
        correct = str(r)
        distractors = [str(r + 1), str(r - 1), str(seq[1] - seq[0])]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Common ratio r = {seq[1]}/{seq[0]} = {r}"
        questions.append({
            'question_text': f"Find the common ratio: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    for _ in range(15):
        a = random.randint(1, 4)
        r = random.randint(2, 3)
        seq = [a * (r**i) for i in range(4)]
        next_term = a * (r**4)
        correct = str(next_term)
        distractors = [str(seq[3] + seq[2]), str(next_term * r), str(seq[3] * 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"r = {r}, next term = {seq[3]} x {r} = {next_term}"
        questions.append({
            'question_text': f"Find the next term: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    for _ in range(15):
        is_geom = random.choice([True, False])
        if is_geom:
            a = random.randint(2, 4)
            r = random.randint(2, 3)
            seq = [a * (r**i) for i in range(4)]
            correct = "Yes"
            explanation = f"Constant ratio of {r} between consecutive terms"
        else:
            a = random.randint(1, 5)
            d = random.randint(3, 6)
            seq = [a + i*d for i in range(4)]
            correct = "No"
            explanation = "Ratios not constant between consecutive terms"
        distractors = ["No" if correct == "Yes" else "Yes", "Cannot tell", "Sometimes"]
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': f"Is this a geometric sequence? {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    return questions

def generate_level_5():
    """Geometric Sequences - nth Term"""
    questions = []
    
    for _ in range(25):
        a = random.randint(1, 4)
        r = random.randint(2, 3)
        n = random.randint(4, 6)
        term = a * (r ** (n - 1))
        correct = str(term)
        distractors = [str(a * (r ** n)), str(a * r * n), str(term * r)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"T_n = ar^(n-1) = {a} x {r}^{n-1} = {a} x {r**(n-1)} = {term}"
        questions.append({
            'question_text': f"Find T_{n} for a = {a}, r = {r}, n = {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    for _ in range(15):
        a = random.randint(2, 5)
        r = random.randint(2, 3)
        t1 = a
        t4 = a * (r ** 3)
        correct = str(r)
        distractors = [str(r + 1), str(t4 // t1), str(a)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"T_4/T_1 = r^3 = {t4}/{t1} = {r**3}, so r = {r}"
        questions.append({
            'question_text': f"In a GP, T_1 = {t1} and T_4 = {t4}. Find r.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    for _ in range(10):
        a = random.randint(2, 4)
        r = random.randint(2, 3)
        seq = [a * (r**i) for i in range(3)]
        correct = f"{a} x {r}^(n-1)"
        distractors = [f"{a} x {r}^n", f"{a} + {r}(n-1)", f"{r} x {a}^(n-1)"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"a = {a}, r = {r}. T_n = ar^(n-1) = {correct}"
        questions.append({
            'question_text': f"Find T_n for: {seq[0]}, {seq[1]}, {seq[2]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    return questions

def generate_level_6():
    """Geometric Series - Finite Sum"""
    questions = []
    
    for _ in range(25):
        a = random.randint(1, 4)
        r = random.randint(2, 3)
        n = random.randint(4, 6)
        total = a * (r**n - 1) // (r - 1)
        correct = str(total)
        distractors = [str(total + a), str(a * r * n), str(total * r)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"S_n = a(r^n - 1)/(r - 1) = {a}({r}^{n} - 1)/({r} - 1) = {total}"
        questions.append({
            'question_text': f"Find S_{n} for a = {a}, r = {r}, n = {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    for _ in range(15):
        a = random.randint(1, 3)
        r = 2
        n = random.randint(4, 6)
        seq = [a * (r**i) for i in range(3)]
        total = a * (r**n - 1) // (r - 1)
        correct = str(total)
        distractors = [str(sum(seq)), str(total + seq[0]), str(a * n * r)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"a = {a}, r = {r}, n = {n}. S_{n} = {total}"
        questions.append({
            'question_text': f"Find the sum of {n} terms: {seq[0]}, {seq[1]}, {seq[2]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    for _ in range(10):
        formulas = [
            ("For r > 1, the sum formula S_n = ", "a(r^n - 1)/(r - 1)", "ar^n", "na x r", "a/(r - 1)"),
            ("In S_n = a(r^n - 1)/(r - 1), 'a' represents", "First term", "Common ratio", "Number of terms", "Last term"),
        ]
        q, correct, d1, d2, d3 = random.choice(formulas)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Geometric series formula: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    return questions

def generate_level_7():
    """Geometric Series - Infinite Sum"""
    questions = []
    
    for _ in range(20):
        a = random.randint(2, 12)
        r_choices = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
        r_num, r_den = random.choice(r_choices)
        result_num = a * r_den
        result_den = r_den - r_num
        if result_num % result_den == 0:
            correct = str(result_num // result_den)
        else:
            correct = f"{result_num}/{result_den}"
        distractors = [str(a), f"{a * r_den}", f"{result_num + r_den}/{result_den}"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"S_inf = a/(1-r) = {a}/(1 - {r_num}/{r_den}) = {correct}"
        questions.append({
            'question_text': f"Find S_infinity for a = {a}, r = {r_num}/{r_den}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    for _ in range(15):
        conditions = [
            ("A geometric series converges if", "|r| < 1", "r > 1", "r < 0", "|r| > 1"),
            ("For S_infinity to exist, we need", "-1 < r < 1", "r > 0", "r < 1 only", "r != 1"),
            ("If r = 2, does S_infinity exist?", "No", "Yes", "Only if a < 1", "Depends on n"),
            ("If r = 0.5, does S_infinity exist?", "Yes", "No", "Only if a > 0", "Cannot tell"),
        ]
        q, correct, d1, d2, d3 = random.choice(conditions)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Convergence condition: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    for _ in range(15):
        a = random.randint(1, 5)
        seq = [a, a//2 if a % 2 == 0 else a, a//4 if a % 4 == 0 else a]
        # Simple: a + a/2 + a/4 + ... = 2a
        correct = str(2 * a)
        distractors = [str(a), str(3 * a), str(4 * a)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"S_inf = a/(1-r) = {a}/(1 - 1/2) = {a}/(1/2) = {2*a}"
        questions.append({
            'question_text': f"Find: {a} + {a}/2 + {a}/4 + {a}/8 + ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    return questions

def generate_level_8():
    """Sigma Notation"""
    questions = []
    
    for _ in range(20):
        n = random.randint(4, 8)
        total = n * (n + 1) // 2
        correct = str(total)
        distractors = [str(n * n), str(total + n), str(n)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Sum of i from 1 to {n} = {n}({n}+1)/2 = {total}"
        questions.append({
            'question_text': f"Evaluate: Sum (i) from i=1 to {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    for _ in range(15):
        n = random.randint(3, 6)
        c = random.randint(2, 5)
        total = c * n
        correct = str(total)
        distractors = [str(c), str(c + n), str(c * (n + 1))]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Sum of {c} from i=1 to {n} = {c} x {n} = {total}"
        questions.append({
            'question_text': f"Evaluate: Sum ({c}) from i=1 to {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    for _ in range(15):
        a = random.randint(1, 3)
        r = 2
        n = random.randint(3, 5)
        terms = [a * (r**i) for i in range(n)]
        total = sum(terms)
        correct = str(total)
        distractors = [str(total + a), str(a * n * r), str(total - terms[0])]
        options, correct_idx = make_unique_options(correct, distractors)
        terms_str = " + ".join(str(t) for t in terms)
        explanation = f"Sum = {terms_str} = {total}"
        questions.append({
            'question_text': f"Evaluate: Sum ({a} x 2^i) from i=0 to {n-1}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    return questions

def generate_level_9():
    """Series Applications"""
    questions = []
    
    for _ in range(20):
        initial = random.randint(100, 500)
        increase = random.randint(10, 30)
        n = random.randint(5, 10)
        final = initial + (n - 1) * increase
        correct = str(final)
        distractors = [str(initial + n * increase), str(initial * n), str(final + increase)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"AP: a = {initial}, d = {increase}. T_{n} = {initial} + ({n}-1) x {increase} = {final}"
        questions.append({
            'question_text': f"A salary starts at ${initial} and increases by ${increase} each year. What is the salary in year {n}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    for _ in range(15):
        initial = random.randint(1000, 5000)
        rate = random.choice([10, 20, 50])
        years = random.randint(2, 4)
        r = 1 + rate / 100
        final = int(initial * (r ** years))
        correct = str(final)
        distractors = [str(initial * years), str(final + initial), str(int(initial * r))]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"GP: a = {initial}, r = {r}. After {years} years: {initial} x {r}^{years} = {final}"
        questions.append({
            'question_text': f"${initial} grows at {rate}% per year. Value after {years} years?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    for _ in range(15):
        height = random.choice([100, 200, 400])
        ratio = random.choice([2, 4])
        bounces = random.randint(2, 4)
        final_height = height // (ratio ** bounces)
        correct = str(final_height)
        distractors = [str(height // ratio), str(final_height * 2), str(height - bounces * ratio)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Each bounce = height/{ratio}. After {bounces} bounces: {height}/{ratio}^{bounces} = {final_height}"
        questions.append({
            'question_text': f"A ball drops from {height}cm and bounces to 1/{ratio} its height. Height after {bounces} bounces?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    return questions

def generate_level_10():
    """Recurrence Relations"""
    questions = []
    
    for _ in range(20):
        a1 = random.randint(1, 5)
        d = random.randint(2, 5)
        terms = [a1 + i * d for i in range(5)]
        correct = f"T_(n+1) = T_n + {d}"
        distractors = [f"T_(n+1) = T_n x {d}", f"T_(n+1) = T_n + {d+1}", f"T_n = {a1} + {d}n"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Each term = previous + {d}, so T_(n+1) = T_n + {d}"
        questions.append({
            'question_text': f"Find the recurrence relation: {terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    for _ in range(15):
        a1 = random.randint(1, 3)
        r = random.randint(2, 3)
        terms = [a1 * (r ** i) for i in range(4)]
        correct = f"T_(n+1) = {r} x T_n"
        distractors = [f"T_(n+1) = T_n + {r}", f"T_(n+1) = T_n^{r}", f"T_n = {a1} x {r}^n"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Each term = previous x {r}, so T_(n+1) = {r} x T_n"
        questions.append({
            'question_text': f"Find the recurrence relation: {terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    for _ in range(15):
        t1 = random.randint(1, 3)
        t2 = random.randint(2, 5)
        t3 = t1 + t2
        t4 = t2 + t3
        t5 = t3 + t4
        correct = f"T_(n+2) = T_(n+1) + T_n"
        distractors = [f"T_(n+1) = 2 x T_n", f"T_(n+2) = T_n x 2", f"T_n = T_(n-1) x T_(n-2)"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Each term = sum of previous two (Fibonacci-type)"
        questions.append({
            'question_text': f"Find the recurrence relation: {t1}, {t2}, {t3}, {t4}, {t5}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    return questions

def generate_level_11():
    """Mixed Sequences"""
    questions = []
    
    for _ in range(25):
        seq_type = random.choice(['arithmetic', 'geometric'])
        if seq_type == 'arithmetic':
            a = random.randint(2, 10)
            d = random.randint(2, 5)
            seq = [a + i*d for i in range(4)]
            correct = "Arithmetic"
            explanation = f"Constant difference d = {d}"
        else:
            a = random.randint(1, 4)
            r = random.randint(2, 3)
            seq = [a * (r**i) for i in range(4)]
            correct = "Geometric"
            explanation = f"Constant ratio r = {r}"
        distractors = ["Geometric" if correct == "Arithmetic" else "Arithmetic", "Neither", "Both"]
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': f"Identify the sequence type: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    for _ in range(25):
        problems = [
            ("AP: a=3, d=4. Find T_10", "39", "40", "43", "36"),
            ("GP: a=2, r=3. Find T_5", "162", "243", "81", "54"),
            ("Sum of AP: a=5, d=3, n=8", "124", "120", "132", "116"),
            ("Sum of GP: a=3, r=2, n=5", "93", "96", "90", "63"),
            ("S_infinity: a=8, r=1/2", "16", "8", "4", "32"),
            ("AP: T_5=20, T_10=35. Find d", "3", "4", "5", "2"),
            ("GP: T_2=6, T_4=54. Find r", "3", "9", "2", "6"),
        ]
        q, correct, d1, d2, d3 = random.choice(problems)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Apply sequence formulas. Answer: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    return questions

def generate_level_12():
    """Mastery Challenge"""
    questions = []
    
    mastery = [
        ("In AP: a=7, d=3. Find S_20", "670", "680", "660", "690"),
        ("In GP: a=5, r=2. Find S_8", "1275", "1280", "1270", "640"),
        ("Find S_infinity: 12 + 6 + 3 + 1.5 + ...", "24", "12", "36", "18"),
        ("AP has T_3=11, T_7=23. Find a", "5", "3", "7", "8"),
        ("GP has T_2=12, T_5=324. Find r", "3", "2", "4", "27"),
        ("Sum: 2 + 5 + 8 + ... + 29", "155", "150", "160", "145"),
        ("How many terms in AP: 5, 9, 13, ..., 85?", "21", "20", "22", "19"),
        ("Find T_8 in GP: 3, 6, 12, ...", "384", "192", "768", "96"),
        ("AP: a=100, d=-7. First negative term position?", "16", "15", "14", "17"),
        ("Sum of first 10 even numbers", "110", "100", "120", "90"),
        ("GP: a=1, S_infinity=4. Find r", "3/4", "1/4", "1/2", "2/3"),
        ("Insert 3 arithmetic means between 4 and 16", "7, 10, 13", "6, 9, 12", "8, 11, 14", "5, 8, 11"),
        ("Sum 1 + 2 + 4 + 8 + ... + 512", "1023", "1024", "511", "512"),
        ("AP: S_10=155, S_20=610. Find S_30", "1365", "1360", "1370", "765"),
    ]
    
    for _ in range(50):
        q, correct, d1, d2, d3 = random.choice(mastery)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Apply sequence/series techniques. Answer: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
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
        f.write(f"-- LC Higher Level - Sequences & Series Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
