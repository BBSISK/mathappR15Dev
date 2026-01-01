#!/usr/bin/env python3
"""
LC Ordinary Level Algebra - 600 Questions Generator
====================================================
50 questions per level × 12 levels = 600 questions

Based on SEC Paper Analysis 2019-2025:
- Algebra worth 265 marks over 7 years
- Focus: Linear equations, quadratics, simultaneous equations, inequalities, expressions
"""

import random

TOPIC_ID = 'lc_ol_algebra'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Simplifying Expressions", "Foundation"),
    2: ("Expanding Brackets", "Foundation"),
    3: ("Factorising Basics", "Foundation"),
    4: ("Linear Equations", "Developing"),
    5: ("Equations with Fractions", "Developing"),
    6: ("Rearranging Formulae", "Developing"),
    7: ("Simultaneous Equations", "Proficient"),
    8: ("Quadratic Equations", "Proficient"),
    9: ("Inequalities", "Proficient"),
    10: ("Algebraic Fractions", "Advanced"),
    11: ("Word Problems", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    options = [correct] + distractors[:3]
    random.shuffle(options)
    return options, options.index(correct)

def generate_level_1():
    """Simplifying Expressions"""
    questions = []
    
    # Collect like terms - simple
    for a in range(2, 10):
        for b in range(1, 8):
            result = a + b
            opts, idx = shuffle_options(f"{result}x", [f"{a+b+1}x", f"{a*b}x", f"{a}x + {b}x"])
            questions.append({
                'text': f"Simplify: {a}x + {b}x",
                'opts': opts, 'idx': idx,
                'exp': f"{a}x + {b}x = {result}x"
            })
            if len(questions) >= 12:
                break
        if len(questions) >= 12:
            break
    
    # Collect like terms - subtraction
    for a in range(5, 12):
        for b in range(1, a):
            result = a - b
            opts, idx = shuffle_options(f"{result}x", [f"{a+b}x", f"{a*b}x", f"{result}"])
            questions.append({
                'text': f"Simplify: {a}x - {b}x",
                'opts': opts, 'idx': idx,
                'exp': f"{a}x - {b}x = {result}x"
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Two types of terms
    for a in range(2, 8):
        for b in range(1, 6):
            for c in range(1, 5):
                for d in range(1, 4):
                    rx, ry = a + c, b + d
                    opts, idx = shuffle_options(f"{rx}x + {ry}y", [f"{rx+ry}xy", f"{a+b}x + {c+d}y", f"{rx}x + {ry}"])
                    questions.append({
                        'text': f"Simplify: {a}x + {b}y + {c}x + {d}y",
                        'opts': opts, 'idx': idx,
                        'exp': f"= {rx}x + {ry}y"
                    })
                    if len(questions) >= 35:
                        break
                if len(questions) >= 35:
                    break
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Simplify with coefficients
    for a in range(2, 8):
        for b in range(2, 6):
            result = a * b
            opts, idx = shuffle_options(f"{result}x", [f"{a+b}x", f"{result}", f"{a}x{b}"])
            questions.append({
                'text': f"Simplify: {a} × {b}x",
                'opts': opts, 'idx': idx,
                'exp': f"{a} × {b}x = {result}x"
            })
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # With subtraction
    for a in range(3, 8):
        for b in range(1, a):
            for c in range(2, 6):
                for d in range(1, c):
                    rx, ry = a - b, c - d
                    opts, idx = shuffle_options(f"{rx}x + {ry}y", [f"{rx-ry}xy", f"{a-c}x + {b-d}y", f"{rx}x - {ry}y"])
                    questions.append({
                        'text': f"Simplify: {a}x - {b}x + {c}y - {d}y",
                        'opts': opts, 'idx': idx,
                        'exp': f"= {rx}x + {ry}y"
                    })
                    if len(questions) >= 50:
                        break
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_2():
    """Expanding Brackets"""
    questions = []
    
    # Single bracket a(x + b)
    for a in range(2, 8):
        for b in range(1, 8):
            ans = f"{a}x + {a*b}"
            opts, idx = shuffle_options(ans, [f"{a}x + {b}", f"{a+b}x", f"x + {a*b}"])
            questions.append({
                'text': f"Expand: {a}(x + {b})",
                'opts': opts, 'idx': idx,
                'exp': f"{a}(x + {b}) = {ans}"
            })
            if len(questions) >= 12:
                break
        if len(questions) >= 12:
            break
    
    # a(x - b)
    for a in range(2, 7):
        for b in range(1, 6):
            ans = f"{a}x - {a*b}"
            opts, idx = shuffle_options(ans, [f"{a}x + {a*b}", f"{a}x - {b}", f"{a-b}x"])
            questions.append({
                'text': f"Expand: {a}(x - {b})",
                'opts': opts, 'idx': idx,
                'exp': f"{a}(x - {b}) = {ans}"
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # a(bx + c)
    for a in range(2, 5):
        for b in range(2, 5):
            for c in range(1, 5):
                coef = a * b
                const = a * c
                ans = f"{coef}x + {const}"
                opts, idx = shuffle_options(ans, [f"{a+b}x + {c}", f"{coef}x + {c}", f"{a}x + {const}"])
                questions.append({
                    'text': f"Expand: {a}({b}x + {c})",
                    'opts': opts, 'idx': idx,
                    'exp': f"= {ans}"
                })
                if len(questions) >= 32:
                    break
            if len(questions) >= 32:
                break
        if len(questions) >= 32:
            break
    
    # Two brackets (x + a)(x + b)
    for a in range(1, 6):
        for b in range(1, 6):
            mid = a + b
            const = a * b
            ans = f"x² + {mid}x + {const}"
            opts, idx = shuffle_options(ans, [f"x² + {a}x + {b}", f"x² + {const}x + {mid}", f"2x + {mid}"])
            questions.append({
                'text': f"Expand: (x + {a})(x + {b})",
                'opts': opts, 'idx': idx,
                'exp': f"= {ans}"
            })
            if len(questions) >= 42:
                break
        if len(questions) >= 42:
            break
    
    # (x - a)(x + b) where b > a
    for a in range(1, 5):
        for b in range(a+1, 7):
            mid = b - a
            const = -a * b
            ans = f"x² + {mid}x - {abs(const)}"
            opts, idx = shuffle_options(ans, [f"x² - {mid}x + {abs(const)}", f"x² + {a+b}x - {abs(const)}", f"x² - {abs(const)}"])
            questions.append({
                'text': f"Expand: (x - {a})(x + {b})",
                'opts': opts, 'idx': idx,
                'exp': f"= {ans}"
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_3():
    """Factorising Basics"""
    questions = []
    
    # Common factor - number
    for a in range(2, 8):
        for b in range(1, 8):
            expr = f"{a}x + {a*b}"
            ans = f"{a}(x + {b})"
            opts, idx = shuffle_options(ans, [f"x({a} + {b})", f"{a}(x + {a*b})", f"{a*b}(x + 1)"])
            questions.append({
                'text': f"Factorise: {expr}",
                'opts': opts, 'idx': idx,
                'exp': f"{expr} = {ans}"
            })
            if len(questions) >= 12:
                break
        if len(questions) >= 12:
            break
    
    # Common factor - x
    for a in range(2, 8):
        for b in range(2, 7):
            expr = f"{a}x² + {b}x"
            ans = f"x({a}x + {b})"
            opts, idx = shuffle_options(ans, [f"{a}x(x + {b})", f"x²({a} + {b})", f"{b}x({a}x + 1)"])
            questions.append({
                'text': f"Factorise: {expr}",
                'opts': opts, 'idx': idx,
                'exp': f"{expr} = {ans}"
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Difference of squares
    squares = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
    for a, a2 in squares:
        expr = f"x² - {a2}"
        ans = f"(x + {a})(x - {a})"
        opts, idx = shuffle_options(ans, [f"(x - {a})²", f"(x + {a})²", f"x(x - {a2})"])
        questions.append({
            'text': f"Factorise: {expr}",
            'opts': opts, 'idx': idx,
            'exp': f"Difference of squares: {ans}"
        })
    
    # x² + bx + c (sum and product)
    factor_pairs = [
        (2, 3, 5, 6), (1, 4, 5, 4), (2, 5, 7, 10), (3, 4, 7, 12),
        (1, 6, 7, 6), (2, 6, 8, 12), (3, 5, 8, 15), (1, 5, 6, 5),
        (2, 4, 6, 8), (3, 6, 9, 18), (4, 5, 9, 20), (1, 3, 4, 3)
    ]
    for a, b, sum_ab, prod_ab in factor_pairs:
        expr = f"x² + {sum_ab}x + {prod_ab}"
        ans = f"(x + {a})(x + {b})"
        opts, idx = shuffle_options(ans, [f"(x + {sum_ab})(x + 1)", f"(x + {prod_ab})(x + 1)", f"(x + {a})²"])
        questions.append({
            'text': f"Factorise: {expr}",
            'opts': opts, 'idx': idx,
            'exp': f"Find two numbers: sum={sum_ab}, product={prod_ab}. {ans}"
        })
        if len(questions) >= 42:
            break
    
    # Common factor with subtraction
    for a in range(2, 6):
        for b in range(1, 5):
            expr = f"{a}x - {a*b}"
            ans = f"{a}(x - {b})"
            opts, idx = shuffle_options(ans, [f"x({a} - {b})", f"{a}(x + {b})", f"{a*b}(x - 1)"])
            questions.append({
                'text': f"Factorise: {expr}",
                'opts': opts, 'idx': idx,
                'exp': f"= {ans}"
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_4():
    """Linear Equations"""
    questions = []
    
    # x + a = b
    for a in range(1, 10):
        for b in range(a+1, 15):
            ans = str(b - a)
            opts, idx = shuffle_options(ans, [str(b + a), str(a), str(b)])
            questions.append({
                'text': f"Solve: x + {a} = {b}",
                'opts': opts, 'idx': idx,
                'exp': f"x = {b} - {a} = {ans}"
            })
            if len(questions) >= 10:
                break
        if len(questions) >= 10:
            break
    
    # x - a = b
    for a in range(1, 8):
        for b in range(1, 10):
            ans = str(a + b)
            opts, idx = shuffle_options(ans, [str(b - a) if b > a else str(a - b), str(a), str(b)])
            questions.append({
                'text': f"Solve: x - {a} = {b}",
                'opts': opts, 'idx': idx,
                'exp': f"x = {b} + {a} = {ans}"
            })
            if len(questions) >= 18:
                break
        if len(questions) >= 18:
            break
    
    # ax = b
    for a in range(2, 8):
        for mult in range(1, 8):
            b = a * mult
            ans = str(mult)
            opts, idx = shuffle_options(ans, [str(mult + 1), str(mult - 1) if mult > 1 else "0", str(a)])
            questions.append({
                'text': f"Solve: {a}x = {b}",
                'opts': opts, 'idx': idx,
                'exp': f"x = {b}/{a} = {ans}"
            })
            if len(questions) >= 28:
                break
        if len(questions) >= 28:
            break
    
    # ax + b = c
    for a in range(2, 6):
        for b in range(1, 6):
            for x in range(1, 8):
                c = a * x + b
                ans = str(x)
                opts, idx = shuffle_options(ans, [str(x + 1), str(x - 1) if x > 1 else "0", str(c)])
                questions.append({
                    'text': f"Solve: {a}x + {b} = {c}",
                    'opts': opts, 'idx': idx,
                    'exp': f"{a}x = {c - b}, x = {ans}"
                })
                if len(questions) >= 40:
                    break
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # ax - b = c
    for a in range(2, 5):
        for b in range(1, 5):
            for x in range(2, 8):
                c = a * x - b
                if c > 0:
                    ans = str(x)
                    opts, idx = shuffle_options(ans, [str(x + 1), str(x - 1), str(c)])
                    questions.append({
                        'text': f"Solve: {a}x - {b} = {c}",
                        'opts': opts, 'idx': idx,
                        'exp': f"{a}x = {c + b}, x = {ans}"
                    })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_5():
    """Equations with Fractions"""
    questions = []
    
    # x/a = b
    for a in range(2, 8):
        for b in range(1, 8):
            ans = str(a * b)
            opts, idx = shuffle_options(ans, [str(b), str(a), str(a + b)])
            questions.append({
                'text': f"Solve: x/{a} = {b}",
                'opts': opts, 'idx': idx,
                'exp': f"x = {a} × {b} = {ans}"
            })
            if len(questions) >= 12:
                break
        if len(questions) >= 12:
            break
    
    # (x + a)/b = c
    for b in range(2, 6):
        for c in range(1, 6):
            for a in range(1, 6):
                x = b * c - a
                if x > 0:
                    ans = str(x)
                    opts, idx = shuffle_options(ans, [str(x + 1), str(x - 1) if x > 1 else "0", str(b * c)])
                    questions.append({
                        'text': f"Solve: (x + {a})/{b} = {c}",
                        'opts': opts, 'idx': idx,
                        'exp': f"x + {a} = {b*c}, x = {ans}"
                    })
                if len(questions) >= 25:
                    break
            if len(questions) >= 25:
                break
        if len(questions) >= 25:
            break
    
    # ax/b = c (whole number answer)
    for a in range(2, 5):
        for b in range(2, 5):
            for x in range(1, 8):
                if (a * x) % b == 0:
                    c = (a * x) // b
                    ans = str(x)
                    opts, idx = shuffle_options(ans, [str(x + 1), str(c), str(a)])
                    questions.append({
                        'text': f"Solve: {a}x/{b} = {c}",
                        'opts': opts, 'idx': idx,
                        'exp': f"{a}x = {b*c}, x = {ans}"
                    })
                if len(questions) >= 38:
                    break
            if len(questions) >= 38:
                break
        if len(questions) >= 38:
            break
    
    # x/a + b = c
    for a in range(2, 6):
        for b in range(1, 5):
            for x_val in range(2, 10):
                if x_val % a == 0:
                    c = x_val // a + b
                    ans = str(x_val)
                    opts, idx = shuffle_options(ans, [str(x_val + a), str(c), str(a * c)])
                    questions.append({
                        'text': f"Solve: x/{a} + {b} = {c}",
                        'opts': opts, 'idx': idx,
                        'exp': f"x/{a} = {c - b}, x = {ans}"
                    })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_6():
    """Rearranging Formulae"""
    questions = []
    
    # Make x subject: y = x + a
    for a in range(1, 10):
        ans = f"x = y - {a}"
        opts, idx = shuffle_options(ans, [f"x = y + {a}", f"x = {a} - y", f"x = {a}y"])
        questions.append({
            'text': f"Make x the subject: y = x + {a}",
            'opts': opts, 'idx': idx,
            'exp': f"x = y - {a}"
        })
        if len(questions) >= 10:
            break
    
    # Make x subject: y = ax
    for a in range(2, 10):
        ans = f"x = y/{a}"
        opts, idx = shuffle_options(ans, [f"x = {a}y", f"x = y - {a}", f"x = y + {a}"])
        questions.append({
            'text': f"Make x the subject: y = {a}x",
            'opts': opts, 'idx': idx,
            'exp': f"x = y/{a}"
        })
        if len(questions) >= 18:
            break
    
    # Make x subject: y = x/a
    for a in range(2, 10):
        ans = f"x = {a}y"
        opts, idx = shuffle_options(ans, [f"x = y/{a}", f"x = y - {a}", f"x = y + {a}"])
        questions.append({
            'text': f"Make x the subject: y = x/{a}",
            'opts': opts, 'idx': idx,
            'exp': f"x = {a}y"
        })
        if len(questions) >= 26:
            break
    
    # y = ax + b
    for a in range(2, 6):
        for b in range(1, 6):
            ans = f"x = (y - {b})/{a}"
            opts, idx = shuffle_options(ans, [f"x = (y + {b})/{a}", f"x = y/{a} + {b}", f"x = {a}y - {b}"])
            questions.append({
                'text': f"Make x the subject: y = {a}x + {b}",
                'opts': opts, 'idx': idx,
                'exp': f"y - {b} = {a}x, x = (y - {b})/{a}"
            })
            if len(questions) >= 38:
                break
        if len(questions) >= 38:
            break
    
    # y = (x + a)/b
    for a in range(1, 6):
        for b in range(2, 6):
            ans = f"x = {b}y - {a}"
            opts, idx = shuffle_options(ans, [f"x = {b}y + {a}", f"x = y/{b} - {a}", f"x = (y - {a})/{b}"])
            questions.append({
                'text': f"Make x the subject: y = (x + {a})/{b}",
                'opts': opts, 'idx': idx,
                'exp': f"{b}y = x + {a}, x = {b}y - {a}"
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_7():
    """Simultaneous Equations"""
    questions = []
    
    # Simple: x + y = a, x - y = b (both even sum)
    for x in range(1, 8):
        for y in range(1, x):
            sum_val = x + y
            diff_val = x - y
            ans = f"x = {x}, y = {y}"
            opts, idx = shuffle_options(ans, [f"x = {y}, y = {x}", f"x = {sum_val}, y = {diff_val}", f"x = {x+1}, y = {y-1}"])
            questions.append({
                'text': f"Solve: x + y = {sum_val}, x - y = {diff_val}",
                'opts': opts, 'idx': idx,
                'exp': f"Add: 2x = {sum_val + diff_val}, x = {x}. Then y = {y}."
            })
            if len(questions) >= 15:
                break
        if len(questions) >= 15:
            break
    
    # x + y = a, 2x + y = b
    for x in range(1, 7):
        for y in range(1, 7):
            eq1 = x + y
            eq2 = 2*x + y
            ans = f"x = {x}, y = {y}"
            opts, idx = shuffle_options(ans, [f"x = {y}, y = {x}", f"x = {x+1}, y = {y-1}", f"x = {eq1}, y = {eq2}"])
            questions.append({
                'text': f"Solve: x + y = {eq1}, 2x + y = {eq2}",
                'opts': opts, 'idx': idx,
                'exp': f"Subtract: x = {x}. Then y = {y}."
            })
            if len(questions) >= 28:
                break
        if len(questions) >= 28:
            break
    
    # 2x + y = a, x + y = b
    for x in range(1, 6):
        for y in range(1, 6):
            eq1 = 2*x + y
            eq2 = x + y
            ans = f"x = {x}, y = {y}"
            opts, idx = shuffle_options(ans, [f"x = {y}, y = {x}", f"x = {x+1}, y = {y}", f"x = {eq2}, y = {eq1}"])
            questions.append({
                'text': f"Solve: 2x + y = {eq1}, x + y = {eq2}",
                'opts': opts, 'idx': idx,
                'exp': f"Subtract: x = {x}. Then y = {y}."
            })
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # 3x + 2y = a, x + y = b
    for x in range(1, 5):
        for y in range(1, 5):
            eq1 = 3*x + 2*y
            eq2 = x + y
            ans = f"x = {x}, y = {y}"
            opts, idx = shuffle_options(ans, [f"x = {y}, y = {x}", f"x = {x+1}, y = {y-1}", f"x = {eq2}, y = {x}"])
            questions.append({
                'text': f"Solve: 3x + 2y = {eq1}, x + y = {eq2}",
                'opts': opts, 'idx': idx,
                'exp': f"Multiply eq2 by 2, subtract: x = {x}, y = {y}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_8():
    """Quadratic Equations"""
    questions = []
    
    # x² = a (perfect squares)
    for a in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
        root = int(a ** 0.5)
        ans = f"x = ±{root}"
        opts, idx = shuffle_options(ans, [f"x = {root}", f"x = {a}", f"x = ±{a}"])
        questions.append({
            'text': f"Solve: x² = {a}",
            'opts': opts, 'idx': idx,
            'exp': f"x = ±√{a} = ±{root}"
        })
    
    # (x + a)² = b²
    for a in range(1, 6):
        for b in range(1, 6):
            ans = f"x = {b - a} or x = {-b - a}"
            opts, idx = shuffle_options(ans, [f"x = {b + a}", f"x = ±{b}", f"x = {a} or x = {b}"])
            questions.append({
                'text': f"Solve: (x + {a})² = {b*b}",
                'opts': opts, 'idx': idx,
                'exp': f"x + {a} = ±{b}, so x = {b-a} or x = {-b-a}"
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Factorised form (x - a)(x - b) = 0
    for a in range(1, 7):
        for b in range(a, 8):
            ans = f"x = {a} or x = {b}"
            opts, idx = shuffle_options(ans, [f"x = {a + b}", f"x = {a * b}", f"x = -{a} or x = -{b}"])
            questions.append({
                'text': f"Solve: (x - {a})(x - {b}) = 0",
                'opts': opts, 'idx': idx,
                'exp': f"x - {a} = 0 or x - {b} = 0"
            })
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # x² + bx + c = 0 (factorisable)
    pairs = [(1, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (3, 4), (1, 6), (2, 6)]
    for r1, r2 in pairs:
        b = r1 + r2
        c = r1 * r2
        ans = f"x = -{r1} or x = -{r2}"
        opts, idx = shuffle_options(ans, [f"x = {r1} or x = {r2}", f"x = {b} or x = {c}", f"x = -{b}"])
        questions.append({
            'text': f"Solve: x² + {b}x + {c} = 0",
            'opts': opts, 'idx': idx,
            'exp': f"(x + {r1})(x + {r2}) = 0"
        })
        if len(questions) >= 45:
            break
    
    # x² - bx + c = 0
    for r1, r2 in [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]:
        b = r1 + r2
        c = r1 * r2
        ans = f"x = {r1} or x = {r2}"
        opts, idx = shuffle_options(ans, [f"x = -{r1} or x = -{r2}", f"x = {b}", f"x = {c}"])
        questions.append({
            'text': f"Solve: x² - {b}x + {c} = 0",
            'opts': opts, 'idx': idx,
            'exp': f"(x - {r1})(x - {r2}) = 0"
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_9():
    """Inequalities"""
    questions = []
    
    # x + a > b
    for a in range(1, 8):
        for b in range(a + 1, 12):
            result = b - a
            ans = f"x > {result}"
            opts, idx = shuffle_options(ans, [f"x < {result}", f"x > {b}", f"x < {a}"])
            questions.append({
                'text': f"Solve: x + {a} > {b}",
                'opts': opts, 'idx': idx,
                'exp': f"x > {b} - {a} = {result}"
            })
            if len(questions) >= 12:
                break
        if len(questions) >= 12:
            break
    
    # x - a < b
    for a in range(1, 6):
        for b in range(1, 8):
            result = a + b
            ans = f"x < {result}"
            opts, idx = shuffle_options(ans, [f"x > {result}", f"x < {b}", f"x > {a}"])
            questions.append({
                'text': f"Solve: x - {a} < {b}",
                'opts': opts, 'idx': idx,
                'exp': f"x < {b} + {a} = {result}"
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # ax > b
    for a in range(2, 6):
        for mult in range(1, 7):
            b = a * mult
            ans = f"x > {mult}"
            opts, idx = shuffle_options(ans, [f"x < {mult}", f"x > {b}", f"x < {a}"])
            questions.append({
                'text': f"Solve: {a}x > {b}",
                'opts': opts, 'idx': idx,
                'exp': f"x > {b}/{a} = {mult}"
            })
            if len(questions) >= 32:
                break
        if len(questions) >= 32:
            break
    
    # ax + b < c
    for a in range(2, 5):
        for b in range(1, 5):
            for x in range(2, 7):
                c = a * x + b
                ans = f"x < {x}"
                opts, idx = shuffle_options(ans, [f"x > {x}", f"x < {c}", f"x > {b}"])
                questions.append({
                    'text': f"Solve: {a}x + {b} < {c}",
                    'opts': opts, 'idx': idx,
                    'exp': f"{a}x < {c - b}, x < {x}"
                })
                if len(questions) >= 42:
                    break
            if len(questions) >= 42:
                break
        if len(questions) >= 42:
            break
    
    # Double inequality a < x + b < c
    for b in range(1, 5):
        for low in range(1, 5):
            for high in range(low + 3, low + 8):
                ans = f"{low - b} < x < {high - b}"
                opts, idx = shuffle_options(ans, [f"{low} < x < {high}", f"x < {high - b}", f"x > {low - b}"])
                questions.append({
                    'text': f"Solve: {low} < x + {b} < {high}",
                    'opts': opts, 'idx': idx,
                    'exp': f"Subtract {b}: {low - b} < x < {high - b}"
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_10():
    """Algebraic Fractions"""
    questions = []
    
    # Simplify ax/bx
    for a in range(2, 8):
        for b in range(2, 8):
            if a != b:
                from math import gcd
                g = gcd(a, b)
                num, den = a // g, b // g
                expr = f"{a}x/{b}x"
                ans = f"{num}/{den}" if den != 1 else str(num)
                opts, idx = shuffle_options(ans, [f"{a}/{b}", f"x", f"{b}/{a}"])
                questions.append({
                    'text': f"Simplify: {expr}",
                    'opts': opts, 'idx': idx,
                    'exp': f"Cancel x: {a}/{b} = {ans}"
                })
                if len(questions) >= 12:
                    break
        if len(questions) >= 12:
            break
    
    # Simplify (ax + ab)/(cx + cb) = a/c
    for a in range(2, 6):
        for b in range(1, 5):
            for c in range(2, 6):
                if a != c:
                    expr = f"({a}x + {a*b})/({c}x + {c*b})"
                    from math import gcd
                    g = gcd(a, c)
                    ans = f"{a//g}/{c//g}" if c//g != 1 else str(a//g)
                    opts, idx = shuffle_options(ans, [f"{a}/{c}", f"x + {b}", f"{a*b}/{c*b}"])
                    questions.append({
                        'text': f"Simplify: {expr}",
                        'opts': opts, 'idx': idx,
                        'exp': f"Factor: {a}(x+{b})/{c}(x+{b}) = {ans}"
                    })
                    if len(questions) >= 25:
                        break
            if len(questions) >= 25:
                break
        if len(questions) >= 25:
            break
    
    # Add fractions with same denominator
    for d in range(2, 6):
        for a in range(1, 5):
            for b in range(1, 5):
                ans = f"{a + b}/{d}" if (a + b) % d != 0 else str((a + b) // d)
                opts, idx = shuffle_options(ans, [f"{a*b}/{d}", f"{a + b}/{d*2}", f"{a}/{d} + {b}/{d}"])
                questions.append({
                    'text': f"Simplify: {a}/{d} + {b}/{d}",
                    'opts': opts, 'idx': idx,
                    'exp': f"= {a + b}/{d}"
                })
                if len(questions) >= 38:
                    break
            if len(questions) >= 38:
                break
        if len(questions) >= 38:
            break
    
    # Cross multiply to solve
    for a in range(2, 5):
        for b in range(2, 5):
            for x in range(1, 6):
                c = a * x
                d = b * x
                ans = f"x = {x}"
                opts, idx = shuffle_options(str(x), [str(x + 1), str(x - 1) if x > 1 else "0", str(a)])
                questions.append({
                    'text': f"Solve: {c}/x = {a*b}/{b}",
                    'opts': opts, 'idx': idx,
                    'exp': f"{c} × {b} = {a*b} × x, x = {x}"
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_11():
    """Word Problems"""
    questions = []
    
    # Age problems
    for curr_age in range(10, 25):
        for years in range(3, 10):
            future_age = curr_age + years
            ans = str(curr_age)
            opts, idx = shuffle_options(ans, [str(future_age), str(curr_age - years), str(years)])
            questions.append({
                'text': f"In {years} years, Tom will be {future_age}. How old is he now?",
                'opts': opts, 'idx': idx,
                'exp': f"x + {years} = {future_age}, x = {curr_age}"
            })
            if len(questions) >= 10:
                break
        if len(questions) >= 10:
            break
    
    # Sum of consecutive numbers
    for start in range(5, 15):
        total = start + (start + 1) + (start + 2)
        ans = f"{start}, {start+1}, {start+2}"
        opts, idx = shuffle_options(ans, [f"{start-1}, {start}, {start+1}", f"{start+1}, {start+2}, {start+3}", f"{total//3}, {total//3}, {total//3}"])
        questions.append({
            'text': f"Three consecutive numbers sum to {total}. Find them.",
            'opts': opts, 'idx': idx,
            'exp': f"n + (n+1) + (n+2) = {total}, n = {start}"
        })
        if len(questions) >= 18:
            break
    
    # Cost problems
    for unit_cost in range(2, 8):
        for qty in range(3, 10):
            total = unit_cost * qty
            ans = f"€{unit_cost}"
            opts, idx = shuffle_options(ans, [f"€{total}", f"€{qty}", f"€{unit_cost + 1}"])
            questions.append({
                'text': f"{qty} items cost €{total}. Cost per item?",
                'opts': opts, 'idx': idx,
                'exp': f"{qty}x = {total}, x = €{unit_cost}"
            })
            if len(questions) >= 28:
                break
        if len(questions) >= 28:
            break
    
    # Rectangle problems
    for width in range(3, 8):
        for length in range(width + 2, width + 8):
            perimeter = 2 * (length + width)
            ans = f"{length} × {width}"
            opts, idx = shuffle_options(ans, [f"{width} × {length - 2}", f"{perimeter//4} × {perimeter//4}", f"{length + 1} × {width - 1}"])
            questions.append({
                'text': f"Rectangle: length = width + {length - width}, perimeter = {perimeter}. Dimensions?",
                'opts': opts, 'idx': idx,
                'exp': f"2(w + w + {length-width}) = {perimeter}, w = {width}, l = {length}"
            })
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # Number puzzles
    for n in range(5, 15):
        doubled_plus = 2 * n + 5
        ans = str(n)
        opts, idx = shuffle_options(ans, [str(n + 1), str(n - 1), str(doubled_plus)])
        questions.append({
            'text': f"Double a number and add 5 gives {doubled_plus}. The number?",
            'opts': opts, 'idx': idx,
            'exp': f"2x + 5 = {doubled_plus}, x = {n}"
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_12():
    """SEC Exam Style"""
    questions = []
    
    # Multi-step linear
    for a in range(2, 5):
        for b in range(1, 4):
            for c in range(2, 5):
                for x in range(1, 6):
                    lhs = a * x + b
                    rhs = c * x + (a - c) * x + b  # Always equals lhs
                    if a != c:
                        d = random.randint(1, 5)
                        rhs = c * x + d
                        if lhs != rhs:
                            # ax + b = cx + d => (a-c)x = d - b
                            if (a - c) != 0 and (d - b) % (a - c) == 0:
                                x_val = (d - b) // (a - c)
                                if x_val > 0:
                                    ans = str(x_val)
                                    opts, idx = shuffle_options(ans, [str(x_val + 1), str(x_val - 1) if x_val > 1 else "0", str(a)])
                                    questions.append({
                                        'text': f"Solve: {a}x + {b} = {c}x + {d}",
                                        'opts': opts, 'idx': idx,
                                        'exp': f"{a-c}x = {d-b}, x = {x_val}"
                                    })
                    if len(questions) >= 10:
                        break
                if len(questions) >= 10:
                    break
            if len(questions) >= 10:
                break
        if len(questions) >= 10:
            break
    
    # Quadratic from area
    for side in range(3, 8):
        area = side * side
        ans = str(side)
        opts, idx = shuffle_options(ans, [str(side + 1), str(area), str(side - 1)])
        questions.append({
            'text': f"Square has area {area} cm². Find side length.",
            'opts': opts, 'idx': idx,
            'exp': f"x² = {area}, x = {side}"
        })
    
    # Simultaneous from context
    for apples, oranges in [(3, 2), (4, 3), (5, 2), (2, 5)]:
        for apple_price, orange_price in [(2, 3), (3, 2), (4, 1), (1, 4)]:
            total1 = apples * apple_price + oranges * orange_price
            total2 = oranges * apple_price + apples * orange_price
            if total1 != total2:
                ans = f"Apple €{apple_price}, Orange €{orange_price}"
                opts, idx = shuffle_options(ans, [f"Apple €{orange_price}, Orange €{apple_price}", 
                                                   f"Apple €{apple_price + 1}, Orange €{orange_price - 1}",
                                                   f"Apple €{total1 // (apples + oranges)}, Orange €{total2 // (apples + oranges)}"])
                questions.append({
                    'text': f"{apples} apples + {oranges} oranges = €{total1}. {oranges} apples + {apples} oranges = €{total2}. Prices?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Solve simultaneously."
                })
                if len(questions) >= 22:
                    break
        if len(questions) >= 22:
            break
    
    # Factorising then solving
    for r1 in range(1, 6):
        for r2 in range(r1, 7):
            b = r1 + r2
            c = r1 * r2
            ans = f"x = {r1} or x = {r2}"
            opts, idx = shuffle_options(ans, [f"x = -{r1} or x = -{r2}", f"x = {b}", f"x = {c}"])
            questions.append({
                'text': f"Solve by factorising: x² - {b}x + {c} = 0",
                'opts': opts, 'idx': idx,
                'exp': f"(x - {r1})(x - {r2}) = 0"
            })
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Inequality word problem
    for budget in [50, 100, 150, 200]:
        for cost in range(5, 15):
            max_items = budget // cost
            ans = f"n ≤ {max_items}"
            opts, idx = shuffle_options(ans, [f"n ≤ {max_items + 1}", f"n = {max_items}", f"n ≥ {max_items}"])
            questions.append({
                'text': f"Budget €{budget}, item costs €{cost}. How many can you buy?",
                'opts': opts, 'idx': idx,
                'exp': f"{cost}n ≤ {budget}, n ≤ {max_items}"
            })
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # Expression simplification
    for a in range(2, 5):
        for b in range(1, 4):
            for c in range(1, 4):
                expanded = f"{a}x² + {a*b + c}x + {b*c}"
                ans = f"({a}x + {c})(x + {b})"
                opts, idx = shuffle_options(ans, [f"({a}x + {b})(x + {c})", f"{a}(x + {b})(x + {c})", f"(x + {a})({b}x + {c})"])
                questions.append({
                    'text': f"Factorise: {a}x² + {a*b + c}x + {b*c}",
                    'opts': opts, 'idx': idx,
                    'exp': f"= {ans}"
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]


def generate_all():
    all_q = []
    generators = [generate_level_1, generate_level_2, generate_level_3, generate_level_4,
                  generate_level_5, generate_level_6, generate_level_7, generate_level_8,
                  generate_level_9, generate_level_10, generate_level_11, generate_level_12]
    
    for level, gen in enumerate(generators, 1):
        qs = gen()
        name, band = LEVEL_CONFIG[level]
        for q in qs:
            q['level'] = level
            q['band'] = band
        all_q.extend(qs)
        print(f"Level {level:2d}: {len(qs):3d} - {name}")
    
    return all_q


def generate_sql(questions):
    lines = [
        "-- LC OL Algebra - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        "-- Create topic",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Algebra', {STRAND_ID}, '🔤', 9, 1);",
        "",
        "-- Clear existing",
        f"DELETE FROM questions_adaptive WHERE topic = '{TOPIC_ID}';",
        "",
    ]
    
    for q in questions:
        txt = q['text'].replace("'", "''")
        a = q['opts'][0].replace("'", "''")
        b = q['opts'][1].replace("'", "''")
        c = q['opts'][2].replace("'", "''")
        d = q['opts'][3].replace("'", "''")
        exp = q['exp'].replace("'", "''")
        
        sql = f"INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode) VALUES ('{TOPIC_ID}', '{txt}', '{a}', '{b}', '{c}', '{d}', {q['idx']}, '{exp}', {q['level']}, '{q['band']}', 'adaptive');"
        lines.append(sql)
    
    lines.append("")
    lines.append(f"SELECT COUNT(*) as total FROM questions_adaptive WHERE topic = '{TOPIC_ID}';")
    
    return '\n'.join(lines)


if __name__ == "__main__":
    print("="*60)
    print("LC OL Algebra - 600 Questions Generator")
    print("="*60 + "\n")
    
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    
    sql = generate_sql(questions)
    with open('lc_ol_algebra_600.sql', 'w') as f:
        f.write(sql)
    
    print(f"Saved: lc_ol_algebra_600.sql ({len(sql):,} chars)")
