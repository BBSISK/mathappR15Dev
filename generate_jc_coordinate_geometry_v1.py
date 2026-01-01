#!/usr/bin/env python3
"""
AgentMath - Coordinate Geometry Generator v1
Junior Cycle Mathematics - SEC Aligned

12 Levels:
1. Plotting & Reading Points (Foundation)
2. Horizontal & Vertical Distance (Foundation)
3. Distance Formula - Diagonal (Foundation)
4. Midpoint Formula (Ordinary)
5. Slope/Gradient - Concept (Ordinary)
6. Slope/Gradient - Calculations (Ordinary)
7. Equation of Line y = mx + c (Higher)
8. Finding Slope and Y-Intercept (Higher)
9. Parallel & Perpendicular Lines (Higher)
10. Equation from Two Points (Mastery)
11. Equation from Point and Slope (Mastery)
12. Problem Solving & Applications (Mastery)

SEC References:
- 2022-2025 OL/HL: Coordinate geometry questions
- Slope calculations, equation of line, midpoint, distance
"""

import random
import math
from fractions import Fraction

TOPIC = "coordinate_geometry"
MODE = "jc_exam"
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12

# Visual SVG generators
def grid_svg(points=None, lines=None, width=200, height=200):
    """Generate coordinate grid with optional points and lines"""
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="{width}" height="{height}" fill="#f8fafc"/>
    '''
    # Grid lines
    cx, cy = width//2, height//2
    scale = 18
    
    # Draw grid
    for i in range(-5, 6):
        x = cx + i * scale
        y = cy - i * scale
        # Vertical lines
        svg += f'<line x1="{x}" y1="10" x2="{x}" y2="{height-10}" stroke="#e2e8f0" stroke-width="1"/>'
        # Horizontal lines
        svg += f'<line x1="10" y1="{y}" x2="{width-10}" y2="{y}" stroke="#e2e8f0" stroke-width="1"/>'
    
    # Axes
    svg += f'<line x1="10" y1="{cy}" x2="{width-10}" y2="{cy}" stroke="#1e293b" stroke-width="2"/>'
    svg += f'<line x1="{cx}" y1="10" x2="{cx}" y2="{height-10}" stroke="#1e293b" stroke-width="2"/>'
    
    # Axis labels
    svg += f'<text x="{width-15}" y="{cy-5}" font-size="12" fill="#1e293b">x</text>'
    svg += f'<text x="{cx+5}" y="20" font-size="12" fill="#1e293b">y</text>'
    
    # Origin label
    svg += f'<text x="{cx-12}" y="{cy+12}" font-size="10" fill="#64748b">O</text>'
    
    # Draw lines if provided
    if lines:
        for line in lines:
            x1, y1, x2, y2, color = line
            px1, py1 = cx + x1 * scale, cy - y1 * scale
            px2, py2 = cx + x2 * scale, cy - y2 * scale
            svg += f'<line x1="{px1}" y1="{py1}" x2="{px2}" y2="{py2}" stroke="{color}" stroke-width="2"/>'
    
    # Draw points if provided
    if points:
        colors = ['#ef4444', '#3b82f6', '#22c55e', '#f59e0b']
        for i, (x, y, label) in enumerate(points):
            px, py = cx + x * scale, cy - y * scale
            color = colors[i % len(colors)]
            svg += f'<circle cx="{px}" cy="{py}" r="5" fill="{color}"/>'
            svg += f'<text x="{px+8}" y="{py-8}" font-size="11" fill="{color}" font-weight="bold">{label}</text>'
    
    svg += '</svg>'
    return svg

def line_graph_svg(m, c, width=200, height=200):
    """Generate graph of y = mx + c"""
    svg = f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="{width}" height="{height}" fill="#f8fafc"/>
    '''
    cx, cy = width//2, height//2
    scale = 18
    
    # Grid
    for i in range(-5, 6):
        x = cx + i * scale
        y = cy - i * scale
        svg += f'<line x1="{x}" y1="10" x2="{x}" y2="{height-10}" stroke="#e2e8f0" stroke-width="1"/>'
        svg += f'<line x1="10" y1="{y}" x2="{width-10}" y2="{y}" stroke="#e2e8f0" stroke-width="1"/>'
    
    # Axes
    svg += f'<line x1="10" y1="{cy}" x2="{width-10}" y2="{cy}" stroke="#1e293b" stroke-width="2"/>'
    svg += f'<line x1="{cx}" y1="10" x2="{cx}" y2="{height-10}" stroke="#1e293b" stroke-width="2"/>'
    
    # Draw line y = mx + c
    # Find points at x = -5 and x = 5
    x1, x2 = -5, 5
    y1, y2 = m * x1 + c, m * x2 + c
    
    # Clip to visible area
    px1, py1 = cx + x1 * scale, cy - y1 * scale
    px2, py2 = cx + x2 * scale, cy - y2 * scale
    
    svg += f'<line x1="{px1}" y1="{py1}" x2="{px2}" y2="{py2}" stroke="#3b82f6" stroke-width="2.5"/>'
    
    # Mark y-intercept
    py_int = cy - c * scale
    svg += f'<circle cx="{cx}" cy="{py_int}" r="4" fill="#ef4444"/>'
    
    svg += '</svg>'
    return svg

