#!/usr/bin/env python3
"""
LC Ordinary Level Coordinate Geometry (Lines) - 600 Questions Generator
========================================================================
50 questions per level × 12 levels = 600 questions

Based on SEC Paper Analysis 2019-2025:
- Coordinate Geometry: distance, midpoint, slope, line equations, parallel/perpendicular
"""

import random
from math import gcd

TOPIC_ID = 'lc_ol_coord_lines'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Plotting Points", "Foundation"),
    2: ("Distance Between Points", "Foundation"),
    3: ("Midpoint Formula", "Foundation"),
    4: ("Slope of a Line", "Developing"),
    5: ("Slope from Two Points", "Developing"),
    6: ("Equation y = mx + c", "Developing"),
    7: ("Finding Equations", "Proficient"),
    8: ("Parallel Lines", "Proficient"),
    9: ("Perpendicular Lines", "Proficient"),
    10: ("Intersecting Lines", "Advanced"),
    11: ("Area and Applications", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    options = [correct] + distractors[:3]
    random.shuffle(options)
    return options, options.index(correct)

def generate_level_1():
    """Plotting Points"""
    questions = []
    
    # Identify quadrant
    quadrants = [
        ((3, 4), "Quadrant I", "x > 0, y > 0"),
        ((-2, 5), "Quadrant II", "x < 0, y > 0"),
        ((-3, -4), "Quadrant III", "x < 0, y < 0"),
        ((4, -2), "Quadrant IV", "x > 0, y < 0"),
        ((5, 3), "Quadrant I", "x > 0, y > 0"),
        ((-4, 2), "Quadrant II", "x < 0, y > 0"),
        ((-1, -5), "Quadrant III", "x < 0, y < 0"),
        ((2, -6), "Quadrant IV", "x > 0, y < 0"),
    ]
    for point, quad, reason in quadrants:
        opts, idx = shuffle_options(quad, ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"])
        questions.append({
            'text': f"In which quadrant is {point}?",
            'opts': opts, 'idx': idx,
            'exp': f"{reason} → {quad}"
        })
    
    # Points on axes
    axis_points = [
        ((0, 5), "y-axis"),
        ((3, 0), "x-axis"),
        ((0, -4), "y-axis"),
        ((-2, 0), "x-axis"),
        ((0, 0), "Origin"),
        ((0, 7), "y-axis"),
        ((6, 0), "x-axis"),
    ]
    for point, location in axis_points:
        opts, idx = shuffle_options(location, ["x-axis", "y-axis", "Origin", "Quadrant I"])
        questions.append({
            'text': f"Where is {point} located?",
            'opts': opts, 'idx': idx,
            'exp': f"{point} is on the {location}."
        })
    
    # Identify x-coordinate
    for x in range(-5, 8):
        for y in range(-4, 6):
            if x != 0 and y != 0:
                opts, idx = shuffle_options(str(x), [str(y), str(x + 1), str(x - 1)])
                questions.append({
                    'text': f"What is the x-coordinate of ({x}, {y})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"x-coordinate is {x}."
                })
                if len(questions) >= 25:
                    break
        if len(questions) >= 25:
            break
    
    # Identify y-coordinate
    for x in range(-4, 6):
        for y in range(-5, 8):
            if x != 0 and y != 0:
                opts, idx = shuffle_options(str(y), [str(x), str(y + 1), str(y - 1)])
                questions.append({
                    'text': f"What is the y-coordinate of ({x}, {y})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"y-coordinate is {y}."
                })
                if len(questions) >= 40:
                    break
        if len(questions) >= 40:
            break
    
    # Distance from origin (simple)
    for x, y in [(3, 4), (5, 12), (8, 6), (0, 5), (4, 0)]:
        if x == 0:
            d = abs(y)
        elif y == 0:
            d = abs(x)
        else:
            d = int((x*x + y*y) ** 0.5) if (x*x + y*y) ** 0.5 == int((x*x + y*y) ** 0.5) else "√" + str(x*x + y*y)
        if isinstance(d, int):
            opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1) if d > 1 else "1", str(x + y)])
            questions.append({
                'text': f"Distance from origin to ({x}, {y})?",
                'opts': opts, 'idx': idx,
                'exp': f"d = √({x}² + {y}²) = {d}."
            })
        if len(questions) >= 50:
            break
    
    # Fill remaining with quadrant questions
    for x in range(1, 8):
        for y in range(1, 8):
            opts, idx = shuffle_options("Quadrant I", ["Quadrant II", "Quadrant III", "Quadrant IV"])
            questions.append({
                'text': f"In which quadrant is ({x}, {y})?",
                'opts': opts, 'idx': idx,
                'exp': "Both positive → Quadrant I."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_2():
    """Distance Between Points"""
    questions = []
    
    # Distance formula
    opts, idx = shuffle_options("√[(x₂-x₁)² + (y₂-y₁)²]", ["(x₂-x₁) + (y₂-y₁)", "|x₂-x₁| × |y₂-y₁|", "(x₂+x₁)/2"])
    questions.append({
        'text': "What is the distance formula?",
        'opts': opts, 'idx': idx,
        'exp': "d = √[(x₂-x₁)² + (y₂-y₁)²]"
    })
    
    # Horizontal distance (same y)
    for x1 in range(0, 6):
        for x2 in range(x1 + 2, x1 + 8):
            for y in range(1, 5):
                d = x2 - x1
                opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1), str(d + 2)])
                questions.append({
                    'text': f"Distance from ({x1}, {y}) to ({x2}, {y})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Horizontal distance = |{x2} - {x1}| = {d}."
                })
                if len(questions) >= 12:
                    break
            if len(questions) >= 12:
                break
        if len(questions) >= 12:
            break
    
    # Vertical distance (same x)
    for y1 in range(0, 5):
        for y2 in range(y1 + 2, y1 + 7):
            for x in range(1, 4):
                d = y2 - y1
                opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1), str(d + 2)])
                questions.append({
                    'text': f"Distance from ({x}, {y1}) to ({x}, {y2})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Vertical distance = |{y2} - {y1}| = {d}."
                })
                if len(questions) >= 22:
                    break
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Pythagorean triples (nice distances)
    triples = [
        ((0, 0), (3, 4), 5),
        ((0, 0), (5, 12), 13),
        ((0, 0), (8, 6), 10),
        ((1, 1), (4, 5), 5),
        ((2, 3), (5, 7), 5),
        ((0, 0), (6, 8), 10),
        ((1, 2), (4, 6), 5),
        ((0, 0), (9, 12), 15),
        ((2, 1), (5, 5), 5),
        ((3, 2), (6, 6), 5),
        ((0, 0), (4, 3), 5),
        ((0, 0), (12, 5), 13),
        ((1, 0), (4, 4), 5),
        ((2, 2), (5, 6), 5),
    ]
    for p1, p2, d in triples:
        opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1), str(d + 2)])
        questions.append({
            'text': f"Distance from {p1} to {p2}?",
            'opts': opts, 'idx': idx,
            'exp': f"d = √[({p2[0]}-{p1[0]})² + ({p2[1]}-{p1[1]})²] = {d}."
        })
        if len(questions) >= 38:
            break
    
    # Distance with square root answer
    sqrt_cases = [
        ((0, 0), (1, 1), "√2"),
        ((0, 0), (1, 2), "√5"),
        ((0, 0), (2, 1), "√5"),
        ((0, 0), (1, 3), "√10"),
        ((0, 0), (2, 2), "√8 or 2√2"),
        ((1, 1), (3, 2), "√5"),
        ((0, 0), (3, 1), "√10"),
        ((1, 2), (2, 4), "√5"),
    ]
    for p1, p2, d in sqrt_cases:
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        sq = dx*dx + dy*dy
        opts, idx = shuffle_options(f"√{sq}", [f"√{sq+1}", f"√{sq-1}" if sq > 1 else "1", str(sq)])
        questions.append({
            'text': f"Distance from {p1} to {p2}?",
            'opts': opts, 'idx': idx,
            'exp': f"d = √({dx}² + {dy}²) = √{sq}."
        })
        if len(questions) >= 45:
            break
    
    # More distance calculations
    for x1, y1, x2, y2 in [(0, 0, 4, 3), (1, 2, 4, 6), (2, 1, 5, 5), (0, 3, 4, 0), (1, 1, 7, 9), (0, 0, 5, 12), (3, 0, 0, 4)]:
        dx, dy = x2 - x1, y2 - y1
        sq = dx*dx + dy*dy
        d = int(sq ** 0.5) if sq ** 0.5 == int(sq ** 0.5) else f"√{sq}"
        if isinstance(d, int):
            opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1) if d > 1 else "1", f"√{sq}"])
        else:
            opts, idx = shuffle_options(d, [f"√{sq+1}", f"√{sq-1}", str(sq)])
        questions.append({
            'text': f"Distance from ({x1}, {y1}) to ({x2}, {y2})?",
            'opts': opts, 'idx': idx,
            'exp': f"d = √({dx}² + {dy}²) = {d}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_3():
    """Midpoint Formula"""
    questions = []
    
    # Midpoint formula
    opts, idx = shuffle_options("((x₁+x₂)/2, (y₁+y₂)/2)", ["(x₂-x₁, y₂-y₁)", ["(x₁×x₂, y₁×y₂)"], "(x₁+x₂, y₁+y₂)"])
    questions.append({
        'text': "What is the midpoint formula?",
        'opts': opts, 'idx': idx,
        'exp': "M = ((x₁+x₂)/2, (y₁+y₂)/2)"
    })
    
    # Simple midpoints (integer results)
    for x1 in range(0, 6, 2):
        for x2 in range(x1 + 2, x1 + 8, 2):
            for y1 in range(0, 6, 2):
                for y2 in range(y1 + 2, y1 + 8, 2):
                    mx, my = (x1 + x2) // 2, (y1 + y2) // 2
                    ans = f"({mx}, {my})"
                    opts, idx = shuffle_options(ans, [f"({mx+1}, {my})", f"({mx}, {my+1})", f"({mx-1}, {my-1})"])
                    questions.append({
                        'text': f"Midpoint of ({x1}, {y1}) and ({x2}, {y2})?",
                        'opts': opts, 'idx': idx,
                        'exp': f"M = (({x1}+{x2})/2, ({y1}+{y2})/2) = {ans}."
                    })
                    if len(questions) >= 20:
                        break
                if len(questions) >= 20:
                    break
            if len(questions) >= 20:
                break
        if len(questions) >= 20:
            break
    
    # Midpoints with fractions
    for x1, x2 in [(1, 4), (2, 5), (0, 3), (1, 6), (3, 8)]:
        for y1, y2 in [(1, 4), (2, 7), (0, 5), (3, 6)]:
            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2
            if mx == int(mx):
                mx = int(mx)
            if my == int(my):
                my = int(my)
            ans = f"({mx}, {my})"
            opts, idx = shuffle_options(ans, [f"({mx}, {my + 0.5 if isinstance(my, float) else my + 1})", f"({x1 + x2}, {y1 + y2})", f"({mx + 1 if isinstance(mx, int) else mx + 0.5}, {my})"])
            questions.append({
                'text': f"Midpoint of ({x1}, {y1}) and ({x2}, {y2})?",
                'opts': opts, 'idx': idx,
                'exp': f"M = (({x1}+{x2})/2, ({y1}+{y2})/2) = {ans}."
            })
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Find endpoint given midpoint and one point
    for x1, y1, mx, my in [(2, 3, 5, 4), (1, 2, 4, 5), (0, 0, 3, 2), (3, 1, 5, 3)]:
        x2, y2 = 2 * mx - x1, 2 * my - y1
        ans = f"({x2}, {y2})"
        opts, idx = shuffle_options(ans, [f"({x2+1}, {y2})", f"({x2}, {y2+1})", f"({mx}, {my})"])
        questions.append({
            'text': f"A({x1}, {y1}), midpoint M({mx}, {my}). Find B.",
            'opts': opts, 'idx': idx,
            'exp': f"B = (2×{mx}-{x1}, 2×{my}-{y1}) = {ans}."
        })
    
    # Midpoint on axis
    for x1, y1, x2, y2 in [(-2, 3, 2, 3), (4, -1, 4, 5), (-3, 2, 3, 2)]:
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        ans = f"({mx}, {my})"
        opts, idx = shuffle_options(ans, [f"({mx+1}, {my})", f"({mx}, {my+1})", f"({x1}, {y1})"])
        questions.append({
            'text': f"Midpoint of ({x1}, {y1}) and ({x2}, {y2})?",
            'opts': opts, 'idx': idx,
            'exp': f"M = {ans}."
        })
        if len(questions) >= 45:
            break
    
    # Fill remaining
    for x1 in range(1, 8):
        for y1 in range(1, 6):
            x2, y2 = x1 + 4, y1 + 2
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2
            ans = f"({mx}, {my})"
            opts, idx = shuffle_options(ans, [f"({mx+1}, {my+1})", f"({x1+x2}, {y1+y2})", f"({mx-1}, {my})"])
            questions.append({
                'text': f"Midpoint of ({x1}, {y1}) and ({x2}, {y2})?",
                'opts': opts, 'idx': idx,
                'exp': f"M = {ans}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_4():
    """Slope of a Line"""
    questions = []
    
    # Slope formula
    opts, idx = shuffle_options("(y₂ - y₁)/(x₂ - x₁)", ["(x₂ - x₁)/(y₂ - y₁)", "(y₂ + y₁)/(x₂ + x₁)", "y₂ - x₂"])
    questions.append({
        'text': "What is the slope formula?",
        'opts': opts, 'idx': idx,
        'exp': "m = (y₂ - y₁)/(x₂ - x₁) = rise/run."
    })
    
    # Positive slope meaning
    opts, idx = shuffle_options("Line rises left to right", ["Line falls left to right", "Line is horizontal", "Line is vertical"])
    questions.append({
        'text': "What does a positive slope mean?",
        'opts': opts, 'idx': idx,
        'exp': "Positive slope → line goes up as you move right."
    })
    
    # Negative slope meaning
    opts, idx = shuffle_options("Line falls left to right", ["Line rises left to right", "Line is horizontal", "Line is vertical"])
    questions.append({
        'text': "What does a negative slope mean?",
        'opts': opts, 'idx': idx,
        'exp': "Negative slope → line goes down as you move right."
    })
    
    # Zero slope
    opts, idx = shuffle_options("Horizontal line", ["Vertical line", "45° line", "Undefined"])
    questions.append({
        'text': "What does slope = 0 mean?",
        'opts': opts, 'idx': idx,
        'exp': "Slope 0 → horizontal line (no rise)."
    })
    
    # Undefined slope
    opts, idx = shuffle_options("Vertical line", ["Horizontal line", "45° line", "Slope = 0"])
    questions.append({
        'text': "When is slope undefined?",
        'opts': opts, 'idx': idx,
        'exp': "Undefined slope → vertical line (no run)."
    })
    
    # Read slope from y = mx + c
    for m in range(-5, 8):
        if m != 0:
            for c in range(0, 5):
                opts, idx = shuffle_options(str(m), [str(c), str(m + 1), str(-m)])
                eq = f"y = {m}x + {c}" if m != 1 else f"y = x + {c}"
                if m == -1:
                    eq = f"y = -x + {c}"
                questions.append({
                    'text': f"What is the slope of {eq}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"In y = mx + c, slope m = {m}."
                })
                if len(questions) >= 22:
                    break
        if len(questions) >= 22:
            break
    
    # Slope from rise and run
    for rise in range(1, 6):
        for run in range(1, 6):
            g = gcd(rise, run)
            m_num, m_den = rise // g, run // g
            if m_den == 1:
                ans = str(m_num)
            else:
                ans = f"{m_num}/{m_den}"
            opts, idx = shuffle_options(ans, [f"{run}/{rise}" if rise != run else "2", str(rise + run), str(rise)])
            questions.append({
                'text': f"Rise = {rise}, run = {run}. Slope?",
                'opts': opts, 'idx': idx,
                'exp': f"m = rise/run = {rise}/{run} = {ans}."
            })
            if len(questions) >= 38:
                break
        if len(questions) >= 38:
            break
    
    # Steeper slope comparison
    slopes = [(2, 3), (1, 4), (0.5, 1), (3, 5)]
    for m1, m2 in slopes:
        steeper = str(m2) if abs(m2) > abs(m1) else str(m1)
        opts, idx = shuffle_options(f"m = {steeper}", [f"m = {m1}", f"m = {m2}", "Same steepness"])
        questions.append({
            'text': f"Which is steeper: m = {m1} or m = {m2}?",
            'opts': opts, 'idx': idx,
            'exp': f"|{steeper}| is larger, so steeper."
        })
        if len(questions) >= 45:
            break
    
    # Horizontal lines
    for c in range(1, 10):
        opts, idx = shuffle_options("0", [str(c), "Undefined", "1"])
        questions.append({
            'text': f"Slope of y = {c}?",
            'opts': opts, 'idx': idx,
            'exp': "Horizontal line → slope = 0."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_5():
    """Slope from Two Points"""
    questions = []
    
    # Integer slopes
    for x1 in range(0, 5):
        for y1 in range(0, 5):
            for m in range(1, 5):
                x2 = x1 + 1
                y2 = y1 + m
                ans = str(m)
                opts, idx = shuffle_options(ans, [str(m + 1), str(m - 1) if m > 1 else "0", str(-m)])
                questions.append({
                    'text': f"Slope through ({x1}, {y1}) and ({x2}, {y2})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"m = ({y2}-{y1})/({x2}-{x1}) = {m}/1 = {ans}."
                })
                if len(questions) >= 15:
                    break
            if len(questions) >= 15:
                break
        if len(questions) >= 15:
            break
    
    # Negative integer slopes
    for x1 in range(1, 5):
        for y1 in range(3, 8):
            for m in range(1, 4):
                x2 = x1 + 1
                y2 = y1 - m
                ans = str(-m)
                opts, idx = shuffle_options(ans, [str(m), str(-m - 1), str(-m + 1) if m > 1 else "0"])
                questions.append({
                    'text': f"Slope through ({x1}, {y1}) and ({x2}, {y2})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"m = ({y2}-{y1})/({x2}-{x1}) = {-m}/1 = {ans}."
                })
                if len(questions) >= 25:
                    break
            if len(questions) >= 25:
                break
        if len(questions) >= 25:
            break
    
    # Fractional slopes
    for x1, y1, x2, y2 in [(0, 0, 2, 1), (1, 1, 3, 2), (0, 0, 4, 1), (2, 3, 4, 4), (1, 2, 5, 4)]:
        dy, dx = y2 - y1, x2 - x1
        g = gcd(abs(dy), abs(dx))
        num, den = dy // g, dx // g
        if den == 1:
            ans = str(num)
        else:
            ans = f"{num}/{den}"
        opts, idx = shuffle_options(ans, [f"{den}/{num}" if num != 0 else "0", str(dy + dx), f"{num + 1}/{den}"])
        questions.append({
            'text': f"Slope through ({x1}, {y1}) and ({x2}, {y2})?",
            'opts': opts, 'idx': idx,
            'exp': f"m = {dy}/{dx} = {ans}."
        })
    
    # Zero slope (horizontal)
    for y in range(1, 8):
        for x1 in range(0, 4):
            x2 = x1 + 3
            opts, idx = shuffle_options("0", [str(y), "Undefined", str(x2 - x1)])
            questions.append({
                'text': f"Slope through ({x1}, {y}) and ({x2}, {y})?",
                'opts': opts, 'idx': idx,
                'exp': f"Same y-values → horizontal → m = 0."
            })
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # Undefined slope (vertical)
    for x in range(1, 7):
        for y1 in range(0, 4):
            y2 = y1 + 3
            opts, idx = shuffle_options("Undefined", ["0", str(x), str(y2 - y1)])
            questions.append({
                'text': f"Slope through ({x}, {y1}) and ({x}, {y2})?",
                'opts': opts, 'idx': idx,
                'exp': f"Same x-values → vertical → undefined."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_6():
    """Equation y = mx + c"""
    questions = []
    
    # Identify slope
    for m in range(-4, 6):
        if m != 0:
            for c in range(-3, 5):
                eq = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
                if m == 1:
                    eq = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
                if m == -1:
                    eq = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
                opts, idx = shuffle_options(str(m), [str(c), str(m + 1), str(-m)])
                questions.append({
                    'text': f"Slope of {eq}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"In y = mx + c, m = {m}."
                })
                if len(questions) >= 12:
                    break
        if len(questions) >= 12:
            break
    
    # Identify y-intercept
    for m in range(1, 5):
        for c in range(-4, 6):
            eq = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            opts, idx = shuffle_options(str(c), [str(m), str(c + 1), str(-c)])
            questions.append({
                'text': f"Y-intercept of {eq}?",
                'opts': opts, 'idx': idx,
                'exp': f"In y = mx + c, c = {c}."
            })
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Write equation from slope and intercept
    for m in range(1, 6):
        for c in range(0, 6):
            ans = f"y = {m}x + {c}" if c > 0 else f"y = {m}x" if c == 0 else f"y = {m}x - {abs(c)}"
            opts, idx = shuffle_options(ans, [f"y = {c}x + {m}", f"y = {m}x + {c+1}", f"y = x + {m+c}"])
            questions.append({
                'text': f"Equation with slope {m} and y-intercept {c}?",
                'opts': opts, 'idx': idx,
                'exp': f"y = mx + c = {ans}."
            })
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Find y for given x
    for m in range(2, 5):
        for c in range(1, 4):
            for x in range(1, 5):
                y = m * x + c
                opts, idx = shuffle_options(str(y), [str(y + 1), str(y - 1), str(m * x)])
                questions.append({
                    'text': f"y = {m}x + {c}. Find y when x = {x}.",
                    'opts': opts, 'idx': idx,
                    'exp': f"y = {m}({x}) + {c} = {y}."
                })
                if len(questions) >= 45:
                    break
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # Find x for given y
    for m in range(2, 5):
        for c in range(0, 3):
            for x in range(1, 5):
                y = m * x + c
                opts, idx = shuffle_options(str(x), [str(x + 1), str(x - 1) if x > 1 else "0", str(y)])
                questions.append({
                    'text': f"y = {m}x + {c}. Find x when y = {y}.",
                    'opts': opts, 'idx': idx,
                    'exp': f"{y} = {m}x + {c}, x = {x}."
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_7():
    """Finding Equations"""
    questions = []
    
    # From slope and point
    for m in range(1, 5):
        for x1 in range(1, 4):
            for y1 in range(1, 5):
                c = y1 - m * x1
                if c >= 0:
                    ans = f"y = {m}x + {c}" if c > 0 else f"y = {m}x"
                else:
                    ans = f"y = {m}x - {abs(c)}"
                opts, idx = shuffle_options(ans, [f"y = {m}x + {y1}", f"y = {x1}x + {y1}", f"y = {m}x + {c + 1 if c >= 0 else c - 1}"])
                questions.append({
                    'text': f"Line with slope {m} through ({x1}, {y1})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"c = {y1} - {m}({x1}) = {c}. {ans}"
                })
                if len(questions) >= 18:
                    break
            if len(questions) >= 18:
                break
        if len(questions) >= 18:
            break
    
    # From two points (integer slope)
    for x1, y1, x2, y2 in [(0, 1, 1, 3), (1, 2, 2, 4), (0, 0, 2, 4), (1, 1, 3, 5), (0, 2, 1, 5)]:
        m = (y2 - y1) // (x2 - x1)
        c = y1 - m * x1
        if c >= 0:
            ans = f"y = {m}x + {c}" if c > 0 else f"y = {m}x"
        else:
            ans = f"y = {m}x - {abs(c)}"
        opts, idx = shuffle_options(ans, [f"y = {m + 1}x + {c}", f"y = {m}x + {c + 1 if c >= 0 else c - 1}", f"y = {c}x + {m}"])
        questions.append({
            'text': f"Equation through ({x1}, {y1}) and ({x2}, {y2})?",
            'opts': opts, 'idx': idx,
            'exp': f"m = {m}, c = {c}. {ans}"
        })
    
    # From y-intercept and another point
    for c in range(0, 5):
        for x in range(1, 4):
            for m in range(1, 5):
                y = m * x + c
                if c > 0:
                    ans = f"y = {m}x + {c}"
                elif c == 0:
                    ans = f"y = {m}x"
                else:
                    ans = f"y = {m}x - {abs(c)}"
                opts, idx = shuffle_options(ans, [f"y = {m+1}x + {c}", f"y = {c}x + {m}", f"y = {m}x + {c+1}"])
                questions.append({
                    'text': f"Line through (0, {c}) and ({x}, {y})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"c = {c}, m = ({y}-{c})/{x} = {m}. {ans}"
                })
                if len(questions) >= 35:
                    break
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Point-slope form
    for m in range(1, 4):
        for x1, y1 in [(2, 3), (1, 4), (3, 2), (2, 5), (4, 1)]:
            c = y1 - m * x1
            if c >= 0:
                ans = f"y = {m}x + {c}" if c != 0 else f"y = {m}x"
            else:
                ans = f"y = {m}x - {abs(c)}"
            opts, idx = shuffle_options(ans, [f"y - {y1} = {m}(x - {x1})", f"y = {m}x + {y1}", f"y = {m}x - {c if c >= 0 else abs(c)}"])
            questions.append({
                'text': f"Slope {m}, point ({x1}, {y1}). Give y = mx + c form.",
                'opts': opts, 'idx': idx,
                'exp': f"c = {y1} - {m}×{x1} = {c}. {ans}"
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_8():
    """Parallel Lines"""
    questions = []
    
    # Parallel lines property
    opts, idx = shuffle_options("Equal slopes", ["Perpendicular slopes", "Opposite slopes", "Zero slopes"])
    questions.append({
        'text': "What do parallel lines have?",
        'opts': opts, 'idx': idx,
        'exp': "Parallel lines have equal slopes (m₁ = m₂)."
    })
    
    # Identify parallel from equations
    parallel_pairs = [
        ("y = 2x + 1", "y = 2x + 5", "Yes"),
        ("y = 3x + 2", "y = 3x - 4", "Yes"),
        ("y = x + 1", "y = x + 7", "Yes"),
        ("y = 2x + 1", "y = 3x + 1", "No"),
        ("y = 4x - 2", "y = 4x + 3", "Yes"),
        ("y = -2x + 5", "y = -2x - 1", "Yes"),
        ("y = 5x + 3", "y = -5x + 3", "No"),
    ]
    for eq1, eq2, ans in parallel_pairs:
        opts, idx = shuffle_options(ans, ["Yes", "No", "Cannot tell", "Only if c is same"])
        questions.append({
            'text': f"Are {eq1} and {eq2} parallel?",
            'opts': opts, 'idx': idx,
            'exp': f"{'Same slopes' if ans == 'Yes' else 'Different slopes'} → {ans}."
        })
    
    # Find slope of parallel line
    for m in range(-4, 6):
        if m != 0:
            for c in range(0, 4):
                eq = f"y = {m}x + {c}"
                if m == 1:
                    eq = f"y = x + {c}"
                opts, idx = shuffle_options(str(m), [str(m + 1), str(-m), str(c)])
                questions.append({
                    'text': f"Slope of line parallel to {eq}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Parallel → same slope = {m}."
                })
                if len(questions) >= 22:
                    break
        if len(questions) >= 22:
            break
    
    # Write equation parallel to given line through point
    for m in range(1, 5):
        for c1 in range(1, 4):
            for x1, y1 in [(1, 2), (2, 3), (0, 4)]:
                c2 = y1 - m * x1
                eq1 = f"y = {m}x + {c1}"
                if c2 >= 0:
                    ans = f"y = {m}x + {c2}" if c2 > 0 else f"y = {m}x"
                else:
                    ans = f"y = {m}x - {abs(c2)}"
                opts, idx = shuffle_options(ans, [f"y = {m}x + {c1}", f"y = {m+1}x + {c2}", f"y = {-m}x + {c2}"])
                questions.append({
                    'text': f"Line parallel to {eq1} through ({x1}, {y1})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Same slope {m}, new c = {c2}. {ans}"
                })
                if len(questions) >= 38:
                    break
            if len(questions) >= 38:
                break
        if len(questions) >= 38:
            break
    
    # Which lines are parallel
    for m in range(2, 5):
        c1, c2, c3 = 1, 4, 7
        lines = [f"y = {m}x + {c1}", f"y = {m}x + {c2}", f"y = {m+1}x + {c3}"]
        opts, idx = shuffle_options(f"{lines[0]} and {lines[1]}", [f"{lines[1]} and {lines[2]}", f"{lines[0]} and {lines[2]}", "None"])
        questions.append({
            'text': f"Which are parallel: {lines[0]}, {lines[1]}, {lines[2]}?",
            'opts': opts, 'idx': idx,
            'exp': f"First two have slope {m}."
        })
        if len(questions) >= 45:
            break
    
    # Parallel to x-axis or y-axis
    opts, idx = shuffle_options("0", ["Undefined", "1", "-1"])
    questions.append({
        'text': "Slope of line parallel to x-axis?",
        'opts': opts, 'idx': idx,
        'exp': "Parallel to x-axis → horizontal → m = 0."
    })
    
    opts, idx = shuffle_options("Undefined", ["0", "1", "-1"])
    questions.append({
        'text': "Slope of line parallel to y-axis?",
        'opts': opts, 'idx': idx,
        'exp': "Parallel to y-axis → vertical → undefined."
    })
    
    # Fill remaining
    for m in range(1, 10):
        opts, idx = shuffle_options(str(m), [str(m + 1), str(-m), "0"])
        questions.append({
            'text': f"Line parallel to y = {m}x + 10 has slope?",
            'opts': opts, 'idx': idx,
            'exp': f"Parallel → same slope = {m}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_9():
    """Perpendicular Lines"""
    questions = []
    
    # Perpendicular slopes property
    opts, idx = shuffle_options("m₁ × m₂ = -1", ["m₁ = m₂", ["m₁ + m₂ = 0"], "m₁ - m₂ = 1"])
    questions.append({
        'text': "What is the relationship for perpendicular slopes?",
        'opts': opts, 'idx': idx,
        'exp': "Perpendicular: m₁ × m₂ = -1 (negative reciprocals)."
    })
    
    # Find perpendicular slope
    perp_pairs = [
        (2, "-1/2"), (3, "-1/3"), (4, "-1/4"), (-2, "1/2"), (-3, "1/3"),
        (1, "-1"), (-1, "1"), (5, "-1/5"), (-4, "1/4"), (6, "-1/6"), (-5, "1/5"),
        (7, "-1/7"), (-6, "1/6"),
    ]
    for m, perp in perp_pairs:
        opts, idx = shuffle_options(perp, [str(m), str(-m), "0"])
        questions.append({
            'text': f"Slope perpendicular to m = {m}?",
            'opts': opts, 'idx': idx,
            'exp': f"Perpendicular slope = -1/{m} = {perp}."
        })
    
    # Fractional slopes
    frac_perp = [
        ("1/2", "-2"), ("1/3", "-3"), ("2/3", "-3/2"), ("-1/2", "2"),
        ("3/4", "-4/3"), ("-2/5", "5/2"),
    ]
    for m, perp in frac_perp:
        opts, idx = shuffle_options(perp, [m, "0", "1"])
        questions.append({
            'text': f"Slope perpendicular to m = {m}?",
            'opts': opts, 'idx': idx,
            'exp': f"Flip and negate: {perp}."
        })
    
    # Are lines perpendicular?
    perp_checks = [
        ("y = 2x + 1", "y = -1/2x + 3", "Yes"),
        ("y = 3x + 1", "y = -1/3x + 5", "Yes"),
        ("y = x + 1", "y = -x + 2", "Yes"),
        ("y = 2x + 1", "y = 2x + 3", "No"),
        ("y = 4x - 1", "y = -1/4x + 2", "Yes"),
        ("y = 3x", "y = 3x + 5", "No"),
    ]
    for eq1, eq2, ans in perp_checks:
        opts, idx = shuffle_options(ans, ["Yes", "No", "Cannot tell", "Only sometimes"])
        questions.append({
            'text': f"Are {eq1} and {eq2} perpendicular?",
            'opts': opts, 'idx': idx,
            'exp': f"Product of slopes {'= -1' if ans == 'Yes' else '≠ -1'}. {ans}."
        })
    
    # Equation perpendicular to given through point
    for m in [2, 3, -2]:
        for x1, y1 in [(0, 0), (1, 2), (2, 1)]:
            if m == 2:
                perp_m = "-1/2"
                c = y1  # simplified for m = -1/2 through origin or simple point
            elif m == 3:
                perp_m = "-1/3"
                c = y1
            else:
                perp_m = "1/2"
                c = y1
            # Simplified - just test the perpendicular slope
            opts, idx = shuffle_options(perp_m, [str(m), str(-m), "0"])
            questions.append({
                'text': f"Slope of line ⊥ to y = {m}x + 1?",
                'opts': opts, 'idx': idx,
                'exp': f"Perpendicular slope = {perp_m}."
            })
            if len(questions) >= 38:
                break
        if len(questions) >= 38:
            break
    
    # Special cases
    opts, idx = shuffle_options("Vertical", ["Horizontal", "45°", "Parallel"])
    questions.append({
        'text': "Line perpendicular to horizontal is?",
        'opts': opts, 'idx': idx,
        'exp': "Horizontal (m=0) ⊥ Vertical (undefined)."
    })
    
    opts, idx = shuffle_options("Horizontal", ["Vertical", "45°", "Parallel"])
    questions.append({
        'text': "Line perpendicular to vertical is?",
        'opts': opts, 'idx': idx,
        'exp': "Vertical (undefined) ⊥ Horizontal (m=0)."
    })
    
    # Fill remaining
    for m in range(2, 15):
        perp = f"-1/{m}"
        opts, idx = shuffle_options(perp, [str(m), f"1/{m}", str(-m)])
        questions.append({
            'text': f"Perpendicular slope to m = {m}?",
            'opts': opts, 'idx': idx,
            'exp': f"-1/{m} = {perp}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_10():
    """Intersecting Lines"""
    questions = []
    
    # Find intersection
    for a in range(1, 4):
        for b in range(1, 4):
            if a != b:
                for c1 in range(0, 3):
                    for c2 in range(c1 + 1, c1 + 4):
                        # y = ax + c1, y = bx + c2
                        # ax + c1 = bx + c2 → x = (c2 - c1)/(a - b)
                        if (c2 - c1) % (a - b) == 0:
                            x = (c2 - c1) // (a - b)
                            y = a * x + c1
                            if x > 0 and y > 0:
                                ans = f"({x}, {y})"
                                opts, idx = shuffle_options(ans, [f"({x+1}, {y})", f"({x}, {y+1})", f"({y}, {x})"])
                                questions.append({
                                    'text': f"Intersection of y = {a}x + {c1} and y = {b}x + {c2}?",
                                    'opts': opts, 'idx': idx,
                                    'exp': f"Solve: {a}x + {c1} = {b}x + {c2}. x = {x}, y = {y}."
                                })
                        if len(questions) >= 18:
                            break
                    if len(questions) >= 18:
                        break
                if len(questions) >= 18:
                    break
            if len(questions) >= 18:
                break
        if len(questions) >= 18:
            break
    
    # Line meets x-axis (y = 0)
    for m in range(1, 5):
        for c in range(2, 10, 2):
            if c % m == 0:
                x_int = -c // m
                if x_int < 0:
                    x_int = c // m  # For positive intersection with negative c
                    c = -c
                ans = f"({-c // m}, 0)"
                opts, idx = shuffle_options(ans, [f"(0, {c})", f"({c}, 0)", f"({m}, 0)"])
                questions.append({
                    'text': f"Where does y = {m}x + {c} meet x-axis?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Set y = 0: x = {-c // m}."
                })
                if len(questions) >= 28:
                    break
        if len(questions) >= 28:
            break
    
    # Line meets y-axis (x = 0)
    for m in range(1, 6):
        for c in range(1, 8):
            ans = f"(0, {c})"
            opts, idx = shuffle_options(ans, [f"({c}, 0)", f"({m}, {c})", f"(0, {m})"])
            questions.append({
                'text': f"Where does y = {m}x + {c} meet y-axis?",
                'opts': opts, 'idx': idx,
                'exp': f"Set x = 0: y = {c}."
            })
            if len(questions) >= 36:
                break
        if len(questions) >= 36:
            break
    
    # Do lines intersect?
    for m in range(1, 4):
        for c1, c2 in [(1, 3), (2, 5), (0, 4)]:
            # Parallel lines don't intersect
            eq1 = f"y = {m}x + {c1}"
            eq2 = f"y = {m}x + {c2}"
            opts, idx = shuffle_options("No - parallel lines", ["Yes - at one point", "Yes - at many points", "Cannot tell"])
            questions.append({
                'text': f"Do {eq1} and {eq2} intersect?",
                'opts': opts, 'idx': idx,
                'exp': f"Same slope → parallel → no intersection."
            })
            if len(questions) >= 42:
                break
        if len(questions) >= 42:
            break
    
    # Simple intersections
    simple_ints = [
        ("y = x", "y = 2", "(2, 2)"),
        ("y = 2x", "y = 4", "(2, 4)"),
        ("y = x + 1", "y = 3", "(2, 3)"),
        ("y = 3x", "y = 6", "(2, 6)"),
        ("x = 3", "y = 5", "(3, 5)"),
        ("y = x", "y = 5", "(5, 5)"),
        ("y = 2x", "y = 8", "(4, 8)"),
        ("y = x + 2", "y = 6", "(4, 6)"),
        ("x = 4", "y = 3", "(4, 3)"),
        ("y = x", "y = 3", "(3, 3)"),
    ]
    for eq1, eq2, ans in simple_ints:
        opts, idx = shuffle_options(ans, [f"({ans[1]}, {ans[4]})" if len(ans) > 4 else "(0, 0)", "(1, 1)", "(0, 2)"])
        questions.append({
            'text': f"Intersection of {eq1} and {eq2}?",
            'opts': opts, 'idx': idx,
            'exp': f"Substitute to find {ans}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_11():
    """Area and Applications"""
    questions = []
    
    # Area of triangle with vertices
    triangles = [
        ((0, 0), (4, 0), (0, 3), 6),
        ((0, 0), (6, 0), (0, 4), 12),
        ((0, 0), (5, 0), (0, 4), 10),
        ((1, 1), (5, 1), (1, 4), 6),
        ((0, 0), (8, 0), (0, 6), 24),
        ((2, 0), (6, 0), (2, 5), 10),
    ]
    for p1, p2, p3, area in triangles:
        opts, idx = shuffle_options(str(area), [str(area + 2), str(area - 2) if area > 2 else "2", str(area * 2)])
        questions.append({
            'text': f"Area of triangle with vertices {p1}, {p2}, {p3}?",
            'opts': opts, 'idx': idx,
            'exp': f"Area = ½ × base × height = {area}."
        })
    
    # Area under line (triangle)
    for m in range(1, 4):
        for c in range(2, 6):
            x_int = c  # When y = 0 for y = -x + c style
            # For y = mx + c meeting axes
            # y-intercept: (0, c)
            # x-intercept: (-c/m, 0) - but we'll use positive cases
            if c % m == 0:
                base = c // m
                height = c
                area = (base * height) // 2
                opts, idx = shuffle_options(str(area), [str(area + 1), str(base * height), str(base + height)])
                questions.append({
                    'text': f"Area of triangle formed by y = -{m}x + {c} and axes?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Base = {base}, height = {c}. Area = ½×{base}×{c} = {area}."
                })
                if len(questions) >= 14:
                    break
        if len(questions) >= 14:
            break
    
    # Collinear points
    collinear = [
        ((0, 0), (1, 1), (2, 2), "Yes"),
        ((1, 2), (2, 4), (3, 6), "Yes"),
        ((0, 1), (1, 2), (2, 4), "No"),
        ((0, 0), (2, 1), (4, 2), "Yes"),
        ((1, 1), (2, 3), (3, 4), "No"),
    ]
    for p1, p2, p3, ans in collinear:
        opts, idx = shuffle_options(ans, ["Yes", "No", "Cannot tell", "Only two are"])
        questions.append({
            'text': f"Are {p1}, {p2}, {p3} collinear?",
            'opts': opts, 'idx': idx,
            'exp': f"Check if slopes are equal. {ans}."
        })
    
    # Distance applications
    for x1, y1, x2, y2 in [(0, 0, 3, 4), (1, 2, 4, 6), (2, 1, 5, 5)]:
        d = int(((x2-x1)**2 + (y2-y1)**2) ** 0.5)
        opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1) if d > 1 else "1", str((x2-x1) + (y2-y1))])
        questions.append({
            'text': f"Length of line segment from ({x1}, {y1}) to ({x2}, {y2})?",
            'opts': opts, 'idx': idx,
            'exp': f"d = √[({x2-x1})² + ({y2-y1})²] = {d}."
        })
    
    # Perimeter of triangle
    for base, height, hyp in [(3, 4, 5), (5, 12, 13), (6, 8, 10)]:
        perimeter = base + height + hyp
        opts, idx = shuffle_options(str(perimeter), [str(perimeter + 2), str(perimeter - 2), str(base * height // 2)])
        questions.append({
            'text': f"Right triangle with legs {base} and {height}. Perimeter?",
            'opts': opts, 'idx': idx,
            'exp': f"Hyp = {hyp}. P = {base} + {height} + {hyp} = {perimeter}."
        })
    
    # Ratio division
    for x1, y1, x2, y2 in [(0, 0, 8, 4), (1, 1, 5, 5), (2, 0, 6, 8)]:
        # Midpoint divides 1:1
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        ans = f"({mx}, {my})"
        opts, idx = shuffle_options(ans, [f"({mx + 1}, {my})", f"({x1 + x2}, {y1 + y2})", f"({mx}, {my + 1})"])
        questions.append({
            'text': f"Point dividing ({x1}, {y1}) to ({x2}, {y2}) in ratio 1:1?",
            'opts': opts, 'idx': idx,
            'exp': f"Midpoint = {ans}."
        })
        if len(questions) >= 38:
            break
    
    # Rectangle area from vertices
    rects = [
        ((0, 0), (4, 0), (4, 3), (0, 3), 12),
        ((1, 1), (5, 1), (5, 4), (1, 4), 12),
        ((0, 0), (6, 0), (6, 4), (0, 4), 24),
    ]
    for p1, p2, p3, p4, area in rects:
        opts, idx = shuffle_options(str(area), [str(area + 4), str(area - 4) if area > 4 else "4", str(area // 2)])
        questions.append({
            'text': f"Area of rectangle with vertices {p1}, {p2}, {p3}, {p4}?",
            'opts': opts, 'idx': idx,
            'exp': f"Area = length × width = {area}."
        })
    
    # Fill remaining
    for base in range(2, 8):
        for height in range(2, 8):
            area = (base * height) // 2
            opts, idx = shuffle_options(str(area), [str(area + 1), str(base * height), str(base + height)])
            questions.append({
                'text': f"Triangle with base {base} and height {height}. Area?",
                'opts': opts, 'idx': idx,
                'exp': f"Area = ½ × {base} × {height} = {area}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_12():
    """SEC Exam Style"""
    questions = []
    
    # Multi-step: find equation then use it
    for m in range(2, 4):
        for x1, y1 in [(1, 3), (2, 5), (1, 4)]:
            c = y1 - m * x1
            for x in range(3, 6):
                y = m * x + c
                opts, idx = shuffle_options(str(y), [str(y + 1), str(y - 1), str(m * x)])
                questions.append({
                    'text': f"Line through ({x1}, {y1}) with slope {m}. Find y when x = {x}.",
                    'opts': opts, 'idx': idx,
                    'exp': f"y = {m}x + {c}. When x = {x}, y = {y}."
                })
                if len(questions) >= 8:
                    break
            if len(questions) >= 8:
                break
        if len(questions) >= 8:
            break
    
    # Parallel line through point
    for m in range(2, 5):
        for c1 in range(1, 3):
            for x1, y1 in [(2, 3), (1, 5)]:
                c2 = y1 - m * x1
                if c2 >= 0:
                    ans = f"y = {m}x + {c2}" if c2 > 0 else f"y = {m}x"
                else:
                    ans = f"y = {m}x - {abs(c2)}"
                opts, idx = shuffle_options(ans, [f"y = {m}x + {c1}", f"y = {-m}x + {c2}", f"y = {m+1}x + {c2}"])
                questions.append({
                    'text': f"Line parallel to y = {m}x + {c1} through ({x1}, {y1})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Same slope {m}, c = {c2}."
                })
                if len(questions) >= 16:
                    break
            if len(questions) >= 16:
                break
        if len(questions) >= 16:
            break
    
    # Find k for parallel/perpendicular
    for k in range(2, 6):
        opts, idx = shuffle_options(str(k), [str(k + 1), str(k - 1), str(-k)])
        questions.append({
            'text': f"Lines y = {k}x + 1 and y = mx + 3 are parallel. Find m.",
            'opts': opts, 'idx': idx,
            'exp': f"Parallel → m = {k}."
        })
        if len(questions) >= 22:
            break
    
    # Distance and midpoint combined
    for x1, y1, x2, y2 in [(0, 0, 6, 8), (2, 1, 8, 9), (1, 2, 5, 5)]:
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        ans = f"({mx}, {my})"
        opts, idx = shuffle_options(ans, [f"({mx + 1}, {my})", f"({x1 + x2}, {y1 + y2})", f"({mx}, {my + 1})"])
        questions.append({
            'text': f"A({x1}, {y1}), B({x2}, {y2}). Midpoint?",
            'opts': opts, 'idx': idx,
            'exp': f"M = {ans}."
        })
    
    # Triangle vertices
    for p1, p2, p3, area in [((0, 0), (4, 0), (0, 6), 12), ((0, 0), (5, 0), (0, 4), 10)]:
        opts, idx = shuffle_options(str(area), [str(area + 2), str(area * 2), str(area - 2)])
        questions.append({
            'text': f"Area of triangle with vertices {p1}, {p2}, {p3}?",
            'opts': opts, 'idx': idx,
            'exp': f"Area = ½ × base × height = {area}."
        })
    
    # Intersection point
    for a, c1, b, c2, x, y in [(2, 1, 1, 3, 2, 5), (3, 2, 1, 4, 1, 5), (2, 0, 1, 2, 2, 4)]:
        ans = f"({x}, {y})"
        opts, idx = shuffle_options(ans, [f"({x + 1}, {y})", f"({x}, {y + 1})", f"({y}, {x})"])
        questions.append({
            'text': f"Intersection of y = {a}x + {c1} and y = {b}x + {c2}?",
            'opts': opts, 'idx': idx,
            'exp': f"Solve simultaneously. Point = {ans}."
        })
    
    # Perpendicular slope
    for m in [2, 3, 4, -2, -3]:
        if m > 0:
            perp = f"-1/{m}"
        else:
            perp = f"1/{abs(m)}"
        opts, idx = shuffle_options(perp, [str(m), str(-m), "0"])
        questions.append({
            'text': f"Slope perpendicular to m = {m}?",
            'opts': opts, 'idx': idx,
            'exp': f"Perpendicular → {perp}."
        })
        if len(questions) >= 40:
            break
    
    # Line through two points
    for x1, y1, x2, y2, m, c in [(0, 2, 1, 4, 2, 2), (0, 1, 2, 5, 2, 1), (1, 3, 2, 5, 2, 1), (0, 3, 1, 5, 2, 3), (1, 1, 3, 5, 2, -1), (0, 0, 2, 6, 3, 0), (2, 1, 4, 5, 2, -3)]:
        if c > 0:
            ans = f"y = {m}x + {c}"
        elif c == 0:
            ans = f"y = {m}x"
        else:
            ans = f"y = {m}x - {abs(c)}"
        opts, idx = shuffle_options(ans, [f"y = {m + 1}x + {c}", f"y = {c}x + {m}", f"y = {m}x + {c + 1 if c >= 0 else c - 1}"])
        questions.append({
            'text': f"Equation through ({x1}, {y1}) and ({x2}, {y2})?",
            'opts': opts, 'idx': idx,
            'exp': f"m = {m}, c = {c}. {ans}"
        })
        if len(questions) >= 48:
            break
    
    # Collinear check
    opts, idx = shuffle_options("Equal slopes", ["Equal distances", "Same quadrant", "On x-axis"])
    questions.append({
        'text': "How to check if three points are collinear?",
        'opts': opts, 'idx': idx,
        'exp': "Collinear if slope AB = slope BC."
    })
    
    opts, idx = shuffle_options("Slopes multiply to -1", ["Slopes are equal", "Slopes add to 0", "Same y-intercept"])
    questions.append({
        'text': "How to verify lines are perpendicular?",
        'opts': opts, 'idx': idx,
        'exp': "Perpendicular: m₁ × m₂ = -1."
    })
    
    # More SEC style questions
    for m in range(2, 6):
        c = m + 1
        opts, idx = shuffle_options(f"(0, {c})", [f"({c}, 0)", f"({m}, {c})", "(0, 0)"])
        questions.append({
            'text': f"Where does y = {m}x + {c} cross the y-axis?",
            'opts': opts, 'idx': idx,
            'exp': f"Y-intercept at (0, {c})."
        })
        if len(questions) >= 50:
            break
    
    for m in range(2, 6):
        opts, idx = shuffle_options(str(m), [str(m + 1), str(-m), "0"])
        questions.append({
            'text': f"What is the slope of y = {m}x - 5?",
            'opts': opts, 'idx': idx,
            'exp': f"In y = mx + c, slope = {m}."
        })
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
        "-- LC OL Coordinate Geometry (Lines) - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        "-- Create topic",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Coordinate Geometry (Lines)', {STRAND_ID}, '📐', 12, 1);",
        "",
        "-- Clear existing",
        f"DELETE FROM questions_adaptive WHERE topic = '{TOPIC_ID}';",
        "",
    ]
    
    for q in questions:
        txt = q['text'].replace("'", "''")
        a = q['opts'][0].replace("'", "''") if isinstance(q['opts'][0], str) else str(q['opts'][0])
        b = q['opts'][1].replace("'", "''") if isinstance(q['opts'][1], str) else str(q['opts'][1])
        c = q['opts'][2].replace("'", "''") if isinstance(q['opts'][2], str) else str(q['opts'][2])
        d = q['opts'][3].replace("'", "''") if isinstance(q['opts'][3], str) else str(q['opts'][3])
        exp = q['exp'].replace("'", "''")
        
        sql = f"INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode) VALUES ('{TOPIC_ID}', '{txt}', '{a}', '{b}', '{c}', '{d}', {q['idx']}, '{exp}', {q['level']}, '{q['band']}', 'adaptive');"
        lines.append(sql)
    
    lines.append("")
    lines.append(f"SELECT COUNT(*) as total FROM questions_adaptive WHERE topic = '{TOPIC_ID}';")
    
    return '\n'.join(lines)


if __name__ == "__main__":
    print("="*60)
    print("LC OL Coordinate Geometry (Lines) - 600 Questions Generator")
    print("="*60 + "\n")
    
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    
    sql = generate_sql(questions)
    with open('lc_ol_coord_lines_600.sql', 'w') as f:
        f.write(sql)
    
    print(f"Saved: lc_ol_coord_lines_600.sql ({len(sql):,} chars)")
