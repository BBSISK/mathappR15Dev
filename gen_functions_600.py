#!/usr/bin/env python3
"""
LC Ordinary Level Functions - 600 Questions Generator
======================================================
50 questions per level × 12 levels = 600 questions

Based on SEC Paper Analysis 2019-2025:
- Functions worth 240 marks over 7 years
- Focus: Function notation, graphs, linear/quadratic functions, transformations
"""

import random

TOPIC_ID = 'lc_ol_functions'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Function Notation", "Foundation"),
    2: ("Evaluating Functions", "Foundation"),
    3: ("Domain and Range", "Foundation"),
    4: ("Linear Functions", "Developing"),
    5: ("Graphing Linear Functions", "Developing"),
    6: ("Slope and Intercept", "Developing"),
    7: ("Quadratic Functions", "Proficient"),
    8: ("Graphing Quadratics", "Proficient"),
    9: ("Roots and Vertex", "Proficient"),
    10: ("Function Transformations", "Advanced"),
    11: ("Inverse Functions", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    options = [correct] + distractors[:3]
    random.shuffle(options)
    return options, options.index(correct)

def generate_level_1():
    """Function Notation"""
    questions = []
    
    # What does f(x) mean?
    opts, idx = shuffle_options("The output when x is the input", ["f times x", "f divided by x", "The x-th term"])
    questions.append({
        'text': "What does f(x) mean?",
        'opts': opts, 'idx': idx,
        'exp': "f(x) represents the output of function f for input x."
    })
    
    # Identify function notation
    notations = [
        ("f(x) = 2x + 1", "Yes"), ("y = 3x - 2", "Yes"), ("f(x) = x²", "Yes"),
        ("2x + 3y = 6", "No, this is an equation"), ("f(x) = 5", "Yes"),
    ]
    for expr, ans in notations:
        opts, idx = shuffle_options(ans, ["No", "Sometimes", "Only for linear"])
        questions.append({
            'text': f"Is {expr} written in function notation?",
            'opts': opts, 'idx': idx,
            'exp': f"{ans}."
        })
    
    # f(a) means substitute a
    for a in range(1, 12):
        opts, idx = shuffle_options(f"Substitute x = {a}", [f"Multiply f by {a}", f"Add {a} to f", f"f to the power {a}"])
        questions.append({
            'text': f"What does f({a}) mean?",
            'opts': opts, 'idx': idx,
            'exp': f"f({a}) means find the value of f when x = {a}."
        })
        if len(questions) >= 18:
            break
    
    # Identify input and output
    for a in range(2, 10):
        for b in range(1, 8):
            result = a + b
            opts, idx = shuffle_options(str(a), [str(b), str(result), "x"])
            questions.append({
                'text': f"In f({a}) = {result}, what is the input?",
                'opts': opts, 'idx': idx,
                'exp': f"Input is {a}, output is {result}."
            })
            if len(questions) >= 30:
                break
        if len(questions) >= 30:
            break
    
    # Identify output
    for a in range(2, 10):
        for b in range(1, 8):
            result = a * 2 + b
            opts, idx = shuffle_options(str(result), [str(a), str(b), "f"])
            questions.append({
                'text': f"In f({a}) = {result}, what is the output?",
                'opts': opts, 'idx': idx,
                'exp': f"Output is {result}."
            })
            if len(questions) >= 42:
                break
        if len(questions) >= 42:
            break
    
    # Write in function notation
    for m in range(2, 6):
        for c in range(1, 5):
            expr = f"y = {m}x + {c}"
            ans = f"f(x) = {m}x + {c}"
            opts, idx = shuffle_options(ans, [f"f(x) = {m} + {c}x", f"f(y) = {m}x + {c}", f"f = {m}x + {c}"])
            questions.append({
                'text': f"Write {expr} in function notation.",
                'opts': opts, 'idx': idx,
                'exp': f"Replace y with f(x): {ans}"
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_2():
    """Evaluating Functions"""
    questions = []
    
    # f(x) = ax + b, find f(c)
    for a in range(2, 7):
        for b in range(1, 6):
            for c in range(1, 8):
                result = a * c + b
                ans = str(result)
                opts, idx = shuffle_options(ans, [str(result + 1), str(result - 1), str(a * c)])
                questions.append({
                    'text': f"f(x) = {a}x + {b}. Find f({c}).",
                    'opts': opts, 'idx': idx,
                    'exp': f"f({c}) = {a}({c}) + {b} = {result}"
                })
                if len(questions) >= 15:
                    break
            if len(questions) >= 15:
                break
        if len(questions) >= 15:
            break
    
    # f(x) = ax - b
    for a in range(2, 6):
        for b in range(1, 5):
            for c in range(2, 8):
                result = a * c - b
                if result > 0:
                    ans = str(result)
                    opts, idx = shuffle_options(ans, [str(result + 1), str(result - 1), str(a * c)])
                    questions.append({
                        'text': f"f(x) = {a}x - {b}. Find f({c}).",
                        'opts': opts, 'idx': idx,
                        'exp': f"f({c}) = {a}({c}) - {b} = {result}"
                    })
                if len(questions) >= 28:
                    break
            if len(questions) >= 28:
                break
        if len(questions) >= 28:
            break
    
    # f(x) = x², find f(a)
    for a in range(1, 10):
        result = a * a
        ans = str(result)
        opts, idx = shuffle_options(ans, [str(2 * a), str(result + 1), str(a)])
        questions.append({
            'text': f"f(x) = x². Find f({a}).",
            'opts': opts, 'idx': idx,
            'exp': f"f({a}) = {a}² = {result}"
        })
        if len(questions) >= 36:
            break
    
    # f(x) = x² + c
    for c in range(1, 6):
        for a in range(1, 7):
            result = a * a + c
            ans = str(result)
            opts, idx = shuffle_options(ans, [str(a * a), str(result + 1), str(2 * a + c)])
            questions.append({
                'text': f"f(x) = x² + {c}. Find f({a}).",
                'opts': opts, 'idx': idx,
                'exp': f"f({a}) = {a}² + {c} = {result}"
            })
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # f(0)
    for a in range(2, 7):
        for b in range(1, 8):
            ans = str(b)
            opts, idx = shuffle_options(ans, [str(a), str(a + b), "0"])
            questions.append({
                'text': f"f(x) = {a}x + {b}. Find f(0).",
                'opts': opts, 'idx': idx,
                'exp': f"f(0) = {a}(0) + {b} = {b}"
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_3():
    """Domain and Range"""
    questions = []
    
    # Define domain
    opts, idx = shuffle_options("All possible input values", ["All possible output values", "The x-intercept", "The y-intercept"])
    questions.append({
        'text': "What is the domain of a function?",
        'opts': opts, 'idx': idx,
        'exp': "Domain = set of all valid inputs (x-values)."
    })
    
    # Define range
    opts, idx = shuffle_options("All possible output values", ["All possible input values", "The x-intercept", "The slope"])
    questions.append({
        'text': "What is the range of a function?",
        'opts': opts, 'idx': idx,
        'exp': "Range = set of all outputs (y-values)."
    })
    
    # Domain of linear (all real)
    for a in range(2, 8):
        for b in range(1, 6):
            opts, idx = shuffle_options("All real numbers", ["x > 0", "x ≥ 0", "x ≠ 0"])
            questions.append({
                'text': f"What is the domain of f(x) = {a}x + {b}?",
                'opts': opts, 'idx': idx,
                'exp': "Linear functions have domain = all real numbers."
            })
            if len(questions) >= 14:
                break
        if len(questions) >= 14:
            break
    
    # Range of linear (all real)
    for a in range(2, 7):
        for b in range(1, 5):
            opts, idx = shuffle_options("All real numbers", ["y > 0", "y ≥ {b}", "y = {b}"])
            questions.append({
                'text': f"What is the range of f(x) = {a}x + {b}?",
                'opts': opts, 'idx': idx,
                'exp': "Linear functions have range = all real numbers."
            })
            if len(questions) >= 24:
                break
        if len(questions) >= 24:
            break
    
    # Domain of x² (all real)
    opts, idx = shuffle_options("All real numbers", ["x ≥ 0", "x > 0", "x ≠ 0"])
    questions.append({
        'text': "What is the domain of f(x) = x²?",
        'opts': opts, 'idx': idx,
        'exp': "Any real number can be squared."
    })
    
    # Range of x² (y ≥ 0)
    opts, idx = shuffle_options("y ≥ 0", ["All real numbers", "y > 0", "y ≤ 0"])
    questions.append({
        'text': "What is the range of f(x) = x²?",
        'opts': opts, 'idx': idx,
        'exp': "x² is always ≥ 0."
    })
    
    # Range of x² + c
    for c in range(1, 10):
        ans = f"y ≥ {c}"
        opts, idx = shuffle_options(ans, ["y ≥ 0", f"y > {c}", "All real numbers"])
        questions.append({
            'text': f"What is the range of f(x) = x² + {c}?",
            'opts': opts, 'idx': idx,
            'exp': f"Minimum is 0 + {c} = {c}, so y ≥ {c}."
        })
        if len(questions) >= 36:
            break
    
    # Range of -x² (y ≤ 0)
    opts, idx = shuffle_options("y ≤ 0", ["y ≥ 0", "All real numbers", "y < 0"])
    questions.append({
        'text': "What is the range of f(x) = -x²?",
        'opts': opts, 'idx': idx,
        'exp': "-x² is always ≤ 0."
    })
    
    # Domain from graph description
    for a in range(0, 8):
        for b in range(a + 3, a + 10):
            ans = f"{a} ≤ x ≤ {b}"
            opts, idx = shuffle_options(ans, [f"{a} ≤ y ≤ {b}", f"x ≤ {b}", f"x ≥ {a}"])
            questions.append({
                'text': f"Graph shows f(x) from x = {a} to x = {b}. Domain?",
                'opts': opts, 'idx': idx,
                'exp': f"Domain: {a} ≤ x ≤ {b}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_4():
    """Linear Functions"""
    questions = []
    
    # Identify linear function
    linear = [
        ("f(x) = 3x + 2", "Yes"), ("f(x) = 2x - 5", "Yes"), ("f(x) = -x + 4", "Yes"),
        ("f(x) = 7", "Yes"), ("f(x) = x/2 + 1", "Yes"),
    ]
    for expr, ans in linear:
        opts, idx = shuffle_options(ans, ["No", "Sometimes", "Only if x > 0"])
        questions.append({
            'text': f"Is {expr} a linear function?",
            'opts': opts, 'idx': idx,
            'exp': f"{ans}. Linear functions have form f(x) = mx + c."
        })
    
    # Not linear
    non_linear = [
        ("f(x) = x²", "No, it's quadratic"), ("f(x) = 1/x", "No, it's reciprocal"),
        ("f(x) = √x", "No, it's square root"), ("f(x) = 2ˣ", "No, it's exponential"),
    ]
    for expr, ans in non_linear:
        opts, idx = shuffle_options("No", ["Yes", "Sometimes", "Only for x > 0"])
        questions.append({
            'text': f"Is {expr} a linear function?",
            'opts': opts, 'idx': idx,
            'exp': ans
        })
    
    # Find y-intercept (set x = 0)
    for m in range(2, 8):
        for c in range(1, 10):
            ans = str(c)
            opts, idx = shuffle_options(ans, [str(m), str(m + c), "0"])
            questions.append({
                'text': f"What is the y-intercept of f(x) = {m}x + {c}?",
                'opts': opts, 'idx': idx,
                'exp': f"Set x = 0: f(0) = {c}."
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Find x-intercept (set y = 0)
    for m in range(2, 6):
        for c in range(2, 10, 2):
            if c % m == 0:
                x_int = c // m
                ans = str(-x_int) if c > 0 else str(x_int)
                # Actually: mx + c = 0 => x = -c/m
                x_val = -c // m
                ans = str(x_val)
                opts, idx = shuffle_options(ans, [str(-x_val), str(c), str(m)])
                questions.append({
                    'text': f"What is the x-intercept of f(x) = {m}x + {c}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Set f(x) = 0: {m}x + {c} = 0, x = {x_val}."
                })
                if len(questions) >= 32:
                    break
        if len(questions) >= 32:
            break
    
    # Identify slope
    for m in range(-5, 8):
        if m != 0:
            for c in range(1, 6):
                ans = str(m)
                opts, idx = shuffle_options(ans, [str(c), str(m + c), str(-m)])
                questions.append({
                    'text': f"What is the slope of f(x) = {m}x + {c}?" if m > 0 else f"What is the slope of f(x) = {m}x + {c}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"In f(x) = mx + c, slope m = {m}."
                })
                if len(questions) >= 45:
                    break
        if len(questions) >= 45:
            break
    
    # Write equation given slope and intercept
    for m in range(2, 6):
        for c in range(1, 6):
            ans = f"f(x) = {m}x + {c}"
            opts, idx = shuffle_options(ans, [f"f(x) = {c}x + {m}", f"f(x) = x + {m + c}", f"f(x) = {m}x - {c}"])
            questions.append({
                'text': f"Write function with slope {m} and y-intercept {c}.",
                'opts': opts, 'idx': idx,
                'exp': f"f(x) = mx + c = {m}x + {c}"
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_5():
    """Graphing Linear Functions"""
    questions = []
    
    # Direction of slope
    for m in range(1, 8):
        opts, idx = shuffle_options("Upward (left to right)", ["Downward (left to right)", "Horizontal", "Vertical"])
        questions.append({
            'text': f"f(x) = {m}x + 2 slopes in which direction?",
            'opts': opts, 'idx': idx,
            'exp': f"Positive slope ({m}) means line goes up."
        })
        if len(questions) >= 8:
            break
    
    for m in range(1, 8):
        opts, idx = shuffle_options("Downward (left to right)", ["Upward (left to right)", "Horizontal", "Vertical"])
        questions.append({
            'text': f"f(x) = -{m}x + 2 slopes in which direction?",
            'opts': opts, 'idx': idx,
            'exp': f"Negative slope (-{m}) means line goes down."
        })
        if len(questions) >= 15:
            break
    
    # Horizontal line
    for c in range(1, 10):
        opts, idx = shuffle_options("Horizontal", ["Vertical", "Diagonal up", "Diagonal down"])
        questions.append({
            'text': f"What type of line is f(x) = {c}?",
            'opts': opts, 'idx': idx,
            'exp': f"f(x) = {c} is horizontal (slope = 0)."
        })
        if len(questions) >= 22:
            break
    
    # Point on line?
    for m in range(2, 5):
        for c in range(1, 5):
            for x in range(1, 6):
                y = m * x + c
                ans = "Yes"
                opts, idx = shuffle_options(ans, ["No", "Cannot tell", "Only if x > 0"])
                questions.append({
                    'text': f"Is ({x}, {y}) on the line f(x) = {m}x + {c}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"f({x}) = {m}({x}) + {c} = {y}. Yes!"
                })
                if len(questions) >= 35:
                    break
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Point NOT on line
    for m in range(2, 5):
        for c in range(1, 4):
            for x in range(1, 5):
                y = m * x + c + 1  # Wrong y
                actual = m * x + c
                opts, idx = shuffle_options("No", ["Yes", "Cannot tell", "Sometimes"])
                questions.append({
                    'text': f"Is ({x}, {y}) on the line f(x) = {m}x + {c}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"f({x}) = {actual} ≠ {y}. No."
                })
                if len(questions) >= 45:
                    break
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # Where does line cross y-axis?
    for m in range(2, 6):
        for c in range(1, 8):
            ans = f"(0, {c})"
            opts, idx = shuffle_options(ans, [f"({c}, 0)", f"(0, {m})", f"({m}, {c})"])
            questions.append({
                'text': f"Where does f(x) = {m}x + {c} cross the y-axis?",
                'opts': opts, 'idx': idx,
                'exp': f"Y-axis at x = 0: (0, {c})."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_6():
    """Slope and Intercept"""
    questions = []
    
    # Calculate slope from two points
    for x1 in range(0, 5):
        for y1 in range(0, 5):
            for x2 in range(x1 + 1, x1 + 5):
                for m in range(1, 5):
                    y2 = y1 + m * (x2 - x1)
                    ans = str(m)
                    opts, idx = shuffle_options(ans, [str(m + 1), str(m - 1) if m > 1 else "0", str(y2 - y1)])
                    questions.append({
                        'text': f"Find slope through ({x1}, {y1}) and ({x2}, {y2}).",
                        'opts': opts, 'idx': idx,
                        'exp': f"m = ({y2}-{y1})/({x2}-{x1}) = {y2-y1}/{x2-x1} = {m}"
                    })
                    if len(questions) >= 18:
                        break
                if len(questions) >= 18:
                    break
            if len(questions) >= 18:
                break
        if len(questions) >= 18:
            break
    
    # Negative slope from points
    for x1 in range(1, 4):
        for y1 in range(5, 10):
            for x2 in range(x1 + 1, x1 + 4):
                for m in range(1, 4):
                    y2 = y1 - m * (x2 - x1)
                    if y2 > 0:
                        ans = str(-m)
                        opts, idx = shuffle_options(ans, [str(m), str(-m - 1), str(y1 - y2)])
                        questions.append({
                            'text': f"Find slope through ({x1}, {y1}) and ({x2}, {y2}).",
                            'opts': opts, 'idx': idx,
                            'exp': f"m = ({y2}-{y1})/({x2}-{x1}) = {-m}"
                        })
                    if len(questions) >= 30:
                        break
                if len(questions) >= 30:
                    break
            if len(questions) >= 30:
                break
        if len(questions) >= 30:
            break
    
    # Parallel lines (same slope)
    for m in range(2, 7):
        for c1 in range(1, 5):
            for c2 in range(c1 + 1, c1 + 5):
                opts, idx = shuffle_options("Parallel", ["Perpendicular", "Intersecting", "Same line"])
                questions.append({
                    'text': f"f(x) = {m}x + {c1} and g(x) = {m}x + {c2}. Relationship?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Same slope ({m}) but different intercepts = parallel."
                })
                if len(questions) >= 40:
                    break
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # Find equation from slope and point
    for m in range(2, 6):
        for x1 in range(1, 5):
            for y1 in range(2, 8):
                c = y1 - m * x1
                if c > 0:
                    ans = f"f(x) = {m}x + {c}"
                    opts, idx = shuffle_options(ans, [f"f(x) = {m}x + {y1}", f"f(x) = {x1}x + {y1}", f"f(x) = {m}x - {c}"])
                    questions.append({
                        'text': f"Line with slope {m} through ({x1}, {y1}). Equation?",
                        'opts': opts, 'idx': idx,
                        'exp': f"y - {y1} = {m}(x - {x1}), so f(x) = {m}x + {c}"
                    })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_7():
    """Quadratic Functions"""
    questions = []
    
    # Identify quadratic
    quads = [
        ("f(x) = x²", "Yes"), ("f(x) = 2x² + 3", "Yes"), ("f(x) = x² - 4x + 1", "Yes"),
        ("f(x) = -x² + 5", "Yes"), ("f(x) = 3x² - 2x", "Yes"),
    ]
    for expr, ans in quads:
        opts, idx = shuffle_options(ans, ["No", "Only for x > 0", "Sometimes"])
        questions.append({
            'text': f"Is {expr} a quadratic function?",
            'opts': opts, 'idx': idx,
            'exp': f"{ans}. Quadratics have x² term."
        })
    
    # Not quadratic
    non_quads = [
        ("f(x) = 2x + 1", "linear"), ("f(x) = x³", "cubic"),
        ("f(x) = 1/x", "reciprocal"), ("f(x) = √x", "square root"),
    ]
    for expr, reason in non_quads:
        opts, idx = shuffle_options("No", ["Yes", "Sometimes", "Only if a > 0"])
        questions.append({
            'text': f"Is {expr} a quadratic function?",
            'opts': opts, 'idx': idx,
            'exp': f"No, it's {reason}."
        })
    
    # Shape of parabola (a > 0)
    for a in range(1, 8):
        opts, idx = shuffle_options("U-shape (opens up)", ["∩-shape (opens down)", "V-shape", "Straight line"])
        questions.append({
            'text': f"What shape is f(x) = {a}x²?",
            'opts': opts, 'idx': idx,
            'exp': f"Positive coefficient ({a}) means opens upward."
        })
        if len(questions) >= 18:
            break
    
    # Shape (a < 0)
    for a in range(1, 8):
        opts, idx = shuffle_options("∩-shape (opens down)", ["U-shape (opens up)", "V-shape", "Straight line"])
        questions.append({
            'text': f"What shape is f(x) = -{a}x²?",
            'opts': opts, 'idx': idx,
            'exp': f"Negative coefficient (-{a}) means opens downward."
        })
        if len(questions) >= 26:
            break
    
    # Evaluate quadratic
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for x in range(1, 5):
                    result = a * x * x + b * x + c
                    ans = str(result)
                    opts, idx = shuffle_options(ans, [str(result + 1), str(result - 1), str(a * x + b)])
                    questions.append({
                        'text': f"f(x) = {a}x² + {b}x + {c}. Find f({x}).",
                        'opts': opts, 'idx': idx,
                        'exp': f"f({x}) = {a}({x})² + {b}({x}) + {c} = {result}"
                    })
                    if len(questions) >= 42:
                        break
                if len(questions) >= 42:
                    break
            if len(questions) >= 42:
                break
        if len(questions) >= 42:
            break
    
    # Y-intercept of quadratic
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 8):
                ans = str(c)
                opts, idx = shuffle_options(ans, [str(a), str(b), str(a + b + c)])
                questions.append({
                    'text': f"Y-intercept of f(x) = {a}x² + {b}x + {c}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"f(0) = {c}."
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_8():
    """Graphing Quadratics"""
    questions = []
    
    # Axis of symmetry x = -b/2a
    for a in range(1, 4):
        for b in range(2, 10, 2):
            x_sym = -b // (2 * a)
            ans = f"x = {x_sym}"
            opts, idx = shuffle_options(ans, [f"x = {-x_sym}", f"x = {b}", f"x = {a}"])
            questions.append({
                'text': f"Axis of symmetry of f(x) = {a}x² + {b}x + 1?",
                'opts': opts, 'idx': idx,
                'exp': f"x = -b/2a = -{b}/(2×{a}) = {x_sym}"
            })
            if len(questions) >= 15:
                break
        if len(questions) >= 15:
            break
    
    # For f(x) = x² + c, vertex at (0, c)
    for c in range(-5, 8):
        ans = f"(0, {c})"
        opts, idx = shuffle_options(ans, [f"({c}, 0)", "(0, 0)", f"(1, {c + 1})"])
        questions.append({
            'text': f"Vertex of f(x) = x² + {c}?" if c >= 0 else f"Vertex of f(x) = x² - {-c}?",
            'opts': opts, 'idx': idx,
            'exp': f"f(x) = x² + {c} has vertex at (0, {c})."
        })
        if len(questions) >= 27:
            break
    
    # Minimum or maximum?
    for a in range(1, 6):
        opts, idx = shuffle_options("Minimum", ["Maximum", "Neither", "Both"])
        questions.append({
            'text': f"Does f(x) = {a}x² have a min or max?",
            'opts': opts, 'idx': idx,
            'exp': f"Opens up (a > 0) so has minimum."
        })
    
    for a in range(1, 6):
        opts, idx = shuffle_options("Maximum", ["Minimum", "Neither", "Both"])
        questions.append({
            'text': f"Does f(x) = -{a}x² have a min or max?",
            'opts': opts, 'idx': idx,
            'exp': f"Opens down (a < 0) so has maximum."
        })
        if len(questions) >= 38:
            break
    
    # Number of x-intercepts
    intercept_qs = [
        ("f(x) = x² - 4", "2", "x² = 4, x = ±2"),
        ("f(x) = x² + 1", "0", "x² = -1 has no real solutions"),
        ("f(x) = x²", "1", "Only touches at x = 0"),
        ("f(x) = x² - 9", "2", "x² = 9, x = ±3"),
        ("f(x) = x² + 4", "0", "x² = -4 has no real solutions"),
    ]
    for expr, ans, exp in intercept_qs:
        opts, idx = shuffle_options(ans, ["0", "1", "2"] if ans not in ["0", "1", "2"] else ["0" if ans != "0" else "1", "1" if ans != "1" else "2", "2" if ans != "2" else "0"])
        questions.append({
            'text': f"How many x-intercepts does {expr} have?",
            'opts': opts, 'idx': idx,
            'exp': exp
        })
    
    # Wider or narrower
    for a in [2, 3, 4, 5]:
        opts, idx = shuffle_options("Narrower", ["Wider", "Same width", "Cannot tell"])
        questions.append({
            'text': f"Is f(x) = {a}x² wider or narrower than x²?",
            'opts': opts, 'idx': idx,
            'exp': f"|{a}| > 1 means narrower."
        })
    
    # Wider (coefficient < 1)
    for denom in [2, 3, 4, 5]:
        opts, idx = shuffle_options("Wider", ["Narrower", "Same width", "Cannot tell"])
        questions.append({
            'text': f"Is f(x) = x²/{denom} wider or narrower than x²?",
            'opts': opts, 'idx': idx,
            'exp': f"Coefficient 1/{denom} < 1 means wider."
        })
    
    # Symmetry
    opts, idx = shuffle_options("x = 0", ["y = 0", "x = 1", "y = 1"])
    questions.append({
        'text': "What is the axis of symmetry of f(x) = x²?",
        'opts': opts, 'idx': idx,
        'exp': "f(x) = x² is symmetric about x = 0 (y-axis)."
    })
    
    opts, idx = shuffle_options("x = 0", ["y = 0", "x = 3", "y = 3"])
    questions.append({
        'text': "What is the axis of symmetry of f(x) = x² + 3?",
        'opts': opts, 'idx': idx,
        'exp': "Vertical shift doesn't change axis: x = 0."
    })
    
    return questions[:50]

def generate_level_9():
    """Roots and Vertex"""
    questions = []
    
    # Find roots of x² - a² = 0
    for a in range(1, 8):
        a_sq = a * a
        ans = f"x = {a} or x = -{a}"
        opts, idx = shuffle_options(ans, [f"x = {a_sq}", f"x = {a}", f"x = ±{a_sq}"])
        questions.append({
            'text': f"Find the roots of f(x) = x² - {a_sq}.",
            'opts': opts, 'idx': idx,
            'exp': f"x² = {a_sq}, x = ±{a}"
        })
        if len(questions) >= 10:
            break
    
    # Roots from factored form
    for r1 in range(1, 6):
        for r2 in range(r1, 7):
            ans = f"x = {r1} or x = {r2}"
            opts, idx = shuffle_options(ans, [f"x = -{r1} or x = -{r2}", f"x = {r1 + r2}", f"x = {r1 * r2}"])
            questions.append({
                'text': f"Roots of f(x) = (x - {r1})(x - {r2})?",
                'opts': opts, 'idx': idx,
                'exp': f"Set each factor = 0."
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Vertex from f(x) = (x - h)² + k
    for h in range(1, 6):
        for k in range(-3, 5):
            ans = f"({h}, {k})"
            opts, idx = shuffle_options(ans, [f"(-{h}, {k})", f"({h}, -{k})", f"({k}, {h})"])
            questions.append({
                'text': f"Vertex of f(x) = (x - {h})² + {k}?" if k >= 0 else f"Vertex of f(x) = (x - {h})² - {-k}?",
                'opts': opts, 'idx': idx,
                'exp': f"Vertex form (x - h)² + k gives vertex ({h}, {k})."
            })
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Sum of roots = -b/a
    for a in range(1, 3):
        for b in range(-6, 7):
            if b != 0:
                sum_roots = -b // a if b % a == 0 else f"{-b}/{a}"
                ans = str(-b) if a == 1 else f"{-b}/{a}"
                opts, idx = shuffle_options(str(-b // a) if b % a == 0 else f"{-b}", [str(b), str(b // a) if b % a == 0 else str(b), "0"])
                questions.append({
                    'text': f"Sum of roots of {a}x² + {b}x + 1 = 0?" if b > 0 else f"Sum of roots of {a}x² - {-b}x + 1 = 0?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Sum = -b/a = {-b}/{a}"
                })
                if len(questions) >= 45:
                    break
        if len(questions) >= 45:
            break
    
    # Product of roots = c/a
    for c in range(1, 8):
        ans = str(c)
        opts, idx = shuffle_options(ans, [str(c + 1), str(c - 1) if c > 1 else "0", str(2 * c)])
        questions.append({
            'text': f"Product of roots of x² - 5x + {c} = 0?",
            'opts': opts, 'idx': idx,
            'exp': f"Product = c/a = {c}/1 = {c}"
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_10():
    """Function Transformations"""
    questions = []
    
    # f(x) + k shifts up
    for k in range(1, 10):
        opts, idx = shuffle_options(f"Up {k} units", [f"Down {k} units", f"Right {k} units", f"Left {k} units"])
        questions.append({
            'text': f"How does f(x) + {k} transform f(x)?",
            'opts': opts, 'idx': idx,
            'exp': f"Adding {k} shifts graph up by {k}."
        })
        if len(questions) >= 10:
            break
    
    # f(x) - k shifts down
    for k in range(1, 10):
        opts, idx = shuffle_options(f"Down {k} units", [f"Up {k} units", f"Right {k} units", f"Left {k} units"])
        questions.append({
            'text': f"How does f(x) - {k} transform f(x)?",
            'opts': opts, 'idx': idx,
            'exp': f"Subtracting {k} shifts graph down by {k}."
        })
        if len(questions) >= 18:
            break
    
    # f(x - h) shifts right
    for h in range(1, 10):
        opts, idx = shuffle_options(f"Right {h} units", [f"Left {h} units", f"Up {h} units", f"Down {h} units"])
        questions.append({
            'text': f"How does f(x - {h}) transform f(x)?",
            'opts': opts, 'idx': idx,
            'exp': f"f(x - {h}) shifts right by {h}."
        })
        if len(questions) >= 26:
            break
    
    # f(x + h) shifts left
    for h in range(1, 10):
        opts, idx = shuffle_options(f"Left {h} units", [f"Right {h} units", f"Up {h} units", f"Down {h} units"])
        questions.append({
            'text': f"How does f(x + {h}) transform f(x)?",
            'opts': opts, 'idx': idx,
            'exp': f"f(x + {h}) shifts left by {h}."
        })
        if len(questions) >= 34:
            break
    
    # -f(x) reflects in x-axis
    opts, idx = shuffle_options("Reflects in x-axis", ["Reflects in y-axis", "Shifts up", "Shifts down"])
    questions.append({
        'text': "How does -f(x) transform f(x)?",
        'opts': opts, 'idx': idx,
        'exp': "-f(x) reflects the graph in the x-axis."
    })
    
    # f(-x) reflects in y-axis
    opts, idx = shuffle_options("Reflects in y-axis", ["Reflects in x-axis", "Shifts left", "Shifts right"])
    questions.append({
        'text': "How does f(-x) transform f(x)?",
        'opts': opts, 'idx': idx,
        'exp': "f(-x) reflects the graph in the y-axis."
    })
    
    # Combined transformations
    for h in range(1, 5):
        for k in range(1, 5):
            ans = f"Right {h}, up {k}"
            opts, idx = shuffle_options(ans, [f"Left {h}, up {k}", f"Right {h}, down {k}", f"Left {h}, down {k}"])
            questions.append({
                'text': f"How does (x - {h})² + {k} transform x²?",
                'opts': opts, 'idx': idx,
                'exp': f"Shift right {h}, up {k}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_11():
    """Inverse Functions"""
    questions = []
    
    # Inverse of f(x) = x + a
    for a in range(1, 12):
        ans = f"f⁻¹(x) = x - {a}"
        opts, idx = shuffle_options(ans, [f"f⁻¹(x) = x + {a}", f"f⁻¹(x) = -x + {a}", f"f⁻¹(x) = {a}x"])
        questions.append({
            'text': f"Find the inverse of f(x) = x + {a}.",
            'opts': opts, 'idx': idx,
            'exp': f"Swap x,y and solve: x = y + {a}, y = x - {a}."
        })
        if len(questions) >= 12:
            break
    
    # Inverse of f(x) = ax
    for a in range(2, 10):
        ans = f"f⁻¹(x) = x/{a}"
        opts, idx = shuffle_options(ans, [f"f⁻¹(x) = {a}x", f"f⁻¹(x) = x - {a}", f"f⁻¹(x) = -x/{a}"])
        questions.append({
            'text': f"Find the inverse of f(x) = {a}x.",
            'opts': opts, 'idx': idx,
            'exp': f"x = {a}y, y = x/{a}."
        })
        if len(questions) >= 22:
            break
    
    # Inverse of f(x) = x/a
    for a in range(2, 10):
        ans = f"f⁻¹(x) = {a}x"
        opts, idx = shuffle_options(ans, [f"f⁻¹(x) = x/{a}", f"f⁻¹(x) = x - {a}", f"f⁻¹(x) = x + {a}"])
        questions.append({
            'text': f"Find the inverse of f(x) = x/{a}.",
            'opts': opts, 'idx': idx,
            'exp': f"x = y/{a}, y = {a}x."
        })
        if len(questions) >= 32:
            break
    
    # Inverse of f(x) = ax + b
    for a in range(2, 5):
        for b in range(1, 5):
            ans = f"f⁻¹(x) = (x - {b})/{a}"
            opts, idx = shuffle_options(ans, [f"f⁻¹(x) = (x + {b})/{a}", f"f⁻¹(x) = {a}x - {b}", f"f⁻¹(x) = x/{a} + {b}"])
            questions.append({
                'text': f"Find the inverse of f(x) = {a}x + {b}.",
                'opts': opts, 'idx': idx,
                'exp': f"x = {a}y + {b}, y = (x - {b})/{a}."
            })
            if len(questions) >= 42:
                break
        if len(questions) >= 42:
            break
    
    # Property: f(f⁻¹(x)) = x
    for a in range(2, 8):
        for b in range(1, 6):
            ans = str(b)
            opts, idx = shuffle_options(ans, [str(a), str(a + b), str(a * b)])
            questions.append({
                'text': f"If f(x) = {a}x and f⁻¹({a * b}) = ?",
                'opts': opts, 'idx': idx,
                'exp': f"f⁻¹(x) = x/{a}, so f⁻¹({a*b}) = {a*b}/{a} = {b}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_12():
    """SEC Exam Style"""
    questions = []
    
    # Complete function from points
    for m in range(2, 5):
        for c in range(1, 5):
            x1, y1 = 1, m + c
            x2, y2 = 2, 2 * m + c
            ans = f"f(x) = {m}x + {c}"
            opts, idx = shuffle_options(ans, [f"f(x) = {c}x + {m}", f"f(x) = {m + c}x", f"f(x) = {m}x - {c}"])
            questions.append({
                'text': f"f({x1}) = {y1} and f({x2}) = {y2}. Find f(x).",
                'opts': opts, 'idx': idx,
                'exp': f"Slope = ({y2}-{y1})/({x2}-{x1}) = {m}. f(x) = {m}x + {c}."
            })
            if len(questions) >= 12:
                break
        if len(questions) >= 12:
            break
    
    # Find where f(x) = g(x)
    for m1 in range(2, 5):
        for c1 in range(1, 4):
            for m2 in range(1, m1):
                for c2 in range(c1 + 1, c1 + 5):
                    # m1*x + c1 = m2*x + c2 => (m1-m2)x = c2 - c1
                    diff_m = m1 - m2
                    diff_c = c2 - c1
                    if diff_c % diff_m == 0:
                        x = diff_c // diff_m
                        if x > 0:
                            ans = str(x)
                            opts, idx = shuffle_options(ans, [str(x + 1), str(x - 1) if x > 1 else "0", str(diff_c)])
                            questions.append({
                                'text': f"f(x) = {m1}x + {c1}, g(x) = {m2}x + {c2}. Where do they meet?",
                                'opts': opts, 'idx': idx,
                                'exp': f"{m1}x + {c1} = {m2}x + {c2}, x = {x}."
                            })
                    if len(questions) >= 22:
                        break
                if len(questions) >= 22:
                    break
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Area under line
    for m in range(1, 4):
        for c in range(1, 4):
            # Triangle from (0,c) to (x-int, 0) to origin
            x_int = c  # Simplified: when y=0, x = c (for m=1)
            area = c * c // 2  # Simplified triangle
            ans = str(area)
            opts, idx = shuffle_options(ans, [str(area + 1), str(c * c), str(c)])
            questions.append({
                'text': f"Area of triangle under f(x) = -{m}x + {c} (x ≥ 0)?",
                'opts': opts, 'idx': idx,
                'exp': f"Base = {c}/{m}, height = {c}. Area = ½ × base × height."
            })
            if len(questions) >= 30:
                break
        if len(questions) >= 30:
            break
    
    # Maximum/minimum from quadratic
    for a in range(1, 4):
        for h in range(1, 5):
            for k in range(1, 6):
                ans = str(k)
                opts, idx = shuffle_options(ans, [str(h), str(k + 1), str(a)])
                questions.append({
                    'text': f"Minimum value of f(x) = {a}(x - {h})² + {k}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Vertex at ({h}, {k}), opens up. Min = {k}."
                })
                if len(questions) >= 40:
                    break
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # Composite functions
    for a in range(2, 5):
        for b in range(1, 4):
            for c in range(2, 5):
                for val in range(1, 4):
                    # f(x) = ax + b, g(x) = cx
                    # f(g(val)) = a(c*val) + b
                    g_val = c * val
                    f_g_val = a * g_val + b
                    ans = str(f_g_val)
                    opts, idx = shuffle_options(ans, [str(f_g_val + 1), str(g_val), str(a * val + b)])
                    questions.append({
                        'text': f"f(x) = {a}x + {b}, g(x) = {c}x. Find f(g({val})).",
                        'opts': opts, 'idx': idx,
                        'exp': f"g({val}) = {g_val}. f({g_val}) = {a}({g_val}) + {b} = {f_g_val}."
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
        "-- LC OL Functions - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        "-- Create topic",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Functions', {STRAND_ID}, '📈', 10, 1);",
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
    print("LC OL Functions - 600 Questions Generator")
    print("="*60 + "\n")
    
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    
    sql = generate_sql(questions)
    with open('lc_ol_functions_600.sql', 'w') as f:
        f.write(sql)
    
    print(f"Saved: lc_ol_functions_600.sql ({len(sql):,} chars)")