def slope_visual_svg(rise, run):
    """Visual showing rise and run for slope"""
    svg = '''<svg viewBox="0 0 180 140" xmlns="http://www.w3.org/2000/svg">
    <rect width="180" height="140" fill="#f0f9ff"/>
    '''
    # Starting point
    x1, y1 = 30, 100
    # Scale
    scale = 15
    x2 = x1 + abs(run) * scale
    y2 = y1 - rise * scale
    
    # Draw horizontal (run)
    svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y1}" stroke="#22c55e" stroke-width="3"/>'
    # Draw vertical (rise)
    svg += f'<line x1="{x2}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ef4444" stroke-width="3"/>'
    # Draw slope line
    svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#3b82f6" stroke-width="2" stroke-dasharray="5,3"/>'
    
    # Points
    svg += f'<circle cx="{x1}" cy="{y1}" r="5" fill="#1e293b"/>'
    svg += f'<circle cx="{x2}" cy="{y2}" r="5" fill="#1e293b"/>'
    
    # Labels
    svg += f'<text x="{(x1+x2)//2}" y="{y1+20}" font-size="12" fill="#22c55e" text-anchor="middle">Run = {run}</text>'
    svg += f'<text x="{x2+10}" y="{(y1+y2)//2}" font-size="12" fill="#ef4444">Rise = {rise}</text>'
    
    svg += '</svg>'
    return svg


def make_options(correct, wrong_set):
    """Create 4 unique options with correct answer included"""
    wrong_list = [w for w in wrong_set if w != correct]
    random.shuffle(wrong_list)
    
    options = [correct] + wrong_list[:3]
    while len(options) < 4:
        # Generate additional wrong answers
        if isinstance(correct, str) and '/' in correct:
            # Fraction
            parts = correct.split('/')
            num = int(parts[0]) + random.choice([-2, -1, 1, 2])
            wrong = f"{num}/{parts[1]}"
        elif isinstance(correct, (int, float)):
            wrong = correct + random.choice([-3, -2, -1, 1, 2, 3])
            wrong = str(wrong)
        else:
            wrong = str(random.randint(-10, 10))
        if wrong not in options and wrong != correct:
            options.append(wrong)
    
    random.shuffle(options)
    correct_idx = options.index(correct)
    return options, correct_idx


# Level 1: Plotting & Reading Points
def gen_level_1(n=50):
    """Foundation: Identify coordinates of plotted points"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
            
        qtype = random.choice(['read', 'quadrant', 'identify'])
        
        if qtype == 'read':
            x = random.randint(-5, 5)
            y = random.randint(-5, 5)
            txt = f"Point P is shown on the grid. What are the coordinates of P?"
            ans = f"({x}, {y})"
            wrongs = {f"({y}, {x})", f"({-x}, {y})", f"({x}, {-y})", f"({x+1}, {y})", f"({x}, {y+1})"}
            vis = grid_svg(points=[(x, y, 'P')])
            exp = f"Read across to x = {x}, then up/down to y = {y}. P = ({x}, {y})"
            
        elif qtype == 'quadrant':
            x = random.choice([-4, -3, -2, 2, 3, 4])
            y = random.choice([-4, -3, -2, 2, 3, 4])
            if x > 0 and y > 0:
                ans = "Quadrant 1"
            elif x < 0 and y > 0:
                ans = "Quadrant 2"
            elif x < 0 and y < 0:
                ans = "Quadrant 3"
            else:
                ans = "Quadrant 4"
            txt = f"In which quadrant is the point ({x}, {y})?"
            wrongs = {"Quadrant 1", "Quadrant 2", "Quadrant 3", "Quadrant 4"}
            vis = grid_svg(points=[(x, y, 'P')])
            exp = f"({x}, {y}): x is {'positive' if x > 0 else 'negative'}, y is {'positive' if y > 0 else 'negative'} → {ans}"
            
        else:  # identify
            x = random.randint(-4, 4)
            y = random.randint(-4, 4)
            txt = f"Which point has coordinates ({x}, {y})?"
            # Create 4 different points
            points = [(x, y, 'A')]
            used_coords = {(x, y)}
            labels = ['B', 'C', 'D']
            for label in labels:
                while True:
                    px, py = random.randint(-4, 4), random.randint(-4, 4)
                    if (px, py) not in used_coords:
                        used_coords.add((px, py))
                        points.append((px, py, label))
                        break
            random.shuffle(points)
            ans = "A"
            wrongs = {"B", "C", "D"}
            vis = grid_svg(points=points)
            exp = f"Point A is at ({x}, {y})"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 2: Horizontal & Vertical Distance
def gen_level_2(n=50):
    """Foundation: Distance along axes (no formula needed)"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
            
        qtype = random.choice(['horizontal', 'vertical', 'horizontal', 'vertical'])
        
        if qtype == 'horizontal':
            y = random.randint(-3, 3)
            x1 = random.randint(-4, 0)
            x2 = random.randint(1, 4)
            dist = abs(x2 - x1)
            txt = f"Find the distance between A({x1}, {y}) and B({x2}, {y})."
            points = [(x1, y, 'A'), (x2, y, 'B')]
            exp = f"Same y-coordinate, so horizontal distance = |{x2} - {x1}| = {dist}"
        else:
            x = random.randint(-3, 3)
            y1 = random.randint(-4, 0)
            y2 = random.randint(1, 4)
            dist = abs(y2 - y1)
            txt = f"Find the distance between A({x}, {y1}) and B({x}, {y2})."
            points = [(x, y1, 'A'), (x, y2, 'B')]
            exp = f"Same x-coordinate, so vertical distance = |{y2} - {y1}| = {dist}"
        
        ans = str(dist)
        key = txt
        if key in used:
            continue
        used.add(key)
        
        wrongs = {str(dist + 1), str(dist - 1) if dist > 1 else str(dist + 2), str(dist + 2), str(abs(dist - 2))}
        opts, idx = make_options(ans, wrongs)
        
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': grid_svg(points=points)
        })
    
    return qs


