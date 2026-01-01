#!/usr/bin/env python3
"""
LC Higher Level - Complex Numbers Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level x 12 levels) for LC HL Complex Numbers
"""

import random
import math

TOPIC = 'lc_hl_complex'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Introduction to i', 'Complex Number Notation', 'Addition & Subtraction',
    'Multiplication', 'Division', 'Conjugates',
    'Argand Diagrams', 'Modulus & Argument', 'Polar Form',
    'De Moivre\'s Theorem', 'Roots of Complex Numbers', 'Mastery Challenge'
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

def format_complex(a, b):
    """Format a + bi nicely"""
    if b == 0:
        return str(a)
    elif a == 0:
        if b == 1:
            return "i"
        elif b == -1:
            return "-i"
        else:
            return f"{b}i"
    elif b == 1:
        return f"{a} + i"
    elif b == -1:
        return f"{a} - i"
    elif b > 0:
        return f"{a} + {b}i"
    else:
        return f"{a} - {abs(b)}i"

def generate_level_1():
    """Introduction to i"""
    questions = []
    
    # Type 1: Powers of i
    for _ in range(20):
        power = random.randint(1, 20)
        remainder = power % 4
        results = {0: "1", 1: "i", 2: "-1", 3: "-i"}
        correct = results[remainder]
        distractors = [v for k, v in results.items() if v != correct]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"i^{power}: divide {power} by 4, remainder = {remainder}. i^0=1, i^1=i, i^2=-1, i^3=-i. Answer: {correct}"
        questions.append({
            'question_text': f"Simplify i^{power}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Definition of i
    for _ in range(15):
        concepts = [
            ("What is i^2?", "-1", "1", "i", "-i"),
            ("i is defined as the square root of", "-1", "1", "0", "-2"),
            ("What is sqrt(-1)?", "i", "-1", "1", "-i"),
            ("i^4 equals", "1", "-1", "i", "-i"),
            ("What is i^3?", "-i", "i", "-1", "1"),
        ]
        q, correct, d1, d2, d3 = random.choice(concepts)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Definition of i: i = sqrt(-1), so i^2 = -1. Answer: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Simplifying sqrt of negative numbers
    for _ in range(15):
        n = random.choice([4, 9, 16, 25, 36, 49])
        root = int(math.sqrt(n))
        correct = f"{root}i"
        distractors = [f"-{root}", f"{root}", f"-{root}i"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"sqrt(-{n}) = sqrt({n}) x sqrt(-1) = {root} x i = {root}i"
        questions.append({
            'question_text': f"Simplify sqrt(-{n})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_2():
    """Complex Number Notation"""
    questions = []
    
    # Type 1: Identify real and imaginary parts
    for _ in range(20):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        if b == 0:
            b = random.choice([-5, -3, -1, 1, 3, 5])
        
        part = random.choice(['real', 'imaginary'])
        z = format_complex(a, b)
        
        if part == 'real':
            correct = str(a)
            distractors = [str(b), str(a + b), str(abs(a))]
            question = f"What is the real part of z = {z}?"
            explanation = f"For z = a + bi, real part = a. Here a = {a}"
        else:
            correct = str(b)
            distractors = [str(a), str(a + b), str(abs(b))]
            question = f"What is the imaginary part of z = {z}?"
            explanation = f"For z = a + bi, imaginary part = b. Here b = {b}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Equality of complex numbers
    for _ in range(15):
        a = random.randint(1, 8)
        b = random.randint(1, 8)
        
        question = f"If {a} + {b}i = x + yi, find x"
        correct = str(a)
        distractors = [str(b), str(a + b), str(a - b)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Two complex numbers are equal when real parts equal and imaginary parts equal. x = {a}"
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Standard form
    for _ in range(15):
        forms = [
            ("Which is in standard form a + bi?", "3 + 4i", "4i + 3", "i4 + 3", "3 + i4"),
            ("Express sqrt(-9) + 5 in standard form", "5 + 3i", "3i + 5", "5 - 3i", "8i"),
            ("What is 7 written as a complex number?", "7 + 0i", "0 + 7i", "7i", "7 + 7i"),
            ("What is 4i written in standard form?", "0 + 4i", "4 + 0i", "4 + 4i", "4i + 0"),
        ]
        q, correct, d1, d2, d3 = random.choice(forms)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Standard form is a + bi where a is real, b is imaginary coefficient"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_3():
    """Addition & Subtraction"""
    questions = []
    
    # Type 1: Addition
    for _ in range(25):
        a1, b1 = random.randint(-5, 8), random.randint(-5, 8)
        a2, b2 = random.randint(-5, 8), random.randint(-5, 8)
        if b1 == 0: b1 = random.choice([-3, -1, 1, 3])
        if b2 == 0: b2 = random.choice([-2, -1, 1, 2])
        
        result_a = a1 + a2
        result_b = b1 + b2
        
        z1 = format_complex(a1, b1)
        z2 = format_complex(a2, b2)
        correct = format_complex(result_a, result_b)
        
        distractors = [
            format_complex(result_a - 1, result_b),
            format_complex(result_a, result_b + 1),
            format_complex(a1 * a2, b1 * b2)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"({z1}) + ({z2}) = ({a1}+{a2}) + ({b1}+{b2})i = {correct}"
        questions.append({
            'question_text': f"Calculate ({z1}) + ({z2})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Subtraction
    for _ in range(25):
        a1, b1 = random.randint(-5, 8), random.randint(-5, 8)
        a2, b2 = random.randint(-5, 8), random.randint(-5, 8)
        if b1 == 0: b1 = random.choice([-3, -1, 1, 3])
        if b2 == 0: b2 = random.choice([-2, -1, 1, 2])
        
        result_a = a1 - a2
        result_b = b1 - b2
        
        z1 = format_complex(a1, b1)
        z2 = format_complex(a2, b2)
        correct = format_complex(result_a, result_b)
        
        distractors = [
            format_complex(a1 + a2, b1 + b2),
            format_complex(result_a + 1, result_b),
            format_complex(result_a, result_b - 1)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"({z1}) - ({z2}) = ({a1}-{a2}) + ({b1}-{b2})i = {correct}"
        questions.append({
            'question_text': f"Calculate ({z1}) - ({z2})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_4():
    """Multiplication"""
    questions = []
    
    # Type 1: Multiply by real number
    for _ in range(15):
        k = random.randint(2, 5)
        a, b = random.randint(1, 6), random.randint(1, 6)
        z = format_complex(a, b)
        correct = format_complex(k * a, k * b)
        distractors = [
            format_complex(k + a, k + b),
            format_complex(k * a, b),
            format_complex(a, k * b)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"{k}({z}) = {k}({a}) + {k}({b})i = {correct}"
        questions.append({
            'question_text': f"Calculate {k}({z})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Multiply by i
    for _ in range(10):
        a, b = random.randint(1, 8), random.randint(1, 8)
        z = format_complex(a, b)
        # i(a + bi) = ai + bi^2 = ai - b = -b + ai
        correct = format_complex(-b, a)
        distractors = [
            format_complex(a, b),
            format_complex(b, a),
            format_complex(-a, -b)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"i({z}) = {a}i + {b}i^2 = {a}i - {b} = {correct}"
        questions.append({
            'question_text': f"Calculate i x ({z})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Multiply two complex numbers
    for _ in range(25):
        a1, b1 = random.randint(1, 4), random.randint(1, 4)
        a2, b2 = random.randint(1, 4), random.randint(1, 4)
        
        # (a1 + b1i)(a2 + b2i) = a1a2 + a1b2i + b1a2i + b1b2i^2
        # = (a1a2 - b1b2) + (a1b2 + b1a2)i
        result_a = a1 * a2 - b1 * b2
        result_b = a1 * b2 + b1 * a2
        
        z1 = format_complex(a1, b1)
        z2 = format_complex(a2, b2)
        correct = format_complex(result_a, result_b)
        
        distractors = [
            format_complex(a1 * a2, b1 * b2),
            format_complex(a1 * a2 + b1 * b2, a1 * b2 - b1 * a2),
            format_complex(result_a + 1, result_b)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"({z1})({z2}) = {a1*a2} + {a1*b2}i + {b1*a2}i + {b1*b2}i^2 = ({a1*a2} - {b1*b2}) + ({a1*b2} + {b1*a2})i = {correct}"
        questions.append({
            'question_text': f"Calculate ({z1}) x ({z2})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_5():
    """Division"""
    questions = []
    
    # Type 1: Divide by real number
    for _ in range(15):
        k = random.choice([2, 3, 4, 5])
        a, b = k * random.randint(1, 4), k * random.randint(1, 4)
        z = format_complex(a, b)
        correct = format_complex(a // k, b // k)
        distractors = [
            format_complex(a - k, b - k),
            format_complex(a // k, b),
            format_complex(a, b // k)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"({z})/{k} = {a}/{k} + ({b}/{k})i = {correct}"
        questions.append({
            'question_text': f"Calculate ({z}) / {k}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Divide by i
    for _ in range(10):
        a, b = random.randint(1, 6), random.randint(1, 6)
        z = format_complex(a, b)
        # (a + bi)/i = (a + bi) x (-i)/(-i^2) = (a + bi)(-i)/1 = -ai - bi^2 = b - ai
        correct = format_complex(b, -a)
        distractors = [
            format_complex(-b, a),
            format_complex(a, -b),
            format_complex(-a, b)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"({z})/i = ({z}) x (-i)/(i x -i) = ({z})(-i)/1 = -ai + b = {correct}"
        questions.append({
            'question_text': f"Calculate ({z}) / i",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Divide two complex numbers (simple cases)
    for _ in range(25):
        # Use cases where division works out nicely
        a2, b2 = random.randint(1, 3), random.randint(1, 3)
        
        # Create result that will be integer
        result_a = random.randint(-3, 3)
        result_b = random.randint(-3, 3)
        if result_a == 0 and result_b == 0:
            result_a = 1
        
        # Work backwards: (a1 + b1i) = (result_a + result_b*i)(a2 + b2i)
        a1 = result_a * a2 - result_b * b2
        b1 = result_a * b2 + result_b * a2
        
        z1 = format_complex(a1, b1)
        z2 = format_complex(a2, b2)
        correct = format_complex(result_a, result_b)
        
        distractors = [
            format_complex(result_a + 1, result_b),
            format_complex(result_a, result_b + 1),
            format_complex(-result_a, result_b)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"({z1})/({z2}): Multiply by conjugate. Result = {correct}"
        questions.append({
            'question_text': f"Calculate ({z1}) / ({z2})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_6():
    """Conjugates"""
    questions = []
    
    # Type 1: Find the conjugate
    for _ in range(20):
        a = random.randint(-8, 8)
        b = random.randint(-8, 8)
        if b == 0:
            b = random.choice([-5, -3, -1, 1, 3, 5])
        
        z = format_complex(a, b)
        correct = format_complex(a, -b)
        distractors = [
            format_complex(-a, b),
            format_complex(-a, -b),
            format_complex(b, a)
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Conjugate of a + bi is a - bi. Conjugate of {z} is {correct}"
        questions.append({
            'question_text': f"Find the conjugate of z = {z}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: z x conjugate(z) = |z|^2
    for _ in range(15):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        mod_sq = a * a + b * b
        
        z = format_complex(a, b)
        correct = str(mod_sq)
        distractors = [str(a * a - b * b), str(2 * a * b), str(mod_sq + 1)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"z x conjugate(z) = (a + bi)(a - bi) = a^2 + b^2 = {a}^2 + {b}^2 = {mod_sq}"
        questions.append({
            'question_text': f"Calculate z x z* where z = {z}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Properties of conjugates
    for _ in range(15):
        props = [
            ("The conjugate of a real number is", "itself", "zero", "its negative", "undefined"),
            ("If z = 3 + 4i, then z + z* equals", "6", "8i", "0", "6 + 8i"),
            ("If z = 2 + 5i, then z - z* equals", "10i", "0", "4", "4 + 10i"),
            ("The conjugate of i is", "-i", "i", "1", "-1"),
            ("(z*)* equals", "z", "-z", "z*", "|z|"),
        ]
        q, correct, d1, d2, d3 = random.choice(props)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Conjugate property: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_7():
    """Argand Diagrams"""
    questions = []
    
    # Type 1: Identify coordinates
    for _ in range(20):
        a = random.randint(-6, 6)
        b = random.randint(-6, 6)
        if a == 0: a = random.choice([-3, -1, 1, 3])
        if b == 0: b = random.choice([-2, -1, 1, 2])
        
        z = format_complex(a, b)
        correct = f"({a}, {b})"
        distractors = [f"({b}, {a})", f"({-a}, {b})", f"({a}, {-b})"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"z = a + bi is plotted at (a, b) = ({a}, {b}) on Argand diagram"
        questions.append({
            'question_text': f"What point represents z = {z} on an Argand diagram?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Quadrant identification
    for _ in range(15):
        quadrant = random.randint(1, 4)
        if quadrant == 1:
            a, b = random.randint(1, 5), random.randint(1, 5)
            correct = "First quadrant"
        elif quadrant == 2:
            a, b = random.randint(-5, -1), random.randint(1, 5)
            correct = "Second quadrant"
        elif quadrant == 3:
            a, b = random.randint(-5, -1), random.randint(-5, -1)
            correct = "Third quadrant"
        else:
            a, b = random.randint(1, 5), random.randint(-5, -1)
            correct = "Fourth quadrant"
        
        z = format_complex(a, b)
        distractors = ["First quadrant", "Second quadrant", "Third quadrant", "Fourth quadrant"]
        distractors.remove(correct)
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"a = {a} ({'positive' if a > 0 else 'negative'}), b = {b} ({'positive' if b > 0 else 'negative'}). {correct}"
        questions.append({
            'question_text': f"In which quadrant is z = {z} located?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Geometric interpretation
    for _ in range(15):
        concepts = [
            ("On an Argand diagram, the x-axis represents", "Real numbers", "Imaginary numbers", "Complex numbers", "Modulus"),
            ("On an Argand diagram, the y-axis represents", "Imaginary numbers", "Real numbers", "Arguments", "Conjugates"),
            ("The distance from origin to z on Argand diagram is", "|z|", "arg(z)", "z*", "Re(z)"),
            ("Conjugate of z is reflected across the", "Real axis", "Imaginary axis", "Origin", "Line y = x"),
            ("Adding complex numbers is like adding", "Vectors", "Scalars", "Matrices", "Angles"),
        ]
        q, correct, d1, d2, d3 = random.choice(concepts)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Argand diagram property: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_8():
    """Modulus & Argument"""
    questions = []
    
    # Type 1: Calculate modulus (Pythagorean triples for nice answers)
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (9, 12, 15)]
    for _ in range(20):
        a, b, mod = random.choice(triples)
        if random.choice([True, False]):
            a = -a
        if random.choice([True, False]):
            b = -b
        
        z = format_complex(a, b)
        correct = str(mod)
        distractors = [str(mod + 1), str(mod - 1), str(abs(a) + abs(b))]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"|z| = sqrt({a}^2 + {b}^2) = sqrt({a*a} + {b*b}) = sqrt({a*a + b*b}) = {mod}"
        questions.append({
            'question_text': f"Find |z| where z = {z}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Simple arguments (on axes)
    for _ in range(15):
        cases = [
            (1, 0, "0"),
            (0, 1, "pi/2"),
            (-1, 0, "pi"),
            (0, -1, "-pi/2"),
            (2, 0, "0"),
            (0, 3, "pi/2"),
            (-4, 0, "pi"),
            (0, -2, "-pi/2"),
        ]
        a, b, arg = random.choice(cases)
        z = format_complex(a, b)
        correct = arg
        all_args = ["0", "pi/2", "pi", "-pi/2", "pi/4", "-pi/4"]
        distractors = [x for x in all_args if x != arg][:3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"z = {z} lies on axis. arg(z) = {arg}"
        questions.append({
            'question_text': f"Find arg(z) where z = {z}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Special angles (45 degrees)
    for _ in range(15):
        cases = [
            (1, 1, "pi/4"),
            (-1, 1, "3pi/4"),
            (-1, -1, "-3pi/4"),
            (1, -1, "-pi/4"),
            (2, 2, "pi/4"),
            (-3, 3, "3pi/4"),
        ]
        a, b, arg = random.choice(cases)
        z = format_complex(a, b)
        correct = arg
        all_args = ["pi/4", "3pi/4", "-3pi/4", "-pi/4", "pi/2", "pi"]
        distractors = [x for x in all_args if x != arg][:3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"z = {z}: tan(theta) = {b}/{a}. arg(z) = {arg}"
        questions.append({
            'question_text': f"Find arg(z) where z = {z}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_9():
    """Polar Form"""
    questions = []
    
    # Type 1: Convert to polar form (simple cases)
    for _ in range(20):
        cases = [
            (1, 0, 1, "0"),
            (0, 1, 1, "pi/2"),
            (-1, 0, 1, "pi"),
            (0, -1, 1, "-pi/2"),
            (1, 1, "sqrt(2)", "pi/4"),
            (-1, 1, "sqrt(2)", "3pi/4"),
            (2, 0, 2, "0"),
            (0, 3, 3, "pi/2"),
        ]
        a, b, r, theta = random.choice(cases)
        z = format_complex(a, b)
        correct = f"{r}(cos({theta}) + isin({theta}))"
        distractors = [
            f"{r}(cos({theta}) - isin({theta}))",
            f"{r}(sin({theta}) + icos({theta}))",
            f"cos({theta}) + isin({theta})"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"z = {z} has r = {r}, theta = {theta}. Polar form: r(cos(theta) + isin(theta))"
        questions.append({
            'question_text': f"Write z = {z} in polar form",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Convert from polar to rectangular
    for _ in range(15):
        cases = [
            (2, "0", 2, 0),
            (3, "pi/2", 0, 3),
            (4, "pi", -4, 0),
            (2, "-pi/2", 0, -2),
        ]
        r, theta, a, b = random.choice(cases)
        polar = f"{r}(cos({theta}) + isin({theta}))"
        correct = format_complex(a, b)
        distractors = [
            format_complex(r, 0),
            format_complex(0, r),
            f"{r}"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"{polar} = {r}cos({theta}) + {r}isin({theta}) = {correct}"
        questions.append({
            'question_text': f"Convert to rectangular form: {polar}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Multiplication in polar form
    for _ in range(15):
        r1 = random.randint(2, 4)
        r2 = random.randint(2, 3)
        
        r_result = r1 * r2
        correct = f"r = {r_result}"
        distractors = [f"r = {r1 + r2}", f"r = {r1}", f"r = {r2}"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"When multiplying, moduli multiply: r = {r1} x {r2} = {r_result}"
        questions.append({
            'question_text': f"If z1 has r = {r1} and z2 has r = {r2}, find r for z1 x z2",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_10():
    """De Moivre's Theorem"""
    questions = []
    
    # Type 1: Apply De Moivre's Theorem
    for _ in range(20):
        r = random.randint(1, 3)
        n = random.randint(2, 4)
        theta_num = random.choice([1, 2, 3])
        theta_denom = random.choice([4, 6])
        
        theta = f"{theta_num}pi/{theta_denom}"
        result_r = r ** n
        result_theta_num = theta_num * n
        result_theta = f"{result_theta_num}pi/{theta_denom}"
        
        correct = f"{result_r}(cos({result_theta}) + isin({result_theta}))"
        distractors = [
            f"{r * n}(cos({result_theta}) + isin({result_theta}))",
            f"{result_r}(cos({theta}) + isin({theta}))",
            f"{result_r}(cos({n}pi/{theta_denom}) + isin({n}pi/{theta_denom}))"
        ]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"(r(cos(t) + isin(t)))^n = r^n(cos(nt) + isin(nt)). r^{n} = {result_r}, {n} x {theta} = {result_theta}"
        questions.append({
            'question_text': f"Use De Moivre: [{r}(cos({theta}) + isin({theta}))]^{n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Simplify using De Moivre
    for _ in range(15):
        cases = [
            ("(cos(pi/4) + isin(pi/4))^4", "-1"),
            ("(cos(pi/6) + isin(pi/6))^6", "-1"),
            ("(cos(pi/3) + isin(pi/3))^3", "-1"),
            ("(cos(pi/2) + isin(pi/2))^2", "-1"),
            ("(cos(pi/4) + isin(pi/4))^8", "1"),
        ]
        expr, rect = random.choice(cases)
        correct = rect
        distractors = ["1" if rect == "-1" else "-1", "i", "-i"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"{expr} = {rect}"
        questions.append({
            'question_text': f"Simplify: {expr}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Statement of theorem
    for _ in range(15):
        statements = [
            ("De Moivre: (cos(t) + isin(t))^n = ", "cos(nt) + isin(nt)", "ncos(t) + nisin(t)", "cos(t)^n + isin(t)^n", "cos(n) + isin(n)"),
            ("Using De Moivre, the modulus of z^n is", "|z|^n", "n|z|", "|z| + n", "|z|/n"),
            ("Using De Moivre, the argument of z^n is", "n x arg(z)", "arg(z)/n", "arg(z) + n", "arg(z^n)"),
        ]
        q, correct, d1, d2, d3 = random.choice(statements)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"De Moivre's Theorem: {correct}"
        questions.append({
            'question_text': q,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_11():
    """Roots of Complex Numbers"""
    questions = []
    
    # Type 1: Number of nth roots
    for _ in range(15):
        n = random.randint(2, 6)
        correct = str(n)
        distractors = [str(n - 1), str(n + 1), str(2 * n)]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Every non-zero complex number has exactly n distinct nth roots. n = {n}"
        questions.append({
            'question_text': f"How many distinct {n}th roots does a non-zero complex number have?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Square roots of simple numbers
    for _ in range(15):
        cases = [
            ("-1", "i and -i"),
            ("-4", "2i and -2i"),
            ("-9", "3i and -3i"),
        ]
        num, roots = random.choice(cases)
        correct = "2"
        distractors = ["1", "3", "4"]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"sqrt({num}) has 2 solutions: {roots}"
        questions.append({
            'question_text': f"How many square roots does {num} have in C?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Roots of unity
    for _ in range(20):
        n = random.randint(3, 6)
        concepts = [
            (f"The {n}th roots of unity are equally spaced on a circle of radius", "1", str(n), f"1/{n}", "n"),
            (f"The angle between consecutive {n}th roots of unity is", f"2pi/{n}", f"pi/{n}", f"pi/{2*n}", "2pi"),
            (f"The sum of all {n}th roots of unity equals", "0", "1", str(n), "-1"),
        ]
        q, correct, d1, d2, d3 = random.choice(concepts)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Roots of unity property: {correct}"
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
        ("Simplify i^42", "-1", "1", "i", "-i"),
        ("Find |3 + 4i|", "5", "7", "1", "25"),
        ("The conjugate of 5 - 2i is", "5 + 2i", "-5 + 2i", "5 - 2i", "-5 - 2i"),
        ("Calculate (2 + i)(2 - i)", "5", "3", "4 + i", "4"),
        ("If z = 1 + i, find z^2", "2i", "2", "1 + 2i", "2 + 2i"),
        ("arg(-1) equals", "pi", "0", "-pi", "pi/2"),
        ("Express 4i in polar form", "4(cos(pi/2) + isin(pi/2))", "4(cos(0) + isin(0))", "4(cos(pi) + isin(pi))", "4i"),
        ("If |z| = 3 and arg(z) = pi/4, find |z^2|", "9", "6", "3", "27"),
        ("The cube roots of 1 are", "1, omega, omega^2", "1, -1, i", "1, i, -i", "1, 2, 3"),
        ("Calculate (1 + i)^4", "-4", "4", "4i", "-4i"),
        ("If z* = 3 - 4i, find z", "3 + 4i", "3 - 4i", "-3 + 4i", "-3 - 4i"),
        ("|z1 x z2| equals", "|z1| x |z2|", "|z1| + |z2|", "|z1| - |z2|", "|z1|/|z2|"),
        ("arg(z1 x z2) equals", "arg(z1) + arg(z2)", "arg(z1) x arg(z2)", "arg(z1) - arg(z2)", "arg(z1)/arg(z2)"),
        ("If z = cos(pi/3) + isin(pi/3), find z^6", "1", "-1", "i", "-i"),
        ("What is Re((2+3i)(1-i))?", "5", "2", "-1", "3"),
    ]
    
    for _ in range(50):
        q, correct, d1, d2, d3 = random.choice(mastery)
        distractors = [d1, d2, d3]
        options, correct_idx = make_unique_options(correct, distractors)
        explanation = f"Apply complex number techniques. Answer: {correct}"
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
        f.write(f"-- LC Higher Level - Complex Numbers Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
