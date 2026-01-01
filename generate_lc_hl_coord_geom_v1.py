#!/usr/bin/env python3
"""
LC Higher Level - Coordinate Geometry Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level x 12 levels) for LC HL Coordinate Geometry
"""

import random
import math

TOPIC = 'lc_hl_coord_geom'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Distance Formula',
    'Midpoint Formula',
    'Slope of a Line',
    'Equation of a Line',
    'Parallel & Perpendicular Lines',
    'Dividing a Line Segment',
    'Area of Triangle (Coordinates)',
    'Equation of a Circle',
    'Tangent to a Circle',
    'Intersection of Line & Circle',
    'Translation of Axes',
    'Mastery Challenge'
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
        unique_wrong.append(f"None of these")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def gcd(a, b):
    """Greatest common divisor"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a if a != 0 else 1

def simplify_fraction(num, den):
    """Simplify a fraction and return as string"""
    if den == 0:
        return "undefined"
    if num == 0:
        return "0"
    
    sign = -1 if (num < 0) != (den < 0) else 1
    num, den = abs(num), abs(den)
    g = gcd(num, den)
    num, den = num // g, den // g
    
    if sign == -1:
        num = -num
    
    if den == 1:
        return str(num)
    return f"{num}/{den}"

def simplify_sqrt(n):
    """Simplify √n into a√b form, return (a, b)"""
    if n <= 0:
        return (0, 0)
    a = 1
    b = n
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % (i * i) == 0:
            a = i
            b = n // (i * i)
            break
    return (a, b)

def format_sqrt(n):
    """Format √n nicely"""
    if n == 0:
        return "0"
    a, b = simplify_sqrt(n)
    if b == 1:
        return str(a)
    elif a == 1:
        return f"√{b}"
    else:
        return f"{a}√{b}"

def format_coord(x, y):
    """Format coordinates as (x, y)"""
    return f"({x}, {y})"

def generate_level_1():
    """Level 1: Distance Formula"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            # Simple integer distance (Pythagorean triples)
            triples = [(3, 4, 5), (5, 12, 13), (8, 6, 10), (6, 8, 10), (9, 12, 15), (5, 12, 13)]
            dx, dy, dist = random.choice(triples)
            x1 = random.randint(-5, 5)
            y1 = random.randint(-5, 5)
            x2 = x1 + dx * random.choice([1, -1])
            y2 = y1 + dy * random.choice([1, -1])
            
            correct = str(dist)
            distractors = [str(dist + 1), str(dist - 1), str(dx + dy)]
            
            question = f"Find the distance between the points {format_coord(x1, y1)} and {format_coord(x2, y2)}."
            explanation = f"Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[({x2}-{x1})² + ({y2}-{y1})²] = √[{dx}² + {dy}²] = √{dx*dx + dy*dy} = {dist}"
        
        elif qtype == 2:
            # Horizontal distance
            y = random.randint(-10, 10)
            x1 = random.randint(-10, 5)
            x2 = x1 + random.randint(3, 12)
            dist = x2 - x1
            
            correct = str(dist)
            distractors = [str(dist + 1), str(dist - 1), str(dist * 2)]
            
            question = f"Find the distance between {format_coord(x1, y)} and {format_coord(x2, y)}."
            explanation = f"Points are on a horizontal line (same y). Distance = |x₂ - x₁| = |{x2} - {x1}| = {dist}"
        
        elif qtype == 3:
            # Vertical distance
            x = random.randint(-10, 10)
            y1 = random.randint(-10, 5)
            y2 = y1 + random.randint(3, 12)
            dist = y2 - y1
            
            correct = str(dist)
            distractors = [str(dist + 1), str(dist - 1), str(dist * 2)]
            
            question = f"Find the distance between {format_coord(x, y1)} and {format_coord(x, y2)}."
            explanation = f"Points are on a vertical line (same x). Distance = |y₂ - y₁| = |{y2} - {y1}| = {dist}"
        
        else:
            # Distance with sqrt answer
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            dx = random.randint(1, 5)
            dy = random.randint(1, 5)
            x2 = x1 + dx * random.choice([1, -1])
            y2 = y1 + dy * random.choice([1, -1])
            dist_sq = dx*dx + dy*dy
            
            correct = format_sqrt(dist_sq)
            distractors = [format_sqrt(dist_sq + 1), format_sqrt(dist_sq - 1), str(dx + dy)]
            
            question = f"Find the distance between {format_coord(x1, y1)} and {format_coord(x2, y2)}."
            explanation = f"Distance = √[(x₂-x₁)² + (y₂-y₁)²] = √[{dx}² + {dy}²] = √{dist_sq} = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_2():
    """Level 2: Midpoint Formula"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            # Find midpoint - integer result
            x1 = random.randint(-10, 10) * 2
            y1 = random.randint(-10, 10) * 2
            x2 = random.randint(-10, 10) * 2
            y2 = random.randint(-10, 10) * 2
            
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2
            
            correct = format_coord(mx, my)
            distractors = [
                format_coord(mx + 1, my),
                format_coord(mx, my + 1),
                format_coord((x2 - x1) // 2, (y2 - y1) // 2)
            ]
            
            question = f"Find the midpoint of the line segment joining {format_coord(x1, y1)} and {format_coord(x2, y2)}."
            explanation = f"Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = (({x1}+{x2})/2, ({y1}+{y2})/2) = {correct}"
        
        elif qtype == 2:
            # Find midpoint - fractional result
            x1 = random.randint(-10, 10)
            y1 = random.randint(-10, 10)
            x2 = random.randint(-10, 10)
            y2 = random.randint(-10, 10)
            
            mx_num, my_num = x1 + x2, y1 + y2
            if mx_num % 2 == 0 and my_num % 2 == 0:
                correct = format_coord(mx_num // 2, my_num // 2)
            else:
                mx_str = str(mx_num // 2) if mx_num % 2 == 0 else f"{mx_num}/2"
                my_str = str(my_num // 2) if my_num % 2 == 0 else f"{my_num}/2"
                correct = f"({mx_str}, {my_str})"
            
            distractors = [
                format_coord(x1 + x2, y1 + y2),
                format_coord(x2 - x1, y2 - y1),
                format_coord((x1 + x2) // 2 + 1, (y1 + y2) // 2)
            ]
            
            question = f"Find the midpoint of the line segment joining {format_coord(x1, y1)} and {format_coord(x2, y2)}."
            explanation = f"Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = (({x1}+{x2})/2, ({y1}+{y2})/2) = {correct}"
        
        elif qtype == 3:
            # Given midpoint, find endpoint
            mx, my = random.randint(-5, 5), random.randint(-5, 5)
            x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
            x2 = 2 * mx - x1
            y2 = 2 * my - y1
            
            correct = format_coord(x2, y2)
            distractors = [
                format_coord(x2 + 2, y2),
                format_coord(x2, y2 + 2),
                format_coord(mx - x1, my - y1)
            ]
            
            question = f"If {format_coord(mx, my)} is the midpoint of the segment from {format_coord(x1, y1)} to point B, find B."
            explanation = f"If M is midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2). So {mx} = ({x1}+x₂)/2 → x₂ = 2({mx})-{x1} = {x2}. Similarly y₂ = {y2}. B = {correct}"
        
        else:
            # Midpoint on x-axis or y-axis
            axis = random.choice(['x', 'y'])
            if axis == 'x':
                x1, y1 = random.randint(-10, 10), random.randint(1, 10)
                x2 = random.randint(-10, 10)
                y2 = -y1
                correct = "x-axis"
                distractors = ["y-axis", "Neither axis", "Both axes"]
                question = f"The midpoint of {format_coord(x1, y1)} and {format_coord(x2, y2)} lies on which axis?"
                explanation = f"Midpoint y-coordinate = ({y1}+{y2})/2 = {y1+y2}/2 = 0. Since y = 0, the midpoint lies on the x-axis."
            else:
                x1, y1 = random.randint(1, 10), random.randint(-10, 10)
                x2 = -x1
                y2 = random.randint(-10, 10)
                correct = "y-axis"
                distractors = ["x-axis", "Neither axis", "Both axes"]
                question = f"The midpoint of {format_coord(x1, y1)} and {format_coord(x2, y2)} lies on which axis?"
                explanation = f"Midpoint x-coordinate = ({x1}+{x2})/2 = {x1+x2}/2 = 0. Since x = 0, the midpoint lies on the y-axis."
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_3():
    """Level 3: Slope of a Line"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            # Simple integer slope
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            m = random.randint(-5, 5)
            dx = random.randint(1, 5)
            x2 = x1 + dx
            y2 = y1 + m * dx
            
            correct = str(m)
            distractors = [str(m + 1), str(m - 1), str(-m)]
            
            question = f"Find the slope of the line through {format_coord(x1, y1)} and {format_coord(x2, y2)}."
            explanation = f"Slope m = (y₂-y₁)/(x₂-x₁) = ({y2}-{y1})/({x2}-{x1}) = {y2-y1}/{x2-x1} = {m}"
        
        elif qtype == 2:
            # Fractional slope
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            dy = random.randint(-5, 5)
            dx = random.randint(2, 6)
            while gcd(abs(dy), dx) == dx or dy == 0:
                dy = random.randint(-5, 5)
            x2 = x1 + dx
            y2 = y1 + dy
            
            correct = simplify_fraction(dy, dx)
            distractors = [
                simplify_fraction(dx, dy) if dy != 0 else "1",
                simplify_fraction(dy + 1, dx),
                simplify_fraction(-dy, dx)
            ]
            
            question = f"Find the slope of the line through {format_coord(x1, y1)} and {format_coord(x2, y2)}."
            explanation = f"Slope m = (y₂-y₁)/(x₂-x₁) = ({y2}-{y1})/({x2}-{x1}) = {dy}/{dx} = {correct}"
        
        elif qtype == 3:
            # Horizontal line (slope = 0)
            y = random.randint(-10, 10)
            x1 = random.randint(-10, 5)
            x2 = x1 + random.randint(2, 8)
            
            correct = "0"
            distractors = ["1", "undefined", str(x2 - x1)]
            
            question = f"Find the slope of the line through {format_coord(x1, y)} and {format_coord(x2, y)}."
            explanation = f"Both points have y = {y}. This is a horizontal line. Slope = 0"
        
        elif qtype == 4:
            # Vertical line (undefined slope)
            x = random.randint(-10, 10)
            y1 = random.randint(-10, 5)
            y2 = y1 + random.randint(2, 8)
            
            correct = "undefined"
            distractors = ["0", "1", "infinity"]
            
            question = f"Find the slope of the line through {format_coord(x, y1)} and {format_coord(x, y2)}."
            explanation = f"Both points have x = {x}. This is a vertical line. Slope is undefined."
        
        else:
            # Identify slope type
            slopes = [
                ("positive", "The line rises from left to right"),
                ("negative", "The line falls from left to right"),
                ("zero", "The line is horizontal"),
                ("undefined", "The line is vertical")
            ]
            slope_type, desc = random.choice(slopes)
            
            correct = slope_type
            distractors = [s[0] for s in slopes if s[0] != slope_type]
            
            question = f"A line has the property: '{desc}'. What type of slope does it have?"
            explanation = f"{desc}, so the slope is {slope_type}."
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_4():
    """Level 4: Equation of a Line"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            # Find equation given slope and y-intercept
            m = random.randint(-5, 5)
            c = random.randint(-10, 10)
            
            if m == 0:
                correct = f"y = {c}"
            elif m == 1:
                correct = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
                if c == 0:
                    correct = "y = x"
            elif m == -1:
                correct = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
                if c == 0:
                    correct = "y = -x"
            else:
                correct = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
                if c == 0:
                    correct = f"y = {m}x"
            
            distractors = [
                f"y = {m}x - {c}" if c >= 0 else f"y = {m}x + {abs(c)}",
                f"y = {c}x + {m}",
                f"y = {-m}x + {c}"
            ]
            
            question = f"Find the equation of the line with slope {m} and y-intercept {c}."
            explanation = f"Using y = mx + c with m = {m} and c = {c}: {correct}"
        
        elif qtype == 2:
            # Find equation given point and slope
            m = random.randint(-4, 4)
            x1 = random.randint(-5, 5)
            y1 = random.randint(-5, 5)
            c = y1 - m * x1
            
            if m == 0:
                correct = f"y = {c}"
            elif c == 0:
                correct = f"y = {m}x" if m not in [1, -1] else ("y = x" if m == 1 else "y = -x")
            elif m == 1:
                correct = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                correct = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                correct = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            
            distractors = [
                f"y = {m}x + {y1}",
                f"y = {-m}x + {c}",
                f"y = {m}x - {c}" if c >= 0 else f"y = {m}x + {abs(c)}"
            ]
            
            question = f"Find the equation of the line through {format_coord(x1, y1)} with slope {m}."
            explanation = f"Using y - y₁ = m(x - x₁): y - {y1} = {m}(x - {x1}). Simplifying: {correct}"
        
        elif qtype == 3:
            # Find equation given two points
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            m = random.randint(-3, 3)
            dx = random.randint(1, 4)
            x2 = x1 + dx
            y2 = y1 + m * dx
            c = y1 - m * x1
            
            if m == 0:
                correct = f"y = {c}"
            elif c == 0:
                correct = f"y = {m}x" if m not in [1, -1] else ("y = x" if m == 1 else "y = -x")
            elif m == 1:
                correct = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                correct = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                correct = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            
            distractors = [
                f"y = {m+1}x + {c}",
                f"y = {m}x + {c+1}" if c >= -1 else f"y = {m}x - {abs(c)-1}",
                f"y = {-m}x + {c}"
            ]
            
            question = f"Find the equation of the line through {format_coord(x1, y1)} and {format_coord(x2, y2)}."
            explanation = f"Slope m = ({y2}-{y1})/({x2}-{x1}) = {y2-y1}/{x2-x1} = {m}. Using point-slope form: {correct}"
        
        elif qtype == 4:
            # Identify slope and y-intercept from equation
            m = random.randint(-5, 5)
            c = random.randint(-10, 10)
            
            if c >= 0:
                eq = f"y = {m}x + {c}"
            else:
                eq = f"y = {m}x - {abs(c)}"
            
            ask = random.choice(['slope', 'y-intercept'])
            if ask == 'slope':
                correct = str(m)
                distractors = [str(c), str(m + 1), str(-m)]
                question = f"What is the slope of the line {eq}?"
                explanation = f"In y = mx + c form, the slope m = {m}"
            else:
                correct = str(c)
                distractors = [str(m), str(c + 1), str(-c)]
                question = f"What is the y-intercept of the line {eq}?"
                explanation = f"In y = mx + c form, the y-intercept c = {c}"
        
        else:
            # Convert to slope-intercept form
            a = random.randint(1, 5)
            b = random.randint(1, 5) * random.choice([1, -1])
            c = random.randint(-15, 15)
            
            m_str = simplify_fraction(-a, b)
            c_str = simplify_fraction(c, b)
            
            if c_str == "0":
                correct = f"y = {m_str}x"
            elif c_str.startswith('-'):
                correct = f"y = {m_str}x - {c_str[1:]}"
            else:
                correct = f"y = {m_str}x + {c_str}"
            
            distractors = [
                f"y = {simplify_fraction(a, b)}x + {c_str}",
                f"y = {m_str}x + {simplify_fraction(-c, b)}",
                f"y = {simplify_fraction(a, -b)}x + {simplify_fraction(c, -b)}"
            ]
            
            question = f"Convert {a}x + {b}y = {c} to slope-intercept form."
            explanation = f"Solving for y: {b}y = -{a}x + {c}, so y = ({-a}/{b})x + ({c}/{b}) = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_5():
    """Level 5: Parallel & Perpendicular Lines"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            # Identify parallel lines
            m = random.randint(-5, 5)
            c1 = random.randint(-10, 10)
            c2 = c1 + random.randint(1, 5) * random.choice([1, -1])
            
            line1 = f"y = {m}x + {c1}" if c1 >= 0 else f"y = {m}x - {abs(c1)}"
            line2 = f"y = {m}x + {c2}" if c2 >= 0 else f"y = {m}x - {abs(c2)}"
            
            correct = "Parallel"
            distractors = ["Perpendicular", "Neither", "Coincident"]
            
            question = f"Are the lines {line1} and {line2} parallel, perpendicular, or neither?"
            explanation = f"Both lines have slope {m}. Since slopes are equal but y-intercepts differ, they are parallel."
        
        elif qtype == 2:
            # Identify perpendicular lines
            m1 = random.randint(1, 5)
            c1 = random.randint(-5, 5)
            c2 = random.randint(-5, 5)
            
            line1 = f"y = {m1}x + {c1}" if c1 >= 0 else f"y = {m1}x - {abs(c1)}"
            m2_str = simplify_fraction(-1, m1)
            line2 = f"y = {m2_str}x + {c2}" if c2 >= 0 else f"y = {m2_str}x - {abs(c2)}"
            
            correct = "Perpendicular"
            distractors = ["Parallel", "Neither", "Coincident"]
            
            question = f"Are the lines {line1} and {line2} parallel, perpendicular, or neither?"
            explanation = f"Slope of line 1 = {m1}. Slope of line 2 = {m2_str}. Product = -1. Lines are perpendicular."
        
        elif qtype == 3:
            # Find parallel line through a point
            m = random.randint(-4, 4)
            if m == 0:
                m = 2
            c_given = random.randint(-5, 5)
            x1 = random.randint(-5, 5)
            y1 = random.randint(-5, 5)
            c_new = y1 - m * x1
            
            given_line = f"y = {m}x + {c_given}" if c_given >= 0 else f"y = {m}x - {abs(c_given)}"
            if c_new >= 0:
                correct = f"y = {m}x + {c_new}"
            else:
                correct = f"y = {m}x - {abs(c_new)}"
            if c_new == 0:
                correct = f"y = {m}x"
            
            distractors = [
                f"y = {-m}x + {c_new}" if c_new >= 0 else f"y = {-m}x - {abs(c_new)}",
                f"y = {m}x + {c_given}",
                f"y = {m+1}x + {c_new}"
            ]
            
            question = f"Find the equation of the line parallel to {given_line} passing through {format_coord(x1, y1)}."
            explanation = f"Parallel lines have same slope. m = {m}. Using point {format_coord(x1, y1)}: c = {y1} - {m}({x1}) = {c_new}. Line: {correct}"
        
        elif qtype == 4:
            # Find perpendicular line through a point
            m1 = random.randint(1, 4) * random.choice([1, -1])
            c_given = random.randint(-5, 5)
            x1 = random.randint(-5, 5)
            y1 = random.randint(-5, 5)
            
            m2_str = simplify_fraction(-1, m1)
            c_num = y1 * m1 + x1
            c_frac = simplify_fraction(c_num, m1)
            
            given_line = f"y = {m1}x + {c_given}" if c_given >= 0 else f"y = {m1}x - {abs(c_given)}"
            
            if c_frac == "0":
                correct = f"y = {m2_str}x"
            elif c_frac.startswith('-'):
                correct = f"y = {m2_str}x - {c_frac[1:]}"
            else:
                correct = f"y = {m2_str}x + {c_frac}"
            
            distractors = [
                f"y = {m1}x + {c_frac}",
                f"y = {simplify_fraction(1, m1)}x + {c_frac}",
                f"y = {m2_str}x + {y1}"
            ]
            
            question = f"Find the equation of the line perpendicular to {given_line} passing through {format_coord(x1, y1)}."
            explanation = f"Perpendicular slope = -1/{m1} = {m2_str}. Using point {format_coord(x1, y1)}: {correct}"
        
        else:
            # Conceptual question about slopes
            concepts = [
                ("Parallel lines have...", "equal slopes", ["slopes that multiply to -1", "opposite slopes", "zero slopes"]),
                ("Perpendicular lines have slopes that...", "multiply to -1", ["are equal", "add to 0", "multiply to 1"]),
                ("The slope of a line perpendicular to y = 3x + 1 is...", "-1/3", ["3", "-3", "1/3"]),
                ("The slope of a line parallel to y = -2x + 5 is...", "-2", ["2", "1/2", "-1/2"]),
            ]
            q_text, correct, distractors = random.choice(concepts)
            question = q_text
            explanation = f"The answer is {correct}."
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_6():
    """Level 6: Dividing a Line Segment"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            # Divide in ratio m:n internally
            x1, y1 = random.randint(-6, 6), random.randint(-6, 6)
            x2, y2 = random.randint(-6, 6), random.randint(-6, 6)
            while x1 == x2 and y1 == y2:
                x2, y2 = random.randint(-6, 6), random.randint(-6, 6)
            
            m = random.randint(1, 4)
            n = random.randint(1, 4)
            
            px_num = m * x2 + n * x1
            py_num = m * y2 + n * y1
            denom = m + n
            
            px_str = simplify_fraction(px_num, denom)
            py_str = simplify_fraction(py_num, denom)
            
            correct = f"({px_str}, {py_str})"
            
            wrong1_x = simplify_fraction(n * x2 + m * x1, denom)
            wrong1_y = simplify_fraction(n * y2 + m * y1, denom)
            
            distractors = [
                f"({wrong1_x}, {wrong1_y})",
                f"({simplify_fraction(px_num + denom, denom)}, {py_str})",
                f"({px_str}, {simplify_fraction(py_num + denom, denom)})"
            ]
            
            question = f"Find the point that divides the segment from {format_coord(x1, y1)} to {format_coord(x2, y2)} in the ratio {m}:{n}."
            explanation = f"Using section formula: P = ((m·x₂ + n·x₁)/(m+n), (m·y₂ + n·y₁)/(m+n)) = {correct}"
        
        elif qtype == 2:
            # Find ratio given point
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            m = random.randint(1, 4)
            n = random.randint(1, 4)
            while gcd(m, n) != 1:
                n = random.randint(1, 4)
            
            dx = random.randint(2, 5) * (m + n)
            dy = random.randint(2, 5) * (m + n)
            x2 = x1 + dx
            y2 = y1 + dy
            
            px = x1 + (m * dx) // (m + n)
            py = y1 + (m * dy) // (m + n)
            
            correct = f"{m}:{n}"
            distractors = [f"{n}:{m}", f"{m+1}:{n}", f"{m}:{n+1}"]
            
            question = f"Point {format_coord(px, py)} divides the segment from {format_coord(x1, y1)} to {format_coord(x2, y2)} in what ratio?"
            explanation = f"Using the section formula backwards, the ratio is {m}:{n}"
        
        elif qtype == 3:
            # Trisection points
            x1, y1 = random.randint(-6, 6), random.randint(-6, 6)
            x2, y2 = x1 + 9, y1 + 6
            
            which = random.choice(['closer to A', 'closer to B'])
            if which == 'closer to A':
                correct = format_coord(x1 + 3, y1 + 2)
                question = f"Find the trisection point of segment from A{format_coord(x1, y1)} to B{format_coord(x2, y2)} that is closer to A."
                explanation = f"Trisection point closer to A divides in ratio 1:2. P = {correct}"
            else:
                correct = format_coord(x1 + 6, y1 + 4)
                question = f"Find the trisection point of segment from A{format_coord(x1, y1)} to B{format_coord(x2, y2)} that is closer to B."
                explanation = f"Trisection point closer to B divides in ratio 2:1. P = {correct}"
            
            distractors = [
                format_coord(x1 + 3, y1 + 4),
                format_coord(x1 + 6, y1 + 2),
                format_coord((x1 + x2) // 2, (y1 + y2) // 2)
            ]
        
        else:
            # External division
            x1, y1 = random.randint(-4, 4), random.randint(-4, 4)
            x2, y2 = random.randint(-4, 4), random.randint(-4, 4)
            while x1 == x2 and y1 == y2:
                x2, y2 = random.randint(-4, 4), random.randint(-4, 4)
            
            m = random.randint(2, 4)
            n = random.randint(1, m - 1)
            
            px_num = m * x2 - n * x1
            py_num = m * y2 - n * y1
            denom = m - n
            
            px_str = simplify_fraction(px_num, denom)
            py_str = simplify_fraction(py_num, denom)
            
            correct = f"({px_str}, {py_str})"
            
            distractors = [
                f"({simplify_fraction(m * x2 + n * x1, m + n)}, {simplify_fraction(m * y2 + n * y1, m + n)})",
                f"({simplify_fraction(px_num + denom, denom)}, {py_str})",
                f"({px_str}, {simplify_fraction(py_num - denom, denom)})"
            ]
            
            question = f"Find the point that divides the segment from {format_coord(x1, y1)} to {format_coord(x2, y2)} externally in the ratio {m}:{n}."
            explanation = f"External division: P = ((m·x₂ - n·x₁)/(m-n), (m·y₂ - n·y₁)/(m-n)) = {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_7():
    """Level 7: Area of Triangle (Coordinates)"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            # Simple triangle area
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            x2, y2 = random.randint(-5, 5), random.randint(-5, 5)
            x3, y3 = random.randint(-5, 5), random.randint(-5, 5)
            
            area_2 = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            
            if area_2 == 0:
                x3 += 1
                area_2 = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            
            if area_2 % 2 == 0:
                correct = str(area_2 // 2)
            else:
                correct = f"{area_2}/2"
            
            distractors = [
                str(area_2),
                str(area_2 // 2 + 1) if area_2 % 2 == 0 else f"{area_2 + 2}/2",
                str(area_2 // 2 - 1) if area_2 % 2 == 0 and area_2 > 2 else str(area_2 // 2 + 2)
            ]
            
            question = f"Find the area of the triangle with vertices A{format_coord(x1, y1)}, B{format_coord(x2, y2)}, and C{format_coord(x3, y3)}."
            explanation = f"Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = ½|{area_2}| = {correct}"
        
        elif qtype == 2:
            # Triangle with one vertex at origin
            x2, y2 = random.randint(1, 8), random.randint(1, 8)
            x3, y3 = random.randint(-8, 0), random.randint(1, 8)
            
            area_2 = abs(x2 * y3 - x3 * y2)
            
            if area_2 % 2 == 0:
                correct = str(area_2 // 2)
            else:
                correct = f"{area_2}/2"
            
            distractors = [str(area_2), str(area_2 // 2 + 2), str(abs(x2 * y2 - x3 * y3) // 2 + 1)]
            
            question = f"Find the area of the triangle with vertices O{format_coord(0, 0)}, P{format_coord(x2, y2)}, and Q{format_coord(x3, y3)}."
            explanation = f"With one vertex at origin: Area = ½|x₂y₃ - x₃y₂| = ½|{area_2}| = {correct}"
        
        elif qtype == 3:
            # Collinearity check
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            m = random.randint(-3, 3)
            dx1 = random.randint(1, 4)
            dx2 = random.randint(1, 4)
            
            collinear = random.choice([True, False])
            
            x2 = x1 + dx1
            y2 = y1 + m * dx1
            x3 = x1 + dx1 + dx2
            
            if collinear:
                y3 = y1 + m * (dx1 + dx2)
                correct = "Yes, they are collinear"
                explanation = f"Area = 0 when points are collinear. All three points lie on line with slope {m}."
            else:
                y3 = y1 + m * (dx1 + dx2) + random.randint(1, 3)
                correct = "No, they are not collinear"
                explanation = f"The area of the triangle is non-zero, so the points are not collinear."
            
            distractors_list = ["Yes, they are collinear", "No, they are not collinear", "Cannot be determined", "Only two are collinear"]
            distractors = [d for d in distractors_list if d != correct]
            
            question = f"Are the points A{format_coord(x1, y1)}, B{format_coord(x2, y2)}, and C{format_coord(x3, y3)} collinear?"
        
        else:
            # Area of quadrilateral
            x1, y1 = 0, 0
            x2, y2 = random.randint(3, 6), 0
            x3, y3 = random.randint(3, 6), random.randint(3, 6)
            x4, y4 = 0, random.randint(3, 6)
            
            area = abs((x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y4 - x4*y3) + (x4*y1 - x1*y4)) // 2
            
            correct = str(area)
            distractors = [str(area + 2), str(area - 2), str(area * 2)]
            
            question = f"Find the area of the quadrilateral with vertices {format_coord(x1, y1)}, {format_coord(x2, y2)}, {format_coord(x3, y3)}, {format_coord(x4, y4)} in order."
            explanation = f"Using the shoelace formula for the quadrilateral, Area = {correct} square units."
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_8():
    """Level 8: Equation of a Circle"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 5)
        
        if qtype == 1:
            # Find equation given centre and radius
            h = random.randint(-5, 5)
            k = random.randint(-5, 5)
            r = random.randint(1, 8)
            
            h_str = f"+ {h}" if h < 0 else f"- {h}" if h > 0 else ""
            k_str = f"+ {k}" if k < 0 else f"- {k}" if k > 0 else ""
            
            if h == 0 and k == 0:
                correct = f"x² + y² = {r*r}"
            elif h == 0:
                correct = f"x² + (y {k_str})² = {r*r}"
            elif k == 0:
                correct = f"(x {h_str})² + y² = {r*r}"
            else:
                correct = f"(x {h_str})² + (y {k_str})² = {r*r}"
            
            distractors = [
                f"x² + y² = {r}",
                f"(x + {h})² + (y + {k})² = {r*r}",
                f"x² + y² = {r*r + h*h + k*k}"
            ]
            
            question = f"Find the equation of the circle with centre {format_coord(h, k)} and radius {r}."
            explanation = f"Circle equation: (x-h)² + (y-k)² = r². With centre ({h}, {k}) and r = {r}: {correct}"
        
        elif qtype == 2:
            # Find centre and radius from equation
            h = random.randint(-5, 5)
            k = random.randint(-5, 5)
            r = random.randint(2, 7)
            
            h_str = f"+ {abs(h)}" if h < 0 else f"- {h}" if h > 0 else ""
            k_str = f"+ {abs(k)}" if k < 0 else f"- {k}" if k > 0 else ""
            
            eq = f"(x {h_str})² + (y {k_str})² = {r*r}".replace("(x )²", "x²").replace("(y )²", "y²")
            
            ask = random.choice(['centre', 'radius'])
            if ask == 'centre':
                correct = format_coord(h, k)
                distractors = [format_coord(-h, -k), format_coord(h, -k), format_coord(-h, k)]
                question = f"Find the centre of the circle {eq}."
                explanation = f"From (x-h)² + (y-k)² = r², the centre is (h, k) = {correct}"
            else:
                correct = str(r)
                distractors = [str(r*r), str(r+1), str(r-1)]
                question = f"Find the radius of the circle {eq}."
                explanation = f"From (x-h)² + (y-k)² = r², r² = {r*r}, so r = {r}"
        
        elif qtype == 3:
            # Convert general form to standard form
            h = random.randint(-4, 4)
            k = random.randint(-4, 4)
            r = random.randint(2, 5)
            
            D = -2 * h
            E = -2 * k
            F = h*h + k*k - r*r
            
            D_str = f"+ {D}x" if D > 0 else f"- {abs(D)}x" if D < 0 else ""
            E_str = f"+ {E}y" if E > 0 else f"- {abs(E)}y" if E < 0 else ""
            F_str = f"+ {F}" if F > 0 else f"- {abs(F)}" if F < 0 else ""
            
            eq = f"x² + y² {D_str} {E_str} {F_str} = 0".replace("  ", " ")
            
            correct = f"Centre {format_coord(h, k)}, radius {r}"
            distractors = [
                f"Centre {format_coord(-h, -k)}, radius {r}",
                f"Centre {format_coord(h, k)}, radius {r*r}",
                f"Centre {format_coord(D, E)}, radius {r}"
            ]
            
            question = f"Find the centre and radius of the circle {eq}."
            explanation = f"Using x² + y² + Dx + Ey + F = 0: centre = (-D/2, -E/2) = ({h}, {k}), r = {r}"
        
        elif qtype == 4:
            # Circle through origin
            h = random.randint(1, 5) * random.choice([1, -1])
            k = random.randint(1, 5) * random.choice([1, -1])
            r_sq = h*h + k*k
            
            correct = str(r_sq)
            distractors = [str(r_sq + 1), str(r_sq - 1), str(2 * r_sq)]
            
            question = f"A circle has centre {format_coord(h, k)} and passes through the origin. What is r²?"
            explanation = f"Distance from centre to origin = √({h}² + {k}²) = √{r_sq}. So r² = {r_sq}."
        
        else:
            # Check if point is inside/on/outside circle
            h, k = random.randint(-3, 3), random.randint(-3, 3)
            r = random.randint(3, 6)
            
            position = random.choice(['inside', 'on', 'outside'])
            if position == 'inside':
                px, py = h + random.randint(0, r-2), k
                dist_sq = (px - h)**2 + (py - k)**2
                while dist_sq >= r*r:
                    px = h + random.randint(-(r-1), r-1)
                    py = k
                    dist_sq = (px - h)**2 + (py - k)**2
            elif position == 'on':
                if r == 5:
                    px, py = h + 3, k + 4
                elif r == 10:
                    px, py = h + 6, k + 8
                else:
                    px, py = h + r, k
            else:
                px, py = h + r + random.randint(1, 3), k + random.randint(1, 3)
            
            dist_sq = (px - h)**2 + (py - k)**2
            
            if dist_sq < r*r:
                correct = "Inside"
            elif dist_sq == r*r:
                correct = "On"
            else:
                correct = "Outside"
            
            distractors = ["Inside", "On", "Outside", "Cannot determine"]
            distractors = [d for d in distractors if d != correct][:3]
            
            question = f"Is the point {format_coord(px, py)} inside, on, or outside the circle with centre {format_coord(h, k)} and radius {r}?"
            explanation = f"Distance² from point to centre = ({px}-{h})² + ({py}-{k})² = {dist_sq}. r² = {r*r}. Point is {correct.lower()}."
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_9():
    """Level 9: Tangent to a Circle"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            # Tangent at a point on circle centred at origin
            r = random.choice([5, 10, 13])
            if r == 5:
                px, py = random.choice([(3, 4), (4, 3), (5, 0), (0, 5)])
            elif r == 10:
                px, py = random.choice([(6, 8), (8, 6), (10, 0), (0, 10)])
            else:
                px, py = random.choice([(5, 12), (12, 5), (13, 0), (0, 13)])
            
            if py == 0:
                correct = f"x = {px}"
                explanation = f"At point ({px}, 0) on circle x² + y² = {r*r}, tangent is vertical: x = {px}"
            elif px == 0:
                correct = f"y = {py}"
                explanation = f"At point (0, {py}) on circle x² + y² = {r*r}, tangent is horizontal: y = {py}"
            else:
                correct = f"{px}x + {py}y = {r*r}"
                explanation = f"Tangent at ({px}, {py}) on x² + y² = {r*r} is: {px}x + {py}y = {r*r}"
            
            distractors = [
                f"{py}x + {px}y = {r*r}",
                f"{px}x - {py}y = {r*r}",
                f"{px}x + {py}y = {r}"
            ]
            
            question = f"Find the equation of the tangent to the circle x² + y² = {r*r} at the point {format_coord(px, py)}."
        
        elif qtype == 2:
            # Slope of tangent at a point
            h, k = random.randint(-3, 3), random.randint(-3, 3)
            r = 5
            px, py = h + 3, k + 4
            
            radius_slope = simplify_fraction(py - k, px - h)
            tangent_slope = simplify_fraction(-(px - h), py - k)
            
            correct = tangent_slope
            distractors = [radius_slope, simplify_fraction(px - h, py - k), simplify_fraction(py - k, -(px - h))]
            
            question = f"Find the slope of the tangent to the circle with centre {format_coord(h, k)} at the point {format_coord(px, py)}."
            explanation = f"Radius slope = ({py}-{k})/({px}-{h}) = {radius_slope}. Tangent is perpendicular, so slope = {correct}"
        
        elif qtype == 3:
            # Length of tangent from external point
            h, k = 0, 0
            r = random.randint(3, 6)
            d = r + random.randint(2, 5)
            px, py = d, 0
            
            tang_sq = d*d - r*r
            correct = format_sqrt(tang_sq)
            distractors = [format_sqrt(d*d + r*r), str(d - r), str(d + r)]
            
            question = f"Find the length of the tangent from point {format_coord(px, py)} to the circle x² + y² = {r*r}."
            explanation = f"Distance from point to centre = {d}. Tangent length = √(d² - r²) = √({d}² - {r}²) = √{tang_sq} = {correct}"
        
        else:
            # Condition for line to be tangent
            r = random.randint(2, 5)
            m = random.randint(-3, 3)
            
            c_sq = r*r * (1 + m*m)
            c_val = int(math.sqrt(c_sq)) if math.sqrt(c_sq) == int(math.sqrt(c_sq)) else None
            
            if c_val:
                correct = f"c = ±{c_val}"
            else:
                correct = f"c = ±√{c_sq}"
            
            distractors = [f"c = ±{r}", f"c = ±{r*r}", f"c = ±√{r*r + m*m}"]
            
            question = f"For what value(s) of c is the line y = {m}x + c tangent to the circle x² + y² = {r*r}?"
            explanation = f"For tangency: c² = r²(1 + m²) = {r*r}(1 + {m*m}) = {c_sq}. So {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_10():
    """Level 10: Intersection of Line & Circle"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            # Number of intersection points
            r = random.randint(3, 6)
            m = random.randint(-2, 2)
            
            case = random.choice(['two', 'one', 'zero'])
            
            if case == 'two':
                max_c = int(math.sqrt(r*r * (1 + m*m))) - 1
                c = random.randint(-max(1, max_c), max(1, max_c))
                correct = "2 points"
                explanation = "Line intersects circle at 2 points (secant)"
            elif case == 'one':
                c_sq = r*r * (1 + m*m)
                if math.sqrt(c_sq) == int(math.sqrt(c_sq)):
                    c = int(math.sqrt(c_sq))
                    correct = "1 point"
                    explanation = "Line is tangent to circle (1 point)"
                else:
                    max_c = int(math.sqrt(c_sq)) - 1
                    c = random.randint(0, max(1, max_c))
                    correct = "2 points"
                    explanation = "Line intersects circle at 2 points"
            else:
                min_c = int(math.sqrt(r*r * (1 + m*m))) + 1
                c = min_c + random.randint(0, 3)
                correct = "0 points"
                explanation = "Line does not intersect circle"
            
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            line = f"y = {m}x {c_str}" if m != 0 else f"y = {c}"
            if m == 1:
                line = f"y = x {c_str}"
            if m == -1:
                line = f"y = -x {c_str}"
            
            distractors = ["0 points", "1 point", "2 points", "3 points"]
            distractors = [d for d in distractors if d != correct][:3]
            
            question = f"How many points of intersection are there between the line {line} and the circle x² + y² = {r*r}?"
        
        elif qtype == 2:
            # Find intersection points (simple case)
            r = 5
            correct = f"({r}, 0) and ({-r}, 0)"
            distractors = [
                f"(0, {r}) and (0, {-r})",
                f"({r}, {r}) and ({-r}, {-r})",
                f"({r}, 0) only"
            ]
            
            question = f"Find the points of intersection of the line y = 0 and the circle x² + y² = {r*r}."
            explanation = f"Substituting y = 0: x² = {r*r}, so x = ±{r}. Points: {correct}"
        
        elif qtype == 3:
            # Chord length
            r = 5
            d = random.randint(1, r-1)
            
            inside_sqrt = r*r - d*d
            a, b = simplify_sqrt(inside_sqrt)
            if b == 1:
                correct = str(2 * a)
            else:
                correct = f"2√{inside_sqrt}" if a == 1 else f"{2*a}√{b}"
            
            distractors = [f"2√{r*r + d*d}", f"√{4*(r*r - d*d)}", str(2 * r)]
            
            question = f"A chord of a circle with radius {r} is at distance {d} from the centre. Find the chord length."
            explanation = f"Chord length = 2√(r² - d²) = 2√({r}² - {d}²) = 2√{inside_sqrt} = {correct}"
        
        else:
            # Find k for tangency
            r = random.randint(2, 5)
            k_sq = 2 * r * r
            
            a, b = simplify_sqrt(k_sq)
            if b == 1:
                correct = f"k = ±{a}"
            elif a == 1:
                correct = f"k = ±√{k_sq}"
            else:
                correct = f"k = ±{a}√{b}"
            
            distractors = [f"k = ±{r}", f"k = ±{2*r}", f"k = ±{r*r}"]
            
            question = f"For what values of k is the line y = x + k tangent to the circle x² + y² = {r*r}?"
            explanation = f"Distance from origin to line = |k|/√2 = {r}. So k = ±{r}√2 = ±√{k_sq}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_11():
    """Level 11: Translation of Axes"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 4)
        
        if qtype == 1:
            # New coordinates after translation
            x, y = random.randint(-8, 8), random.randint(-8, 8)
            h, k = random.randint(-5, 5), random.randint(-5, 5)
            
            X = x - h
            Y = y - k
            
            correct = format_coord(X, Y)
            distractors = [
                format_coord(x + h, y + k),
                format_coord(h - x, k - y),
                format_coord(X + 1, Y)
            ]
            
            question = f"If the origin is translated to {format_coord(h, k)}, what are the new coordinates of the point {format_coord(x, y)}?"
            explanation = f"New coordinates: (X, Y) = (x - h, y - k) = ({x} - {h}, {y} - {k}) = {correct}"
        
        elif qtype == 2:
            # Original coordinates from new coordinates
            X, Y = random.randint(-6, 6), random.randint(-6, 6)
            h, k = random.randint(-4, 4), random.randint(-4, 4)
            
            x = X + h
            y = Y + k
            
            correct = format_coord(x, y)
            distractors = [
                format_coord(X - h, Y - k),
                format_coord(h - X, k - Y),
                format_coord(x + 1, y)
            ]
            
            question = f"The origin is translated to {format_coord(h, k)}. If a point has new coordinates {format_coord(X, Y)}, find its original coordinates."
            explanation = f"Original coordinates: (x, y) = (X + h, Y + k) = ({X} + {h}, {Y} + {k}) = {correct}"
        
        elif qtype == 3:
            # Transform equation
            h, k = random.randint(1, 4), random.randint(1, 4)
            
            const = h*h - k
            const_str = f"+ {const}" if const > 0 else f"- {abs(const)}" if const < 0 else ""
            
            correct = f"Y = X² + {2*h}X {const_str}".strip()
            if const == 0:
                correct = f"Y = X² + {2*h}X"
            
            distractors = [
                f"Y = X² - {2*h}X {const_str}",
                f"Y = X² + {2*h}X + {h*h + k}",
                f"Y = (X - {h})² + {k}"
            ]
            
            question = f"If the origin is shifted to {format_coord(h, k)}, transform the equation y = x² to the new coordinates."
            explanation = f"Substituting x = X + {h}, y = Y + {k}: Y + {k} = (X + {h})². Expanding: {correct}"
        
        else:
            # Find translation to remove first-degree terms
            g = random.randint(-4, 4)
            f = random.randint(-4, 4)
            c = random.randint(-10, 10)
            
            g_str = f"+ {2*g}x" if g > 0 else f"- {2*abs(g)}x" if g < 0 else ""
            f_str = f"+ {2*f}y" if f > 0 else f"- {2*abs(f)}y" if f < 0 else ""
            c_str = f"+ {c}" if c > 0 else f"- {abs(c)}" if c < 0 else ""
            
            eq = f"x² + y² {g_str} {f_str} {c_str} = 0".replace("  ", " ")
            
            correct = format_coord(-g, -f)
            distractors = [
                format_coord(g, f),
                format_coord(2*g, 2*f),
                format_coord(-2*g, -2*f)
            ]
            
            question = f"To what point should the origin be translated to remove the first-degree terms from {eq}?"
            explanation = f"For x² + y² + 2gx + 2fy + c = 0, translate to (-g, -f) = ({-g}, {-f})"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    for _ in range(50):
        qtype = random.randint(1, 6)
        
        if qtype == 1:
            # Combined distance and midpoint
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            x2, y2 = x1 + 6, y1 + 8
            
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2
            
            question = f"A and B are points with AB = 10. If A = {format_coord(x1, y1)} and the midpoint M = {format_coord(mx, my)}, find B."
            correct = format_coord(x2, y2)
            distractors = [
                format_coord(2*mx - x1 + 1, 2*my - y1),
                format_coord(x1 + 10, y1),
                format_coord(mx + 3, my + 4)
            ]
            explanation = f"B = (2mx - x1, 2my - y1) = (2·{mx} - {x1}, 2·{my} - {y1}) = {correct}"
        
        elif qtype == 2:
            # Circumcentre of triangle (right triangle)
            x1, y1 = 0, 0
            x2, y2 = 6, 0
            x3, y3 = 0, 8
            
            cx, cy = 3, 4
            
            correct = format_coord(cx, cy)
            distractors = [
                format_coord(2, 2),
                format_coord(3, 3),
                format_coord(2, 4)
            ]
            
            question = f"Find the circumcentre of the triangle with vertices A{format_coord(x1, y1)}, B{format_coord(x2, y2)}, C{format_coord(x3, y3)}."
            explanation = f"For a right triangle, the circumcentre is the midpoint of the hypotenuse. Circumcentre = {correct}"
        
        elif qtype == 3:
            # Centroid
            x1, y1 = random.randint(-6, 6), random.randint(-6, 6)
            x2, y2 = random.randint(-6, 6), random.randint(-6, 6)
            x3 = 3 * random.randint(-3, 3) - x1 - x2
            y3 = 3 * random.randint(-3, 3) - y1 - y2
            
            gx = (x1 + x2 + x3) // 3
            gy = (y1 + y2 + y3) // 3
            
            correct = format_coord(gx, gy)
            distractors = [
                format_coord(gx + 1, gy),
                format_coord((x1 + x2) // 2, (y1 + y2) // 2),
                format_coord(gx, gy + 1)
            ]
            
            question = f"Find the centroid of the triangle with vertices {format_coord(x1, y1)}, {format_coord(x2, y2)}, {format_coord(x3, y3)}."
            explanation = f"Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) = {correct}"
        
        elif qtype == 4:
            # Two circles - intersection type
            h1, k1, r1 = 0, 0, 5
            h2 = random.randint(3, 12)
            k2 = 0
            r2 = random.randint(2, 5)
            
            d = h2
            
            if d > r1 + r2:
                correct = "No intersection (external)"
            elif d == r1 + r2:
                correct = "External tangency (1 point)"
            elif abs(r1 - r2) < d < r1 + r2:
                correct = "2 intersection points"
            elif d == abs(r1 - r2):
                correct = "Internal tangency (1 point)"
            else:
                correct = "No intersection (one inside other)"
            
            distractors = [
                "No intersection (external)",
                "External tangency (1 point)",
                "2 intersection points",
                "Internal tangency (1 point)"
            ]
            distractors = [d for d in distractors if d != correct][:3]
            
            question = f"Circle 1: centre {format_coord(h1, k1)}, radius {r1}. Circle 2: centre {format_coord(h2, k2)}, radius {r2}. Describe their intersection."
            explanation = f"Distance between centres = {d}. Sum of radii = {r1 + r2}. |Difference| = {abs(r1-r2)}. {correct}"
        
        elif qtype == 5:
            # Perpendicular distance from point to line
            a, b = random.randint(1, 4), random.randint(1, 4)
            c = random.randint(5, 15)
            px, py = random.randint(-5, 5), random.randint(-5, 5)
            
            num = abs(a * px + b * py - c)
            den_sq = a*a + b*b
            
            correct = f"{num}/√{den_sq}"
            
            distractors = [
                f"{num + 1}/√{den_sq}",
                f"{num}/√{den_sq + 1}",
                str(num)
            ]
            
            question = f"Find the perpendicular distance from point {format_coord(px, py)} to the line {a}x + {b}y = {c}."
            explanation = f"Distance = |{a}({px}) + {b}({py}) - {c}| / √({a}² + {b}²) = {num}/√{den_sq}"
        
        else:
            # Reflection of point in line y = x
            px, py = random.randint(-5, 5), random.randint(-5, 5)
            
            correct = format_coord(py, px)
            distractors = [
                format_coord(-px, -py),
                format_coord(-py, -px),
                format_coord(px, -py)
            ]
            
            question = f"Find the reflection of the point {format_coord(px, py)} in the line y = x."
            explanation = f"Reflection in y = x swaps the coordinates. ({px}, {py}) → {correct}"
        
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
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
        f.write(f"-- LC Higher Level - Coordinate Geometry Questions\n")
        f.write(f"-- Generated: 2025-12-15\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