# Level 3: Distance Formula - Diagonal
def gen_level_3(n=50):
    """Foundation: Distance formula for diagonal distances"""
    qs = []
    used = set()
    
    # Pre-generate nice Pythagorean triples for clean answers
    nice_pairs = [
        ((0, 0), (3, 4), 5), ((0, 0), (4, 3), 5), ((1, 1), (4, 5), 5),
        ((0, 0), (5, 12), 13), ((0, 0), (6, 8), 10), ((1, 2), (4, 6), 5),
        ((-1, -1), (2, 3), 5), ((0, 0), (8, 6), 10), ((2, 1), (5, 5), 5),
        ((0, 0), (1, 1), "√2"), ((0, 0), (2, 2), "2√2"), ((0, 0), (3, 3), "3√2"),
        ((1, 1), (3, 3), "2√2"), ((0, 0), (1, 2), "√5"), ((0, 0), (2, 1), "√5"),
        ((0, 0), (2, 4), "2√5"), ((1, 0), (3, 2), "2√2"), ((0, 1), (2, 3), "2√2"),
    ]
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        p1, p2, dist = random.choice(nice_pairs)
        x1, y1 = p1
        x2, y2 = p2
        
        # Sometimes offset both points
        if random.random() < 0.5:
            offset_x = random.randint(-2, 2)
            offset_y = random.randint(-2, 2)
            x1, y1 = x1 + offset_x, y1 + offset_y
            x2, y2 = x2 + offset_x, y2 + offset_y
        
        txt = f"Find the distance between A({x1}, {y1}) and B({x2}, {y2})."
        key = txt
        if key in used:
            continue
        used.add(key)
        
        dx, dy = x2 - x1, y2 - y1
        ans = str(dist)
        
        if isinstance(dist, int):
            wrongs = {str(dist + 1), str(dist - 1) if dist > 1 else str(dist + 2), 
                     str(abs(dx) + abs(dy)), str(dx * dy) if dx * dy > 0 else "1"}
        else:
            base = dist.replace("√", "")
            wrongs = {"√" + str(int(base[0]) + 1) + base[1:] if base[0].isdigit() else "2" + dist,
                     str(abs(dx) + abs(dy)), "√" + str(dx**2 + dy**2), dist.replace("2", "3")}
        
        exp = f"d = √[({x2}-{x1})² + ({y2}-{y1})²] = √[{dx}² + {dy}²] = √{dx**2 + dy**2} = {dist}"
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': grid_svg(points=[(x1, y1, 'A'), (x2, y2, 'B')])
        })
    
    return qs


