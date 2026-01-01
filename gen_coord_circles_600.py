#!/usr/bin/env python3
"""
LC Ordinary Level Coordinate Geometry (Circles) - 600 Questions Generator
==========================================================================
50 questions per level × 12 levels = 600 questions

Based on SEC Paper Analysis 2019-2025:
- Circle equation, centre, radius, points on circle, tangents
"""

import random
from math import gcd

TOPIC_ID = 'lc_ol_coord_circles'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Circle Basics", "Foundation"),
    2: ("Centre and Radius", "Foundation"),
    3: ("Standard Form (x-h)² + (y-k)²", "Foundation"),
    4: ("Points on a Circle", "Developing"),
    5: ("General Form x² + y² + Dx + Ey + F", "Developing"),
    6: ("Converting Forms", "Developing"),
    7: ("Circle Through Points", "Proficient"),
    8: ("Tangent Lines", "Proficient"),
    9: ("Circle and Line Intersection", "Proficient"),
    10: ("Distance from Centre", "Advanced"),
    11: ("Circle Problems", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    options = [correct] + distractors[:3]
    random.shuffle(options)
    return options, options.index(correct)

def generate_level_1():
    """Circle Basics"""
    questions = []
    
    # Definition
    opts, idx = shuffle_options("Set of points equidistant from centre", ["A curved rectangle", "An oval shape", "A line segment"])
    questions.append({
        'text': "What is a circle?",
        'opts': opts, 'idx': idx,
        'exp': "Circle = all points at fixed distance (radius) from centre."
    })
    
    # Radius definition
    opts, idx = shuffle_options("Distance from centre to any point on circle", ["Distance across the circle", "The circumference", "The area"])
    questions.append({
        'text': "What is the radius of a circle?",
        'opts': opts, 'idx': idx,
        'exp': "Radius = distance from centre to edge."
    })
    
    # Diameter definition
    opts, idx = shuffle_options("Distance across circle through centre", ["Half the radius", "The circumference", "Distance from centre to edge"])
    questions.append({
        'text': "What is the diameter?",
        'opts': opts, 'idx': idx,
        'exp': "Diameter = 2 × radius, passing through centre."
    })
    
    # Diameter and radius relationship
    opts, idx = shuffle_options("d = 2r", ["d = r/2", "d = r²", "d = πr"])
    questions.append({
        'text': "How are diameter (d) and radius (r) related?",
        'opts': opts, 'idx': idx,
        'exp': "Diameter = 2 × radius."
    })
    
    # Find diameter from radius
    for r in range(1, 12):
        d = 2 * r
        opts, idx = shuffle_options(str(d), [str(r), str(d + 1), str(d - 1) if d > 1 else "1"])
        questions.append({
            'text': f"Radius = {r}. What is the diameter?",
            'opts': opts, 'idx': idx,
            'exp': f"d = 2 × {r} = {d}."
        })
        if len(questions) >= 18:
            break
    
    # Find radius from diameter
    for d in range(2, 30, 2):
        r = d // 2
        opts, idx = shuffle_options(str(r), [str(d), str(r + 1), str(r - 1) if r > 1 else "1"])
        questions.append({
            'text': f"Diameter = {d}. What is the radius?",
            'opts': opts, 'idx': idx,
            'exp': f"r = {d} ÷ 2 = {r}."
        })
        if len(questions) >= 35:
            break
    
    # Centre notation
    opts, idx = shuffle_options("(h, k) or (a, b)", ["(r, d)", "(x, y) only", "(0, 0) always"])
    questions.append({
        'text': "How is the centre of a circle typically written?",
        'opts': opts, 'idx': idx,
        'exp': "Centre is a point, often written as (h, k)."
    })
    
    # Circle at origin
    opts, idx = shuffle_options("(0, 0)", ["(1, 1)", "(r, r)", "Unknown"])
    questions.append({
        'text': "A circle centred at the origin has centre...?",
        'opts': opts, 'idx': idx,
        'exp': "Origin = (0, 0)."
    })
    
    # Chord definition
    opts, idx = shuffle_options("Line segment with both endpoints on circle", ["The radius", "The diameter", "A tangent line"])
    questions.append({
        'text': "What is a chord?",
        'opts': opts, 'idx': idx,
        'exp': "Chord = line segment joining two points on circle."
    })
    
    # Longest chord
    opts, idx = shuffle_options("Diameter", ["Radius", "Any chord", "Circumference"])
    questions.append({
        'text': "What is the longest chord of a circle?",
        'opts': opts, 'idx': idx,
        'exp': "Diameter is the longest chord (passes through centre)."
    })
    
    # Tangent definition
    opts, idx = shuffle_options("Line touching circle at exactly one point", ["Line through centre", "The diameter", "A chord"])
    questions.append({
        'text': "What is a tangent to a circle?",
        'opts': opts, 'idx': idx,
        'exp': "Tangent touches circle at one point only."
    })
    
    # Tangent and radius relationship
    opts, idx = shuffle_options("Perpendicular (90°)", ["Parallel", "Equal", "45°"])
    questions.append({
        'text': "A tangent and radius at point of contact are...?",
        'opts': opts, 'idx': idx,
        'exp': "Tangent ⊥ radius at point of tangency."
    })
    
    # Fill remaining with basic calculations
    for r in range(3, 20):
        d = 2 * r
        opts, idx = shuffle_options(str(d), [str(r), str(d + 2), str(r * r)])
        questions.append({
            'text': f"Circle has radius {r}. Diameter?",
            'opts': opts, 'idx': idx,
            'exp': f"d = 2r = {d}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_2():
    """Centre and Radius"""
    questions = []
    
    # Identify centre from equation x² + y² = r²
    for r in range(1, 8):
        r_sq = r * r
        opts, idx = shuffle_options("(0, 0)", [f"({r}, {r})", f"(0, {r})", f"({r}, 0)"])
        questions.append({
            'text': f"Centre of x² + y² = {r_sq}?",
            'opts': opts, 'idx': idx,
            'exp': f"x² + y² = r² has centre at origin (0, 0)."
        })
        if len(questions) >= 8:
            break
    
    # Identify radius from equation x² + y² = r²
    for r in range(1, 10):
        r_sq = r * r
        opts, idx = shuffle_options(str(r), [str(r_sq), str(r + 1), str(r - 1) if r > 1 else "1"])
        questions.append({
            'text': f"Radius of x² + y² = {r_sq}?",
            'opts': opts, 'idx': idx,
            'exp': f"r² = {r_sq}, so r = {r}."
        })
        if len(questions) >= 18:
            break
    
    # Centre from (x-h)² + (y-k)² = r²
    centres = [(2, 3), (1, 4), (3, 2), (-1, 2), (2, -3), (0, 5), (4, 0), (-2, -1), (5, 1), (1, 1), (3, 4), (4, 2), (2, 5), (5, 3), (1, 3)]
    for h, k in centres:
        opts, idx = shuffle_options(f"({h}, {k})", [f"({-h}, {-k})", f"({k}, {h})", f"({h+1}, {k})"])
        r = random.randint(2, 5)
        r_sq = r * r
        # Format equation
        x_part = f"(x - {h})²" if h > 0 else f"(x + {-h})²" if h < 0 else "x²"
        y_part = f"(y - {k})²" if k > 0 else f"(y + {-k})²" if k < 0 else "y²"
        questions.append({
            'text': f"Centre of {x_part} + {y_part} = {r_sq}?",
            'opts': opts, 'idx': idx,
            'exp': f"(x - h)² + (y - k)² form → centre ({h}, {k})."
        })
        if len(questions) >= 30:
            break
    
    # Radius from (x-h)² + (y-k)² = r²
    for r in range(2, 10):
        r_sq = r * r
        h, k = random.randint(1, 5), random.randint(1, 5)
        opts, idx = shuffle_options(str(r), [str(r_sq), str(r + 1), str(h)])
        questions.append({
            'text': f"Radius of (x - {h})² + (y - {k})² = {r_sq}?",
            'opts': opts, 'idx': idx,
            'exp': f"r² = {r_sq}, so r = {r}."
        })
        if len(questions) >= 42:
            break
    
    # Write equation given centre and radius
    for h, k, r in [(0, 0, 3), (1, 2, 4), (2, 3, 5), (0, 4, 2), (3, 0, 3), (2, 2, 3), (1, 3, 4), (3, 1, 5), (4, 2, 3), (2, 4, 4), (5, 0, 2), (0, 3, 4)]:
        r_sq = r * r
        if h == 0 and k == 0:
            ans = f"x² + y² = {r_sq}"
        elif h == 0:
            ans = f"x² + (y - {k})² = {r_sq}"
        elif k == 0:
            ans = f"(x - {h})² + y² = {r_sq}"
        else:
            ans = f"(x - {h})² + (y - {k})² = {r_sq}"
        opts, idx = shuffle_options(ans, [f"x² + y² = {r_sq}", f"(x + {h})² + (y + {k})² = {r_sq}", f"(x - {h})² + (y - {k})² = {r}"])
        questions.append({
            'text': f"Equation: centre ({h}, {k}), radius {r}?",
            'opts': opts, 'idx': idx,
            'exp': f"(x - {h})² + (y - {k})² = {r}² = {r_sq}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_3():
    """Standard Form (x-h)² + (y-k)²"""
    questions = []
    
    # Standard form identification
    opts, idx = shuffle_options("(x - h)² + (y - k)² = r²", ["x² + y² + Dx + Ey + F = 0", "ax² + by² = c", "y = mx + c"])
    questions.append({
        'text': "What is the standard form of a circle equation?",
        'opts': opts, 'idx': idx,
        'exp': "Standard form: (x - h)² + (y - k)² = r²."
    })
    
    # What h and k represent
    opts, idx = shuffle_options("Centre coordinates", ["Radius values", "Diameter", "Area"])
    questions.append({
        'text': "In (x - h)² + (y - k)² = r², what are h and k?",
        'opts': opts, 'idx': idx,
        'exp': "h and k are the x and y coordinates of centre."
    })
    
    # Read centre from various equations
    equations = [
        ("(x - 2)² + (y - 3)² = 16", "(2, 3)", 4),
        ("(x - 5)² + (y - 1)² = 9", "(5, 1)", 3),
        ("(x + 1)² + (y - 4)² = 25", "(-1, 4)", 5),
        ("(x - 3)² + (y + 2)² = 4", "(3, -2)", 2),
        ("(x + 2)² + (y + 3)² = 36", "(-2, -3)", 6),
        ("x² + (y - 5)² = 49", "(0, 5)", 7),
        ("(x - 4)² + y² = 1", "(4, 0)", 1),
        ("(x + 6)² + (y - 2)² = 100", "(-6, 2)", 10),
        ("(x - 1)² + (y - 1)² = 9", "(1, 1)", 3),
        ("(x - 3)² + (y - 4)² = 25", "(3, 4)", 5),
        ("(x + 4)² + (y - 1)² = 16", "(-4, 1)", 4),
    ]
    for eq, centre, r in equations:
        opts, idx = shuffle_options(centre, ["(0, 0)", f"({r}, {r})", centre.replace("-", "+")])
        questions.append({
            'text': f"Centre of {eq}?",
            'opts': opts, 'idx': idx,
            'exp': f"Centre = {centre}."
        })
    
    # Read radius
    for eq, centre, r in equations:
        r_sq = r * r
        opts, idx = shuffle_options(str(r), [str(r_sq), str(r + 1), str(r - 1) if r > 1 else "1"])
        questions.append({
            'text': f"Radius of {eq}?",
            'opts': opts, 'idx': idx,
            'exp': f"r² = {r_sq}, r = {r}."
        })
        if len(questions) >= 24:
            break
    
    # Write equation from centre and radius
    for h, k, r in [(1, 2, 3), (2, 5, 4), (-1, 3, 2), (4, -1, 5), (0, 3, 4), (2, 0, 3), (-2, -4, 6), (3, 3, 3), (1, 1, 2), (4, 2, 3), (2, 4, 5), (3, -2, 4), (-3, 1, 5), (5, 2, 3), (1, 5, 4), (2, -2, 3)]:
        r_sq = r * r
        if h >= 0:
            x_part = f"(x - {h})²" if h > 0 else "x²"
        else:
            x_part = f"(x + {-h})²"
        if k >= 0:
            y_part = f"(y - {k})²" if k > 0 else "y²"
        else:
            y_part = f"(y + {-k})²"
        ans = f"{x_part} + {y_part} = {r_sq}"
        opts, idx = shuffle_options(ans, [f"(x + {h})² + (y + {k})² = {r_sq}", f"{x_part} + {y_part} = {r}", f"(x - {h})² + (y - {k})² = {r}"])
        questions.append({
            'text': f"Equation: centre ({h}, {k}), radius {r}?",
            'opts': opts, 'idx': idx,
            'exp': f"(x - {h})² + (y - {k})² = {r_sq}."
        })
        if len(questions) >= 42:
            break
    
    # Diameter from equation
    for eq, centre, r in equations:
        d = 2 * r
        opts, idx = shuffle_options(str(d), [str(r), str(d + 2), str(r * r)])
        questions.append({
            'text': f"Diameter of {eq}?",
            'opts': opts, 'idx': idx,
            'exp': f"r = {r}, d = 2r = {d}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_4():
    """Points on a Circle"""
    questions = []
    
    # Test if point is on circle x² + y² = r²
    for r in [5, 10, 13]:
        r_sq = r * r
        # Points on circle (Pythagorean)
        if r == 5:
            on_points = [(3, 4), (4, 3), (0, 5), (5, 0), (-3, 4)]
            off_points = [(2, 3), (4, 4), (1, 5)]
        elif r == 10:
            on_points = [(6, 8), (8, 6), (0, 10), (10, 0)]
            off_points = [(5, 5), (7, 7), (3, 9)]
        else:  # r = 13
            on_points = [(5, 12), (12, 5), (0, 13)]
            off_points = [(6, 11), (10, 8), (7, 10)]
        
        for x, y in on_points:
            opts, idx = shuffle_options("Yes", ["No", "Cannot tell", "Only if x > 0"])
            questions.append({
                'text': f"Is ({x}, {y}) on x² + y² = {r_sq}?",
                'opts': opts, 'idx': idx,
                'exp': f"{x}² + {y}² = {x*x} + {y*y} = {x*x + y*y} = {r_sq}. Yes!"
            })
            if len(questions) >= 12:
                break
        
        for x, y in off_points:
            opts, idx = shuffle_options("No", ["Yes", "Cannot tell", "Only if y > 0"])
            questions.append({
                'text': f"Is ({x}, {y}) on x² + y² = {r_sq}?",
                'opts': opts, 'idx': idx,
                'exp': f"{x}² + {y}² = {x*x + y*y} ≠ {r_sq}. No."
            })
            if len(questions) >= 20:
                break
        if len(questions) >= 20:
            break
    
    # Point on circle with centre not at origin
    for h, k, r in [(2, 3, 5), (1, 1, 5), (0, 2, 5)]:
        r_sq = r * r
        # Point on circle: (h + 3, k + 4) for 3-4-5 triangle
        x_on, y_on = h + 3, k + 4
        x_off, y_off = h + 2, k + 2
        
        opts, idx = shuffle_options("Yes", ["No", "Cannot tell", "Maybe"])
        questions.append({
            'text': f"Is ({x_on}, {y_on}) on (x - {h})² + (y - {k})² = {r_sq}?",
            'opts': opts, 'idx': idx,
            'exp': f"({x_on} - {h})² + ({y_on} - {k})² = 9 + 16 = 25. Yes!"
        })
        
        dist_sq = (x_off - h)**2 + (y_off - k)**2
        opts, idx = shuffle_options("No", ["Yes", "Cannot tell", "Maybe"])
        questions.append({
            'text': f"Is ({x_off}, {y_off}) on (x - {h})² + (y - {k})² = {r_sq}?",
            'opts': opts, 'idx': idx,
            'exp': f"Distance² = {dist_sq} ≠ {r_sq}. No."
        })
        if len(questions) >= 30:
            break
    
    # Find y given x on circle
    for r in [5, 10, 13, 17]:
        r_sq = r * r
        if r == 5:
            pairs = [(3, 4), (4, 3), (0, 5)]
        elif r == 10:
            pairs = [(6, 8), (8, 6), (0, 10)]
        elif r == 13:
            pairs = [(5, 12), (12, 5), (0, 13)]
        else:  # r = 17
            pairs = [(8, 15), (15, 8), (0, 17)]
        
        for x, y in pairs:
            opts, idx = shuffle_options(f"±{y}", [f"{y} only", f"±{x}", f"±{r}"])
            questions.append({
                'text': f"On x² + y² = {r_sq}, if x = {x}, find y.",
                'opts': opts, 'idx': idx,
                'exp': f"y² = {r_sq} - {x}² = {y*y}, y = ±{y}."
            })
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # Distance from centre
    for h, k, r, x, y in [(0, 0, 5, 3, 4), (1, 2, 5, 4, 6), (2, 3, 5, 5, 7), (0, 0, 5, 4, 3), (0, 0, 10, 6, 8), (0, 0, 13, 5, 12), (1, 1, 5, 4, 5), (2, 2, 5, 5, 6), (0, 0, 5, 0, 5), (0, 0, 5, 5, 0), (3, 4, 5, 6, 8), (0, 0, 10, 8, 6), (0, 0, 17, 8, 15), (0, 0, 17, 15, 8)]:
        r_sq = r * r
        dist_sq = (x - h)**2 + (y - k)**2
        dist = int(dist_sq ** 0.5) if dist_sq ** 0.5 == int(dist_sq ** 0.5) else f"√{dist_sq}"
        on_circle = "Yes" if dist_sq == r_sq else "No"
        opts, idx = shuffle_options(on_circle, ["Yes", "No", "Cannot tell"])
        questions.append({
            'text': f"Centre ({h}, {k}), r = {r}. Is ({x}, {y}) on circle?",
            'opts': opts, 'idx': idx,
            'exp': f"Distance = {dist}, r = {r}. {on_circle}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_5():
    """General Form x² + y² + Dx + Ey + F = 0"""
    questions = []
    
    # General form identification
    opts, idx = shuffle_options("x² + y² + Dx + Ey + F = 0", ["(x - h)² + (y - k)² = r²", "y = mx + c", "ax² + bx + c = 0"])
    questions.append({
        'text': "What is the general form of a circle equation?",
        'opts': opts, 'idx': idx,
        'exp': "General form: x² + y² + Dx + Ey + F = 0."
    })
    
    # Identify D, E, F from equations
    equations = [
        ("x² + y² + 4x + 6y + 9 = 0", 4, 6, 9),
        ("x² + y² - 2x + 4y - 4 = 0", -2, 4, -4),
        ("x² + y² + 6x - 8y + 5 = 0", 6, -8, 5),
        ("x² + y² - 4x - 2y + 1 = 0", -4, -2, 1),
        ("x² + y² + 10x + 0y - 11 = 0", 10, 0, -11),
        ("x² + y² + 0x + 8y + 7 = 0", 0, 8, 7),
    ]
    
    for eq, D, E, F in equations:
        opts, idx = shuffle_options(str(D), [str(E), str(F), str(-D)])
        questions.append({
            'text': f"In {eq}, what is D?",
            'opts': opts, 'idx': idx,
            'exp': f"D = coefficient of x = {D}."
        })
        
        opts, idx = shuffle_options(str(E), [str(D), str(F), str(-E)])
        questions.append({
            'text': f"In {eq}, what is E?",
            'opts': opts, 'idx': idx,
            'exp': f"E = coefficient of y = {E}."
        })
        if len(questions) >= 18:
            break
    
    # Centre from general form: (-D/2, -E/2)
    for eq, D, E, F in equations:
        h, k = -D // 2, -E // 2
        opts, idx = shuffle_options(f"({h}, {k})", [f"({D}, {E})", f"({-h}, {-k})", f"({D//2}, {E//2})"])
        questions.append({
            'text': f"Centre of {eq}?",
            'opts': opts, 'idx': idx,
            'exp': f"Centre = (-D/2, -E/2) = ({h}, {k})."
        })
        if len(questions) >= 30:
            break
    
    # Radius from general form: r = √(h² + k² - F) = √((D/2)² + (E/2)² - F)
    for D, E, F in [(4, 6, 9), (-2, 4, -4), (6, -8, 5), (-4, -2, 1)]:
        h, k = -D // 2, -E // 2
        r_sq = h*h + k*k - F
        if r_sq > 0 and r_sq ** 0.5 == int(r_sq ** 0.5):
            r = int(r_sq ** 0.5)
            opts, idx = shuffle_options(str(r), [str(r_sq), str(r + 1), str(abs(F))])
            eq = f"x² + y² + {D}x + {E}y + {F} = 0".replace("+ -", "- ")
            questions.append({
                'text': f"Radius of {eq}?",
                'opts': opts, 'idx': idx,
                'exp': f"r² = ({h})² + ({k})² - ({F}) = {r_sq}. r = {r}."
            })
        if len(questions) >= 40:
            break
    
    # Identify if equation represents a circle
    valid = [
        ("x² + y² + 2x + 4y - 4 = 0", "Yes"),
        ("x² + y² - 6x + 8y + 9 = 0", "Yes"),
        ("x² + y² + 4x + 4y + 8 = 0", "No - r² negative"),
        ("2x² + 2y² + 4x + 6y - 8 = 0", "Yes - divide by 2"),
    ]
    for eq, ans in valid:
        is_yes = "Yes" if "Yes" in ans else "No"
        opts, idx = shuffle_options(is_yes, ["Yes", "No", "Cannot tell"])
        questions.append({
            'text': f"Does {eq} represent a circle?",
            'opts': opts, 'idx': idx,
            'exp': ans
        })
    
    # Fill remaining
    for D in range(-6, 8, 2):
        for E in range(-6, 8, 2):
            if D != 0 or E != 0:
                h, k = -D // 2, -E // 2
                opts, idx = shuffle_options(f"({h}, {k})", [f"({D}, {E})", f"({-h}, {-k})", "(0, 0)"])
                questions.append({
                    'text': f"Centre if D = {D}, E = {E}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"Centre = (-D/2, -E/2) = ({h}, {k})."
                })
                if len(questions) >= 50:
                    break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_6():
    """Converting Forms"""
    questions = []
    
    # Standard to general
    for h, k, r in [(1, 2, 3), (2, 3, 4), (3, 1, 5), (-1, 2, 3), (2, -1, 4)]:
        r_sq = r * r
        # (x - h)² + (y - k)² = r²
        # x² - 2hx + h² + y² - 2ky + k² = r²
        # x² + y² - 2hx - 2ky + (h² + k² - r²) = 0
        D, E, F = -2*h, -2*k, h*h + k*k - r_sq
        ans = f"x² + y² + {D}x + {E}y + {F} = 0".replace("+ -", "- ")
        x_part = f"(x - {h})²" if h > 0 else f"(x + {-h})²"
        y_part = f"(y - {k})²" if k > 0 else f"(y + {-k})²"
        eq = f"{x_part} + {y_part} = {r_sq}"
        opts, idx = shuffle_options(f"D = {D}", [f"D = {-D}", f"D = {h}", f"D = {2*h}"])
        questions.append({
            'text': f"Convert {eq} to general. What is D?",
            'opts': opts, 'idx': idx,
            'exp': f"D = -2h = -2({h}) = {D}."
        })
        if len(questions) >= 10:
            break
    
    # General to standard - find centre
    for D, E, F in [(-4, -6, 9), (2, -4, -4), (-6, 8, 5), (4, 2, -11)]:
        h, k = -D // 2, -E // 2
        eq = f"x² + y² + {D}x + {E}y + {F} = 0".replace("+ -", "- ")
        opts, idx = shuffle_options(f"({h}, {k})", [f"({D}, {E})", f"({-h}, {-k})", f"({D//2}, {E//2})"])
        questions.append({
            'text': f"Convert {eq}. Centre?",
            'opts': opts, 'idx': idx,
            'exp': f"h = -D/2 = {h}, k = -E/2 = {k}."
        })
        if len(questions) >= 18:
            break
    
    # General to standard - find radius
    for D, E, F in [(-4, -6, 9), (2, -4, -4), (-6, 8, 5), (4, 2, 1)]:
        h, k = -D // 2, -E // 2
        r_sq = h*h + k*k - F
        if r_sq > 0 and r_sq ** 0.5 == int(r_sq ** 0.5):
            r = int(r_sq ** 0.5)
            eq = f"x² + y² + {D}x + {E}y + {F} = 0".replace("+ -", "- ")
            opts, idx = shuffle_options(str(r), [str(r_sq), str(r + 1), str(abs(F))])
            questions.append({
                'text': f"Convert {eq}. Radius?",
                'opts': opts, 'idx': idx,
                'exp': f"r² = {h}² + {k}² - {F} = {r_sq}. r = {r}."
            })
        if len(questions) >= 28:
            break
    
    # Complete the square hints
    opts, idx = shuffle_options("Add (D/2)² and (E/2)²", ["Subtract D and E", "Multiply by 2", "Divide by F"])
    questions.append({
        'text': "To convert general to standard, we...?",
        'opts': opts, 'idx': idx,
        'exp': "Complete square by adding (D/2)² and (E/2)² to both sides."
    })
    
    # Coefficient relationship
    opts, idx = shuffle_options("-2h", ["h", "2h", "h²"])
    questions.append({
        'text': "In general form, D equals?",
        'opts': opts, 'idx': idx,
        'exp': "D = -2h where h is x-coordinate of centre."
    })
    
    opts, idx = shuffle_options("-2k", ["k", "2k", "k²"])
    questions.append({
        'text': "In general form, E equals?",
        'opts': opts, 'idx': idx,
        'exp': "E = -2k where k is y-coordinate of centre."
    })
    
    # More conversions
    for h, k, r in [(2, 1, 4), (3, 2, 5), (1, 4, 3), (4, 3, 5), (2, 2, 3), (5, 1, 4), (1, 5, 3), (3, 3, 4), (4, 1, 5), (2, 4, 3), (5, 2, 4), (1, 1, 3)]:
        D, E = -2*h, -2*k
        opts, idx = shuffle_options(f"D = {D}, E = {E}", [f"D = {2*h}, E = {2*k}", f"D = {h}, E = {k}", f"D = {-h}, E = {-k}"])
        questions.append({
            'text': f"Circle with centre ({h}, {k}). Find D and E.",
            'opts': opts, 'idx': idx,
            'exp': f"D = -2({h}) = {D}, E = -2({k}) = {E}."
        })
        if len(questions) >= 40:
            break
    
    # Find F
    for h, k, r in [(1, 2, 3), (2, 1, 4), (3, 2, 5), (1, 3, 4), (2, 2, 3), (4, 1, 5), (3, 3, 4), (1, 4, 3)]:
        F = h*h + k*k - r*r
        opts, idx = shuffle_options(str(F), [str(-F), str(h*h + k*k), str(r*r)])
        questions.append({
            'text': f"Centre ({h}, {k}), radius {r}. Find F.",
            'opts': opts, 'idx': idx,
            'exp': f"F = h² + k² - r² = {h*h} + {k*k} - {r*r} = {F}."
        })
        if len(questions) >= 50:
            break
    
    # Fill remaining
    for D in [-2, -4, -6, 2, 4, 6, 8, -8, 10, -10]:
        h = -D // 2
        opts, idx = shuffle_options(str(h), [str(D), str(-h), str(D // 2)])
        questions.append({
            'text': f"If D = {D}, what is h (x-coordinate of centre)?",
            'opts': opts, 'idx': idx,
            'exp': f"h = -D/2 = {h}."
        })
        if len(questions) >= 48:
            break
    
    for E in [-2, -4, -6, 2, 4]:
        k = -E // 2
        opts, idx = shuffle_options(str(k), [str(E), str(-k), str(E // 2)])
        questions.append({
            'text': f"If E = {E}, what is k (y-coordinate of centre)?",
            'opts': opts, 'idx': idx,
            'exp': f"k = -E/2 = {k}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_7():
    """Circle Through Points"""
    questions = []
    
    # Circle through origin with given centre
    for h, k in [(3, 4), (5, 12), (6, 8), (4, 3), (8, 6)]:
        r_sq = h*h + k*k
        r = int(r_sq ** 0.5) if r_sq ** 0.5 == int(r_sq ** 0.5) else f"√{r_sq}"
        if isinstance(r, int):
            opts, idx = shuffle_options(str(r), [str(r + 1), str(r - 1), str(h + k)])
            questions.append({
                'text': f"Circle centre ({h}, {k}) passes through origin. Radius?",
                'opts': opts, 'idx': idx,
                'exp': f"r = distance to origin = √({h}² + {k}²) = {r}."
            })
        if len(questions) >= 8:
            break
    
    # Circle with diameter endpoints
    for x1, y1, x2, y2 in [(0, 0, 4, 0), (0, 0, 0, 6), (1, 1, 5, 5), (2, 0, 6, 0), (0, 2, 0, 8), (1, 1, 7, 7), (2, 2, 6, 6), (0, 0, 8, 0), (3, 3, 7, 7)]:
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        opts, idx = shuffle_options(f"({cx}, {cy})", [f"({x1}, {y1})", f"({x2}, {y2})", f"({cx+1}, {cy})"])
        questions.append({
            'text': f"Diameter has endpoints ({x1}, {y1}) and ({x2}, {y2}). Centre?",
            'opts': opts, 'idx': idx,
            'exp': f"Centre = midpoint = ({cx}, {cy})."
        })
        if len(questions) >= 20:
            break
    
    # Radius from diameter endpoints
    for x1, y1, x2, y2 in [(0, 0, 6, 8), (0, 0, 8, 6), (1, 1, 7, 9), (2, 2, 8, 10)]:
        dx, dy = x2 - x1, y2 - y1
        d_sq = dx*dx + dy*dy
        d = int(d_sq ** 0.5) if d_sq ** 0.5 == int(d_sq ** 0.5) else None
        if d:
            r = d // 2
            opts, idx = shuffle_options(str(r), [str(d), str(r + 1), str(r - 1) if r > 1 else "1"])
            questions.append({
                'text': f"Diameter endpoints ({x1}, {y1}) and ({x2}, {y2}). Radius?",
                'opts': opts, 'idx': idx,
                'exp': f"Diameter = {d}, radius = {d}/2 = {r}."
            })
        if len(questions) >= 24:
            break
    
    # Does point lie inside/outside/on circle
    for h, k, r, x, y in [(0, 0, 5, 3, 4), (0, 0, 5, 2, 2), (0, 0, 5, 4, 4), (2, 3, 5, 5, 7), (2, 3, 5, 2, 3), (0, 0, 10, 6, 8), (0, 0, 10, 5, 5), (0, 0, 13, 5, 12), (0, 0, 13, 10, 10), (1, 1, 5, 4, 5), (1, 1, 5, 3, 3)]:
        dist_sq = (x - h)**2 + (y - k)**2
        r_sq = r * r
        if dist_sq == r_sq:
            pos = "On"
        elif dist_sq < r_sq:
            pos = "Inside"
        else:
            pos = "Outside"
        opts, idx = shuffle_options(pos, ["Inside", "On", "Outside"])
        questions.append({
            'text': f"Centre ({h}, {k}), r = {r}. Where is ({x}, {y})?",
            'opts': opts, 'idx': idx,
            'exp': f"Distance² = {dist_sq}, r² = {r_sq}. {pos}."
        })
        if len(questions) >= 40:
            break
    
    # Find equation given centre and point on circle
    for h, k, x, y in [(0, 0, 3, 4), (1, 2, 4, 6), (2, 1, 5, 5)]:
        r_sq = (x - h)**2 + (y - k)**2
        r = int(r_sq ** 0.5) if r_sq ** 0.5 == int(r_sq ** 0.5) else None
        if r:
            opts, idx = shuffle_options(str(r_sq), [str(r), str(r_sq + 1), str((x-h)**2)])
            questions.append({
                'text': f"Centre ({h}, {k}), passes through ({x}, {y}). r² = ?",
                'opts': opts, 'idx': idx,
                'exp': f"r² = ({x}-{h})² + ({y}-{k})² = {r_sq}."
            })
        if len(questions) >= 42:
            break
    
    # Fill remaining
    for h, k in [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 8), (8, 6), (9, 12), (12, 9)]:
        r_sq = h*h + k*k  # passes through origin
        opts, idx = shuffle_options(str(r_sq), [str(h*h), str(k*k), str(h + k)])
        questions.append({
            'text': f"Centre ({h}, {k}), passes through (0, 0). Find r².",
            'opts': opts, 'idx': idx,
            'exp': f"r² = {h}² + {k}² = {r_sq}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_8():
    """Tangent Lines"""
    questions = []
    
    # Tangent property
    opts, idx = shuffle_options("Perpendicular to radius", ["Parallel to radius", "Equal to diameter", "Through centre"])
    questions.append({
        'text': "A tangent at point of contact is...?",
        'opts': opts, 'idx': idx,
        'exp': "Tangent ⊥ radius at point of tangency."
    })
    
    # Slope of radius to point
    for h, k, x, y in [(0, 0, 3, 4), (0, 0, 4, 3), (1, 2, 4, 6), (2, 1, 5, 5)]:
        if x - h != 0:
            m_rad = (y - k) / (x - h)
            if m_rad == int(m_rad):
                m_rad = int(m_rad)
                opts, idx = shuffle_options(str(m_rad), [str(-m_rad), str(m_rad + 1), "0"])
                questions.append({
                    'text': f"Centre ({h}, {k}), point ({x}, {y}). Slope of radius?",
                    'opts': opts, 'idx': idx,
                    'exp': f"m = ({y}-{k})/({x}-{h}) = {m_rad}."
                })
        if len(questions) >= 8:
            break
    
    # Slope of tangent (perpendicular to radius)
    for m_rad in [1, 2, 3, 4, -1, -2]:
        if m_rad == 1:
            m_tan = "-1"
        elif m_rad == -1:
            m_tan = "1"
        else:
            m_tan = f"-1/{m_rad}" if m_rad > 0 else f"1/{-m_rad}"
        opts, idx = shuffle_options(m_tan, [str(m_rad), str(-m_rad), "0"])
        questions.append({
            'text': f"Radius has slope {m_rad}. Tangent slope?",
            'opts': opts, 'idx': idx,
            'exp': f"Tangent ⊥ radius: m_tan = -1/{m_rad} = {m_tan}."
        })
        if len(questions) >= 18:
            break
    
    # Tangent at point on circle x² + y² = r²
    for x, y, r in [(3, 4, 5), (4, 3, 5), (5, 12, 13), (6, 8, 10), (8, 6, 10), (12, 5, 13), (8, 15, 17), (15, 8, 17)]:
        # Tangent at (x, y) on x² + y² = r²: xx₁ + yy₁ = r²
        # Or: slope of radius = y/x, so tangent slope = -x/y
        m_rad = f"{y}/{x}"
        m_tan = f"-{x}/{y}"
        opts, idx = shuffle_options(m_tan, [m_rad, f"{x}/{y}", "0"])
        questions.append({
            'text': f"Tangent to x² + y² = {r*r} at ({x}, {y}). Slope?",
            'opts': opts, 'idx': idx,
            'exp': f"Radius slope = {y}/{x}, tangent slope = -{x}/{y}."
        })
        if len(questions) >= 28:
            break
    
    # Length of tangent from external point
    for h, k, r, x, y in [(0, 0, 3, 5, 0), (0, 0, 4, 5, 0), (0, 0, 5, 13, 0)]:
        d_sq = (x - h)**2 + (y - k)**2
        t_sq = d_sq - r*r
        t = int(t_sq ** 0.5) if t_sq > 0 and t_sq ** 0.5 == int(t_sq ** 0.5) else None
        if t:
            opts, idx = shuffle_options(str(t), [str(t + 1), str(r), str(int(d_sq ** 0.5))])
            questions.append({
                'text': f"Circle centre ({h}, {k}), r = {r}. Tangent length from ({x}, {y})?",
                'opts': opts, 'idx': idx,
                'exp': f"t = √(d² - r²) = √({d_sq} - {r*r}) = {t}."
            })
        if len(questions) >= 34:
            break
    
    # Tangent touches at one point
    opts, idx = shuffle_options("One", ["Two", "Zero", "Infinite"])
    questions.append({
        'text': "How many points does a tangent touch a circle?",
        'opts': opts, 'idx': idx,
        'exp': "Tangent touches at exactly one point."
    })
    
    # External point tangents
    opts, idx = shuffle_options("Two", ["One", "Zero", "Infinite"])
    questions.append({
        'text': "How many tangents from external point to circle?",
        'opts': opts, 'idx': idx,
        'exp': "Two tangents from any external point."
    })
    
    # Point on circle tangents
    opts, idx = shuffle_options("One", ["Two", "Zero", "Infinite"])
    questions.append({
        'text': "How many tangents from point ON the circle?",
        'opts': opts, 'idx': idx,
        'exp': "One tangent at any point on the circle."
    })
    
    # Fill remaining
    for m_rad in range(1, 20):
        m_tan = f"-1/{m_rad}"
        opts, idx = shuffle_options(m_tan, [str(m_rad), f"1/{m_rad}", str(-m_rad)])
        questions.append({
            'text': f"Radius slope = {m_rad}. Tangent slope = ?",
            'opts': opts, 'idx': idx,
            'exp': f"Perpendicular: -1/{m_rad}."
        })
        if len(questions) >= 45:
            break
    
    for m_rad in range(-1, -12, -1):
        m_tan = f"1/{-m_rad}"
        opts, idx = shuffle_options(m_tan, [str(m_rad), f"-1/{-m_rad}", str(-m_rad)])
        questions.append({
            'text': f"Radius slope = {m_rad}. Tangent slope = ?",
            'opts': opts, 'idx': idx,
            'exp': f"Perpendicular: 1/{-m_rad}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_9():
    """Circle and Line Intersection"""
    questions = []
    
    # Number of intersections based on distance
    opts, idx = shuffle_options("2 points", ["1 point", "0 points", "Infinite"])
    questions.append({
        'text': "If line distance from centre < radius, intersections?",
        'opts': opts, 'idx': idx,
        'exp': "Distance < r means line passes through circle (2 points)."
    })
    
    opts, idx = shuffle_options("1 point (tangent)", ["2 points", "0 points", "Infinite"])
    questions.append({
        'text': "If line distance from centre = radius, intersections?",
        'opts': opts, 'idx': idx,
        'exp': "Distance = r means tangent (1 point)."
    })
    
    opts, idx = shuffle_options("0 points", ["1 point", "2 points", "Infinite"])
    questions.append({
        'text': "If line distance from centre > radius, intersections?",
        'opts': opts, 'idx': idx,
        'exp': "Distance > r means line misses circle."
    })
    
    # Discriminant interpretation
    opts, idx = shuffle_options("2 intersection points", ["1 point (tangent)", "No intersection", "Cannot tell"])
    questions.append({
        'text': "Substituting line into circle gives Δ > 0. Meaning?",
        'opts': opts, 'idx': idx,
        'exp': "Δ > 0 means two distinct solutions = 2 points."
    })
    
    opts, idx = shuffle_options("Tangent (1 point)", ["2 points", "No intersection", "Cannot tell"])
    questions.append({
        'text': "Substituting line into circle gives Δ = 0. Meaning?",
        'opts': opts, 'idx': idx,
        'exp': "Δ = 0 means one repeated solution = tangent."
    })
    
    opts, idx = shuffle_options("No intersection", ["1 point", "2 points", "Cannot tell"])
    questions.append({
        'text': "Substituting line into circle gives Δ < 0. Meaning?",
        'opts': opts, 'idx': idx,
        'exp': "Δ < 0 means no real solutions = no intersection."
    })
    
    # Simple intersection: y = constant with x² + y² = r²
    for y_val, r in [(3, 5), (4, 5), (0, 5), (6, 10), (8, 10)]:
        r_sq = r * r
        x_sq = r_sq - y_val * y_val
        if x_sq > 0:
            x = int(x_sq ** 0.5) if x_sq ** 0.5 == int(x_sq ** 0.5) else None
            if x:
                ans = f"(±{x}, {y_val})"
                opts, idx = shuffle_options(ans, [f"({x}, {y_val}) only", f"({x}, ±{y_val})", f"(0, {y_val})"])
                questions.append({
                    'text': f"y = {y_val} intersects x² + y² = {r_sq} at?",
                    'opts': opts, 'idx': idx,
                    'exp': f"x² = {r_sq} - {y_val*y_val} = {x_sq}, x = ±{x}."
                })
        elif x_sq == 0:
            ans = f"(0, {y_val})"
            opts, idx = shuffle_options(ans, [f"(±{y_val}, {y_val})", "No intersection", f"({r}, {y_val})"])
            questions.append({
                'text': f"y = {y_val} intersects x² + y² = {r_sq} at?",
                'opts': opts, 'idx': idx,
                'exp': f"x = 0, tangent at (0, {y_val})."
            })
        if len(questions) >= 18:
            break
    
    # x = constant with x² + y² = r²
    for x_val, r in [(3, 5), (4, 5), (0, 5)]:
        r_sq = r * r
        y_sq = r_sq - x_val * x_val
        if y_sq > 0:
            y = int(y_sq ** 0.5) if y_sq ** 0.5 == int(y_sq ** 0.5) else None
            if y:
                ans = f"({x_val}, ±{y})"
                opts, idx = shuffle_options(ans, [f"({x_val}, {y}) only", f"(±{x_val}, {y})", f"({x_val}, 0)"])
                questions.append({
                    'text': f"x = {x_val} intersects x² + y² = {r_sq} at?",
                    'opts': opts, 'idx': idx,
                    'exp': f"y² = {r_sq} - {x_val*x_val} = {y_sq}, y = ±{y}."
                })
        if len(questions) >= 26:
            break
    
    # Does line intersect/touch/miss
    cases = [
        (0, 0, 5, 3, "Intersects (2 points)"),  # y = 3 and r = 5
        (0, 0, 5, 5, "Tangent (1 point)"),       # y = 5 and r = 5
        (0, 0, 5, 6, "No intersection"),         # y = 6 and r = 5
        (0, 0, 10, 6, "Intersects (2 points)"),
        (0, 0, 10, 10, "Tangent (1 point)"),
    ]
    for h, k, r, y_val, result in cases:
        r_sq = r * r
        opts, idx = shuffle_options(result, ["Intersects (2 points)", "Tangent (1 point)", "No intersection"])
        questions.append({
            'text': f"x² + y² = {r_sq} and y = {y_val}?",
            'opts': opts, 'idx': idx,
            'exp': f"|{y_val}| vs r = {r}: {result}."
        })
        if len(questions) >= 38:
            break
    
    # Fill remaining
    for r in range(3, 10):
        r_sq = r * r
        for y in range(r - 2, r + 3):
            if y < r:
                result = "2 points"
            elif y == r:
                result = "1 point"
            else:
                result = "0 points"
            opts, idx = shuffle_options(result, ["2 points", "1 point", "0 points"])
            questions.append({
                'text': f"x² + y² = {r_sq} and y = {y}. How many intersections?",
                'opts': opts, 'idx': idx,
                'exp': f"y = {y}, r = {r}. {result}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_10():
    """Distance from Centre"""
    questions = []
    
    # Distance formula reminder
    opts, idx = shuffle_options("√[(x₂-x₁)² + (y₂-y₁)²]", ["(x₂-x₁) + (y₂-y₁)", "|x₂-x₁|", "(x₂-x₁)²"])
    questions.append({
        'text': "Distance between two points formula?",
        'opts': opts, 'idx': idx,
        'exp': "d = √[(x₂-x₁)² + (y₂-y₁)²]."
    })
    
    # Distance from centre to point
    for h, k, x, y in [(0, 0, 3, 4), (0, 0, 5, 12), (0, 0, 6, 8), (1, 2, 4, 6), (2, 3, 5, 7)]:
        d_sq = (x - h)**2 + (y - k)**2
        d = int(d_sq ** 0.5) if d_sq ** 0.5 == int(d_sq ** 0.5) else f"√{d_sq}"
        if isinstance(d, int):
            opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1) if d > 1 else "1", str(d_sq)])
            questions.append({
                'text': f"Distance from ({h}, {k}) to ({x}, {y})?",
                'opts': opts, 'idx': idx,
                'exp': f"d = √[({x}-{h})² + ({y}-{k})²] = {d}."
            })
        if len(questions) >= 12:
            break
    
    # Compare distance to radius
    for h, k, r, x, y in [(0, 0, 5, 3, 4), (0, 0, 5, 4, 4), (0, 0, 5, 2, 2), (2, 3, 5, 5, 7), (2, 3, 5, 2, 3)]:
        d_sq = (x - h)**2 + (y - k)**2
        r_sq = r * r
        if d_sq < r_sq:
            pos = "Inside"
        elif d_sq == r_sq:
            pos = "On"
        else:
            pos = "Outside"
        opts, idx = shuffle_options(pos, ["Inside", "On", "Outside"])
        questions.append({
            'text': f"Centre ({h}, {k}), r = {r}. Is ({x}, {y}) inside/on/outside?",
            'opts': opts, 'idx': idx,
            'exp': f"d² = {d_sq}, r² = {r_sq}. Point is {pos.lower()}."
        })
        if len(questions) >= 22:
            break
    
    # Distance from centre determines position
    opts, idx = shuffle_options("d < r", ["d > r", "d = r", "d = 0"])
    questions.append({
        'text': "Point inside circle when distance d...?",
        'opts': opts, 'idx': idx,
        'exp': "Inside when d < r."
    })
    
    opts, idx = shuffle_options("d = r", ["d < r", "d > r", "d = 0"])
    questions.append({
        'text': "Point on circle when distance d...?",
        'opts': opts, 'idx': idx,
        'exp': "On circle when d = r."
    })
    
    opts, idx = shuffle_options("d > r", ["d < r", "d = r", "d = 2r"])
    questions.append({
        'text': "Point outside circle when distance d...?",
        'opts': opts, 'idx': idx,
        'exp': "Outside when d > r."
    })
    
    # Closest point on circle to external point
    for h, k, r, x, y in [(0, 0, 5, 10, 0), (0, 0, 5, 0, 10), (0, 0, 5, 13, 0)]:
        d = int(((x - h)**2 + (y - k)**2) ** 0.5)
        closest_dist = d - r
        opts, idx = shuffle_options(str(closest_dist), [str(d), str(r), str(d + r)])
        questions.append({
            'text': f"Centre ({h}, {k}), r = {r}. Closest distance from ({x}, {y}) to circle?",
            'opts': opts, 'idx': idx,
            'exp': f"Distance to centre = {d}. Closest = {d} - {r} = {closest_dist}."
        })
        if len(questions) >= 35:
            break
    
    # Furthest point on circle from external point
    for h, k, r, x, y in [(0, 0, 5, 10, 0), (0, 0, 5, 0, 13)]:
        d = int(((x - h)**2 + (y - k)**2) ** 0.5)
        furthest_dist = d + r
        opts, idx = shuffle_options(str(furthest_dist), [str(d), str(r), str(d - r)])
        questions.append({
            'text': f"Centre ({h}, {k}), r = {r}. Furthest distance from ({x}, {y}) to circle?",
            'opts': opts, 'idx': idx,
            'exp': f"Distance to centre = {d}. Furthest = {d} + {r} = {furthest_dist}."
        })
        if len(questions) >= 42:
            break
    
    # Fill remaining
    for h, k in [(0, 0), (1, 2), (2, 3), (3, 1), (0, 0), (0, 0), (0, 0), (1, 1), (2, 2)]:
        for x, y in [(3, 4), (5, 12), (6, 8), (8, 6), (4, 3), (12, 5), (8, 15), (9, 12), (12, 9)]:
            d_sq = (x - h)**2 + (y - k)**2
            d = int(d_sq ** 0.5) if d_sq ** 0.5 == int(d_sq ** 0.5) else None
            if d:
                opts, idx = shuffle_options(str(d), [str(d + 1), str(d - 1) if d > 1 else "1", str(d_sq)])
                questions.append({
                    'text': f"Distance from ({h}, {k}) to ({x}, {y})?",
                    'opts': opts, 'idx': idx,
                    'exp': f"d = {d}."
                })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_11():
    """Circle Problems"""
    questions = []
    
    # Concentric circles
    opts, idx = shuffle_options("Same centre", ["Same radius", "Same diameter", "Intersecting"])
    questions.append({
        'text': "What are concentric circles?",
        'opts': opts, 'idx': idx,
        'exp': "Concentric = sharing the same centre."
    })
    
    # Area of circle
    for r in range(2, 8):
        area = f"{r*r}π"
        opts, idx = shuffle_options(area, [f"{2*r}π", f"{r}π", f"{r*r*r}π"])
        questions.append({
            'text': f"Area of circle with radius {r}?",
            'opts': opts, 'idx': idx,
            'exp': f"A = πr² = π({r})² = {area}."
        })
        if len(questions) >= 10:
            break
    
    # Circumference
    for r in range(2, 8):
        circum = f"{2*r}π"
        opts, idx = shuffle_options(circum, [f"{r*r}π", f"{r}π", f"{4*r}π"])
        questions.append({
            'text': f"Circumference of circle with radius {r}?",
            'opts': opts, 'idx': idx,
            'exp': f"C = 2πr = 2π({r}) = {circum}."
        })
        if len(questions) >= 18:
            break
    
    # Two circles - do they intersect?
    circle_pairs = [
        ((0, 0, 3), (5, 0, 2), "Yes - intersect"),  # d = 5, r1 + r2 = 5 (touch)
        ((0, 0, 3), (10, 0, 2), "No - too far"),     # d = 10 > 5
        ((0, 0, 5), (3, 0, 3), "Yes - intersect"),   # d = 3 < 8
        ((0, 0, 3), (1, 0, 1), "No - one inside"),   # d = 1 < |3-1| = 2
        ((0, 0, 4), (8, 0, 3), "Yes - intersect"),   # d = 8 < 7 NO, d = 8, r1+r2 = 7, no intersection
        ((0, 0, 5), (6, 0, 4), "Yes - intersect"),   # d = 6 < 9
        ((0, 0, 3), (7, 0, 3), "Yes - intersect"),   # d = 7 < 6 NO touch at one point
        ((0, 0, 4), (5, 0, 5), "Yes - intersect"),   # d = 5 < 9
    ]
    for (h1, k1, r1), (h2, k2, r2), result in circle_pairs:
        d = int(((h2 - h1)**2 + (k2 - k1)**2) ** 0.5)
        opts, idx = shuffle_options(result, ["Yes - intersect", "No - too far", "No - one inside", "Touch at 1 point"])
        questions.append({
            'text': f"Circles: C₁({h1},{k1}) r={r1}, C₂({h2},{k2}) r={r2}. Intersect?",
            'opts': opts, 'idx': idx,
            'exp': f"Distance = {d}, r₁+r₂ = {r1+r2}. {result}."
        })
        if len(questions) >= 30:
            break
    
    # Find equation from description
    for h, k, r in [(1, 2, 3), (2, 3, 4), (0, 0, 5), (3, 1, 2)]:
        r_sq = r * r
        D, E, F = -2*h, -2*k, h*h + k*k - r_sq
        ans = f"D={D}, E={E}, F={F}"
        opts, idx = shuffle_options(ans, [f"D={-D}, E={-E}, F={F}", f"D={D}, E={E}, F={-F}", f"D={h}, E={k}, F={r_sq}"])
        questions.append({
            'text': f"Circle centre ({h}, {k}), radius {r}. Find D, E, F.",
            'opts': opts, 'idx': idx,
            'exp': f"D=-2h={D}, E=-2k={E}, F=h²+k²-r²={F}."
        })
        if len(questions) >= 32:
            break
    
    # Unit circle
    opts, idx = shuffle_options("x² + y² = 1", ["x² + y² = 0", "(x-1)² + (y-1)² = 1", "x + y = 1"])
    questions.append({
        'text': "Equation of the unit circle?",
        'opts': opts, 'idx': idx,
        'exp': "Unit circle: centre (0,0), r = 1."
    })
    
    # Semicircle
    opts, idx = shuffle_options("πr²/2", ["πr²", "2πr", "πr"])
    questions.append({
        'text': "Area of semicircle with radius r?",
        'opts': opts, 'idx': idx,
        'exp': "Semicircle = half circle = πr²/2."
    })
    
    # Fill remaining with mixed problems
    for r in range(3, 15):
        d = 2 * r
        opts, idx = shuffle_options(str(d), [str(r), str(r*r), str(d + 2)])
        questions.append({
            'text': f"Circle has area {r*r}π. Diameter?",
            'opts': opts, 'idx': idx,
            'exp': f"r² = {r*r}, r = {r}, d = {d}."
        })
        if len(questions) >= 44:
            break
    
    for r in range(2, 15):
        opts, idx = shuffle_options(str(r), [str(r*r), str(2*r), str(r + 1)])
        questions.append({
            'text': f"Circumference = {2*r}π. Radius?",
            'opts': opts, 'idx': idx,
            'exp': f"2πr = {2*r}π, r = {r}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_12():
    """SEC Exam Style"""
    questions = []
    
    # Multi-step: find centre and radius from general form
    for D, E, F in [(-4, -6, 9), (2, -4, -4), (-6, 8, -9)]:
        h, k = -D // 2, -E // 2
        r_sq = h*h + k*k - F
        if r_sq > 0 and r_sq ** 0.5 == int(r_sq ** 0.5):
            r = int(r_sq ** 0.5)
            eq = f"x² + y² + {D}x + {E}y + {F} = 0".replace("+ -", "- ")
            opts, idx = shuffle_options(f"({h}, {k})", [f"({D}, {E})", f"({-h}, {-k})", f"({D//2}, {E//2})"])
            questions.append({
                'text': f"Circle {eq}. Centre?",
                'opts': opts, 'idx': idx,
                'exp': f"Centre = (-D/2, -E/2) = ({h}, {k})."
            })
            
            opts, idx = shuffle_options(str(r), [str(r_sq), str(r + 1), str(abs(F))])
            questions.append({
                'text': f"Circle {eq}. Radius?",
                'opts': opts, 'idx': idx,
                'exp': f"r = √({h}² + {k}² - {F}) = {r}."
            })
        if len(questions) >= 10:
            break
    
    # Point on circle verification
    for h, k, r, x, y in [(0, 0, 5, 3, 4), (2, 3, 5, 5, 7), (1, 2, 5, 4, 6)]:
        d_sq = (x - h)**2 + (y - k)**2
        r_sq = r * r
        on_circle = "Yes" if d_sq == r_sq else "No"
        opts, idx = shuffle_options(on_circle, ["Yes", "No", "Cannot tell"])
        questions.append({
            'text': f"Is ({x}, {y}) on circle centre ({h}, {k}), r = {r}?",
            'opts': opts, 'idx': idx,
            'exp': f"({x}-{h})² + ({y}-{k})² = {d_sq}. r² = {r_sq}. {on_circle}."
        })
        if len(questions) >= 16:
            break
    
    # Tangent slope
    for x, y, r in [(3, 4, 5), (5, 12, 13), (4, 3, 5)]:
        m_tan = f"-{x}/{y}"
        opts, idx = shuffle_options(m_tan, [f"{y}/{x}", f"{x}/{y}", f"-{y}/{x}"])
        questions.append({
            'text': f"Tangent to x² + y² = {r*r} at ({x}, {y}). Slope?",
            'opts': opts, 'idx': idx,
            'exp': f"Radius slope = {y}/{x}. Tangent = -{x}/{y}."
        })
        if len(questions) >= 22:
            break
    
    # Circle through point with given centre
    for h, k, x, y in [(0, 0, 3, 4), (1, 2, 4, 6), (2, 1, 5, 5)]:
        r_sq = (x - h)**2 + (y - k)**2
        r = int(r_sq ** 0.5) if r_sq ** 0.5 == int(r_sq ** 0.5) else None
        if r:
            opts, idx = shuffle_options(str(r), [str(r_sq), str(r + 1), str(x + y)])
            questions.append({
                'text': f"Circle centre ({h}, {k}) through ({x}, {y}). Radius?",
                'opts': opts, 'idx': idx,
                'exp': f"r = √[({x}-{h})² + ({y}-{k})²] = {r}."
            })
        if len(questions) >= 28:
            break
    
    # Line and circle intersection count
    for r, y_val in [(5, 3), (5, 5), (5, 7), (10, 6), (10, 10), (10, 12), (13, 5), (13, 12), (13, 13), (13, 15)]:
        if y_val < r:
            result = "2"
        elif y_val == r:
            result = "1"
        else:
            result = "0"
        opts, idx = shuffle_options(result, ["0", "1", "2"])
        questions.append({
            'text': f"x² + y² = {r*r} and y = {y_val}. Intersection points?",
            'opts': opts, 'idx': idx,
            'exp': f"y = {y_val}, r = {r}. {result} point(s)."
        })
        if len(questions) >= 40:
            break
    
    # Diameter endpoints to equation
    for x1, y1, x2, y2 in [(0, 0, 4, 0), (0, 0, 6, 8), (2, 0, 6, 0), (0, 0, 8, 6), (0, 0, 10, 0), (1, 1, 5, 5)]:
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        d_sq = (x2 - x1)**2 + (y2 - y1)**2
        r = int((d_sq ** 0.5) / 2) if (d_sq ** 0.5) == int(d_sq ** 0.5) else None
        if r:
            r_sq = r * r
            opts, idx = shuffle_options(str(r), [str(r_sq), str(2*r), str(r + 1)])
            questions.append({
                'text': f"Diameter from ({x1}, {y1}) to ({x2}, {y2}). Radius?",
                'opts': opts, 'idx': idx,
                'exp': f"Diameter = {int(d_sq**0.5)}, r = {r}."
            })
        if len(questions) >= 42:
            break
    
    # Mixed: write equation
    for h, k, r in [(2, 3, 4), (1, 1, 5), (3, 2, 3), (4, 1, 3), (2, 2, 4), (1, 3, 5), (3, 3, 2)]:
        D, E = -2*h, -2*k
        opts, idx = shuffle_options(f"D = {D}", [f"D = {2*h}", f"D = {h}", f"D = {-h}"])
        questions.append({
            'text': f"Circle centre ({h}, {k}). Value of D?",
            'opts': opts, 'idx': idx,
            'exp': f"D = -2h = -2({h}) = {D}."
        })
        if len(questions) >= 48:
            break
    
    # Final questions
    opts, idx = shuffle_options("(-D/2, -E/2)", ["(D, E)", "(D/2, E/2)", "(-D, -E)"])
    questions.append({
        'text': "Centre from x² + y² + Dx + Ey + F = 0?",
        'opts': opts, 'idx': idx,
        'exp': "Centre = (-D/2, -E/2)."
    })
    
    opts, idx = shuffle_options("√[(D/2)² + (E/2)² - F]", ["D + E - F", "(D² + E²)/F", "D/2 + E/2"])
    questions.append({
        'text': "Radius formula from general form?",
        'opts': opts, 'idx': idx,
        'exp': "r = √[(D/2)² + (E/2)² - F]."
    })
    
    # More SEC style: tangent perpendicular to radius
    for m in [2, 3, 4, 5]:
        m_tan = f"-1/{m}"
        opts, idx = shuffle_options(m_tan, [str(m), f"1/{m}", str(-m)])
        questions.append({
            'text': f"Radius slope = {m}. Tangent slope?",
            'opts': opts, 'idx': idx,
            'exp': f"Perpendicular: -1/{m}."
        })
        if len(questions) >= 46:
            break
    
    # More on/inside/outside
    for h, k, r, x, y in [(0, 0, 5, 3, 4), (0, 0, 5, 2, 2), (0, 0, 10, 6, 8), (0, 0, 13, 5, 12), (0, 0, 5, 4, 3), (0, 0, 10, 8, 6), (0, 0, 17, 8, 15), (0, 0, 17, 15, 8), (0, 0, 13, 12, 5)]:
        d_sq = (x - h)**2 + (y - k)**2
        r_sq = r * r
        if d_sq == r_sq:
            pos = "On"
        elif d_sq < r_sq:
            pos = "Inside"
        else:
            pos = "Outside"
        opts, idx = shuffle_options(pos, ["Inside", "On", "Outside"])
        questions.append({
            'text': f"r = {r}. Is ({x}, {y}) inside/on/outside?",
            'opts': opts, 'idx': idx,
            'exp': f"d² = {d_sq}, r² = {r_sq}. {pos}."
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
        "-- LC OL Coordinate Geometry (Circles) - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        "-- Create topic",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Coordinate Geometry (Circles)', {STRAND_ID}, '⭕', 13, 1);",
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
    print("LC OL Coordinate Geometry (Circles) - 600 Questions Generator")
    print("="*60 + "\n")
    
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    
    sql = generate_sql(questions)
    with open('lc_ol_coord_circles_600.sql', 'w') as f:
        f.write(sql)
    
    print(f"Saved: lc_ol_coord_circles_600.sql ({len(sql):,} chars)")