# Level 4: Midpoint Formula
def gen_level_4(n=50):
    """Ordinary: Find midpoint of line segment"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        # Use even differences for integer midpoints
        x1 = random.randint(-4, 2)
        x2 = x1 + random.choice([2, 4, 6])
        y1 = random.randint(-4, 2)
        y2 = y1 + random.choice([2, 4, 6])
        
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        
        txt = f"Find the midpoint of the line segment from A({x1}, {y1}) to B({x2}, {y2})."
        key = txt
        if key in used:
            continue
        used.add(key)
        
        ans = f"({mx}, {my})"
        wrongs = {f"({mx+1}, {my})", f"({mx}, {my+1})", f"({mx-1}, {my-1})", 
                 f"({(x1+x2)}, {(y1+y2)})", f"({my}, {mx})"}
        
        exp = f"M = (({x1}+{x2})/2, ({y1}+{y2})/2) = ({x1+x2}/2, {y1+y2}/2) = ({mx}, {my})"
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': grid_svg(points=[(x1, y1, 'A'), (x2, y2, 'B'), (mx, my, 'M')])
        })
    
    return qs


# Level 5: Slope/Gradient - Concept
def gen_level_5(n=50):
    """Ordinary: Understand slope concept - positive, negative, zero, undefined"""
    qs = []
    used = set()
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['identify', 'direction', 'compare', 'visual', 'steeper', 'sign'])
        
        if qtype == 'identify':
            slope_type = random.choice(['positive', 'negative', 'zero', 'undefined'])
            offset_x = random.randint(-1, 1)
            offset_y = random.randint(-1, 1)
            if slope_type == 'positive':
                x1, y1, x2, y2 = -2 + offset_x, -1 + offset_y, 2 + offset_x, 3 + offset_y
                ans = "Positive"
            elif slope_type == 'negative':
                x1, y1, x2, y2 = -2 + offset_x, 2 + offset_y, 2 + offset_x, -1 + offset_y
                ans = "Negative"
            elif slope_type == 'zero':
                y_val = random.randint(-2, 2)
                x1, y1, x2, y2 = -2, y_val, 2, y_val
                ans = "Zero"
            else:
                x_val = random.randint(-2, 2)
                x1, y1, x2, y2 = x_val, -2, x_val, 2
                ans = "Undefined"
            txt = f"What type of slope does the line through ({x1}, {y1}) and ({x2}, {y2}) have?"
            wrongs = {"Positive", "Negative", "Zero", "Undefined"}
            vis = grid_svg(lines=[(x1, y1, x2, y2, '#3b82f6')])
            exp = f"The line goes {'up' if slope_type == 'positive' else 'down' if slope_type == 'negative' else 'flat' if slope_type == 'zero' else 'straight up/down'} → {ans} slope"
            
        elif qtype == 'direction':
            direction = random.choice(['uphill', 'downhill', 'horizontal', 'vertical'])
            if direction == 'uphill':
                ans = "Positive"
                txt = "A line goes uphill from left to right. What is its slope type?"
            elif direction == 'downhill':
                ans = "Negative"
                txt = "A line goes downhill from left to right. What is its slope type?"
            elif direction == 'horizontal':
                ans = "Zero"
                txt = "A horizontal line has what type of slope?"
            else:
                ans = "Undefined"
                txt = "A vertical line has what type of slope?"
            wrongs = {"Positive", "Negative", "Zero", "Undefined"}
            vis = slope_visual_svg(2 if direction == 'uphill' else -2 if direction == 'downhill' else 0, 3)
            exp = f"{'Uphill = positive' if direction == 'uphill' else 'Downhill = negative' if direction == 'downhill' else 'Horizontal = zero' if direction == 'horizontal' else 'Vertical = undefined'}"
            
        elif qtype == 'compare':
            m1 = random.choice([1, 2, 3, 4, 5])
            m2 = random.choice([1, 2, 3, 4, 5])
            while m2 == m1:
                m2 = random.choice([1, 2, 3, 4, 5])
            txt = f"Line A has slope {m1}. Line B has slope {m2}. Which is steeper?"
            ans = "Line A" if m1 > m2 else "Line B"
            wrongs = {"Line A", "Line B", "Same steepness", "Cannot tell"}
            vis = grid_svg()
            exp = f"Greater absolute slope = steeper. |{m1}| {'>' if m1 > m2 else '<'} |{m2}|, so {ans} is steeper"
            
        elif qtype == 'visual':
            rise = random.choice([1, 2, 3, 4])
            run = random.choice([1, 2, 3, 4])
            txt = f"From the diagram showing rise = {rise} and run = {run}, what is the slope?"
            if rise == run:
                ans = "1"
            else:
                from math import gcd
                g = gcd(rise, run)
                if run // g == 1:
                    ans = str(rise // g)
                else:
                    ans = f"{rise // g}/{run // g}"
            wrongs = {f"{run}/{rise}" if rise != run else "2", str(rise + run), str(rise - run) if rise > run else str(run - rise), "0"}
            vis = slope_visual_svg(rise, run)
            exp = f"Slope = rise/run = {rise}/{run}" + (f" = {ans}" if rise != run else " = 1")
            
        elif qtype == 'steeper':
            m1 = random.choice([-3, -2, 2, 3])
            m2 = random.choice([-1, 1])
            txt = f"Which slope is steeper: {m1} or {m2}?"
            ans = str(m1) if abs(m1) > abs(m2) else str(m2)
            wrongs = {str(m1), str(m2), "Same", "Cannot compare"}
            vis = grid_svg()
            exp = f"|{m1}| = {abs(m1)}, |{m2}| = {abs(m2)}. Greater absolute value = steeper → {ans}"
            
        else:  # sign
            m = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            if m > 0:
                ans = "Uphill (left to right)"
                txt = f"A line has slope {m}. How does it look?"
            else:
                ans = "Downhill (left to right)"
                txt = f"A line has slope {m}. How does it look?"
            wrongs = {"Uphill (left to right)", "Downhill (left to right)", "Horizontal", "Vertical"}
            vis = line_graph_svg(m, 0)
            exp = f"Positive slope → uphill. Negative slope → downhill. Slope {m} is {'positive' if m > 0 else 'negative'} → {ans}"
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 6: Slope/Gradient - Calculations
def gen_level_6(n=50):
    """Ordinary: Calculate slope using formula"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        # Generate points with nice slopes
        x1 = random.randint(-3, 2)
        y1 = random.randint(-3, 2)
        
        # Ensure nice fraction or integer slope
        run = random.choice([1, 2, 3, 4])
        rise = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        
        x2 = x1 + run
        y2 = y1 + rise
        
        # Simplify fraction
        from math import gcd
        g = gcd(abs(rise), abs(run))
        num, den = rise // g, run // g
        
        if den == 1:
            ans = str(num)
        else:
            ans = f"{num}/{den}"
        
        txt = f"Find the slope of the line through A({x1}, {y1}) and B({x2}, {y2})."
        key = txt
        if key in used:
            continue
        used.add(key)
        
        wrongs = {f"{den}/{num}" if num != 0 else "0", f"{-num}/{den}" if den != 1 else str(-num),
                 f"{num+1}/{den}" if den != 1 else str(num+1), str(rise + run)}
        
        exp = f"m = (y₂-y₁)/(x₂-x₁) = ({y2}-{y1})/({x2}-{x1}) = {rise}/{run} = {ans}"
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': grid_svg(points=[(x1, y1, 'A'), (x2, y2, 'B')])
        })
    
    return qs


# Level 7: Equation of Line y = mx + c
def gen_level_7(n=50):
    """Higher: Understand y = mx + c form"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['identify_m', 'identify_c', 'write_eq', 'match'])
        
        m = random.choice([-3, -2, -1, 1, 2, 3])
        c = random.randint(-4, 4)
        
        if qtype == 'identify_m':
            if m == 1:
                eq = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                eq = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                eq = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            txt = f"What is the slope of the line {eq}?"
            ans = str(m)
            wrongs = {str(c), str(-m), str(m+1), str(abs(m))}
            exp = f"In y = mx + c, m is the slope. Here m = {m}"
            vis = line_graph_svg(m, c)
            
        elif qtype == 'identify_c':
            if m == 1:
                eq = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                eq = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                eq = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            txt = f"What is the y-intercept of the line {eq}?"
            ans = str(c)
            wrongs = {str(m), str(-c), str(c+1), "0"}
            exp = f"In y = mx + c, c is the y-intercept. Here c = {c}"
            vis = line_graph_svg(m, c)
            
        elif qtype == 'write_eq':
            txt = f"A line has slope {m} and y-intercept {c}. What is its equation?"
            if m == 1:
                ans = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                ans = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                ans = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            wrongs = {f"y = {c}x + {m}", f"y = {-m}x + {c}", f"y = {m}x + {-c}", f"y = x + {m+c}"}
            exp = f"y = mx + c with m = {m} and c = {c} gives {ans}"
            vis = line_graph_svg(m, c)
            
        else:  # match
            txt = f"Which line passes through (0, {c}) with slope {m}?"
            if m == 1:
                ans = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                ans = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                ans = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            wrongs = {f"y = {c}x + {m}", f"y = {m+1}x + {c}", f"y = {m}x + {c+1}", f"y = {-m}x + {c}"}
            exp = f"Point (0, {c}) means y-intercept = {c}. With slope {m}: {ans}"
            vis = line_graph_svg(m, c)
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 8: Finding Slope and Y-Intercept from Equation
def gen_level_8(n=50):
    """Higher: Convert to y = mx + c form"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['rearrange', 'from_ax_by', 'find_both'])
        
        m = random.choice([-3, -2, -1, 1, 2, 3])
        c = random.randint(-4, 4)
        
        if qtype == 'rearrange':
            # Given ax + by = c form
            a = random.choice([1, 2, 3])
            b = random.choice([1, 2])
            const = random.randint(2, 8)
            # ax + by = const → y = (-a/b)x + const/b
            slope = Fraction(-a, b)
            y_int = Fraction(const, b)
            
            txt = f"Rearrange {a}x + {b}y = {const} into y = mx + c form. What is m?"
            ans = str(slope)
            wrongs = {str(-slope), str(Fraction(a, b)), str(Fraction(b, a)), str(a)}
            exp = f"{b}y = -{a}x + {const} → y = {slope}x + {y_int}. So m = {slope}"
            vis = grid_svg()
            
        elif qtype == 'from_ax_by':
            a = random.choice([2, 3, 4])
            b = random.choice([1, 2])
            const = random.randint(-6, 6)
            while const == 0:
                const = random.randint(-6, 6)
            
            # ax - by = const → y = (a/b)x - const/b
            slope = Fraction(a, b)
            y_int = Fraction(-const, b)
            
            txt = f"For the line {a}x - {b}y = {const}, find the y-intercept."
            ans = str(y_int)
            wrongs = {str(-y_int), str(const), str(Fraction(const, b)), str(slope)}
            exp = f"-{b}y = -{a}x + {const} → y = {slope}x + {y_int}. Y-intercept = {y_int}"
            vis = grid_svg()
            
        else:  # find_both
            a = random.choice([1, 2])
            b = 1
            const = random.randint(1, 5)
            
            txt = f"For y + {a}x = {const}, what are (slope, y-intercept)?"
            ans = f"({-a}, {const})"
            wrongs = {f"({a}, {const})", f"({-a}, {-const})", f"({const}, {-a})", f"({a}, {-const})"}
            exp = f"y = -{a}x + {const}. Slope = {-a}, y-intercept = {const}"
            vis = line_graph_svg(-a, const)
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 9: Parallel & Perpendicular Lines
def gen_level_9(n=50):
    """Higher: Parallel and perpendicular line relationships"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['parallel_slope', 'perp_slope', 'identify_parallel', 'identify_perp'])
        
        if qtype == 'parallel_slope':
            m = random.choice([-3, -2, -1, 1, 2, 3, Fraction(1,2), Fraction(2,3), Fraction(-1,2)])
            c = random.randint(-3, 3)
            txt = f"Line L has equation y = {m}x + {c}. What is the slope of any line parallel to L?"
            ans = str(m)
            wrongs = {str(-m), str(Fraction(-1, m) if m != 0 else 0), str(m) + "1" if isinstance(m, Fraction) else str(int(m)+1), "0"}
            exp = f"Parallel lines have equal slopes. Slope of L = {m}, so parallel slope = {m}"
            vis = line_graph_svg(float(m), c)
            
        elif qtype == 'perp_slope':
            m = random.choice([1, 2, 3, -1, -2, -3, Fraction(1,2), Fraction(1,3)])
            perp_m = Fraction(-1, m)
            c = random.randint(-3, 3)
            txt = f"Line L has slope {m}. What is the slope of a line perpendicular to L?"
            ans = str(perp_m)
            wrongs = {str(m), str(-m), str(Fraction(1, m)), "0"}
            exp = f"Perpendicular slopes multiply to -1. If m₁ = {m}, then m₂ = -1/{m} = {perp_m}"
            vis = grid_svg()
            
        elif qtype == 'identify_parallel':
            m = random.choice([1, 2, -1, -2])
            c1 = random.randint(-3, 0)
            c2 = random.randint(1, 3)
            txt = f"Are y = {m}x + {c1} and y = {m}x + {c2} parallel, perpendicular, or neither?"
            ans = "Parallel"
            wrongs = {"Perpendicular", "Neither", "Same line"}
            exp = f"Both have slope {m}. Equal slopes → Parallel"
            vis = grid_svg()
            
        else:  # identify_perp
            m1 = random.choice([2, 3])
            m2 = Fraction(-1, m1)
            c = random.randint(-2, 2)
            txt = f"Are y = {m1}x + 1 and y = {m2}x + {c} parallel, perpendicular, or neither?"
            ans = "Perpendicular"
            wrongs = {"Parallel", "Neither", "Same line"}
            exp = f"Slopes: {m1} and {m2}. Product = {m1} × {m2} = -1 → Perpendicular"
            vis = grid_svg()
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 10: Equation from Two Points
def gen_level_10(n=50):
    """Mastery: Find equation given two points"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        # Generate points with nice slope
        x1 = random.randint(-2, 1)
        y1 = random.randint(-2, 2)
        
        run = random.choice([1, 2, 3])
        rise = random.choice([-3, -2, -1, 1, 2, 3])
        
        x2 = x1 + run
        y2 = y1 + rise
        
        # Calculate slope
        from math import gcd
        g = gcd(abs(rise), abs(run))
        m_num, m_den = rise // g, run // g
        
        if m_den == 1:
            m = m_num
            m_str = str(m)
        else:
            m = Fraction(m_num, m_den)
            m_str = str(m)
        
        # Calculate y-intercept: c = y - mx
        # c = y1 - m * x1
        if m_den == 1:
            c = y1 - m * x1
        else:
            c = Fraction(y1 * m_den - m_num * x1, m_den)
        
        # Build equation string
        if m_den == 1:
            if m == 1:
                eq = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                eq = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                eq = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
        else:
            eq = f"y = {m}x + {c}" if float(c) >= 0 else f"y = {m}x - {abs(c)}"
        
        txt = f"Find the equation of the line through ({x1}, {y1}) and ({x2}, {y2})."
        ans = eq
        key = txt
        if key in used:
            continue
        used.add(key)
        
        # Generate wrong answers
        wrong_m = -m if isinstance(m, int) else Fraction(-m.numerator, m.denominator)
        wrong_c = -c if isinstance(c, int) else -c
        wrongs = {
            f"y = {wrong_m}x + {c}",
            f"y = {m}x + {wrong_c}",
            f"y = {c}x + {m}" if isinstance(m, int) and isinstance(c, int) else f"y = x + {c}",
            f"y = {m_str}x" if c == 0 else f"y = {m}x + {c+1}"
        }
        
        exp = f"m = ({y2}-{y1})/({x2}-{x1}) = {rise}/{run} = {m_str}. Using y = mx + c with point ({x1},{y1}): {y1} = {m_str}×{x1} + c → c = {c}. Equation: {eq}"
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': grid_svg(points=[(x1, y1, 'A'), (x2, y2, 'B')])
        })
    
    return qs


# Level 11: Equation from Point and Slope
def gen_level_11(n=50):
    """Mastery: Find equation given point and slope"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['basic', 'parallel', 'perpendicular'])
        
        x1 = random.randint(-3, 3)
        y1 = random.randint(-3, 3)
        
        if qtype == 'basic':
            m = random.choice([-3, -2, -1, 1, 2, 3])
            c = y1 - m * x1
            
            if m == 1:
                eq = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            elif m == -1:
                eq = f"y = -x + {c}" if c >= 0 else f"y = -x - {abs(c)}"
            else:
                eq = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            
            txt = f"Find the equation of the line through ({x1}, {y1}) with slope {m}."
            exp = f"Using y - y₁ = m(x - x₁): y - {y1} = {m}(x - {x1}) → {eq}"
            
        elif qtype == 'parallel':
            m_given = random.choice([1, 2, -1, -2])
            c_given = random.randint(-2, 2)
            m = m_given  # Parallel = same slope
            c = y1 - m * x1
            
            if m == 1:
                eq = f"y = x + {c}" if c >= 0 else f"y = x - {abs(c)}"
            else:
                eq = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}"
            
            txt = f"Find the equation of the line through ({x1}, {y1}) parallel to y = {m_given}x + {c_given}."
            exp = f"Parallel → same slope = {m}. Through ({x1}, {y1}): c = {y1} - {m}×{x1} = {c}. Equation: {eq}"
            
        else:  # perpendicular
            m_given = random.choice([1, 2, -1, -2])
            c_given = random.randint(-2, 2)
            m = Fraction(-1, m_given)  # Perpendicular slope
            c = Fraction(y1, 1) - m * x1
            
            eq = f"y = {m}x + {c}" if float(c) >= 0 else f"y = {m}x - {abs(c)}"
            
            txt = f"Find the equation of the line through ({x1}, {y1}) perpendicular to y = {m_given}x + {c_given}."
            exp = f"Perpendicular → slope = -1/{m_given} = {m}. Through ({x1}, {y1}): {eq}"
        
        ans = eq
        key = txt
        if key in used:
            continue
        used.add(key)
        
        wrongs = {
            f"y = {-m}x + {c}" if isinstance(m, int) else f"y = {-m}x + {c}",
            f"y = {m}x + {-c}" if isinstance(c, int) else f"y = {m}x - {c}",
            f"y = {m}x",
            f"y = {c}x + {m}" if isinstance(m, int) and isinstance(c, int) else f"y = x + {c}"
        }
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': grid_svg(points=[(x1, y1, 'P')])
        })
    
    return qs


# Level 12: Problem Solving & Applications
def gen_level_12(n=50):
    """Mastery: Real-world applications and multi-step problems"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['collinear', 'triangle', 'rectangle', 'x_intercept', 'intersection'])
        
        if qtype == 'collinear':
            # Check if three points are collinear
            x1, y1 = random.randint(-2, 0), random.randint(-2, 0)
            m = random.choice([1, 2, -1, -2, Fraction(1, 2)])
            run = random.choice([2, 3, 4])
            x2 = x1 + run
            y2 = y1 + int(m * run) if isinstance(m, int) else y1 + m * run
            
            # Third point - either collinear or not
            is_collinear = random.choice([True, False])
            if is_collinear:
                x3 = x2 + run
                y3 = y2 + int(m * run) if isinstance(m, int) else y2 + m * run
                ans = "Yes"
            else:
                x3 = x2 + run
                y3 = y2 + int(m * run) + random.choice([1, -1])
                ans = "No"
            
            txt = f"Are the points A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}) collinear?"
            wrongs = {"Yes", "No", "Cannot determine", "Only A and B"}
            exp = f"Check if slope AB = slope BC. {'They are equal' if is_collinear else 'They are different'} → {ans}"
            vis = grid_svg(points=[(x1, y1, 'A'), (x2, y2, 'B'), (x3, y3, 'C')])
            
        elif qtype == 'triangle':
            # Area or perimeter of triangle
            vertices = [(0, 0), (4, 0), (0, 3)]
            area = 6  # 1/2 × 4 × 3
            txt = f"Find the area of triangle with vertices A(0, 0), B(4, 0), C(0, 3)."
            ans = "6"
            wrongs = {"12", "7", "10", "3.5"}
            exp = "Base = 4, Height = 3. Area = ½ × 4 × 3 = 6 square units"
            vis = grid_svg(points=[(0, 0, 'A'), (4, 0, 'B'), (0, 3, 'C')])
            
        elif qtype == 'rectangle':
            # Check if points form rectangle
            txt = "Points A(0, 0), B(4, 0), C(4, 3), D(0, 3) form which shape?"
            ans = "Rectangle"
            wrongs = {"Square", "Parallelogram", "Trapezium", "Rhombus"}
            exp = "AB = CD = 4, BC = AD = 3. All angles 90°. Sides unequal → Rectangle"
            vis = grid_svg(points=[(0, 0, 'A'), (4, 0, 'B'), (4, 3, 'C'), (0, 3, 'D')])
            
        elif qtype == 'x_intercept':
            m = random.choice([1, 2, -1, -2])
            c = random.choice([2, 4, -2, -4])
            x_int = -c // m
            txt = f"Find the x-intercept of y = {m}x + {c}."
            ans = f"({x_int}, 0)"
            wrongs = {f"(0, {c})", f"({-x_int}, 0)", f"({c}, 0)", f"(0, {x_int})"}
            exp = f"At x-intercept, y = 0. 0 = {m}x + {c} → x = {x_int}. Point: ({x_int}, 0)"
            vis = line_graph_svg(m, c)
            
        else:  # intersection
            # Two lines intersecting
            m1 = 1
            c1 = random.randint(-2, 2)
            m2 = -1
            c2 = random.randint(-2, 2)
            # Solve: m1*x + c1 = m2*x + c2
            # (m1 - m2)x = c2 - c1
            x_int = (c2 - c1) // (m1 - m2)
            y_int = m1 * x_int + c1
            
            txt = f"Find where y = x + {c1} and y = -x + {c2} intersect."
            ans = f"({x_int}, {y_int})"
            wrongs = {f"({y_int}, {x_int})", f"({-x_int}, {y_int})", f"({x_int}, {-y_int})", f"(0, {c1})"}
            exp = f"x + {c1} = -x + {c2} → 2x = {c2 - c1} → x = {x_int}, y = {y_int}"
            vis = grid_svg()
        
        key = (txt, ans)
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Main generator
def generate_all():
    """Generate all 600 questions"""
    all_questions = []
    generators = [
        (1, gen_level_1), (2, gen_level_2), (3, gen_level_3), (4, gen_level_4),
        (5, gen_level_5), (6, gen_level_6), (7, gen_level_7), (8, gen_level_8),
        (9, gen_level_9), (10, gen_level_10), (11, gen_level_11), (12, gen_level_12)
    ]
    
    for level, gen in generators:
        print(f"Generating Level {level}...")
        qs = gen(QUESTIONS_PER_LEVEL)
        for q in qs:
            q['level'] = level
            q['topic'] = TOPIC
            q['mode'] = MODE
        all_questions.extend(qs)
    
    return all_questions


def validate(questions):
    """Validate generated questions"""
    errors = []
    level_counts = {i: 0 for i in range(1, 13)}
    visual_counts = {i: 0 for i in range(1, 13)}
    
    for q in questions:
        level = q['level']
        level_counts[level] += 1
        
        # Check required fields
        required = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 
                   'correct_idx', 'explanation', 'level', 'topic', 'mode']
        for field in required:
            if field not in q or q[field] is None:
                errors.append(f"L{level}: Missing {field}")
        
        # Check 4 unique options
        opts = [q.get('option_a'), q.get('option_b'), q.get('option_c'), q.get('option_d')]
        if len(set(opts)) != 4:
            errors.append(f"L{level}: Non-unique options: {opts}")
        
        # Check visual
        if q.get('image_svg'):
            visual_counts[level] += 1
    
    return errors, level_counts, visual_counts


def print_summary(errors, level_counts, visual_counts):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    all_pass = True
    for level in range(1, 13):
        count = level_counts[level]
        vis_pct = (visual_counts[level] / count * 100) if count > 0 else 0
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        if count < QUESTIONS_PER_LEVEL:
            all_pass = False
        bar = "█" * (count // 2) + " " * (25 - count // 2)
        print(f"Level {level:2}: [{bar}] {count}/{QUESTIONS_PER_LEVEL} | Vis: {vis_pct:.0f}% | {status}")
    
    print("=" * 60)
    print(f"Total Errors: {len(errors)}")
    if errors[:10]:
        for e in errors[:10]:
            print(f"  - {e}")
    
    return all_pass


def test_single_insert():
    """Test database insert with single question"""
    print("\n=== Testing Single Insert ===")
    qs = gen_level_1(1)
    if qs:
        q = qs[0]
        print(f"Question: {q['question_text'][:50]}...")
        print(f"Options: A={q['option_a']}, B={q['option_b']}, C={q['option_c']}, D={q['option_d']}")
        print(f"Correct: {['A','B','C','D'][q['correct_idx']]}")
        print(f"Has SVG: {'Yes' if q.get('image_svg') else 'No'}")
        return True
    return False


def get_difficulty_band(level):
    """Map level to difficulty band"""
    if level <= 3:
        return 'Foundation'
    elif level <= 6:
        return 'Ordinary'
    elif level <= 9:
        return 'Higher'
    else:
        return 'Mastery'


def insert_to_db(questions):
    """Insert questions to database"""
    import sqlite3
    import os
    
    db_paths = [
        'instance/mathquiz.db',
        '../instance/mathquiz.db',
        '/home/bbsisk/mathappR12/instance/mathquiz.db'
    ]
    
    db_path = None
    for path in db_paths:
        if os.path.exists(path):
            db_path = path
            break
    
    if not db_path:
        print("Database not found. Please run from app directory.")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Delete existing
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (TOPIC,))
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions")
    conn.commit()
    
    # Insert new
    inserted = 0
    errors = 0
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text, option_a, option_b, option_c, option_d,
                 correct_answer, explanation, mode, image_svg)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'],
                q['level'],
                get_difficulty_band(q['level']),
                q['question_text'],
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_idx'],
                q['explanation'],
                q['mode'],
                q.get('image_svg', '')
            ))
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"Insert error: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"Inserted {inserted} questions, {errors} errors")
    return errors == 0


if __name__ == "__main__":
    print("=" * 60)
    print("AgentMath - Coordinate Geometry Generator v1")
    print("=" * 60)
    
    qs = generate_all()
    errors, level_counts, visual_counts = validate(qs)
    all_pass = print_summary(errors, level_counts, visual_counts)
    
    print("\n" + "=" * 60)
    response = input("Insert? (y/n): ").strip().lower()
    if response == 'y':
        if insert_to_db(qs):
            print("✓ Successfully inserted all questions!")
        else:
            print("✗ Some errors occurred during insertion")
    else:
        print("Cancelled.")
